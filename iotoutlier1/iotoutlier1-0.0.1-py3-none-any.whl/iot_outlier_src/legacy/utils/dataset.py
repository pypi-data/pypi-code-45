# Authors: XXX
#
# License : XXX
""" Dataset class

"""
import os
from collections import OrderedDict, Counter
from copy import deepcopy

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler


class Dataset():

    def __init__(self, case='experiment_1', input_dir='',
                 random_state=42):
        self.case = case
        self.input_dir = input_dir
        self.random_state = random_state

        self.dataset_dict, self.num_features = get_dataset(self.input_dir)

    def datasets_stat(self):

        print_dict(self.datasets_dict['train_set_dict'])
        print_dict(self.datasets_dict['val_set_dict'])
        # for idx, (data_key, value_dict) in enumerate(
        #         self.datasets_dict.items()):  # {'train_set_dict': {'SYNT_train_set':,'UNB_train_set':,'MAWI_train_set'}, 'test_set_dict'}
        #     for i, (sub_key, value) in enumerate(value_dict.items()):
        #         print(f'idx:{idx}, {data_key}:{sub_key}, len(value): {len(value)}')
        #         if len(value) == 0:
        #             continue
        #         X = self.datasets_dict[data_key][sub_key]['X']
        #         y = self.datasets_dict[data_key][sub_key]['y']
        #         # v_stat_dict = data_stat(X=X, y=y)
        #         data_stat_pandas(X=X, check_idx=[1, 2], data_name=sub_key)

    def normalize_data(self, norm_method='z-score', train_set_key='SYNT', not_normalized_features_lst=[]):

        train_set_key = train_set_key + '_train_set'
        print(f'\n-normalize {train_set_key} with {norm_method}')

        train_set_dict = self.datasets_dict['train_set_dict']
        val_set_dict = self.datasets_dict['val_set_dict']
        test_set_dict = self.datasets_dict['test_set_dict']

        new_train_set_dict = {}
        new_val_set_dict = {}
        new_test_set_dict = {}

        features_idx = []
        for idx in range(self.num_features):
            if idx not in not_normalized_features_lst:
                features_idx.append(idx)
        print(f'features_idx ({len(features_idx)}) need to be normalized, which are {features_idx},\n'
              f'not_features_idx ({len(not_normalized_features_lst)}) won\'t be normalized, which are {not_normalized_features_lst}.\n'
              f'***not_normalized features will be appended to the normalized features (i.e., after normalization, features\' order will be changed.)')

        X_train = train_set_dict[train_set_key]['X']
        new_X_train, self.scaler = normalize_data_with_sklearn(X_train, scaler='', norm_method=norm_method,
                                                               features_idx=features_idx)
        if norm_method == 'robust':
            # self.scaler.transformers = [('name', StandardScaler(), features_idx)]
            X_train_mu = self.scaler.named_transformers_['scaler'].center_
            X_train_std = self.scaler.named_transformers_[
                'scaler'].scale_  # recommend: self.scale_ = _handle_zeros_in_scale(np.sqrt(self.var_))
            print(
                f'\n-- with {norm_method}, parameters (center and scale) are obtained from {train_set_key},'
                f'which are ,\nX_train_center ({len(X_train_mu)}):{data_print(X_train_mu)},\nX_train_scale ({len(X_train_std)}):{data_print(X_train_std)}')
        elif norm_method == 'min-max':
            X_train_mu = self.scaler.named_transformers_['scaler'].data_min_
            # d_std = np.sqrt(scaler.var_)   # do not use this form, because some var_ will be 0.
            X_train_std = self.scaler.named_transformers_[
                'scaler'].data_max_  # recommend: self.scale_ = _handle_zeros_in_scale(np.sqrt(self.var_))
            print(
                f'\n-- with {norm_method}, parameters (min and max) are obtained from {train_set_key},'
                f'which are ,\nX_train_min ({len(X_train_mu)}):{data_print(X_train_mu)},\nX_train_scale ({len(X_train_std)}):{data_print(X_train_std)}')
        elif norm_method == 'z-score':
            X_train_mu = self.scaler.named_transformers_['scaler'].mean_
            # d_std = np.sqrt(scaler.var_)   # do not use this form, because some var_ will be 0.
            X_train_std = self.scaler.named_transformers_[
                'scaler'].scale_  # recommend: self.scale_ = _handle_zeros_in_scale(np.sqrt(self.var_))
            print(
                f'\n-- with {norm_method}, parameters (mu and std) are obtained from {train_set_key},'
                f'which are ,\nX_train_mu ({len(X_train_mu)}):{data_print(X_train_mu)},\nX_train_std ({len(X_train_std)}):{data_print(X_train_std)}')
        else:
            pass

        before_range = (np.max(X_train, axis=0) - np.min(X_train, axis=0))
        value = list(map('{:.0f}'.format, before_range))  # limit the float to int print.
        value = [float(v) for v in value]
        print(f'before normalization, range_val ({len(value)}): {value}')  # f'{value:{width}.{precision}}'

        after_range = (np.max(new_X_train, axis=0) - np.min(new_X_train, axis=0))
        value = list(map('{:.0f}'.format, after_range))  # limit the float to int print.
        value = [float(v) for v in value]
        print(f'after normalization,  range_val ({len(value)}): {value}')  # f'{value:{width}.{precision}}'

        new_train_set_dict.update({train_set_key: {}})
        new_train_set_dict[train_set_key].update({'X': new_X_train})
        new_train_set_dict[train_set_key]['y'] = train_set_dict[train_set_key]['y']

        for key, value_dict in val_set_dict.items():
            if len(value_dict) == 0:
                continue
            if norm_method == 'robust':
                print(
                    f'\n--normalize {key} with {norm_method} and parameters (center and scale) obtained from {train_set_key},'
                    f'in which,\nX_train_center:{data_print(X_train_mu)},\nX_train_scale:{data_print(X_train_std)}')
            elif norm_method == 'min-max':
                print(
                    f'\n--normalize {key} with {norm_method} and parameters (min and max) obtained from {train_set_key},'
                    f'in which,\nX_train_min:{data_print(X_train_mu)},\nX_train_max:{data_print(X_train_std)}')
            elif norm_method == 'z-score':
                print(
                    f'\n--normalize {key} with {norm_method} and parameters (mu and std) obtained from {train_set_key},'
                    f'in which,\nX_train_mu:{data_print(X_train_mu)},\nX_train_std:{data_print(X_train_std)}')
            else:
                pass
            X_val = value_dict['X']
            new_X_val = self.scaler.transform(X_val)

            before_range = (np.max(X_val, axis=0) - np.min(X_val, axis=0))
            value = list(map('{:.0f}'.format, before_range))  # limit the float to int print.
            value = [float(v) for v in value]
            print(f'before normalization, range_val ({len(value)}): {value}')  # f'{value:{width}.{precision}}'

            after_range = (np.max(new_X_val, axis=0) - np.min(new_X_val, axis=0))
            value = list(map('{:.0f}'.format, after_range))  # limit the float to int print.
            value = [float(v) for v in value]
            print(f'after normalization,  range_val ({len(value)}): {value}')  # f'{value:{width}.{precision}}'

            new_val_set_dict[key] = {}
            new_val_set_dict[key]['X'] = new_X_val
            new_val_set_dict[key]['y'] = value_dict['y']

        for key, value_dict in test_set_dict.items():
            if len(value_dict) == 0:
                continue
            if norm_method == 'robust':
                print(
                    f'\n--normalize {key} with {norm_method} and parameters (center and scale) obtained from {train_set_key},'
                    f'in which,\nX_train_center:{data_print(X_train_mu)},\nX_train_scale:{data_print(X_train_std)}')
            elif norm_method == 'min-max':
                print(
                    f'\n--normalize {key} with {norm_method} and parameters (min and max) obtained from {train_set_key},'
                    f'in which,\nX_train_min:{data_print(X_train_mu)},\nX_train_max:{data_print(X_train_std)}')
            elif norm_method == 'z-score':
                print(
                    f'\n--normalize {key} with {norm_method} and parameters (mu and std) obtained from {train_set_key},'
                    f'in which,\nX_train_mu:{data_print(X_train_mu)},\nX_train_std:{data_print(X_train_std)}')
            else:
                pass
            X_test = value_dict['X']
            new_X_test = self.scaler.transform(X_test)

            before_range = (np.max(X_test, axis=0) - np.min(X_test, axis=0))
            value = list(map('{:.0f}'.format, before_range))  # limit the float to int print.
            value = [float(v) for v in value]
            print(f'before normalization, range_val ({len(value)}): {value}')  # f'{value:{width}.{precision}}'

            after_range = (np.max(new_X_test, axis=0) - np.min(new_X_test, axis=0))
            value = list(map('{:.0f}'.format, after_range))  # limit the float to int print.
            value = [float(v) for v in value]
            print(f'after normalization,  range_val ({len(value)}): {value}')  # f'{value:{width}.{precision}}'

            new_test_set_dict[key] = {}
            new_test_set_dict[key]['X'] = new_X_test
            new_test_set_dict[key]['y'] = value_dict['y']

        self.datasets_dict['train_set_dict'] = new_train_set_dict
        self.datasets_dict['val_set_dict'] = new_val_set_dict
        self.datasets_dict['test_set_dict'] = new_test_set_dict
        # return {'train_set_dict': new_train_set_dict, 'val_set_dict': new_val_set_dict,
        #         'test_set_dict': new_test_set_dict}

    def selected_sub_features(self, features_lst=[]):

        if len(features_lst) > 0:
            for key_set, value_dict in self.datasets_dict.items():
                for sub_key, sub_value in value_dict.items():
                    new_x = select_sub_features_data(sub_value['X'], features_lst)
                    value_dict[sub_key]['X'] = new_x
                    value_dict[sub_key]['y'] = sub_value['y']
            self.num_features = len(features_lst)
            print(f'using selected_features_lst (size={self.num_features}): {features_lst}')
        else:
            num_features = self.num_features
            print(f'using all features: {num_features}')


