### Generating the report.csv
## Modules
import csv
import pandas as pd
import sqlite3
# Connecting to the Database
#conn = sqlite3.connect('weather.db')

# Reading a CSV file with Pandas Module
""" df = pd.read_csv('report.csv')
print(df) """

# Reading a CSV file with Pandas and formatting names
df = pd.read_csv('report.csv', index_col=['Date'], names=["Date","Status"], header=0, parse_dates=['Date'])
print(df)

# Reading a already created CSV file with Python CSV Module, this also formats the data
""" with open('report.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t Date: {row[0]}, Status: {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.') """