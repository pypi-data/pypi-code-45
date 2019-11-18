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


class TagRefRequest(object):
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
        'search': 'Search',
        'tag': 'Tag',
        'propagation': 'Propagation',
        'label': 'str',
        'id': 'str',
        'action': 'str',
        'collection': 'str',
        'partition_filter': 'str',
        'propagated': 'int',
        'creation_time': 'int'
    }

    attribute_map = {
        'search': 'search',
        'tag': 'tag',
        'propagation': 'propagation',
        'label': 'label',
        'id': 'id',
        'action': 'action',
        'collection': 'collection',
        'partition_filter': 'partitionFilter',
        'propagated': 'propagated',
        'creation_time': 'creationTime'
    }

    def __init__(self, search=None, tag=None, propagation=None, label=None, id=None, action=None, collection=None, partition_filter=None, propagated=None, creation_time=None):
        """
        TagRefRequest - a model defined in Swagger
        """

        self._search = None
        self._tag = None
        self._propagation = None
        self._label = None
        self._id = None
        self._action = None
        self._collection = None
        self._partition_filter = None
        self._propagated = None
        self._creation_time = None

        if search is not None:
          self.search = search
        if tag is not None:
          self.tag = tag
        if propagation is not None:
          self.propagation = propagation
        if label is not None:
          self.label = label
        if id is not None:
          self.id = id
        if action is not None:
          self.action = action
        if collection is not None:
          self.collection = collection
        if partition_filter is not None:
          self.partition_filter = partition_filter
        if propagated is not None:
          self.propagated = propagated
        if creation_time is not None:
          self.creation_time = creation_time

    @property
    def search(self):
        """
        Gets the search of this TagRefRequest.

        :return: The search of this TagRefRequest.
        :rtype: Search
        """
        return self._search

    @search.setter
    def search(self, search):
        """
        Sets the search of this TagRefRequest.

        :param search: The search of this TagRefRequest.
        :type: Search
        """

        self._search = search

    @property
    def tag(self):
        """
        Gets the tag of this TagRefRequest.

        :return: The tag of this TagRefRequest.
        :rtype: Tag
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this TagRefRequest.

        :param tag: The tag of this TagRefRequest.
        :type: Tag
        """

        self._tag = tag

    @property
    def propagation(self):
        """
        Gets the propagation of this TagRefRequest.

        :return: The propagation of this TagRefRequest.
        :rtype: Propagation
        """
        return self._propagation

    @propagation.setter
    def propagation(self, propagation):
        """
        Sets the propagation of this TagRefRequest.

        :param propagation: The propagation of this TagRefRequest.
        :type: Propagation
        """

        self._propagation = propagation

    @property
    def label(self):
        """
        Gets the label of this TagRefRequest.

        :return: The label of this TagRefRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this TagRefRequest.

        :param label: The label of this TagRefRequest.
        :type: str
        """

        self._label = label

    @property
    def id(self):
        """
        Gets the id of this TagRefRequest.

        :return: The id of this TagRefRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TagRefRequest.

        :param id: The id of this TagRefRequest.
        :type: str
        """

        self._id = id

    @property
    def action(self):
        """
        Gets the action of this TagRefRequest.

        :return: The action of this TagRefRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this TagRefRequest.

        :param action: The action of this TagRefRequest.
        :type: str
        """
        allowed_values = ["ADD", "REMOVE", "REMOVEALL"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def collection(self):
        """
        Gets the collection of this TagRefRequest.

        :return: The collection of this TagRefRequest.
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """
        Sets the collection of this TagRefRequest.

        :param collection: The collection of this TagRefRequest.
        :type: str
        """

        self._collection = collection

    @property
    def partition_filter(self):
        """
        Gets the partition_filter of this TagRefRequest.

        :return: The partition_filter of this TagRefRequest.
        :rtype: str
        """
        return self._partition_filter

    @partition_filter.setter
    def partition_filter(self, partition_filter):
        """
        Sets the partition_filter of this TagRefRequest.

        :param partition_filter: The partition_filter of this TagRefRequest.
        :type: str
        """

        self._partition_filter = partition_filter

    @property
    def propagated(self):
        """
        Gets the propagated of this TagRefRequest.

        :return: The propagated of this TagRefRequest.
        :rtype: int
        """
        return self._propagated

    @propagated.setter
    def propagated(self, propagated):
        """
        Sets the propagated of this TagRefRequest.

        :param propagated: The propagated of this TagRefRequest.
        :type: int
        """

        self._propagated = propagated

    @property
    def creation_time(self):
        """
        Gets the creation_time of this TagRefRequest.

        :return: The creation_time of this TagRefRequest.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this TagRefRequest.

        :param creation_time: The creation_time of this TagRefRequest.
        :type: int
        """

        self._creation_time = creation_time

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
        if not isinstance(other, TagRefRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
