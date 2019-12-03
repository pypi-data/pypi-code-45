"Main interface for sms service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateAppResponseappSummarylaunchDetailsTypeDef",
    "ClientCreateAppResponseappSummaryTypeDef",
    "ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    "ClientCreateAppResponseserverGroupsserverListvmServerTypeDef",
    "ClientCreateAppResponseserverGroupsserverListTypeDef",
    "ClientCreateAppResponseserverGroupsTypeDef",
    "ClientCreateAppResponsetagsTypeDef",
    "ClientCreateAppResponseTypeDef",
    "ClientCreateAppServerGroupsserverListvmServervmServerAddressTypeDef",
    "ClientCreateAppServerGroupsserverListvmServerTypeDef",
    "ClientCreateAppServerGroupsserverListTypeDef",
    "ClientCreateAppServerGroupsTypeDef",
    "ClientCreateAppTagsTypeDef",
    "ClientCreateReplicationJobResponseTypeDef",
    "ClientGenerateChangeSetResponses3LocationTypeDef",
    "ClientGenerateChangeSetResponseTypeDef",
    "ClientGenerateTemplateResponses3LocationTypeDef",
    "ClientGenerateTemplateResponseTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef",
    "ClientGetAppLaunchConfigurationResponseTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef",
    "ClientGetAppReplicationConfigurationResponseTypeDef",
    "ClientGetAppResponseappSummarylaunchDetailsTypeDef",
    "ClientGetAppResponseappSummaryTypeDef",
    "ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    "ClientGetAppResponseserverGroupsserverListvmServerTypeDef",
    "ClientGetAppResponseserverGroupsserverListTypeDef",
    "ClientGetAppResponseserverGroupsTypeDef",
    "ClientGetAppResponsetagsTypeDef",
    "ClientGetAppResponseTypeDef",
    "ClientGetConnectorsResponseconnectorListTypeDef",
    "ClientGetConnectorsResponseTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListTypeDef",
    "ClientGetReplicationJobsResponseTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobTypeDef",
    "ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef",
    "ClientGetReplicationRunsResponsereplicationRunListTypeDef",
    "ClientGetReplicationRunsResponseTypeDef",
    "ClientGetServersResponseserverListvmServervmServerAddressTypeDef",
    "ClientGetServersResponseserverListvmServerTypeDef",
    "ClientGetServersResponseserverListTypeDef",
    "ClientGetServersResponseTypeDef",
    "ClientGetServersVmServerAddressListTypeDef",
    "ClientListAppsResponseappslaunchDetailsTypeDef",
    "ClientListAppsResponseappsTypeDef",
    "ClientListAppsResponseTypeDef",
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef",
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef",
    "ClientStartOnDemandReplicationRunResponseTypeDef",
    "ClientUpdateAppResponseappSummarylaunchDetailsTypeDef",
    "ClientUpdateAppResponseappSummaryTypeDef",
    "ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    "ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef",
    "ClientUpdateAppResponseserverGroupsserverListTypeDef",
    "ClientUpdateAppResponseserverGroupsTypeDef",
    "ClientUpdateAppResponsetagsTypeDef",
    "ClientUpdateAppResponseTypeDef",
    "ClientUpdateAppServerGroupsserverListvmServervmServerAddressTypeDef",
    "ClientUpdateAppServerGroupsserverListvmServerTypeDef",
    "ClientUpdateAppServerGroupsserverListTypeDef",
    "ClientUpdateAppServerGroupsTypeDef",
    "ClientUpdateAppTagsTypeDef",
    "GetConnectorsPaginatePaginationConfigTypeDef",
    "GetConnectorsPaginateResponseconnectorListTypeDef",
    "GetConnectorsPaginateResponseTypeDef",
    "GetReplicationJobsPaginatePaginationConfigTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListTypeDef",
    "GetReplicationJobsPaginateResponseTypeDef",
    "GetReplicationRunsPaginatePaginationConfigTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobTypeDef",
    "GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef",
    "GetReplicationRunsPaginateResponsereplicationRunListTypeDef",
    "GetReplicationRunsPaginateResponseTypeDef",
    "GetServersPaginatePaginationConfigTypeDef",
    "GetServersPaginateResponseserverListvmServervmServerAddressTypeDef",
    "GetServersPaginateResponseserverListvmServerTypeDef",
    "GetServersPaginateResponseserverListTypeDef",
    "GetServersPaginateResponseTypeDef",
    "GetServersPaginateVmServerAddressListTypeDef",
    "ListAppsPaginatePaginationConfigTypeDef",
    "ListAppsPaginateResponseappslaunchDetailsTypeDef",
    "ListAppsPaginateResponseappsTypeDef",
    "ListAppsPaginateResponseTypeDef",
)


_ClientCreateAppResponseappSummarylaunchDetailsTypeDef = TypedDict(
    "_ClientCreateAppResponseappSummarylaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ClientCreateAppResponseappSummarylaunchDetailsTypeDef(
    _ClientCreateAppResponseappSummarylaunchDetailsTypeDef
):
    pass


