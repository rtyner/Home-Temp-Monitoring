#!/usr/bin/env python3
from sqlite3 import Error
import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('../data/database.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the TEMP table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS temp")
 
# Creating table
table = """ CREATE TABLE temp (
            Date CHAR(25),
            Time CHAR(25),
            Sensor CHAR(25),
            Temperature INT,
            Humiditiy INT
        ); """
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()
