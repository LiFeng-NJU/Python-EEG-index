# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:36:27 2020

@author: LF
"""
import mne
import mne_nirs
from mne.channels import read_custom_montage
import numpy 
a = [[-0.5878,0.809,0],
     [-0.6149,0.7564,0.2206],
     [-0.454,0.891,0],
     [-0.4284,0.875,0.2213],
     [-0.2508,0.9565,0.1438],
     [-0.352,0.8111,0.4658],
     [-0.1857,0.915,0.3558],
     [0,0.8312,0.5554],
     [0,0.9799,0.19490],
     [0.1857,0.915,0.3558],
     [0.2508,0.9565,0.1437],
     [-0.6957,0.1838,0.6933],
     [-0.555,0.0002,0.8306],
     [-0.8311,0.0001,0.5552],
     [-0.6959,-0.1836,0.6936],
     [-0.6109,-0.5259,0.5904],
     [-0.4217,-0.6869,0.5912],
     [-0.6411,-0.6546,0.3985],
     [-0.4537,-0.796,0.3995],
     [0.352,0.8111,0.4658],
     [0.4284,0.875,0.2212],
     [0.6149,0.7564,0.2206],
     [0.454,0.891,0],
     [0.5878,0.809,0],
     [0.6957,0.1838,0.6933],
     [0.8311,0.0001,0.5552],
     [0.555,0.0002,0.8306],
     [0.6959,-0.1836,0.6936],
     [0.6109,-0.5258,0.5904],
     [0.6411,-0.6546,0.3985],
     [0.4216,-0.687,0.5912],
     [0.4537,-0.796,0.3995],
     [0,-0.8306,0.5551],
     [-0.1858,-0.9151,0.3559],
     [0.1859,-0.9151,0.3559],
     [0,-0.9797,0.1949]
     ]
a=numpy.array(a)
print (type(a))
#print (a)
value0 = a[0,:]
value1 = a[1,:]
value2 = a[2,:]
value3 = a[3,:]
value4 = a[4,:]
value5 = a[5,:]
value6 = a[6,:]
value7 = a[7,:]
value8 = a[8,:]
value9 = a[9,:]
value10 = a[10,:]
value11 = a[11,:]
value12 = a[12,:]
value13 = a[13,:]
value14 = a[14,:]
value15 = a[15,:]
value16 = a[16,:]
value17 = a[17,:]
value18 = a[18,:]
value19 = a[19,:]
value20 = a[20,:]
value21 = a[21,:]
value22 = a[22,:]
value22 = a[22,:]
value23 = a[23,:]
value24 = a[24,:]
value25 = a[25,:]
value26 = a[26,:]
value27 = a[27,:]
value28 = a[28,:]
value29 = a[29,:]
value30 = a[30,:]
value31 = a[31,:]
value32 = a[32,:]
value33 = a[33,:]
value34 = a[34,:]
value35 = a[35,:]

c = {'AF7': value0,'AFF5': value1,'AFp7':value2,'AF5h':value3,'AFp3':value4,'AFF3h':value5,
     'AF1':value6,'AFFz':value7,'AFpz':value8,'AF2':value9,'AFp4':value10,
     'FCC3':value11,'C3h':value12,'C5h':value13,'CCP3':value14,'CPP3':value15,
     'P3h':value16,'P5h':value17,'PPO3':value18,'AFF4h':value19,'AF6h':value20,
     'AFF6':value21,'AFp8':value22,'AF8':value23,'FCC4':value24,'C6h':value25,
     'C4h':value26,'CCP4':value27,'CPP4':value28,'P6h':value29,'P4h':value30,
     'PPO4':value31,'PPOz':value32,'PO1':value33,'PO2':value34,'POOz':value35}
print(c)

#montage = read_custom_montage(fname, head_size=0.095, coord_frame='mri')
#ch_pos1 = {'AF7':(-0.587800000000000	0.809000000000000	0),'AFF5':(-0.614900000000000	0.756400000000000	0.220600000000000)}
montage = mne.channels.make_dig_montage(ch_pos = c, coord_frame='head')
#montage = mne.channels.make_standard_montage(kind = 'standard_1005', head_size=0.095)
montage.plot(kind ='topomap',sphere = 1.1)
montage.save('1.locs')
