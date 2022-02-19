# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:41:47 2020

@author: LF
"""

import mne
import scipy.io as scio
import numpy as np
from tqdm import tqdm
sum_1 = np.zeros((800, 30))
for samples in tqdm(range (1, 301, 1)):
    data = 'E://FileShare//FileForWork//EEG//lie_eeg//'+ str(samples) +'.mat'
    mat_data = scio.loadmat(data)
    data = mat_data['EEG']
    sum_1 = sum_1 + data
data=sum_1/300
data = data.T
n_channels = 30
sampling_freq = 500  # in Hertz
info = mne.create_info(n_channels, sfreq=sampling_freq)
ch_names = ['O2','O1','Oz','Pz','P4','CP4','P8','C4','TP8','T8',
            'P7','P3','CP3','CPz','Cz','FC4','FT8','TP7','C3','FCz',
            'Fz','F4','F8','T7','FT7','FC3','F3','Fp2','F7','Fp1']
ch_types = ['eeg']*30
info = mne.create_info(ch_names, ch_types=ch_types, sfreq=sampling_freq)
#info.set_montage('standard_1005')
info['description'] = 'My custom dataset'
data = data
'''
info = mne.create_info(ch_names=ch_names,
                       ch_types=ch_types,
                       sfreq=sampling_freq)
'''
print(info)
data_EEG = mne.EvokedArray(data, info,tmin=-0.3,nave=5)
montage = mne.channels.make_standard_montage(kind = 'standard_1005', head_size=0.095)
data_EEG.set_montage(montage)
data_EEG.plot_sensors(show_names=True)
data_EEG.plot(unit = False,xlim ='tight')#ylim=dict(eeg=[-5,20])
times = np.linspace(0.0, 1.2, 9)
data_EEG.plot_topomap(ch_type='eeg', times=times, colorbar=True,cmap='Spectral_r')
print(info)