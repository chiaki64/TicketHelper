#-*- coding:utf8 -*-
import time
import json

'''
def _init():
    with open('Station.ini', 'r') as s:
        text = s.readline()
        names = json.loads(text)
    print(names['诏安'])
    print('拜山' in names)
'''


def StartStation():
    print("请输入起始站点:")#尝试用API分析当前地址
    from_station = input()
    from_station=str(from_station)

    with open('Station.ini', 'r') as s:
        text = s.readline()
        names = json.loads(text)
    print(names[from_station])#del
    return names[from_station]

def EndStation():
    print("请输入目标站点:")#尝试用API分析当前地址
    to_station = input()
    to_station=str(to_station)

    with open('Station.ini', 'r') as s:
        text = s.readline()
        names = json.loads(text)
    print(names[to_station])#del
    return names[to_station]

def TodayTime():
    todaytime=time.strftime("%Y-%m-%d")
    print(todaytime)
    return todaytime

pass
