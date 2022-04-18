# Database Reports
Generates statistical reports which are used by community members to improve Wikipedia.

This project allows the [Community Tech bot](https://en.wikipedia.org/wiki/User:Community_Tech_bot) to make periodic updates to these reports on different language Wikipedias. As of now the project support report generation for English ([see here](https://en.wikipedia.org/wiki/Wikipedia:Database_reports)), Vietnamese, Korean and French Wikipedia.

## Specific statistics that the reports support:
* Unused templates
* Forgotten articles
* Most used templates
* New wiki projects
* Talk pages by size
* Orphaned talk pages
* Unused file redirects
* Forgotten articles
* Page with most revisions
* Page count by namespace
* Most edited articles last month
* PRODed articles with deletion logs
* Active editors with the longest-established accounts

## Installation
Virtualenv is recommended:

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

After installation, either activate virtualenv like above or use `venv/bin/python` to run scripts.

## Generating a report

Run ```python3 main.py test orphaned_talk```. It takes two arguments; in this example test refers to
`test.wikipedia.org` and `orphaned_talk` is the type of statistics you're requesting. This command outputs
the name of the page on which the report got dumped.

You can pass the ```--dry-run``` flag to print output to stdout rather than editing the wiki.

On Toolforge, the reports are defined in the ```jobs.yaml``` file.
See the [Toolforge jobs framework documentation](https://wikitech.wikimedia.org/wiki/Help:Toolforge/Jobs_framework) for more information.

If you need to run a one-off job on Toolforge, find the corresponding command in ```jobs.yaml``` and [schedule it](https://wikitech.wikimedia.org/wiki/Help:Toolforge/Jobs_framework#Creating_one-off_jobs) using ```toolforge-jobs```.

## Adding support for a report
* To add support for a specific statistics that you would like to see in a report, declare a function in `main.py` and define it in `reports.py`
* To provide support for translations in a specific language, include the dictionary in `i18n/i18n.py`

## Contributing
Bug reports, fixes, and new features are welcomed. If you'd like to contribute code please:
* Fork the project
* Start a branch named for your new feature or bug
* Create a pull request
