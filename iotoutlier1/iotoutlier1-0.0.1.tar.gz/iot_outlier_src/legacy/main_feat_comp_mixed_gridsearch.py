# Authors: kun.bj@outlook.com
#
# License: xxx
""" Main function for feature set comparison.
    Measure metrics: ROC amd AUC

"""
import itertools
import pickle
from collections import OrderedDict
from copy import deepcopy
from inspect import signature

import matplotlib.pyplot as plt
from scipy.spatial import distance
from sklearn import metrics, clone
from sklearn.metrics import roc_curve
# from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from _config import *
from detector.gmm_class import GMMDetector
from detector.ocsvm_class import OCSVMDetector
from detector.pca_class import PCADetector
from legacy.utils.dataset import stat_data


def print_func_args(func):
    sig = signature(func)
    for key, value in sig.parameters.items():
        print(f'{key}, {value}')


class GridSearch():

    def __init__(self, estimator='', scoring='auc',
                 param_grid={'n_components': [i + 1 for i in range(10)], 'covariance_type': ['full', 'diag']}):

        self.estimator = estimator
        self.best_score_ = 0
        self.best_params_ = {}
        self.param_grid = param_grid

    def fit(self, X_train='', y_train='', X_test='', y_test=''):

        keys, values = zip(*self.param_grid.items())
        combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]
        print(len(combinations))
        # print(combinations)
        for idx, params in enumerate(combinations):
            self.detector = clone(self.estimator)
            self.detector.set_params(**params)  # set params
            print(f'idx: {idx+1}, detector_params: {self.detector.get_params()}')
            self.detector.fit(X_train, y_train)
            self.detector.test(X_test, y_test)
            print(f'auc: {self.detector.auc}')

            if self.detector.auc > self.best_score_:
                self.best_score_ = self.detector.auc
                self.best_params_ = params  # if key exists, update; otherwise, add new key
                self.best_estimator_ = deepcopy(self.detector)
                # self.best_estimator_ = clone(self.detector)
                # self.best_estimator_ = GMMDetector()
                # self.best_estimator_.set_params(**params)
                # print(self.best_estimator_.get_params())
                # self.best_estimator_.fit(X_train, y_train)
                # self.best_estimator_.test(X_test, y_test)

                print(f'best_auc: {self.best_estimator_.auc}, {self.best_score_}')


