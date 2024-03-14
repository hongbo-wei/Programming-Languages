starturl = 'http://www.dr-chuck.com/txt.htm'
if ( starturl.endswith('/') ) : starturl = starturl[:-1]
web = starturl
print(web)
if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
    pos = starturl.rfind('/')
    web = starturl[:pos]
    print(pos)
    print(web)