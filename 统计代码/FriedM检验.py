# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:42:41 2021

@author: LF
"""
import scipy.stats as stats
a = stats.friedmanchisquare([0,0,175,9,1],
                            [0,0,206,25,6],
                            [0,0,184,33,74],
                            [0,0,19,1,12]
                            )
print(a)
