"""
    Purpose:
        visualize the results.
"""
import datetime
import time
from collections import OrderedDict

import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn import metrics
from sklearn.metrics import roc_curve

rcParams.update({'figure.autolayout': True})


def insert_newlines(data_str, step=45):
    return '\n'.join(data_str[i:i + step] for i in range(0, len(data_str), step))


def plot_roc(roc_dicts_lst, out_file='output_data/figures/roc_of_different_algorithms.pdf', title='ROC'):
    """

    :param roc_list: [[key, roc_dict], [key, roc_dict], ... ]
    :param out_file:
    :param title:
    :return:
    """
    # with plt.style.context(('ggplot')):
    fig, ax = plt.subplots()

    colors_lst = ['r', 'm', 'b', 'g', 'y', 'c', '#0072BD', '#A2142F', '#EDB120', 'k', '#D95319', '#4DBEEE',
                  'C1']  # add more color values: https://www.mathworks.com/help/matlab/ref/plot.html
    required_colors_num = len(roc_dicts_lst) * len(roc_dicts_lst[0][-1])  # roc_dicts_list[0] = [key, roc_dict]
    if len(colors_lst) < required_colors_num:
        print(
            f'the number of colors we has ({len(colors_lst)}) does not meet the required number of colors (required_colors_num).')
    else:
        print(f'required colors number ({required_colors_num}) <= colors number ({len(colors_lst)}).')

    # colors_dict['ocsvm'.upper()] =
    for idx, (feature_set_key, roc_dict) in enumerate(roc_dicts_lst):
        # colors_dict[feature_set_key] = {'AE': 'r', 'DT': 'm', 'PCA': 'C1', 'IF': 'b', 'OCSVM': 'g'}
        for i, (key, value_dict) in enumerate(roc_dict.items()):
            key = key.upper()
            y_true = value_dict['y_true']
            y_scores = value_dict['y_scores']
            fpr, tpr, thres = roc_curve(y_true=y_true, y_score=y_scores)
            # IMPORTANT: first argument is true values, second argument is predicted probabilities (i.e., y_scores)
            # auc = "%.5f" % metrics.auc(fpr, tpr)
            auc = f'{metrics.auc(fpr, tpr):.4f}'
            print(f'key={key}:{feature_set_key}, auc={auc}, fpr={fpr}, tpr={tpr}')
            if key == 'PCA':
                lw = 3
            else:
                lw = 2

            ax.plot(fpr, tpr, colors_lst.pop(0), label=f'{feature_set_key}. AUC:{auc}', lw=lw, alpha=1, linestyle='-')

    ax.plot([0, 1], [0, 1], 'k--', label='', alpha=0.9)
    plt.xlim([0.0, 1.0])
    plt.ylim([0., 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='lower right')

    title = insert_newlines(title)
    plt.title(title)

    # sub_dir = os.path.split(input_file)[0]
    # output_pre_path = os.path.split(input_file)[-1].split('.')[0]
    # out_file = os.path.join(sub_dir, output_pre_path + '_ROC.pdf')
    print(f'ROC:{out_file}')
    plt.savefig(out_file)  # should use before plt.show()

    plt.show()


def plot_auc_and_strength_of_outiler(auc_dicts_lst, out_file='output_data/figures/auc_on_different_strengths.pdf',
                                     title='AUC'):
    """

    :param auc_dicts_lst:
    :param out_file:
    :param title:
    :return:
    """
    # with plt.style.context(('ggplot')):
    fig, ax = plt.subplots()

    colors_lst = ['r', 'b', 'g', 'm', 'y', 'c', '#0072BD', '#A2142F', '#EDB120', 'k', '#D95319', '#4DBEEE',
                  'C1']  # add more color values: https://www.mathworks.com/help/matlab/ref/plot.html
    required_colors_num = len(auc_dicts_lst) * len(auc_dicts_lst[0][-1])  # auc_dicts_lst[0] = [key, roc_dict]
    if len(colors_lst) < required_colors_num:
        print(
            f'the number of colors we has ({len(colors_lst)}) does not meet the required number of colors (required_colors_num).')
    else:
        print(f'required colors number ({required_colors_num}) <= colors number ({len(colors_lst)}).')

    strengths_lst = []
    aucs_dict = OrderedDict()
    best_algorithm_name = ''
    for idx, (strength_key, auc_dict) in enumerate(auc_dicts_lst):
        # colors_dict[feature_set_key] = {'AE': 'r', 'DT': 'm', 'PCA': 'C1', 'IF': 'b', 'OCSVM': 'g'}
        for i, (feature_set_key, value_dict) in enumerate(auc_dict.items()):
            # feature_set_key = feature_set_key.upper()
            print(f'key={feature_set_key}, strength={strength_key}, auc={value_dict}')
            k, v = value_dict.popitem()
            if feature_set_key not in aucs_dict.keys():
                best_algorithm_name = k
                aucs_dict[feature_set_key] = [v]  #
            else:
                aucs_dict[feature_set_key].append(v)
                # aucs_dict = {'prop_set':[0.8, 0.9, ...], 'trad_set':[0.7, 0.9, 0.6, ...]}
        strengths_lst.append(strength_key)

    marker = ['o', 's', 'D', '^', 'v' '*', '.', ',']
    linestyle = ['None', '-', '--', ':', '-.']
    for idx, (feature_set_key, value_lst) in enumerate(aucs_dict.items()):
        # ax.plot(strengths_lst, value_lst, colors_lst.pop(0), label=f'{feature_set_key} : {strength_key}', lw=lw, alpha=1, linestyle='--')
        plt.plot(strengths_lst, value_lst, color=colors_lst.pop(0), marker=f'{marker[idx]}', linestyle='-',
                 label=f'{best_algorithm_name}:{feature_set_key}', alpha=1)  # fmt = '[color][marker][line]'
    plt.xlim([0.0, 1.0])
    plt.ylim([0., 1.05])
    plt.xlabel('Strength of outiler')
    plt.ylabel('AUC')
    plt.legend(loc='lower right')
    plt.title(title)

    # sub_dir = os.path.split(input_file)[0]
    # output_pre_path = os.path.split(input_file)[-1].split('.')[0]
    # out_file = os.path.join(sub_dir, output_pre_path + '_ROC.pdf')
    print(f'AUC:{out_file}')
    plt.savefig(out_file)  # should use before plt.show()

    plt.show()


# def show_data_2(data1, data2, x_label='epochs', y_label='mean loss', title=''):
#     plt.figure()
#     plt.plot(data1, 'r', alpha=0.5, label='train_loss in each epoch')
#     plt.plot(data2, 'b', alpha=0.5, label='val loss in each epoch')
#     # plt.plot(new_decision_data[:, 2], 'g', alpha=0.5, label='D_G_fake')
#     plt.legend(loc='upper right')
#     plt.xlabel(x_label)
#     plt.ylabel(y_label)
#     plt.title(title)
#     plt.show()


def print_time(func):
    def function_wrapper(*args, **kwargs):
        # print("Before calling " + func.__name__)
        start_time = time.time()
        st = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
        func(*args, kwargs['input_file'], kwargs['file_type'], kwargs['output_file'], kwargs['num_pkts_thres'])
        # print("After calling " + func.__name__)
        end_time = time.time()
        et = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f'It begins at {st}, ends at {et} and takes {end_time-start_time} s')

    return function_wrapper
