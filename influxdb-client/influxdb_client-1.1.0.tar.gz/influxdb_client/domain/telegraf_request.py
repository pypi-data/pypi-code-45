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


class TelegrafRequest(object):
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
        'description': 'str',
        'agent': 'TelegrafRequestAgent',
        'plugins': 'list[TelegrafRequestPlugin]',
        'org_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'agent': 'agent',
        'plugins': 'plugins',
        'org_id': 'orgID'
    }

    def __init__(self, name=None, description=None, agent=None, plugins=None, org_id=None):  # noqa: E501
        """TelegrafRequest - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._description = None
        self._agent = None
        self._plugins = None
        self._org_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if agent is not None:
            self.agent = agent
        if plugins is not None:
            self.plugins = plugins
        if org_id is not None:
            self.org_id = org_id

    @property
    def name(self):
        """Gets the name of this TelegrafRequest.  # noqa: E501


        :return: The name of this TelegrafRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TelegrafRequest.


        :param name: The name of this TelegrafRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this TelegrafRequest.  # noqa: E501


        :return: The description of this TelegrafRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TelegrafRequest.


        :param description: The description of this TelegrafRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def agent(self):
        """Gets the agent of this TelegrafRequest.  # noqa: E501


        :return: The agent of this TelegrafRequest.  # noqa: E501
        :rtype: TelegrafRequestAgent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this TelegrafRequest.


        :param agent: The agent of this TelegrafRequest.  # noqa: E501
        :type: TelegrafRequestAgent
        """

        self._agent = agent

    @property
    def plugins(self):
        """Gets the plugins of this TelegrafRequest.  # noqa: E501


        :return: The plugins of this TelegrafRequest.  # noqa: E501
        :rtype: list[TelegrafRequestPlugin]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this TelegrafRequest.


        :param plugins: The plugins of this TelegrafRequest.  # noqa: E501
        :type: list[TelegrafRequestPlugin]
        """

        self._plugins = plugins

    @property
    def org_id(self):
        """Gets the org_id of this TelegrafRequest.  # noqa: E501


        :return: The org_id of this TelegrafRequest.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this TelegrafRequest.


        :param org_id: The org_id of this TelegrafRequest.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

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
        if not isinstance(other, TelegrafRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
