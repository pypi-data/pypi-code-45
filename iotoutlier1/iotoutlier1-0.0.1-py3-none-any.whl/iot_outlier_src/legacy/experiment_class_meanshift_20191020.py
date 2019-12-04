""" experiment class

"""
# Authors: kun.bj@outlook.com
#
# License: xxx
import pickle
from collections import Counter

import numpy as np
from scipy.spatial import distance
from sklearn.cluster import MeanShift

from data_process import Dataset
from detector.gmm_class import GMMDetector
from detector.kde_class import KDEDetector
from detector.model_selection.grid_search import GridSearch
from detector.ocsvm_class import OCSVMDetector
from detector.pca_class import PCADetector
from utils.tool import stat_data, pprint, check_n_generate_path


# It is a list of strings defining what symbols in a module will be exported
# when from <module> import * is used on the module.
# __all__ = ['Dataset', 'GridSearch', 'main_individual', 'main_mix']


def obtain_means_init(X_train, bandwidth=None):
    ms = MeanShift(bandwidth=bandwidth)
    ms.fit(X_train)

    means_init = ms.cluster_centers_
    labels = ms.labels_
    print(f'mean_shift: {len(Counter(labels))}, {Counter(labels)}')
    # stat_data(Counter(labels.values()), name='Counter(labels) of MeanShift')

    return means_init, len(set(labels))


class IndividualExperiment:

    def __init__(self, input_file, feat_set='', norm_method='std', data_aug=False, shuffle_flg=True, random_state=42):
        """ initialize parameters and get the data from file

        :param input_file:
        :param feat_set:
        :param norm_method:
        :param data_aug:
        :param shuffle_flg: Ture: random select a part of normal data from all normal data to make up of test set
        :param random_state: to reproduce all experimental results
        """

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
        self.X_train, self.X_test = self.data_inst.normalise_data(self.X_train, self.X_test,
                                                                  norm_method=self.norm_method)

        self.data_aug = data_aug
        self.random_state = random_state

    def run(self, detector_name='OCSVM', X_train='', y_train=None, X_test='', y_test='', gridsearch_flg=False):
        """ build detector and get the results

        :param detector_name:
        :param X_train:
        :param y_train:
        :param X_test:
        :param y_test:
        :param gridsearch_flg:
        :return:
        """
        funcparams_dict = {'detector_name': detector_name, 'gridsearch_flg': gridsearch_flg}
        pprint(funcparams_dict, name='run')
        print(f'3) train and test using {detector_name}')
        result_dict = {}

        if gridsearch_flg:
            # find the best parameters of the detector
            if detector_name.upper() == 'OCSVM':
                distances = distance.pdist(X_train, metric='euclidean')
                stat_data(distances.reshape(-1, 1), name='distances')
                q_lst = list(np.linspace(0.0, 1, 501))[1:]  # exclude 0
                sigma_lst = (np.quantile(distances, q=q_lst) ** 2)
                gamma_lst = list(1 / sigma_lst)  # sigma =np.quantile(distances, q=q_lst
                # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(),
                # key=lambda item: item[0])}')
                print(f'gamma_lst:{gamma_lst},\nq_lst: {q_lst}')
                detector = OCSVMDetector(random_state=self.random_state)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'gamma': gamma_lst, 'kernel': ['rbf']})

            elif detector_name.upper() == 'GMM':
                detector = GMMDetector(random_state=self.random_state)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'n_components': [i + 1 for i in range(500)], 'covariance_type': ['diag']})

            elif detector_name.upper() == 'PCA':
                detector = PCADetector(random_state=self.random_state)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'n_components': [i + 1 for i in range(500)]})

            elif detector_name.upper() == 'KDE':
                detector = KDEDetector(random_state=self.random_state)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'bandwidth': list(np.linspace(0.0, 5, 501))[1:]})
            else:
                print(f'detector: {detector_name} is not implemented yet, please check and retry')
                return -1

            grid.fit(X_train, y_train, X_test, y_test)
            self.detector = grid.best_estimator_
            print(f'{detector_name}.params: {self.detector.get_params()}')

            self.detector.test(X_test, y_test)
            # print(f'auc: {detector.auc}')
            result_dict[detector_name] = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                                          'auc': self.detector.auc,
                                          'best_score_': grid.best_score_, 'best_params_': grid.best_params_,
                                          'best_estimator_': grid.best_estimator_
                                          }

        else:  # gridsearch_flg: False
            # rule of thumb in practice
            print('without grid search')
            distances = distance.pdist(X_train, metric='euclidean')
            stat_data(distances.reshape(-1, 1), name='distances')
            q = 0.7
            sigma = np.quantile(distances, q=q)
            print(f'sigma: {sigma}, q (for setting bandwidth in MeanShift): {q}')
            if detector_name.upper() == 'OCSVM':
                gamma = 1 / (sigma ** 2)
                # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(),
                # key=lambda item: item[0])}')
                print(f'gamma: {gamma}, q: {q}, sigma: {sigma}')
                self.detector = OCSVMDetector(gamma=gamma, random_state=self.random_state)

            elif detector_name.upper() == 'GMM':
                means_init, n_components = obtain_means_init(X_train, bandwidth=sigma)
                self.detector = GMMDetector(n_components=n_components, means_init=means_init, covariance_type='diag',
                                            random_state=self.random_state)

            elif detector_name.upper() == 'PCA':
                self.detector = PCADetector(n_components=2, random_state=self.random_state)

            elif detector_name.upper() == 'KDE':
                self.detector = KDEDetector(bandwidth=sigma, random_state=self.random_state)

            else:
                print(f'detector: {detector_name} is not implemented yet, please check and retry')
                return -1

            print(f'{detector_name}.params: {self.detector.get_params()}')
            self.detector.fit(X_train, y_train)
            self.detector.test(X_test, y_test)

            result_dict[detector_name] = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                                          'best_score_': self.detector.auc, 'best_params_': self.detector.get_params(),
                                          'best_estimator_': self.detector
                                          }

        return result_dict

    def dump_model(self, detector, model_file=''):

        check_n_generate_path(file_path=model_file, overwrite=True)

        print(f'model_file: {model_file}')
        with open(model_file, 'wb') as out_hdl:
            pickle.dump(detector, out_hdl)

        return model_file
