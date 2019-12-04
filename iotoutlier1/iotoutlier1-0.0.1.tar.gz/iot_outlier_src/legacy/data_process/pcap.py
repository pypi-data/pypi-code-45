import os
from collections import OrderedDict

import numpy as np

from data_process import keep_ips_in_pcap
from data_process import random_select_flows, _load_labels_and_label_flows, \
    _flows_to_samp_basic_features, _flows_to_basic_features, _flows_to_IAT_features, _load_pcap_to_flows
from utils.tool import get_file_path, merge_pcaps, merge_labels, dump_data


#
# class PcapFactory():
#
#     def __init__(self, srcIP = '', params={}):
#         if params['dataset_name'] in ['CICIDS2017', 'Demo']:
#            flows, labels = self.pcap2flows(self.params['pcap_file'], labels_csv=self.params['label_file'])
#            self.pcap_file = self.params['pcap_file']
#         elif self.params['dataset_name'] == 'SMTV':
#             flows, labels = self.pcap2flows_SMTV(pcap_file_lst=[self.params['nrml_pcap'], self.params['anml_pcap']])
#             # flows, labels = self.pcap2flows(self.params['pcap_file'], labels_csv=self.params['label_file'])
#             pcap_dir = 'multi-srcIPs'
#             self.pcap_file = os.path.join(self.params['ipt_dir'], f'{pcap_dir}/{self.srcIP}')


