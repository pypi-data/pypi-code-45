""" Main function for feature set comparison.
    Measure metrics: ROC amd AUC

    1. best parameters using grid search
    2. rule of thumb

"""
# Authors: kun.bj@outlook.com
#
# License: xxx

from collections import OrderedDict
from copy import deepcopy

from _config import *
from data_process import IAT_to_fixed_out, merge_files_to_one, transform_samp_baseline_to_fixed_out
from legacy.experiment_class import IndividualExperiment
from utils.tool import pprint, execute_time
from utils.visual import plot_roc_auc


def conduct_comparison_experiment(detector_name='',
                                  srcIP='',
                                  pparam_dict=OrderedDict(),
                                  bparam_dict=OrderedDict(),
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
            'quant': quant,
            'norm_method': norm_method,
            'gridsearch_flg': gridsearch_flg,
            'random_state': random_state,
            'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=conduct_comparison_experiment.__name__)

    # get results on pparam_dict and bparam_dict by the detector
    result_dict_dict = OrderedDict()  # store the dict results: {feat_set: results of the feat_set}
    param_limit = 50  # # limit the length of the params string, which is used for file name

    # 1. obtain results (such as ROC and AUC) of IAT or FFT on pparam_dict
    prop_set = pparam_dict['feat_set']  # proposed features:  IAT or FFT
    fft_part = pparam_dict['fft_part']  # only for FFT: 'real' or 'real+imaginary'
    iat_file = pparam_dict['iat_file'].format(input_dir=input_dir, srcIP=srcIP)

    # 1.1) get the fixed size of IAT or FFT based on the given quantile (default 0.9)
    prop_file, fft_bin = IAT_to_fixed_out(input_file=iat_file, feat_set=prop_set, quant=quant,
                                          fft_part=fft_part, overwrite=True, verbose=verbose)

    # 1.2) get the results
    prop = IndividualExperiment(input_file=prop_file, feat_set=prop_set, norm_method=norm_method,
                                random_state=random_state)
    result_dict = prop.run(detector_name=detector_name,
                           X_train=prop.X_train, y_train=prop.y_train,
                           X_test=prop.X_test, y_test=prop.y_test,
                           gridsearch_flg=gridsearch_flg)

    # 1.3) save the built detector to file
    params_dict = deepcopy(prop.detector.get_params())
    if 'means_init' in params_dict.keys():  # avoid too long name in the output_file name
        del params_dict['means_init']
    params_str = str(list(params_dict.values()))
    if len(params_str) > param_limit:  # limit the length of the output_file name
        params_str = params_str[:param_limit]
    # os.path.join() prop_file.replace(old='input', new='output')
    propmodel_file = f'{output_dir}/{prop_file}_{detector_name}_{str(params_str)}.joblib'
    propmodel_file = prop.dump_model(prop.detector, model_file=propmodel_file)
    result_dict_dict[prop_set] = result_dict  # store the result on prop_set

    # 2. obtain results (such as ROC and AUC) of Baseline
    base_set = bparam_dict['feat_set']
    base_file = bparam_dict['base_file'].format(input_dir=input_dir, srcIP=srcIP, feat_set=base_set)

    # 2.1) Baseline has the fixed features. No need to use IAT_to_fixed_out()

    # 2.2) get the results on bparam_dict
    base = IndividualExperiment(input_file=base_file, feat_set=base_set,
                                norm_method=norm_method,
                                random_state=random_state)
    result_dict = base.run(detector_name=detector_name,
                           X_train=base.X_train, y_train=base.y_train,
                           X_test=base.X_test, y_test=base.y_test,
                           gridsearch_flg=gridsearch_flg)

    # 2.3) save the detector to file
    params_dict = deepcopy(base.detector.get_params())
    if 'means_init' in params_dict.keys():
        del params_dict['means_init']
    params_str = str(list(params_dict.values()))
    if len(params_str) > param_limit:  # limit the length of the output_file name
        params_str = params_str[:param_limit]
    basemodel_file = f'{output_dir}/{base_file}_{detector_name}_{str(params_str)}.joblib'
    basemodel_file = base.dump_model(base.detector, model_file=basemodel_file)
    result_dict_dict[base_set] = result_dict  # store the result on base_set

    for i, (samp_base_set, samp_base_file) in enumerate(bparam_dict.items()):
        if samp:
            continue
        # 3. obtain results (such as ROC and AUC) of Baseline 2
        samp_base_file = samp_base_file.format(input_dir=input_dir, srcIP=srcIP, feat_set=samp_base_set)

        # 3.1) get the fixed size (fft_bin) for sampling baseline
        base_fixed_file = transform_samp_baseline_to_fixed_out(input_file=samp_base_file, fft_bin=fft_bin,
                                                               overwrite=True, verbose=verbose)
        # 3.2) get the results on bparam_dict
        samp_base = IndividualExperiment(input_file=base_fixed_file, feat_set=samp_base_set,
                                         norm_method=norm_method,
                                         random_state=random_state)
        result_dict = samp_base.run(detector_name=detector_name,
                                    X_train=samp_base.X_train, y_train=samp_base.y_train,
                                    X_test=samp_base.X_test, y_test=samp_base.y_test,
                                    gridsearch_flg=gridsearch_flg)

        # 2.3) save the detector to file
        params_dict = deepcopy(samp_base.detector.get_params())
        if 'means_init' in params_dict.keys():
            del params_dict['means_init']
        params_str = str(list(params_dict.values()))
        if len(params_str) > param_limit:  # limit the length of the output_file name
            params_str = params_str[:param_limit]
        samp_base_model_file = f'{output_dir}/{base_fixed_file}_{detector_name}_{str(params_str)}.joblib'
        samp_base_model_file = samp_base.dump_model(samp_base.detector, model_file=samp_base_model_file)
        result_dict_dict[samp_base_set] = result_dict  # store the result on samp_base_set

    # 3 save all result in pdf
    if pparam_dict['feat_set'] == 'FFT':
        path_name = pparam_dict['feat_set'] + '_' + pparam_dict['fft_part']
    else:
        path_name = pparam_dict['feat_set']
    output_file = f'{output_dir}/{prop_file}_{detector_name}_{path_name}_{str(params_str)}.pdf'
    plot_roc_auc(result_dict_dict, output_file=output_file, title=f'{detector_name}, srcIP:{srcIP}')

    return result_dict_dict, propmodel_file, basemodel_file, samp_base_model_file


@execute_time
def main(experiment='ind', detector_name='GMM', quant=0.9, input_dir='input_data/CICIDS2017', output_dir='output_data',
         norm_method=None, gridsearch_flg=False, sampling_tuple={}, random_state=42, verbose=True):
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
                           'quant': quant, 'input_dir': input_dir, 'output_dir': output_dir,
                           'norm_method': norm_method, 'gridsearch_flg': gridsearch_flg,
                           'sampling_tuple': sampling_tuple,
                           'random_state': random_state, 'verbose': verbose}
        pprint(OrderedDict(funcparams_dict), name=main.__name__)

    if experiment == 'ind':
        # for each IP, compare prop set and baseline set
        srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']

        pparam_dict = {
            # raw IATs file, which is used to obtain IAT and FFT features with fixed size
            'iat_file': '{input_dir}/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-IAT.dat',
            'feat_set': 'IAT',  # IAT or FFT
            'fft_part': 'real'  # real or real + imaginary
        }

        bparam_dict = {
            # Baseline 1 features file
            'base_file': '{input_dir}/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-{feat_set}-' \
                         'dim_10.dat',
            'feat_set': 'StatBaseline'  # Baseline 1, with fixed sizes of flows
        }
        for i, (sampling_type, sampling) in enumerate(sampling_tuple):
            # Baseline 2 features file with different flows size
            samp_feat_set = f'samp_{sampling_type}_{sampling}_feat_set'

            bparam_dict[f'samp_{sampling_type}_{sampling}_base_file'] = \
                '{input_dir}/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-{feat_set}-' \
                + f'{sampling_type}_{sampling}.dat'
            bparam_dict[samp_feat_set] = 'Samp_{sampling_type}_{sampling}_Baseline'

        for idx, srcIP in enumerate(srcIP_lst):
            print(f'\n*index: {idx}')
            # get results on pparam_dict and bparam_dict by the detector
            conduct_comparison_experiment(detector_name=detector_name,
                                          srcIP=srcIP,
                                          pparam_dict=OrderedDict(pparam_dict),
                                          bparam_dict=OrderedDict(bparam_dict),
                                          norm_method=norm_method,
                                          gridsearch_flg=gridsearch_flg,
                                          quant=quant,
                                          random_state=random_state)
            # break

    elif experiment == 'mix':
        # merge 5 IPs in one

        srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']

        # 1. get mixed data first
        pparam_dict = {
            'iat_file': '',
            # raw IATs file, which is used to obtain IAT and FFT features with fixed size
            'feat_set': 'IAT',
            'fft_part': 'real'
        }
        mixed_srcIP = '-'.join(srcIP_lst)
        iat_file = '{input_dir}/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-IAT.dat'  # raw IATs file
        propfile_lst = [iat_file.format(input_dir=input_dir, srcIP=srcIP) for srcIP in srcIP_lst]
        mixed_iat_file = f'{input_dir}/srcIP_{mixed_srcIP}/Friday-WorkingHours/srcIP_{mixed_srcIP}.pcap-IAT.dat'  # raw IATs file
        mixed_iat_file = merge_files_to_one(propfile_lst, mixed_file=mixed_iat_file)
        pparam_dict['iat_file'] = mixed_iat_file

        bparam_dict = {
            'base_file': '',
            'feat_set': 'Baseline',
        }
        base_set = bparam_dict['feat_set']
        feat_set = base_set
        mixed_base_file = f'{input_dir}/srcIP_{mixed_srcIP}/Friday-WorkingHours/srcIP_{mixed_srcIP}.pcap-{feat_set}.dat'  # raw IATs file
        base_file = '{input_dir}/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-{feat_set}-' \
                    f'dim_10.dat'
        basefile_lst = [base_file.format(input_dir=input_dir, srcIP=srcIP, feat_set=feat_set) for srcIP in srcIP_lst]
        mixed_base_file = merge_files_to_one(file_lst=basefile_lst, mixed_file=mixed_base_file)
        bparam_dict['base_file'] = mixed_base_file

        # 2. get results on pparam_dict and bparam_dict by the detector
        conduct_comparison_experiment(detector_name=detector_name,
                                      srcIP=mixed_srcIP,
                                      pparam_dict=pparam_dict,
                                      bparam_dict=bparam_dict,
                                      norm_method=norm_method,
                                      gridsearch_flg=gridsearch_flg,
                                      quant=quant,
                                      random_state=random_state)

    elif experiment == 'more':
        # add Monday data to Friday, and the results are saved in Monday folder

        srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']

        # 1. get mixed data first
        pparam_dict = {
            'iat_file': '',
            # raw IATs file, which is used to obtain IAT and FFT features with fixed size
            'feat_set': 'FFT',  # proposed features:  IAT or FFT
            'fft_part': 'real'  # only for FFT: 'real' or 'real+imaginary'
        }
        bparam_dict = {
            'base_file': '',
            'feat_set': 'Baseline',
        }

        for idx, srcIP in enumerate(srcIP_lst):
            print(f'\n*index: {idx}')

            # 1. get mixed data first: mix Monday and Friday data
            iat_file = f'{input_dir}/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-IAT.dat'  # raw IATs file
            iat_file_2 = f'{input_dir}/srcIP_{srcIP}/Monday-WorkingHours/srcIP_{srcIP}.pcap-IAT.dat'  # raw IATs file
            propfile_lst = [iat_file, iat_file_2]
            mixed_iat_file = iat_file_2 + '-more_data.dat'
            mixed_iat_file = merge_files_to_one(propfile_lst, mixed_file=mixed_iat_file)
            pparam_dict['iat_file'] = mixed_iat_file

            base_set = bparam_dict['feat_set']
            base_file = f'{input_dir}/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap-{base_set}-' \
                        f'dim_10.dat'  # baseline features file
            base_file_2 = f'{input_dir}/srcIP_{srcIP}/Monday-WorkingHours/srcIP_{srcIP}.pcap-{base_set}-' \
                          f'dim_10.dat'  # baseline features file
            basefile_lst = [base_file, base_file_2]
            mixed_base_file = base_file_2 + '-more_data.dat'
            mixed_base_file = merge_files_to_one(basefile_lst, mixed_file=mixed_base_file)
            bparam_dict['base_file'] = mixed_base_file

            # 2. get results on pparam_dict and bparam_dict by the detector
            conduct_comparison_experiment(detector_name=detector_name,
                                          srcIP=srcIP,
                                          pparam_dict=OrderedDict(pparam_dict),
                                          bparam_dict=OrderedDict(bparam_dict),
                                          norm_method=norm_method,
                                          gridsearch_flg=gridsearch_flg,
                                          quant=quant,
                                          random_state=random_state)


if __name__ == '__main__':
    # if len(sys.argv) < 1:
    #   #     sys.exit("Usage: python3 {} [pcap_file] [labels_csv] [FFT bins] "
    #              "[num pkt thresh] [output_file] [do_subflows TRUE|FALSE]".format(sys.argv[0]))
    # detector_name = sys.argv[1]
    detector_name = 'KDE'  # GMM, OCSVM, PCA, KDE
    experiment = 'ind'  # ind: individual; mix; more: add more data
    quant = 0.90  # to obtain fft_bin from raw IATs data using np.quantile (IATs, q=0.9)
    sampling_tuple = (('number', 2), ('number', 5), ('number', 10), ('interval', 0.1), ('interval', 0.01))
    # sampling_type = ['number', 'number', 'number', 'interval']   # For baseline 2, sampling rate features
    # sampling = []
    # sampling_type = 'interval'  # For baseline 2, sampling rate features
    # sampling = 0.01

    main(experiment=experiment,
         detector_name=detector_name,
         quant=quant,
         input_dir=input_dir,
         output_dir=output_dir,
         norm_method=norm_method,
         gridsearch_flg=gridsearch_flg,
         sampling_tuple=sampling_tuple,
         random_state=random_state,
         verbose=verbose)
