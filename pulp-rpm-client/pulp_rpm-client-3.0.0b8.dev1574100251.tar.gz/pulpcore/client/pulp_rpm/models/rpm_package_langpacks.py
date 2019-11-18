# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_rpm.configuration import Configuration


class RpmPackageLangpacks(object):
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
        'matches': 'object',
        'digest': 'str'
    }

    attribute_map = {
        'matches': 'matches',
        'digest': 'digest'
    }

    def __init__(self, matches=None, digest=None, local_vars_configuration=None):  # noqa: E501
        """RpmPackageLangpacks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._matches = None
        self._digest = None
        self.discriminator = None

        self.matches = matches
        self.digest = digest

    @property
    def matches(self):
        """Gets the matches of this RpmPackageLangpacks.  # noqa: E501

        Langpacks matches.  # noqa: E501

        :return: The matches of this RpmPackageLangpacks.  # noqa: E501
        :rtype: object
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this RpmPackageLangpacks.

        Langpacks matches.  # noqa: E501

        :param matches: The matches of this RpmPackageLangpacks.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and matches is None:  # noqa: E501
            raise ValueError("Invalid value for `matches`, must not be `None`")  # noqa: E501

        self._matches = matches

    @property
    def digest(self):
        """Gets the digest of this RpmPackageLangpacks.  # noqa: E501

        Langpacks digest.  # noqa: E501

        :return: The digest of this RpmPackageLangpacks.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this RpmPackageLangpacks.

        Langpacks digest.  # noqa: E501

        :param digest: The digest of this RpmPackageLangpacks.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and digest is None:  # noqa: E501
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                digest is not None and len(digest) < 1):
            raise ValueError("Invalid value for `digest`, length must be greater than or equal to `1`")  # noqa: E501

        self._digest = digest

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
        if not isinstance(other, RpmPackageLangpacks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmPackageLangpacks):
            return True

        return self.to_dict() != other.to_dict()