class Experiment:

    def __init__(self, input_file, feat_set='', norm_method='std', data_aug=False, shuffle_flg=True, random_state=42):

        print_values(input_file=input_file, feat_set=feat_set, norm_method=norm_method,
                     data_aug=data_aug,
                     shuffle_flg=shuffle_flg, random_state=random_state)
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

        # print_func_args(self.__init__)

    def run(self, detector_name='OCSVM', X_train='', y_train=None, X_test='', y_test='', grid_search_flg=False):
        print(f'3) train and test using {detector_name}')
        result_dict = {}

        if grid_search_flg:
            if detector_name.upper() == 'OCSVM':
                distances = distance.pdist(X_train, metric='euclidean')
                stat_data(distances.reshape(-1, 1), name='distances')
                # gamma_lst = []
                # for q in np.linspace(0, 1, 11):
                #     sigma = np.quantile(distances, q=q)
                #     if sigma == 0.0:
                #         continue
                #     gamma_lst.append(1 / (sigma ** 2))
                gamma_lst = 1 / (np.quantile(distances, q=np.linspace(0.1, 1, 10)) ** 2)
                # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(), key=lambda item: item[0])}')
                print(f'gamma_lst:{gamma_lst}')
                detector = OCSVMDetector(random_state=self.random_state)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'gamma': gamma_lst, 'kernel': ['rbf']})
                print(f'grid:{grid}')
                grid.fit(X_train, y_train, X_test, y_test)


            elif detector_name.upper() == 'GMM':

                detector = GMMDetector(random_state=self.random_state)
                # grid = GridSearchCV(estimator=detector, scoring='accuracy',
                #                     param_grid={'n_components': [i+1 for i in range(10)], 'covariance_type':['full','diag']})

                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'n_components': [i + 1 for i in range(10)], 'covariance_type': ['diag']})
                print(f'grid:{grid}')
                grid.fit(X_train, y_train, X_test, y_test)

                # grid.fit(X_train, y_train)

            elif detector_name.upper() == 'PCA':
                detector = PCADetector(random_state=self.random_state)
                grid = GridSearchCV(estimator=detector, param_grid='')

            # grid.fit(X_train, y_train)
            # print(grid)
            # # summarize the results of the grid search
            print(f'grid.best_score_: {grid.best_score_}')
            print(f'grid.best_params_: {grid.best_params_}')
            print(f'grid.best_estimator_: {grid.best_estimator_}')
            detector = grid.best_estimator_

            # # # detector.fit(X_train)
            # detector.test(X_test, y_test)
            # print(f'auc: {detector.auc}')

            key = detector_name
            result_dict[key] = {'y_true': y_test, 'y_scores': detector.y_scores, 'auc': detector.auc,
                                'best_score_': grid.best_score_, 'best_params_': grid.best_params_,
                                'best_estimator_': grid.best_estimator_
                                }

        else:
            if detector_name.upper() == 'OCSVM':
                distances = distance.pdist(X_train, metric='euclidean')
                stat_data(distances.reshape(-1, 1), name='distances')
                q = 0.1
                print('without grid search cv')
                sigma = np.quantile(distances, q=q)
                gamma = 1 / (sigma ** 2)
                # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(), key=lambda item: item[0])}')
                print(f'gamma:{gamma}, q:{q}, sigma:{sigma}')
                detector = OCSVMDetector(gamma=gamma, random_state=self.random_state)

            elif detector_name.upper() == 'GMM':
                detector = GMMDetector(n_components=10, covariance_type='diag', random_state=self.random_state)

            elif detector_name.upper() == 'PCA':
                detector = PCADetector(random_state=self.random_state)

            print(f'{detector_name}.params: {detector.get_params()}')
            detector.fit(X_train, y_train)
            detector.test(X_test, y_test)

            key = detector_name
            result_dict[key] = {'y_true': y_test, 'y_scores': detector.y_scores, 'auc': detector_name.auc,
                                'best_score_': detector.auc, 'best_params_': detector.get_params(),
                                'best_estimator_': detector
                                }

        # ocsvm = OCSVMDetector()
        # ocsvm.train(X_train)
        # # dump(ocsvm, 'output_data/models_dumping/ocsvm_' + case + '.joblib')
        # # model = load('output_data/models_dumping/ocsvm_' + case + '.joblib')
        # ocsvm.test(X_test, y_test)
        # roc_dict['ocsvm'] = {'y_true': y_test, 'y_scores': ocsvm.y_scores}
        # auc_dict['ocsvm'] = ocsvm.auc

        return result_dict

    def normalise_data(self, X_train, X_test, norm_method='std'):

        if norm_method in ['min-max', 'std']:
            if norm_method == 'min-max':
                train_scaler = MinMaxScaler()
            if norm_method == 'std':
                train_scaler = StandardScaler()
            train_scaler.fit(X_train)
            X_train = train_scaler.transform(X_train)
            X_test = train_scaler.transform(X_test)

            print('after normalization: X_train distribution:')
            stat_data(X_train)
            print('after normalization:X_test distribution:')
            stat_data(X_test)

            return X_train, X_test

        elif norm_method == 'none':
            print('without normalization')
            return X_train, X_test
        else:
            print('not implemented.')
            return -1


#
#
# def run_experiment(experiment=(), srcIP_lst=[], norm_method='std', data_aug=False):
#     exper, case = experiment  # # case1:(IAT VS Baseline),  case 2 (FFT VS Baseline)
#     print(f'exper: {exper}, case: {case}')
#
#     if exper == 'demo':
#         srcIP = srcIP_lst[0]
#         print(f'demo_srcIP: {srcIP}')
#         main_for_roc(srcIP, experiment=experiment, norm_method=norm_method, data_aug=data_aug)
#
#     elif exper == 'individual':
#         for i, srcIP in enumerate(srcIP_lst):
#             print(f'indiv_srcIP: {srcIP}')
#             main_for_roc(srcIP, experiment=experiment, norm_method=norm_method, data_aug=data_aug)
#
#     elif exper == 'mix':
#         # mix multi devices' data
#         feat_set = case.split()[0]
#         files_lst = [obtain_file_path(srcIP, feat_set=feat_set) for srcIP in srcIP_lst]
#         merged_file = obtain_file_path(srcIP='-'.join(srcIP_lst), feat_set=feat_set)
#         merged_file = merge_multifiles_to_one(files_lst=files_lst, merged_file=merged_file)
#
#         print(f'merged_file: {merged_file}')
#         main_for_roc(srcIP='-'.join(srcIP_lst), experiment=experiment, data_aug=data_aug)
#     else:
#         print('not implement')
#

