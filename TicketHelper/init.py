#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

import urllib
import ssl
import json
import time
from TicketHelper.Station import Station
from TicketHelper.connect import ConnectStatus
from TicketHelper.Printf import Printf

#   实例化对象
ConnectStatus = ConnectStatus()
Station = Station()
Printf = Printf()

class init:

    def __init__(self):
        pass

    def run(self):
        #   判断网络环境
        if not(ConnectStatus.connect()):
            print("No network Connection.")
            exit()
        else:
            #   获取站点&日期
            from_station = Station.startstation()
            to_station = Station.endstation()
            queryDate = Station.querydate()

        #   目标链接
        targeturl = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+queryDate+'&from_station='+from_station+'&to_station='+to_station
        # print(targeturl)

        #   证书问题
        ssl._create_default_https_context = ssl._create_unverified_context
        information = urllib.request.urlopen(str(targeturl)).read().decode('utf-8')
        # print(information)

        content = json.loads(information)
        # print(content)

        #   计时
        time_start = time.time()

        #   输出获取结果
        if content['data']['flag']:
            ticketinfo = content['data']['datas']
            count = Printf.printf(ticketinfo)

        else:
            print("指定日期没有可搭乘的火车")
        pass

        time_end=time.time()

        print("本次搜索共耗时", '%.3f' % (time_end-time_start), "秒,获得", count, "条结果")
        #   过滤结果
        #   过滤 ->"message":"没有符合条件的数据！"

        #   输出结果



if __name__ == '__main__':
    TickeHelper = init()
    TickeHelper.run()