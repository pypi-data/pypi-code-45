"Main interface for efs service type defs"
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


ClientCreateFileSystemResponseSizeInBytesTypeDef = TypedDict(
    "ClientCreateFileSystemResponseSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)

ClientCreateFileSystemResponseTagsTypeDef = TypedDict(
    "ClientCreateFileSystemResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemResponseTypeDef = TypedDict(
    "ClientCreateFileSystemResponseTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": ClientCreateFileSystemResponseSizeInBytesTypeDef,
        "PerformanceMode": Literal["generalPurpose", "maxIO"],
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": Literal["bursting", "provisioned"],
        "ProvisionedThroughputInMibps": float,
        "Tags": List[ClientCreateFileSystemResponseTagsTypeDef],
    },
    total=False,
)

_RequiredClientCreateFileSystemTagsTypeDef = TypedDict(
    "_RequiredClientCreateFileSystemTagsTypeDef", {"Key": str}
)
_OptionalClientCreateFileSystemTagsTypeDef = TypedDict(
    "_OptionalClientCreateFileSystemTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateFileSystemTagsTypeDef(
    _RequiredClientCreateFileSystemTagsTypeDef, _OptionalClientCreateFileSystemTagsTypeDef
):
    pass


ClientCreateMountTargetResponseTypeDef = TypedDict(
    "ClientCreateMountTargetResponseTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "IpAddress": str,
        "NetworkInterfaceId": str,
    },
    total=False,
)

_RequiredClientCreateTagsTagsTypeDef = TypedDict(
    "_RequiredClientCreateTagsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTagsTagsTypeDef = TypedDict(
    "_OptionalClientCreateTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTagsTagsTypeDef(
    _RequiredClientCreateTagsTagsTypeDef, _OptionalClientCreateTagsTagsTypeDef
):
    pass


ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef,
        "PerformanceMode": Literal["generalPurpose", "maxIO"],
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": Literal["bursting", "provisioned"],
        "ProvisionedThroughputInMibps": float,
        "Tags": List[ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef],
    },
    total=False,
)

ClientDescribeFileSystemsResponseTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List[ClientDescribeFileSystemsResponseFileSystemsTypeDef],
        "NextMarker": str,
    },
    total=False,
)

ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef = TypedDict(
    "ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)

ClientDescribeLifecycleConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeLifecycleConfigurationResponseTypeDef",
    {
        "LifecyclePolicies": List[
            ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef
        ]
    },
    total=False,
)

ClientDescribeMountTargetSecurityGroupsResponseTypeDef = TypedDict(
    "ClientDescribeMountTargetSecurityGroupsResponseTypeDef",
    {"SecurityGroups": List[str]},
    total=False,
)

ClientDescribeMountTargetsResponseMountTargetsTypeDef = TypedDict(
    "ClientDescribeMountTargetsResponseMountTargetsTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "IpAddress": str,
        "NetworkInterfaceId": str,
    },
    total=False,
)

ClientDescribeMountTargetsResponseTypeDef = TypedDict(
    "ClientDescribeMountTargetsResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List[ClientDescribeMountTargetsResponseMountTargetsTypeDef],
        "NextMarker": str,
    },
    total=False,
)

ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"Marker": str, "Tags": List[ClientDescribeTagsResponseTagsTypeDef], "NextMarker": str},
    total=False,
)

ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef = TypedDict(
    "ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)

ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef = TypedDict(
    "ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)

ClientPutLifecycleConfigurationResponseTypeDef = TypedDict(
    "ClientPutLifecycleConfigurationResponseTypeDef",
    {"LifecyclePolicies": List[ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef]},
    total=False,
)

ClientUpdateFileSystemResponseSizeInBytesTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)

ClientUpdateFileSystemResponseTagsTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateFileSystemResponseTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": ClientUpdateFileSystemResponseSizeInBytesTypeDef,
        "PerformanceMode": Literal["generalPurpose", "maxIO"],
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": Literal["bursting", "provisioned"],
        "ProvisionedThroughputInMibps": float,
        "Tags": List[ClientUpdateFileSystemResponseTagsTypeDef],
    },
    total=False,
)

DescribeFileSystemsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeFileSystemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)

DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

DescribeFileSystemsPaginateResponseFileSystemsTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef,
        "PerformanceMode": Literal["generalPurpose", "maxIO"],
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": Literal["bursting", "provisioned"],
        "ProvisionedThroughputInMibps": float,
        "Tags": List[DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef],
    },
    total=False,
)

DescribeFileSystemsPaginateResponseTypeDef = TypedDict(
    "DescribeFileSystemsPaginateResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List[DescribeFileSystemsPaginateResponseFileSystemsTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeMountTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMountTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMountTargetsPaginateResponseMountTargetsTypeDef = TypedDict(
    "DescribeMountTargetsPaginateResponseMountTargetsTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": Literal["creating", "available", "updating", "deleting", "deleted"],
        "IpAddress": str,
        "NetworkInterfaceId": str,
    },
    total=False,
)

DescribeMountTargetsPaginateResponseTypeDef = TypedDict(
    "DescribeMountTargetsPaginateResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List[DescribeMountTargetsPaginateResponseMountTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeTagsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeTagsPaginateResponseTagsTypeDef = TypedDict(
    "DescribeTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

DescribeTagsPaginateResponseTypeDef = TypedDict(
    "DescribeTagsPaginateResponseTypeDef",
    {"Marker": str, "Tags": List[DescribeTagsPaginateResponseTagsTypeDef], "NextToken": str},
    total=False,
)
