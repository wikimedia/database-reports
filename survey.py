import MySQLdb
from config import *

'''
Extra namespaces (ones we care about anyway):
'commonswiki' => array(
		100 => 'Creator',
		101 => 'Creator_talk',
		102 => 'TimedText', # For video subtitles -- BV 2009-11-08
		103 => 'TimedText_talk',
		104 => 'Sequence',
		105 => 'Sequence_talk',
		106 => 'Institution',
		107 => 'Institution_talk',
	),
'dewiki' => array(
		100 => 'Portal',
		101 => 'Portal_Diskussion'
	),
'enwiki' => array(
		100 => 'Portal',
		101 => 'Portal_talk',
		# 106 => 'Table',
		# 107 => 'Table_talk',
		108 => 'Book',
		109 => 'Book_talk',
		118 => 'Draft', // T59569
		119 => 'Draft_talk',
	),
'eswiki' => array(
		100 => 'Portal',
		101 => 'Portal_Discusión',
		102 => 'Wikiproyecto',
		103 => 'Wikiproyecto_Discusión',
		104 => 'Anexo', // T11304
		105 => 'Anexo_Discusión',
	),
'frwiki' => array(
		100 => 'Portail',
		101 => 'Discussion_Portail',
		102 => 'Projet',
		103 => 'Discussion_Projet',
		104 => 'Référence',
		105 => 'Discussion_Référence',
	),
'ruwiki' => array(
		100 => 'Портал',
		101 => 'Обсуждение_портала',
		102 => 'Инкубатор', // Incubator
		103 => 'Обсуждение_Инкубатора', // Incubator talk
		104 => 'Проект', // T36124 - Project
		105 => 'Обсуждение_проекта', // T36124 - Project talk
		106 => 'Арбитраж', // T36527 - Arbcom
		107 => 'Обсуждение_арбитража',
		),
'zhwiki' => array(
		100 => 'Portal',
		101 => 'Portal_talk',
		118 => 'Draft', // T91223
		119 => 'Draft_talk' // T91223
	),
'jawiki' => array(
		NS_TALK => "ノート",
		NS_USER_TALK => "利用者‐会話",
		NS_PROJECT_TALK => "Wikipedia‐ノート",
		NS_FILE_TALK => "ファイル‐ノート",
		NS_MEDIAWIKI_TALK => "MediaWiki‐ノート",
		NS_TEMPLATE => "Template",
		NS_TEMPLATE_TALK => "Template‐ノート",
		NS_HELP => "Help",
		NS_HELP_TALK => "Help‐ノート",
		NS_CATEGORY => "Category",
		NS_CATEGORY_TALK => "Category‐ノート",
		100 => 'Portal',
		101 => 'Portal‐ノート',
		102 => 'プロジェクト',
		103 => 'プロジェクト‐ノート',
		829 => 'モジュール‐ノート', // T49933
	),
'arwiki' => array(
		100 => 'بوابة',
		101 => 'نقاش_البوابة',
	),
'ptwiki' => array(
		NS_USER => 'Usuário(a)', // T29495
		NS_USER_TALK => 'Usuário(a)_Discussão',
		100 => 'Portal',
		101 => 'Portal_Discussão',
		104 => 'Livro',
		105 => 'Livro_Discussão',
	),

'''

def main():
	wikis = ['test']
	f1 = open( 'result.txt', 'w' )



def result( wikis ):
	for wiki in wikis:
		db = MySQLdb.connect( host = wiki + 'wiki.labsdb', user = credentials['user'], passwd = credentials['pass'], db = wiki + 'wiki_p' )
		


def query( wiki, namespaces, db ):
	if wiki == 'ru':
		namespaces = [ [0, 6, 102], [8, 10, 828], [4, 14, 100, 104] ]
	else:
		namespaces = [ [0, 6, 118], [8, 10, 828], [4, 14, 100, 102] ]
	cur = db.cursor()

	list1 = set()

	for n in namespaces:
		placeholder = '?' # http://stackoverflow.com/questions/283645/python-list-in-sql-query-as-parameter
		placeholders = ', '.join(placeholder for unused in n)
		q = """SELECT rc_user, rc_user_text, SUM(CASE WHEN rc_namespace IN (%s) THEN 1 ELSE 0 END) AS hits
			   FROM recentchanges
			   WHERE rc_bot = 0
			   GROUP by rc_user
			   ORDER BY hits DESC
			   LIMIT 100;
			"""
		cur.execute( q, placeholders )

		for row in cur.fetchall():
			list1.add( row[1] )

	print len(list1)








