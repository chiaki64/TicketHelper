#判断网络环境
import TicketHelper.connect
import TicketHelper.Station
import urllib.request
import ssl
import sys
import http.cookiejar


if(not(TicketHelper.connect.connect())):
    print("No network Connection.")
else:
    print("No network Connection.")

pass


#获取站点…&日期
from_station = TicketHelper.Station.StartStation()
to_station = TicketHelper.Station.EndStation()
queryDate = TicketHelper.Station.TodayTime()
#目标链接
testurl='https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate='+queryDate+'&from_station='+'ZDS'+'&to_station='+'XKS'
print(testurl)

#证书问题
ssl._create_default_https_context = ssl._create_unverified_context
information=urllib.request.urlopen(str(testurl)).read()

print(information)

#过滤结果

#输出结果