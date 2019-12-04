# Authors: kun.bj@outlook.com
#
# License: xxx
""" Main function for feature set comparison.
    Measure metrics: ROC amd AUC

"""
import itertools
import os
import pickle
from collections import Counter, OrderedDict
from copy import deepcopy
from random import shuffle

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance
from sklearn import metrics, clone
from sklearn.metrics import roc_curve
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.utils import shuffle

from detector.gmm_class import GMMDetector
from detector.kde_class import KDEDetector
from detector.ocsvm_class import OCSVMDetector
from detector.pca_class import PCADetector
from legacy.utils.dataset import stat_data

# It is a list of strings defining what symbols in a module will be exported
# when from <module> import * is used on the module.
__all__ = ['Dataset', 'GridSearch', 'main_individual', 'main_mix']


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
        """ split data into train and test set.
            Note: number of flows might decrease due to "NONE" label in labels.

        :param features:
        :param labels:
        :param shuffle_flg:
        :param random_state:
        :return:
        """

        X_normal = []
        y_normal = []
        X_anomaly = []
        y_anomaly = []
        none_num = 0

        for i, value in enumerate(labels):  # change the labels to 0 or 1
            feat = list(features[i])
            if value.upper() in ['NORMAL', 'BENIGN']:
                X_normal.append(feat)
                y_normal.append(0)
            elif value.upper() in ['BOT']:
                X_anomaly.append(feat)
                y_anomaly.append(1)
            else:
                none_num += 1
        print(f'{none_num} flows appear in pcap, however, don\'t appear in labels.csv')
        print(f'0: NORMAL, 1: ANOMALY')

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
              f'\nX_test :{X_test.shape}, y_test :{Counter(y_test)}, in which, 0: normal and 1: anomaly')
        stat_data(X_train, name='X_train')
        stat_data(X_test, name='X_test')

        return X_train, y_train, X_test, y_test


class GridSearch():

    def __init__(self, estimator='', scoring='auc',
                 param_grid={'n_components': [i + 1 for i in range(10)], 'covariance_type': ['full', 'diag']}):

        self.estimator = estimator
        self.param_grid = param_grid
        self.scoring = scoring

    def fit(self, X_train='', y_train='', X_test='', y_test=''):
        """ get the best parameters of the detector

        :param X_train:
        :param y_train:
        :param X_test:
        :param y_test:
        :return:
        """

        keys, values = zip(*self.param_grid.items())
        combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]
        print(len(combinations))
        # print(combinations)
        self.best_score_ = 0
        self.best_params_ = {}
        for idx, params in enumerate(combinations):
            self.detector = clone(self.estimator)  # constructs a new estimator with the same parameters, but not fit
            self.detector.set_params(**params)  # set params
            print(f'idx: {idx+1}, detector_params: {self.detector.get_params()}')
            try:
                self.detector.fit(X_train, y_train)
            except Exception as e:
                print(f'{e}, skipping {params}')
                continue
            self.detector.test(X_test, y_test)
            print(f'auc: {self.detector.auc}')

            if self.scoring == 'auc':
                if self.detector.auc > self.best_score_:
                    self.best_score_ = self.detector.auc
                    self.best_params_ = params  # if key exists, update; otherwise, add new key
                    self.best_estimator_ = deepcopy(self.detector)
                    print(f'best_auc: {self.best_estimator_.auc}, {self.best_score_}')
            else:
                print(f'scoring: {self.scoring} is not implemented yet, please check and retry')

        # # summarize the results of the grid search
        print(f'grid.best_score_: {self.best_score_}')
        print(f'grid.best_params_: {self.best_params_}')
        print(f'grid.best_estimator_: {self.best_estimator_}')

        return self