def discretize_features(features_arr=[]):
    # features=[]
    # for idx, feat in enumerate(features_arr):
    #     if idx

    features = []
    if features_arr[0] == '6':  # 6: tcp
        features.extend([1, 0])  # one hot: tcp and udp
    else:  # features_arr[0] == '17':  # 17: udp
        features.extend([0, 1])

    features.extend(features_arr[1:])

    return features


def load_norm_anomaly_data(input_dir='', data_name='SYNT'):
    label_dict = {'norm': [f'n_{i}' for i in range(10)],
                  'anomaly': [f'a_{i}' for i in range(10)]}  # norm_0, # anomaly_0
    new_norm_dict = []
    new_anomaly_dict = []

    if data_name == 'SYNT':
        ### all norm data, maybe more than norm data
        n_i = 0  # norm index
        input_file = os.path.join(input_dir, "synthetic_dataset/Sess_normal_0.txt")
        norm_dict = load_data_from_txt(input_file=input_file, data_range=(0, 77989), label=label_dict['norm'][n_i])
        if n_i == 0:
            new_norm_dict = norm_dict
        else:
            new_norm_dict['X'] = np.concatenate([new_norm_dict['X'], norm_dict['X']], axis=0)  # concatenate by rows
            new_norm_dict['y'] = np.concatenate([new_norm_dict['y'], norm_dict['y']], axis=0)  # concatenate by rows
        n_i += 1

        ### all anomaly data, maybe more than norm data
        a_i = 0
        input_file = os.path.join(input_dir, "synthetic_dataset/Sess_DDoS_Excessive_GET_POST.txt")
        anomaly_11_dict = load_data_from_txt(input_file=input_file, data_range=(0, 36000),
                                             label=label_dict['anomaly'][a_i])
        new_anomaly_dict = anomaly_11_dict

        a_i += 1

        input_file = os.path.join(input_dir, "synthetic_dataset/Sess_DDoS_Recursive_GET.dms")
        anomaly_12_dict = load_data_from_txt(input_file=input_file, data_range=(0, 37000),
                                             label=label_dict['anomaly'][a_i])
        new_anomaly_dict['X'] = np.concatenate([new_anomaly_dict['X'], anomaly_12_dict['X']],
                                               axis=0)  # concatenate by rows
        new_anomaly_dict['y'] = np.concatenate([new_anomaly_dict['y'], anomaly_12_dict['y']],
                                               axis=0)  # concatenate by rows
        a_i += 1

        input_file = os.path.join(input_dir, "synthetic_dataset/Sess_DDoS_Slow_POST_Two_Arm_HTTP_server_wait.dms")
        anomaly_13_dict = load_data_from_txt(input_file=input_file, data_range=(0, 243),
                                             label=label_dict['anomaly'][a_i])
        new_anomaly_dict['X'] = np.concatenate([new_anomaly_dict['X'], anomaly_13_dict['X']],
                                               axis=0)  # concatenate by rows
        new_anomaly_dict['y'] = np.concatenate([new_anomaly_dict['y'], anomaly_13_dict['y']],
                                               axis=0)  # concatenate by rows
        a_i += 1

        input_file = os.path.join(input_dir, "synthetic_dataset/Sess_DDoS_SlowLoris_Two_Arm_HTTP_server_wait.dms")
        anomaly_14_dict = load_data_from_txt(input_file=input_file, data_range=(0, 1000),
                                             label=label_dict['anomaly'][a_i])
        new_anomaly_dict['X'] = np.concatenate([new_anomaly_dict['X'], anomaly_14_dict['X']],
                                               axis=0)  # concatenate by rows
        new_anomaly_dict['y'] = np.concatenate([new_anomaly_dict['y'], anomaly_14_dict['y']],
                                               axis=0)  # concatenate by rows
        a_i += 1
    elif data_name == 'UNB':
        ### all norm data
        n_i = 0  # norm index
        input_file = os.path.join(input_dir, "unb/Normal_UNB.txt")
        norm_dict = load_data_from_txt(input_file=input_file, data_range=(0, 59832), label=label_dict['norm'][n_i])
        if n_i == 0:
            new_norm_dict = norm_dict
        else:
            new_norm_dict['X'] = np.concatenate([new_norm_dict['X'], norm_dict['X']], axis=0)  # concatenate by rows
            new_norm_dict['y'] = np.concatenate([new_norm_dict['y'], norm_dict['y']], axis=0)  # concatenate by rows
        n_i += 1

        ### all anomaly data
        a_i = 0
        input_file = os.path.join(input_dir, "unb/DoSHulk_UNB.txt")
        anomaly_21_dict = load_data_from_txt(input_file=input_file, data_range=(0, 11530),
                                             label=label_dict['anomaly'][a_i])
        new_anomaly_dict = anomaly_21_dict
        a_i += 1

        input_file = input_file = os.path.join(input_dir, "unb/DOSSlowHttpTest_UNB.txt")
        anomaly_22_dict = load_data_from_txt(input_file=input_file, data_range=(0, 6414),
                                             label=label_dict['anomaly'][a_i])
        new_anomaly_dict['X'] = np.concatenate([new_anomaly_dict['X'], anomaly_22_dict['X']],
                                               axis=0)  # concatenate by rows
        new_anomaly_dict['y'] = np.concatenate([new_anomaly_dict['y'], anomaly_22_dict['y']],
                                               axis=0)  # concatenate by rows
        a_i += 1

        input_file = os.path.join(input_dir, "unb/UNB_DosGoldenEye_UNB_IDS2017.txt")
        anomaly_23_dict = load_data_from_txt(input_file=input_file, data_range=(0, 1268),
                                             label=label_dict['anomaly'][a_i])
        new_anomaly_dict['X'] = np.concatenate([new_anomaly_dict['X'], anomaly_23_dict['X']],
                                               axis=0)  # concatenate by rows
        new_anomaly_dict['y'] = np.concatenate([new_anomaly_dict['y'], anomaly_23_dict['y']],
                                               axis=0)  # concatenate by rows
        a_i += 1

        input_file = input_file = os.path.join(input_dir, "unb/UNB_DoSSlowloris_UNB_IDS2017.txt")
        anomaly_24_dict = load_data_from_txt(input_file=input_file, data_range=(0, 16741),
                                             label=label_dict['anomaly'][a_i])
        new_anomaly_dict['X'] = np.concatenate([new_anomaly_dict['X'], anomaly_24_dict['X']],
                                               axis=0)  # concatenate by rows
        new_anomaly_dict['y'] = np.concatenate([new_anomaly_dict['y'], anomaly_24_dict['y']],
                                               axis=0)  # concatenate by rows
        a_i += 1
    elif data_name == 'MAWI':
        ### all norm data
        n_i = 0
        input_file = os.path.join(input_dir, "mawi/Normal_mawi_day1.txt")
        norm_dict = load_data_from_txt(input_file=input_file, data_range=(0, 62000), label=label_dict['norm'][n_i])
        if n_i == 0:
            new_norm_dict = norm_dict
        else:
            new_norm_dict['X'] = np.concatenate([new_norm_dict['X'], norm_dict['X']], axis=0)  # concatenate by rows
            new_norm_dict['y'] = np.concatenate([new_norm_dict['y'], norm_dict['y']], axis=0)  # concatenate by rows
        n_i += 1
        anomaly_dict_lst = []
    else:
        print('**** other case.')
        return -1

    return new_norm_dict, new_anomaly_dict


