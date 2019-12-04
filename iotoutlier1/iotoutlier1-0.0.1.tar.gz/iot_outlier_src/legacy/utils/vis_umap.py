# -*- coding: utf-8 -*-
"""
    visualize high-dimensions data by T-SNE

    refer to :
            1 http://alexanderfabisch.github.io/t-sne-in-scikit-learn.html
            2 http://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#sphx-glr-auto-examples-manifold-plot-compare-methods-py
"""
import os
import pickle
from collections import OrderedDict

import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from data_process import IAT_to_fixed_out
from legacy.experiment_class import Experiment
from legacy.main_featcomp import merge_files_to_one
from legacy.utils import print_values

# from preprocess.data_preprocess import load_data, remove_special_labels
# from numpy_load_and_arff import load_npy_data

rcParams.update({'figure.autolayout': True})

import umap.umap_ as umap


def vis_high_dims_data_umap_2(X, y, show_label_flg=False, title=''):
    """

    :param X:  features
    :param y:  labels
    :param show_label_flg :
    :return:
    """
    # res_umap=umap.UMAP(n_neighbors=5,min_dist=0.3, metric='correlation').fit_transform(X,y)
    res_umap = umap.UMAP(n_neighbors=50, min_dist=0.8, metric='correlation', random_state=42).fit_transform(X, y)

    if not show_label_flg:
        # plt.figure(figsize=(10, 5))
        fig, ax = plt.subplots(figsize=(12, 7))
        plt.scatter(res_umap[:, 0], res_umap[:, 1], c=y, cmap=plt.cm.get_cmap("jet", 8), alpha=0.8)
        # cbar = fig.colorbar(cax, ticks=[1, 2, 3, 4, 5, 6, 7, 8], orientation='horizontal')
        cbar = fig.colorbar(ax, ticks=[1, 2, 3, 4, 5, 6, 7, 8])
        cbar.ax.set_xticklabels(
            ['Google', 'Twitter', 'Youtube', 'Outlook', 'Github', 'Facebook', 'Slack', 'Bing'])  # horizontal colorbar

        # plt.colorbar(ticks=range(0,9))
        plt.setp(ax, xticks=[], yticks=[])
        # plt.title('umap results')
        plt.show()
    else:
        plot_with_labels(X, y, res_umap, "UMAP", min_dist=2.0)


def vis_high_dims_data_umap(X, y, show_label_flg=False, title=''):
    """

    :param X:  features
    :param y:  labels
    :param show_label_flg :
    :return:
    """
    # res_umap=umap.UMAP(n_neighbors=5,min_dist=0.3, metric='correlation').fit_transform(X,y)
    res_umap = umap.UMAP(n_neighbors=30, min_dist=0.12, spread=1.8, metric='correlation').fit_transform(X, y)

    if not show_label_flg:
        plt.figure(figsize=(10, 5))
        plt.scatter(res_umap[:, 0], res_umap[:, 1], c=y, cmap=plt.cm.get_cmap("jet", 7), alpha=0.7)
        plt.colorbar(ticks=range(7))
        plt.title(title)
        plt.savefig(title + "_umap.pdf", dpi=400)
        plt.show()
    else:
        plot_with_labels(X, y, res_umap, "UMAP", min_dist=2.0)


def vis_high_dims_data_t_sne(X, y, show_label_flg=False, title=''):
    """

    :param X:  features
    :param y:  labels
    :param show_label_flg :
    :return:
    """
    res_tsne = TSNE(n_components=2, verbose=2, learning_rate=1, n_iter=500, random_state=0).fit_transform(X, y)

    if not show_label_flg:
        plt.figure(figsize=(10, 5))
        plt.scatter(res_tsne[:, 0], res_tsne[:, 1], c=y, cmap=plt.cm.get_cmap("jet", 10), alpha=0.7)
        plt.colorbar(ticks=range(10))
        plt.title(title)
        plt.savefig("t_SNE.jpg", dpi=400)
    else:
        plot_with_labels(X, y, res_tsne, "t-SNE", min_dist=20.0)


def vis_high_dims_data_pca(X, y, show_label_flg=False, title=''):
    """

    :param X:  features
    :param y:  labels
    :param show_label_flg :
    :return:
    """
    res_tsne = PCA(n_components=2, random_state=0).fit_transform(X, y)

    if not show_label_flg:
        plt.figure(figsize=(10, 5))
        plt.scatter(res_tsne[:, 0], res_tsne[:, 1], c=y, cmap=plt.cm.get_cmap("jet", 10), alpha=0.7)
        plt.colorbar(ticks=range(10))
        plt.title(title)
        plt.show()
    else:
        plot_with_labels(X, y, res_tsne, "pca", min_dist=20.0)


