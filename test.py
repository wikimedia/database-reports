import mwclient
site = mwclient.Site('en.wikipedia.org')

page = site.Pages['Battle of Trenton']

text = page.text()
print 'Trenton thingy: ', text.encode('utf-8')


password = WTLGQYvp0zq8oeNS
user = s52664
