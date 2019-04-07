# Generating the analytics images
# Modules
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
  graphData = pd.read_csv('analytics.csv')
  Date = graphData['Date']
  temp = graphData['Temp']
  plt.scatter(Date, temp, edgecolors='r')
  plt.xlabel('Timestamp')
  plt.ylabel('Temp')
  plt.title('Temperature data from Pi')
  plt.show()

if __name__ == "__main__":
    main()

