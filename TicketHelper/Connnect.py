import urllib.request
def connect():
      is_online = u'<title>' in urllib.request.urlopen("http://www.baidu.com").read().decode('utf-8')
      if(is_online):
        return True

print(connect())