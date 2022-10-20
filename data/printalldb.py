#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('/home/bl/dev/Home-Temp-Monitoring/data/database.db')
cursor = conn.execute('SELECT * FROM temp')
results = cursor.fetchall()
print(results)