def modify_label(datasets_dict, label_dict={'norm': 1, 'anomaly': 0}, old_label_dict={}):
    """

    Args:
        datasets_dict:
        label_dict:
        old_label_dict:  label_dict = {'norm': [f'n_{i}' for i in range(10)], 'anomaly': [f'a_{i}' for i in range(10)]}  # norm_0, # anomaly_0

    Returns:

    """
    new_datasets_dict = deepcopy(datasets_dict)
    for idx, (i_key, i_value) in enumerate(
            new_datasets_dict.items()):  # {'train_set_dict':, 'val_set_dict':, 'test_set_dict':}
        for j, (j_key, j_value) in enumerate(i_value.items()):  # {'SYNT_train_set':{'X':, 'y'}}
            if len(j_value) == 0:
                continue
            for s, y_v in enumerate(j_value['y']):
                if y_v.startswith('n_'):
                    j_value['y'][s] = label_dict['norm']
                elif y_v.startswith('a_'):
                    j_value['y'][s] = label_dict['anomaly']
                else:
                    pass
            j_value['y'] = np.asarray(j_value['y'], dtype=int)  # change str to int

    return new_datasets_dict


def print_params(func):
    pass


def load_data(input_file='', data_range=(0, 100), label=''):
    """

    :param input_file:
    :param data_range: (start, end) = data_range
    :param label:
    :return:
    """
    import pandas as pd
    print(f'input_file: {input_file}, data_range: {data_range}, label: {label}')

    start, end = data_range
    if start >= 0:
        if end >= start:
            end = end
        elif end == -1:
            end = 1000
        else:
            return -1
        df = pd.read_csv(input_file, sep=',', nrows=end, index_col=[i for i in range(start, end)])
    else:
        return -1

    print(f'{df.describe()}')
    X = df.values

    y = [label for i in range(X.shape[0])]
    return X, y


