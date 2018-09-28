import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
#fruits = pd.read_table('fruit_data_with_colors.txt')
#print(fruits.head())
#print(fruits['fruit_name'].unique())
#print(fruits.describe())

irisdataset = sns.load_dataset('iris')
#print(irisdataset.shape)
print (irisdataset.head())
print(irisdataset.describe())
print(irisdataset['species'].unique())


sns.countplot(x='species',data=irisdataset)
plt.show()

from sklearn.svm import SVC

X = irisdataset[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = irisdataset['species']
X_train, X_test, y_train, y_test = train_test_split(X, y)

svm = SVC()
#print (X_test, y_test)

svm.fit(X_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))