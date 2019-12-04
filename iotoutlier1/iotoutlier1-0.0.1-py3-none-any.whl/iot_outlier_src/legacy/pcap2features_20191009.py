# kun.bj@outlook.com
#
# License: xxx
import pickle
from collections import Counter

import numpy as np
import pandas as pd
from scapy.all import *
# from base import stat_data
# from utils.data_process import stat_data
from scapy.layers.inet import *

TCP_TIMEOUT = 1000 * 600  # 600 seconds
UDP_TIMEOUT = 1000 * 600  # 600 seconds


def parse_dataset(pcap_file, labels_csv, fft_bins='', num_pkt_thresh=2, feat_set=''):
    '''Parses pcap file into FFT features and labels file into string labels

      Arguments:
        pcap_file (string) = path to .pcap file
        labels_csv (string) = path to .csv file in CICIDS format
        num_pkts_thresh (int) = discards flows with fewer packets than max(2, thresh)
        fft_bins (int) = number of FFT bins

      Returns 2-tuple of (list, dict):
        features (list) = [(fid, n-bin FFT of IPIs, n-bin FFT of sizes)]
        labels[(5-tuple flow ID)] -> [label] (e.g. "BENIGN")
    '''
    flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh)
    print(f'num. of flows: {len(flows)}')
    if feat_set == 'IAT':
        features = _flows_to_IAT_features(flows)
    elif feat_set == 'FFT':
        features = _flows_to_fft_features(flows, fft_bins)
    elif feat_set == 'Baseline':
        features = _flows_to_basic_features(flows)
    else:
        print('not implemented.')
        return -1

    labels = _load_labels_2(labels_csv, features)
    print(f'num. of labels: {len(labels)}')
    # fids, features = list(*zip(features))
    fids = list(map(lambda x: x[0], features))
    features = list(map(lambda x: x[1], features))
    print(f'num. of flows: {len(fids)}')

    return fids, features, labels


def _load_pcap_to_flows(pcap_file, num_pkts_thresh):
    '''Reads pcap and divides packets into 5-tuple flows (arrival times and sizes)

       Arguments:
         pcap_file (string) = path to pcap file
         num_pkts_thresh (int) = discards flows with fewer packets than max(2, thresh)

       Returns:
         flows (list) = [(fid, arrival times list, packet sizes list)]
    '''
    # read packets iteratively
    active_flows = defaultdict(list)
    all_flows = []
    for i, pkt in enumerate(PcapReader(pcap_file)):
        if i % 10000 == 0:
            print("Packet {}".format(i))

        # handle TCP packets
        if IP in pkt and TCP in pkt:
            # parse 5-tuple flow ID
            fid = (pkt[IP].src, pkt[IP].dst, pkt[TCP].sport, pkt[TCP].dport, 6)
            # create a new active flow if one doesn't exist
            if not active_flows[fid]:
                active_flows[fid].append((pkt.time, len(pkt)))
            # if this packet is a FIN, add it and close the active flow
            if pkt[TCP].flags.F:
                active_flows[fid].append((pkt.time, len(pkt)))
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
            # if the TCP timeout has elapsed, close the old active flow and start anew
            elif pkt.time - active_flows[fid][-1][0] > TCP_TIMEOUT:
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
                active_flows[fid].append((pkt.time, len(pkt)))
            # otherwise, add to existing flow
            else:
                active_flows[fid].append((pkt.time, len(pkt)))

        # handle UDP packets
        elif IP in pkt and UDP in pkt:
            # parse 5-tuple flow ID
            fid = (pkt[IP].src, pkt[IP].dst, pkt[UDP].sport, pkt[UDP].dport, 17)
            # create a new active flow if one doesn't exist
            if not active_flows[fid]:
                active_flows[fid].append((pkt.time, len(pkt)))
            # if UDP timeout has elapsed, close the old active flow and start anew
            if pkt.time - active_flows[fid][-1][0] > UDP_TIMEOUT:
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
                active_flows[fid].append((pkt.time, len(pkt)))
            # otherwise add to existing flow
            else:
                active_flows[fid].append((pkt.time, len(pkt)))

    # store all active flows
    for fid in active_flows:
        all_flows.append((fid, active_flows[fid]))  # change dict to tuple

    # sort all flows by packet arrival time
    flows = [(fid, *list(zip(*sorted(times_sizes)))) for fid, times_sizes in all_flows if
             len(times_sizes) > max(2, num_pkts_thresh)]
    return flows


