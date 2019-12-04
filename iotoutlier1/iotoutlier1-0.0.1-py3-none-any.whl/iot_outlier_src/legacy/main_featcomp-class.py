""" Main function for feature set comparison.
    Measure metrics: ROC amd AUC

    1. best parameters using grid search
    2. rule of thumb

      # data_inst = Dataset(input_file=file)     # based on the Baseline  data
      # fft_bin = int(np.round(np.quantile([len(feat) for feat in data_inst.features], q=0.9)))

"""
# Authors: kun.bj@outlook.com
#
# License: xxx
import subprocess
from collections import OrderedDict, Counter
from copy import deepcopy

import pandas as pd

from _config import *
from data_process import keep_ips_in_pcap
from data_process import main_pcap2features, parse_dataset, \
    _load_pcap_to_flows, parse_dataset_smart_tv
from data_process import transform_iat_to_fixed_out, transform_samp_baseline_to_fixed_out
from legacy.experiment_class import IndividualExperiment
from utils.tool import pprint, execute_time, transform_params_to_str, dump_data
from utils.visual import plot_roc_auc


def conduct_comparison_experiment(detector_name='',
                                  experiment='',
                                  srcIP='',
                                  prop_feat='IAT',
                                  prop_file='',
                                  bparam_dict=OrderedDict(),
                                  ipt_dir='',
                                  opt_dir='',
                                  norm_method=None,
                                  gridsearch_flg=False,
                                  q_fixed_iat=0.9,
                                  random_state=42,
                                  verbose=True):
    """ Get comparison results on proposed set and baseline set

    :param detector_name:
    :param srcIP:
    :param pparam_dict:
    :param bparam_dict:
    :param norm_method:
    :param gridsearch_flg:
    :param q_fixed_IAT:
    :param random_state:
    :param verbose:
    :return:
    """
    if verbose:
        funcparams_dict = {
            'srcIP': srcIP,
            'detector_name': detector_name,
            'prop_feat': prop_feat,
            'prop_file': prop_file,
            'bparam_dict': bparam_dict,
            'ipt_dir': ipt_dir,
            'opt_dir': opt_dir,
            'q_fixed_iat': q_fixed_iat,
            'norm_method': norm_method,
            'gridsearch_flg': gridsearch_flg,
            'random_state': random_state,
            'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=conduct_comparison_experiment.__name__)

    # get results on pparam_dict and bparam_dict by the detector
    result_dict_dict = OrderedDict()  # store the dict results: {feat_set: results of the feat_set}
    fig_name = ''
    # fft_bin_dict = OrderedDict()
    # 1. obtain results (such as ROC and AUC) of IAT or FFT on pparam_dict
    fft_part = 'real'  # only for FFT: 'real' or 'real+imaginary'
    print('\n' + f'prop_file: {prop_file}, prop_feat: {prop_feat}')

    # 1.1) get the fixed size of IAT or FFT based on the given quantile (default 0.9)
    prop_file, fft_bin = transform_iat_to_fixed_out(input_file=prop_file, feat_set=prop_feat, quant=q_fixed_iat,
                                                    fft_part=fft_part, overwrite=True, verbose=verbose)

    # 1.2) get the results
    prop = IndividualExperiment(input_file=prop_file, feat_set=prop_feat, norm_method=norm_method,
                                random_state=random_state, verbose=verbose)
    result_dict = prop.run(detector_name=detector_name,
                           X_train=prop.X_train, y_train=prop.y_train,
                           X_test=prop.X_test, y_test=prop.y_test,
                           gridsearch_flg=gridsearch_flg)

    # 1.3) save the built detector to file
    params_str = transform_params_to_str(deepcopy(prop.detector.get_params()),
                                         remove_lst=['verbose', 'random_state', 'means_init', None, 'auto'])
    pmodel_file = f'{opt_dir}/{prop_file}_{detector_name}_{str(params_str)}.joblib'
    pmodel_file = prop.dump_model(prop.detector, model_file=pmodel_file)

    result_dict_dict[prop_feat] = result_dict  # store the result on prop_feat
    fig_name += f'{os.path.splitext(pmodel_file)[0]}_'

    for i, (base_feat, base_file) in enumerate(bparam_dict.items()):
        # 2. obtain results (such as ROC and AUC) of Baseline 2
        print('\n' + f'base_file: {base_file}, base_feat: {base_feat}')
        if 'SampBaseline-rate' in base_file:
            sampling_rate = base_file.split('SampBaseline-rate_')[-1]
        else:
            sampling_rate = None

        if base_feat != 'StatBaseline' or base_feat == 'SampBaseline':
            # 2.1) get the fixed size (fft_bin) for sampling baseline
            base_file = transform_samp_baseline_to_fixed_out(input_file=base_file, fft_bin=fft_bin,
                                                             # same with the IAT length
                                                             overwrite=True, verbose=verbose)
        # 2.2) get the results on bparam_dict
        base = IndividualExperiment(input_file=base_file, feat_set=base_feat,
                                    norm_method=norm_method,
                                    random_state=random_state, verbose=verbose)
        result_dict = base.run(detector_name=detector_name,
                               X_train=base.X_train, y_train=base.y_train,
                               X_test=base.X_test, y_test=base.y_test,
                               gridsearch_flg=gridsearch_flg)

        # 2.3) save the detector to file
        params_str = transform_params_to_str(deepcopy(base.detector.get_params()),
                                             remove_lst=['verbose', 'random_state', 'means_init', None, 'auto'])
        bmodel_file = f'{opt_dir}/{base_file}_{detector_name}_{str(params_str)}.joblib'
        bmodel_file = base.dump_model(base.detector, model_file=bmodel_file)
        result_dict_dict[base_feat] = result_dict  # store the result on samp_base_set
    # fig_name += f'{os.path.split(bmodel_file)[-1]}_{len(bparam_dict.items())}_'
    fig_name += f'-SampBaseline-rate_{sampling_rate}-feat_set:{prop_feat}-gridsearch:{gridsearch_flg}-{detector_name}'
    if prop_feat == 'FFT':
        fig_name += f'fft_part:{fft_part}'

    # 3 save all result in pdf
    if len(fig_name) > 300:  # avoid fig_name too long
        fig_name = fig_name[:300]
    # output_file = f'{opt_dir}/{fig_name}.pdf'
    output_file = f'{fig_name}.pdf'
    # plot_roc_auc(result_dict_dict, output_file=output_file,
    #              title=f'{detector_name}, srcIP:{srcIP}, gridsearch:{gridsearch_flg}')
    plot_roc_auc(result_dict_dict, output_file=output_file,
                 title=f'{detector_name}, gridsearch:{gridsearch_flg}, experiment: {experiment}, srcIP:{srcIP}, '
                       f'train:({Counter(prop.y_train)}), test:({Counter(prop.y_test)})')

    return result_dict_dict


@execute_time
def main_experiment(experiment='ind', detector_lst=['GMM'], q_fixed_iat=0.9,
                    ipt_dir='input_data/CICIDS2017', opt_dir='output_data',
                    norm_method=None, gridsearch_lst=[False],
                    sampling_lst='',
                    random_state=42, verbose=True):
    """

    :param experiment:
    :param detector_name:
    :param q_fixed_iat:
    :param ipt_dir:
    :param opt_dir:
    :param norm_method:
    :param gridsearch_flg:
    :param random_state:
    :param verbose:
    :return:
    """
    if verbose:
        funcparams_dict = {'experiment': experiment, 'detector_lst': detector_lst,
                           'q_fixed_iat': q_fixed_iat,
                           'ipt_dir': ipt_dir, 'opt_dir': opt_dir,
                           'norm_method': norm_method, 'gridsearch_lst': gridsearch_lst,
                           'sampling_lst': sampling_lst,
                           'random_state': random_state, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=main_experiment.__name__)

    # Step 0: extract features from pcap and save the features to local files
    get_sampling_flg = False
    if get_sampling_flg:
        # to obtain the sampling_lst from pcap
        q_smpl_rate = 0.9
        q_fixed_iat, sub_dir, q_smpl_rate, sampling_lst = main_pcap2features(experiment=experiment,
                                                                             q_fixed_iat=q_fixed_iat,
                                                                             q_smpl_rate=q_smpl_rate)
    else:
        if experiment == 'ind':  # only Friday data
            q_smpl_rate = 0.6
            sub_dir = 'Friday-WorkingHours'
            sampling_lst = [0.013366915384928386, 1.2888627893784468e-05, 4.0084123611450195e-06,
                            0.004426524639129641, 0.005506066715016085]  # q_smpl_rate=0.6 for experiment = 'ind'
            # for Friday data
            # sampling_lst = [4.5899, 6.7859, 7.2307, 5.7866, 3.5814]         #q=0.9
            # sampling_lst = [2.0662943522135417e-07, 1.6829546760110295e-07, 1.7881393432617188e-07,
            #                 1.430511474609375e-07, 1.6829546760110295e-07]  # q=0.1
            # sampling_lst = [2.702077229817708e-07, 1.8232008990119484e-07,
            #                 1.9371509552001953e-07, 2.026557922363281e-07, 2.384185791015625e-07]  # q=0.3
            # sampling_lst = [0.0034731308619181315, 2.384185791015625e-07,2.9355287551879883e-06,
            #                 0.0015740692615509033,  0.0018327656914206112] # q=0.5
            # sampling_lst = [ 0.013366915384928386,  1.2888627893784468e-05,  4.0084123611450195e-06,
            #                   0.004426524639129641, 0.005506066715016085]     # q=0.6
        elif experiment == 'more':  # merged multi-days data
            q_smpl_rate = 0.1
            sub_dir = 'Merged-WorkingHours'
            sampling_lst = [2.0662943522135417e-07, 1.5894571940104166e-07, 1.7881393432617188e-07,
                            1.5058015522203947e-07, 1.5894571940104166e-07]  # q_smpl_rate=0.1 for experiment='more'
        else:
            raise ValueError(f'experiment: {experiment} is not implemented.')
    sampling_tuple = (q_smpl_rate, sampling_lst)
    print(f'sampling_tuple: {sampling_tuple}')

    # Step 1: load features data and conduct the comparison experiment
    # for each IP, compare prop set and baseline set
    # srcIP_lst = [ '192.168.10.8', '192.168.10.9', '192.168.10.15'] for fast test
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    for gs_i, gridsearch_flg in enumerate(gridsearch_lst):  #
        print('\n\n' + '-' * 50 + f'gs_i: {gs_i}, gridsearch_flg: {gridsearch_flg}' + '-' * 50)
        for pf_i, prop_feat in enumerate(['IAT', 'FFT']):
            print('\n' + '+' * 35 + f'pf_i: {pf_i}, prop_feat: {prop_feat}' + '+' * 35)
            for dt_i, detector_name in enumerate(detector_lst):
                # for dt_i, detector_name in enumerate(['GMM']):      # for testing
                print('\n' + '*' * 25 + f'dt_i: {dt_i}, detector_name: {detector_name}' + '*' * 25)
                # only one prop_file, however, maybe multi-baseline files (Baseline 1 and Baseline 2)
                prop_file = f'{ipt_dir}' + '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-IAT.dat'
                # bparm_set params: might include multi-files
                bparam_dict = {  # (key, value): key-feature set, value-file
                    # Baseline 1 features file
                    'StatBaseline': f'{ipt_dir}' + '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-{feat_set}-' \
                                                                                      'dim_10.dat',
                }
                for idx, srcIP in enumerate(srcIP_lst):
                    print('\n' + '%' * 15 + f'index: {idx}, srcIP: {srcIP}')

                    # raw Baseline 2 features file, flows are in different sizes
                    sampling = sampling_lst[idx]
                    sampling_type = 'rate'
                    samp_feat_set = f'SampBaseline-{sampling_type}' + f'_{sampling}-q_sampling_rate_{q_smpl_rate}'
                    # print(f'index: {idx}, srcIP: {srcIP}, samp_feat_set: {samp_feat_set}')
                    bparam_dict[samp_feat_set] = f'{ipt_dir}' + \
                                                 '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-' + '{feat_set}.dat'

                    # obtain results on pparam_dict and bparam_dict by the detector
                    conduct_comparison_experiment(detector_name=detector_name,
                                                  srcIP=srcIP,
                                                  prop_feat=prop_feat,
                                                  prop_file=prop_file,
                                                  bparam_dict=OrderedDict(bparam_dict),
                                                  ipt_dir=ipt_dir,
                                                  opt_dir=opt_dir,
                                                  norm_method=norm_method,
                                                  gridsearch_flg=gridsearch_flg,
                                                  q_fixed_iat=q_fixed_iat,
                                                  random_state=random_state, verbose=verbose)

                    del bparam_dict[samp_feat_set]


def pcap2features(experiment, pcap_file, label_file, q_fixed_iat=0.9, q_sampling_rate=0.9):
    num_pkt_thresh = 2  # each flow at least has max(2, num_pkt_thresh) packets
    sampling_type = 'rate'

    fftbin_lst = []
    sampling_lst = []

    # 1) obtain fids, features, labels from pcap and label_file
    print(f'\nobtain IAT set')
    prop_set = 'IAT'  # only IAT
    prop_fids, prop_features, prop_labels, _ = parse_dataset(pcap_file, labels_csv=label_file,
                                                             experiment=experiment,
                                                             num_pkt_thresh=num_pkt_thresh, feat_set=prop_set)
    iat_file = f'{pcap_file}-{prop_set}.dat'  # store IATs which have different dimensions to file
    dump_data(data=(prop_fids, prop_features, prop_labels), output_file=iat_file)

    fft_bin = int(np.round(np.quantile([len(iat) for iat in prop_features], q=q_fixed_iat)))
    print(f'fft_bin: {fft_bin} when q_fixed_iat equals {q_fixed_iat}')
    fftbin_lst.append(fft_bin)

    # 2) obtain baseline set 1: statistical inform
    print(f'\nobtain Baseline set')
    base_feat = 'StatBaseline'  # label basic flow features
    base_fids, base_features, base_labels, _ = parse_dataset(pcap_file, labels_csv=label_file,
                                                             experiment=experiment,
                                                             num_pkt_thresh=num_pkt_thresh, feat_set=base_feat)
    base_dim = len(base_features[0])
    print(f'feat_set: {base_feat}, dimension: {base_dim}')
    base_file = f'{pcap_file}-{base_feat}-dim_{base_dim}.dat'  # store Baseline 1 with fixed size
    dump_data(data=(base_fids, base_features, base_labels), output_file=base_file)

    # 3) obtain baseline set 2: sampling rate
    print(f'\nobtain Baseline set 2')
    samp_base_feat = 'SampBaseline'  # label sampled features
    samp_base_fids, samp_base_features, samp_base_labels, sampling = parse_dataset(pcap_file, experiment=experiment,
                                                                                   labels_csv=label_file,
                                                                                   sampling_type=sampling_type,
                                                                                   sampling=None,
                                                                                   q_sampling_rate=q_sampling_rate,
                                                                                   # calculate the sampling based on fft_bins and flow durations
                                                                                   num_pkt_thresh=num_pkt_thresh,
                                                                                   fft_bin=fft_bin,
                                                                                   # used for calculating the sampling rate
                                                                                   feat_set=samp_base_feat)
    sampling_lst.append(sampling)
    print(
        f'feat_feat: {samp_base_feat}, with different lengths. sampling_type: {sampling_type}, sampling: {sampling}')
    # store sampled IATs which have different dimensions to file
    samp_base_file = f'{pcap_file}-{samp_base_feat}-{sampling_type}_{sampling}-q_sampling_rate_{q_sampling_rate}.dat'
    dump_data(data=(samp_base_fids, samp_base_features, samp_base_labels), output_file=samp_base_file)
    # break
    print(f'{list(zip([pcap_file], fftbin_lst, sampling_lst))}')
    # break

    return iat_file, base_file, samp_base_file, sampling


class Experiment:

    def __init__(self, expt_name='indv_data', pcap_file='', label_file='', src='', norm_method='std',
                 q_fixed_iat=0.9, q_smpl_rate=0.9, dataset_name='', ipt_dir='', opt_dir=''):
        self.expt_name = expt_name
        self.pcap_file = pcap_file
        self.label_file = label_file
        self.q_fixed_iat = q_fixed_iat
        self.q_smpl_rate = q_smpl_rate
        self.ipt_dir = ipt_dir
        self.opt_dir = opt_dir
        self.src = src
        self.norm_method = norm_method

        self.vebose = True
        self.random_state = 42

    def run(self, detector_lst=['GMM', 'OCSVM', 'KDE'], prop_feat_lst=['IAT', 'FFT'], gridsearch_lst=[False, True]):

        # Step 1: load features data and conduct the comparison experiment
        for dt_i, detector_name in enumerate(detector_lst):
            # for dt_i, detector_name in enumerate(['GMM']):      # for testing
            print('\n' + '*' * 50 + f'dt_i: {dt_i}, detector_name: {detector_name}' + '*' * 50)
            for gs_i, gridsearch_flg in enumerate(gridsearch_lst):  #
                print('\n\n' + '-' * 35 + f'gs_i: {gs_i}, gridsearch_flg: {gridsearch_flg}' + '-' * 35)
                for pf_i, prop_feat in enumerate(prop_feat_lst):
                    print('\n' + '+' * 25 + f'pf_i: {pf_i}, prop_feat: {prop_feat}' + '+' * 25)
                    conduct_comparison_experiment(detector_name=detector_name,
                                                  experiment=self.expt_name,
                                                  srcIP=self.src,
                                                  prop_feat=prop_feat,
                                                  prop_file=self.iat_file,
                                                  bparam_dict={'StatBaseline': self.base_file,
                                                               'SampBaseline': self.samp_base_file},
                                                  ipt_dir=self.ipt_dir,
                                                  opt_dir=self.opt_dir,
                                                  norm_method=self.norm_method,
                                                  gridsearch_flg=gridsearch_flg,
                                                  q_fixed_iat=self.q_fixed_iat,
                                                  random_state=self.random_state,
                                                  verbose=self.vebose)


class CICIDS2017_Exprmt(Experiment):

    def __init__(self, expt_name='indv_data', pcap_file='', label_file='', src='', norm_method='std',
                 q_fixed_iat=0.9, q_smpl_rate=0.9, dataset_name='', ipt_dir='', opt_dir=''):
        super(CICIDS2017_Exprmt, self).__init__()
        self.expt_name = expt_name
        self.pcap_file = pcap_file
        self.label_file = label_file
        self.q_fixed_iat = q_fixed_iat
        self.q_smpl_rate = q_smpl_rate
        self.ipt_dir = ipt_dir
        self.opt_dir = opt_dir
        self.src = src
        self.norm_method = norm_method
        self.vebose = True
        self.random_state = 42

        # # to obtain the sampling_lst from pcap
        self.iat_file, self.base_file, self.samp_base_file, self.sampling_rate = \
            pcap2features(experiment=expt_name, pcap_file=pcap_file, label_file=label_file,
                          q_fixed_iat=q_fixed_iat,
                          q_sampling_rate=q_smpl_rate
                          )

        # self.iat_file = 'input_data/CICIDS2017/five_srcs/Comb-WorkingHours/five_srcs.pcap-IAT.dat'
        # self.base_file= 'input_data/CICIDS2017/five_srcs/Comb-WorkingHours/five_srcs.pcap-StatBaseline-dim_10.dat'
        # self.samp_base_file= 'input_data/CICIDS2017/five_srcs/Comb-WorkingHours/five_srcs.pcap-SampBaseline-rate_7.195447351038456-q_sampling_rate_0.9.dat'
        # self.sampling_rate= 7.195447351038456


#     #
#     # def plot_roc_auc(self, result_dict_dict, prop_feat=''):
#     #     # fig_name += f'{os.path.split(bmodel_file)[-1]}_{len(bparam_dict.items())}_'
#     #     fig_name = ''
#     #     fig_name += f'-SampBaseline-rate_{sampling_rate}-feat_set:{prop_feat}-gridsearch:{gridsearch_flg}-{detector_name}'
#     #     if prop_feat == 'FFT':
#     #         fig_name += f'fft_part:{fft_part}'
#     #
#     #     # 3 save all result in pdf
#     #     if len(fig_name) > 300:  # avoid fig_name too long
#     #         fig_name = fig_name[:300]
#     #     # output_file = f'{opt_dir}/{fig_name}.pdf'
#     #     output_file = f'{fig_name}.pdf'
#     #     plot_roc_auc(result_dict_dict, output_file=output_file,
#     #                  title=f'{detector_name}, srcIP:{srcIP}, gridsearch:{gridsearch_flg}')
#     #
#     # def save(self, data=[]):
#     #     pass
#
#
class SMTV_Exprmt(Experiment):

    def __init__(self, expt_name='indv_data', nrml_pcap='', anml_pcap='', label_file='', src='', norm_method='std',
                 q_fixed_iat=0.9, q_smpl_rate=0.9, dataset_name='', ipt_dir='', opt_dir=''):
        super(SMTV_Exprmt, self).__init__()
        self.expt_name = expt_name
        self.nrml_pcap = nrml_pcap
        self.anml_pcap = anml_pcap
        self.label_file = label_file
        self.q_fixed_iat = q_fixed_iat
        self.q_smpl_rate = q_smpl_rate
        self.ipt_dir = ipt_dir
        self.opt_dir = opt_dir
        self.src = src
        self.norm_method = norm_method
        self.vebose = True
        self.random_state = 42

        # to obtain the sampling_lst from pcap
        self.iat_file, self.base_file, self.samp_base_file, self.sampling_rate = \
            self._pcap2features_smart_tv(experiment=expt_name, nrml_pcap=nrml_pcap, anml_pcap=anml_pcap,
                                         ipt_dir=os.path.join(self.ipt_dir, src),
                                         q_fixed_iat=q_fixed_iat,
                                         q_sampling_rate=q_smpl_rate
                                         )

        # self.iat_file = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/multi-srcIPs.pcap-IAT.dat'
        # self.base_file= 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/multi-srcIPs.pcap-StatBaseline-dim_10.dat'
        # self.samp_base_file= 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/multi-srcIPs.pcap-SampBaseline-rate_0.227432940064407-q_sampling_rate_0.9.dat'
        # self.sampling_rate= 0.227432940064407

    def _pcap2features_smart_tv(self, experiment='indv_data', src='merged_normal_anomaly', nrml_pcap='', anml_pcap='',
                                ipt_dir='input_data/smart-tv-roku-data',
                                q_fixed_iat=0.9,
                                q_sampling_rate=0.9):
        """ Obtain raw features data: IAT, Baseline 1 and Baseline 2
            1) IAT (with different dimensions of different flows),
            2) Baseline 1 (statistic: such as max, mean and std): fixed length (10 dimensions vector)
            3) Baseline 2 (sampling based on number (such as choose 1 from 10 packets) or
                  time (such as 0.1s and 2s))
        :return:
        """
        num_pkt_thresh = 2  # each flow at least has max(2, num_pkt_thresh) packets
        sampling_type = 'rate'

        srcIP_lst = [src]
        fftbin_lst = []
        sampling_lst = []

        pcap_dir = 'normal_anomaly'
        # nrml_pcap = os.path.join(ipt_dir, 'multi-srcIPs/normal_anomaly/merged_normal.pcap')
        # anml_pcap = os.path.join(ipt_dir, 'multi-srcIPs/normal_anomaly/merged_anomaly.pcap')
        pcap_file = os.path.join(ipt_dir, f'{pcap_dir}/{src}')

        # 1) obtain fids, features, labels from pcap and label_file
        print(f'\nobtain IAT set')
        prop_set = 'IAT'  # only IAT
        prop_fids, prop_features, prop_labels, _ = parse_dataset_smart_tv(
            pcap_file_lst=[nrml_pcap, anml_pcap], labels_csv=None,
            num_pkt_thresh=num_pkt_thresh, feat_set=prop_set)
        iat_file = f'{pcap_file}-{prop_set}.dat'  # store IATs which have different dimensions to file
        dump_data(data=(prop_fids, prop_features, prop_labels), output_file=iat_file)

        fft_bin = int(np.round(np.quantile([len(iat) for iat in prop_features], q=q_fixed_iat)))
        print(f'fft_bin: {fft_bin} when q_fixed_iat equals {q_fixed_iat}')
        fftbin_lst.append(fft_bin)

        # 2) obtain baseline set 1: statistical inform
        print(f'\nobtain Baseline set')
        base_set = 'StatBaseline'  # label basic flow features
        base_fids, base_features, base_labels, _ = parse_dataset_smart_tv(
            pcap_file_lst=[nrml_pcap, anml_pcap], labels_csv=None,
            num_pkt_thresh=num_pkt_thresh, feat_set=base_set)
        base_dim = len(base_features[0])
        print(f'feat_set: {base_set}, dimension: {base_dim}')
        base_file = f'{pcap_file}-{base_set}-dim_{base_dim}.dat'  # store Baseline 1 with fixed size
        dump_data(data=(base_fids, base_features, base_labels), output_file=base_file)

        # 3) obtain baseline set 2: sampling rate
        print(f'\nobtain Baseline set 2')
        samp_base_set = 'SampBaseline'  # label sampled features
        samp_base_fids, samp_base_features, samp_base_labels, sampling = parse_dataset_smart_tv(
            pcap_file_lst=[nrml_pcap, anml_pcap],
            labels_csv=None,
            sampling_type=sampling_type,
            sampling=None,
            q_sampling_rate=q_sampling_rate,
            # calculate the sampling based on fft_bins and flow durations
            num_pkt_thresh=num_pkt_thresh,
            fft_bin=fft_bin,
            # used for calculating the sampling rate
            feat_set=samp_base_set)
        sampling_lst.append(sampling)
        print(
            f'feat_set: {samp_base_set}, with different lengths. sampling_type: {sampling_type}, sampling: {sampling}')
        # store sampled IATs which have different dimensions to file
        samp_base_file = f'{pcap_file}-{samp_base_set}-{sampling_type}_{sampling}-q_sampling_rate_{q_sampling_rate}.dat'
        dump_data(data=(samp_base_fids, samp_base_features, samp_base_labels), output_file=samp_base_file)

        print()
        # break
        print(f'{list(zip(srcIP_lst, fftbin_lst, sampling_lst))}')
        # break

        return iat_file, base_file, samp_base_file, sampling


#

def get_file_path(ipt_dir='', src='', sub_dir_l2='', file_name=''):
    file_path = os.path.join(ipt_dir, src, sub_dir_l2, file_name)

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


def preprocess_smart_tv_data(ipt_dir, overwrite=True):
    src_lst = ['10.42.0.119', '10.42.0.120', '10.42.0.119',
               '10.42.0.120', '10.42.0.119', '10.42.0.119',
               '10.42.0.120', '10.42.0.120', '10.42.0.119',
               '10.42.0.119', '10.42.0.120', '10.42.0.120']  # filter unrelated packets
    pcap_lst = ['48626-1569697955-normal.pcap', '54065-1569633493-normal.pcap', '36732-1569696202-normal.pcap',
                '222279-1569631187-normal.pcap', '71376-1569639462-normal.pcap', '48631-1569699232-normal.pcap',
                '258327-1569630531-normal.pcap', '121375-1569631825-normal.pcap',
                '16184-1569701783-normal.pcap',
                '25082-1569695098-normal.pcap', '13933-1569628870-normal.pcap',
                '172665-1569633928-normal.pcap']  # normal
    # pcap_file_lst = []
    # for i, (src, pcap_file) in enumerate(zip(src_lst, pcap_lst)):
    #     pcap_file_i = get_file_path(ipt_dir, 'raw_pcap', sub_dir_l2='', file_name=pcap_file)
    #     pcapout_file = os.path.join(ipt_dir, f'multi-srcIPs/normal_anomaly/srcIP_{src}_{pcap_file}')
    #     if overwrite:
    #         keep_ips_in_pcap(input_file=pcap_file_i, output_file=pcapout_file, kept_ips=['10.42.0.119'])
    #     pcap_file_lst.append(pcapout_file)
    # nrml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_normal.pcap')
    # merge_pcaps(pcap_file_lst, mrg_pcap_path=nrml_pcap)
    # nrml_label = generate_label(nrml_pcap, label='NORMAL')
    #
    # src_lst = ['10.42.0.120', '10.42.0.120', '10.42.0.119']  # filter unrelated packets
    # pcap_file_lst = ['12-1569622891.pcap', '2285-1569623141.pcap', '18502-1569700271.pcap']  # anomaly
    # for i, (src, pcap_file) in enumerate(zip(src_lst, pcap_lst)):
    #     pcap_file_i = get_file_path(ipt_dir, 'raw_pcap', sub_dir_l2='', file_name=pcap_file)
    #     pcapout_file = os.path.join(ipt_dir, f'multi-srcIPs/normal_anomaly/srcIP_{src}_{pcap_file}')
    #     if overwrite:
    #         keep_ips_in_pcap(input_file=pcap_file_i, output_file=pcapout_file, kept_ips=['10.42.0.119'])
    #     pcap_file_lst.append(pcapout_file)
    # anml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_anomaly.pcap')
    # merge_pcaps(pcap_file_lst, mrg_pcap_path=anml_pcap)
    # anml_label = generate_label(anml_pcap, label='ANOMALY')
    #

    mrg_pcap_path = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly',
                                  file_name='multi-srcIPs.pcap')
    # merge_pcaps([nrml_pcap, anml_pcap], mrg_pcap_path)
    mrg_label_path = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly',
                                   file_name='multi-srcIPs.csv')
    nrml_label = '/Users/kunyang/PycharmProjects/IoT_feature_sets_comparison_20190822/input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/merged_normal.csv'
    anml_label = '/Users/kunyang/PycharmProjects/IoT_feature_sets_comparison_20190822/input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/merged_anomaly.csv'
    merge_labels([nrml_label, anml_label], mrg_label_path)

    return 'multi-srcIPs', mrg_pcap_path, mrg_label_path


