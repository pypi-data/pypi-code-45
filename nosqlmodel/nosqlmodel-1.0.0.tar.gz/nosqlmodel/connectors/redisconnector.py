# -*- coding: utf-8 -*-
"""
Basic redis connector
"""
import json

import redis

from nosqlmodel.connectors.baseconnector import BaseNosqlConnector

__author__ = 'ozgur'
__creation_date__ = '9.09.2019' '10:07'

RHOST = "localhost"
RPORT = "6379"


class RedisConnector(BaseNosqlConnector):

    def __init__(self, dbnum: int = 0):
        self.redisdbnum = dbnum
        self.conn = redis.StrictRedis(host=RHOST, port=RPORT, charset="utf-8",
                                      decode_responses=True, db=self.redisdbnum)
        super().__init__()

    def delete_table(self):
        self.flush()

    def create_table(self):
        pass

    def dbsize(self) -> int:
        """
        returns the itemcount in db
        :return: item count
        """
        # return self.conn.dbsize()
        return len(self.keys())

    def keys(self, pattern='*') -> list:
        """
        :param pattern: str urlpathregex
        :return: the keys in db
        """
        return list(
            set(self.conn.keys(pattern=pattern)) - set(self.conn.keys(self.tagprefix + "*")))

    def get(self, key: str) -> str or dict or list:
        """
        get value by key\n
        :param key: str
        :return: str or dict or list
        """
        key = str(key)
        retval = self.conn.get(key)

        if retval:
            # noinspection PyBroadException
            try:
                retval = json.loads(retval, encoding="UTF-8")
            except Exception:
                retval = str(retval)
        else:
            pass

        return retval

    def get_all_as_dict(self) -> dict:
        """
        get all values in store \n
        :return:dict
        """
        keys = self.keys()
        retdct = {}
        for key in keys:
            retdct[key] = self.get(key)

        return retdct

    def get_all_as_list(self) -> list:
        """
        get all values in store \n
        :return:dict
        """
        keys = self.keys()
        retlist = []
        for key in keys:
            retlist.append(self.get(key))

        return retlist

    def upsert(self, key: str, value: str or list or dict) -> bool:
        """
        adds a value to store
        :param key: key
        :param value: value to insert
        :return: bool
        """
        key = str(key)
        if isinstance(value, (list, (dict, set, tuple))):
            value = json.dumps(value, ensure_ascii=False)
        elif isinstance(value, object) and hasattr(value, "__dict__"):
            value = json.dumps(value.__dict__, ensure_ascii=False)
        else:
            value = str(value)
        ret = self.conn.set(key, value)
        if ret:
            return True
        else:
            return False

    def remove(self, key: str) -> bool:
        """
        removes the key from store
        :param key: str or list or tuple
        :return:
        """
        key = str(key)
        ret = str(self.conn.delete(key))
        return {"1": True}.get(ret, False)

    def remove_keys(self, keys: list) -> bool:
        """
        removes the key from store
        :param keys:
        :return:
        """
        ret = str(self.conn.delete(keys))
        return {"1": True}.get(ret, False)

    def flush(self):
        """
        Flushes current store\n
        :return: None
        """
        self.conn.flushdb()

    def tags(self) -> list:
        """
        returns tag list \n
        :return:
        """
        taglist = self.conn.keys(self.tagprefix + "*")
        retlist = []
        for tag in taglist:
            retlist.append(tag.replace(self.tagprefix, ""))
        return retlist

    def gettagkeys(self, tag: str) -> list:
        """
        get all keys of given tag \n
        :param tag:
        :return:
        """
        memberids = self.conn.smembers(self.tagprefix + tag)
        return list(memberids)

    def gettag(self, tag: str) -> list:
        """
        get all dict items in given tag \n
        :param tag:
        :return: list of dictionaries
        """
        memberids = self.gettagkeys(tag)
        retlist = []
        for memberid in list(memberids):
            retlist.append(self.get(memberid))

        return retlist

    def addtag(self, tag: str, key: str):
        """
        Adds tags to keys \n
        :param tag: list
        :param key: list
        :return: None
        """
        if not (tag and key):
            raise TypeError
        self.conn.sadd(self.tagprefix + tag, key)

    def removefromtag(self, tag: str, key: str or list):
        """
        Remove items from lists \n
        :param tag: str
        :param key: str or list
        :return: None
        """

        tag = str(tag)
        # ! dont touch it. srem doesnt accept list !!!!!
        if isinstance(key, (list, tuple, set)):
            for k in key:
                self.conn.srem(self.tagprefix + tag, k)
        else:
            self.conn.srem(self.tagprefix + tag, key)
