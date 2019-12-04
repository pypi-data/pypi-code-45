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
import pickle
import sys

# from data_process.preprocess_pcap import main_preprocess_pcap

sys.path.append(os.getcwd())  # for Slurm. Because Slurm cannot find the project

from collections import OrderedDict
from utils.tool import execute_time, dump_data, pprint, check_n_generate_path
import numpy as np
import pandas as pd
from scapy.layers.inet import *
from scapy.utils import PcapReader
from sklearn.utils import shuffle


def random_select_flows(flows, labels, experiment='ind', random_state=42):
    if experiment.upper() in ['INDV', 'MIX']:  # for indv and mix use all of data.
        return flows, labels

    cnt_normal = 0
    cnt_anomaly = 0
    for i, label_i in enumerate(labels):
        if label_i.upper() in ['NORMAL', 'BENIGN']:
            cnt_normal += 1
        elif label_i.upper() in ['BOT', 'ANOMALY']:
            cnt_anomaly += 1

    get_all_flows_flg = True  # True: use all of flows samples, False: random select part of flow samples.
    part_anomaly_thres = cnt_anomaly
    part_normal_thres = 20000 + part_anomaly_thres  # only random get 20000 normal samples.
    if cnt_normal > part_normal_thres:  # if cnt_normal > 20000 and cnt_anomaly > 150:
        get_all_flows_flg = False  # make all dataset have the same size
        # break # if has break here, it only print part of flows in cnt_normal

    print(f'before, len(flows): {len(flows)}, len(lables): {len(labels)}, get_all_flows_flg: {get_all_flows_flg}, '
          f'cnt_normal: {cnt_normal}, cnt_anomaly: {cnt_anomaly}')

    if not get_all_flows_flg:
        c = list(zip(flows, labels))
        flows_shuffle, labels_shuffle = zip(*shuffle(c, random_state=random_state))
        cnt_normal = 0
        cnt_anomaly = 0
        flows = []
        labels = []
        for i, (flows_i, label_i) in enumerate(zip(flows_shuffle, labels_shuffle)):
            if label_i.upper() in ['NORMAL', 'BENIGN']:
                cnt_normal += 1
                if cnt_normal <= part_normal_thres:
                    flows.append(flows_i)
                    labels.append(label_i)
            elif label_i.upper() in ['BOT', 'ANOMALY']:
                cnt_anomaly += 1
                if cnt_anomaly <= part_anomaly_thres:
                    flows.append(flows_i)
                    labels.append(label_i)

            if cnt_normal > part_normal_thres and cnt_anomaly > part_anomaly_thres:
                break
        else:
            pass
    print(f'len(flows): {len(flows)}, len(lables): {len(labels)}, get_all_flows_flg: {get_all_flows_flg}, '
          f'cnt_normal: {cnt_normal}, cnt_anomaly: {cnt_anomaly}')

    return flows, labels


