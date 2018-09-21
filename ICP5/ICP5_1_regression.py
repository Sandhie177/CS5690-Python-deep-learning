#importing libraries
import csv
import numpy as np
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



get_data('ICP5_1.csv')  # calling get_data method by passing the csv file to it

#getting the maximum and minimum values of x-axix
min_a= min(*A)-2
max_a= max(*A)+2

#finding the mean of A and B
mean_a = np.mean(A)
mean_b = np.mean(B)

# Total number of values
m = len(A)

# Using the formula to calculate b1 and b2
numer = 0
denom = 0

#loop for the equation
for i in range(m):
    numer += (A[i] - mean_a) * (B[i] - mean_b)
    denom += (A[i] - mean_a) ** 2
b1 = numer / denom
b0 = mean_b - (b1 * mean_a)

# Print coefficients
#print(b1, b0)

x = np.linspace(min_a, max_a, 1000)
y = b0 + b1 * x

plt.scatter(A, B, color='red')
plt.plot(x, y,color='green') #calling show_plot to show the graph


