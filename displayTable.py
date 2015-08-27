def generate_wikitext( content ):
	wikitext = '{| class="wikitable" \n |- \n'
	collen = len( content[0] )
	rowlen = len( content )

	for x in range( 0, collen ):
		wikitext = wikitext + '! ' + content[0][x] + '\n'

	for x in range( 0, rowlen ):
		wikitext = wikitext + '|- \n'
		for i in range( 0, collen ):
			wikitext = wikitext + '| ' + content[x][i] + '\n'

	wikitext = wikitext + '|}'
	return wikitext
