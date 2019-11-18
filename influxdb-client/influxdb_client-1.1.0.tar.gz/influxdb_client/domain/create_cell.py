# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CreateCell(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'x': 'int',
        'y': 'int',
        'w': 'int',
        'h': 'int',
        'using_view': 'str'
    }

    attribute_map = {
        'name': 'name',
        'x': 'x',
        'y': 'y',
        'w': 'w',
        'h': 'h',
        'using_view': 'usingView'
    }

    def __init__(self, name=None, x=None, y=None, w=None, h=None, using_view=None):  # noqa: E501
        """CreateCell - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._x = None
        self._y = None
        self._w = None
        self._h = None
        self._using_view = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if w is not None:
            self.w = w
        if h is not None:
            self.h = h
        if using_view is not None:
            self.using_view = using_view

    @property
    def name(self):
        """Gets the name of this CreateCell.  # noqa: E501


        :return: The name of this CreateCell.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCell.


        :param name: The name of this CreateCell.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def x(self):
        """Gets the x of this CreateCell.  # noqa: E501


        :return: The x of this CreateCell.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this CreateCell.


        :param x: The x of this CreateCell.  # noqa: E501
        :type: int
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this CreateCell.  # noqa: E501


        :return: The y of this CreateCell.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this CreateCell.


        :param y: The y of this CreateCell.  # noqa: E501
        :type: int
        """

        self._y = y

    @property
    def w(self):
        """Gets the w of this CreateCell.  # noqa: E501


        :return: The w of this CreateCell.  # noqa: E501
        :rtype: int
        """
        return self._w

    @w.setter
    def w(self, w):
        """Sets the w of this CreateCell.


        :param w: The w of this CreateCell.  # noqa: E501
        :type: int
        """

        self._w = w

    @property
    def h(self):
        """Gets the h of this CreateCell.  # noqa: E501


        :return: The h of this CreateCell.  # noqa: E501
        :rtype: int
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this CreateCell.


        :param h: The h of this CreateCell.  # noqa: E501
        :type: int
        """

        self._h = h

    @property
    def using_view(self):
        """Gets the using_view of this CreateCell.  # noqa: E501

        Makes a copy of the provided view.  # noqa: E501

        :return: The using_view of this CreateCell.  # noqa: E501
        :rtype: str
        """
        return self._using_view

    @using_view.setter
    def using_view(self, using_view):
        """Sets the using_view of this CreateCell.

        Makes a copy of the provided view.  # noqa: E501

        :param using_view: The using_view of this CreateCell.  # noqa: E501
        :type: str
        """

        self._using_view = using_view

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateCell):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
