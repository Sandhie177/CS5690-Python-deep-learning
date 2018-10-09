#Report your views on the k nearest neighbor algorithm when we change the K how it will affect the accuracy.

#importing libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

# Loading the "digits" dataset
digits = datasets.load_digits()

# getting the data and response of the dataset
X,y=digits.data, digits.target
# split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#taking 5 neighboring elements for classification
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train) #fitting training set into model
#predicting y values with respect to X test values
y_pred = model.predict(X_test)
#printing accuracy of the model
print('the accuracy of the model for k value = 5 is: ', metrics.accuracy_score(y_test, y_pred))

#changing neighbor element numbers in range of 0 to 50
k_range = range(1, 50)
scores = [] #defining empty list

for k in k_range: #loop for each neighbor element number
    #taking k neighboring elements for classification
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train) #fitting training set into model
    y_pred = knn.predict(X_test) #predicting y values with respect to X test values
    scores.append(metrics.accuracy_score(y_test, y_pred)) #appending the accuracy values in the list
#plotting graph
plt.plot(k_range, scores) 
plt.xlabel("value of k")
plt.ylabel("testing accuracy")
plt.show()

