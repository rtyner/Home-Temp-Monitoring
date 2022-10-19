#!/usr/bin/env python3
from sqlite3 import Error
import sqlite3


# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('/home/bl/dev/temp_to_db/temp.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the TEMP table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS TEMP")
 
# Creating table
table = """ CREATE TABLE TEMP (
            Date CHAR(25) NOT NULL,
            Time CHAR(25) NOT NULL,
            Temperature INT,
            Humiditiy INT
        ); """
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()