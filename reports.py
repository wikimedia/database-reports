import mwclient
import MySQLdb
import datetime
from displayTable import *


class Reports:
	def __init__( self, site, db, wiki ):
		self.db = db
		self.site = site
		self.wiki = wiki

	def forgotten_articles( self ):
		# Make the query
		cur = self.db.cursor()
		query = """SELECT p.page_title, p.page_namespace, p.page_is_redirect, r.editcount FROM page p
				   LEFT JOIN ( SELECT COUNT(*) AS editcount FROM revision ) r ON r.rev_page = p.page_id
				   WHERE page_is_redirect = 0 AND page_namespace = 0 
				   ORDER BY page_touched 
				   LIMIT 500"""
		cur.execute( query )

		# Extract the data into a Python nested list
		content = []
		content.append( ['forgotten-articles-title', 'forgotten-articles-last-edited', 'forgotten-articles-editcount'] )
		for row in cur.fetchall() :
			content.append( [ '[[' + row[0] + ']]', datetime.datetime.strptime( row[1],'%Y%m%d%H%M%S'), row[3] ] )

		# Format the data as wikitext
		text = display_report( self.wiki, content, 'forgotten-articles-desc' )
		self.publish_report( 'Forgotten articles', text )

	def page_count_by_namespace( self ):
		cur = self.db.cursor()
		query = """SELECT page_namespace, COUNT(*) AS total, SUM(page_is_redirect) AS redirect FROM page
				   GROUP BY page_namespace"""
		cur.execute( query )

		content = []
		content.append( ['pagecount-namespace', 'pagecount-total', 'pagecount-redirect', 'pagecount-non-redirect'] )
		for row in cur.fetchall():
			content.append( [ row[0], row[1], row[2], row[1]-row[2] ])

		text = display_report( self.wiki, content , 'pagecount-desc' )
		self.publish_report( 'Page count by namespace', text )

	def publish_report( self, title, content ):
		page = self.site.Pages[ str( title ) ]
		page.save( content, summary = 'bot test edit' )





