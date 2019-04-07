# Generating the analytics images
# Modules
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Main:
    graphData = pd.read_csv('analytics.csv')
    temp = graphData['Temp']
    humidity = graphData['Humid']
    Status = graphData['Status']

    @staticmethod
    def main():
        Main.createImageOne()
        Main.createImageTwo()

    @staticmethod
    def createImageOne():
        """Using Matplotlib"""
        plt.scatter(Main.humidity, Main.temp, edgecolors='face', alpha=0.5)
        plt.xlabel('Humidity')
        plt.ylabel('Temp')
        plt.title('Temperature vs Humidity')
        plt.show()

    @staticmethod
    def createImageTwo():
        """Using Seaborn"""
        sns.swarmplot(x='Temp', y='Status', data=Main.graphData)
        plt.show()


Main.main()
