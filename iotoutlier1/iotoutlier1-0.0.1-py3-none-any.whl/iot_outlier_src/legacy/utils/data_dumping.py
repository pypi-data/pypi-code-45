"""
    Purpose:
        dump data to disk.

"""


def lst_to_str(data):
    lst_str = '['
    for v in data:
        lst_str += str(v) + ','

    lst_str += ']'

    return lst_str


def save_features_selection_results(out_file, features_descended_dict):
    with open(out_file, 'w') as hdl:
        for key, value in features_descended_dict.items():
            line = str(key) + ':' + str(len(value)) + ':' + lst_to_str(value)
            hdl.write(line + '\n')

    return out_file


def save_thres_res_metrics(out_file, thres_lst, res_metrics_lst):
    with open(out_file, 'w') as out_hdl:
        line = 'thres_AE, tpr, fnr, fpr, tnr, acc'
        out_hdl.write(line + '\n')
        for i, thres in enumerate(thres_lst):
            line = str(thres) + ',' + str(res_metrics_lst['tpr'][i]) + ',' + str(res_metrics_lst['fnr'][i]) + ',' + str(
                res_metrics_lst['fpr'][i]) + ',' + str(res_metrics_lst['tnr'][i]) + ',' + str(res_metrics_lst['acc'][i])
            out_hdl.write(line + '\n')


def save_roc_to_txt(out_file, y_test_pred_labels_dict):
    # print(f'y_test_pred_labels_dict:{y_test_pred_labels_dict}')
    with open(out_file, 'w') as out_hdl:
        line = 'model-y_true[0]:y_preds_probs[0], y_true[1]:y_preds_probs[1],....'
        out_hdl.write(line + '\n')
        for idx, (key, value) in enumerate(y_test_pred_labels_dict.items()):
            line = str(key) + '@'
            if len(value) == 0:
                print(f'key:{key}, value:{value}')
                continue
            y_true, y_preds_labels = value
            y_true = np.reshape(y_true, (y_true.shape[0],))
            for i in range(y_true.shape[0] - 1):
                line += str(y_true[i]) + ':' + str(y_preds_labels[i]) + ','
            line += str(y_true[-1]) + ':' + str(y_preds_labels[i])
            out_hdl.write(line + '\n')