def _flows_to_IAT_features(flows):
    '''Converts flows to FFT features

       Arguments:
         flows (list) = representation returned from read_pcap
         fft_bins (int) = number of FFT bins

       Returns:
         features (list) = [(fid, n-bin FFT of IPIs, n-bin FFT of packet sizes)]
    '''
    # convert Unix timestamp arrival times into interpacket intervals
    flows = [(fid, np.diff(times), sizes[1:]) for (fid, times, sizes) in flows]
    # calculate discrete FFTs
    features = [(fid, times) for (fid, times, sizes) in flows]

    return features


def _flows_to_fft_features(flows, fft_bins):
    '''Converts flows to FFT features

       Arguments:
         flows (list) = representation returned from read_pcap
         fft_bins (int) = number of FFT bins

       Returns:
         features (list) = [(fid, n-bin FFT of IPIs, n-bin FFT of packet sizes)]
    '''
    # convert Unix timestamp arrival times into interpacket intervals
    flows = [(fid, np.diff(times), sizes[1:]) for (fid, times, sizes) in flows]
    # calculate discrete FFTs
    features = [(fid, np.real(np.fft.fft(times, n=fft_bins))) for (fid, times, sizes) in flows]
    # features = [(fid, np.absolute(np.fft.fft(times, n=fft_bins))) for (fid, times, sizes) in flows]

    # features=[]
    # for i, (fid, times, sizes) in enumerate(flows):
    #     complex_v = np.fft.fft(times, fft_bins)
    #     if i == 0:
    #         print(f'{len(np.real(complex_v))}, {len(np.imag(complex_v))}')
    #     v= np.concatenate([np.real(complex_v), np.imag(complex_v)], axis=np.newaxis)
    #     features.append((fid, v))
    # # features = [(fid, np.real(np.fft.fft(times, n=fft_bins)), np.imag(np.fft.fft(times, n=fft_bins))) for (fid, times, sizes) in flows]

    return features


def _get_statistical_info(data):
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


def _flows_to_basic_features(flows):
    '''Converts flows to FFT features

       Arguments:
         flows (list) = representation returned from read_pcap
         fft_bins (int) = number of FFT bins

       Returns:
         features (list) = [(fid, n-bin FFT of IPIs, n-bin FFT of packet sizes)]
    '''
    # convert Unix timestamp arrival times into interpacket intervals
    # flows = [(fid, np.diff(times), sizes[1:]) for (fid, times, sizes) in flows]
    flows = [(fid, np.diff(times), sizes) for (fid, times, sizes) in flows]
    # calculate discrete FFTs

    # features = [(fid, (times[-1] - times[0]), _get_statistical_info(sizes)) for (fid, times, sizes) in flows]
    features = []
    for fid, times, sizes in flows:
        sub_duration = times[-1] - times[0]
        num_pkts = len(sizes)
        num_bytes = sum(sizes)  # all bytes in sub_duration  sum(len(pkt))
        if sub_duration == 0:
            pkts_rate = 0.0
            bytes_rate = 0.0
        else:
            pkts_rate = num_pkts / sub_duration  # it will be very larger due to the very small sub_duration
            bytes_rate = num_bytes / sub_duration
        base_feature = [sub_duration, pkts_rate, bytes_rate] + _get_statistical_info(sizes)

        features.append((fid, tuple([float(v) for v in base_feature])))

    return features


#
# def _load_labels(csv_file):
#     '''Load binary labels from CICIDS format CSV
#
#        Arguments:
#          csv_file (string): path to CSV file
#
#        Returns:
#          labels[(5-tuple flow ID)] -> label (string) (e.g. "BENIGN")
#     '''
#     # load CSV with pandas
#     csv = pd.read_csv(csv_file)
#
#     # process each row iteratively
#     labels = {}
#     for i, r in enumerate(csv.index):
#         if i % 10000 == 0:
#             print("Label CSV row {}".format(i))
#
#         row = csv.loc[r]
#         # parse 5-tuple flow ID
#         fid = (row[" Source IP"], row[" Destination IP"], row[" Source Port"],
#                row[" Destination Port"], row[" Protocol"])
#         # ensure all 5-tuple flows have same label
#         if fid in labels:
#             assert (labels[fid] == row[" Label"])
#         # set label of flow ID
#         labels[fid] = row[" Label"]
#     return labels


