# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2019
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
To implement the backward propagation procedure necessary for relevance
propagation, we will add a 'relprop' method to each layer.
"""

# Imports
import torch
import torch.nn as nn
import torch.nn.functional as func


LOWEST = None
HIGHEST = None
REGISTERY = {}


def register(cls):
    def register_decorator(func):
        REGISTERY.setdefault(cls, []).append(func)
    return register_decorator


@register("main")
def relprop(self, R):
    for layer_index in range(len(self.layers), 0, -1):
        R = self.layers[layer_index - 1].relprop(R)
    return R


@register(nn.Linear)
def relprop(self, R):
    V = torch.clamp(self.weight, min=0)
    Z = torch.mm(self.X, torch.transpose(V, 0, 1)) + 1e-9
    S = R / Z
    C = torch.mm(S, V)
    R = self.X * C
    return R


@register(nn.Linear)
def relprop1(self, R):
    W = self.weight
    V = torch.clamp(self.weight, min=0)
    U = torch.clamp(self.weight, max=0)
    X = self.X
    L = self.X * 0 + LOWEST
    H = self.X * 0 + HIGHEST
    WT = torch.transpose(W, 0, 1)
    VT = torch.transpose(V, 0, 1)
    UT = torch.transpose(U, 0, 1)
    Z = torch.mm(X, WT) - torch.mm(L, VT) - torch.mm(H, UT) + 1e-9
    S = R / Z
    R = X * torch.mm(S, W) - L * torch.mm(S, V) - H * torch.mm(S, U)
    return R


@register(nn.ReLU)
def relprop(self, R):
    return R


@register(nn.MaxPool2d)
def gradprop(self, DY):
    DX = self.X * 0
    temp, indices = func.max_pool2d(
        self.X, self.kernel_size, self.stride, self.padding, self.dilation,
        self.ceil_mode, True)
    DX = func.max_unpool2d(
        DY, indices, self.kernel_size, self.stride, self.padding)
    return DX


@register(nn.MaxPool2d)
def relprop(self, R):
    Z = self.Y + 1e-9
    S = R / Z
    C = self.gradprop(S)
    R = self.X * C
    return R


@register(nn.Conv2d)
def gradprop(self, DY):
    output_padding = self.X.size()[2] - (
        (self.Y.size()[2] - 1) * self.stride[0] - 2 * self.padding[0] +
        self.kernel_size[0])
    return func.conv_transpose2d(
        DY, self.weight, stride=self.stride, padding=self.padding,
        output_padding=output_padding)


@register(nn.Conv2d)
def relprop(self, R):
    Z = self.Y + 1e-9
    S = R / Z
    C = self.gradprop(S)
    R = self.X * C
    return R
