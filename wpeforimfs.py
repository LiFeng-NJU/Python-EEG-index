# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:42:19 2020

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


sum_1 = np.zeros(shape=(800,1))
for samples in range (1, 2, 1):
    data = r'E:/imfs/inn/'+ str(samples)+'_' +'6.mat'
    mat_data = scio.loadmat(data)
    EEG_data = mat_data['imfs_choose']
    #sum_1 = sum_1 + EEG_data
result_1 = EEG_data.T
#ERP_result = sum_1/300
#result_1 = EEG_data[:,:]

def ERP_image():
    for channel_number in range(0,30,1):
        plt.cla()
        plt.plot(result_1[:,channel_number])
        plt.savefig(str(channel_number)+'_lie_25.png', dpi=400, bbox_inches='tight')
    return (print('ERP图像已经处理完毕'))

def weighted_ordinal_patterns(ts, embdim, embdelay):
    time_series = ts
    possible_permutations = list(itertools.permutations(range(embdim)))
    temp_list = list()
    wop = list()
    for i in range(len(time_series) - embdelay * (embdim - 1)):
        Xi = time_series[i:(embdim+i)]
        Xn = time_series[(i+embdim-1): (i+embdim+embdim-1)]
        Xi_mean = np.mean(Xi)
        Xi_var = (Xi-Xi_mean)**2
        weight = np.mean(Xi_var)
        sorted_index_array = list(np.argsort(Xi))
        temp_list.append([''.join(map(str, sorted_index_array)), weight])
    result = pd.DataFrame(temp_list,columns=['pattern','weights'])
    freqlst = dict(result['pattern'].value_counts())
    for pat in (result['pattern'].unique()):
        wop.append(np.sum(result.loc[result['pattern']==pat,'weights'].values))
    return(wop)
    
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
    return((s_entropy(p)/max_entropy))

def calculate():
    for channel_number in range(0,1,1):
        PESerial = list()
        for zeros in range (0,50,1):
            PESerial.append(0)
        for TimeWindows in range(0,750,1):
            ts = result_1[TimeWindows:TimeWindows+50,channel_number]
            OrdinalPatternsSerial = weighted_ordinal_patterns(ts, 5, 1)
            #print(OrdinalPatternsSerial)
            #ShannonEntropy = s_entropy(OrdinalPatternsSerial)
            PE = p_entropy(OrdinalPatternsSerial) 
            if math.isnan(PE):
                PE = 0
            PESerial.append(PE)
        #print(PESerial)
        plt.cla()
        plt.ylim(-0.2,1)
        plt.plot(PESerial)
        plt.savefig(str(channel_number)+'lie_25_WPE.png', dpi=400)
    
#ERP_image()
a = calculate()