def _load_labels_2(csv_file, features):
    '''Load binary labels from CICIDS format CSV

       Arguments:
         csv_file (string): path to CSV file

       Returns:
         labels[(5-tuple flow ID)] -> label (string) (e.g. "BENIGN")
    '''
    # load CSV with pandas
    csv = pd.read_csv(csv_file)

    labels = {}
    for i, r in enumerate(csv.index):
        if i % 10000 == 0:
            print("Label CSV row {}".format(i))

        row = csv.loc[r]
        # parse 5-tuple flow ID
        fid = (row[" Source IP"], row[" Destination IP"], row[" Source Port"],
               row[" Destination Port"], row[" Protocol"])
        # ensure all 5-tuple flows have same label
        if fid in labels:
            assert (labels[fid] == row[" Label"])
        # set label of flow ID
        labels[fid] = row[" Label"]

    # process each row iteratively
    new_labels = []
    not_existed_num = 0
    for i, value in enumerate(features):
        fid = value[0]
        if fid in labels.keys():
            new_labels.append(labels[fid])
        else:
            not_existed_num += 1
            new_labels.append('None')  # not existed in labels.csv

    print(f'{not_existed_num} flows do not exist in {labels_file}')
    return new_labels


def main_parse_pcap(input_file, labels_file='', feat_set='IAT', fft_bins='', quant=0.9):
    num_pkt_thresh = 2
    # 1) obtain fids, features, labels
    fids, features, labels = parse_dataset(input_file, labels_csv=labels_file, fft_bins=fft_bins,
                                           num_pkt_thresh=num_pkt_thresh, feat_set=feat_set)

    print(f'fids: {len(fids)}, features: {len(features)}, labels: {len(labels)}')
    print(f'labels: {Counter(labels)}')
    # stat_data(features)

    if feat_set == 'IAT':
        # 2) save (fids, features, labels) to file
        output_file_1 = input_file + f'_{feat_set}.dat'  # save IAT with different dimension
        if os.path.exists(output_file_1):
            os.remove(output_file_1)
        print(f'output_file: {output_file_1}')
        # # save results
        with open(output_file_1, 'wb') as out_hdl:
            pickle.dump((fids, features, labels), out_hdl)

        # 3) obtain fft_bins, and save flows_len_arr to file
        flows_len_arr = [len(value) for value in features]
        fft_bins = int(np.quantile(flows_len_arr, q=quant))
        print(f'choose quantile = {quant} and get fft_bins: {fft_bins}.')
        print(f'len(flows_len_arr): {len(flows_len_arr)}, {sorted(set(flows_len_arr))}, \n{Counter(flows_len_arr)}')
        # stat_data(np.array(flows_len_arr).reshape(-1, 1))

        output_file_2 = input_file + f'_{feat_set}_flows_len.dat'
        if os.path.exists(output_file_2):
            os.remove(output_file_2)
        print(f'output_file: {output_file_2}')
        # # save results
        with open(output_file_2, 'wb') as out_hdl:
            pickle.dump(flows_len_arr, out_hdl)

        # 4) save the fixed IAT with fft_bins
        print(f'feat_set: {feat_set}, dimension: {fft_bins}')
        output_file_3 = input_file + f'_{feat_set}_dimension_{fft_bins}.dat'
        if os.path.exists(output_file_3):
            os.remove(output_file_3)
        print(f'output_file: {output_file_3}')

        features_fixed = []
        for feat in features:
            feat = list(feat)  # (fid, IAT)
            if len(feat) > fft_bins:
                feat = feat[:fft_bins]
            else:
                feat += [0] * (fft_bins - len(feat))

            features_fixed.append(np.asarray(feat, dtype=float))
        # # save results
        with open(output_file_3, 'wb') as out_hdl:
            pickle.dump((fids, features_fixed, labels), out_hdl)

    elif feat_set == 'FFT':
        # 2) save (fids, features, labels) to file
        print(f'feat_set: {feat_set}, dimension: {fft_bins}')
        output_file_1 = input_file + f'_{feat_set}_dimension_{fft_bins}.dat'  # IAT with different dimension
        if os.path.exists(output_file_1):
            os.remove(output_file_1)
        print(f'output_file: {output_file_1}')
        # # save results
        with open(output_file_1, 'wb') as out_hdl:
            pickle.dump((fids, features, labels), out_hdl)
    elif feat_set == 'Baseline':
        # 2) save (fids, features, labels) to file
        dim = len(features[0])
        print(f'feat_set: {feat_set}, dimension: {dim}')
        output_file_1 = input_file + f'_{feat_set}_dimension_{dim}.dat'  # IAT with different dimension
        if os.path.exists(output_file_1):
            os.remove(output_file_1)
        print(f'output_file: {output_file_1}')
        # # save results
        with open(output_file_1, 'wb') as out_hdl:
            pickle.dump((fids, features, labels), out_hdl)

    return fft_bins


