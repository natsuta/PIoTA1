import sense_hat, datetime, time, sqlite3, json
from pushbullet import Pushbullet
dbname='weather.db'
sense = sense_hat.SenseHat()

# get data from SenseHat
def getData():
	currentDT = datetime.datetime.now()
	temp = sense.get_temperature()
	humid = sense.get_humidity()
	
	if temp is not None and humid is not None:
		temp = round(temp, 1)
		humid = round(humid, 1)
		printData(currentDT, temp, humid)
		logData(temp, humid)

# Prints out the information for confirmation purposes
def printData(currentDT, temp, humid):
	print("Date: " + currentDT.strftime("%Y/%m/%d"))
	print("Time: " + currentDT.strftime("%H:%M:%S"))
	print("Temperature: {}".format(temp))
	print("Humidity: {}".format(humid))

# log data into database
def logData(temp, humid):
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?), (?))", (temp, humid))
	with open('config.json', 'r') as json_file:
		data = json.load(json_file)
		# if temperature of humidity is outside of ranges defined in config.json
		if temp < data['min_temperature'] or temp > data['max_temperature'] or humid < data["min_humidity"] or humid > data["max_humidity"]:
			# if statement should be != for once a day sending, use == for testing
			if curs.execute("SELECT date('now')") != curs.execute("SELECT timestamp FROM SenseHat_data"):
				send_notif(temp, humid)
	conn.commit()
	conn.close()

# display data from database
def displayData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print (row)
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
	
	push = pb.push_note("Weather Report", msgbody)
	print("Notification sent")


def main():
	getData()
	displayData()
	
main()