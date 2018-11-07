from __future__ import print_function
import numpy as np
import pandas as pd
import keras
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.regularizers import L1L2
from keras.models import Sequential
from keras.callbacks import TensorBoard, EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
from time import time

# load dataset
dataset = pd.read_csv("diabetes.csv", header=None).values
#splitting dataset into testing and training set
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8],test_size=0.25, random_state=87)
#function for modelling
def basic_model_1(x_size, y_size):
    my_first_nn = Sequential() # create sequential neural network model
    my_first_nn.add(Dense(32, input_dim=8, activation='relu', kernel_regularizer=L1L2(l1=0.0,l2=0.1))) # 1st hidden layer with dimension 8
    my_first_nn.add(Dense(64, activation='relu')) # 2nd hidden layer 
    my_first_nn.add(Dense(128, activation='relu')) # 3rd hidden layer
    my_first_nn.add(Dense(1, activation='sigmoid')) # output layer 
    my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')
    return(my_first_nn)

np.random.seed(155) #creating a random number seed    
model = basic_model_1(8, 1) #declaring model
model.summary()
epochs = 200 #declaring epoch
batch_size =128 #declaring batch size
tensorboard=TensorBoard(log_dir="logs/{}".format(time())) #tensorboard declaration to visualize plot
history = model.fit(X_train, Y_train, #model fitting
    batch_size=batch_size,
    epochs=epochs,
    shuffle=True,
    verbose=0, # Change it to 2, if wished to observe execution
    validation_data=(X_test, Y_test),
    callbacks=[tensorboard])
train_score = model.evaluate(X_train, Y_train, verbose=0) #evaluating model for training
valid_score = model.evaluate(X_test, Y_test, verbose=0) #evaluating model for testing
print('Train accuracy: ', train_score)
print('Test accuracy: ', valid_score) #compilation is done

