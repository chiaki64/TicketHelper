import urllib.request
import socket

def connect():
      is_online = u'<title>' in urllib.request.urlopen("http://www.baidu.com").read().decode('utf-8')
      #urllib.request.close()
      if(is_online):
        return True
'''


def connect():
    request=urllib.request.Request("http://www.baidu.com")
    response = urllib.request.urlopen(request)
    buff = response.read()
    #....
    html = buff.decode('utf-8')
    response.close()
    online = u'<title>' in html
    if(online):
        return True
    else:
        return False
'''




#print(connect())