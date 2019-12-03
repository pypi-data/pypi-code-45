#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 6:08 PM
# @Author  : jack.du
# @Email   : xianghua.du@start.com.cn
# @File    : optionparser.py
# @Software: PyCharm
import argparse

class OptionParser(argparse.ArgumentParser):
    usage = None
    description = None
    optionals_title = None
    positionals_title = None

    epilog = ('You can find additional help about %(prog)s issuing "man %(prog)s" '
              'or on https://github.com/duxianghua/StarTools')

    def __init__(self, *args, **kwargs):
        if self.usage:
            kwargs.setdefault('usage', self.usage)

        if self.description:
            kwargs.setdefault('description', self.description)

        if self.epilog:
            kwargs.setdefault('epilog', self.epilog)

        argparse.ArgumentParser.__init__(self, *args, **kwargs)

        self._set_arguments()

        if self.optionals_title:
            self._optionals.title = self.optionals_title

        if self.positionals_title:
            self._positionals.title = self.positionals_title


    def conflict_handler(self, *args, **kwargs):
        pass

    def parse_args(self, args=None, namespace=None):
        options = argparse.ArgumentParser.parse_args(self, args, namespace)
        self.config = options.__dict__
        return options

    def to_dict(self):
        pass

    def _set_arguments(self):
        pass