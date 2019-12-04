import pickle

import numpy as np
import pandas as pd
from scapy.all import *

TCP_TIMEOUT = 1000 * 600  # 600 seconds
UDP_TIMEOUT = 1000 * 600  # 600 seconds


def parse_dataset(pcap_file, labels_csv, fft_bins, num_pkt_thresh, flg=1):
    '''Parses pcap file into FFT features and labels file into string labels

      Arguments:
        pcap_file (string) = path to .pcap file
        labels_csv (string) = path to .csv file in CICIDS format
        num_pkts_thresh (int) = discards flows with fewer packets than max(2, thresh)
        fft_bins (int) = number of FFT bins

        flg ==1: get features set 1
        flg ==2: get features set 2, must set fft_bins

      Returns 2-tuple of (list, dict):
        features (list) = [(fid, n-bin FFT of IPIs, n-bin FFT of sizes)]
        labels[(5-tuple flow ID)] -> [label] (e.g. "BENIGN")
    '''
    flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh)
    # features = _flows_to_fft_features(flows, fft_bins)
    features = _flows_to_features(flows, quantile=0.9, flg=flg, fft_bins=fft_bins)
    labels = _load_labels(labels_csv)
    return features, labels


def main():
    '''Main function performs all data loading, parsing, and saving'''
    # parse arguments
    if len(sys.argv) < 6:
        sys.exit("Usage: python3 {} [pcap_file] [labels_csv] [FFT bins] "
                 "[num pkt thresh] [output_file]".format(sys.argv[0]))
    pcap_file, labels_csv, output_file = sys.argv[1], sys.argv[2], sys.argv[5]
    fft_bins, num_pkt_thresh = int(sys.argv[3]), int(sys.argv[4])

    # process data
    features, labels = parse_dataset(pcap_file, labels_csv, fft_bins, num_pkt_thresh)

    # save results
    with open(output_file, 'wb') as output:
        pickle.dump((features, labels), output)


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
        if i % 1000 == 0:
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
    features = [(fid, np.real(np.fft.fft(times, n=fft_bins)),
                 np.real(np.fft.fft(sizes, n=fft_bins))) for (fid, times, sizes) in flows]
    return features


def _flows_to_features(flows, quantile=0.9, flg=1, fft_bins=5):
    '''Converts flows to FFT features

       Arguments:
         flows (list) = representation returned from read_pcap

         flg ==1: get features set 1
         flg ==2: get features set 2, must set fft_bins

    '''
    # convert Unix timestamp arrival times into interpacket intervals
    flows = [(fid, np.diff(times), sizes[1:]) for (fid, times, sizes) in flows]

    time_arr_len = [len(times) for (fid, times, sizes) in flows]
    fixed_size = np.quantile(time_arr_len, q=quantile)
    print(f'the fixed size of IATs in quantile ({quantile}) is {fixed_size}')

    features = []
    for (fid, times, sizes) in flows:
        if len(times) >= fixed_size:
            v = times[:fixed_size]  # trim
        else:
            v += [0] * (fixed_size - len(times))  # append 0 to the end
        if flg == 1:
            features.append((fid, v))
        elif flg == 2:
            v += np.real(np.fft.fft(times, n=fft_bins))
            features.append((fid, v))
        else:
            # todo
            print('not implement yet')

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
        if i % 1000 == 0:
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


if __name__ == "__main__":
    main()
