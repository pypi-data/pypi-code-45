"""Obtain distribution data

"""
# kun.bj@outlook.com
#
# License: xxx
import os
import sys

sys.path.append(os.getcwd())  # for Slurm. Because Slurm cannot find the project
sys.path.append('..')
print(f'sys.path: {sys.path}')

from data_process import Dataset
from utils.tool import execute_time, dump_data


@execute_time
def obtain_data_dist(input_file, output_file=''):
    data_inst = Dataset(input_file)
    # IATlen_arr = [len(iat) for iat in data_inst.features]  # IAT = data_inst.features
    value_lst = [len(value) for value in data_inst.features]  #
    dump_data(data=value_lst, output_file=output_file)

    return value_lst


def main():
    input_dir = 'input_data/CICIDS2017'
    output_dir = 'output_data'
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    for i, srcIP in enumerate(srcIP_lst):
        print(f'\ni:{i}')
        input_file = f'{input_dir}/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-IAT.dat'
        output_file = f'{output_dir}/{input_file}-flow_len.dat'
        value_lst = obtain_data_dist(input_file, output_file=output_file)
        print(f'len(value_lst): {len(value_lst)}')


if __name__ == '__main__':
    main()
