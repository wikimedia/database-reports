import mwclient
import MySQLdb
from displayTable import *
from config import *
from reports import *

def main():
	# Connect to database
	db = MySQLdb.connect( host = credentials['host'], user = credentials['user'], passwd = credentials['pass'], db = credentials['db'] )
	
	# Logging the bot in
	site = mwclient.Site('test.wikipedia.org')
	site.login( testbot['user'], testbot['pass'] )

	# Calling Forgotten Articles
	rep = Reports( site, db, 'en' )
	rep.forgotten_articles()
	rep.page_count_by_namespace()
	rep.pages_with_most_revisions()

main()
