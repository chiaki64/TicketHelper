#!/usr/bin/env python
# -*- coding: gbk -*

import TicketHelper.connect
import TicketHelper.Station
import urllib.request
import ssl
import sys
import http  #.cookiejar

#判断网络环境
if(not(TicketHelper.connect.connect())):
    #print("No network Connection.")
    exit()
else:
    #获取站点&日期
    from_station = TicketHelper.Station.StartStation()
    to_station = TicketHelper.Station.EndStation()
    queryDate = TicketHelper.Station.QueryDate()

    #目标链接
    testurl='https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+queryDate+'&from_station='+from_station+'&to_station='+to_station
    print(testurl)

    #证书问题
    ssl._create_default_https_context = ssl._create_unverified_context
    information = urllib.request.urlopen(str(testurl)).read()

    print(information)#Mark

    isExist = '\"flag\":true' in str(information)
    if(not(isExist)):
        print("指定日期没有可搭乘的火车")
    else:
        print("指定日期有可搭乘的火车")

    #过滤结果
    ##过滤 ->"message":"没有符合条件的数据！"

    #输出结果

