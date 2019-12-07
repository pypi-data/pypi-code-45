import json

class JsonUtil:
    '''
    Json 工具类
    '''
    __init_status = False
    __json = None
    __struct = {}
    __count = {}

    @staticmethod
    def str_to_json(st):
        '''
        字符串转dict对象静态工具方法
        :param st:
        :return:
        '''
        return json.loads(st)

    @staticmethod
    def json_to_str(st):
        '''
        dict转字符串静态工具方法
        :param st:
        :return:
        '''
        return json.dumps(st, ensure_ascii=False)

    @classmethod
    def load(cls, param):
        '''
        装载json字符串或对象，以便于调用类方法
        :param st:
        :return:
        '''
        if type(param) == str:
            cls.__json = json.loads(param)
        elif type(param) == dict:
            cls.__json = param
        return cls

    @classmethod
    def print(cls):
        '''
        返回包含所有结构的json
        :return:
        '''
        cls.__init()
        return cls.__struct

    @classmethod
    def get(cls, key):
        '''
        获取某个key的结果
        :param key: 字典的key
        :return: list，对应key的结果列表（可能包含多个同名key）
        '''
        cls.__init()
        return cls.__struct.get(key)

    @classmethod
    def get_first(cls, key):
        '''
        获取某个key的第一个结果
        :param key: 字典的key
        :return: list的第一个元素
        '''
        return cls.get_one(key)

    @classmethod
    def get_one(cls, key, index=0):
        '''
        获取某个key的指定位置结果
        :param key: 字典的key
        :param index: 第 index 次出现
        :return: list 的第 index个元素，从0开始
        '''
        cls.__init()
        return cls.__struct[key][0]

    @classmethod
    def __init(cls):
        '''
        装载dict对象
        :return:
        '''
        if not cls.__init_status:
            if cls.__json is None:
                return ValueError('当前没有Json对象')
            cls.__re_init(cls.__json)
            cls.__init_status = True

    @classmethod
    def __re_init(cls, param):
        '''
        提取嵌套dict至最外层
        :param param:
        :return:
        '''
        if type(param) in (dict,):
            for key, value in param.items():
                count = cls.__count.get(key)
                if count is None:
                    count = 0
                    cls.__struct[key] = []
                cls.__struct[key].insert(count, value)
                count += 1
                cls.__count[key] = count
                cls.__re_init(value)
        elif type(param) in (list, tuple):
            for single in param:
                cls.__re_init(single)