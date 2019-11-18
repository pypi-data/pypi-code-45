# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: 2.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1Sequence(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'count': 'str',
        'end': 'str',
        'format': 'str',
        'start': 'str'
    }

    attribute_map = {
        'count': 'count',
        'end': 'end',
        'format': 'format',
        'start': 'start'
    }

    def __init__(self, count=None, end=None, format=None, start=None):  # noqa: E501
        """V1alpha1Sequence - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._end = None
        self._format = None
        self._start = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if end is not None:
            self.end = end
        if format is not None:
            self.format = format
        if start is not None:
            self.start = start

    @property
    def count(self):
        """Gets the count of this V1alpha1Sequence.  # noqa: E501

        Count is number of elements in the sequence (default: 0). Not to be used with end  # noqa: E501

        :return: The count of this V1alpha1Sequence.  # noqa: E501
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this V1alpha1Sequence.

        Count is number of elements in the sequence (default: 0). Not to be used with end  # noqa: E501

        :param count: The count of this V1alpha1Sequence.  # noqa: E501
        :type: str
        """

        self._count = count

    @property
    def end(self):
        """Gets the end of this V1alpha1Sequence.  # noqa: E501

        Number at which to end the sequence (default: 0). Not to be used with Count  # noqa: E501

        :return: The end of this V1alpha1Sequence.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this V1alpha1Sequence.

        Number at which to end the sequence (default: 0). Not to be used with Count  # noqa: E501

        :param end: The end of this V1alpha1Sequence.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def format(self):
        """Gets the format of this V1alpha1Sequence.  # noqa: E501

        Format is a printf format string to format the value in the sequence  # noqa: E501

        :return: The format of this V1alpha1Sequence.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this V1alpha1Sequence.

        Format is a printf format string to format the value in the sequence  # noqa: E501

        :param format: The format of this V1alpha1Sequence.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def start(self):
        """Gets the start of this V1alpha1Sequence.  # noqa: E501

        Number at which to start the sequence (default: 0)  # noqa: E501

        :return: The start of this V1alpha1Sequence.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this V1alpha1Sequence.

        Number at which to start the sequence (default: 0)  # noqa: E501

        :param start: The start of this V1alpha1Sequence.  # noqa: E501
        :type: str
        """

        self._start = start

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, V1alpha1Sequence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
