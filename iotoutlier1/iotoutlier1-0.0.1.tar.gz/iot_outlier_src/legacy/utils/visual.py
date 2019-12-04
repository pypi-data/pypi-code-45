import os
from copy import deepcopy

import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import roc_curve

from utils.tool import transform_params_to_str


def insert_newlines(data_str, step=35):
    """ format the title with fixed length

    :param data_str:
    :param step:
    :return:
    """
    return '\n'.join(data_str[i:i + step] for i in range(0, len(data_str), step))


def plot_roc_auc(result_dict_lst, output_file='output_data/figures/roc_of_different_algorithms.pdf',
                 title='ROC'):
    """ plot roc and auc

    :param result_dict_lst:
    :param out_file:
    :param title:
    :return:
    """
    # with plt.style.context(('ggplot')):
    fig, ax = plt.subplots()

    colors_lst = ['r', 'm', 'b', 'g', 'y', 'c', '#0072BD', '#A2142F', '#EDB120', 'k', '#D95319', '#4DBEEE',
                  'C1']  # add more color values: https://www.mathworks.com/help/matlab/ref/plot.html
    for idx, (feature_set_key, result_dict) in enumerate(result_dict_lst.items()):
        # colors_dict[feature_set_key] = {'AE': 'r', 'DT': 'm', 'PCA': 'C1', 'IF': 'b', 'OCSVM': 'g'}
        for i, (detector_key, value_dict) in enumerate(result_dict.items()):
            detector_key = detector_key.upper()
            y_true = value_dict['y_true']
            y_scores = value_dict['y_scores']
            fpr, tpr, thres = roc_curve(y_true=y_true, y_score=y_scores)
            # IMPORTANT: first argument is true values, second argument is predicted probabilities (i.e., y_scores)
            auc = value_dict['best_score_']
            print(f'auc: {metrics.auc(fpr, tpr)} == {auc} ?')  # for verify
            auc = f'{auc:.4f}'
            print(f'result of {detector_key}: {feature_set_key}, auc={auc}, fpr={fpr}, tpr={tpr}')
            # print(best_dict[feature_set_key]['best_score_'] == auc)
            if detector_key == 'PCA':
                lw = 3
            else:
                lw = 2
            params_str = transform_params_to_str(deepcopy(value_dict['best_params_']),
                                                 remove_lst=['means_init', 'verbose', 'random_state',
                                                             None, 'auto', 'quantile'],
                                                 param_limit=100)
            params_str = insert_newlines(str(params_str))
            feat_str = insert_newlines(f'{feature_set_key}. AUC:{auc}')
            ax.plot(fpr, tpr, colors_lst.pop(0), label=f'{feat_str},\n {params_str}', lw=lw,
                    alpha=0.9,
                    linestyle='-')
            ax.text(2, 7, 'this is\nyet another test',
                    rotation=45,
                    horizontalalignment='center',
                    verticalalignment='top',
                    multialignment='center')

    ax.plot([0, 1], [0, 1], 'k--', label='', alpha=0.9)
    plt.xlim([0.0, 1.0])
    plt.ylim([0., 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='lower right', framealpha=0.1)

    if len(title) > 300:
        title = title[:300]
    plt.title(insert_newlines(title, step=50))
    # plt.subplots_adjust(bottom=0.25, top=0.75)
    print(f'ROC:{output_file}')
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    plt.savefig(output_file)  # should use before plt.show()
    plt.show()

    return output_file


def plot_data(x, y):
    # beta = 0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 0.999:
    # beta = 0.1, num_clusters = 3962,
    # beta = 0.2, num_clusters = 3961,
    # beta = 0.4, num_clusters = 3952,
    # beta = 0.6, num_clusters = 3943,
    # beta = 0.8, num_clusters = 3939,
    # beta = 0.9, num_clusters = 3935,
    # beta = 0.999, num_clusters = 3911,

    # with plt.style.context(('ggplot')):
    fig, ax = plt.subplots()
    ax.plot(x, y, '*-',
            alpha=0.9)

    # ax.plot([0, 1], [0, 1], 'k--', label='', alpha=0.9)
    plt.xlim([0.0, 1.0])
    # plt.ylim([0., 1.05])
    plt.xlabel('Beta')
    plt.ylabel('Num_clusters')
    plt.legend(loc='lower right')
    plt.title('QuickShift_PP: k and beta')
    plt.show()


if __name__ == '__main__':
    beta_lst = [0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 0.999]
    num_clusters_lst = [3962, 3961, 3952, 3943, 3939, 3935, 3911]
    plot_data(x=beta_lst, y=num_clusters_lst)
