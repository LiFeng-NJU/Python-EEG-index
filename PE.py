# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 02:05:51 2020

@author: LF
"""

import itertools
import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as scio
import math


sum_1 = np.zeros(shape=(800,30))
for samples in range (1, 301, 1):
    data = 'E://FileShare//FileForWork//EEG//lie_eeg//'+ str(samples) +'.mat'
    mat_data = scio.loadmat(data)
    EEG_data = mat_data['EEG']
    sum_1 = sum_1 + EEG_data
ERP_result = sum_1/300
result_1 = ERP_result[150:550,:]

def ERP_image():
    for channel_number in range(0,30,1):
        plt.cla()
        plt.plot(result_1[:,channel_number])
        plt.savefig(str(channel_number)+'_lie_25.png', dpi=400, bbox_inches='tight')
    return (print('ERP图像已经处理完毕'))

def ordinal_patterns(ts, embdim, embdelay):
    ''' This function computes the ordinal patterns of a time series for a given embedding dimension and embedding delay.
    USAGE: ordinal_patterns(ts, embdim, embdelay)
    ARGS: ts = Numeric vector representing the time series, embdim = embedding dimension (3<=embdim<=7 prefered range), embdelay =  embdding delay
    OUPTUT: A numeric vector representing frequencies of ordinal patterns'''
    time_series = ts
    possible_permutations = list(itertools.permutations(range(embdim)))
    lst = list()
    for i in range(len(time_series) - embdelay * (embdim - 1)):
        sorted_index_array = list(np.argsort(time_series[i:(embdim+i)]))
        lst.append(sorted_index_array)
    lst = np.array(lst)
    element, freq = np.unique(lst, return_counts = True, axis = 0)
    freq = list(freq)
    if len(freq) != len(possible_permutations):
        for i in range(len(possible_permutations)-len(freq)):
            freq.append(0)
        return(freq)
    else:
        return(freq)
    
def s_entropy(freq_list):
    ''' This function computes the shannon entropy of a given frequency distribution.
    USAGE: shannon_entropy(freq_list)
    ARGS: freq_list = Numeric vector representing the frequency distribution
    OUTPUT: A numeric value representing shannon's entropy'''
    freq_list = [element for element in freq_list if element != 0]
    sh_entropy = 0.0
    for freq in freq_list:
        sh_entropy += freq * np.log(freq)
    sh_entropy = -sh_entropy
    return(sh_entropy)

def p_entropy(op):
    ordinal_pat = op
    max_entropy = np.log(len(ordinal_pat))
    p = np.divide(np.array(ordinal_pat), float(sum(ordinal_pat)))
    return(s_entropy(p)/max_entropy)

def calculate():
    for channel_number in range(0,30,1):
        PESerial = []
        for TimeWindows in range(0,350,1):
            ts = result_1[TimeWindows:TimeWindows+25,channel_number]
            OrdinalPatternsSerial = ordinal_patterns(ts, 4, 1)
            #ShannonEntropy = s_entropy(OrdinalPatternsSerial)
            PE = p_entropy(OrdinalPatternsSerial)  
            PESerial.append(PE)
        plt.cla()
        plt.plot(PESerial)
        plt.savefig(str(channel_number)+'lie_25.png', dpi=400, bbox_inches='tight')
#ERP_image()
calculate()