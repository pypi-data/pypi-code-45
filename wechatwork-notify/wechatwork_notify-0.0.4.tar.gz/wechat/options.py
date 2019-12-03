#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 3:28 下午
# @Author  : jack.du
# @Email   : xianghua.du@start.com.cn
# @File    : options.py
# @Software: PyCharm
from __future__ import absolute_import

from wechat.utils.parsers import OptionParser

class WeChatOptionParser(OptionParser):
    def _set_arguments(self):
        self.add_argument('-f', '--file', default=None)
        self.add_argument('--profile', default='default')

        self.add_argument('--corpid', default=None)
        self.add_argument('--corpsecret', default=None)

        self.add_argument('--touser', default='@all')
        self.add_argument('--toparty', default=None)
        self.add_argument('--totag', default=None)
        self.add_argument('--msgtype', default='text', help='msgype only supports text type',
                      choices=['text'])
        self.add_argument('-a', '--agentid', type=int)
        self.add_argument('--safe', default=0, type=int, choices=[0, 1])
        self.add_argument('--enable_id_trans', default=0, type=int, choices=[0, 1])
        self.add_argument('--enable_duplicate_check', default=0, type=int, choices=[0, 1])
        self.add_argument('--duplicate_check_interval', default=1800)

        self.add_argument("-c", "--content", help='message content....')

        self.add_argument("--debug", help='show logs for debug.', action='store_true')
        self.add_argument("--configure", help='Invoke interactive (re)configuration tool.', action='store_true')
