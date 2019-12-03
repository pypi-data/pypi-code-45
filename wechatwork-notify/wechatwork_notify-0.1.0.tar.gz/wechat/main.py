#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 4:52 下午
# @Author  : jack.du
# @Email   : xianghua.du@start.com.cn
# @File    : send_wechatwork.py
# @Software: PyCharm
from __future__ import absolute_import

import logging
import sys
import os

from wechat.options import WeChatOptionParser
from wechat.config import Config
from wechat.modules import wechatwork
from wechat.modules import message

log = logging.getLogger()



def main():
    arg_parser = WeChatOptionParser()
    options = arg_parser.parse_args()

    if options.debug:
        log.setLevel('DEBUG')
        log.debug('log level set to Debug')

    if options.file:
        config_file = options.file
    else:
        config_file = os.path.join(os.path.expandvars('$HOME'), '.wechat/config')

    cfg = Config(config_file, profile=options.profile)

    if options.configure:
        cfg.configure()
        sys.exit(0)

    if not cfg.has_profile():
        log.error('The config profile (%s) could not be found' %options.profile)
        sys.exit(1)

    if not options.content:
        arg_parser.print_help()
        log.error('%s: argument -c/--content is required' % arg_parser.prog)
        sys.exit(1)

    log.debug('cfg.agentid: %s' %cfg.agentid)
    if not options.agentid and not cfg.agentid:
        arg_parser.print_help()
        log.error('%s: argument -a/--agentid is required' % arg_parser.prog)
        sys.exit(1)

    if options.corpid:
        cfg.update_option('corpid', options.corpid)

    if options.corpsecret:
        cfg.update_option('corpsecret', options.corpsecret)

    if cfg.agentid and not options.agentid:
        log.debug('agentid: %s' %cfg.agentid)
        options.agentid = cfg.agentid

    log.debug("corpid: %s" %cfg.corpid)
    log.debug("corpsecret: %s " %cfg.corpsecret)
    log.debug("agentid: %s " % cfg.agentid)

    if not cfg.corpid or not cfg.corpsecret:
        print('miss corpid or corpsecret.')
        sys.exit(1)

    log.debug("argconfig: %s" %options.__dict__)
    try:
        w = wechatwork.WeChatWork(cfg.corpid, cfg.corpsecret)
        data = message.Message(**options.__dict__)
        data.text = message.Text(options.content)
        w.sendMessage(data.to_dict())
    except IOError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()