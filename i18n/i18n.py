#!/usr/bin/python
# -*- coding: utf-8 -*-

lang_dicts = {

	'endict' : {
		"reports_base_url": "Wikipedia:Database reports/", # The base URL for the report, preceding the page title
		"summary": "Bot: Updating report",
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

		"unusedtemplate-page-title": "Unused templates",
		"unusedtemplate-desc": "Templates with the no transclusions (limited to the first 2000 entries)",
		"unusedtemplate-title": "Template title",

		"orphantalk-page-title": "Orphaned talk pages",
		"orphantalk-desc": "Orphaned talk pages, limited to 1000",
		"orphantalk-itemtitle": "Page",
		"orphantalk-namespace": "Namespace",
		"orphantalk-exists": "Exists?",
		"orphantalk-isredirect": "Redirect?",
		"orphantalk-count": "Count",
		"orphantalk-pagesize": "Size",

		"article_by_size-page-title": "Articles by size",
		"article_by_size-desc": "Articles ranked by total size, principal mainspace.",
		"article_by_size-namespace": "Namespace",
		"article_by_size-title": "Article",
		"article_by_size-size": "Taille",

		"most_edited_page_last_month-page-title": "Most edited articles last month",
		"most_edited_page_last_month-desc": "Articles ranked by number of edits during last 30 days, limit to the 25 firsts.",
		"most_edited_page_last_month-title": "Title",
		"most_edited_page_last_month-editcount": "Revisions",
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
		"reports_base_url": "Wikipedia:Database reports/", # The base URL for the report, preceding the page title
		"summary": "Bot: Updating report",
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

		"unusedtemplate-page-title": "Unused templates",
		"unusedtemplate-desc": "Templates with the no transclusions (limited to the first 5000 entries)",
		"unusedtemplate-title": "Template title",

		"orphantalk-page-title": "Orphaned talk pages",
		"orphantalk-desc": "Orphaned talk pages, limited to 1000",
		"orphantalk-count": "Count",
		"orphantalk-itemtitle": "Page",
		"orphantalk-namespace": "Namespace",
		"orphantalk-exists": "Exists?",
		"orphantalk-isredirect": "Redirect?",
		"orphantalk-pagesize": "Size",

		"article_by_size-page-title": "Articles by size",
		"article_by_size-desc": "Articles ranked by total size, principal mainspace.",
		"article_by_size-namespace": "Namespace",
		"article_by_size-title": "Article",
		"article_by_size-size": "Taille",

		"most_edited_page_last_month-page-title": "Most edited articles last month",
		"most_edited_page_last_month-desc": "Articles ranked by number of edits during last 30 days, limit to the 25 firsts.",
		"most_edited_page_last_month-title": "Title",
		"most_edited_page_last_month-editcount": "Revisions",
	},

	'frdict' : {
		"reports_base_url": "Wikipedia:Rapports/", # The base URL for the report, preceding the page title
		"summary": "Bot: Mise à jour",
		"yes-label": "Oui",
		"no-label": "Non",

		"forgotten-articles-page-title": "Articles oublies", # The page title where report is published
		"forgotten-articles-desc": "Liste des 500 articles qui n'ont pas étés édités depuis le plus longtemps, hors redirections. Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"forgotten-articles-title": "Titre",
		"forgotten-articles-last-edited": "Dernière édition",
		"forgotten-articles-editcount": "Nombre d'éditions",

		"pagecount-page-title": "Nombre de pages par namespace",
		"pagecount-desc": "Le nombre d'articles par [[Aide:Espace de noms|espace de nom]] (''namespace''). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"pagecount-namespace": "Namespace ID",
		"pagecount-total": "Nombre total de pages",
		"pagecount-redirect": "Pages avec redirections",
		"pagecount-non-redirect": "Pages sans redirections",
		"pagecount-namespace-name": "Namespace",

		"pagerevisions-page-title": "Pages avec le plus de modifications",
		"pagerevisions-desc": "Pages avec le plus de modifications (limité aux 1000 premiers articles). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"pagerevisions-namespace": "Namespace",
		"pagerevisions-title": "Article",
		"pagerevisions-revisions": "Modifications",

		"autopatrol-page-title": "Editors eligible for Autopatrol privilege - right not used ?",
		"autopatrol-desc": "List of editors who are eligible for the autopatrol privilege and don't have it yet. Limited to 500 users with most articles created.",
		"autopatrol-username": "Username",
		"autopatrol-listlink": " ",
		"autopatrol-articles": "Article count",

		"tpbs-page-title": "Pages de discussion par taille",
		"tpbs-desc": "Pages de discussion par leur taille totale, tous espaces de nom confondus, y compris les sous-pages (archives, pages individuelles, PàS, ...). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"tpbs-namespace": "Namespace",
		"tpbs-size": "Taille (en MB)",
		"tpbs-page": "Page",

		"ufr-page-title": "Unused file redirects - not necessary ?",
		"ufr-desc": "List of file redirects with at most one incoming link, limited to top 500 results.",
		"ufr-page": "Page",
		"ufr-imagelinks": "Image Links",
		"ufr-links": "Links",

		"oldestactive-page-title": "Editeurs actifs avec les comptes les plus anciens",
		"oldestactive-desc": "Les 200 éditeurs actifs (dernière modification dans les 30 derniers jours) par date de création. Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"oldestactive-username": "Nom d'utilisateur",
		"oldestactive-creationdate": "Date de création",
		"oldestactive-editcount": "Compteur d'édition approximatif",

		"deletedprods-page-title": "PRODed articles with deletion logs - not necessary ?",
		"deletedprods-desc": "List of [[WP:PROD|PRODed]] articles that have previously been deleted. Limited to 500 articles.",
		"deletedprods-title": "Article title",
		"deletedprods-deletecount": "Delete count",
		"deletedprods-firstdeltime": "First deletion",
		"deletedprods-lastdeltime": "Last deletion",
		"deletedprods-delcomments": "Deletion comments",

		"mostusedtemplate-page-title": "Modeles inclus sur le plus grand nombre de pages",
		"mostusedtemplate-desc": "Modèles inclus sur le plus grand nombre de pages (limité à 3000)",
		"mostusedtemplate-title": "Nom du modèle",
		"mostusedtemplate-count": "Nombre d'inclusions",

		"unusedtemplate-page-title": "Modeles inutilises",
		"unusedtemplate-desc": "Modèles avec le moins d'inclusions (limité à 2000).",
		"unusedtemplate-title": "Nom du modèle",

		"orphantalk-page-title": "Pages de discussion orphelines",
		"orphantalk-desc": "Pages de discussion orphelines (limité à 1000). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"orphantalk-itemtitle": "Page",
		"orphantalk-namespace": "Namespace",
		"orphantalk-exists": "Existe",
		"orphantalk-isredirect": "Redirection",
		"orphantalk-count": "Compteur",
		"orphantalk-pagesize": "Taille",


		"article_by_size-page-title": "Articles par taille",
		"article_by_size-desc": "Articles les plus longs (espace principal). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"article_by_size-namespace": "Namespace",
		"article_by_size-title": "Article",
		"article_by_size-size": "Taille",

		"most_edited_page_last_month-page-title": "Articles les plus edites le mois dernier",
		"most_edited_page_last_month-desc": "Liste des 25 articles ayant eu le plus de modifications durant les 30 derniers jours. Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"most_edited_page_last_month-title": "Titre",
		"most_edited_page_last_month-editcount": "Nombre d'éditions",
	}
}
