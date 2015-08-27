import mwclient
import MySQLdb
import datetime
from config import *

# Test stuff
# site = mwclient.Site('en.wikipedia.org')
# page = site.Pages['Battle of Trenton']
# text = page.text()
# print 'Trenton thingy: ', text.encode('utf-8')

db = MySQLdb.connect( host = credentials['host'], user = credentials['user'], passwd = credentials['pass'], db = credentials['db'] )

cur = db.cursor()

query = "SELECT p.page_title, p.page_touched, p.page_namespace, p.page_is_redirect FROM page p" +
	"WHERE page_is_redirect = 0 AND page_namespace = 0" +
	"ORDER BY page_touched LIMIT 500"

cur.execute( query )

site = mwclient.Site('test.wikipedia.org')
site.login( testbot['user'], testbot['pass'] )
page = site.Pages['DBR test']

newtext = '{| class="wikitable" \n |- \n !Title \n !Last touched \n'

for row in cur.fetchall() :
    newtext = newtext + '|- \n | [[' + row[0] + ']] \n | ' 
    newtext = newtext + datetime.datetime.fromtimestamp( int(row[1])/1000 ).strftime('%Y-%m-%d %H:%M:%S') + '\n'

page.save( newtext, summary = 'bot test edit 7' )