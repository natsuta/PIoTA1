### Generating the report.csv
## Modules
import csv
import pandas as pd
import sqlite3
# Connecting to the Database - to run uncomment db connections
conn = sqlite3.connect('weather.db')
""" curs = conn.cursor()
curs.execute("select * from SENSEHAT_data")
results = curs.fetchall()
print(results) """
# Connecting to a Database and reading data using Pandas, then creating a data frame
conn = sqlite3.connect("weather.db")
df = pd.read_sql_query("select timestamp from SENSEHAT_data", conn)
#print(df)

export_csv = df.to_csv('report.csv', index=0, header=['Date'])

# Reading a CSV file with Pandas Module
""" df = pd.read_csv('report.csv')
print(df) """

# Reading a CSV file with Pandas and formatting names
""" df = pd.read_csv('reports.csv', index_col=['Date'], names=["Date","Status"], header=0, parse_dates=['Date'])
print(df) """

# Reading a already created CSV file with Python CSV Module, this also formats the data
""" with open('report.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:git
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t Date: {row[0]}, Status: {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.') """

conn.close()
#curs.close()