def get_dataset(input_dir='input_dir', label_dict={'normal': 0, 'attack': 1}):
    dataset_dict = {}

    input_files_dict = OrderedDict(
        {'prop_set': {'normal': 'input_data/demo_dataset/proposed_features/normal_demo_dataset_sub.txt',
                      'anomaly': 'input_data/demo_dataset/proposed_features/anomaly_demo_dataset_sub.txt'},
         'trad_set': {'normal': 'input_data/demo_dataset/traditional_features/normal_demo_dataset_sub.txt',
                      'anomaly': 'input_data/demo_dataset/traditional_features/anomaly_demo_dataset_sub.txt'}})

    input_files_dict = OrderedDict(
        {'prop_set': {'normal': 'input_data/IoT_botnet_attacks_N_BaIoT/Danmini_Doorbell/benign_traffic.csv',
                      'anomaly': 'input_data/demo_dataset/proposed_features/anomaly_demo_dataset_sub.txt'},
         'trad_set': {'normal': 'input_data/demo_dataset/traditional_features/normal_demo_dataset_sub.txt',
                      'anomaly': 'input_data/demo_dataset/traditional_features/anomaly_demo_dataset_sub.txt'}})

    gafgyt_normal_input = {
        'benign': 'input_data/IoT_botnet_attacks_N_BaIoT/Danmini_Doorbell/benign_traffic.csv'}  # more than one benign files
    gafgyt_attacks_input = {
        'tcp': 'input_data/IoT_botnet_attacks_N_BaIoT/Danmini_Doorbell/gafgyt_attacks/tcp.csv'}  # more than one attack files

    for i, (key, value) in enumerate(gafgyt_normal_input.items()):
        print(f'i: {i}, key: {key}, value: {value}')
        X, y = load_data(input_file=value, data_range=(0, 100), label=label_dict['normal'])
        if i == 0:
            X_normal = X
            y_normal = y
        else:
            X_normal = np.concatenate([X_normal, X], axis=0)
            y_normal = np.concatenate([y_normal, y], axis=0)

    for i, (key, value) in enumerate(gafgyt_attacks_input.items()):
        print(f'i: {i}, key: {key}, value: {value}')
        X, y = load_data(input_file=value, data_range=(0, 100), label=label_dict['attack'])
        if i == 0:
            X_attack = X
            y_attack = y
        else:
            X_attack = np.concatenate([X_attack, X], axis=0)
            y_attack = np.concatenate([y_attack, y], axis=0)

    dataset = {'normal': {'X': X_normal, 'y': y_normal},
               'attack': {'X': X_attack, 'y': y_attack}}

    normal_dict = {'X': X_normal, 'y': y_normal}
    attack_dict = {'X': X_attack, 'y': y_attack}
    # norm_dict= load_data_from_txt(input_file=input_files_dict['prop_set']['normal'],data_range=(0, 1000), label=label_dict['norm'], discretize_flg=False)
    # anomaly_dict = load_data_from_txt(input_file=input_files_dict['prop_set']['anomaly'], data_range=(0, 1000),
    #                                label=label_dict['anomaly'], discretize_flg=False)

    test_size = 0.3
    random_state = 42
    X_norm_train, X_norm_test, y_norm_train, y_norm_test = train_test_split(normal_dict['X'], normal_dict['y'],
                                                                            test_size=test_size,
                                                                            random_state=random_state)
    X_anomaly_train, X_anomaly_test, y_anomaly_train, y_anomaly_test = train_test_split(attack_dict['X'],
                                                                                        attack_dict['y'],
                                                                                        test_size=test_size,
                                                                                        random_state=random_state)
    X_test = np.concatenate([X_norm_test, X_anomaly_test], axis=0)  # axis =0 means that concatenate by rows
    y_test = np.concatenate([y_norm_test, y_anomaly_test], axis=0)

    train_set_dict = {'X': X_norm_train, 'y': y_norm_train}  # only one train_set
    val_set_dict = {'X': {}, 'y': {}}  # only one val_set
    test_set_dict = {'X': X_test, 'y': y_test}  # more than one test_set
    num_features = train_set_dict['X'].shape[1]

    # dataset_dict = modify_label(dataset_dict, label_dict={'norm': 0, 'anomaly': 1})

    for i, (key, value_dict) in enumerate(dataset_dict.items()):
        if len(value_dict) == 0:
            continue
        print_dict(value_dict)

    dataset_dict = {'train_set_dict': train_set_dict, 'val_set_dict': val_set_dict, 'test_set_dict': test_set_dict}
    return dataset_dict, num_features  # {'train_set_dict':, 'val_set_dict':, 'test_set_dict':}


