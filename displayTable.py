from i18n import i18n
import time

''' Function to generate the wikitext for the report page
	@param wiki - Language code for the wiki (eg: 'en', 'es', 'it')
	@param content - Python 2D array (nested list) containing table entries
	@param desc - Key to the description message of the report
'''

def display_report( wiki, content, desc ):

	# Find out the dictionary containing messages for given wiki/language code
	dict_obj = i18n.lang_dicts[ str( wiki + 'dict') ]

	wikitext = dict_obj[ str( desc ) ] + ' -- ~~~ <onlyinclude>~~~~~</onlyinclude>\n'
	wikitext = wikitext + '{| class="wikitable sortable" \n |- \n'
	collen = len( content[0] )
	rowlen = len( content )

	for x in range( 0, collen ):
		wikitext = wikitext + '! ' + dict_obj[ str( content[0][x] ) ] + '\n'

	for x in range( 1, rowlen ):
		wikitext = wikitext + '|- \n'
		for i in range( 0, collen ):
			wikitext = wikitext + '| ' + str( content[x][i] ) + '\n'

	wikitext = wikitext + '|}'
	return wikitext
