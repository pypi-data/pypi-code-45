#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 17:06
# @Author  : chaonan
# @FileName: formatters.py
import logging
import json


class JsonFomatter(logging.Formatter):
    def format(self, record):
        """
        """
        print("=====")
        return super().format(record)


logger = logging.getLogger("nick")
logger.setLevel(logging.DEBUG)  #设置logger日志等级
ch = logging.StreamHandler()
formatter = JsonFomatter()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.info("提示")