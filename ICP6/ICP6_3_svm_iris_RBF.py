#importing libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

#Load the iris dataset
irisdatasets = datasets.load_iris()
#Loading all the features in X value
X = irisdatasets.data
#Loading the feature names in y value
y = irisdatasets.target

#Declaring train and data set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#Using rbf kernel as Support Vector machine
svm = SVC(kernel='rbf', random_state=0, gamma=1, C=1)
#fitting the model with train data
svm.fit(X_train, y_train)

#calculating accuracy for train data set and test data set
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))

