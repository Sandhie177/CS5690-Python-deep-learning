#importing libraries
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
from keras import metrics
from keras import regularizers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.optimizers import Adam, RMSprop
from keras.callbacks import TensorBoard, EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
from time import time

df = pd.read_csv('boston.csv') #reading file
boston_data = pd.DataFrame(df, columns=[
        'CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PT','B','LSTAT','MV']) #reading input data
label_col = 'price' #output data
print(boston_data.describe()) #printing the description of the data

#splitting into testing and training data set
boston_x_train, boston_x_valid, boston_y_train, boston_y_valid = train_test_split(boston_data.iloc[:,0:13], boston_data.iloc[:,13],
                                                    test_size=0.3, random_state=87)
np.random.seed(155)
#function to return maximum, minimum, mean and deviation
def norm_stats(df1, df2):
    dfs = df1.append(df2)
    minimum = np.min(dfs)
    maximum = np.max(dfs)
    mu = np.mean(dfs)
    sigma = np.std(dfs)
    return (minimum, maximum, mu, sigma)
#function to normalization
def z_score(col, stats):
    m, M, mu, s = stats
    df2 = pd.DataFrame()
    for c in col.columns:
        df2[c] = (col[c]-mu[c])/s[c]
    return df2
stats = norm_stats(boston_x_train, boston_x_valid)
arr_x_train = np.array(z_score(boston_x_train, stats))
arr_y_train = np.array(boston_y_train)
arr_x_valid = np.array(z_score(boston_x_valid, stats))
arr_y_valid = np.array(boston_y_valid)
print('Training shape:', arr_x_train.shape)
print('ddd',arr_y_train.shape)
print('Training samples: ', arr_x_train.shape[0])
print('Validation samples: ', arr_x_valid.shape[0])

#function for modelling
def basic_model_1(x_size, y_size):
    t_model = Sequential() #create model
    t_model.add(Dense(100, input_shape=(x_size,), activation='relu', kernel_regularizer=None)) #input layer
    t_model.add(Dense(50, activation="relu")) #hidden layer
    t_model.add(Dense(y_size)) #output layer
    print(t_model.summary()) 
    t_model.compile(loss='mean_squared_error', 
        optimizer=RMSprop(lr=0.001),
        metrics=[metrics.mae]) #compile model
    return(t_model)
    
#function for plotting the loss
def plot_history(history):
    loss_list = [s for s in history.history.keys() if 'loss' in s and 'val' not in s]
    val_loss_list = [s for s in history.history.keys() if 'loss' in s and 'val' in s]

    if len(loss_list) == 0:
        print('Loss is missing in history')
        return 
    ## As loss always exists
    epochs = range(1,len(history.history[loss_list[0]]) + 1)
    ## Loss
    plt.figure(1)
    for l in loss_list:
        plt.plot(epochs, history.history[l], 'b', label='Training loss (' + str(str(format(history.history[l][-1],'.5f'))+')'))
    for l in val_loss_list:
        plt.plot(epochs, history.history[l], 'g', label='Validation loss (' + str(str(format(history.history[l][-1],'.5f'))+')'))
    
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    
model = basic_model_1(arr_x_train.shape[1], 1) #declaring model
model.summary()
epochs = 200 #declaring epochs
batch_size =256 #declaring batch size
tensorboard=TensorBoard(log_dir="logs/{}".format(time())) #tensorboard declaration to visualize plot
history = model.fit(arr_x_train, arr_y_train, #model fitting
    batch_size=batch_size,
    epochs=epochs,
    shuffle=True,
    verbose=0, # Change it to 2, if wished to observe execution
    validation_data=(arr_x_valid, arr_y_valid),
    callbacks=[tensorboard])

train_score = model.evaluate(arr_x_train, arr_y_train, verbose=0) #evaluating model for training
valid_score = model.evaluate(arr_x_valid, arr_y_valid, verbose=0) #evaluating model for testing

print('Train MAE: ', round(train_score[1], 4), ', Train Loss: ', round(train_score[0], 4))
print('Val MAE: ', round(valid_score[1], 4), ', Val Loss: ', round(valid_score[0], 4))
plot_history(history)