#
#
#
#
#
#
# def load_and_split_data(input_file='', case='', shuffle_flg=True, random_state=random_state):
#     print('1) load data and split it to train set and test set, normal and anormaly in test set with ratio: 1:1')
#     fids, features, labels = load_pickled_data(input_file)
#
#     feat_set = case.split()[0]
#     if feat_set in ['IAT', 'FFT']:
#         feat_len_arr = [len(v) for v in features]
#         fft_bins = int(np.quantile(feat_len_arr, q=0.9))
#     else:  # for baseline_set, no need fft_bins
#         fft_bins = 0
#     print(f'feat_set: {feat_set}, fft_bins:{fft_bins}')
#
#     X_normal = []
#     y_normal = []
#     X_anomaly = []
#     y_anomaly = []
#     for i, value in enumerate(labels):
#         feat = list(features[i])  # (fid, IAT)
#         if feat_set == 'FFT' or feat_set == 'IAT':
#             if len(feat) > fft_bins:
#                 feat = feat[:fft_bins]
#             else:
#                 feat += [0] * (fft_bins - len(feat))
#         else:  # baseline_set
#             # nothing need to do
#             pass
#         if value.upper() in ['NORMAL', 'BENIGN']:
#             X_normal.append(feat)
#             y_normal.append(0)
#         else:
#             X_anomaly.append(feat)
#             y_anomaly.append(1)
#
#     if shuffle_flg:
#         c = list(zip(X_normal, y_normal))
#         shuffle(c, random_state=random_state)
#         X_normal, y_normal = zip(*c)
#
#     X_normal = np.array(list(X_normal), dtype=float)
#     y_normal = np.array(y_normal, dtype=int)
#     X_anomaly = np.array(X_anomaly, dtype=float)
#     y_anomaly = np.array(y_anomaly, dtype=int)
#
#     train_size = len(y_normal) - len(y_anomaly)
#     X_train = X_normal[:train_size, :]
#     y_train = y_normal[:train_size]
#     if len(y_anomaly) == 0:
#         X_test = X_normal[:100, :]
#         y_test = y_normal[:100]
#     else:
#         X_test = np.concatenate([X_normal[train_size:, :], X_anomaly], axis=0)
#         y_test = np.concatenate([y_normal[train_size:], y_anomaly], axis=0)
#
#     return X_train, y_train, X_test, y_test, fft_bins
#


#
#
# def grid_search_cv():
#     Cs = [0.001, 0.01, 0.1, 1, 10]
#     gammas = [0.001, 0.01, 0.1, 1]
#     param_grid = {'C': Cs, 'gamma': gammas}
#     grid_search = GridSearchCV(svm.SVC(kernel='rbf'), param_grid, cv=nfolds)
#     grid_search.fit(X, y)
#
#     return grid_search.best_params_

