""" Data process

"""
# Authors: kun.bj@outlook.com
#
# License: xxx

# 1. system and built-in libraries
import os
import pickle
from collections import OrderedDict, Counter

# 2. thrid-part libraries
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.utils import shuffle

# 3. local libraries
from data_process.pcap2features_sampling import _load_pcap_to_flows, _flows_to_samp_basic_features, \
    _flows_to_basic_features, _flows_to_IAT_features, random_select_flows, _load_labels_and_label_flows, \
    _load_pcap_to_subflows
from data_process.pcap import keep_ips_in_pcap
from utils.tool import get_file_path, dump_data, pprint, merge_pcaps, merge_labels, stat_data


class DataFactory:

    def __init__(self, dataset_name='', params={}):
        self.dataset_name = dataset_name
        self.params = params
        self.params['dataset_name'] = self.dataset_name
        self.verbose = self.params['verbose']

    def run(self):

        if self.dataset_name == 'CICIDS2017':
            self.srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
            self.ds_inst = DatasetCICIDS2017(srcIP_lst=self.srcIP_lst, params=self.params)
        elif self.dataset_name == 'SMTV':
            self.srcIP_lst = ['multi-srcIPs']
            self.ds_inst = DatasetSMTV(srcIP_lst=self.srcIP_lst, params=self.params)
        elif self.dataset_name.startswith('DEMO'):
            if self.dataset_name == 'DEMO_CICIDS2017':
                self.srcIP_lst = ['192.168.10.5', '192.168.10.8']  # self.srcIP_lst = ['192.168.10.5', '192.168.10.8']
                # self.params['ipt_dir'] = os.path.join(self.params['ipt_dir'],'DEMO', 'CICIDS2017')
                self.ds_inst = DatasetCICIDS2017(self.srcIP_lst, self.params)  # test CICIDS2017
            elif self.dataset_name == 'DEMO_SMTV':
                self.srcIP_lst = ['multi-srcIPs']
                # self.params['ipt_dir'] = os.path.join(self.params['ipt_dir'],'DEMO', 'SMTV')
                self.ds_inst = DatasetSMTV(srcIP_lst=self.srcIP_lst, params=self.params)  # test SMTV
        else:
            msg = f'{self.dataset_name} is not correct.'
            raise ValueError(msg)

        self.ds_inst.run()  # data process:  # 1) pcap2features, 2) get train set and test set 3) update params
        self.dataset_dict = self.ds_inst.dataset_dict  # dataset_dict={'sub_data_name':SingleDataset()}
        pprint(self.dataset_dict, name='DataFactory.dataset_dict', verbose=self.verbose)


