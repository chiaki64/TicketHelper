#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

import urllib
import ssl
import json
import string

class TicketPrice:

    def __int__(self):
        pass
    
    def TicketPrice(self,train_no,from_station_no,to_station_no,seat_types,train_date):
        self.priceurl='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no='+train_no+'&from_station_no='+from_station_no+'&to_station_no='+to_station_no+'&seat_types='+seat_types+'&train_date='+train_date
        #   print(priceurl)

        #   证书问题
        ssl._create_default_https_context = ssl._create_unverified_context
        self.information = urllib.request.urlopen(str(self.priceurl)).read().decode('gbk')
        #   print(information)
        #   END
        self.information = str(self.information)

        #   print(information.replace('楼',''))
        self.ticketcontent = json.loads(self.information.replace('楼',''))

        return self.ticketcontent
