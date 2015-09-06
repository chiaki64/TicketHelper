#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

import time
import json
import datetime

def StartStation():
    print("��������ʼվ��:") #������API������ǰ��ַ
    from_station = input()
    from_station=str(from_station)
    with open('Station.ini', 'r') as s:
        text = s.readline()
        names = json.loads(text)
    print(names[from_station])#del
    return names[from_station]

def EndStation():
    print("������Ŀ��վ��:") #������API������ǰ��ַ
    to_station = input()
    to_station=str(to_station)
    with open('Station.ini', 'r') as s:
        text = s.readline()
        names = json.loads(text)
    print(names[to_station]) #del
    return names[to_station]

def QueryDate():
    print("��ѡ���ѯ���� 1.���� 2.���� 3.�Զ���(��ʽ:��-��-��)")
    choose = input()
    if(choose == '1'):
        QueryDate=time.strftime("%Y-%m-%d")
    elif(choose == '2'):
        today = datetime.date.today()
        QueryDate = today + datetime.timedelta(days=1)
    else:
        QueryDate = input()
    print("��ѯ���� ",QueryDate)
    return str(QueryDate)