class DatasetCICIDS2017:
    def __init__(self, srcIP_lst, params):
        self.srcIP_lst = srcIP_lst
        self.params = params
        self.params['srcIP_lst'] = srcIP_lst
        self.dataset_dict = OrderedDict()
        self.params['dataset_dict'] = self.dataset_dict
        self.verbose = self.params['verbose']

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
                                   single_data_name=sub_data_name, pcap_file=pcap_file, label_file=label_file)
                sd.run()  # pcap2features, update params
                self.dataset_dict[sub_data_name] = sd  # {'sub_dataset_name': single_ds, ...}

        elif self.params['expt_name'] == 'AGMT':  # Friday + Monday data
            for i, srcIP in enumerate(self.srcIP_lst):
                sub_data_name = f'DS-srcIP_{srcIP}'  # DS: dataset

                pcap_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/AGMT-WorkingHours',
                                          file_name=f'srcIP_{srcIP}_AGMT.pcap')
                label_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/AGMT-WorkingHours',
                                           file_name=f'srcIP_{srcIP}_AGMT.csv')
                if self.params['overwrite']:
                    pcap_file_1 = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                                file_name=f'srcIP_{srcIP}.pcap')
                    pcap_file_2 = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Monday-WorkingHours',
                                                file_name=f'srcIP_{srcIP}.pcap')
                    merge_pcaps([pcap_file_1, pcap_file_2], mrg_pcap_path=pcap_file)

                    label_file_1 = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                                 file_name=f'srcIP_{srcIP}.csv')
                    label_file_2 = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Monday-WorkingHours',
                                                 file_name=f'srcIP_{srcIP}.csv')
                    merge_labels([label_file_1, label_file_2], mrg_label_path=label_file)

                # 1) pcap2features 2) features to train and test set
                sd = SingleDataset(srcIP=srcIP, params=self.params,
                                   single_data_name=sub_data_name, pcap_file=pcap_file, label_file=label_file)
                sd.run()  # pcap2features, update params
                self.dataset_dict[sub_data_name] = sd  # {'sub_dataset_name': single_ds, ...}

        elif self.params['expt_name'] == 'MIX':  # combine Friday data
            pcap_file_lst = []
            label_file_lst = []
            for i, srcIP in enumerate(self.srcIP_lst):
                sub_data_name = f'DS-srcIP_{srcIP}'
                pcap_file_i = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                            file_name=f'srcIP_{srcIP}.pcap')
                pcap_file_lst.append(pcap_file_i)
                label_file_i = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/Friday-WorkingHours',
                                             file_name=f'srcIP_{srcIP}.csv')
                label_file_lst.append(label_file_i)

            sub_data_name = 'DS-five_srcIPs'
            mrg_srcIP = 'five_srcIPs'
            pcap_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/MIX-WorkingHours',
                                      file_name=f'srcIP_{mrg_srcIP}.pcap')
            label_file = get_file_path(self.params['ipt_dir'], sub_dir=f'{sub_data_name}/MIX-WorkingHours',
                                       file_name=f'srcIP_{mrg_srcIP}.csv')
            if self.params['overwrite']:
                merge_pcaps(pcap_file_lst, mrg_pcap_path=pcap_file)
                merge_labels(label_file_lst, mrg_label_path=label_file)

            # 1) pcap2features 2) features to train and test set
            sd = SingleDataset(srcIP=mrg_srcIP, params=self.params,
                               single_data_name=sub_data_name, pcap_file=pcap_file, label_file=label_file)
            sd.run()  # pcap2features, update params
            self.dataset_dict[sub_data_name] = sd  # {'sub_dataset_name': single_ds, ...}

        else:
            expt_name = self.params['expt_name']
            msg = f'{expt_name} is not correct.'
            raise ValueError(msg)


