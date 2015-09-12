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

#   ʵ��������
ConnectStatus = ConnectStatus()
Station = Station()
Printf = Printf()

class init:

    def __init__(self):
        pass

    def run(self):
        #   �ж����绷��
        if not(ConnectStatus.connect()):
            print("No network Connection.")
            exit()
        else:
            #   ��ȡվ��&����
            from_station = Station.startstation()
            to_station = Station.endstation()
            queryDate = Station.querydate()

        #   Ŀ������
        targeturl = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+queryDate+'&from_station='+from_station+'&to_station='+to_station
        # print(targeturl)

        #   ֤������
        ssl._create_default_https_context = ssl._create_unverified_context
        information = urllib.request.urlopen(str(targeturl)).read().decode('utf-8')
        # print(information)

        content = json.loads(information)
        # print(content)

        #   ��ʱ
        time_start = time.time()

        #   �����ȡ���
        if content['data']['flag']:
            ticketinfo = content['data']['datas']
            count = Printf.printf(ticketinfo)

        else:
            print("ָ������û�пɴ�˵Ļ�")
        pass

        time_end=time.time()

        print("������������ʱ", '%.3f' % (time_end-time_start), "��,���", count, "�����")
        #   ���˽��
        #   ���� ->"message":"û�з������������ݣ�"

        #   ������



if __name__ == '__main__':
    TickeHelper = init()
    TickeHelper.run()