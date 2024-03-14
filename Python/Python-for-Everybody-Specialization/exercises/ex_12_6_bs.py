import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Web - ')
count = int(input('Enter count - '))
i = int(input('Enter position - '))

def scrape(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all the anchor tags
    tags = soup('a')
    return tags

l = list()
for n in range(count):
    for tag in scrape(url):
        l.append(tag.get('href', None))
        if len(l) == i:
            break
    url = l[i-1]
    print(url)
    l = list()
name = re.findall('.by_(\S+)[.]',url)
print(name)
