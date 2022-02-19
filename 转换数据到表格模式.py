# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:07:21 2020

@author: LF
"""

import numpy as np
import pandas as pd
kk = []
x_data_1 = np.load('./inn_200-500.npy')
for k in range(0,300,1):
    for z in range(0,30,1):
        x_data_1_1 = np.append(x_data_1[k,z,:],0)
        print(x_data_1_1.shape)
        kk = np.concatenate((kk,x_data_1_1),axis=0)
kkk = kk.reshape(9000,301)
df = pd.DataFrame(kkk)
df.to_excel('0.xlsx') 