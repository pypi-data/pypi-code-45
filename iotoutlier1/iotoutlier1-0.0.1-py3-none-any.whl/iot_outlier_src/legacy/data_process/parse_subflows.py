import pickle

import numpy as np
import pandas as pd
from scapy.all import *
from scapy.layers.inet import *

TCP_TIMEOUT = 1000 * 600  # 600 seconds
UDP_TIMEOUT = 1000 * 600  # 600 seconds


def parse_dataset(pcap_file, labels_csv, fft_bins, num_pkt_thresh, do_subflows):
    '''Parses pcap file into FFT features and labels file into string labels

      Arguments:
        pcap_file (string) = path to .pcap file
        labels_csv (string) = path to .csv file in CICIDS format
        num_pkts_thresh (int) = discards flows with fewer packets than max(2, thresh)
        fft_bins (int) = number of FFT bins
        do_subflows (bool) = whether to parse and label subflows

      Returns 4-tuple of (list, list, list, list)
        flow_features (list) = [(fid, n-bin FFT of IPIs, n-bin FFT of sizes)]
        flow_labels (list) = [string label] (equivalently indexed to flow_features)
      if do_subflows is FALSE the following will be empty lists:
        subflow_features (list) [(fids, n-bin FFT of IPIs, n-bin FFT of sizes)]
        subflow_labels (list) [string label] (equivalently indexed to subflow_features))
    '''
    flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh)
    labels = _load_labels(labels_csv)
    flow_labels = _label_flows(flows, labels)
    flow_features = _flows_to_fft_features(flows, fft_bins)

    if do_subflows:
        subflows = _parse_subflows(flows, num_pkt_thresh)
        subflow_labels = _label_subflows(subflows, labels)
        subflow_features = _flows_to_fft_features(subflows, fft_bins)
        print("Number of FIDs in each subflow: {}".format([len(fids) for fids in list(zip(*subflows))[0]]))
    else:
        subflow_features, subflow_labels = [], []

    return flow_features, flow_labels, subflow_features, subflow_labels


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
        all_flows.append((fid, active_flows[fid]))

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


def _label_flows(flows, labels):
    '''Assign labels to each flow

    Arguments:
      flows = flows format returned from _parse_pcap_to_flows()
      labels = labels format returned from _load_labels()

    Returns:
       flow_labels [string] = list of string labels equivalently indexed to flows
    '''
    flow_labels = []
    for fid, _, _ in flows:
        try:
            flow_labels.append(labels[fid])
        except KeyError:
            flow_labels.append("UNKNOWN")
    return flow_labels


def _parse_subflows(flows, num_pkt_thresh):
    '''Convert flows into subflow representation

    Arguments:
      flows = flows format returned from _load_pcap_to_flows()
      num_pkt_thresh (int) = discard subflows with fewer than this many packets

    Returns:
      subflows = list of (fids, times, sizes) for flow ids and each packet within each subflow
    '''
    # convert flows into list of all packets (time, size, fid)
    all_pkts = []
    for fid, times, sizes in flows:
        all_pkts.extend([(times[i], sizes[i], fid) for i in range(len(times))])
    # sort packets in all flows by arrival time
    all_pkts.sort()
    all_fids_sorted = list(zip(*all_pkts))[2]

    # iterate through packets in time order and create subflows
    subflows = []
    curr_subflow = ([], [], [])  # (fids, times, sizes)
    for i, (time, size, fid) in enumerate(all_pkts):

        # an existing flow is continuing, so add it to subflow
        if fid in curr_subflow[0]:
            curr_subflow[1].append(time)
            curr_subflow[2].append(size)

        # a new flow has started, so create a new subflow keeping the old fids
        else:
            if len(curr_subflow[1]) > max(2, num_pkt_thresh):
                subflows.append(curr_subflow)
            curr_fids = curr_subflow[0]
            curr_fids.append(fid)
            curr_subflow = (curr_fids, [time], [size])

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
            curr_subflow = (curr_fids, [], [])

    # return the subflows
    return subflows


def _label_subflows(subflows, labels):
    '''Assigns singular labels to each subflow depending on the set of flows it contains
       If *all* contained flows are benign, the subflow is benign, otherwise malicious

    Arguments:
      subflows = subflows format returned from _parse_subflows()
      labels = labels format returned from _load_labels()

    Returns:
      subflow_labels [string] = list of 1 string label per equivalently indexed subflow
    '''
    subflow_labels = []
    for fids, _, _ in subflows:
        fids_labels = []
        for fid in fids:
            try:
                fids_labels.append(labels[fid])
            except KeyError:
                fids_labels.append("UNKNOWN")
        unique_labels = list(set(fids_labels))
        if all(label == "UNKNOWN" for label in fids_labels):
            subflow_labels.append("UNKNOWN")
        elif all(label == "BENIGN" or label == "UNKNOWN" for label in fids_labels):
            subflow_labels.append("BENIGN")
        else:
            subflow_labels.append("MALICIOUS")
    return subflow_labels


def main():
    # '''Main function performs all data loading, parsing, and saving'''
    # # parse arguments
    # if len(sys.argv) < 7:
    #     sys.exit("Usage: python3 {} [pcap_file] [labels_csv] [FFT bins] "
    #              "[num pkt thresh] [output_file] [do_subflows TRUE|FALSE]".format(sys.argv[0]))
    # pcap_file, labels_csv, output_file = sys.argv[1], sys.argv[2], sys.argv[5]
    # fft_bins, num_pkt_thresh = int(sys.argv[3]), int(sys.argv[4])
    # do_subflows = sys.argv[6].upper() == "TRUE"

    pcap_file = '../data/test.pcap'
    labels_csv = '../data/test.csv'
    output_file = pcap_file + '_subflows.dat'
    fft_bins = 10
    num_pkt_thresh = 2
    do_subflows = True
    # process data

    flow_features, flow_labels, subflow_features, subflow_labels = parse_dataset(
        pcap_file, labels_csv, fft_bins, num_pkt_thresh, do_subflows)

    # save results
    with open(output_file, 'wb') as output:
        pickle.dump((flow_features, flow_labels, subflow_features, subflow_labels), output)


if __name__ == "__main__":
    main()
