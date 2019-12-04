# Authors: kun.bj@outlook.com
#
# License: xxx
"""Main function for AUC on different feature sets using the best detection algorithm.

"""
from collections import Counter, OrderedDict

from sklearn.preprocessing import MinMaxScaler

from _config import *
from detector.gmm_class import GMMDetector
from legacy.utils import load_and_split_data, select_features_from_list
from legacy.utils.dataset import stat_data
from legacy.utils.visualization import plot_auc_and_strength_of_outiler


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
        print('2) normalization (minmaxscaler)')
        train_scaler = MinMaxScaler()
        train_scaler.fit(X_train)
        X_train = train_scaler.transform(X_train)
        X_test = train_scaler.transform(X_test)

    stat_data(X_train)
    print(f'Counter(y_train): {Counter(y_train)}')
    stat_data(X_test)
    print(f'Counter(y_test): {Counter(y_test)}')

    print('3) train and test the best detection algorithm.')
    roc_dict = {}
    auc_dict = {}

    # ocsvm = OCSVMDetector()
    # ocsvm.train(X_train)
    # # dump(ocsvm, 'output_data/models_dumping/ocsvm_' + case + '.joblib')
    # # model = load('output_data/models_dumping/ocsvm_' + case + '.joblib')
    # ocsvm.test(X_test, y_test)
    #
    # roc_dict['ocsvm'] = {'y_true': y_test, 'y_scores': ocsvm.y_scores}
    # auc_dict['ocsvm'] = ocsvm.auc

    gmm = GMMDetector(verbose=True)
    gmm.train(X_train)
    # dump(gmm, 'output_data/models_dumping/gmm_' + case + '.joblib')
    # model = load('output_data/models_dumping/gmm_' + case + '.joblib')
    gmm.test(X_test, y_test)

    roc_dict['gmm'] = {'y_true': y_test, 'y_scores': gmm.y_scores}
    auc_dict['gmm'] = gmm.auc

    # pca = PCADetector()
    # pca.train(X_train)
    # # dump(pca, 'output_data/models_dumping/pca_' + case + '.joblib')
    # # model = load('output_data/models_dumping/pca_' + case + '.joblib')
    # pca.test(X_test, y_test)
    # roc_dict['pca'] = {'y_true': y_test, 'y_scores': pca.y_scores}
    # auc_dict['pca'] = pca.auc

    return roc_dict, auc_dict


def main_for_auc():
    """
       "test_size, random_state and so on", all of them come from _config.py.
    :return:
    """
    print(f"\nstep 1. obtain different strength datasets.")
    different_strength_datasets_dict = OrderedDict()
    # strength_lst = [0.1, 0.2, 0.4, 0.8, 1]  # strength of outlier: weaker strengths, smaller feature values.

    strength_lst = [0.1, 0.2, 0.4, 0.8, 1]  # strength of outlier: weaker strengths, smaller feature values.
    # strength_lst = [1]
    for idx, strength_value in enumerate(strength_lst):
        strength_key = strength_value

        demo_flg = True
        if demo_flg:
            idx_features_lst = [random.randint(5, 20) for i in range(4 + idx)]
            print(f'idx:{idx}, strength_key: {strength_key}, proposed feature set, idx_features_lst:{idx_features_lst}')
            select_features_from_list(input_file='input_data/demo_dataset/proposed_features/normal_demo_dataset.txt',
                                      output_file=f'input_data/demo_dataset/proposed_features/normal_demo_dataset_{strength_key}.txt',
                                      features_lst=idx_features_lst)
            select_features_from_list(input_file='input_data/demo_dataset/proposed_features/anomaly_demo_dataset.txt',
                                      output_file=f'input_data/demo_dataset/proposed_features/anomaly_demo_dataset_{strength_key}.txt',
                                      features_lst=idx_features_lst)
            idx_features_lst = [random.randint(5, 20) for i in range(2 + idx)]
            print(
                f'idx:{idx}, strength_key: {strength_key}, traditional feature set, idx_features_lst:{idx_features_lst}')
            select_features_from_list(input_file='input_data/demo_dataset/traditional_features/normal_demo_dataset.txt',
                                      output_file=f'input_data/demo_dataset/traditional_features/normal_demo_dataset_{strength_key}.txt',
                                      features_lst=idx_features_lst)
            select_features_from_list(
                input_file='input_data/demo_dataset/traditional_features/anomaly_demo_dataset.txt',
                output_file=f'input_data/demo_dataset/traditional_features/anomaly_demo_dataset_{strength_key}.txt',
                features_lst=idx_features_lst)

        values_dict = OrderedDict(
            {'prop_set': {
                'normal_file': f'input_data/demo_dataset/proposed_features/normal_demo_dataset_{strength_key}.txt',
                'anomaly_file': f'input_data/demo_dataset/proposed_features/anomaly_demo_dataset_{strength_key}.txt'},
                'trad_set': {
                    'normal_file': f'input_data/demo_dataset/traditional_features/normal_demo_dataset_{strength_key}.txt',
                    'anomaly_file': f'input_data/demo_dataset/traditional_features/anomaly_demo_dataset_{strength_key}.txt'}})

        different_strength_datasets_dict[strength_key] = values_dict

    print(f"\nstep 2. calculate auc under the corresponding strength data_process.")
    all_auc_dicts_lst = []
    for idx, (strength_key, values) in enumerate(different_strength_datasets_dict.items()):
        print(f"\n- strength of outiler: {strength_key}")
        input_files_dict = values
        # roc_dicts_lst = []
        auc_dicts_dict = OrderedDict()
        for ith, (feature_set_key, value_dict) in enumerate(input_files_dict.items()):
            """
                obtain roc_dict and auc_dict on different feature sets with the same (attack) strength of outiler.
            """
            print(
                f'\n-- ith:{ith}: evaluation on {feature_set_key} by the best detection algorithm under the same strength of outlier ({strength_key}).')
            roc_dict, auc_dict = main_for_each_feature_set(
                norm_file=value_dict['normal_file'],
                anomaly_file=value_dict['anomaly_file'],
                test_size=test_size, random_state=random_state)

            # roc_dicts_lst.append([key, roc_dict])
            auc_dicts_dict[feature_set_key] = auc_dict

        all_auc_dicts_lst.append([strength_key, auc_dicts_dict])

    print(f"\nstep 3. plot auc.")
    plot_auc_and_strength_of_outiler(all_auc_dicts_lst, out_file='output_data/figures/auc_on_different_strengths.pdf',
                                     title='AUC')


if __name__ == '__main__':
    main_for_auc()
