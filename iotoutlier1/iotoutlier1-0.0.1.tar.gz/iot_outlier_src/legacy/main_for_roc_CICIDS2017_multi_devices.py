# Authors: kun.bj@outlook.com
#
# License: xxx
"""
    Purpose: ROC

"""
import pickle
import subprocess

# from random import shuffle
from scipy.spatial import distance
from sklearn.utils import shuffle

from detector.ocsvm_class import OCSVM_Class
from legacy.utils.dataset import stat_data

"""
    Purpose:
        main function for feature set comparison.

"""
from collections import Counter, OrderedDict

from sklearn.preprocessing import MinMaxScaler, StandardScaler

from _config import *
from legacy.utils import load_and_split_data
from legacy.utils.visualization import plot_roc
import os


def load_and_split_data(input_file='', case='', shuffle_flg=True, random_state=random_state):
    print(f'input_file: {input_file}')
    print('1) load data and split it to train set and test set, normal and anormaly in test set with ratio: 1:1')
    fids, features, labels = load_pickled_data(input_file)

    feat_set = case.split()[0]
    if feat_set in ['IAT', 'FFT']:
        feat_len_arr = [len(v) for v in features]
        fft_bins = int(np.quantile(feat_len_arr, q=0.9))
    else:  # for baseline_set, no need fft_bins
        fft_bins = 0
    print(f'feat_set: {feat_set}, fft_bins:{fft_bins}')

    X_normal = []
    y_normal = []
    X_anomaly = []
    y_anomaly = []
    none_num = 0
    for i, value in enumerate(labels):
        feat = list(features[i])  # (fid, IAT)
        if feat_set == 'IAT':
            if len(feat) > fft_bins:
                feat = feat[:fft_bins]
            else:
                feat += [0] * (fft_bins - len(feat))
        else:  # baseline_set
            # nothing need to do
            pass
        if value.upper() in ['NORMAL', 'BENIGN']:
            X_normal.append(feat)
            y_normal.append(0)
        elif value.upper() in ['NONE']:  # flow appears in pcap, however, does not in labels.csv
            none_num += 1
            continue
        else:
            X_anomaly.append(feat)
            y_anomaly.append(1)

    print(f'{none_num} flows appear in pcap, however, don\'t appear in labels.csv')
    if shuffle_flg:
        c = list(zip(X_normal, y_normal))
        # shuffle(c)
        X_normal, y_normal = zip(*shuffle(c, random_state=random_state))

    X_normal = np.array(list(X_normal), dtype=float)
    y_normal = np.array(y_normal, dtype=int)
    X_anomaly = np.array(X_anomaly, dtype=float)
    y_anomaly = np.array(y_anomaly, dtype=int)

    train_size = len(y_normal) - len(y_anomaly)
    X_train = X_normal[:train_size, :]
    y_train = y_normal[:train_size]
    if len(y_anomaly) == 0:
        X_test = X_normal[:100, :]
        y_test = y_normal[:100]
    else:
        X_test = np.concatenate([X_normal[train_size:, :], X_anomaly], axis=0)
        y_test = np.concatenate([y_normal[train_size:], y_anomaly], axis=0)

    return X_train, y_train, X_test, y_test, fft_bins


def normalise_data(X_train, X_test, norm_method='std'):
    print(f'\n2) normalization ({norm_method})')
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
# def grid_search_cv():
#     Cs = [0.001, 0.01, 0.1, 1, 10]
#     gammas = [0.001, 0.01, 0.1, 1]
#     param_grid = {'C': Cs, 'gamma': gammas}
#     grid_search = GridSearchCV(svm.SVC(kernel='rbf'), param_grid, cv=nfolds)
#     grid_search.fit(X, y)
#
#     return grid_search.best_params_


