#!/usr/bin/env python3
import requests as req
from datetime import datetime
now = datetime.now()
 
date_string = now.strftime("%m-%d-%Y")
time_string = now.strftime("%H:%M:%S")

sensors_dns = {
    "https://temp-outside.rtynerlabs.io":"outside",
    "https://temp-server.rtynerlabs.io":"server",
    "https://temp-inside.rtynerlabs.io":"inside",
}

print(date_string)
print(time_string)
print("")
for x in sensors_dns:
    req_temp = x+"/temperature"
    req_hum = x+"/humidity"
    print(sensors_dns[x])
    print("Temp:",req.get(req_temp).text,"F")
    print("Humidity",req.get(req_hum).text,"%")
    print("")