class Experiment:

    def __init__(self, input_file, feat_set='', norm_method='std', data_aug=False, shuffle_flg=True, random_state=42):
        """ initialize parameters and get the data from file

        :param input_file:
        :param feat_set:
        :param norm_method:
        :param data_aug:
        :param shuffle_flg: Ture: random select a part of normal data from all normal data to make up of test set
        :param random_state: to reproduce all experimental results
        """

        print_values(input_file=input_file, feat_set=feat_set, norm_method=norm_method,
                     data_aug=data_aug,
                     shuffle_flg=shuffle_flg, random_state=random_state)

        self.feat_set = feat_set

        print('1) load data and split train and test set')
        self.data_inst = Dataset(input_file)
        self.X_train, self.y_train, self.X_test, self.y_test = self.data_inst.split_train_test(
            features=self.data_inst.features,
            labels=self.data_inst.labels,
            shuffle_flg=shuffle_flg,
            random_state=random_state)

        self.norm_method = norm_method
        print(f'2) normalization ({norm_method})')
        self.X_train, self.X_test = self.normalise_data(self.X_train, self.X_test, norm_method=self.norm_method)

        self.data_aug = data_aug
        self.random_state = random_state

    def run(self, detector_name='OCSVM', X_train='', y_train=None, X_test='', y_test='', grid_search_flg=False):
        """ build detector and get the results

        :param detector_name:
        :param X_train:
        :param y_train:
        :param X_test:
        :param y_test:
        :param grid_search_flg:
        :return:
        """
        print(f'3) train and test using {detector_name}')
        result_dict = {}

        if grid_search_flg:
            if detector_name.upper() == 'OCSVM':
                distances = distance.pdist(X_train, metric='euclidean')
                stat_data(distances.reshape(-1, 1), name='distances')
                q_lst = list(np.linspace(0.0, 1, 21))[1:]
                gamma_lst = list(1 / (np.quantile(distances, q=q_lst) ** 2))
                # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(),
                # key=lambda item: item[0])}')
                print(f'gamma_lst:{gamma_lst},\nq_lst: {q_lst}')
                detector = OCSVMDetector(random_state=self.random_state)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'gamma': gamma_lst, 'kernel': ['rbf']})

            elif detector_name.upper() == 'GMM':
                detector = GMMDetector(random_state=self.random_state)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'n_components': [i + 1 for i in range(20)], 'covariance_type': ['diag']})

            elif detector_name.upper() == 'PCA':
                detector = PCADetector(random_state=self.random_state)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'n_components': [i + 1 for i in range(10)]})

            elif detector_name.upper() == 'KDE':
                detector = KDEDetector(random_state=self.random_state)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'bandwidth': [i + 1 for i in range(20)]})
            else:
                print(f'detector: {detector_name} is not implemented yet, please check and retry')
                return -1

            grid.fit(X_train, y_train, X_test, y_test)
            detector = grid.best_estimator_
            print(f'{detector_name}.params: {detector.get_params()}')

            detector.test(X_test, y_test)
            # print(f'auc: {detector.auc}')
            result_dict[detector_name] = {'y_true': y_test, 'y_scores': detector.y_scores, 'auc': detector.auc,
                                          'best_score_': grid.best_score_, 'best_params_': grid.best_params_,
                                          'best_estimator_': grid.best_estimator_
                                          }

        else:  # grid_search_flg: False
            if detector_name.upper() == 'OCSVM':
                distances = distance.pdist(X_train, metric='euclidean')
                stat_data(distances.reshape(-1, 1), name='distances')
                q = 0.1
                print('without grid search')
                sigma = np.quantile(distances, q=q)
                gamma = 1 / (sigma ** 2)
                # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(),
                # key=lambda item: item[0])}')
                print(f'gamma: {gamma}, q: {q}, sigma: {sigma}')
                detector = OCSVMDetector(gamma=gamma, random_state=self.random_state)

            elif detector_name.upper() == 'GMM':
                detector = GMMDetector(n_components=7, covariance_type='diag', random_state=self.random_state)

            elif detector_name.upper() == 'PCA':
                detector = PCADetector(n_components=2, random_state=self.random_state)

            elif detector_name.upper() == 'KDE':
                detector = KDEDetector(bandwidth=3, random_state=self.random_state)

            else:
                print(f'detector: {detector_name} is not implemented yet, please check and retry')
                return -1

            print(f'{detector_name}.params: {detector.get_params()}')
            detector.fit(X_train, y_train)
            detector.test(X_test, y_test)

            result_dict[detector_name] = {'y_true': y_test, 'y_scores': detector.y_scores, 'auc': detector.auc,
                                          'best_score_': detector.auc, 'best_params_': detector.get_params(),
                                          'best_estimator_': detector
                                          }

        model_file = f'output_data/models_dumping/{detector_name}_' + self.feat_set + str(
            detector.get_params()) + '.joblib'
        print(f'model_file: {model_file}')
        with open(model_file, 'wb') as out_hdl:
            pickle.dump(detector, out_hdl)
        # detector = pickle.load(model_file)

        return result_dict

    def normalise_data(self, X_train, X_test, norm_method='std'):
        """ if normalise data or not

        :param X_train:
        :param X_test:
        :param norm_method:
        :return:
        """

        if norm_method in ['min-max', 'std']:
            if norm_method == 'min-max':
                train_scaler = MinMaxScaler()
            if norm_method == 'std':
                train_scaler = StandardScaler()
            train_scaler.fit(X_train)
            X_train = train_scaler.transform(X_train)
            X_test = train_scaler.transform(X_test)

            print('after normalization: X_train distribution:')
            stat_data(X_train, name='X_train')
            print('after normalization:X_test distribution:')
            stat_data(X_test, name='X_test')

            return X_train, X_test

        elif norm_method == 'none':
            print('without normalization')
            return X_train, X_test
        else:
            print(f'norm_method: {norm_method} is not implemented yet, please check and retry')
            return -1


