""" Detector

"""
# Authors: kun.bj@outlook.com
#
# License: xxx

# 3. local libraries
# from QuickshiftPP import QuickshiftPP   # it's the right way to use pyx file after building and installing
from QuickshiftPP import QuickshiftPP
# 1. system and built-in libraries
from abc import abstractmethod
from collections import Counter

# 2. thrid-part libraries
import numpy as np
from scipy.spatial import distance
from sklearn.cluster import MeanShift

from data_process.data_factory import SingleDataset
from detector.ae_class import AEDetector
from detector.gmm_class import GMMDetector
from detector.kde_class import KDEDetector
from detector.model_selection.grid_search import GridSearch
from detector.ocsvm_class import OCSVMDetector
from utils.tool import pprint, stat_data


def obtain_means_init(X_train, bandwidth=None):
    ms = MeanShift(bandwidth=bandwidth)
    ms.fit(X_train)

    means_init = ms.cluster_centers_
    labels = ms.labels_
    print(f'mean_shift: {len(Counter(labels))}, {Counter(labels)}')

    return means_init, len(set(labels))


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
        print(f'k: {k} > len(X_train): {len(X_train)}')
        k = int(len(X_train) / 2)  # /2: for some unknown cases in QuickshiftPP
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


class BaseDetectorFactory():

    def __init__(self, dataset_dict='', params={}):
        self.dataset_dict = dataset_dict
        self.params = params
        self.params['dataset_dict'] = dataset_dict

    def run(self):
        for t, (sub_data_name, sd_inst) in enumerate(self.dataset_dict.items()):  # {'sub_dataset_name': single_ds, ...}
            pprint(sd_inst.dataset_dict, name='BaseDetectorFactory.ds_inst_dataset_dict')

            single_result_dict = {}  # store the result on iat, fft, stat and samp
            for i, (key, value_dict) in enumerate(sd_inst.dataset_dict.items()):
                print(f'i:{i}, key:{key}, value_dict.keys():{value_dict.keys()}')
                if key == 'samp_dict':
                    samp_set_best_auc = 0
                    for j, (q_samp_j, samp_dict_j) in enumerate(value_dict.items()):
                        # value_dict={'iat_dict':{'feat_set':, 'data':,}}, 'fft_dict':{}, ...}
                        result_tmp = self.run_model(samp_dict_j)
                        # result_tmp={detector_name: {best_score:, best_params:,...}}
                        auc_j = result_tmp['auc']
                        print(f'q_samp_{j}:{q_samp_j}, auc_{j}: {auc_j}')
                        feat_set = samp_dict_j['feat_set']
                        # only save the best auc on samp_set
                        if auc_j >= samp_set_best_auc:
                            samp_set_best_auc = auc_j
                            single_result_dict[
                                feat_set] = result_tmp  # {'iat_set': result_tmp, 'fft_set': result_tmp, ...}
                            samp_set_best_dict = samp_dict_j
                    self.dataset_dict[sub_data_name].dataset_dict[key] = samp_set_best_dict
                    self.dataset_dict[sub_data_name].dataset_dict[key]['result'] = result_tmp
                elif key in ['iat_dict', 'fft_dict', 'stat_dict']:
                    # value_dict={'iat_dict':{'feat_set':, 'data':,}}, 'fft_dict':{}, ...}
                    result_tmp = self.run_model(
                        value_dict)  # result_tmp={detector_name: {best_score:, best_params:,...}}
                    self.dataset_dict[sub_data_name].dataset_dict[key]['result'] = result_tmp
                else:
                    msg = f'{key} is not correct.'
                    raise ValueError(msg)

    @abstractmethod
    def run_model(self, feat_dict={}):  # feat_dict={'feat_set':, 'feat_file':, 'data':(), ...}
        pass


