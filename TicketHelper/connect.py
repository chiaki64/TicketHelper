#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

import urllib.request
import socket

class ConnectStatus:

    def __init__(self):
        pass

    def connect(self):
        print(type(self))
        self.status = False
        try:
            self.status = u'<title>' in urllib.request.urlopen("http://www.baidu.com", None, 4).read().decode('utf-8')
        except urllib.error.URLError as e:
            print("Network Connection Error : ", e, "\nPlease Check You Network Connection")
        finally:
            if self.status:
                return True
            else:
                return False


# print(connect())

if __name__ == '__main__':
    cs = ConnectStatus()
    cs.connect()
