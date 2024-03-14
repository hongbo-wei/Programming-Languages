import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# https://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_1689134.xml
url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

total = 0
c = 0
counts = tree.findall('.//count')  # lst = tree.findall('comments/comment')
for item in counts:                # for item in lst:
    count = int(item.text)         # count = int(item.find('count').text)
    c += 1
    total += count

print('Count', c)
print('Sum', total)