#判断网络环境
import TicketHelper.connect
import TicketHelper.Station
import urllib.request


if(not(TicketHelper.connect.connect())):
    print("No network Connection.")
else:
    print("No network Connection.")

pass
TicketHelper.Station.TodayTime()

print('1')

from_station=TicketHelper.Station.StartStation()
to_station=TicketHelper.Station.EndStation()

information=urllib.request.urlopen("http://www.chiaki.ml").read()
print(information)


#print("true")
#IncompleteRead

#选择输入方式

#输出结果