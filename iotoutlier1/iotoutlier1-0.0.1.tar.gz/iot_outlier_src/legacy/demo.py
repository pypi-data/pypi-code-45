# from pyod.models.ocsvm import OCSVM
# from sklearn import datasets, linear_model
# from sklearn.base import ClassifierMixin, BaseEstimator
# from sklearn.mixture import GaussianMixture
# from sklearn.model_selection import cross_val_score, cross_validate, GridSearchCV
# import numpy as np


class SomeClass:
    def __init__(self, some_kw=None, some_kw_1=None, **kwargs):
        """
        @param some_kw: A known-at-dev-time keyword argument
        @type some_kw: str
        @param some_kw_1: Another known-at-dev-time keyword argument
        @type some_kw_1: str
        @keyword kwargs: More kwargs that will be set on the instance
        """
        self.some_kw = some_kw
        self.some_kw_1 = some_kw_1
        for k, v in kwargs.items():
            setattr(self, k, v)


an_instance = SomeClass(some_kw="hello", other_kw="world", b='b')
print(an_instance.some_kw)
print(an_instance.some_kw_1)
print(an_instance.other_kw)


class Person():
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', "")
        self.age = kwargs.get('age', -1)
        self.gender = kwargs.get('gender', "x")


him = Person(name="Phred", age=42, gender="yes")

print(him.name)
print(him.age)
print(him.gender)


class Person():
    def __init__(self, **kwargs):
        self.name = ""
        self.age = -1
        self.gender = "x"
        self.__dict__.update(kwargs)


him = Person(name="Phred", age=42, gender="yes", notused="Spare")

print(him.name)
print(him.age)
print(him.gender)
print(him.notused)


class SingleDataset():

    def __init__(self, srcIP='', params='', **kwargs):
        # super(SingleDataset, self).__init__()

        for i, (key, value) in enumerate(kwargs.items()):
            callable_method = getattr(self, key)
            self.key = value
            callable_method(user={}, **{option_name: user_defaults[option_name]})

        self.srcIP = srcIP
        self.params = params
        # self.params['srcIP'] = srcIP


sd = SingleDataset(a=1, b=2, c=3)

user_defaults = {'key': 1, '2': 3}
for option_name, option_value in user_defaults.items():
    callable_method = getattr(option_name, option_name)
    callable_method(user={}, **{option_name: user_defaults[option_name]})


# #
# # diabetes = datasets.load_diabetes()
# # X = diabetes.data[:150]
# # y = diabetes.target[:150]
# # # lasso = linear_model.Lasso()
# # # for value in
# # lasso= GaussianMixture()
# # lasso= OCSVM()
# # # print(cross_val_score(lasso, X, y, cv=3, fit_params={'n_components':1}))
# # # [0.33150734 0.08022311 0.03531764]
# # grid=GridSearchCV(lasso, scoring='accuracy', param_grid={'n_components':[1,2]})
# # print(grid.fit(X))
# # print(grid.best_params_)
# from gmm_base import GMM
# from gmm_class import GMM_Class
#
#
# class MyClassifier(BaseEstimator):
#     def __init__(self,n_components=1, lr=0.1):
#         # Some code
#         self.n_components = n_components
#
#     def fit(self, X, y):
#         # Some code
#         self.gmm = GMM(n_components= self.n_components)
#         self.gmm.fit(X,y)
#         return self
#
#     def predict(self, X):
#         # Some code
#         return X % 3
#
# #
# # params = {
# #     'n_components': [1, 5, 7]
# # }
# # gs = GridSearchCV(estimator=MyClassifier(), scoring='accuracy',param_grid=params, cv=4)
# #
# # x = np.arange(30).reshape(-1,1)
# # y = np.concatenate((np.zeros(10), np.ones(10), np.ones(10) * 2))
# # gs.fit(x,y)
# #
# # print(gs.best_params_)
#
# class Demo():
#
#     def __init__(self):
#         pass
#
#     def run(self):
#         params = {
#             'n_components': [1, 5, 7]
#         }
#         gs = GridSearchCV(estimator=MyClassifier(), scoring='accuracy', param_grid=params, cv=4)
#
#         x = np.arange(30).reshape(-1, 1)
#         y = np.concatenate((np.zeros(10), np.ones(10), np.ones(10) * 2))
#         gs.fit(x, y)
#
#         print(gs.best_params_)
#
# if __name__ == '__main__':
#     Demo().run()
#
# data_str = 'q_fixed_iat:0.9, bin_size:9\ncovariance_type:diag, n_components:4, '
# step = 40
# for i in range(0, len(data_str), step):
#     print(data_str[i:i + step])

