#Implement Support Vector Machine classification:
#a. Apply SVC with kernel“poly” degree =4
#b. Apply SVC with “rbf”kernel
#c. change gamma and C parameters in the model to see how the result may changed. 

#importing libraries
from sklearn import datasets, metrics
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

#loading "digits" data set
digits = datasets.load_digits()

# split the data into training and validation sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

#taking the kernel name as input
kernel_name=eval(input('What is the kernel you want to use? Enter "1" for "Linear", "2" for "Poly" and "3" for "rbf"'))
r=10 #defining random state as 10

#loop for linear kernel
if (kernel_name==1):
    print ('kernel_name=Linear') 
    #using linear kernel as support vector machine
    svm = SVC(kernel='linear', random_state=r, C=1)
    #fitting the model with the train data
    svm.fit(X_train, y_train)
    #changing "C" parameters within the range of 0 to 10
    C_range = range(1, 10)
    scores = [] #defining empty list
    
    for c in C_range: #loop to perform linear kernel with different C value
        svm = SVC(kernel='linear', random_state=r, C=c)
        svm.fit(X_train, y_train)
        y_pred=svm.predict(X_test) #predicting y value with respect to given X value
        scores.append(metrics.accuracy_score(y_test, y_pred)) #appending the different accuracies 
#plotting graph
    plt.plot(C_range, scores) 
    plt.xlabel("value of C")
    plt.ylabel("testing accuracy")
    plt.show()

#loop for Poly kernel
if (kernel_name==2):
    print ('kernel_name=Poly')
    #using Poly kernel as support vector machine
    svm = SVC(kernel='poly', random_state=r, degree=4)
    #fitting the model with the train data
    svm.fit(X_train, y_train)
    #changing "degree" parameter within the range of 0 to 10
    degree_range = range(1, 10)
    scores = [] #defining empty list
    
    for d in degree_range: #loop to perform Poly kernel with different degree value
        svm = SVC(kernel='poly', random_state=r, degree=d)
        svm.fit(X_train, y_train)
        y_pred=svm.predict(X_test) #predicting y value with respect to given X value
        scores.append(metrics.accuracy_score(y_test, y_pred)) #appending the different accuracies
#plotting graph
    plt.plot(degree_range, scores) 
    plt.xlabel("value of degree")
    plt.ylabel("testing accuracy")
    plt.show()

#loop for rbf kernel
if (kernel_name==3):
    print ('kernel_name=rbf')
    #using rbf kernel as support vector machine
    svm = SVC(kernel='rbf', random_state=r, gamma=1, C=1)
    #fitting the model with the train data
    svm.fit(X_train, y_train)
    #changing "gamma" parameter within the range of 0 to 10
    gamma_range = range(1, 10)
    scores = [] #defining empty list
    
    for g in gamma_range: #loop to perform rbf kernel with different degree value
        svm = SVC(kernel='rbf', random_state=r, gamma=g, C=1)
        svm.fit(X_train, y_train)
        y_pred=svm.predict(X_test) #predicting y value with respect to given X value
        scores.append(metrics.accuracy_score(y_test, y_pred)) #appending the different accuracies
#plotting graph
    plt.plot(gamma_range, scores) 
    plt.xlabel("value of gamma")
    plt.ylabel("testing accuracy")
    plt.show()


#printing the accuracy for train and test data set
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))
