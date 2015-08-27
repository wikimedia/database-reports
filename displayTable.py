def generate_wikitext( content ):
	wikitext = '{| class="wikitable sortable" style="width:100%; margin:auto;" \n |- \n'
	wikitext = wikitext + '! ' + 'No.' + '\n'
	collen = len( content[0] )
	rowlen = len( content )

	for x in range( 0, collen ):
		wikitext = wikitext + '! ' + str( content[0][x] ) + '\n'

	for x in range( 1, rowlen ):
		wikitext = wikitext + '|- \n'
		wikitext = wikitext + '| ' + str( x ) + '\n'
		for i in range( 0, collen ):
			wikitext = wikitext + '| ' + str( content[x][i] ) + '\n'

	wikitext = wikitext + '|}'
	return wikitext