class GMMFactory(BaseDetectorFactory):

    def __init__(self, kernel='rbf', dataset_dict='', params={}):
        super(GMMFactory, self).__init__(dataset_dict=dataset_dict, params=params)
        self.dataset_dict = dataset_dict
        self.params = params
        # if kernel not in keys:
        #     self.parameter[kernel] = kernel  # create new key
        # else:
        #     self.parameter[kernel] = kernel  # update
        # for I, k, v ink wargs:
        #     self.parameter[k] = v
        #
        # GMM_para = parameters.add[kernel]

    def run_model(self, feat_dict={}):  # feat_dict={'feat_set':, 'feat_file':, 'data':(), ...}
        gs_flg = self.params['gs_flg']
        X_train, y_train, X_test, y_test = feat_dict['data']
        detector_name = self.params['detector_name']
        # result_dict = {detector_name: {}}
        sd_inst = SingleDataset()
        norm_X_train, norm_X_test = sd_inst.normalise_data(X_train, X_test,
                                                           norm_method=self.params['norm_method'])
        if gs_flg:
            print(f'with grid search: {detector_name.upper()}, gs_flg: {gs_flg}')
            # find the best parameters of the detector
            detector = GMMDetector(random_state=self.params['random_state'], verbose=self.params['verbose'])
            grid = GridSearch(estimator=detector, scoring='auc',
                              param_grid={'n_components': [i + 1 for i in range(50)],
                                          'covariance_type': ['diag']})

            grid.fit(X_train, y_train, X_test, y_test)
            self.detector = grid.best_estimator_
            print(f'{detector_name}.params: {self.detector.get_params()}')

            self.detector.test(X_test, y_test)
            print(f'auc: {self.detector.auc}')
            result_dict = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                           'auc': self.detector.auc,
                           'best_score_': grid.best_score_, 'best_params_': grid.best_params_,
                           'best_estimator_': grid.best_estimator_
                           }

        else:  # gs_flg: False
            # rule of thumb in practice
            print('without grid search')
            # distances = distance.pdist(norm_X_train, metric='euclidean')
            # stat_data(distances.reshape(-1, 1), name='distances')
            # q = 0.3   # cannot work for meanshift, so we use q=0.7
            # sigma = np.quantile(distances, q=q)
            # print(f'sigma: {sigma}, q (for setting bandwidth in MeanShift): {q}')
            #
            # # means_init, n_components = obtain_means_init(norm_X_train, bandwidth=sigma)
            means_init, n_components = obtain_means_init_quickshift_pp(norm_X_train,
                                                                       k=int(np.log(len(norm_X_train)) ** 4))

            if self.params['norm_method'] == 'std':
                means_init = means_init * sd_inst.train_scaler.scale_ + sd_inst.train_scaler.mean_

            self.detector = GMMDetector(n_components=n_components, means_init=means_init,
                                        covariance_type='diag',
                                        random_state=self.params['random_state'], verbose=self.params['verbose'])

            print(f'{detector_name}.params: {self.detector.get_params()}')
            self.detector.fit(X_train, y_train)
            self.detector.test(X_test, y_test)

            result_dict = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                           'auc': self.detector.auc,
                           'best_score_': self.detector.auc,
                           'best_params_': self.detector.get_params(),
                           'best_estimator_': self.detector
                           }

        return result_dict


