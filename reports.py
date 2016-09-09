import mwclient
import MySQLdb
from i18n import i18n
import datetime
from displayTable import *
import re

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
		query = """SELECT SQL_SMALL_RESULT
					MAX(rev_timestamp) AS lastedit, COUNT(rev_id) AS editcount, page_title
					FROM revision,
					# This inner query returns the 500 pages with the earliest timestamps on their latest revisions
					( SELECT rev_timestamp as lastedit,page_id,page_title
						FROM page, revision
						WHERE page_id IN
						# This query returns the list of regular articles created earlier than page_id X
						( SELECT page_id
							FROM page
							WHERE page_namespace = 0
							AND page_is_redirect = 0
							AND NOT EXISTS ( SELECT 1 FROM page_props WHERE pp_page=page_id AND pp_propname = 'disambiguation' )
							AND page_id < 21000000
							# Big hackerish heuristic cheat here! Ignore all pages newer than page_id X.
							# Currently set to ignore articles created after Dec 2008
							# If less than 500 results appear in the final output, this needs to be re-baselined
						)
						AND rev_id=page_latest
						ORDER BY lastedit ASC
						LIMIT 500
					) as InnerQuery
				WHERE rev_page=page_id
				GROUP BY page_id
				ORDER BY lastedit ASC"""
		cur.execute( query )

		# Extract the data into a Python nested list
		content = []
		content.append( ['forgotten-articles-title', 'forgotten-articles-last-edited', 'forgotten-articles-editcount'] )
		for row in cur.fetchall() :
			# A page name is being caught by the testwiki abuse filter - the following lets this run:
			if re.search('abuse_filter',row[2],re.IGNORECASE):
				continue
			content.append( [ self.linkify( row[2] ), datetime.datetime.strptime( row[0],'%Y%m%d%H%M%S'), row[1] ] )

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

		# Format the data as wikitext
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
		# Format the data as wikitext
		text = display_report( self.wiki, content , 'pagerevisions-desc' )
		self.publish_report( 'pagerevisions-page-title', text )

	# Editors eligible for autopatrol privileges
	# Identify users who meet the criteria for being granted "autopatrolled" on the English Wikipedia but who don't already have it.
	# Author: Andrew Crawford (thparkth) <acrawford@laetabilis.com>
	def autopatrol_eligibles( self ):
		cur = self.db.cursor()
		query = """ SELECT
				# "editor" consisting of user_name, wrapped in HTML tags linking to the sigma "created" tool
				CONCAT (
					'[[User:',user_name,'|',user_name,']]'
				 ) AS editor,
				CONCAT (
					'[https://tools.wmflabs.org/sigma/created.py?name=',
					REPLACE(user_name," ","%20"),
					'&server=enwiki&max=100&startdate=&ns=,,&redirects=none&deleted=undeleted (list)]'
				 ) AS listlink,
				# derived column "created count" returned by this subquery
				( SELECT count(*)
					FROM revision_userindex
					LEFT JOIN page ON page_id = rev_page
					WHERE page_namespace = 0 AND rev_parent_id = 0 AND rev_user_text = user_name AND rev_deleted = 0 AND page_is_redirect = 0
				) AS created_count
				FROM
				( # This query returns users who have created pages in the last 30 days and who are not already members of autoreviewed
					SELECT DISTINCT user_name
					FROM recentchanges
					LEFT JOIN user
					ON rc_user = user_id
					LEFT JOIN page
					ON rc_cur_id=page_id
					WHERE
							# User created a page within the last thirty days
							rc_timestamp > date_format(date_sub(NOW(),INTERVAL 30 DAY),'%Y%m%d%H%i%S') AND
							# It was an article
							rc_namespace = 0 AND
							# The user was human
							rc_bot = 0 AND
							# It was a new page
							rc_new = 1 AND
							# It's not a redirect
							page_is_redirect = 0 AND
							# User doesn't already have autoreviewer
							NOT EXISTS
							( SELECT 1 FROM user_groups WHERE ug_user=user_id AND ( ug_group='autoreviewer' OR ug_group='sysop' )
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
		# Format the data as wikitext
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

		# Format the data as wikitext
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

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'ufr-desc' )
		self.publish_report( 'ufr-page-title', text )


	def oldest_active( self ):
		cur = self.db.cursor()
		query = """SELECT SQL_SMALL_RESULT
					CONCAT( '[[User:',user_name,'|',user_name,']]' ) AS user_name
					,user_registration
					,user_editcount
					FROM (
						SELECT user_name,user_registration,user_editcount
						FROM user
						WHERE user_name IN (
							SELECT DISTINCT rc_user_text
							FROM recentchanges
							WHERE rc_timestamp > date_format( date_sub(NOW(),INTERVAL 30 DAY),'%Y%m%d%H%i%S' )
							AND rc_user_text NOT REGEXP '^[0-9]{1,3}\\.[0-9]'
							AND rc_user_text NOT REGEXP '\\:.+\\:'
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

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'oldestactive-desc' )
		self.publish_report( 'oldestactive-page-title', text )

	def deleted_prods( self ):
		cur = self.db.cursor()
		query = """SELECT
					page_title,
					count(log_id) AS entries,
					min(log_timestamp) AS firstdel,
					max(log_timestamp) AS lastdel,
					group_concat(
						log_timestamp," - ",log_comment,"<br>"
						ORDER BY log_timestamp ASC
						SEPARATOR " "
					) as log
				FROM categorylinks,page,logging_logindex
				WHERE cl_from=page_id
				AND cl_to="All_articles_proposed_for_deletion"
				AND page_title=log_title
				AND log_type="delete"
				AND log_action="delete"
				AND log_namespace=0
				GROUP BY page_id
				LIMIT 500"""
		cur.execute( query )
		content = []
		content.append(
			['deletedprods-title',
			 'deletedprods-deletecount',
			 'deletedprods-firstdeltime',
			 'deletedprods-lastdeltime',
			 'deletedprods-delcomments'
			 ]
		)
		for row in cur.fetchall():
			logtext = row[4];
			logtext = re.sub("{","<nowiki>{</nowiki>",logtext)
			logtext = re.sub("}","<nowiki>}</nowiki>",logtext)
			content.append( [ self.linkify( row[0] ), row[1], datetime.datetime.strptime( row[2],'%Y%m%d%H%M%S'), datetime.datetime.strptime( row[3],'%Y%m%d%H%M%S'), logtext ] )

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'deletedprods-desc' )
		self.publish_report( 'deletedprods-page-title', text )

	def most_used_templates( self ):
		cur = self.db.cursor()
		query = """SELECT tl_title, COUNT(*)
					FROM templatelinks
					WHERE tl_namespace = 10
					GROUP BY tl_title
					ORDER BY COUNT(*) DESC
					LIMIT 3000"""
		cur.execute( query )
		content = []
		content.append( ['mostusedtemplate-title', 'mostusedtemplate-count'] )
		for row in cur.fetchall():
			content.append( [ self.linkify( row[0], 10 ), row[1] ] )

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'mostusedtemplate-desc' )
		self.publish_report( 'mostusedtemplate-page-title', text )

	def unused_templates( self ):
		cur = self.db.cursor()
		query = """SELECT page_title
					FROM page
					LEFT JOIN categorylinks
					ON page_id = cl_from
					AND cl_to = 'Wikipedia_substituted_templates'
					LEFT JOIN redirect
					ON rd_from = page_id
					LEFT JOIN templatelinks
					ON page_namespace = tl_namespace
					AND page_title = tl_title
					WHERE page_namespace = 10
					AND rd_from IS NULL
					AND tl_from IS NULL
					AND cl_from IS NULL
					LIMIT 2000"""
		cur.execute( query )
		content = []
		content.append( ['unusedtemplate-title'] )
		for row in cur.fetchall():
			content.append( [ self.linkify( row[0], 10 ) ] )

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'unusedtemplate-desc' )
		self.publish_report( 'unusedtemplate-page-title', text )

	def orphaned_talk( self ):
		cur = self.db.cursor()
		query = """SELECT page_namespace, page_id, page_title, page_is_redirect, page_len
					FROM page talkpage
					WHERE talkpage.page_title NOT LIKE '%/%'
					AND talkpage.page_namespace IN (1,11,15,101,119)
					AND NOT EXISTS (
						SELECT 1
						FROM page mainpage
						WHERE mainpage.page_namespace=talkpage.page_namespace-1
						AND mainpage.page_title=talkpage.page_title
					)
					AND NOT EXISTS (
						SELECT 1
						FROM templatelinks
						WHERE talkpage.page_id=tl_from
						AND tl_title='G8-exempt'
					)
					LIMIT 1000"""
		cur.execute( query )
		content = []
		content.append( ["orphantalk-count", "orphantalk-isredirect", "orphantalk-namespace", "orphantalk-itemtitle", "orphantalk-pagesize"] )
		namespace_translate={ 1:"Talk", 5:"Wikipedia_Talk", 11:"Template_Talk", 15:"Category_Talk", 101:"Portal_Talk", 119:"Draft_Talk" }
		count = 1

		for row in cur.fetchall():
			namespace = namespace_translate[row[0]]
			fulllink  = namespace+':' + row[2]
			pagesize  = round( row[4]/1024, 1 );
			if row[3] == 0:
				redirect_label = " "
			else:
				redirect_label = "'''Redirect'''"
			content.append(	[ count, redirect_label, namespace, '{{No redirect|'+fulllink+'|'+row[2]+'}}', str(pagesize) +' kB' ] )
			count = count + 1

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'orphantalk-desc' )
		self.publish_report( 'orphantalk-page-title', text )

	def most_edited_page_last_month( self ):
		# Make the query
		cur = self.db.cursor()
		query = """SELECT rc_title, count(*) as num_edits
					FROM recentchanges
					WHERE rc_namespace = 0
					GROUP BY 1 ORDER BY 2 DESC
					LIMIT 25;"""
		cur.execute( query )

		# Extract the data into a Python nested list
		content = []
		content.append( ['most_edited_page_last_month-title', 'most_edited_page_last_month-editcount'] )
		for row in cur.fetchall() :
			content.append( [ self.linkify( row[0] ), row[1] ] )

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'most_edited_page_last_month-desc' )
		self.publish_report( 'most_edited_page_last_month-page-title', text )

	# Longest articles (NS=0)
	def article_by_size( self ):
		cur = self.db.cursor()
		query = """SELECT
					page_namespace,
					page_title,
					page_len
					FROM page
					WHERE page_namespace = 0
					AND page_len > 175000
					AND page_title NOT LIKE "%/%"
					ORDER BY page_len DESC
					LIMIT 1000;"""
		cur.execute( query )
		content = []
		content.append( ['article_by_size-namespace', 'article_by_size-title', 'article_by_size-size'] )
		for row in cur.fetchall():
			content.append( [ row[0], self.linkify( row[1], row[0] ), row[2] ])

		# Format the data as wikitext
		text = display_report( self.wiki, content , 'article_by_size-desc' )
		self.publish_report( 'article_by_size-page-title', text )

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
		page.save( content, summary = dict_obj[ 'summary' ] , minor=True)


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

