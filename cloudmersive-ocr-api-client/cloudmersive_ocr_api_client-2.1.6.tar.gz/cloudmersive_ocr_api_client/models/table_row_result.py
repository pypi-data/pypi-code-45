# coding: utf-8

"""
    ocrapi

    The powerful Optical Character Recognition (OCR) APIs let you convert scanned images of pages into recognized text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cloudmersive_ocr_api_client.models.table_cell_result import TableCellResult  # noqa: F401,E501


class TableRowResult(object):
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
        'table_row_cells_result': 'list[TableCellResult]'
    }

    attribute_map = {
        'table_row_cells_result': 'TableRowCellsResult'
    }

    def __init__(self, table_row_cells_result=None):  # noqa: E501
        """TableRowResult - a model defined in Swagger"""  # noqa: E501

        self._table_row_cells_result = None
        self.discriminator = None

        if table_row_cells_result is not None:
            self.table_row_cells_result = table_row_cells_result

    @property
    def table_row_cells_result(self):
        """Gets the table_row_cells_result of this TableRowResult.  # noqa: E501

        Table cells in this row result  # noqa: E501

        :return: The table_row_cells_result of this TableRowResult.  # noqa: E501
        :rtype: list[TableCellResult]
        """
        return self._table_row_cells_result

    @table_row_cells_result.setter
    def table_row_cells_result(self, table_row_cells_result):
        """Sets the table_row_cells_result of this TableRowResult.

        Table cells in this row result  # noqa: E501

        :param table_row_cells_result: The table_row_cells_result of this TableRowResult.  # noqa: E501
        :type: list[TableCellResult]
        """

        self._table_row_cells_result = table_row_cells_result

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
        if issubclass(TableRowResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TableRowResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
