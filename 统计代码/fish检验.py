# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:13:36 2021

@author: LF
"""
from scipy.stats import fisher_exact,chi2_contingency
'''
A = int(input('BAV总数目：'))
A1 = int(input('BAV数目：'))
A2 = A-A1
B = int(input('TAV总数目：'))
B1 = int(input('TAV数目：'))
B2 = B-B1
'''
stat, p =fisher_exact([[267,230],[412,238]])
a = chi2_contingency([[22,0],[7,17]])
print(p,a)