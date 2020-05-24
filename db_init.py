#!/usr/bin/python3.8

import sqlite3
import os

try:
    os.remove('data.db')
except:
    pass

db = sqlite3.connect('data.db')

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE motion_event
    (
        eventID INTEGER PRIMARY KEY AUTOINCREMENT,
        deviceID INTEGER,
        deviceName TEXT,
        timestamp INTEGER
    );
''')

db.commit()
db.close()