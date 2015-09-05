#!/usr/bin/env python
# -*- coding: gbk -*

import urllib.request
import socket

def connect():
    is_online = False
    try:
        is_online = u'<title>' in urllib.request.urlopen("http://www.baidu.com", None, 2).read().decode('utf-8')
    except urllib.error.URLError as e:
        print("Network Connection Error : ", e, "\nPlease Check You Network Connection")
    finally:
        if(is_online):
            return True
        else:
            return False


#print(connect())