#!/usr/bin/env python3
import requests as req
from datetime import datetime
now = datetime.now()
 
date_string = now.strftime("%m-%d-%Y")
time_string = now.strftime("%H:%M:%S")

