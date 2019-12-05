"Main interface for mediastore service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateContainerResponseContainerTypeDef = TypedDict(
    "ClientCreateContainerResponseContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)

ClientCreateContainerResponseTypeDef = TypedDict(
    "ClientCreateContainerResponseTypeDef",
    {"Container": ClientCreateContainerResponseContainerTypeDef},
    total=False,
)

_RequiredClientCreateContainerTagsTypeDef = TypedDict(
    "_RequiredClientCreateContainerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateContainerTagsTypeDef = TypedDict(
    "_OptionalClientCreateContainerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateContainerTagsTypeDef(
    _RequiredClientCreateContainerTagsTypeDef, _OptionalClientCreateContainerTagsTypeDef
):
    pass


ClientDescribeContainerResponseContainerTypeDef = TypedDict(
    "ClientDescribeContainerResponseContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)

ClientDescribeContainerResponseTypeDef = TypedDict(
    "ClientDescribeContainerResponseTypeDef",
    {"Container": ClientDescribeContainerResponseContainerTypeDef},
    total=False,
)

ClientGetContainerPolicyResponseTypeDef = TypedDict(
    "ClientGetContainerPolicyResponseTypeDef", {"Policy": str}, total=False
)

ClientGetCorsPolicyResponseCorsPolicyTypeDef = TypedDict(
    "ClientGetCorsPolicyResponseCorsPolicyTypeDef",
    {
        "AllowedOrigins": List[str],
        "AllowedMethods": List[Literal["PUT", "GET", "DELETE", "HEAD"]],
        "AllowedHeaders": List[str],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)

ClientGetCorsPolicyResponseTypeDef = TypedDict(
    "ClientGetCorsPolicyResponseTypeDef",
    {"CorsPolicy": List[ClientGetCorsPolicyResponseCorsPolicyTypeDef]},
    total=False,
)

ClientGetLifecyclePolicyResponseTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponseTypeDef", {"LifecyclePolicy": str}, total=False
)

ClientListContainersResponseContainersTypeDef = TypedDict(
    "ClientListContainersResponseContainersTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)

ClientListContainersResponseTypeDef = TypedDict(
    "ClientListContainersResponseTypeDef",
    {"Containers": List[ClientListContainersResponseContainersTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

_RequiredClientPutCorsPolicyCorsPolicyTypeDef = TypedDict(
    "_RequiredClientPutCorsPolicyCorsPolicyTypeDef", {"AllowedOrigins": List[str]}
)
_OptionalClientPutCorsPolicyCorsPolicyTypeDef = TypedDict(
    "_OptionalClientPutCorsPolicyCorsPolicyTypeDef",
    {
        "AllowedMethods": List[Literal["PUT", "GET", "DELETE", "HEAD"]],
        "AllowedHeaders": List[str],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)


class ClientPutCorsPolicyCorsPolicyTypeDef(
    _RequiredClientPutCorsPolicyCorsPolicyTypeDef, _OptionalClientPutCorsPolicyCorsPolicyTypeDef
):
    pass


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ListContainersPaginatePaginationConfigTypeDef = TypedDict(
    "ListContainersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListContainersPaginateResponseContainersTypeDef = TypedDict(
    "ListContainersPaginateResponseContainersTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)

ListContainersPaginateResponseTypeDef = TypedDict(
    "ListContainersPaginateResponseTypeDef",
    {"Containers": List[ListContainersPaginateResponseContainersTypeDef]},
    total=False,
)
