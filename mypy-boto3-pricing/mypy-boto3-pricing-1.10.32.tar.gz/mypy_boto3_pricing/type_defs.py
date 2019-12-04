"Main interface for pricing service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientDescribeServicesResponseServicesTypeDef",
    "ClientDescribeServicesResponseTypeDef",
    "ClientGetAttributeValuesResponseAttributeValuesTypeDef",
    "ClientGetAttributeValuesResponseTypeDef",
    "ClientGetProductsFiltersTypeDef",
    "ClientGetProductsResponseTypeDef",
    "DescribeServicesPaginatePaginationConfigTypeDef",
    "DescribeServicesPaginateResponseServicesTypeDef",
    "DescribeServicesPaginateResponseTypeDef",
    "GetAttributeValuesPaginatePaginationConfigTypeDef",
    "GetAttributeValuesPaginateResponseAttributeValuesTypeDef",
    "GetAttributeValuesPaginateResponseTypeDef",
    "GetProductsPaginateFiltersTypeDef",
    "GetProductsPaginatePaginationConfigTypeDef",
    "GetProductsPaginateResponseTypeDef",
)


_ClientDescribeServicesResponseServicesTypeDef = TypedDict(
    "_ClientDescribeServicesResponseServicesTypeDef",
    {"ServiceCode": str, "AttributeNames": List[str]},
    total=False,
)


class ClientDescribeServicesResponseServicesTypeDef(_ClientDescribeServicesResponseServicesTypeDef):
    """
    - *(dict) --*

      The metadata for a service, such as the service code and available attribute names.
      - **ServiceCode** *(string) --*

        The code for the AWS service.
    """


