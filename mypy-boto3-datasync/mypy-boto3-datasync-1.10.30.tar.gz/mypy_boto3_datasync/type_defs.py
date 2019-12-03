"Main interface for datasync service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateAgentResponseTypeDef",
    "ClientCreateAgentTagsTypeDef",
    "ClientCreateLocationEfsEc2ConfigTypeDef",
    "ClientCreateLocationEfsResponseTypeDef",
    "ClientCreateLocationEfsTagsTypeDef",
    "ClientCreateLocationNfsMountOptionsTypeDef",
    "ClientCreateLocationNfsOnPremConfigTypeDef",
    "ClientCreateLocationNfsResponseTypeDef",
    "ClientCreateLocationNfsTagsTypeDef",
    "ClientCreateLocationS3ResponseTypeDef",
    "ClientCreateLocationS3S3ConfigTypeDef",
    "ClientCreateLocationS3TagsTypeDef",
    "ClientCreateLocationSmbMountOptionsTypeDef",
    "ClientCreateLocationSmbResponseTypeDef",
    "ClientCreateLocationSmbTagsTypeDef",
    "ClientCreateTaskExcludesTypeDef",
    "ClientCreateTaskOptionsTypeDef",
    "ClientCreateTaskResponseTypeDef",
    "ClientCreateTaskScheduleTypeDef",
    "ClientCreateTaskTagsTypeDef",
    "ClientDescribeAgentResponsePrivateLinkConfigTypeDef",
    "ClientDescribeAgentResponseTypeDef",
    "ClientDescribeLocationEfsResponseEc2ConfigTypeDef",
    "ClientDescribeLocationEfsResponseTypeDef",
    "ClientDescribeLocationNfsResponseMountOptionsTypeDef",
    "ClientDescribeLocationNfsResponseOnPremConfigTypeDef",
    "ClientDescribeLocationNfsResponseTypeDef",
    "ClientDescribeLocationS3ResponseS3ConfigTypeDef",
    "ClientDescribeLocationS3ResponseTypeDef",
    "ClientDescribeLocationSmbResponseMountOptionsTypeDef",
    "ClientDescribeLocationSmbResponseTypeDef",
    "ClientDescribeTaskExecutionResponseExcludesTypeDef",
    "ClientDescribeTaskExecutionResponseIncludesTypeDef",
    "ClientDescribeTaskExecutionResponseOptionsTypeDef",
    "ClientDescribeTaskExecutionResponseResultTypeDef",
    "ClientDescribeTaskExecutionResponseTypeDef",
    "ClientDescribeTaskResponseExcludesTypeDef",
    "ClientDescribeTaskResponseOptionsTypeDef",
    "ClientDescribeTaskResponseScheduleTypeDef",
    "ClientDescribeTaskResponseTypeDef",
    "ClientListAgentsResponseAgentsTypeDef",
    "ClientListAgentsResponseTypeDef",
    "ClientListLocationsResponseLocationsTypeDef",
    "ClientListLocationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTaskExecutionsResponseTaskExecutionsTypeDef",
    "ClientListTaskExecutionsResponseTypeDef",
    "ClientListTasksResponseTasksTypeDef",
    "ClientListTasksResponseTypeDef",
    "ClientStartTaskExecutionIncludesTypeDef",
    "ClientStartTaskExecutionOverrideOptionsTypeDef",
    "ClientStartTaskExecutionResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateTaskExcludesTypeDef",
    "ClientUpdateTaskOptionsTypeDef",
    "ClientUpdateTaskScheduleTypeDef",
    "ListAgentsPaginatePaginationConfigTypeDef",
    "ListAgentsPaginateResponseAgentsTypeDef",
    "ListAgentsPaginateResponseTypeDef",
    "ListLocationsPaginatePaginationConfigTypeDef",
    "ListLocationsPaginateResponseLocationsTypeDef",
    "ListLocationsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListTaskExecutionsPaginatePaginationConfigTypeDef",
    "ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef",
    "ListTaskExecutionsPaginateResponseTypeDef",
    "ListTasksPaginatePaginationConfigTypeDef",
    "ListTasksPaginateResponseTasksTypeDef",
    "ListTasksPaginateResponseTypeDef",
)


_ClientCreateAgentResponseTypeDef = TypedDict(
    "_ClientCreateAgentResponseTypeDef", {"AgentArn": str}, total=False
)


class ClientCreateAgentResponseTypeDef(_ClientCreateAgentResponseTypeDef):
    """
    - *(dict) --*

      CreateAgentResponse
      - **AgentArn** *(string) --*

        The Amazon Resource Name (ARN) of the agent. Use the ``ListAgents`` operation to return a
        list of agents for your account and AWS Region.
    """


