"""Obtain features (IAT and baseline) from pcap

"""
# kun.bj@outlook.com
#
# License: xxx
import os
import sys
from collections import OrderedDict

sys.path.append(os.getcwd())  # for Slurm. Because Slurm cannot find the project

from utils.tool import execute_time, dump_data, pprint
import numpy as np
import pandas as pd
from scapy.layers.inet import *
from scapy.utils import PcapReader

TCP_TIMEOUT = 600  # 600 seconds
UDP_TIMEOUT = 600  # 600 seconds


def parse_dataset(pcap_file, labels_csv, fft_bins='', num_pkt_thresh=2, feat_set='', verbose=True):
    '''Parses pcap file into FFT features and labels file into string labels

      Arguments:
        pcap_file (string) = path to .pcap file
        labels_csv (string) = path to .csv file in CICIDS format
        num_pkt_thresh (int) = discards flows with fewer packets than max(2, thresh)
        fft_bins (int) = number of FFT bins

      Returns 2-tuple of (list, dict):
        features (list) = [(fid, n-bin FFT of IPIs, n-bin FFT of sizes)]
        labels[(5-tuple flow ID)] -> [label] (e.g. "BENIGN")
    '''
    if verbose:
        funcparams_dict = {'pcap_file': pcap_file, 'labels_csv': labels_csv, 'fft_bins': fft_bins,
                           'num_pkt_thresh': num_pkt_thresh, 'feat_set': feat_set, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=parse_dataset.__name__)

    flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh)
    print(f'num. of flows: {len(flows)}')
    if feat_set == 'IAT':
        features = _flows_to_IAT_features(flows)
    # elif feat_set == 'FFT':
    #     features = _flows_to_fft_features(flows, fft_bins)
    elif feat_set == 'Baseline':
        features = _flows_to_basic_features(flows)
    else:
        print(f'feat_set: {feat_set} is not implemented.')
        return -1

    labels = _load_labels_and_label_flows(labels_csv, features)
    print(f'num. of labels: {len(labels)}')
    # fids, features = list(*zip(features))
    fids = list(map(lambda x: x[0], features))
    features = list(map(lambda x: x[1], features))
    print(f'num. of flows: {len(fids)}')

    return fids, features, labels


def _load_pcap_to_flows(pcap_file, num_pkt_thresh, verbose=True):
    '''Reads pcap and divides packets into 5-tuple flows (arrival times and sizes)

       Arguments:
         pcap_file (string) = path to pcap file
         num_pkt_thresh (int) = discards flows with fewer packets than max(2, thresh)

       Returns:
         flows (list) = [(fid, arrival times list, packet sizes list)]
    '''
    if verbose:
        funcparams_dict = {'pcap_file': pcap_file,
                           'num_pkt_thresh': num_pkt_thresh, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=_load_pcap_to_flows.__name__)

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
                continue
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
                continue
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

    # sort all flows by packet arrival time, each flow must have at least two packets
    flows = [(fid, *list(zip(*sorted(times_sizes)))) for fid, times_sizes in all_flows if
             len(times_sizes) >= max(2, num_pkt_thresh)]

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
    # flows = [(fid, np.diff(times), sizes[1:]) for (fid, times, sizes) in flows]
    # calculate IATs
    # features = [(fid, times) for (fid, times, sizes) in flows]

    # for test purpose.
    for i, (fid, times, sizes) in enumerate(flows):  # flows is a list [(fid, features, label)]
        iats = np.diff(times)
        if len(iats[iats == 0]):
            if len(times) > 20:  # only print part of data
                print(f'i: {i}, np.diff(times): fid: {fid}, times (part of times to display): {times[:20]}, '
                      f'sizes: {sizes[:20]}, one reason is that retransmitted packets have the same time in wireshark,'
                      f'please check the pcap')
            else:
                print(
                    f'i: {i}, np.diff(times): fid: {fid}, times: {times}, sizes: {sizes}, '
                    f'one reason is that retransmitted packets have the same time in wireshark, please check the pcap')
        if sum(iats) == 0:  # flow's duration is 0.0. Is it possible? One reason is that the flow only have two packets,
            # one is the sent packet, another is the retransmitted packet which has the same time
            # to the sent packet in wireshark, please check
            print(f'i: {i}, sum(np.diff(times)):  fid: {fid}, times: {times}, sizes: {sizes}')

    features = [(fid, np.diff(times)) for (fid, times, sizes) in flows]

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
    data: len(pkt)

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
    flows = [(fid, np.diff(times), sizes) for (fid, times, sizes) in flows]  # there is no need to use sizes[1:]
    # len(np.diff(times)) + 1  == len(sizes)
    features = []
    for fid, times, sizes in flows:  # fid, IAT, pkt_len
        sub_duration = sum(times)  # Note: times here actually is the results of np.diff()
        num_pkts = len(sizes)  # number of packets in the flow
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


