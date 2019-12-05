"Main interface for pricing service type defs"
from __future__ import annotations

import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientDescribeServicesResponseServicesTypeDef = TypedDict(
    "ClientDescribeServicesResponseServicesTypeDef",
    {"ServiceCode": str, "AttributeNames": List[str]},
    total=False,
)

ClientDescribeServicesResponseTypeDef = TypedDict(
    "ClientDescribeServicesResponseTypeDef",
    {
        "Services": List[ClientDescribeServicesResponseServicesTypeDef],
        "FormatVersion": str,
        "NextToken": str,
    },
    total=False,
)

ClientGetAttributeValuesResponseAttributeValuesTypeDef = TypedDict(
    "ClientGetAttributeValuesResponseAttributeValuesTypeDef", {"Value": str}, total=False
)

ClientGetAttributeValuesResponseTypeDef = TypedDict(
    "ClientGetAttributeValuesResponseTypeDef",
    {
        "AttributeValues": List[ClientGetAttributeValuesResponseAttributeValuesTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientGetProductsFiltersTypeDef = TypedDict(
    "_RequiredClientGetProductsFiltersTypeDef", {"Type": str}
)
_OptionalClientGetProductsFiltersTypeDef = TypedDict(
    "_OptionalClientGetProductsFiltersTypeDef", {"Field": str, "Value": str}, total=False
)


class ClientGetProductsFiltersTypeDef(
    _RequiredClientGetProductsFiltersTypeDef, _OptionalClientGetProductsFiltersTypeDef
):
    pass


ClientGetProductsResponseTypeDef = TypedDict(
    "ClientGetProductsResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str], "NextToken": str},
    total=False,
)

DescribeServicesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeServicesPaginateResponseServicesTypeDef = TypedDict(
    "DescribeServicesPaginateResponseServicesTypeDef",
    {"ServiceCode": str, "AttributeNames": List[str]},
    total=False,
)

DescribeServicesPaginateResponseTypeDef = TypedDict(
    "DescribeServicesPaginateResponseTypeDef",
    {"Services": List[DescribeServicesPaginateResponseServicesTypeDef], "FormatVersion": str},
    total=False,
)

GetAttributeValuesPaginatePaginationConfigTypeDef = TypedDict(
    "GetAttributeValuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetAttributeValuesPaginateResponseAttributeValuesTypeDef = TypedDict(
    "GetAttributeValuesPaginateResponseAttributeValuesTypeDef", {"Value": str}, total=False
)

GetAttributeValuesPaginateResponseTypeDef = TypedDict(
    "GetAttributeValuesPaginateResponseTypeDef",
    {"AttributeValues": List[GetAttributeValuesPaginateResponseAttributeValuesTypeDef]},
    total=False,
)

_RequiredGetProductsPaginateFiltersTypeDef = TypedDict(
    "_RequiredGetProductsPaginateFiltersTypeDef", {"Type": str}
)
_OptionalGetProductsPaginateFiltersTypeDef = TypedDict(
    "_OptionalGetProductsPaginateFiltersTypeDef", {"Field": str, "Value": str}, total=False
)


class GetProductsPaginateFiltersTypeDef(
    _RequiredGetProductsPaginateFiltersTypeDef, _OptionalGetProductsPaginateFiltersTypeDef
):
    pass


GetProductsPaginatePaginationConfigTypeDef = TypedDict(
    "GetProductsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetProductsPaginateResponseTypeDef = TypedDict(
    "GetProductsPaginateResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str]},
    total=False,
)
