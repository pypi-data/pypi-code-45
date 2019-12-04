""" Preprocess pcap
    Only keep given srcIPs' traffic, remove other traffic from a given pcap (too large)

    Split pcap:
        editcap -A “2017-07-07 9:00” -B ”2017-07-07 12:00” Friday-WorkingHours.pcap Friday-WorkingHours_09_00-12_00.pcap

    Using tshark to filter packets
        : tshark -r {input_file} -w {output_file} ip.src=={srcIP}



    For example,
     > tshark -r Friday-WorkingHours.pcap -w Friday-WorkingHours@5_Bots_SrcIPs-20170707-09_00-12_00.pcap
                                  ip.src==192.168.10.5 or ip.src==192.168.10.8 or ip.src==192.168.10.9
                                  or ip.src==192.168.10.14 or ip.src==192.168.10.15

     > tshark -r Monday-WorkingHours.pcap -w Monday-WorkingHours@5_SrcIPs-Normal.pcap
                                  "ip.src==192.168.10.5 or ip.src==192.168.10.8 or ip.src==192.168.10.9
                                  or ip.src==192.168.10.14 or ip.src==192.168.10.15"


"""
# kun.bj@outlook.com
#
# License: xxx
import datetime
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # add project path to sys path.
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(f'sys.path: {sys.path}')
print(f'__file__: {__file__}')

import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict, Counter

from data_process.pcap2features_sampling import _load_pcap_to_subflows, _load_pcap_to_flows, \
    _load_labels_and_label_flows

from utils.tool import check_n_generate_path, execute_time, pprint, stat_data


