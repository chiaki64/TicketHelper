import urllib.request
import socket

def connect():
      is_online = u'<title>' in urllib.request.urlopen("http://www.baidu.com").read().decode('utf-8')
      #urllib.request.close()
      if(is_online):
        return True
      else:
        return False


#print(connect())