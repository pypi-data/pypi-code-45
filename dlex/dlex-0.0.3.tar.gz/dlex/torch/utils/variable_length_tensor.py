from typing import List, Any

import torch
from torch import LongTensor
import numpy as np


def pad_sequence(data: List[List[Any]], padding_value):
    max_len = max([len(seq) for seq in data])
    if isinstance(data[0][0], list):
        padding_value = [padding_value for _ in range(len(data[0][0]))]
    data = [torch.tensor(seq + [padding_value] * (max_len - len(seq))) for seq in data]
    lengths = [max(len(seq), 1) for seq in data]
    return data, lengths


def get_mask(lengths: LongTensor, max_len: int = None, dtype: str = None):
    """Get mask tensor

    :param max_len: if None, max of lengths is used
    :type max_len: int
    :param dtype:
    :type dtype: str
    :return:
    """
    assert len(lengths.shape) == 1, 'Length shape should be 1 dimensional.'
    max_len = max_len or torch.max(lengths).item()
    mask = torch.arange(
        max_len, device=lengths.device,
        dtype=lengths.dtype).expand(len(lengths), max_len) < lengths.unsqueeze(1)
    if dtype is not None:
        mask = torch.as_tensor(mask, dtype=dtype, device=lengths.device)
    return mask