def demo_t_sne():
    """
        display iris_data by TSNE
    :return:
    """

    from sklearn.datasets import load_iris
    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE
    import matplotlib.pyplot as plt

    iris = load_iris()
    X_tsne = TSNE(learning_rate=100, n_components=2, perplexity=10, verbose=2).fit_transform(iris.data)
    X_pca = PCA().fit_transform(iris.data)

    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=iris.target)
    plt.title('TSNE')
    plt.subplot(122)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target)
    plt.title('PCA')
    plt.show()


def plot_with_labels(X, y, X_embedded, name, min_dist=10.0):
    """
        plot with labels
    :param X:
    :param y:
    :param X_embedded: Fit X into an embedded space and return that transformed output.
    :param name: title
    :param min_dist: min distance
    :return:
    """
    import matplotlib
    from matplotlib.pyplot import figure, title, axes, setp, subplots_adjust, scatter, cm
    import numpy as np
    # Plotting function
    matplotlib.rc('font', **{'family': 'sans-serif',
                             'weight': 'bold',
                             'size': 18})
    matplotlib.rc('text', **{'usetex': True})

    fig = figure(figsize=(10, 10))
    ax = axes(frameon=False)
    title("\\textbf{MNIST dataset} -- Two-dimensional "
          "embedding of 70,000 handwritten digits with %s" % name)
    setp(ax, xticks=(), yticks=())
    subplots_adjust(left=0.0, bottom=0.0, right=1.0, top=0.9,
                    wspace=0.0, hspace=0.0)
    scatter(X_embedded[:, 0], X_embedded[:, 1],
            c=y, marker="x")

    if min_dist is not None:
        from matplotlib import offsetbox
        shown_images = np.array([[15., 15.]])
        indices = np.arange(X_embedded.shape[0])
        np.random.shuffle(indices)
        for i in indices[:5000]:
            dist = np.sum((X_embedded[i] - shown_images) ** 2, 1)
            if np.min(dist) < min_dist:
                continue
            shown_images = np.r_[shown_images, [X_embedded[i]]]
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(X[i].reshape(28, 28),
                                      cmap=cm.gray_r), X_embedded[i])
            ax.add_artist(imagebox)
    # plt.show()
    plt.savefig("t_SNE.jpg", dpi=400)


def change_labels(y):
    for i in range(len(y)):
        if y[i] == 0:
            y[i] = 'a'
        elif y[i] == 1:
            y[i] = 'b'
        elif y[i] == 2:
            y[i] = 'c'
        elif y[i] == 3:
            y[i] = 'd'
        else:
            pass


def main_individual(srcIP='',
                    prop_param_dict={},
                    base_param_dict={},
                    norm_method='std',
                    grid_search_flg=True,
                    data_aug=False,
                    random_state=42,
                    quant=0.9
                    ):
    """

    :param srcIP_lst:
    :param detector_name:  'OCSVM', 'GMM', 'PCA', 'KDE'
    :param norm_method:  none: without normalization, otherwise, 'min-max' or 'std'
    :param grid_search_flg: True: to pick the best parameters of the detector
    :param data_aug:
    :param random_state:  to reproduce the results
    :return:
    """
    detector_name = prop_param_dict['detector_name']
    print_values(detector_name=detector_name, norm_method=norm_method, data_aug=data_aug, random_state=random_state,
                 grid_search_flg=grid_search_flg)

    result_dict_lst = OrderedDict()  # store the results: {feat_set: results of the feat_set}

    # 1. obtain results (such as ROC and AUC) of IAT or FFT
    prop_set = prop_param_dict['feat_set']  # proposed features:  IAT or FFT
    fft_part = prop_param_dict['fft_part']  # only for FFT: 'real' or 'real+imaginary'
    iat_file = prop_param_dict['iat_file'].format(srcIP=srcIP)
    prop_file, fft_bin = IAT_to_fixed_out(input_file=iat_file, feat_set=prop_set, quant=quant,
                                          fft_part=fft_part, overwrite=True)

    prop = Experiment(input_file=prop_file, feat_set=prop_set, norm_method=norm_method, random_state=random_state)
    # result_dict = prop.run(detector_name=detector_name,
    #                        X_train=prop.X_train, y_train=prop.y_train,
    #                        X_test=prop.X_test, y_test=prop.y_test,
    #                        grid_search_flg=grid_search_flg)
    # result_dict_lst[prop_set] = result_dict
    size = 3000
    if len(prop.X_train) > size:
        X = prop.X_train[:size, :]
        y = prop.y_train[:size, ]
    vis_high_dims_data_umap(X, y, show_label_flg=False, title=f'{prop_set}, srcIP:{srcIP}')

    # 2. obtain results (such as ROC and AUC) of Baseline
    base_set = base_param_dict['feat_set']
    base_file = base_param_dict['base_file'].format(srcIP=srcIP, feat_set=base_set)
    base = Experiment(input_file=base_file, feat_set=base_set, norm_method=norm_method, random_state=random_state)
    # result_dict = base.run(detector_name=detector_name,
    #                        X_train=base.X_train, y_train=base.y_train,
    #                        X_test=base.X_test, y_test=base.y_test,
    #                        grid_search_flg=grid_search_flg)
    # result_dict_lst[base_set] = result_dict
    if len(base.X_train) > size:
        X = base.X_train[:size, :]
        y = base.y_train[:size, ]
    vis_high_dims_data_umap(X, y, show_label_flg=False, title=f'{base_set}, srcIP:{srcIP}')

    return result_dict_lst