_ClientCreateAppResponseappSummaryTypeDef = TypedDict(
    "_ClientCreateAppResponseappSummaryTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "DELETE_FAILED"],
        "statusMessage": str,
        "replicationStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_REPLICATION",
            "VALIDATION_IN_PROGRESS",
            "REPLICATION_PENDING",
            "REPLICATION_IN_PROGRESS",
            "REPLICATED",
            "DELTA_REPLICATION_IN_PROGRESS",
            "DELTA_REPLICATED",
            "DELTA_REPLICATION_FAILED",
            "REPLICATION_FAILED",
            "REPLICATION_STOPPING",
            "REPLICATION_STOP_FAILED",
            "REPLICATION_STOPPED",
        ],
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_LAUNCH",
            "VALIDATION_IN_PROGRESS",
            "LAUNCH_PENDING",
            "LAUNCH_IN_PROGRESS",
            "LAUNCHED",
            "DELTA_LAUNCH_IN_PROGRESS",
            "DELTA_LAUNCH_FAILED",
            "LAUNCH_FAILED",
            "TERMINATE_IN_PROGRESS",
            "TERMINATE_FAILED",
            "TERMINATED",
        ],
        "launchStatusMessage": str,
        "launchDetails": ClientCreateAppResponseappSummarylaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ClientCreateAppResponseappSummaryTypeDef(_ClientCreateAppResponseappSummaryTypeDef):
    """
    - **appSummary** *(dict) --*

      Summary description of the application.
      - **appId** *(string) --*

        Unique ID of the application.
    """


_ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef(
    _ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef
):
    pass


_ClientCreateAppResponseserverGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientCreateAppResponseserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientCreateAppResponseserverGroupsserverListvmServerTypeDef(
    _ClientCreateAppResponseserverGroupsserverListvmServerTypeDef
):
    pass


_ClientCreateAppResponseserverGroupsserverListTypeDef = TypedDict(
    "_ClientCreateAppResponseserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientCreateAppResponseserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientCreateAppResponseserverGroupsserverListTypeDef(
    _ClientCreateAppResponseserverGroupsserverListTypeDef
):
    pass


_ClientCreateAppResponseserverGroupsTypeDef = TypedDict(
    "_ClientCreateAppResponseserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientCreateAppResponseserverGroupsserverListTypeDef],
    },
    total=False,
)


class ClientCreateAppResponseserverGroupsTypeDef(_ClientCreateAppResponseserverGroupsTypeDef):
    pass


