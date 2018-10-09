#Pick any dataset from the dataset sheet in the class sheeta. 
#plot how many of each category is available in your dataset
#create one prediction model based on Naïve Bayes Classification and evaluate your model

#importing libraries
from sklearn.datasets import load_digits
from sklearn import metrics 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

#loading "digits" data set
digits = load_digits()

y=digits.target
sns.countplot(y)
plt.show()
print ("a) Ploting the number of each catergories")
#print (len(digits.data))

# split the data into training and validation sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

# train the model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# use the model to predict the labels of the test data
y_pred = gnb.predict(X_test)

print("Gaussian Naive Bayes model accuracy:", metrics.accuracy_score(y_test, y_pred))