_ClientCreateAgentTagsTypeDef = TypedDict(
    "_ClientCreateAgentTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateAgentTagsTypeDef(_ClientCreateAgentTagsTypeDef):
    pass


_RequiredClientCreateLocationEfsEc2ConfigTypeDef = TypedDict(
    "_RequiredClientCreateLocationEfsEc2ConfigTypeDef", {"SubnetArn": str}
)
_OptionalClientCreateLocationEfsEc2ConfigTypeDef = TypedDict(
    "_OptionalClientCreateLocationEfsEc2ConfigTypeDef",
    {"SecurityGroupArns": List[str]},
    total=False,
)


class ClientCreateLocationEfsEc2ConfigTypeDef(
    _RequiredClientCreateLocationEfsEc2ConfigTypeDef,
    _OptionalClientCreateLocationEfsEc2ConfigTypeDef,
):
    """
    The subnet and security group that the Amazon EFS file system uses. The security group that you
    provide needs to be able to communicate with the security group on the mount target in the
    subnet specified.
    The exact relationship between security group M (of the mount target) and security group S
    (which you provide for DataSync to use at this stage) is as follows:
    * Security group M (which you associate with the mount target) must allow inbound access for the
    Transmission Control Protocol (TCP) on the NFS port (2049) from security group S. You can enable
    inbound connections either by IP address (CIDR range) or security group.
    * Security group S (provided to DataSync to access EFS) should have a rule that enables outbound
    connections to the NFS port on one of the file system’s mount targets. You can enable outbound
    connections either by IP address (CIDR range) or security group. For information about security
    groups and mount targets, see Security Groups for Amazon EC2 Instances and Mount Targets in the
    *Amazon EFS User Guide.*
    - **SubnetArn** *(string) --***[REQUIRED]**

      The ARN of the subnet and the security group that DataSync uses to access the target EFS file
      system.
    """


_ClientCreateLocationEfsResponseTypeDef = TypedDict(
    "_ClientCreateLocationEfsResponseTypeDef", {"LocationArn": str}, total=False
)


class ClientCreateLocationEfsResponseTypeDef(_ClientCreateLocationEfsResponseTypeDef):
    """
    - *(dict) --*

      CreateLocationEfs
      - **LocationArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
    """


_RequiredClientCreateLocationEfsTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationEfsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationEfsTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationEfsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationEfsTagsTypeDef(
    _RequiredClientCreateLocationEfsTagsTypeDef, _OptionalClientCreateLocationEfsTagsTypeDef
):
    """
    - *(dict) --*

      Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
      that contains a list of tasks when the  ListTagsForResource operation is called.
      - **Key** *(string) --***[REQUIRED]**

        The key for an AWS resource tag.
    """


_ClientCreateLocationNfsMountOptionsTypeDef = TypedDict(
    "_ClientCreateLocationNfsMountOptionsTypeDef",
    {"Version": Literal["AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1"]},
    total=False,
)


class ClientCreateLocationNfsMountOptionsTypeDef(_ClientCreateLocationNfsMountOptionsTypeDef):
    """
    The NFS mount options that DataSync can use to mount your NFS share.
    - **Version** *(string) --*

      The specific NFS version that you want DataSync to use to mount your NFS share. If the server
      refuses to use the version specified, the sync will fail. If you don't specify a version,
      DataSync defaults to ``AUTOMATIC`` . That is, DataSync automatically selects a version based
      on negotiation with the NFS server.
      You can specify the following NFS versions:
      * **`NFSv3 <https://tools.ietf.org/html/rfc1813>`__ ** - stateless protocol version that
      allows for asynchronous writes on the server.
      * **`NFSv4.0 <https://tools.ietf.org/html/rfc3530>`__ ** - stateful, firewall-friendly
      protocol version that supports delegations and pseudo filesystems.
      * **`NFSv4.1 <https://tools.ietf.org/html/rfc5661>`__ ** - stateful protocol version that
      supports sessions, directory delegations, and parallel data processing. Version 4.1 also
      includes all features available in version 4.0.
    """


_ClientCreateLocationNfsOnPremConfigTypeDef = TypedDict(
    "_ClientCreateLocationNfsOnPremConfigTypeDef", {"AgentArns": List[str]}
)


class ClientCreateLocationNfsOnPremConfigTypeDef(_ClientCreateLocationNfsOnPremConfigTypeDef):
    """
    Contains a list of Amazon Resource Names (ARNs) of agents that are used to connect to an NFS
    server.
    - **AgentArns** *(list) --***[REQUIRED]**

      ARNs)of the agents to use for an NFS location.
      - *(string) --*
    """


_ClientCreateLocationNfsResponseTypeDef = TypedDict(
    "_ClientCreateLocationNfsResponseTypeDef", {"LocationArn": str}, total=False
)


class ClientCreateLocationNfsResponseTypeDef(_ClientCreateLocationNfsResponseTypeDef):
    """
    - *(dict) --*

      CreateLocationNfsResponse
      - **LocationArn** *(string) --*

        The Amazon Resource Name (ARN) of the source NFS file system location that is created.
    """


_RequiredClientCreateLocationNfsTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationNfsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationNfsTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationNfsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationNfsTagsTypeDef(
    _RequiredClientCreateLocationNfsTagsTypeDef, _OptionalClientCreateLocationNfsTagsTypeDef
):
    """
    - *(dict) --*

      Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
      that contains a list of tasks when the  ListTagsForResource operation is called.
      - **Key** *(string) --***[REQUIRED]**

        The key for an AWS resource tag.
    """


_ClientCreateLocationS3ResponseTypeDef = TypedDict(
    "_ClientCreateLocationS3ResponseTypeDef", {"LocationArn": str}, total=False
)


class ClientCreateLocationS3ResponseTypeDef(_ClientCreateLocationS3ResponseTypeDef):
    """
    - *(dict) --*

      CreateLocationS3Response
      - **LocationArn** *(string) --*

        The Amazon Resource Name (ARN) of the source Amazon S3 bucket location that is created.
    """


_ClientCreateLocationS3S3ConfigTypeDef = TypedDict(
    "_ClientCreateLocationS3S3ConfigTypeDef", {"BucketAccessRoleArn": str}
)


class ClientCreateLocationS3S3ConfigTypeDef(_ClientCreateLocationS3S3ConfigTypeDef):
    """
    The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used
    to access an Amazon S3 bucket.
    For detailed information about using such a role, see Creating a Location for Amazon S3 in the
    *AWS DataSync User Guide* .
    - **BucketAccessRoleArn** *(string) --***[REQUIRED]**

      The Amazon S3 bucket to access. This bucket is used as a parameter in the  CreateLocationS3
      operation.
    """


_RequiredClientCreateLocationS3TagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationS3TagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationS3TagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationS3TagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationS3TagsTypeDef(
    _RequiredClientCreateLocationS3TagsTypeDef, _OptionalClientCreateLocationS3TagsTypeDef
):
    """
    - *(dict) --*

      Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
      that contains a list of tasks when the  ListTagsForResource operation is called.
      - **Key** *(string) --***[REQUIRED]**

        The key for an AWS resource tag.
    """


_ClientCreateLocationSmbMountOptionsTypeDef = TypedDict(
    "_ClientCreateLocationSmbMountOptionsTypeDef",
    {"Version": Literal["AUTOMATIC", "SMB2", "SMB3"]},
    total=False,
)


class ClientCreateLocationSmbMountOptionsTypeDef(_ClientCreateLocationSmbMountOptionsTypeDef):
    """
    The mount options used by DataSync to access the SMB server.
    - **Version** *(string) --*

      The specific SMB version that you want DataSync to use to mount your SMB share. If you don't
      specify a version, DataSync defaults to ``AUTOMATIC`` . That is, DataSync automatically
      selects a version based on negotiation with the SMB server.
    """


_ClientCreateLocationSmbResponseTypeDef = TypedDict(
    "_ClientCreateLocationSmbResponseTypeDef", {"LocationArn": str}, total=False
)


class ClientCreateLocationSmbResponseTypeDef(_ClientCreateLocationSmbResponseTypeDef):
    """
    - *(dict) --*

      CreateLocationSmbResponse
      - **LocationArn** *(string) --*

        The Amazon Resource Name (ARN) of the source SMB file system location that is created.
    """


_RequiredClientCreateLocationSmbTagsTypeDef = TypedDict(
    "_RequiredClientCreateLocationSmbTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLocationSmbTagsTypeDef = TypedDict(
    "_OptionalClientCreateLocationSmbTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLocationSmbTagsTypeDef(
    _RequiredClientCreateLocationSmbTagsTypeDef, _OptionalClientCreateLocationSmbTagsTypeDef
):
    """
    - *(dict) --*

      Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
      that contains a list of tasks when the  ListTagsForResource operation is called.
      - **Key** *(string) --***[REQUIRED]**

        The key for an AWS resource tag.
    """


_ClientCreateTaskExcludesTypeDef = TypedDict(
    "_ClientCreateTaskExcludesTypeDef", {"FilterType": str, "Value": str}, total=False
)


class ClientCreateTaskExcludesTypeDef(_ClientCreateTaskExcludesTypeDef):
    """
    - *(dict) --*

      Specifies which files, folders and objects to include or exclude when transferring files from
      source to destination.
      - **FilterType** *(string) --*

        The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.
    """


_ClientCreateTaskOptionsTypeDef = TypedDict(
    "_ClientCreateTaskOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientCreateTaskOptionsTypeDef(_ClientCreateTaskOptionsTypeDef):
    """
    The set of configuration options that control the behavior of a single execution of the task
    that occurs when you call ``StartTaskExecution`` . You can configure these options to preserve
    metadata such as user ID (UID) and group ID (GID), file permissions, data integrity
    verification, and so on.
    For each individual task execution, you can override these options by specifying the
    ``OverrideOptions`` before starting a the task execution. For more information, see the
    operation.
    - **VerifyMode** *(string) --*

      A value that determines whether a data integrity verification should be performed at the end
      of a task execution after all data and metadata have been transferred.
      Default value: POINT_IN_TIME_CONSISTENT.
      POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
      ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.
      NONE: Skip verification.
    """


_ClientCreateTaskResponseTypeDef = TypedDict(
    "_ClientCreateTaskResponseTypeDef", {"TaskArn": str}, total=False
)


class ClientCreateTaskResponseTypeDef(_ClientCreateTaskResponseTypeDef):
    """
    - *(dict) --*

      CreateTaskResponse
      - **TaskArn** *(string) --*

        The Amazon Resource Name (ARN) of the task.
    """


_ClientCreateTaskScheduleTypeDef = TypedDict(
    "_ClientCreateTaskScheduleTypeDef", {"ScheduleExpression": str}
)


class ClientCreateTaskScheduleTypeDef(_ClientCreateTaskScheduleTypeDef):
    """
    Specifies a schedule used to periodically transfer files from a source to a destination
    location. The schedule should be specified in UTC time. For more information, see
    task-scheduling .
    - **ScheduleExpression** *(string) --***[REQUIRED]**

      A cron expression that specifies when AWS DataSync initiates a scheduled transfer from a
      source to a destination location.
    """


_RequiredClientCreateTaskTagsTypeDef = TypedDict(
    "_RequiredClientCreateTaskTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTaskTagsTypeDef = TypedDict(
    "_OptionalClientCreateTaskTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTaskTagsTypeDef(
    _RequiredClientCreateTaskTagsTypeDef, _OptionalClientCreateTaskTagsTypeDef
):
    """
    - *(dict) --*

      Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
      that contains a list of tasks when the  ListTagsForResource operation is called.
      - **Key** *(string) --***[REQUIRED]**

        The key for an AWS resource tag.
    """


_ClientDescribeAgentResponsePrivateLinkConfigTypeDef = TypedDict(
    "_ClientDescribeAgentResponsePrivateLinkConfigTypeDef",
    {
        "VpcEndpointId": str,
        "PrivateLinkEndpoint": str,
        "SubnetArns": List[str],
        "SecurityGroupArns": List[str],
    },
    total=False,
)


class ClientDescribeAgentResponsePrivateLinkConfigTypeDef(
    _ClientDescribeAgentResponsePrivateLinkConfigTypeDef
):
    pass


_ClientDescribeAgentResponseTypeDef = TypedDict(
    "_ClientDescribeAgentResponseTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": Literal["ONLINE", "OFFLINE"],
        "LastConnectionTime": datetime,
        "CreationTime": datetime,
        "EndpointType": Literal["PUBLIC", "PRIVATE_LINK", "FIPS"],
        "PrivateLinkConfig": ClientDescribeAgentResponsePrivateLinkConfigTypeDef,
    },
    total=False,
)


class ClientDescribeAgentResponseTypeDef(_ClientDescribeAgentResponseTypeDef):
    """
    - *(dict) --*

      DescribeAgentResponse
      - **AgentArn** *(string) --*

        The Amazon Resource Name (ARN) of the agent.
    """


_ClientDescribeLocationEfsResponseEc2ConfigTypeDef = TypedDict(
    "_ClientDescribeLocationEfsResponseEc2ConfigTypeDef",
    {"SubnetArn": str, "SecurityGroupArns": List[str]},
    total=False,
)


class ClientDescribeLocationEfsResponseEc2ConfigTypeDef(
    _ClientDescribeLocationEfsResponseEc2ConfigTypeDef
):
    pass


_ClientDescribeLocationEfsResponseTypeDef = TypedDict(
    "_ClientDescribeLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "Ec2Config": ClientDescribeLocationEfsResponseEc2ConfigTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeLocationEfsResponseTypeDef(_ClientDescribeLocationEfsResponseTypeDef):
    """
    - *(dict) --*

      DescribeLocationEfsResponse
      - **LocationArn** *(string) --*

        The Amazon resource Name (ARN) of the EFS location that was described.
    """


_ClientDescribeLocationNfsResponseMountOptionsTypeDef = TypedDict(
    "_ClientDescribeLocationNfsResponseMountOptionsTypeDef",
    {"Version": Literal["AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1"]},
    total=False,
)


class ClientDescribeLocationNfsResponseMountOptionsTypeDef(
    _ClientDescribeLocationNfsResponseMountOptionsTypeDef
):
    pass


_ClientDescribeLocationNfsResponseOnPremConfigTypeDef = TypedDict(
    "_ClientDescribeLocationNfsResponseOnPremConfigTypeDef", {"AgentArns": List[str]}, total=False
)


class ClientDescribeLocationNfsResponseOnPremConfigTypeDef(
    _ClientDescribeLocationNfsResponseOnPremConfigTypeDef
):
    pass


_ClientDescribeLocationNfsResponseTypeDef = TypedDict(
    "_ClientDescribeLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "OnPremConfig": ClientDescribeLocationNfsResponseOnPremConfigTypeDef,
        "MountOptions": ClientDescribeLocationNfsResponseMountOptionsTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeLocationNfsResponseTypeDef(_ClientDescribeLocationNfsResponseTypeDef):
    """
    - *(dict) --*

      DescribeLocationNfsResponse
      - **LocationArn** *(string) --*

        The Amazon resource Name (ARN) of the NFS location that was described.
    """


_ClientDescribeLocationS3ResponseS3ConfigTypeDef = TypedDict(
    "_ClientDescribeLocationS3ResponseS3ConfigTypeDef", {"BucketAccessRoleArn": str}, total=False
)


class ClientDescribeLocationS3ResponseS3ConfigTypeDef(
    _ClientDescribeLocationS3ResponseS3ConfigTypeDef
):
    pass


_ClientDescribeLocationS3ResponseTypeDef = TypedDict(
    "_ClientDescribeLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "S3StorageClass": Literal[
            "STANDARD",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "S3Config": ClientDescribeLocationS3ResponseS3ConfigTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeLocationS3ResponseTypeDef(_ClientDescribeLocationS3ResponseTypeDef):
    """
    - *(dict) --*

      DescribeLocationS3Response
      - **LocationArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon S3 bucket location.
    """


_ClientDescribeLocationSmbResponseMountOptionsTypeDef = TypedDict(
    "_ClientDescribeLocationSmbResponseMountOptionsTypeDef",
    {"Version": Literal["AUTOMATIC", "SMB2", "SMB3"]},
    total=False,
)


class ClientDescribeLocationSmbResponseMountOptionsTypeDef(
    _ClientDescribeLocationSmbResponseMountOptionsTypeDef
):
    pass


_ClientDescribeLocationSmbResponseTypeDef = TypedDict(
    "_ClientDescribeLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AgentArns": List[str],
        "User": str,
        "Domain": str,
        "MountOptions": ClientDescribeLocationSmbResponseMountOptionsTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeLocationSmbResponseTypeDef(_ClientDescribeLocationSmbResponseTypeDef):
    """
    - *(dict) --*

      DescribeLocationSmbResponse
      - **LocationArn** *(string) --*

        The Amazon resource Name (ARN) of the SMB location that was described.
    """


_ClientDescribeTaskExecutionResponseExcludesTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseExcludesTypeDef",
    {"FilterType": str, "Value": str},
    total=False,
)


class ClientDescribeTaskExecutionResponseExcludesTypeDef(
    _ClientDescribeTaskExecutionResponseExcludesTypeDef
):
    pass


_ClientDescribeTaskExecutionResponseIncludesTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseIncludesTypeDef",
    {"FilterType": str, "Value": str},
    total=False,
)


class ClientDescribeTaskExecutionResponseIncludesTypeDef(
    _ClientDescribeTaskExecutionResponseIncludesTypeDef
):
    pass


_ClientDescribeTaskExecutionResponseOptionsTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDescribeTaskExecutionResponseOptionsTypeDef(
    _ClientDescribeTaskExecutionResponseOptionsTypeDef
):
    pass


_ClientDescribeTaskExecutionResponseResultTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseResultTypeDef",
    {
        "PrepareDuration": int,
        "PrepareStatus": Literal["PENDING", "SUCCESS", "ERROR"],
        "TotalDuration": int,
        "TransferDuration": int,
        "TransferStatus": Literal["PENDING", "SUCCESS", "ERROR"],
        "VerifyDuration": int,
        "VerifyStatus": Literal["PENDING", "SUCCESS", "ERROR"],
        "ErrorCode": str,
        "ErrorDetail": str,
    },
    total=False,
)


class ClientDescribeTaskExecutionResponseResultTypeDef(
    _ClientDescribeTaskExecutionResponseResultTypeDef
):
    pass


_ClientDescribeTaskExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": Literal[
            "QUEUED", "LAUNCHING", "PREPARING", "TRANSFERRING", "VERIFYING", "SUCCESS", "ERROR"
        ],
        "Options": ClientDescribeTaskExecutionResponseOptionsTypeDef,
        "Excludes": List[ClientDescribeTaskExecutionResponseExcludesTypeDef],
        "Includes": List[ClientDescribeTaskExecutionResponseIncludesTypeDef],
        "StartTime": datetime,
        "EstimatedFilesToTransfer": int,
        "EstimatedBytesToTransfer": int,
        "FilesTransferred": int,
        "BytesWritten": int,
        "BytesTransferred": int,
        "Result": ClientDescribeTaskExecutionResponseResultTypeDef,
    },
    total=False,
)


