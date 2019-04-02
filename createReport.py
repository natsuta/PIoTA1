#Generating the report.csv
import csv

csvData = [['Temperature', 'Humidity', 'Status'],['25.1', '30.9', 'OK']['45.1', '90.9', 'BAD']]

with open('person.csv', 'w', ) as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()