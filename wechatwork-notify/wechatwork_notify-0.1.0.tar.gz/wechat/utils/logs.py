#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 2:40 下午
# @Author  : jack.du
# @Email   : xianghua.du@start.com.cn
# @File    : logs.py
# @Software: PyCharm
import logging


def console_handler():
    formatter = logging.Formatter(
        '[%(levelname)-6s] %(message)s', datefmt='%H:%M:%S'
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)
    return stream_handler

def logger(level='INFO'):
    logging.root.setLevel(level)
    logging.root.addHandler(console_handler())