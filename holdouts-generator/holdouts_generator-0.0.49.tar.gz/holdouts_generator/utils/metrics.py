from typing import List, Dict
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import hamming_loss
from sklearn.metrics import hinge_loss
from sklearn.metrics import jaccard_score
from sklearn.metrics import log_loss
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import zero_one_loss
from sklearn.metrics import brier_score_loss
from sklearn.metrics import roc_auc_score
from deflate_dict import deflate

metrics_groups = {
    "continous": [
        average_precision_score,
        roc_auc_score
    ],
    "integer": [
        accuracy_score,
        balanced_accuracy_score,
        f1_score,
        precision_score,
        recall_score
    ]
}


def is_binary_classification_problem(y_true: np.ndarray) -> bool:
    """Return boolean representing if given problem labels are from a binary classification problem.

    Parameters
    ----------
    y_true: np.ndarray,
        Array with ground truth labels.

    Returns
    -------
    Boolean representing if given labels are from a binary classification problem.
    """
    return {0, 1}.issuperset(y_true)


def binary_classifications_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Return dictionary of binary classifications metrics.

    Parameters
    ----------
    y_true: np.ndarray,
        Array with ground truth labels.
    y_pred: np.ndarray,
        Array with predictions of the labels.

    Returns
    -------
    Return dictionary of classifications.
    """
    true_negatives, false_positives, false_negatives, true_positives = [
        int(e) for e in confusion_matrix(y_true, np.array(y_pred).round()).ravel()
    ]
    return {
        **{
            metric.__name__: float(metric(y_true, y_pred))
            for metric in metrics_groups["continous"]
        },
        **{
            metric.__name__: float(metric(y_true, np.array(y_pred).round()))
            for metric in metrics_groups["integer"]
        },
        "fall_out": false_positives / (false_negatives + true_positives),
        "true_negatives": true_negatives,
        "true_positives": true_positives,
        "false_negatives": false_negatives,
        "false_positives": false_positives
    }


def train_test_binary_classifications_metrics(
    y_true_train: np.ndarray,
    y_pred_train: np.ndarray,
    y_true_test: np.ndarray,
    y_pred_test: np.ndarray
) -> Dict[str, float]:
    """Return dictionary with binary classification metrics for both the training and test set.

    Parameters
    ----------
    y_true_train: np.ndarray,
        Array with ground truth labels from the train set.
    y_pred_train: np.ndarray,
        Array with predictions of the labels from the train set.
    y_true_test: np.ndarray,
        Array with ground truth labels from the test set.
    y_pred_test: np.ndarray,
        Array with predictions of the labels from the test set.

    Returns
    -------
    Dictionary with binary classification metrics.
    """
    return deflate({
        "train": binary_classifications_metrics(y_true_train, y_pred_train),
        "test": binary_classifications_metrics(y_true_test, y_pred_test)
    })