class Pcap:

    def __init__(self, params='', **kwargs):
        self.params = params
        for i, (key, value) in enumerate(kwargs):
            self.key = value

    def run(self):
        self.result_dict = OrderedDict()  # {(srcIP, pcap, label): {iat_file, baseline1, baseline2}}
        if self.params['dataset_name'] in ['CICIDS2017', 'DEMO']:
            self.flows, self.labels = self.pcap2flows_CICIDS2017(pcap_file=self.pcap_file, labels_csv=self.label_file)
            # self.pcap_file = self.params['pcap_file']
            # self.label_file = self.params['label_file']
        elif self.params['dataset_name'] == 'SMTV':
            self.flows, self.labels = self.pcap2flows_SMTV(pcap_file_lst=[self.nrml_pcap, self.anml_pcap])
            pcap_dir = 'multi-srcIPs'
            # srcIP = self.params['srcIP']
            self.pcap_file = os.path.join(self.params['ipt_dir'], f'{pcap_dir}/{srcIP}')
            self.label_file = ''
            # self.params['pcap_file'] = self.pcap_file
            # self.params['label_file'] = self.label_file
        else:
            dataset_name = self.params['dataset_name']
            msg = f'{dataset_name} is not implemented.'
            raise ValueError(msg)
        self.flows2features(self.flows, self.labels)  # iat_file, stat_file, samp_file, sampling_rate.

    def preprocess_pcap(self):
        if self.params['dataset_name'] == 'Demo':
            ipt_dir = os.path.join(self.params['ipt_dir'], self.params['dataset_name'])
            sub_dir_l2 = ''
            if self.params['expt_name'] == 'indv_data':  # only Friday data
                pass
            elif self.params['expt_name'] == 'augt_data':
                pass
            elif self.params['expt_name'] == 'comb_data':
                pass
            self.params['pcap_file'] = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2=sub_dir_l2,
                                                     file_name=f'srcIP_{self.srcIP}.pcap')
            self.params['label_file'] = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2=sub_dir_l2,
                                                      file_name=f'srcIP_{self.srcIP}.csv')
        elif self.params['dataset_name'] == 'CICIDS2017':
            ipt_dir = self.params['ipt_dir']
            if self.params['expt_name'] == 'indv_data':  # only Friday data
                sub_dir_l2 = 'Friday-WorkingHours'
                self.params['pcap_file'] = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2=sub_dir_l2,
                                                         file_name=f'srcIP_{self.srcIP}.pcap')
                self.params['label_file'] = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2=sub_dir_l2,
                                                          file_name=f'srcIP_{self.srcIP}.csv')
            elif self.params['expt_name'] == 'agmt_data':  # Friday + Monday data
                # sub_dir_l2 = 'Friday-WorkingHours'
                pcap_path = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2='Friday-WorkingHours',
                                          file_name=f'srcIP_{self.srcIP}.pcap')
                pcap_path_2 = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2='Monday-WorkingHours',
                                            file_name=f'srcIP_{self.srcIP}.pcap')
                mrg_pcap_path = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2='More-WorkingHours',
                                              file_name=f'srcIP_{self.srcIP}_more.pcap')

                label_path = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2='Friday-WorkingHours',
                                           file_name=f'srcIP_{self.srcIP}.csv')
                label_path_2 = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2='Monday-WorkingHours',
                                             file_name=f'srcIP_{self.srcIP}.csv')
                mrg_label_path = get_file_path(ipt_dir, f'srcIP_{self.srcIP}', sub_dir_l2='More-WorkingHours',
                                               file_name=f'srcIP_{self.srcIP}_more.csv')
                if self.params['overwrite']:
                    merge_pcaps([pcap_path, pcap_path_2], mrg_pcap_path=mrg_pcap_path)
                    merge_labels([label_path, label_path_2], mrg_label_path=mrg_label_path)

                self.params['pcap_file'] = mrg_pcap_path
                self.params['label_file'] = mrg_label_path

            elif self.params['expt_name'] == 'comb_data':  # combine Friday data
                # src_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
                pcap_file_lst = []
                label_file_lst = []
                srcIP = self.params['srcIP']
                sub_dir_l2 = 'Friday-WorkingHours'
                # for i, srcIP in enumerate(src_lst):
                pcap_path = get_file_path(ipt_dir, f'srcIP_{srcIP}', sub_dir_l2='Friday-WorkingHours',
                                          file_name=f'srcIP_{srcIP}.pcap')
                pcap_file_lst.append(pcap_path)
                label_path = get_file_path(ipt_dir, f'srcIP_{srcIP}', sub_dir_l2='Friday-WorkingHours',
                                           file_name=f'srcIP_{srcIP}.csv')
                label_file_lst.append(label_path)
                mrg_pcap_path = get_file_path(ipt_dir, f'five_srcs', sub_dir_l2='Comb-WorkingHours',
                                              file_name=f'five_srcs.pcap')
                mrg_label_path = get_file_path(ipt_dir, f'five_srcs', sub_dir_l2='Comb-WorkingHours',
                                               file_name=f'five_labels.csv')
                if self.params['overwrite']:
                    merge_pcaps(pcap_file_lst, mrg_pcap_path=mrg_pcap_path)
                    merge_labels(label_file_lst, mrg_label_path=mrg_label_path)
                # pcap_file_lst = [mrg_pcap_path]
                # label_file_lst = [mrg_label_path]
                # src_lst = ['five_srcs']

                self.params['pcap_file'] = mrg_pcap_path
                self.params['label_file'] = mrg_label_path

        elif self.params['dataset_name'] == 'SMTV':  # smart-tv-roku-data
            ipt_dir = 'input_data/smart-tv-roku-data'

            # if self.params['overwrite']:
            #     srcIP, pcap_file, label_file = preprocess_smart_tv_data(ipt_dir=ipt_dir, self.params['overwrite']=False)
            #
            #     src_lst = [srcIP]
            #     pcap_file_lst = [pcap_file]
            #     label_file_lst=[label_file]
            #
            # else:
            #     src_lst = ['multi-srcIPs.pcap']
            #     pcap_file_lst = ['input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/multi-srcIPs.pcap']
            #     label_file_lst = ['input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/multi-srcIPs.csv']

            if self.params['overwrite']:
                srcIP, nrml_pcap, anml_pcap = get_nrml_anml_smart_tv_data(ipt_dir, overwrite=self.params['overwrite'])

            else:
                srcIP = 'multi-srcIPs'
                nrml_pcap = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/src_10.42.0.119_merged_normal.pcap'
                anml_pcap = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/src_10.42.0.119_merged_anomaly.pcap'

            self.params['nrml_pcap'] = nrml_pcap
            self.params['anml_pcap'] = anml_pcap

            # expt = SMTV_Exprmt(expt_name=None, nrml_pcap=nrml_pcap, anml_pcap=anml_pcap,
            #                    srcIP=srcIP,
            #                    ipt_dir=ipt_dir, opt_dir='output_data',
            #                    q_fixed_iat=0.9,
            #                    q_smpl_rate=0.9)  # exprmt_name = 'indv_data', 'agmt_data', 'comb_data'
            # expt.run(detector_lst=['GMM', 'OCSVM', 'KDE'], prop_feat_lst=['IAT', 'FFT'], gridsearch_lst=[True, False])
            # # expt.save()

        else:
            raise ValueError()

    # def pcap2features(self, pcap_file, labels_csv):
    #     flows, labels= self.pcap2flows(pcap_file,labels_csv)
    #     self.flows2features(flows, labels)

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
    nrml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_normal.pcap')
    merge_pcaps(pcap_file_lst, mrg_pcap_path=nrml_pcap)
    # nrml_label = generate_label(nrml_pcap, label='NORMAL')
    src_nrml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly',
                                  file_name=f'src_{srcIP}_merged_normal.pcap')
    if overwrite:
        keep_ips_in_pcap(input_file=nrml_pcap, output_file=src_nrml_pcap, kept_ips=[srcIP])

    # src_lst = [keep_ip] * len(pcap_lst)
    # pcap_file_lst = []
    # for i, (srcIP, pcap_file) in enumerate(zip(src_lst, pcap_lst)):
    #     pcap_file_i = get_file_path(ipt_dir,  'raw_pcap/normal', sub_dir_l2='', file_name=pcap_file)
    #     pcapout_file = os.path.join(ipt_dir, f'multi-srcIPs/normal_anomaly/srcIP_{srcIP}_{pcap_file}')
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
    # for i, (srcIP, pcap_file) in enumerate(zip(src_lst, pcap_lst)):
    #     pcap_file_i = get_file_path(ipt_dir, 'raw_pcap/anomaly', sub_dir_l2='', file_name=pcap_file)
    #     pcapout_file = os.path.join(ipt_dir, f'multi-srcIPs/normal_anomaly/srcIP_{srcIP}_{pcap_file}')
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
    anml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_anomaly.pcap')
    merge_pcaps(pcap_file_lst, mrg_pcap_path=anml_pcap)
    # anml_label = generate_label(anml_pcap, label='ANOMALY')
    src_anml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly',
                                  file_name=f'src_{srcIP}_merged_anomaly.pcap')
    if overwrite:
        keep_ips_in_pcap(input_file=anml_pcap, output_file=src_anml_pcap, kept_ips=[srcIP])

    return 'multi-srcIPs', src_nrml_pcap, src_anml_pcap
