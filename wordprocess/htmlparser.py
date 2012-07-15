#!/usr/bin/python
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
import re
#xml = '<person name="Bob"><parent rel="mother" name="Alice">'
with open('chapter1.html') as f:
    html = f.read()
#html = '<html><head><title>titlestr</title></head><body><ul><li><p>this is p first inner</p></li><li><p>this is p inner</p></li></ul></body></html>'
#soup = BeautifulSoup('chapter1.html')
if 1:
    soup = BeautifulSoup(html)
    results = soup.findAll(['p', 'ul'])
    #results = soup.findAll(re.compile('.*'))
    import pdb; pdb.set_trace()
    print soup.prettify()
    print '--' * 10
    print results
else:
    soup = BeautifulSoup(html)
    texts = soup.findAll(re.compile('.*'),text=True)

    def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element)):
            return False
        return True

    visible_texts = filter(visible, texts)
    print visible_texts
    import pdb; pdb.set_trace()
#SoupStrainer(lambda name, attrs: \
#                                len(name) == 1 and not attrs)
#[tag for tag in BeautifulSoup(doc, parseOnlyThese=shortWithNoAttrs)]