def parse_dataset(pcap_file, labels_csv, experiment='ind', num_pkt_thresh=2, feat_set='', fft_bin=10, verbose=True,
                  sampling_type=None, sampling=None, q_sampling_rate=0.9, do_subflows_flg=False):
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
        funcparams_dict = {'pcap_file': pcap_file, 'labels_csv': labels_csv, 'experiment': experiment,
                           'sampling_type': sampling_type, 'sampling': sampling,
                           'num_pkt_thresh': num_pkt_thresh, 'feat_set': feat_set, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=parse_dataset.__name__)

    if do_subflows_flg:
        flows = _load_pcap_to_subflows(pcap_file, num_pkt_thresh=num_pkt_thresh, interval=0.1)
        # print("Number of FIDs in each subflow: {}".format([len(fids) for fids in list(zip(*flows))[0]]))
    else:
        flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh)  # get all flows which at least has more than 2 packets
    print(f'num. of flows: {len(flows)}')
    labels = _load_labels_and_label_flows(labels_csv, features=[(fid, _) for fid, _, _ in flows])

    flows, labels = random_select_flows(flows, labels, experiment=experiment)

    if feat_set == 'IAT':  # get IATs
        features = _flows_to_IAT_features(flows)
    elif feat_set == 'StatBaseline':  # get Baseline 1 which includes pkts_rate, bytes_rate, max, min, Q1, Q2, Q3.
        features = _flows_to_basic_features(flows)
    elif feat_set == 'SampBaseline':  # get features after sampling packets.
        if sampling == None:  # default sampling rate
            sampling_arr = [(max(times) - min(times)) / fft_bin for fid, times, sizes in flows]  # flow_duration/fft_bin
            # print(f'Counter(sampling_arr): {list(Counter(sampling_arr))[:100]}')   # [:100] for saving memory. if not, script will fails due to the lack of memory
            sampling = np.quantile(sampling_arr,
                                   q=q_sampling_rate)  # make 0.9 flow_duration /fft bin less than the sampling_rate.
            # sampling = float(f'{sampling:.4f}')           # if only keep .4f, sampling will be 0.
        print(f'sampling_type: {sampling_type}, samping: {sampling}')
        features = _flows_to_samp_basic_features(flows, sampling_type=sampling_type, sampling=sampling)
    else:
        raise ValueError(f'feat_set: {feat_set} is not implemented.')

    # labels = _load_labels_and_label_flows(labels_csv, features)
    print(f'num. of labels: {len(labels)}')
    # fids, features = list(*zip(features))
    fids = list(map(lambda x: x[0], features))
    features = list(map(lambda x: x[1], features))
    print(f'num. of flows: {len(fids)}')

    return fids, features, labels, sampling


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
                active_flows[fid].append((float(pkt.time), len(pkt)))
                continue
            # if this packet is a FIN, add it and close the active flow
            if pkt[TCP].flags.F:
                active_flows[fid].append((float(pkt.time), len(pkt)))
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
            # if the TCP timeout has elapsed, close the old active flow and start anew
            elif float(pkt.time) - active_flows[fid][-1][0] > TCP_TIMEOUT:
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
                active_flows[fid].append((float(pkt.time), len(pkt)))
            # otherwise, add to existing flow
            else:
                active_flows[fid].append((float(pkt.time), len(pkt)))

        # handle UDP packets
        elif IP in pkt and UDP in pkt:
            # parse 5-tuple flow ID
            fid = (pkt[IP].src, pkt[IP].dst, pkt[UDP].sport, pkt[UDP].dport, 17)
            # create a new active flow if one doesn't exist
            if not active_flows[fid]:
                active_flows[fid].append((float(pkt.time), len(pkt)))
                continue
            # if UDP timeout has elapsed, close the old active flow and start anew
            if float(pkt.time) - active_flows[fid][-1][0] > UDP_TIMEOUT:
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
                active_flows[fid].append((float(pkt.time), len(pkt)))
            # otherwise add to existing flow
            else:
                active_flows[fid].append((float(pkt.time), len(pkt)))

    # store remained active flows
    for fid in active_flows.keys():
        all_flows.append((fid, active_flows[fid]))  # change dict to tuple

    # sort all flows by packet arrival time, each flow must have at least two packets
    flows = [(fid, *list(zip(*sorted(times_sizes)))) for fid, times_sizes in all_flows if
             len(times_sizes) >= max(2, num_pkt_thresh)]

    return flows


