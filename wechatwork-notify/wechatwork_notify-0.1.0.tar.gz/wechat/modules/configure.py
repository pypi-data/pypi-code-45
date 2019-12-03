#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 5:44 PM
# @Author  : jack.du
# @Email   : xianghua.du@start.com.cn
# @File    : configure.py
# @Software: PyCharm
import six
import os

if six.PY3:
    import configparser as ConfigParser

if six.PY2:
    import ConfigParser


class ArgumentInput(object):
    def __init__(self, type, func, desc):
        if six.PY2:
            self.input = raw_input

        if six.PY3:
            self.input = input

        self.type = type
        self.func = func
        self.desc = desc

    def __call__(self, value=None):
        if not value:
            value = self.input("{0}: ".format(self.desc))
        return self.type(value)


class WechatConfig(object):
    def __init__(self, path):
        self.path = path
        self.parser = ConfigParser.ConfigParser()
        self.get()

    def get(self):
        if os.path.exists(self.path):
            self.parser.read(self.path)

    def save(self):
        with open(self.path, 'w') as f:
            f.write(self.parser)

    def to_dict(self):
        return {s: dict(self.parser.items(s)) for s in self.parser.sections()}
