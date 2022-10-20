#!/usr/bin/env python3
import requests as req
from datetime import datetime
now = datetime.now()
 
date_string = now.strftime("%m-%d-%Y")
time_string = now.strftime("%H:%M:%S")

sensors_ip = {
    "192.168.5.250":"outside",
    "192.168.5.251":"bedroom",
    "192.168.5.252":"living_room",
    "192.168.5.253":"kitchen"
}

print(date_string)
print(time_string)
print("")

for x in sensors_ip:
    req_temp = "http://"+x+"/temperature"
    req_hum = "http://"+x+"/humidity"
    print(sensors_ip[x])
    print("Temp:",req.get(req_temp).text,"F")
    print("Humidity",req.get(req_hum).text,"%")
    print("")

