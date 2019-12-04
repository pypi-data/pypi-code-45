import pickle
from collections import Counter

import numpy as np
import pandas as pd
from scapy.all import *

# from base import stat_data

TCP_TIMEOUT = 1000 * 600  # 600 seconds
UDP_TIMEOUT = 1000 * 600  # 600 seconds


def parse_dataset(pcap_file, labels_csv, fft_bins='', num_pkt_thresh=2, features_flg=''):
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
    if features_flg == 'IAT':
        features = _flows_to_IAT_features(flows)
    elif features_flg == 'FFT':
        features = _flows_to_fft_features(flows, fft_bins)
    elif features_flg == 'Baseline':
        features = _flows_to_basic_features(flows)
    else:
        print('not implemented.')
        return -1

    labels = _load_labels_2(labels_csv, features)

    # fids, features = list(*zip(features))
    fids = list(map(lambda x: x[0], features))
    features = list(map(lambda x: x[1], features))
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


def _load_labels(csv_file):
    '''Load binary labels from CICIDS format CSV

       Arguments:
         csv_file (string): path to CSV file

       Returns:
         labels[(5-tuple flow ID)] -> label (string) (e.g. "BENIGN")
    '''
    # load CSV with pandas
    csv = pd.read_csv(csv_file)

    # process each row iteratively
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
    return labels


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

    for i, value in enumerate(features):
        fid = value[0]
        if fid in labels.keys():
            new_labels.append(labels[fid])

    return new_labels


def main(srcIP, features_flg, fft_bins='', quant=0.9):
    # '''Main function performs all data loading, parsing, and saving'''
    # # parse arguments
    # if len(sys.argv) < 6:
    #     sys.exit("Usage: python3 {} [pcap_file] [labels_csv] [FFT bins] "
    #              "[num pkt thresh] [output_file]".format(sys.argv[0]))
    # pcap_file, labels_csv, output_file = sys.argv[1], sys.argv[2], sys.argv[5]
    # fft_bins, num_pkt_thresh = int(sys.argv[3]), int(sys.argv[4])

    # features_flg = 'Baseline'  # 'IAT', 'FFT', 'Baseline'
    print(f'features_flg:{features_flg}')
    # pcap_file =f'input_data/data/test.pcap'
    # pcap_file = f'CICIDS2017/Merged-WorkingHours-Morning_5_bots_20170707-09_40-11_30-srcIP_{srcIP}.pcap'
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

    labels_csv = 'input_data/CICIDS2017/Merged-WorkingHours-Morning.pcap_ISCX.csv'
    # labels_csv = 'input_data/data/test.csv'
    num_pkt_thresh = 2
    # process data
    fids, features, labels = parse_dataset(pcap_file, labels_csv, fft_bins=fft_bins, num_pkt_thresh=num_pkt_thresh,
                                           features_flg=features_flg)

    # print(f'features: {features.shape}, labels: {Counter(labels)}')
    print(f'labels: {Counter(labels)}')
    # stat_data(features)

    output_file = pcap_file + f'_{features_flg}.txt'
    # # save results
    with open(output_file, 'wb') as out_hdl:
        pickle.dump((fids, features, labels), out_hdl)

    flows_len_arr = [len(value) for value in features]
    fft_bins = int(np.quantile(flows_len_arr, q=quant))
    print(f'choose quantile = {quant} and get fft_bins: {fft_bins}.')
    print(f'len(flows_len_arr): {len(flows_len_arr)}, {sorted(set(flows_len_arr))}, {Counter(flows_len_arr)}')
    # stat_data(np.array(flows_len_arr).reshape(-1, 1))

    output_file = pcap_file + f'_{features_flg}_flows_len.txt'
    # # save results
    with open(output_file, 'wb') as out_hdl:
        pickle.dump(flows_len_arr, out_hdl)

    return fft_bins


def get_normal_data(pcap_file, label=['Benign']):
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


#         tshark -r Merged-WorkingHours.pcap -w result.pcap "ip.src==192.168.10.5 or ip.src==192.168.10.8 or ip.src==192.168.10.9 or ip.src==192.168.10.14 or ip.src==192.168.10.15"
#  tshark -r Monday-WorkingHours.pcap -w Monday-WorkingHours_normal.pcap "ip.src==192.168.10.5 or ip.src==192.168.10.8 or ip.src==192.168.10.9 or ip.src==192.168.10.14 or ip.src==192.168.10.15"


if __name__ == "__main__":
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    # # features_flg = 'Baseline'  # 'IAT', 'FFT', 'Baseline'
    # for srcIP in srcIP_lst:
    #     flow_len_thres=main(srcIP, features_flg='IAT', quant = 0.9)
    #     print(f'srcIP: {srcIP}, flow_len_thres: {flow_len_thres}')
    #     main(srcIP, features_flg='FFT', fft_bins = flow_len_thres)
    #     main(srcIP, features_flg='Baseline')

    # features_flg = 'Baseline'  # 'IAT', 'FFT', 'Baseline'
    for srcIP in srcIP_lst:
        flow_len_thres = main(srcIP, features_flg='IAT', quant=0.9)
        print(f'srcIP: {srcIP}, flow_len_thres: {flow_len_thres}')
        main(srcIP, features_flg='FFT', fft_bins=flow_len_thres)
        main(srcIP, features_flg='Baseline')