def _load_labels_and_label_flows(label_file='csv_file', features=''):
    '''Load binary labels from CICIDS format CSV

       Arguments:
         label_file: csv_file (string): path to CSV file

       Returns:
         labels[(5-tuple flow ID)] -> label (string) (e.g. "BENIGN")
    '''
    # load CSV with pandas
    csv = pd.read_csv(label_file)

    labels = {}
    for i, r in enumerate(csv.index):
        if i % 10000 == 0:
            print("Label CSV row {}".format(i))
        row = csv.loc[r]
        # parse 5-tuple flow ID
        fid = (row[" Source IP"], row[" Destination IP"], row[" Source Port"],
               row[" Destination Port"], row[" Protocol"])
        # ensure all 5-tuple flows have same label
        if fid in labels.keys():
            assert (labels[fid] == row[" Label"])  # if one fid has different labels
        # set label of flow ID
        labels[fid] = row[" Label"]

    # obtain the labels of the corresponding features
    new_labels = []
    not_existed_num = 0
    for i, (fid, feat) in enumerate(features):
        if fid in labels.keys():
            new_labels.append(labels[fid])
        else:
            not_existed_num += 1
            new_labels.append('None')  # the fid does not exist in labels.csv

    print(f'{not_existed_num} flows do not exist in {label_file}')

    return new_labels


#
# def main_parse_pcap(pcap_file, label_file='', feat_set='IAT', fft_bins='', quant=0.9):
#     """Get (fid, features, labels) from the given pcap_file and label_file
#
#     :param pcap_file:
#     :param label_file:
#     :param feat_set:
#     :param fft_bins:
#     :param quant:
#     :return:
#     """
#
#     funcparams_dict = {'pcap_file': pcap_file, 'label_file': label_file,
#                        'feat_set': feat_set, 'quant': quant, 'fft_bin': fft_bins}
#     pprint(OrderedDict(funcparams_dict), name=main_parse_pcap.__name__)
#
#     num_pkt_thresh = 2  # only keep the flow which at least has 2 packets.
#     # 1) obtain fids, features, labels from pcap and label_file
#     fids, features, labels = parse_dataset(pcap_file, labels_csv=label_file, fft_bins=fft_bins,
#                                            num_pkt_thresh=num_pkt_thresh, feat_set=feat_set)
#
#     tmp = [feat[0] for feat in features]  # for test purpose
#     print(f'{np.quantile(tmp, q=[0, 0.25, 0.5, 0.75, 1])}')
#     print(f'fids: {len(fids)}, features: {len(features)}, labels: {len(labels)}')
#     print(f'labels: {Counter(labels)}')
#     stat_data(features, name=f'{feat_set} features')
#
#     if feat_set == 'IAT':
#         # 2) save (fids, features, labels) to file
#         iat_file = pcap_file + f'_{feat_set}.dat'  # save IAT with different dimension
#         dump_data(data=(fids, features, labels), output_file=iat_file)
#
#         # 3) obtain fft_bins, and save flows_len_arr to file
#         flowslen_arr = [len(iats) for iats in features]
#         fft_bins = int(np.round(np.quantile(flowslen_arr, q=quant)))
#         print(f'choose quantile = {quant} and get fft_bins: {fft_bins}.')
#         print(f'len(flowslen_arr): {len(flowslen_arr)}, {sorted(set(flowslen_arr))}, \n{Counter(flowslen_arr)}')
#         # stat_data(np.array(flows_len_arr).reshape(-1, 1))
#         flowslen_file = pcap_file + f'_{feat_set}_flows_len.dat'
#         dump_data(data=flowslen_arr, output_file=flowslen_file)
#
#         # # 4) save the fixed IAT with fft_bins
#         # print(f'feat_set: {feat_set}, dimension: {fft_bins}')
#         # fixed_iat_file = pcap_file + f'_{feat_set}_dimension_{fft_bins}.dat'
#         #
#         # features_fixed = []
#         # for feat in features:
#         #     feat = list(feat)
#         #     if len(feat) > fft_bins:
#         #         feat = feat[:fft_bins]
#         #     else:
#         #         feat += [0] * (fft_bins - len(feat))
#         #     features_fixed.append(np.asarray(feat, dtype=float))
#         # dump_data(data=(fids, features_fixed, labels), output_file=fixed_iat_file)
#
#     elif feat_set == 'FFT':
#         # 2) save (fids, features, labels) to file
#         print(f'feat_set: {feat_set}, dimension: {fft_bins}')
#         output_file_1 = pcap_file + f'_{feat_set}_dimension_{fft_bins}.dat'  # IAT with different dimension
#         dump_data(data=(fids, features, labels), output_file=output_file_1)
#
#     elif feat_set == 'Baseline':
#         # 2) save (fids, features, labels) to file
#         dim = len(features[0])
#         print(f'feat_set: {feat_set}, dimension: {dim}')
#         base_file = pcap_file + f'_{feat_set}_dimension_{dim}.dat'  # IAT with different dimension
#         dump_data(data=(fids, features, labels), output_file=base_file)
#
#     return fft_bins
#