def load_data_from_txt(input_file, data_range=(0, 100), label=1, discretize_flg=True):
    """
        1) load data from txt
        2) label data
        3) discretize feature if discretize_flg == True.

        features: ts, sip, dip, sport, dport, proto, dura, orig_pks, reply_pks, orig_bytes, reply_bytes, orig_min_pkt_size, orig_max_pkt_size, reply_min_pkt_size, reply_max_pkt_size, orig_min_interval, orig_max_interval, reply_min_interval, reply_max_interval, orig_min_ttl, orig_max_ttl, reply_min_ttl, reply_max_ttl, urg, ack, psh, rst, syn, fin, is_new, state, prev_state
            idx : 0    1    2    3      4      5      6      7         8          9            10            11                 12                  13                  14                       15            16                      17               18                19          20             21           22            23   24   25   26   27   28   29      30      31
    :param input_file:
    :param range: ('start=0', 'end=77989'):
    :param discretize_flg: label all data, default: 1.
    :return:
    """
    print(
        f'input_file: {input_file}, data_range: {data_range}, label: {label}, discretize_flg: {discretize_flg}')
    start, end = data_range
    x = []
    cnt = 0
    with open(input_file, 'r') as hdl:
        line = hdl.readline()
        while line != '' and cnt < end:
            if line.startswith('ts'):
                line = hdl.readline()
                continue
            if (cnt >= start) and (cnt < end):
                if discretize_flg:
                    arr = line.split(',')[5:]
                    features = discretize_features(arr)
                    x.append(features)  # without : "ts, sip, dip, sport, dport"
                else:
                    x.append(line.split(','))  # without : "ts, sip, dip, sport, dport"
            line = hdl.readline()
            cnt += 1
    if type(label) == str:
        y = np.asarray([label for i in range(len(x))], dtype=str)
    else:
        y = np.ones(len(x)) * int(label)  # if label = 0, y = 0
    data_dict = {'X': np.asarray(x, dtype=float), 'y': y}

    return data_dict


