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


class TelegrafPluginInputNetResponse(object):
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
        'type': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'comment': 'comment'
    }

    def __init__(self, name=None, type=None, comment=None):  # noqa: E501
        """TelegrafPluginInputNetResponse - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._type = None
        self._comment = None
        self.discriminator = None

        self.name = name
        self.type = type
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        """Gets the name of this TelegrafPluginInputNetResponse.  # noqa: E501


        :return: The name of this TelegrafPluginInputNetResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TelegrafPluginInputNetResponse.


        :param name: The name of this TelegrafPluginInputNetResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this TelegrafPluginInputNetResponse.  # noqa: E501


        :return: The type of this TelegrafPluginInputNetResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TelegrafPluginInputNetResponse.


        :param type: The type of this TelegrafPluginInputNetResponse.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this TelegrafPluginInputNetResponse.  # noqa: E501


        :return: The comment of this TelegrafPluginInputNetResponse.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this TelegrafPluginInputNetResponse.


        :param comment: The comment of this TelegrafPluginInputNetResponse.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if not isinstance(other, TelegrafPluginInputNetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