def get_nrml_anml_smart_tv_data(ipt_dir, keep_ip='10.42.0.119', overwrite=True):
    # src_lst = ['10.42.0.119', '10.42.0.120', '10.42.0.119',
    #            '10.42.0.120', '10.42.0.119', '10.42.0.119',
    #            '10.42.0.120', '10.42.0.120', '10.42.0.119',
    #            '10.42.0.119', '10.42.0.120', '10.42.0.120']  # filter unrelated packets
    # pcap_lst = ['48626-1569697955-normal.pcap', '54065-1569633493-normal.pcap', '36732-1569696202-normal.pcap',
    #             '222279-1569631187-normal.pcap', '71376-1569639462-normal.pcap', '48631-1569699232-normal.pcap',
    #             '258327-1569630531-normal.pcap', '121375-1569631825-normal.pcap',
    #             '16184-1569701783-normal.pcap',
    #             '25082-1569695098-normal.pcap', '13933-1569628870-normal.pcap',
    #             '172665-1569633928-normal.pcap']  # normal

    pcap_file_lst = []
    nrml_dir = os.path.join(ipt_dir, 'raw_pcap', 'normal')
    src = '10.42.0.1'
    for i, pcap in enumerate(os.listdir(nrml_dir)):
        if not pcap.endswith('.pcap'):
            print(f'i:{i+1}, pcap:{pcap}')
            continue
        # pcap = os.path.join(nrml_dir,pcap)
        # pcap_lst.append(pcap)
        pcap_file_lst.append(os.path.join(nrml_dir, pcap))
    nrml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_normal.pcap')
    merge_pcaps(pcap_file_lst, mrg_pcap_path=nrml_pcap)
    # nrml_label = generate_label(nrml_pcap, label='NORMAL')
    src_nrml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly',
                                  file_name=f'src_{src}_merged_normal.pcap')
    if overwrite:
        keep_ips_in_pcap(input_file=nrml_pcap, output_file=src_nrml_pcap, kept_ips=[src])

    # src_lst = [keep_ip] * len(pcap_lst)
    # pcap_file_lst = []
    # for i, (src, pcap_file) in enumerate(zip(src_lst, pcap_lst)):
    #     pcap_file_i = get_file_path(ipt_dir,  'raw_pcap/normal', sub_dir_l2='', file_name=pcap_file)
    #     pcapout_file = os.path.join(ipt_dir, f'multi-srcIPs/normal_anomaly/srcIP_{src}_{pcap_file}')
    #     print(f'i:{i+1}, pcapout_file:{pcapout_file}')
    #     if overwrite:
    #         keep_ips_in_pcap(input_file=pcap_file_i, output_file=pcapout_file, kept_ips=['10.42.0.119'])
    #     pcap_file_lst.append(pcapout_file)
    # nrml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_normal.pcap')
    # merge_pcaps(pcap_file_lst, mrg_pcap_path=nrml_pcap)
    # nrml_label = generate_label(nrml_pcap, label='NORMAL')

    # # src_lst = ['10.42.0.120', '10.42.0.120', '10.42.0.119']  # filter unrelated packets
    # # pcap_file_lst = ['12-1569622891.pcap', '2285-1569623141.pcap', '18502-1569700271.pcap']  # anomaly
    # pcap_lst = []
    # anml_dir = os.path.join(ipt_dir,'raw_pcap','anomaly')
    # for i, pcap in enumerate(os.listdir(anml_dir)):
    #     if not pcap.endswith('.pcap'):
    #         print(f'i:{i+1}, pcap:{pcap}')
    #         continue
    #     # pcap = os.path.join(anml_dir, pcap)
    #     pcap_lst.append(pcap)
    #
    # src_lst = [keep_ip] * len(pcap_lst)
    #
    # pcap_file_lst=[]
    # for i, (src, pcap_file) in enumerate(zip(src_lst, pcap_lst)):
    #     pcap_file_i = get_file_path(ipt_dir, 'raw_pcap/anomaly', sub_dir_l2='', file_name=pcap_file)
    #     pcapout_file = os.path.join(ipt_dir, f'multi-srcIPs/normal_anomaly/srcIP_{src}_{pcap_file}')
    #     print(f'i:{i+1}, pcapout_file:{pcapout_file}')
    #     if overwrite:
    #         keep_ips_in_pcap(input_file=pcap_file_i, output_file=pcapout_file, kept_ips=['10.42.0.119'])
    #     pcap_file_lst.append(pcapout_file)
    # anml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_anomaly.pcap')
    # merge_pcaps(pcap_file_lst, mrg_pcap_path=anml_pcap)
    # anml_label = generate_label(anml_pcap, label='ANOMALY')

    pcap_file_lst = []
    src = '10.42.0.120'
    anml_dir = os.path.join(ipt_dir, 'raw_pcap', 'anomaly')
    # src = '69.16.175.42'
    # anml_dir = os.path.join(ipt_dir, 'raw_pcap', 'normal')
    for i, pcap in enumerate(os.listdir(anml_dir)):
        if not pcap.endswith('.pcap'):
            print(f'i:{i+1}, pcap:{pcap}')
            continue
        # pcap = os.path.join(nrml_dir,pcap)
        # pcap_lst.append(pcap)
        pcap_file_lst.append(os.path.join(anml_dir, pcap))
    anml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly', file_name='merged_anomaly.pcap')
    merge_pcaps(pcap_file_lst, mrg_pcap_path=anml_pcap)
    # anml_label = generate_label(anml_pcap, label='ANOMALY')
    src_anml_pcap = get_file_path(ipt_dir, 'multi-srcIPs', sub_dir_l2='normal_anomaly',
                                  file_name=f'src_{src}_merged_anomaly.pcap')
    if overwrite:
        keep_ips_in_pcap(input_file=anml_pcap, output_file=src_anml_pcap, kept_ips=[src])

    return 'multi-srcIPs', src_nrml_pcap, src_anml_pcap


