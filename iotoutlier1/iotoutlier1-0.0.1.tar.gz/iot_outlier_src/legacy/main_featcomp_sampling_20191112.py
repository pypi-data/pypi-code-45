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

from collections import OrderedDict
from copy import deepcopy

from _config import *
from data_process import main_pcap2features
from data_process import transform_iat_to_fixed_out, transform_samp_baseline_to_fixed_out
from legacy.experiment_class import IndividualExperiment
from utils.tool import pprint, execute_time, transform_params_to_str
from utils.visual import plot_roc_auc


def conduct_comparison_experiment(detector_name='',
                                  srcIP='',
                                  pparam_dict=OrderedDict(),
                                  bparam_dict=OrderedDict(),
                                  input_dir='',
                                  output_dir='',
                                  norm_method=None,
                                  gridsearch_flg=False,
                                  quant=0.9,
                                  random_state=42,
                                  verbose=True):
    """ Get comparison results on proposed set and baseline set

    :param detector_name:
    :param srcIP:
    :param pparam_dict:
    :param bparam_dict:
    :param norm_method:
    :param gridsearch_flg:
    :param quant:
    :param random_state:
    :param verbose:
    :return:
    """
    if verbose:
        funcparams_dict = {
            'srcIP': srcIP,
            'detector_name': detector_name,
            'pparam_dict': pparam_dict,
            'bparam_dict': bparam_dict,
            'input_dir': input_dir,
            'output_dir': output_dir,
            'quant': quant,
            'norm_method': norm_method,
            'gridsearch_flg': gridsearch_flg,
            'random_state': random_state,
            'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=conduct_comparison_experiment.__name__)

    # get results on pparam_dict and bparam_dict by the detector
    result_dict_dict = OrderedDict()  # store the dict results: {feat_set: results of the feat_set}
    fig_name = ''
    fft_bin_dict = OrderedDict()
    # 1. obtain results (such as ROC and AUC) of IAT or FFT on pparam_dict
    for i, (prop_set, prop_file) in enumerate(pparam_dict.items()):
        prop_file = prop_file.format(srcIP=srcIP)
        fft_part = 'real'  # only for FFT: 'real' or 'real+imaginary'
        print('\n' + f'prop_file: {prop_file}, prop_set: {prop_set}')

        # 1.1) get the fixed size of IAT or FFT based on the given quantile (default 0.9)
        prop_file, fft_bin = transform_iat_to_fixed_out(input_file=prop_file, feat_set=prop_set, quant=quant,
                                                        fft_part=fft_part, overwrite=True, verbose=verbose)
        fft_bin_dict[prop_file] = fft_bin

        # 1.2) get the results
        prop = IndividualExperiment(input_file=prop_file, feat_set=prop_set, norm_method=norm_method,
                                    random_state=random_state, verbose=verbose)
        result_dict = prop.run(detector_name=detector_name,
                               X_train=prop.X_train, y_train=prop.y_train,
                               X_test=prop.X_test, y_test=prop.y_test,
                               gridsearch_flg=gridsearch_flg)

        # 1.3) save the built detector to file
        params_str = transform_params_to_str(deepcopy(prop.detector.get_params()),
                                             remove_lst=['verbose', 'random_state', 'means_init', None, 'auto'])
        pmodel_file = f'{output_dir}/{prop_file}_{detector_name}_{str(params_str)}.joblib'
        pmodel_file = prop.dump_model(prop.detector, model_file=pmodel_file)

        result_dict_dict[prop_set] = result_dict  # store the result on prop_set
    fig_name += f'{os.path.splitext(pmodel_file)[0]}_{len(pparam_dict.items())}_'

    for i, (base_set, base_file) in enumerate(bparam_dict.items()):
        # 2. obtain results (such as ROC and AUC) of Baseline 2
        base_file = base_file.format(srcIP=srcIP, feat_set=base_set)
        print('\n' + f'base_file: {base_file}, base_set: {base_set}')
        if 'SampBaseline-rate' in base_file:
            sampling_rate = base_file.split('SampBaseline-rate_')[-1]
        else:
            sampling_rate = None

        if base_set != 'StatBaseline' or base_set == 'SampBaseline':
            # 2.1) get the fixed size (fft_bin) for sampling baseline
            fft_bin = list(fft_bin_dict.values())[0]  # same with the IAT length
            print(f'fft_bin: {fft_bin}')

            base_file = transform_samp_baseline_to_fixed_out(input_file=base_file, fft_bin=fft_bin,
                                                             overwrite=True, verbose=verbose)
        # 2.2) get the results on bparam_dict
        base = IndividualExperiment(input_file=base_file, feat_set=base_set,
                                    norm_method=norm_method,
                                    random_state=random_state, verbose=verbose)
        result_dict = base.run(detector_name=detector_name,
                               X_train=base.X_train, y_train=base.y_train,
                               X_test=base.X_test, y_test=base.y_test,
                               gridsearch_flg=gridsearch_flg)

        # 2.3) save the detector to file
        params_str = transform_params_to_str(deepcopy(base.detector.get_params()),
                                             remove_lst=['verbose', 'random_state', 'means_init', None, 'auto'])
        bmodel_file = f'{output_dir}/{base_file}_{detector_name}_{str(params_str)}.joblib'
        bmodel_file = base.dump_model(base.detector, model_file=bmodel_file)
        result_dict_dict[base_set] = result_dict  # store the result on samp_base_set
    # fig_name += f'{os.path.split(bmodel_file)[-1]}_{len(bparam_dict.items())}_'
    fig_name += f'-SampBaseline-rate_{sampling_rate}-feat_set:{prop_set}-gridsearch:{gridsearch_flg}-{detector_name}'
    if prop_feat == 'FFT':
        fig_name += f'fft_part:{fft_part}'

    # 3 save all result in pdf
    if len(fig_name) > 300:  # avoid fig_name too long
        fig_name = fig_name[:300]
    # output_file = f'{output_dir}/{fig_name}.pdf'
    output_file = f'{fig_name}.pdf'
    plot_roc_auc(result_dict_dict, output_file=output_file,
                 title=f'{detector_name}, srcIP:{srcIP}, gridsearch:{gridsearch_flg}')

    return result_dict_dict


@execute_time
def main(experiment='ind', detector_name='GMM', prop_feat='IAT', quant=0.9,
         input_dir='input_data/CICIDS2017', output_dir='output_data',
         norm_method=None, gridsearch_flg=False,
         sampling_lst='',
         random_state=42, verbose=True):
    """

    :param experiment:
    :param detector_name:
    :param quant:
    :param input_dir:
    :param output_dir:
    :param norm_method:
    :param gridsearch_flg:
    :param random_state:
    :param verbose:
    :return:
    """
    if verbose:
        funcparams_dict = {'experiment': experiment, 'detector_name': detector_name,
                           'quant': quant,
                           'input_dir': input_dir, 'output_dir': output_dir,
                           'norm_method': norm_method, 'gridsearch_flg': gridsearch_flg,
                           'sampling_lst': sampling_lst,
                           'random_state': random_state, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=main.__name__)

    # for each IP, compare prop set and baseline set
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    # srcIP_lst = [ '192.168.10.8', '192.168.10.9', '192.168.10.15'] for fast test
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
    if experiment == 'ind':
        sub_dir = 'Friday-WorkingHours'
    elif experiment == 'more':
        # # for merged data (Friday and Monday)
        # sampling_lst = [0.0016492684682210285,1.7219119601779514e-07,
        #                 1.9371509552001953e-07, 2.1332188656455592e-07, 2.2517310248480902e-07]  # q=0.3
        sub_dir = 'Merged-WorkingHours'
    else:
        raise ValueError('experiment is not implemented.')
    # prop_set params: might include multi-files
    pparam_dict = {  # IAT or FFT. (key, value): key-feature set, value-file
        # raw IATs file, which is used to obtain IAT and FFT features with fixed size
        # Note: no mater what key (prop_feat) is, the input_file always is 'raw-IAT-data'
        # if key=IAT, obtain fixed IAT from raw-IAT
        # if key = FFT, still obtain fixed FFT from raw-IAT
        prop_feat: f'{input_dir}' + '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-IAT.dat'
    }

    # prop_set params: might include multi-files
    bparam_dict = {  # (key, value): key-feature set, value-file
        # Baseline 1 features file
        'StatBaseline': f'{input_dir}' + '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-{feat_set}-' \
                                                                            'dim_10.dat',
    }
    # # add more baselines to bparam_dict
    # for i, (sampling_type, sampling) in enumerate(sampling_tuple):
    #     # raw Baseline 2 features file, flows are in different sizes
    #     samp_feat_set = f'SampBaseline-{sampling_type}_{sampling}'
    #     bparam_dict[samp_feat_set] = f'{input_dir}' + \
    #                                  '/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-' + f'{samp_feat_set}.dat'

    for idx, srcIP in enumerate(srcIP_lst):
        print('\n' + '%' * 15 + f'index: {idx}, srcIP: {srcIP}')

        # raw Baseline 2 features file, flows are in different sizes
        sampling = sampling_lst[idx]
        sampling_type = 'rate'
        samp_feat_set = f'SampBaseline-{sampling_type}' + f'_{sampling}'
        # print(f'index: {idx}, srcIP: {srcIP}, samp_feat_set: {samp_feat_set}')
        bparam_dict[samp_feat_set] = f'{input_dir}' + \
                                     '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-' + '{feat_set}.dat'

        # obtain results on pparam_dict and bparam_dict by the detector
        conduct_comparison_experiment(detector_name=detector_name,
                                      srcIP=srcIP,
                                      pparam_dict=OrderedDict(pparam_dict),
                                      bparam_dict=OrderedDict(bparam_dict),
                                      input_dir=input_dir,
                                      output_dir=output_dir,
                                      norm_method=norm_method,
                                      gridsearch_flg=gridsearch_flg,
                                      quant=quant,
                                      random_state=random_state, verbose=verbose)

        del bparam_dict[samp_feat_set]
        # break


if __name__ == '__main__':
    # if len(sys.argv) < 1:
    #   #     sys.exit("Usage: python3 {} [pcap_file] [labels_csv] [FFT bins] "
    #              "[num pkt thresh] [output_file] [do_subflows TRUE|FALSE]".format(sys.argv[0]))
    # detector_name = sys.argv[1]
    # gridsearch_flg = eval(sys.argv[2])
    # detector_name = 'OCSVM'  # 1) GMM; 2) OCSVM; 3) KDE; 4) PCA

    experiment = 'more'  # 1) ind: individual; 2) mix; 3) more: add more data
    get_sampling_flg = True
    if get_sampling_flg:
        sampling_lst = main_pcap2features(experiment=experiment, q_sampling=0.9)
    else:
        sampling_lst = [2.0662943522135417e-07, 1.5894571940104166e-07, 1.7881393432617188e-07, 1.5058015522203947e-07,
                        1.5894571940104166e-07]  # q=0.1

    print(f'sampling_lst: {sampling_lst}')

    for gs_i, gridsearch_flg in enumerate([False, True]):  #
        print('\n\n' + '-' * 50 + f'gs_i: {gs_i}, gridsearch_flg: {gridsearch_flg}' + '-' * 50)
        for pf_i, prop_feat in enumerate(['IAT', 'FFT']):
            print('\n' + '+' * 35 + f'pf_i: {pf_i}, prop_feat: {prop_feat}' + '+' * 35)
            for dt_i, detector_name in enumerate(['GMM', 'OCSVM', 'KDE']):
                # for dt_i, detector_name in enumerate(['GMM']):      # for testing
                print('\n' + '*' * 25 + f'dt_i: {dt_i}, detector_name: {detector_name}' + '*' * 25)
                quant = 0.90  # to obtain fft_bin from raw IATs data (with different dimensions) using np.quantile (IATs, q=0.9)
                # For baseline 2, sampling features based on number of packet or time interval
                # ('number', 2) ((sampling_type, sampling)) means choose the first packets on each 2 packets
                # sampling_tuple=()   # only compare proposed features and Baseline 1 (statistical features)
                # sampling_tuple = (('number', 2), ('number', 5), ('number', 8),('number', 10))
                # sampling_tuple = (('number', 2), ('number', 3), ('number', 5))
                # sampling_tuple = ('interval', 0.01), ('interval', 0.05), ('interval', 0.1), ('interval', 1)
                # sampling_tuple = (('rate', 1000000), ('rate', 100000), ('rate', 10000), ('rate', 1000))
                # sampling_tuple = (('rate', 0.1), ('rate', 1), ('rate', 2), ('rate', 5), ('rate', 10))
                # sampling_tuple = (('rate', 5), ('rate', 0.1) )
                main(experiment=experiment,
                     detector_name=detector_name,
                     prop_feat=prop_feat,
                     quant=quant,
                     input_dir=input_dir,
                     output_dir=output_dir,
                     norm_method=norm_method,
                     gridsearch_flg=gridsearch_flg,
                     sampling_lst=sampling_lst,
                     random_state=random_state,
                     verbose=verbose)
