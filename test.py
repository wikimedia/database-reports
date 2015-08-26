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

cur.execute( "SELECT p.page_title, p.page_touched FROM page p ORDER BY p.page_touched DESC LIMIT 20" )

site = mwclient.Site('test.wikipedia.org')
site.login( testbot['user'], testbot['pass'] )
page = site.Pages['DBR test']
# text = page.text()

#print 'Page default text was: ', text

newtext = '{| class="wikitable" |- !Title !Last touched |- '

for row in cur.fetchall() :
    newtext = newtext + '| [[' + row[0] + ']] | ' + datetime.datetime.fromtimestamp( int(row[1])/1000 ).strftime('%Y-%m-%d') + '<br>'

page.save(newtext, summary = 'bot test edit 2')