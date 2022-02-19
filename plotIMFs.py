# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:08:05 2020

@author: LF
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.load('./EMD/lie_imfs3.npy')
y = x.T
shape = y.shape[1]
print(y.shape[1])
for i in range(0,shape,1):
    z = y[:,i]
    plt.cla()
    plt.plot(z)
    plt.savefig(str(i)+'test3.png', dpi=600, bbox_inches='tight')

