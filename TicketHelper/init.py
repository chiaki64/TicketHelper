#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

import TicketHelper.Station
import TicketHelper.TicketPrice
#import TicketHelper.connect
from TicketHelper.connect import ConnectStatus
import urllib
import ssl
import json
import time

#ConnectStatus = TicketHelper.connect.ConnectStatus()
Station = TicketHelper.Station.Station()
Price = TicketHelper.TicketPrice.TicketPrice()

#   �ж����绷��
if not(ConnectStatus.connect()):
    print("No network Connection.")
    exit()
else:
    #   ��ȡվ��&����
    from_station = Station.StartStation()
    to_station = Station.EndStation()
    queryDate = Station.QueryDate()

    #   Ŀ������
    targeturl = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+queryDate+'&from_station='+from_station+'&to_station='+to_station
    #   print(targeturl)

    #   ֤������
    ssl._create_default_https_context = ssl._create_unverified_context
    information = urllib.request.urlopen(str(targeturl)).read().decode('utf-8')

    #   print(information)#Mark

    #   information=str(information)
    #   print(information)
    content = json.loads(information)
    #   print(content)

    #   ��ʱ
    time_start=time.time()
    count = 0;

    if content['data']['flag']:
        ticketInfo=content['data']['datas']
        #   print("��Ʊ��Ϣ:",ticketInfo,"\n")

        for item in ticketInfo:
            if item["zy_num"] == '--':
                item["zy_num"] = ''
            if item["zy_num"] == '��':
                item["zy_num"] = 'N'
            if item["ze_num"] == '--':
                item["ze_num"] = ''
            if item["ze_num"] == '��':
                item["ze_num"] = 'N'
            if item["wz_num"] == '--':
                item["wz_num"] = ''
            if item["wz_num"] == '��':
                item["wz_num"] = 'N'

            start_train_date = str(item["start_train_date"])
            start_train_date = start_train_date[:4]+'-'+start_train_date[4:6]+'-'+start_train_date[6:]
            #   print(start_train_date)

            ticketcontent = Price.TicketPrice(item["train_no"],item["from_station_no"],item["to_station_no"],item["seat_types"],start_train_date)
            #   print(ticketcontent)
            price = ticketcontent['data']

            if 'M' in price:
                M_price = str(price["M"])
            else:
                M_price = 'None'

            if 'O' in price:
                O_price = str(price["O"])
            else:
                O_price = 'None'

            if 'WZ' in price:
                WZ_price = str(price["WZ"])
            else:
                WZh_price='None'

            print("����",'%-5s' % item["station_train_code"],"����ʱ��",item["start_time"],"����ʱ��",item["arrive_time"],"һ����",'%-3s' % item["zy_num"],'��'+'%-6s' % M_price,"������",'%-3s' % item["ze_num"],
                  '��'+'%-6s' % O_price,"����",'%-3s' % item["wz_num"],'��'+'%-6s' % WZ_price)
            #   print(item)
            count = 1 + int(count)

    else:
        print("ָ������û�пɴ�˵Ļ�")
        pass

    time_end=time.time()
    print("������������ʱ", time_end-time_start, "��,���", count, "�����")
    #   ���˽��
    #   ���� ->"message":"û�з������������ݣ�"

    #   ������

