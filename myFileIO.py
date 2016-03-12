#coding: utf-8
import json
import os.path

def get_days_no_rain():
    in_file = open('/home/pi/DadWeather/noRainDay','r')
    days_no_rain = int(in_file.read())
    in_file.close()
    return days_no_rain
    
def set_days_no_rain(days_no_rain):
    out_file = open('/home/pi/DadWeather/noRainDay','w')
    out_file.write(str(days_no_rain))
    out_file.close()
    return

def read_rain_month(month,year):
    path = "/home/pi/DadWeather/rain_data/"+str(year)+"/"+str(month)
    if os.path.isfile(path):
        in_file = open(path,'r')
        rain_list = json.load(in_file)
        in_file.close
    else:
        basedir = os.path.dirname(path)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        open(path,'a').close()
        rain_list = []
    return rain_list

def write_rain_month(month,year,rain_list):
    out_file = open("/home/pi/DadWeather/rain_data/"+str(year)+"/"+str(month),'w')
    json.dump(rain_list,out_file)
    out_file.close()
    return
