### Generating the report.csv
## Modules
import csv
import pandas as pd
import sqlite3
   
# Connecting to a Database and reading data using Pandas, then creating a data frame
conn = sqlite3.connect("weather.db")
dataframe = pd.read_sql_query("SELECT * FROM SENSEHAT_data", conn)
filename = input('Enter a filename (click enter to keep default): ') + '.csv' or 'report.csv'
status = pd.Series([])
for i in range(len(dataframe)):
    if dataframe["temp"][i] >= 30:
        status[i]="BAD"
    elif dataframe["temp"][i] <= 20:
        status[i]="BAD"
    elif dataframe["humid"] >= 60:
        status[i]="BAD"
    elif dataframe["humid"] <= 50:
        status="BAD"
    else:
        status[i]="OK"

dataframe.insert(3, 'Status', status)
dataframe.to_csv(filename, date_format='%s', index=0)
print(dataframe)
conn.close()



