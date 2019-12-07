from .__init__ import *
import json

class PyMysqlUtil:
    '''
    todo 基于PyMysql模块的工具类（面向对象），部分功能尚未完成
    todo 仅get_result()方法与close()方法会返回结果，close()方法在返回结果的同时还会关闭连接
    todo 使用get_result()方法后之前操作数据的结果均会返回，并清空所有记录
    '''
    __conn = None
    __result = []

    @classmethod
    def connect(cls, host, port, username, password, db=None):
        '''
       创建连接
        :param host: Mysql Host
        :param port: Mysql Port
        :param username: Mysql Username
        :param password: Mysql Password
        :param db: Mysql DataBase Name
        :return:
        '''
        import pymysql
        cls.__conn = pymysql.connect(host=host, port=int(port), user=username, password=password, database=db)
        return cls

    @classmethod
    def execute(cls, sql):
        '''
        Mysql sql执行方法（不建议使用）
        :param sql:
        :return:
        '''
        cls.__check_conn()
        if BasicCheckUtil.is_none(sql):
            raise ValueError('sql 不能为空')
        conn = cls.__conn
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return cls

    @classmethod
    def insert_dict_auto_incr_col(cls, table, data, mode='into'):
        pass

    @classmethod
    def insert_dict(cls, table, data, mode='into', values_list_split=','):
        '''
       插入单条字典结构数据
        :param table: 表名
        :param data: 字典结构数据
        :param mode: 插入模式，into,overwrite,ignore 等，默认into（追加）
        :return:
        '''
        cls.__check_conn()
        if BasicCheckUtil.not_none(cls.__check_insert(table, data)):
            return cls

        conn = cls.__conn
        keys = ",".join(data.keys())
        # values检测
        values = cls.__check_values([data[key] for key in data.keys()], values_list_split)
        sql = f'insert {mode} {table} ({keys}) values({",".join(["%s" for i in range(len(data))])})'
        cursor = conn.cursor()
        try:
            cursor.execute(sql, values)
            conn.commit()
        except Exception:
            cls.__result.append(RuntimeError(f"插入数据失败，失败sql：{sql % values}"))
            return cls

        cursor.close()
        cls.__result.append(True)
        return cls

    @classmethod
    def insert_dicts(cls, table, data, once_length=200, mode='into', values_list_split=','):
        '''
       插入 字典元祖/字典列表 结构数据，形如 ({},{}) 或 [{},{}]，要求每个字典的key全部一致
        :param table: 表名
        :param data: 数据
        :param once_length: 单批插入数据量
        :param mode: 插入模式，into,overwrite,ignore 等，默认into（追加）
        :return:
        '''
        cls.__check_conn()
        if BasicCheckUtil.not_none(cls.__check_insert(table, data)):
            return cls

        conn = cls.__conn
        keys = ",".join(data[0].keys())
        cursor = conn.cursor()
        for i in range(int((len(data) - 1) / once_length) + 1):
            #分为length批次写入
            length = min(len(data), (i + 1) * once_length)
            sql = f'insert {mode} {table} ({keys}) values '
            values = []
            for dict_obj in data[i * once_length: length]:
                sql += f' ({",".join(["%s" for i in range(len(dict_obj))])}),'
                values += [dict_obj[key] for key in dict_obj.keys()]
            #剔除末尾空格
            sql = sql[:-1]
            # values检测
            values = cls.__check_values(values, values_list_split)
            try:
                cursor.execute(sql, values)
            except Exception:
                cls.__result.append(RuntimeError(f"插入数据失败，失败sql：{sql}"))
                return cls

        conn.commit()
        cls.__result.append(True)
        cursor.close()
        return cls

    @classmethod
    def query(cls, sql, args=None, type='dict'):
        '''
       Mysql查询方法
        :param sql: 查询sql，传参使用%s代替
        :param args: 参数对象，元组（tuper）或列表（list）均可
        :param type: 类型，dict返回形如[{'xxx' : 'xxx'},{'xxx' : 'xxx'}]，tuple返回形如((xxx,xx),(xxx,xx))结果
        :return:
        '''
        cls.__check_conn()
        if BasicCheckUtil.is_none(sql):
            cls.__result.append(ValueError('sql 不能为空'))
            return cls

        if type not in ('dict', 'tuple'):
            cls.__result.append(TypeError('返回元素子元素类型必须指定为dict或tuple'))
            return cls

        conn = cls.__conn
        if type == 'dict':
            from pymysql.cursors import DictCursor
            cursor = conn.cursor(cursor=DictCursor)
        else:
            cursor = conn.cursor()
        cursor.execute(sql, args=args)
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        cls.__result.append(result)
        return cls

    @classmethod
    def insert(cls, sql, args=None):
        '''
        todo
        :param sql: sql 字符串
        :param args: 参数元组或列表
        :return:
        '''
        cls.__result.append(cls.__execute(sql, args, 'insert 失败'))
        return cls

    @classmethod
    def update(cls, sql, args=None):
        '''
       修改数据
        :param sql: sql 字符串
        :param args: 参数元组或列表
        :return:
        '''
        cls.__result.append(cls.__execute(sql, args, 'update 失败'))
        return cls
    
    @classmethod
    def get_result(cls):
        '''
        返回之前所有提交的结果，并清空缓存结果
        :return: 
        '''
        result = cls.__result
        cls.__result = []
        return result
    
    @classmethod
    def close(cls):
        '''
        关闭Mysql连接,并返回之前所有执行的结果
        :return:
        '''
        cls.__conn.close()
        return cls.__result

    @classmethod
    def __execute(cls, sql, args=None, error_message='执行失败'):
        '''
       Sql 执行方法
        :param sql: sql字符串
        :return:
        '''
        cls.__check_conn()
        if BasicCheckUtil.is_empty(sql):
            return ValueError('sql 不能为空')
        conn = cls.__conn
        cursor = conn.cursor()
        try:
            cursor.execute(sql, args)
            conn.commit()
        except:
           return RuntimeError(f"{error_message}，失败sql：{sql % (tuple() if args == None else args)}")
        cursor.close()
        return True

    @staticmethod
    def __check_values(values, split):
        '''
        values 参数检测
        :return:
        '''
        for index in range(len(values)):
            if type(values[index]) in (tuple, list):
                values[index] = split.join(values[index])
            if type(values[index]) in (dict,):
                values[index] = json.dumps(values[index], ensure_ascii=False)
        return values

    @classmethod
    def __check_insert(cls, table, data):
        if BasicCheckUtil.is_empty(table):
            cls.__result.append(ValueError('表名不能为空'))
            return cls
        if BasicCheckUtil.is_empty(data):
            cls.__result.append(ValueError('数据不能为空'))
            return cls
    @classmethod
    def __check_conn(cls):
        '''
       检测是否存在Mysql连接
        :return:
        '''
        if BasicCheckUtil.is_none(cls.__conn):
            raise ConnectionError('当前没有Mysql可用连接对象')