def main_for_each_feature_set(input_file='', case='', random_state=42, norm_method='std'):
    """

    :param norm_file:
    :param anomaly_file:
    :param test_size:
    :param random_state:
    :return:
    """
    X_train, y_train, X_test, y_test, fft_bins = load_and_split_data(input_file=input_file, case=case, shuffle_flg=True,
                                                                     random_state=random_state)
    print(f'--- train set and test set --'
          f'\nX_train:{X_train.shape}, y_train:{Counter(y_train)}'
          f'\nX_test :{X_test.shape}, y_test :{Counter(y_test)}, in which, 0: normals and 1: anomalies.')
    stat_data(X_train)
    stat_data(X_test)

    X_train, X_test = normalise_data(X_train, X_test, norm_method=norm_method)

    print('\n3) train and test different models')
    roc_dict = {}
    auc_dict = {}

    distances = distance.pdist(X_train, metric='euclidean')
    print(f'max_distance: {max(distances)}, min_distance: {min(distances)}')

    grid_serach_flg = False
    if grid_serach_flg:
        # sigma = np.quantile(distances, q=q)
        # gamma = 1 / (sigma ** 2)
        # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(), key=lambda item: item[0])}')
        # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}')

        auc_max = 0
        for q in np.linspace(0.0, 1.0, 11):
            if q == 0.0:
                sigma = next((x for i, x in enumerate(sorted(distances)) if x),
                             None)  # return the first non-zero element.

                # continue
            elif q == 1.0:
                sigma = max(distances)
            else:
                sigma = np.quantile(distances, q=q)
            gamma = 1 / (sigma ** 2)
            # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(), key=lambda item: item[0])}')
            print(f'gamma:{gamma}, q:{q}, sigma:{sigma}')
            ocsvm = OCSVM_Class(gamma=gamma)
            ocsvm.fit(X_train)
            # dump(ocsvm, 'output_data/models_dumping/ocsvm_' + case + '.joblib')
            # model = load('output_data/models_dumping/ocsvm_' + case + '.joblib')
            ocsvm.test(X_test, y_test)
            print(f'auc:{ocsvm.auc}')
            if ocsvm.auc > auc_max:
                auc_max = ocsvm.auc
                gamma_max = gamma
                q_max = q
                roc_dict['ocsvm'] = {'y_true': y_test, 'y_scores': ocsvm.y_scores}
                auc_dict['ocsvm'] = ocsvm.auc

        print(f'auc_max:{auc_max}, gamma_max:{gamma_max}, q_max:{q_max}')
        # Cs = [0.001, 0.01, 0.1, 1, 10]
        # gamma = [ 1/ np.quantile(distances, q=q)**2 for q in np.linspace(0,1,11)]
        # nfolds = 3
        # # param_grid = {'C': Cs, 'gamma': gamma}
        # param_grid = {'gamma': gamma}
        # grid_search = GridSearchCV(estimator=OCSVM_Class(gamma=gamma), param_grid=param_grid, cv=nfolds)
        # grid_search.fit(X_train, y=None)
        #
        # print(f'grid_search.best_params_:{grid_search.best_params_}')

        #     return grid_search.best_params_
    else:
        q = 0.3
        print('without grid search cv')
        sigma = np.quantile(distances, q=q)
        gamma = 1 / (sigma ** 2)
        # print(f'gamma:{gamma}, q:{q}, sigma:{sigma}, Counter(distances):{sorted(Counter(distances).items(), key=lambda item: item[0])}')
        print(f'gamma:{gamma}, q:{q}, sigma:{sigma}')
        ocsvm = OCSVM_Class(gamma=gamma)
        ocsvm.fit(X_train)
        # dump(ocsvm, 'output_data/models_dumping/ocsvm_' + case + '.joblib')
        # model = load('output_data/models_dumping/ocsvm_' + case + '.joblib')
        ocsvm.test(X_test, y_test)
        roc_dict['ocsvm'] = {'y_true': y_test, 'y_scores': ocsvm.y_scores}
        auc_dict['ocsvm'] = ocsvm.auc

        # gmm = GMM_Class(n_components=5, covariance_type='diag')
        # gmm.train(X_train)
        # # dump(pca, 'output_data/models_dumping/gmm_' + case + '.joblib')
        # # model = load('output_data/models_dumping/gmm_' + case + '.joblib')
        # gmm.test(X_test, y_test)
        # roc_dict['gmm'] = {'y_true': y_test, 'y_scores': gmm.y_scores}
        # auc_dict['gmm'] = gmm.auc

    # knn = KNN_Class()
    # knn.train(X_train)
    # # dump(pca, 'output_data/models_dumping/knn_' + case + '.joblib')
    # # model = load('output_data/models_dumping/knn_' + case + '.joblib')
    # knn.test(X_test, y_test)
    # roc_dict['knn'] = {'y_true': y_test, 'y_scores': knn.y_scores}
    # auc_dict['knn'] = knn.auc
    # knn.visualize(X_train[:,:2], y_train, X_test[:,:2], y_test, knn.knn.predict(X_train), knn.knn.predict(X_test), show_figure=True)

    # pca = PCA_Class()
    # pca.train(X_train)
    # # dump(pca, 'output_data/models_dumping/pca_' + case + '.joblib')
    # # model = load('output_data/models_dumping/pca_' + case + '.joblib')
    # pca.test(X_test, y_test)
    # roc_dict['pca'] = {'y_true': y_test, 'y_scores': pca.y_scores}
    # auc_dict['pca'] = pca.auc

    # iforest = IForest_Class()
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


