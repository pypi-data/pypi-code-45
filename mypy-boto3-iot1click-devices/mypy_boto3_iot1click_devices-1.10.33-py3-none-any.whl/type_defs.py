"Main interface for iot1click-devices service type defs"
from __future__ import annotations

import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientClaimDevicesByClaimCodeResponseTypeDef = TypedDict(
    "ClientClaimDevicesByClaimCodeResponseTypeDef", {"ClaimCode": str, "Total": int}, total=False
)

ClientDescribeDeviceResponseDeviceDescriptionTypeDef = TypedDict(
    "ClientDescribeDeviceResponseDeviceDescriptionTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeDeviceResponseTypeDef = TypedDict(
    "ClientDescribeDeviceResponseTypeDef",
    {"DeviceDescription": ClientDescribeDeviceResponseDeviceDescriptionTypeDef},
    total=False,
)

ClientFinalizeDeviceClaimResponseTypeDef = TypedDict(
    "ClientFinalizeDeviceClaimResponseTypeDef", {"State": str}, total=False
)

ClientGetDeviceMethodsResponseDeviceMethodsTypeDef = TypedDict(
    "ClientGetDeviceMethodsResponseDeviceMethodsTypeDef",
    {"DeviceType": str, "MethodName": str},
    total=False,
)

ClientGetDeviceMethodsResponseTypeDef = TypedDict(
    "ClientGetDeviceMethodsResponseTypeDef",
    {"DeviceMethods": List[ClientGetDeviceMethodsResponseDeviceMethodsTypeDef]},
    total=False,
)

ClientInitiateDeviceClaimResponseTypeDef = TypedDict(
    "ClientInitiateDeviceClaimResponseTypeDef", {"State": str}, total=False
)

ClientInvokeDeviceMethodDeviceMethodTypeDef = TypedDict(
    "ClientInvokeDeviceMethodDeviceMethodTypeDef",
    {"DeviceType": str, "MethodName": str},
    total=False,
)

ClientInvokeDeviceMethodResponseTypeDef = TypedDict(
    "ClientInvokeDeviceMethodResponseTypeDef", {"DeviceMethodResponse": str}, total=False
)

ClientListDeviceEventsResponseEventsDeviceTypeDef = TypedDict(
    "ClientListDeviceEventsResponseEventsDeviceTypeDef",
    {"Attributes": Dict[str, Any], "DeviceId": str, "Type": str},
    total=False,
)

ClientListDeviceEventsResponseEventsTypeDef = TypedDict(
    "ClientListDeviceEventsResponseEventsTypeDef",
    {"Device": ClientListDeviceEventsResponseEventsDeviceTypeDef, "StdEvent": str},
    total=False,
)

ClientListDeviceEventsResponseTypeDef = TypedDict(
    "ClientListDeviceEventsResponseTypeDef",
    {"Events": List[ClientListDeviceEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)

ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "ClientListDevicesResponseDevicesTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListDevicesResponseTypeDef = TypedDict(
    "ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUnclaimDeviceResponseTypeDef = TypedDict(
    "ClientUnclaimDeviceResponseTypeDef", {"State": str}, total=False
)

ListDeviceEventsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDeviceEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDeviceEventsPaginateResponseEventsDeviceTypeDef = TypedDict(
    "ListDeviceEventsPaginateResponseEventsDeviceTypeDef",
    {"Attributes": Dict[str, Any], "DeviceId": str, "Type": str},
    total=False,
)

ListDeviceEventsPaginateResponseEventsTypeDef = TypedDict(
    "ListDeviceEventsPaginateResponseEventsTypeDef",
    {"Device": ListDeviceEventsPaginateResponseEventsDeviceTypeDef, "StdEvent": str},
    total=False,
)

ListDeviceEventsPaginateResponseTypeDef = TypedDict(
    "ListDeviceEventsPaginateResponseTypeDef",
    {"Events": List[ListDeviceEventsPaginateResponseEventsTypeDef]},
    total=False,
)

ListDevicesPaginatePaginationConfigTypeDef = TypedDict(
    "ListDevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDevicesPaginateResponseDevicesTypeDef = TypedDict(
    "ListDevicesPaginateResponseDevicesTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListDevicesPaginateResponseTypeDef = TypedDict(
    "ListDevicesPaginateResponseTypeDef",
    {"Devices": List[ListDevicesPaginateResponseDevicesTypeDef]},
    total=False,
)
