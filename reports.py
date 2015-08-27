import mwclient
import MySQLdb
from displayTable import *

class Reports:
	def forgotten_articles( self, site, db ):
		cur = db.cursor()
		query = "SELECT p.page_title, p.page_touched, p.page_namespace, p.page_is_redirect FROM page p WHERE page_is_redirect = 0 AND page_namespace = 0 ORDER BY page_touched LIMIT 5"
		cur.execute( query )
		page = site.Pages['DBR test']
		content = []
		content.append( ['Title', 'Last touched'] )
		for row in cur.fetchall() :
			content.append( [row[0], datetime.datetime.strptime( row[1],'%Y%m%d%H%M%S')] )
		text = generate_wikitext( content )
		page.save( text, summary = 'bot test edit' )