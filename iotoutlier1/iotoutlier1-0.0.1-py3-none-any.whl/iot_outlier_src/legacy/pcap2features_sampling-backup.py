"""Obtain features (IAT and baseline) from pcap


    Unfortunately the speed of vanilla Linux kernel networking is not sufficient for more specialized workloads.
    For example, here at CloudFlare, we are constantly dealing with large packet floods.
    Vanilla Linux can do only about 1M pps. This is not enough in our environment,
    especially since the network cards are capable of handling a much higher throughput.
    Modern 10Gbps NIC’s can usually process at least 10M pps.
    Such as DPDK, Moongen

    https://serverascode.com/2018/12/31/ten-million-packets-per-second.html


"""
# kun.bj@outlook.com
#
# License: xxx
import os
import sys

sys.path.append(os.getcwd())  # for Slurm. Because Slurm cannot find the project

from collections import OrderedDict
from utils.tool import execute_time, dump_data, pprint
import numpy as np
import pandas as pd
from scapy.layers.inet import *
from scapy.utils import PcapReader
from sklearn.utils import shuffle


def parse_dataset(pcap_file, labels_csv, num_pkt_thresh=2, feat_set='', verbose=True,
                  sampling_type=None, sampling=None):
    '''Parses pcap file into flow features (such as, IAT, pkts_rate and max_pkt) and labels flow into string labels

      Arguments:
        pcap_file (string) = path to .pcap file
        labels_csv (string) = path to .csv file in CICIDS format
        num_pkt_thresh (int) = discards flows with fewer packets than max(2, thresh), exclude (2 packets)

      Returns 2-tuple of (list, dict):
        features (list) = [(fid, features)]
        labels[(5-tuple flow ID)] -> [label] (e.g. "BENIGN")
    '''
    if verbose:
        funcparams_dict = {'pcap_file': pcap_file, 'labels_csv': labels_csv,
                           'sampling_type': sampling_type, 'sampling': sampling,
                           'num_pkt_thresh': num_pkt_thresh, 'feat_set': feat_set, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=parse_dataset.__name__)

    flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh)  # get all flows which at least has more than 2 packets
    print(f'num. of flows: {len(flows)}')
    if feat_set == 'IAT':  # get IATs
        features = _flows_to_IAT_features(flows)
    elif feat_set == 'StatBaseline':  # get Baseline 1 which includes pkts_rate, bytes_rate, max, min, Q1, Q2, Q3.
        features = _flows_to_basic_features(flows)
    elif feat_set == 'SampBaseline':  # get features after sampling packets.
        features = _flows_to_samp_basic_features(flows, sampling_type=sampling_type, sampling=sampling)
    else:
        raise ValueError(f'feat_set: {feat_set} is not implemented.')

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

    TCP_TIMEOUT = 600  # 600 seconds
    UDP_TIMEOUT = 600  # 600 seconds

    if verbose:
        funcparams_dict = {'pcap_file': pcap_file, 'TCP_TIMEOUT': TCP_TIMEOUT, 'UDP_TIMEOUT': UDP_TIMEOUT,
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

    # store remained active flows
    for fid in active_flows.keys():
        all_flows.append((fid, active_flows[fid]))  # change dict to tuple

    # sort all flows by packet arrival time, each flow must have at least two packets
    flows = [(fid, *list(zip(*sorted(times_sizes)))) for fid, times_sizes in all_flows if
             len(times_sizes) >= max(2, num_pkt_thresh)]

    return flows


def _flows_to_IAT_features(flows, verbose=True):
    '''Get IATs features from flows

       Arguments:
         flows (list) = representation returned from read_pcap

       Returns:
         features (list) = [(fid, IATs)]
    '''
    # convert Unix timestamp arrival times into interpacket intervals
    # calculate IATs
    if verbose:  # for verifying the code
        for i, (fid, times, sizes) in enumerate(flows):  # flows is a list [(fid, features, label)]
            iats = np.diff(times)
            if (0 in iats) or (len(iats[iats == 0])):  # if two packets have the same timestamp?
                if len(times) > 20:  # only print part of data
                    print(f'i: {i}, np.diff(times): fid: {fid}, times (part of times to display): {times[:20]}, '
                          f'sizes: {sizes[:20]}, one reason is that retransmitted packets have the same time '
                          f'in wireshark, please check the pcap')
                else:
                    print(
                        f'i: {i}, np.diff(times): fid: {fid}, times: {times}, sizes: {sizes}, one reason is that '
                        f'retransmitted packets have the same time in wireshark, please check the pcap')
            if sum(iats) == 0:  # flow's duration is 0.0. Is it possible?
                # One reason is that the flow only have two packets:
                # one is the sent packet, another is the retransmitted packet which has the same time
                # to the sent packet in wireshark, please check
                print(f'i: {i}, sum(np.diff(times)):  fid: {fid}, times: {times}, sizes: {sizes}')

    features = [(fid, np.diff(times)) for (fid, times, sizes) in flows]  # (fid, np.array())

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


       Returns:
         features (list) = [(fid, (max, min, ... ))]
    '''
    # convert Unix timestamp arrival times into interpacket intervals
    flows = [(fid, np.diff(times), sizes) for (fid, times, sizes) in flows]  # No need to use sizes[1:]
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

        features.append((fid, np.asarray([np.float64(v) for v in base_feature], dtype=np.float64)))  # (fid, np.array())

    return features


def handle_large_time_diff(start_time, end_time, interval=0.1):
    if start_time >= end_time:
        raise ValueError('start_time >= end_time')

    num_intervals = int((end_time - start_time) // interval)
    # print(f'num_intervals: {num_intervals}')
    features_lst = [0] * num_intervals

    start_time = start_time + num_intervals * interval

    return features_lst, start_time


def sampling_packets(flow, sampling_type='number', sampling=5, random_state=42):
    """

    :param flow:
    :param sampling_type:
    :param sampling:
    :return:
    """
    fid, times, sizes = flow
    sampling_data = []
    if sampling_type == 'interval':  # sampling = 0.1s, 1s, 2s, ....  second unit
        for i in range(len(times)):
            if i == 0:  # get first packet
                current = times[0]
                sampling_data.append((times[0], sizes[0]))
                continue
            if times[i] - current > sampling:  # sampling time interval: 0.1s, 1s, 2s, ...
                current = times[i]
                sampling_data.append((times[i], sizes[i]))
        times, sizes = list(zip(*sampling_data))

    elif sampling_type == 'number':  # sampling = 1, 5, ...
        sampling_data = [(times[i], sizes[i]) for i in range(len(times)) if i % sampling == 0]
        times, sizes = list(zip(*sampling_data))

    elif sampling_type == 'samp_rate':  # sampling_rate within flows. sampling_rate=100 means that selects 100 pkts per second
        sub_flow_duration = max(times) - min(times)  # times[-1]-times[0]  # duration in second
        num_samp_pkts = int(np.round(sampling * sub_flow_duration))
        print(f'num_samp_pkts({num_samp_pkts}) >? len(times)({len(times)}), sub_flow_duration: {sub_flow_duration}')
        # random select num_samp_pkts from len(times)
        # np.random.randint(low, high, size) Return random integers from `low` (inclusive) to `high` (exclusive).
        if num_samp_pkts <= 0:
            times = []
            sizes = []
        elif num_samp_pkts < len(times):
            indexs = list(range(0, len(times)))
            indexs = shuffle(indexs, random_state=random_state)  # set random_state to make results reproducible
            indexs = sorted(indexs[:num_samp_pkts])  # IAT (times) should arrive in order
            times = [times[i] for i in indexs]
            sizes = [sizes[i] for i in indexs]
        else:  # num_samp_pkts >= len(times):  keep all packets of the flow
            return fid, times

    elif sampling_type == 'rate':  # sampling_rate within flows.
        # The length in time of this small window is what we’re calling sampling rate.
        # features obtained on sampling_rate = 0.1 means that:
        #  1) split each flow into small windows, each window has 0.1 duration (the length in time of each small window)
        #  2) obtain the number of packets in each window (0.1s).
        #  3) all the number of packets in each window make up of the features.

        features = []
        num_pkts_sub = 0
        for i in range(len(times)):  # times: the arrival time of each packet
            if i == 0:
                current = times[0]
                num_pkts_sub += 1
                continue
            if times[i] - current <= sampling:  # interval
                num_pkts_sub += 1
            else:  # if times[i]-current > sampling:    # interval
                current += sampling
                features.append(num_pkts_sub)
                # the time diff between times[i] and times[i-1] will be larger than mutli-samplings
                # for example, times[i]=10.0s, times[i-1]=2.0s, sampling=0.1,
                # for this case, we should insert int((10.0-2.0)//0.1) * [0]
                if current + sampling <= times[i]:  # move current to the nearest position to time[i]
                    feat_lst_tmp, current = handle_large_time_diff(start_time=current, end_time=times[i],
                                                                   interval=sampling)
                    features.extend(feat_lst_tmp)
                num_pkts_sub = 0
                num_pkts_sub += 1

        if num_pkts_sub > 0:  # handle the last sub period in the flow.
            features.append(num_pkts_sub)

        return fid, features
    else:
        raise ValueError(f'sample_type: {sample_type} is not implemented.')

    return fid, times


#
# def _flows_to_samp_basic_features(flows, sampling_type=None, sampling=None, verbose=True):
#     ''' sampling packets in flows
#     '''
#
#     samp_flows = []
#     for fid, times, sizes in flows:
#         samp_fid, samp_times, samp_sizes = sampling_packets((fid, times, sizes), sampling_type=sampling_type,
#                                                             sampling=sampling)
#         samp_flows.append((samp_fid, samp_times, samp_sizes))
#     if verbose:
#         show_len = 100  # only show the first 20 difference
#         samp_lens = np.asarray([len(samp_times) for (fid, samp_times, samp_sizes) in samp_flows])[:show_len]
#         raw_lens = np.asarray([len(times) for (fid, times, sizes) in flows])[:show_len]
#         print(f'after sampling, number of unsampled packets in each flow (raw_lens-samp_lens): {raw_lens-samp_lens}')
#     # It will discard some flows which have one packet after sampling.
#     # After np.diff(times), the minimum flow has one IAT based on two packets.
#     features = [(fid, np.diff(times)) for (fid, times, sizes) in samp_flows if len(times) >= 2]
#
#     return features


def _flows_to_samp_basic_features(flows, fft_bin, q=0.9, sampling_type=None, sampling=None, verbose=True):
    ''' sampling packets in flows
    '''

    sampling_arr = [(max(times) - min(times)) / fft_bin for fid, times, sizes in flows]  # flow_duration/fft_bin
    sampling = np.quantile(sampling_arr, q=q)  # sampling = 0.9 flow_duration / fft_bin
    print(f'samping: {sampling}')
    samp_flows = []
    for fid, times, sizes in flows:
        samp_fid, samp_features = sampling_packets((fid, times, sizes), sampling_type=sampling_type,
                                                   sampling=sampling)
        samp_flows.append((samp_fid, samp_features))

    if verbose:  # for debug
        show_len = 100  # only show the first 20 difference
        samp_lens = np.asarray([len(samp_features) for (fid, samp_features) in samp_flows])[:show_len]
        raw_lens = np.asarray([max(times) - min(times) for (fid, times, sizes) in flows])[:show_len]
        print(f'(flow duration, num_windows, sampling_rate({sampling}))\n{list(zip(raw_lens,samp_lens))}')

    features = samp_flows

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


def demo():
    pcap_file = 'input_data/data/test.pcap'
    label_file = 'input_data/data/test.csv'
    num_pkt_thresh = 2
    # sampling_type = 'interval'
    # sampling = 0.1  # second unit
    sampling_type = 'rate'  # sampling rate: sampling_rate=100 means that selects 100 pkts per second
    sampling = 0.01  # 0.01s: small window (sampling rate)

    # # 1) obtain fids, features, labels from pcap and label_file
    # print(f'obtain IAT set')
    # prop_set = 'IAT'  # only IAT
    # prop_fids, prop_features, prop_labels = parse_dataset(pcap_file, labels_csv=label_file,
    #                                                       num_pkt_thresh=num_pkt_thresh, feat_set=prop_set)
    # iat_file = f'{pcap_file}-{prop_set}.dat'  # store IATs which have different dimensions to file
    # dump_data(data=(prop_fids, prop_features, prop_labels), output_file=iat_file)
    #
    # q = 0.9  # use for obtaining fft_bin
    # fft_bin = int(np.round(np.quantile([len(iat) for iat in prop_features], q=q)))
    # print(f'fft_bin: {fft_bin} when q equals {q}')
    #
    # # 2) obtain baseline set 1: statistical inform
    # print(f'obtain Baseline set')
    # base_set = 'StatBaseline'  # label basic flow features
    # base_fids, base_features, base_labels = parse_dataset(pcap_file, labels_csv=label_file,
    #                                                       num_pkt_thresh=num_pkt_thresh, feat_set=base_set)
    # base_dim = len(base_features[0])
    # print(f'feat_set: {base_set}, dimension: {base_dim}')
    # base_file = f'{pcap_file}-{base_set}-dim_{base_dim}.dat'  # store Baseline 1 with fixed size
    # dump_data(data=(base_fids, base_features, base_labels), output_file=base_file)

    # 3) obtain baseline set 2: sampling rate
    print(f'obtain Baseline set 2')
    samp_base_set = 'SampBaseline'  # label sampled features
    samp_base_fids, samp_base_features, samp_base_labels = parse_dataset(pcap_file, labels_csv=label_file,
                                                                         sampling_type=sampling_type,
                                                                         sampling=sampling,
                                                                         num_pkt_thresh=num_pkt_thresh,
                                                                         feat_set=samp_base_set)
    print(f'feat_set: {samp_base_set}, with different lengths')
    # store sampled IATs which have different dimensions to file
    samp_base_file = f'{pcap_file}-{samp_base_set}-{sampling_type}_{sampling}.dat'
    dump_data(data=(samp_base_fids, samp_base_features, samp_base_labels), output_file=samp_base_file)


@execute_time
def main():
    """ Obtain raw features data: IAT, Baseline 1 and Baseline 2
        1) IAT (with different dimensions of different flows),
        2) Baseline 1 (statistic: such as max, mean and std): fixed length (10 dimensions vector)
        3) Baseline 2 (sampling based on number (such as choose 1 from 10 packets) or
              time (such as 0.1s and 2s))
    :return:
    """
    input_dir = 'input_data/CICIDS2017'
    # pcap_dir and label_dir may be in different folders
    dir_tuple = [('Friday-WorkingHours', 'Friday-WorkingHours'),  # (pcap_dir, label_dir)
                 ('Monday-WorkingHours', 'Monday-WorkingHours')]
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    num_pkt_thresh = 2  # each flow at least has max(2, num_pkt_thresh) packets

    fftbin_lst = []
    # sampling_type = 'interval' # sampling based on number: choose 1 from 10 packets, or based on interval (second unit)
    # sampling = 0.09  # sampling based on number: choose 1 from 10 packets, or 0.1s
    # sampling_type = 'number'  # sampling based on number: choose 1 from 10 packets, or based on interval (second unit)
    # sampling = 4  # sampling based on number: choose 1 from 10 packets, or 0.1s
    # sampling_type = 'samp_rate'  # sampling rate: sampling_rate=100 means that selects 100 pkts per second without repeated sampling
    # sampling = 1000  # 1000 pkts per second
    sampling_type = 'rate'  # sampling rate: 0.1 means that split flow into small windows, each window has 0.1s duration
    sampling = 10  # 2s

    for (pcap_dir, label_dir) in dir_tuple:  # for different days' data
        for srcIP in srcIP_lst:  # for different IPs
            pcap_file = os.path.join(input_dir, f'srcIP_{srcIP}', pcap_dir, f'srcIP_{srcIP}.pcap')
            label_file = os.path.join(input_dir, f'srcIP_{srcIP}', label_dir, f'srcIP_{srcIP}.csv')

            # # 1) obtain fids, features, labels from pcap and label_file
            # print(f'obtain IAT set')
            # prop_set = 'IAT'  # only IAT
            # prop_fids, prop_features, prop_labels = parse_dataset(pcap_file, labels_csv=label_file,
            #                                                       num_pkt_thresh=num_pkt_thresh, feat_set=prop_set)
            # iat_file = f'{pcap_file}-{prop_set}.dat'  # store IATs which have different dimensions to file
            # dump_data(data=(prop_fids, prop_features, prop_labels), output_file=iat_file)
            #
            # q = 0.9  # use for obtaining fft_bin
            # fft_bin = int(np.round(np.quantile([len(iat) for iat in prop_features], q=q)))
            # print(f'fft_bin: {fft_bin} when q equals {q}')
            # fftbin_lst.append(fft_bin)
            #
            # # 2) obtain baseline set 1: statistical inform
            # print(f'obtain Baseline set')
            # base_set = 'StatBaseline'  # label basic flow features
            # base_fids, base_features, base_labels = parse_dataset(pcap_file, labels_csv=label_file,
            #                                                       num_pkt_thresh=num_pkt_thresh, feat_set=base_set)
            # base_dim = len(base_features[0])
            # print(f'feat_set: {base_set}, dimension: {base_dim}')
            # base_file = f'{pcap_file}-{base_set}-dim_{base_dim}.dat'  # store Baseline 1 with fixed size
            # dump_data(data=(base_fids, base_features, base_labels), output_file=base_file)

            # 3) obtain baseline set 2: sampling rate
            print(f'obtain Baseline set 2')
            samp_base_set = 'SampBaseline'  # label sampled features
            samp_base_fids, samp_base_features, samp_base_labels = parse_dataset(pcap_file, labels_csv=label_file,
                                                                                 sampling_type=sampling_type,
                                                                                 sampling=sampling,
                                                                                 num_pkt_thresh=num_pkt_thresh,
                                                                                 feat_set=samp_base_set)
            print(f'feat_set: {samp_base_set}, with different lengths')
            # store sampled IATs which have different dimensions to file
            samp_base_file = f'{pcap_file}-{samp_base_set}-{sampling_type}_{sampling}.dat'
            dump_data(data=(samp_base_fids, samp_base_features, samp_base_labels), output_file=samp_base_file)

            print()
            # break
        print(f'{list(zip(srcIP_lst, fftbin_lst))}')
        break


if __name__ == '__main__':
    demo()
    main()