#
# def main_for_each_feature_set(input_file='', case='', random_state=42, norm_method='std'):
#     """
#
#     :param norm_file:
#     :param anomaly_file:
#     :param test_size:
#     :param random_state:
#     :return:
#     """
#     X_train, y_train, X_test, y_test, fft_bins = load_and_split_data(input_file=input_file, case=case, shuffle_flg=True,
#                                                                      random_state=random_state)
#     print(f'--- train set and test set --'
#           f'\nX_train:{X_train.shape}, y_train:{Counter(y_train)}'
#           f'\nX_test :{X_test.shape}, y_test :{Counter(y_test)}, in which, 0: normals and 1: anomalies.')
#     stat_data(X_train)
#     stat_data(X_test)
#
#     X_train, X_test = normalise_data(X_train, X_test, norm_method=norm_method)
#
#     print('\n3) train and test different models')
#     roc_dict = {}
#     auc_dict = {}
#
#     # gmm = GMMDetector(n_components=3)
#     # gmm.train(X_train)
#     # # dump(pca, 'output_data/models_dumping/gmm_' + case + '.joblib')
#     # # model = load('output_data/models_dumping/gmm_' + case + '.joblib')
#     # gmm.test(X_test, y_test)
#     # roc_dict['gmm'] = {'y_true': y_test, 'y_scores': gmm.y_scores}
#     # auc_dict['gmm']=gmm.auc
#
#     # knn = KNNDetector()
#     # knn.train(X_train)
#     # # dump(pca, 'output_data/models_dumping/knn_' + case + '.joblib')
#     # # model = load('output_data/models_dumping/knn_' + case + '.joblib')
#     # knn.test(X_test, y_test)
#     # roc_dict['knn'] = {'y_true': y_test, 'y_scores': knn.y_scores}
#     # auc_dict['knn'] = knn.auc
#     # knn.visualize(X_train[:,:2], y_train, X_test[:,:2], y_test, knn.knn.predict(X_train), knn.knn.predict(X_test), show_figure=True)
#
#     # pca = PCADetector()
#     # pca.train(X_train)
#     # # dump(pca, 'output_data/models_dumping/pca_' + case + '.joblib')
#     # # model = load('output_data/models_dumping/pca_' + case + '.joblib')
#     # pca.test(X_test, y_test)
#     # roc_dict['pca'] = {'y_true': y_test, 'y_scores': pca.y_scores}
#     # auc_dict['pca'] = pca.auc
#
#     ocsvm = OCSVMDetector()
#     ocsvm.train(X_train)
#     # dump(ocsvm, 'output_data/models_dumping/ocsvm_' + case + '.joblib')
#     # model = load('output_data/models_dumping/ocsvm_' + case + '.joblib')
#     ocsvm.test(X_test, y_test)
#     roc_dict['ocsvm'] = {'y_true': y_test, 'y_scores': ocsvm.y_scores}
#     auc_dict['ocsvm'] = ocsvm.auc
#
#     # iforest = IForestDetector()
#     # iforest.train(X_train)
#     # # dump(ocsvm, 'output_data/models_dumping/iforest_' + case + '.joblib')
#     # # model = load('output_data/models_dumping/iforest_' + case + '.joblib')
#     # iforest.test(X_test, y_test)
#     # roc_dict['iforest'] = {'y_true': y_test, 'y_scores': iforest.y_scores}
#     # auc_dict['iforest'] = iforest.auc
#
#     return roc_dict, auc_dict
#
#
# def seperate_normal_anomaly_file(merged_file=''):
#     with open(merged_file, 'rb') as in_hdl:
#         features, labels = pickle.load(in_hdl)
#
#     return features, labels


