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


class LinePlusSingleStatProperties(object):
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
        'colors': 'list[DashboardColor]',
        'shape': 'str',
        'note': 'str',
        'show_note_when_empty': 'bool',
        'axes': 'Axes',
        'legend': 'Legend',
        'x_column': 'str',
        'y_column': 'str',
        'shade_below': 'bool',
        'prefix': 'str',
        'suffix': 'str',
        'decimal_places': 'DecimalPlaces'
    }

    attribute_map = {
        'type': 'type',
        'queries': 'queries',
        'colors': 'colors',
        'shape': 'shape',
        'note': 'note',
        'show_note_when_empty': 'showNoteWhenEmpty',
        'axes': 'axes',
        'legend': 'legend',
        'x_column': 'xColumn',
        'y_column': 'yColumn',
        'shade_below': 'shadeBelow',
        'prefix': 'prefix',
        'suffix': 'suffix',
        'decimal_places': 'decimalPlaces'
    }

    def __init__(self, type=None, queries=None, colors=None, shape=None, note=None, show_note_when_empty=None, axes=None, legend=None, x_column=None, y_column=None, shade_below=None, prefix=None, suffix=None, decimal_places=None):  # noqa: E501
        """LinePlusSingleStatProperties - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._queries = None
        self._colors = None
        self._shape = None
        self._note = None
        self._show_note_when_empty = None
        self._axes = None
        self._legend = None
        self._x_column = None
        self._y_column = None
        self._shade_below = None
        self._prefix = None
        self._suffix = None
        self._decimal_places = None
        self.discriminator = None

        self.type = type
        self.queries = queries
        self.colors = colors
        self.shape = shape
        self.note = note
        self.show_note_when_empty = show_note_when_empty
        self.axes = axes
        self.legend = legend
        if x_column is not None:
            self.x_column = x_column
        if y_column is not None:
            self.y_column = y_column
        if shade_below is not None:
            self.shade_below = shade_below
        self.prefix = prefix
        self.suffix = suffix
        self.decimal_places = decimal_places

    @property
    def type(self):
        """Gets the type of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The type of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LinePlusSingleStatProperties.


        :param type: The type of this LinePlusSingleStatProperties.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def queries(self):
        """Gets the queries of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The queries of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: list[DashboardQuery]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this LinePlusSingleStatProperties.


        :param queries: The queries of this LinePlusSingleStatProperties.  # noqa: E501
        :type: list[DashboardQuery]
        """
        if queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501

        self._queries = queries

    @property
    def colors(self):
        """Gets the colors of this LinePlusSingleStatProperties.  # noqa: E501

        Colors define color encoding of data into a visualization  # noqa: E501

        :return: The colors of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: list[DashboardColor]
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this LinePlusSingleStatProperties.

        Colors define color encoding of data into a visualization  # noqa: E501

        :param colors: The colors of this LinePlusSingleStatProperties.  # noqa: E501
        :type: list[DashboardColor]
        """
        if colors is None:
            raise ValueError("Invalid value for `colors`, must not be `None`")  # noqa: E501

        self._colors = colors

    @property
    def shape(self):
        """Gets the shape of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The shape of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this LinePlusSingleStatProperties.


        :param shape: The shape of this LinePlusSingleStatProperties.  # noqa: E501
        :type: str
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def note(self):
        """Gets the note of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The note of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this LinePlusSingleStatProperties.


        :param note: The note of this LinePlusSingleStatProperties.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def show_note_when_empty(self):
        """Gets the show_note_when_empty of this LinePlusSingleStatProperties.  # noqa: E501

        If true, will display note when empty  # noqa: E501

        :return: The show_note_when_empty of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: bool
        """
        return self._show_note_when_empty

    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty):
        """Sets the show_note_when_empty of this LinePlusSingleStatProperties.

        If true, will display note when empty  # noqa: E501

        :param show_note_when_empty: The show_note_when_empty of this LinePlusSingleStatProperties.  # noqa: E501
        :type: bool
        """
        if show_note_when_empty is None:
            raise ValueError("Invalid value for `show_note_when_empty`, must not be `None`")  # noqa: E501

        self._show_note_when_empty = show_note_when_empty

    @property
    def axes(self):
        """Gets the axes of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The axes of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: Axes
        """
        return self._axes

    @axes.setter
    def axes(self, axes):
        """Sets the axes of this LinePlusSingleStatProperties.


        :param axes: The axes of this LinePlusSingleStatProperties.  # noqa: E501
        :type: Axes
        """
        if axes is None:
            raise ValueError("Invalid value for `axes`, must not be `None`")  # noqa: E501

        self._axes = axes

    @property
    def legend(self):
        """Gets the legend of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The legend of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: Legend
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Sets the legend of this LinePlusSingleStatProperties.


        :param legend: The legend of this LinePlusSingleStatProperties.  # noqa: E501
        :type: Legend
        """
        if legend is None:
            raise ValueError("Invalid value for `legend`, must not be `None`")  # noqa: E501

        self._legend = legend

    @property
    def x_column(self):
        """Gets the x_column of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The x_column of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: str
        """
        return self._x_column

    @x_column.setter
    def x_column(self, x_column):
        """Sets the x_column of this LinePlusSingleStatProperties.


        :param x_column: The x_column of this LinePlusSingleStatProperties.  # noqa: E501
        :type: str
        """

        self._x_column = x_column

    @property
    def y_column(self):
        """Gets the y_column of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The y_column of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: str
        """
        return self._y_column

    @y_column.setter
    def y_column(self, y_column):
        """Sets the y_column of this LinePlusSingleStatProperties.


        :param y_column: The y_column of this LinePlusSingleStatProperties.  # noqa: E501
        :type: str
        """

        self._y_column = y_column

    @property
    def shade_below(self):
        """Gets the shade_below of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The shade_below of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: bool
        """
        return self._shade_below

    @shade_below.setter
    def shade_below(self, shade_below):
        """Sets the shade_below of this LinePlusSingleStatProperties.


        :param shade_below: The shade_below of this LinePlusSingleStatProperties.  # noqa: E501
        :type: bool
        """

        self._shade_below = shade_below

    @property
    def prefix(self):
        """Gets the prefix of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The prefix of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this LinePlusSingleStatProperties.


        :param prefix: The prefix of this LinePlusSingleStatProperties.  # noqa: E501
        :type: str
        """
        if prefix is None:
            raise ValueError("Invalid value for `prefix`, must not be `None`")  # noqa: E501

        self._prefix = prefix

    @property
    def suffix(self):
        """Gets the suffix of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The suffix of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this LinePlusSingleStatProperties.


        :param suffix: The suffix of this LinePlusSingleStatProperties.  # noqa: E501
        :type: str
        """
        if suffix is None:
            raise ValueError("Invalid value for `suffix`, must not be `None`")  # noqa: E501

        self._suffix = suffix

    @property
    def decimal_places(self):
        """Gets the decimal_places of this LinePlusSingleStatProperties.  # noqa: E501


        :return: The decimal_places of this LinePlusSingleStatProperties.  # noqa: E501
        :rtype: DecimalPlaces
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this LinePlusSingleStatProperties.


        :param decimal_places: The decimal_places of this LinePlusSingleStatProperties.  # noqa: E501
        :type: DecimalPlaces
        """
        if decimal_places is None:
            raise ValueError("Invalid value for `decimal_places`, must not be `None`")  # noqa: E501

        self._decimal_places = decimal_places

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
        if not isinstance(other, LinePlusSingleStatProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
