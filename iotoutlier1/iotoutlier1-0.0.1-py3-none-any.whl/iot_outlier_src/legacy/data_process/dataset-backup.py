""" Dataset class

"""

import pickle
from collections import Counter, OrderedDict

import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.utils import shuffle

from utils.tool import stat_data, pprint, dump_data


class Dataset:

    def __init__(self, input_file=''):
        self.input_file = input_file
        self.fids, self.features, self.labels = self.load_pickled_data(input_file=self.input_file)

    def load_pickled_data(self, input_file):
        """ Especially for loading multi-objects stored in a file.

           :param input_file:
           :return:
           """

        fids = []
        features = []
        labels = []
        with open(input_file, 'rb') as in_hdl:
            while True:
                try:
                    fids_, features_, labels_ = pickle.load(in_hdl)
                    fids.extend(fids_)
                    features.extend(features_)
                    labels.extend(labels_)
                except EOFError:
                    break

        return fids, features, labels

    def split_train_test(self, features='', labels='', shuffle_flg=True, random_state=42):

        X_normal = []
        y_normal = []
        X_anomaly = []
        y_anomaly = []
        none_num = 0

        for i, value in enumerate(labels):
            feat = list(features[i])
            if value.upper() in ['NORMAL', 'BENIGN']:
                X_normal.append(feat)
                y_normal.append(0)
            elif value.upper() in ['BOT', 'ANOMALY']:
                X_anomaly.append(feat)
                y_anomaly.append(1)
            else:  # label in [None, 'None', ... ]
                print(f'i:{i}, {value}')
                none_num += 1
        print(f'{none_num} flows appear in pcap, however, don\'t appear in labels.csv')
        print(f'0: Normal, 1: Anomaly')

        if shuffle_flg:  # random select a part of normal flows from normal flows
            c = list(zip(X_normal, y_normal))
            X_normal, y_normal = zip(*shuffle(c, random_state=random_state))

        X_normal = np.array(X_normal, dtype=float)
        y_normal = np.array(y_normal, dtype=int)
        X_anomaly = np.array(X_anomaly, dtype=float)
        y_anomaly = np.array(y_anomaly, dtype=int)

        if len(y_anomaly) == 0:
            print(f'no anomaly data in this data_process')
            train_size = len(y_normal) - 100  # use 100 normal flows as test set.
            X_train = X_normal[:train_size, :]
            y_train = y_normal[:train_size]
            X_test = X_normal[:100, :]
            y_test = y_normal[:100]
        else:
            train_size = len(y_normal) - len(y_anomaly)
            X_train = X_normal[:train_size, :]
            y_train = y_normal[:train_size]
            X_test = np.concatenate([X_normal[train_size:, :], X_anomaly], axis=0)
            y_test = np.concatenate([y_normal[train_size:], y_anomaly], axis=0)

        print(f'--- train set and test set --'
              f'\nX_train:{X_train.shape}, y_train:{Counter(y_train)}'
              f'\nX_test :{X_test.shape}, y_test :{Counter(y_test)}, in which, 0: normals and 1: anomalies.')
        stat_data(X_train, name='X_train')
        stat_data(X_test, name='X_test')

        return X_train, y_train, X_test, y_test

    def normalise_data(self, X_train, X_test, norm_method='std'):
        """ if normalise data or not

        :param X_train:
        :param X_test:
        :param norm_method:
        :return:
        """
        print(f'2) normalization ({norm_method})')
        if norm_method in ['min-max', 'std', 'robust']:
            if norm_method == 'min-max':  # (x-min)/(max-min)
                self.train_scaler = MinMaxScaler()
            elif norm_method == 'std':  # (x-u)/sigma
                self.train_scaler = StandardScaler()
            elif norm_method == 'robust':  # (x-Q2)/(Q3-Q1)
                self.train_scaler = RobustScaler()
            self.train_scaler.fit(X_train)
            X_train = self.train_scaler.transform(X_train)
            X_test = self.train_scaler.transform(X_test)

            print('after normalization: X_train distribution:')
            stat_data(X_train, name='X_train')
            print('after normalization:X_test distribution:')
            stat_data(X_test, name='X_test')

            return X_train, X_test

        elif norm_method == 'log':  # log scaler
            # X_train = np.log(X_train)         # np.log(v): v > 0
            min_trainvalues = np.min(X_train, axis=0)
            X_train = np.log(X_train - min_trainvalues + 1)  # X_train-in_values + 1: scale all values to [1, . ]
            # and np.log(values) will be [0, .]

            X_test = np.clip(X_test - min_trainvalues, a_min=0, a_max=10e+6)  # all values less than 0 are clipped to 0
            X_test = np.log(X_test + 1)

            print('after normalization: X_train distribution:')
            stat_data(X_train, name='X_train')
            print('after normalization:X_test distribution:')
            stat_data(X_test, name='X_test')

            return X_train, X_test

        elif norm_method == 'none' or norm_method == None:
            print('without normalization')
            return X_train, X_test

        else:
            print(f'norm_method: {norm_method} is not implemented yet, please check and retry')
            return -1


