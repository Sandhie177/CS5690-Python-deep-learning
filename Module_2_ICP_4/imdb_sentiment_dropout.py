#importing libraries
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Activation, Dense, Embedding, SimpleRNN, Dropout
from keras import backend as K
from keras.callbacks import TensorBoard, EarlyStopping, ModelCheckpoint
#from keras_tqdm import TQDMNotebookCallback
#from keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
#from keras.callbacks import TensorBoard
from keras.preprocessing.text import Tokenizer
from time import time

#reading file
imdb_df = pd.read_csv('./labeledTrainData.tsv', sep = '\t')
pd.set_option('display.max_colwidth', 500)

num_words = 10000
tokenizer = Tokenizer(num_words = num_words) #tokenizing
tokenizer.fit_on_texts( imdb_df.review )
sequences = tokenizer.texts_to_sequences(imdb_df.review)
y = np.array(imdb_df.sentiment)
print(y)
from keras.preprocessing.sequence import pad_sequences

max_review_length = 552

pad = 'pre'

X = pad_sequences(sequences,
                  max_review_length,
                  padding=pad,
                  truncating=pad)
#splitting testing and training data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size = 0.2)
input_shape = X_train.shape
K.clear_session()
#defining model
rnn_model = Sequential()
# We specify the maximum input length to our Embedding layer
# so we can later flatten the embedded inputs

rnn_model.add(Embedding(num_words,
                        8,
                        input_length=max_review_length))

rnn_model.add(SimpleRNN(32))
#adding dropout layer
rnn_model.add(Dropout(0.1))
rnn_model.add(Dense(32))
rnn_model.add(Dense(1))
rnn_model.add(Activation('sigmoid'))
rnn_model.summary()
#compiling model
rnn_model.compile(optimizer="adam",
              loss='binary_crossentropy',
              metrics=['accuracy'])
#visualizing in tensor board
tensorboard=TensorBoard(log_dir="logs_dimension/{}".format(time())) #tensorboard declaration to visualize plot

rnn_history = rnn_model.fit(X_train,
                            y_train,
                            epochs=10,
                            batch_size=32,
                            validation_split=0.3,
                            callbacks=[tensorboard])