_ClientCreateAppResponsetagsTypeDef = TypedDict(
    "_ClientCreateAppResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateAppResponsetagsTypeDef(_ClientCreateAppResponsetagsTypeDef):
    pass


_ClientCreateAppResponseTypeDef = TypedDict(
    "_ClientCreateAppResponseTypeDef",
    {
        "appSummary": ClientCreateAppResponseappSummaryTypeDef,
        "serverGroups": List[ClientCreateAppResponseserverGroupsTypeDef],
        "tags": List[ClientCreateAppResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreateAppResponseTypeDef(_ClientCreateAppResponseTypeDef):
    """
    - *(dict) --*

      - **appSummary** *(dict) --*

        Summary description of the application.
        - **appId** *(string) --*

          Unique ID of the application.
    """


_ClientCreateAppServerGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientCreateAppServerGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientCreateAppServerGroupsserverListvmServervmServerAddressTypeDef(
    _ClientCreateAppServerGroupsserverListvmServervmServerAddressTypeDef
):
    pass


_ClientCreateAppServerGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientCreateAppServerGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientCreateAppServerGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientCreateAppServerGroupsserverListvmServerTypeDef(
    _ClientCreateAppServerGroupsserverListvmServerTypeDef
):
    pass


_ClientCreateAppServerGroupsserverListTypeDef = TypedDict(
    "_ClientCreateAppServerGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientCreateAppServerGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientCreateAppServerGroupsserverListTypeDef(_ClientCreateAppServerGroupsserverListTypeDef):
    pass


_ClientCreateAppServerGroupsTypeDef = TypedDict(
    "_ClientCreateAppServerGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientCreateAppServerGroupsserverListTypeDef],
    },
    total=False,
)


class ClientCreateAppServerGroupsTypeDef(_ClientCreateAppServerGroupsTypeDef):
    """
    - *(dict) --*

      A logical grouping of servers.
      - **serverGroupId** *(string) --*

        Identifier of a server group.
    """


_ClientCreateAppTagsTypeDef = TypedDict(
    "_ClientCreateAppTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateAppTagsTypeDef(_ClientCreateAppTagsTypeDef):
    """
    - *(dict) --*

      A label that can be assigned to an application.
      - **key** *(string) --*

        Tag key.
    """


_ClientCreateReplicationJobResponseTypeDef = TypedDict(
    "_ClientCreateReplicationJobResponseTypeDef", {"replicationJobId": str}, total=False
)


class ClientCreateReplicationJobResponseTypeDef(_ClientCreateReplicationJobResponseTypeDef):
    """
    - *(dict) --*

      - **replicationJobId** *(string) --*

        The unique identifier of the replication job.
    """


_ClientGenerateChangeSetResponses3LocationTypeDef = TypedDict(
    "_ClientGenerateChangeSetResponses3LocationTypeDef", {"bucket": str, "key": str}, total=False
)


class ClientGenerateChangeSetResponses3LocationTypeDef(
    _ClientGenerateChangeSetResponses3LocationTypeDef
):
    """
    - **s3Location** *(dict) --*

      Location of the Amazon S3 object.
      - **bucket** *(string) --*

        Amazon S3 bucket name.
    """


_ClientGenerateChangeSetResponseTypeDef = TypedDict(
    "_ClientGenerateChangeSetResponseTypeDef",
    {"s3Location": ClientGenerateChangeSetResponses3LocationTypeDef},
    total=False,
)


class ClientGenerateChangeSetResponseTypeDef(_ClientGenerateChangeSetResponseTypeDef):
    """
    - *(dict) --*

      - **s3Location** *(dict) --*

        Location of the Amazon S3 object.
        - **bucket** *(string) --*

          Amazon S3 bucket name.
    """


_ClientGenerateTemplateResponses3LocationTypeDef = TypedDict(
    "_ClientGenerateTemplateResponses3LocationTypeDef", {"bucket": str, "key": str}, total=False
)


class ClientGenerateTemplateResponses3LocationTypeDef(
    _ClientGenerateTemplateResponses3LocationTypeDef
):
    """
    - **s3Location** *(dict) --*

      Location of the Amazon S3 object.
      - **bucket** *(string) --*

        Amazon S3 bucket name.
    """


_ClientGenerateTemplateResponseTypeDef = TypedDict(
    "_ClientGenerateTemplateResponseTypeDef",
    {"s3Location": ClientGenerateTemplateResponses3LocationTypeDef},
    total=False,
)


class ClientGenerateTemplateResponseTypeDef(_ClientGenerateTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **s3Location** *(dict) --*

        Location of the Amazon S3 object.
        - **bucket** *(string) --*

          Amazon S3 bucket name.
    """


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef
):
    pass


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef
):
    pass


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef
):
    pass


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
):
    pass


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    {
        "s3Location": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef
):
    pass


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
    {
        "server": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef,
        "logicalId": str,
        "vpc": str,
        "subnet": str,
        "securityGroup": str,
        "ec2KeyName": str,
        "userData": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef,
        "instanceType": str,
        "associatePublicIpAddress": bool,
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
):
    pass


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List[
            ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef
):
    pass


_ClientGetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "serverGroupLaunchConfigurations": List[
            ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseTypeDef(
    _ClientGetAppLaunchConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **appId** *(string) --*

        ID of the application associated with the launch configuration.
    """


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
    {
        "seedTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "licenseType": Literal["AWS", "BYOL"],
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef
):
    pass


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef
):
    pass


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef
):
    pass


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef
):
    pass


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    {
        "server": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef,
        "serverReplicationParameters": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef,
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
):
    pass


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List[
            ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef
):
    """
    - *(dict) --*

      Replication configuration for a server group.
      - **serverGroupId** *(string) --*

        Identifier of the server group this replication configuration is associated with.
    """


_ClientGetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseTypeDef",
    {
        "serverGroupReplicationConfigurations": List[
            ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseTypeDef(
    _ClientGetAppReplicationConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **serverGroupReplicationConfigurations** *(list) --*

        Replication configurations associated with server groups in this application.
        - *(dict) --*

          Replication configuration for a server group.
          - **serverGroupId** *(string) --*

            Identifier of the server group this replication configuration is associated with.
    """


_ClientGetAppResponseappSummarylaunchDetailsTypeDef = TypedDict(
    "_ClientGetAppResponseappSummarylaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ClientGetAppResponseappSummarylaunchDetailsTypeDef(
    _ClientGetAppResponseappSummarylaunchDetailsTypeDef
):
    pass


_ClientGetAppResponseappSummaryTypeDef = TypedDict(
    "_ClientGetAppResponseappSummaryTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "DELETE_FAILED"],
        "statusMessage": str,
        "replicationStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_REPLICATION",
            "VALIDATION_IN_PROGRESS",
            "REPLICATION_PENDING",
            "REPLICATION_IN_PROGRESS",
            "REPLICATED",
            "DELTA_REPLICATION_IN_PROGRESS",
            "DELTA_REPLICATED",
            "DELTA_REPLICATION_FAILED",
            "REPLICATION_FAILED",
            "REPLICATION_STOPPING",
            "REPLICATION_STOP_FAILED",
            "REPLICATION_STOPPED",
        ],
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_LAUNCH",
            "VALIDATION_IN_PROGRESS",
            "LAUNCH_PENDING",
            "LAUNCH_IN_PROGRESS",
            "LAUNCHED",
            "DELTA_LAUNCH_IN_PROGRESS",
            "DELTA_LAUNCH_FAILED",
            "LAUNCH_FAILED",
            "TERMINATE_IN_PROGRESS",
            "TERMINATE_FAILED",
            "TERMINATED",
        ],
        "launchStatusMessage": str,
        "launchDetails": ClientGetAppResponseappSummarylaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ClientGetAppResponseappSummaryTypeDef(_ClientGetAppResponseappSummaryTypeDef):
    """
    - **appSummary** *(dict) --*

      Information about the application.
      - **appId** *(string) --*

        Unique ID of the application.
    """


_ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef(
    _ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef
):
    pass


_ClientGetAppResponseserverGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientGetAppResponseserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientGetAppResponseserverGroupsserverListvmServerTypeDef(
    _ClientGetAppResponseserverGroupsserverListvmServerTypeDef
):
    pass


_ClientGetAppResponseserverGroupsserverListTypeDef = TypedDict(
    "_ClientGetAppResponseserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetAppResponseserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientGetAppResponseserverGroupsserverListTypeDef(
    _ClientGetAppResponseserverGroupsserverListTypeDef
):
    pass


_ClientGetAppResponseserverGroupsTypeDef = TypedDict(
    "_ClientGetAppResponseserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientGetAppResponseserverGroupsserverListTypeDef],
    },
    total=False,
)


class ClientGetAppResponseserverGroupsTypeDef(_ClientGetAppResponseserverGroupsTypeDef):
    pass


_ClientGetAppResponsetagsTypeDef = TypedDict(
    "_ClientGetAppResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetAppResponsetagsTypeDef(_ClientGetAppResponsetagsTypeDef):
    pass


_ClientGetAppResponseTypeDef = TypedDict(
    "_ClientGetAppResponseTypeDef",
    {
        "appSummary": ClientGetAppResponseappSummaryTypeDef,
        "serverGroups": List[ClientGetAppResponseserverGroupsTypeDef],
        "tags": List[ClientGetAppResponsetagsTypeDef],
    },
    total=False,
)


class ClientGetAppResponseTypeDef(_ClientGetAppResponseTypeDef):
    """
    - *(dict) --*

      - **appSummary** *(dict) --*

        Information about the application.
        - **appId** *(string) --*

          Unique ID of the application.
    """


_ClientGetConnectorsResponseconnectorListTypeDef = TypedDict(
    "_ClientGetConnectorsResponseconnectorListTypeDef",
    {
        "connectorId": str,
        "version": str,
        "status": Literal["HEALTHY", "UNHEALTHY"],
        "capabilityList": List[Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER", "SNAPSHOT_BATCHING"]],
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmManagerId": str,
        "ipAddress": str,
        "macAddress": str,
        "associatedOn": datetime,
    },
    total=False,
)


class ClientGetConnectorsResponseconnectorListTypeDef(
    _ClientGetConnectorsResponseconnectorListTypeDef
):
    """
    - *(dict) --*

      Represents a connector.
      - **connectorId** *(string) --*

        The identifier of the connector.
    """


_ClientGetConnectorsResponseTypeDef = TypedDict(
    "_ClientGetConnectorsResponseTypeDef",
    {"connectorList": List[ClientGetConnectorsResponseconnectorListTypeDef], "nextToken": str},
    total=False,
)


class ClientGetConnectorsResponseTypeDef(_ClientGetConnectorsResponseTypeDef):
    """
    - *(dict) --*

      - **connectorList** *(list) --*

        Information about the registered connectors.
        - *(dict) --*

          Represents a connector.
          - **connectorId** *(string) --*

            The identifier of the connector.
    """


_ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef
):
    pass


_ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": Literal[
            "PENDING", "MISSED", "ACTIVE", "FAILED", "COMPLETED", "DELETING", "DELETED"
        ],
        "type": Literal["ON_DEMAND", "AUTOMATIC"],
        "stageDetails": ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef
):
    pass


_ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef
):
    pass


_ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef",
    {
        "vmServerAddress": ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef
):
    pass


_ClientGetReplicationJobsResponsereplicationJobListTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef,
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": Literal["AWS", "BYOL"],
        "roleName": str,
        "latestAmiId": str,
        "state": Literal[
            "PENDING",
            "ACTIVE",
            "FAILED",
            "DELETING",
            "DELETED",
            "COMPLETED",
            "PAUSED_ON_FAILURE",
            "FAILING",
        ],
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List[
            ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef
        ],
    },
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListTypeDef
):
    """
    - *(dict) --*

      Represents a replication job.
      - **replicationJobId** *(string) --*

        The identifier of the replication job.
    """


_ClientGetReplicationJobsResponseTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponseTypeDef",
    {
        "replicationJobList": List[ClientGetReplicationJobsResponsereplicationJobListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetReplicationJobsResponseTypeDef(_ClientGetReplicationJobsResponseTypeDef):
    """
    - *(dict) --*

      - **replicationJobList** *(list) --*

        Information about the replication jobs.
        - *(dict) --*

          Represents a replication job.
          - **replicationJobId** *(string) --*

            The identifier of the replication job.
    """


_ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef
):
    pass


_ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": Literal[
            "PENDING", "MISSED", "ACTIVE", "FAILED", "COMPLETED", "DELETING", "DELETED"
        ],
        "type": Literal["ON_DEMAND", "AUTOMATIC"],
        "stageDetails": ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef
):
    pass


_ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef
):
    pass


_ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef",
    {
        "vmServerAddress": ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef
):
    pass


_ClientGetReplicationRunsResponsereplicationJobTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef,
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": Literal["AWS", "BYOL"],
        "roleName": str,
        "latestAmiId": str,
        "state": Literal[
            "PENDING",
            "ACTIVE",
            "FAILED",
            "DELETING",
            "DELETED",
            "COMPLETED",
            "PAUSED_ON_FAILURE",
            "FAILING",
        ],
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List[
            ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef
        ],
    },
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobTypeDef
):
    """
    - **replicationJob** *(dict) --*

      Information about the replication job.
      - **replicationJobId** *(string) --*

        The identifier of the replication job.
    """


_ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef(
    _ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef
):
    pass


_ClientGetReplicationRunsResponsereplicationRunListTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": Literal[
            "PENDING", "MISSED", "ACTIVE", "FAILED", "COMPLETED", "DELETING", "DELETED"
        ],
        "type": Literal["ON_DEMAND", "AUTOMATIC"],
        "stageDetails": ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientGetReplicationRunsResponsereplicationRunListTypeDef(
    _ClientGetReplicationRunsResponsereplicationRunListTypeDef
):
    pass


_ClientGetReplicationRunsResponseTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponseTypeDef",
    {
        "replicationJob": ClientGetReplicationRunsResponsereplicationJobTypeDef,
        "replicationRunList": List[ClientGetReplicationRunsResponsereplicationRunListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetReplicationRunsResponseTypeDef(_ClientGetReplicationRunsResponseTypeDef):
    """
    - *(dict) --*

      - **replicationJob** *(dict) --*

        Information about the replication job.
        - **replicationJobId** *(string) --*

          The identifier of the replication job.
    """


_ClientGetServersResponseserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetServersResponseserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetServersResponseserverListvmServervmServerAddressTypeDef(
    _ClientGetServersResponseserverListvmServervmServerAddressTypeDef
):
    pass


_ClientGetServersResponseserverListvmServerTypeDef = TypedDict(
    "_ClientGetServersResponseserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientGetServersResponseserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientGetServersResponseserverListvmServerTypeDef(
    _ClientGetServersResponseserverListvmServerTypeDef
):
    pass


_ClientGetServersResponseserverListTypeDef = TypedDict(
    "_ClientGetServersResponseserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetServersResponseserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientGetServersResponseserverListTypeDef(_ClientGetServersResponseserverListTypeDef):
    pass


_ClientGetServersResponseTypeDef = TypedDict(
    "_ClientGetServersResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": Literal[
            "NOT_IMPORTED", "IMPORTING", "AVAILABLE", "DELETED", "EXPIRED"
        ],
        "serverList": List[ClientGetServersResponseserverListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetServersResponseTypeDef(_ClientGetServersResponseTypeDef):
    """
    - *(dict) --*

      - **lastModifiedOn** *(datetime) --*

        The time when the server was last modified.
    """


_ClientGetServersVmServerAddressListTypeDef = TypedDict(
    "_ClientGetServersVmServerAddressListTypeDef", {"vmManagerId": str, "vmId": str}, total=False
)


class ClientGetServersVmServerAddressListTypeDef(_ClientGetServersVmServerAddressListTypeDef):
    """
    - *(dict) --*

      Represents a VM server location.
      - **vmManagerId** *(string) --*

        The identifier of the VM manager.
    """


_ClientListAppsResponseappslaunchDetailsTypeDef = TypedDict(
    "_ClientListAppsResponseappslaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ClientListAppsResponseappslaunchDetailsTypeDef(
    _ClientListAppsResponseappslaunchDetailsTypeDef
):
    pass


_ClientListAppsResponseappsTypeDef = TypedDict(
    "_ClientListAppsResponseappsTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "DELETE_FAILED"],
        "statusMessage": str,
        "replicationStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_REPLICATION",
            "VALIDATION_IN_PROGRESS",
            "REPLICATION_PENDING",
            "REPLICATION_IN_PROGRESS",
            "REPLICATED",
            "DELTA_REPLICATION_IN_PROGRESS",
            "DELTA_REPLICATED",
            "DELTA_REPLICATION_FAILED",
            "REPLICATION_FAILED",
            "REPLICATION_STOPPING",
            "REPLICATION_STOP_FAILED",
            "REPLICATION_STOPPED",
        ],
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_LAUNCH",
            "VALIDATION_IN_PROGRESS",
            "LAUNCH_PENDING",
            "LAUNCH_IN_PROGRESS",
            "LAUNCHED",
            "DELTA_LAUNCH_IN_PROGRESS",
            "DELTA_LAUNCH_FAILED",
            "LAUNCH_FAILED",
            "TERMINATE_IN_PROGRESS",
            "TERMINATE_FAILED",
            "TERMINATED",
        ],
        "launchStatusMessage": str,
        "launchDetails": ClientListAppsResponseappslaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ClientListAppsResponseappsTypeDef(_ClientListAppsResponseappsTypeDef):
    """
    - *(dict) --*

      Information about the application.
      - **appId** *(string) --*

        Unique ID of the application.
    """


_ClientListAppsResponseTypeDef = TypedDict(
    "_ClientListAppsResponseTypeDef",
    {"apps": List[ClientListAppsResponseappsTypeDef], "nextToken": str},
    total=False,
)


class ClientListAppsResponseTypeDef(_ClientListAppsResponseTypeDef):
    """
    - *(dict) --*

      - **apps** *(list) --*

        A list of application summaries.
        - *(dict) --*

          Information about the application.
          - **appId** *(string) --*

            Unique ID of the application.
    """


_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef(
    _ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef
):
    pass


_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef(
    _ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef
):
    pass


_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef(
    _ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef
):
    pass


_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef(
    _ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
):
    pass


_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    {
        "s3Location": ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
    },
    total=False,
)


class ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef(
    _ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef
):
    pass


_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
    {
        "server": ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef,
        "logicalId": str,
        "vpc": str,
        "subnet": str,
        "securityGroup": str,
        "ec2KeyName": str,
        "userData": ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef,
        "instanceType": str,
        "associatePublicIpAddress": bool,
    },
    total=False,
)


class ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef(
    _ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
):
    pass


_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List[
            ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef(
    _ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef
):
    """
    - *(dict) --*

      Launch configuration for a server group.
      - **serverGroupId** *(string) --*

        Identifier of the server group the launch configuration is associated with.
    """


_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
    {
        "seedTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "licenseType": Literal["AWS", "BYOL"],
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef(
    _ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef
):
    pass


_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef(
    _ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef
):
    pass


_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef(
    _ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef
):
    pass


_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef(
    _ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef
):
    pass


_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    {
        "server": ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef,
        "serverReplicationParameters": ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef,
    },
    total=False,
)


class ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef(
    _ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
):
    pass


_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List[
            ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef(
    _ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef
):
    """
    - *(dict) --*

      Replication configuration for a server group.
      - **serverGroupId** *(string) --*

        Identifier of the server group this replication configuration is associated with.
    """


_ClientStartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "_ClientStartOnDemandReplicationRunResponseTypeDef", {"replicationRunId": str}, total=False
)


class ClientStartOnDemandReplicationRunResponseTypeDef(
    _ClientStartOnDemandReplicationRunResponseTypeDef
):
    """
    - *(dict) --*

      - **replicationRunId** *(string) --*

        The identifier of the replication run.
    """


_ClientUpdateAppResponseappSummarylaunchDetailsTypeDef = TypedDict(
    "_ClientUpdateAppResponseappSummarylaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ClientUpdateAppResponseappSummarylaunchDetailsTypeDef(
    _ClientUpdateAppResponseappSummarylaunchDetailsTypeDef
):
    pass


_ClientUpdateAppResponseappSummaryTypeDef = TypedDict(
    "_ClientUpdateAppResponseappSummaryTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "DELETE_FAILED"],
        "statusMessage": str,
        "replicationStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_REPLICATION",
            "VALIDATION_IN_PROGRESS",
            "REPLICATION_PENDING",
            "REPLICATION_IN_PROGRESS",
            "REPLICATED",
            "DELTA_REPLICATION_IN_PROGRESS",
            "DELTA_REPLICATED",
            "DELTA_REPLICATION_FAILED",
            "REPLICATION_FAILED",
            "REPLICATION_STOPPING",
            "REPLICATION_STOP_FAILED",
            "REPLICATION_STOPPED",
        ],
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_LAUNCH",
            "VALIDATION_IN_PROGRESS",
            "LAUNCH_PENDING",
            "LAUNCH_IN_PROGRESS",
            "LAUNCHED",
            "DELTA_LAUNCH_IN_PROGRESS",
            "DELTA_LAUNCH_FAILED",
            "LAUNCH_FAILED",
            "TERMINATE_IN_PROGRESS",
            "TERMINATE_FAILED",
            "TERMINATED",
        ],
        "launchStatusMessage": str,
        "launchDetails": ClientUpdateAppResponseappSummarylaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ClientUpdateAppResponseappSummaryTypeDef(_ClientUpdateAppResponseappSummaryTypeDef):
    """
    - **appSummary** *(dict) --*

      Summary description of the application.
      - **appId** *(string) --*

        Unique ID of the application.
    """


_ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef(
    _ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef
):
    pass


_ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef(
    _ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef
):
    pass


_ClientUpdateAppResponseserverGroupsserverListTypeDef = TypedDict(
    "_ClientUpdateAppResponseserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientUpdateAppResponseserverGroupsserverListTypeDef(
    _ClientUpdateAppResponseserverGroupsserverListTypeDef
):
    pass


_ClientUpdateAppResponseserverGroupsTypeDef = TypedDict(
    "_ClientUpdateAppResponseserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientUpdateAppResponseserverGroupsserverListTypeDef],
    },
    total=False,
)


class ClientUpdateAppResponseserverGroupsTypeDef(_ClientUpdateAppResponseserverGroupsTypeDef):
    pass


_ClientUpdateAppResponsetagsTypeDef = TypedDict(
    "_ClientUpdateAppResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateAppResponsetagsTypeDef(_ClientUpdateAppResponsetagsTypeDef):
    pass


_ClientUpdateAppResponseTypeDef = TypedDict(
    "_ClientUpdateAppResponseTypeDef",
    {
        "appSummary": ClientUpdateAppResponseappSummaryTypeDef,
        "serverGroups": List[ClientUpdateAppResponseserverGroupsTypeDef],
        "tags": List[ClientUpdateAppResponsetagsTypeDef],
    },
    total=False,
)


class ClientUpdateAppResponseTypeDef(_ClientUpdateAppResponseTypeDef):
    """
    - *(dict) --*

      - **appSummary** *(dict) --*

        Summary description of the application.
        - **appId** *(string) --*

          Unique ID of the application.
    """


_ClientUpdateAppServerGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientUpdateAppServerGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientUpdateAppServerGroupsserverListvmServervmServerAddressTypeDef(
    _ClientUpdateAppServerGroupsserverListvmServervmServerAddressTypeDef
):
    pass


_ClientUpdateAppServerGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientUpdateAppServerGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientUpdateAppServerGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class ClientUpdateAppServerGroupsserverListvmServerTypeDef(
    _ClientUpdateAppServerGroupsserverListvmServerTypeDef
):
    pass


_ClientUpdateAppServerGroupsserverListTypeDef = TypedDict(
    "_ClientUpdateAppServerGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientUpdateAppServerGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientUpdateAppServerGroupsserverListTypeDef(_ClientUpdateAppServerGroupsserverListTypeDef):
    pass


_ClientUpdateAppServerGroupsTypeDef = TypedDict(
    "_ClientUpdateAppServerGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientUpdateAppServerGroupsserverListTypeDef],
    },
    total=False,
)


class ClientUpdateAppServerGroupsTypeDef(_ClientUpdateAppServerGroupsTypeDef):
    """
    - *(dict) --*

      A logical grouping of servers.
      - **serverGroupId** *(string) --*

        Identifier of a server group.
    """


_ClientUpdateAppTagsTypeDef = TypedDict(
    "_ClientUpdateAppTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateAppTagsTypeDef(_ClientUpdateAppTagsTypeDef):
    """
    - *(dict) --*

      A label that can be assigned to an application.
      - **key** *(string) --*

        Tag key.
    """


_GetConnectorsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetConnectorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetConnectorsPaginatePaginationConfigTypeDef(_GetConnectorsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetConnectorsPaginateResponseconnectorListTypeDef = TypedDict(
    "_GetConnectorsPaginateResponseconnectorListTypeDef",
    {
        "connectorId": str,
        "version": str,
        "status": Literal["HEALTHY", "UNHEALTHY"],
        "capabilityList": List[Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER", "SNAPSHOT_BATCHING"]],
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmManagerId": str,
        "ipAddress": str,
        "macAddress": str,
        "associatedOn": datetime,
    },
    total=False,
)


class GetConnectorsPaginateResponseconnectorListTypeDef(
    _GetConnectorsPaginateResponseconnectorListTypeDef
):
    """
    - *(dict) --*

      Represents a connector.
      - **connectorId** *(string) --*

        The identifier of the connector.
    """


_GetConnectorsPaginateResponseTypeDef = TypedDict(
    "_GetConnectorsPaginateResponseTypeDef",
    {"connectorList": List[GetConnectorsPaginateResponseconnectorListTypeDef], "NextToken": str},
    total=False,
)


class GetConnectorsPaginateResponseTypeDef(_GetConnectorsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **connectorList** *(list) --*

        Information about the registered connectors.
        - *(dict) --*

          Represents a connector.
          - **connectorId** *(string) --*

            The identifier of the connector.
    """


_GetReplicationJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetReplicationJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetReplicationJobsPaginatePaginationConfigTypeDef(
    _GetReplicationJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef
):
    pass


_GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": Literal[
            "PENDING", "MISSED", "ACTIVE", "FAILED", "COMPLETED", "DELETING", "DELETED"
        ],
        "type": Literal["ON_DEMAND", "AUTOMATIC"],
        "stageDetails": GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef
):
    pass


_GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef
):
    pass


_GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef",
    {
        "vmServerAddress": GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef
):
    pass


_GetReplicationJobsPaginateResponsereplicationJobListTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": str,
        "vmServer": GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef,
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": Literal["AWS", "BYOL"],
        "roleName": str,
        "latestAmiId": str,
        "state": Literal[
            "PENDING",
            "ACTIVE",
            "FAILED",
            "DELETING",
            "DELETED",
            "COMPLETED",
            "PAUSED_ON_FAILURE",
            "FAILING",
        ],
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List[
            GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef
        ],
    },
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListTypeDef
):
    """
    - *(dict) --*

      Represents a replication job.
      - **replicationJobId** *(string) --*

        The identifier of the replication job.
    """


_GetReplicationJobsPaginateResponseTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponseTypeDef",
    {
        "replicationJobList": List[GetReplicationJobsPaginateResponsereplicationJobListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetReplicationJobsPaginateResponseTypeDef(_GetReplicationJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **replicationJobList** *(list) --*

        Information about the replication jobs.
        - *(dict) --*

          Represents a replication job.
          - **replicationJobId** *(string) --*

            The identifier of the replication job.
    """


_GetReplicationRunsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetReplicationRunsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetReplicationRunsPaginatePaginationConfigTypeDef(
    _GetReplicationRunsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef
):
    pass


_GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": Literal[
            "PENDING", "MISSED", "ACTIVE", "FAILED", "COMPLETED", "DELETING", "DELETED"
        ],
        "type": Literal["ON_DEMAND", "AUTOMATIC"],
        "stageDetails": GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef
):
    pass


_GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef
):
    pass


_GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef",
    {
        "vmServerAddress": GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef
):
    pass


_GetReplicationRunsPaginateResponsereplicationJobTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": str,
        "vmServer": GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef,
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": Literal["AWS", "BYOL"],
        "roleName": str,
        "latestAmiId": str,
        "state": Literal[
            "PENDING",
            "ACTIVE",
            "FAILED",
            "DELETING",
            "DELETED",
            "COMPLETED",
            "PAUSED_ON_FAILURE",
            "FAILING",
        ],
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List[
            GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef
        ],
    },
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobTypeDef
):
    """
    - **replicationJob** *(dict) --*

      Information about the replication job.
      - **replicationJobId** *(string) --*

        The identifier of the replication job.
    """


_GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef(
    _GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef
):
    pass


_GetReplicationRunsPaginateResponsereplicationRunListTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": Literal[
            "PENDING", "MISSED", "ACTIVE", "FAILED", "COMPLETED", "DELETING", "DELETED"
        ],
        "type": Literal["ON_DEMAND", "AUTOMATIC"],
        "stageDetails": GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationRunListTypeDef(
    _GetReplicationRunsPaginateResponsereplicationRunListTypeDef
):
    pass


_GetReplicationRunsPaginateResponseTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponseTypeDef",
    {
        "replicationJob": GetReplicationRunsPaginateResponsereplicationJobTypeDef,
        "replicationRunList": List[GetReplicationRunsPaginateResponsereplicationRunListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetReplicationRunsPaginateResponseTypeDef(_GetReplicationRunsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **replicationJob** *(dict) --*

        Information about the replication job.
        - **replicationJobId** *(string) --*

          The identifier of the replication job.
    """


_GetServersPaginatePaginationConfigTypeDef = TypedDict(
    "_GetServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetServersPaginatePaginationConfigTypeDef(_GetServersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetServersPaginateResponseserverListvmServervmServerAddressTypeDef = TypedDict(
    "_GetServersPaginateResponseserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class GetServersPaginateResponseserverListvmServervmServerAddressTypeDef(
    _GetServersPaginateResponseserverListvmServervmServerAddressTypeDef
):
    pass


_GetServersPaginateResponseserverListvmServerTypeDef = TypedDict(
    "_GetServersPaginateResponseserverListvmServerTypeDef",
    {
        "vmServerAddress": GetServersPaginateResponseserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)


class GetServersPaginateResponseserverListvmServerTypeDef(
    _GetServersPaginateResponseserverListvmServerTypeDef
):
    pass


_GetServersPaginateResponseserverListTypeDef = TypedDict(
    "_GetServersPaginateResponseserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": GetServersPaginateResponseserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class GetServersPaginateResponseserverListTypeDef(_GetServersPaginateResponseserverListTypeDef):
    pass


_GetServersPaginateResponseTypeDef = TypedDict(
    "_GetServersPaginateResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": Literal[
            "NOT_IMPORTED", "IMPORTING", "AVAILABLE", "DELETED", "EXPIRED"
        ],
        "serverList": List[GetServersPaginateResponseserverListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetServersPaginateResponseTypeDef(_GetServersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **lastModifiedOn** *(datetime) --*

        The time when the server was last modified.
    """


_GetServersPaginateVmServerAddressListTypeDef = TypedDict(
    "_GetServersPaginateVmServerAddressListTypeDef", {"vmManagerId": str, "vmId": str}, total=False
)


class GetServersPaginateVmServerAddressListTypeDef(_GetServersPaginateVmServerAddressListTypeDef):
    """
    - *(dict) --*

      Represents a VM server location.
      - **vmManagerId** *(string) --*

        The identifier of the VM manager.
    """


_ListAppsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAppsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAppsPaginatePaginationConfigTypeDef(_ListAppsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAppsPaginateResponseappslaunchDetailsTypeDef = TypedDict(
    "_ListAppsPaginateResponseappslaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ListAppsPaginateResponseappslaunchDetailsTypeDef(
    _ListAppsPaginateResponseappslaunchDetailsTypeDef
):
    pass


_ListAppsPaginateResponseappsTypeDef = TypedDict(
    "_ListAppsPaginateResponseappsTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "DELETE_FAILED"],
        "statusMessage": str,
        "replicationStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_REPLICATION",
            "VALIDATION_IN_PROGRESS",
            "REPLICATION_PENDING",
            "REPLICATION_IN_PROGRESS",
            "REPLICATED",
            "DELTA_REPLICATION_IN_PROGRESS",
            "DELTA_REPLICATED",
            "DELTA_REPLICATION_FAILED",
            "REPLICATION_FAILED",
            "REPLICATION_STOPPING",
            "REPLICATION_STOP_FAILED",
            "REPLICATION_STOPPED",
        ],
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_LAUNCH",
            "VALIDATION_IN_PROGRESS",
            "LAUNCH_PENDING",
            "LAUNCH_IN_PROGRESS",
            "LAUNCHED",
            "DELTA_LAUNCH_IN_PROGRESS",
            "DELTA_LAUNCH_FAILED",
            "LAUNCH_FAILED",
            "TERMINATE_IN_PROGRESS",
            "TERMINATE_FAILED",
            "TERMINATED",
        ],
        "launchStatusMessage": str,
        "launchDetails": ListAppsPaginateResponseappslaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ListAppsPaginateResponseappsTypeDef(_ListAppsPaginateResponseappsTypeDef):
    """
    - *(dict) --*

      Information about the application.
      - **appId** *(string) --*

        Unique ID of the application.
    """


_ListAppsPaginateResponseTypeDef = TypedDict(
    "_ListAppsPaginateResponseTypeDef",
    {"apps": List[ListAppsPaginateResponseappsTypeDef], "NextToken": str},
    total=False,
)


class ListAppsPaginateResponseTypeDef(_ListAppsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **apps** *(list) --*

        A list of application summaries.
        - *(dict) --*

          Information about the application.
          - **appId** *(string) --*

            Unique ID of the application.
    """
