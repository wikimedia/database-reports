import mwclient
import MySQLdb
from config import *

# Test stuff
#site = mwclient.Site('en.wikipedia.org')
#page = site.Pages['Battle of Trenton']
#text = page.text()
#print 'Trenton thingy: ', text.encode('utf-8')

db = MySQLdb.connect( host = credentials['host'], user = credentials['user'], passwd = credentials['pass'], db = credentials['db'] )

cur = db.cursor()

cur.execute( "SELECT p.page_title, p.page_touched FROM page p ORDER BY p.page_touched DESC LIMIT 20" )

for row in cur.fetchall() :
    print row