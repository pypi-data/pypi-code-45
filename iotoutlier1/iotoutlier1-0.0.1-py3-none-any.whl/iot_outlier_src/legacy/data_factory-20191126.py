import os
import pickle
from collections import OrderedDict

import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.utils import shuffle

from data_process import _fix_data, _get_fft_data, Dataset
from data_process import _load_pcap_to_flows, _flows_to_samp_basic_features, \
    _flows_to_basic_features, _flows_to_IAT_features, random_select_flows, _load_labels_and_label_flows
from data_process import keep_ips_in_pcap
from utils.tool import get_file_path, dump_data, pprint, merge_pcaps, merge_labels, stat_data


class DataFactory:

    def __init__(self, dataset_name='', params=''):
        self.params = params
        self.dataset_name = dataset_name
        self.params['dataset_name'] = self.dataset_name

    def run(self):

        if self.dataset_name == 'CICIDS2017':
            self.srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
            self.ds_inst = DatasetCICIDS2017(self.srcIP_lst, self.params)
        elif self.dataset_name == 'SMTV':
            self.srcIP_lst = ['multi-srcIPs']
            self.ds_inst = DatasetSMTV(self.srcIP_lst, self.params)
        elif self.dataset_name == 'DEMO':
            # self.srcIP_lst = ['192.168.10.5', '192.168.10.8']
            # self.ds_inst = DatasetCICIDS2017(self.srcIP_lst, self.params)  # test CICIDS2017
            self.srcIP_lst = ['192.168.10.5', '192.168.10.8']
            self.ds_inst = DatasetSMTV(self.srcIP_lst, self.params)  # test SMTV
        else:
            msg = f'{self.dataset_name} is not correct.'
            raise ValueError(msg)

        self.ds_inst.run()  # data process:  # 1) pcap2features, 2) get train set and test set 3) update params
        self.dataset_dict = self.ds_inst.dataset_dict
        pprint(self.dataset_dict, name='DataFactory.dataset_dict', verbose=self.params['verbose'])


