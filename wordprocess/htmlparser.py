#!/usr/bin/python
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
#xml = '<person name="Bob"><parent rel="mother" name="Alice">'
#with open('chapter1.html') as f:
#    html = f.read()
html = '<html><head><title>titlestr</title></head><body><ul><li><p>this is p first inner</p></li><li><p>this is p inner</p></li></ul></body></html>'
#soup = BeautifulSoup('chapter1.html')
soup = BeautifulSoup(html)
results = soup.findAll(['p', 'ul'])
import pdb; pdb.set_trace()
print soup.prettify()
print '--' * 10
print results
#SoupStrainer(lambda name, attrs: \
#                                len(name) == 1 and not attrs)
#[tag for tag in BeautifulSoup(doc, parseOnlyThese=shortWithNoAttrs)]