def _load_pcap_to_subflows(pcap_file, num_pkt_thresh, interval=0.01, verbose=True):
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
                active_flows[fid].append((float(pkt.time), len(pkt)))
                continue
            # if this packet is a FIN, add it and close the active flow
            if pkt[TCP].flags.F:
                active_flows[fid].append((float(pkt.time), len(pkt)))
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
            # if the TCP timeout has elapsed, close the old active flow and start anew
            elif float(pkt.time) - active_flows[fid][-1][0]  > TCP_TIMEOUT:
                 # active_flows={key=fid: value=[pk;time, pkt.len]}
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
                active_flows[fid].append((float(pkt.time), len(pkt)))
            # if the TCP timeout has elapsed, close the old active flow and start anew
            elif float(pkt.time) - active_flows[fid][0][0] > interval:
                # subflow duration; current.pkt.time-first.pkt.time > interval
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
                active_flows[fid].append((float(pkt.time), len(pkt)))
            # otherwise, add to existing flow
            else:
                active_flows[fid].append((float(pkt.time), len(pkt)))

        # handle UDP packets
        elif IP in pkt and UDP in pkt:
            # parse 5-tuple flow ID
            fid = (pkt[IP].src, pkt[IP].dst, pkt[UDP].sport, pkt[UDP].dport, 17)
            # create a new active flow if one doesn't exist
            if not active_flows[fid]:
                active_flows[fid].append((float(pkt.time), len(pkt)))
                continue
            # if UDP timeout has elapsed, close the old active flow and start anew
            if float(pkt.time) - active_flows[fid][-1][0] > UDP_TIMEOUT:
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
                active_flows[fid].append((float(pkt.time), len(pkt)))
            elif float(pkt.time) - active_flows[fid][0][0] > interval:  # subflow duration
                all_flows.append((fid, active_flows[fid]))
                del active_flows[fid]
                active_flows[fid].append((float(pkt.time), len(pkt)))
            # otherwise add to existing flow
            else:
                active_flows[fid].append((float(pkt.time), len(pkt)))

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
                    print(f'i: {i}, 0 in np.diff(times): fid: {fid}, times (part of times to display): {times[:20]}, '
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
                print(f'i: {i}, sum(np.diff(times)) == 0:  fid: {fid}, times: {times}, sizes: {sizes}')

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


def handle_large_time_diff(start_time, end_time, interval=0.1, max_num=10000):
    """

    :param start_time:
    :param end_time:
    :param interval:
    :param max_num: the maximum number of 0 inserted to the features
    :return:
    """
    if start_time >= end_time:
        raise ValueError('start_time >= end_time')

    num_intervals = int((end_time - start_time) // interval)
    # print(f'num_intervals: {num_intervals}')
    if num_intervals > max_num:
        # print(
        #     f'num_intervals with 0: {num_intervals} = (end_time({end_time}) - start_time({start_time}))/(sampling_rate: {interval})'
        #     f', only keep: {max_num}')
        num_intervals = max_num
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
        # print(f'len(times): {len(times)}, duration: {max(times)-min(times)}, sampling: {sampling}, num_features: {int(np.round((max(times)-min(times))/sampling))}')
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
                    if len(features) > 1000:  # avoid num_features too large to excess the memory.
                        return fid, features[:1000]
                num_pkts_sub = 0
                num_pkts_sub += 1

        if num_pkts_sub > 0:  # handle the last sub period in the flow.
            features.append(num_pkts_sub)

        return fid, features
    else:
        raise ValueError(f'sample_type: {sample_type} is not implemented.')

    return fid, times


def _flows_to_samp_basic_features(flows, sampling_type='rate', sampling=None, verbose=True):
    ''' sampling packets in flows
    '''

    samp_flows = []
    for fid, times, sizes in flows:
        samp_fid, samp_features = sampling_packets((fid, times, sizes), sampling_type=sampling_type,
                                                   sampling=sampling)
        samp_flows.append((samp_fid, samp_features))

    if verbose:  # for debug
        show_len = 100  # only show the first 20 difference
        samp_lens = np.asarray([len(samp_features) for (fid, samp_features) in samp_flows])[:show_len]
        raw_lens = np.asarray([max(times) - min(times) for (fid, times, sizes) in flows])[:show_len]
        print(f'(flow duration, num_windows), when sampling_rate({sampling})):\n{list(zip(raw_lens,samp_lens))}')

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
            # assert (labels[fid] == row[" Label"])  # if one fid has different labels
            if labels[fid] != row[" Label"]:
                print(labels[fid], row[" Label"])
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


def _parse_subflows_and_label(flows, labels, num_pkt_thresh):
    '''Convert flows into subflow representation

    Arguments:
      flows = flows format returned from _load_pcap_to_flows()
      num_pkt_thresh (int) = discard subflows with fewer than this many packets

    Returns:
      subflows = list of (fids, times, sizes) for flow ids and each packet within each subflow
    '''
    # convert flows into list of all packets (time, size, fid)
    all_pkts = []
    for (fid, times, sizes), label in list(zip(flows, labels)):
        all_pkts.extend([(times[i], sizes[i], fid, label) for i in range(len(times))])
    # sort packets in all flows by arrival time
    all_pkts.sort()
    all_fids_sorted = list(zip(*all_pkts))[2]

    # iterate through packets in time order and create subflows
    subflows = []
    curr_subflow = ([], [], [], [])  # (fids, times, sizes, labels)
    for i, (time, size, fid, label) in enumerate(all_pkts):

        # an existing flow is continuing, so add it to subflow
        if fid in curr_subflow[0]:
            curr_subflow[1].append(time)
            curr_subflow[2].append(size)
            curr_subflow[3].append(label)

        # a new flow has started, so create a new subflow keeping the old fids
        else:
            if len(curr_subflow[1]) > max(2, num_pkt_thresh):
                subflows.append(curr_subflow)
            curr_fids = curr_subflow[0]
            curr_fids.append(fid)
            curr_subflow = (curr_fids, [time], [size], label)

        # if this is the last packet, add the current subflow and stop
        if i == len(all_pkts) - 1:
            if len(curr_subflow[1]) > max(2, num_pkt_thresh):
                subflows.append(curr_subflow)

        # if this is the last packet in this flow, end the subflow
        elif fid not in all_fids_sorted[i + 1:]:
            if len(curr_subflow[1]) > max(2, num_pkt_thresh):
                subflows.append(curr_subflow)
            curr_fids = curr_subflow[0]
            curr_fids.remove(fid)
            curr_subflow = (curr_fids, [], [], label)

    # return the subflows

    flows = list(map(lambda x: (x[0], x[1], x[2]), subflows))
    labels = list(map(lambda x: x[3], subflows))
    print(f'num. of flows: {len(labels)}')

    return flows, labels


@execute_time
def demo():
    pcap_file = 'input_data/data/test.pcap'
    label_file = 'input_data/data/test.csv'
    num_pkt_thresh = 2
    # sampling_type = 'interval'
    # sampling = 0.1  # second unit
    sampling_type = 'rate'  # sampling rate: sampling_rate=100 means that selects 100 pkts per second
    sampling = None  #

    # 1) obtain fids, features, labels from pcap and label_file
    print(f'\nobtain IAT set')
    prop_set = 'IAT'  # only IAT
    prop_fids, prop_features, prop_labels, _ = parse_dataset(pcap_file, labels_csv=label_file,
                                                             num_pkt_thresh=num_pkt_thresh, feat_set=prop_set)
    iat_file = f'{pcap_file}-{prop_set}.dat'  # store IATs which have different dimensions to file
    dump_data(data=(prop_fids, prop_features, prop_labels), output_file=iat_file)

    q = 0.9  # use for obtaining fft_bin
    fft_bin = int(np.round(np.quantile([len(iat) for iat in prop_features], q=q)))
    print(f'fft_bin: {fft_bin} when q equals {q}')

    # # 2) obtain baseline set 1: statistical inform
    # print(f'\nobtain Baseline set')
    # base_set = 'StatBaseline'  # label basic flow features
    # base_fids, base_features, base_labels, _ = parse_dataset(pcap_file, labels_csv=label_file,
    #                                                       num_pkt_thresh=num_pkt_thresh, feat_set=base_set)
    # base_dim = len(base_features[0])
    # print(f'feat_set: {base_set}, dimension: {base_dim}')
    # base_file = f'{pcap_file}-{base_set}-dim_{base_dim}.dat'  # store Baseline 1 with fixed size
    # dump_data(data=(base_fids, base_features, base_labels), output_file=base_file)

    # 3) obtain baseline set 2: sampling rate
    print(f'\nobtain Baseline set 2')
    samp_base_set = 'SampBaseline'  # label sampled features
    samp_base_fids, samp_base_features, samp_base_labels, sampling = parse_dataset(pcap_file, labels_csv=label_file,
                                                                                   sampling_type=sampling_type,
                                                                                   sampling=None,
                                                                                   num_pkt_thresh=num_pkt_thresh,
                                                                                   fft_bin=fft_bin,
                                                                                   feat_set=samp_base_set)
    print(f'feat_set: {samp_base_set}, with different lengths')
    # store sampled IATs which have different dimensions to file
    samp_base_file = f'{pcap_file}-{samp_base_set}-{sampling_type}_{sampling}.dat'
    dump_data(data=(samp_base_fids, samp_base_features, samp_base_labels), output_file=samp_base_file)


def merge_files_to_one(file_lst=[], mixed_file='', verbose=True):
    if verbose:
        funcparams_dict = {'file_lst': file_lst, 'mixed_file': mixed_file}
        pprint(OrderedDict(funcparams_dict), name=merge_files_to_one.__name__)
    check_n_generate_path(file_path=mixed_file, overwrite=True)

    with open(mixed_file, 'wb') as out_hdl:
        for idx, file_path in enumerate(file_lst):
            print(f'*index: {idx}, file_path: {file_path}')
            with open(file_path, 'rb') as in_hdl:
                fids, features, labels = pickle.load(in_hdl)
                pickle.dump((fids, features, labels), out_hdl)

    print(f'mixed_file: {mixed_file}')

    return mixed_file


if __name__ == '__main__':
    from os import sys, path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    demo()
    preprocess_flg = False
    # if preprocess_flg:  # filter unrelated IPs and the results will be saved at 'multi-srcIPs' for smart-tv-roku-data
    #     main_preprocess_pcap(dataset_name='smart-tv-roku-data', overwrite=True)
