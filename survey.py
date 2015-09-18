import MySQLdb
import random
from config import *

def main():

	wikis = ['ar', 'ru', 'en', 'fr', 'ja', 'de', 'commons', 'es', 'zh', 'pt']
	f1 = open( 'result.txt', 'w' )
	
	for wiki in wikis:
		db = MySQLdb.connect( host = wiki + 'wiki.labsdb', user = credentials['user'], passwd = credentials['pass'], db = wiki + 'wiki_p' )
		res = query( wiki, db )
		res = random.sample( res, 100 )
		f1.write( wiki + '\n' )
		for r in res:
			f1.write( r + '\n' )
		f1.write( '\n\n' )


def query( wiki, db ):
	if wiki == 'ru':
		namespaces = [ [0, 6, 102], [8, 10, 828], [4, 14, 100, 104] ]
	else:
		namespaces = [ [0, 6, 118], [8, 10, 828], [4, 14, 100, 102] ]
	cur = db.cursor()

	list1 = set()

	for n in namespaces:
		placeholders = ','.join( ['%s'] * len(n) )

		q = """SELECT rc_user, rc_user_text, SUM(CASE WHEN rc_namespace IN (%s) THEN 1 ELSE 0 END) AS hits
			   FROM recentchanges
			   WHERE rc_bot = 0
			   GROUP by rc_user
			   ORDER BY hits DESC
			   LIMIT 100;
			"""
		cur.execute( q % placeholders, tuple(n) )

		for row in cur.fetchall():
			list1.add( row[1] )

	print len(list1)
	return list1



main()




