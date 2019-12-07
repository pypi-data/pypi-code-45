from .__init__ import *

class AcceptsUtil:
    '''
    todo 请求头Accept参数生成工具类
    '''
    @staticmethod
    def get_accept():
        '''
        todo 获取请求头Accept参数
        :return:
        '''
        return 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'

    @staticmethod
    def get_accept_language():
        '''
        todo 获取请求头Accept-Language参数
        :return:
        '''
        return 'zh-CN,zh;q=0.9,en;q=0.8'