def print_dict(train_set_dict):
    """

    :param train_set_dict:  train_set_dict = {'train_set': {'X': x_train, 'y': y_train}}
    :return:
    """
    for key, value in train_set_dict.items():
        if len(value) == 0:
            continue
        print(f'{key}:', end='')
        x = value['X']
        y = value['y']
        print(f'x.shape: {x.shape}, y.shape: {Counter(y.reshape(-1,))}')


def data_print(X_train_mu):
    return [float(v) for v in X_train_mu]


def data_stat_pandas(X='', y=None, check_idx=[1, 2, 3], data_name=''):
    import pandas as pd
    """ numpy to pandas
        You need to specify data, index and columns to DataFrame constructor, as in:
        >>> pd.DataFrame(data=data[1:,1:],    # values
        ...              index=data[1:,0],    # 1st column as index
        ...              columns=data[0,1:])  # 1st row as the column names
        
       you may need to change above to np.int_(data[1:,1:]) to have correct data type.

    """
    cols = check_idx
    # data = pd.read_csv('loan.csv', nrows=30000,
    #                    usecols=cols)  # the first 30000 rows in the data set (to reduce the computation time)

    index = [i for i in range(X.shape[0])]
    columns = [i for i in range(X.shape[1])]
    data = pd.DataFrame(data=X, index=index, columns=columns)
    pd.set_option('display.max_columns', None)  # in order to display all columns in terminal
    print(f'data_name: {data_name}\n', data.describe())