def demo():
    pcap_file = 'input_data/data/test.pcap'
    label_file = 'input_data/data/test.csv'
    num_pkt_thresh = 2

    srcIP = 'all'  # get all flows data ingored IPs
    # 1) obtain fids, features, labels from pcap and label_file
    print(f'obtain IAT set')
    prop_set = 'IAT'
    fids, features, labels = parse_dataset(pcap_file, labels_csv=label_file,
                                           num_pkt_thresh=num_pkt_thresh, feat_set=prop_set)
    iat_file = f'{pcap_file}-{prop_set}.dat'  # store IATs which have different dimensions to file
    dump_data(data=(fids, features, labels), output_file=iat_file)

    # 2) obtain baseline set
    print(f'obtain Baseline set')
    base_set = 'Baseline'
    fids, features, labels = parse_dataset(pcap_file, labels_csv=label_file,
                                           num_pkt_thresh=num_pkt_thresh, feat_set=base_set)
    dim = len(features[0])
    print(f'feat_set: {base_set}, dimension: {dim}')
    base_file = f'{pcap_file}-{base_set}-dim_{dim}.dat'
    dump_data(data=(fids, features, labels), output_file=base_file)


@execute_time
def main():
    """ Only for IAT and Baseline data

    :return:
    """
    input_dir = 'input_data/CICIDS2017'
    # pcap_dir and labels_dir may be in different folders
    dir_tuple = [('Friday-WorkingHours', 'Friday-WorkingHours'),  # (pcap_dir, labels_dir)
                 ('Monday-WorkingHours', 'Monday-WorkingHours')]
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    num_pkt_thresh = 2  # each flow at least has max(2, num_pkt_thresh) packets

    fftbin_lst = []
    q = 0.9  # use for obtaining fft_bin
    for (pcap_dir, label_dir) in dir_tuple:
        for srcIP in srcIP_lst:
            pcap_file = os.path.join(input_dir, f'srcIP_{srcIP}', pcap_dir, f'srcIP_{srcIP}.pcap')
            label_file = os.path.join(input_dir, f'srcIP_{srcIP}', label_dir, f'srcIP_{srcIP}.csv')

            # 1) obtain fids, features, labels from pcap and label_file
            print(f'obtain IAT set')
            prop_set = 'IAT'  # only IAT
            fids, features, labels = parse_dataset(pcap_file, labels_csv=label_file,
                                                   num_pkt_thresh=num_pkt_thresh, feat_set=prop_set)
            iat_file = f'{pcap_file}-{prop_set}.dat'  # store IATs which have different dimensions to file
            dump_data(data=(fids, features, labels), output_file=iat_file)

            fft_bin = int(np.round(np.quantile([len(iat) for iat in features], q=q)))
            print(f'fft_bin: {fft_bin} when q equals {q}')
            fftbin_lst.append(fft_bin)

            # 2) obtain baseline set
            print(f'obtain Baseline set')
            base_set = 'Baseline'
            fids, features, labels = parse_dataset(pcap_file, labels_csv=label_file,
                                                   num_pkt_thresh=num_pkt_thresh, feat_set=base_set)
            dim = len(features[0])
            print(f'feat_set: {base_set}, dimension: {dim}')
            base_file = f'{pcap_file}-{base_set}-dim_{dim}.dat'
            dump_data(data=(fids, features, labels), output_file=base_file)

            print()
            # break
        print(f'{zip(srcIP_lst, fftbin_lst)}')
        break


if __name__ == '__main__':
    main()