#
# import progressbar
#
# progressbar.progressbar(print('adsfa'))
# # for i in progressbar.progressbar(range(100)):
# #     # time.sleep(0.02)
# #     print('adfasf')
# input_file = '../input_data/UNSW_2018_IoT_Botnet_Final_10_best_Testing.csv'


#
# tqdm(print('adf'))
# for i in tqdm(range(10)):
#     print(f'i: {i}, afa')


#
# with tqdm() as pbar:
#     for i in range(10):
#         time.sleep(0.2)
#         print(f'i: {i}, afa')
#         pbar.update(10)

# input_file='input_data/UNSW_2018_IoT_Botnet_Final_10_best_Training.csv'
# input_file = 'input_data/UNSW_2018_IoT_Botnet_Dataset_2.csv'
def load_csv(input_file):
    features = {}
    i = 0
    num_norm = 0
    num_anomaly = 0
    with open(input_file, 'r') as in_hdl:
        line = in_hdl.readline()
        while (line):
            i += 1
            if i % 10000 == 0:
                print("Label CSV row {}".format(i))
            if ',35.165.2' in line:
                # if '192.168.100.147' in line or '192.168.100.148' in line or '192.168.100.149'  in line or '192.168.100.150'  in line:
                # if 'normal' in line or 'Normal' in line:
                if 'normal' in line or 'Normal' in line:
                    num_norm += 1
                    print(f'{i}: {line}')
                elif 'DDoS' in line or 'DoS' in line:
                    num_anomaly += 1

                line = in_hdl.readline()
                continue

            line = in_hdl.readline()
    print(f'num_norm: {num_norm}, num_anomaly: {num_anomaly}, tot_lines: {i}')
    #     # parse 5-tuple flow ID
    #     # fid = (row[" Source IP"], row[" Destination IP"], row[" Source Port"],
    #     #        row[" Destination Port"], row[" Protocol"])
    #     fid = (row["saddr"], row["daddr"], row["sport"],
    #            row["dport"], row["proto"])      # proto,saddr,sport,daddr,dport,
    #     # ensure all 5-tuple flows have same label
    #     if fid in labels.keys():
    #         try:
    #             assert (labels[fid] == row["category"])  # if one fid has different labels
    #         except:
    #             # print(f'i: {i}, fid: {fid},row["category"]: {row["attack"], row["category"], row["subcategory"]}, labels[fid]: {labels[fid]}')
    #             pass
    #     # set label of flow ID
    #     labels[fid] = row["category"]
    #     key = row['saddr']
    #     # key = fid
    #     if key not in features.keys():
    #         features[key] = {row["category"]:1}
    #     else:
    #         if row["category"] not in features[key]:
    #             features[key][row["category"]]=1
    #             print(f'i: {i}, key: {key}, {features[key]}')
    #         else:
    #             features[key][row["category"]] += 1
    #
    #     # if i > 20000:
    #     #     break
    # print(f'{Counter(features)}')
    # print(f'{features}')
    # print(f'{not_existed_num} flows do not exist in {label_file}')


load_csv(input_file)

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
roc_auc_score(y_true, y_scores)
fpr, tpr, thres = roc_curve(y_true=y_true, y_score=y_scores)
print(f'x=fpr: {fpr},\ny=tpr: {tpr},\nthres: {thres}')
plt.plot(fpr, tpr)
# plt.show()

import warnings as wn

import numpy as np

wn.warn('radf')
# set seed for reproducibility
np.random.seed(0)
#
# a=2
# # raise ValueError(f'print: {a}')
#
# raise  ValueError("Invalid value for 'n_components': %d "
#                              "Estimation requires at least one component"
#                              % a)

