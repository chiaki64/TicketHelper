#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

import urllib.request
import socket

class ConnectStatus:

    def __init__(self):
        pass

    def connect(self):
        is_online = False
        try:
            is_online = u'<title>' in urllib.request.urlopen("http://www.baidu.com", None, 4).read().decode('utf-8')
        except urllib.error.URLError as e:
            print("Network Connection Error : ", e, "\nPlease Check You Network Connection")
        finally:
            if is_online:
                return True
            else:
                return False


#   print(connect())

if __name__ == '__main__':
    cs = ConnectStatus()
    cs.connect()
