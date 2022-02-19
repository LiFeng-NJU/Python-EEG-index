# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:58:34 2021

@author: LF
"""

import mne
import scipy.io as scio
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from mne.datasets import eegbci
from mne.io import concatenate_raws, read_raw_edf
from mne.time_frequency import tfr_multitaper
from mne.stats import permutation_cluster_1samp_test as pcluster_test
from mne.viz.utils import center_cmap
import mne
from mne.viz import plot_alignment, set_3d_view
#创建一个空矩阵,便于合并操作
zero_ = np.zeros((800, 30))

#将mat数据合并
for samples in tqdm(range (1, 301, 1)):
    data = 'E://FileShare//FileForWork//EEG//lie_eeg//'+ str(samples) +'.mat'
    mat_data = scio.loadmat(data)
    E_data = mat_data['EEG']
    data = E_data
    data = np.concatenate((zero_,data))
    zero_ = data  
    
#去除空矩阵
data_choose = data[800:,:]

#转置矩阵便于mne识别
data= data_choose.T

#设置数据信息
sampling_freq = 500  
ch_names = ['O2','O1','Oz','Pz','P4','CP4','P8','C4','TP8','T8',
                'P7','P3','CP3','CPz','Cz','FC4','FT8','TP7','C3','FCz',
                'Fz','F4','F8','T7','FT7','FC3','F3','Fp2','F7','Fp1']
ch_types = ['eeg']*30 
info = mne.create_info(ch_names=ch_names,ch_types=ch_types,sfreq=sampling_freq)
raw = mne.io.RawArray(data, info)

#设置电极位置
montage = mne.channels.make_standard_montage(kind = 'standard_1005', head_size=0.095)
raw.set_montage(montage)
event_F = np.array([[150,0,1]])
for i in tqdm(range (1, 300, 1)):
    event = np.append(event_F, [[150+800*i,0,1]],axis = 0)
annotations = mne.annotations_from_events(event, sfreq=sampling_freq )
raw.set_annotations(annotations)
print(raw)
print(raw.info)
event_id = 1
raw.plot(events=event,scalings = 'auto', duration=20,proj = False)
'''
epochs = mne.Epochs(raw, event, event_id, -0.3, 1.3, baseline=None, reject = None) 
epochs.plot(n_epochs=1, n_channels=1,)
'''






'''
data = np.reshape(data, (1,data.shape[0],data.shape[1]))
for subjects in tqdm(range (1, 301, 1)):
    n_channels = 30
    sampling_freq = 500  
    ch_names = ['O2','O1','Oz','Pz','P4','CP4','P8','C4','TP8','T8',
                'P7','P3','CP3','CPz','Cz','FC4','FT8','TP7','C3','FCz',
                'Fz','F4','F8','T7','FT7','FC3','F3','Fp2','F7','Fp1']
    ch_types = ['eeg']*30  
    info = mne.create_info(ch_names,ch_types ,
                           500)
    info['description'] = 'My custom dataset'  
    print(info)
    data_epochs = data[1,30*(subjects-1):30*subjects,:]
    data_EEG = mne.EpochsArray(data_epochs, info, tmin=-0.3)
    montage = mne.channels.make_standard_montage(kind = 'standard_1005', head_size=0.095)
    data_EEG.set_montage(montage)
'''