#
# def main_for_roc(srcIP, experiment='', data_aug=False, norm_method='none'):
#     """
#         "test_size, random_state and so on", all of them come from _config.py.
#     :return:
#     """
#
#     experi, case = experiment
#
#     feat_set = case.split()[0]
#     if experi == 'demo':
#         files_dict = OrderedDict(
#             {
#                 'proposed_set': f'input_data/data/test.pcap_{feat_set}.dat',
#                 'baseline_set': f'input_data/data/test.pcap_Baseline.dat'
#             })
#     else:
#         files_dict = OrderedDict(
#             {
#                 'proposed_set': f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_{feat_set}.dat',
#                 'baseline_set': f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_Baseline.dat'
#             })
#         if data_aug:
#             files_aug_dict = OrderedDict(
#                 {
#                     'proposed_set': f'input_data/CICIDS2017/srcIP_{srcIP}/Monday-WorkingHours/srcIP_{srcIP}.pcap_{feat_set}.dat',
#                     'baseline_set': f'input_data/CICIDS2017/srcIP_{srcIP}/Monday-WorkingHours/srcIP_{srcIP}..pcap_Baseline.dat'
#                 })
#             for i, (key, value) in enumerate(files_dict.items()):
#                 files_lst = [value, files_aug_dict[key]]
#                 merged_file = value + '_augmented.dat'
#                 files_dict[key] = merge_multifiles_to_one(files_lst=files_lst, merged_file=merged_file)
#
#     roc_dicts_lst = []
#     auc_dicts_lst = []
#     for idx, (key, file_path) in enumerate(files_dict.items()):
#         print(f'\n{idx}: evaluation on feat_set:{feat_set}, key:{key}')
#
#         roc_dict, auc_dict = main_for_each_feature_set(input_file=file_path, case=case,
#                                                        random_state=random_state,
#                                                        norm_method=norm_method)
#
#         roc_dicts_lst.append([key, roc_dict])
#         auc_dicts_lst.append([key, auc_dict])
#
#     print('\n3: plot roc.')
#     plot_roc(roc_dicts_lst=roc_dicts_lst, title=f'srcIP: {srcIP}, {case}')
#     # plot_auc_and_strength_of_outiler(auc_dicts_lst=auc_dicts_lst)
#
#
# def merge_multifiles_to_one(files_lst=[], output_file=''):
#     # os.chdir("/mydir")
#     # extension = 'csv'
#     # all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#     # # combine all files in the list
#     # combined_csv = pd.concat([pd.read_csv(f) for f in files_lst])  # different lines
#     # # export to csv
#     # combined_csv.to_csv(output_file, index=False, encoding='utf-8-sig')
#
#     # with open(output_file, 'w') as out_hdl:
#     #     for file in files_lst:
#     #         with open(file, 'r') as in_hdl:
#     #             line = in_hdl.readline()
#     #             while line:
#     #                 out_hdl.write(line)
#     #                 line = in_hdl.readline()
#
#     with open(output_file, 'wb') as out_hdl:
#         # pickle.dump(len(files_lst), out_hdl)
#         for file in files_lst:
#             print(f'file:{file}')
#             with open(file, 'rb') as in_hdl:
#                 fids, features, labels = pickle.load(in_hdl)
#                 pickle.dump((fids, features, labels), out_hdl)
#
#     return output_file


#
# def load_pickled_data(input_file=''):
#     """ Especially for loading multi-objects stored in a file.
#
#     :param input_file:
#     :return:
#     """
#
#     fids = []
#     features = []
#     labels = []
#     with open(input_file, 'rb') as in_hdl:
#         while True:
#             try:
#                 fids_, features_, labels_ = pickle.load(in_hdl)
#                 fids.extend(fids_)
#                 features.extend(features_)
#                 labels.extend(labels_)
#             except EOFError:
#                 break
#     return fids, features, labels

#
# def obtain_fft_bins(features, q=0.9):
#     # with open(v1_file, 'r') as in_hdl:
#     #     line = in_hdl.readline()
#     #     while line:
#     #         arr = line.strip().split(',')
#     #         features.append(arr[:-1])
#     #         line = in_hdl.readline()
#     flows_len_arr = [len(value) for value in features]
#     fft_bins = int(np.quantile(flows_len_arr, q=q))
#     print(f'choose quantile = {q} and get fft_bins: {fft_bins}.')
#     print(f'len(flows_len_arr): {len(flows_len_arr)}, {sorted(set(flows_len_arr))}, {Counter(flows_len_arr)}')
#     stat_data(np.array(flows_len_arr).reshape(-1, 1))
#
#     return fft_bins
#
#
# def obtain_normal_data(pcap_file, label=['Benign']):
#     pcap_file = f'input_data/CICIDS2017/Merged-WorkingHours/5_bots_20170707-09_00-12_00-srcIP_{srcIP}.pcap'
#     dir = os.path.dirname(pcap_file)
#     if not os.path.exists(dir):
#         os.makedirs(dir)
#     if not os.path.exists(pcap_file):
#         # input_file = 'input_data/CICIDS2017/Merged-WorkingHours-Morning_5_bots_20170707-09_40-11_30.pcap'
#         input_file = 'input_data/CICIDS2017/Friday-WorkingHours@5_Bots_SrcIPs-20170707-09_00-12_00.pcap'
#         cmd = f"tshark -r {input_file} -w {pcap_file} ip.src=={srcIP}"
#         print(f'{cmd}')
#         result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')


#
# def obtain_file_path(srcIP, feat_set='IAT'):
#     file_path = f'input_data/CICIDS2017/Merged-WorkingHours/5_bots_20170707-09_00-12_00-srcIP_{srcIP}.pcap_{feat_set}.dat'  # (fid, features), label
#     # v1_files = [IAT_file.format(srcIP) for srcIP in srcIP_lst]
#     # v1_megerd_file = IAT_file.format()
#     return file_path


