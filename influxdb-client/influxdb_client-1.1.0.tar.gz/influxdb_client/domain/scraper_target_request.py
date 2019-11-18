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


class ScraperTargetRequest(object):
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
        'url': 'str',
        'org_id': 'str',
        'bucket_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'url': 'url',
        'org_id': 'orgID',
        'bucket_id': 'bucketID'
    }

    def __init__(self, name=None, type=None, url=None, org_id=None, bucket_id=None):  # noqa: E501
        """ScraperTargetRequest - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._type = None
        self._url = None
        self._org_id = None
        self._bucket_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if org_id is not None:
            self.org_id = org_id
        if bucket_id is not None:
            self.bucket_id = bucket_id

    @property
    def name(self):
        """Gets the name of this ScraperTargetRequest.  # noqa: E501

        The name of the scraper target.  # noqa: E501

        :return: The name of this ScraperTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScraperTargetRequest.

        The name of the scraper target.  # noqa: E501

        :param name: The name of this ScraperTargetRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ScraperTargetRequest.  # noqa: E501

        The type of the metrics to be parsed.  # noqa: E501

        :return: The type of this ScraperTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScraperTargetRequest.

        The type of the metrics to be parsed.  # noqa: E501

        :param type: The type of this ScraperTargetRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this ScraperTargetRequest.  # noqa: E501

        The URL of the metrics endpoint.  # noqa: E501

        :return: The url of this ScraperTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ScraperTargetRequest.

        The URL of the metrics endpoint.  # noqa: E501

        :param url: The url of this ScraperTargetRequest.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def org_id(self):
        """Gets the org_id of this ScraperTargetRequest.  # noqa: E501

        The organization ID.  # noqa: E501

        :return: The org_id of this ScraperTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this ScraperTargetRequest.

        The organization ID.  # noqa: E501

        :param org_id: The org_id of this ScraperTargetRequest.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def bucket_id(self):
        """Gets the bucket_id of this ScraperTargetRequest.  # noqa: E501

        The ID of the bucket to write to.  # noqa: E501

        :return: The bucket_id of this ScraperTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """Sets the bucket_id of this ScraperTargetRequest.

        The ID of the bucket to write to.  # noqa: E501

        :param bucket_id: The bucket_id of this ScraperTargetRequest.  # noqa: E501
        :type: str
        """

        self._bucket_id = bucket_id

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
        if not isinstance(other, ScraperTargetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
