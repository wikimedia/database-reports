import mwclient
import pymysql
import datetime
from .config import *
from reports import *
import sys
from displayTable import *

def forgotten_articles():

	db = pymysql.connect( host = 'enwiki.labsdb', user = credentials['user'], passwd = credentials['pass'], db = 'enwiki_p' )
	site = mwclient.Site( 'en.wikipedia.org' )
	site.login( cttbot['user'], cttbot['pass'] )
	print('initiated')

	# Make the query
	cur = db.cursor()
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
	text = display_report( 'en', content, 'forgotten-articles-desc' )

	page = site.Pages[ 'Wikipedia:Database reports/Forgotten_articles']
	page.save( content, summary = 'bot test edit' )

forgotten_articles()
