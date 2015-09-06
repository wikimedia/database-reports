import mwclient
import MySQLdb
from displayTable import *
from config import *
from reports import *
import sys

def main (args):
	wiki = args[1]
	for arg in args[2:]:
		print arg
		run = Run( wiki )
		method = getattr(run, str(arg) )
		if not method:
			raise Exception("Method not implemented")
		else:
			method()

class Run:
	def __init__( self, wiki ):
		self.db = MySQLdb.connect( host = wiki + 'wiki.labsdb', user = credentials['user'], passwd = credentials['pass'], db = wiki + 'wiki_p' )
		self.site = mwclient.Site( wiki + '.wikipedia.org' )
		self.site.login( cttbot['user'], cttbot['pass'] )
		self.rep = Reports( self.site, self.db, 'en' )
		print 'initiated'

	def forgotten_articles(self):
		print 'okay'
		self.rep.forgotten_articles()

	def pagecountbynamespace(self):
		print 'Still okay'
		self.rep.page_count_by_namespace()

if __name__ == '__main__':
	main(sys.argv)