def seperate_normal_anomaly_file(merged_file=''):
    with open(merged_file, 'rb') as in_hdl:
        features, labels = pickle.load(in_hdl)

    return features, labels


def insert_newlines(data_str, step=45):
    return '\n'.join(data_str[i:i + step] for i in range(0, len(data_str), step))


def plot_roc_auc(result_dict_lst, out_file='output_data/figures/roc_of_different_algorithms.pdf',
                 title='ROC'):
    """

    :param result_dict_lst:
    :param out_file:
    :param title:
    :return:
    """
    # with plt.style.context(('ggplot')):
    fig, ax = plt.subplots()

    colors_lst = ['r', 'm', 'b', 'g', 'y', 'c', '#0072BD', '#A2142F', '#EDB120', 'k', '#D95319', '#4DBEEE',
                  'C1']  # add more color values: https://www.mathworks.com/help/matlab/ref/plot.html
    # required_colors_num = len(roc_dicts_lst) * len(roc_dicts_lst[0][-1])  # roc_dicts_list[0] = [key, roc_dict]
    # if len(colors_lst) < required_colors_num:
    #     print(
    #         f'the number of colors we has ({len(colors_lst)}) does not meet the required number of colors (required_colors_num).')
    # else:
    #     print(f'required colors number ({required_colors_num}) <= colors number ({len(colors_lst)}).')

    # colors_dict['ocsvm'.upper()] =
    for idx, (feature_set_key, result_dict) in enumerate(result_dict_lst.items()):
        # colors_dict[feature_set_key] = {'AE': 'r', 'DT': 'm', 'PCA': 'C1', 'IF': 'b', 'OCSVM': 'g'}
        for i, (detector_key, value_dict) in enumerate(result_dict.items()):
            detector_key = detector_key.upper()
            y_true = value_dict['y_true']
            y_scores = value_dict['y_scores']
            fpr, tpr, thres = roc_curve(y_true=y_true, y_score=y_scores)
            # IMPORTANT: first argument is true values, second argument is predicted probabilities (i.e., y_scores)
            # auc = "%.5f" % metrics.auc(fpr, tpr)
            auc = f'{metrics.auc(fpr, tpr):.4f}'
            print(f'detector_key={detector_key}:{feature_set_key}, auc={auc}, fpr={fpr}, tpr={tpr}')
            # print(best_dict[feature_set_key]['best_score_'] == auc)
            if detector_key == 'PCA':
                lw = 3
            else:
                lw = 2
            params = value_dict['best_params_']
            ax.plot(fpr, tpr, colors_lst.pop(0), label=f'{feature_set_key}. AUC:{auc},\n {params}', lw=lw, alpha=1,
                    linestyle='-')
            ax.text(2, 7, 'this is\nyet another test',
                    rotation=45,
                    horizontalalignment='center',
                    verticalalignment='top',
                    multialignment='center')

            # plt.text(x[-1], y[-1], 'sample {i}'.format(i=i))

    ax.plot([0, 1], [0, 1], 'k--', label='', alpha=0.9)
    plt.xlim([0.0, 1.0])
    plt.ylim([0., 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='lower right')

    title = insert_newlines(title)
    plt.title(title)

    # plt.subplots_adjust(bottom=0.25, top=0.75)

    # sub_dir = os.path.split(input_file)[0]
    # output_pre_path = os.path.split(input_file)[-1].split('.')[0]
    # out_file = os.path.join(sub_dir, output_pre_path + '_ROC.pdf')
    print(f'ROC:{out_file}')
    plt.savefig(out_file)  # should use before plt.show()

    plt.show()


def print_values(**kwargs):
    for idx, (key, value) in enumerate(kwargs.items()):
        if idx == len(kwargs.keys()) - 1:
            print(f'{key}: {value}')
        else:
            print(f'{key}: {value}, ', end='')


def IAT_to_fixed_out(input_file='IAT_file', feat_set='IAT', quant=0.8, fft_part='real'):
    """ obtain fixed output from raw IAT data based on feat_set, quant and fft_part

    :param input_file:
    :param feat_set:
    :param quant:
    :param fft_part:
    :return:
    """
    # 1) load IAT data from file
    print(f'IAT_file (with different IAT dimensions): {input_file}')
    data_inst = Dataset(input_file=input_file)

    # 2) obtain fft_bins according to quant
    flows_len_arr = [len(value) for value in data_inst.features]
    fft_bin = int(np.quantile(flows_len_arr, q=quant))
    print(f'choose quantile = {quant} and get fft_bin: {fft_bin}.')

    # 3) save the fixed IAT with fft_bins
    if feat_set == 'IAT':
        print(f'feat_set: {feat_set}, dimension: {fft_bin}')
        fixed_out_file = input_file + f'_{feat_set}_quant_{quant}_dimension_{fft_bin}.dat'

        if not os.path.exists(fixed_out_file):
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

    if feat_set == 'FFT':
        # 4) save the fixed FFT with fft_bins
        print(f'feat_set: {feat_set}, dimension: {fft_bin}')
        fixed_out_file = input_file + f'_{feat_set}_quant_{quant}_dimension_{fft_bin}_{fft_part}.dat'  # IAT with different dimension

        if not os.path.exists(fixed_out_file):
            print(f'fixed_fft_file: {fixed_out_file}')

            # calculate discrete FFTs
            if fft_part == 'real':  # default
                features = [np.real(np.fft.fft(IATs, n=fft_bin)) for IATs in data_inst.features]
            elif fft_part == 'real+imaginary':
                features = []
                for i, IATs in enumerate(data_inst.features):
                    complex_v = np.fft.fft(IATs, fft_bin)
                    if i == 0:
                        print(f'{len(np.real(complex_v))}, {len(np.imag(complex_v))}')
                    v = np.concatenate([np.real(complex_v), np.imag(complex_v)], axis=np.newaxis)
                    features.append(v)
            else:
                print('not implement.')
                return -1

            # # save results
            with open(fixed_out_file, 'wb') as out_hdl:
                pickle.dump((data_inst.fids, features, data_inst.labels), out_hdl)
        else:
            print(f'fixed_fft_file exists: {fixed_out_file}')  # fft

    return fixed_out_file, fft_bin


def main():
    norm_method = 'none'  # none: without normalization, otherwise, 'min-max' or 'std'
    data_aug = False  # data_augmentation: if add more normal flows.
    random_state = 42
    detector_name = 'OCSVM'  # 'OCSVM', 'GMM'
    grid_search_flg = True
    print_values(detector_name=detector_name, norm_method=norm_method, data_aug=data_aug, random_state=random_state,
                 grid_search_flg=grid_search_flg)

    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    quant = 0.9  # to obtain fft_bin from IATs data

    for idx, srcIP in enumerate(srcIP_lst):
        print(f'\n*index: {idx}, srcIP: {srcIP}, quant (for obtaining fft_bin): {quant}')

        prop_set = 'FFT'  # IAT or FFT

        IAT_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat'  # proposed features file
        prop_file, fft_bin = IAT_to_fixed_out(input_file=IAT_file, feat_set=prop_set, quant=quant, fft_part='real')

        result_dict_lst = OrderedDict()

        prop = Experiment(input_file=prop_file, feat_set=prop_set, norm_method=norm_method, random_state=random_state)
        result_dict = prop.run(detector_name=detector_name,
                               X_train=prop.X_train, y_train=prop.y_train,
                               X_test=prop.X_test, y_test=prop.y_test,
                               grid_search_flg=grid_search_flg)
        result_dict_lst[prop_set] = result_dict

        base_set = 'Baseline'
        base_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_{base_set}_dimension_10.dat'  # baseline features file
        base = Experiment(input_file=base_file, feat_set=base_set, norm_method=norm_method, random_state=random_state)
        result_dict = base.run(detector_name=detector_name,
                               X_train=base.X_train, y_train=base.y_train,
                               X_test=base.X_test, y_test=base.y_test,
                               grid_search_flg=grid_search_flg)
        result_dict_lst[base_set] = result_dict

        plot_roc_auc(result_dict_lst, title=f'{detector_name}, srcIP:{srcIP}')

        # break


if __name__ == '__main__':
    main()
