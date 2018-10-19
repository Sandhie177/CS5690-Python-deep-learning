import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv("diabetes.csv", header=None).values

# print(dataset)
import numpy as np
#splitting dataset into testing and training set
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8],
                                                    test_size=0.25, random_state=87)
#creating a random number seed
np.random.seed(155)
my_first_nn = Sequential() # create sequential neural network model
my_first_nn.add(Dense(32, input_dim=8, activation='relu')) # 1st hidden layer with dimension 8
my_first_nn.add(Dense(64, activation='relu')) # 2nd hidden layer 
my_first_nn.add(Dense(128, activation='relu')) # 3rd hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer 
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam') #compilation is done
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0) #data fitting

print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))
