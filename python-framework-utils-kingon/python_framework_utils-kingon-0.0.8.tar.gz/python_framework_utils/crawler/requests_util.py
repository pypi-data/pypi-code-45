import requests
from bs4 import BeautifulSoup
from .__init__ import *

class RequestsUtil:
    '''
    todo Requests 工具方法，集成requests模块与BeautifulSoup于一体的类方法，快速爬取 + 解析（仅完成部分功能）
    '''
    __params = {
        'beautifulsoup_type' : None,
        'res' : None,
        'soup' : None,
        # todo 缓存尚未实现
        'cache_search': []
    }
    @classmethod
    def get(cls, url, beautifulsoup_type='lxml', params=None, **kwargs):
        '''
        get请求
        :param url: 请求url,需要带协议头(http://|https://)
        :param beautifulsoup_type: Beautifulsoup解析类型，默认lxml
        :param params: 同requests.get的params
        :param kwargs: 同requests.get的kwarges
        :return:返回对象本身
        '''
        res = requests.get(url, params, **kwargs)
        cls.__params['res'] = res
        cls.__params['beautifulsoup_type'] = beautifulsoup_type
        return cls

    @classmethod
    def post(cls,url, beautifulsoup_type='lxml', data=None, json=None, **kwargs):
        '''
        post 请求
        :param url:  请求url,需要带协议头(http://或https://)
        :param beautifulsoup_type: Beautifulsoup解析类型，默认lxml
        :param data: 同requests.post的data
        :param json: 同requests.post的json
        :param kwargs: 同requests.post的kwargs
        :return: 返回类对象本身
        '''
        res = requests.post(url, data, json, **kwargs)
        cls.__params['res'] = res
        cls.__params['beautifulsoup_type'] = beautifulsoup_type
        return cls

    @classmethod
    def find_all(cls, tag_name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs):
        """
        Extracts a list of Tag objects that match the given
        criteria.  You can specify the name of the Tag and any
        attributes you want the Tag to have.

        The value of a key-value pair in the 'attrs' map can be a
        string, a list of strings, a regular expression object, or a
        callable that takes a string and returns whether or not the
        string matches for some custom definition of 'matches'. The
        same is true of the tag name.
        """
        cls.__soup()
        return cls.__params['soup'].find_all(tag_name, attrs, recursive, text, limit, **kwargs)

    @classmethod
    def find(cls, tag_name=None, attrs={}, recursive=True, text=None, **kwargs):
        '''
        Return only the first child of this Tag matching the given criteria.
        :param tag_name: 标签名
        :param attrs: 属性
        :return: bs4.element.Tag 对象
        '''
        cls.__soup()
        return cls.__params['soup'].find(tag_name, attrs, recursive, text, **kwargs)

    @classmethod
    def select(cls, selector, _candidate_generator=None, limit=None):
        """Perform a CSS selection operation on the current element."""
        cls.__soup()
        return cls.__params['soup'].select(selector, _candidate_generator, limit)

    @classmethod
    def prettify(cls):
        '''
        格式化html
        :return:
        '''
        cls.__soup()
        return cls.__params['soup'].prettify()

    @classmethod
    def code(cls):
        '''
        获取响应码
        :return:
        '''
        cls.__check_response()
        return cls.__params['res'].code

    @classmethod
    def text(cls):
        '''
        获取响应文本结构
        :return:
        '''
        cls.__check_response()
        return cls.__params['res'].text

    @classmethod
    def json(cls):
        '''
        获取响应json结构
        :return:
        '''
        cls.__check_response()
        return cls.__params['res'].json()

    @classmethod
    def __check_response(cls):
        '''
        检查是否存在响应
        '''
        if BasicCheckUtil.is_none(cls.__params.get('res')):
            raise ValueError('当前没有requests请求')

    @classmethod
    def __soup(cls):
        '''
        生成soup对象
        '''
        cls.__check_response()
        if BasicCheckUtil.not_none(cls.__params.get('soup')):
            return
        cls.__params['soup'] = BeautifulSoup(cls.__params['res'].text, cls.__params['beautifulsoup_type'])
