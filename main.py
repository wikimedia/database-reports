import mwclient
import MySQLdb
from displayTable import *
from config import *
from reports import *

class Main:
	def __init__(self):
		self.db = MySQLdb.connect( host = credentials['host'], user = credentials['user'], passwd = credentials['pass'], db = credentials['db'] )
		self.site = mwclient.Site('test.wikipedia.org')
		site.login( cttbot['user'], cttbot['pass'] )
		self.rep = Reports( site, db, 'en' )


	def forgotten_articles(self):
		print 'Hi'
		# self.rep.forgotten_articles()