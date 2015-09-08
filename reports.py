import mwclient
import MySQLdb
import datetime
from displayTable import *


class Reports:
	def __init__( self, site, db, wiki ):
		self.db = db
		self.site = site
		self.wiki = wiki

	# Oldest edited articles
	def forgotten_articles( self ):
		# Make the query
		cur = self.db.cursor()
		query = """SELECT p.page_title, p.page_namespace, p.page_is_redirect, p.page_touched, r.editcount FROM page p
				   LEFT JOIN ( SELECT COUNT(*) AS editcount, rev_page FROM revision GROUP BY rev_page ) r ON r.rev_page = p.page_id
				   WHERE page_is_redirect = 0 AND page_namespace = 0 
				   ORDER BY page_touched 
				   LIMIT 500"""
		cur.execute( query )

		# Extract the data into a Python nested list
		content = []
		content.append( ['forgotten-articles-title', 'forgotten-articles-last-edited', 'forgotten-articles-editcount'] )
		for row in cur.fetchall() :
			content.append( [ '[[' + row[0] + ']]', datetime.datetime.strptime( row[3],'%Y%m%d%H%M%S'), row[4] ] )

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'forgotten-articles-desc' )
		self.publish_report( 'Forgotten articles', text )


	# Page count by namespace
	def page_count_by_namespace( self ):
		cur = self.db.cursor()
		query = """SELECT page_namespace, COUNT(*) AS total, SUM(page_is_redirect) AS redirect FROM page
				   GROUP BY page_namespace"""
		cur.execute( query )

		content = []
		content.append( ['pagecount-namespace', 'pagecount-namespace-name', 'pagecount-total', 'pagecount-redirect', 'pagecount-non-redirect'] )
		for row in cur.fetchall():
			content.append( [ row[0], '{{subst:ns:' + row[0] + '}}', row[1], row[2], row[1]-row[2] ])

		text = display_report( self.wiki, content , 'pagecount-desc' )
		self.publish_report( 'Page count by namespace', text )


	# Pages with most revisions
	def pages_with_most_revisions( self ):
		cur = self.db.cursor()
		query = """SELECT COUNT(*) AS revisions, rev_page, p.page_namespace, p.page_title FROM revision r
				   LEFT JOIN ( SELECT page_id, page_title, page_namespace FROM page ) p ON r.rev_page = p.page_id
				   GROUP BY rev_page
				   ORDER BY revisions DESC
				   LIMIT 20"""
		cur.execute( query )

		content = []
		content.append( ['pagerevisions-namespace', 'pagerevisions-title', 'pagerevisions-revisions'] )
		for row in cur.fetchall():
			content.append( [ row[2], '[[' + str( row[3] ) + ']]', row[0] ])

		text = display_report( self.wiki, content , 'pagerevisions-desc' )
		self.publish_report( 'Pages with most revisions', text )


	# Blank pages with a single author
	def blank_pages( self ):
		cur = self.db.cursor()
		query = """SELECT p.page_title, p.page_len, p.page_latest, p.page_namespace, r.authors FROM page p
				   LEFT JOIN ( SELECT rev_page, COUNT(DISTINCT rev_user_text) AS authors FROM revision
				   GROUP BY rev_page ) r ON r.rev_page = p.page_latest
				   WHERE p.page_len = 0
				   HAVING r.authors = 1"""
		cur.execute( query )

		content = []
		content.append( ['blankpages-title'] )
		for row in cur.fetchall():
			if row[3] != 6 and row[3] != 7:
				content.append( [ '[[{{subst:ns:' + str( row[3] ) + '}}:' + row[0] + ']]' ] )

		text = display_report( self.wiki, content , 'blankpages-desc' )
		self.publish_report( 'Blank pages', text )


	''' Publish report on page with given title, with the given content
		@param title Page title
		@param content Content to be displayed on page
	'''
	def publish_report( self, title, content ):
		page = self.site.Pages[ 'Wikipedia:Database reports/' + str( title ) ]
		page.save( content, summary = 'bot test edit' )





