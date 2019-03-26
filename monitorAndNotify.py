import sense_hat, datetime, time, sqlite3
dbname='weather.db'
sense = sense_hat.SenseHat()

# get data from SenseHat
def getData():
	currentDT = datetime.datetime.now()
	temp = sense.get_temperature()
	humid = sense.get_humidity()
	
	if temp is not None and humid is not None:
		printData(currentDT, temp, humid)
		logData(currentDT, temp, humid)

# Prints out the information for confirmation purposes
def printData(currentDT, temp, humid):
	print("Date: " + currentDT.strftime("%Y/%m/%d"))
	print("Time: " + currentDT.strftime("%H:%M:%S"))
	print("Temperature: " + (string) temp)
	print("Humidity: " + humid)

# log data into database
def logData(currentDT, temp, humid):
	conn=sqlite3.connect(dbname)
	    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?))", (temp,))
    conn.commit()
    conn.close()
	
def main():
	getData()
	