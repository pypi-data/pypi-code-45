# Authors: kun.bj@outlook.com
#
# License: xxx
"""
    Purpose: ROC

"""
import pickle
from random import shuffle

from detector.ocsvm_class import OCSVMDetector
from legacy.utils.dataset import stat_data

"""
    Purpose:
        main function for feature set comparison.

"""
from collections import OrderedDict

from _config import *
from legacy.utils import load_and_split_data
from legacy.utils.visualization import plot_roc


def load_and_split_data(merged_file='', trad_set_flg=''):
    # print('1) load data and split it to train set and test set with ratio: 7:3')
    X_train, y_train, X_test, y_test = load_and_split_data(
        test_size=test_size, random_state=random_state)

    print('1) load data and split it to train set and test set, normal and anormaly in test set with ratio: 1:1')
    with open(merged_file, 'rb') as in_hdl:
        features, labels = pickle.load(in_hdl)

    X_normal = []
    y_normal = []
    X_anomaly = []
    y_anomaly = []
    for i, value in enumerate(labels):
        feat = list(features[i][1])  # (fid, IAT)
        if not trad_set_flg:
            if len(feat) > fft_bins:
                feat = feat[:fft_bins]
            else:
                feat += [0] * (fft_bins - len(feat))
        else:
            # nothing need to do
            pass
        if value.upper() in ['NORMAL', 'BENIGN']:
            X_normal.append(feat)
            y_normal.append(0)
        else:
            X_anomaly.append(feat)
            y_anomaly.append(1)

    shuffle_flg = True
    if shuffle_flg:
        c = list(zip(X_normal, y_normal))
        shuffle(c)
        X_normal, y_normal = zip(*c)

    X_normal = np.array(list(X_normal), dtype=float)
    y_normal = np.array(y_normal, dtype=int)
    X_anomaly = np.array(X_anomaly, dtype=float)
    y_anomaly = np.array(y_anomaly, dtype=int)

    train_size = len(y_normal) - len(y_anomaly)
    X_train = X_normal[:train_size, :]
    y_train = y_normal[:train_size]
    X_test = np.concatenate([X_normal[train_size:, :], X_anomaly], axis=0)
    y_test = np.concatenate([y_normal[train_size:], y_anomaly], axis=0)

    return X_train, y_train, X_test, y_test


def main_for_each_feature_set(merged_file='', fft_bins=18, trad_set_flg=True, test_size=0.3, random_state=42,
                              norm_method='std'):
    """

    :param norm_file:
    :param anomaly_file:
    :param test_size:
    :param random_state:
    :return:
    """

    # print('before normalization: X_train distribution:')
    # stat_data(X_train)
    # print('before normalization:X_test distribution:')
    # stat_data(X_test)
    #
    # print(f'--- train set and test set --'
    #       f'\nX_train:{X_train.shape}, y_train:{Counter(y_train)}'
    #       f'\nX_test :{X_test.shape}, y_test :{Counter(y_test)}, in which, 0: normals and 1: anomalies.')
    #
    # print(f'\n2) normalization ({norm_method})')
    # if norm_method == 'min-max':
    #     train_scaler = MinMaxScaler()
    # elif norm_method =='std':
    #     train_scaler = StandardScaler()
    # else:
    #     print('not implemented.')
    #     return -1
    # train_scaler.fit(X_train)
    # X_train = train_scaler.transform(X_train)
    # X_test = train_scaler.transform(X_test)

    print('X_train distribution:')
    stat_data(X_train)
    print('X_test distribution:')
    stat_data(X_test)

    print('\n3) train and test different models')
    roc_dict = {}
    auc_dict = {}

    # gmm = GMMDetector(n_components=3)
    # gmm.train(X_train)
    # # dump(pca, 'output_data/models_dumping/gmm_' + case + '.joblib')
    # # model = load('output_data/models_dumping/gmm_' + case + '.joblib')
    # gmm.test(X_test, y_test)
    # roc_dict['gmm'] = {'y_true': y_test, 'y_scores': gmm.y_scores}
    # auc_dict['gmm']=gmm.auc

    # knn = KNNDetector()
    # knn.train(X_train)
    # # dump(pca, 'output_data/models_dumping/knn_' + case + '.joblib')
    # # model = load('output_data/models_dumping/knn_' + case + '.joblib')
    # knn.test(X_test, y_test)
    # roc_dict['knn'] = {'y_true': y_test, 'y_scores': knn.y_scores}
    # auc_dict['knn'] = knn.auc
    # knn.visualize(X_train[:,:2], y_train, X_test[:,:2], y_test, knn.knn.predict(X_train), knn.knn.predict(X_test), show_figure=True)

    # pca = PCADetector()
    # pca.train(X_train)
    # # dump(pca, 'output_data/models_dumping/pca_' + case + '.joblib')
    # # model = load('output_data/models_dumping/pca_' + case + '.joblib')
    # pca.test(X_test, y_test)
    # roc_dict['pca'] = {'y_true': y_test, 'y_scores': pca.y_scores}
    # auc_dict['pca'] = pca.auc

    ocsvm = OCSVMDetector()
    ocsvm.train(X_train)
    # dump(ocsvm, 'output_data/models_dumping/ocsvm_' + case + '.joblib')
    # model = load('output_data/models_dumping/ocsvm_' + case + '.joblib')
    ocsvm.test(X_test, y_test)
    roc_dict['ocsvm'] = {'y_true': y_test, 'y_scores': ocsvm.y_scores}
    auc_dict['ocsvm'] = ocsvm.auc

    # iforest = IForestDetector()
    # iforest.train(X_train)
    # # dump(ocsvm, 'output_data/models_dumping/iforest_' + case + '.joblib')
    # # model = load('output_data/models_dumping/iforest_' + case + '.joblib')
    # iforest.test(X_test, y_test)
    # roc_dict['iforest'] = {'y_true': y_test, 'y_scores': iforest.y_scores}
    # auc_dict['iforest'] = iforest.auc

    return roc_dict, auc_dict


