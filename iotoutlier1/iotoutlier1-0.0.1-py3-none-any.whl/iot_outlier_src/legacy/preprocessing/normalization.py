"""
   Purpose:

    several standard data normalization techniques such as min-max, softmax, z-score, decimal scaling, box-cox and etc
"""


def normalize_data(np_arr, eplison=10e-4):
    """

    :param np_arr:
    :param eplison: handle with 0.
    :return:
    """
    min_val = np.min(np_arr, axis=0)  # X
    max_val = np.max(np_arr, axis=0)
    range_val = (max_val - min_val)
    if not range_val.all():  # Returns True if all elements evaluate to True.
        for i in range(len(range_val)):
            if range_val[i] == 0.0:
                range_val[i] += eplison
    print('range_val is ', range_val)
    norm_data = (np_arr - min_val) / range_val

    return norm_data


def normalize_data_min_max(np_arr, eplison=10e-4, min_val=[], max_val=[], no_normalized_features_idx=[]):
    """

    :param np_arr:
    :param eplison: handle with 0.
    :return:
    """
    if len(min_val) == 0 or len(max_val) == 0:
        print(f'len(min_val) = {len(min_val)}, len(max_val) = {len(max_val)}')
        min_val = np.min(np_arr, axis=0)
        max_val = np.max(np_arr, axis=0)

    range_val = (max_val - min_val)

    if len(no_normalized_features_idx) == 0:
        if not range_val.all():  # Returns True if all elements evaluate to True.
            for i in range(len(range_val)):
                if range_val[i] == 0.0:
                    range_val[i] += eplison
        print('range_val is ', range_val)
        norm_data = (np_arr - min_val) / range_val
    else:
        norm_data = []
        for i in range(np_arr.shape[1]):
            val = np_arr[:, i]
            if i not in no_normalized_features_idx:
                if range_val[i] == 0.0:
                    range_val[i] += eplison
                val = (val - min_val[i]) / range_val[i]
            norm_data.append(val)

        norm_data = np.asarray(norm_data, dtype=float).transpose()

    return norm_data, min_val, max_val


def normalizate_data_with_sigmoid(np_arr, eplison=10e-4):
    """

    :param np_arr:
    :param eplison: handle with 0.
    :return:
    """
    min_val = np.min(np_arr, axis=0)  # X
    max_val = np.max(np_arr, axis=0)
    range_val = (max_val - min_val)
    if not range_val.all():  # Returns True if all elements evaluate to True.
        for i in range(len(range_val)):
            if range_val[i] == 0.0:
                range_val[i] += eplison
    print('range_val is ', range_val)
    norm_data = []
    for i in range(np_arr.shape):
        norm_data.append(list(map(lambda x: 1 / (1 + np.exp(-(x))), np_arr)))
    # norm_data = list(map(lambda x: np.exp(-(x)), np_arr))
    norm_data = np.asarray(norm_data, dtype=float)

    return norm_data


def normalizate_data_with_u_std(np_arr, u_std_dict={'u': 0.5, 'std': 1.0}):
    """

    :param np_arr:
    :param u_std_dict: {'u':0.5,'std':1.0}
    :return:
    """
    # u_val = np.mean(np_arr, axis=0)  # X
    # std_val = np.std(np_arr, axis=0)

    norm_data = (np_arr - u_std_dict['u']) / u_std_dict['std']

    return norm_data


# from utils.load_data import z_score_np
import numpy as np
from sklearn.metrics import confusion_matrix


def z_score_np(data_np, mu=[], d_std=[]):
    if len(mu) == 0 or len(d_std) == 0:
        print(f'len(mu) = {len(mu)}, len(d_std) = {len(d_std)}')
        mu = data_np.mean(axis=0)
        d_std = data_np.std(axis=0)
    # avoid d_std equals 0.
    for idx in range(d_std.shape[0]):
        if d_std[idx] == 0:
            print(f'the variance of the {idx}-th feature is 0.')
            d_std[idx] = d_std[idx] + np.math.exp(-8)

    data_np = (data_np - mu) / d_std

    return data_np, mu, d_std


