"""
    includes all the configuration and some constants.

"""

# global random_state, norm_flg, test_size

"""
   Step 1.  random control in order to achieve reproductive results

    cited from https://stackoverflow.com/questions/54047654/tensorflow-different-results-with-the-same-random-seed
"""

# Seed value
# Apparently you may use different seed values at each stage
random_state = 42

# 1. Set the `PYTHONHASHSEED` environment variable at a fixed value
import os

os.environ['PYTHONHASHSEED'] = str(random_state)

# 2. Set the `python` built-in pseudo-random generator at a fixed value
import random

random.seed(random_state)

# 3. Set the `numpy` pseudo-random generator at a fixed value
import numpy as np

np.random.seed(random_state)

"""
    Step 2. 
"""
import sys

sys.stdout.flush()
# out_file = 'stdout_content.txt'
# # sys.stdout = open(out_file, mode='w', buffering=1)
# ###skip 'buffering' if you don't want the output to be flushed right away after written
# # sys.stdout = sys.__stdout__
#
import functools

print = functools.partial(print, flush=True)

"""
    Step 3. 
"""
# input_dir = "input_data/CICIDS2017"
# output_dir = "output_data"
# # norm_flg = True  # normlize the data.
# norm_method = 'std'  # 'min-max' or 'std' or 'robust'; None: without normalization
# gridsearch_flg = True  # grid_search_flg
# data_aug = False
# # test_size = 0.3
# show_flg = True  # plot the results
# title_flg = True  # if the figures have the title or not.
# verbose = True

#
# params = {}
# params['expt_name'] = 'indv_data'
# params['feat_set_lst'] = ['iat_set', 'fft_set']
# params['ipt_dir'] = "input_data"  # ipt_dir
# params['opt_dir'] = "output_data"  # opt_dir
# # norm_flg = True  # normlize the data.
# params['norm_method'] = 'std'  # 'min-max' or 'std' or 'robust'; None: without normalization
# params['grid_search_lst'] = [True, False]  # grid_search_flg
# params['q_fixed_iat'] = 0.9
# params['q_sampling_rate'] = 0.9
# params['sampling_method'] = 'rate'
# params['data_aug'] = False
# # test_size = 0.3
# params['show_flg'] = True  # plot the results
# params['title_flg'] = True  # if the figures have the title or not.
# params['verbose'] = True
# params['overwrite'] = True
# params['random_state'] = random_state


class Parameter:
    def __init__(self, random_state=random_state, **kwargs):
        self.params = {}
        self.params['random_state'] = random_state

        for i, (key, value) in enumerate(kwargs.items()):
            if key == 'dataset_name':
                dataset_name = value
            self.params[key] = value
        self.params['subflow_flg'] = False  # default: False (using flow to get features)
        self.params['subflow_interval'] = 0.1  # 0.1s as subflow duration (window)
        self.params['ipt_dir'] = f"input_data/{dataset_name}"  # ipt_dir
        self.params['norm_method'] = 'std'
        self.params['opt_dir'] = "output_data"  # opt_dir
        # norm_flg = True  # normlize the data.
        self.params['norm_method'] = 'std'  # 'min-max' or 'std' or 'robust'; None: without normalization
        # self.params['gridsearch_lst'] = [True, False]  # grid_search_flg
        self.params['q_fixed_iat'] = 0.9
        # self.params['q_sampling_rate'] = 0.9
        self.params['sampling_method'] = 'rate'
        # test_size = 0.3
        self.params['show_flg'] = True  # plot the results
        self.params['title_flg'] = True  # if the figures have the title or not.
        self.params['verbose'] = True
        self.params['overwrite'] = True
