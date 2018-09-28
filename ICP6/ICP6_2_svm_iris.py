#importing library file
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.svm import SVC


#loading iris dataset
irisdataset = sns.load_dataset('iris')

#printing the 1st five data
print (irisdataset.head())
#printing the description of the data
print(irisdataset.describe())
#shows the name of the species by uniqueifying
print(irisdataset['species'].unique())

#counts members under each species
sns.countplot(x='species',data=irisdataset)
plt.show()

#taking the values of different variables
X = irisdataset[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = irisdataset['species']

#splitting the dataset into train data and test data
X_train, X_test, y_train, y_test = train_test_split(X, y)

#using linear kernel as support vector machine
svm = SVC(kernel='linear', random_state=0, C=1)
#fitting the model with the train data
svm.fit(X_train, y_train)

#printing the accuracy for train and test data set
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))