def z_score_np_1(data_np, mu=[], d_std=[]):
    # def min_max_np(data_np, d_min=[], d_max=[]):
    d_min = mu
    d_max = d_std

    if len(d_min) == 0 or len(d_max) == 0:
        print(f'len(d_min) = {len(d_min)}, len(d_max) = {len(d_max)}')
        d_min = data_np.min(axis=0)
        d_max = data_np.max(axis=0)

    diff = d_max - d_min
    # avoid diff equals 0.
    for idx in range(diff.shape[0]):
        if diff[idx] == 0:
            print(f'the range of the {idx}-th feature is 0.')
            diff[idx] = diff[idx] + np.math.exp(-8)

    data_np = (data_np - d_min) / diff * (1 - (-1)) + (-1)  # normalize the result to [-1,1]

    return data_np, d_min, d_max


def calucalate_metrics(y_ture, y_preds):
    conf = confusion_matrix(y_ture, y_preds)
    print(conf)
    if len(conf) == 1:
        print(f'tpr (recall): {-1}, fnr: {-1}, fpr: {-1}, tnr: {-1}, acc: {-1}')
        # return recall, fnr, fpr, tnr, acc
        return -1, -1, -1, -1, -1

    if (conf[0, 0] + conf[1, 0]) != 0:
        pr = conf[0, 0] / (conf[0, 0] + conf[1, 0])
    else:
        pr = 0

    if (conf[0, 0] + conf[0, 1]) != 0:
        recall = conf[0, 0] / (conf[0, 0] + conf[0, 1])
    else:
        recall = 0

    if (pr + recall) != 0:
        f1 = (2 * pr * recall) / (pr + recall)
    else:
        f1 = 0

    # print(classification_report(data_test_labels,pred_class))
    # try:
    #     print("F1 Score : ", f1)
    #     fpr = (conf[1, 0] / (conf[1, 0] + conf[1, 1]))
    #     print("FPR : ", (conf[1, 0] / (conf[1, 0] + conf[1, 1])))
    #     print("DR : ", recall)
    #     print(conf)
    # except:
    #     fpr = 0
    #     print("FPR = 100")

    if (conf[0, 0] + conf[0, 1]) != 0:
        fnr = conf[0, 1] / (conf[0, 0] + conf[0, 1])
    else:
        fnr = 0
    if (conf[1, 0] + conf[1, 1]) != 0:
        fpr = conf[1, 0] / (conf[1, 0] + conf[1, 1])
    else:
        fpr = 0

    if (conf[1, 0] + conf[1, 1]) != 0:
        tnr = (conf[1, 1]) / (conf[1, 0] + conf[1, 1])
    else:
        tnr = 0

    if (conf[0, 0] + conf[0, 1] + conf[1, 0] + conf[1, 1]) != 0:
        acc = (conf[0, 0] + conf[1, 1]) / (conf[0, 0] + conf[0, 1] + conf[1, 0] + conf[1, 1])
    else:
        acc = 0
    dr = recall

    print(f'tpr (recall): {recall}, fnr: {fnr}, fpr: {fpr}, tnr: {tnr}, acc: {acc}')

    return recall, fnr, fpr, tnr, acc


# Calculate f1_score
def f1_score(conf):
    if (conf[0, 0] + conf[1, 0]) != 0:
        pr = conf[0, 0] / (conf[0, 0] + conf[1, 0])
    else:
        pr = 0

    if (conf[0, 0] + conf[0, 1]) != 0:
        recall = conf[0, 0] / (conf[0, 0] + conf[0, 1])
    else:
        recall = 0

    if (pr + recall) != 0:
        f1 = (2 * pr * recall) / (pr + recall)
    else:
        f1 = 0

    return f1
