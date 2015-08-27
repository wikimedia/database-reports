import mwclient
import MySQLdb
from displayTable import *
import datetime
from config import *

db = MySQLdb.connect( host = credentials['host'], user = credentials['user'], passwd = credentials['pass'], db = credentials['db'] )

cur = db.cursor()

query = "SELECT p.page_title, p.page_touched, p.page_namespace, p.page_is_redirect FROM page p WHERE page_is_redirect = 0 AND page_namespace = 0 ORDER BY page_touched LIMIT 5"

cur.execute( query )

site = mwclient.Site('test.wikipedia.org')
site.login( testbot['user'], testbot['pass'] )
page = site.Pages['DBR test']

content = []
content.append( ['Title', 'Last touched'] )

for row in cur.fetchall() :
	content.append( row[0], datetime.datetime.strptime( row[1],'%Y%m%d%H%M%S') )

newtext = generate_wikitext( content )

page.save( newtext, summary = 'bot test edit' )