class DatasetCICIDS2017:
    def __init__(self, srcIP_lst, params):
        self.srcIP_lst = srcIP_lst
        self.params = params
        self.params['srcIP_lst'] = srcIP_lst
        self.dataset_dict = OrderedDict()
        self.params['dataset_dict'] = self.dataset_dict

    def run(self):
        if self.params['expt_name'] == 'INDV':  # only Friday data
            for i, srcIP in enumerate(self.srcIP_lst):
                sub_data_name = f'DS-srcIP_{srcIP}'  # DS: dataset
                pcap_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                          file_name=f'srcIP_{srcIP}.pcap')
                label_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                           file_name=f'srcIP_{srcIP}.csv')

                # 1) pcap2features 2) features to train and test set
                sd = SingleDataset(srcIP=srcIP, params=self.params,
                                   data_name=sub_data_name, pcap_file=pcap_file, label_file=label_file)
                sd.run()  # pcap2features, update params

                self.dataset_dict[sub_data_name] = sd  # {'sub_dataset_name': single_ds, ...}

        elif self.params['expt_name'] == 'AGMT':  # Friday + Monday data
            for i, srcIP in enumerate(self.srcIP_lst):
                sub_data_name = f'DS-srcIP_{srcIP}'  # DS: dataset
                pcap_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                          file_name=f'srcIP_{srcIP}.pcap')
                pcap_file_2 = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Monday-WorkingHours',
                                            file_name=f'srcIP_{srcIP}.pcap')
                mrg_pcap_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/AGMT-WorkingHours',
                                              file_name=f'srcIP_{srcIP}_AGMT.pcap')

                label_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                           file_name=f'srcIP_{srcIP}.csv')
                label_file_2 = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Monday-WorkingHours',
                                             file_name=f'srcIP_{srcIP}.csv')
                mrg_label_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/AGMT-WorkingHours',
                                               file_name=f'srcIP_{srcIP}_AGMT.csv')
                if self.params['overwrite']:
                    merge_pcaps([pcap_file, pcap_file_2], mrg_pcap_path=mrg_pcap_file)
                    merge_labels([label_file, label_file_2], mrg_label_path=mrg_label_file)

                # 1) pcap2features 2) features to train and test set
                sd = SingleDataset(srcIP=srcIP, params=self.params,
                                   data_name=sub_data_name, pcap_file=pcap_file, label_file=label_file)
                sd.run()  # pcap2features, update params

                self.dataset_dict[sub_data_name] = sd  # {'sub_dataset_name': single_ds, ...}
        elif self.params['expt_name'] == 'MIX':  # combine Friday data
            pcap_file_lst = []
            label_file_lst = []
            for i, srcIP in enumerate(self.srcIP_lst):
                sub_data_name = f'DS-srcIP_{srcIP}'
                pcap_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                          file_name=f'srcIP_{srcIP}.pcap')
                pcap_file_lst.append(pcap_file)
                label_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                           file_name=f'srcIP_{srcIP}.csv')
                label_file_lst.append(label_file)

            sub_data_name = 'DS-five_srcIPs'
            mrg_srcIP = 'five_srcIPs'
            mrg_pcap_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/MIX-WorkingHours',
                                          file_name=f'srcIP_{mrg_srcIP}.pcap')
            mrg_label_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/MIX-WorkingHours',
                                           file_name=f'srcIP_{mrg_srcIP}.csv')
            if self.params['overwrite']:
                merge_pcaps(pcap_file_lst, mrg_pcap_path=mrg_pcap_file)
                merge_labels(label_file_lst, mrg_label_path=mrg_label_file)

            # 1) pcap2features 2) features to train and test set
            sd = SingleDataset(srcIP=mrg_srcIP, params=self.params,
                               data_name=sub_data_name, pcap_file=mrg_pcap_file, label_file=mrg_label_file)
            sd.run()  # pcap2features, update params

            self.dataset_dict[sub_data_name] = sd  # {'sub_dataset_name': single_ds, ...}

        else:
            expt_name = self.params['expt_name']
            msg = f'{expt_name} is not correct.'
            raise ValueError(msg)


class DatasetSMTV:
    def __init__(self, srcIP_lst='', params=''):
        super(DatasetSMTV, self).__init__()
        self.srcIP_lst = srcIP_lst
        self.params = params
        self.params['srcIP_lst'] = srcIP_lst
        self.dataset_lst = []

    def run(self):
        if self.params['expt_name'] == ' INDV':  # only Friday data
            pass
        elif self.params['expt_name'] == ' AGMT':  # Friday + Monday data
            pass
        elif self.params['expt_name'] == 'MIX':  # combine Friday data
            # ipt_dir = 'input_data/smart-tv-roku-data'
            pass
        if self.params['overwrite']:
            srcIP, nrml_pcap, anml_pcap = get_nrml_anml_smart_tv_data(self.params['ipt_dir'],
                                                                      overwrite=self.params['overwrite'])
        else:
            srcIP = 'multi-srcIPs'
            nrml_pcap = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/src_10.42.0.119_merged_normal.pcap'
            anml_pcap = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/src_10.42.0.119_merged_anomaly.pcap'

        self.params['nrml_pcap'] = nrml_pcap
        self.params['anml_pcap'] = anml_pcap
        self.dataset_lst.append(SingleDataset(srcIP=srcIP, params=self.params))


