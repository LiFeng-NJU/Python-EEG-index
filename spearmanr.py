# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:23:51 2020

@author: LF
"""

from scipy.stats import spearmanr
import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt 
data = 'E://FileShare//FileForWork//EEG//lie_eeg//'+ str(1) +'.mat'
data1 = scio.loadmat(data)
data2 = data1['EEG']
result = data2[0:800,7]
plt.plot(result)

x = np.load('E:\PyEMD\PyEMD\Test_lie_1_imfs_channel_0.npy')
y = x.T
plt.plot(y[:,1])
num = y.shape[1]
for channel in range(0,num,1):
    pccs = spearmanr(result, y[:,channel])
    print(pccs)