class OCSVMFactory(BaseDetectorFactory):

    def __init__(self, kernel='rbf', dataset_dict='', params={}):
        super(OCSVMFactory, self).__init__(dataset_dict=dataset_dict, params=params)
        self.dataset_dict = dataset_dict
        self.params = params
        # if kernel not in keys:
        #     self.parameter[kernel] = kernel  # create new key
        # else:
        #     self.parameter[kernel] = kernel  # update
        # for I, k, v ink wargs:
        #     self.parameter[k] = v
        #
        # GMM_para = parameters.add[kernel]

    def run_model(self, feat_dict):
        gs_flg = self.params['gs_flg']
        X_train, y_train, X_test, y_test = feat_dict['data']
        detector_name = self.params['detector_name']
        # result_dict = {detector_name: {}}
        sd_inst = SingleDataset(params={})

        norm_X_train, norm_X_test = sd_inst.normalise_data(X_train, X_test,
                                                           norm_method=self.params['norm_method'])
        if gs_flg:
            print(f'with grid search: {detector_name.upper()}, gs_flg: {gs_flg}')
            # find the best parameters of the detector
            distances = distance.pdist(norm_X_train, metric='euclidean')
            stat_data(distances.reshape(-1, 1), name='distances')
            q_lst = list(np.linspace(0.0, 1, 20, endpoint=False))[1:]  # exclude 0
            sigma_lst = np.quantile(distances, q=q_lst)
            gamma_lst = list(1 / sigma_lst ** 2)  # sigma =np.quantile(distances, q=q_lst
            # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(),
            # key=lambda item: item[0])}')
            print(f'gamma_lst:{gamma_lst},\nq_lst: {q_lst},\nsigma_lst: {sigma_lst}')
            detector = OCSVMDetector(random_state=self.params['random_state'], verbose=self.params['verbose'])
            grid = GridSearch(estimator=detector, scoring='auc',
                              param_grid={'gamma': gamma_lst, 'kernel': ['rbf']})
            X_train = norm_X_train
            X_test = norm_X_test

            grid.fit(X_train, y_train, X_test, y_test)
            self.detector = grid.best_estimator_
            print(f'{detector_name}.params: {self.detector.get_params()}')

            self.detector.test(X_test, y_test)
            print(f'auc: {self.detector.auc}')
            result_dict = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                           'auc': self.detector.auc,
                           'best_score_': grid.best_score_, 'best_params_': grid.best_params_,
                           'best_estimator_': grid.best_estimator_
                           }

        else:  # gs_flg: False
            # rule of thumb in practice
            print('without grid search')
            distances = distance.pdist(norm_X_train, metric='euclidean')
            stat_data(distances.reshape(-1, 1), name='distances')
            q = 0.3
            sigma = np.quantile(distances, q=q)
            if sigma == 0:  # find a new non-zero sigma
                print(f'sigma: {sigma}, q: {q}')
                q_lst = list(np.linspace(q + 0.01, 1, 20, endpoint=False))
                sigma_lst = np.quantile(distances, q=q_lst)
                sigma, q = [(s_v, q_v) for (s_v, q_v) in zip(sigma_lst, q_lst) if s_v > 0][0]
            print(f'sigma: {sigma}, q {q}')
            gamma = 1 / (sigma ** 2)
            # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(),
            # key=lambda item: item[0])}')
            print(f'gamma: {gamma}, q: {q}, sigma: {sigma}')
            self.detector = OCSVMDetector(gamma=gamma, random_state=self.params['random_state'],
                                          verbose=self.params['verbose'])

            X_train = norm_X_train
            X_test = norm_X_test

            print(f'{detector_name}.params: {self.detector.get_params()}')
            self.detector.fit(X_train, y_train)
            self.detector.test(X_test, y_test)

            result_dict = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                           'auc': self.detector.auc,
                           'best_score_': self.detector.auc,
                           'best_params_': self.detector.get_params(),
                           'best_estimator_': self.detector
                           }

        return result_dict


class KDEFactory(BaseDetectorFactory):

    def __init__(self, kernel='rbf', dataset_dict='', params={}):
        super(KDEFactory, self).__init__(dataset_dict=dataset_dict, params=params)
        self.dataset_dict = dataset_dict
        self.params = params
        # if kernel not in keys:
        #     self.parameter[kernel] = kernel  # create new key
        # else:
        #     self.parameter[kernel] = kernel  # update
        # for I, k, v ink wargs:
        #     self.parameter[k] = v
        #
        # GMM_para = parameters.add[kernel]

    def run_model(self, feat_dict):
        gs_flg = self.params['gs_flg']
        X_train, y_train, X_test, y_test = feat_dict['data']
        detector_name = self.params['detector_name']
        result_dict = {}
        sd_inst = SingleDataset(params={})

        norm_X_train, norm_X_test = sd_inst.normalise_data(X_train, X_test,
                                                           norm_method=self.params['norm_method'])
        if gs_flg:
            print(f'with grid search: {detector_name.upper()}, gs_flg: {gs_flg}')
            # find the best parameters of the detector
            distances = distance.pdist(norm_X_train, metric='euclidean')
            stat_data(distances.reshape(-1, 1), name='distances')
            q_lst = list(np.linspace(0.0, 1, 20, endpoint=False))[1:]  # exclude 0
            sigma_lst = np.quantile(distances, q=q_lst)
            print(f'q_lst: {q_lst},\nsigma_lst:{list(sigma_lst)}')

            detector = KDEDetector(random_state=self.params['random_state'], verbose=self.params['verbose'])
            # grid = GridSearch(estimator=detector, scoring='auc',
            #                   param_grid={'bandwidth': list(np.linspace(0.0, 5, 501, endpoint=False))[1:]})

            grid = GridSearch(estimator=detector, scoring='auc',
                              param_grid={'bandwidth': sigma_lst})

            X_train = norm_X_train
            X_test = norm_X_test

            grid.fit(X_train, y_train, X_test, y_test)
            self.detector = grid.best_estimator_
            print(f'{detector_name}.params: {self.detector.get_params()}')

            self.detector.test(X_test, y_test)
            print(f'auc: {self.detector.auc}')
            result_dict = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                           'auc': self.detector.auc,
                           'best_score_': grid.best_score_, 'best_params_': grid.best_params_,
                           'best_estimator_': grid.best_estimator_
                           }

        else:  # gs_flg: False
            # rule of thumb in practice
            print('without grid search')
            distances = distance.pdist(norm_X_train, metric='euclidean')
            stat_data(distances.reshape(-1, 1), name='distances')
            q = 0.3
            sigma = np.quantile(distances, q=q)  # distances >=0
            if sigma == 0:  # find a new non-zero sigma
                print(f'sigma: {sigma}, q: {q}')
                q_lst = list(np.linspace(q + 0.01, 1, 20, endpoint=False))
                sigma_lst = np.quantile(distances, q=q_lst)

                sigma, q = [(s_v, q_v) for (s_v, q_v) in zip(sigma_lst, q_lst) if s_v > 0][0]

            print(f'sigma: {sigma}, q {q}')

            self.detector = KDEDetector(bandwidth=sigma, random_state=self.params['random_state'],
                                        verbose=self.params['verbose'])

            X_train = norm_X_train
            X_test = norm_X_test

            print(f'{detector_name}.params: {self.detector.get_params()}')
            self.detector.fit(X_train, y_train)
            self.detector.test(X_test, y_test)

            result_dict = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                           'auc': self.detector.auc,
                           'best_score_': self.detector.auc,
                           'best_params_': self.detector.get_params(),
                           'best_estimator_': self.detector
                           }

        return result_dict


