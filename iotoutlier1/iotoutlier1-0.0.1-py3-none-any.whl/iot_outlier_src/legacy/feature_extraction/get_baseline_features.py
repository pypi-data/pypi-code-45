# kun.bj@outlook.com
#
# license: xxx
"""Get baseline features: 12 features
    Common statistical features on forward flows (ignore any header informations (such as port, TCP flags, ttl and so on)), which are:
    1) time_interval: the time interval of the flow (separate by TCP.flag.F or TIMEOUT)
    2) num_pkts: The number of packets in this flow
    3) num_bytes : The number of bytes (wirelen: the frame length of Ethernet packet) in this flow
    4) pkts_rate: The number of packets is transferred per second (num_pkts / time_interval)
    5) bytes_rate : The number of bytes is transferred per second  (num_bytes / time_interval)
    6) wirelen: the frame length (mean, standard deviation, first quartile (q1), second quartile (q2, median) third quartile (q3), minimum and maximum)

    Note:
        Only consider forward flows (i.e., clients start TCP connections)
        Inter-arrival time (IAT) do not include in baseline features because we use it as one of ours.
"""

from collections import OrderedDict, Counter

import numpy as np
from scapy.all import *
from scapy.layers.inet import *


def print_time(func):
    def function_wrapper(*args, **kwargs):
        # print("Before calling " + func.__name__)
        start_time = time.time()
        func(*args, kwargs['input_file'], kwargs['file_type'], kwargs['output_file'], kwargs['num_pkts_thres'])
        # print("After calling " + func.__name__)
        end_time = time.time() - start_time
        print(f'It begins at {start_time} and takes {end_time}s')

    return function_wrapper


