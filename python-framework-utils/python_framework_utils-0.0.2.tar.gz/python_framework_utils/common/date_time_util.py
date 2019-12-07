import time
from .__init__ import *
class DateTimeUtil:
    '''
    todo 日期时间工具类
    '''
    @staticmethod
    def now(format='%Y-%m-%d %H:%M:%S'):
        '''
        todo 获取当前时间字符串，默认%Y-%m-%d %H:%M:%S
        :param format: 日期时间格式
        :return:
        '''
        return time.strftime(format, time.localtime(time.time()))
    @staticmethod
    def now_timestamp(type='int'):
        '''
        todo 获取当前时间戳
        :param type int 或 float. 返回数据类型
        :return:
        '''
        if type == 'int':
            return int(time.time())
        else:
            return time.time()

    @staticmethod
    def timestamp_to_str(timestamp=None, format='%Y-%m-%d %H:%M:%S'):
        '''
        todo 时间戳转日期时间字符串
        :param timestamp: 时间戳
        :param format: 转化格式
        :return:
        '''
        if BasicCheckUtil.is_none(timestamp):
            timestamp = time.time()
        return time.strftime(format, time.localtime(timestamp))

    @staticmethod
    def str_to_timestamp(st=None, format='%Y-%m-%d %H:%M:%S', type='int'):
        '''
        todo 日期时间字符串转时间戳
        :param st: 日期时间字符串
        :param format: 日期时间格式
        :param type: int 或 float. 返回数据类型
        :return:
        '''
        if BasicCheckUtil.is_none(st):
            if type == 'int':
                return int(time.time())
            else:
                return time.time()
        if type == 'int':
            return int(time.mktime(time.strptime(st, format)))
        else:
            return time.mktime(time.strptime(st, format))

