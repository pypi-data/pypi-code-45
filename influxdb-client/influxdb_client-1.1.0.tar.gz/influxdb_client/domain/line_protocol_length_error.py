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


class LineProtocolLengthError(object):
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
        'code': 'str',
        'message': 'str',
        'max_length': 'int'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'max_length': 'maxLength'
    }

    def __init__(self, code=None, message=None, max_length=None):  # noqa: E501
        """LineProtocolLengthError - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._message = None
        self._max_length = None
        self.discriminator = None

        self.code = code
        self.message = message
        self.max_length = max_length

    @property
    def code(self):
        """Gets the code of this LineProtocolLengthError.  # noqa: E501

        Code is the machine-readable error code.  # noqa: E501

        :return: The code of this LineProtocolLengthError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LineProtocolLengthError.

        Code is the machine-readable error code.  # noqa: E501

        :param code: The code of this LineProtocolLengthError.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this LineProtocolLengthError.  # noqa: E501

        Message is a human-readable message.  # noqa: E501

        :return: The message of this LineProtocolLengthError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LineProtocolLengthError.

        Message is a human-readable message.  # noqa: E501

        :param message: The message of this LineProtocolLengthError.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def max_length(self):
        """Gets the max_length of this LineProtocolLengthError.  # noqa: E501

        Max length in bytes for a body of line-protocol.  # noqa: E501

        :return: The max_length of this LineProtocolLengthError.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this LineProtocolLengthError.

        Max length in bytes for a body of line-protocol.  # noqa: E501

        :param max_length: The max_length of this LineProtocolLengthError.  # noqa: E501
        :type: int
        """
        if max_length is None:
            raise ValueError("Invalid value for `max_length`, must not be `None`")  # noqa: E501

        self._max_length = max_length

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
        if not isinstance(other, LineProtocolLengthError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
