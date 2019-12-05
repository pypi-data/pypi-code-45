# -*- coding: utf-8 -*-
import json
import os
import uuid
import zipfile

from simplejsonobject import JsonObject

from nosqlmodel.connectors.redisconnector import RedisConnector

__author__ = 'ozgur'
__creation_date__ = '12.09.2019' '13:48'


class BaseNoSqlModel(JsonObject):
    """
    Nosql model with basic functionality\n
    """

    class Meta:
        connector = RedisConnector()
        indexkey = None

    def __init__(self):
        self.idkey = None

    def delete_table(self):
        """
        deletes table from db
        :return:
        """
        self.Meta.connector.delete_table()

    def create_table(self):
        """
        creates a new table, delete first if exists \n
        :return:
        """
        self.Meta.connector.create_table()

    @classmethod
    def flush(cls):
        """
        flushes al records
        :return: None
        """
        cls.Meta.connector.flush()

    @classmethod
    def dbsize(cls) -> int:
        """
        returns the itemcount in db
        :return: item count
        """
        return cls.Meta.connector.dbsize()

    @classmethod
    def get_keys(cls, pattern: str = "*") -> list:
        """
        return all idkeys in db
        :return:
        """
        return cls.Meta.connector.keys(pattern)

    def get_by_id(self, idkey: str) -> bool:
        """
        get item by id
        :return:
        """
        ret = self.Meta.connector.get(idkey)
        if ret:
            self.from_dict(ret)
            return True
        else:
            return False

    def get_or_create_by_id(self, idkey: str) -> bool:
        """
        get item by id
        :return:
        """
        ret = self.Meta.connector.get(idkey)
        if ret:
            self.from_dict(ret)
            return True
        else:
            self.__dict__[self.Meta.indexkey] = idkey
            return False

    @classmethod
    def get_all_as_list(cls) -> list:
        """
        returns all db as list of item dicts\n
        :return:  [object_dict]
        """
        return cls.Meta.connector.get_all_as_list()

    @classmethod
    def get_all_as_dict(cls) -> dict:
        """
        returns all db as dict of item dicts\n
        :return:  {"id":object_dict,}
        """
        return cls.Meta.connector.get_all_as_dict()

    @classmethod
    def get_all_as_objectlist(cls) -> list:
        """
        returns all db as list of item objects\n
        :return:  [object]
        """
        retlist = []
        for itemdict in cls.get_all_as_list():
            retobj = cls()
            retobj.from_dict(itemdict)
            retlist.append(retobj)
        return retlist

    @classmethod
    def get_all_as_objectdict(cls) -> dict:
        """
        returns all db as dict of item objects\n
        :return:  {key:object}
        """
        retdict = {}
        for key, itemdict in cls.get_all_as_dict():
            retobj = cls()
            retobj.from_dict(itemdict)
            retdict[key] = retobj
        return retdict

    def save_to_cache(self, tags: list = None) -> bool:
        """
        saves object
        :return: success status
        """
        if not self.idkey:
            if self.Meta.indexkey:
                bnoid = self.__dict__.get(self.Meta.indexkey, None)
                self.idkey = bnoid if bnoid else str(uuid.uuid4())
            else:
                self.idkey = str(uuid.uuid4())
        else:
            pass
        retval = self.Meta.connector.upsert(self.idkey, self.to_dict())

        if tags:
            tnew = [x for x in tags if x]
            self.add_tags_to_item(tnew)

        return retval

    def delete(self):
        """
        Deletes item from redis \n
        :return: None
        """
        if not self.idkey:
            raise KeyError("First you must save to remove it")
        self.Meta.connector.remove(self.idkey)

    @classmethod
    def get_tag_keys(cls, tag: str) -> list:
        """
        returns keys tagged bay given tag
        :return: list
        """
        return cls.Meta.connector.gettagkeys(tag)

    @classmethod
    def get_tags(cls) -> list:
        """
        returns tag list
        :return: list
        """
        return cls.Meta.connector.tags()

    @classmethod
    def get_by_tag(cls, tag: str) -> list:
        """
        returns obejct list tagged by given tag
        :return:[BaseNosqlModel]
        """
        retlist = []
        for itemdict in cls.Meta.connector.gettag(tag):
            retobj = cls()
            retobj.from_dict(itemdict)
            retlist.append(retobj)
        return retlist

    def add_tags_to_item(self, taglist: list):
        """
        adds tags to object
        :param taglist:
        :return:
        """
        if not self.idkey:
            raise KeyError("You must save before adding a tag")
        for tag in taglist:
            self.Meta.connector.addtag(tag, self.idkey)

    def remove_item_from_tag(self, tag: str):
        if not self.idkey:
            raise KeyError("You must save before removing from a tag")
        self.Meta.connector.removefromtag(tag, self.idkey)

    def from_dict(self, updatedict: dict):
        """
        populates data from dict
        Warning this will also overrides the id too!!        \n
        :param updatedict: dict which contains data
        :return: None
        """
        try:
            del updatedict["connector"]
        except (KeyError, TypeError):
            pass
        super().from_dict(updatedict.copy())

    def to_dict(self) -> dict:
        """
        populates data to dict \n
        :return: None
        """
        retval = super().to_dict()
        try:
            del retval["connector"]
        except (KeyError, TypeError):
            pass
        return retval

    @classmethod
    def export_to_json_text(cls, exportdict: dict = None, compress_data=False) -> str:
        """
         transforms exportdict or whole database into json \n
        :param compress_data: bool, data will be compressed or not
        :param exportdict: must be dictionary of same class objects
        :return: returns a json compliant text file
        """
        edict = {}
        if exportdict:
            for key, value in exportdict.items():
                try:
                    edict[key] = value.to_dict()
                except AttributeError:
                    pass
        else:
            edict = cls.Meta.connector.get_all_as_dict()
        if compress_data:
            for key, subdict in edict.items():
                edict[key] = dict((i, d) for i, d in subdict if d)

            retval = json.dumps(edict, ensure_ascii=False, indent=4)
        else:
            retval = json.dumps(edict, ensure_ascii=False)
        return retval

    @classmethod
    def export_to_json_file(cls, filepath: str, exportdict: dict = None, compress_data=False):
        """
         transforms exportdict or whole database into *.json file \n
        :param filepath: must end with .json
        :param exportdict: must be dictionary of same class objects
        :param compress_data: bool, data will be compressed or not
        :return:
        """
        with open(filepath, "w") as ofile:
            ofile.write(cls.export_to_json_text(exportdict, compress_data=compress_data))

    @classmethod
    def export_to_json_zip(cls, filepath: str, exportdict: dict = None, compress_data=False):
        """
         transforms exportdict or whole database into *.zip file \n
        :param filepath: must be end with .zip
        :param exportdict: must be dictionary of same class objects
        :param compress_data: bool, data will be compressed or not
        :return:
        """
        if not filepath.endswith(".zip"):
            raise FileNotFoundError("Wrong filename:" + filepath)
        else:
            tempfilepath = filepath.replace(".zip", ".json")
        cls.export_to_json_file(tempfilepath, exportdict, compress_data=compress_data)
        zipfile.ZipFile(filepath, mode='w').write(tempfilepath)
        os.remove(tempfilepath)

    @classmethod
    def import_from_json_text(cls, jsontext: str):
        """
        import and update db from exported json text \n
        :param jsontext: exported json text
        :return:
        """
        datadict = json.loads(jsontext, encoding="UTF-8")
        for key, value in datadict.items():
            instance = cls()
            instance.from_dict(value)
            instance.save_to_cache()

    @classmethod
    def import_from_json_file(cls, filepath: str):
        """
        import and update db from exported *.json file \n
        :param filepath: exported *.json file
        :return:
        """
        with open(filepath, "r") as ofile:
            content = ofile.read()
            cls.import_from_json_text(content)

    @classmethod
    def import_from_json_zip(cls, filepath: str):
        """
        import and update db from exported *.json file \n
        :param filepath: exported *.json file
        :return:
        """
        if not filepath.endswith(".zip"):
            raise FileNotFoundError("Wrong filename:" + filepath)
        else:
            tempfilepath = filepath.replace(".zip", ".json")

        with zipfile.ZipFile(filepath, 'r') as zipObj:
            zipObj.extractall("/")
        cls.import_from_json_file(tempfilepath)
        os.remove(tempfilepath)
