""" useful tools

"""
# Authors: kun.bj@outlook.com
#
# License: xxx
import os
import pickle
import subprocess
import time
from collections import OrderedDict
from copy import deepcopy
from datetime import datetime
from functools import wraps

import numpy as np
import pandas as pd


def stat_data(data=None, name='data'):
    #
    # import inspect
    # a= inspect.signature(stat_data)

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 100)
    pd.set_option('display.float_format', lambda x: '%.3f' % x)  # without scientific notation

    columns = ['col_' + str(i) for i in range(data.shape[1])]
    dataset = pd.DataFrame(data=data, index=range(data.shape[0]), columns=columns)
    print(f'{name}.shape: {data.shape}')
    print(dataset.describe())
    print(dataset.info(verbose=True))


def _pprint(params, offset=0, printer=repr, sorted_flg=False):
    """Pretty print the dictionary 'params'

    Parameters
    ----------
    params : dict
        The dictionary to pretty print

    offset : int
        The offset in characters to add at the begin of each line.

    printer : callable
        The function to convert entries to strings, typically
        the builtin str or repr

    """
    # Do a multi-line justified repr:
    options = np.get_printoptions()
    np.set_printoptions(precision=5, threshold=64, edgeitems=2)
    params_list = list()
    this_line_length = offset
    line_sep = ',\n' + (1 + offset // 2) * ' '
    if sorted_flg:
        items = sorted(params.items())
    else:
        items = params.items()
    for i, (k, v) in enumerate(items):
        if type(v) is float:
            # use str for representing floating point numbers
            # this way we get consistent representation across
            # architectures and versions.
            this_repr = '%s=%s' % (k, str(v))
        else:
            # use repr of the rest
            this_repr = '%s=%s' % (k, printer(v))
        if len(this_repr) > 500:
            this_repr = this_repr[:300] + '...' + this_repr[-100:]
        if i > 0:
            if (this_line_length + len(this_repr) >= 75 or '\n' in this_repr):
                params_list.append(line_sep)
                this_line_length = len(line_sep)
            else:
                params_list.append(', ')
                this_line_length += 2
        else:  # i == 0
            params_list.append(' ')
            this_line_length += 2

        params_list.append(this_repr)
        this_line_length += len(this_repr)

    np.set_printoptions(**options)
    lines = ''.join(params_list)
    # Strip trailing space to avoid nightmare in doctests
    lines = '\n'.join(l.rstrip(' ') for l in lines.split('\n'))
    return lines


def pprint(params_dict=OrderedDict(), name='func_name', verbose=True):
    print(f'{name}\'s parameters: ')
    params_str = _pprint(params_dict, sorted_flg=False)
    print(f'{params_str}')


def check_n_generate_path(file_path, overwrite=True):
    path_dir = os.path.dirname(file_path)
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)

    if os.path.exists(file_path):
        if overwrite:
            os.remove(file_path)

    return file_path


def execute_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        st = datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
        print(f'\'{func.__name__}()\' starts at {st}')
        result = func(*args, **kwargs)
        end = time.time()
        ed = datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
        tot_time = (end - start) / 60
        tot_time = float(f'{tot_time:.4f}')
        print(f'\'{func.__name__}()\' ends at {ed}. It takes {tot_time} mins')
        return result

    return wrapper


def dump_data(data, output_file='', verbose=True):
    if verbose:
        funcparams_dict = {'len(data)': len(data), 'output_file': output_file}
        pprint(funcparams_dict, name=dump_data.__name__)

    check_n_generate_path(output_file, overwrite=True)

    # # save results
    with open(output_file, 'wb') as out_hdl:
        pickle.dump(data, out_hdl)

    return output_file


def check_value():
    pass


def remove_redundant_flows(input_file='labels_csv', output_file='', verbose=True):
    """ only keep the given srcIP or srcIPs, and reduce file size

    :param input_file: labels_csv
    :param output_file: five_tuple + labels
    :return:
    """
    if verbose:
        funcparams_dict = {'input_file': input_file, 'output_file': output_file,
                           'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=remove_redundant_flows.__name__)

    assert os.path.exists(input_file)
    assert output_file == '', f'output_file is {output_file}, please check and retry'
    check_n_generate_path(file_path=output_file, overwrite=True)

    df = pd.read_csv(input_file)
    cols_name = list(df.columns)  # 'Source IP'
    five_tuple_labels = [cols_name[2], cols_name[3], cols_name[4], cols_name[5], cols_name[6],
                         cols_name[-1]]  # five_tuple, labels
    print(f'five_tuple_labels:{five_tuple_labels}')

    df = df[five_tuple_labels]
    print(f'before removing redundant five tuples: {len(df)}')
    # dropping duplicate values
    df.drop_duplicates(keep=False, inplace=True)
    print(f'after removing redundant five tuples: {len(df)}')

    df.to_csv(output_file)

    return output_file


def transform_params_to_str(data_dict,
                            remove_lst=['verbose', 'random_state', 'means_init', None, 'auto', 'quantile'],
                            param_limit=50):
    # param_limit = 50  # # limit the length of the params string, which is used for file name

    params_dict = deepcopy(data_dict)
    params_str = ''
    for i, (key, value) in enumerate(params_dict.items()):
        if key not in remove_lst and value not in remove_lst:
            if type(value) == float or type(value) == np.float64:
                value = f'{value:.4f}'
            params_str += f'{key}:{value}, '
    if len(params_str) > param_limit:  # limit the length of the output_file name
        params_str = params_str[:param_limit]

    return params_str


def get_file_path(ipt_dir='', **kwargs):
    file_path = ipt_dir
    for i, (key, value) in enumerate(kwargs.items()):
        file_path = os.path.join(file_path, value)

    return file_path


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


def merge_labels(label_file_lst=[], mrg_label_path=''):
    if os.path.exists(mrg_label_path):
        os.remove(mrg_label_path)

    if not os.path.exists(os.path.dirname(mrg_label_path)):
        os.makedirs(os.path.dirname(mrg_label_path))
    # combine all label files in the list
    # combined_csv = pd.concat([pd.read_csv(f, header=None, usecols=[3,6]) for f in label_file_lst])
    result_lst = []
    for i, f in enumerate(label_file_lst):
        if i == 0:
            result_lst.append(pd.read_csv(f))
        else:
            result_lst.append(pd.read_csv(f, skiprows=0))
    combined_csv = pd.concat(result_lst)
    # export to csv
    print(f'{mrg_label_path}')
    combined_csv.to_csv(mrg_label_path, index=False, encoding='utf-8-sig')


def generate_label(pcap_file, label='Normal', num_pkt_thresh=2):
    # pcap_file = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/merged_normal.pcap'  # for testing
    flows = _load_pcap_to_flows(pcap_file, num_pkt_thresh)  # get all flows which at least has more than 2 packets
    # fids = [[fid, label] for fid, _, _ in flows]
    label_file = os.path.splitext(pcap_file)[0] + '.csv'
    if os.path.exists(label_file):
        os.remove(label_file)

    # pd.DataFrame(fids).to_csv(label_file)
    with open(label_file, 'w') as out_hdl:
        header = [" Source IP", " Destination IP", " Source Port", " Destination Port", " Protocol", " Label"]
        out_hdl.write(",".join(header) + '\n')
        for i, (fid, _, _) in enumerate(flows):
            line_lst = [str(v) for v in fid]
            line_lst.append(str(label))
            out_hdl.write(','.join(line_lst) + '\n')

    return label_file
