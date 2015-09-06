#!/usr/bin/env python
# -*- coding: gbk -*
'''
import urllib
import ssl
import json

def TicketPrice(train_no,from_station_no,to_station_no,seat_types,train_date):
    testurl='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no='+train_no+'&from_station_no='+from_station_no+'&to_station_no='+to_station_no+'&seat_types='+seat_types+'&train_date='+train_date

    print(testurl)
    pass




#证书问题
ssl._create_default_https_context = ssl._create_unverified_context
information = urllib.request.urlopen(str(testurl)).read().decode('utf-8')
'''