def insert_newlines(data_str, step=45):
    """ format the title with fixed length

    :param data_str:
    :param step:
    :return:
    """
    return '\n'.join(data_str[i:i + step] for i in range(0, len(data_str), step))


def plot_roc_auc(result_dict_lst, output_file='output_data/figures/roc_of_different_algorithms.pdf',
                 title='ROC'):
    """ plot roc and auc

    :param result_dict_lst:
    :param out_file:
    :param title:
    :return:
    """
    # with plt.style.context(('ggplot')):
    fig, ax = plt.subplots()

    colors_lst = ['r', 'm', 'b', 'g', 'y', 'c', '#0072BD', '#A2142F', '#EDB120', 'k', '#D95319', '#4DBEEE',
                  'C1']  # add more color values: https://www.mathworks.com/help/matlab/ref/plot.html
    for idx, (feature_set_key, result_dict) in enumerate(result_dict_lst.items()):
        # colors_dict[feature_set_key] = {'AE': 'r', 'DT': 'm', 'PCA': 'C1', 'IF': 'b', 'OCSVM': 'g'}
        for i, (detector_key, value_dict) in enumerate(result_dict.items()):
            detector_key = detector_key.upper()
            y_true = value_dict['y_true']
            y_scores = value_dict['y_scores']
            fpr, tpr, thres = roc_curve(y_true=y_true, y_score=y_scores)
            # IMPORTANT: first argument is true values, second argument is predicted probabilities (i.e., y_scores)
            auc = value_dict['auc']
            print(f'auc: {metrics.auc(fpr, tpr)}, {auc}')
            auc = f'{auc:.4f}'
            print(f'result of {detector_key}: {feature_set_key}, auc={auc}, fpr={fpr}, tpr={tpr}')
            # print(best_dict[feature_set_key]['best_score_'] == auc)
            if detector_key == 'PCA':
                lw = 3
            else:
                lw = 2
            params = value_dict['best_params_']
            params = insert_newlines(str(params))
            ax.plot(fpr, tpr, colors_lst.pop(0), label=f'{feature_set_key}. AUC:{auc},\n {params}', lw=lw, alpha=1,
                    linestyle='-')
            ax.text(2, 7, 'this is\nyet another test',
                    rotation=45,
                    horizontalalignment='center',
                    verticalalignment='top',
                    multialignment='center')

    ax.plot([0, 1], [0, 1], 'k--', label='', alpha=0.9)
    plt.xlim([0.0, 1.0])
    plt.ylim([0., 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='lower right')

    plt.title(insert_newlines(title))
    # plt.subplots_adjust(bottom=0.25, top=0.75)
    print(f'ROC:{output_file}')
    plt.savefig(output_file)  # should use before plt.show()
    plt.show()

    return output_file


def print_values(**kwargs):
    for idx, (key, value) in enumerate(kwargs.items()):
        if idx == len(kwargs.keys()) - 1:
            print(f'{key}: {value}')
        else:
            print(f'{key}: {value}, ', end='')


def IAT_to_fixed_out(input_file='IAT_file', feat_set='IAT', quant=0.8, fft_part='real', overwrite=True):
    """ obtain fixed output from raw IATs based on feat_set, quant and fft_part

    :param input_file:
    :param feat_set:
    :param quant:
    :param fft_part: only works when feat_set =='FFT'
    :param overwrite: True,  remove the file and re-generate all data
    :return:
    """
    print_values(input_file=input_file, feat_set=feat_set, quant=quant, fft_part=fft_part, overwrite=overwrite)

    # 1) load IAT data from file
    print(f'IAT_file (with different IAT dimensions): {input_file}')
    data_inst = Dataset(input_file=input_file)

    # 2) obtain fft_bins according to quant
    flows_len_arr = [len(value) for value in data_inst.features]
    fft_bin = int(np.quantile(flows_len_arr, q=quant))
    print(f'choose quantile = {quant} and get fft_bin: {fft_bin}.')

    # 3) save the fixed IAT with fft_bins
    if feat_set == 'IAT':
        print(f'dimension of {feat_set}: {fft_bin}')
        fixed_out_file = input_file + f'_{feat_set}_quant_{quant}_dimension_{fft_bin}.dat'

        if os.path.exists(fixed_out_file):
            if overwrite:
                os.remove(fixed_out_file)
                print(f'fixed_iat_file: {fixed_out_file}')  # IAT
                features_fixed = []
                for feat in data_inst.features:
                    feat = list(feat)  # (fid, IAT)
                    if len(feat) > fft_bin:
                        feat = feat[:fft_bin]
                    else:
                        feat += [0] * (fft_bin - len(feat))

                    features_fixed.append(np.asarray(feat, dtype=float))
                # # save results
                with open(fixed_out_file, 'wb') as out_hdl:
                    pickle.dump((data_inst.fids, features_fixed, data_inst.labels), out_hdl)
            else:
                print(f'fixed_iat_file exists: {fixed_out_file}')  # IAT
        else:  # file doesn't exist
            print(f'fixed_iat_file: {fixed_out_file}')  # IAT
            features_fixed = []
            for feat in data_inst.features:
                feat = list(feat)
                if len(feat) > fft_bin:
                    feat = feat[:fft_bin]
                else:
                    feat += [0] * (fft_bin - len(feat))

                features_fixed.append(np.asarray(feat, dtype=float))
            # # save results
            with open(fixed_out_file, 'wb') as out_hdl:
                pickle.dump((data_inst.fids, features_fixed, data_inst.labels), out_hdl)

    if feat_set == 'FFT':
        # 4) save the fixed FFT with fft_bins
        print(f'dimension of {feat_set}: {fft_bin}')
        if fft_part == 'real+imaginary':
            fixed_out_file = input_file + f'_{feat_set}_quant_{quant}_dimension_{fft_bin*2}_{fft_part}.dat'  # real + imaginary
        else:
            fixed_out_file = input_file + f'_{feat_set}_quant_{quant}_dimension_{fft_bin}_{fft_part}.dat'  # real

        if os.path.exists(fixed_out_file):
            if overwrite:
                os.remove(fixed_out_file)
                # calculate discrete FFTs
                if fft_part == 'real':  # default
                    features = [np.real(np.fft.fft(IATs, n=fft_bin)) for IATs in data_inst.features]
                elif fft_part == 'real+imaginary':
                    features = []
                    for i, IATs in enumerate(data_inst.features):
                        complex_v = np.fft.fft(IATs, fft_bin)
                        if i == 0:
                            print(f'dimension of the real part: {len(np.real(complex_v))}, '
                                  f'dimension of the imaginary part: {len(np.imag(complex_v))}')
                        v = np.concatenate([np.real(complex_v), np.imag(complex_v)], axis=np.newaxis)
                        features.append(v)
                else:
                    print(f'fft_part: {fft_part} is not correct, please modify it and retry')
                    return -1
                # # save results
                with open(fixed_out_file, 'wb') as out_hdl:
                    pickle.dump((data_inst.fids, features, data_inst.labels), out_hdl)
            else:
                print(f'fixed_fft_file exists: {fixed_out_file}')  # fft

        else:
            print(f'fixed_fft_file: {fixed_out_file}')

            # calculate discrete FFTs
            if fft_part == 'real':  # default
                features = [np.real(np.fft.fft(IATs, n=fft_bin)) for IATs in data_inst.features]
            elif fft_part == 'real+imaginary':
                features = []
                for i, IATs in enumerate(data_inst.features):
                    complex_v = np.fft.fft(IATs, fft_bin)
                    if i == 0:
                        print(f'dimension of the real part: {len(np.real(complex_v))}, '
                              f'dimension of the imaginary part: {len(np.imag(complex_v))}')
                    v = np.concatenate([np.real(complex_v), np.imag(complex_v)], axis=np.newaxis)
                    features.append(v)
            else:
                print(f'fft_part: {fft_part} is not correct, please modify it and retry')
                return -1
            # # save results
            with open(fixed_out_file, 'wb') as out_hdl:
                pickle.dump((data_inst.fids, features, data_inst.labels), out_hdl)

    return fixed_out_file, fft_bin


def merge_multifiles_to_one(files_lst=[], output_file=''):
    with open(output_file, 'wb') as out_hdl:
        # pickle.dump(len(files_lst), out_hdl)
        for file in files_lst:
            print(f'file:{file}')
            with open(file, 'rb') as in_hdl:
                fids, features, labels = pickle.load(in_hdl)
                pickle.dump((fids, features, labels), out_hdl)

    return output_file


def add_data_to_file(input_file_lst, output_file):
    with open(output_file, 'wb') as out_hdl:
        for input_file in input_file_lst:
            data_inst = Dataset(input_file)
            pickle.dump((data_inst.fids, data_inst.features, data_inst.labels), out_hdl)

    return output_file


def main_more_data():
    norm_method = 'none'  # none: without normalization, otherwise, 'min-max' or 'std'
    data_aug = False  # data_augmentation: if add more normal flows.
    random_state = 42  # to reproduce the results
    detector_name = 'GMM'  # 'OCSVM', 'GMM', 'PCA'
    grid_search_flg = True  # True: to pick the best parameters of the detector
    print_values(detector_name=detector_name, norm_method=norm_method, data_aug=data_aug, random_state=random_state,
                 grid_search_flg=grid_search_flg)

    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    quant = 0.9  # to obtain fft_bin from IATs data
    for idx, srcIP in enumerate(srcIP_lst):
        print(f'\n*index: {idx}, srcIP: {srcIP}, quant (for obtaining fft_bin): {quant}')

        result_dict_lst = OrderedDict()  # store the results: {feat_set: results of the feat_set}

        # 1. obtain results (such as ROC and AUC) of IAT or FFT
        prop_set = 'IAT'  # proposed features:  IAT or FFT
        fft_part = 'real'  # only for FFT: 'real' or 'real+imaginary'
        IAT_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat'  # raw IATs file
        IAT_file_2 = f'input_data/CICIDS2017/srcIP_{srcIP}/Monday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat'  # raw IATs file
        input_file_lst = [IAT_file, IAT_file_2]
        output_file = IAT_file_2 + '_more_data.dat'
        more_data_file = add_data_to_file(input_file_lst, output_file)

        prop_file, fft_bin = IAT_to_fixed_out(input_file=more_data_file, feat_set=prop_set, quant=quant,
                                              fft_part=fft_part, overwrite=True)

        prop = Experiment(input_file=prop_file, feat_set=prop_set, norm_method=norm_method, random_state=random_state)
        result_dict = prop.run(detector_name=detector_name,
                               X_train=prop.X_train, y_train=prop.y_train,
                               X_test=prop.X_test, y_test=prop.y_test,
                               grid_search_flg=grid_search_flg)
        result_dict_lst[prop_set] = result_dict

        # 2. obtain results (such as ROC and AUC) of Baseline
        base_set = 'Baseline'
        base_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_{base_set}_' \
                    f'dimension_10.dat'  # baseline features file
        base_file_2 = f'input_data/CICIDS2017/srcIP_{srcIP}/Monday-WorkingHours/srcIP_{srcIP}.pcap_{base_set}_' \
                      f'dimension_10.dat'  # baseline features file
        input_file_lst = [base_file, base_file_2]
        output_file = base_file_2 + '_more_data.dat'
        more_data_file = add_data_to_file(input_file_lst, output_file)

        base = Experiment(input_file=more_data_file, feat_set=base_set, norm_method=norm_method,
                          random_state=random_state)
        result_dict = base.run(detector_name=detector_name,
                               X_train=base.X_train, y_train=base.y_train,
                               X_test=base.X_test, y_test=base.y_test,
                               grid_search_flg=grid_search_flg)
        result_dict_lst[base_set] = result_dict

        plot_roc_auc(result_dict_lst, title=f'{detector_name}, srcIP:{srcIP}')

        # break


def main_mix():
    norm_method = 'none'  # none: without normalization, otherwise, 'min-max' or 'std'
    data_aug = False  # data_augmentation: if add more normal flows.
    random_state = 42  # to reproduce the results
    detector_name = 'OCSVM'  # 'OCSVM', 'GMM', 'PCA'
    grid_search_flg = True  # True: to pick the best parameters of the detector
    print_values(detector_name=detector_name, norm_method=norm_method, data_aug=data_aug, random_state=random_state,
                 grid_search_flg=grid_search_flg)

    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    mixed_srcIP = '-'.join(srcIP_lst)
    mixed_iat_file = f'input_data/CICIDS2017/srcIP_{mixed_srcIP}/Friday-WorkingHours/srcIP_{mixed_srcIP}.pcap_IAT.dat'  # raw IATs file
    if os.path.exists(mixed_iat_file):
        os.remove(mixed_iat_file)
    with open(mixed_iat_file, 'wb') as out_hdl:
        for idx, srcIP in enumerate(srcIP_lst):
            IAT_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat'  # raw IATs file
            print(f'*index: {idx}, IAT_file: {IAT_file}')
            with open(IAT_file, 'rb') as in_hdl:
                fids, features, labels = pickle.load(in_hdl)
                pickle.dump((fids, features, labels), out_hdl)

    base_set = 'Baseline'
    mixed_base_file = f'input_data/CICIDS2017/srcIP_{mixed_srcIP}/Friday-WorkingHours/srcIP_{mixed_srcIP}.pcap_{base_set}.dat'  # raw IATs file
    if os.path.exists(mixed_base_file):
        os.remove(mixed_base_file)
    with open(mixed_base_file, 'wb') as out_hdl:
        for idx, srcIP in enumerate(srcIP_lst):
            base_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_{base_set}_' \
                        f'dimension_10.dat'  # baseline features file
            print(f'*index: {idx}, base_file: {base_file}')
            with open(base_file, 'rb') as in_hdl:
                fids, features, labels = pickle.load(in_hdl)
                pickle.dump((fids, features, labels), out_hdl)

    # 1. obtain results (such as ROC and AUC) of IAT or FFT
    quant = 0.9  # to obtain fft_bin from IATs data
    prop_set = 'IAT'  # proposed features:  IAT or FFT
    fft_part = 'real'  # only for FFT: 'real' or 'real+imaginary'
    result_dict_lst = OrderedDict()  # store the results: {feat_set: results of the feat_set}
    prop_file, fft_bin = IAT_to_fixed_out(input_file=mixed_iat_file, feat_set=prop_set, quant=quant,
                                          fft_part=fft_part, overwrite=True)

    prop = Experiment(input_file=prop_file, feat_set=prop_set, norm_method=norm_method, random_state=random_state)
    result_dict = prop.run(detector_name=detector_name,
                           X_train=prop.X_train, y_train=prop.y_train,
                           X_test=prop.X_test, y_test=prop.y_test,
                           grid_search_flg=grid_search_flg)
    result_dict_lst[prop_set] = result_dict

    # 2. obtain results (such as ROC and AUC) of Baseline
    base = Experiment(input_file=mixed_base_file, feat_set=base_set, norm_method=norm_method, random_state=random_state)
    result_dict = base.run(detector_name=detector_name,
                           X_train=base.X_train, y_train=base.y_train,
                           X_test=base.X_test, y_test=base.y_test,
                           grid_search_flg=grid_search_flg)
    result_dict_lst[base_set] = result_dict

    plot_roc_auc(result_dict_lst, title=f'{detector_name}, srcIP:{mixed_srcIP}')


def main_individual():
    norm_method = 'none'  # none: without normalization, otherwise, 'min-max' or 'std'
    data_aug = False  # data_augmentation: if add more normal flows.
    random_state = 42  # to reproduce the results
    detector_name = 'KDE'  # 'OCSVM', 'GMM', 'PCA', 'KDE'
    grid_search_flg = True  # True: to pick the best parameters of the detector
    print_values(detector_name=detector_name, norm_method=norm_method, data_aug=data_aug, random_state=random_state,
                 grid_search_flg=grid_search_flg)

    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    quant = 0.95  # to obtain fft_bin from IATs data
    for idx, srcIP in enumerate(srcIP_lst):
        print(f'\n*index: {idx}, srcIP: {srcIP}, quant (for obtaining fft_bin): {quant}')

        result_dict_lst = OrderedDict()  # store the results: {feat_set: results of the feat_set}

        # 1. obtain results (such as ROC and AUC) of IAT or FFT
        prop_set = 'IAT'  # proposed features:  IAT or FFT
        fft_part = 'real'  # only for FFT: 'real' or 'real+imaginary'
        IAT_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat'  # raw IATs file
        prop_file, fft_bin = IAT_to_fixed_out(input_file=IAT_file, feat_set=prop_set, quant=quant,
                                              fft_part=fft_part, overwrite=True)

        prop = Experiment(input_file=prop_file, feat_set=prop_set, norm_method=norm_method, random_state=random_state)
        result_dict = prop.run(detector_name=detector_name,
                               X_train=prop.X_train, y_train=prop.y_train,
                               X_test=prop.X_test, y_test=prop.y_test,
                               grid_search_flg=grid_search_flg)
        result_dict_lst[prop_set] = result_dict

        # 2. obtain results (such as ROC and AUC) of Baseline
        base_set = 'Baseline'
        base_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_{base_set}_' \
                    f'dimension_10.dat'  # baseline features file
        base = Experiment(input_file=base_file, feat_set=base_set, norm_method=norm_method, random_state=random_state)
        result_dict = base.run(detector_name=detector_name,
                               X_train=base.X_train, y_train=base.y_train,
                               X_test=base.X_test, y_test=base.y_test,
                               grid_search_flg=grid_search_flg)
        result_dict_lst[base_set] = result_dict

        plot_roc_auc(result_dict_lst, title=f'{detector_name}, srcIP:{srcIP}')

        # break


if __name__ == '__main__':
    main_individual()  # individual ip analysis
    # main_mix()        # merge 5 IPs in one
    # main_more_data()    # add Monday data to Friday, and the results are saved in Monday folder
