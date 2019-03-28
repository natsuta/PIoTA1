from bluetooth import *
from pprint import pprint
from pushbullet import Pushbullet
import sense_hat

sense = sense_hat.SenseHat()
pb = Pushbullet("o.KFPP3JCPriu5ydbOQYan1jqCSSP3jia6")
target_name = "Galaxy A8 (2018)"

def getData():
	temp = sense.get_temperature()
	humid = sense.get_humidity()
	
	temp = round(temp, 1)
	humid = round(humid, 1)
	
	search(target_name)
	send_notif(temp, humid)
	
def search(target_name):
	target_address = None
	while target_address is None:
		nearby_devices = discover_devices(lookup_names = True)
		for bdaddr, bname in nearby_devices:
			if target_name == bname:
				target_address = bdaddr
				break

	if target_address is not None:
		print("found target bluetooth device with address", target_address)
	else:
		print("could not find target bluetooth device nearby")

def send_notif(temp, humid):
	minTemp = 20
	maxTemp = 30
	minHumid = 50
	maxHumid = 60
	
	line1 = "Temperature: {}".format(temp)
	line2 = "Humidity: {}".format(humid)
	line3a = "Temperature in optimum range"
	line3b = "Temperature out of optimum range"
	line4a = "Humidity in optimum range"
	line4b = "Humidity out of optimum range"
	
	msgbody = "{}\n{}".format(line1, line2)
	
	if temp < minTemp or temp > maxTemp:
		msgbody = "{}\n{}".format(msgbody, line3b)
	else:
		msgbody = "{}\n{}".format(msgbody, line3a)
		
	if humid < minHumid or humid > maxHumid:
		msgbody = "{}\n{}".format(msgbody, line4b)
	else:
		msgbody = "{}\n{}".format(msgbody, line4a)	
	
	push = pb.push_note("Weather Report", msgbody)

def main():
	getData()
	
main()