class Pcap2Features():

    def __init__(self, verbose=False):
        self.TCP_TIMEOUT = 1000 * 600  # 600 seconds
        self.UDP_TIMEOUT = 1000 * 600  # 600 seconds

    def pcap2features(self, input_file='', file_type='normal', output_file='', num_pkts_thres=2):
        """ extract flows from pcap file

        Parameters:

        input_file: pcap_file
        file_type: normal or anomaly
        output_file: save results to output_file
        num_pkts_thres: each sub_flow must has more than max(2, num_pkts_thres) packets

        Returns
        -------
            flows_lst: (five-tuple, value=(raw features))
            The same TCP flow will be separate into multi-subflows accroding to the TIME_OUT or Flags (flow restarts),
            so it cannot be stored in dictionary (which requires key must be unique).

        """
        start_time = time.time()

        if file_type == 'normal':
            label = 0
        else:
            label = 1

        self.num_pkts_thres = num_pkts_thres
        cmd = f'tshark -r "{input_file}" | wc -l'
        print(cmd)
        totals = int(subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8'))
        print(f'total numbers of packets is {int(totals)}')

        if output_file == '':
            output_file = input_file + '_features_labels.txt'
        with open(output_file, 'w') as out_hdl:

            active_flows = OrderedDict()  # key=flow_id, value = all_features
            drop_flows = OrderedDict()  # flows donot meet some conditions.
            with PcapReader(input_file) as pr:
                for i, pkt in enumerate(pr):  # iterator, please use it to process large file, such as more than 4 GB
                    if (i + 1) % 10000 == 0:
                        percent = '{:.2f}'.format((i + 1) / totals * 100)
                        print(f'handle {i+1}/{totals} ({percent}%) packets')
                    if (IP in pkt) and (TCP in pkt or UDP in pkt):  # not handle IPv6
                        # handle TCP packets
                        if TCP in pkt:
                            # parse 5-tuple flow ID
                            sport = pkt[TCP].sport
                            dport = pkt[TCP].dport
                            prtl = pkt[IP].proto
                            fid = (pkt[IP].src, pkt[IP].dst, sport, dport, prtl)
                            if fid not in active_flows.keys():
                                active_flows[fid] = {'single': [prtl, sport, dport],  # maybe need to add TCP flags
                                                     'multi': [(pkt.time, len(pkt), len(pkt[IP].payload), pkt.ttl)],
                                                     'tcp_flgs': [self._get_tcp_flags(tcp_pkt=pkt[TCP])]
                                                     }
                            else:
                                # if this packet is a FIN, add it and close the active flow
                                if pkt[TCP].flags.F:
                                    active_flows[fid]['multi'].append(
                                        (pkt.time, len(pkt), len(pkt[IP].payload), pkt.ttl))
                                    if len(active_flows[fid]['multi']) >= max(2, self.num_pkts_thres):
                                        features, features_str = self._single_flow2features(active_flows[fid])
                                        fid_str = ','.join(list(map(lambda x: str(x), fid)))
                                        out_hdl.write(fid_str + '@' + features_str + '@' + str(label) + '\n')

                                    # self.flows_lst.append((fid, active_flows[fid]))
                                    del active_flows[fid]
                                    # if the TCP timeout has elapsed, close the old active flow and start a new
                                elif pkt.time - active_flows[fid]['multi'][-1][0] > self.TCP_TIMEOUT:
                                    if len(active_flows[fid]['multi']) >= max(2, self.num_pkts_thres):
                                        features, features_str = self._single_flow2features(active_flows[fid])
                                        fid_str = ','.join(list(map(lambda x: str(x), fid)))
                                        out_hdl.write(fid_str + '@' + features_str + '@' + str(label) + '\n')
                                    # self.flows_lst.append((fid, active_flows[fid]))
                                    del active_flows[fid]
                                    active_flows[fid] = {'single': [prtl, sport, dport],  # maybe need to add TCP flags
                                                         'multi': [(pkt.time, len(pkt), len(pkt[IP].payload), pkt.ttl)],
                                                         'tcp_flgs': [self._get_tcp_flags(tcp_pkt=pkt[TCP])]}
                                    # otherwise, add to existing flow
                                else:
                                    active_flows[fid]['multi'].append(
                                        (pkt.time, len(pkt), len(pkt[IP].payload), pkt.ttl))
                                    active_flows[fid]['tcp_flgs'].append(self._get_tcp_flags(tcp_pkt=pkt[TCP]))

                        # handle UDP packets
                        elif UDP in pkt:
                            # parse 5-tuple flow ID
                            sport = pkt[UDP].sport
                            dport = pkt[UDP].dport
                            prtl = pkt[IP].proto

                            fid = (pkt[IP].src, pkt[IP].dst, sport, dport, prtl)
                            if fid not in active_flows.keys():
                                active_flows[fid] = {'single': [prtl, sport, dport],  # maybe need to add TCP flags
                                                     'multi': [(pkt.time, len(pkt), len(pkt[IP].payload), pkt.ttl)],
                                                     'tcp_flgs': [self._get_tcp_flags(tcp_pkt=pkt[UDP])]}
                            else:
                                # if the UDP timeout has elapsed, close the old active flow and start a new one
                                if pkt.time - active_flows[fid]['multi'][-1][0] > self.UDP_TIMEOUT:
                                    if len(active_flows[fid]['multi']) >= max(2, self.num_pkts_thres):
                                        features, features_str = self._single_flow2features(active_flows[fid])
                                        fid_str = ','.join(list(map(lambda x: str(x), fid)))
                                        out_hdl.write(fid_str + '@' + features_str + '@' + str(label) + '\n')
                                    # self.flows_lst.append((fid, active_flows[fid]))
                                    del active_flows[fid]
                                    active_flows[fid] = {'single': [prtl, sport, dport],
                                                         # maybe need to add TCP flags, len(pkt) is len(frame)
                                                         'multi': [(pkt.time, len(pkt), len(pkt[IP].payload), pkt.ttl)],
                                                         'tcp_flgs': [self._get_tcp_flags(tcp_pkt=pkt[UDP])]}
                                    # otherwise, add to existing flow
                                else:
                                    active_flows[fid]['multi'].append(
                                        (pkt.time, len(pkt), len(pkt[IP].payload), pkt.ttl))
                                    active_flows[fid]['tcp_flgs'].append(self._get_tcp_flags(tcp_pkt=pkt[UDP]))
                        else:
                            print(f'pkt:{pkt.name, pkt.payload().name}')
                            # print('not TCP or UDP packets.')
                            pass

                # handle the remained active flow in active_flows_dict
                for i, fid in enumerate(active_flows.keys()):
                    if len(active_flows[fid]['multi']) >= max(2, self.num_pkts_thres):
                        # print(f'i:{i}, {active_flows[fid]}')
                        features, features_str = self._single_flow2features(active_flows[fid])
                        fid_str = ','.join(list(map(lambda x: str(x), fid)))
                        out_hdl.write(fid_str + '@' + features_str + '@' + str(label) + '\n')
                    # self.flows_lst.append((fid, active_flows[fid]))

        end_time = time.time() - start_time
        print(f'It begins at {start_time} and takes {end_time}s')

        return output_file

    def _single_flow2features(self, single_flow_dict):
        """ get features of each flow,  # flow[fid]= {'single': [], 'multi':[], 'tcp_flgs':[]}

        Parameters
        ----------
        single_flow_dict

        Returns
        -------
        features: all features calculated from the flow
        features_str: ','.join(features)
        """

        value = single_flow_dict  # {'single': [], 'multi':[], 'tcp_flgs':[]}
        multi_values = list(
            zip(*sorted(value['multi'], key=lambda x: x[0])))  # sort value by pkt.time, and split tuple
        features = []
        for j, v in enumerate(multi_values):
            if j == 0:
                # convert Unix timestamp arrival times into interpacket intervals
                sub_duration = v[-1] - v[0]  # sub-duration
                features.extend([sub_duration])
                v = np.diff(v)  # get interarrival time
            elif j == 1:
                num_pkts = len(v)
                num_bytes = sum(v)  # all bytes in sub_duration  sum(len(pkt))
                if sub_duration == 0:
                    pkts_rate = 0.0
                    bytes_rate = 0.0
                else:
                    pkts_rate = num_pkts / sub_duration  # it will be very larger due to the very small sub_duration
                    bytes_rate = num_bytes / sub_duration
                # num_bytes = sum(len(pkts))  # actually it can be obtained by num_pkts* average(len(pkts)), which can be seen in _get_statistical_info(v)
                features.extend([num_pkts, pkts_rate, num_bytes, bytes_rate])
                v = v[1:]
            else:
                v = v[1:]  # ignore the first value for other features
            features.extend(self._get_statistical_info(v))

        multi_values = np.sum(np.array(value['tcp_flgs'], dtype=int), axis=0)  # add by rows
        all_features = list(map(lambda x: str(x), value['single'] + features + list(multi_values)))

        return np.array(all_features, dtype=float), ','.join(all_features)

    def _get_tcp_flags(self, tcp_pkt):
        """
        Note: maybe multi-flags are true in the same packet

        Parameters
        ----------
        pkt: tcp or udp packet

        Returns
        -------
            CWR: the CWR bit set in the TCP header (0 for UDP).
            ECE: the ECE bit set in the TCP header (0 for UDP).
            URG: the URG bit set in the TCP header (0 for UDP).
            ACK: the ACK bit set in the TCP header (0 for UDP).
            PSH: the PSH bit set in the TCP header (0 for UDP).
            RST: the RST bit set in the TCP header (0 for UDP).
            SYN: the SYN bit set in the TCP header (0 for UDP).
            FIN: the FIN bit set in the TCP header (0 for UDP).
        """
        if tcp_pkt.name == 'TCP':
            return [tcp_pkt.flags.C, tcp_pkt.flags.E, tcp_pkt.flags.U, tcp_pkt.flags.A, tcp_pkt.flags.P,
                    tcp_pkt.flags.R, tcp_pkt.flags.S, tcp_pkt.flags.F]  # true or false
        else:
            return [0, 0, 0, 0, 0, 0, 0, 0]

    def _get_statistical_info(self, data):
        """

        Parameters
        ----------
        data

        Returns
        -------
            a list includes mean, median, std, q1, q2, q3, min, and max.

        """
        q1, q2, q3 = np.quantile(data, q=[0.25, 0.5, 0.75])  # q should be [0,1] and q2 is np.median(data)
        return [np.mean(data), np.std(data), q1, q2, q3, np.min(data), np.max(data)]

    def load_data(self, input_file=''):
        """ load save data

        Parameters
        ----------
        input_file

        Returns
        -------

        """

        fids = []
        features = []
        labels = []
        with open(input_file, 'r') as in_hdl:
            line = in_hdl.readline()
            while line:
                arr = line.split('@')
                fids.append(arr[0])
                features.append(arr[1].split(','))
                labels.append(int(arr[2]))

                line = in_hdl.readline()

        features = np.array(features, dtype=float)
        return fids, features, labels


def stat_data(data=None):
    #
    # import inspect
    # a= inspect.signature(stat_data)

    import pandas as pd
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 100)

    columns = ['col_' + str(i) for i in range(data.shape[1])]
    dataset = pd.DataFrame(data=data, index=range(data.shape[0]), columns=columns)
    print(f'data.shape: {data.shape}')
    # for 1-d arrary, it return std (NaN) because  n-1 will be 0 (std = 1/(n-1) * sum((x-u)^2))
    print(dataset.describe())


def main():
    '''Main function performs all data loading, parsing, and saving'''
    # parse arguments
    if len(sys.argv) < 5:
        sys.exit("Usage: python3 {} [pcap_file] [file_type] "
                 "[num pkt thresh] [output_file]".format(sys.argv[0]))
    pcap_file, file_typew = sys.argv[1], sys.argv[2]
    num_pkts_thres = int(sys.argv[3])
    output_file = sys.argv[4]

    # process data
    inst = Pcap2Features()
    output_file = inst.pcap2features(input_file=pcap_file, file_type='normal', output_file=output_file,
                                     num_pkts_thres=num_pkts_thres)

    # output_file = '../../../../Downloads/Monday-WorkingHours_1000000pkts_00000_20170703075558.pcap_features_labels.txt'
    print(f'output: {output_file}')
    fids, features, labels = inst.load_data(input_file=output_file)

    print(f'features: {features.shape}, labels: {Counter(labels)}')
    stat_data(features)


if __name__ == "__main__":
    main()
