#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 4:01 PM
# @Author  : jack.du
# @Email   : xianghua.du@start.com.cn
# @File    : login.py
# @Software: PyCharm
import os
import time
import json
import logging

try:
    import urllib3
except ImportError:
    raise ImportError('xxx Python client requires urllib3.')

urllib3.disable_warnings()
log = logging.getLogger()

class WeChatWork:
    def __init__(self, corpid, corpsecret, cache_dir="/tmp"):
        self.cache_file_path = os.path.join(cache_dir, corpid)
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.http = urllib3.PoolManager()

    def accessToken(self):
        if self.token_cache():
            return self.token_cache()

        _url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'.format(self.corpid,
                                                                                               self.corpsecret)
        r = self.http.request('get', _url)
        data = json.loads(r.data.decode('utf-8'))

        if data['errcode'] != 0:
            raise ValueError(data['errmsg'])

        self.write_cache(data)
        return data['access_token']

    def write_cache(self, data, cache_path=None):
        if not cache_path:
            cache_path = self.cache_file_path

        if isinstance(data, dict):
            data['cache_time'] = str(time.time())

        with open(cache_path, 'w') as f:
            f.write(json.dumps(data))

    def token_cache(self):
        '''
        :return: access_token
        :cache = {"errcode":0,"errmsg":"ok","access_token":token,"expires_in":7200}'
        '''
        'token cache format is json'
        if not os.path.exists(self.cache_file_path):
            return False

        with open(self.cache_file_path, 'r') as f:
            data = f.read()

        try:
            cache = json.loads(data)
        except Exception:
            return False

        if float(time.time()) - float(cache["cache_time"]) < cache["expires_in"]:
            return cache["access_token"]
        else:
            return False

    def sendMessage(self, message):
        _url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(self.accessToken())
        encode_data = json.dumps(message).encode('utf-8')
        r = self.http.request("POST", _url, body=encode_data)
        log.info("Response: " + r.data.decode('utf-8'))