"Main interface for sms service type defs"
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


ClientCreateAppResponseappSummarylaunchDetailsTypeDef = TypedDict(
    "ClientCreateAppResponseappSummarylaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)

ClientCreateAppResponseappSummaryTypeDef = TypedDict(
    "ClientCreateAppResponseappSummaryTypeDef",
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

ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientCreateAppResponseserverGroupsserverListvmServerTypeDef = TypedDict(
    "ClientCreateAppResponseserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientCreateAppResponseserverGroupsserverListTypeDef = TypedDict(
    "ClientCreateAppResponseserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientCreateAppResponseserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientCreateAppResponseserverGroupsTypeDef = TypedDict(
    "ClientCreateAppResponseserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientCreateAppResponseserverGroupsserverListTypeDef],
    },
    total=False,
)

ClientCreateAppResponsetagsTypeDef = TypedDict(
    "ClientCreateAppResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateAppResponseTypeDef = TypedDict(
    "ClientCreateAppResponseTypeDef",
    {
        "appSummary": ClientCreateAppResponseappSummaryTypeDef,
        "serverGroups": List[ClientCreateAppResponseserverGroupsTypeDef],
        "tags": List[ClientCreateAppResponsetagsTypeDef],
    },
    total=False,
)

ClientCreateAppServerGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "ClientCreateAppServerGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientCreateAppServerGroupsserverListvmServerTypeDef = TypedDict(
    "ClientCreateAppServerGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientCreateAppServerGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientCreateAppServerGroupsserverListTypeDef = TypedDict(
    "ClientCreateAppServerGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientCreateAppServerGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientCreateAppServerGroupsTypeDef = TypedDict(
    "ClientCreateAppServerGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientCreateAppServerGroupsserverListTypeDef],
    },
    total=False,
)

ClientCreateAppTagsTypeDef = TypedDict(
    "ClientCreateAppTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateReplicationJobResponseTypeDef = TypedDict(
    "ClientCreateReplicationJobResponseTypeDef", {"replicationJobId": str}, total=False
)

ClientGenerateChangeSetResponses3LocationTypeDef = TypedDict(
    "ClientGenerateChangeSetResponses3LocationTypeDef", {"bucket": str, "key": str}, total=False
)

ClientGenerateChangeSetResponseTypeDef = TypedDict(
    "ClientGenerateChangeSetResponseTypeDef",
    {"s3Location": ClientGenerateChangeSetResponses3LocationTypeDef},
    total=False,
)

ClientGenerateTemplateResponses3LocationTypeDef = TypedDict(
    "ClientGenerateTemplateResponses3LocationTypeDef", {"bucket": str, "key": str}, total=False
)

