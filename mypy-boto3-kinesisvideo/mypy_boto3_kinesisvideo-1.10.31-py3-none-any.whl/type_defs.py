"Main interface for kinesisvideo service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateStreamResponseTypeDef",
    "ClientDescribeStreamResponseStreamInfoTypeDef",
    "ClientDescribeStreamResponseTypeDef",
    "ClientGetDataEndpointResponseTypeDef",
    "ClientListStreamsResponseStreamInfoListTypeDef",
    "ClientListStreamsResponseTypeDef",
    "ClientListStreamsStreamNameConditionTypeDef",
    "ClientListTagsForStreamResponseTypeDef",
    "ListStreamsPaginatePaginationConfigTypeDef",
    "ListStreamsPaginateResponseStreamInfoListTypeDef",
    "ListStreamsPaginateResponseTypeDef",
    "ListStreamsPaginateStreamNameConditionTypeDef",
)


_ClientCreateStreamResponseTypeDef = TypedDict(
    "_ClientCreateStreamResponseTypeDef", {"StreamARN": str}, total=False
)


class ClientCreateStreamResponseTypeDef(_ClientCreateStreamResponseTypeDef):
    """
    - *(dict) --*

      - **StreamARN** *(string) --*

        The Amazon Resource Name (ARN) of the stream.
    """


_ClientDescribeStreamResponseStreamInfoTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamInfoTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING"],
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)


class ClientDescribeStreamResponseStreamInfoTypeDef(_ClientDescribeStreamResponseStreamInfoTypeDef):
    """
    - **StreamInfo** *(dict) --*

      An object that describes the stream.
      - **DeviceName** *(string) --*

        The name of the device that is associated with the stream.
    """


_ClientDescribeStreamResponseTypeDef = TypedDict(
    "_ClientDescribeStreamResponseTypeDef",
    {"StreamInfo": ClientDescribeStreamResponseStreamInfoTypeDef},
    total=False,
)


class ClientDescribeStreamResponseTypeDef(_ClientDescribeStreamResponseTypeDef):
    """
    - *(dict) --*

      - **StreamInfo** *(dict) --*

        An object that describes the stream.
        - **DeviceName** *(string) --*

          The name of the device that is associated with the stream.
    """


_ClientGetDataEndpointResponseTypeDef = TypedDict(
    "_ClientGetDataEndpointResponseTypeDef", {"DataEndpoint": str}, total=False
)


class ClientGetDataEndpointResponseTypeDef(_ClientGetDataEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **DataEndpoint** *(string) --*

        The endpoint value. To read data from the stream or to write data to it, specify this
        endpoint in your application.
    """


_ClientListStreamsResponseStreamInfoListTypeDef = TypedDict(
    "_ClientListStreamsResponseStreamInfoListTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING"],
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)


class ClientListStreamsResponseStreamInfoListTypeDef(
    _ClientListStreamsResponseStreamInfoListTypeDef
):
    """
    - *(dict) --*

      An object describing a Kinesis video stream.
      - **DeviceName** *(string) --*

        The name of the device that is associated with the stream.
    """


_ClientListStreamsResponseTypeDef = TypedDict(
    "_ClientListStreamsResponseTypeDef",
    {"StreamInfoList": List[ClientListStreamsResponseStreamInfoListTypeDef], "NextToken": str},
    total=False,
)


class ClientListStreamsResponseTypeDef(_ClientListStreamsResponseTypeDef):
    """
    - *(dict) --*

      - **StreamInfoList** *(list) --*

        An array of ``StreamInfo`` objects.
        - *(dict) --*

          An object describing a Kinesis video stream.
          - **DeviceName** *(string) --*

            The name of the device that is associated with the stream.
    """


_ClientListStreamsStreamNameConditionTypeDef = TypedDict(
    "_ClientListStreamsStreamNameConditionTypeDef",
    {"ComparisonOperator": str, "ComparisonValue": str},
    total=False,
)


class ClientListStreamsStreamNameConditionTypeDef(_ClientListStreamsStreamNameConditionTypeDef):
    """
    Optional: Returns only streams that satisfy a specific condition. Currently, you can specify
    only the prefix of a stream name as a condition.
    - **ComparisonOperator** *(string) --*

      A comparison operator. Currently, you can specify only the ``BEGINS_WITH`` operator, which
      finds streams whose names start with a given prefix.
    """


_ClientListTagsForStreamResponseTypeDef = TypedDict(
    "_ClientListTagsForStreamResponseTypeDef",
    {"NextToken": str, "Tags": Dict[str, str]},
    total=False,
)


class ClientListTagsForStreamResponseTypeDef(_ClientListTagsForStreamResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If you specify this parameter and the result of a ``ListTags`` call is truncated, the
        response includes a token that you can use in the next request to fetch the next set of
        tags.
    """


_ListStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamsPaginatePaginationConfigTypeDef(_ListStreamsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStreamsPaginateResponseStreamInfoListTypeDef = TypedDict(
    "_ListStreamsPaginateResponseStreamInfoListTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING"],
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)


class ListStreamsPaginateResponseStreamInfoListTypeDef(
    _ListStreamsPaginateResponseStreamInfoListTypeDef
):
    """
    - *(dict) --*

      An object describing a Kinesis video stream.
      - **DeviceName** *(string) --*

        The name of the device that is associated with the stream.
    """


_ListStreamsPaginateResponseTypeDef = TypedDict(
    "_ListStreamsPaginateResponseTypeDef",
    {"StreamInfoList": List[ListStreamsPaginateResponseStreamInfoListTypeDef]},
    total=False,
)


class ListStreamsPaginateResponseTypeDef(_ListStreamsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **StreamInfoList** *(list) --*

        An array of ``StreamInfo`` objects.
        - *(dict) --*

          An object describing a Kinesis video stream.
          - **DeviceName** *(string) --*

            The name of the device that is associated with the stream.
    """


_ListStreamsPaginateStreamNameConditionTypeDef = TypedDict(
    "_ListStreamsPaginateStreamNameConditionTypeDef",
    {"ComparisonOperator": str, "ComparisonValue": str},
    total=False,
)


class ListStreamsPaginateStreamNameConditionTypeDef(_ListStreamsPaginateStreamNameConditionTypeDef):
    """
    Optional: Returns only streams that satisfy a specific condition. Currently, you can specify
    only the prefix of a stream name as a condition.
    - **ComparisonOperator** *(string) --*

      A comparison operator. Currently, you can specify only the ``BEGINS_WITH`` operator, which
      finds streams whose names start with a given prefix.
    """
