"Main interface for iot1click-devices service type defs"
from __future__ import annotations

from typing import Any, Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientClaimDevicesByClaimCodeResponseTypeDef",
    "ClientDescribeDeviceResponseDeviceDescriptionTypeDef",
    "ClientDescribeDeviceResponseTypeDef",
    "ClientFinalizeDeviceClaimResponseTypeDef",
    "ClientGetDeviceMethodsResponseDeviceMethodsTypeDef",
    "ClientGetDeviceMethodsResponseTypeDef",
    "ClientInitiateDeviceClaimResponseTypeDef",
    "ClientInvokeDeviceMethodDeviceMethodTypeDef",
    "ClientInvokeDeviceMethodResponseTypeDef",
    "ClientListDeviceEventsResponseEventsDeviceTypeDef",
    "ClientListDeviceEventsResponseEventsTypeDef",
    "ClientListDeviceEventsResponseTypeDef",
    "ClientListDevicesResponseDevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUnclaimDeviceResponseTypeDef",
    "ListDeviceEventsPaginatePaginationConfigTypeDef",
    "ListDeviceEventsPaginateResponseEventsDeviceTypeDef",
    "ListDeviceEventsPaginateResponseEventsTypeDef",
    "ListDeviceEventsPaginateResponseTypeDef",
    "ListDevicesPaginatePaginationConfigTypeDef",
    "ListDevicesPaginateResponseDevicesTypeDef",
    "ListDevicesPaginateResponseTypeDef",
)


_ClientClaimDevicesByClaimCodeResponseTypeDef = TypedDict(
    "_ClientClaimDevicesByClaimCodeResponseTypeDef", {"ClaimCode": str, "Total": int}, total=False
)


