# Authors: kun.bj@outlook.com
#
# License: xxx
"""
    Purpose: ROC

"""
from detector.gmm_class import GMMDetector
from detector.ocsvm_class import OCSVMDetector

"""
    Purpose:
        main function for feature set comparison.

"""
from collections import Counter, OrderedDict

from sklearn.preprocessing import MinMaxScaler

from _config import *
from detector.pca_class import PCADetector
from legacy.utils import load_and_split_data, select_features_from_list
from legacy.utils.visualization import plot_roc


def main_for_each_feature_set(norm_file='', anomaly_file='', test_size=0.3, random_state=42):
    """

    :param norm_file:
    :param anomaly_file:
    :param test_size:
    :param random_state:
    :return:
    """
    print('1) load data and split it to train set and test set with ratio: 7:3')
    X_train, y_train, X_test, y_test = load_and_split_data(norm_file=norm_file, anomaly_file=anomaly_file,
                                                           test_size=test_size, random_state=random_state)
    print(f'--- train set and test set --'
          f'\nX_train:{X_train.shape}, y_train:{Counter(y_train)}'
          f'\nX_test :{X_test.shape}, y_test :{Counter(y_test)}, in which, 0: normals and 1: anomalies.')

    if norm_flg:
        print('\n2) normalization (minmaxscaler)')
        train_scaler = MinMaxScaler()
        train_scaler.fit(X_train)
        X_train = train_scaler.transform(X_train)
        X_test = train_scaler.transform(X_test)

    print('\n3) train and test different models')
    roc_dict = {}
    auc_dict = {}

    gmm = GMMDetector(n_components=3)
    gmm.train(X_train)
    # dump(pca, 'output_data/models_dumping/gmm_' + case + '.joblib')
    # model = load('output_data/models_dumping/gmm_' + case + '.joblib')
    gmm.test(X_test, y_test)
    roc_dict['gmm'] = {'y_true': y_test, 'y_scores': gmm.y_scores}
    auc_dict['gmm'] = gmm.auc

    # knn = KNNDetector()
    # knn.train(X_train)
    # # dump(pca, 'output_data/models_dumping/knn_' + case + '.joblib')
    # # model = load('output_data/models_dumping/knn_' + case + '.joblib')
    # knn.test(X_test, y_test)
    # roc_dict['knn'] = {'y_true': y_test, 'y_scores': knn.y_scores}
    # auc_dict['knn'] = knn.auc
    # knn.visualize(X_train[:,:2], y_train, X_test[:,:2], y_test, knn.knn.predict(X_train), knn.knn.predict(X_test), show_figure=True)

    pca = PCADetector()
    pca.train(X_train)
    # dump(pca, 'output_data/models_dumping/pca_' + case + '.joblib')
    # model = load('output_data/models_dumping/pca_' + case + '.joblib')
    pca.test(X_test, y_test)
    roc_dict['pca'] = {'y_true': y_test, 'y_scores': pca.y_scores}
    auc_dict['pca'] = pca.auc

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


def main_for_roc():
    """
        "test_size, random_state and so on", all of them come from _config.py.
    :return:
    """
    flg = True
    if flg:
        select_features_from_list('input_data/demo_dataset/proposed_features/normal_demo_dataset.txt',
                                  features_lst=[5, 7, 9, 11, 13])
        select_features_from_list('input_data/demo_dataset/proposed_features/anomaly_demo_dataset.txt',
                                  features_lst=[5, 7, 9, 11, 13])
        select_features_from_list('input_data/demo_dataset/traditional_features/normal_demo_dataset.txt',
                                  features_lst=[6, 8, 10, 12, 14])
        select_features_from_list('input_data/demo_dataset/traditional_features/anomaly_demo_dataset.txt',
                                  features_lst=[6, 8, 10, 12, 14])

    input_files_dict = OrderedDict(
        {'prop_set': {'normal_file': 'input_data/demo_dataset/proposed_features/normal_demo_dataset_sub.txt',
                      'anomaly_file': 'input_data/demo_dataset/proposed_features/anomaly_demo_dataset_sub.txt'},
         'trad_set': {'normal_file': 'input_data/demo_dataset/traditional_features/normal_demo_dataset_sub.txt',
                      'anomaly_file': 'input_data/demo_dataset/traditional_features/anomaly_demo_dataset_sub.txt'}})

    roc_dicts_lst = []
    auc_dicts_lst = []
    for idx, (key, value_dict) in enumerate(input_files_dict.items()):
        print(f'\n{idx}: evaluation on {key} with different detection algorithms.')
        roc_dict, auc_dict = main_for_each_feature_set(
            norm_file=value_dict['normal_file'],
            anomaly_file=value_dict['anomaly_file'],
            test_size=test_size, random_state=random_state)

        roc_dicts_lst.append([key, roc_dict])
        auc_dicts_lst.append([key, auc_dict])

    print('\n3: plot roc.')
    plot_roc(roc_dicts_lst=roc_dicts_lst)
    # plot_auc_and_strength_of_outiler(auc_dicts_lst=auc_dicts_lst)


if __name__ == '__main__':
    main_for_roc()
