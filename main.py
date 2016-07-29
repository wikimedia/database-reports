import mwclient
import MySQLdb
from displayTable import *
from config import *
from reports import *
import sys

def main ( args ):
	wiki = args[1]
	for arg in args[2:]:
		print arg
		run = Run( wiki )
		method = getattr( run, str( arg ) )
		if not method:
			raise Exception( "Method not implemented" )
		else:
			method()

class Run:
	def __init__( self, wiki ):
		self.db = MySQLdb.connect( host = wiki + 'wiki.labsdb', user = credentials['user'], passwd = credentials['pass'], db = wiki + 'wiki_p' )
		self.site = mwclient.Site( wiki + '.wikipedia.org' )
		self.site.login( cttbot['user'], cttbot['pass'] )
		self.rep = Reports( self.site, self.db, wiki )

	def forgotten_articles( self ):
		self.rep.forgotten_articles()

	def pagecountbynamespace( self ):
		self.rep.page_count_by_namespace()

	def pages_with_most_revisions( self ):
		self.rep.pages_with_most_revisions()

	def blank_pages( self ):
		self.rep.blank_pages()

	def autopatrol_eligibles( self ):
		self.rep.autopatrol_eligibles()

	def talk_pages_by_size( self ):
		self.rep.talk_pages_by_size()

	def unused_file_redirects( self ):
		self.rep.unused_file_redirects()

	def oldest_active( self ):
		self.rep.oldest_active()

	def deleted_prods( self ):
		self.rep.deleted_prods()

	def most_used_templates( self ):
		self.rep.most_used_templates()


if __name__ == '__main__':
	main(sys.argv)