def get_nrml_anml_smart_tv_data(ipt_dir, keep_ip='10.42.0.119', overwrite=True):
    # src_lst = ['10.42.0.119', '10.42.0.120', '10.42.0.119',
    #            '10.42.0.120', '10.42.0.119', '10.42.0.119',
    #            '10.42.0.120', '10.42.0.120', '10.42.0.119',
    #            '10.42.0.119', '10.42.0.120', '10.42.0.120']  # filter unrelated packets
    # pcap_lst = ['48626-1569697955-normal.pcap', '54065-1569633493-normal.pcap', '36732-1569696202-normal.pcap',
    #             '222279-1569631187-normal.pcap', '71376-1569639462-normal.pcap', '48631-1569699232-normal.pcap',
    #             '258327-1569630531-normal.pcap', '121375-1569631825-normal.pcap',
    #             '16184-1569701783-normal.pcap',
    #             '25082-1569695098-normal.pcap', '13933-1569628870-normal.pcap',
    #             '172665-1569633928-normal.pcap']  # normal

    pcap_file_lst = []
    nrml_dir = os.path.join(ipt_dir, 'raw_pcap', 'normal')
    srcIP = '10.42.0.1'
    for i, pcap in enumerate(os.listdir(nrml_dir)):
        if not pcap.endswith('.pcap'):
            print(f'i:{i+1}, pcap:{pcap}')
            continue
        # pcap = os.path.join(nrml_dir,pcap)
        # pcap_lst.append(pcap)
        pcap_file_lst.append(os.path.join(nrml_dir, pcap))
    sub_data_name = 'DS-multi-srcIPs'
    nrml_pcap = get_file_path(ipt_dir, sub_dir=f'{sub_data_name}/normal_anomaly', file_name='normal.pcap')
    merge_pcaps(pcap_file_lst, mrg_pcap_path=nrml_pcap)
    src_nrml_pcap = get_file_path(ipt_dir, sub_dir=f'{sub_data_name}/normal_anomaly',
                                  file_name=f'srcIP_{srcIP}_normal.pcap')
    if overwrite:
        keep_ips_in_pcap(input_file=nrml_pcap, output_file=src_nrml_pcap, kept_ips=[srcIP])

    # src_lst = [keep_ip] * len(pcap_lst)
    # pcap_file_lst = []
    # for i, (src, pcap_file) in enumerate(zip(src_lst, pcap_lst)):
    #     pcap_file_i = get_file_path(ipt_dir,  'raw_pcap/normal', sub_dir_l2='', file_name=pcap_file)
    #     pcapout_file = os.path.join(ipt_dir, f'multi-srcIPs/normal_anomaly/srcIP_{src}_{pcap_file}')
    #     print(f'i:{i+1}, pcapout_file:{pcapout_file}')
    #     if overwrite:
    #         keep_ips_in_pcap(input_file=pcap_file_i, output_file=pcapout_file, kept_ips=['10.42.0.119'])
    #     pcap_file_lst.append(pcapout_file)
    # nrml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_normal.pcap')
    # merge_pcaps(pcap_file_lst, mrg_pcap_path=nrml_pcap)
    # nrml_label = generate_label(nrml_pcap, label='NORMAL')

    # # src_lst = ['10.42.0.120', '10.42.0.120', '10.42.0.119']  # filter unrelated packets
    # # pcap_file_lst = ['12-1569622891.pcap', '2285-1569623141.pcap', '18502-1569700271.pcap']  # anomaly
    # pcap_lst = []
    # anml_dir = os.path.join(ipt_dir,'raw_pcap','anomaly')
    # for i, pcap in enumerate(os.listdir(anml_dir)):
    #     if not pcap.endswith('.pcap'):
    #         print(f'i:{i+1}, pcap:{pcap}')
    #         continue
    #     # pcap = os.path.join(anml_dir, pcap)
    #     pcap_lst.append(pcap)
    #
    # src_lst = [keep_ip] * len(pcap_lst)
    #
    # pcap_file_lst=[]
    # for i, (src, pcap_file) in enumerate(zip(src_lst, pcap_lst)):
    #     pcap_file_i = get_file_path(ipt_dir, 'raw_pcap/anomaly', sub_dir_l2='', file_name=pcap_file)
    #     pcapout_file = os.path.join(ipt_dir, f'multi-srcIPs/normal_anomaly/srcIP_{src}_{pcap_file}')
    #     print(f'i:{i+1}, pcapout_file:{pcapout_file}')
    #     if overwrite:
    #         keep_ips_in_pcap(input_file=pcap_file_i, output_file=pcapout_file, kept_ips=['10.42.0.119'])
    #     pcap_file_lst.append(pcapout_file)
    # anml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_anomaly.pcap')
    # merge_pcaps(pcap_file_lst, mrg_pcap_path=anml_pcap)
    # anml_label = generate_label(anml_pcap, label='ANOMALY')

    pcap_file_lst = []
    srcIP = '10.42.0.119'
    anml_dir = os.path.join(ipt_dir, 'raw_pcap', 'anomaly')
    for i, pcap in enumerate(os.listdir(anml_dir)):
        if not pcap.endswith('.pcap'):
            print(f'i:{i+1}, pcap:{pcap}')
            continue
        # pcap = os.path.join(nrml_dir,pcap)
        # pcap_lst.append(pcap)
        pcap_file_lst.append(os.path.join(anml_dir, pcap))
    anml_pcap = get_file_path(ipt_dir, sub_dir=f'{sub_data_name}/normal_anomaly', file_name='anomaly.pcap')
    merge_pcaps(pcap_file_lst, mrg_pcap_path=anml_pcap)
    # anml_label = generate_label(anml_pcap, label='ANOMALY')
    src_anml_pcap = get_file_path(ipt_dir, sub_dir=f'{sub_data_name}/normal_anomaly',
                                  file_name=f'srcIP_{srcIP}_anomaly.pcap')
    if overwrite:
        keep_ips_in_pcap(input_file=anml_pcap, output_file=src_anml_pcap, kept_ips=[srcIP])

    return 'multi-srcIPs', src_nrml_pcap, src_anml_pcap


