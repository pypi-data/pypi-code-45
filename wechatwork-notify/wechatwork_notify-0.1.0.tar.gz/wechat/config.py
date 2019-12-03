#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 2:56 PM
# @Author  : jack.du
# @Email   : xianghua.du@start.com.cn
# @File    : config.py
# @Software: PyCharm
from __future__ import absolute_import

import six
import os
import logging

log = logging.getLogger()

if six.PY3:
    import configparser as ConfigParser
    OrderedDict = dict

if six.PY2:
    import ConfigParser
    from collections import OrderedDict

corpid = None
corpsecret = None
access_token = None
config_path = '/tmp/config'
message = {}

class Config(object):
    corpid = None
    corpsecret = None
    access_token = None
    agentid = None
    configfile = None
    cache_path = '/tmp/%s' %corpid
    profile = 'profile default'

    def __init__(self, configfile, profile=None):
        self.parser = ConfigParser.ConfigParser()

        if profile:
            self.profile = "profile %s" %profile

        self.configfile = configfile

        self.read_config_file(self.configfile, self.profile)

    def read_config_file(self, configfile, section):
        log.debug("configfile: %s" %configfile)
        log.debug("section: %s" %section)

        self.parser.read(configfile)

        if not self.parser.has_section(section) and section != 'DEFAULT':
            log.debug('The config profile (%s) could not be found' %(section))
            return

        for k, v in self.parser.items(section):
            log.debug('update config.%s = %s' %(k, v))
            self.update_option(k, v)

    def dump_config(self):
        parser_dict = {s: dict(self.parser.items(s)) for s in self.parser.sections()}
        log.debug('save config: %s' %str(parser_dict))

        config_dir = os.path.dirname(self.configfile)

        if not os.path.exists(config_dir):
            os.mkdir(config_dir)

        if self.parser:
            with open(self.configfile, 'w') as configfile:
                self.parser.write(configfile)

    def configure(self):
        corpid = ArgumentInput(str, "wechat_work_corpid: [%s]" %self.corpid)
        corpsecret = ArgumentInput(str, "wechat_work_corpsecret: [%s]" % self.corpsecret)
        agentid = ArgumentInput(str, "wechat_work_agentid: [%s]" % self.agentid)

        self.set_section('corpid', corpid())
        self.set_section('corpsecret', corpsecret())
        self.set_section('agentid', agentid())

        self.dump_config()

    def update_option(self, option, value):
        if value is None:
            return

        if hasattr(Config, option):
            setattr(Config, option, value)
        else:
            raise ValueError('Invalid parameter "{0}"'.format(option))

    def set_section(self, option, value):
        if not value:
            return

        if not self.parser.has_section(self.profile):
            self.parser.add_section(self.profile)
        self.parser.set(self.profile, option, value)

    def has_profile(self):
        return self.parser.has_section(self.profile)


class ArgumentInput(object):
    def __init__(self, type, desc):
        if six.PY2:
            self.input = raw_input

        if six.PY3:
            self.input = input

        self.type = type
        self.desc = desc

    def __call__(self, value=None):
        if not value:
            value = self.input("{0}: ".format(self.desc))
        return self.type(value)