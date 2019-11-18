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


class CreateDashboardRequest(object):
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
        'org_id': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'org_id': 'orgID',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, org_id=None, name=None, description=None):  # noqa: E501
        """CreateDashboardRequest - a model defined in OpenAPI"""  # noqa: E501

        self._org_id = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.org_id = org_id
        self.name = name
        if description is not None:
            self.description = description

    @property
    def org_id(self):
        """Gets the org_id of this CreateDashboardRequest.  # noqa: E501

        The ID of the organization that owns the dashboard.  # noqa: E501

        :return: The org_id of this CreateDashboardRequest.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CreateDashboardRequest.

        The ID of the organization that owns the dashboard.  # noqa: E501

        :param org_id: The org_id of this CreateDashboardRequest.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this CreateDashboardRequest.  # noqa: E501

        The user-facing name of the dashboard.  # noqa: E501

        :return: The name of this CreateDashboardRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDashboardRequest.

        The user-facing name of the dashboard.  # noqa: E501

        :param name: The name of this CreateDashboardRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateDashboardRequest.  # noqa: E501

        The user-facing description of the dashboard.  # noqa: E501

        :return: The description of this CreateDashboardRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDashboardRequest.

        The user-facing description of the dashboard.  # noqa: E501

        :param description: The description of this CreateDashboardRequest.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, CreateDashboardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
