#!/usr/bin/env python3

from bluetooth import *
from pprint import pprint
from pushbullet import Pushbullet
import sense_hat, json, shlex
import subprocess as sp

sense = sense_hat.SenseHat()
pb = Pushbullet("o.KFPP3JCPriu5ydbOQYan1jqCSSP3jia6")

class btsearch:
	def search():
		target_address = None
		print("Searching for paired Bluetooth device")
		filter = '(?<=\()[^\)]+'
		p1 = sp.Popen(["bt-device", "-l"], stdout=sp.PIPE, close_fds=True)
		p2 = sp.Popen(["grep", "-oP", filter], stdin=p1.stdout, stdout=sp.PIPE, close_fds=True, universal_newlines=True)
		data = p2.stdout.readlines()
		
		while target_address is None:
			for macadr in data:
				search = macadr.rstrip("\n")
				nearby_devices = discover_devices(lookup_names = True)
				for bdaddr, bname in nearby_devices:
					if search == bdaddr:
						target_name = bname
						target_address = bdaddr
						break

		if target_address is not None:
			print("Found target Bluetooth device {} with address {}".format(target_name, target_address))
			return True
		else:
			print("Could not find target Bluetooth device nearby")
			return False

class weather:
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

class notification:
	def send_notif(temp, humid):
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
		
		push = pb.push_note("Bluetooth Weather Report", msgbody)
		print("Notification sent")

def main():
	if (btsearch.search()):
		temp = weather.getTemp()
		humid = weather.getHumid()
		notification.send_notif(temp, humid)
	
main()