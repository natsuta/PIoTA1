#!/usr/bin/env python3

import sense_hat
import datetime
import time
import sqlite3
import json
from pushbullet import Pushbullet
dbname = '/home/pi/Documents/PIoTA1/weather.db'
sense = sense_hat.SenseHat()

class weather:
    # get data from SenseHat
    def getTemp():
        print("Getting temperature from Sense HAT")
        temp = sense.get_temperature()
        temp = round(temp, 1)
        return temp

    def getHumid():
        print("Getting humidity from Sense HAT")
        humid = sense.get_humidity()
        humid = round(humid, 1)
        return humid

# Prints out the information for confirmation purposes
    def printData(temp, humid):
        currentDT = datetime.datetime.now()
        print("Date: " + currentDT.strftime("%Y/%m/%d"))
        print("Time: " + currentDT.strftime("%H:%M:%S"))
        print("Temperature: {}".format(temp))
        print("Humidity: {}".format(humid))

class database:
    # log data into database
    def logData(temp, humid):
        conn = sqlite3.connect(dbname)
        curs = conn.cursor()
        curs.execute("INSERT INTO SENSEHAT_data values(datetime('now', 'localtime'), (?), (?))", \
		(temp, humid))
        conn.commit()
        conn.close()

    # display data from database
    def displayData():
        conn = sqlite3.connect(dbname)
        curs = conn.cursor()
        print ("\nEntire database contents:\n")
        for row in curs.execute("SELECT * FROM SenseHat_data"):
            print(row)
        conn.close()

class notification:
    def check(temp, humid):
        with open('config.json', 'r') as json_file:
            data = json.load(json_file)
            # if temperature of humidity is outside of ranges defined in config.json
            if temp < data['min_temperature'] or temp > data['max_temperature'] \
			or humid < data["min_humidity"] or humid > data["max_humidity"]:
                conn = sqlite3.connect(dbname)
                curs = conn.cursor()
                # if statement should be != for once a day sending, use == for testing
                if curs.execute("SELECT date('now')") != curs.execute("SELECT timestamp FROM SenseHat_data"):
                    conn.close()
                    return True
                conn.close()

    def send_notif(temp, humid):
        pb = Pushbullet("o.KFPP3JCPriu5ydbOQYan1jqCSSP3jia6")
        line1 = "Temperature: {}".format(temp)
        line2 = "Humidity: {}".format(humid)
        line3a = "Temperature in optimum range"
        line3b = "Temperature out of optimum range"
        line4a = "Humidity in optimum range"
        line4b = "Humidity out of optimum range"

        msgbody = "{}\n{}".format(line1, line2)

        with open('config.json', 'r') as json_file:
            data = json.load(json_file)
            if temp < data['min_temperature'] or temp > data['max_temperature']:
                msgbody = "{}\n{}".format(msgbody, line3b)
            else:
                msgbody = "{}\n{}".format(msgbody, line3a)

            if humid < data["min_humidity"] or humid > data["max_humidity"]:
                msgbody = "{}\n{}".format(msgbody, line4b)
            else:
                msgbody = "{}\n{}".format(msgbody, line4a)    

        push = pb.push_note("Database Weather Report", msgbody)
        print("Notification sent")

class Main:
    def main():
        temp = weather.getTemp()
        humid = weather.getHumid()

        weather.printData(temp, humid)
        database.logData(temp, humid)
        database.displayData()

        if (notification.check(temp, humid)):
            notification.send_notif(temp, humid)

Main.main()