_ClientDescribeServicesResponseTypeDef = TypedDict(
    "_ClientDescribeServicesResponseTypeDef",
    {
        "Services": List[ClientDescribeServicesResponseServicesTypeDef],
        "FormatVersion": str,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeServicesResponseTypeDef(_ClientDescribeServicesResponseTypeDef):
    """
    - *(dict) --*

      - **Services** *(list) --*

        The service metadata for the service or services in the response.
        - *(dict) --*

          The metadata for a service, such as the service code and available attribute names.
          - **ServiceCode** *(string) --*

            The code for the AWS service.
    """


_ClientGetAttributeValuesResponseAttributeValuesTypeDef = TypedDict(
    "_ClientGetAttributeValuesResponseAttributeValuesTypeDef", {"Value": str}, total=False
)


class ClientGetAttributeValuesResponseAttributeValuesTypeDef(
    _ClientGetAttributeValuesResponseAttributeValuesTypeDef
):
    """
    - *(dict) --*

      The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned IOPS``
      for the ``Amazon EC2``  ``volumeType`` attribute.
      - **Value** *(string) --*

        The specific value of an ``attributeName`` .
    """


_ClientGetAttributeValuesResponseTypeDef = TypedDict(
    "_ClientGetAttributeValuesResponseTypeDef",
    {
        "AttributeValues": List[ClientGetAttributeValuesResponseAttributeValuesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetAttributeValuesResponseTypeDef(_ClientGetAttributeValuesResponseTypeDef):
    """
    - *(dict) --*

      - **AttributeValues** *(list) --*

        The list of values for an attribute. For example, ``Throughput Optimized HDD`` and
        ``Provisioned IOPS`` are two available values for the ``AmazonEC2``  ``volumeType`` .
        - *(dict) --*

          The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned
          IOPS`` for the ``Amazon EC2``  ``volumeType`` attribute.
          - **Value** *(string) --*

            The specific value of an ``attributeName`` .
    """


_RequiredClientGetProductsFiltersTypeDef = TypedDict(
    "_RequiredClientGetProductsFiltersTypeDef", {"Type": str}
)
_OptionalClientGetProductsFiltersTypeDef = TypedDict(
    "_OptionalClientGetProductsFiltersTypeDef", {"Field": str, "Value": str}, total=False
)


class ClientGetProductsFiltersTypeDef(
    _RequiredClientGetProductsFiltersTypeDef, _OptionalClientGetProductsFiltersTypeDef
):
    """
    - *(dict) --*

      The constraints that you want all returned products to match.
      - **Type** *(string) --***[REQUIRED]**

        The type of filter that you want to use.
        Valid values are: ``TERM_MATCH`` . ``TERM_MATCH`` returns only products that match both the
        given filter field and the given value.
    """


_ClientGetProductsResponseTypeDef = TypedDict(
    "_ClientGetProductsResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str], "NextToken": str},
    total=False,
)


class ClientGetProductsResponseTypeDef(_ClientGetProductsResponseTypeDef):
    """
    - *(dict) --*

      - **FormatVersion** *(string) --*

        The format version of the response. For example, aws_v1.
    """


_DescribeServicesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeServicesPaginatePaginationConfigTypeDef(
    _DescribeServicesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeServicesPaginateResponseServicesTypeDef = TypedDict(
    "_DescribeServicesPaginateResponseServicesTypeDef",
    {"ServiceCode": str, "AttributeNames": List[str]},
    total=False,
)


class DescribeServicesPaginateResponseServicesTypeDef(
    _DescribeServicesPaginateResponseServicesTypeDef
):
    """
    - *(dict) --*

      The metadata for a service, such as the service code and available attribute names.
      - **ServiceCode** *(string) --*

        The code for the AWS service.
    """


_DescribeServicesPaginateResponseTypeDef = TypedDict(
    "_DescribeServicesPaginateResponseTypeDef",
    {"Services": List[DescribeServicesPaginateResponseServicesTypeDef], "FormatVersion": str},
    total=False,
)


class DescribeServicesPaginateResponseTypeDef(_DescribeServicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Services** *(list) --*

        The service metadata for the service or services in the response.
        - *(dict) --*

          The metadata for a service, such as the service code and available attribute names.
          - **ServiceCode** *(string) --*

            The code for the AWS service.
    """


_GetAttributeValuesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetAttributeValuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetAttributeValuesPaginatePaginationConfigTypeDef(
    _GetAttributeValuesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetAttributeValuesPaginateResponseAttributeValuesTypeDef = TypedDict(
    "_GetAttributeValuesPaginateResponseAttributeValuesTypeDef", {"Value": str}, total=False
)


class GetAttributeValuesPaginateResponseAttributeValuesTypeDef(
    _GetAttributeValuesPaginateResponseAttributeValuesTypeDef
):
    """
    - *(dict) --*

      The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned IOPS``
      for the ``Amazon EC2``  ``volumeType`` attribute.
      - **Value** *(string) --*

        The specific value of an ``attributeName`` .
    """


_GetAttributeValuesPaginateResponseTypeDef = TypedDict(
    "_GetAttributeValuesPaginateResponseTypeDef",
    {"AttributeValues": List[GetAttributeValuesPaginateResponseAttributeValuesTypeDef]},
    total=False,
)


class GetAttributeValuesPaginateResponseTypeDef(_GetAttributeValuesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **AttributeValues** *(list) --*

        The list of values for an attribute. For example, ``Throughput Optimized HDD`` and
        ``Provisioned IOPS`` are two available values for the ``AmazonEC2``  ``volumeType`` .
        - *(dict) --*

          The values of a given attribute, such as ``Throughput Optimized HDD`` or ``Provisioned
          IOPS`` for the ``Amazon EC2``  ``volumeType`` attribute.
          - **Value** *(string) --*

            The specific value of an ``attributeName`` .
    """


_RequiredGetProductsPaginateFiltersTypeDef = TypedDict(
    "_RequiredGetProductsPaginateFiltersTypeDef", {"Type": str}
)
_OptionalGetProductsPaginateFiltersTypeDef = TypedDict(
    "_OptionalGetProductsPaginateFiltersTypeDef", {"Field": str, "Value": str}, total=False
)


class GetProductsPaginateFiltersTypeDef(
    _RequiredGetProductsPaginateFiltersTypeDef, _OptionalGetProductsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      The constraints that you want all returned products to match.
      - **Type** *(string) --***[REQUIRED]**

        The type of filter that you want to use.
        Valid values are: ``TERM_MATCH`` . ``TERM_MATCH`` returns only products that match both the
        given filter field and the given value.
    """


_GetProductsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetProductsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetProductsPaginatePaginationConfigTypeDef(_GetProductsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetProductsPaginateResponseTypeDef = TypedDict(
    "_GetProductsPaginateResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str]},
    total=False,
)


class GetProductsPaginateResponseTypeDef(_GetProductsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **FormatVersion** *(string) --*

        The format version of the response. For example, aws_v1.
    """
