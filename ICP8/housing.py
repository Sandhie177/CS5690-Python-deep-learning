import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv("boston.csv", header=None).values

# print(dataset)
import numpy as np
#splitting dataset into testing and training set
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:13], dataset[:,13],
                                                    test_size=0.25, random_state=87)
#creating a random number seed
np.random.seed(155)
my_first_nn = Sequential() # create sequential neural network model
my_first_nn.add(Dense(32, input_dim=13, activation='relu')) # 1st hidden layer with dimension 13
my_first_nn.add(Dense(64, activation='relu')) #2nd layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='mean_squared_error', optimizer='adam') #compilation is done for mean squared error
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=20, verbose=0,
                                     initial_epoch=0) #data fitting

print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))
