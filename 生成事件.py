# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:02:38 2021

@author: LF
"""
import numpy as np
from tqdm import tqdm
event = np.array([[149,0,1]])
for i in tqdm(range (1, 300, 1)):
    event = np.append(event, [[149+300*i,0,1]],axis = 0)