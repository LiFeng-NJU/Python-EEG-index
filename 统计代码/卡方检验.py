# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:48:12 2021

@author: LF
"""

import numpy as np
from scipy.stats import chi2_contingency
d = np.array([[22,0],[7,17]])
a = chi2_contingency(d)
'''
Total_Num = float(input('请输入总人数：'))
Total_Man = float(input('请输入总男性数：'))
Total_WoMan = Total_Num - Total_Man

Northeast_Num = float(input('请输入总Northeast人数：'))
Northeast_Man = float(input('请输入总Northeast男性数：'))
Northeast_WoMan = Northeast_Num - Northeast_Man

Northwest_Num = float(input('请输入总Northwest人数：'))
Northwest_Man = float(input('请输入总Northwest男性数：'))
Northwest_WoMan = Northwest_Num - Northwest_Man

Southwest_Num = float(input('请输入总Southwest人数：'))
Southwest_Man = float(input('请输入总Southwest男性数：'))
Southwest_WoMan = Southwest_Num - Southwest_Man

Centralsouth_Num = float(input('请输入总Central-south人数：'))
Centralsouth_Man = float(input('请输入总Central-south男性数：'))
Centralsouth_WoMan = Centralsouth_Num - Centralsouth_Man

Centraleast_Num = float(input('请输入总Central-east人数：'))
Centraleast_Man = float(input('请输入总Central-east男性数：'))
Centraleast_WoMan = Centraleast_Num - Centraleast_Man



d = np.array([[Northeast_Man,Northwest_Man,Southwest_Man,Centralsouth_Man,Centraleast_Man], 
              [Northeast_WoMan, Northwest_WoMan, Southwest_WoMan,Centralsouth_WoMan,Centraleast_WoMan]])
d = np.array([111,19,830,81,89],[63,8,0,54,0,1])
a = chi2_contingency(d)
print(a[1])
'''
'''
d = np.array([[Southwest_Man,Centralsouth_Man,Centraleast_Man], 
              [Southwest_WoMan,Centralsouth_WoMan,Centraleast_WoMan]])
a = chi2_contingency(d)
print(a[1])
'''
