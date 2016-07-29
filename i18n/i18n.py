#!/usr/bin/python
# -*- coding: utf-8 -*-

lang_dicts = {

	'endict' : {
		"reports_base_url": "Wikipedia:Database reports/", # The base URL for the report, preceding the page title

		"yes-label": "Yes",
		"no-label": "No",

		"forgotten-articles-page-title": "Forgotten articles", # The page title where report is published
		"forgotten-articles-desc": "List of 500 articles that not been edited in the longest time, ignoring redirects and disambiguation pages.",
		"forgotten-articles-title": "Title",
		"forgotten-articles-last-edited": "Last edited",
		"forgotten-articles-editcount": "Number of edits",

		"pagecount-page-title": "Page count by namespace",
		"pagecount-desc": "The number of pages in each [[Wikipedia:Namespace|namespace]]",
		"pagecount-namespace": "Namespace ID",
		"pagecount-total": "Total pages",
		"pagecount-redirect": "Pages with redirects",
		"pagecount-non-redirect": "Pages without redirects",
		"pagecount-namespace-name": "Namespace",

		"pagerevisions-page-title": "Pages with the most revisions",
		"pagerevisions-desc": "Pages with the most revisions (limited to the first 1000 entries)",
		"pagerevisions-namespace": "Namespace",
		"pagerevisions-title": "Article",
		"pagerevisions-revisions": "Revisions",

		"autopatrol-page-title": "Editors eligible for Autopatrol privilege",
		"autopatrol-desc": "List of editors who are eligible for the autopatrol privilege and don't have it yet. Limited to 500 users with most articles created.",
		"autopatrol-username": "Username",
		"autopatrol-listlink": " ",
		"autopatrol-articles": "Article count",

		"tpbs-page-title": "Talk pages by size",
		"tpbs-desc": "Talk pages ranked by total size, including all subpages (e.g. archival subpages, individual WP:RFAs, etc.), to provide statistics on very active discussion pages.",
		"tpbs-namespace": "Namespace",
		"tpbs-size": "Size (in MB)",
		"tpbs-page": "Page",

		"ufr-page-title": "Unused file redirects",
		"ufr-desc": "List of file redirects with at most one incoming link, limited to top 500 results.",
		"ufr-page": "Page",
		"ufr-imagelinks": "Image Links",
		"ufr-links": "Links",

		"oldestactive-page-title": "Active editors with the longest-established accounts",
		"oldestactive-desc": "The 200 earliest-created editor accounts that have been active in the last thirty days.",
		"oldestactive-username": "Username",
		"oldestactive-creationdate": "Date created",
		"oldestactive-editcount": "Approx. edit count",

		"deletedprods-page-title": "PRODed articles with deletion logs",
		"deletedprods-desc": "List of [[WP:PROD|PRODed]] articles that have previously been deleted. Limited to 500 articles.",
		"deletedprods-title": "Article title",
		"deletedprods-deletecount": "Delete count",
		"deletedprods-firstdeltime": "First deletion",
		"deletedprods-lastdeltime": "Last deletion",
		"deletedprods-delcomments": "Deletion comments",

		"mostusedtemplate-page-title": "Templates transcluded on the most pages",
		"mostusedtemplate-desc": "Templates with the most transclusions (limited to the first 3000 entries)",
		"mostusedtemplate-title": "Template title",
		"mostusedtemplate-count": "Number of transclusions",

		"orphantalk-page-title": "Orphaned talk pages",
		"orphantalk-desc": "Orphaned talk pages, limited to 1000",
		"orphantalk-itemtitle": "Page",
		"orphantalk-namespace": "Namespace",
		"orphantalk-exists": "Exists?",
		"orphantalk-isredirect": "Redirect?",
		"orphantalk-count": "Count",
		"orphantalk-pagesize": "Size",
	},

	'esdict' : {
		"forgotten-articles-desc": "List of non-disambiguation, non-redirect oldest 1000 articles. - Spanish",
		"forgotten-articles-title": "Title - Spanish",
		"forgotten-articles-last-edited": "Last edited - Spanish",
		"forgotten-articles-editcount": "Number of edits - Spanish",

		"pagecount-desc": "The number of pages in each namespace. - Spanish",
		"pagecount-namespace": "Namespace - Spanish",
		"pagecount-total": "Total pages - Spanish",
		"pagecount-redirect": "Pages with redirects - Spanish",
		"pagecount-non-redirect": "Pages without redirects - Spanish",
	},

	'dedict' : {
		"reports_base_url": "Benutzer:Kopiersperre/",

		"forgotten-articles-page-title": "Vergessene Artikel",
		"forgotten-articles-desc": "Diese Liste enthält die 1000 Artikel, die am längsten nicht mehr bearbeitet wurden.",
		"forgotten-articles-title": "Artikel",
		"forgotten-articles-last-edited": "Letzte Bearbeitung",
		"forgotten-articles-editcount": "Bearbeitungen insgesamt",
	},

	'testdict': {
		"yes-label": "Yes",
		"no-label": "No",

		"reports_base_url": "Wikipedia:Database reports/",
		"forgotten-articles-page-title": "Forgotten articles - test", # The page title where report is published
		"forgotten-articles-desc": "List of 500 articles that not been edited in the longest time, ignoring redirects and disambiguation pages.",
		"forgotten-articles-title": "Title - test",
		"forgotten-articles-last-edited": "Last edited",
		"forgotten-articles-editcount": "Number of edits",

		"autopatrol-page-title": "Editors eligible for Autopatrol privilege",
		"autopatrol-desc": "List of editors who are eligible for the autopatrol privilege and don't have it yet. Limited to 500 users with most articles created.",
		"autopatrol-username": "Username",
		"autopatrol-listlink": " ",
		"autopatrol-articles": "Article count",

		"oldestactive-page-title": "Active editors with the longest-established accounts",
		"oldestactive-desc": "The 200 earliest-created editor accounts that have been active in the last thirty days.",
		"oldestactive-username": "Username",
		"oldestactive-creationdate": "Date created",

		"oldestactive-editcount": "Approx. edit count",

		"deletedprods-page-title": "PRODed articles with deletion logs",
		"deletedprods-desc": "Articles which are currently proposed for deletion which have previously been deleted..",
		"deletedprods-title": "Article title",
		"deletedprods-deletecount": "Delete count",
		"deletedprods-firstdeltime": "First deletion",
		"deletedprods-lastdeltime": "Last deletion",
		"deletedprods-delcomments": "Deletion comments",

		"mostusedtemplate-page-title": "Templates transcluded on the most pages",
		"mostusedtemplate-desc": "Templates with the most transclusions (limited to the first 3000 entries)",
		"mostusedtemplate-title": "Template title",
		"mostusedtemplate-count": "Number of transclusions",


		"orphantalk-page-title": "Orphaned talk pages",
		"orphantalk-desc": "Orphaned talk pages, limited to 1000",
		"orphantalk-count": "Count",
		"orphantalk-itemtitle": "Page",
		"orphantalk-namespace": "Namespace",
		"orphantalk-exists": "Exists?",
		"orphantalk-isredirect": "Redirect?",
		"orphantalk-pagesize": "Size",
	}

}
