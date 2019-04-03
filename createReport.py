### Generating the report.csv
## Modules
import csv, pandas as pd, sqlite3, json
   
# Connecting to a Database and reading data using Pandas, then creating a data frame
conn = sqlite3.connect("weather.db")
dataframe = pd.read_sql_query("SELECT * FROM SENSEHAT_data", conn)
filename = input('Enter a filename (click enter to keep default): ') + '.csv' or 'report.csv'

with open('config.json', 'r') as json_file:
		data = json.load(json_file) 
    
print(data["max_temperature"])

status = pd.Series([])
for i in range(len(dataframe)):
    if dataframe["temp"][i] >= data["max_temperature"]:
        status[i]="BAD" + ':' + ' ' + 'Temperature is High'
    elif dataframe["temp"][i] <= data["min_temperature"]:
        status[i]="BAD" + ':' + ' ' + 'Temperature is Low'
    elif dataframe["humid"] >= data["max_humidity"]:
        status[i]="BAD" + ':' + ' ' + 'Humidity is High'
    elif dataframe["humid"] <= data["min_humidity"]:
        status="BAD" + ':' + ' ' + 'Temperature is Low'
    else:
        status[i]="OK"

dataframe.insert(3, 'Status', status)
#dataframe.insert(4, 'Message', message)
dataframe.to_csv(filename, date_format='%s', index=0)
#print(dataframe)
conn.close()



