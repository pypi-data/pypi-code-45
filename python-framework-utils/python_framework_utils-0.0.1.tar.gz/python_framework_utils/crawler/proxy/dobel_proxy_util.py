from .__init__ import *

class DobelProxyUtil:
    '''
    todo 多贝云代理工具类
    '''

    # todo 多贝云代理配置
    __duobel_proxy = {
            'host': 'http-proxy-t1.dobel.cn',
            'port': '9180',
            'username': 'POISCCBFCE5RSO70',
            'password': 'HxMDsR9s',
        }
    # todo 多贝云切换代理IP
    __change_ip = 'http://ip.dobel.cn/switch-ip'

    @classmethod
    def get_duobel_http(cls):
        '''
        todo 多贝云 获取代理http,形如 http://user:password@host:port 字符串
        :return:
        '''
        proxy = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
          "host" : cls.__duobel_proxy['host'],
          "port" : cls.__duobel_proxy['port'],
          "user" : cls.__duobel_proxy['username'],
          "pass" : cls.__duobel_proxy['password'],
        }
        return proxy

    @classmethod
    def get_doubel_requests_proxy(cls):
        '''
        todo 多贝云 获取requests模块需要的代理对象，dict类型，形如 {'http' : 'xxx','https' : 'xxx'}
        :return:
        '''
        http = cls.get_duobel_http()
        http_proxy = {
            'http' : http,
            'https' : http,
        }
        return http_proxy

    @classmethod
    def change_proxy(cls):
        '''
        todo 多贝云 主动切换代理IP
        :return:
        '''
        import requests
        res = requests.get(cls.__change_ip, proxies=cls.get_doubel_requests_proxy())
        return True