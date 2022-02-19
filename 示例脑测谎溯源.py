# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 00:34:15 2020

@author: LF
"""
import mne
import os
import os.path as op
from mne.datasets import  fetch_fsaverage
from mne.preprocessing import ICA

#MRI数据成像示例
fs_dir = fetch_fsaverage(verbose=True)
subjects_dir = op.dirname(fs_dir)
subject = 'fsaverage'
trans = 'fsaverage'
src = op.join(fs_dir, 'bem', 'fsaverage-ico-5-src.fif')
bem = op.join(fs_dir, 'bem', 'fsaverage-5120-5120-5120-bem-sol.fif')

sample_data_folder = r'E:\FileShare\FileForWork\2020测谎\EEGDatas\2 张锦佳\测谎'
sample_data_raw_file = os.path.join(sample_data_folder, 'zjj_3.vhdr')
raw = mne.io.read_raw_brainvision(sample_data_raw_file, preload=True)
print(raw.info)
raw.set_channel_types({'IO': 'eog'})
original_bads = raw.info['bads']
raw.info['bads'].append('TP9')
raw.info['bads'].append('TP10')
montage = mne.channels.make_standard_montage(kind = 'standard_1020', head_size=0.095)
raw.set_montage(montage)
raw.plot_sensors(show_names=True)
raw.set_eeg_reference(ref_channels='average',projection=True)#ref_channels=['TP9','TP10'])
raw.filter(l_freq=1,h_freq=30)
#mne.set_eeg_reference(raw, ref_channels=['TP9','TP10'], projection=False, ch_type='eeg')
eog_events = mne.preprocessing.find_eog_events(raw, ch_name='IO')
ica = ICA(n_components=61, random_state=36)#,method = 'FastICA'
ica.fit(raw)
plot_components = ica.plot_components()
#ica.plot_scores(plot_components)
#ica.exclude = []
# find which ICs match the EOG pattern
#eog_indices, eog_scores = ica.find_bads_eog(raw,threshold =1.5)
#ica.exclude = eog_indices
ica.exclude = [0, 1]
ica.apply(raw)

tmin, tmax = -0.3, 1
custom_mapping = {'Stimulus/S  5': 5}#, 'Stimulus/S 32':32, 'Stimulus/S 48':48
(events,event_id) = mne.events_from_annotations(raw, event_id=custom_mapping)
#print(events,event_id)

epochs = mne.Epochs(raw, events, event_id, tmin = tmin,  tmax = tmax,
                    baseline=(-0.3, 0), preload=True)
#epochs.plot(picks='Cz')




cov = mne.compute_covariance(epochs, tmax=0.,method='auto',rank=None)

evoked = epochs.average()
#evoked.add_proj(mne.compute_proj_evoked(evoked.copy().crop(tmax=0)))
#evoked.apply_proj()
mne.preprocessing.fix_stim_artifact(evoked)
evoked.shift_time(-0.004)
evoked.plot(picks='Pz')
print(evoked.info)

white = (1.0, 1.0, 1.0)
coord_frame = 'mri'
fig = mne.viz.create_3d_figure(size=(600, 400), bgcolor=white)
fig = mne.viz.plot_alignment(raw.info, src=src, eeg=['original'], 
                             trans=trans,show_axes=True, mri_fiducials=True,
                             dig='fiducials',
                             surfaces='white',coord_frame='head',fig=fig)#, 'projected'
fwd = mne.make_forward_solution(raw.info, trans=trans, src=src,
                                bem=bem, eeg=True, mindist=5.0, n_jobs=1)
#print(fwd)

#mne.viz.set_3d_view(figure=fig, azimuth=180, distance=0.25)
eeg_map = mne.sensitivity_map(fwd, ch_type='eeg', mode='fixed')
#eeg_map.plot(time_label='EEG sensitivity', subjects_dir=subjects_dir,clim=dict(lims=[5, 50, 100]))

inv = mne.minimum_norm.make_inverse_operator(evoked.info, fwd, cov, verbose=True)
stc = mne.minimum_norm.apply_inverse(evoked, inv)
print(stc)
stc.plot(subjects_dir=subjects_dir, initial_time=0.0,hemi='both', views='auto',
         surface='white',size=(600, 400))
stc.plot(mode='stat_map')
'''
fwd = mne.make_forward_solution(evoked.info, trans=trans,src=src, 
                                bem=bem, verbose=True)
inv = mne.minimum_norm.make_inverse_operator(evoked.info, fwd, cov_reg, verbose=True)
stc = mne.minimum_norm.apply_inverse(evoked, inv)
stc.plot(subjects_dir=subjects_dir, 
         initial_time=0.0,
         hemi='both',  views='coronal')
'''