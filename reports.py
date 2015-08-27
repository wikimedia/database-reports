import mwclient
import MySQLdb
import datetime
from displayTable import *

class Reports:

	def __init__( self, site, db ):
		self.db = db
		self.site = site

	def forgotten_articles( self ):
		cur = self.db.cursor()
		query = "SELECT p.page_title, r.rev_timestamp, p.page_touched, p.page_namespace, p.page_is_redirect FROM page p "
		query = query + "LEFT JOIN revision r ON p.page_latest = r.rev_id "
		query = query + "WHERE page_is_redirect = 0 AND page_namespace = 0 ORDER BY page_touched LIMIT 500"
		cur.execute( query )
		page = self.site.Pages['Forgotten articles']
		content = []
		content.append( ['Title', 'Last touched'] )
		for row in cur.fetchall() :
			content.append( [ '[[' + row[0] + ']]', datetime.datetime.strptime( row[1],'%Y%m%d%H%M%S') ] )
		text = generate_wikitext( content )
		page.save( text, summary = 'bot test edit' )

	def page_count_by_namespace( self ):
		cur = self.db.cursor()
		page = self.site.Pages['Page count by namespace']
		query = "SELECT COUNT(*) AS total, SUM(page_is_redirect) AS redirect, page_namespace FROM page GROUP BY page_namespace"
		cur.execute( query )
		page = self.site.Pages['Page count by namespace']
		content = []
		content.append( ['Namespace', 'Total', 'Redirects', 'Non-redirects'] )
		for row in cur.fetchall():
			content.append( [ row[2], row[0], row[1], row[0]-row[1] ])
		text = generate_wikitext( content )
		page.save( text, summary = 'bot test edit' )