class BaseDataset():

    def __init__(self, input_file=''):
        self.input_file = input_file

    def load_data(self):
        self.fids, self.features, self.labels = self.load_pickled_data(input_file=self.input_file)

    def load_pickled_data(self, input_file):
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

    def split_train_test(self, features='', labels='', shuffle_flg=True, random_state=42):

        X_normal = []
        y_normal = []
        X_anomaly = []
        y_anomaly = []
        none_num = 0

        for i, value in enumerate(labels):
            feat = list(features[i])
            if value.upper() in ['NORMAL', 'BENIGN']:
                X_normal.append(feat)
                y_normal.append(0)
            elif value.upper() in ['BOT', 'ANOMALY']:
                X_anomaly.append(feat)
                y_anomaly.append(1)
            else:  # label in [None, 'None', ... ]
                print(f'i:{i}, {value}')
                none_num += 1
        print(f'{none_num} flows appear in pcap, however, don\'t appear in labels.csv')
        print(f'0: Normal, 1: Anomaly')

        if shuffle_flg:  # random select a part of normal flows from normal flows
            c = list(zip(X_normal, y_normal))
            X_normal, y_normal = zip(*shuffle(c, random_state=random_state))

        X_normal = np.array(X_normal, dtype=float)
        y_normal = np.array(y_normal, dtype=int)
        X_anomaly = np.array(X_anomaly, dtype=float)
        y_anomaly = np.array(y_anomaly, dtype=int)

        if len(y_anomaly) == 0:
            print(f'no anomaly data in this data_process')
            train_size = len(y_normal) - 100  # use 100 normal flows as test set.
            X_train = X_normal[:train_size, :]
            y_train = y_normal[:train_size]
            X_test = X_normal[:100, :]
            y_test = y_normal[:100]
        else:
            train_size = len(y_normal) - len(y_anomaly)
            X_train = X_normal[:train_size, :]
            y_train = y_normal[:train_size]
            X_test = np.concatenate([X_normal[train_size:, :], X_anomaly], axis=0)
            y_test = np.concatenate([y_normal[train_size:], y_anomaly], axis=0)

        print(f'--- train set and test set --'
              f'\nX_train:{X_train.shape}, y_train:{Counter(y_train)}'
              f'\nX_test :{X_test.shape}, y_test :{Counter(y_test)}, in which, 0: normals and 1: anomalies.')
        stat_data(X_train, name='X_train')
        stat_data(X_test, name='X_test')

        return X_train, y_train, X_test, y_test

    def normalise_data(self, X_train, X_test, norm_method='std'):
        """ if normalise data or not

        :param X_train:
        :param X_test:
        :param norm_method:
        :return:
        """
        print(f'2) normalization ({norm_method})')
        if norm_method in ['min-max', 'std', 'robust']:
            if norm_method == 'min-max':  # (x-min)/(max-min)
                self.train_scaler = MinMaxScaler()
            elif norm_method == 'std':  # (x-u)/sigma
                self.train_scaler = StandardScaler()
            elif norm_method == 'robust':  # (x-Q2)/(Q3-Q1)
                self.train_scaler = RobustScaler()
            self.train_scaler.fit(X_train)
            X_train = self.train_scaler.transform(X_train)
            X_test = self.train_scaler.transform(X_test)

            print('after normalization: X_train distribution:')
            stat_data(X_train, name='X_train')
            print('after normalization:X_test distribution:')
            stat_data(X_test, name='X_test')

            return X_train, X_test

        elif norm_method == 'log':  # log scaler
            # X_train = np.log(X_train)         # np.log(v): v > 0
            min_trainvalues = np.min(X_train, axis=0)
            X_train = np.log(X_train - min_trainvalues + 1)  # X_train-in_values + 1: scale all values to [1, . ]
            # and np.log(values) will be [0, .]

            X_test = np.clip(X_test - min_trainvalues, a_min=0, a_max=10e+6)  # all values less than 0 are clipped to 0
            X_test = np.log(X_test + 1)

            print('after normalization: X_train distribution:')
            stat_data(X_train, name='X_train')
            print('after normalization:X_test distribution:')
            stat_data(X_test, name='X_test')

            return X_train, X_test

        elif norm_method == 'none' or norm_method == None:
            print('without normalization')
            return X_train, X_test

        else:
            print(f'norm_method: {norm_method} is not implemented yet, please check and retry')
            return -1


