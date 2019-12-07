import os
from .__init__ import *
class FileUtil:
    '''
    todo 文件操作工具类
    '''
    @staticmethod
    def exists(path=None):
        '''
        todo 检测目录/文件是否存在
        :param path: 目录/文件 绝对/相对路径
        :return:
        '''
        if BasicCheckUtil.is_none(path):
            raise ValueError('路径不能为空')
        return os.path.exists(path)

    @staticmethod
    def dir_create(path=None):
        '''
        todo 创建目录，支持多级目录嵌套创建
        :param path: 目录相对路径/绝对路径
        :return:
        '''
        if BasicCheckUtil.is_none(path):
            raise ValueError("路径不能为空")
        if not FileUtil.dir_exists(path):
            os.makedirs(path)
        return True

    @staticmethod
    def file_create(path=None):
        '''
        todo 创建文件，支持多级目录嵌套创建
        :param path: 文件相对路径/绝对路径
        :return:
        '''
        if BasicCheckUtil.is_none(path):
            raise ValueError("路径不能为空")
        # win 分隔符替换
        path = path.replace(r'\\','/')
        with open(path) as f:
            pass
        return True

    @staticmethod
    def file_remove(path=None):
        '''
        todo 删除文件
        :param path: 文件相对/绝对路径
        :return:
        '''
        if BasicCheckUtil.is_none(path):
            raise ValueError("文件路径不能为空")
        return os.remove(path)

    @staticmethod
    def file_exists(path=None):
        '''
        todo 检测文件是否存在
        :param file_path: 文件绝对/相对路径
        :return:
        '''
        if BasicCheckUtil.is_none(path):
            raise ValueError("文件路径不能为空")
        return os.path.isfile(path)

    @staticmethod
    def dir_exists(path=None):
        '''
        todo 检测目录是否存在
        :param dir_path: 目录绝对/相对路径
        :return:
        '''
        if BasicCheckUtil.is_none(path):
            raise ValueError('文件路径不能为空')
        return os.path.isdir(path)