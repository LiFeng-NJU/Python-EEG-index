# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:05:09 2020

@author: LF
"""
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import regularizers
import keras
from sklearn import preprocessing 
from sklearn.model_selection import KFold
num_classes = 2
df = pd.read_excel(r'C:\Users\LF\Desktop\11.xlsx')
x = np.array(df) 
print(x.shape)
end = 1923
x_data = x[:,0:end-1]
print(x_data.shape)
y_data = x[:,end-1:end]
print(y_data.shape)
seed = 6
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

for train, test in kfold.split(x_data, y_train_num):
    model = Sequential()
    model.add(Dense(16, input_shape=(1922,),kernel_regularizer=regularizers.l1(0.001),activation='relu'))
    model.add(Dropout(0.01))
    model.add(Dense(16, input_shape=(1922,),kernel_regularizer=regularizers.l1(0.001),activation='relu'))
    model.add(Dropout(0.01))
    model.add(Dense(4, kernel_regularizer=regularizers.l1(0.001),activation='relu'))
    model.add(Dropout(0.01))
    model.add(Dense(2, activation='sigmoid'))
    model.compile(optimizer='SGD',loss='binary_crossentropy',metrics=['accuracy'])
    model.summary()
    model.fit(x_data[train],y_train_num[train], epochs=500, batch_size=32,verbose=1)
    scores = model.evaluate(x_data[test], y_train_num[test], verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)
print(cvscores)
print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))
