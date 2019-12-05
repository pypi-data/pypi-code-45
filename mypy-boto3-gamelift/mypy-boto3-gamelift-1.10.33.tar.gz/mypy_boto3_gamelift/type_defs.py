"Main interface for gamelift service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateAliasResponseAliasRoutingStrategyTypeDef = TypedDict(
    "ClientCreateAliasResponseAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)

ClientCreateAliasResponseAliasTypeDef = TypedDict(
    "ClientCreateAliasResponseAliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ClientCreateAliasResponseAliasRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientCreateAliasResponseTypeDef = TypedDict(
    "ClientCreateAliasResponseTypeDef",
    {"Alias": ClientCreateAliasResponseAliasTypeDef},
    total=False,
)

ClientCreateAliasRoutingStrategyTypeDef = TypedDict(
    "ClientCreateAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)

ClientCreateBuildResponseBuildTypeDef = TypedDict(
    "ClientCreateBuildResponseBuildTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": Literal["INITIALIZED", "READY", "FAILED"],
        "SizeOnDisk": int,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "CreationTime": datetime,
    },
    total=False,
)

ClientCreateBuildResponseStorageLocationTypeDef = TypedDict(
    "ClientCreateBuildResponseStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ClientCreateBuildResponseUploadCredentialsTypeDef = TypedDict(
    "ClientCreateBuildResponseUploadCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str},
    total=False,
)

ClientCreateBuildResponseTypeDef = TypedDict(
    "ClientCreateBuildResponseTypeDef",
    {
        "Build": ClientCreateBuildResponseBuildTypeDef,
        "UploadCredentials": ClientCreateBuildResponseUploadCredentialsTypeDef,
        "StorageLocation": ClientCreateBuildResponseStorageLocationTypeDef,
    },
    total=False,
)

ClientCreateBuildStorageLocationTypeDef = TypedDict(
    "ClientCreateBuildStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ClientCreateFleetCertificateConfigurationTypeDef = TypedDict(
    "ClientCreateFleetCertificateConfigurationTypeDef",
    {"CertificateType": Literal["DISABLED", "GENERATED"]},
)

_RequiredClientCreateFleetEC2InboundPermissionsTypeDef = TypedDict(
    "_RequiredClientCreateFleetEC2InboundPermissionsTypeDef", {"FromPort": int}
)
_OptionalClientCreateFleetEC2InboundPermissionsTypeDef = TypedDict(
    "_OptionalClientCreateFleetEC2InboundPermissionsTypeDef",
    {"ToPort": int, "IpRange": str, "Protocol": Literal["TCP", "UDP"]},
    total=False,
)


class ClientCreateFleetEC2InboundPermissionsTypeDef(
    _RequiredClientCreateFleetEC2InboundPermissionsTypeDef,
    _OptionalClientCreateFleetEC2InboundPermissionsTypeDef,
):
    pass


ClientCreateFleetResourceCreationLimitPolicyTypeDef = TypedDict(
    "ClientCreateFleetResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)

ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef = TypedDict(
    "ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef",
    {"CertificateType": Literal["DISABLED", "GENERATED"]},
    total=False,
)

ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)

ClientCreateFleetResponseFleetAttributesTypeDef = TypedDict(
    "ClientCreateFleetResponseFleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": Literal["ON_DEMAND", "SPOT"],
        "InstanceType": Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ],
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": Literal[
            "NEW",
            "DOWNLOADING",
            "VALIDATING",
            "BUILDING",
            "ACTIVATING",
            "ACTIVE",
            "DELETING",
            "ERROR",
            "TERMINATED",
        ],
        "BuildId": str,
        "ScriptId": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": Literal["NoProtection", "FullProtection"],
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "ResourceCreationLimitPolicy": ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef,
        "MetricGroups": List[str],
        "StoppedActions": List[str],
        "InstanceRoleArn": str,
        "CertificateConfiguration": ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef,
    },
    total=False,
)

ClientCreateFleetResponseTypeDef = TypedDict(
    "ClientCreateFleetResponseTypeDef",
    {"FleetAttributes": ClientCreateFleetResponseFleetAttributesTypeDef},
    total=False,
)

_RequiredClientCreateFleetRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_RequiredClientCreateFleetRuntimeConfigurationServerProcessesTypeDef", {"LaunchPath": str}
)
_OptionalClientCreateFleetRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_OptionalClientCreateFleetRuntimeConfigurationServerProcessesTypeDef",
    {"Parameters": str, "ConcurrentExecutions": int},
    total=False,
)


class ClientCreateFleetRuntimeConfigurationServerProcessesTypeDef(
    _RequiredClientCreateFleetRuntimeConfigurationServerProcessesTypeDef,
    _OptionalClientCreateFleetRuntimeConfigurationServerProcessesTypeDef,
):
    pass


ClientCreateFleetRuntimeConfigurationTypeDef = TypedDict(
    "ClientCreateFleetRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[ClientCreateFleetRuntimeConfigurationServerProcessesTypeDef],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)

_RequiredClientCreateGameSessionGamePropertiesTypeDef = TypedDict(
    "_RequiredClientCreateGameSessionGamePropertiesTypeDef", {"Key": str}
)
_OptionalClientCreateGameSessionGamePropertiesTypeDef = TypedDict(
    "_OptionalClientCreateGameSessionGamePropertiesTypeDef", {"Value": str}, total=False
)


class ClientCreateGameSessionGamePropertiesTypeDef(
    _RequiredClientCreateGameSessionGamePropertiesTypeDef,
    _OptionalClientCreateGameSessionGamePropertiesTypeDef,
):
    pass


ClientCreateGameSessionQueueDestinationsTypeDef = TypedDict(
    "ClientCreateGameSessionQueueDestinationsTypeDef", {"DestinationArn": str}, total=False
)

ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)

ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef = TypedDict(
    "ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)

ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)

ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef = TypedDict(
    "ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List[
            ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef
        ],
        "Destinations": List[
            ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef
        ],
    },
    total=False,
)

