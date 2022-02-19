# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:41:09 2020

@author: LF
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io as scio
from scipy.stats import spearmanr,entropy
#from MEMD_all import memd
from sklearn import metrics 
for samples in range (1, 2, 1):
    data = 'E://FileShare//FileForWork//EEG//lie_eeg//'+ str(samples) +'.mat'
    mat_data = scio.loadmat(data)
    EEG_data = mat_data['EEG']
    #sum_1 = sum_1 + EEG_data
result_1 = EEG_data[:,1]
result_2 = EEG_data[:,4]
plt.plot(result_1)
y = []
x = metrics.homogeneity_score(result_1,result_2)
x1 = metrics.normalized_mutual_info_score(result_1,result_2)
print(x,x1)
#y.append(x)
    

'''
imf = memd(result_1)
imf_x = imf[:,0,:].T #imfs corresponding to 1st component
imf_y = imf[:,1,:].T #imfs corresponding to 2nd component
imf_z = imf[:,2,:].T #imfs corresponding to 3rd component
for column_num in range(0,imf.shape[0]):
    plt.plot(EEG_data[:,0])
    plt.plot(imf_x)
    correlation,p_value = spearmanr(EEG_data[:,1],imf_y[:,column_num])
    print(correlation,p_value)
    if correlation>0.7 and p_value<0.01:
        print('column_num'+str(column_num+1))
'''