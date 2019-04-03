import sqlite3
dbname='/home/pi/Documents/PIoTA1/weather.db'

class view:
	def displayData():
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	print ("\nEntire database contents:\n")
	for row in curs.execute("SELECT * FROM SenseHat_data"):
		print (row)
	conn.close()
	
view.displayData()