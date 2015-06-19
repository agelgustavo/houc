import urllib2
import re

from urllib import FancyURLopener
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

page = urllib2.urlopen("http://magiccards.info/query?q=dark+ritual&v=card&s=cname")
pattern = re.compile('http://magiccards.info/scans/.*"')

bytes_to_read = 1000
while 1:
    matches = pattern.findall(page.read(bytes_to_read))
    if len(matches) == 1:
        image_url = matches[0].strip('"')
        browser = MyOpener()
        browser.retrieve(image_url, 'carta.jpg')
        break
    else:
        bytes_to_read += 1000