def normalize_data_with_sklearn(X='', scaler='', norm_method='z-score', features_idx=[]):
    """

    Args:
        X:
        scaler:
        norm_method:
        features_idx: which features will be normalized. [1,2,3]

    Returns:


        the easiest way is to apply the StandardScaler to only the subset of features that need to be scaled, and then concatenate the result with the remaining features.
        Alternatively, scikit-learn also offers (a still experimental, i.e. subject to change) ColumnTransformer API. It works similar to a pipline:

        from sklearn.compose import ColumnTransformer
        from sklearn.preprocessing import  StandarScaler
        column_trans = ColumnTransformer(
            [('scaler', StandardScaler(),2],
            remainder='passthrough')
        column_trans.fit_transform(X)

        The third entry of the tuple (here : 2) can be a single or a list of column indices (or column names when working with a pandas DataFrame).

    """
    print(f'only normalize features_idx ({len(features_idx)}): {features_idx}, others do not normalize')
    if scaler != '':
        ct_scaler = scaler
    else:
        if norm_method == 'z-score':
            scaler = StandardScaler()
        elif norm_method == 'min-max':
            scaler = MinMaxScaler()
        elif norm_method == 'robust':  # default: Robust Scalar (Scaling to median and quantiles)
            '''
               Scaling using median and quantiles consists of subtracting the median to all the observations and 
               then dividing by the interquartile difference. It Scales features using statistics that are robust 
               to outliers.
    
                The interquartile difference is the difference between the 75th and 25th quantile:
                    IQR = 75th quantile — 25th quantile
                The equation to calculate scaled values:
                    X_scaled = (X — X.median) / IQR
            '''

            scaler = RobustScaler()
        else:
            print(f'norm_method: {norm_method} is not implemented yet')
            return -1
        '''
            ColumnTransformer([('scaler', scaler, features_idx)],remainder='passthrough')  
            will normalize features_idx, for the remainder features, they will append to last columns.
            (i.e., ColumnTransformer will change featues' order.)
            
             By specifying ``remainder='passthrough'``, all remaining columns that
             were not specified in `transformers` will be automatically passed
             through. This subset of columns is concatenated with the output of
              ColumnTransformer(
            
            ct = [("norm1", Normalizer(norm='l1'), [0, 1]), ("norm2", Normalizer(norm='l1'), slice(2, 4))])the transformers.
        
        '''
        ct_scaler = ColumnTransformer([('scaler', scaler, features_idx)], remainder='passthrough')

        ct_scaler.fit(X)
    # range_val = col_trans_scaler.named_transformers_['scaler'].scale_
    # print(f'after normalized, range_val: {range_val}')
    trans_X = ct_scaler.transform(X)

    return trans_X, ct_scaler


