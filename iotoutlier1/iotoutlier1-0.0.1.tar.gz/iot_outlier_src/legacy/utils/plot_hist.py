""" plot data distribution

"""
# Authors: kun.bj@outlook.com
#
# License: xxx
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from data_process import Dataset
from utils.tool import stat_data


def plot_histgram(data, bins=100, title=''):
    # data = np.histogram(data, bins=bins)

    plt.hist(data, bins=bins)  # arguments are passed to np.histogram
    plt.title(f"{title}")
    plt.ylabel('Counts')
    plt.xlabel('Number of packets in each flow')
    # plt.xlim(0,15)
    plt.show()


def main():
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    # sampling_lst = [4.5899, 6.7859, 7.2307, 5.7866, 3.5814]         #q=0.9
    # sampling_lst = [2.0662943522135417e-07, 1.6829546760110295e-07, 1.7881393432617188e-07,
    #                 1.430511474609375e-07, 1.6829546760110295e-07]  # q=0.1
    sampling_lst = [2.702077229817708e-07, 1.8232008990119484e-07,
                    1.9371509552001953e-07, 2.026557922363281e-07, 2.384185791015625e-07]  # q=0.3
    # sampling_lst = [0.0034731308619181315, 2.384185791015625e-07, 2.9355287551879883e-06,
    #                 0.0015740692615509033, 0.0018327656914206112]  # q=0.5
    # sampling_lst = [ 0.013366915384928386,  1.2888627893784468e-05,  4.0084123611450195e-06,
    #                   0.004426524639129641, 0.005506066715016085]     # q=0.6
    rescale_flg = False
    bins = 20
    data_aug = False
    for i, srcIP in enumerate(srcIP_lst):
        print(f'\ni: {i}, srcIP: {srcIP}')

        plt.subplot(2, 3, i + 1)  # plt.subplot(131)
        if data_aug:
            input_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-IAT.dat_augmented.dat'
        else:
            input_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-IAT.dat'
            # input_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-SampBaseline-number_10.dat'
            # input_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-SampBaseline-interval_0.1.dat'
            input_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-SampBaseline-rate_{sampling_lst[i]}.dat'

        print(f'input_file: {input_file}')
        data_inst = Dataset(input_file=input_file)
        print(f'Counter(data_inst.labels): {Counter(data_inst.labels)}')

        individual_flg = False
        if individual_flg:
            anomaly_IAT_len_arr = []
            normal_IAT_len_arr = []
            other_IAT_len_arr = []
            for i, iat in enumerate(data_inst.features):
                if data_inst.labels[i] not in ['NORMAL', 'BENIGN', 0, None, 'None']:
                    anomaly_IAT_len_arr.append(len(iat))
                elif data_inst.labels[i] in ['NORMAL', 'BENIGN']:
                    normal_IAT_len_arr.append(len(iat))
                else:
                    other_IAT_len_arr.append(len(iat))

            anomaly_IATs_lens_flg = True  # only show attack IATs dimensions distribution
            norm_IATs_lens_flg = True
            if anomaly_IATs_lens_flg:
                IAT_len_arr = anomaly_IAT_len_arr
                title = f'srcIP:{srcIP},\nmin:{min(IAT_len_arr)}, max:{max(IAT_len_arr)},\ntotal anomaly: {len(IAT_len_arr)}'
            elif norm_IATs_lens_flg:
                IAT_len_arr = normal_IAT_len_arr
                title = f'srcIP:{srcIP},\nmin:{min(IAT_len_arr)}, max:{max(IAT_len_arr)},\ntotal normal: {len(IAT_len_arr)}'
            else:
                IAT_len_arr = other_IAT_len_arr
                title = f'srcIP:{srcIP},\nmin:{min(IAT_len_arr)}, max:{max(IAT_len_arr)},\ntotal other: {len(IAT_len_arr)}'
        else:
            IAT_len_arr = [len(iat) for i, iat in enumerate(data_inst.features) if
                           data_inst.labels[i] not in [None, 'None']]
            title = f'srcIP:{srcIP},\nmin:{min(IAT_len_arr)}, max:{max(IAT_len_arr)},\ntotal: {len(IAT_len_arr)}' + ',\nfft_bins: {fft_bins}, q: {quant}'
        print(f'{sorted(Counter(IAT_len_arr).items(), key=lambda item: item[0])}')
        quant = 0.9
        fft_bins = int(np.quantile(IAT_len_arr, q=quant))
        print(f'fft_bins: {fft_bins}, quantile = {quant}')
        if not individual_flg:
            title = title.format(fft_bins=fft_bins, quant=quant)
        stat_data(np.array(IAT_len_arr).reshape(-1, 1))
        if rescale_flg:
            IAT_len_arr = [value for value in IAT_len_arr if value < 25]
            bins = 30
        # plot_histgram(IAT_len_arr, title=f'srcIP:{srcIP}, quantile:{quant}, length_IAT:{thres}')
        plt.hist(IAT_len_arr, bins=bins)  # arguments are passed to np.histogram

        hist, bin_edges = np.histogram(IAT_len_arr, bins=bins)
        print(f'hist:{hist},\nbin_edges:{bin_edges}')
        max_idx = np.argmax(hist)
        if max_idx - 1 >= 0:
            max_range = f'[{int(bin_edges[max_idx-1])}, {int(bin_edges[max_idx])}]'
        else:
            max_range = f'[0, {int(bin_edges[max_idx])}]'
        min_idx = np.argmin(hist)
        if min_idx - 1 >= 0:
            min_range = f'[{int(bin_edges[min_idx-1])}, {int(bin_edges[min_idx])}]'
        else:
            min_range = f'[0, {int(bin_edges[min_idx])}]'

        # title = f'srcIP:{srcIP},\nmax:{max(hist)} in {max_range},' \
        #         f'\nmin:{min(hist)} in {min_range}'
        plt.title(f"{title}")
        plt.ylabel('Counts')
        # plt.xlabel('Number of packets in each flow')
        plt.xlabel('Dimension of new_features')
    plt.show()


if __name__ == '__main__':
    main()
