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
import errno
import shutil
from collections import OrderedDict
from copy import deepcopy

from _config import *
from data_process import main_pcap2features
from data_process import main_preprocess_pcap
from data_process import transform_iat_to_fixed_out, transform_samp_baseline_to_fixed_out
from legacy.experiment_class import IndividualExperiment
from utils.tool import pprint, execute_time, transform_params_to_str
from utils.visual import plot_roc_auc


def conduct_comparison_experiment(experiment='',
                                  detector_name='',
                                  srcIP='',
                                  prop_feat='IAT',
                                  prop_file='',
                                  bparam_dict=OrderedDict(),
                                  input_dir='',
                                  output_dir='',
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
            'experiment': experiment,
            'srcIP': srcIP,
            'detector_name': detector_name,
            'prop_feat': prop_feat,
            'prop_file': prop_file,
            'bparam_dict': bparam_dict,
            'input_dir': input_dir,
            'output_dir': output_dir,
            'q_fixed_iat': q_fixed_iat,
            'norm_method': norm_method,
            'gridsearch_flg': gridsearch_flg,
            'random_state': random_state,
            'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=conduct_comparison_experiment.__name__)

    # get results on pparam_dict and bparam_dict by the detector
    result_dict_dict = OrderedDict()  # store the dict results: {feat_set: results of the feat_set}
    fft_bin_dict = OrderedDict()
    # 1. obtain results (such as ROC and AUC) of IAT or FFT on pparam_dict
    prop_file = prop_file.format(srcIP=srcIP)
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
    pmodel_file = f'{output_dir}/{prop_file}_{detector_name}_{str(params_str)}.joblib'
    pmodel_file = prop.dump_model(prop.detector, model_file=pmodel_file)

    result_dict_dict[prop_feat] = result_dict  # store the result on prop_feat
    fig_name = f'{os.path.splitext(pmodel_file)[0]}_{experiment}_'

    for i, (base_feat, base_file) in enumerate(bparam_dict.items()):
        # 2. obtain results (such as ROC and AUC) of Baseline 2
        base_file = base_file.format(srcIP=srcIP, feat_set=base_feat)
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
        bmodel_file = f'{output_dir}/{base_file}_{detector_name}_{str(params_str)}.joblib'
        bmodel_file = base.dump_model(base.detector, model_file=bmodel_file)
        result_dict_dict[base_feat] = result_dict  # store the result on samp_base_set
    # fig_name += f'{os.path.split(bmodel_file)[-1]}_{len(bparam_dict.items())}_'
    fig_name += f'-SampBaseline-rate_{sampling_rate}-feat_set:{prop_feat}-gridsearch:{gridsearch_flg}-{detector_name}'
    if prop_feat == 'FFT':
        fig_name += f'fft_part:{fft_part}'

    # 3 save all result in pdf
    if len(fig_name) > 300:  # avoid fig_name too long
        fig_name = fig_name[:300]
    # output_file = f'{output_dir}/{fig_name}.pdf'
    output_file = f'{fig_name}.pdf'
    plot_roc_auc(result_dict_dict, output_file=output_file,
                 title=f'{detector_name}, gridsearch:{gridsearch_flg}, experiment: {experiment}, srcIP:{srcIP}')

    return result_dict_dict


@execute_time
def main_experiment_CICIDS2017(experiment='ind', detector_lst=['GMM'], q_fixed_iat=0.9, q_sampling_rate=0.9,
                               input_dir='input_data/CICIDS2017', output_dir='output_data',
                               norm_method=None, gridsearch_lst=[False],
                               sampling_lst='',
                               random_state=42, verbose=True):
    """

    :param experiment:
    :param detector_name:
    :param q_fixed_iat:
    :param input_dir:
    :param output_dir:
    :param norm_method:
    :param gridsearch_flg:
    :param random_state:
    :param verbose:
    :return:
    """
    if verbose:
        funcparams_dict = {'experiment': experiment, 'detector_lst': detector_lst,
                           'q_fixed_iat': q_fixed_iat, 'q_sampling_rate': q_sampling_rate,
                           'input_dir': input_dir, 'output_dir': output_dir,
                           'norm_method': norm_method, 'gridsearch_lst': gridsearch_lst,
                           'sampling_lst': sampling_lst,
                           'random_state': random_state, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=main_experiment_CICIDS2017.__name__)

    # Step 0: extract features from pcap and save the features to local files
    get_sampling_flg = True
    if get_sampling_flg:
        # to obtain the sampling_lst from pcap
        q_sampling_rate = q_sampling_rate
        q_fixed_iat, sub_dir, q_sampling_rate, sampling_lst = main_pcap2features(experiment=experiment,
                                                                                 q_fixed_iat=q_fixed_iat,
                                                                                 q_sampling_rate=q_sampling_rate)
    else:
        if experiment == 'ind':  # only Friday data
            q_sampling_rate = 0.6
            sub_dir = 'Friday-WorkingHours'
            sampling_lst = [0.013366915384928386, 1.2888627893784468e-05, 4.0084123611450195e-06,
                            0.004426524639129641, 0.005506066715016085]  # q_sampling_rate=0.6 for experiment = 'ind'
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
            q_sampling_rate = 0.1
            sub_dir = 'Merged-WorkingHours'
            sampling_lst = [2.0662943522135417e-07, 1.5894571940104166e-07, 1.7881393432617188e-07,
                            1.5058015522203947e-07, 1.5894571940104166e-07]  # q_sampling_rate=0.1 for experiment='more'
        else:
            raise ValueError(f'experiment: {experiment} is not implemented.')
    sampling_tuple = (q_sampling_rate, sampling_lst)
    print(f'sampling_tuple: {sampling_tuple}')

    # Step 1: load features data and conduct the comparison experiment
    # for each IP, compare prop set and baseline set
    # srcIP_lst = [ '192.168.10.8', '192.168.10.9', '192.168.10.15'] for fast test
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    for gs_i, gridsearch_flg in enumerate(gridsearch_lst):  #
        print('\n\n' + '-' * 50 + f'gs_i: {gs_i}, gridsearch_flg: {gridsearch_flg}' + '-' * 50)
        for dt_i, detector_name in enumerate(detector_lst):
            # for dt_i, detector_name in enumerate(['GMM']):      # for testing
            print('\n' + '*' * 35 + f'dt_i: {dt_i}, detector_name: {detector_name}' + '*' * 35)
            for pf_i, prop_feat in enumerate(['IAT', 'FFT']):
                print('\n' + '+' * 25 + f'pf_i: {pf_i}, prop_feat: {prop_feat}' + '+' * 25)
                # only one prop_file, however, maybe multi-baseline files (Baseline 1 and Baseline 2)
                prop_file = f'{input_dir}' + '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-IAT.dat'
                # bparm_set params: might include multi-files
                bparam_dict = {  # (key, value): key-feature set, value-file
                    # Baseline 1 features file
                    'StatBaseline': f'{input_dir}' + '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-{feat_set}-' \
                                                                                        'dim_10.dat',
                }
                for idx, srcIP in enumerate(srcIP_lst):
                    print('\n' + '%' * 15 + f'index: {idx}, srcIP: {srcIP}')

                    # raw Baseline 2 features file, flows are in different sizes
                    sampling = sampling_lst[idx]
                    sampling_type = 'rate'
                    samp_feat_set = f'SampBaseline-{sampling_type}' + f'_{sampling}-q_sampling_rate_{q_sampling_rate}'
                    # print(f'index: {idx}, srcIP: {srcIP}, samp_feat_set: {samp_feat_set}')
                    bparam_dict[samp_feat_set] = f'{input_dir}' + \
                                                 '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-' + '{feat_set}.dat'

                    # obtain results on pparam_dict and bparam_dict by the detector
                    conduct_comparison_experiment(detector_name=detector_name,
                                                  srcIP=srcIP,
                                                  prop_feat=prop_feat,
                                                  prop_file=prop_file,
                                                  bparam_dict=OrderedDict(bparam_dict),
                                                  input_dir=input_dir,
                                                  output_dir=output_dir,
                                                  norm_method=norm_method,
                                                  gridsearch_flg=gridsearch_flg,
                                                  q_fixed_iat=q_fixed_iat,
                                                  random_state=random_state, verbose=verbose)

                    del bparam_dict[samp_feat_set]


@execute_time
def main_experiment(experiment='ind', detector_lst=['GMM'], q_fixed_iat=0.9, q_sampling_rate=0.9,
                    dataset_name='CICIDS2017',
                    input_dir='input_data/CICIDS2017', output_dir='output_data',
                    norm_method=None, gridsearch_lst=[False],
                    sampling_lst='',
                    random_state=42, verbose=True):
    """

    :param experiment:
    :param detector_name:
    :param q_fixed_iat:
    :param input_dir:
    :param output_dir:
    :param norm_method:
    :param gridsearch_flg:
    :param random_state:
    :param verbose:
    :return:
    """
    if verbose:
        funcparams_dict = {'experiment': experiment, 'detector_lst': detector_lst,
                           'q_fixed_iat': q_fixed_iat, 'q_sampling_rate': q_sampling_rate,
                           'input_dir': input_dir, 'output_dir': output_dir,
                           'norm_method': norm_method, 'gridsearch_lst': gridsearch_lst,
                           'sampling_lst': sampling_lst,
                           'random_state': random_state, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=main_experiment.__name__)

    # Step 0: extract features from pcap and save the features to local files
    get_sampling_flg = True
    if get_sampling_flg:
        preprocess_flg = False
        if preprocess_flg:  # filter unrelated IPs and the results will be saved at 'multi-srcIPs' for smart-tv-roku-data
            print('\n')
            main_preprocess_pcap(dataset_name=dataset_name, input_dir=input_dir, overwrite=True)
        # to obtain the sampling_lst from pcap
        q_sampling_rate = q_sampling_rate
        print('\n')
        q_fixed_iat, sub_dir, q_sampling_rate, sampling_lst = main_pcap2features(experiment=experiment,
                                                                                 q_fixed_iat=q_fixed_iat,
                                                                                 q_sampling_rate=q_sampling_rate,
                                                                                 dataset_name=dataset_name)
        if experiment in ['ind', 'more']:
            srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
        elif experiment == 'mix':
            srcIP_lst = ['192.168.10.5-192.168.10.8-192.168.10.9-192.168.10.14-192.168.10.15']  # 17, 6.783957346747903
    else:
        if dataset_name == 'CICIDS2017':
            if experiment == 'ind':  # only Friday data
                q_sampling_rate = 0.6
                sub_dir = 'Friday-WorkingHours'
                sampling_lst = [0.013366915384928386, 1.2888627893784468e-05, 4.0084123611450195e-06,
                                0.004426524639129641,
                                0.005506066715016085]  # q_sampling_rate=0.6 for experiment = 'ind'
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
                srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']

            elif experiment == 'more':  # merged multi-days data
                q_sampling_rate = 0.1
                sub_dir = 'Merged-WorkingHours'
                sampling_lst = [2.0662943522135417e-07, 1.5894571940104166e-07, 1.7881393432617188e-07,
                                1.5058015522203947e-07,
                                1.5894571940104166e-07]  # q_sampling_rate=0.1 for experiment='more'
                srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
            elif experiment == 'mix':
                srcIP_lst = [
                    '192.168.10.5-192.168.10.8-192.168.10.9-192.168.10.14-192.168.10.15']  # 17, 6.783957346747903
                sub_dir = 'mix-WorkingHours'
                q_sampling_rate = 0.9
                sampling_lst = [6.783957346747903]
            else:
                raise ValueError(f'experiment: {experiment} is not implemented.')
        elif dataset_name == 'smart-tv-roku-data':
            q_sampling_rate = 0.9
            sub_dir = 'normal_anomaly'
            sampling_lst = [0.2941480266130889]  # q_sampling_rate=0.1 for experiment='more'

    sampling_tuple = (q_sampling_rate, sampling_lst)
    print(f'sampling_tuple: {sampling_tuple}')

    # Step 1: load features data and conduct the comparison experiment
    for gs_i, gridsearch_flg in enumerate(gridsearch_lst):  #
        print('\n\n' + '-' * 50 + f'gs_i: {gs_i}, gridsearch_flg: {gridsearch_flg}' + '-' * 50)
        for dt_i, detector_name in enumerate(detector_lst):
            # for dt_i, detector_name in enumerate(['GMM']):      # for testing
            print('\n' + '*' * 35 + f'dt_i: {dt_i}, detector_name: {detector_name}' + '*' * 35)
            for pf_i, prop_feat in enumerate(['IAT', 'FFT']):
                print('\n' + '+' * 25 + f'pf_i: {pf_i}, prop_feat: {prop_feat}' + '+' * 25)

                if dataset_name == 'CICIDS2017':
                    # for each IP, compare prop set and baseline set
                    # srcIP_lst = [ '192.168.10.8', '192.168.10.9', '192.168.10.15'] for fast test
                    # srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']

                    # only one prop_file, however, maybe multi-baseline files (Baseline 1 and Baseline 2)
                    prop_file = f'{input_dir}' + '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-IAT.dat'
                    # bparm_set params: might include multi-files
                    bparam_dict = {  # (key, value): key-feature set, value-file
                        # Baseline 1 features file
                        'StatBaseline': f'{input_dir}' + '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-{feat_set}-' \
                                                                                            'dim_10.dat',
                    }
                    for idx, srcIP in enumerate(srcIP_lst):
                        print('\n' + '%' * 15 + f'index: {idx}, srcIP: {srcIP}')

                        # raw Baseline 2 features file, flows are in different sizes
                        sampling = sampling_lst[idx]
                        sampling_type = 'rate'
                        samp_feat_set = f'SampBaseline-{sampling_type}' + f'_{sampling}-q_sampling_rate_{q_sampling_rate}'
                        # print(f'index: {idx}, srcIP: {srcIP}, samp_feat_set: {samp_feat_set}')
                        bparam_dict[samp_feat_set] = f'{input_dir}' + \
                                                     '/srcIP_{srcIP}/' + f'{sub_dir}' + '/srcIP_{srcIP}.pcap-' + '{feat_set}.dat'

                        # obtain results on pparam_dict and bparam_dict by the detector
                        conduct_comparison_experiment(experiment=experiment,
                                                      detector_name=detector_name,
                                                      srcIP=srcIP,
                                                      prop_feat=prop_feat,
                                                      prop_file=prop_file,
                                                      bparam_dict=OrderedDict(bparam_dict),
                                                      input_dir=input_dir,
                                                      output_dir=output_dir,
                                                      norm_method=norm_method,
                                                      gridsearch_flg=gridsearch_flg,
                                                      q_fixed_iat=q_fixed_iat,
                                                      random_state=random_state, verbose=verbose)

                        del bparam_dict[samp_feat_set]
                elif dataset_name == 'smart-tv-roku-data':
                    srcIP_lst = ['merged_normal_anomaly']
                    # only one prop_file, however, maybe multi-baseline files (Baseline 1 and Baseline 2)
                    prop_file = f'{input_dir}' + '/multi-srcIPs/' + f'{sub_dir}' + '/{srcIP}-IAT.dat'
                    # bparm_set params: might include multi-files
                    bparam_dict = {  # (key, value): key-feature set, value-file
                        # Baseline 1 features file
                        'StatBaseline': f'{input_dir}' + '/multi-srcIPs/' + f'{sub_dir}' + '/{srcIP}-{feat_set}-' \
                                                                                           'dim_10.dat',
                    }
                    for idx, srcIP in enumerate(srcIP_lst):
                        print('\n' + '%' * 15 + f'index: {idx}, srcIP: {srcIP}')

                        # raw Baseline 2 features file, flows are in different sizes
                        sampling = sampling_lst[idx]
                        sampling_type = 'rate'
                        samp_feat_set = f'SampBaseline-{sampling_type}' + f'_{sampling}-q_sampling_rate_{q_sampling_rate}'
                        # print(f'index: {idx}, srcIP: {srcIP}, samp_feat_set: {samp_feat_set}')
                        bparam_dict[samp_feat_set] = f'{input_dir}' + \
                                                     '/multi-srcIPs/' + f'{sub_dir}' + '/{srcIP}-' + '{feat_set}.dat'

                        # obtain results on pparam_dict and bparam_dict by the detector
                        conduct_comparison_experiment(experiment=experiment,
                                                      detector_name=detector_name,
                                                      srcIP=srcIP,
                                                      prop_feat=prop_feat,
                                                      prop_file=prop_file,
                                                      bparam_dict=OrderedDict(bparam_dict),
                                                      input_dir=input_dir,
                                                      output_dir=output_dir,
                                                      norm_method=norm_method,
                                                      gridsearch_flg=gridsearch_flg,
                                                      q_fixed_iat=q_fixed_iat,
                                                      random_state=random_state, verbose=verbose)

                        del bparam_dict[samp_feat_set]


if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     q_sampling_rate = 0.9  # default value
    # else:
    #     # q_sampling_rate = float(sys.argv[1])
    #     pass
    # exec_time = sys.argv[1]
    # if exec_time=='':
    #     exec_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    # input_dir=os.path.join('input_data', exec_time, 'CICIDS2017')

    q_sampling_rate = 0.9  # default value
    # dataset_name = 'smart-tv-roku-data'  # 'CICIDS2017'
    dataset_name = 'CICIDS2017'  # 'CICIDS2017'
    input_dir = os.path.join('input_data', f'q_sampling_rate_{q_sampling_rate}', dataset_name)

    overwrite = False
    if overwrite:
        if os.path.exists(input_dir):
            shutil.rmtree(input_dir)
        try:
            src = os.path.join('input_data', dataset_name)
            shutil.copytree(src=src, dst=input_dir)  # will call os.makedirs()
        except OSError as exc:  # python >2.5
            if exc.errno == errno.ENOTDIR:
                shutil.copy(src=src, dst=input_dir)
            else:
                raise

    experiment = 'ind'  # 1) ind: individual; 2) mix; 3) more: add more data
    main_experiment(experiment=experiment,
                    detector_lst=['GMM', 'OCSVM', 'KDE'],  # ['PCA'] for debug
                    gridsearch_lst=[True, False],  # [False, True],
                    dataset_name=dataset_name,
                    input_dir=input_dir,
                    output_dir=output_dir,
                    norm_method=norm_method,
                    q_fixed_iat=0.9,  # it impacts IAT/FFT/Baseline 2 (pcap2features)
                    q_sampling_rate=q_sampling_rate,
                    random_state=random_state,
                    verbose=verbose)
