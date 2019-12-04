"""
    Purpose:
        feature extraction and feature selection
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2


def select_sub_features_data(x_norm_train, sub_features_list):
    for idx, new_feature in enumerate(sub_features_list):
        if idx == 0:
            x_norm_train_sub = x_norm_train[:, new_feature]
            x_norm_train_sub = np.reshape(x_norm_train_sub, (x_norm_train_sub.shape[0], 1))
            continue
        else:
            x_norm_train_sub = np.concatenate(
                (x_norm_train_sub, np.reshape(x_norm_train[:, new_feature], (x_norm_train.shape[0], 1))), axis=1)

    return x_norm_train_sub


def feature_selection_with_sklearn(X, var=0.8, num_features=2):
    # clf = Pipeline([
    #     ('feature_selection', SelectFromModel(DecisionTreeClassifier())),
    #     ('classification', DecisionTreeClassifier())
    # ])
    # clf.fit(X, y)
    # print(clf.named_steps['classification'].feature_importances_)
    # clf.feature_importances_.index()
    X_new = SelectKBest(chi2, k=2)
    y = np.ones((X.shape[0],))
    X_new.fit(X, y)

    sel = VarianceThreshold(threshold=var)
    new_X = sel.fit_transform(X)

    features_descended_lst = {}
    for idx, v in enumerate(sel.variances_):
        features_descended_lst[idx] = v

    features_descended_lst = dict(sorted(features_descended_lst.items(), key=lambda x: x[1], reverse=True))

    sub_features_list = select_top_k_features(features_descended_lst, num_features=num_features)

    return sub_features_list


def select_top_k_features(feature_descended_dict, num_features=2):
    sub_features_list = []
    for i, (key, value) in enumerate(feature_descended_dict.items()):
        if i < num_features:
            sub_features_list.append(key)

    return sorted(sub_features_list)


def feature_selection_1(x_norm_train, num_features=2, corr_thres=0.5, show_flg=True):
    data_df = pd.DataFrame(data=x_norm_train)
    corr = data_df.corr(method='pearson')
    if show_flg:
        # Using Pearson Correlation
        plt.figure(figsize=(12, 10))
        # sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
        sns.heatmap(corr, annot=True, cmap=plt.cm.Blues)
        plt.show()

    features_descended_dict = {}
    cnt = 0
    try_times = 100
    while corr_thres >= 0.1 and corr_thres < 1.0:
        print(f'current corr_thres:{corr_thres}')
        # print(f'{corr.values[0,:]}')
        corr_tmp = corr
        columns = np.full((corr.shape[0],), True, dtype=bool)  # False means that this feature won't be selected.
        for i in range(corr_tmp.shape[0]):
            # if columns[i] == False:
            #     continue
            for j in range(i + 1, corr_tmp.shape[0]):
                if abs(corr_tmp.iloc[i, j]) > corr_thres or abs(corr_tmp.iloc[i, j]) == np.nan:
                    if columns[j]:
                        columns[j] = False

        for i, keep in enumerate(columns):
            if keep == True:
                features_descended_dict[i] = 1

        # features_descended_dict = dict(sorted(features_descended_dict.items(), key=lambda x: x[1], reverse=True))
        # print(f'{len(features_descended_dict.items())}, {features_descended_dict.items()}')

        if len(features_descended_dict.keys()) > num_features:
            sub_feature_lst = []
            for key, value in features_descended_dict.items():
                sub_feature_lst.append(key)

            print(f'1-current corr_thres:{corr_thres}')

            return sorted(sub_feature_lst[:num_features], reverse=False)

        elif len(features_descended_dict.keys()) < num_features:
            corr_thres -= 0.02
            cnt += 1
        else:
            print(f'2-current corr_thres:{corr_thres}')

            return sorted(features_descended_dict.keys(), reverse=False)

        if cnt > try_times:
            print(f'try more than {try_times} times.')
            break

    print(f'3-current corr_thres:{corr_thres}')
    return sorted(features_descended_dict.keys(), reverse=False)


def get_min_max_in_matrix(data_n_n, max_val=0):
    rows, cols = data_n_n.shape[0], data_n_n.shape[1]

    min_val = 10
    for i in range(rows):
        for j in range(i + 1, cols):
            if np.isnan(data_n_n[i][j]):
                continue
            if abs(data_n_n[i][j]) >= max_val:
                max_val = abs(data_n_n[i][j])
                # data_n_n[i][j] = np.nan
            if abs(data_n_n[i][j]) <= min_val:
                min_val = abs(data_n_n[i][j])
                # data_n_n[i][j] ='-'

    return data_n_n, min_val, max_val
