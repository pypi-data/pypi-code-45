"Main interface for efs service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateFileSystemResponseSizeInBytesTypeDef",
    "ClientCreateFileSystemResponseTagsTypeDef",
    "ClientCreateFileSystemResponseTypeDef",
    "ClientCreateFileSystemTagsTypeDef",
    "ClientCreateMountTargetResponseTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    "ClientDescribeFileSystemsResponseTypeDef",
    "ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    "ClientDescribeLifecycleConfigurationResponseTypeDef",
    "ClientDescribeMountTargetSecurityGroupsResponseTypeDef",
    "ClientDescribeMountTargetsResponseMountTargetsTypeDef",
    "ClientDescribeMountTargetsResponseTypeDef",
    "ClientDescribeTagsResponseTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef",
    "ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    "ClientPutLifecycleConfigurationResponseTypeDef",
    "ClientUpdateFileSystemResponseSizeInBytesTypeDef",
    "ClientUpdateFileSystemResponseTagsTypeDef",
    "ClientUpdateFileSystemResponseTypeDef",
    "DescribeFileSystemsPaginatePaginationConfigTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
    "DescribeFileSystemsPaginateResponseTypeDef",
    "DescribeMountTargetsPaginatePaginationConfigTypeDef",
    "DescribeMountTargetsPaginateResponseMountTargetsTypeDef",
    "DescribeMountTargetsPaginateResponseTypeDef",
    "DescribeTagsPaginatePaginationConfigTypeDef",
    "DescribeTagsPaginateResponseTagsTypeDef",
    "DescribeTagsPaginateResponseTypeDef",
)


_ClientCreateFileSystemResponseSizeInBytesTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class ClientCreateFileSystemResponseSizeInBytesTypeDef(
    _ClientCreateFileSystemResponseSizeInBytesTypeDef
):
    pass


_ClientCreateFileSystemResponseTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateFileSystemResponseTagsTypeDef(_ClientCreateFileSystemResponseTagsTypeDef):
    pass


_ClientCreateFileSystemResponseTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseTypeDef",
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


class ClientCreateFileSystemResponseTypeDef(_ClientCreateFileSystemResponseTypeDef):
    """
    - *(dict) --*

      A description of the file system.
      - **OwnerId** *(string) --*

        The AWS account that created the file system. If the file system was created by an IAM user,
        the parent account to which the user belongs is the owner.
    """


_RequiredClientCreateFileSystemTagsTypeDef = TypedDict(
    "_RequiredClientCreateFileSystemTagsTypeDef", {"Key": str}
)
_OptionalClientCreateFileSystemTagsTypeDef = TypedDict(
    "_OptionalClientCreateFileSystemTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateFileSystemTagsTypeDef(
    _RequiredClientCreateFileSystemTagsTypeDef, _OptionalClientCreateFileSystemTagsTypeDef
):
    """
    - *(dict) --*

      A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can
      be represented in UTF-8, and the following characters:``+ - = . _ : /``
      - **Key** *(string) --***[REQUIRED]**

        The tag key (String). The key can't start with ``aws:`` .
    """


_ClientCreateMountTargetResponseTypeDef = TypedDict(
    "_ClientCreateMountTargetResponseTypeDef",
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


class ClientCreateMountTargetResponseTypeDef(_ClientCreateMountTargetResponseTypeDef):
    """
    - *(dict) --*

      Provides a description of a mount target.
      - **OwnerId** *(string) --*

        AWS account ID that owns the resource.
    """


_RequiredClientCreateTagsTagsTypeDef = TypedDict(
    "_RequiredClientCreateTagsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTagsTagsTypeDef = TypedDict(
    "_OptionalClientCreateTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTagsTagsTypeDef(
    _RequiredClientCreateTagsTagsTypeDef, _OptionalClientCreateTagsTagsTypeDef
):
    """
    - *(dict) --*

      A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can
      be represented in UTF-8, and the following characters:``+ - = . _ : /``
      - **Key** *(string) --***[REQUIRED]**

        The tag key (String). The key can't start with ``aws:`` .
    """


_ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsSizeInBytesTypeDef
):
    pass


_ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef
):
    pass


_ClientDescribeFileSystemsResponseFileSystemsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsTypeDef",
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


class ClientDescribeFileSystemsResponseFileSystemsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsTypeDef
):
    pass


_ClientDescribeFileSystemsResponseTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List[ClientDescribeFileSystemsResponseFileSystemsTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeFileSystemsResponseTypeDef(_ClientDescribeFileSystemsResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        Present if provided by caller in the request (String).
    """


_ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef = TypedDict(
    "_ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)


class ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef(
    _ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef
):
    """
    - *(dict) --*

      Describes a policy used by EFS lifecycle management to transition files to the Infrequent
      Access (IA) storage class.
      - **TransitionToIA** *(string) --*

        A value that describes the period of time that a file is not accessed, after which it
        transitions to the IA storage class. Metadata operations such as listing the contents of a
        directory don't count as file access events.
    """


_ClientDescribeLifecycleConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeLifecycleConfigurationResponseTypeDef",
    {
        "LifecyclePolicies": List[
            ClientDescribeLifecycleConfigurationResponseLifecyclePoliciesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeLifecycleConfigurationResponseTypeDef(
    _ClientDescribeLifecycleConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **LifecyclePolicies** *(list) --*

        An array of lifecycle management policies. Currently, EFS supports a maximum of one policy
        per file system.
        - *(dict) --*

          Describes a policy used by EFS lifecycle management to transition files to the Infrequent
          Access (IA) storage class.
          - **TransitionToIA** *(string) --*

            A value that describes the period of time that a file is not accessed, after which it
            transitions to the IA storage class. Metadata operations such as listing the contents of
            a directory don't count as file access events.
    """


_ClientDescribeMountTargetSecurityGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeMountTargetSecurityGroupsResponseTypeDef",
    {"SecurityGroups": List[str]},
    total=False,
)


class ClientDescribeMountTargetSecurityGroupsResponseTypeDef(
    _ClientDescribeMountTargetSecurityGroupsResponseTypeDef
):
    """
    - *(dict) --*

      - **SecurityGroups** *(list) --*

        An array of security groups.
        - *(string) --*
    """


_ClientDescribeMountTargetsResponseMountTargetsTypeDef = TypedDict(
    "_ClientDescribeMountTargetsResponseMountTargetsTypeDef",
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


class ClientDescribeMountTargetsResponseMountTargetsTypeDef(
    _ClientDescribeMountTargetsResponseMountTargetsTypeDef
):
    pass


_ClientDescribeMountTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeMountTargetsResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List[ClientDescribeMountTargetsResponseMountTargetsTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeMountTargetsResponseTypeDef(_ClientDescribeMountTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        If the request included the ``Marker`` , the response returns that value in this field.
    """


_ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeTagsResponseTagsTypeDef(_ClientDescribeTagsResponseTagsTypeDef):
    pass


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"Marker": str, "Tags": List[ClientDescribeTagsResponseTagsTypeDef], "NextMarker": str},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        If the request included a ``Marker`` , the response returns that value in this field.
    """


_ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef = TypedDict(
    "_ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)


class ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef(
    _ClientPutLifecycleConfigurationLifecyclePoliciesTypeDef
):
    """
    - *(dict) --*

      Describes a policy used by EFS lifecycle management to transition files to the Infrequent
      Access (IA) storage class.
      - **TransitionToIA** *(string) --*

        A value that describes the period of time that a file is not accessed, after which it
        transitions to the IA storage class. Metadata operations such as listing the contents of a
        directory don't count as file access events.
    """


_ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef = TypedDict(
    "_ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef",
    {
        "TransitionToIA": Literal[
            "AFTER_7_DAYS", "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_90_DAYS"
        ]
    },
    total=False,
)


class ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef(
    _ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef
):
    """
    - *(dict) --*

      Describes a policy used by EFS lifecycle management to transition files to the Infrequent
      Access (IA) storage class.
      - **TransitionToIA** *(string) --*

        A value that describes the period of time that a file is not accessed, after which it
        transitions to the IA storage class. Metadata operations such as listing the contents of a
        directory don't count as file access events.
    """


_ClientPutLifecycleConfigurationResponseTypeDef = TypedDict(
    "_ClientPutLifecycleConfigurationResponseTypeDef",
    {"LifecyclePolicies": List[ClientPutLifecycleConfigurationResponseLifecyclePoliciesTypeDef]},
    total=False,
)


class ClientPutLifecycleConfigurationResponseTypeDef(
    _ClientPutLifecycleConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **LifecyclePolicies** *(list) --*

        An array of lifecycle management policies. Currently, EFS supports a maximum of one policy
        per file system.
        - *(dict) --*

          Describes a policy used by EFS lifecycle management to transition files to the Infrequent
          Access (IA) storage class.
          - **TransitionToIA** *(string) --*

            A value that describes the period of time that a file is not accessed, after which it
            transitions to the IA storage class. Metadata operations such as listing the contents of
            a directory don't count as file access events.
    """


_ClientUpdateFileSystemResponseSizeInBytesTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class ClientUpdateFileSystemResponseSizeInBytesTypeDef(
    _ClientUpdateFileSystemResponseSizeInBytesTypeDef
):
    pass


_ClientUpdateFileSystemResponseTagsTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdateFileSystemResponseTagsTypeDef(_ClientUpdateFileSystemResponseTagsTypeDef):
    pass


_ClientUpdateFileSystemResponseTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseTypeDef",
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


class ClientUpdateFileSystemResponseTypeDef(_ClientUpdateFileSystemResponseTypeDef):
    """
    - *(dict) --*

      A description of the file system.
      - **OwnerId** *(string) --*

        The AWS account that created the file system. If the file system was created by an IAM user,
        the parent account to which the user belongs is the owner.
    """


_DescribeFileSystemsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFileSystemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFileSystemsPaginatePaginationConfigTypeDef(
    _DescribeFileSystemsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef",
    {"Value": int, "Timestamp": datetime, "ValueInIA": int, "ValueInStandard": int},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsSizeInBytesTypeDef
):
    pass


_DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef
):
    pass


_DescribeFileSystemsPaginateResponseFileSystemsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
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


class DescribeFileSystemsPaginateResponseFileSystemsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsTypeDef
):
    pass


_DescribeFileSystemsPaginateResponseTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List[DescribeFileSystemsPaginateResponseFileSystemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseTypeDef(_DescribeFileSystemsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        Present if provided by caller in the request (String).
    """


_DescribeMountTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMountTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMountTargetsPaginatePaginationConfigTypeDef(
    _DescribeMountTargetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMountTargetsPaginateResponseMountTargetsTypeDef = TypedDict(
    "_DescribeMountTargetsPaginateResponseMountTargetsTypeDef",
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


class DescribeMountTargetsPaginateResponseMountTargetsTypeDef(
    _DescribeMountTargetsPaginateResponseMountTargetsTypeDef
):
    pass


_DescribeMountTargetsPaginateResponseTypeDef = TypedDict(
    "_DescribeMountTargetsPaginateResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List[DescribeMountTargetsPaginateResponseMountTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeMountTargetsPaginateResponseTypeDef(_DescribeMountTargetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        If the request included the ``Marker`` , the response returns that value in this field.
    """


_DescribeTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTagsPaginatePaginationConfigTypeDef(_DescribeTagsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTagsPaginateResponseTagsTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class DescribeTagsPaginateResponseTagsTypeDef(_DescribeTagsPaginateResponseTagsTypeDef):
    pass


_DescribeTagsPaginateResponseTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTypeDef",
    {"Marker": str, "Tags": List[DescribeTagsPaginateResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class DescribeTagsPaginateResponseTypeDef(_DescribeTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        If the request included a ``Marker`` , the response returns that value in this field.
    """
