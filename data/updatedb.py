#!/usr/bin/env python3
import sqlite3
import requests
import requests as req

# time stuff
from datetime import datetime
now = datetime.now()   
date_string = now.strftime("%m-%d-%Y")
time_string = now.strftime("%H:%M:%S")

# sensor ip -> name
sensors_ip = {
    "192.168.4.250":"outside",
    "192.168.4.251":"bedroom",
    "192.168.4.252":"living_room",
    "192.168.4.253":"kitchen"
}

connection = sqlite3.connect('database.db')
cur = connection.cursor()

for x in sensors_ip:
    req_temp = "http://"+x+"/temperature"
    req_hum = "http://"+x+"/humidity"
    cur.execute("INSERT INTO temp (Date, Time, Sensor, Temperature, Humiditiy) VALUES (?, ?, ?, ?, ?)",
        (date_string, time_string, sensors_ip[x], req.get(req_temp).text, req.get(req_hum).text))
    print(x,"added..")
connection.commit()
connection.close()