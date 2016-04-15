import mwclient
import MySQLdb
from i18n import i18n
import datetime
from displayTable import *


class Reports:
	def __init__( self, site, db, wiki ):
		self.db = db
		self.site = site
		self.wiki = wiki

	# Oldest edited articles
	# Run time on enwiki 5 hours 23 minutes as of 8 Sept 2015
	def forgotten_articles( self ):
		# Make the query
		cur = self.db.cursor()
		query = """SELECT p.page_title, p.page_namespace, p.page_is_redirect, p.page_touched, r.editcount FROM page p
				   LEFT JOIN ( SELECT COUNT(*) AS editcount, rev_page FROM revision GROUP BY rev_page ) r ON r.rev_page = p.page_id
				   WHERE page_is_redirect = 0 AND page_namespace = 0
				   AND p.page_id NOT IN ( SELECT pp_page FROM page_props WHERE pp_propname = 'disambiguation' )
				   ORDER BY page_touched
				   LIMIT 500"""
		cur.execute( query )

		# Extract the data into a Python nested list
		content = []
		content.append( ['forgotten-articles-title', 'forgotten-articles-last-edited', 'forgotten-articles-editcount'] )
		for row in cur.fetchall() :
			content.append( [ self.linkify( row[0] ), datetime.datetime.strptime( row[3],'%Y%m%d%H%M%S'), row[4] ] )

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'forgotten-articles-desc' )
		self.publish_report( 'forgotten-articles-page-title', text )


	# Page count by namespace
	# Run time on enwiki 4 hours 8 minutes as of 8 Sept 2015
	def page_count_by_namespace( self ):
		cur = self.db.cursor()
		query = """SELECT page_namespace, COUNT(*) AS total, SUM(page_is_redirect) AS redirect FROM page
				   GROUP BY page_namespace"""
		cur.execute( query )

		content = []
		content.append( ['pagecount-namespace', 'pagecount-namespace-name', 'pagecount-total', 'pagecount-redirect', 'pagecount-non-redirect'] )
		for row in cur.fetchall():
			content.append( [ row[0], '{{subst:ns:' + str( row[0] ) + '}}', row[1], row[2], row[1]-row[2] ])

		text = display_report( self.wiki, content , 'pagecount-desc' )
		self.publish_report( 'pagecount-page-title', text )


	# Pages with most revisions
	def pages_with_most_revisions( self ):
		cur = self.db.cursor()
		query = """SELECT COUNT(*) AS revisions, rev_page, p.page_namespace, p.page_title FROM revision r
				   LEFT JOIN ( SELECT page_id, page_title, page_namespace FROM page ) p ON r.rev_page = p.page_id
				   GROUP BY rev_page
				   ORDER BY revisions DESC
				   LIMIT 1000"""
		cur.execute( query )

		content = []
		content.append( ['pagerevisions-namespace', 'pagerevisions-title', 'pagerevisions-revisions'] )
		for row in cur.fetchall():
			content.append( [ row[2], self.linkify( row[3], row[2] ), row[0] ])

		text = display_report( self.wiki, content , 'pagerevisions-desc' )
		self.publish_report( 'pagerevisions-page-title', text )


	# Editors eligible for autopatrol privileges
	# Identify users who meet the criteria for being granted "autopatrolled" on the English Wikipedia but who don't already have it.
	# Author: Andrew Crawford (thparkth) <acrawford@laetabilis.com>
	def autopatrol_eligibles( self ):
		cur = self.db.cursor()
		query = """ SELECT
				/* "editor" consisting of user_name, wrapped in HTML tags linking to the sigma "created" tool */
				CONCAT (
                                        '[[User:',user_name,'|',user_name,']]'
				 ) AS editor,
				CONCAT (
                                        '[https://tools.wmflabs.org/sigma/created.py?name=',
					REPLACE(user_name,' ','_'),
					'&server=enwiki&max=100&startdate=&ns=,,&redirects=none&deleted=undeleted (list)]'
				 ) AS listlink,
				/* derived column "created count" returned by this subquery */
				(
					SELECT count(*)
					FROM revision_userindex
					LEFT JOIN page ON page_id = rev_page
					WHERE page_namespace = 0 AND rev_parent_id = 0 AND rev_user_text = user_name AND rev_deleted = 0 AND page_is_redirect = 0
				) AS created_count
				FROM
				(
					/* This query returns users who have created pages in the last 30 days and who are not already members of autoreviewed */
					SELECT DISTINCT user_name
					FROM recentchanges
					LEFT JOIN user
					ON rc_user = user_id
					LEFT JOIN page
					ON rc_cur_id=page_id
					WHERE
							/* User created a page within the last thirty days */
							rc_timestamp > date_format(date_sub(NOW(),INTERVAL 30 DAY),'%Y%m%d%H%i%S') AND
							/* It was an article */
							rc_namespace = 0 AND
							/* The user was human */
							rc_bot = 0 AND
							/* It was a new page */
							rc_new = 1 AND
							/* It's not a redirect */
							page_is_redirect = 0 AND
							/* User doesn't already have autoreviewer */
							NOT EXISTS
							(
								SELECT 1 FROM user_groups WHERE ug_user=user_id AND ( ug_group='autoreviewer' OR ug_group='sysop' )
							)
				) as InnerQuery
				HAVING created_count > 24
				ORDER BY created_count DESC
				LIMIT 500"""
		cur.execute( query )

		content = []
		content.append( ['autopatrol-username', 'autopatrol-listlink', 'autopatrol-articles'] )
		for row in cur.fetchall():
			if row[1] is None:
				continue
			content.append( [  row[0], row[1], row[2] ] )

		text = display_report( self.wiki, content , 'autopatrol-desc' )
		self.publish_report( 'autopatrol-page-title', text )


	def talk_pages_by_size( self ):
		cur = self.db.cursor()
		query = """SELECT page_namespace,
				   REPLACE( SUBSTRING_INDEX(page_title, '/', 1 ), '_', ' ' ) AS parent,
				   SUM( page_len ) / 1024 / 1024 AS total_size
				   FROM page
				   WHERE page_namespace MOD 2 = 1
				   GROUP BY page_namespace, parent
				   ORDER BY total_size DESC
				   LIMIT 300"""
		cur.execute( query )

		content = []
		content.append( ['tpbs-namespace', 'tpbs-page', 'tpbs-size'] )
		for row in cur.fetchall():
			content.append( [ row[0], self.linkify( row[1], row[0] ), row[2] ] )

		text = display_report( self.wiki, content, 'tpbs-desc' )
		self.publish_report( 'tpbs-page-title', text )


	def unused_file_redirects( self ):
		cur = self.db.cursor()
		query = """SELECT page_title,
				   (	SELECT COUNT(*)
						FROM imagelinks
						WHERE il_to = page_title
				   ) AS imagelinks,
				   (	SELECT COUNT(*)
						FROM pagelinks
						WHERE pl_namespace = 6
						AND pl_title = page_title
				   ) AS links
				   FROM page
				   WHERE page_namespace = 6
				   AND page_is_redirect = 1
				   HAVING imagelinks + links <= 1
				   """
		cur.execute( query )

		content = []
		content.append( ['ufr-page', 'ufr-imagelinks', 'ufr-links'] )
		for row in cur.fetchall():
			content.append( [ self.linkify( row[0], 6 ), row[1], row[2] ] )

		text = display_report( self.wiki, content, 'ufr-desc' )
		self.publish_report( 'ufr-page-title', text )


        def oldest_active( self ):
                cur = self.db.cursor()
                query = """SELECT SQL_SMALL_RESULT
                                CONCAT(
                                        '[[User:',user_name,'|',user_name,']]'
                                ) AS user_name
                                ,user_registration
                                ,user_editcount
                        FROM
                            (
                                SELECT  user_name,user_registration,user_editcount
                                FROM    user
                                WHERE   user_name IN
                                (
                                        SELECT DISTINCT rc_user_text
                                        FROM    recentchanges
                                        WHERE   rc_timestamp>date_format(date_sub(NOW(),INTERVAL 30 DAY),'%Y%m%d%H%i%S')
                                        AND     rc_user_text NOT REGEXP '^[0-9]{1,3}\\.[0-9]'
                                        AND     rc_user_text NOT REGEXP '\\:.+\\:'
                                )
                                AND user_registration IS NOT NULL
                                ORDER BY user_id
                                LIMIT 250
                          ) AS InnerQuery
                        ORDER BY user_registration
                        LIMIT 200"""
                cur.execute( query )

                content = []
                content.append( ['oldestactive-username', 'oldestactive-creationdate', 'oldestactive-editcount'] )
                for row in cur.fetchall():
                        content.append( [ row[0], row[1] , row[2] ] );

                text = display_report( self.wiki, content, 'oldestactive-desc' )
                self.publish_report( 'oldestactive-page-title', text )





	''' Publish report on page with given title, with the given content
		@param title Page title
		@param content Content to be displayed on page
	'''
	def publish_report( self, title, content ):
		dict_obj = i18n.lang_dicts[ str( self.wiki + 'dict') ]
		reports_base_url = dict_obj[ str( 'reports_base_url' ) ]
		report_title = dict_obj[ str( title ) ]
		print str( reports_base_url + report_title )
		page = self.site.Pages[ reports_base_url + report_title ]
		page.save( content, summary = 'Updating report' )


	def linkify( self, title, namespace = None ):
		title = str( title )
		title_clean = title.replace( '_', ' ' )
		if namespace is None:
			return '[[' + title_clean + ']]'
		elif namespace is 6:
			return '[[:{{subst:ns:%s}}:%s]]' % ( namespace, title_clean )
		else:
			return '[[{{subst:ns:%s}}:%s]]' % ( namespace, title_clean )


	def userify( self, name ):
		name = str( name )
		return '[[User:' + name + ' | ' + name + ']]'

