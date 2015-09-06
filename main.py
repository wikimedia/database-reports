import mwclient
import MySQLdb
from displayTable import *
from config import *
from reports import *
import sys

def main (args):
	for arg in args[1:]:
		print arg
		run = Run()
		method = getattr(run, str(arg))
		if not method:
			raise Exception("Method not implemented")
		else:
			method()

class Run:
	def __init__(self):
		self.db = MySQLdb.connect( host = credentials['host'], user = credentials['user'], passwd = credentials['pass'], db = credentials['db'] )
		self.site = mwclient.Site('test.wikipedia.org')
		site.login( cttbot['user'], cttbot['pass'] )
		self.rep = Reports( site, db, 'en' )
		print 'initiated'

	def forgotten_articles(self):
		print 'okay'
		rep.forgotten_articles()

	def pagecountbynamespace(self):
		print 'Still okay'
		rep.page_count_by_namespace()

if __name__ == '__main__':
	main(sys.argv)
