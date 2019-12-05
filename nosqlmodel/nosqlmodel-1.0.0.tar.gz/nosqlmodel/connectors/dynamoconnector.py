# -*- coding: utf-8 -*-
"""
Basic dynamodb connector
"""
import json
import time
from decimal import Decimal

import boto3
# from boto3.resources.factory.dynamodb import Table
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from nosqlmodel.connectors.baseconnector import BaseNosqlConnector

__author__ = 'ozgur'
__creation_date__ = '9.09.2019' '10:07'

D_REGION_NAME = ""
D_AWS_ACCESS_KEY_ID = ""
D_AWS_SECRET_ACCESS_KEY = ""


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


class DynamoConnector(BaseNosqlConnector):

    def __init__(self, tablename: str):
        self.source = boto3.resource(
            'dynamodb',
            region_name=D_REGION_NAME,
            aws_access_key_id=D_AWS_ACCESS_KEY_ID,
            aws_secret_access_key=D_AWS_SECRET_ACCESS_KEY
        )
        self.table = self.source.Table(tablename)  # pylint: disable=E1101
        self.taglistkey = "tags"
        super().__init__()

    @staticmethod
    def _f_to_d(fval: float) -> Decimal:
        """
        float to decimal converter \n
        :param fval: float value
        :return: Decimal
        """
        return Decimal(str(fval))

    @staticmethod
    def _d_to_f(dval: Decimal) -> float:
        """
        Deciaml to float converter \n
        :param dval: Decimal value
        :return: float
        """
        return float(dval)

    def delete_table(self):
        try:
            self.table.delete()
            time.sleep(10)
        except ClientError:
            pass

    def create_table(self):
        self.table = self.source.create_table(  # pylint: disable=E1101
            TableName='Test',
            KeySchema=[
                {
                    'AttributeName': 'idkey',
                    'KeyType': 'HASH'  # Partition key
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'idkey',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        time.sleep(10)

    @staticmethod
    def issuccess(resp: dict) -> bool:
        """
        checks if request is success (returns 200)
        :param resp: boto response dict
        :return: bool
        """
        if resp.get("ResponseMetadata", {}).get("HTTPStatusCode", 0) is 200:
            return True
        else:
            return False

    def keys(self, pattern='*') -> list:
        """
        :param pattern: str urlpathregex
        :return: the keys in db
        """
        retlist = []
        resp = self.table.scan(
            ProjectionExpression='idkey',
        )
        data = resp['Items']

        while 'LastEvaluatedKey' in resp:
            resp = self.table.scan(
                ExclusiveStartKey=resp['LastEvaluatedKey'],
                ProjectionExpression='idkey',
            )
            data.extend(resp['Items'])

        for rdict in data:
            val = rdict['idkey']
            if not str(val).startswith(self.tagprefix):
                retlist.append(val)
        return retlist

    def dbsize(self) -> int:
        """
        returns the itemcount in db
        :return: item count
        """
        # return self.conn.dbsize()
        return len(self.keys())

    def get(self, key: str) -> str or dict or list:
        """
        get value by key\n
        :param key: str
        :return: str or dict or list
        """
        key = str(key)
        retval = self.table.get_item(
            Key={
                'idkey': key
            }
        ).get("Item", None)
        if retval:
            for key, value in retval.items():
                if isinstance(value, Decimal):
                    retval[key] = self._d_to_f(value)

        return retval

    def get_all_as_list(self) -> list:
        """
        get all values in store \n
        :return:dict
        """

        resp = self.table.scan()
        data = resp['Items']
        tagindexlist = []

        while 'LastEvaluatedKey' in resp:
            resp = self.table.scan(
                ExclusiveStartKey=resp['LastEvaluatedKey']
            )
            data.extend(resp['Items'])
        for index, ddict in enumerate(data):
            if str(ddict["idkey"]).startswith(self.tagprefix):
                tagindexlist.append(index)
            else:
                for key, value in ddict.items():
                    if isinstance(value, Decimal):
                        ddict[key] = self._d_to_f(value)
                data[index] = ddict

        tagindexlist.reverse()
        for index in tagindexlist:
            del data[index]

        return data

    def get_all_as_dict(self) -> dict:
        """
        get all values in store \n
        :return:dict
        """
        retdict = {}
        plist = self.get_all_as_list()
        for idict in plist:
            retdict[idict["idkey"]] = idict
        return retdict

    def upsert(self, key: str, value: dict) -> bool:
        """
        adds a value to store
        :param key: key
        :param value: value to insert
        :return: bool
        """
        value = value.copy()
        if "idkey" not in value:
            value["idkey"] = key

        for key, data in value.items():
            if isinstance(data, float):
                value[key] = self._f_to_d(data)
        resp = self.table.put_item(Item=value)
        return self.issuccess(resp)

    def remove(self, key: str) -> bool:
        """
        removes the key from store
        :param key: str or list or tuple
        :return:
        """

        resp = self.table.delete_item(
            Key={
                'idkey': str(key),
            }
        )
        return self.issuccess(resp)

    def remove_keys(self, keys: list) -> bool:
        """
        removes the key from store
        :param keys:
        :return:
        """
        # ret = str(self.table.delete(keys))
        # return {"1": True}.get(ret, False)

        with self.table.batch_writer() as batch:
            for key in keys:
                batch.delete_item(Key={'idkey': str(key)})
        return True

    def flush(self):
        """
        Flushes current store\n
        :return: None
        """
        keys = self.keys()
        with self.table.batch_writer() as batch:
            for key in keys:
                batch.delete_item(Key={'idkey': key})

    def tags(self) -> list:
        """
        returns tag list \n
        :return:
        """
        fe = Key("idkey").begins_with(self.tagprefix)
        resp = self.table.scan(
            FilterExpression=fe,
            ProjectionExpression='idkey',
        )
        data = resp['Items']

        while 'LastEvaluatedKey' in resp:
            resp = self.table.scan(
                FilterExpression=fe,
                ProjectionExpression='idkey',
                ExclusiveStartKey=resp['LastEvaluatedKey']
            )
            data.extend(resp['Items'])
        for index, ddict in enumerate(data):
            data[index] = ddict

        return [rdict['idkey'].replace(self.tagprefix, "", 1) for rdict in data]

    def gettagkeys(self, tag: str) -> list:
        """
        get all keys of given tag \n
        :param tag:
        :return:
        """
        tdict = self.get(self.tagprefix + tag)
        retval = tdict[self.taglistkey] if tdict else []
        return retval

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
        tags = self.gettagkeys(tag)
        tags.append(key)
        tags = list(set(tags))
        ukey = self.tagprefix + tag
        self.upsert(ukey, {"idkey": ukey, self.taglistkey: tags})

    def removefromtag(self, tag: str, key: str or list):
        """
        Remove items from lists \n
        :param tag: str
        :param key: str or list
        :return: None
        """

        tags = list(set(self.gettagkeys(tag)))
        if isinstance(key, str):
            # noinspection PyBroadException
            try:
                tags.remove(key)
            except Exception:
                pass
        else:
            for k in key:
                # noinspection PyBroadException
                try:
                    tags.remove(k)
                except Exception:
                    pass

        ukey = self.tagprefix + tag
        self.upsert(ukey, {"idkey": ukey, self.taglistkey: tags})
