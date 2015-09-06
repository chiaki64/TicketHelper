#!/usr/bin/env python
# -*- coding: gbk -*

import TicketHelper.connect
import TicketHelper.Station
import TicketHelper.TicketPrice
import urllib
import ssl
import json
import time
import sys
import http  #.cookiejar


#判断网络环境
if(not(TicketHelper.connect.connect())):
    print("No network Connection.")
    exit()
else:
    #计时
    time_start=time.time()
    count=1;
    #获取站点&日期
    from_station = TicketHelper.Station.StartStation()
    to_station = TicketHelper.Station.EndStation()
    queryDate = TicketHelper.Station.QueryDate()

    #目标链接
    testurl='https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+queryDate+'&from_station='+from_station+'&to_station='+to_station
    print(testurl)

    #证书问题
    ssl._create_default_https_context = ssl._create_unverified_context
    information = urllib.request.urlopen(str(testurl)).read().decode('utf-8')

    print(information)#Mark

    '''
    isExist = '\"flag\":true' in str(information)
    if(not(isExist)):
        print("指定日期没有可搭乘的火车")
    else:
        print("指定日期有可搭乘的火车")
    '''
    print("0")
    #    information=str(information)
    #    print(information)
    content = json.loads(information)
    print(content)

    if(content['data']['flag']):
        ticketInfo=content['data']['datas']
        print("车票信息:",ticketInfo,"\n")

        for item in ticketInfo:
            if(item["zy_num"]=='--'):
                item["zy_num"]=''
            if(item["zy_num"]=='无'):
                item["zy_num"]='N'
            if(item["ze_num"]=='--'):
                item["ze_num"]=''
            if(item["ze_num"]=='无'):
                item["ze_num"]='N'
            if(item["wz_num"]=='--'):
                item["wz_num"]=''
            if(item["wz_num"]=='无'):
                item["wz_num"]='N'

            start_train_date=str(item["start_train_date"])
            start_train_date=start_train_date[:4]+'-'+start_train_date[4:6]+'-'+start_train_date[6:]
            #print(start_train_date)

            ticketcontent=TicketHelper.TicketPrice.TicketPrice(item["train_no"],item["from_station_no"],item["to_station_no"],item["seat_types"],start_train_date)
            #print(ticketcontent)
            price=ticketcontent['data']
            #
            if('M' in price):
                M_price=str(price["M"])
            else:
                M_price='None'

            if('O' in price):
                O_price=str(price["O"])
            else:
                O_price='None'

            if('WZ' in price):
                WZ_price=str(price["WZ"])
            else:
                WZh_price='None'
            #

            print("车次",'%-5s' % item["station_train_code"],"出发时间",item["start_time"],"到达时间",item["arrive_time"],"一等座",'%-3s' % item["zy_num"],'%-6s' % M_price,"二等座",'%-3s' % item["ze_num"],
                  '%-6s' % O_price,"无座",'%-3s' % item["wz_num"],'%-6s' % WZ_price)
            #print(item)
            count=count+1

    else:
        print("指定日期没有可搭乘的火车")
        pass

    time_end=time.time()
    print("搜索共耗时",time_end-time_start,"秒,获得",count,"条结果")
    #过滤结果
    ##过滤 ->"message":"没有符合条件的数据！"

    #输出结果

