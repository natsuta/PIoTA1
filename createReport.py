# Generating the report.csv
# Modules
import csv
import pandas as pd
import sqlite3
import json
import time
import numpy as np
from datetime import datetime


def main():
    try:  # In case of file being deleted, will error handle
        # Loading the JSON Variables into memory to perform status operation
        JSONFilename = 'config.json'
        with open(JSONFilename, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print("File: " + "'" + JSONFilename + "'" +
              " \nDoes not exist in the file directory. ")
        exit()

    # Connecting to a Database and reading data using Pandas, then creating a data frame
    conn = sqlite3.connect("weather.db")
    dataframe = pd.read_sql_query("SELECT * FROM SENSEHAT_data", conn)
    # Creating an iterable series to have a dynamic Status and message applied.
    # Temperature and Humidity are set in config.
    status = pd.Series([])
    for i in range(len(dataframe)):
        if dataframe["temp"][i] >= data["max_temperature"]:
            status[i] = " BAD" + ':' + ' ' + 'Temperature is High'
        elif dataframe["temp"][i] <= data["min_temperature"]:
            status[i] = " BAD" + ':' + ' ' + 'Temperature is Low'
        elif dataframe["humid"][i] >= data["max_humidity"]:
            status[i] = " BAD" + ':' + ' ' + 'Humidity is High'
        elif dataframe["humid"][i] <= data["min_humidity"]:
            status = " BAD" + ':' + ' ' + 'Temperature is Low'
        else:
            status[i] = " OK: " + ' ' + 'Readings are Normal'
    # Inserting Status & Message Column
    dataframe.insert(3, 'Status', status)
    # Formatting Dataframe for final output
    # Dropping the temperature and humidity data, comment this to keep them in the report
    dataframe = dataframe.drop(["temp", "humid"], axis=1)
    dataframe = dataframe.rename(columns={'timestamp':'Date'})
    dataframe = dataframe.rename(columns=str.title)
    # Creating the CSV with all the dataframe changes
    # Optional user generated file name
    filename = input(
        'Enter a filename (click enter to keep default)\nAdd .csv to custom name: ') or 'report.csv'
    # File Creation
    dataframe.to_csv(filename, index=0)

    print("Creating Report...")
    time.sleep(0.5)
    print("Report Created \nFilename: " + filename)

    # Closing DB Connection
    conn.close()


# print(dataframe)
if __name__ == "__main__":
    main()
