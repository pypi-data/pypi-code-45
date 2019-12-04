""" experiment class
    from QuickshiftPP import QuickshiftPP
"""
# Authors: kun.bj@outlook.com
#
# License: xxx
import pickle
# from QuickshiftPP import QuickshiftPP   # it's the right way to use pyx file after building and installing
from QuickshiftPP import QuickshiftPP
from collections import Counter

import numpy as np
from scipy.spatial import distance
from sklearn.cluster import MeanShift

# from data_process.dataset import Dataset
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

    return means_init, len(set(labels))


def diagonalize_matrix(A):
    w, v = np.linalg.eig(A)
    idx = w.argsort()[::-1]  # large to small
    # idx = w.argsort() #small to large
    w = w[idx]
    v = v[:, idx]

    return w


def obtain_means_init_quickshift_pp(X_train, k=''):
    """
        1) Download quickshift++ from github
        2) unzip and move the folder to your project
        3) python3 setup.py build
        4) python3 setup.py install
        5) from QuickshiftPP import QuickshiftPP
    :param X_train:
    :param k:
    :return:
    """
    # Declare a Quickshift++ model with tuning hyperparameters.
    if k == '':
        k = int(np.round(np.log(len(X_train)) ** 2))

    print(f'k:{k}')
    if k > len(X_train):
        print(f'k: {k} > len(X_train)-10: {len(X_train)-10}')
        k = len(X_train) - 10  # -10: for some unknown cases in QuickshiftPP
    beta = 0.999
    model = QuickshiftPP(k=k, beta=beta)
    print(f'k: {k}, beta: {beta}')
    # k: number of neighbors in k-NN
    # beta: fluctuation parameter which ranges between 0 and 1.

    # Compute the clustering.
    model.fit(X_train)
    labels_ = model.memberships
    cluster_centers_ = []
    for i in range(np.max(labels_) + 1):
        ind_i = np.where(labels_ == i)[0]  # get index of each cluster
        cluster_i_center = np.mean(X_train[ind_i], axis=0)  # get center of each cluster
        cluster_centers_.append(cluster_i_center)

    means_init = np.asarray(cluster_centers_, dtype=float)
    # covariances = diagonalize_matrix(np.cov(X_train))  # M=PDP^(-1)

    print(f'quickshift: {len(Counter(labels_))}, {Counter(labels_)}')

    return means_init, len(set(labels_))


