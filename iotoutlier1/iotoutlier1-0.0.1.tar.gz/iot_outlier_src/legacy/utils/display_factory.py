""" Display

"""
# Authors: kun.bj@outlook.com
#
# License: xxx
# 1. system and built-in libraries
import os
from collections import Counter
from copy import deepcopy

# 2. thrid-part libraries
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import roc_curve

# 3. local libraries
from utils.tool import pprint
from utils.tool import transform_params_to_str


class DisplayFactory:

    def __init__(self, dataset_dict='', params={}):
        self.dataset_dict = dataset_dict
        self.params = params
        self.params['dataset_dict'] = dataset_dict  # save all results:  # {sub_name: SingleDataset, ... }

    def run(self):

        for i, (sub_ds_name, sd_inst) in enumerate(self.dataset_dict.items()):  # {sub_name: SingleDataset, ... }
            ds_dict = sd_inst.dataset_dict  # SingleDataset
            pprint(ds_dict, name=f'{i+1}/{len(self.dataset_dict.items())}, DisplayFactory.sd_inst.dataset_dict')

            sampling_rate = ds_dict['samp_dict']['sampling_rate']
            q_sampling_rate = ds_dict['samp_dict']['q_sampling_rate']
            detector_name = self.params['detector_name']
            dataset_name = self.params['dataset_name']  # 'CICIDS2017', 'SMTV'
            expt_name = self.params['expt_name']  # 'INDV', 'AGMT'
            srcIP = sd_inst.srcIP
            gs_flg = self.params['gs_flg']
            X_train, y_train, X_test, y_test = ds_dict['samp_dict']['data']

            fig_name = os.path.join(self.params['opt_dir'],
                                    os.path.dirname(sd_inst.dataset_dict['iat_dict']['feat_file']),
                                    f'sampling_{q_sampling_rate}_{sampling_rate}/')
            fig_name += f'expt_{expt_name}-{detector_name}-gs_{gs_flg}'

            if len(fig_name) > 300:  # avoid fig_name too long
                fig_name = fig_name[:300]

            output_file = f'{fig_name}.pdf'
            self._plot_roc_auc(sd_inst, output_file=output_file,
                               title=f'{detector_name}, gs:{gs_flg}, expt: {expt_name}, srcIP:{srcIP}, '
                                     f'data: {dataset_name}, train:({dict(Counter(y_train))}), test:({dict(Counter(y_test))})')

        detector_name = self.params['detector_name']
        gs_flg = self.params['gs_flg']
        output_file = os.path.join(self.params['opt_dir'], self.params['dataset_name'], self.params['expt_name'],
                                   f'{detector_name}-gs_flg:{gs_flg}-results.txt')
        self.save_results(self.dataset_dict, output_file=output_file)

    def save_results(self, dataset_dict, output_file='results.txt'):
        data_lst = []
        dataset_name = self.params['dataset_name']
        detector_name = self.params['detector_name']
        gs_flg = self.params['gs_flg']
        header = f'({dataset_name}|{detector_name}|{gs_flg})sub_ds_name,iat_auc(q_fixed_iat),fft_auc(q_fixed_iat),' \
                 f'stat_auc,samp_auc(best_q_sampling_rate)'
        for i, (sub_ds_name, sd_inst) in enumerate(dataset_dict.items()):  # {sub_name: SingleDataset, ... }
            tmp_lst = [sub_ds_name]  # [sub_ds_name, iat_auc, fft_auc, stat_auc, samp_auc]
            for j, (result_key, result_dict) in enumerate(sd_inst.dataset_dict.items()):
                auc = result_dict['result']['auc']
                if result_key == 'samp_dict':
                    q_sampling_rate_j = result_dict['q_sampling_rate']
                    auc = f'{auc:.4f}(q_samp={q_sampling_rate_j})'
                elif result_key == 'iat_dict':
                    q_iat = result_dict['q_fixed_iat']
                    auc = f'{auc:.4f}(q_iat={q_iat})'
                elif result_key == 'fft_dict':
                    q_iat = result_dict['q_fixed_iat']
                    auc = f'{auc:.4f}(q_iat={q_iat})'
                else:
                    auc = f'{auc:.4f}'
                print(f'feat_set: {result_key}, auc: {auc}')
                tmp_lst.append(auc)
            data_lst.append(','.join(tmp_lst))

        if not os.path.exists(os.path.dirname(output_file)):
            os.makedirs(os.path.dirname(output_file))
        with open(output_file, 'w') as out_hdl:
            out_hdl.write(header + '\n')
            for i, line in enumerate(data_lst):
                out_hdl.write(line + '\n')

    def _insert_newlines(self, data_str, step=40):
        """ format the title with fixed length

        :param data_str:
        :param step:
        :return:
        """
        return '\n'.join([data_str[i:i + step] for i in range(0, len(data_str), step)])

    def _plot_roc_auc(self, sd_inst, output_file='output_data/figures/roc_of_different_algorithms.pdf',
                      title='ROC'):
        """ plot roc and auc

        :param result_dict_lst:
        :param out_file:
        :param title:
        :return:
        """
        dataset_dict = sd_inst.dataset_dict
        detector_name = self.params['detector_name']
        # with plt.style.context(('ggplot')):
        fig, ax = plt.subplots()

        colors_lst = ['r', 'm', 'b', 'g', 'y', 'c', '#0072BD', '#A2142F', '#EDB120', 'k', '#D95319', '#4DBEEE',
                      'C1']  # add more color values: https://www.mathworks.com/help/matlab/ref/plot.html
        for idx, (key, result_dict) in enumerate(dataset_dict.items()):
            # colors_dict[feature_set_key] = {'AE': 'r', 'DT': 'm', 'PCA': 'C1', 'IF': 'b', 'OCSVM': 'g'}
            feature_set_key = result_dict['feat_set']
            value_dict = result_dict['result']
            y_true = value_dict['y_true']
            y_scores = value_dict['y_scores']
            fpr, tpr, thres = roc_curve(y_true=y_true, y_score=y_scores)
            # IMPORTANT: first argument is true values, second argument is predicted probabilities (i.e., y_scores)
            auc = value_dict['best_score_']
            print(f'auc: {metrics.auc(fpr, tpr)} == {auc} ?')  # for verify
            auc = f'{auc:.4f}'
            print(f'result of {detector_name}: {feature_set_key}, auc={auc}, fpr={fpr}, tpr={tpr}')
            # print(best_dict[feature_set_key]['best_score_'] == auc)
            if detector_name == 'PCA':
                lw = 3
            else:
                lw = 2

            if feature_set_key == 'iat_set':
                q_fixed_iat = result_dict['q_fixed_iat']
                bin_size = result_dict['bin_size']
                params_str = f'q_fixed_iat:{q_fixed_iat}, bin_size:{bin_size}\n'

            if feature_set_key == 'fft_set':
                q_fixed_iat = result_dict['q_fixed_iat']
                bin_size = result_dict['bin_size']
                params_str = f'q_fixed_iat:{q_fixed_iat}, bin_size:{bin_size}\n'

            if feature_set_key == 'stat_set':
                params_str = ''
            if feature_set_key == 'samp_set':
                q_sampling_rate = result_dict['q_sampling_rate']
                sampling_rate = result_dict['sampling_rate']
                sampling_rate = f'{sampling_rate:.4f}'
                params_str = f'q_samp:{q_sampling_rate}, samp_rate:{sampling_rate}\n'

            params_str += transform_params_to_str(deepcopy(value_dict['best_params_']),
                                                  remove_lst=['means_init', 'verbose', 'random_state',
                                                              None, 'auto', 'quantile'],
                                                  param_limit=100)
            params_str = self._insert_newlines(str(params_str), step=40)
            feat_str = self._insert_newlines(f'{feature_set_key}. AUC:{auc}')
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
        plt.title(self._insert_newlines(title, step=50))
        # plt.subplots_adjust(bottom=0.25, top=0.75)
        print(f'ROC:{output_file}')
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        plt.savefig(output_file)  # should use before plt.show()
        plt.show()

        return output_file

    def _plot_data(self, x, y):
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
