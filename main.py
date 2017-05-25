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

	def new_wikiprojects( self ):
		self.rep.new_wikiprojects()

	def pagecountbynamespace( self ):
		self.rep.page_count_by_namespace()

	def pages_with_most_revisions( self ):
		self.rep.pages_with_most_revisions()

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

	def orphaned_talk( self ):
		self.rep.orphaned_talk()

	def unused_templates( self ):
		self.rep.unused_templates()

	def article_by_size( self ):
		self.rep.article_by_size()

	def most_edited_page_last_month( self ):
		self.rep.most_edited_page_last_month()

	def most_watched(self):
		self.rep.most_watched()

if __name__ == '__main__':
	main(sys.argv)
