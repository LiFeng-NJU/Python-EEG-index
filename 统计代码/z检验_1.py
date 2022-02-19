# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:46:58 2021

@author: LF
"""

import numpy as np
from scipy import stats

BAV_Num = int(input('BAV数目：'))
BAV_Avr = float(input('BAV均值：'))
BAV_B = float(input('BAV标准差：'))
TAV_Num = int(input('TAV数目：'))
TAV_Avr = float(input('TAV均值：'))
TAV_B = float(input('TAV标准差：'))

Avr = abs(BAV_Avr-TAV_Avr)
C1_Num = np.square(BAV_B)/BAV_Num
C2_Num = np.square(TAV_B)/TAV_Num
C = np.sqrt(C1_Num+C2_Num)
Z = Avr/C
print(Z)

Sw = pow(((BAV_Num-1)*pow(BAV_B,2)+(TAV_Num-1)*pow(TAV_B,2))/BAV_Num+TAV_Num-2,0.5)
Se = Sw*pow((1/BAV_Num + 1/TAV_Num),0.5)
T = Avr/ Se
print(T)
print(BAV_Num+TAV_Num-2)