class AEFactory(BaseDetectorFactory):

    def __init__(self, kernel='rbf', dataset_dict='', params={}):
        super(AEFactory, self).__init__(dataset_dict=dataset_dict, params=params)
        self.dataset_dict = dataset_dict
        self.params = params
        # if kernel not in keys:
        #     self.parameter[kernel] = kernel  # create new key
        # else:
        #     self.parameter[kernel] = kernel  # update
        # for I, k, v ink wargs:
        #     self.parameter[k] = v
        #
        # GMM_para = parameters.add[kernel]

    def run_model(self, feat_dict):
        gs_flg = self.params['gs_flg']
        X_train, y_train, X_test, y_test = feat_dict['data']
        detector_name = self.params['detector_name']
        result_dict = {}
        sd_inst = SingleDataset(params={})

        norm_X_train, norm_X_test = sd_inst.normalise_data(X_train, X_test,
                                                           norm_method=self.params['norm_method'])

        # rule of thumb in practice
        print('without grid search')

        self.detector = AEDetector(random_state=self.params['random_state'],
                                   verbose=self.params['verbose'])

        X_train = norm_X_train
        X_test = norm_X_test

        print(f'{detector_name}.params: {self.detector.get_params()}')
        self.detector.fit(X_train, y_train)
        self.detector.test(X_test, y_test)

        result_dict = {'y_true': y_test, 'y_scores': self.detector.y_scores,
                       'auc': self.detector.auc,
                       'best_score_': self.detector.auc,
                       'best_params_': self.detector.get_params(),
                       'best_estimator_': self.detector
                       }

        return result_dict


class DetectorFactory:
    def __init__(self, detector_name='', params={}, dataset_dict=''):
        self.detector_name = detector_name
        self.dataset_dict = dataset_dict

        self.params = params
        self.params['detector_name'] = detector_name
        self.params['dataset_dict'] = dataset_dict

    def run(self):

        if self.detector_name == 'GMM':
            self.detector = GMMFactory(dataset_dict=self.dataset_dict, params=self.params)
        elif self.detector_name == 'OCSVM':
            self.detector = OCSVMFactory(dataset_dict=self.dataset_dict, params=self.params)
        elif self.detector_name == 'KDE':
            self.detector = KDEFactory(dataset_dict=self.dataset_dict, params=self.params)
        elif self.detector_name == 'AE':
            self.detector = AEFactory(dataset_dict=self.dataset_dict, params=self.params)
        else:
            msg = f'{self.detector_name} is not implemented.'
            raise ValueError(msg)

        self.detector.run()  # update dataset_dict