def normalize_data_with_sklearn_all_features(X='', scaler='', norm_method='z-score', features_idx=[]):
    """

    Args:
        X:
        scaler:
        norm_method:
        features_idx: which features will be normalized. [1,2,3]

    Returns:


        the easiest way is to apply the StandardScaler to only the subset of features that need to be scaled, and then concatenate the result with the remaining features.
        Alternatively, scikit-learn also offers (a still experimental, i.e. subject to change) ColumnTransformer API. It works similar to a pipline:

        from sklearn.compose import ColumnTransformer
        from sklearn.preprocessing import  StandarScaler
        column_trans = ColumnTransformer(
            [('scaler', StandardScaler(),2],
            remainder='passthrough')
        column_trans.fit_transform(X)

        The third entry of the tuple (here : 2) can be a single or a list of column indices (or column names when working with a pandas DataFrame).

    """

    if norm_method == 'z-score':
        scaler = StandardScaler()
    elif norm_method == 'min-max':
        scaler = MinMaxScaler()
    else:  # default: Robust Scalar (Scaling to median and quantiles)
        '''
           Scaling using median and quantiles consists of subtracting the median to all the observations and 
           then dividing by the interquartile difference. It Scales features using statistics that are robust 
           to outliers.

            The interquartile difference is the difference between the 75th and 25th quantile:
                IQR = 75th quantile — 25th quantile
            The equation to calculate scaled values:
                X_scaled = (X — X.median) / IQR
        '''

        scaler = RobustScaler()

    scaler.fit(X)
    trans_X = scaler.transform(X)

    return trans_X, scaler


def stat_data(data=None, name='data'):
    #
    # import inspect
    # a= inspect.signature(stat_data)

    import pandas as pd
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 100)
    pd.set_option('display.float_format', lambda x: '%.3f' % x)  # without scientific notation

    columns = ['col_' + str(i) for i in range(data.shape[1])]
    dataset = pd.DataFrame(data=data, index=range(data.shape[0]), columns=columns)
    print(f'{name}.shape: {data.shape}')
    print(dataset.describe())
