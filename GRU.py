# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:49:33 2020

@author: LF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout,Dense, GRU, Masking
from keras import regularizers
import keras
#from sklearn import preprocessing 
from sklearn.model_selection import KFold
num_classes = 2
end = 1923
seed = 6
timesteps = 1
df = pd.read_excel(r'C:\Users\LF\Desktop\11.xlsx')
x = np.array(df) 
print(x.shape)
x_data = x[:,0:end-1]
print(x_data.shape)
#print(x_data)
x_data = np.reshape(x_data, (x_data.shape[0], 62, 31))
#print(x_data)
print(x_data.shape)
y_data = x[:,end-1:end]
print(y_data.shape)
'''    
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(-1, 1))
x_minMax = min_max_scaler.fit_transform(x_data)
x_train_num = x_minMax
print(x_train_num)
training_data = np.hstack((x_train_num, y_data))
'''

kfold = KFold(n_splits=12,  shuffle=True, random_state=seed)
y_train_num = keras.utils.to_categorical(y_data, num_classes)
cvscores = []
mean_cvscores = []
 
for i in range(0,62):
    x_data[:,i,:] = 0.
    for train, test in kfold.split(x_data, y_train_num):
        model = Sequential()
        model.add(Masking(mask_value=0., input_shape=(62, 31)))
        model.add(LSTM(32, input_shape = (62, 31), return_sequences=True))
        model.add(LSTM(32, return_sequences=True))
        model.add(LSTM(32))
        model.add(LSTM(8))
        model.add(Dense(2, activation='softmax'))
        model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])
        model.summary()
        history = model.fit(x_data[train],y_train_num[train], epochs=200, batch_size=16,verbose=1)
        scores = model.evaluate(x_data[test], y_train_num[test], verbose=0)
        #plt.plot(history.history['loss'])
        #plt.plot(history.history['accuracy'])
        #plt.legend()
        #plt.show()
        print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        cvscores.append(scores[1] * 100)
    print(cvscores)
    print("%.2f%% (+/- %.2f%%) %.2f%%" % (np.mean(cvscores), np.std(cvscores), np.var(cvscores)))
    mean_cvscores.append(np.mean(cvscores))
