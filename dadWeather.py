#coding: utf-8
import webget
import myFileIO
from datetime import timezone,timedelta
import datetime

URL = 'http://www.cwb.gov.tw/V7/observe/rainfall/Rain_Hr/7.htm'
rain_str = webget.split_text(webget.url_to_text(URL))
days_no_rain = myFileIO.get_days_no_rain()
print (rain_str)
current_time = datetime.datetime.now(timezone(timedelta(hours=8)))
lookup_time = current_time-timedelta(days=1)
rain_list = myFileIO.read_rain_month(lookup_time.month,lookup_time.year)

#insert rain_str into list, filling all missing values with ?
date = lookup_time.day
if len(rain_list) < date:
    rain_list = rain_list + ['?']*(date - len(rain_list))
rain_list[date-1]=rain_str
#assert len(rain_list)==date

myFileIO.write_rain_month(lookup_time.month,lookup_time.year,rain_list)

if rain_str == "-":
    days_no_rain = days_no_rain + 1
else:
    days_no_rain = 0
myFileIO.set_days_no_rain(days_no_rain)
webget.send_email('dennis15926@gmail.com','RainProgram',rain_str)
text = """爸，昨天霧峰有下雨喔！
累計"""+str(rain_str)+"毫米"
if days_no_rain == 0:
    webget.send_email(['dennis15926@gmail.com','anchen0102@yahoo.com.tw'],"昨天霧峰有下雨",text)

