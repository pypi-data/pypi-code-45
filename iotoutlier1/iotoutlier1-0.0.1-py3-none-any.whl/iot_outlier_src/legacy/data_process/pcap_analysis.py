"""Obtain features (IAT and baseline) from pcap

"""
# kun.bj@outlook.com
#
# License: xxx
import os
import subprocess
import sys

from data_process import _load_pcap_to_flows
from data_process import keep_ips_in_pcap

sys.path.append(os.getcwd())  # for Slurm. Because Slurm cannot find the project


def merge_pcaps(pcap_file_lst=[], mrg_pcap_path=''):
    if os.path.exists(mrg_pcap_path):
        os.remove(mrg_pcap_path)
    if not os.path.exists(os.path.dirname(mrg_pcap_path)):
        os.makedirs(os.path.dirname(mrg_pcap_path))
    cmd = f"mergecap -w {mrg_pcap_path} " + ' '.join(pcap_file_lst)
    print(f'{cmd}')
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
    except Exception as e:
        print(f'{e}, {result}')
        return -1


def main_SMTV():  # smart-tv

    pcap_file = 'input_data/demo_data/srcIP_test.pcap'
    pcap_file = 'input_data/smart-tv-roku-data/raw_pcap/src_10.42.0.119.pcap'
    flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh=2)  # get all flows which at least has more than 2 packets
    print(f'num. of flows: {len(flows)}')

    pcap_file_lst = []
    ipt_dir = 'input_data/smart-tv-roku-data/raw_pcap/pcaps'
    for i, pcap in enumerate(os.listdir(ipt_dir)):
        if not pcap.endswith('.pcap'):
            print(f'i:{i+1}, pcap:{pcap}')
            continue
        pcap = os.path.join(ipt_dir, pcap)
        print(f'i:{i+1}, pcap:{pcap}')
        pcap_file_lst.append(pcap)

    mrg_pcap_path = os.path.join(os.path.dirname(ipt_dir), 'all.pcap')
    merge_pcaps(pcap_file_lst, mrg_pcap_path=mrg_pcap_path)

    src_lst = ['10.42.0.119', '10.42.0.120']
    for i, src in enumerate(src_lst):
        pcap_file = os.path.join(os.path.dirname(ipt_dir), f'src_{src}.pcap')
        print(f'pcap_file: {pcap_file}')
        keep_ips_in_pcap(input_file=mrg_pcap_path, output_file=pcap_file, kept_ips=[src])

        flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh=2)  # get all flows which at least has more than 2 packets
        print(f'num. of flows: {len(flows)}')
        # labels = _load_labels_and_label_flows(labels_csv, features=[(fid, _) for fid, _, _ in flows])


if __name__ == '__main__':
    main_SMTV()
