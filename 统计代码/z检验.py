# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:57:20 2021

@author: LF
"""

import statsmodels.stats.weightstats as sw
import random
BAV_Num = int(input('BAV数目：'))
BAV_Avr = float(input('BAV均值：'))
BAV_B = float(input('BAV标准差：'))
TAV_Num = int(input('TAV数目：'))
TAV_Avr = float(input('TAV均值：'))
TAV_B = float(input('TAV标准差：'))
arr1 = []
for i in range(0,BAV_Num,1):
    arr1.append(random.gauss(BAV_Avr, BAV_B))
arr2 = []
for j in range(0,TAV_Num,1):
    arr2.append(random.gauss(TAV_Avr, TAV_B))

tstats, pvalue = sw.ztest(arr1, arr2, value=BAV_Avr-TAV_Avr, alternative='two-sided')
print(round(tstats,4), round(pvalue,4))


