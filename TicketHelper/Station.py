#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

import time
import json
import datetime

class Station:
    def __init__(self):
        pass

    def StartStation(self):
        print("请输入起始站点:")  # 尝试用API分析当前地址
        self.from_station = input()
        self.from_station=str(self.from_station)
        with open('Station.ini', 'r') as self.s:
            self.text = self.s.readline()
            self.names = json.loads(self.text)
        print(self.names[self.from_station])  # del
        return self.names[self.from_station]

    def EndStation(self):
        print("请输入目标站点:")  # 尝试用API分析当前地址
        self.to_station = input()
        self.to_station=str(self.to_station)
        with open('Station.ini', 'r') as s:
            text = s.readline()
            names = json.loads(text)
        print(names[self.to_station])  # del
        return names[self.to_station]

    def QueryDate(self):
        print("请选择查询日期 1.今天 2.明天 3.自定义(格式:年-月-日)")
        self.choose = input()
        if self.choose == '1':
            self.QueryDate=time.strftime("%Y-%m-%d")
        elif self.choose == '2':
            today = datetime.date.today()
            self.QueryDate = today + datetime.timedelta(days=1)
        else:
            self.QueryDate = input()
        print("查询日期 ",self.QueryDate)
        return str(self.QueryDate)

    def exist(self):
        pass
    #   比较字符串 KeyError


if __name__ == '__main__':
    s = Station()
    s.QueryDate()