def main(dataset_name='CICIDS2017', expt_name='indv_data', overwrite=True):
    if dataset_name == 'demo_data':
        src_lst = ['test']
        ipt_dir = os.path.join('input_data', dataset_name)
        if expt_name == 'indv_data':  # only Friday data
            pcap_file_lst = []
            label_file_lst = []
            for i, src in enumerate(src_lst):
                pcap_file_lst.append(get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='',
                                                   file_name=f'srcIP_{src}.pcap'))
                label_file_lst.append(get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='',
                                                    file_name=f'srcIP_{src}.csv'))
        for i, (src, pcap_file, label_file) in enumerate(zip(src_lst, pcap_file_lst, label_file_lst)):
            print(f'i={i+1}/{len(pcap_file_lst)}, pcap_file: {pcap_file}, label_file: {label_file}')
            expt = CICIDS2017_Exprmt(expt_name='indv_data', pcap_file=pcap_file, label_file=label_file,
                                     src=src,
                                     ipt_dir=ipt_dir, opt_dir='output_data',
                                     q_fixed_iat=0.9,
                                     q_smpl_rate=0.9)  # exprmt_name = 'indv_data', 'agmt_data', 'comb_data'
            expt.run(detector_lst=['GMM', 'OCSVM', 'KDE'], prop_feat_lst=['IAT', 'FFT'], gridsearch_lst=[True, False])
            expt.save()

    if dataset_name == 'CICIDS2017':

        ipt_dir = os.path.join('input_data', dataset_name)
        if expt_name == 'indv_data':  # only Friday data
            # src_lst = ['192.168.10.14', '192.168.10.15']  # for debug code
            src_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
            pcap_file_lst = []
            label_file_lst = []
            for i, src in enumerate(src_lst):
                pcap_file_lst.append(get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='Friday-WorkingHours',
                                                   file_name=f'srcIP_{src}.pcap'))
                label_file_lst.append(get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='Friday-WorkingHours',
                                                    file_name=f'srcIP_{src}.csv'))
        elif expt_name == 'agmt_data':  # Friday + Monday data
            pcap_file_lst = []
            label_file_lst = []
            src_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
            for i, src in enumerate(src_lst):
                pcap_path = get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='Friday-WorkingHours',
                                          file_name=f'srcIP_{src}.pcap')
                pcap_path_2 = get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='Monday-WorkingHours',
                                            file_name=f'srcIP_{src}.pcap')
                mrg_pcap_path = get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='More-WorkingHours',
                                              file_name=f'srcIP_{src}_more.pcap')

                label_path = get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='Friday-WorkingHours',
                                           file_name=f'srcIP_{src}.csv')
                label_path_2 = get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='Monday-WorkingHours',
                                             file_name=f'srcIP_{src}.csv')
                mrg_label_path = get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='More-WorkingHours',
                                               file_name=f'srcIP_{src}_more.csv')
                if overwrite:
                    merge_pcaps([pcap_path, pcap_path_2], mrg_pcap_path=mrg_pcap_path)
                    merge_labels([label_path, label_path_2], mrg_label_path=mrg_label_path)
                pcap_file_lst.append(mrg_pcap_path)
                label_file_lst.append(mrg_label_path)
        elif expt_name == 'comb_data':  # combine Friday data
            src_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
            pcap_file_lst = []
            label_file_lst = []
            for i, src in enumerate(src_lst):
                pcap_path = get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='Friday-WorkingHours',
                                          file_name=f'srcIP_{src}.pcap')
                pcap_file_lst.append(pcap_path)
                label_path = get_file_path(ipt_dir, f'srcIP_{src}', sub_dir_l2='Friday-WorkingHours',
                                           file_name=f'srcIP_{src}.csv')
                label_file_lst.append(label_path)
            mrg_pcap_path = get_file_path(ipt_dir, f'five_srcs', sub_dir_l2='Comb-WorkingHours',
                                          file_name=f'five_srcs.pcap')
            mrg_label_path = get_file_path(ipt_dir, f'five_srcs', sub_dir_l2='Comb-WorkingHours',
                                           file_name=f'five_labels.csv')
            if overwrite:
                merge_pcaps(pcap_file_lst, mrg_pcap_path=mrg_pcap_path)
                merge_labels(label_file_lst, mrg_label_path=mrg_label_path)
            pcap_file_lst = [mrg_pcap_path]
            label_file_lst = [mrg_label_path]
            src_lst = ['five_srcs']

        for i, (src, pcap_file, label_file) in enumerate(zip(src_lst, pcap_file_lst, label_file_lst)):
            print(f'i={i+1}/{len(pcap_file_lst)}, pcap_file: {pcap_file}, label_file: {label_file}')
            expt = CICIDS2017_Exprmt(expt_name=expt_name, pcap_file=pcap_file, label_file=label_file,
                                     src=src,
                                     ipt_dir=ipt_dir, opt_dir='output_data',
                                     q_fixed_iat=0.9,
                                     q_smpl_rate=0.9)  # exprmt_name = 'indv_data', 'agmt_data', 'comb_data'
            expt.run(detector_lst=['GMM', 'OCSVM', 'KDE'], prop_feat_lst=['IAT', 'FFT'], gridsearch_lst=[True, False])
            expt.save()


    elif dataset_name == 'SMTV':  # smart-tv-roku-data
        ipt_dir = 'input_data/smart-tv-roku-data'

        # if overwrite:
        #     src, pcap_file, label_file = preprocess_smart_tv_data(ipt_dir=ipt_dir, overwrite=False)
        #
        #     src_lst = [src]
        #     pcap_file_lst = [pcap_file]
        #     label_file_lst=[label_file]
        #
        # else:
        #     src_lst = ['multi-srcIPs.pcap']
        #     pcap_file_lst = ['input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/multi-srcIPs.pcap']
        #     label_file_lst = ['input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/multi-srcIPs.csv']

        if overwrite:
            src, nrml_pcap, anml_pcap = get_nrml_anml_smart_tv_data(ipt_dir, overwrite=overwrite)

        else:
            src = 'multi-srcIPs'
            nrml_pcap = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/src_10.42.0.119_merged_normal.pcap'
            anml_pcap = 'input_data/smart-tv-roku-data/multi-srcIPs/normal_anomaly/src_10.42.0.119_merged_anomaly.pcap'
        expt = SMTV_Exprmt(expt_name=None, nrml_pcap=nrml_pcap, anml_pcap=anml_pcap,
                           src=src,
                           ipt_dir=ipt_dir, opt_dir='output_data',
                           q_fixed_iat=0.9,
                           q_smpl_rate=0.9)  # exprmt_name = 'indv_data', 'agmt_data', 'comb_data'
        expt.run(detector_lst=['GMM', 'OCSVM', 'KDE'], prop_feat_lst=['IAT', 'FFT'], gridsearch_lst=[True, False])
        # expt.save()

    else:
        raise ValueError()


if __name__ == '__main__':
    # for i in progressbar.progressbar(range(100)):
    #     main(dataset_name='demo_data', expt_name='indv_data', overwrite=True)
    # main(dataset_name='CICIDS2017', expt_name='agmt_data', overwrite=True)   # augmented_data
    main(dataset_name='SMTV', expt_name=None, overwrite=True)
