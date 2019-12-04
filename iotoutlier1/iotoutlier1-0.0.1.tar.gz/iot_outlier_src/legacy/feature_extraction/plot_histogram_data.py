import pickle
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from legacy.utils.dataset import stat_data


#
# def load_pickle_data(input_file):
#     # save results
#     with open(input_file, 'rb') as in_hdl:
#         IATs = pickle.load(in_hdl)
#
#     return IATs


def load_pickled_data(input_file=''):
    """ Especially for loading multi-objects stored in a file.

    :param input_file:
    :return:
    """

    fids = []
    features = []
    labels = []
    with open(input_file, 'rb') as in_hdl:
        while True:
            try:
                fids_, features_, labels_ = pickle.load(in_hdl)
                fids.extend(fids_)
                features.extend(features_)
                labels.extend(labels_)
            except EOFError:
                break
    return fids, features, labels


# Counter(
#   {2: 2099, 4: 1173, 3: 352, 6: 247, 8: 237, 9: 174, 5: 153, 10: 93, 16: 87, 11: 76, 21: 69, 14: 67, 15: 66,
#    13: 60, 12: 59, 7: 50, 18: 49, 20: 49, 39: 49, 19: 35, 17: 29, 22: 26, 25: 25, 23: 22, 24: 22, 26: 18,
#    27: 14, 34: 11, 37: 10, 28: 9, 41: 9, 30: 8, 35: 7, 31: 7, 40: 5, 29: 5, 44: 5, 47: 5, 42: 4, 33: 4,
#    43: 4, 51: 4, 63: 3, 64: 3, 67: 3, 116: 3, 45: 3, 212: 3, 32: 3, 38: 3, 49: 3, 36: 3, 48: 3, 54: 3,
#    58: 2, 57: 2, 61: 2, 97: 2, 50: 2, 117: 2, 112: 2, 118: 2, 74: 2, 262: 2, 52: 2, 60: 2, 173: 2, 110: 2,
#    55: 2, 62: 1, 65: 1, 186: 1, 961: 1, 5248: 1, 399: 1, 132: 1, 111: 1, 281: 1, 91: 1, 154: 1, 157: 1,
#    80: 1, 1071: 1, 140: 1, 115: 1, 71: 1, 188: 1, 53: 1, 73: 1, 541: 1, 423: 1, 348: 1, 872: 1, 606: 1,
#    100: 1, 239: 1, 1005: 1, 121: 1, 109: 1, 536: 1, 79: 1, 479: 1, 296: 1, 84: 1, 108: 1, 89: 1, 95: 1,
#    731: 1, 2460: 1, 214: 1, 557: 1, 92: 1, 574: 1, 56: 1, 264: 1, 164: 1, 842: 1, 6343: 1, 70: 1, 992: 1,
#    254: 1, 868: 1, 4097: 1, 789: 1, 460: 1, 148: 1, 127: 1, 153: 1, 69: 1})


def plot_histgram(data, bins=100, title=''):
    # data = np.histogram(data, bins=bins)

    plt.hist(data, bins=bins)  # arguments are passed to np.histogram
    plt.title(f"{title}")
    plt.ylabel('Counts')
    plt.xlabel('Number of packets in each flow')
    # plt.xlim(0,15)
    plt.show()


if __name__ == '__main__':

    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    rescale_flg = False
    bins = 20
    base_set = 'Baseline'
    data_aug = False
    for i, srcIP in enumerate(srcIP_lst):
        plt.subplot(2, 3, i + 1)  # plt.subplot(131)

        if data_aug:
            input_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat_augmented.dat'
            # output_file = input_file+'_flows_len.dat'
            # _, IATs, _ = load_pickled_data(input_file)
            # input_file = output_file
            # IAT_len_arr = [len(v) for v in IATs]
            # with open(input_file, 'wb') as out_hdl:
            #     pickle.dump(IAT_len_arr, out_hdl)

        else:
            # input_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat'
            input_file = f'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_{base_set}_dimension_10.dat'

        output_file = input_file + '_flows_len.dat'
        _, IATs, _ = load_pickled_data(input_file)
        input_file = output_file
        IAT_len_arr = [len(v) for v in IATs]
        with open(input_file, 'wb') as out_hdl:
            pickle.dump(IAT_len_arr, out_hdl)

        print(f'input_file: {input_file}')
        # print(f'{sorted(Counter(IAT_len_arr))}')
        print(f'{sorted(Counter(IAT_len_arr).items(), key=lambda item: item[0])}')
        quant = 0.9
        thres = int(np.quantile(IAT_len_arr, q=quant))
        print(f'thres: {thres}, quantile = {quant}')
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
        title = f'srcIP:{srcIP},\nmin:{min(IAT_len_arr)}, max:{max(IAT_len_arr)}'
        plt.title(f"{title}")
        plt.ylabel('Counts')
        # plt.xlabel('Number of packets in each flow')
        plt.xlabel('Dimension of IATs')
    plt.show()
