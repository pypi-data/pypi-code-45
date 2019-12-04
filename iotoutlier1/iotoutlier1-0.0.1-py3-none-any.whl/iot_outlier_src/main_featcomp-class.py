""" Main function for feature sets comparison.
    Measure metrics: ROC amd AUC

    1. Best parameters using grid search
    2. Rule of thumb

"""
# Authors: kun.bj@outlook.com
#
# License: xxx

# 1. system and built-in libraries

# 2. thrid-part libraries
from colorama import Fore, Style

# 3. local libraries
from _config import Parameter
from data_process.data_factory import DataFactory
from detector.detector_factory import DetectorFactory
from utils.display_factory import DisplayFactory
from utils.tool import pprint, execute_time


class MainFactory:

    def __init__(self, params={}):
        self.params = params
        pprint(self.params, name=MainFactory.__name__)  # print common parameters
        self.dataset_name = self.params['dataset_name']
        self.detector_name = self.params['detector_name']

    def run(self):
        print('1. Data process')
        dt = DataFactory(dataset_name=self.dataset_name, params=self.params)  # update params
        dt.run()  # 1) pcap2features, 2) get train set and test set 3) update params

        print('2. Algorithm analysis')
        dtr = DetectorFactory(detector_name=self.detector_name, dataset_dict=dt.dataset_dict,
                              params=self.params)  # update params
        dtr.run()  # Execute algorithm

        print('3. Result display')
        dp = DisplayFactory(dataset_dict=dtr.dataset_dict, params=self.params)
        dp.run()


@execute_time
def main(dataset_lst=['CICIDS2017', 'SMTV'], expt_lst=['INDV', 'AGMT'], detector_lst=['OCSVM', 'KDE'],
         gs_lst=[False, True]):
    for i_ds, ds_name in enumerate(dataset_lst):
        print('\n' + '+' * 35 + f' {i_ds+1}/{len(dataset_lst)}({dataset_lst}), '
                                f'current dataset_name: {ds_name} ' + '+' * 35)
        for i_ep, ep_name in enumerate(expt_lst):
            print('\n' + '%' * 30 + f' {i_ep+1}/{len(expt_lst)}({expt_lst}), '
                                    f'current experiment_name: {ep_name} ' + '+' * 30)
            # Todo: 'Decouple Pcap from DataFacotory'
            for i_dt, dt_name in enumerate(detector_lst):
                print('\n' + '*' * 25 + f' {i_dt+1}/{len(detector_lst)}({detector_lst}), '
                                        f'current detector_name: {dt_name} ' + '*' * 25)
                for i_gs, gs_flg in enumerate(gs_lst):  #
                    print('\n' + '-' * 20 + f' {i_gs+1}/{len(gs_lst)}({gs_lst}), '
                                            f'current gridsearch_flg: {gs_flg} ' + '-' * 20)
                    try:
                        params = Parameter(dataset_name=ds_name, expt_name=ep_name, detector_name=dt_name,
                                           gs_flg=gs_flg).params
                        mf = MainFactory(params=params)
                        mf.run()
                    except Exception as e:
                        print(Fore.RED +f'***  Exception ({e}) happens'+f' with params: {params}')
                        print(Style.RESET_ALL)      # reset color. Otherwise, all the print will use the red color


if __name__ == '__main__':
    main(dataset_lst=['DEMO_CICIDS2017', ],  # ['DEMO_CICIDS2017', 'SMTV'],
         expt_lst=['AGMT','INDV',  'MIX', ],
         detector_lst=['AE','GMM', 'OCSVM'],  #
         gs_lst=[True, False])

    main(dataset_lst=['CICIDS2017', 'SMTV'],  # ['DEMO_CICIDS2017', 'SMTV'],
         expt_lst=['AGMT', 'MIX', 'INDV'],
         detector_lst=['AE','GMM', 'OCSVM', 'KDE'],  # AE
         gs_lst=[True, False])
