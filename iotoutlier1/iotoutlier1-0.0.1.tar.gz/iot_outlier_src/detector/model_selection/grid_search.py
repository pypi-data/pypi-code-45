""" grid search class

"""
# Authors: kun.bj@outlook.com
#
# License: xxx

import itertools
from copy import deepcopy

from sklearn import clone


class GridSearch:

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
        print(f'len(combinations of parameters): {len(combinations)}')
        # print(combinations)
        self.best_score_ = -1
        self.best_params_ = {}
        self.best_estimator_ = None
        self.best_index = 0
        for idx, params in enumerate(combinations):
            self.detector = clone(self.estimator)  # constructs a new estimator with the same parameters, but not fit
            self.detector.set_params(**params)  # set params
            print(f'idx: {idx+1}, detector_params: {self.detector.get_params()}')
            try:
                self.detector.fit(X_train, y_train)
                self.detector.test(X_test, y_test)
            except Exception as e:
                print(f'{e}, skipping {params}')
                continue

            print(f'auc: {self.detector.auc}')

            if self.scoring == 'auc':
                if self.detector.auc > self.best_score_:
                    self.best_score_ = self.detector.auc
                    self.best_params_ = params  # if key exists, update; otherwise, add new key
                    self.best_estimator_ = deepcopy(self.detector)
                    self.best_index = idx
                    # print(f'best_auc: {self.best_estimator_.auc}, {self.best_score_}')
            else:
                print(f'scoring: {self.scoring} is not implemented yet, please check and retry')

        # # summarize the results of the grid search
        print(f'grid.best_score_: {self.best_score_}')
        print(f'grid.best_params_: {self.best_params_}')
        print(f'grid.best_estimator_: {self.best_estimator_}')
        print(f'grid.best_index: {self.best_index}')

        return self
