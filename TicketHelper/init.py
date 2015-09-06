#!/usr/bin/env python
# -*- coding: gbk -*

import TicketHelper.connect
import TicketHelper.Station
#import TicketHelper.TicketPrice
import urllib
import ssl
import json
import sys
import http  #.cookiejar


#�ж����绷��
if(not(TicketHelper.connect.connect())):
    #print("No network Connection.")
    exit()
else:
    #��ȡվ��&����
    from_station = TicketHelper.Station.StartStation()
    to_station = TicketHelper.Station.EndStation()
    queryDate = TicketHelper.Station.QueryDate()

    #Ŀ������
    testurl='https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+queryDate+'&from_station='+from_station+'&to_station='+to_station
    print(testurl)

    #֤������
    ssl._create_default_https_context = ssl._create_unverified_context
    information = urllib.request.urlopen(str(testurl)).read().decode('utf-8')

    print(information)#Mark

    '''
    isExist = '\"flag\":true' in str(information)
    if(not(isExist)):
        print("ָ������û�пɴ�˵Ļ�")
    else:
        print("ָ�������пɴ�˵Ļ�")
    '''
    print("0")
    #    information=str(information)
    #    print(information)
    content = json.loads(information)
    print(content)

    if(content['data']['flag']):
        ticketInfo=content['data']['datas']
        print("��Ʊ��Ϣ:",ticketInfo,"\n")

        for item in ticketInfo:
            if(item["zy_num"]=='--'):
                item["zy_num"]=''
            if(item["zy_num"]=='��'):
                item["zy_num"]='N'
            if(item["ze_num"]=='--'):
                item["ze_num"]=''
            if(item["ze_num"]=='��'):
                item["ze_num"]='N'
            if(item["wz_num"]=='--'):
                item["wz_num"]=''
            if(item["wz_num"]=='��'):
                item["wz_num"]='N'


          #  TicketHelper.TicketPrice.TicketPrice(item["train_no"],item["from_station_no"])


            print("����",'%-5s' % item["station_train_code"],"����ʱ��",item["start_time"],"��ʱ",item["lishi"],"һ����",'%-3s' % item["zy_num"],"�۸�","������",'%-3s' % item["ze_num"],
                  "�۸�","����",'%-3s' % item["wz_num"],"�۸�")
            #print(item)

    else:
        print("ָ������û�пɴ�˵Ļ�")
        pass

    #���˽��
    ##���� ->"message":"û�з������������ݣ�"

    #������

