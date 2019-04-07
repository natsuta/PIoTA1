# Generating the analytics images
# Modules
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

class Main:
    graphData = pd.read_csv('analytics.csv')
    temp = graphData['Temp']
    humidity = graphData['Humid']
    Status = graphData['Status']

    @staticmethod
    def main():
        print('Generating Images...')
        Main.createImageOne()
        Main.createImageTwo()

    @staticmethod
    def createImageOne():
        """Using Matplotlib"""
        plt_plot = plt.scatter(Main.humidity, Main.temp, edgecolors='face', alpha=0.5)
        plt.xlabel('Humidity'), plt.ylabel('Temp'), plt.title('Temperature vs Humidity')
        fig1 = plt_plot.get_figure()
        fig1.savefig('Image1.png', bbox_inches='tight')

    @staticmethod
    def createImageTwo():
        """Using Seaborn"""
        sns_plot = sns.swarmplot(x='Temp', y='Humid', data=Main.graphData)
        fig2 = sns_plot.get_figure()
        fig2.savefig('Image2.png', bbox_inches='tight')



Main.main()
