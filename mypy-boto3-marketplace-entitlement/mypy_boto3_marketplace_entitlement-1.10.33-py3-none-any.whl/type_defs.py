"Main interface for marketplace-entitlement service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientGetEntitlementsResponseEntitlementsValueTypeDef = TypedDict(
    "ClientGetEntitlementsResponseEntitlementsValueTypeDef",
    {"IntegerValue": int, "DoubleValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)

ClientGetEntitlementsResponseEntitlementsTypeDef = TypedDict(
    "ClientGetEntitlementsResponseEntitlementsTypeDef",
    {
        "ProductCode": str,
        "Dimension": str,
        "CustomerIdentifier": str,
        "Value": ClientGetEntitlementsResponseEntitlementsValueTypeDef,
        "ExpirationDate": datetime,
    },
    total=False,
)

ClientGetEntitlementsResponseTypeDef = TypedDict(
    "ClientGetEntitlementsResponseTypeDef",
    {"Entitlements": List[ClientGetEntitlementsResponseEntitlementsTypeDef], "NextToken": str},
    total=False,
)

GetEntitlementsPaginatePaginationConfigTypeDef = TypedDict(
    "GetEntitlementsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetEntitlementsPaginateResponseEntitlementsValueTypeDef = TypedDict(
    "GetEntitlementsPaginateResponseEntitlementsValueTypeDef",
    {"IntegerValue": int, "DoubleValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)

GetEntitlementsPaginateResponseEntitlementsTypeDef = TypedDict(
    "GetEntitlementsPaginateResponseEntitlementsTypeDef",
    {
        "ProductCode": str,
        "Dimension": str,
        "CustomerIdentifier": str,
        "Value": GetEntitlementsPaginateResponseEntitlementsValueTypeDef,
        "ExpirationDate": datetime,
    },
    total=False,
)

GetEntitlementsPaginateResponseTypeDef = TypedDict(
    "GetEntitlementsPaginateResponseTypeDef",
    {"Entitlements": List[GetEntitlementsPaginateResponseEntitlementsTypeDef]},
    total=False,
)