def _fix_data(features, fft_bin):
    fixed_features = []
    for feat in features:
        feat = list(feat)
        if len(feat) > fft_bin:
            feat = feat[:fft_bin]
        else:
            feat += [0] * (fft_bin - len(feat))

        fixed_features.append(np.asarray(feat, dtype=float))

    return fixed_features


def _get_fft_data(features, fft_bin='', fft_part='real'):
    # calculate discrete FFTs
    if fft_part == 'real':  # default
        fft_features = [np.real(np.fft.fft(IATs, n=fft_bin)) for IATs in features]
    elif fft_part == 'real+imaginary':
        fft_features = []
        for i, IATs in enumerate(features):
            complex_v = np.fft.fft(IATs, fft_bin)
            if i == 0:
                print(f'dimension of the real part: {len(np.real(complex_v))}, '
                      f'dimension of the imaginary part: {len(np.imag(complex_v))}')
            v = np.concatenate([np.real(complex_v), np.imag(complex_v)], axis=np.newaxis)
            fft_features.append(v)
    else:
        print(f'fft_part: {fft_part} is not correct, please modify it and retry')
        return -1

    return fft_features


def transform_samp_baseline_to_fixed_out(input_file='IAT_sampling_file', fft_bin=10,
                                         overwrite=True, verbose=True):
    """ obtain fixed output from raw IATs based on feat_set, quant and fft_part

    :param input_file:
    :param feat_set:
    :param quant:
    :param fft_part: only works when feat_set =='FFT'
    :param overwrite: True,  remove the file and re-generate all data
    :return:
    """

    # 1) load IAT data from file
    print(f'IAT_file (with different IAT dimensions): {input_file}')
    data_inst = Dataset(input_file=input_file)

    fixed_out_file = input_file + f'-fixed_{fft_bin}.dat'
    fixed_features = _fix_data(data_inst.features, fft_bin)
    dump_data((data_inst.fids, fixed_features, data_inst.labels), output_file=fixed_out_file)

    print(f'sampling fixed_out_file: {fixed_out_file}, with fft_bin: {fft_bin}')
    return fixed_out_file


def transform_iat_to_fixed_out(input_file='IAT_file', feat_set='IAT', quant=0.8, fft_part='real',
                               overwrite=True, verbose=True):
    """ obtain fixed output from raw IATs based on feat_set, quant and fft_part

    :param input_file:
    :param feat_set:
    :param quant:
    :param fft_part: only works when feat_set =='FFT'
    :param overwrite: True,  remove the file and re-generate all data
    :return:
    """
    if verbose:
        funcparams_dict = {'input_file': input_file, 'feat_set': feat_set, 'quant': quant,
                           'fft_part': fft_part, 'overwrite': overwrite, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=transform_iat_to_fixed_out.__name__)

    # 1) load IAT data from file
    print(f'IAT_file (with different IAT dimensions): {input_file}')
    data_inst = Dataset(input_file=input_file)

    # 2) obtain fft_bins according to quant
    flows_len_arr = [len(iats) for iats in data_inst.features]  # IATs
    fft_bin = int(np.round(np.quantile(flows_len_arr, q=quant)))  # be careful of np.round() and int()
    print(f'choose quantile = {quant} and get fft_bin: {fft_bin}.')

    # print(f'dimension of {feat_set}: {fft_bin}')
    # 3) save the fixed IAT with fft_bins
    if feat_set == 'IAT':
        fixed_out_file = input_file + f'-{feat_set}-quant_{quant}-dim_{fft_bin}.dat'
        fixed_features = _fix_data(data_inst.features, fft_bin)
        dump_data((data_inst.fids, fixed_features, data_inst.labels), output_file=fixed_out_file)

    if feat_set == 'FFT':
        # 4) save the fixed FFT with fft_bins
        if fft_part == 'real+imaginary':
            fixed_out_file = input_file + f'-{feat_set}-quant_{quant}-dim_{fft_bin*2}-fft_part_{fft_part}.dat'  # real + imaginary
        else:
            fixed_out_file = input_file + f'-{feat_set}-quant_{quant}-dim_{fft_bin}-fft_part_{fft_part}.dat'  # real

        fft_features = _get_fft_data(data_inst.features, fft_bin=fft_bin, fft_part=fft_part)
        dump_data((data_inst.fids, fft_features, data_inst.labels), output_file=fixed_out_file)

    print(f'fixed_out_file: {fixed_out_file}, with fft_bin: {fft_bin}')
    return fixed_out_file, fft_bin
