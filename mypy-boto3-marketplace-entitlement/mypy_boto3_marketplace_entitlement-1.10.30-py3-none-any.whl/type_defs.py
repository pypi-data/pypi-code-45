"Main interface for marketplace-entitlement service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientGetEntitlementsResponseEntitlementsValueTypeDef",
    "ClientGetEntitlementsResponseEntitlementsTypeDef",
    "ClientGetEntitlementsResponseTypeDef",
    "GetEntitlementsPaginatePaginationConfigTypeDef",
    "GetEntitlementsPaginateResponseEntitlementsValueTypeDef",
    "GetEntitlementsPaginateResponseEntitlementsTypeDef",
    "GetEntitlementsPaginateResponseTypeDef",
)


_ClientGetEntitlementsResponseEntitlementsValueTypeDef = TypedDict(
    "_ClientGetEntitlementsResponseEntitlementsValueTypeDef",
    {"IntegerValue": int, "DoubleValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)


class ClientGetEntitlementsResponseEntitlementsValueTypeDef(
    _ClientGetEntitlementsResponseEntitlementsValueTypeDef
):
    pass


_ClientGetEntitlementsResponseEntitlementsTypeDef = TypedDict(
    "_ClientGetEntitlementsResponseEntitlementsTypeDef",
    {
        "ProductCode": str,
        "Dimension": str,
        "CustomerIdentifier": str,
        "Value": ClientGetEntitlementsResponseEntitlementsValueTypeDef,
        "ExpirationDate": datetime,
    },
    total=False,
)


class ClientGetEntitlementsResponseEntitlementsTypeDef(
    _ClientGetEntitlementsResponseEntitlementsTypeDef
):
    """
    - *(dict) --*

      An entitlement represents capacity in a product owned by the customer. For example, a customer
      might own some number of users or seats in an SaaS application or some amount of data capacity
      in a multi-tenant database.
      - **ProductCode** *(string) --*

        The product code for which the given entitlement applies. Product codes are provided by AWS
        Marketplace when the product listing is created.
    """


_ClientGetEntitlementsResponseTypeDef = TypedDict(
    "_ClientGetEntitlementsResponseTypeDef",
    {"Entitlements": List[ClientGetEntitlementsResponseEntitlementsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetEntitlementsResponseTypeDef(_ClientGetEntitlementsResponseTypeDef):
    """
    - *(dict) --*

      The GetEntitlementsRequest contains results from the GetEntitlements operation.
      - **Entitlements** *(list) --*

        The set of entitlements found through the GetEntitlements operation. If the result contains
        an empty set of entitlements, NextToken might still be present and should be used.
        - *(dict) --*

          An entitlement represents capacity in a product owned by the customer. For example, a
          customer might own some number of users or seats in an SaaS application or some amount of
          data capacity in a multi-tenant database.
          - **ProductCode** *(string) --*

            The product code for which the given entitlement applies. Product codes are provided by
            AWS Marketplace when the product listing is created.
    """


_GetEntitlementsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetEntitlementsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetEntitlementsPaginatePaginationConfigTypeDef(
    _GetEntitlementsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetEntitlementsPaginateResponseEntitlementsValueTypeDef = TypedDict(
    "_GetEntitlementsPaginateResponseEntitlementsValueTypeDef",
    {"IntegerValue": int, "DoubleValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)


class GetEntitlementsPaginateResponseEntitlementsValueTypeDef(
    _GetEntitlementsPaginateResponseEntitlementsValueTypeDef
):
    pass


_GetEntitlementsPaginateResponseEntitlementsTypeDef = TypedDict(
    "_GetEntitlementsPaginateResponseEntitlementsTypeDef",
    {
        "ProductCode": str,
        "Dimension": str,
        "CustomerIdentifier": str,
        "Value": GetEntitlementsPaginateResponseEntitlementsValueTypeDef,
        "ExpirationDate": datetime,
    },
    total=False,
)


class GetEntitlementsPaginateResponseEntitlementsTypeDef(
    _GetEntitlementsPaginateResponseEntitlementsTypeDef
):
    """
    - *(dict) --*

      An entitlement represents capacity in a product owned by the customer. For example, a customer
      might own some number of users or seats in an SaaS application or some amount of data capacity
      in a multi-tenant database.
      - **ProductCode** *(string) --*

        The product code for which the given entitlement applies. Product codes are provided by AWS
        Marketplace when the product listing is created.
    """


_GetEntitlementsPaginateResponseTypeDef = TypedDict(
    "_GetEntitlementsPaginateResponseTypeDef",
    {"Entitlements": List[GetEntitlementsPaginateResponseEntitlementsTypeDef]},
    total=False,
)


class GetEntitlementsPaginateResponseTypeDef(_GetEntitlementsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The GetEntitlementsRequest contains results from the GetEntitlements operation.
      - **Entitlements** *(list) --*

        The set of entitlements found through the GetEntitlements operation. If the result contains
        an empty set of entitlements, NextToken might still be present and should be used.
        - *(dict) --*

          An entitlement represents capacity in a product owned by the customer. For example, a
          customer might own some number of users or seats in an SaaS application or some amount of
          data capacity in a multi-tenant database.
          - **ProductCode** *(string) --*

            The product code for which the given entitlement applies. Product codes are provided by
            AWS Marketplace when the product listing is created.
    """
