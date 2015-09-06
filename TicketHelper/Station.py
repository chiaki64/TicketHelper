#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

import time
import json
import datetime

def StartStation():
    print("请输入起始站点:") #尝试用API分析当前地址
    from_station = input()
    from_station=str(from_station)
    with open('Station.ini', 'r') as s:
        text = s.readline()
        names = json.loads(text)
    print(names[from_station])#del
    return names[from_station]

def EndStation():
    print("请输入目标站点:") #尝试用API分析当前地址
    to_station = input()
    to_station=str(to_station)
    with open('Station.ini', 'r') as s:
        text = s.readline()
        names = json.loads(text)
    print(names[to_station]) #del
    return names[to_station]

def QueryDate():
    print("请选择查询日期 1.今天 2.明天 3.自定义(格式:年-月-日)")
    choose = input()
    if(choose == '1'):
        QueryDate=time.strftime("%Y-%m-%d")
    elif(choose == '2'):
        today = datetime.date.today()
        QueryDate = today + datetime.timedelta(days=1)
    else:
        QueryDate = input()
    print("查询日期 ",QueryDate)
    return str(QueryDate)

