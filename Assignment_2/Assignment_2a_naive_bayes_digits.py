# -*- coding: utf-8 -*-
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn import metrics 
import seaborn as sns
import pandas as pd


digits = load_digits()
#dig = pd.DataFrame(digits.data)
# plot the digits: each image is 8x8 pixels
#print (dig.head())
y=digits.target
sns.countplot(y)

print (len(digits.data))

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# split the data into training and validation sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

# train the model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# use the model to predict the labels of the test data
y_pred = gnb.predict(X_test)


print("Gaussian Naive Bayes model accuracy:", metrics.accuracy_score(y_test, y_pred))



