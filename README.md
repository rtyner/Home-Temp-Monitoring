# Home-Temp-Monitoring
esp8266, dht22, python3 script to pull date, add to db, and dashboard to view

# Getting Started
## Hardware
- esp8266 -> micro controller w/wifi
- dht22 -> temperature and humidity monitor
- USB cable -> power
- USB brick -> to power sensor

## Software 
- Arduino IDE: Arch Linux ``sudo pacman -S arduino``
- Download: Download and copy to $HOME/Arduino/library/ESPAsyncWebServer/
- ESPAsyncTCP: Download and copy to $HOME/Arduino/library/
- Adafruit_Sensor: Arduino IDE: ``Sketch -> Download Libraries``
- ESP8266: Arduino IDE: File -> Preferences -> Additional Board Manager URLs: ``http://arduino.esp8266.com/stable/package_esp8266com_index.json``

## Configure the ESP8266
- Load the appropriate ino into the Arduino IDE, connect the esp8266, ensure it shows up in ``Tools -> Board``, then click ``Sketch -> Verify/Compile``. 
- Make sure you update the SSID/Key as required by your network.
- Once validated upload it to the board ``Sketch -> Upload``. INO files can be found in the arduino folder within this repository. 
- Disconnect the unit from power. Wire up the dht22 sensors as per the following:

## Wiring
DHT22 back:
- Left: negative -> esp8266 gnd
- Middle: out -> esp8266 d1
- Right: positive -> esp8266 3v3

# Networking
- Go to your router and set dhcp static for the new mac address on the network. In my case see below.
- For DNS, using nginxproxymanager to forward the domain name to the internal IP.
- Using UptimeKuma to monitor the IP to see if any go down. 

| Sensor | IP | DNS |
|---|---|---|
| Outside | 10.2.2.103| https://temp-outside.blurer.net|
| Bedroom | 10.2.2.100| https://temp-bedroom.blurer.net|
| LivingRoom | 10.2.2.102| https://temp-livingroom.blurer.net|
| Kitchen | 10.2.2.101| https://temp-kitchen.blurer.net|
| VM | 10.2.2.10| https://tempmon.blurer.net|

# VM Setup
I am using Debian 11 to run this. On Proxmox set the following:

```
host: vm102
hostname: tempmon.blurer.net
dns: 10.1.1.10, 10.1.1.11
vcpu: 1v
mem: 0.5g
hdd: 32g
ip: 10.2.2.10
```

# Python - createdb.py
- Execute this python script to create the sqlite3 db. To be used later. 

# Python - CurrentTemps.py
- Need to document, but this is the current output:

```
[Running] /usr/bin/env python3 "/home/bl/dev/Home-Temp-Monitoring/CurrentTemps.py"
10-19-2022
07:05:29
Outside:  55.22  F
Outside:  41.50  %
Bedroom:  62.42  F
Bedroom:  46.20  %
Living Room:  62.42  F
Living Room:  37.50  %
```

### To Do:
- Import the sensor name, date, time, temp, and humidity into the sqlite db. 
- Take the sqlite db and present it via webapp.
- Add logic for high and low tempearture, high and low humidity, heat index, and converting units to celsius
- Setup webapp with the following:
    - Graphs
    - High/low temp
    - High/low humidity
    - Heat index/real feel temp
- Setup api to query the database
- Create docker container
