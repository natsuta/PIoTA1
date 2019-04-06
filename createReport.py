# Generating the report.csv
# Modules
import csv
import pandas as pd
import sqlite3
import json
import time

# Loading the JSON Variables into memory to perform status operation
JSONFilename = input(
    "Enter Config File Name (if config.json press enter): ") or 'config.json'
JSONFilename + '.json'
with open(JSONFilename, 'r') as json_file:
    data = json.load(json_file)

# Connecting to a Database and reading data using Pandas, then creating a data frame
conn = sqlite3.connect("weather.db")
dataframe = pd.read_sql_query("SELECT * FROM SENSEHAT_data", conn)
# Creating an iterable series to have a dynamic Status
status = pd.Series([])
for i in range(len(dataframe)):
    if dataframe["temp"][i] >= data["max_temperature"]:
        status[i] = "BAD" + ':' + ' ' + 'Temperature is High'
    elif dataframe["temp"][i] <= data["min_temperature"]:
        status[i]="BAD" + ':' + ' ' + 'Temperature is Low'
    elif dataframe["humid"][i] >= data["max_humidity"]:
        status[i]="BAD" + ':' + ' ' + 'Humidity is High'
    elif dataframe["humid"][i] <= data["min_humidity"]:
        status="BAD" + ':' + ' ' + 'Temperature is Low'
    else:
        status[i]="OK: " + ' ' + 'Readings are Normal'
# Inserting Status & Message Column
dataframe.insert(3, 'Status', status)
# Optional user generated file name
filename = input('Enter a filename (click enter to keep default): ') + '.csv' or 'report.csv' 
# File Creation
dataframe.to_csv(filename, index=0)
print("Creating Report...")
time.sleep(0.5)
print("Report Created, Name: " + filename)
# print(dataframe)
conn.close()