if __name__ == '__main__':

    demo = False

    start_time = time.time()
    st = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
    print(f'start at {st}')
    if demo:

        pcap_file = '../data/test.pcap'
        labels_file = '../data/test.csv'

        srcIP = 'all'
        # 1) obtain IAT set
        print(f'obtain IAT set')
        quant = 0.9
        flow_len_thres = main_parse_pcap(input_file=pcap_file, labels_file=labels_file, feat_set='IAT', quant=quant)
        print(f'srcIP: {srcIP}, quant: {quant}, flow_len_thres: {flow_len_thres}')

        # 2) obtain FFT set
        print(f'obtain FFT set')
        main_parse_pcap(input_file=pcap_file, labels_file=labels_file, feat_set='FFT', fft_bins=flow_len_thres)

        # 3) obtain baseline set
        print(f'obtain Baseline set')
        main_parse_pcap(input_file=pcap_file, labels_file=labels_file, feat_set='Baseline')

    else:
        dir_tuple = [('Friday-WorkingHours', 'Friday-WorkingHours'),
                     ('Monday-WorkingHours', 'Monday-WorkingHours')]
        srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']

        fft_bin_lst = []
        for (pcap_dir, labels_dir) in dir_tuple:
            for srcIP in srcIP_lst:
                pcap_file = os.path.join('.', f'srcIP_{srcIP}', pcap_dir, f'srcIP_{srcIP}.pcap')
                print(f'pcap_file: {pcap_file}')
                labels_file = os.path.join('.', f'srcIP_{srcIP}', labels_dir, f'srcIP_{srcIP}.csv')
                print(f'labels_file: {labels_file}')

                # 1) obtain IAT set
                print(f'obtain IAT set')
                quant = 0.9
                fft_bins = main_parse_pcap(input_file=pcap_file, labels_file=labels_file, feat_set='IAT',
                                           quant=quant)
                print(f'srcIP: {srcIP}, quant: {quant}, flow_len_thres: {fft_bins}')

                # # 1) use fft_bins to fix the IAT size
                # print(f'obtain IAT set')
                # fft_bins = main_parse_pcap(input_file=pcap_file, labels_file=labels_file, feat_set='IAT',
                #                            quant=quant)
                # print(f'srcIP: {srcIP}, quant: {quant}, flow_len_thres: {fft_bins}')
                #
                # # 2) obtain FFT set
                # print(f'obtain FFT set')
                # main_parse_pcap(input_file=pcap_file, labels_file=labels_file, feat_set='FFT', fft_bins=fft_bins)

                # 3) obtain baseline set
                print(f'obtain Baseline set')
                main_parse_pcap(input_file=pcap_file, labels_file=labels_file, feat_set='Baseline')

                fft_bin_lst.append(fft_bins)
                print()

            #     break
            print(f'{zip(srcIP_lst, fft_bin_lst)}')
            break

    end_time = time.time()
    et = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
    print(f'end at {et}, tatally takes {end_time-start_time} s')