class DatasetSMTV:
    def __init__(self, srcIP_lst='', params={}):
        super(DatasetSMTV, self).__init__()
        self.srcIP_lst = srcIP_lst
        self.params = params
        self.params['srcIP_lst'] = srcIP_lst
        self.dataset_dict = OrderedDict()
        self.params['dataset_dict'] = self.dataset_dict
        self.verbose = self.params['verbose']

    def run(self):
        if self.params['expt_name'] == 'INDV':  # only Friday data
            for i, srcIP in enumerate(self.srcIP_lst):
                sub_data_name = f'DS-srcIP_{srcIP}'  # DS: dataset
                if self.params['overwrite']:
                    srcIP, nrml_pcap, anml_pcap = self._get_nrml_anml_smart_tv_data(self.params['ipt_dir'],
                                                                                    overwrite=self.params['overwrite'])
                else:
                    srcIP = 'multi-srcIPs'
                    nrml_pcap = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/src_10.42.0.119_merged_normal.pcap'
                    anml_pcap = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/src_10.42.0.119_merged_anomaly.pcap'
                # 1) pcap2features 2) features to train and test set
                sd = SingleDataset(srcIP=srcIP, params=self.params,
                                   single_data_name=sub_data_name, nrml_pcap=nrml_pcap, anml_pcap=anml_pcap)
                sd.run()  # pcap2features, update params
                self.dataset_dict[sub_data_name] = sd  # {'sub_dataset_name': single_ds, ...}

        elif self.params['expt_name'] == 'AGMT':  # Friday + Monday data
            pass
        elif self.params['expt_name'] == 'MIX':  # combine Friday data
            # ipt_dir = 'input_data/smart-tv-roku-data'
            pass
        else:
            expt_name = self.params['expt_name']
            msg = f'{expt_name} is not correct.'
            raise ValueError(msg)

    def _get_nrml_anml_smart_tv_data(self, ipt_dir, keep_ip='10.42.0.119', overwrite=True):
        pcap_file_lst = []
        nrml_dir = os.path.join(ipt_dir, 'raw_pcap', 'normal')
        srcIP = '10.42.0.1'
        for i, pcap in enumerate(os.listdir(nrml_dir)):
            if not pcap.endswith('.pcap'):
                print(f'i:{i+1}, pcap:{pcap}')
                continue
            pcap_file_lst.append(os.path.join(nrml_dir, pcap))
        sub_data_name = 'DS-srcIP_multi-srcIPs'
        nrml_pcap = get_file_path(ipt_dir, sub_dir=f'{sub_data_name}/normal_anomaly', file_name='normal.pcap')
        merge_pcaps(pcap_file_lst, mrg_pcap_path=nrml_pcap)
        src_nrml_pcap = get_file_path(ipt_dir, sub_dir=f'{sub_data_name}/normal_anomaly',
                                      file_name=f'srcIP_{srcIP}_normal.pcap')
        if overwrite:
            keep_ips_in_pcap(input_file=nrml_pcap, output_file=src_nrml_pcap, kept_ips=[srcIP])

        pcap_file_lst = []
        srcIP = '10.42.0.119'
        anml_dir = os.path.join(ipt_dir, 'raw_pcap', 'anomaly')
        for i, pcap in enumerate(os.listdir(anml_dir)):
            if not pcap.endswith('.pcap'):
                print(f'i:{i+1}, pcap:{pcap}')
                continue
            pcap_file_lst.append(os.path.join(anml_dir, pcap))
        anml_pcap = get_file_path(ipt_dir, sub_dir=f'{sub_data_name}/normal_anomaly', file_name='anomaly.pcap')
        merge_pcaps(pcap_file_lst, mrg_pcap_path=anml_pcap)
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

    def __init__(self, srcIP='', single_data_name='', params={}, **kwargs):
        super(SingleDataset, self).__init__()

        self.kwargs = kwargs
        if len(kwargs) > 0:
            ## Explict set value to variable
            # if 'pcap_file' in kwargs.keys() and 'label_file' in kwargs.keys():
            #     self.pcap_file = kwargs['pcap_file']
            #     self.label_file = kwargs['label_file']
            # if 'nrml_pcap' in kwargs.keys() and 'anml_pcap' in kwargs.keys():
            #     self.nrml_pcap = self.kwargs['nrml_pcap']
            #     self.anml_pcap = self.kwargs['nrml_pcap']
            ## Implict set value to variable
            for i, (key, value) in enumerate(kwargs.items()):
                setattr(self, key, value)
        self.single_data_name = single_data_name
        self.srcIP = srcIP
        self.params = params
        self.num_pkt_thresh = 2
        self.params['num_pkt_thresh'] = self.num_pkt_thresh

    def run(self):

        # 1. pcap2flows
        if self.params['dataset_name'] == 'CICIDS2017':
            # self.pcap_file = self.kwargs['pcap_file']
            # self.label_file = self.kwargs['label_file']
            self.flows, self.labels = self.pcap2flows_CICIDS2017(pcap_file=self.pcap_file, labels_csv=self.label_file)

        elif self.params['dataset_name'] == 'SMTV':
            # self.nrml_pcap = self.kwargs['nrml_pcap']
            # self.anml_pcap = self.kwargs['anml_pcap']
            self.flows, self.labels = self.pcap2flows_SMTV(pcap_file_lst=[self.nrml_pcap, self.anml_pcap])
            sub_data_name = 'DS-srcIP_multi-srcIPs'
            self.pcap_file = os.path.join(self.params['ipt_dir'],
                                          f'{sub_data_name}/{self.srcIP}')  # dir_name for SMTV_dataset
            self.label_file = ''

        elif self.params['dataset_name'].startswith('DEMO'):
            if self.params['dataset_name'] == 'DEMO_CICIDS2017':
                self.pcap_file = self.kwargs['pcap_file']
                self.label_file = self.kwargs['label_file']
                self.flows, self.labels = self.pcap2flows_CICIDS2017(pcap_file=self.pcap_file,
                                                                     labels_csv=self.label_file)
            elif self.params['dataset_name'] == 'DEMO_SMTV':
                self.nrml_pcap = self.kwargs['nrml_pcap']
                self.anml_pcap = self.kwargs['anml_pcap']
                self.flows, self.labels = self.pcap2flows_SMTV(pcap_file_lst=[self.nrml_pcap, self.anml_pcap])
                sub_data_name = 'DS-srcIP_multi-srcIPs'
                self.pcap_file = os.path.join(self.params['ipt_dir'], f'{sub_data_name}/{self.srcIP}')
                self.label_file = ''

        else:
            dataset_name = self.params['dataset_name']
            msg = f'{dataset_name} is not implemented.'
            raise ValueError(msg)

        # 2. flow2features
        # if self.params['subflow_flg']:      # default: False (using flow to get features)
        #     self.flows, self.labels = _parse_subflows_and_label(self.flows, self.labels, self.num_pkt_thresh)
        #     print("Number of FIDs in each subflow: {}".format([len(fids) for fids in list(zip(*self.flows))[0]]))

        self.flows2features(self.flows, self.labels)  # get iat_dict={iat_file, ...}, stat_dict, ...

        # 3. features2dataset
        self.features2dataset()  # update self.iat_dict, self.fft_dict

        self.dataset_dict = OrderedDict()  # # iat_dict, fft_dict, stat_dict, samp_dict
        self.dataset_dict['iat_dict'] = self.iat_dict
        self.dataset_dict['fft_dict'] = self.fft_dict
        self.dataset_dict['stat_dict'] = self.stat_dict
        self.dataset_dict['samp_dict'] = self.samp_dict

    def flows2features(self, flows, labels):
        pcap_file = self.pcap_file  # dir_name for iat_file, stat_file, samp_file
        q_fixed_iat = self.params['q_fixed_iat']

        if self.params['subflow_flg']:
            flow_dir_tmp = 'subflow'
        else:
            flow_dir_tmp = 'flow'
        # 1. 'iat_set'
        feat_set = 'iat_set'
        fids_features = _flows_to_IAT_features(flows)
        fids = list(map(lambda x: x[0], fids_features))
        features = list(map(lambda x: x[1], fids_features))
        print(f'num. of flows: {len(fids)}')
        iat_file = f'{pcap_file}-{flow_dir_tmp}-{feat_set}.dat'  # store IATs which have different dimensions to file
        dump_data(data=(fids, features, labels), output_file=iat_file)
        self.iat_dict = {'feat_set': feat_set, 'feat_file': iat_file,
                         'q_fixed_iat': q_fixed_iat}

        bin_size = int(np.round(np.quantile([len(iat) for iat in features], q=q_fixed_iat)))
        print(f'bin_size: {bin_size} when q_fixed_iat equals {q_fixed_iat}')
        self.iat_dict['bin_size'] = bin_size

        # 2. stat_set:
        feat_set = 'stat_set'
        fids_features = _flows_to_basic_features(flows)
        fids = list(map(lambda x: x[0], fids_features))
        features = list(map(lambda x: x[1], fids_features))
        feat_dim = len(features[0])
        print(f'feat_set: {feat_set}, dimension: {feat_dim}')
        stat_file = f'{pcap_file}-{flow_dir_tmp}-{feat_set}-dim_{feat_dim}.dat'  # store Baseline 1 with fixed size
        dump_data(data=(fids, features, labels), output_file=stat_file)
        self.stat_dict = {'feat_set': 'stat_set', 'feat_file': stat_file}

        # 3. samp_set
        feat_set = 'samp_set'
        sampling_method = self.params['sampling_method']
        # q_sampling_rate = self.params['q_sampling_rate']
        sampling_arr = [(max(times) - min(times)) / bin_size for fid, times, sizes in flows]  # flow_duration/fft_bin
        # print(f'Counter(sampling_arr): {list(Counter(sampling_arr))[:100]}')
        #  [:100] for saving memory. if not, script will fails due to the lack of memory
        # make 0.9 flow_duration /fft bin less than the sampling_rate.

        self.samp_dict = OrderedDict()
        for i, q_sampling_rate in enumerate(list(np.linspace(0.0, 1, 10, endpoint=False))[1:]):  # exclude 0
            sampling_rate = np.quantile(sampling_arr, q=q_sampling_rate)
            print(f'sampling_method: {sampling_method}, q_sampling_rate: {q_sampling_rate}, '
                  f'sampling_rate: {sampling_rate}')
            fids_features = _flows_to_samp_basic_features(flows, sampling_type=sampling_method, sampling=sampling_rate)

            fids = list(map(lambda x: x[0], fids_features))
            features = list(map(lambda x: x[1], fids_features))
            print(f'feat_feat: {feat_set}, with different lengths. sampling_type: {sampling_method}, '
                  f'sampling_rate: {sampling_rate}')
            # store sampled IATs which have different dimensions to file
            samp_file = f'{pcap_file}-{flow_dir_tmp}-{feat_set}-{sampling_method}_{sampling_rate}-q_sampling_rate_{q_sampling_rate}.dat'
            dump_data(data=(fids, features, labels), output_file=samp_file)
            self.samp_dict_i = {'feat_set': feat_set, 'feat_file': samp_file, 'sampling_rate': sampling_rate,
                                'q_fixed_iat': q_fixed_iat, 'bin_size': bin_size,
                                'q_sampling_rate': q_sampling_rate}

            self.samp_dict[q_sampling_rate] = self.samp_dict_i

    def features2dataset(self):
        for i, value_dict in enumerate([self.iat_dict, self.stat_dict]):
            pprint(value_dict, name='value_dict')
            feat_set = value_dict['feat_set']
            feat_file = value_dict['feat_file']
            self.fids, self.features, self.labels = self.load_pickled_data(input_file=feat_file)
            if feat_set == 'iat_set':
                # 1. IAT_fixed data
                q_fixed_iat = self.iat_dict['q_fixed_iat']
                bin_size = self.iat_dict['bin_size']
                fixed_iat_file = feat_file + f'-{feat_set}-q_fixed_iat_{q_fixed_iat}-dim_{bin_size}.dat'
                fixed_iat_features = _fix_data(self.features, bin_size)
                dump_data((self.fids, fixed_iat_features, self.labels), output_file=fixed_iat_file)
                self.iat_dict['fixed_feat_file'] = fixed_iat_file
                x_train, y_train, x_test, y_test = self.split_train_test(features=fixed_iat_features,
                                                                         labels=self.labels)
                self.iat_dict['data'] = (x_train, y_train, x_test, y_test)

                # 2. fft_fixed data
                # save the fixed FFT with fft_bins
                fft_part = 'real'
                feat_set = 'fft_set'
                self.fft_dict = {'feat_set': feat_set, 'fixed_feat_file': '', 'data': '', 'fft_part': fft_part,
                                 'bin_size': bin_size, 'q_fixed_iat': q_fixed_iat}
                if fft_part == 'real+imaginary':
                    fixed_fft_file = feat_file + f'-{feat_set}-q_fixed_iat_{q_fixed_iat}-dim_{bin_size*2}-fft_part_{fft_part}.dat'  # real + imaginary
                else:
                    fixed_fft_file = feat_file + f'-{feat_set}-q_fixed_iat_{q_fixed_iat}-dim_{bin_size}-fft_part_{fft_part}.dat'  # real

                fixed_fft_features = _get_fft_data(self.features, fft_bin=bin_size, fft_part=fft_part)
                dump_data((self.fids, fixed_fft_features, self.labels), output_file=fixed_fft_file)
                self.fft_dict['fixed_feat_file'] = fixed_fft_file
                x_train, y_train, x_test, y_test = self.split_train_test(features=fixed_fft_features,
                                                                         labels=self.labels)
                self.fft_dict['data'] = (x_train, y_train, x_test, y_test)

            elif feat_set == 'stat_set':
                # 3. stat_set
                x_train, y_train, x_test, y_test = self.split_train_test(features=self.features, labels=self.labels)
                self.stat_dict['data'] = (x_train, y_train, x_test, y_test)

        # 4. sampling_fixed data
        for i, (q_sampling_rate, samp_dict_i) in enumerate(self.samp_dict.items()):
            feat_set = samp_dict_i['feat_set']
            feat_file = samp_dict_i['feat_file']
            self.fids, self.features, self.labels = self.load_pickled_data(input_file=feat_file)

            fixed_samp_file = feat_file + f'-{feat_set}-q_fixed_iat_{q_fixed_iat}-dim_{bin_size}.dat'
            fixed_samp_features = _fix_data(self.features, bin_size)
            dump_data((self.fids, fixed_samp_features, self.labels), output_file=fixed_samp_file)
            self.samp_dict[q_sampling_rate]['fixed_feat_file'] = fixed_samp_file
            x_train, y_train, x_test, y_test = self.split_train_test(features=fixed_samp_features,
                                                                     labels=self.labels)
            self.samp_dict[q_sampling_rate]['data'] = (x_train, y_train, x_test, y_test)

        pprint(self.iat_dict, name='iat_dict')
        pprint(self.fft_dict, name='fft_dict')

    def pcap2flows_CICIDS2017(self, pcap_file, labels_csv):
        # get all flows which at least has more than 2 packets
        if self.params['subflow_flg']:
            flows = _load_pcap_to_subflows(pcap_file, num_pkt_thresh=self.num_pkt_thresh,
                                           interval=self.params['subflow_interval'])
            # print("Number of FIDs in each subflow: {}".format([len(fids) for fids in list(zip(*flows))[0]]))
        else:
            flows = _load_pcap_to_flows(pcap_file,
                                        self.num_pkt_thresh)  # get all flows which at least has more than 2 packets
        print(f'num. of flows: {len(flows)}')
        labels = _load_labels_and_label_flows(labels_csv, features=[(fid, _) for fid, _, _ in flows])

        flows, labels = random_select_flows(flows, labels, experiment=self.params['expt_name'])
        # labels = _load_labels_and_label_flows(labels_csv, features)
        print(f'num. of labels: {len(labels)}')
        # # fids, features = list(*zip(features))

        return flows, labels

    def pcap2flows_SMTV(self, pcap_file_lst):
        flows = []
        labels = []
        for i, pcap_file in enumerate(pcap_file_lst):
            # get all flows which at least has more than 2 packets
            # flows_i = _load_pcap_to_flows(pcap_file, self.num_pkt_thresh)
            if self.params['subflow_flg']:
                flows_i = _load_pcap_to_subflows(pcap_file, num_pkt_thresh=self.num_pkt_thresh,
                                                 interval=self.params['subflow_interval'])
                # print("Number of FIDs in each subflow: {}".format([len(fids) for fids in list(zip(*flows))[0]]))
            else:
                flows_i = _load_pcap_to_flows(pcap_file,
                                              self.num_pkt_thresh)  # get all flows which at least has more than 2 packets

            flows.extend(flows_i)
            print(f'num. of flows_i: {len(flows_i)}')
            if 'normal.pcap' in pcap_file:
                labels_i = ['Normal'] * len(flows_i)
            elif 'anomaly.pcap' in pcap_file:
                labels_i = ['Anomaly'] * len(flows_i)
            else:
                labels_i = ['None'] * len(flows_i)
            labels.extend(labels_i)
        print(f'num. of flows: {len(flows)}')
        print(f'num. of labels: {len(labels)}')

        flows, labels = random_select_flows(flows, labels, experiment=self.params['expt_name'])
        print(f'num. of labels: {len(labels)}')

        return flows, labels


def _fix_data(features, fft_bin):
    fixed_features = []
    for feat in features:
        feat = list(feat)
        if len(feat) > fft_bin:
            feat = feat[:fft_bin]
        else:
            feat += [0] * (fft_bin - len(feat))

        fixed_features.append(np.asarray(feat, dtype=float))

    return fixed_features


def _get_fft_data(features, fft_bin='', fft_part='real'):
    # calculate discrete FFTs
    if fft_part == 'real':  # default
        fft_features = [np.real(np.fft.fft(IATs, n=fft_bin)) for IATs in features]
    elif fft_part == 'real+imaginary':
        fft_features = []
        for i, IATs in enumerate(features):
            complex_v = np.fft.fft(IATs, fft_bin)
            if i == 0:
                print(f'dimension of the real part: {len(np.real(complex_v))}, '
                      f'dimension of the imaginary part: {len(np.imag(complex_v))}')
            v = np.concatenate([np.real(complex_v), np.imag(complex_v)], axis=np.newaxis)
            fft_features.append(v)
    else:
        print(f'fft_part: {fft_part} is not correct, please modify it and retry')
        return -1

    return fft_features
