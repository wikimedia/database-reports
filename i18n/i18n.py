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

		"newwp-date": "Date created",
		"newwp-title": "Title",
		"newwp-page-title": "New WikiProjects",
		"newwp-desc": "Wikiprojects created in the last month",

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
		"mostusedtemplate-desc": "Modeles inclus sur le plus grand nombre de pages (limité à 3000)",
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
	},

	'kodict' : {
		"reports_base_url": "위키백과:데이터베이스 보고서/", # The base URL for the report, preceding the page title
		"summary": "봇: 보고서 업데이트",
		"yes-label": "예",
		"no-label": "아니오",

		"forgotten-articles-page-title": "잊혀진 문서", # The page title where report is published
		"forgotten-articles-desc": "가장 오랫동안 편집되지 않은 500개 문서, 넘겨주기/동음이의어 문서 제외.",
		"forgotten-articles-title": "제목",
		"forgotten-articles-last-edited": "마지막 편집",
		"forgotten-articles-editcount": "편집 수",

		"pagecount-page-title": "이름공간 별 문서 수",
		"pagecount-desc": "각 [[위키백과:이름공간|이름공간]] 별로 포함된 문서 수",
		"pagecount-namespace": "이름공간 ID",
		"pagecount-total": "총 문서 수",
		"pagecount-redirect": "넘겨주기 문서 수",
		"pagecount-non-redirect": "넘겨주기가 아닌 문서 수",
		"pagecount-namespace-name": "이름공간",

		"pagerevisions-page-title": "가장 많이 편집된 문서",
		"pagerevisions-desc": "가장 많은 편집을 가진 문서. 첫 1000개 값만 표시됩니다.",
		"pagerevisions-namespace": "이름공간",
		"pagerevisions-title": "문서",
		"pagerevisions-revisions": "편집 수",

		"newwp-date": "생성된 날짜",
		"newwp-title": "제목",
		"newwp-page-title": "새 위키프로젝트",
		"newwp-desc": "최근 한 달 사이에 생성된 위키프로젝트들",

		"autopatrol-page-title": "점검 면제자를 받아도 될 만한 사용자",
		"autopatrol-desc": "점검 면제자를 받아도 될 만한 편집 수를 가지고 있지만 점검 면제자 권한은 없는 사용자. 가장 많은 문서를 생성한 사람을 기준으로 첫 500명까지만 표시됩니다.",
		"autopatrol-username": "사용자 이름",
		"autopatrol-listlink": " ",
		"autopatrol-articles": "문서 카운트",

		"tpbs-page-title": "크기별 토론 문서",
		"tpbs-desc": "의견이 많이 오가는 토론장을 파악하기 위해 보존문서, 의견 요청, 그 외 하위 문서를 모두 포함한 토론 문서의 총 크기.",
		"tpbs-namespace": "이름공간",
		"tpbs-size": "크기 (MB)",
		"tpbs-page": "문서",

		"ufr-page-title": "쓰지 않는 파일 넘겨주기",
		"ufr-desc": "최대 1개의 문서에서 사용되는 파일 넘겨주기 목록. 최근 500개만 표시됩니다.",
		"ufr-page": "문서",
		"ufr-imagelinks": "사진 링크",
		"ufr-links": "링크",

		"oldestactive-page-title": "가장 오래 활동한 편집자",
		"oldestactive-desc": "최근 30일동안 활동한 편집자 중 가장 먼저 계정을 생성한 사용자 200명.",
		"oldestactive-username": "사용자 이름",
		"oldestactive-creationdate": "계정을 생성한 날짜",
		"oldestactive-editcount": "대략적인 편집 수",

		# "deletedprods-page-title": "PRODed articles with deletion logs",
		# "deletedprods-desc": "List of [[WP:PROD|PRODed]] articles that have previously been deleted. Limited to 500 articles.",
		# "deletedprods-title": "Article title",
		# "deletedprods-deletecount": "Delete count",
		# "deletedprods-firstdeltime": "First deletion",
		# "deletedprods-lastdeltime": "Last deletion",
		# "deletedprods-delcomments": "Deletion comments",

		"mostusedtemplate-page-title": "가장 많은 문서에서 끼워넣는 틀",
		"mostusedtemplate-desc": "가장 많은 문서에서 끼워넣는 틀. 첫 3000개만 표시합니다.",
		"mostusedtemplate-title": "틀 이름",
		"mostusedtemplate-count": "끼워넣기 수",

		"unusedtemplate-page-title": "쓰이지 않는 틀",
		"unusedtemplate-desc": "끼워넣는 문서가 없는 틀. 첫 2000개만 표시합니다.)",
		"unusedtemplate-title": "틀 이름",

		"orphantalk-page-title": "버려진 토론 문서",
		"orphantalk-desc": "버려진 토론 문서. 첫 1000개만 표시됩니다.",
		"orphantalk-itemtitle": "문서",
		"orphantalk-namespace": "이름공간",
		"orphantalk-exists": "존재하는 문서 여부",
		"orphantalk-isredirect": "넘겨주기",
		"orphantalk-count": "카운트",
		"orphantalk-pagesize": "크기",

		"article_by_size-page-title": "크기별 문서",
		"article_by_size-desc": "주 이름공간의 문서 크기가 가장 많은 순으로 정렬",
		"article_by_size-namespace": "이름공간",
		"article_by_size-title": "문서",
		"article_by_size-size": "크기",

		"most_edited_page_last_month-page-title": "지난 달에 가장 많이 편집된 문서",
		"most_edited_page_last_month-desc": "최근 30일동안 가장 많이 편집된 문서. 첫 25개 한정으로 표시합니다.",
		"most_edited_page_last_month-title": "제목",
		"most_edited_page_last_month-editcount": "편집 수",
	},

	'vidict' : {
		"reports_base_url": "Wikipedia:Báo cáo cơ sở dữ liệu/",
		"summary": "Bot: Đang cập nhật báo cáo",
		"yes-label": "Vâng",
		"no-label": "Không",

		"article_by_size-page-title": "Bài viết theo kích cỡ",
		"article_by_size-desc": "Các bài viết theo tổng kích cỡ, chủ yếu trong không gian tên chính",
		"article_by_size-namespace": "Không gian tên",
		"article_by_size-title": "Bài viết",
		"article_by_size-size": "Độ dài",

		"most_edited_page_last_month-page-title": "Bài viết được sửa nhiều lần nhất trong tháng vừa qua",
		"most_edited_page_last_month-desc": "Các bài viết theo số lần sửa đổi trong 30 ngày vừa qua, giới hạn trong 25 bài được sửa nhiều nhất",
		"most_edited_page_last_month-title": "Tên bài",
		"most_edited_page_last_month-editcount": "Số phiên bản",

		"oldestactive-page-title": "Thành viên tích cực có lịch sử đóng",
		"oldestactive-desc": "50 tài khoản người dùng được mở sớm nhất tích cực sửa đổi trong 30 ngày vừa qua",
		"oldestactive-username": "Tên người dùng",
		"oldestactive-creationdate": "Ngày mở tài khoản",
		"oldestactive-editcount": "Số sửa đổi xấp xỉ",

		"pagecount-page-title": "Số trang theo không gian tên",
		"pagecount-desc": "Số trang theo từng không gian tên",
		"pagecount-namespace": "ID không gian tên",
		"pagecount-total": "Tổng số trang",
		"pagecount-redirect": "Trang đổi hướng",
		"pagecount-non-redirect": "Trang không đổi hướng",
		"pagecount-namespace-name": "Không gian tên",
	}
}