class PCAP():

    def __init__(self, pcap_file='', subflow_flg=False, num_pkt_thresh=2, interval=0.1, overwrite=True, verbose=True, **kwargs):
        self.pcap_file = pcap_file
        self.subflow_flg = subflow_flg
        self.num_pkt_thresh= num_pkt_thresh
        self.interval = interval
        self.overwrite = overwrite
        self.verbose = verbose

        if len(kwargs) > 0:
            for i, (key, value) in enumerate(kwargs.items()):
                setattr(self, key, value)

    def filter_ip(self, pcap_file, kept_ips=[], output_file=''):

        if output_file == '':
            output_file = os.path.splitext(pcap_file)[0] + 'filtered_ips.pcap'  # Split a path in root and extension.
        # only keep srcIPs' traffic
        srcIP_str = " or ".join([f'ip.src!={srcIP}' for srcIP in kept_ips])
        cmd = f"tshark -r {pcap_file} -w {output_file} {srcIP_str}"

        print(f'{cmd}')
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        except Exception as e:
            print(f'{e}, {result}')
            return -1

        return output_file

    def keep_ip(self, pcap_file,kept_ips=[], output_file = ''):

        if output_file =='':
            output_file = os.path.splitext(pcap_file)[0]+'kept_ips.pcap'  #  Split a path in root and extension.
        # only keep srcIPs' traffic
        srcIP_str = " or ".join([f'ip.src=={srcIP}' for srcIP in kept_ips])
        cmd = f"tshark -r {pcap_file} -w {output_file} {srcIP_str}"

        print(f'{cmd}')
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        except Exception as e:
            print(f'{e}, {result}')
            return -1

        return output_file

    def merge_pcaps(self, pcap_file_lst=[], output_file='merged.pcap'):
        num_pcap = len(pcap_file_lst)
        if num_pcap == 0:
            msg=f'{len(pcaps)} pcaps need to be merged.'
            raise ValueError(msg)
        else:

            if os.path.exists(output_file):
                if self.overwrite:  os.remove(output_file)
            if not os.path.exists(os.path.dirname(output_file)):
                os.makedirs(os.path.dirname(output_file))
            cmd = f"mergecap -w {output_file} " + ' '.join(pcap_file_lst)
            print(f'{cmd}')
            try:
                result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
            except Exception as e:
                print(f'{e}, {result}')
                return -1
        return output_file


    def split_pcap(self):
        pass

    def change_format(self): # change pcap format
        pass

    def pcap2flows(self):
        if self.subflow_flg:
            self.flows = _load_pcap_to_subflows(self.pcap_file, num_pkt_thresh=self.num_pkt_thresh, interval=self.interval)
        else:
            self.flows = _load_pcap_to_flows(self.pcap_file, self.num_pkt_thresh)  # get all flows which at least has more than 2 packets
        if self.verbose:
            print(f'num. of flows: {len(self.flows)}')

        return self.flows

    def stats_flows(self, flows=''):
        # fids, features = list(*zip(features))
        self.fids = list(map(lambda x: x[0], flows))
        self.features = list(map(lambda x: (x[1], x[2]), flows))    # times, pkts

        self.flows_durations=[float(pkt_times[-1])-float(pkt_times[0]) for pkt_times, pkt_sizes in self.features]
        self.num_pkts = sum([len(pkt_sizes) for pkt_times, pkt_sizes in self.features])

        if self.verbose:
            stat_data(np.asarray(self.flows_durations).reshape(-1, 1), name='flows_durations')
            print(f'{self.num_pkts} TCP and UDP packets in the {self.pcap_file}')


    def read_labels(self):
        self.labels=[]
        if hasattr(self, 'label_file'):
            with open(self.label_file, 'r') as f:
                line = f.readline()
                while line:
                    # Todo
                    line = f.readline()


    def label_flows(self, flows='', label_file=''):
        time_windows = label_file

        def time_in_time_window(pkt_times, time_window):  # judge if pkt_times in time_window)
            start_time, end_time = time_window
            if np.min(pkt_times) > str2time(end_time) or np.max(pkt_times) < str2time(start_time):
                return False
            else:
                return True

        self.labels =[]
        for i, (fid, pkt_times, pkt_sizes) in enumerate(flows):
            in_time_flg = False
            for j, time_window in enumerate(time_windows):
                if time_in_time_window(pkt_times, time_window):
                    in_time_flg= True
                    break
            if  in_time_flg:
                label_i ='ANOMALY'
            else:
                label_i ='NORMAL'
            self.labels.append(label_i)


        return self.labels









    def plot_hist(self, data='', bins=50, title='', rescale_flg=False):

        plt.subplot()  # plt.subplot(131)
        quant = 0.9
        data_thres = np.quantile(data, q=quant)
        data_thres =f'{data_thres:.4f}'
        print(f'data_thres: {data_thres} when quantile = {quant}')
        print(f'Counter(data): {Counter(data)}')

        if rescale_flg:
            data = [value for value in data if value < 1]
            bins = 30

        plt.hist(data, bins=bins)  # arguments are passed to np.histogram

        # hist, bin_edges = np.histogram(data, bins=bins)
        # print(f'hist:{hist},\nbin_edges:{bin_edges}')
        # max_idx = np.argmax(hist)
        # if max_idx - 1 >= 0:
        #     max_range = f'[{int(bin_edges[max_idx-1])}, {int(bin_edges[max_idx])}]'
        # else:
        #     max_range = f'[0, {int(bin_edges[max_idx])}]'
        # min_idx = np.argmin(hist)
        # if min_idx - 1 >= 0:
        #     min_range = f'[{int(bin_edges[min_idx-1])}, {int(bin_edges[min_idx])}]'
        # else:
        #     min_range = f'[0, {int(bin_edges[min_idx])}]'
        #
        # # title = f'srcIP:{srcIP},\nmax:{max(hist)} in {max_range},' \
        # #         f'\nmin:{min(hist)} in {min_range}'
        min_data = f'{min(data):.4f}'
        max_data = f'{max(data):.4f}'
        title += f'\nmin:{min_data}, max:{max_data}, duration:{data_thres}, when q={quant}'
        plt.title(f"{title}")
        plt.ylabel('Counts')
        plt.xlabel('duration of flow')
        plt.show()


def float2date(float_time):
    date_str = datetime.datetime.fromtimestamp(float_time).strftime('%Y-%m-%d %H:%M:%S')
    return date_str

def str2time(str_time):
    float_time=time.mktime(time.strptime(str_time, '%Y-%m-%d %H:%M:%S'))
    return float_time