def main_for_roc(srcIP, experiment='', data_aug=False, norm_method='none'):
    """
        "test_size, random_state and so on", all of them come from _config.py.
    :return:
    """

    experi, case = experiment

    feat_set = case.split()[0]
    if experi == 'demo':
        files_dict = OrderedDict(
            {
                'proposed': f'input_data/data/test.pcap_{feat_set}.dat',
                'baseline': f'input_data/data/test.pcap_Baseline.dat'
            })
    else:
        files_dict = OrderedDict(
            {
                f'{feat_set}': f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_{feat_set}.dat',
                'baseline': f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_Baseline.dat'
            })
        if data_aug:
            files_aug_dict = OrderedDict(
                {
                    f'{feat_set}': f'input_data/CICIDS2017/srcIP_{srcIP}/Monday-WorkingHours/srcIP_{srcIP}.pcap_{feat_set}.dat',
                    'baseline': f'input_data/CICIDS2017/srcIP_{srcIP}/Monday-WorkingHours/srcIP_{srcIP}.pcap_Baseline.dat'
                })
            for i, (key, value) in enumerate(files_dict.items()):
                print(f'i:{i}, key:{key}')
                files_lst = [value, files_aug_dict[key]]
                merged_file = value + '_augmented.dat'
                files_dict[key] = merge_multifiles_to_one(files_lst=files_lst, output_file=merged_file)

    roc_dicts_lst = []
    auc_dicts_lst = []
    for idx, (key, file_path) in enumerate(files_dict.items()):
        print(f'\n{idx}: evaluation on {key}')

        roc_dict, auc_dict = main_for_each_feature_set(input_file=file_path, case=case,
                                                       random_state=random_state,
                                                       norm_method=norm_method)

        roc_dicts_lst.append([key, roc_dict])
        auc_dicts_lst.append([key, auc_dict])

    print('\n3: plot roc.')
    # plot_roc(roc_dicts_lst=roc_dicts_lst, title=f'srcIP: {srcIP}, {case}')
    plot_roc(roc_dicts_lst=roc_dicts_lst, title=f'srcIP: {srcIP}, OCSVM')
    # plot_auc_and_strength_of_outiler(auc_dicts_lst=auc_dicts_lst)


def merge_multifiles_to_one(files_lst=[], output_file=''):
    # os.chdir("/mydir")
    # extension = 'csv'
    # all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    # # combine all files in the list
    # combined_csv = pd.concat([pd.read_csv(f) for f in files_lst])  # different lines
    # # export to csv
    # combined_csv.to_csv(output_file, index=False, encoding='utf-8-sig')

    # with open(output_file, 'w') as out_hdl:
    #     for file in files_lst:
    #         with open(file, 'r') as in_hdl:
    #             line = in_hdl.readline()
    #             while line:
    #                 out_hdl.write(line)
    #                 line = in_hdl.readline()

    with open(output_file, 'wb') as out_hdl:
        # pickle.dump(len(files_lst), out_hdl)
        for file in files_lst:
            print(f'file:{file}')
            fids, features, labels = load_pickled_data(file)
            pickle.dump((fids, features, labels), out_hdl)
            # with open(file, 'rb') as in_hdl:
            #     fids, features, labels = pickle.load(in_hdl)
            #     pickle.dump((fids, features, labels), out_hdl)

    return output_file


def load_pickled_data(input_file=''):
    """ Especially for loading multi-objects stored in a file.

    :param input_file:
    :return:
    """

    fids = []
    features = []
    labels = []
    with open(input_file, 'rb') as in_hdl:
        while True:
            try:
                fids_, features_, labels_ = pickle.load(in_hdl)
                fids.extend(fids_)
                features.extend(features_)
                labels.extend(labels_)
            except EOFError:
                break
    return fids, features, labels


