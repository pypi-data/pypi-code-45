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
from influxdb_client.domain.view_properties import ViewProperties


class ScatterViewProperties(ViewProperties):
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
        'type': 'str',
        'queries': 'list[DashboardQuery]',
        'colors': 'list[str]',
        'shape': 'str',
        'note': 'str',
        'show_note_when_empty': 'bool',
        'x_column': 'str',
        'y_column': 'str',
        'fill_columns': 'list[str]',
        'symbol_columns': 'list[str]',
        'x_domain': 'list[float]',
        'y_domain': 'list[float]',
        'x_axis_label': 'str',
        'y_axis_label': 'str',
        'x_prefix': 'str',
        'x_suffix': 'str',
        'y_prefix': 'str',
        'y_suffix': 'str'
    }

    attribute_map = {
        'type': 'type',
        'queries': 'queries',
        'colors': 'colors',
        'shape': 'shape',
        'note': 'note',
        'show_note_when_empty': 'showNoteWhenEmpty',
        'x_column': 'xColumn',
        'y_column': 'yColumn',
        'fill_columns': 'fillColumns',
        'symbol_columns': 'symbolColumns',
        'x_domain': 'xDomain',
        'y_domain': 'yDomain',
        'x_axis_label': 'xAxisLabel',
        'y_axis_label': 'yAxisLabel',
        'x_prefix': 'xPrefix',
        'x_suffix': 'xSuffix',
        'y_prefix': 'yPrefix',
        'y_suffix': 'ySuffix'
    }

    def __init__(self, type=None, queries=None, colors=None, shape=None, note=None, show_note_when_empty=None, x_column=None, y_column=None, fill_columns=None, symbol_columns=None, x_domain=None, y_domain=None, x_axis_label=None, y_axis_label=None, x_prefix=None, x_suffix=None, y_prefix=None, y_suffix=None):  # noqa: E501
        """ScatterViewProperties - a model defined in OpenAPI"""  # noqa: E501
        ViewProperties.__init__(self)

        self._type = None
        self._queries = None
        self._colors = None
        self._shape = None
        self._note = None
        self._show_note_when_empty = None
        self._x_column = None
        self._y_column = None
        self._fill_columns = None
        self._symbol_columns = None
        self._x_domain = None
        self._y_domain = None
        self._x_axis_label = None
        self._y_axis_label = None
        self._x_prefix = None
        self._x_suffix = None
        self._y_prefix = None
        self._y_suffix = None
        self.discriminator = None

        self.type = type
        self.queries = queries
        self.colors = colors
        self.shape = shape
        self.note = note
        self.show_note_when_empty = show_note_when_empty
        self.x_column = x_column
        self.y_column = y_column
        self.fill_columns = fill_columns
        self.symbol_columns = symbol_columns
        self.x_domain = x_domain
        self.y_domain = y_domain
        self.x_axis_label = x_axis_label
        self.y_axis_label = y_axis_label
        self.x_prefix = x_prefix
        self.x_suffix = x_suffix
        self.y_prefix = y_prefix
        self.y_suffix = y_suffix

    @property
    def type(self):
        """Gets the type of this ScatterViewProperties.  # noqa: E501


        :return: The type of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScatterViewProperties.


        :param type: The type of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def queries(self):
        """Gets the queries of this ScatterViewProperties.  # noqa: E501


        :return: The queries of this ScatterViewProperties.  # noqa: E501
        :rtype: list[DashboardQuery]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this ScatterViewProperties.


        :param queries: The queries of this ScatterViewProperties.  # noqa: E501
        :type: list[DashboardQuery]
        """
        if queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501

        self._queries = queries

    @property
    def colors(self):
        """Gets the colors of this ScatterViewProperties.  # noqa: E501

        Colors define color encoding of data into a visualization  # noqa: E501

        :return: The colors of this ScatterViewProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this ScatterViewProperties.

        Colors define color encoding of data into a visualization  # noqa: E501

        :param colors: The colors of this ScatterViewProperties.  # noqa: E501
        :type: list[str]
        """
        if colors is None:
            raise ValueError("Invalid value for `colors`, must not be `None`")  # noqa: E501

        self._colors = colors

    @property
    def shape(self):
        """Gets the shape of this ScatterViewProperties.  # noqa: E501


        :return: The shape of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this ScatterViewProperties.


        :param shape: The shape of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def note(self):
        """Gets the note of this ScatterViewProperties.  # noqa: E501


        :return: The note of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ScatterViewProperties.


        :param note: The note of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def show_note_when_empty(self):
        """Gets the show_note_when_empty of this ScatterViewProperties.  # noqa: E501

        If true, will display note when empty  # noqa: E501

        :return: The show_note_when_empty of this ScatterViewProperties.  # noqa: E501
        :rtype: bool
        """
        return self._show_note_when_empty

    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty):
        """Sets the show_note_when_empty of this ScatterViewProperties.

        If true, will display note when empty  # noqa: E501

        :param show_note_when_empty: The show_note_when_empty of this ScatterViewProperties.  # noqa: E501
        :type: bool
        """
        if show_note_when_empty is None:
            raise ValueError("Invalid value for `show_note_when_empty`, must not be `None`")  # noqa: E501

        self._show_note_when_empty = show_note_when_empty

    @property
    def x_column(self):
        """Gets the x_column of this ScatterViewProperties.  # noqa: E501


        :return: The x_column of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._x_column

    @x_column.setter
    def x_column(self, x_column):
        """Sets the x_column of this ScatterViewProperties.


        :param x_column: The x_column of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if x_column is None:
            raise ValueError("Invalid value for `x_column`, must not be `None`")  # noqa: E501

        self._x_column = x_column

    @property
    def y_column(self):
        """Gets the y_column of this ScatterViewProperties.  # noqa: E501


        :return: The y_column of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._y_column

    @y_column.setter
    def y_column(self, y_column):
        """Sets the y_column of this ScatterViewProperties.


        :param y_column: The y_column of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if y_column is None:
            raise ValueError("Invalid value for `y_column`, must not be `None`")  # noqa: E501

        self._y_column = y_column

    @property
    def fill_columns(self):
        """Gets the fill_columns of this ScatterViewProperties.  # noqa: E501


        :return: The fill_columns of this ScatterViewProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._fill_columns

    @fill_columns.setter
    def fill_columns(self, fill_columns):
        """Sets the fill_columns of this ScatterViewProperties.


        :param fill_columns: The fill_columns of this ScatterViewProperties.  # noqa: E501
        :type: list[str]
        """
        if fill_columns is None:
            raise ValueError("Invalid value for `fill_columns`, must not be `None`")  # noqa: E501

        self._fill_columns = fill_columns

    @property
    def symbol_columns(self):
        """Gets the symbol_columns of this ScatterViewProperties.  # noqa: E501


        :return: The symbol_columns of this ScatterViewProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._symbol_columns

    @symbol_columns.setter
    def symbol_columns(self, symbol_columns):
        """Sets the symbol_columns of this ScatterViewProperties.


        :param symbol_columns: The symbol_columns of this ScatterViewProperties.  # noqa: E501
        :type: list[str]
        """
        if symbol_columns is None:
            raise ValueError("Invalid value for `symbol_columns`, must not be `None`")  # noqa: E501

        self._symbol_columns = symbol_columns

    @property
    def x_domain(self):
        """Gets the x_domain of this ScatterViewProperties.  # noqa: E501


        :return: The x_domain of this ScatterViewProperties.  # noqa: E501
        :rtype: list[float]
        """
        return self._x_domain

    @x_domain.setter
    def x_domain(self, x_domain):
        """Sets the x_domain of this ScatterViewProperties.


        :param x_domain: The x_domain of this ScatterViewProperties.  # noqa: E501
        :type: list[float]
        """
        if x_domain is None:
            raise ValueError("Invalid value for `x_domain`, must not be `None`")  # noqa: E501

        self._x_domain = x_domain

    @property
    def y_domain(self):
        """Gets the y_domain of this ScatterViewProperties.  # noqa: E501


        :return: The y_domain of this ScatterViewProperties.  # noqa: E501
        :rtype: list[float]
        """
        return self._y_domain

    @y_domain.setter
    def y_domain(self, y_domain):
        """Sets the y_domain of this ScatterViewProperties.


        :param y_domain: The y_domain of this ScatterViewProperties.  # noqa: E501
        :type: list[float]
        """
        if y_domain is None:
            raise ValueError("Invalid value for `y_domain`, must not be `None`")  # noqa: E501

        self._y_domain = y_domain

    @property
    def x_axis_label(self):
        """Gets the x_axis_label of this ScatterViewProperties.  # noqa: E501


        :return: The x_axis_label of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._x_axis_label

    @x_axis_label.setter
    def x_axis_label(self, x_axis_label):
        """Sets the x_axis_label of this ScatterViewProperties.


        :param x_axis_label: The x_axis_label of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if x_axis_label is None:
            raise ValueError("Invalid value for `x_axis_label`, must not be `None`")  # noqa: E501

        self._x_axis_label = x_axis_label

    @property
    def y_axis_label(self):
        """Gets the y_axis_label of this ScatterViewProperties.  # noqa: E501


        :return: The y_axis_label of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._y_axis_label

    @y_axis_label.setter
    def y_axis_label(self, y_axis_label):
        """Sets the y_axis_label of this ScatterViewProperties.


        :param y_axis_label: The y_axis_label of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if y_axis_label is None:
            raise ValueError("Invalid value for `y_axis_label`, must not be `None`")  # noqa: E501

        self._y_axis_label = y_axis_label

    @property
    def x_prefix(self):
        """Gets the x_prefix of this ScatterViewProperties.  # noqa: E501


        :return: The x_prefix of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._x_prefix

    @x_prefix.setter
    def x_prefix(self, x_prefix):
        """Sets the x_prefix of this ScatterViewProperties.


        :param x_prefix: The x_prefix of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if x_prefix is None:
            raise ValueError("Invalid value for `x_prefix`, must not be `None`")  # noqa: E501

        self._x_prefix = x_prefix

    @property
    def x_suffix(self):
        """Gets the x_suffix of this ScatterViewProperties.  # noqa: E501


        :return: The x_suffix of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._x_suffix

    @x_suffix.setter
    def x_suffix(self, x_suffix):
        """Sets the x_suffix of this ScatterViewProperties.


        :param x_suffix: The x_suffix of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if x_suffix is None:
            raise ValueError("Invalid value for `x_suffix`, must not be `None`")  # noqa: E501

        self._x_suffix = x_suffix

    @property
    def y_prefix(self):
        """Gets the y_prefix of this ScatterViewProperties.  # noqa: E501


        :return: The y_prefix of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._y_prefix

    @y_prefix.setter
    def y_prefix(self, y_prefix):
        """Sets the y_prefix of this ScatterViewProperties.


        :param y_prefix: The y_prefix of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if y_prefix is None:
            raise ValueError("Invalid value for `y_prefix`, must not be `None`")  # noqa: E501

        self._y_prefix = y_prefix

    @property
    def y_suffix(self):
        """Gets the y_suffix of this ScatterViewProperties.  # noqa: E501


        :return: The y_suffix of this ScatterViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._y_suffix

    @y_suffix.setter
    def y_suffix(self, y_suffix):
        """Sets the y_suffix of this ScatterViewProperties.


        :param y_suffix: The y_suffix of this ScatterViewProperties.  # noqa: E501
        :type: str
        """
        if y_suffix is None:
            raise ValueError("Invalid value for `y_suffix`, must not be `None`")  # noqa: E501

        self._y_suffix = y_suffix

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
        if not isinstance(other, ScatterViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
