#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.execute('SELECT * FROM temp')
results = cursor.fetchall()
print(results)