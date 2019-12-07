from .__init__ import *

class UserAgentsUtil:
    '''
    todo 用户代理工具类
    todo 用于生成用户代理（UserAgent）
    '''
    @staticmethod
    def get_ua():
        '''
        todo 随机生成UA
        :return:
        '''
        from fake_useragent import FakeUserAgent
        ua = FakeUserAgent()
        return ua.random

    @staticmethod
    def get_chrome_ua():
        '''
        todo 随机生成chrome UA
        :return:
        '''
        from fake_useragent import FakeUserAgent
        ua = FakeUserAgent()
        return ua.chrome

    @staticmethod
    def get_firefox_ua():
        '''
        todo 随机生成firefox UA
        :return:
        '''
        from fake_useragent import FakeUserAgent
        ua = FakeUserAgent()
        return ua.firefox

    @staticmethod
    def get_ie_ua():
        '''
        todo 随机生成ie UA
        :return:
        '''
        from fake_useragent import FakeUserAgent
        ua = FakeUserAgent()
        return ua.ie

    @staticmethod
    def get_safari_ua():
        '''
        todo 随机生成safari UA
        :return:
        '''
        from fake_useragent import FakeUserAgent
        ua = FakeUserAgent()
        return ua.safari

    @staticmethod
    def get_opera_ua():
        '''
        todo 随机生成opera UA
        :return:
        '''
        from fake_useragent import FakeUserAgent
        ua = FakeUserAgent()
        return ua.opera