def keep_ips_in_pcap(input_file='pcap_file', output_file='', kept_ips=[], verbose=True):
    """ only keep the given srcIP or srcIPs' traffic

    :param input_file: input_pcap_file
    :param output_file: pcap file only contains kept_ips' traffic
    :param kept_ips: ips list
    :return:
    """
    if verbose:
        funcparams_dict = {'input_file': input_file, 'output_file': output_file, 'kept_ips': kept_ips,
                           'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=keep_ips_in_pcap.__name__)

    if len(kept_ips) == 0:
        print(f'kept_ips is {kept_ips}, please check and retry')
        return -1
    check_n_generate_path(file_path=output_file, overwrite=True)

    if len(kept_ips) == 1:  # only keep srcIP's traffic
        srcIP = kept_ips[0]
        cmd = f"tshark -r {input_file} -w {output_file} ip.src=={srcIP}"
    else:  # only keep srcIPs' traffic
        srcIP_str = " or ".join([f'ip.src=={srcIP}' for srcIP in kept_ips])
        cmd = f"tshark -r {input_file} -w {output_file} {srcIP_str}"

    print(f'{cmd}')
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
    except Exception as e:
        print(f'{e}, {result}')
        return -1

    return output_file


# No need to do this part, in pcap2features.py, it will read label_csv with all columns.
# def remove_redundant_flows(input_file='labels_csv', output_file='', verbose=True):
#     """ only keep the given srcIP or srcIPs, and reduce file size
#
#     :param input_file: labels_csv
#     :param output_file: five_tuple + labels
#     :return:
#     """
#     if verbose:
#         funcparams_dict = {'input_file': input_file, 'output_file': output_file,
#                            'verbose': verbose}
#         pprint(OrderedDict(funcparams_dict), name=remove_redundant_flows.__name__)
#
#     assert os.path.exists(input_file)
#     assert output_file == '', f'output_file is {output_file}, please check and retry'
#     check_n_generate_path(file_path=output_file, overwrite=True)
#
#     df = pd.read_csv(input_file)
#     cols_name = list(df.columns)  # 'Source IP'
#     five_tuple_labels = [cols_name[2], cols_name[3], cols_name[4], cols_name[5], cols_name[6],
#                          cols_name[-1]]  # five_tuple, labels
#     print(f'five_tuple_labels:{five_tuple_labels}')
#
#     df = df[five_tuple_labels]
#     print(f'before removing redundant five tuples: {len(df)}')
#     # dropping duplicate values
#     df.drop_duplicates(keep=False, inplace=True)
#     print(f'after removing redundant five tuples: {len(df)}')
#
#     df.to_csv(output_file)
#
#     return output_file


def keep_ips_in_label(input_file='labels_csv', output_file='', kept_ips=[], verbose=True):
    """ only keep the given srcIP or srcIPs

    :param input_file: labels_csv
    :param output_file:
    :param kept_ips: ips list
    :return:
    """
    if verbose:
        funcparams_dict = {'input_file': input_file, 'output_file': output_file, 'kept_ips': kept_ips,
                           'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=keep_ips_in_label.__name__)

    assert len(kept_ips) != 0, f'kept_ips is {kept_ips}'  # assert condition, if condition is false, arise error

    check_n_generate_path(output_file, overwrite=True)

    df = pd.read_csv(input_file)
    name = list(df.columns)[1]  # 'Source IP'
    print(f'name: {name}')
    # index_names = dfObj[(dfObj['Age'] >= 30) & (dfObj['Age'] <= 40)].index
    # dfObj.drop(index_names, inplace=True)
    if len(kept_ips) == 1:
        srcIP = kept_ips[0]
        index_names = df[df[name] != srcIP].index
    else:
        # todo
        # indexNames = df[df[name] != srcIP or ].index
        print('not implement')

    df.drop(index_names, inplace=True)  # remove index
    df.to_csv(output_file)

    return output_file

#
# @execute_time
# def main_preprocess_pcap(dataset_name='CICIDS2017', input_dir='input_data', overwrite=False):
#     if dataset_name == 'CICIDS2017':
#         srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
#
#         if overwrite:
#             pcaps_labels_lst = [('Monday-WorkingHours.pcap', 'Monday-WorkingHours.pcap_ISCX.csv'),
#                                 ('Friday-WorkingHours-20170707-09_00-12_00.pcap',
#                                  'Friday-WorkingHours-Morning.pcap_ISCX.csv')]
#             preprocess_flg = False
#             if preprocess_flg:
#                 # To reduce process time, only keep 5 srcIPs from the given big pcap by tshark first.
#                 #  > tshark -r pcap_file -w output_file srcIP == or srcIP == ...
#                 pcap_file = os.path.join(input_dir, 'Monday-WorkingHours.pcap')
#                 pcapout_file = os.path.join(input_dir, 'Monday-WorkingHours@5_SrcIPs-Normal.pcap')
#                 mondaypcap_file = keep_ips_in_pcap(input_file=pcap_file, output_file=pcapout_file, kept_ips=srcIP_lst)
#
#                 pcap_file = os.path.join(input_dir, 'Friday-WorkingHours-20170707-09_00-12_00.pcap')
#                 pcapout_file = os.path.join(input_dir, 'Friday-WorkingHours@5_Bots_SrcIPs-20170707-09_00-12_00.pcap')
#                 fridaypcap_file = keep_ips_in_pcap(input_file=pcap_file, output_file=pcapout_file, kept_ips=srcIP_lst)
#
#                 pcaps_labels_lst = [(mondaypcap_file, 'Monday-WorkingHours.pcap_ISCX.csv'),
#                                     (fridaypcap_file, 'Friday-WorkingHours-Morning.pcap_ISCX.csv')]
#         else:
#             pcaps_labels_lst = [('Monday-WorkingHours@5_SrcIPs-Normal.pcap', 'Monday-WorkingHours.pcap_ISCX.csv'),
#                                 ('Friday-WorkingHours@5_Bots_SrcIPs-20170707-09_00-12_00.pcap',
#                                  'Friday-WorkingHours-Morning.pcap_ISCX.csv')]
#
#         for (pcap_file, label_file) in pcaps_labels_lst:
#             pre_dir = pcap_file.split('@')[0]
#             print(f'-------------- process {pre_dir} ------------------------')
#             for idx, srcIP in enumerate(srcIP_lst):
#                 print(f'\nidx: {idx}, srcIP: {srcIP}, input_dir: {input_dir}')
#                 kept_ips = [srcIP]
#                 # 1) keep ips in the given pcap
#                 srcIPpcap_file = os.path.join(input_dir, pcap_file)
#                 pcapout_file = os.path.join(input_dir, f'srcIP_{srcIP}', pre_dir, f'srcIP_{srcIP}.pcap')
#                 keep_ips_in_pcap(input_file=srcIPpcap_file, output_file=pcapout_file,
#                                  kept_ips=kept_ips)  # only keep srcIP's traffic
#
#                 # 2) keep ips in the given label file
#                 srcIPlabel_file = os.path.join(input_dir, label_file)
#                 labelout_file = os.path.join(input_dir, f'srcIP_{srcIP}', pre_dir, f'srcIP_{srcIP}.csv')
#                 keep_ips_in_label(input_file=srcIPlabel_file, output_file=labelout_file, kept_ips=kept_ips)
#
#     elif dataset_name == 'smart-tv-roku-data':
#         if overwrite:
#             srcIP_lst = ['10.42.0.119', '10.42.0.120', '10.42.0.119',
#                          '10.42.0.120', '10.42.0.119', '10.42.0.119',
#                          '10.42.0.120', '10.42.0.120', '10.42.0.119',
#                          '10.42.0.119', '10.42.0.120', '10.42.0.120']  # filter unrelated packets
#             pcap_lst = ['48626-1569697955-normal.pcap', '54065-1569633493-normal.pcap', '36732-1569696202-normal.pcap',
#                         '222279-1569631187-normal.pcap', '71376-1569639462-normal.pcap', '48631-1569699232-normal.pcap',
#                         '258327-1569630531-normal.pcap', '121375-1569631825-normal.pcap',
#                         '16184-1569701783-normal.pcap',
#                         '25082-1569695098-normal.pcap', '13933-1569628870-normal.pcap',
#                         '172665-1569633928-normal.pcap']  # normal
#             pcap_file_lst = []
#             for i, pcap in enumerate(pcap_lst):
#                 pcap_file = os.path.join(input_dir, 'raw_pcap/' + pcap)
#                 print(f'i: {i}, pcap_file: {pcap_file}')
#                 srcIP = srcIP_lst[i]
#                 pcapout_file = os.path.join(input_dir, f'multi-srcIPs/normal_anomaly/srcIP_{srcIP}_{pcap}')
#                 keep_ips_in_pcap(input_file=pcap_file, output_file=pcapout_file, kept_ips=['10.42.0.119'])
#                 pcap_file_lst.append(pcapout_file)
#
#             merged_pcaps = os.path.join(input_dir, f'multi-srcIPs/normal_anomaly/merged_normal.pcap')
#             cmd = f"mergecap -w {merged_pcaps} " + ' '.join(pcap_file_lst)
#             print(f'{cmd}')
#             try:
#                 result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
#             except Exception as e:
#                 print(f'{e}, {result}')
#                 return -1
#
#             srcIP_lst = ['10.42.0.120', '10.42.0.120', '10.42.0.119']  # filter unrelated packets
#             pcap_lst = ['12-1569622891.pcap', '2285-1569623141.pcap', '18502-1569700271.pcap']  # anomaly
#             pcap_file_lst = []
#             for i, pcap in enumerate(pcap_lst):
#                 pcap_file = os.path.join(input_dir, 'raw_pcap/' + pcap)
#                 print(f'i: {i}, pcap_file: {pcap_file}')
#                 srcIP = srcIP_lst[i]
#                 pcapout_file = os.path.join(input_dir, f'multi-srcIPs/normal_anomaly/srcIP_{srcIP}_{pcap}')
#                 keep_ips_in_pcap(input_file=pcap_file, output_file=pcapout_file, kept_ips=['10.42.0.119'])
#                 pcap_file_lst.append(pcapout_file)
#             merged_pcaps = os.path.join(input_dir, f'multi-srcIPs/normal_anomaly/merged_anomaly.pcap')
#             cmd = f"mergecap -w {merged_pcaps} " + ' '.join(pcap_file_lst)
#             print(f'{cmd}')
#             try:
#                 result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
#             except Exception as e:
#                 print(f'{e}, {result}')
#                 return -1
#

if __name__ == '__main__':
    # main_preprocess_pcap(dataset_name='smart-tv-roku-data', overwrite=True)

    duration_flg=False
    if duration_flg:
        pcap_dict = {'BelkinWemoSwitch':'../input_data/Noah_IoT/BelkinWemoSwitch.pcap',
                     'Google_home2':'../input_data/Noah_IoT/Google_home2.pcap',
                    'NestCam_MotionDetection':'../input_data/Noah_IoT/NestCam_MotionDetection.pcap',
                    'SenseSleepMonitor':'../input_data/Noah_IoT/SenseSleepMonitor.pcap'}
        for i, (key, value) in enumerate(pcap_dict.items()):
            pp = PCAP(pcap_file=value, subflow_flg=True)
            pp.pcap2flows()
            pp.stats_flows(flows=pp.flows)
            pp.plot_hist(data=pp.flows_durations, title=key, bins=50)

    label_flg = True
    if label_flg:
        pcap_dict = {'BelkinWemoSwitch': {'pcap_file': '../input_data/Noah_IoT/BelkinWemoSwitch.pcap',
                                          'label_file':[('2016-07-07 14:46:00', '2016-07-07 14:46:08'),
                                                        ('2016-07-07 14:46:10', '2016-07-07 14:46:12')]}
                     }
        for i, (key, value_dict) in enumerate(pcap_dict.items()):
            pcap_file = value_dict['pcap_file']
            label_file = value_dict['label_file']
            pp = PCAP(pcap_file=pcap_file, subflow_flg=True)
            pp.pcap2flows()
            pp.stats_flows(flows=pp.flows)
            pp.label_flows(pp.flows, label_file=label_file)
            print(f'Counter(labels): {Counter(pp.labels)}')
            pp.plot_hist(data=pp.flows_durations, title=key, bins=50)
