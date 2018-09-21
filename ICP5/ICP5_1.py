#importing libraries
import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#declaring 2 empty list
A = []
B = []

#function to take the file name as input and get the values inside to impty lists
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            A.append(float(row[0])) #appending A variables
            B.append(float(row[1])) #appending B variables
    return

#function to plot the graph
def show_plot(A, B):
    
    plt.scatter(A, B, color='red')  # plotting the initial datapoints
    plt.plot(A, linear_mod.predict(A), color='blue', linewidth=3)  # plotting the line made by linear regression
    plt.show()
    return


get_data('ICP5_1.csv')  # calling get_data method by passing the csv file to it


linear_mod = linear_model.LinearRegression()
A = np.reshape(A, (len(A), 1))  # converting to matrix of n X 1
B = np.reshape(B, (len(B), 1))
linear_mod.fit(A, B)  # fitting the data points in the model

show_plot(A, B) #calling show_plot to show the graph


