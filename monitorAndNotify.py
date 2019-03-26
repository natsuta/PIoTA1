import sense_hat, datetime, sqlite3
dbname='weather.db'

sense = sense_hat.SenseHat()
currentDT = datetime.datetime.now()
temp = sense.get_temperature()
humid = sense.get_humidity()

print("Date: " + currentDT.strftime("%Y/%m/%d"))
print("Time: " + currentDT.strftime("%H:%M:%S"))
print("Temperature: " + (string) temp)
print("Humidity: " + humidity)