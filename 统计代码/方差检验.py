# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:10:40 2021

@author: LF
"""

import numpy as np

X_Num = int(input('请输入X的数目：'))
X_Avg =float(input('请输入X_Avg：'))
B = float(input('请输入B：'))

X1_Num = int(input('请输入X1的数目：'))
X1_Avg =float(input('请输入X1_Avg：'))
B1 = float(input('请输入B1：'))

X2_Num = int(input('请输入X2的数目：'))
X2_Avg =float(input('请输入X2_Avg：'))
B2 = float(input('请输入B2：'))

X3_Num = int(input('请输入X3的数目：'))
X3_Avg =float(input('请输入X3_Avg：'))
B3 = float(input('请输入B3：'))

X4_Num = int(input('请输入X4的数目：'))
X4_Avg =float(input('请输入X4_Avg：'))
B4 = float(input('请输入B4：'))

X5_Num = int(input('请输入X5的数目：'))
X5_Avg =float(input('请输入X5_Avg：'))
B5 = float(input('请输入B5：'))

SS_out = pow(X1_Avg-X_Avg,2)+pow(X2_Avg-X_Avg,2)+pow(X3_Avg-X_Avg,2)+pow(X4_Avg-X_Avg,2)+pow(X5_Avg-X_Avg,2)
SS_in = (X1_Num-1)*pow(B1,2)+(X2_Num-1)*pow(B2,2)+(X3_Num-1)*pow(B3,2)+(X4_Num-1)*pow(B4,2)+(X5_Num-1)*pow(B5,2)
MS_out = SS_out/4
MS_in= SS_in/X_Num-5
F = MS_out/MS_in
print(F)
