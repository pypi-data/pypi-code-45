"Main interface for mediastore-data service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeObjectResponseTypeDef",
    "ClientGetObjectResponseTypeDef",
    "ClientListItemsResponseItemsTypeDef",
    "ClientListItemsResponseTypeDef",
    "ClientPutObjectResponseTypeDef",
    "ListItemsPaginatePaginationConfigTypeDef",
    "ListItemsPaginateResponseItemsTypeDef",
    "ListItemsPaginateResponseTypeDef",
)


_ClientDescribeObjectResponseTypeDef = TypedDict(
    "_ClientDescribeObjectResponseTypeDef",
    {
        "ETag": str,
        "ContentType": str,
        "ContentLength": int,
        "CacheControl": str,
        "LastModified": datetime,
    },
    total=False,
)


class ClientDescribeObjectResponseTypeDef(_ClientDescribeObjectResponseTypeDef):
    """
    - *(dict) --*

      - **ETag** *(string) --*

        The ETag that represents a unique instance of the object.
    """


_ClientGetObjectResponseTypeDef = TypedDict(
    "_ClientGetObjectResponseTypeDef",
    {
        "Body": StreamingBody,
        "CacheControl": str,
        "ContentRange": str,
        "ContentLength": int,
        "ContentType": str,
        "ETag": str,
        "LastModified": datetime,
        "StatusCode": int,
    },
    total=False,
)


class ClientGetObjectResponseTypeDef(_ClientGetObjectResponseTypeDef):
    """
    - *(dict) --*

      - **Body** (:class:`.StreamingBody`) --

        The bytes of the object.
    """


_ClientListItemsResponseItemsTypeDef = TypedDict(
    "_ClientListItemsResponseItemsTypeDef",
    {
        "Name": str,
        "Type": Literal["OBJECT", "FOLDER"],
        "ETag": str,
        "LastModified": datetime,
        "ContentType": str,
        "ContentLength": int,
    },
    total=False,
)


class ClientListItemsResponseItemsTypeDef(_ClientListItemsResponseItemsTypeDef):
    """
    - *(dict) --*

      A metadata entry for a folder or object.
      - **Name** *(string) --*

        The name of the item.
    """


_ClientListItemsResponseTypeDef = TypedDict(
    "_ClientListItemsResponseTypeDef",
    {"Items": List[ClientListItemsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientListItemsResponseTypeDef(_ClientListItemsResponseTypeDef):
    """
    - *(dict) --*

      - **Items** *(list) --*

        The metadata entries for the folders and objects at the requested path.
        - *(dict) --*

          A metadata entry for a folder or object.
          - **Name** *(string) --*

            The name of the item.
    """


_ClientPutObjectResponseTypeDef = TypedDict(
    "_ClientPutObjectResponseTypeDef",
    {"ContentSHA256": str, "ETag": str, "StorageClass": str},
    total=False,
)


class ClientPutObjectResponseTypeDef(_ClientPutObjectResponseTypeDef):
    """
    - *(dict) --*

      - **ContentSHA256** *(string) --*

        The SHA256 digest of the object that is persisted.
    """


_ListItemsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListItemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListItemsPaginatePaginationConfigTypeDef(_ListItemsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListItemsPaginateResponseItemsTypeDef = TypedDict(
    "_ListItemsPaginateResponseItemsTypeDef",
    {
        "Name": str,
        "Type": Literal["OBJECT", "FOLDER"],
        "ETag": str,
        "LastModified": datetime,
        "ContentType": str,
        "ContentLength": int,
    },
    total=False,
)


class ListItemsPaginateResponseItemsTypeDef(_ListItemsPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      A metadata entry for a folder or object.
      - **Name** *(string) --*

        The name of the item.
    """


_ListItemsPaginateResponseTypeDef = TypedDict(
    "_ListItemsPaginateResponseTypeDef",
    {"Items": List[ListItemsPaginateResponseItemsTypeDef]},
    total=False,
)


class ListItemsPaginateResponseTypeDef(_ListItemsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Items** *(list) --*

        The metadata entries for the folders and objects at the requested path.
        - *(dict) --*

          A metadata entry for a folder or object.
          - **Name** *(string) --*

            The name of the item.
    """
