from .__init__ import *
from .headers.user_agents_util import UserAgentsUtil
from .headers.accepts_util import AcceptsUtil
class HeadersUtil:
    '''
    todo 用户请求头获取工具类
    '''
    @staticmethod
    def get_default_headers():
        '''
        todo 获取默认请求头，仅包含一个固定 pc 用户代理
        :return:
        '''
        __default_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }
        return __default_headers

    @staticmethod
    def get_simple_headers():
        '''
        todo 获取一个随机用户代理的请求头，并包含一些基本配置
        :return:
        '''
        headers = {
            'User-Agent' : UserAgentsUtil.get_ua(),
            'Accept' : AcceptsUtil.get_accept(),
        }
        return headers
