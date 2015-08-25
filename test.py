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

cur.execute( "SELECT * FROM user WHERE user_editcount > 10000 LIMIT 5" )

for row in cur.fetchall() :
    print row