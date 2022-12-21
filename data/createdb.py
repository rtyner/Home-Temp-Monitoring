#!/usr/bin/env python3
from sqlite3 import Error
import sqlite3

# Connecting to sqlite
# connection object
<<<<<<< HEAD:data/createdb.py
<<<<<<< HEAD:db/createdb.py
connection_obj = sqlite3.connect('../data/database.db')
=======
connection_obj = sqlite3.connect('database.db')
>>>>>>> c5e9a625483a89ae0e70a774f97cfd1823a8e991:data/createdb.py
=======
connection_obj = sqlite3.connect('../data/database.db')
>>>>>>> 377375c74b14d59b18ecc1a3795ce74207d54b52:db/createdb.py
 
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
