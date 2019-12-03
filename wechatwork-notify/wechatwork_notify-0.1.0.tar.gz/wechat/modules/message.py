#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 9:33 PM
# @Author  : jack.du
# @Email   : xianghua.du@start.com.cn
# @File    : message.py
# @Software: PyCharm
import six


class Text(object):
    attr_types = {
        'content': 'str'
    }
    def __init__(self, content):
        self.content = content

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if isinstance(content, str):
            self._content = content
        else:
            raise ValueError("content only str types.")

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.attr_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

class Video(object):
    attr_types = {
        'media_id': 'str',
        'title': 'str',
        'description': 'str'
    }

    def __init__(self, media_id, title=None, description=None):
        self._media_id = None
        self._title = None
        self._description = None

        if media_id is not None:
            self._media_id = media_id
        if title is not None:
            self._title = title
        if description is not None:
            self._description = None

    @property
    def media_id(self):
        if self._media_id is None:
            raise ValueError("content can't is None.")
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        if isinstance(media_id, str):
            self._media_id = media_id
        else:
            raise ValueError("content only str types.")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        '''
        :param title:
        :return:
        '''
        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError("title only str types.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,description):
        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.attr_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

class Markdown(Text):
    pass

class Message(object):
    attr_types = {}
    text_attr_types = {
        'touser': 'str',
        'toparty': 'str',
        'totag': 'str',
        'agentid': 'int',
        'msgtype': 'str',
        'text': 'Text',
        'enable_duplicate_check': 'bool',
        'duplicate_check_interval': 'str'
    }

    markdown_attr_types = {
        'touser': 'str',
        'toparty': 'str',
        'totag': 'str',
        'agentid': 'int',
        'msgtype': 'str',
        'markdown': 'Markdown',
        'enable_duplicate_check': 'bool',
        'duplicate_check_interval': 'str'
    }

    def __init__(self,touser=None, toparty=None, totag=None, agentid=None, safe=None, msgtype=None,
                 enable_id_trans=None, enable_duplicate_check=None, duplicate_check_interval=None, *args, **kwargs):
        self._touser = '@all'
        self._toparty = None
        self._totag = None
        self._agentid = None
        self._safe = None
        self._msgtype = None
        self._text = None
        self._markdown = None
        self._enable_id_trans = 0
        self._enable_duplicate_check = 0
        self._duplicate_check_interval = 1800


        if touser is not None:
            self.touser = touser
        if toparty is not None:
            self.toparty = toparty
        if totag is not None:
            self.totag = totag
        if msgtype is not None:
            self.msgtype = msgtype
        if agentid is not None:
            self.agentid = agentid
        if safe is not None:
            self.safe =safe


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self,text):
        self._text = text
        self.msgtype = 'text'
        self.attr_types = self.text_attr_types

    @property
    def markdown(self):
        return self._markdown

    @markdown.setter
    def markdown(self, markdown):
        self._markdown = markdown
        self.msgtype = 'markdown'
        self.attr_types = self.markdown_attr_types

    @property
    def msgtype(self):
        return self._msgtype

    @msgtype.setter
    def msgtype(self, msgtype):
        self._msgtype = msgtype

    @property
    def touser(self):
        return self._touser

    @touser.setter
    def touser(self,touser):
        self._touser = touser

    @property
    def toparty(self):
        return self._toparty

    @toparty.setter
    def toparty(self, toparty):
        self._toparty = toparty

    @property
    def totag(self):
        return self._totag

    @totag.setter
    def totag(self, totag):
        self._totag = totag

    @property
    def agentid(self):
        if self._agentid is not None:
            return self._agentid
        else:
            raise ValueError("agentid attributes of message class can't is none")

    @agentid.setter
    def agentid(self, agentid):
        try:
            self._agentid = int(agentid)
        except ValueError:
            raise ValueError("invalid value agentid: %s" %agentid)

    @property
    def safe(self):
        return self._safe

    @safe.setter
    def safe(self, safe):
        self._safe = safe

    @property
    def enable_duplicate_check(self):
        return self._enable_duplicate_check

    @enable_duplicate_check.setter
    def enable_duplicate_check(self, enable_duplicate_check):
        self._enable_duplicate_check = enable_duplicate_check

    @property
    def duplicate_check_interval(self):
        return self._duplicate_check_interval

    @duplicate_check_interval.setter
    def duplicate_check_interval(self, duplicate_check_interval):
        self._duplicate_check_interval = duplicate_check_interval

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.attr_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result