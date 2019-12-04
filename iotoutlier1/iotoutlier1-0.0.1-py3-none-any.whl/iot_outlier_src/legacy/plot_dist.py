""" plot data distribution

"""
# Authors: kun.bj@outlook.com
#
# License: xxx

import pickle
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from utils.tool import stat_data


def load_pickle_features_labels_data(input_file):
    # save results
    with open(input_file, 'rb') as in_hdl:
        features, labels = pickle.load(in_hdl)

    return features, labels


def plot_histgram(data, bins=100, title=''):
    # data = np.histogram(data, bins=bins)

    plt.hist(data, bins=bins)  # arguments are passed to np.histogram
    plt.title(f"{title}")
    plt.ylabel('Counts')
    plt.xlabel('Number of packets in each flow')
    # plt.xlim(0,15)
    plt.show()


if __name__ == '__main__':

    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    for i, srcIP in enumerate(srcIP_lst):
        plt.subplot(2, 3, i + 1)  # plt.subplot(131)

        input_file = f'input_data/CICIDS2017/Merged-WorkingHours/5_bots_20170707-09_00-12_00-srcIP_{srcIP}.pcap_IAT.txt'
        print(f'input_file: {input_file}')
        features, labels = load_pickle_features_labels_data(input_file)
        print(f'{Counter(labels)}')

        fft_bins = 21
        X_normal = []
        y_normal = []
        X_anomaly = []
        y_anomaly = []
        for i, value in enumerate(labels):
            feat = list(features[i][1])  # (fid, IAT)
            if len(feat) > fft_bins:
                feat = feat[:fft_bins]
            else:
                feat += [0] * (fft_bins - len(feat))

            if value.upper() in ['NORMAL', 'BENIGN']:
                X_normal.append(feat)
                y_normal.append(0)
            else:
                X_anomaly.append(feat)
                y_anomaly.append(1)

        X_normal = np.array(list(X_normal), dtype=float)
        y_normal = np.array(y_normal, dtype=int)
        X_anomaly = np.array(X_anomaly, dtype=float)
        y_anomaly = np.array(y_anomaly, dtype=int)

        print('X_noraml distribution:')
        stat_data(X_normal)
        print('X_anomaly distribution:')
        stat_data(X_anomaly)
