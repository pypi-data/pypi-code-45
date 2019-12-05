"Main interface for mediastore-data service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientDescribeObjectResponseTypeDef = TypedDict(
    "ClientDescribeObjectResponseTypeDef",
    {
        "ETag": str,
        "ContentType": str,
        "ContentLength": int,
        "CacheControl": str,
        "LastModified": datetime,
    },
    total=False,
)

ClientGetObjectResponseTypeDef = TypedDict(
    "ClientGetObjectResponseTypeDef",
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

ClientListItemsResponseItemsTypeDef = TypedDict(
    "ClientListItemsResponseItemsTypeDef",
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

ClientListItemsResponseTypeDef = TypedDict(
    "ClientListItemsResponseTypeDef",
    {"Items": List[ClientListItemsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientPutObjectResponseTypeDef = TypedDict(
    "ClientPutObjectResponseTypeDef",
    {"ContentSHA256": str, "ETag": str, "StorageClass": str},
    total=False,
)

ListItemsPaginatePaginationConfigTypeDef = TypedDict(
    "ListItemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListItemsPaginateResponseItemsTypeDef = TypedDict(
    "ListItemsPaginateResponseItemsTypeDef",
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

ListItemsPaginateResponseTypeDef = TypedDict(
    "ListItemsPaginateResponseTypeDef",
    {"Items": List[ListItemsPaginateResponseItemsTypeDef]},
    total=False,
)