# generate 1000 data points randomly drawn from an exponential distribution
# original_data = np.random.exponential(size=10000)
#
# min_v = np.min(original_data)
# max_v = np.max(original_data)
#
# mean_v = np.mean(original_data)
# std_v = np.std(original_data)
# median_v = np.median(original_data)
# Q0, Q1, Q2, Q3, Q4 = np.quantile(original_data, q=[0.0, 0.25, 0.5, 0.75, 1.0])
#
# print(f'min:{min_v}, median:{median_v}, max:{max_v}, mean:{mean_v},  std:{std_v}')
#
# print(f'Q0:{Q0}, Q1:{Q1}, Q2:{Q2}, Q3:{Q3}, Q4:{Q4}')
#
# # plot both together to compare
# fig, ax = plt.subplots(1, 2)
# ax[0].hist(original_data)
# sns.distplot(original_data, ax=ax[0], color='y')
# ax[0].set_title("Original Data")
# ax[0].set_xlim(auto=False, xmin=min_v, xmax=max_v)
# #
# # # mix-max scale the data between 0 and 1
# # scaled_data = original_data-min_v
# # sns.distplot(scaled_data, ax=ax[1])
# # ax[1].set_title("original_data-min_v")
# # ax[1].set_xlim(auto=False, xmin=np.min(scaled_data), xmax=np.max(scaled_data))
# # # xi = list(range(len(x)))
# # # plt.xticks(xi, x)
#
#
# # std
# scaled_data = (original_data - mean_v) / std_v
# scaled_data = StandardScaler().fit_transform(original_data.reshape(-1, 1))
# ax[1].hist(scaled_data)
# sns.distplot(scaled_data, ax=ax[1])
# ax[1].set_title("original_data-mean_v")
# ax[1].set_xlim(auto=False, xmin=np.min(scaled_data), xmax=np.max(scaled_data))
#
# #
# # scaled_data = (original_data-Q2)
# # sns.distplot(scaled_data, ax=ax[3])
# # ax[3].set_title("original_data-Q2")
#
# plt.show()
#
# # plot both together to compare
# fig, ax = plt.subplots(1, 4)
# sns.distplot(original_data, ax=ax[0], color='y')
# ax[0].set_title("Original Data")
#
# # minmax
# scaled_data = (original_data - min_v) / (max_v - min_v)
# sns.distplot(scaled_data, ax=ax[1])
# ax[1].set_title("minmax")
#
# # std
# scaled_data = (original_data - mean_v) / std_v
# sns.distplot(scaled_data, ax=ax[2])
# ax[2].set_title("z-score")
#
# plt.show()
#
#
# import pickle
#
# import numpy as np
#
# from utils.tool import stat_data
#
#
# def load_pickled_data(input_file):
#     """ Especially for loading multi-objects stored in a file.
#
#        :param input_file:
#        :return:
#        """
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
#
#     return fids, features, labels
#
#
# srcIP = '192.168.10.5'
# input_file = f'/Users/kunyang/PycharmProjects/IoT_feature_sets_comparison_20190822/input_data/CICIDS2017/srcIP_{srcIP}/Monday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat'
# fids, features, labels = load_pickled_data(input_file)
# data = list(map(lambda x: x[0:2], features))
# stat_data(np.asarray(data, dtype=float))
#
# from inspect import signature
#
#
# def print_func_args(func):
#     sig = signature(func)
#     for key, value in sig.parameters.items():
#         print(f'{key}, {value}')
#
#
# def print_func_args(func, a, b, c):
#     sig = signature(func)
#     sig.bind(a=2, b=b, c=c)
#     for key, value in sig.parameters.items():
#         print(f'{key}, {value}')
#
#
# def add_test(v=0, m=2):
#     a = 0
#     b = 2
#     c = 3
#     add(a, b, c)
#
#
# def add(a=1, b=2, c=''):
#     print_func_args(add, a, b, c)
#     return a + b
#
#
# add_test()
#
# import itertools
#
# param_grid = {'n_components': [i + 1 for i in range(10)], 'covariance_type': ['full', 'diag'],
#               'kernel': ['rbf', 'linear']}
# keys, values = zip(*param_grid.items())
# experiments = [dict(zip(keys, v)) for v in itertools.product(*values)]
# print(len(experiments))
# print(experiments)
#
#
# def cluster():
#     from sklearn.cluster import MeanShift
#     import numpy as np
#     X = np.array([[1, 1], [2, 1], [1, 0],
#                   ...[4, 7], [3, 5], [3, 6]])
#     clustering = MeanShift(bandwidth=2).fit(X)
#     print(clustering.labels_)
#
#     # clustering.predict([[0, 0], [5, 5]])
#
#     # clustering
#     # MeanShift(bandwidth=2, bin_seeding=False, cluster_all=True, min_bin_freq=1,
#     #           n_jobs=None, seeds=None)
