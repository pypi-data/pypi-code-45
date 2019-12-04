"""
    load features data from txt
"""
import os
import pickle

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle


def random_sampling_data(X, y, num=100, random_state=42):
    """

    :param data:
    :param num:
    :return:
    """

    if num > len(y):
        print(f'input data size {len(y)} is less than the sampled number.')
        return -1

    X, y = shuffle(X, y, n_samples=num, random_state=random_state)

    return X, y


def load_and_split_data(norm_file='input_data/demo_dataset/normal_demo_dataset.txt',
                        anomaly_file='input_data/demo_dataset/anomaly_demo_dataset.txt',
                        test_size=0.3, random_state=42):
    """

    :param test_size:
    :param random_state:
    :return:
    """
    X_norm, y_norm = load_data_from_txt(input_file=norm_file, sample_type='normal')
    X_train, X_norm_test, y_train, y_norm_test = train_test_split(X_norm, y_norm, test_size=test_size,
                                                                  random_state=random_state)
    X_anomaly, y_anomaly = load_data_from_txt(input_file=anomaly_file, sample_type='anomaly')

    X_anomaly, y_anomaly = random_sampling_data(X_anomaly, y_anomaly, num=len(y_norm_test), random_state=random_state)

    X_test = np.concatenate([X_norm_test, X_anomaly], axis=0)  # axis =0 means that concatenate by rows
    y_test = np.concatenate([y_norm_test, y_anomaly], axis=0)

    return X_train, y_train, X_test, y_test


def load_data_from_txt(input_file, sample_type='normal'):
    X = []
    y = []
    with open(input_file, 'r') as hdl:
        line = hdl.readline()
        while line != '':
            if line.startswith('ts'):
                line = hdl.readline()
                continue
            X.append(line.split(','))
            if sample_type == 'normal':
                y.append(0)  # normal: 0
            else:
                y.append(1)  # anomaly: 1
            line = hdl.readline()

    return np.asarray(X, dtype=float), np.asarray(y, dtype=int)


def select_features_from_list(input_file='', output_file='', features_lst=[5, 9, 10, 12]):
    """

    :param input_file:
    :param features_lst:
    :return:
    """

    X = []
    with open(input_file, 'r') as hdl:
        line = hdl.readline()
        while line != '':
            if line.startswith('ts'):
                line = hdl.readline()
                continue
            arr = line.split(',')
            line_tmp = ''
            for idx in features_lst[:-1]:
                line_tmp += str(arr[idx]) + ','
            X.append(line_tmp + str(arr[features_lst[-1]]))
            line = hdl.readline()

    if output_file == '':
        output_file = os.path.splitext(input_file)[0] + '_sub.txt'

    with open(output_file, 'w') as hdl:
        for line in X:
            hdl.write(line + '\n')

    return output_file


def balance_data(x_norm_train_DT, y_norm_train_DT, x_attack_train_DT, y_attack_train_DT, random_state=42):
    min_size = x_norm_train_DT.shape[0]
    if min_size > x_attack_train_DT.shape[0]:
        min_size = x_attack_train_DT.shape[0]
        x_train_DT = np.concatenate([shuffle(x_norm_train_DT, random_state=random_state)[:min_size], x_attack_train_DT])
        y_train_DT = np.concatenate([y_norm_train_DT[:min_size], y_attack_train_DT])
    else:
        x_train_DT = np.concatenate([x_norm_train_DT, shuffle(x_attack_train_DT, random_state=random_state)[:min_size]])
        y_train_DT = np.concatenate([y_norm_train_DT, y_attack_train_DT[:min_size]])
    print(f'\nWith data balance, x_train.shape: {x_train_DT.shape}')
    print(
        f' in which, x_norm_train_DT.shape: {x_norm_train_DT[:min_size].shape}, and x_attack_train_DT.shape: {x_attack_train_DT[:min_size].shape}')
    return x_train_DT, y_train_DT


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


def load_data_from_txt_1(input_file, start=0, end=77989, discretize_flg=True):
    """
        features: ts, sip, dip, sport, dport, proto, dura, orig_pks, reply_pks, orig_bytes, reply_bytes, orig_min_pkt_size, orig_max_pkt_size, reply_min_pkt_size, reply_max_pkt_size, orig_min_interval, orig_max_interval, reply_min_interval, reply_max_interval, orig_min_ttl, orig_max_ttl, reply_min_ttl, reply_max_ttl, urg, ack, psh, rst, syn, fin, is_new, state, prev_state
            idx : 0    1    2    3      4      5      6      7         8          9            10            11                 12                  13                  14                       15            16                      17               18                19          20             21           22            23   24   25   26   27   28   29      30      31
    :param input_file:
    :param start:
    :param end:
    :param discretize_flg:
    :return:
    """
    data = []
    cnt = 0
    with open(input_file, 'r') as hdl:
        line = hdl.readline()
        while line != '' and cnt < end:
            if line.startswith('ts'):
                line = hdl.readline()
                continue
            if cnt >= start:
                if discretize_flg:
                    arr = line.split(',')[5:]
                    features = discretize_features(arr)
                    data.append(features)  # without : "ts, sip, dip, sport, dport"
                else:
                    data.append(line.split(',')[5:])  # without : "ts, sip, dip, sport, dport"
            line = hdl.readline()
            cnt += 1

    return np.asarray(data, dtype=float)


def dump_model(model, out_file):
    """
        save model to disk
    :param model:
    :param out_file:
    :return:
    """
    out_dir = os.path.split(out_file)[0]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    with open(out_file, 'wb') as f:
        pickle.dump(model, f)

    print("Model saved in %s" % out_file)

    return out_file


def load_model(input_file):
    """

    :param input_file:
    :return:
    """
    print("Loading model...")
    with open(input_file, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded.")

    return model


def get_variable_name(data_var):
    """
        get variable name as string
    :param data_var:
    :return:
    """
    name = ''
    keys = locals().keys()
    for key, val in locals().items():
        # if id(key) == id(data_var):
        print(key, id(key), id(data_var), key is data_var)
        # if id(key) == id(data_var):
        if val == data_var:
            name = key
            break

    return name