class ClientClaimDevicesByClaimCodeResponseTypeDef(_ClientClaimDevicesByClaimCodeResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **ClaimCode** *(string) --*

        The claim code provided by the device manufacturer.
    """


_ClientDescribeDeviceResponseDeviceDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeviceResponseDeviceDescriptionTypeDef",
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


class ClientDescribeDeviceResponseDeviceDescriptionTypeDef(
    _ClientDescribeDeviceResponseDeviceDescriptionTypeDef
):
    """
    - **DeviceDescription** *(dict) --*

      Device details.
      - **Arn** *(string) --*

        The ARN of the device.
    """


_ClientDescribeDeviceResponseTypeDef = TypedDict(
    "_ClientDescribeDeviceResponseTypeDef",
    {"DeviceDescription": ClientDescribeDeviceResponseDeviceDescriptionTypeDef},
    total=False,
)


class ClientDescribeDeviceResponseTypeDef(_ClientDescribeDeviceResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **DeviceDescription** *(dict) --*

        Device details.
        - **Arn** *(string) --*

          The ARN of the device.
    """


_ClientFinalizeDeviceClaimResponseTypeDef = TypedDict(
    "_ClientFinalizeDeviceClaimResponseTypeDef", {"State": str}, total=False
)


class ClientFinalizeDeviceClaimResponseTypeDef(_ClientFinalizeDeviceClaimResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **State** *(string) --*

        The device's final claim state.
    """


_ClientGetDeviceMethodsResponseDeviceMethodsTypeDef = TypedDict(
    "_ClientGetDeviceMethodsResponseDeviceMethodsTypeDef",
    {"DeviceType": str, "MethodName": str},
    total=False,
)


class ClientGetDeviceMethodsResponseDeviceMethodsTypeDef(
    _ClientGetDeviceMethodsResponseDeviceMethodsTypeDef
):
    """
    - *(dict) --*

      - **DeviceType** *(string) --*

        The type of the device, such as "button".
    """


_ClientGetDeviceMethodsResponseTypeDef = TypedDict(
    "_ClientGetDeviceMethodsResponseTypeDef",
    {"DeviceMethods": List[ClientGetDeviceMethodsResponseDeviceMethodsTypeDef]},
    total=False,
)


class ClientGetDeviceMethodsResponseTypeDef(_ClientGetDeviceMethodsResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **DeviceMethods** *(list) --*

        List of available device APIs.
        - *(dict) --*

          - **DeviceType** *(string) --*

            The type of the device, such as "button".
    """


_ClientInitiateDeviceClaimResponseTypeDef = TypedDict(
    "_ClientInitiateDeviceClaimResponseTypeDef", {"State": str}, total=False
)


class ClientInitiateDeviceClaimResponseTypeDef(_ClientInitiateDeviceClaimResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **State** *(string) --*

        The device's final claim state.
    """


_ClientInvokeDeviceMethodDeviceMethodTypeDef = TypedDict(
    "_ClientInvokeDeviceMethodDeviceMethodTypeDef",
    {"DeviceType": str, "MethodName": str},
    total=False,
)


class ClientInvokeDeviceMethodDeviceMethodTypeDef(_ClientInvokeDeviceMethodDeviceMethodTypeDef):
    """
    The device method to invoke.
    - **DeviceType** *(string) --*

      The type of the device, such as "button".
    """


_ClientInvokeDeviceMethodResponseTypeDef = TypedDict(
    "_ClientInvokeDeviceMethodResponseTypeDef", {"DeviceMethodResponse": str}, total=False
)


class ClientInvokeDeviceMethodResponseTypeDef(_ClientInvokeDeviceMethodResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **DeviceMethodResponse** *(string) --*

        A JSON encoded string containing the device method response.
    """


_ClientListDeviceEventsResponseEventsDeviceTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseEventsDeviceTypeDef",
    {"Attributes": Dict[str, Any], "DeviceId": str, "Type": str},
    total=False,
)


class ClientListDeviceEventsResponseEventsDeviceTypeDef(
    _ClientListDeviceEventsResponseEventsDeviceTypeDef
):
    """
    - **Device** *(dict) --*

      An object representing the device associated with the event.
      - **Attributes** *(dict) --*

        The user specified attributes associated with the device for an event.
    """


_ClientListDeviceEventsResponseEventsTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseEventsTypeDef",
    {"Device": ClientListDeviceEventsResponseEventsDeviceTypeDef, "StdEvent": str},
    total=False,
)


class ClientListDeviceEventsResponseEventsTypeDef(_ClientListDeviceEventsResponseEventsTypeDef):
    """
    - *(dict) --*

      - **Device** *(dict) --*

        An object representing the device associated with the event.
        - **Attributes** *(dict) --*

          The user specified attributes associated with the device for an event.
    """


_ClientListDeviceEventsResponseTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseTypeDef",
    {"Events": List[ClientListDeviceEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientListDeviceEventsResponseTypeDef(_ClientListDeviceEventsResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **Events** *(list) --*

        An array of zero or more elements describing the event(s) associated with the device.
        - *(dict) --*

          - **Device** *(dict) --*

            An object representing the device associated with the event.
            - **Attributes** *(dict) --*

              The user specified attributes associated with the device for an event.
    """


_ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientListDevicesResponseDevicesTypeDef",
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


class ClientListDevicesResponseDevicesTypeDef(_ClientListDevicesResponseDevicesTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The ARN of the device.
    """


_ClientListDevicesResponseTypeDef = TypedDict(
    "_ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "NextToken": str},
    total=False,
)


class ClientListDevicesResponseTypeDef(_ClientListDevicesResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **Devices** *(list) --*

        A list of devices.
        - *(dict) --*

          - **Arn** *(string) --*

            The ARN of the device.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        A collection of key/value pairs defining the resource tags. For example, { "tags": {"key1":
        "value1", "key2": "value2"} }. For more information, see `AWS Tagging Strategies
        <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`__ .
        - *(string) --*

          - *(string) --*
    """


_ClientUnclaimDeviceResponseTypeDef = TypedDict(
    "_ClientUnclaimDeviceResponseTypeDef", {"State": str}, total=False
)


class ClientUnclaimDeviceResponseTypeDef(_ClientUnclaimDeviceResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **State** *(string) --*

        The device's final claim state.
    """


_ListDeviceEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeviceEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeviceEventsPaginatePaginationConfigTypeDef(
    _ListDeviceEventsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeviceEventsPaginateResponseEventsDeviceTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseEventsDeviceTypeDef",
    {"Attributes": Dict[str, Any], "DeviceId": str, "Type": str},
    total=False,
)


class ListDeviceEventsPaginateResponseEventsDeviceTypeDef(
    _ListDeviceEventsPaginateResponseEventsDeviceTypeDef
):
    """
    - **Device** *(dict) --*

      An object representing the device associated with the event.
      - **Attributes** *(dict) --*

        The user specified attributes associated with the device for an event.
    """


_ListDeviceEventsPaginateResponseEventsTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseEventsTypeDef",
    {"Device": ListDeviceEventsPaginateResponseEventsDeviceTypeDef, "StdEvent": str},
    total=False,
)


class ListDeviceEventsPaginateResponseEventsTypeDef(_ListDeviceEventsPaginateResponseEventsTypeDef):
    """
    - *(dict) --*

      - **Device** *(dict) --*

        An object representing the device associated with the event.
        - **Attributes** *(dict) --*

          The user specified attributes associated with the device for an event.
    """


_ListDeviceEventsPaginateResponseTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseTypeDef",
    {"Events": List[ListDeviceEventsPaginateResponseEventsTypeDef]},
    total=False,
)


class ListDeviceEventsPaginateResponseTypeDef(_ListDeviceEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **Events** *(list) --*

        An array of zero or more elements describing the event(s) associated with the device.
        - *(dict) --*

          - **Device** *(dict) --*

            An object representing the device associated with the event.
            - **Attributes** *(dict) --*

              The user specified attributes associated with the device for an event.
    """


_ListDevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDevicesPaginatePaginationConfigTypeDef(_ListDevicesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDevicesPaginateResponseDevicesTypeDef = TypedDict(
    "_ListDevicesPaginateResponseDevicesTypeDef",
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


class ListDevicesPaginateResponseDevicesTypeDef(_ListDevicesPaginateResponseDevicesTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The ARN of the device.
    """


_ListDevicesPaginateResponseTypeDef = TypedDict(
    "_ListDevicesPaginateResponseTypeDef",
    {"Devices": List[ListDevicesPaginateResponseDevicesTypeDef]},
    total=False,
)


class ListDevicesPaginateResponseTypeDef(_ListDevicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      200 response
      - **Devices** *(list) --*

        A list of devices.
        - *(dict) --*

          - **Arn** *(string) --*

            The ARN of the device.
    """