ClientGenerateTemplateResponseTypeDef = TypedDict(
    "ClientGenerateTemplateResponseTypeDef",
    {"s3Location": ClientGenerateTemplateResponses3LocationTypeDef},
    total=False,
)

ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef = TypedDict(
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef = TypedDict(
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef = TypedDict(
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)

ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef = TypedDict(
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    {
        "s3Location": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
    },
    total=False,
)

ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef = TypedDict(
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
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

ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef = TypedDict(
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List[
            ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientGetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "ClientGetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "serverGroupLaunchConfigurations": List[
            ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef = TypedDict(
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
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

ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef = TypedDict(
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef = TypedDict(
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef = TypedDict(
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    {
        "server": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef,
        "serverReplicationParameters": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef,
    },
    total=False,
)

ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef = TypedDict(
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List[
            ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientGetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "ClientGetAppReplicationConfigurationResponseTypeDef",
    {
        "serverGroupReplicationConfigurations": List[
            ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef
        ]
    },
    total=False,
)

ClientGetAppResponseappSummarylaunchDetailsTypeDef = TypedDict(
    "ClientGetAppResponseappSummarylaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)

ClientGetAppResponseappSummaryTypeDef = TypedDict(
    "ClientGetAppResponseappSummaryTypeDef",
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

ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientGetAppResponseserverGroupsserverListvmServerTypeDef = TypedDict(
    "ClientGetAppResponseserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientGetAppResponseserverGroupsserverListTypeDef = TypedDict(
    "ClientGetAppResponseserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetAppResponseserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientGetAppResponseserverGroupsTypeDef = TypedDict(
    "ClientGetAppResponseserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientGetAppResponseserverGroupsserverListTypeDef],
    },
    total=False,
)

ClientGetAppResponsetagsTypeDef = TypedDict(
    "ClientGetAppResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientGetAppResponseTypeDef = TypedDict(
    "ClientGetAppResponseTypeDef",
    {
        "appSummary": ClientGetAppResponseappSummaryTypeDef,
        "serverGroups": List[ClientGetAppResponseserverGroupsTypeDef],
        "tags": List[ClientGetAppResponsetagsTypeDef],
    },
    total=False,
)

ClientGetConnectorsResponseconnectorListTypeDef = TypedDict(
    "ClientGetConnectorsResponseconnectorListTypeDef",
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

ClientGetConnectorsResponseTypeDef = TypedDict(
    "ClientGetConnectorsResponseTypeDef",
    {"connectorList": List[ClientGetConnectorsResponseconnectorListTypeDef], "nextToken": str},
    total=False,
)

ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef = TypedDict(
    "ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)

ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef = TypedDict(
    "ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef",
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

ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef = TypedDict(
    "ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef = TypedDict(
    "ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef",
    {
        "vmServerAddress": ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientGetReplicationJobsResponsereplicationJobListTypeDef = TypedDict(
    "ClientGetReplicationJobsResponsereplicationJobListTypeDef",
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

ClientGetReplicationJobsResponseTypeDef = TypedDict(
    "ClientGetReplicationJobsResponseTypeDef",
    {
        "replicationJobList": List[ClientGetReplicationJobsResponsereplicationJobListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef = TypedDict(
    "ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)

ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef = TypedDict(
    "ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef",
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

ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef = TypedDict(
    "ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef = TypedDict(
    "ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef",
    {
        "vmServerAddress": ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientGetReplicationRunsResponsereplicationJobTypeDef = TypedDict(
    "ClientGetReplicationRunsResponsereplicationJobTypeDef",
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

ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef = TypedDict(
    "ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)

ClientGetReplicationRunsResponsereplicationRunListTypeDef = TypedDict(
    "ClientGetReplicationRunsResponsereplicationRunListTypeDef",
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

ClientGetReplicationRunsResponseTypeDef = TypedDict(
    "ClientGetReplicationRunsResponseTypeDef",
    {
        "replicationJob": ClientGetReplicationRunsResponsereplicationJobTypeDef,
        "replicationRunList": List[ClientGetReplicationRunsResponsereplicationRunListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetServersResponseserverListvmServervmServerAddressTypeDef = TypedDict(
    "ClientGetServersResponseserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientGetServersResponseserverListvmServerTypeDef = TypedDict(
    "ClientGetServersResponseserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientGetServersResponseserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientGetServersResponseserverListTypeDef = TypedDict(
    "ClientGetServersResponseserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetServersResponseserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientGetServersResponseTypeDef = TypedDict(
    "ClientGetServersResponseTypeDef",
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

ClientGetServersVmServerAddressListTypeDef = TypedDict(
    "ClientGetServersVmServerAddressListTypeDef", {"vmManagerId": str, "vmId": str}, total=False
)

ClientListAppsResponseappslaunchDetailsTypeDef = TypedDict(
    "ClientListAppsResponseappslaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)

ClientListAppsResponseappsTypeDef = TypedDict(
    "ClientListAppsResponseappsTypeDef",
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

ClientListAppsResponseTypeDef = TypedDict(
    "ClientListAppsResponseTypeDef",
    {"apps": List[ClientListAppsResponseappsTypeDef], "nextToken": str},
    total=False,
)

ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef = TypedDict(
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef = TypedDict(
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef = TypedDict(
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)

ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef = TypedDict(
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    {
        "s3Location": ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
    },
    total=False,
)

ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef = TypedDict(
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
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

ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef = TypedDict(
    "ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List[
            ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef = TypedDict(
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
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

ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef = TypedDict(
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef = TypedDict(
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef = TypedDict(
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    {
        "server": ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef,
        "serverReplicationParameters": ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef,
    },
    total=False,
)

ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef = TypedDict(
    "ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List[
            ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientStartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "ClientStartOnDemandReplicationRunResponseTypeDef", {"replicationRunId": str}, total=False
)

ClientUpdateAppResponseappSummarylaunchDetailsTypeDef = TypedDict(
    "ClientUpdateAppResponseappSummarylaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)

ClientUpdateAppResponseappSummaryTypeDef = TypedDict(
    "ClientUpdateAppResponseappSummaryTypeDef",
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

ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef = TypedDict(
    "ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientUpdateAppResponseserverGroupsserverListTypeDef = TypedDict(
    "ClientUpdateAppResponseserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientUpdateAppResponseserverGroupsTypeDef = TypedDict(
    "ClientUpdateAppResponseserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientUpdateAppResponseserverGroupsserverListTypeDef],
    },
    total=False,
)

ClientUpdateAppResponsetagsTypeDef = TypedDict(
    "ClientUpdateAppResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateAppResponseTypeDef = TypedDict(
    "ClientUpdateAppResponseTypeDef",
    {
        "appSummary": ClientUpdateAppResponseappSummaryTypeDef,
        "serverGroups": List[ClientUpdateAppResponseserverGroupsTypeDef],
        "tags": List[ClientUpdateAppResponsetagsTypeDef],
    },
    total=False,
)

ClientUpdateAppServerGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "ClientUpdateAppServerGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

ClientUpdateAppServerGroupsserverListvmServerTypeDef = TypedDict(
    "ClientUpdateAppServerGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientUpdateAppServerGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

ClientUpdateAppServerGroupsserverListTypeDef = TypedDict(
    "ClientUpdateAppServerGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientUpdateAppServerGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ClientUpdateAppServerGroupsTypeDef = TypedDict(
    "ClientUpdateAppServerGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientUpdateAppServerGroupsserverListTypeDef],
    },
    total=False,
)

ClientUpdateAppTagsTypeDef = TypedDict(
    "ClientUpdateAppTagsTypeDef", {"key": str, "value": str}, total=False
)

GetConnectorsPaginatePaginationConfigTypeDef = TypedDict(
    "GetConnectorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetConnectorsPaginateResponseconnectorListTypeDef = TypedDict(
    "GetConnectorsPaginateResponseconnectorListTypeDef",
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

GetConnectorsPaginateResponseTypeDef = TypedDict(
    "GetConnectorsPaginateResponseTypeDef",
    {"connectorList": List[GetConnectorsPaginateResponseconnectorListTypeDef], "NextToken": str},
    total=False,
)

GetReplicationJobsPaginatePaginationConfigTypeDef = TypedDict(
    "GetReplicationJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef = TypedDict(
    "GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)

GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef = TypedDict(
    "GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef",
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

GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef = TypedDict(
    "GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef = TypedDict(
    "GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef",
    {
        "vmServerAddress": GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

GetReplicationJobsPaginateResponsereplicationJobListTypeDef = TypedDict(
    "GetReplicationJobsPaginateResponsereplicationJobListTypeDef",
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

GetReplicationJobsPaginateResponseTypeDef = TypedDict(
    "GetReplicationJobsPaginateResponseTypeDef",
    {
        "replicationJobList": List[GetReplicationJobsPaginateResponsereplicationJobListTypeDef],
        "NextToken": str,
    },
    total=False,
)

GetReplicationRunsPaginatePaginationConfigTypeDef = TypedDict(
    "GetReplicationRunsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef = TypedDict(
    "GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)

GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef = TypedDict(
    "GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef",
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

GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef = TypedDict(
    "GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef = TypedDict(
    "GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef",
    {
        "vmServerAddress": GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

GetReplicationRunsPaginateResponsereplicationJobTypeDef = TypedDict(
    "GetReplicationRunsPaginateResponsereplicationJobTypeDef",
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

GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef = TypedDict(
    "GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)

GetReplicationRunsPaginateResponsereplicationRunListTypeDef = TypedDict(
    "GetReplicationRunsPaginateResponsereplicationRunListTypeDef",
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

GetReplicationRunsPaginateResponseTypeDef = TypedDict(
    "GetReplicationRunsPaginateResponseTypeDef",
    {
        "replicationJob": GetReplicationRunsPaginateResponsereplicationJobTypeDef,
        "replicationRunList": List[GetReplicationRunsPaginateResponsereplicationRunListTypeDef],
        "NextToken": str,
    },
    total=False,
)

GetServersPaginatePaginationConfigTypeDef = TypedDict(
    "GetServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetServersPaginateResponseserverListvmServervmServerAddressTypeDef = TypedDict(
    "GetServersPaginateResponseserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)

GetServersPaginateResponseserverListvmServerTypeDef = TypedDict(
    "GetServersPaginateResponseserverListvmServerTypeDef",
    {
        "vmServerAddress": GetServersPaginateResponseserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

GetServersPaginateResponseserverListTypeDef = TypedDict(
    "GetServersPaginateResponseserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": GetServersPaginateResponseserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

GetServersPaginateResponseTypeDef = TypedDict(
    "GetServersPaginateResponseTypeDef",
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

GetServersPaginateVmServerAddressListTypeDef = TypedDict(
    "GetServersPaginateVmServerAddressListTypeDef", {"vmManagerId": str, "vmId": str}, total=False
)

ListAppsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAppsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAppsPaginateResponseappslaunchDetailsTypeDef = TypedDict(
    "ListAppsPaginateResponseappslaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)

ListAppsPaginateResponseappsTypeDef = TypedDict(
    "ListAppsPaginateResponseappsTypeDef",
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

ListAppsPaginateResponseTypeDef = TypedDict(
    "ListAppsPaginateResponseTypeDef",
    {"apps": List[ListAppsPaginateResponseappsTypeDef], "NextToken": str},
    total=False,
)
