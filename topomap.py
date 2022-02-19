# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:51:21 2020

@author: LF
"""

import mne
import matplotlib.pyplot as plt
import numpy as np
from mne import read_evokeds
from mne.preprocessing import ICA
import matplotlib.pyplot as plt
import mne
from mne.datasets import sample, fetch_fsaverage
from mne.beamformer import make_lcmv, apply_lcmv

input_fname = r'C:\Users\LF\Desktop\epoch_7.set'
raw = mne.io.read_epochs_eeglab(input_fname)  # 加载.set数据
print(raw.info)
print(raw)
raw.set_channel_types({'IO': 'eog'})
montage = mne.channels.make_standard_montage(kind = 'standard_1005', head_size=0.095)
raw.set_montage(montage,raise_if_subset=False)
layout_from_raw = mne.channels.make_eeg_layout(raw.info)
layout_from_raw.plot()
#eog_events = mne.preprocessing.find_eog_events(raw, ch_name='IO')
ica = ICA(n_components=10, random_state=97)#,method = 'FastICA'
ica.fit(raw)
ica.plot_sources(raw)
ica.plot_components()
ica.exclude = [1]
ica.apply(raw)
#data,times=raw[:]
#print(data)
#print(mne.events_from_annotations(raw))
evoked = raw.average()
print(evoked)
evoked.plot(time_unit='s')
evoked.plot_topomap(times=np.array([0.0, 0.30, 0.4,0.60, 0.70]),
                    time_unit='s')