ClientCreateGameSessionQueueResponseTypeDef = TypedDict(
    "ClientCreateGameSessionQueueResponseTypeDef",
    {"GameSessionQueue": ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef},
    total=False,
)

ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef = TypedDict(
    "ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateGameSessionResponseGameSessionTypeDef = TypedDict(
    "ClientCreateGameSessionResponseGameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": Literal["ACTIVE", "ACTIVATING", "TERMINATED", "TERMINATING", "ERROR"],
        "StatusReason": str,
        "GameProperties": List[ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": Literal["ACCEPT_ALL", "DENY_ALL"],
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

ClientCreateGameSessionResponseTypeDef = TypedDict(
    "ClientCreateGameSessionResponseTypeDef",
    {"GameSession": ClientCreateGameSessionResponseGameSessionTypeDef},
    total=False,
)

_RequiredClientCreateMatchmakingConfigurationGamePropertiesTypeDef = TypedDict(
    "_RequiredClientCreateMatchmakingConfigurationGamePropertiesTypeDef", {"Key": str}
)
_OptionalClientCreateMatchmakingConfigurationGamePropertiesTypeDef = TypedDict(
    "_OptionalClientCreateMatchmakingConfigurationGamePropertiesTypeDef",
    {"Value": str},
    total=False,
)


class ClientCreateMatchmakingConfigurationGamePropertiesTypeDef(
    _RequiredClientCreateMatchmakingConfigurationGamePropertiesTypeDef,
    _OptionalClientCreateMatchmakingConfigurationGamePropertiesTypeDef,
):
    pass


ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef = TypedDict(
    "ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef = TypedDict(
    "ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef",
    {
        "Name": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List[
            ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef
        ],
        "GameSessionData": str,
        "BackfillMode": Literal["AUTOMATIC", "MANUAL"],
    },
    total=False,
)

ClientCreateMatchmakingConfigurationResponseTypeDef = TypedDict(
    "ClientCreateMatchmakingConfigurationResponseTypeDef",
    {"Configuration": ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef},
    total=False,
)

ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef = TypedDict(
    "ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef",
    {"RuleSetName": str, "RuleSetBody": str, "CreationTime": datetime},
    total=False,
)

ClientCreateMatchmakingRuleSetResponseTypeDef = TypedDict(
    "ClientCreateMatchmakingRuleSetResponseTypeDef",
    {"RuleSet": ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef},
    total=False,
)

ClientCreatePlayerSessionResponsePlayerSessionTypeDef = TypedDict(
    "ClientCreatePlayerSessionResponsePlayerSessionTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": Literal["RESERVED", "ACTIVE", "COMPLETED", "TIMEDOUT"],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)

ClientCreatePlayerSessionResponseTypeDef = TypedDict(
    "ClientCreatePlayerSessionResponseTypeDef",
    {"PlayerSession": ClientCreatePlayerSessionResponsePlayerSessionTypeDef},
    total=False,
)

ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef = TypedDict(
    "ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": Literal["RESERVED", "ACTIVE", "COMPLETED", "TIMEDOUT"],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)

ClientCreatePlayerSessionsResponseTypeDef = TypedDict(
    "ClientCreatePlayerSessionsResponseTypeDef",
    {"PlayerSessions": List[ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef]},
    total=False,
)

ClientCreateScriptResponseScriptStorageLocationTypeDef = TypedDict(
    "ClientCreateScriptResponseScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ClientCreateScriptResponseScriptTypeDef = TypedDict(
    "ClientCreateScriptResponseScriptTypeDef",
    {
        "ScriptId": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": ClientCreateScriptResponseScriptStorageLocationTypeDef,
    },
    total=False,
)

ClientCreateScriptResponseTypeDef = TypedDict(
    "ClientCreateScriptResponseTypeDef",
    {"Script": ClientCreateScriptResponseScriptTypeDef},
    total=False,
)

ClientCreateScriptStorageLocationTypeDef = TypedDict(
    "ClientCreateScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef = TypedDict(
    "ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)

ClientCreateVpcPeeringAuthorizationResponseTypeDef = TypedDict(
    "ClientCreateVpcPeeringAuthorizationResponseTypeDef",
    {
        "VpcPeeringAuthorization": ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef
    },
    total=False,
)

ClientDescribeAliasResponseAliasRoutingStrategyTypeDef = TypedDict(
    "ClientDescribeAliasResponseAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)

ClientDescribeAliasResponseAliasTypeDef = TypedDict(
    "ClientDescribeAliasResponseAliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ClientDescribeAliasResponseAliasRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientDescribeAliasResponseTypeDef = TypedDict(
    "ClientDescribeAliasResponseTypeDef",
    {"Alias": ClientDescribeAliasResponseAliasTypeDef},
    total=False,
)

ClientDescribeBuildResponseBuildTypeDef = TypedDict(
    "ClientDescribeBuildResponseBuildTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": Literal["INITIALIZED", "READY", "FAILED"],
        "SizeOnDisk": int,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeBuildResponseTypeDef = TypedDict(
    "ClientDescribeBuildResponseTypeDef",
    {"Build": ClientDescribeBuildResponseBuildTypeDef},
    total=False,
)

ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef = TypedDict(
    "ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef",
    {
        "EC2InstanceType": Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ],
        "CurrentInstances": int,
        "InstanceLimit": int,
    },
    total=False,
)

ClientDescribeEc2InstanceLimitsResponseTypeDef = TypedDict(
    "ClientDescribeEc2InstanceLimitsResponseTypeDef",
    {"EC2InstanceLimits": List[ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef]},
    total=False,
)

ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef = TypedDict(
    "ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef",
    {"CertificateType": Literal["DISABLED", "GENERATED"]},
    total=False,
)

ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)

ClientDescribeFleetAttributesResponseFleetAttributesTypeDef = TypedDict(
    "ClientDescribeFleetAttributesResponseFleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": Literal["ON_DEMAND", "SPOT"],
        "InstanceType": Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ],
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": Literal[
            "NEW",
            "DOWNLOADING",
            "VALIDATING",
            "BUILDING",
            "ACTIVATING",
            "ACTIVE",
            "DELETING",
            "ERROR",
            "TERMINATED",
        ],
        "BuildId": str,
        "ScriptId": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": Literal["NoProtection", "FullProtection"],
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "ResourceCreationLimitPolicy": ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef,
        "MetricGroups": List[str],
        "StoppedActions": List[str],
        "InstanceRoleArn": str,
        "CertificateConfiguration": ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeFleetAttributesResponseTypeDef = TypedDict(
    "ClientDescribeFleetAttributesResponseTypeDef",
    {
        "FleetAttributes": List[ClientDescribeFleetAttributesResponseFleetAttributesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef = TypedDict(
    "ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef",
    {
        "DESIRED": int,
        "MINIMUM": int,
        "MAXIMUM": int,
        "PENDING": int,
        "ACTIVE": int,
        "IDLE": int,
        "TERMINATING": int,
    },
    total=False,
)

ClientDescribeFleetCapacityResponseFleetCapacityTypeDef = TypedDict(
    "ClientDescribeFleetCapacityResponseFleetCapacityTypeDef",
    {
        "FleetId": str,
        "InstanceType": Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ],
        "InstanceCounts": ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef,
    },
    total=False,
)

ClientDescribeFleetCapacityResponseTypeDef = TypedDict(
    "ClientDescribeFleetCapacityResponseTypeDef",
    {
        "FleetCapacity": List[ClientDescribeFleetCapacityResponseFleetCapacityTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeFleetEventsResponseEventsTypeDef = TypedDict(
    "ClientDescribeFleetEventsResponseEventsTypeDef",
    {
        "EventId": str,
        "ResourceId": str,
        "EventCode": Literal[
            "GENERIC_EVENT",
            "FLEET_CREATED",
            "FLEET_DELETED",
            "FLEET_SCALING_EVENT",
            "FLEET_STATE_DOWNLOADING",
            "FLEET_STATE_VALIDATING",
            "FLEET_STATE_BUILDING",
            "FLEET_STATE_ACTIVATING",
            "FLEET_STATE_ACTIVE",
            "FLEET_STATE_ERROR",
            "FLEET_INITIALIZATION_FAILED",
            "FLEET_BINARY_DOWNLOAD_FAILED",
            "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND",
            "FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE",
            "FLEET_VALIDATION_TIMED_OUT",
            "FLEET_ACTIVATION_FAILED",
            "FLEET_ACTIVATION_FAILED_NO_INSTANCES",
            "FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED",
            "SERVER_PROCESS_INVALID_PATH",
            "SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT",
            "SERVER_PROCESS_PROCESS_READY_TIMEOUT",
            "SERVER_PROCESS_CRASHED",
            "SERVER_PROCESS_TERMINATED_UNHEALTHY",
            "SERVER_PROCESS_FORCE_TERMINATED",
            "SERVER_PROCESS_PROCESS_EXIT_TIMEOUT",
            "GAME_SESSION_ACTIVATION_TIMEOUT",
            "FLEET_CREATION_EXTRACTING_BUILD",
            "FLEET_CREATION_RUNNING_INSTALLER",
            "FLEET_CREATION_VALIDATING_RUNTIME_CONFIG",
            "FLEET_VPC_PEERING_SUCCEEDED",
            "FLEET_VPC_PEERING_FAILED",
            "FLEET_VPC_PEERING_DELETED",
            "INSTANCE_INTERRUPTED",
        ],
        "Message": str,
        "EventTime": datetime,
        "PreSignedLogUrl": str,
    },
    total=False,
)

ClientDescribeFleetEventsResponseTypeDef = TypedDict(
    "ClientDescribeFleetEventsResponseTypeDef",
    {"Events": List[ClientDescribeFleetEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef = TypedDict(
    "ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef",
    {"FromPort": int, "ToPort": int, "IpRange": str, "Protocol": Literal["TCP", "UDP"]},
    total=False,
)

ClientDescribeFleetPortSettingsResponseTypeDef = TypedDict(
    "ClientDescribeFleetPortSettingsResponseTypeDef",
    {"InboundPermissions": List[ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef]},
    total=False,
)

ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef = TypedDict(
    "ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef",
    {
        "FleetId": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
    },
    total=False,
)

ClientDescribeFleetUtilizationResponseTypeDef = TypedDict(
    "ClientDescribeFleetUtilizationResponseTypeDef",
    {
        "FleetUtilization": List[ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef = TypedDict(
    "ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef = TypedDict(
    "ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": Literal["ACTIVE", "ACTIVATING", "TERMINATED", "TERMINATING", "ERROR"],
        "StatusReason": str,
        "GameProperties": List[
            ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": Literal["ACCEPT_ALL", "DENY_ALL"],
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef = TypedDict(
    "ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef",
    {
        "GameSession": ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef,
        "ProtectionPolicy": Literal["NoProtection", "FullProtection"],
    },
    total=False,
)

ClientDescribeGameSessionDetailsResponseTypeDef = TypedDict(
    "ClientDescribeGameSessionDetailsResponseTypeDef",
    {
        "GameSessionDetails": List[
            ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef = TypedDict(
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)

ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": Any},
    total=False,
)

ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef = TypedDict(
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": Literal["PENDING", "FULFILLED", "CANCELLED", "TIMED_OUT", "FAILED"],
        "GameProperties": List[
            ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
        ],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List[
            ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List[
            ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
        ],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

ClientDescribeGameSessionPlacementResponseTypeDef = TypedDict(
    "ClientDescribeGameSessionPlacementResponseTypeDef",
    {"GameSessionPlacement": ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef},
    total=False,
)

ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef = TypedDict(
    "ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)

ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef = TypedDict(
    "ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)

ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef = TypedDict(
    "ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List[
            ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef
        ],
        "Destinations": List[
            ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef
        ],
    },
    total=False,
)

ClientDescribeGameSessionQueuesResponseTypeDef = TypedDict(
    "ClientDescribeGameSessionQueuesResponseTypeDef",
    {
        "GameSessionQueues": List[ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeGameSessionsResponseGameSessionsTypeDef = TypedDict(
    "ClientDescribeGameSessionsResponseGameSessionsTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": Literal["ACTIVE", "ACTIVATING", "TERMINATED", "TERMINATING", "ERROR"],
        "StatusReason": str,
        "GameProperties": List[ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": Literal["ACCEPT_ALL", "DENY_ALL"],
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

ClientDescribeGameSessionsResponseTypeDef = TypedDict(
    "ClientDescribeGameSessionsResponseTypeDef",
    {"GameSessions": List[ClientDescribeGameSessionsResponseGameSessionsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeInstancesResponseInstancesTypeDef = TypedDict(
    "ClientDescribeInstancesResponseInstancesTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "DnsName": str,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "Type": Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ],
        "Status": Literal["PENDING", "ACTIVE", "TERMINATING"],
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeInstancesResponseTypeDef = TypedDict(
    "ClientDescribeInstancesResponseTypeDef",
    {"Instances": List[ClientDescribeInstancesResponseInstancesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef = TypedDict(
    "ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef",
    {
        "Name": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List[
            ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef
        ],
        "GameSessionData": str,
        "BackfillMode": Literal["AUTOMATIC", "MANUAL"],
    },
    total=False,
)

ClientDescribeMatchmakingConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeMatchmakingConfigurationsResponseTypeDef",
    {
        "Configurations": List[
            ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef = TypedDict(
    "ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)

ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef = TypedDict(
    "ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List[
            ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef = TypedDict(
    "ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)

ClientDescribeMatchmakingResponseTicketListPlayersTypeDef = TypedDict(
    "ClientDescribeMatchmakingResponseTicketListPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[
            str, ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef
        ],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)

ClientDescribeMatchmakingResponseTicketListTypeDef = TypedDict(
    "ClientDescribeMatchmakingResponseTicketListTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "Status": Literal[
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "PLACING",
            "QUEUED",
            "REQUIRES_ACCEPTANCE",
            "SEARCHING",
            "TIMED_OUT",
        ],
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List[ClientDescribeMatchmakingResponseTicketListPlayersTypeDef],
        "GameSessionConnectionInfo": ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef,
        "EstimatedWaitTime": int,
    },
    total=False,
)

ClientDescribeMatchmakingResponseTypeDef = TypedDict(
    "ClientDescribeMatchmakingResponseTypeDef",
    {"TicketList": List[ClientDescribeMatchmakingResponseTicketListTypeDef]},
    total=False,
)

ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef = TypedDict(
    "ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef",
    {"RuleSetName": str, "RuleSetBody": str, "CreationTime": datetime},
    total=False,
)

ClientDescribeMatchmakingRuleSetsResponseTypeDef = TypedDict(
    "ClientDescribeMatchmakingRuleSetsResponseTypeDef",
    {"RuleSets": List[ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef = TypedDict(
    "ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": Literal["RESERVED", "ACTIVE", "COMPLETED", "TIMEDOUT"],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)

ClientDescribePlayerSessionsResponseTypeDef = TypedDict(
    "ClientDescribePlayerSessionsResponseTypeDef",
    {
        "PlayerSessions": List[ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    {"LaunchPath": str, "Parameters": str, "ConcurrentExecutions": int},
    total=False,
)

ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef = TypedDict(
    "ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)

ClientDescribeRuntimeConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeRuntimeConfigurationResponseTypeDef",
    {"RuntimeConfiguration": ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef},
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef",
    {"TargetValue": float},
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    {
        "FleetId": str,
        "Name": str,
        "Status": Literal[
            "ACTIVE",
            "UPDATE_REQUESTED",
            "UPDATING",
            "DELETE_REQUESTED",
            "DELETING",
            "DELETED",
            "ERROR",
        ],
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": Literal[
            "ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"
        ],
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Threshold": float,
        "EvaluationPeriods": int,
        "MetricName": Literal[
            "ActivatingGameSessions",
            "ActiveGameSessions",
            "ActiveInstances",
            "AvailableGameSessions",
            "AvailablePlayerSessions",
            "CurrentPlayerSessions",
            "IdleInstances",
            "PercentAvailableGameSessions",
            "PercentIdleInstances",
            "QueueDepth",
            "WaitTime",
        ],
        "PolicyType": Literal["RuleBased", "TargetBased"],
        "TargetConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScriptResponseScriptStorageLocationTypeDef = TypedDict(
    "ClientDescribeScriptResponseScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ClientDescribeScriptResponseScriptTypeDef = TypedDict(
    "ClientDescribeScriptResponseScriptTypeDef",
    {
        "ScriptId": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": ClientDescribeScriptResponseScriptStorageLocationTypeDef,
    },
    total=False,
)

ClientDescribeScriptResponseTypeDef = TypedDict(
    "ClientDescribeScriptResponseTypeDef",
    {"Script": ClientDescribeScriptResponseScriptTypeDef},
    total=False,
)

ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef = TypedDict(
    "ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)

ClientDescribeVpcPeeringAuthorizationsResponseTypeDef = TypedDict(
    "ClientDescribeVpcPeeringAuthorizationsResponseTypeDef",
    {
        "VpcPeeringAuthorizations": List[
            ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef
        ]
    },
    total=False,
)

ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef = TypedDict(
    "ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef",
    {"Code": str, "Message": str},
    total=False,
)

ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef = TypedDict(
    "ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef",
    {
        "FleetId": str,
        "IpV4CidrBlock": str,
        "VpcPeeringConnectionId": str,
        "Status": ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef,
        "PeerVpcId": str,
        "GameLiftVpcId": str,
    },
    total=False,
)

ClientDescribeVpcPeeringConnectionsResponseTypeDef = TypedDict(
    "ClientDescribeVpcPeeringConnectionsResponseTypeDef",
    {
        "VpcPeeringConnections": List[
            ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef
        ]
    },
    total=False,
)

ClientGetGameSessionLogUrlResponseTypeDef = TypedDict(
    "ClientGetGameSessionLogUrlResponseTypeDef", {"PreSignedUrl": str}, total=False
)

ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef = TypedDict(
    "ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef",
    {"UserName": str, "Secret": str},
    total=False,
)

ClientGetInstanceAccessResponseInstanceAccessTypeDef = TypedDict(
    "ClientGetInstanceAccessResponseInstanceAccessTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "Credentials": ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef,
    },
    total=False,
)

ClientGetInstanceAccessResponseTypeDef = TypedDict(
    "ClientGetInstanceAccessResponseTypeDef",
    {"InstanceAccess": ClientGetInstanceAccessResponseInstanceAccessTypeDef},
    total=False,
)

ClientListAliasesResponseAliasesRoutingStrategyTypeDef = TypedDict(
    "ClientListAliasesResponseAliasesRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)

ClientListAliasesResponseAliasesTypeDef = TypedDict(
    "ClientListAliasesResponseAliasesTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ClientListAliasesResponseAliasesRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientListAliasesResponseTypeDef = TypedDict(
    "ClientListAliasesResponseTypeDef",
    {"Aliases": List[ClientListAliasesResponseAliasesTypeDef], "NextToken": str},
    total=False,
)

ClientListBuildsResponseBuildsTypeDef = TypedDict(
    "ClientListBuildsResponseBuildsTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": Literal["INITIALIZED", "READY", "FAILED"],
        "SizeOnDisk": int,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "CreationTime": datetime,
    },
    total=False,
)

ClientListBuildsResponseTypeDef = TypedDict(
    "ClientListBuildsResponseTypeDef",
    {"Builds": List[ClientListBuildsResponseBuildsTypeDef], "NextToken": str},
    total=False,
)

ClientListFleetsResponseTypeDef = TypedDict(
    "ClientListFleetsResponseTypeDef", {"FleetIds": List[str], "NextToken": str}, total=False
)

ClientListScriptsResponseScriptsStorageLocationTypeDef = TypedDict(
    "ClientListScriptsResponseScriptsStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ClientListScriptsResponseScriptsTypeDef = TypedDict(
    "ClientListScriptsResponseScriptsTypeDef",
    {
        "ScriptId": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": ClientListScriptsResponseScriptsStorageLocationTypeDef,
    },
    total=False,
)

ClientListScriptsResponseTypeDef = TypedDict(
    "ClientListScriptsResponseTypeDef",
    {"Scripts": List[ClientListScriptsResponseScriptsTypeDef], "NextToken": str},
    total=False,
)

ClientPutScalingPolicyResponseTypeDef = TypedDict(
    "ClientPutScalingPolicyResponseTypeDef", {"Name": str}, total=False
)

ClientPutScalingPolicyTargetConfigurationTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetConfigurationTypeDef", {"TargetValue": float}
)

ClientRequestUploadCredentialsResponseStorageLocationTypeDef = TypedDict(
    "ClientRequestUploadCredentialsResponseStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef = TypedDict(
    "ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str},
    total=False,
)

ClientRequestUploadCredentialsResponseTypeDef = TypedDict(
    "ClientRequestUploadCredentialsResponseTypeDef",
    {
        "UploadCredentials": ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef,
        "StorageLocation": ClientRequestUploadCredentialsResponseStorageLocationTypeDef,
    },
    total=False,
)

ClientResolveAliasResponseTypeDef = TypedDict(
    "ClientResolveAliasResponseTypeDef", {"FleetId": str}, total=False
)

ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientSearchGameSessionsResponseGameSessionsTypeDef = TypedDict(
    "ClientSearchGameSessionsResponseGameSessionsTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": Literal["ACTIVE", "ACTIVATING", "TERMINATED", "TERMINATING", "ERROR"],
        "StatusReason": str,
        "GameProperties": List[ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": Literal["ACCEPT_ALL", "DENY_ALL"],
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

ClientSearchGameSessionsResponseTypeDef = TypedDict(
    "ClientSearchGameSessionsResponseTypeDef",
    {"GameSessions": List[ClientSearchGameSessionsResponseGameSessionsTypeDef], "NextToken": str},
    total=False,
)

ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef = TypedDict(
    "ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerData": str},
    total=False,
)

_RequiredClientStartGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "_RequiredClientStartGameSessionPlacementGamePropertiesTypeDef", {"Key": str}
)
_OptionalClientStartGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "_OptionalClientStartGameSessionPlacementGamePropertiesTypeDef", {"Value": str}, total=False
)


class ClientStartGameSessionPlacementGamePropertiesTypeDef(
    _RequiredClientStartGameSessionPlacementGamePropertiesTypeDef,
    _OptionalClientStartGameSessionPlacementGamePropertiesTypeDef,
):
    pass


ClientStartGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "ClientStartGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": Any},
    total=False,
)

ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef = TypedDict(
    "ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)

ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": Any},
    total=False,
)

ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef = TypedDict(
    "ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": Literal["PENDING", "FULFILLED", "CANCELLED", "TIMED_OUT", "FAILED"],
        "GameProperties": List[
            ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
        ],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List[
            ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List[
            ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
        ],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

ClientStartGameSessionPlacementResponseTypeDef = TypedDict(
    "ClientStartGameSessionPlacementResponseTypeDef",
    {"GameSessionPlacement": ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef},
    total=False,
)

ClientStartMatchBackfillPlayersPlayerAttributesTypeDef = TypedDict(
    "ClientStartMatchBackfillPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)

ClientStartMatchBackfillPlayersTypeDef = TypedDict(
    "ClientStartMatchBackfillPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[str, ClientStartMatchBackfillPlayersPlayerAttributesTypeDef],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)

ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef = TypedDict(
    "ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)

ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef = TypedDict(
    "ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List[
            ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
        ],
    },
    total=False,
)

ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef = TypedDict(
    "ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)

ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef = TypedDict(
    "ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[
            str, ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef
        ],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)

ClientStartMatchBackfillResponseMatchmakingTicketTypeDef = TypedDict(
    "ClientStartMatchBackfillResponseMatchmakingTicketTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "Status": Literal[
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "PLACING",
            "QUEUED",
            "REQUIRES_ACCEPTANCE",
            "SEARCHING",
            "TIMED_OUT",
        ],
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List[ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef],
        "GameSessionConnectionInfo": ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef,
        "EstimatedWaitTime": int,
    },
    total=False,
)

ClientStartMatchBackfillResponseTypeDef = TypedDict(
    "ClientStartMatchBackfillResponseTypeDef",
    {"MatchmakingTicket": ClientStartMatchBackfillResponseMatchmakingTicketTypeDef},
    total=False,
)

ClientStartMatchmakingPlayersPlayerAttributesTypeDef = TypedDict(
    "ClientStartMatchmakingPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)

ClientStartMatchmakingPlayersTypeDef = TypedDict(
    "ClientStartMatchmakingPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[str, ClientStartMatchmakingPlayersPlayerAttributesTypeDef],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)

ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef = TypedDict(
    "ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)

ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef = TypedDict(
    "ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List[
            ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
        ],
    },
    total=False,
)

ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef = TypedDict(
    "ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)

ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef = TypedDict(
    "ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[
            str, ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef
        ],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)

ClientStartMatchmakingResponseMatchmakingTicketTypeDef = TypedDict(
    "ClientStartMatchmakingResponseMatchmakingTicketTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "Status": Literal[
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "PLACING",
            "QUEUED",
            "REQUIRES_ACCEPTANCE",
            "SEARCHING",
            "TIMED_OUT",
        ],
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List[ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef],
        "GameSessionConnectionInfo": ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef,
        "EstimatedWaitTime": int,
    },
    total=False,
)

ClientStartMatchmakingResponseTypeDef = TypedDict(
    "ClientStartMatchmakingResponseTypeDef",
    {"MatchmakingTicket": ClientStartMatchmakingResponseMatchmakingTicketTypeDef},
    total=False,
)

ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef = TypedDict(
    "ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)

ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": Any},
    total=False,
)

ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef = TypedDict(
    "ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": Literal["PENDING", "FULFILLED", "CANCELLED", "TIMED_OUT", "FAILED"],
        "GameProperties": List[
            ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
        ],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List[
            ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List[
            ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
        ],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

ClientStopGameSessionPlacementResponseTypeDef = TypedDict(
    "ClientStopGameSessionPlacementResponseTypeDef",
    {"GameSessionPlacement": ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef},
    total=False,
)

ClientUpdateAliasResponseAliasRoutingStrategyTypeDef = TypedDict(
    "ClientUpdateAliasResponseAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)

ClientUpdateAliasResponseAliasTypeDef = TypedDict(
    "ClientUpdateAliasResponseAliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ClientUpdateAliasResponseAliasRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientUpdateAliasResponseTypeDef = TypedDict(
    "ClientUpdateAliasResponseTypeDef",
    {"Alias": ClientUpdateAliasResponseAliasTypeDef},
    total=False,
)

ClientUpdateAliasRoutingStrategyTypeDef = TypedDict(
    "ClientUpdateAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)

ClientUpdateBuildResponseBuildTypeDef = TypedDict(
    "ClientUpdateBuildResponseBuildTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": Literal["INITIALIZED", "READY", "FAILED"],
        "SizeOnDisk": int,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "CreationTime": datetime,
    },
    total=False,
)

ClientUpdateBuildResponseTypeDef = TypedDict(
    "ClientUpdateBuildResponseTypeDef",
    {"Build": ClientUpdateBuildResponseBuildTypeDef},
    total=False,
)

ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)

ClientUpdateFleetAttributesResponseTypeDef = TypedDict(
    "ClientUpdateFleetAttributesResponseTypeDef", {"FleetId": str}, total=False
)

ClientUpdateFleetCapacityResponseTypeDef = TypedDict(
    "ClientUpdateFleetCapacityResponseTypeDef", {"FleetId": str}, total=False
)

_RequiredClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef = TypedDict(
    "_RequiredClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef",
    {"FromPort": int},
)
_OptionalClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef = TypedDict(
    "_OptionalClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef",
    {"ToPort": int, "IpRange": str, "Protocol": Literal["TCP", "UDP"]},
    total=False,
)


class ClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef(
    _RequiredClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef,
    _OptionalClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef,
):
    pass


_RequiredClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef = TypedDict(
    "_RequiredClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef", {"FromPort": int}
)
_OptionalClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef = TypedDict(
    "_OptionalClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef",
    {"ToPort": int, "IpRange": str, "Protocol": Literal["TCP", "UDP"]},
    total=False,
)


class ClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef(
    _RequiredClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef,
    _OptionalClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef,
):
    pass


ClientUpdateFleetPortSettingsResponseTypeDef = TypedDict(
    "ClientUpdateFleetPortSettingsResponseTypeDef", {"FleetId": str}, total=False
)

ClientUpdateGameSessionQueueDestinationsTypeDef = TypedDict(
    "ClientUpdateGameSessionQueueDestinationsTypeDef", {"DestinationArn": str}, total=False
)

ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)

ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef = TypedDict(
    "ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)

ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)

ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef = TypedDict(
    "ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List[
            ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef
        ],
        "Destinations": List[
            ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef
        ],
    },
    total=False,
)

ClientUpdateGameSessionQueueResponseTypeDef = TypedDict(
    "ClientUpdateGameSessionQueueResponseTypeDef",
    {"GameSessionQueue": ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef},
    total=False,
)

ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef = TypedDict(
    "ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientUpdateGameSessionResponseGameSessionTypeDef = TypedDict(
    "ClientUpdateGameSessionResponseGameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": Literal["ACTIVE", "ACTIVATING", "TERMINATED", "TERMINATING", "ERROR"],
        "StatusReason": str,
        "GameProperties": List[ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": Literal["ACCEPT_ALL", "DENY_ALL"],
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

ClientUpdateGameSessionResponseTypeDef = TypedDict(
    "ClientUpdateGameSessionResponseTypeDef",
    {"GameSession": ClientUpdateGameSessionResponseGameSessionTypeDef},
    total=False,
)

_RequiredClientUpdateMatchmakingConfigurationGamePropertiesTypeDef = TypedDict(
    "_RequiredClientUpdateMatchmakingConfigurationGamePropertiesTypeDef", {"Key": str}
)
_OptionalClientUpdateMatchmakingConfigurationGamePropertiesTypeDef = TypedDict(
    "_OptionalClientUpdateMatchmakingConfigurationGamePropertiesTypeDef",
    {"Value": str},
    total=False,
)


class ClientUpdateMatchmakingConfigurationGamePropertiesTypeDef(
    _RequiredClientUpdateMatchmakingConfigurationGamePropertiesTypeDef,
    _OptionalClientUpdateMatchmakingConfigurationGamePropertiesTypeDef,
):
    pass


ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef = TypedDict(
    "ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef = TypedDict(
    "ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef",
    {
        "Name": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List[
            ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef
        ],
        "GameSessionData": str,
        "BackfillMode": Literal["AUTOMATIC", "MANUAL"],
    },
    total=False,
)

ClientUpdateMatchmakingConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateMatchmakingConfigurationResponseTypeDef",
    {"Configuration": ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef},
    total=False,
)

ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    {"LaunchPath": str, "Parameters": str, "ConcurrentExecutions": int},
    total=False,
)

ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef = TypedDict(
    "ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)

ClientUpdateRuntimeConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateRuntimeConfigurationResponseTypeDef",
    {"RuntimeConfiguration": ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef},
    total=False,
)

_RequiredClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_RequiredClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef",
    {"LaunchPath": str},
)
_OptionalClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_OptionalClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef",
    {"Parameters": str, "ConcurrentExecutions": int},
    total=False,
)


class ClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef(
    _RequiredClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef,
    _OptionalClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef,
):
    pass


ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef = TypedDict(
    "ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)

ClientUpdateScriptResponseScriptStorageLocationTypeDef = TypedDict(
    "ClientUpdateScriptResponseScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ClientUpdateScriptResponseScriptTypeDef = TypedDict(
    "ClientUpdateScriptResponseScriptTypeDef",
    {
        "ScriptId": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": ClientUpdateScriptResponseScriptStorageLocationTypeDef,
    },
    total=False,
)

ClientUpdateScriptResponseTypeDef = TypedDict(
    "ClientUpdateScriptResponseTypeDef",
    {"Script": ClientUpdateScriptResponseScriptTypeDef},
    total=False,
)

ClientUpdateScriptStorageLocationTypeDef = TypedDict(
    "ClientUpdateScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ClientValidateMatchmakingRuleSetResponseTypeDef = TypedDict(
    "ClientValidateMatchmakingRuleSetResponseTypeDef", {"Valid": bool}, total=False
)

DescribeFleetAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeFleetAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef = TypedDict(
    "DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef",
    {"CertificateType": Literal["DISABLED", "GENERATED"]},
    total=False,
)

DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)

DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef = TypedDict(
    "DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": Literal["ON_DEMAND", "SPOT"],
        "InstanceType": Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ],
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": Literal[
            "NEW",
            "DOWNLOADING",
            "VALIDATING",
            "BUILDING",
            "ACTIVATING",
            "ACTIVE",
            "DELETING",
            "ERROR",
            "TERMINATED",
        ],
        "BuildId": str,
        "ScriptId": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": Literal["NoProtection", "FullProtection"],
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "ResourceCreationLimitPolicy": DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef,
        "MetricGroups": List[str],
        "StoppedActions": List[str],
        "InstanceRoleArn": str,
        "CertificateConfiguration": DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef,
    },
    total=False,
)

DescribeFleetAttributesPaginateResponseTypeDef = TypedDict(
    "DescribeFleetAttributesPaginateResponseTypeDef",
    {"FleetAttributes": List[DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef]},
    total=False,
)

DescribeFleetCapacityPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeFleetCapacityPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef = TypedDict(
    "DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef",
    {
        "DESIRED": int,
        "MINIMUM": int,
        "MAXIMUM": int,
        "PENDING": int,
        "ACTIVE": int,
        "IDLE": int,
        "TERMINATING": int,
    },
    total=False,
)

DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef = TypedDict(
    "DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef",
    {
        "FleetId": str,
        "InstanceType": Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ],
        "InstanceCounts": DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef,
    },
    total=False,
)

DescribeFleetCapacityPaginateResponseTypeDef = TypedDict(
    "DescribeFleetCapacityPaginateResponseTypeDef",
    {"FleetCapacity": List[DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef]},
    total=False,
)

DescribeFleetEventsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeFleetEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeFleetEventsPaginateResponseEventsTypeDef = TypedDict(
    "DescribeFleetEventsPaginateResponseEventsTypeDef",
    {
        "EventId": str,
        "ResourceId": str,
        "EventCode": Literal[
            "GENERIC_EVENT",
            "FLEET_CREATED",
            "FLEET_DELETED",
            "FLEET_SCALING_EVENT",
            "FLEET_STATE_DOWNLOADING",
            "FLEET_STATE_VALIDATING",
            "FLEET_STATE_BUILDING",
            "FLEET_STATE_ACTIVATING",
            "FLEET_STATE_ACTIVE",
            "FLEET_STATE_ERROR",
            "FLEET_INITIALIZATION_FAILED",
            "FLEET_BINARY_DOWNLOAD_FAILED",
            "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND",
            "FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE",
            "FLEET_VALIDATION_TIMED_OUT",
            "FLEET_ACTIVATION_FAILED",
            "FLEET_ACTIVATION_FAILED_NO_INSTANCES",
            "FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED",
            "SERVER_PROCESS_INVALID_PATH",
            "SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT",
            "SERVER_PROCESS_PROCESS_READY_TIMEOUT",
            "SERVER_PROCESS_CRASHED",
            "SERVER_PROCESS_TERMINATED_UNHEALTHY",
            "SERVER_PROCESS_FORCE_TERMINATED",
            "SERVER_PROCESS_PROCESS_EXIT_TIMEOUT",
            "GAME_SESSION_ACTIVATION_TIMEOUT",
            "FLEET_CREATION_EXTRACTING_BUILD",
            "FLEET_CREATION_RUNNING_INSTALLER",
            "FLEET_CREATION_VALIDATING_RUNTIME_CONFIG",
            "FLEET_VPC_PEERING_SUCCEEDED",
            "FLEET_VPC_PEERING_FAILED",
            "FLEET_VPC_PEERING_DELETED",
            "INSTANCE_INTERRUPTED",
        ],
        "Message": str,
        "EventTime": datetime,
        "PreSignedLogUrl": str,
    },
    total=False,
)

DescribeFleetEventsPaginateResponseTypeDef = TypedDict(
    "DescribeFleetEventsPaginateResponseTypeDef",
    {"Events": List[DescribeFleetEventsPaginateResponseEventsTypeDef]},
    total=False,
)

DescribeFleetUtilizationPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeFleetUtilizationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef = TypedDict(
    "DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef",
    {
        "FleetId": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
    },
    total=False,
)

DescribeFleetUtilizationPaginateResponseTypeDef = TypedDict(
    "DescribeFleetUtilizationPaginateResponseTypeDef",
    {"FleetUtilization": List[DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef]},
    total=False,
)

DescribeGameSessionDetailsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeGameSessionDetailsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef = TypedDict(
    "DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef = TypedDict(
    "DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": Literal["ACTIVE", "ACTIVATING", "TERMINATED", "TERMINATING", "ERROR"],
        "StatusReason": str,
        "GameProperties": List[
            DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": Literal["ACCEPT_ALL", "DENY_ALL"],
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef = TypedDict(
    "DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef",
    {
        "GameSession": DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef,
        "ProtectionPolicy": Literal["NoProtection", "FullProtection"],
    },
    total=False,
)

DescribeGameSessionDetailsPaginateResponseTypeDef = TypedDict(
    "DescribeGameSessionDetailsPaginateResponseTypeDef",
    {
        "GameSessionDetails": List[
            DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef
        ]
    },
    total=False,
)

DescribeGameSessionQueuesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeGameSessionQueuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef = TypedDict(
    "DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)

DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef = TypedDict(
    "DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)

DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef = TypedDict(
    "DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List[
            DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef
        ],
        "Destinations": List[
            DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef
        ],
    },
    total=False,
)

DescribeGameSessionQueuesPaginateResponseTypeDef = TypedDict(
    "DescribeGameSessionQueuesPaginateResponseTypeDef",
    {"GameSessionQueues": List[DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef]},
    total=False,
)

DescribeGameSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeGameSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

DescribeGameSessionsPaginateResponseGameSessionsTypeDef = TypedDict(
    "DescribeGameSessionsPaginateResponseGameSessionsTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": Literal["ACTIVE", "ACTIVATING", "TERMINATED", "TERMINATING", "ERROR"],
        "StatusReason": str,
        "GameProperties": List[
            DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": Literal["ACCEPT_ALL", "DENY_ALL"],
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

DescribeGameSessionsPaginateResponseTypeDef = TypedDict(
    "DescribeGameSessionsPaginateResponseTypeDef",
    {"GameSessions": List[DescribeGameSessionsPaginateResponseGameSessionsTypeDef]},
    total=False,
)

DescribeInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeInstancesPaginateResponseInstancesTypeDef = TypedDict(
    "DescribeInstancesPaginateResponseInstancesTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "DnsName": str,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "Type": Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ],
        "Status": Literal["PENDING", "ACTIVE", "TERMINATING"],
        "CreationTime": datetime,
    },
    total=False,
)

DescribeInstancesPaginateResponseTypeDef = TypedDict(
    "DescribeInstancesPaginateResponseTypeDef",
    {"Instances": List[DescribeInstancesPaginateResponseInstancesTypeDef]},
    total=False,
)

DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef",
    {
        "Name": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List[
            DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef
        ],
        "GameSessionData": str,
        "BackfillMode": Literal["AUTOMATIC", "MANUAL"],
    },
    total=False,
)

DescribeMatchmakingConfigurationsPaginateResponseTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsPaginateResponseTypeDef",
    {
        "Configurations": List[
            DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef
        ]
    },
    total=False,
)

DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef",
    {"RuleSetName": str, "RuleSetBody": str, "CreationTime": datetime},
    total=False,
)

DescribeMatchmakingRuleSetsPaginateResponseTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsPaginateResponseTypeDef",
    {"RuleSets": List[DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef]},
    total=False,
)

DescribePlayerSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribePlayerSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef = TypedDict(
    "DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": Literal["RESERVED", "ACTIVE", "COMPLETED", "TIMEDOUT"],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)

DescribePlayerSessionsPaginateResponseTypeDef = TypedDict(
    "DescribePlayerSessionsPaginateResponseTypeDef",
    {"PlayerSessions": List[DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef]},
    total=False,
)

DescribeScalingPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef",
    {"TargetValue": float},
    total=False,
)

DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
    {
        "FleetId": str,
        "Name": str,
        "Status": Literal[
            "ACTIVE",
            "UPDATE_REQUESTED",
            "UPDATING",
            "DELETE_REQUESTED",
            "DELETING",
            "DELETED",
            "ERROR",
        ],
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": Literal[
            "ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"
        ],
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Threshold": float,
        "EvaluationPeriods": int,
        "MetricName": Literal[
            "ActivatingGameSessions",
            "ActiveGameSessions",
            "ActiveInstances",
            "AvailableGameSessions",
            "AvailablePlayerSessions",
            "CurrentPlayerSessions",
            "IdleInstances",
            "PercentAvailableGameSessions",
            "PercentIdleInstances",
            "QueueDepth",
            "WaitTime",
        ],
        "PolicyType": Literal["RuleBased", "TargetBased"],
        "TargetConfiguration": DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef,
    },
    total=False,
)

DescribeScalingPoliciesPaginateResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesPaginateResponseTypeDef",
    {"ScalingPolicies": List[DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef]},
    total=False,
)

ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef = TypedDict(
    "ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)

ListAliasesPaginateResponseAliasesTypeDef = TypedDict(
    "ListAliasesPaginateResponseAliasesTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ListAliasesPaginateResponseTypeDef = TypedDict(
    "ListAliasesPaginateResponseTypeDef",
    {"Aliases": List[ListAliasesPaginateResponseAliasesTypeDef]},
    total=False,
)

ListBuildsPaginatePaginationConfigTypeDef = TypedDict(
    "ListBuildsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListBuildsPaginateResponseBuildsTypeDef = TypedDict(
    "ListBuildsPaginateResponseBuildsTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": Literal["INITIALIZED", "READY", "FAILED"],
        "SizeOnDisk": int,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "CreationTime": datetime,
    },
    total=False,
)

ListBuildsPaginateResponseTypeDef = TypedDict(
    "ListBuildsPaginateResponseTypeDef",
    {"Builds": List[ListBuildsPaginateResponseBuildsTypeDef]},
    total=False,
)

ListFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListFleetsPaginateResponseTypeDef = TypedDict(
    "ListFleetsPaginateResponseTypeDef", {"FleetIds": List[str]}, total=False
)

SearchGameSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "SearchGameSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

SearchGameSessionsPaginateResponseGameSessionsTypeDef = TypedDict(
    "SearchGameSessionsPaginateResponseGameSessionsTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": Literal["ACTIVE", "ACTIVATING", "TERMINATED", "TERMINATING", "ERROR"],
        "StatusReason": str,
        "GameProperties": List[SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": Literal["ACCEPT_ALL", "DENY_ALL"],
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

SearchGameSessionsPaginateResponseTypeDef = TypedDict(
    "SearchGameSessionsPaginateResponseTypeDef",
    {"GameSessions": List[SearchGameSessionsPaginateResponseGameSessionsTypeDef]},
    total=False,
)