def seperate_normal_anomaly_file(merged_file=''):
    with open(merged_file, 'rb') as in_hdl:
        features, labels = pickle.load(in_hdl)

    return features, labels


def main_for_roc(srcIP, fft_bins, case='Case 1'):
    """
        "test_size, random_state and so on", all of them come from _config.py.
    :return:
    """
    # flg = True
    # if flg:
    #     select_features_from_list('input_data/demo_dataset/proposed_features/normal_demo_dataset.txt',
    #                               features_lst=[5, 7, 9, 11, 13])
    #     select_features_from_list('input_data/demo_dataset/proposed_features/anomaly_demo_dataset.txt',
    #                               features_lst=[5, 7, 9, 11, 13])
    #     select_features_from_list('input_data/demo_dataset/traditional_features/normal_demo_dataset.txt',
    #                               features_lst=[6, 8, 10, 12, 14])
    #     select_features_from_list('input_data/demo_dataset/traditional_features/anomaly_demo_dataset.txt',
    #                               features_lst=[6, 8, 10, 12, 14])

    # input_files_dict = OrderedDict(
    #     {'prop_set': {'normal_file': 'input_data/demo_dataset/proposed_features/normal_demo_dataset_sub.txt',
    #                   'anomaly_file': 'input_data/demo_dataset/proposed_features/anomaly_demo_dataset_sub.txt'},
    #      'trad_set': {'normal_file': 'input_data/demo_dataset/traditional_features/normal_demo_dataset_sub.txt',
    #                   'anomaly_file': 'input_data/demo_dataset/traditional_features/anomaly_demo_dataset_sub.txt'}})

    if case == 'Case 1':
        input_files_dict = OrderedDict(
            {
                'IAT_set': f'input_data/CICIDS2017/Merged-WorkingHours/5_bots_20170707-09_00-12_00-srcIP_{srcIP}.pcap_IAT.txt',
                'baseline_set': f'input_data/CICIDS2017/Merged-WorkingHours/5_bots_20170707-09_00-12_00-srcIP_{srcIP}.pcap_Baseline.txt'
            })
    else:
        input_files_dict = OrderedDict(
            {
                'FFT_set': f'input_data/CICIDS2017/Merged-WorkingHours/5_bots_20170707-09_00-12_00-srcIP_{srcIP}.pcap_FFT.txt',
                'baseline_set': f'input_data/CICIDS2017/Merged-WorkingHours/5_bots_20170707-09_00-12_00-srcIP_{srcIP}.pcap_Baseline.txt'
            })

    roc_dicts_lst = []
    auc_dicts_lst = []
    for idx, (key, value_dict) in enumerate(input_files_dict.items()):
        print(f'\n{idx}: evaluation on {key} with different detection algorithms.')
        if key == 'baseline_set':
            # fft_bins = 10   # if use this way, the fft_bins will change for all remained cases
            roc_dict, auc_dict = main_for_each_feature_set(merged_file=value_dict, fft_bins=0, trad_set_flg=True,
                                                           test_size=test_size, random_state=random_state,
                                                           norm_method=norm_method)
        else:
            roc_dict, auc_dict = main_for_each_feature_set(merged_file=value_dict, fft_bins=fft_bins,
                                                           trad_set_flg=False,
                                                           test_size=test_size, random_state=random_state,
                                                           norm_method=norm_method)

        roc_dicts_lst.append([key, roc_dict])
        auc_dicts_lst.append([key, auc_dict])

    print('\n3: plot roc.')
    plot_roc(roc_dicts_lst=roc_dicts_lst, title=f'srcIP: {srcIP}, fft_bins: {fft_bins}, {case}')
    # plot_auc_and_strength_of_outiler(auc_dicts_lst=auc_dicts_lst)


if __name__ == '__main__':

    experiment = 'single-device'
    # srcIP = '192.168.10.15'
    case = 'Case 1'  # case1:(IAT VS Baseline),  case 2 (FFT VS Baseline)
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    fft_bins_lst = [16, 19, 19, 21, 18]
    # srcIP_lst = [ '192.168.10.15']
    # fft_bins_lst = [18]

    if experiment == 'single-device':
        for i, (srcIP, fft_bins) in enumerate(zip(srcIP_lst, fft_bins_lst)):
            print(f'srcIP: {srcIP}, fft_bins: {fft_bins}')
            main_for_roc(srcIP, fft_bins, case)

    elif experiment == 'multi-devices':
        X_train = []
        y_train = []
        X_test = []
        y_test = []
        for i, (srcIP, fft_bins) in enumerate(zip(srcIP_lst, fft_bins_lst)):
            print(f'srcIP: {srcIP}, fft_bins: {fft_bins}')
            X_train_i, y_train_i, X_test_i, y_test_i = load_and_split_data(norm_file='', anomaly_file='')
            X_train = np.concatenate([X_train, X_train_i], axis=0)
            y_train = np.concatenate([y_train, y_train_i], axis=0)
            X_test = np.concatenate([X_test, X_test_i], axis=0)
            X_train = np.concatenate([y_test_i, y_test_i], axis=0)
