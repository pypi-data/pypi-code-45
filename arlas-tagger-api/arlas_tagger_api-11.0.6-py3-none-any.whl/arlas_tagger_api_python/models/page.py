# coding: utf-8

"""
    ARLAS Tagger API

    (Un)Tag fields of ARLAS collections

    OpenAPI spec version: 11.0.6
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Page(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'size': 'int',
        '_from': 'int',
        'sort': 'str',
        'after': 'str',
        'before': 'str'
    }

    attribute_map = {
        'size': 'size',
        '_from': 'from',
        'sort': 'sort',
        'after': 'after',
        'before': 'before'
    }

    def __init__(self, size=None, _from=None, sort=None, after=None, before=None):
        """
        Page - a model defined in Swagger
        """

        self._size = None
        self.__from = None
        self._sort = None
        self._after = None
        self._before = None

        if size is not None:
          self.size = size
        if _from is not None:
          self._from = _from
        if sort is not None:
          self.sort = sort
        if after is not None:
          self.after = after
        if before is not None:
          self.before = before

    @property
    def size(self):
        """
        Gets the size of this Page.

        :return: The size of this Page.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Page.

        :param size: The size of this Page.
        :type: int
        """

        self._size = size

    @property
    def _from(self):
        """
        Gets the _from of this Page.

        :return: The _from of this Page.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this Page.

        :param _from: The _from of this Page.
        :type: int
        """

        self.__from = _from

    @property
    def sort(self):
        """
        Gets the sort of this Page.

        :return: The sort of this Page.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this Page.

        :param sort: The sort of this Page.
        :type: str
        """

        self._sort = sort

    @property
    def after(self):
        """
        Gets the after of this Page.

        :return: The after of this Page.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this Page.

        :param after: The after of this Page.
        :type: str
        """

        self._after = after

    @property
    def before(self):
        """
        Gets the before of this Page.

        :return: The before of this Page.
        :rtype: str
        """
        return self._before

    @before.setter
    def before(self, before):
        """
        Sets the before of this Page.

        :param before: The before of this Page.
        :type: str
        """

        self._before = before

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Page):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