class SingleDataset(BaseDataset):

    def __init__(self, srcIP='', data_name='', params='', **kwargs):
        # super(SingleDataset, self).__init__()

        for i, (key, value) in enumerate(kwargs.items()):
            self.key = value

        self.kwargs = kwargs
        self.single_data_name = data_name
        self.srcIP = srcIP
        self.params = params
        # self.params['srcIP'] = srcIP

    def run(self):

        # 1. pcap2flows
        if self.params['dataset_name'] in ['CICIDS2017', 'DEMO']:
            self.pcap_file = self.kwargs['pcap_file']
            self.label_file = self.kwargs['label_file']
            self.flows, self.labels = self.pcap2flows_CICIDS2017(pcap_file=self.pcap_file, labels_csv=self.label_file)

        elif self.params['dataset_name'] == 'SMTV':
            self.nrml_pcap = self.kwargs['nrml_pcap']
            self.anml_pcap = self.kwargs['label_file']
            self.flows, self.labels = self.pcap2flows_SMTV(pcap_file_lst=[self.nrml_pcap, self.anml_pcap])
            pcap_dir = 'multi-srcIPs'
            self.pcap_file = os.path.join(self.params['ipt_dir'], f'{pcap_dir}/{self.srcIP}')
            self.label_file = ''
        else:
            dataset_name = self.params['dataset_name']
            msg = f'{dataset_name} is not implemented.'
            raise ValueError(msg)

        # 2. flow2features
        self.flows2features(self.flows, self.labels)  # get iat_file, stat_file, samp_file, sampling_rate.

        # 3. features2dataset
        self.features2dataset()  # get self.iat_dict, self.fft_dict

        self.dataset_dict = OrderedDict()  # # iat_dict, fft_dict, stat_dict, samp_dict
        self.dataset_dict['iat_dict'] = self.iat_dict
        self.dataset_dict['fft_dict'] = self.fft_dict
        self.dataset_dict['stat_dict'] = self.stat_dict
        self.dataset_dict['samp_dict'] = self.samp_dict

    def features2dataset(self):
        for i, value_dict in enumerate([self.iat_dict, self.stat_dict, self.samp_dict]):
            pprint(value_dict, name='value_dict')
            feat_file = value_dict['feat_file']
            obj_i = Dataset(input_file=feat_file)
            feat_set = value_dict['feat_set']
            if feat_set == 'iat_set':
                # 1. IAT_fixed data
                q_fixed_iat = self.iat_dict['q_fixed_iat']
                bin_size = self.iat_dict['bin_size']
                fixed_iat_file = feat_file + f'-{feat_set}-q_fixed_iat_{q_fixed_iat}-dim_{bin_size}.dat'
                fixed_iat_features = _fix_data(obj_i.features, bin_size)
                dump_data((obj_i.fids, fixed_iat_features, obj_i.labels), output_file=fixed_iat_file)
                self.iat_dict['fixed_feat_file'] = fixed_iat_file
                x_train, y_train, x_test, y_test = obj_i.split_train_test(features=fixed_iat_features,
                                                                          labels=obj_i.labels)
                self.iat_dict['data'] = (x_train, y_train, x_test, y_test)

                # 2. fft_fixed data
                # save the fixed FFT with fft_bins
                fft_part = 'real'
                feat_set = 'fft_set'
                self.fft_dict = {'feat_set': feat_set, 'fixed_feat_file': '', 'data': '', 'fft_part': fft_part,
                                 'fft_bin': bin_size, 'q_fixed_iat': q_fixed_iat}
                if fft_part == 'real+imaginary':
                    fixed_fft_file = feat_file + f'-{feat_set}-q_fixed_iat_{q_fixed_iat}-dim_{bin_size*2}-fft_part_{fft_part}.dat'  # real + imaginary
                else:
                    fixed_fft_file = feat_file + f'-{feat_set}-q_fixed_iat_{q_fixed_iat}-dim_{bin_size}-fft_part_{fft_part}.dat'  # real

                fixed_fft_features = _get_fft_data(obj_i.features, fft_bin=bin_size, fft_part=fft_part)
                dump_data((obj_i.fids, fixed_fft_features, obj_i.labels), output_file=fixed_fft_file)
                self.fft_dict['fixed_feat_file'] = fixed_fft_file
                x_train, y_train, x_test, y_test = obj_i.split_train_test(features=fixed_fft_features,
                                                                          labels=obj_i.labels)
                self.fft_dict['data'] = (x_train, y_train, x_test, y_test)

            elif feat_set == 'stat_set':
                # 3. stat_set
                x_train, y_train, x_test, y_test = obj_i.split_train_test(features=obj_i.features, labels=obj_i.labels)
                self.stat_dict['data'] = (x_train, y_train, x_test, y_test)
            elif feat_set == 'samp_set':
                # 4. sampling_fixed data
                # q_sampling_rate = self.samp_dict['q_sampling_rate']
                # sampling_rate = self.samp_dict['sampling_rate']
                fixed_samp_file = feat_file + f'-{feat_set}-q_fixed_iat_{q_fixed_iat}-dim_{bin_size}.dat'
                fixed_samp_features = _fix_data(obj_i.features, bin_size)
                dump_data((obj_i.fids, fixed_samp_features, obj_i.labels), output_file=fixed_samp_file)
                self.samp_dict['fixed_feat_file'] = fixed_samp_file
                x_train, y_train, x_test, y_test = obj_i.split_train_test(features=fixed_samp_features,
                                                                          labels=obj_i.labels)
                self.samp_dict['data'] = (x_train, y_train, x_test, y_test)

        pprint(self.iat_dict, name='iat_dict')
        pprint(self.fft_dict, name='fft_dict')

    def load_pickled_data(self, input_file):
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

    def pcap2flows_CICIDS2017(self, pcap_file, labels_csv):
        num_pkt_thresh = 2
        flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh)  # get all flows which at least has more than 2 packets
        print(f'num. of flows: {len(flows)}')
        labels = _load_labels_and_label_flows(labels_csv, features=[(fid, _) for fid, _, _ in flows])

        flows, labels = random_select_flows(flows, labels, experiment=self.params['expt_name'])
        # labels = _load_labels_and_label_flows(labels_csv, features)
        print(f'num. of labels: {len(labels)}')
        # # fids, features = list(*zip(features))

        return flows, labels

    def flows2features(self, flows, labels):
        pcap_file = self.pcap_file
        # IAT value
        fids_features = _flows_to_IAT_features(flows)
        fids = list(map(lambda x: x[0], fids_features))
        features = list(map(lambda x: x[1], fids_features))
        print(f'num. of flows: {len(fids)}')
        feat_set = 'iat_set'
        iat_file = f'{pcap_file}-{feat_set}.dat'  # store IATs which have different dimensions to file
        dump_data(data=(fids, features, labels), output_file=iat_file)
        # self.params['iat_dict'] = {'feat_set': feat_set, 'feat_file': iat_file,
        #                            'q_fixed_iat':self.params['q_fixed_iat']}

        self.iat_dict = {'feat_set': feat_set, 'feat_file': iat_file,
                         'q_fixed_iat': self.params['q_fixed_iat']}

        q_fixed_iat = self.params['q_fixed_iat']
        fft_bin = int(np.round(np.quantile([len(iat) for iat in features], q=self.params['q_fixed_iat'])))
        print(f'fft_bin: {fft_bin} when q_fixed_iat equals {q_fixed_iat}')
        # fftbin_lst.append(fft_bin)
        # self.params['bin_size'] = fft_bin
        # self.params['iat_dict']['bin_size'] = fft_bin
        self.iat_dict['bin_size'] = fft_bin

        # stat_set:
        fids_features = _flows_to_basic_features(flows)
        fids = list(map(lambda x: x[0], fids_features))
        features = list(map(lambda x: x[1], fids_features))
        feat_dim = len(features[0])
        feat_set = 'stat_set'
        print(f'feat_set: {feat_set}, dimension: {feat_dim}')
        stat_file = f'{pcap_file}-{feat_set}-dim_{feat_dim}.dat'  # store Baseline 1 with fixed size
        dump_data(data=(fids, features, labels), output_file=stat_file)
        # self.params['stat_dict'] = {'feat_set': 'stat_set', 'feat_file': stat_file}
        self.stat_dict = {'feat_set': 'stat_set', 'feat_file': stat_file}

        sampling_type = self.params['sampling_method']
        q_sampling_rate = self.params['q_sampling_rate']
        sampling_arr = [(max(times) - min(times)) / fft_bin for fid, times, sizes in
                        flows]  # flow_duration/fft_bin
        # print(f'Counter(sampling_arr): {list(Counter(sampling_arr))[:100]}')   # [:100] for saving memory. if not, script will fails due to the lack of memory
        sampling = np.quantile(sampling_arr,
                               q=self.params[
                                   'q_sampling_rate'])  # make 0.9 flow_duration /fft bin less than the sampling_rate.
        # sampling = float(f'{sampling:.4f}')           # if only keep .4f, sampling will be 0.
        print(f'sampling_type: {sampling_type}, samping: {sampling}')
        self.params['sampling_rate'] = sampling
        fids_features = _flows_to_samp_basic_features(flows, sampling_type=self.params['sampling_method'],
                                                      sampling=sampling)
        fids = list(map(lambda x: x[0], fids_features))
        features = list(map(lambda x: x[1], fids_features))
        feat_set = 'samp_set'
        print(
            f'feat_feat: {feat_set}, with different lengths. sampling_type: {sampling_type}, sampling: {sampling}')
        # store sampled IATs which have different dimensions to file
        samp_file = f'{pcap_file}-{feat_set}-{sampling_type}_{sampling}-q_sampling_rate_{q_sampling_rate}.dat'
        dump_data(data=(fids, features, labels), output_file=samp_file)
        # break
        # self.params['samp_dict'] = {'feat_set': feat_set, 'feat_file': samp_file, 'sampling_rate': sampling,
        #                             'q_sampling_rate': q_sampling_rate}
        self.samp_dict = {'feat_set': feat_set, 'feat_file': samp_file, 'sampling_rate': sampling,
                          'q_sampling_rate': q_sampling_rate}

    def pcap2flows_SMTV(self, pcap_file_lst):
        num_pkt_thresh = 2
        flows = []
        labels = []
        for i, pcap_file in enumerate(pcap_file_lst):
            flows_i = _load_pcap_to_flows(pcap_file,
                                          num_pkt_thresh)  # get all flows which at least has more than 2 packets
            flows.extend(flows_i)
            print(f'num. of flows_i: {len(flows_i)}')
            if 'merged_normal.pcap' in pcap_file:
                labels_i = ['Normal'] * len(flows_i)
            elif 'merged_anomaly.pcap' in pcap_file:
                labels_i = ['Anomaly'] * len(flows_i)
            else:
                labels_i = ['None'] * len(flows_i)
            labels.extend(labels_i)
        print(f'num. of flows: {len(flows)}')
        print(f'num. of labels: {len(labels)}')

        return flows, labels

    #
    # def normalise_data(self, X_train, X_test, norm_method='std'):
    #     """ if normalise data or not
    #
    #     :param X_train:
    #     :param X_test:
    #     :param norm_method:
    #     :return:
    #     """
    #     print(f'2) normalization ({norm_method})')
    #     if norm_method in ['min-max', 'std', 'robust']:
    #         if norm_method == 'min-max':  # (x-min)/(max-min)
    #             self.train_scaler = MinMaxScaler()
    #         elif norm_method == 'std':  # (x-u)/sigma
    #             self.train_scaler = StandardScaler()
    #         elif norm_method == 'robust':  # (x-Q2)/(Q3-Q1)
    #             self.train_scaler = RobustScaler()
    #         self.train_scaler.fit(X_train)
    #         X_train = self.train_scaler.transform(X_train)
    #         X_test = self.train_scaler.transform(X_test)
    #
    #         print('after normalization: X_train distribution:')
    #         stat_data(X_train, name='X_train')
    #         print('after normalization:X_test distribution:')
    #         stat_data(X_test, name='X_test')
    #
    #         return X_train, X_test
    #
    #     elif norm_method == 'log':  # log scaler
    #         # X_train = np.log(X_train)         # np.log(v): v > 0
    #         min_trainvalues = np.min(X_train, axis=0)
    #         X_train = np.log(X_train - min_trainvalues + 1)  # X_train-in_values + 1: scale all values to [1, . ]
    #         # and np.log(values) will be [0, .]
    #
    #         X_test = np.clip(X_test - min_trainvalues, a_min=0,
    #                          a_max=10e+6)  # all values less than 0 are clipped to 0
    #         X_test = np.log(X_test + 1)
    #
    #         print('after normalization: X_train distribution:')
    #         stat_data(X_train, name='X_train')
    #         print('after normalization:X_test distribution:')
    #         stat_data(X_test, name='X_test')
    #
    #         return X_train, X_test
    #
    #     elif norm_method == 'none' or norm_method == None:
    #         print('without normalization')
    #         return X_train, X_test
    #
    #     else:
    #         print(f'norm_method: {norm_method} is not implemented yet, please check and retry')
    #         return -1
