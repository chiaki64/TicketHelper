#!/usr/bin/env python
# -*- coding: gbk -*
# @auther:Hieda no Chiaki <forblackking@gmail.com>

from TicketHelper.TicketPrice import TicketPrice

Price = TicketPrice()

class Printf:

    def __init__(self):
        pass

    def printf(self, ticketinfo): # ���ֵ��**
        # print(ticketinfo)
        count = 0

        for item in ticketinfo:
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
            # print(start_train_date)

            ticketcontent = Price.TicketPrice(item["train_no"],item["from_station_no"],item["to_station_no"],item["seat_types"],start_train_date)
            # print(ticketcontent)
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
            # print(item)

            count = int(count) + 1

        return count



if __name__ == '__main__':
    pass