def merge_files_to_one(srcIP_lst, sub_file='', feat_set='', mixed_file=''):
    if os.path.exists(mixed_file):
        os.remove(mixed_file)
    with open(mixed_file, 'wb') as out_hdl:
        for idx, srcIP in enumerate(srcIP_lst):
            sub_file_tmp = sub_file.format(srcIP=srcIP, feat_set=feat_set)
            print(f'*index: {idx}, sub_file: {sub_file_tmp}')
            with open(sub_file_tmp, 'rb') as in_hdl:
                fids, features, labels = pickle.load(in_hdl)
                pickle.dump((fids, features, labels), out_hdl)

    return mixed_file


def main():
    experiment = 'ind'  # ind: individual; mix; more: add more data
    srcIP_lst = ['192.168.10.5', '192.168.10.8', '192.168.10.9', '192.168.10.14', '192.168.10.15']
    detector_name = 'KDE'  # GMM, OCSVM, PCA, KDE
    prop_param_dict = {'detector_name': '{}'.format(detector_name),
                       'iat_file': 'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat',
                       # raw IATs file, which is used to obtain IAT and FFT features with fixed size
                       'feat_set': 'IAT',
                       'fft_part': 'real'
                       }
    base_param_dict = {'detector_name': '{}'.format(detector_name),
                       'base_file': 'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_{feat_set}_' \
                                    'dimension_10.dat',  # baseline features file
                       'feat_set': 'Baseline',
                       }
    quant = 0.90  # to obtain fft_bin from IATs data
    if experiment == 'ind':
        for idx, srcIP in enumerate(srcIP_lst):
            print(f'\n*index: {idx}, srcIP: {srcIP}, quant (for obtaining fft_bin): {quant}')
            result_dict_lst = main_individual(srcIP, prop_param_dict=prop_param_dict,
                                              base_param_dict=base_param_dict, quant=quant)  # individual ip analysis
    elif experiment == 'mix':  # merge 5 IPs in one
        mixed_srcIP = '-'.join(srcIP_lst)
        iat_file = 'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_IAT.dat'  # raw IATs file
        mixed_iat_file = f'input_data/CICIDS2017/srcIP_{mixed_srcIP}/Friday-WorkingHours/srcIP_{mixed_srcIP}.pcap_IAT.dat'  # raw IATs file
        mixed_iat_file = merge_files_to_one(srcIP_lst, sub_file=iat_file, mixed_file=mixed_iat_file)
        prop_param_dict['iat_file'] = mixed_iat_file

        base_set = base_param_dict['feat_set']
        feat_set = base_set
        mixed_base_file = f'input_data/CICIDS2017/srcIP_{mixed_srcIP}/Friday-WorkingHours/srcIP_{mixed_srcIP}.pcap_{feat_set}.dat'  # raw IATs file
        base_file = 'input_data/CICIDS2017/srcIP_{srcIP}/Friday-WorkingHours/srcIP_{srcIP}.pcap_{feat_set}_' \
                    f'dimension_10.dat'
        mixed_base_file = merge_files_to_one(srcIP_lst, sub_file=base_file, feat_set=base_set,
                                             mixed_file=mixed_base_file)
        base_param_dict['base_file'] = mixed_base_file
        result_dict_lst = main_individual(srcIP=mixed_srcIP, prop_param_dict=prop_param_dict,
                                          base_param_dict=base_param_dict, quant=quant)  # individual ip analysis


    elif experiment == 'more_data':
        pass
        # main_more_data()  # add Monday data to Friday, and the results are saved in Monday folder


if __name__ == '__main__':
    main()
