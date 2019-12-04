# Authors: kun.bj@outlook.com
#
# License: xxx
""" Kernel K-means to detect anomaly
"""
from collections import Counter

from sklearn.preprocessing import MinMaxScaler

from _config import *
from detector.ocsvm_class import OCSVM_Class
from legacy.detection_algorithms import KKMeans_Class
from legacy.utils import load_and_split_data
from legacy.utils.dataset import Dataset


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

    print('3) train and test the best detection algorithm.')
    roc_dict = {}
    auc_dict = {}

    ocsvm = OCSVM_Class()
    ocsvm.train(X_train)
    # dump(ocsvm, 'output_data/models_dumping/ocsvm_' + case + '.joblib')
    # model = load('output_data/models_dumping/ocsvm_' + case + '.joblib')
    ocsvm.test(X_test, y_test)

    roc_dict['ocsvm'] = {'y_true': y_test, 'y_scores': ocsvm.y_scores}
    auc_dict['ocsvm'] = ocsvm.auc

    return roc_dict, auc_dict


def main_for_kernel_kmeans():
    """
       "test_size, random_state and so on", all of them come from _config.py.
    :return:
    """

    conf_inst = Configuration()  # return an instance or object of Configuration class.
    dataset_inst = Dataset(input_dir=conf_inst.input_dir,
                           random_state=conf_inst.random_state)
    # dataset_inst.datasets_stat()
    print(f'All parameters used: {conf_inst}')

    # # dataset_inst.selected_sub_features(features_lst=conf_inst.features_lst)
    # if conf_inst.norm_flg:
    #     dataset_inst.normalize_data(norm_method=conf_inst.norm_method, train_set_key=dataset_key,
    #                                  not_normalized_features_lst=conf_inst.not_normalized_features_lst)
    #     
    dataset_dict = dataset_inst.dataset_dict
    train_set_dict = dataset_dict['train_set_dict']  # train_set_dict= {'X':, 'y':}
    val_set_dict = dataset_dict['val_set_dict']  # val_set_dict={'X':, 'y':}

    ################## algorithm AE #################################################
    kkmeans_inst = KKMeans_Class(n_clusters=2, kernel='linear')
    # kkmeans_inst =
    print(f'\n{kkmeans_inst.alg_name} train and test')

    kkmeans_inst.train(X=train_set_dict['X'], y=None, val_set_dict=val_set_dict)
    kkmeans_inst.dump_model()
    ### find optimal thres on train set
    # kkmeans_inst.find_optimal_thres(X=train_set_dict['X'], y=train_set_dict['y'])

    dataset_key = 'demo'
    print(f'test {kkmeans_inst.alg_name} on {dataset_key}_train_set')
    kkmeans_inst.test(X=train_set_dict['X'], y=train_set_dict['y'])

    all_results_dict = {}  # save all results in dict
    for key, value_dict in dataset_dict['test_set_dict'].items():
        # print(f'test {kkmeans_inst.alg_name} on {key} with AE_thres: {kkmeans_inst.thres_AE}')
        X_test, y_test = value_dict['X'], value_dict['y']
        test_set_name = key

        # different_thres_fnr_fpr_flg = True
        # if different_thres_fnr_fpr_flg:
        #     thres_lst = np.linspace(0, 3, 10)
        #     kkmeans_inst.test_different_thres(X=X_test, y=y_test, thres_lst=thres_lst)
        #
        # if conf_inst.balance_flg:
        #     print(f'--balance \'{test_set_name}\'')
        #     value_dict = {'X': X_test, 'y': y_test}
        #     value_dict = balance_dict(value_dict)
        #     X_test = value_dict['X']
        #     y_test = value_dict['y']

        kkmeans_inst.test(X=X_test, y=y_test)

        if key not in all_results_dict.keys():
            all_results_dict[key] = {}
        all_results_dict[key]['AE'] = {'y_true': y_test, 'y_pred': kkmeans_inst.y_pred, 'y_proba': kkmeans_inst.y_proba,
                                       'reconstr_errors': kkmeans_inst.reconstr_errors_arr}

    # ################## ROC of all result #################################################
    # # save_roc_to_txt(out_file=roc_out_file, all_results_dict=all_results_dict)
    # for key, value_dict in all_results_dict.items():
    #     test_set_name = key
    #     roc_out_file = concat_path(conf_inst.output_dir + '/figures', f'{test_set_name}_roc.pdf')
    #     plot_roc_curve(all_results_dict=value_dict, out_file=roc_out_file, title_flg=conf_inst.title_flg,
    #                        title='roc')


if __name__ == '__main__':
    main_for_kernel_kmeans()
