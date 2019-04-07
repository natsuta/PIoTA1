import sqlite3
import sys
con = sqlite3.connect('weather.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, humid NUMERIC)")