class ClientDescribeTaskExecutionResponseTypeDef(_ClientDescribeTaskExecutionResponseTypeDef):
    """
    - *(dict) --*

      DescribeTaskExecutionResponse
      - **TaskExecutionArn** *(string) --*

        The Amazon Resource Name (ARN) of the task execution that was described.
        ``TaskExecutionArn`` is hierarchical and includes ``TaskArn`` for the task that was
        executed.
        For example, a ``TaskExecution`` value with the ARN
        ``arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2/execution/exec-08ef1e88ec491019b``
        executed the task with the ARN
        ``arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2`` .
    """


_ClientDescribeTaskResponseExcludesTypeDef = TypedDict(
    "_ClientDescribeTaskResponseExcludesTypeDef", {"FilterType": str, "Value": str}, total=False
)


class ClientDescribeTaskResponseExcludesTypeDef(_ClientDescribeTaskResponseExcludesTypeDef):
    pass


_ClientDescribeTaskResponseOptionsTypeDef = TypedDict(
    "_ClientDescribeTaskResponseOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientDescribeTaskResponseOptionsTypeDef(_ClientDescribeTaskResponseOptionsTypeDef):
    pass


_ClientDescribeTaskResponseScheduleTypeDef = TypedDict(
    "_ClientDescribeTaskResponseScheduleTypeDef", {"ScheduleExpression": str}, total=False
)


class ClientDescribeTaskResponseScheduleTypeDef(_ClientDescribeTaskResponseScheduleTypeDef):
    pass


_ClientDescribeTaskResponseTypeDef = TypedDict(
    "_ClientDescribeTaskResponseTypeDef",
    {
        "TaskArn": str,
        "Status": Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"],
        "Name": str,
        "CurrentTaskExecutionArn": str,
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
        "CloudWatchLogGroupArn": str,
        "SourceNetworkInterfaceArns": List[str],
        "DestinationNetworkInterfaceArns": List[str],
        "Options": ClientDescribeTaskResponseOptionsTypeDef,
        "Excludes": List[ClientDescribeTaskResponseExcludesTypeDef],
        "Schedule": ClientDescribeTaskResponseScheduleTypeDef,
        "ErrorCode": str,
        "ErrorDetail": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeTaskResponseTypeDef(_ClientDescribeTaskResponseTypeDef):
    """
    - *(dict) --*

      DescribeTaskResponse
      - **TaskArn** *(string) --*

        The Amazon Resource Name (ARN) of the task that was described.
    """


_ClientListAgentsResponseAgentsTypeDef = TypedDict(
    "_ClientListAgentsResponseAgentsTypeDef",
    {"AgentArn": str, "Name": str, "Status": Literal["ONLINE", "OFFLINE"]},
    total=False,
)


class ClientListAgentsResponseAgentsTypeDef(_ClientListAgentsResponseAgentsTypeDef):
    """
    - *(dict) --*

      Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that
      contains a list of agents when the  ListAgents operation is called.
      - **AgentArn** *(string) --*

        The Amazon Resource Name (ARN) of the agent.
    """


_ClientListAgentsResponseTypeDef = TypedDict(
    "_ClientListAgentsResponseTypeDef",
    {"Agents": List[ClientListAgentsResponseAgentsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAgentsResponseTypeDef(_ClientListAgentsResponseTypeDef):
    """
    - *(dict) --*

      ListAgentsResponse
      - **Agents** *(list) --*

        A list of agents in your account.
        - *(dict) --*

          Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that
          contains a list of agents when the  ListAgents operation is called.
          - **AgentArn** *(string) --*

            The Amazon Resource Name (ARN) of the agent.
    """


_ClientListLocationsResponseLocationsTypeDef = TypedDict(
    "_ClientListLocationsResponseLocationsTypeDef",
    {"LocationArn": str, "LocationUri": str},
    total=False,
)


class ClientListLocationsResponseLocationsTypeDef(_ClientListLocationsResponseLocationsTypeDef):
    """
    - *(dict) --*

      Represents a single entry in a list of locations. ``LocationListEntry`` returns an array that
      contains a list of locations when the  ListLocations operation is called.
      - **LocationArn** *(string) --*

        The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon EFS,
        the location is the export path. For Amazon S3, the location is the prefix path that you
        want to mount and use as the root of the location.
    """


_ClientListLocationsResponseTypeDef = TypedDict(
    "_ClientListLocationsResponseTypeDef",
    {"Locations": List[ClientListLocationsResponseLocationsTypeDef], "NextToken": str},
    total=False,
)


class ClientListLocationsResponseTypeDef(_ClientListLocationsResponseTypeDef):
    """
    - *(dict) --*

      ListLocationsResponse
      - **Locations** *(list) --*

        An array that contains a list of locations.
        - *(dict) --*

          Represents a single entry in a list of locations. ``LocationListEntry`` returns an array
          that contains a list of locations when the  ListLocations operation is called.
          - **LocationArn** *(string) --*

            The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon
            EFS, the location is the export path. For Amazon S3, the location is the prefix path
            that you want to mount and use as the root of the location.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
      that contains a list of tasks when the  ListTagsForResource operation is called.
      - **Key** *(string) --*

        The key for an AWS resource tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      ListTagsForResourceResponse
      - **Tags** *(list) --*

        Array of resource tags.
        - *(dict) --*

          Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an
          array that contains a list of tasks when the  ListTagsForResource operation is called.
          - **Key** *(string) --*

            The key for an AWS resource tag.
    """


_ClientListTaskExecutionsResponseTaskExecutionsTypeDef = TypedDict(
    "_ClientListTaskExecutionsResponseTaskExecutionsTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": Literal[
            "QUEUED", "LAUNCHING", "PREPARING", "TRANSFERRING", "VERIFYING", "SUCCESS", "ERROR"
        ],
    },
    total=False,
)


class ClientListTaskExecutionsResponseTaskExecutionsTypeDef(
    _ClientListTaskExecutionsResponseTaskExecutionsTypeDef
):
    """
    - *(dict) --*

      Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns an
      array that contains a list of specific invocations of a task when  ListTaskExecutions
      operation is called.
      - **TaskExecutionArn** *(string) --*

        The Amazon Resource Name (ARN) of the task that was executed.
    """


_ClientListTaskExecutionsResponseTypeDef = TypedDict(
    "_ClientListTaskExecutionsResponseTypeDef",
    {
        "TaskExecutions": List[ClientListTaskExecutionsResponseTaskExecutionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTaskExecutionsResponseTypeDef(_ClientListTaskExecutionsResponseTypeDef):
    """
    - *(dict) --*

      ListTaskExecutionsResponse
      - **TaskExecutions** *(list) --*

        A list of executed tasks.
        - *(dict) --*

          Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns
          an array that contains a list of specific invocations of a task when  ListTaskExecutions
          operation is called.
          - **TaskExecutionArn** *(string) --*

            The Amazon Resource Name (ARN) of the task that was executed.
    """


_ClientListTasksResponseTasksTypeDef = TypedDict(
    "_ClientListTasksResponseTasksTypeDef",
    {
        "TaskArn": str,
        "Status": Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"],
        "Name": str,
    },
    total=False,
)


class ClientListTasksResponseTasksTypeDef(_ClientListTasksResponseTasksTypeDef):
    """
    - *(dict) --*

      Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that contains
      a list of tasks when the  ListTasks operation is called. A task includes the source and
      destination file systems to sync and the options to use for the tasks.
      - **TaskArn** *(string) --*

        The Amazon Resource Name (ARN) of the task.
    """


_ClientListTasksResponseTypeDef = TypedDict(
    "_ClientListTasksResponseTypeDef",
    {"Tasks": List[ClientListTasksResponseTasksTypeDef], "NextToken": str},
    total=False,
)


class ClientListTasksResponseTypeDef(_ClientListTasksResponseTypeDef):
    """
    - *(dict) --*

      ListTasksResponse
      - **Tasks** *(list) --*

        A list of all the tasks that are returned.
        - *(dict) --*

          Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that
          contains a list of tasks when the  ListTasks operation is called. A task includes the
          source and destination file systems to sync and the options to use for the tasks.
          - **TaskArn** *(string) --*

            The Amazon Resource Name (ARN) of the task.
    """


_ClientStartTaskExecutionIncludesTypeDef = TypedDict(
    "_ClientStartTaskExecutionIncludesTypeDef", {"FilterType": str, "Value": str}, total=False
)


class ClientStartTaskExecutionIncludesTypeDef(_ClientStartTaskExecutionIncludesTypeDef):
    """
    - *(dict) --*

      Specifies which files, folders and objects to include or exclude when transferring files from
      source to destination.
      - **FilterType** *(string) --*

        The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.
    """


_ClientStartTaskExecutionOverrideOptionsTypeDef = TypedDict(
    "_ClientStartTaskExecutionOverrideOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientStartTaskExecutionOverrideOptionsTypeDef(
    _ClientStartTaskExecutionOverrideOptionsTypeDef
):
    """
    Represents the options that are available to control the behavior of a  StartTaskExecution
    operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file
    permissions, and also overwriting files in the destination, data integrity verification, and so
    on.
    A task has a set of default options associated with it. If you don't specify an option in
    StartTaskExecution , the default value is used. You can override the defaults options on each
    task execution by specifying an overriding ``Options`` value to  StartTaskExecution .
    - **VerifyMode** *(string) --*

      A value that determines whether a data integrity verification should be performed at the end
      of a task execution after all data and metadata have been transferred.
      Default value: POINT_IN_TIME_CONSISTENT.
      POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
      ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.
      NONE: Skip verification.
    """


_ClientStartTaskExecutionResponseTypeDef = TypedDict(
    "_ClientStartTaskExecutionResponseTypeDef", {"TaskExecutionArn": str}, total=False
)


class ClientStartTaskExecutionResponseTypeDef(_ClientStartTaskExecutionResponseTypeDef):
    """
    - *(dict) --*

      StartTaskExecutionResponse
      - **TaskExecutionArn** *(string) --*

        The Amazon Resource Name (ARN) of the specific task execution that was started.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
      that contains a list of tasks when the  ListTagsForResource operation is called.
      - **Key** *(string) --***[REQUIRED]**

        The key for an AWS resource tag.
    """


_ClientUpdateTaskExcludesTypeDef = TypedDict(
    "_ClientUpdateTaskExcludesTypeDef", {"FilterType": str, "Value": str}, total=False
)


class ClientUpdateTaskExcludesTypeDef(_ClientUpdateTaskExcludesTypeDef):
    """
    - *(dict) --*

      Specifies which files, folders and objects to include or exclude when transferring files from
      source to destination.
      - **FilterType** *(string) --*

        The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.
    """


_ClientUpdateTaskOptionsTypeDef = TypedDict(
    "_ClientUpdateTaskOptionsTypeDef",
    {
        "VerifyMode": Literal["POINT_IN_TIME_CONSISTENT", "ONLY_FILES_TRANSFERRED", "NONE"],
        "OverwriteMode": Literal["ALWAYS", "NEVER"],
        "Atime": Literal["NONE", "BEST_EFFORT"],
        "Mtime": Literal["NONE", "PRESERVE"],
        "Uid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "Gid": Literal["NONE", "INT_VALUE", "NAME", "BOTH"],
        "PreserveDeletedFiles": Literal["PRESERVE", "REMOVE"],
        "PreserveDevices": Literal["NONE", "PRESERVE"],
        "PosixPermissions": Literal["NONE", "PRESERVE"],
        "BytesPerSecond": int,
        "TaskQueueing": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientUpdateTaskOptionsTypeDef(_ClientUpdateTaskOptionsTypeDef):
    """
    Represents the options that are available to control the behavior of a  StartTaskExecution
    operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file
    permissions, and also overwriting files in the destination, data integrity verification, and so
    on.
    A task has a set of default options associated with it. If you don't specify an option in
    StartTaskExecution , the default value is used. You can override the defaults options on each
    task execution by specifying an overriding ``Options`` value to  StartTaskExecution .
    - **VerifyMode** *(string) --*

      A value that determines whether a data integrity verification should be performed at the end
      of a task execution after all data and metadata have been transferred.
      Default value: POINT_IN_TIME_CONSISTENT.
      POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
      ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.
      NONE: Skip verification.
    """


_ClientUpdateTaskScheduleTypeDef = TypedDict(
    "_ClientUpdateTaskScheduleTypeDef", {"ScheduleExpression": str}
)


class ClientUpdateTaskScheduleTypeDef(_ClientUpdateTaskScheduleTypeDef):
    """
    Specifies a schedule used to periodically transfer files from a source to a destination
    location. You can configure your task to execute hourly, daily, weekly or on specific days of
    the week. You control when in the day or hour you want the task to execute. The time you specify
    is UTC time. For more information, see  task-scheduling .
    - **ScheduleExpression** *(string) --***[REQUIRED]**

      A cron expression that specifies when AWS DataSync initiates a scheduled transfer from a
      source to a destination location.
    """


_ListAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAgentsPaginatePaginationConfigTypeDef(_ListAgentsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAgentsPaginateResponseAgentsTypeDef = TypedDict(
    "_ListAgentsPaginateResponseAgentsTypeDef",
    {"AgentArn": str, "Name": str, "Status": Literal["ONLINE", "OFFLINE"]},
    total=False,
)


class ListAgentsPaginateResponseAgentsTypeDef(_ListAgentsPaginateResponseAgentsTypeDef):
    """
    - *(dict) --*

      Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that
      contains a list of agents when the  ListAgents operation is called.
      - **AgentArn** *(string) --*

        The Amazon Resource Name (ARN) of the agent.
    """


_ListAgentsPaginateResponseTypeDef = TypedDict(
    "_ListAgentsPaginateResponseTypeDef",
    {"Agents": List[ListAgentsPaginateResponseAgentsTypeDef]},
    total=False,
)


class ListAgentsPaginateResponseTypeDef(_ListAgentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      ListAgentsResponse
      - **Agents** *(list) --*

        A list of agents in your account.
        - *(dict) --*

          Represents a single entry in a list of agents. ``AgentListEntry`` returns an array that
          contains a list of agents when the  ListAgents operation is called.
          - **AgentArn** *(string) --*

            The Amazon Resource Name (ARN) of the agent.
    """


_ListLocationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLocationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLocationsPaginatePaginationConfigTypeDef(_ListLocationsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLocationsPaginateResponseLocationsTypeDef = TypedDict(
    "_ListLocationsPaginateResponseLocationsTypeDef",
    {"LocationArn": str, "LocationUri": str},
    total=False,
)


class ListLocationsPaginateResponseLocationsTypeDef(_ListLocationsPaginateResponseLocationsTypeDef):
    """
    - *(dict) --*

      Represents a single entry in a list of locations. ``LocationListEntry`` returns an array that
      contains a list of locations when the  ListLocations operation is called.
      - **LocationArn** *(string) --*

        The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon EFS,
        the location is the export path. For Amazon S3, the location is the prefix path that you
        want to mount and use as the root of the location.
    """


_ListLocationsPaginateResponseTypeDef = TypedDict(
    "_ListLocationsPaginateResponseTypeDef",
    {"Locations": List[ListLocationsPaginateResponseLocationsTypeDef]},
    total=False,
)


class ListLocationsPaginateResponseTypeDef(_ListLocationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      ListLocationsResponse
      - **Locations** *(list) --*

        An array that contains a list of locations.
        - *(dict) --*

          Represents a single entry in a list of locations. ``LocationListEntry`` returns an array
          that contains a list of locations when the  ListLocations operation is called.
          - **LocationArn** *(string) --*

            The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon
            EFS, the location is the export path. For Amazon S3, the location is the prefix path
            that you want to mount and use as the root of the location.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    - *(dict) --*

      Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an array
      that contains a list of tasks when the  ListTagsForResource operation is called.
      - **Key** *(string) --*

        The key for an AWS resource tag.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      ListTagsForResourceResponse
      - **Tags** *(list) --*

        Array of resource tags.
        - *(dict) --*

          Represents a single entry in a list of AWS resource tags. ``TagListEntry`` returns an
          array that contains a list of tasks when the  ListTagsForResource operation is called.
          - **Key** *(string) --*

            The key for an AWS resource tag.
    """


_ListTaskExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTaskExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTaskExecutionsPaginatePaginationConfigTypeDef(
    _ListTaskExecutionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef = TypedDict(
    "_ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": Literal[
            "QUEUED", "LAUNCHING", "PREPARING", "TRANSFERRING", "VERIFYING", "SUCCESS", "ERROR"
        ],
    },
    total=False,
)


class ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef(
    _ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef
):
    """
    - *(dict) --*

      Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns an
      array that contains a list of specific invocations of a task when  ListTaskExecutions
      operation is called.
      - **TaskExecutionArn** *(string) --*

        The Amazon Resource Name (ARN) of the task that was executed.
    """


_ListTaskExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListTaskExecutionsPaginateResponseTypeDef",
    {"TaskExecutions": List[ListTaskExecutionsPaginateResponseTaskExecutionsTypeDef]},
    total=False,
)


class ListTaskExecutionsPaginateResponseTypeDef(_ListTaskExecutionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      ListTaskExecutionsResponse
      - **TaskExecutions** *(list) --*

        A list of executed tasks.
        - *(dict) --*

          Represents a single entry in a list of task executions. ``TaskExecutionListEntry`` returns
          an array that contains a list of specific invocations of a task when  ListTaskExecutions
          operation is called.
          - **TaskExecutionArn** *(string) --*

            The Amazon Resource Name (ARN) of the task that was executed.
    """


_ListTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTasksPaginatePaginationConfigTypeDef(_ListTasksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTasksPaginateResponseTasksTypeDef = TypedDict(
    "_ListTasksPaginateResponseTasksTypeDef",
    {
        "TaskArn": str,
        "Status": Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"],
        "Name": str,
    },
    total=False,
)


class ListTasksPaginateResponseTasksTypeDef(_ListTasksPaginateResponseTasksTypeDef):
    """
    - *(dict) --*

      Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that contains
      a list of tasks when the  ListTasks operation is called. A task includes the source and
      destination file systems to sync and the options to use for the tasks.
      - **TaskArn** *(string) --*

        The Amazon Resource Name (ARN) of the task.
    """


_ListTasksPaginateResponseTypeDef = TypedDict(
    "_ListTasksPaginateResponseTypeDef",
    {"Tasks": List[ListTasksPaginateResponseTasksTypeDef]},
    total=False,
)


class ListTasksPaginateResponseTypeDef(_ListTasksPaginateResponseTypeDef):
    """
    - *(dict) --*

      ListTasksResponse
      - **Tasks** *(list) --*

        A list of all the tasks that are returned.
        - *(dict) --*

          Represents a single entry in a list of tasks. ``TaskListEntry`` returns an array that
          contains a list of tasks when the  ListTasks operation is called. A task includes the
          source and destination file systems to sync and the options to use for the tasks.
          - **TaskArn** *(string) --*

            The Amazon Resource Name (ARN) of the task.
    """
