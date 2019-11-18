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


class NotificationEndpointBase(object):
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
        'id': 'str',
        'org_id': 'str',
        'user_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'description': 'str',
        'name': 'str',
        'status': 'str',
        'labels': 'list[Label]',
        'links': 'NotificationEndpointBaseLinks',
        'type': 'NotificationEndpointType'
    }

    attribute_map = {
        'id': 'id',
        'org_id': 'orgID',
        'user_id': 'userID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'description': 'description',
        'name': 'name',
        'status': 'status',
        'labels': 'labels',
        'links': 'links',
        'type': 'type'
    }

    def __init__(self, id=None, org_id=None, user_id=None, created_at=None, updated_at=None, description=None, name=None, status='active', labels=None, links=None, type=None):  # noqa: E501
        """NotificationEndpointBase - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._org_id = None
        self._user_id = None
        self._created_at = None
        self._updated_at = None
        self._description = None
        self._name = None
        self._status = None
        self._labels = None
        self._links = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if org_id is not None:
            self.org_id = org_id
        if user_id is not None:
            self.user_id = user_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if description is not None:
            self.description = description
        self.name = name
        if status is not None:
            self.status = status
        if labels is not None:
            self.labels = labels
        if links is not None:
            self.links = links
        self.type = type

    @property
    def id(self):
        """Gets the id of this NotificationEndpointBase.  # noqa: E501


        :return: The id of this NotificationEndpointBase.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationEndpointBase.


        :param id: The id of this NotificationEndpointBase.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this NotificationEndpointBase.  # noqa: E501


        :return: The org_id of this NotificationEndpointBase.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this NotificationEndpointBase.


        :param org_id: The org_id of this NotificationEndpointBase.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def user_id(self):
        """Gets the user_id of this NotificationEndpointBase.  # noqa: E501


        :return: The user_id of this NotificationEndpointBase.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NotificationEndpointBase.


        :param user_id: The user_id of this NotificationEndpointBase.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this NotificationEndpointBase.  # noqa: E501


        :return: The created_at of this NotificationEndpointBase.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NotificationEndpointBase.


        :param created_at: The created_at of this NotificationEndpointBase.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NotificationEndpointBase.  # noqa: E501


        :return: The updated_at of this NotificationEndpointBase.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NotificationEndpointBase.


        :param updated_at: The updated_at of this NotificationEndpointBase.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def description(self):
        """Gets the description of this NotificationEndpointBase.  # noqa: E501

        An optional description of the notification endpoint.  # noqa: E501

        :return: The description of this NotificationEndpointBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NotificationEndpointBase.

        An optional description of the notification endpoint.  # noqa: E501

        :param description: The description of this NotificationEndpointBase.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this NotificationEndpointBase.  # noqa: E501


        :return: The name of this NotificationEndpointBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationEndpointBase.


        :param name: The name of this NotificationEndpointBase.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this NotificationEndpointBase.  # noqa: E501

        The status of the endpoint.  # noqa: E501

        :return: The status of this NotificationEndpointBase.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NotificationEndpointBase.

        The status of the endpoint.  # noqa: E501

        :param status: The status of this NotificationEndpointBase.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def labels(self):
        """Gets the labels of this NotificationEndpointBase.  # noqa: E501


        :return: The labels of this NotificationEndpointBase.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NotificationEndpointBase.


        :param labels: The labels of this NotificationEndpointBase.  # noqa: E501
        :type: list[Label]
        """

        self._labels = labels

    @property
    def links(self):
        """Gets the links of this NotificationEndpointBase.  # noqa: E501


        :return: The links of this NotificationEndpointBase.  # noqa: E501
        :rtype: NotificationEndpointBaseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NotificationEndpointBase.


        :param links: The links of this NotificationEndpointBase.  # noqa: E501
        :type: NotificationEndpointBaseLinks
        """

        self._links = links

    @property
    def type(self):
        """Gets the type of this NotificationEndpointBase.  # noqa: E501


        :return: The type of this NotificationEndpointBase.  # noqa: E501
        :rtype: NotificationEndpointType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NotificationEndpointBase.


        :param type: The type of this NotificationEndpointBase.  # noqa: E501
        :type: NotificationEndpointType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, NotificationEndpointBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
