# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:09:33 2021

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

print(__doc__)
sum_1 = np.zeros((800, 30))
for samples in tqdm(range (1, 301, 1)):
    data = 'E://FileShare//FileForWork//EEG//inn_eeg//'+ str(samples) +'.mat'
    mat_data = scio.loadmat(data)
    data = mat_data['EEG']
    #sum_1 = sum_1 + data
#data=sum_1/300
data = data.T
n_channels = 30
sampling_freq = 500  
info = mne.create_info(n_channels, sfreq=sampling_freq)
print(info)
ch_names = ['O2','O1','Oz','Pz','P4','CP4','P8','C4','TP8','T8',
            'P7','P3','CP3','CPz','Cz','FC4','FT8','TP7','C3','FCz',
            'Fz','F4','F8','T7','FT7','FC3','F3','Fp2','F7','Fp1']
ch_types = ['eeg']*30
info = mne.create_info(ch_names, ch_types=ch_types, sfreq=sampling_freq)
info['description'] = 'My custom dataset'
data = data
info = mne.create_info(ch_names=ch_names,
                       ch_types=ch_types,
                       sfreq=sampling_freq)
data_EEG = mne.EvokedArray(data, info,tmin=-0.3,nave=5)
montage = mne.channels.make_standard_montage(kind = 'standard_1005', head_size=0.095)
data_EEG.set_montage(montage)
#画3D电极图
'''
data_path = mne.datasets.sample.data_path()
subjects_dir = data_path + '/subjects'
trans = mne.read_trans(data_path + '/MEG/sample/sample_audvis_raw-trans.fif')
fig = plot_alignment(data_EEG.info, trans, subject='sample', dig=False,
                     eeg=['original', 'projected'], meg=[],
                     coord_frame='head', subjects_dir=subjects_dir)
set_3d_view(figure=fig, azimuth=135, elevation=80)
'''
#ERDS
freqs = np.arange(4, 8, 1)
n_cycles = freqs
vmin, vmax = -1, 1.5  # set min and max ERDS values in plot
cmap = center_cmap(plt.cm.RdBu, vmin, vmax) 
baseline = [-0.3, 0]  # baseline interval (in s)
kwargs = dict(n_permutations=100, step_down_p=0.05, seed=1,
              buffer_size=None, out_type='mask')
tfr = tfr_multitaper(data_EEG, freqs=freqs, n_cycles=n_cycles,
                     use_fft=True, return_itc=False, average=False,
                     decim=1)
tmin, tmax = 0, 0.1
tfr.crop(tmin, tmax)
tfr.apply_baseline(baseline, mode="percent")
for ch in range(3,5,1):
    tfr.average().plot([ch], vmin=vmin, vmax=vmax, cmap=(cmap, False),
                       colorbar=False, show=False)
    plt.show()
