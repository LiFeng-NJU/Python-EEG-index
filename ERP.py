# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 01:05:42 2020

@author: LF
"""

import scipy.io as scio
import matplotlib.pyplot as plt
import numpy
sum = numpy.zeros(shape=(800,30))
for i in range (1, 301, 1):
    data = 'E://FileShare//FileForWork//EEG//lie_eeg//'+ str(i) +'.mat'
    data1 = scio.loadmat(data)
    data2 = data1['EEG']
    #print(data2)
    sum = sum + data2
    #print(data3)
plt.figure(figsize=(8,6),dpi=80)
plt.plot(sum)
print(sum.shape)

result = sum/300
for j in range (0,30,1):
    plt.cla()
    a = result[:,j]
    plt.xlim((-200, 1000))
    plt.plot(a, color='blue', linewidth=1.0)
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    plt.savefig('lie'+str(j)+'.png', dpi=600, bbox_inches='tight')
