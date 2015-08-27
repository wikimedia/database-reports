import mwclient
import MySQLdb
import datetime
from displayTable import *
from config import *

# Test stuff
# site = mwclient.Site('en.wikipedia.org')
# page = site.Pages['Battle of Trenton']
# text = page.text()
# print 'Trenton thingy: ', text.encode('utf-8')

arr = [['Hello', 'Title'],['a', 'b'],['c','d'],['e','f']]
print generate_wikitext( arr )