class IndividualExperiment:

    def __init__(self, input_file, feat_set='', norm_method='std', data_aug=False,
                 shuffle_flg=True, random_state=42, verbose=True):
        """ initialize parameters and get the data from file

        :param input_file:
        :param feat_set:
        :param norm_method:
        :param data_aug:
        :param shuffle_flg: Ture: random select a part of normal data from all normal data to make up of test set
        :param random_state: to reproduce all experimental results
        """

        self.feat_set = feat_set

        print(f'1) load {input_file} and split train and test set')
        self.data_inst = Dataset(input_file)
        self.X_train, self.y_train, self.X_test, self.y_test = self.data_inst.split_train_test(
            features=self.data_inst.features,
            labels=self.data_inst.labels,
            shuffle_flg=shuffle_flg,
            random_state=random_state)

        self.norm_method = norm_method

        # self.X_train, self.X_test = self.data_inst.normalise_data(self.X_train, self.X_test,
        #                                                           norm_method=self.norm_method)

        self.data_aug = data_aug
        self.random_state = random_state
        self.verbose = verbose

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
        if self.verbose:
            funcparams_dict = {'detector_name': detector_name, 'gridsearch_flg': gridsearch_flg}
            pprint(funcparams_dict, name='run')
            # print(f'3) train and test using {detector_name}')
        result_dict = {}

        norm_X_train, norm_X_test = self.data_inst.normalise_data(X_train, X_test,
                                                                  norm_method=self.norm_method)

        if gridsearch_flg:
            print(f'with grid search: {detector_name.upper()}, gridsearch_flg: {gridsearch_flg}')
            # find the best parameters of the detector
            if detector_name.upper() == 'OCSVM':
                distances = distance.pdist(norm_X_train, metric='euclidean')
                stat_data(distances.reshape(-1, 1), name='distances')
                q_lst = list(np.linspace(0.0, 1, 20))[1:]  # exclude 0
                sigma_lst = np.quantile(distances, q=q_lst)
                gamma_lst = list(1 / sigma_lst ** 2)  # sigma =np.quantile(distances, q=q_lst
                # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(),
                # key=lambda item: item[0])}')
                print(f'gamma_lst:{gamma_lst},\nq_lst: {q_lst},\nsigma_lst: {sigma_lst}')
                detector = OCSVMDetector(random_state=self.random_state, verbose=self.verbose)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'gamma': gamma_lst, 'kernel': ['rbf']})
                X_train = norm_X_train
                X_test = norm_X_test

            elif detector_name.upper() == 'GMM':
                detector = GMMDetector(random_state=self.random_state, verbose=self.verbose)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'n_components': [i + 1 for i in range(50)], 'covariance_type': ['diag']})

            elif detector_name.upper() == 'PCA':
                detector = PCADetector(random_state=self.random_state, verbose=self.verbose)
                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'n_components': [i + 1 for i in range(100)]})

            elif detector_name.upper() == 'KDE':
                distances = distance.pdist(norm_X_train, metric='euclidean')
                stat_data(distances.reshape(-1, 1), name='distances')
                q_lst = list(np.linspace(0.0, 1, 20))[1:]  # exclude 0
                sigma_lst = np.quantile(distances, q=q_lst)
                print(f'q_lst: {q_lst},\nsigma_lst:{list(sigma_lst)}')

                detector = KDEDetector(random_state=self.random_state, verbose=self.verbose)
                # grid = GridSearch(estimator=detector, scoring='auc',
                #                   param_grid={'bandwidth': list(np.linspace(0.0, 5, 501))[1:]})

                grid = GridSearch(estimator=detector, scoring='auc',
                                  param_grid={'bandwidth': sigma_lst})

                X_train = norm_X_train
                X_test = norm_X_test

            else:
                print(f'detector: {detector_name} is not implemented yet, please check and retry')
                return -1

            grid.fit(X_train, y_train, X_test, y_test)
            self.detector = grid.best_estimator_
            print(f'{detector_name}.params: {self.detector.get_params()}')

            self.detector.test(X_test, y_test)
            print(f'auc: {self.detector.auc}')
            result_dict[detector_name] = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                                          'auc': self.detector.auc,
                                          'best_score_': grid.best_score_, 'best_params_': grid.best_params_,
                                          'best_estimator_': grid.best_estimator_
                                          }

        else:  # gridsearch_flg: False
            # rule of thumb in practice
            print('without grid search')

            if detector_name.upper() == 'OCSVM':
                distances = distance.pdist(norm_X_train, metric='euclidean')
                stat_data(distances.reshape(-1, 1), name='distances')
                q = 0.3
                sigma = np.quantile(distances, q=q)
                if sigma == 0:  # find a new non-zero sigma
                    print(f'sigma: {sigma}, q: {q}')
                    q_lst = list(np.linspace(q + 0.01, 1, 20))
                    sigma_lst = np.quantile(distances, q=q_lst)
                    sigma, q = [(s_v, q_v) for (s_v, q_v) in zip(sigma_lst, q_lst) if s_v > 0][0]
                print(f'sigma: {sigma}, q {q}')
                gamma = 1 / (sigma ** 2)
                # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(),
                # key=lambda item: item[0])}')
                print(f'gamma: {gamma}, q: {q}, sigma: {sigma}')
                self.detector = OCSVMDetector(gamma=gamma, random_state=self.random_state, verbose=self.verbose)

                X_train = norm_X_train
                X_test = norm_X_test

            elif detector_name.upper() == 'GMM':
                # distances = distance.pdist(norm_X_train, metric='euclidean')
                # stat_data(distances.reshape(-1, 1), name='distances')
                # q = 0.3   # cannot work for meanshift, so we use q=0.7
                # sigma = np.quantile(distances, q=q)
                # print(f'sigma: {sigma}, q (for setting bandwidth in MeanShift): {q}')
                #
                # # means_init, n_components = obtain_means_init(norm_X_train, bandwidth=sigma)
                means_init, n_components = obtain_means_init_quickshift_pp(norm_X_train,
                                                                           k=int(np.log(len(norm_X_train)) ** 4))
                if self.norm_method == 'std':
                    means_init = means_init * self.data_inst.train_scaler.scale_ + self.data_inst.train_scaler.mean_

                self.detector = GMMDetector(n_components=n_components, means_init=means_init, covariance_type='diag',
                                            random_state=self.random_state, verbose=self.verbose)

            elif detector_name.upper() == 'PCA':
                self.detector = PCADetector(n_components=3, random_state=self.random_state, verbose=self.verbose)

            elif detector_name.upper() == 'KDE':
                distances = distance.pdist(norm_X_train, metric='euclidean')
                stat_data(distances.reshape(-1, 1), name='distances')
                q = 0.3
                sigma = np.quantile(distances, q=q)  # distances >=0
                if sigma == 0:  # find a new non-zero sigma
                    print(f'sigma: {sigma}, q: {q}')
                    q_lst = list(np.linspace(q + 0.01, 1, 20))
                    sigma_lst = np.quantile(distances, q=q_lst)

                    sigma, q = [(s_v, q_v) for (s_v, q_v) in zip(sigma_lst, q_lst) if s_v > 0][0]

                print(f'sigma: {sigma}, q {q}')

                self.detector = KDEDetector(bandwidth=sigma, random_state=self.random_state, verbose=self.verbose)

                X_train = norm_X_train
                X_test = norm_X_test

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