def obtain_fft_bins(features, q=0.9):
    # with open(v1_file, 'r') as in_hdl:
    #     line = in_hdl.readline()
    #     while line:
    #         arr = line.strip().split(',')
    #         features.append(arr[:-1])
    #         line = in_hdl.readline()
    flows_len_arr = [len(value) for value in features]
    fft_bins = int(np.quantile(flows_len_arr, q=q))
    print(f'choose quantile = {q} and get fft_bins: {fft_bins}.')
    print(f'len(flows_len_arr): {len(flows_len_arr)}, {sorted(set(flows_len_arr))}, {Counter(flows_len_arr)}')
    stat_data(np.array(flows_len_arr).reshape(-1, 1))

    return fft_bins


def obtain_normal_data(pcap_file, label=['Benign']):
    pcap_file = f'input_data/CICIDS2017/Merged-WorkingHours/5_bots_20170707-09_00-12_00-srcIP_{srcIP}.pcap'
    dir = os.path.dirname(pcap_file)
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not os.path.exists(pcap_file):
        # input_file = 'input_data/CICIDS2017/Merged-WorkingHours-Morning_5_bots_20170707-09_40-11_30.pcap'
        input_file = 'input_data/CICIDS2017/Friday-WorkingHours@5_Bots_SrcIPs-20170707-09_00-12_00.pcap'
        cmd = f"tshark -r {input_file} -w {pcap_file} ip.src=={srcIP}"
        print(f'{cmd}')
        result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')


def obtain_file_path(srcIP, feat_set='IAT', sub_pre='Friday-WorkingHours'):
    file_path = f'input_data/CICIDS2017/srcIP_{srcIP}/{sub_pre}/srcIP_{srcIP}.pcap_{feat_set}.dat'  # (fid, features), label
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    # v1_files = [IAT_file.format(srcIP) for srcIP in srcIP_lst]
    # v1_megerd_file = IAT_file.format()
    return file_path


def run_experiment(experiment=(), srcIP_lst=[], norm_method='std', data_aug=False):
    exper, case = experiment  # # case1:(IAT VS Baseline),  case 2 (FFT VS Baseline)
    print(f'exper: {exper}, case: {case}')

    if exper == 'demo':
        srcIP = srcIP_lst[0]
        print(f'demo_srcIP: {srcIP}')
        main_for_roc(srcIP, experiment=experiment, norm_method=norm_method, data_aug=data_aug)

    elif exper == 'individual':
        for i, srcIP in enumerate(srcIP_lst):
            print(f'indiv_srcIP: {srcIP}')
            main_for_roc(srcIP, experiment=experiment, norm_method=norm_method, data_aug=data_aug)

    elif exper == 'mix':
        # mix multi devices' data
        for feat_set in [case.split()[0], 'Baseline']:  # [IAT, Baseline] or [FFT, Baseline]
            files_lst = [obtain_file_path(srcIP, feat_set=feat_set, sub_pre='Friday-WorkingHours') for srcIP in
                         srcIP_lst]
            merged_file = obtain_file_path(srcIP='-'.join(srcIP_lst), feat_set=feat_set, sub_pre='Friday-WorkingHours')
            merged_file = merge_multifiles_to_one(files_lst=files_lst, output_file=merged_file)
            print(f'merged_file: {merged_file}')
        if data_aug:
            for feat_set in [case.split()[0], 'Baseline']:
                files_lst = [obtain_file_path(srcIP, feat_set=feat_set, sub_pre='Monday-WorkingHours') for srcIP in
                             srcIP_lst]
                merged_file = obtain_file_path(srcIP='-'.join(srcIP_lst), feat_set=feat_set,
                                               sub_pre='Monday-WorkingHours')
                merged_file = merge_multifiles_to_one(files_lst=files_lst, output_file=merged_file)
                print(f'merged_file: {merged_file}')
        main_for_roc(srcIP='-'.join(srcIP_lst), experiment=experiment, norm_method=norm_method, data_aug=data_aug)
    else:
        print('not implement')


if __name__ == '__main__':
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    experiment = ('individual', 'FFT VS Baseline')  # demo, individual, mix
    norm_method = 'none'  # none: without normalization, otherwise, min-max or std
    data_augmentation = False  # add more normal or not
    print(f'experiment:{experiment}, norm_method:{norm_method}, data_aug:{data_augmentation}')
    run_experiment(experiment=experiment, srcIP_lst=srcIP_lst, norm_method=norm_method, data_aug=data_augmentation)
