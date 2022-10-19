#!/usr/bin/env python3
import requests as req
from datetime import datetime
now = datetime.now()
 
date_string = now.strftime("%m-%d-%Y")
time_string = now.strftime("%H:%M:%S")

out_temp_get = req.get("http://192.168.5.250/temperature")
out_humidity_get = req.get("http://192.168.5.250/humidity")

bed_temp_get = req.get("http://192.168.5.251/temperature")
bed_humidity_get = req.get("http://192.168.5.251/humidity")

living_temp_get = req.get("http://192.168.5.252/temperature")
living_humidity_get = req.get("http://192.168.5.252/humidity")

print(date_string)
print(time_string)
print("Outside:",out_temp_get.text,"F")
print("Outside:",out_humidity_get.text,"%")
print("Bedroom:",bed_temp_get.text,"F")
print("Bedroom:",bed_humidity_get.text,"%")
print("Living Room:",living_temp_get.text,"F")
print("Living Room:",living_humidity_get.text,"%")
#print("home_outside")

