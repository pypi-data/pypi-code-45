"Main interface for gamelift service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateAliasResponseAliasRoutingStrategyTypeDef",
    "ClientCreateAliasResponseAliasTypeDef",
    "ClientCreateAliasResponseTypeDef",
    "ClientCreateAliasRoutingStrategyTypeDef",
    "ClientCreateBuildResponseBuildTypeDef",
    "ClientCreateBuildResponseStorageLocationTypeDef",
    "ClientCreateBuildResponseUploadCredentialsTypeDef",
    "ClientCreateBuildResponseTypeDef",
    "ClientCreateBuildStorageLocationTypeDef",
    "ClientCreateFleetCertificateConfigurationTypeDef",
    "ClientCreateFleetEC2InboundPermissionsTypeDef",
    "ClientCreateFleetResourceCreationLimitPolicyTypeDef",
    "ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef",
    "ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    "ClientCreateFleetResponseFleetAttributesTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientCreateFleetRuntimeConfigurationServerProcessesTypeDef",
    "ClientCreateFleetRuntimeConfigurationTypeDef",
    "ClientCreateGameSessionGamePropertiesTypeDef",
    "ClientCreateGameSessionQueueDestinationsTypeDef",
    "ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    "ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    "ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    "ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef",
    "ClientCreateGameSessionQueueResponseTypeDef",
    "ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef",
    "ClientCreateGameSessionResponseGameSessionTypeDef",
    "ClientCreateGameSessionResponseTypeDef",
    "ClientCreateMatchmakingConfigurationGamePropertiesTypeDef",
    "ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    "ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef",
    "ClientCreateMatchmakingConfigurationResponseTypeDef",
    "ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef",
    "ClientCreateMatchmakingRuleSetResponseTypeDef",
    "ClientCreatePlayerSessionResponsePlayerSessionTypeDef",
    "ClientCreatePlayerSessionResponseTypeDef",
    "ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef",
    "ClientCreatePlayerSessionsResponseTypeDef",
    "ClientCreateScriptResponseScriptStorageLocationTypeDef",
    "ClientCreateScriptResponseScriptTypeDef",
    "ClientCreateScriptResponseTypeDef",
    "ClientCreateScriptStorageLocationTypeDef",
    "ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef",
    "ClientCreateVpcPeeringAuthorizationResponseTypeDef",
    "ClientDescribeAliasResponseAliasRoutingStrategyTypeDef",
    "ClientDescribeAliasResponseAliasTypeDef",
    "ClientDescribeAliasResponseTypeDef",
    "ClientDescribeBuildResponseBuildTypeDef",
    "ClientDescribeBuildResponseTypeDef",
    "ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef",
    "ClientDescribeEc2InstanceLimitsResponseTypeDef",
    "ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef",
    "ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    "ClientDescribeFleetAttributesResponseFleetAttributesTypeDef",
    "ClientDescribeFleetAttributesResponseTypeDef",
    "ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef",
    "ClientDescribeFleetCapacityResponseFleetCapacityTypeDef",
    "ClientDescribeFleetCapacityResponseTypeDef",
    "ClientDescribeFleetEventsResponseEventsTypeDef",
    "ClientDescribeFleetEventsResponseTypeDef",
    "ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef",
    "ClientDescribeFleetPortSettingsResponseTypeDef",
    "ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef",
    "ClientDescribeFleetUtilizationResponseTypeDef",
    "ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    "ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef",
    "ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef",
    "ClientDescribeGameSessionDetailsResponseTypeDef",
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef",
    "ClientDescribeGameSessionPlacementResponseTypeDef",
    "ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef",
    "ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    "ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef",
    "ClientDescribeGameSessionQueuesResponseTypeDef",
    "ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    "ClientDescribeGameSessionsResponseGameSessionsTypeDef",
    "ClientDescribeGameSessionsResponseTypeDef",
    "ClientDescribeInstancesResponseInstancesTypeDef",
    "ClientDescribeInstancesResponseTypeDef",
    "ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef",
    "ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef",
    "ClientDescribeMatchmakingConfigurationsResponseTypeDef",
    "ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    "ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef",
    "ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef",
    "ClientDescribeMatchmakingResponseTicketListPlayersTypeDef",
    "ClientDescribeMatchmakingResponseTicketListTypeDef",
    "ClientDescribeMatchmakingResponseTypeDef",
    "ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef",
    "ClientDescribeMatchmakingRuleSetsResponseTypeDef",
    "ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef",
    "ClientDescribePlayerSessionsResponseTypeDef",
    "ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    "ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    "ClientDescribeRuntimeConfigurationResponseTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    "ClientDescribeScalingPoliciesResponseTypeDef",
    "ClientDescribeScriptResponseScriptStorageLocationTypeDef",
    "ClientDescribeScriptResponseScriptTypeDef",
    "ClientDescribeScriptResponseTypeDef",
    "ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef",
    "ClientDescribeVpcPeeringAuthorizationsResponseTypeDef",
    "ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef",
    "ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef",
    "ClientDescribeVpcPeeringConnectionsResponseTypeDef",
    "ClientGetGameSessionLogUrlResponseTypeDef",
    "ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef",
    "ClientGetInstanceAccessResponseInstanceAccessTypeDef",
    "ClientGetInstanceAccessResponseTypeDef",
    "ClientListAliasesResponseAliasesRoutingStrategyTypeDef",
    "ClientListAliasesResponseAliasesTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListBuildsResponseBuildsTypeDef",
    "ClientListBuildsResponseTypeDef",
    "ClientListFleetsResponseTypeDef",
    "ClientListScriptsResponseScriptsStorageLocationTypeDef",
    "ClientListScriptsResponseScriptsTypeDef",
    "ClientListScriptsResponseTypeDef",
    "ClientPutScalingPolicyResponseTypeDef",
    "ClientPutScalingPolicyTargetConfigurationTypeDef",
    "ClientRequestUploadCredentialsResponseStorageLocationTypeDef",
    "ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef",
    "ClientRequestUploadCredentialsResponseTypeDef",
    "ClientResolveAliasResponseTypeDef",
    "ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    "ClientSearchGameSessionsResponseGameSessionsTypeDef",
    "ClientSearchGameSessionsResponseTypeDef",
    "ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef",
    "ClientStartGameSessionPlacementGamePropertiesTypeDef",
    "ClientStartGameSessionPlacementPlayerLatenciesTypeDef",
    "ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    "ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    "ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    "ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef",
    "ClientStartGameSessionPlacementResponseTypeDef",
    "ClientStartMatchBackfillPlayersPlayerAttributesTypeDef",
    "ClientStartMatchBackfillPlayersTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketTypeDef",
    "ClientStartMatchBackfillResponseTypeDef",
    "ClientStartMatchmakingPlayersPlayerAttributesTypeDef",
    "ClientStartMatchmakingPlayersTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketTypeDef",
    "ClientStartMatchmakingResponseTypeDef",
    "ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    "ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    "ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    "ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef",
    "ClientStopGameSessionPlacementResponseTypeDef",
    "ClientUpdateAliasResponseAliasRoutingStrategyTypeDef",
    "ClientUpdateAliasResponseAliasTypeDef",
    "ClientUpdateAliasResponseTypeDef",
    "ClientUpdateAliasRoutingStrategyTypeDef",
    "ClientUpdateBuildResponseBuildTypeDef",
    "ClientUpdateBuildResponseTypeDef",
    "ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef",
    "ClientUpdateFleetAttributesResponseTypeDef",
    "ClientUpdateFleetCapacityResponseTypeDef",
    "ClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef",
    "ClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef",
    "ClientUpdateFleetPortSettingsResponseTypeDef",
    "ClientUpdateGameSessionQueueDestinationsTypeDef",
    "ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    "ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    "ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    "ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef",
    "ClientUpdateGameSessionQueueResponseTypeDef",
    "ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef",
    "ClientUpdateGameSessionResponseGameSessionTypeDef",
    "ClientUpdateGameSessionResponseTypeDef",
    "ClientUpdateMatchmakingConfigurationGamePropertiesTypeDef",
    "ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    "ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef",
    "ClientUpdateMatchmakingConfigurationResponseTypeDef",
    "ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    "ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    "ClientUpdateRuntimeConfigurationResponseTypeDef",
    "ClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef",
    "ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef",
    "ClientUpdateScriptResponseScriptStorageLocationTypeDef",
    "ClientUpdateScriptResponseScriptTypeDef",
    "ClientUpdateScriptResponseTypeDef",
    "ClientUpdateScriptStorageLocationTypeDef",
    "ClientValidateMatchmakingRuleSetResponseTypeDef",
    "DescribeFleetAttributesPaginatePaginationConfigTypeDef",
    "DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef",
    "DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    "DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef",
    "DescribeFleetAttributesPaginateResponseTypeDef",
    "DescribeFleetCapacityPaginatePaginationConfigTypeDef",
    "DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef",
    "DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef",
    "DescribeFleetCapacityPaginateResponseTypeDef",
    "DescribeFleetEventsPaginatePaginationConfigTypeDef",
    "DescribeFleetEventsPaginateResponseEventsTypeDef",
    "DescribeFleetEventsPaginateResponseTypeDef",
    "DescribeFleetUtilizationPaginatePaginationConfigTypeDef",
    "DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef",
    "DescribeFleetUtilizationPaginateResponseTypeDef",
    "DescribeGameSessionDetailsPaginatePaginationConfigTypeDef",
    "DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    "DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef",
    "DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef",
    "DescribeGameSessionDetailsPaginateResponseTypeDef",
    "DescribeGameSessionQueuesPaginatePaginationConfigTypeDef",
    "DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef",
    "DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    "DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef",
    "DescribeGameSessionQueuesPaginateResponseTypeDef",
    "DescribeGameSessionsPaginatePaginationConfigTypeDef",
    "DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    "DescribeGameSessionsPaginateResponseGameSessionsTypeDef",
    "DescribeGameSessionsPaginateResponseTypeDef",
    "DescribeInstancesPaginatePaginationConfigTypeDef",
    "DescribeInstancesPaginateResponseInstancesTypeDef",
    "DescribeInstancesPaginateResponseTypeDef",
    "DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef",
    "DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef",
    "DescribeMatchmakingConfigurationsPaginateResponseTypeDef",
    "DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef",
    "DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef",
    "DescribeMatchmakingRuleSetsPaginateResponseTypeDef",
    "DescribePlayerSessionsPaginatePaginationConfigTypeDef",
    "DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef",
    "DescribePlayerSessionsPaginateResponseTypeDef",
    "DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
    "DescribeScalingPoliciesPaginateResponseTypeDef",
    "ListAliasesPaginatePaginationConfigTypeDef",
    "ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef",
    "ListAliasesPaginateResponseAliasesTypeDef",
    "ListAliasesPaginateResponseTypeDef",
    "ListBuildsPaginatePaginationConfigTypeDef",
    "ListBuildsPaginateResponseBuildsTypeDef",
    "ListBuildsPaginateResponseTypeDef",
    "ListFleetsPaginatePaginationConfigTypeDef",
    "ListFleetsPaginateResponseTypeDef",
    "SearchGameSessionsPaginatePaginationConfigTypeDef",
    "SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    "SearchGameSessionsPaginateResponseGameSessionsTypeDef",
    "SearchGameSessionsPaginateResponseTypeDef",
)


_ClientCreateAliasResponseAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientCreateAliasResponseAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)


class ClientCreateAliasResponseAliasRoutingStrategyTypeDef(
    _ClientCreateAliasResponseAliasRoutingStrategyTypeDef
):
    pass


_ClientCreateAliasResponseAliasTypeDef = TypedDict(
    "_ClientCreateAliasResponseAliasTypeDef",
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


class ClientCreateAliasResponseAliasTypeDef(_ClientCreateAliasResponseAliasTypeDef):
    """
    - **Alias** *(dict) --*

      Object that describes the newly created alias record.
      - **AliasId** *(string) --*

        Unique identifier for an alias; alias IDs are unique within a region.
    """


_ClientCreateAliasResponseTypeDef = TypedDict(
    "_ClientCreateAliasResponseTypeDef",
    {"Alias": ClientCreateAliasResponseAliasTypeDef},
    total=False,
)


class ClientCreateAliasResponseTypeDef(_ClientCreateAliasResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Alias** *(dict) --*

        Object that describes the newly created alias record.
        - **AliasId** *(string) --*

          Unique identifier for an alias; alias IDs are unique within a region.
    """


_ClientCreateAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientCreateAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)


class ClientCreateAliasRoutingStrategyTypeDef(_ClientCreateAliasRoutingStrategyTypeDef):
    """
    Object that specifies the fleet and routing type to use for the alias.
    - **Type** *(string) --*

      Type of routing strategy.
      Possible routing types include the following:
      * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active
      fleets.
      * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a
      message to the user. A terminal alias throws a TerminalRoutingStrategyException with the
      RoutingStrategy message embedded.
    """


_ClientCreateBuildResponseBuildTypeDef = TypedDict(
    "_ClientCreateBuildResponseBuildTypeDef",
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


class ClientCreateBuildResponseBuildTypeDef(_ClientCreateBuildResponseBuildTypeDef):
    """
    - **Build** *(dict) --*

      The newly created build record, including a unique build ID and status.
      - **BuildId** *(string) --*

        Unique identifier for a build.
    """


_ClientCreateBuildResponseStorageLocationTypeDef = TypedDict(
    "_ClientCreateBuildResponseStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientCreateBuildResponseStorageLocationTypeDef(
    _ClientCreateBuildResponseStorageLocationTypeDef
):
    pass


_ClientCreateBuildResponseUploadCredentialsTypeDef = TypedDict(
    "_ClientCreateBuildResponseUploadCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str},
    total=False,
)


class ClientCreateBuildResponseUploadCredentialsTypeDef(
    _ClientCreateBuildResponseUploadCredentialsTypeDef
):
    pass


_ClientCreateBuildResponseTypeDef = TypedDict(
    "_ClientCreateBuildResponseTypeDef",
    {
        "Build": ClientCreateBuildResponseBuildTypeDef,
        "UploadCredentials": ClientCreateBuildResponseUploadCredentialsTypeDef,
        "StorageLocation": ClientCreateBuildResponseStorageLocationTypeDef,
    },
    total=False,
)


class ClientCreateBuildResponseTypeDef(_ClientCreateBuildResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Build** *(dict) --*

        The newly created build record, including a unique build ID and status.
        - **BuildId** *(string) --*

          Unique identifier for a build.
    """


_ClientCreateBuildStorageLocationTypeDef = TypedDict(
    "_ClientCreateBuildStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientCreateBuildStorageLocationTypeDef(_ClientCreateBuildStorageLocationTypeDef):
    """
    Information indicating where your game build files are stored. Use this parameter only when
    creating a build with files stored in an Amazon S3 bucket that you own. The storage location
    must specify an Amazon S3 bucket name and key, as well as a the ARN for a role that you set up
    to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket must be in the same
    region that you want to create a new build in.
    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.
    """


_ClientCreateFleetCertificateConfigurationTypeDef = TypedDict(
    "_ClientCreateFleetCertificateConfigurationTypeDef",
    {"CertificateType": Literal["DISABLED", "GENERATED"]},
)


class ClientCreateFleetCertificateConfigurationTypeDef(
    _ClientCreateFleetCertificateConfigurationTypeDef
):
    """
    - **CertificateType** *(string) --***[REQUIRED]**
    """


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
    """
    - *(dict) --*

      A range of IP addresses and port settings that allow inbound traffic to connect to server
      processes on an Amazon GameLift. New game sessions that are started on the fleet are assigned
      an IP address/port number combination, which must fall into the fleet's allowed ranges. For
      fleets created with a custom game server, the ranges reflect the server's game session
      assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges,
      one for TCP messaging and one for UDP for use by the Realtime servers.
      - **FromPort** *(integer) --***[REQUIRED]**

        Starting value for a range of allowed port numbers.
    """


_ClientCreateFleetResourceCreationLimitPolicyTypeDef = TypedDict(
    "_ClientCreateFleetResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class ClientCreateFleetResourceCreationLimitPolicyTypeDef(
    _ClientCreateFleetResourceCreationLimitPolicyTypeDef
):
    """
    Policy that limits the number of game sessions an individual player can create over a span of
    time for this fleet.
    - **NewGameSessionsPerCreator** *(integer) --*

      Maximum number of game sessions that an individual can create during the policy period.
    """


_ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef",
    {"CertificateType": Literal["DISABLED", "GENERATED"]},
    total=False,
)


class ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef(
    _ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef
):
    pass


_ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef(
    _ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef
):
    pass


_ClientCreateFleetResponseFleetAttributesTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetAttributesTypeDef",
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


class ClientCreateFleetResponseFleetAttributesTypeDef(
    _ClientCreateFleetResponseFleetAttributesTypeDef
):
    """
    - **FleetAttributes** *(dict) --*

      Properties for the newly created fleet.
      - **FleetId** *(string) --*

        Unique identifier for a fleet.
    """


_ClientCreateFleetResponseTypeDef = TypedDict(
    "_ClientCreateFleetResponseTypeDef",
    {"FleetAttributes": ClientCreateFleetResponseFleetAttributesTypeDef},
    total=False,
)


class ClientCreateFleetResponseTypeDef(_ClientCreateFleetResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetAttributes** *(dict) --*

        Properties for the newly created fleet.
        - **FleetId** *(string) --*

          Unique identifier for a fleet.
    """


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
    """
    - *(dict) --*

      A set of instructions for launching server processes on each instance in a fleet. Server
      processes run either a custom game build executable or a Realtime Servers script. Each
      instruction set identifies the location of the custom game build executable or Realtime launch
      script, optional launch parameters, and the number of server processes with this configuration
      to maintain concurrently on the instance. Server process configurations make up a fleet's ``
      RuntimeConfiguration `` .
      - **LaunchPath** *(string) --***[REQUIRED]**

        Location of the server executable in a custom game build or the name of the Realtime script
        file that contains the ``Init()`` function. Game builds and Realtime scripts are installed
        on instances at the root:
        * Windows (for custom game builds only): ``C:\\game`` . Example:
        "``C:\\game\\MyGame\\server.exe`` "
        * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
        "``/local/game/MyRealtimeScript.js`` "
    """


_ClientCreateFleetRuntimeConfigurationTypeDef = TypedDict(
    "_ClientCreateFleetRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[ClientCreateFleetRuntimeConfigurationServerProcessesTypeDef],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)


class ClientCreateFleetRuntimeConfigurationTypeDef(_ClientCreateFleetRuntimeConfigurationTypeDef):
    """
    Instructions for launching server processes on each instance in the fleet. Server processes run
    either a custom game build executable or a Realtime Servers script. The run-time configuration
    lists the types of server processes to run on an instance and includes the following
    configuration settings: the server executable or launch script file, launch parameters, and the
    number of processes to run concurrently on each instance. A CreateFleet request must include a
    run-time configuration with at least one server process configuration.
    - **ServerProcesses** *(list) --*

      Collection of server process configurations that describe which server processes to run on
      each instance in a fleet.
      - *(dict) --*

        A set of instructions for launching server processes on each instance in a fleet. Server
        processes run either a custom game build executable or a Realtime Servers script. Each
        instruction set identifies the location of the custom game build executable or Realtime
        launch script, optional launch parameters, and the number of server processes with this
        configuration to maintain concurrently on the instance. Server process configurations make
        up a fleet's ``  RuntimeConfiguration `` .
        - **LaunchPath** *(string) --***[REQUIRED]**

          Location of the server executable in a custom game build or the name of the Realtime
          script file that contains the ``Init()`` function. Game builds and Realtime scripts are
          installed on instances at the root:
          * Windows (for custom game builds only): ``C:\\game`` . Example:
          "``C:\\game\\MyGame\\server.exe`` "
          * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
          "``/local/game/MyRealtimeScript.js`` "
    """


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
    """
    - *(dict) --*

      Set of key-value pairs that contain information about a game session. When included in a game
      session request, these properties communicate details to be used when setting up the new game
      session, such as to specify a game mode, level, or map. Game properties are passed to the game
      server process when initiating a new game session; the server process uses the properties as
      appropriate. For more information, see the `Amazon GameLift Developer Guide
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
      .
      - **Key** *(string) --***[REQUIRED]**

        Game property identifier.
    """


_ClientCreateGameSessionQueueDestinationsTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueDestinationsTypeDef", {"DestinationArn": str}, total=False
)


class ClientCreateGameSessionQueueDestinationsTypeDef(
    _ClientCreateGameSessionQueueDestinationsTypeDef
):
    """
    - *(dict) --*

      Fleet designated in a game session queue. Requests for new game sessions in the queue are
      fulfilled by starting a new game session on any destination configured for a queue.
      *  CreateGameSessionQueue
      *  DescribeGameSessionQueues
      *  UpdateGameSessionQueue
      *  DeleteGameSessionQueue
      - **DestinationArn** *(string) --*

        Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID
        or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef(
    _ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef
):
    """
    - *(dict) --*

      Queue setting that determines the highest latency allowed for individual players when placing
      a game session. When a latency policy is in force, a game session cannot be placed at any
      destination in a region where a player is reporting latency higher than the cap. Latency
      policies are only enforced when the placement request contains player latency information.
      *  CreateGameSessionQueue
      *  DescribeGameSessionQueues
      *  UpdateGameSessionQueue
      *  DeleteGameSessionQueue
      - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

        The maximum latency value that is allowed for any player, in milliseconds. All policies must
        have a value set for this property.
    """


_ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef(
    _ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef
):
    pass


_ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef(
    _ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef
):
    pass


_ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef",
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


class ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef(
    _ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef
):
    """
    - **GameSessionQueue** *(dict) --*

      Object that describes the newly created game session queue.
      - **Name** *(string) --*

        Descriptive label that is associated with game session queue. Queue names must be unique
        within each region.
    """


_ClientCreateGameSessionQueueResponseTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueResponseTypeDef",
    {"GameSessionQueue": ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef},
    total=False,
)


class ClientCreateGameSessionQueueResponseTypeDef(_ClientCreateGameSessionQueueResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessionQueue** *(dict) --*

        Object that describes the newly created game session queue.
        - **Name** *(string) --*

          Descriptive label that is associated with game session queue. Queue names must be unique
          within each region.
    """


_ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef = TypedDict(
    "_ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef(
    _ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef
):
    pass


_ClientCreateGameSessionResponseGameSessionTypeDef = TypedDict(
    "_ClientCreateGameSessionResponseGameSessionTypeDef",
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


class ClientCreateGameSessionResponseGameSessionTypeDef(
    _ClientCreateGameSessionResponseGameSessionTypeDef
):
    """
    - **GameSession** *(dict) --*

      Object that describes the newly created game session record.
      - **GameSessionId** *(string) --*

        Unique identifier for the game session. A game session ARN has the following format:
        ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
        token>`` .
    """


_ClientCreateGameSessionResponseTypeDef = TypedDict(
    "_ClientCreateGameSessionResponseTypeDef",
    {"GameSession": ClientCreateGameSessionResponseGameSessionTypeDef},
    total=False,
)


class ClientCreateGameSessionResponseTypeDef(_ClientCreateGameSessionResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSession** *(dict) --*

        Object that describes the newly created game session record.
        - **GameSessionId** *(string) --*

          Unique identifier for the game session. A game session ARN has the following format:
          ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
          token>`` .
    """


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
    """
    - *(dict) --*

      Set of key-value pairs that contain information about a game session. When included in a game
      session request, these properties communicate details to be used when setting up the new game
      session, such as to specify a game mode, level, or map. Game properties are passed to the game
      server process when initiating a new game session; the server process uses the properties as
      appropriate. For more information, see the `Amazon GameLift Developer Guide
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
      .
      - **Key** *(string) --***[REQUIRED]**

        Game property identifier.
    """


_ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef = TypedDict(
    "_ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef(
    _ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef
):
    pass


_ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef = TypedDict(
    "_ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef",
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


class ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef(
    _ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef
):
    """
    - **Configuration** *(dict) --*

      Object that describes the newly created matchmaking configuration.
      - **Name** *(string) --*

        Unique identifier for a matchmaking configuration. This name is used to identify the
        configuration associated with a matchmaking request or ticket.
    """


_ClientCreateMatchmakingConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateMatchmakingConfigurationResponseTypeDef",
    {"Configuration": ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef},
    total=False,
)


class ClientCreateMatchmakingConfigurationResponseTypeDef(
    _ClientCreateMatchmakingConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Configuration** *(dict) --*

        Object that describes the newly created matchmaking configuration.
        - **Name** *(string) --*

          Unique identifier for a matchmaking configuration. This name is used to identify the
          configuration associated with a matchmaking request or ticket.
    """


_ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef = TypedDict(
    "_ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef",
    {"RuleSetName": str, "RuleSetBody": str, "CreationTime": datetime},
    total=False,
)


class ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef(
    _ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef
):
    """
    - **RuleSet** *(dict) --*

      Object that describes the newly created matchmaking rule set.
      - **RuleSetName** *(string) --*

        Unique identifier for a matchmaking rule set
    """


_ClientCreateMatchmakingRuleSetResponseTypeDef = TypedDict(
    "_ClientCreateMatchmakingRuleSetResponseTypeDef",
    {"RuleSet": ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef},
    total=False,
)


class ClientCreateMatchmakingRuleSetResponseTypeDef(_ClientCreateMatchmakingRuleSetResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **RuleSet** *(dict) --*

        Object that describes the newly created matchmaking rule set.
        - **RuleSetName** *(string) --*

          Unique identifier for a matchmaking rule set
    """


_ClientCreatePlayerSessionResponsePlayerSessionTypeDef = TypedDict(
    "_ClientCreatePlayerSessionResponsePlayerSessionTypeDef",
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


class ClientCreatePlayerSessionResponsePlayerSessionTypeDef(
    _ClientCreatePlayerSessionResponsePlayerSessionTypeDef
):
    """
    - **PlayerSession** *(dict) --*

      Object that describes the newly created player session record.
      - **PlayerSessionId** *(string) --*

        Unique identifier for a player session.
    """


_ClientCreatePlayerSessionResponseTypeDef = TypedDict(
    "_ClientCreatePlayerSessionResponseTypeDef",
    {"PlayerSession": ClientCreatePlayerSessionResponsePlayerSessionTypeDef},
    total=False,
)


class ClientCreatePlayerSessionResponseTypeDef(_ClientCreatePlayerSessionResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **PlayerSession** *(dict) --*

        Object that describes the newly created player session record.
        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session.
    """


_ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef = TypedDict(
    "_ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef",
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


class ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef(
    _ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef
):
    """
    - *(dict) --*

      Properties describing a player session. Player session objects are created either by creating
      a player session for a specific game session, or as part of a game session placement. A player
      session represents either a player reservation for a game session (status ``RESERVED`` ) or
      actual player activity in a game session (status ``ACTIVE`` ). A player session object
      (including player data) is automatically passed to a game session when the player connects to
      the game session and is validated.
      When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
      session ends, the player session object is retained for 30 days and then removed.
      *  CreatePlayerSession
      *  CreatePlayerSessions
      *  DescribePlayerSessions
      * Game session placements

        *  StartGameSessionPlacement
        *  DescribeGameSessionPlacement
        *  StopGameSessionPlacement
    """


_ClientCreatePlayerSessionsResponseTypeDef = TypedDict(
    "_ClientCreatePlayerSessionsResponseTypeDef",
    {"PlayerSessions": List[ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef]},
    total=False,
)


class ClientCreatePlayerSessionsResponseTypeDef(_ClientCreatePlayerSessionsResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **PlayerSessions** *(list) --*

        Collection of player session objects created for the added players.
        - *(dict) --*

          Properties describing a player session. Player session objects are created either by
          creating a player session for a specific game session, or as part of a game session
          placement. A player session represents either a player reservation for a game session
          (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A
          player session object (including player data) is automatically passed to a game session
          when the player connects to the game session and is validated.
          When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
          session ends, the player session object is retained for 30 days and then removed.
          *  CreatePlayerSession
          *  CreatePlayerSessions
          *  DescribePlayerSessions
          * Game session placements

            *  StartGameSessionPlacement
            *  DescribeGameSessionPlacement
            *  StopGameSessionPlacement
    """


_ClientCreateScriptResponseScriptStorageLocationTypeDef = TypedDict(
    "_ClientCreateScriptResponseScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientCreateScriptResponseScriptStorageLocationTypeDef(
    _ClientCreateScriptResponseScriptStorageLocationTypeDef
):
    pass


_ClientCreateScriptResponseScriptTypeDef = TypedDict(
    "_ClientCreateScriptResponseScriptTypeDef",
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


class ClientCreateScriptResponseScriptTypeDef(_ClientCreateScriptResponseScriptTypeDef):
    """
    - **Script** *(dict) --*

      The newly created script record with a unique script ID. The new script's storage location
      reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your
      account, the storage location reflects the information that was provided in the *CreateScript*
      request; (2) If the script file was uploaded from a local zip file, the storage location
      reflects an S3 location controls by the Amazon GameLift service.
      - **ScriptId** *(string) --*

        Unique identifier for a Realtime script
    """


_ClientCreateScriptResponseTypeDef = TypedDict(
    "_ClientCreateScriptResponseTypeDef",
    {"Script": ClientCreateScriptResponseScriptTypeDef},
    total=False,
)


class ClientCreateScriptResponseTypeDef(_ClientCreateScriptResponseTypeDef):
    """
    - *(dict) --*

      - **Script** *(dict) --*

        The newly created script record with a unique script ID. The new script's storage location
        reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your
        account, the storage location reflects the information that was provided in the
        *CreateScript* request; (2) If the script file was uploaded from a local zip file, the
        storage location reflects an S3 location controls by the Amazon GameLift service.
        - **ScriptId** *(string) --*

          Unique identifier for a Realtime script
    """


_ClientCreateScriptStorageLocationTypeDef = TypedDict(
    "_ClientCreateScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientCreateScriptStorageLocationTypeDef(_ClientCreateScriptStorageLocationTypeDef):
    """
    Location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored.
    The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and
    a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket
    must be in the same region where you want to create a new script. By default, Amazon GameLift
    uploads the latest version of the zip file; if you have S3 object versioning turned on, you can
    use the ``ObjectVersion`` parameter to specify an earlier version.
    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.
    """


_ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef = TypedDict(
    "_ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)


class ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef(
    _ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef
):
    """
    - **VpcPeeringAuthorization** *(dict) --*

      Details on the requested VPC peering authorization, including expiration.
      - **GameLiftAwsAccountId** *(string) --*

        Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You
        can find your Account ID in the AWS Management Console under account settings.
    """


_ClientCreateVpcPeeringAuthorizationResponseTypeDef = TypedDict(
    "_ClientCreateVpcPeeringAuthorizationResponseTypeDef",
    {
        "VpcPeeringAuthorization": ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef
    },
    total=False,
)


class ClientCreateVpcPeeringAuthorizationResponseTypeDef(
    _ClientCreateVpcPeeringAuthorizationResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **VpcPeeringAuthorization** *(dict) --*

        Details on the requested VPC peering authorization, including expiration.
        - **GameLiftAwsAccountId** *(string) --*

          Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet.
          You can find your Account ID in the AWS Management Console under account settings.
    """


_ClientDescribeAliasResponseAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientDescribeAliasResponseAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)


class ClientDescribeAliasResponseAliasRoutingStrategyTypeDef(
    _ClientDescribeAliasResponseAliasRoutingStrategyTypeDef
):
    pass


_ClientDescribeAliasResponseAliasTypeDef = TypedDict(
    "_ClientDescribeAliasResponseAliasTypeDef",
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


class ClientDescribeAliasResponseAliasTypeDef(_ClientDescribeAliasResponseAliasTypeDef):
    """
    - **Alias** *(dict) --*

      Object that contains the requested alias.
      - **AliasId** *(string) --*

        Unique identifier for an alias; alias IDs are unique within a region.
    """


_ClientDescribeAliasResponseTypeDef = TypedDict(
    "_ClientDescribeAliasResponseTypeDef",
    {"Alias": ClientDescribeAliasResponseAliasTypeDef},
    total=False,
)


class ClientDescribeAliasResponseTypeDef(_ClientDescribeAliasResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Alias** *(dict) --*

        Object that contains the requested alias.
        - **AliasId** *(string) --*

          Unique identifier for an alias; alias IDs are unique within a region.
    """


_ClientDescribeBuildResponseBuildTypeDef = TypedDict(
    "_ClientDescribeBuildResponseBuildTypeDef",
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


class ClientDescribeBuildResponseBuildTypeDef(_ClientDescribeBuildResponseBuildTypeDef):
    """
    - **Build** *(dict) --*

      Set of properties describing the requested build.
      - **BuildId** *(string) --*

        Unique identifier for a build.
    """


_ClientDescribeBuildResponseTypeDef = TypedDict(
    "_ClientDescribeBuildResponseTypeDef",
    {"Build": ClientDescribeBuildResponseBuildTypeDef},
    total=False,
)


class ClientDescribeBuildResponseTypeDef(_ClientDescribeBuildResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Build** *(dict) --*

        Set of properties describing the requested build.
        - **BuildId** *(string) --*

          Unique identifier for a build.
    """


_ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef = TypedDict(
    "_ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef",
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


class ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef(
    _ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef
):
    """
    - *(dict) --*

      Maximum number of instances allowed based on the Amazon Elastic Compute Cloud (Amazon EC2)
      instance type. Instance limits can be retrieved by calling  DescribeEC2InstanceLimits .
      - **EC2InstanceType** *(string) --*

        Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type
        determines the computing resources of each instance in the fleet, including CPU, memory,
        storage, and networking capacity. Amazon GameLift supports the following EC2 instance types.
        See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for detailed
        descriptions.
    """


_ClientDescribeEc2InstanceLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeEc2InstanceLimitsResponseTypeDef",
    {"EC2InstanceLimits": List[ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef]},
    total=False,
)


class ClientDescribeEc2InstanceLimitsResponseTypeDef(
    _ClientDescribeEc2InstanceLimitsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **EC2InstanceLimits** *(list) --*

        Object that contains the maximum number of instances for the specified instance type.
        - *(dict) --*

          Maximum number of instances allowed based on the Amazon Elastic Compute Cloud (Amazon EC2)
          instance type. Instance limits can be retrieved by calling  DescribeEC2InstanceLimits .
          - **EC2InstanceType** *(string) --*

            Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type
            determines the computing resources of each instance in the fleet, including CPU, memory,
            storage, and networking capacity. Amazon GameLift supports the following EC2 instance
            types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for
            detailed descriptions.
    """


_ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef = TypedDict(
    "_ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef",
    {"CertificateType": Literal["DISABLED", "GENERATED"]},
    total=False,
)


class ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef(
    _ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef
):
    pass


_ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "_ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef(
    _ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef
):
    pass


_ClientDescribeFleetAttributesResponseFleetAttributesTypeDef = TypedDict(
    "_ClientDescribeFleetAttributesResponseFleetAttributesTypeDef",
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


class ClientDescribeFleetAttributesResponseFleetAttributesTypeDef(
    _ClientDescribeFleetAttributesResponseFleetAttributesTypeDef
):
    """
    - *(dict) --*

      General properties describing a fleet.
      *  CreateFleet
      *  ListFleets
      *  DeleteFleet
      * Describe fleets:

        *  DescribeFleetAttributes
        *  DescribeFleetCapacity
        *  DescribeFleetPortSettings
        *  DescribeFleetUtilization
        *  DescribeRuntimeConfiguration
        *  DescribeEC2InstanceLimits
        *  DescribeFleetEvents
    """


_ClientDescribeFleetAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeFleetAttributesResponseTypeDef",
    {
        "FleetAttributes": List[ClientDescribeFleetAttributesResponseFleetAttributesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeFleetAttributesResponseTypeDef(_ClientDescribeFleetAttributesResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetAttributes** *(list) --*

        Collection of objects containing attribute metadata for each requested fleet ID.
        - *(dict) --*

          General properties describing a fleet.
          *  CreateFleet
          *  ListFleets
          *  DeleteFleet
          * Describe fleets:

            *  DescribeFleetAttributes
            *  DescribeFleetCapacity
            *  DescribeFleetPortSettings
            *  DescribeFleetUtilization
            *  DescribeRuntimeConfiguration
            *  DescribeEC2InstanceLimits
            *  DescribeFleetEvents
    """


_ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef = TypedDict(
    "_ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef",
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


class ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef(
    _ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef
):
    pass


_ClientDescribeFleetCapacityResponseFleetCapacityTypeDef = TypedDict(
    "_ClientDescribeFleetCapacityResponseFleetCapacityTypeDef",
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


class ClientDescribeFleetCapacityResponseFleetCapacityTypeDef(
    _ClientDescribeFleetCapacityResponseFleetCapacityTypeDef
):
    """
    - *(dict) --*

      Information about the fleet's capacity. Fleet capacity is measured in EC2 instances. By
      default, new fleets have a capacity of one instance, but can be updated as needed. The maximum
      number of instances for a fleet is determined by the fleet's instance type.
      *  CreateFleet
      *  ListFleets
      *  DeleteFleet
      * Describe fleets:

        *  DescribeFleetAttributes
        *  DescribeFleetCapacity
        *  DescribeFleetPortSettings
        *  DescribeFleetUtilization
        *  DescribeRuntimeConfiguration
        *  DescribeEC2InstanceLimits
        *  DescribeFleetEvents
    """


_ClientDescribeFleetCapacityResponseTypeDef = TypedDict(
    "_ClientDescribeFleetCapacityResponseTypeDef",
    {
        "FleetCapacity": List[ClientDescribeFleetCapacityResponseFleetCapacityTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeFleetCapacityResponseTypeDef(_ClientDescribeFleetCapacityResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetCapacity** *(list) --*

        Collection of objects containing capacity information for each requested fleet ID. Leave
        this parameter empty to retrieve capacity information for all fleets.
        - *(dict) --*

          Information about the fleet's capacity. Fleet capacity is measured in EC2 instances. By
          default, new fleets have a capacity of one instance, but can be updated as needed. The
          maximum number of instances for a fleet is determined by the fleet's instance type.
          *  CreateFleet
          *  ListFleets
          *  DeleteFleet
          * Describe fleets:

            *  DescribeFleetAttributes
            *  DescribeFleetCapacity
            *  DescribeFleetPortSettings
            *  DescribeFleetUtilization
            *  DescribeRuntimeConfiguration
            *  DescribeEC2InstanceLimits
            *  DescribeFleetEvents
    """


_ClientDescribeFleetEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeFleetEventsResponseEventsTypeDef",
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


class ClientDescribeFleetEventsResponseEventsTypeDef(
    _ClientDescribeFleetEventsResponseEventsTypeDef
):
    """
    - *(dict) --*

      Log entry describing an event that involves Amazon GameLift resources (such as a fleet). In
      addition to tracking activity, event codes and messages can provide additional information for
      troubleshooting and debugging problems.
      - **EventId** *(string) --*

        Unique identifier for a fleet event.
    """


_ClientDescribeFleetEventsResponseTypeDef = TypedDict(
    "_ClientDescribeFleetEventsResponseTypeDef",
    {"Events": List[ClientDescribeFleetEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeFleetEventsResponseTypeDef(_ClientDescribeFleetEventsResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Events** *(list) --*

        Collection of objects containing event log entries for the specified fleet.
        - *(dict) --*

          Log entry describing an event that involves Amazon GameLift resources (such as a fleet).
          In addition to tracking activity, event codes and messages can provide additional
          information for troubleshooting and debugging problems.
          - **EventId** *(string) --*

            Unique identifier for a fleet event.
    """


_ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef = TypedDict(
    "_ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef",
    {"FromPort": int, "ToPort": int, "IpRange": str, "Protocol": Literal["TCP", "UDP"]},
    total=False,
)


class ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef(
    _ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef
):
    """
    - *(dict) --*

      A range of IP addresses and port settings that allow inbound traffic to connect to server
      processes on an Amazon GameLift. New game sessions that are started on the fleet are assigned
      an IP address/port number combination, which must fall into the fleet's allowed ranges. For
      fleets created with a custom game server, the ranges reflect the server's game session
      assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges,
      one for TCP messaging and one for UDP for use by the Realtime servers.
      - **FromPort** *(integer) --*

        Starting value for a range of allowed port numbers.
    """


_ClientDescribeFleetPortSettingsResponseTypeDef = TypedDict(
    "_ClientDescribeFleetPortSettingsResponseTypeDef",
    {"InboundPermissions": List[ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef]},
    total=False,
)


class ClientDescribeFleetPortSettingsResponseTypeDef(
    _ClientDescribeFleetPortSettingsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **InboundPermissions** *(list) --*

        Object that contains port settings for the requested fleet ID.
        - *(dict) --*

          A range of IP addresses and port settings that allow inbound traffic to connect to server
          processes on an Amazon GameLift. New game sessions that are started on the fleet are
          assigned an IP address/port number combination, which must fall into the fleet's allowed
          ranges. For fleets created with a custom game server, the ranges reflect the server's game
          session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two
          port ranges, one for TCP messaging and one for UDP for use by the Realtime servers.
          - **FromPort** *(integer) --*

            Starting value for a range of allowed port numbers.
    """


_ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef = TypedDict(
    "_ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef",
    {
        "FleetId": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
    },
    total=False,
)


class ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef(
    _ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef
):
    """
    - *(dict) --*

      Current status of fleet utilization, including the number of game and player sessions being
      hosted.
      *  CreateFleet
      *  ListFleets
      *  DeleteFleet
      * Describe fleets:

        *  DescribeFleetAttributes
        *  DescribeFleetCapacity
        *  DescribeFleetPortSettings
        *  DescribeFleetUtilization
        *  DescribeRuntimeConfiguration
        *  DescribeEC2InstanceLimits
        *  DescribeFleetEvents
    """


_ClientDescribeFleetUtilizationResponseTypeDef = TypedDict(
    "_ClientDescribeFleetUtilizationResponseTypeDef",
    {
        "FleetUtilization": List[ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeFleetUtilizationResponseTypeDef(_ClientDescribeFleetUtilizationResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetUtilization** *(list) --*

        Collection of objects containing utilization information for each requested fleet ID.
        - *(dict) --*

          Current status of fleet utilization, including the number of game and player sessions
          being hosted.
          *  CreateFleet
          *  ListFleets
          *  DeleteFleet
          * Describe fleets:

            *  DescribeFleetAttributes
            *  DescribeFleetCapacity
            *  DescribeFleetPortSettings
            *  DescribeFleetUtilization
            *  DescribeRuntimeConfiguration
            *  DescribeEC2InstanceLimits
            *  DescribeFleetEvents
    """


_ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef = TypedDict(
    "_ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef(
    _ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef
):
    pass


_ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef = TypedDict(
    "_ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef",
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


class ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef(
    _ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef
):
    """
    - **GameSession** *(dict) --*

      Object that describes a game session.
      - **GameSessionId** *(string) --*

        Unique identifier for the game session. A game session ARN has the following format:
        ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
        token>`` .
    """


_ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef = TypedDict(
    "_ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef",
    {
        "GameSession": ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef,
        "ProtectionPolicy": Literal["NoProtection", "FullProtection"],
    },
    total=False,
)


class ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef(
    _ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef
):
    """
    - *(dict) --*

      A game session's properties plus the protection policy currently in force.
      - **GameSession** *(dict) --*

        Object that describes a game session.
        - **GameSessionId** *(string) --*

          Unique identifier for the game session. A game session ARN has the following format:
          ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
          token>`` .
    """


_ClientDescribeGameSessionDetailsResponseTypeDef = TypedDict(
    "_ClientDescribeGameSessionDetailsResponseTypeDef",
    {
        "GameSessionDetails": List[
            ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeGameSessionDetailsResponseTypeDef(
    _ClientDescribeGameSessionDetailsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessionDetails** *(list) --*

        Collection of objects containing game session properties and the protection policy currently
        in force for each session matching the request.
        - *(dict) --*

          A game session's properties plus the protection policy currently in force.
          - **GameSession** *(dict) --*

            Object that describes a game session.
            - **GameSessionId** *(string) --*

              Unique identifier for the game session. A game session ARN has the following format:
              ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
              token>`` .
    """


_ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef(
    _ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
):
    pass


_ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef(
    _ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
):
    pass


_ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": Any},
    total=False,
)


class ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef(
    _ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
):
    pass


_ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef",
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


class ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef(
    _ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef
):
    """
    - **GameSessionPlacement** *(dict) --*

      Object that describes the requested game session placement.
      - **PlacementId** *(string) --*

        Unique identifier for a game session placement.
    """


_ClientDescribeGameSessionPlacementResponseTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseTypeDef",
    {"GameSessionPlacement": ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef},
    total=False,
)


class ClientDescribeGameSessionPlacementResponseTypeDef(
    _ClientDescribeGameSessionPlacementResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessionPlacement** *(dict) --*

        Object that describes the requested game session placement.
        - **PlacementId** *(string) --*

          Unique identifier for a game session placement.
    """


_ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef = TypedDict(
    "_ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef(
    _ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef
):
    pass


_ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef(
    _ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef
):
    pass


_ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef = TypedDict(
    "_ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef",
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


class ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef(
    _ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef
):
    """
    - *(dict) --*

      Configuration of a queue that is used to process game session placement requests. The queue
      configuration identifies several game features:
      * The destinations where a new game session can potentially be hosted. Amazon GameLift tries
      these destinations in an order based on either the queue's default order or player latency
      information, if provided in a placement request. With latency information, Amazon GameLift can
      place game sessions where the majority of players are reporting the lowest possible latency.
      * The length of time that placement requests can wait in the queue before timing out.
      * A set of optional latency policies that protect individual players from high latencies,
      preventing game sessions from being placed where any individual player is reporting latency
      higher than a policy's maximum.
      *  CreateGameSessionQueue
      *  DescribeGameSessionQueues
      *  UpdateGameSessionQueue
      *  DeleteGameSessionQueue
      - **Name** *(string) --*

        Descriptive label that is associated with game session queue. Queue names must be unique
        within each region.
    """


_ClientDescribeGameSessionQueuesResponseTypeDef = TypedDict(
    "_ClientDescribeGameSessionQueuesResponseTypeDef",
    {
        "GameSessionQueues": List[ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeGameSessionQueuesResponseTypeDef(
    _ClientDescribeGameSessionQueuesResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessionQueues** *(list) --*

        Collection of objects that describes the requested game session queues.
        - *(dict) --*

          Configuration of a queue that is used to process game session placement requests. The
          queue configuration identifies several game features:
          * The destinations where a new game session can potentially be hosted. Amazon GameLift
          tries these destinations in an order based on either the queue's default order or player
          latency information, if provided in a placement request. With latency information, Amazon
          GameLift can place game sessions where the majority of players are reporting the lowest
          possible latency.
          * The length of time that placement requests can wait in the queue before timing out.
          * A set of optional latency policies that protect individual players from high latencies,
          preventing game sessions from being placed where any individual player is reporting
          latency higher than a policy's maximum.
          *  CreateGameSessionQueue
          *  DescribeGameSessionQueues
          *  UpdateGameSessionQueue
          *  DeleteGameSessionQueue
          - **Name** *(string) --*

            Descriptive label that is associated with game session queue. Queue names must be unique
            within each region.
    """


_ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "_ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef(
    _ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef
):
    pass


_ClientDescribeGameSessionsResponseGameSessionsTypeDef = TypedDict(
    "_ClientDescribeGameSessionsResponseGameSessionsTypeDef",
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


class ClientDescribeGameSessionsResponseGameSessionsTypeDef(
    _ClientDescribeGameSessionsResponseGameSessionsTypeDef
):
    """
    - *(dict) --*

      Properties describing a game session.
      A game session in ACTIVE status can host players. When a game session ends, its status is set
      to ``TERMINATED`` .
      Once the session ends, the game session object is retained for 30 days. This means you can
      reuse idempotency token values after this time. Game session logs are retained for 14 days.
      *  CreateGameSession
      *  DescribeGameSessions
      *  DescribeGameSessionDetails
      *  SearchGameSessions
      *  UpdateGameSession
      *  GetGameSessionLogUrl
      * Game session placements

        *  StartGameSessionPlacement
        *  DescribeGameSessionPlacement
        *  StopGameSessionPlacement
    """


_ClientDescribeGameSessionsResponseTypeDef = TypedDict(
    "_ClientDescribeGameSessionsResponseTypeDef",
    {"GameSessions": List[ClientDescribeGameSessionsResponseGameSessionsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeGameSessionsResponseTypeDef(_ClientDescribeGameSessionsResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessions** *(list) --*

        Collection of objects containing game session properties for each session matching the
        request.
        - *(dict) --*

          Properties describing a game session.
          A game session in ACTIVE status can host players. When a game session ends, its status is
          set to ``TERMINATED`` .
          Once the session ends, the game session object is retained for 30 days. This means you can
          reuse idempotency token values after this time. Game session logs are retained for 14
          days.
          *  CreateGameSession
          *  DescribeGameSessions
          *  DescribeGameSessionDetails
          *  SearchGameSessions
          *  UpdateGameSession
          *  GetGameSessionLogUrl
          * Game session placements

            *  StartGameSessionPlacement
            *  DescribeGameSessionPlacement
            *  StopGameSessionPlacement
    """


_ClientDescribeInstancesResponseInstancesTypeDef = TypedDict(
    "_ClientDescribeInstancesResponseInstancesTypeDef",
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


class ClientDescribeInstancesResponseInstancesTypeDef(
    _ClientDescribeInstancesResponseInstancesTypeDef
):
    """
    - *(dict) --*

      Properties that describe an instance of a virtual computing resource that hosts one or more
      game servers. A fleet may contain zero or more instances.
      - **FleetId** *(string) --*

        Unique identifier for a fleet that the instance is in.
    """


_ClientDescribeInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeInstancesResponseTypeDef",
    {"Instances": List[ClientDescribeInstancesResponseInstancesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeInstancesResponseTypeDef(_ClientDescribeInstancesResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Instances** *(list) --*

        Collection of objects containing properties for each instance returned.
        - *(dict) --*

          Properties that describe an instance of a virtual computing resource that hosts one or
          more game servers. A fleet may contain zero or more instances.
          - **FleetId** *(string) --*

            Unique identifier for a fleet that the instance is in.
    """


_ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef = TypedDict(
    "_ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef(
    _ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef
):
    pass


_ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "_ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef",
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


class ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef(
    _ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef
):
    """
    - *(dict) --*

      Guidelines for use with FlexMatch to match players into games. All matchmaking requests must
      specify a matchmaking configuration.
      - **Name** *(string) --*

        Unique identifier for a matchmaking configuration. This name is used to identify the
        configuration associated with a matchmaking request or ticket.
    """


_ClientDescribeMatchmakingConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeMatchmakingConfigurationsResponseTypeDef",
    {
        "Configurations": List[
            ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMatchmakingConfigurationsResponseTypeDef(
    _ClientDescribeMatchmakingConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Configurations** *(list) --*

        Collection of requested matchmaking configuration objects.
        - *(dict) --*

          Guidelines for use with FlexMatch to match players into games. All matchmaking requests
          must specify a matchmaking configuration.
          - **Name** *(string) --*

            Unique identifier for a matchmaking configuration. This name is used to identify the
            configuration associated with a matchmaking request or ticket.
    """


_ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef(
    _ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
):
    pass


_ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef",
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


class ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef(
    _ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef
):
    pass


_ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef(
    _ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef
):
    pass


_ClientDescribeMatchmakingResponseTicketListPlayersTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListPlayersTypeDef",
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


class ClientDescribeMatchmakingResponseTicketListPlayersTypeDef(
    _ClientDescribeMatchmakingResponseTicketListPlayersTypeDef
):
    pass


_ClientDescribeMatchmakingResponseTicketListTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListTypeDef",
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


class ClientDescribeMatchmakingResponseTicketListTypeDef(
    _ClientDescribeMatchmakingResponseTicketListTypeDef
):
    """
    - *(dict) --*

      Ticket generated to track the progress of a matchmaking request. Each ticket is uniquely
      identified by a ticket ID, supplied by the requester, when creating a matchmaking request with
      StartMatchmaking . Tickets can be retrieved by calling  DescribeMatchmaking with the ticket
      ID.
      - **TicketId** *(string) --*

        Unique identifier for a matchmaking ticket.
    """


_ClientDescribeMatchmakingResponseTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTypeDef",
    {"TicketList": List[ClientDescribeMatchmakingResponseTicketListTypeDef]},
    total=False,
)


class ClientDescribeMatchmakingResponseTypeDef(_ClientDescribeMatchmakingResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **TicketList** *(list) --*

        Collection of existing matchmaking ticket objects matching the request.
        - *(dict) --*

          Ticket generated to track the progress of a matchmaking request. Each ticket is uniquely
          identified by a ticket ID, supplied by the requester, when creating a matchmaking request
          with  StartMatchmaking . Tickets can be retrieved by calling  DescribeMatchmaking with the
          ticket ID.
          - **TicketId** *(string) --*

            Unique identifier for a matchmaking ticket.
    """


_ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef = TypedDict(
    "_ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef",
    {"RuleSetName": str, "RuleSetBody": str, "CreationTime": datetime},
    total=False,
)


class ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef(
    _ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef
):
    """
    - *(dict) --*

      Set of rule statements, used with FlexMatch, that determine how to build your player matches.
      Each rule set describes a type of group to be created and defines the parameters for
      acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.
      A rule set may define the following elements for a match. For detailed information and
      examples showing how to construct a rule set, see `Build a FlexMatch Rule Set
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ .
      * Teams -- Required. A rule set must define one or multiple teams for the match and set
      minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that
      requires all eight slots to be filled.
      * Player attributes -- Optional. These attributes specify a set of player characteristics to
      evaluate when looking for a match. Matchmaking requests that use a rule set with player
      attributes must provide the corresponding attribute values. For example, an attribute might
      specify a player's skill or level.
      * Rules -- Optional. Rules define how to evaluate potential players for a match based on
      player attributes. A rule might specify minimum requirements for individual players, teams, or
      entire matches. For example, a rule might require each player to meet a certain skill level,
      each team to have at least one player in a certain role, or the match to have a minimum
      average skill level. or may describe an entire group--such as all teams must be evenly matched
      or have at least one player in a certain role.
      * Expansions -- Optional. Expansions allow you to relax the rules after a period of time when
      no acceptable matches are found. This feature lets you balance getting players into games in a
      reasonable amount of time instead of making them wait indefinitely for the best possible
      match. For example, you might use an expansion to increase the maximum skill variance between
      players after 30 seconds.
      - **RuleSetName** *(string) --*

        Unique identifier for a matchmaking rule set
    """


_ClientDescribeMatchmakingRuleSetsResponseTypeDef = TypedDict(
    "_ClientDescribeMatchmakingRuleSetsResponseTypeDef",
    {"RuleSets": List[ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeMatchmakingRuleSetsResponseTypeDef(
    _ClientDescribeMatchmakingRuleSetsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **RuleSets** *(list) --*

        Collection of requested matchmaking rule set objects.
        - *(dict) --*

          Set of rule statements, used with FlexMatch, that determine how to build your player
          matches. Each rule set describes a type of group to be created and defines the parameters
          for acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.
          A rule set may define the following elements for a match. For detailed information and
          examples showing how to construct a rule set, see `Build a FlexMatch Rule Set
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ .
          * Teams -- Required. A rule set must define one or multiple teams for the match and set
          minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that
          requires all eight slots to be filled.
          * Player attributes -- Optional. These attributes specify a set of player characteristics
          to evaluate when looking for a match. Matchmaking requests that use a rule set with player
          attributes must provide the corresponding attribute values. For example, an attribute
          might specify a player's skill or level.
          * Rules -- Optional. Rules define how to evaluate potential players for a match based on
          player attributes. A rule might specify minimum requirements for individual players,
          teams, or entire matches. For example, a rule might require each player to meet a certain
          skill level, each team to have at least one player in a certain role, or the match to have
          a minimum average skill level. or may describe an entire group--such as all teams must be
          evenly matched or have at least one player in a certain role.
          * Expansions -- Optional. Expansions allow you to relax the rules after a period of time
          when no acceptable matches are found. This feature lets you balance getting players into
          games in a reasonable amount of time instead of making them wait indefinitely for the best
          possible match. For example, you might use an expansion to increase the maximum skill
          variance between players after 30 seconds.
          - **RuleSetName** *(string) --*

            Unique identifier for a matchmaking rule set
    """


_ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef = TypedDict(
    "_ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef",
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


class ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef(
    _ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef
):
    """
    - *(dict) --*

      Properties describing a player session. Player session objects are created either by creating
      a player session for a specific game session, or as part of a game session placement. A player
      session represents either a player reservation for a game session (status ``RESERVED`` ) or
      actual player activity in a game session (status ``ACTIVE`` ). A player session object
      (including player data) is automatically passed to a game session when the player connects to
      the game session and is validated.
      When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
      session ends, the player session object is retained for 30 days and then removed.
      *  CreatePlayerSession
      *  CreatePlayerSessions
      *  DescribePlayerSessions
      * Game session placements

        *  StartGameSessionPlacement
        *  DescribeGameSessionPlacement
        *  StopGameSessionPlacement
    """


_ClientDescribePlayerSessionsResponseTypeDef = TypedDict(
    "_ClientDescribePlayerSessionsResponseTypeDef",
    {
        "PlayerSessions": List[ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribePlayerSessionsResponseTypeDef(_ClientDescribePlayerSessionsResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **PlayerSessions** *(list) --*

        Collection of objects containing properties for each player session that matches the
        request.
        - *(dict) --*

          Properties describing a player session. Player session objects are created either by
          creating a player session for a specific game session, or as part of a game session
          placement. A player session represents either a player reservation for a game session
          (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A
          player session object (including player data) is automatically passed to a game session
          when the player connects to the game session and is validated.
          When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
          session ends, the player session object is retained for 30 days and then removed.
          *  CreatePlayerSession
          *  CreatePlayerSessions
          *  DescribePlayerSessions
          * Game session placements

            *  StartGameSessionPlacement
            *  DescribeGameSessionPlacement
            *  StopGameSessionPlacement
    """


_ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    {"LaunchPath": str, "Parameters": str, "ConcurrentExecutions": int},
    total=False,
)


class ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef(
    _ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
):
    """
    - *(dict) --*

      A set of instructions for launching server processes on each instance in a fleet. Server
      processes run either a custom game build executable or a Realtime Servers script. Each
      instruction set identifies the location of the custom game build executable or Realtime launch
      script, optional launch parameters, and the number of server processes with this configuration
      to maintain concurrently on the instance. Server process configurations make up a fleet's ``
      RuntimeConfiguration `` .
      - **LaunchPath** *(string) --*

        Location of the server executable in a custom game build or the name of the Realtime script
        file that contains the ``Init()`` function. Game builds and Realtime scripts are installed
        on instances at the root:
        * Windows (for custom game builds only): ``C:\\game`` . Example:
        "``C:\\game\\MyGame\\server.exe`` "
        * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
        "``/local/game/MyRealtimeScript.js`` "
    """


_ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef = TypedDict(
    "_ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)


class ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef(
    _ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef
):
    """
    - **RuntimeConfiguration** *(dict) --*

      Instructions describing how server processes should be launched and maintained on each
      instance in the fleet.
      - **ServerProcesses** *(list) --*

        Collection of server process configurations that describe which server processes to run on
        each instance in a fleet.
        - *(dict) --*

          A set of instructions for launching server processes on each instance in a fleet. Server
          processes run either a custom game build executable or a Realtime Servers script. Each
          instruction set identifies the location of the custom game build executable or Realtime
          launch script, optional launch parameters, and the number of server processes with this
          configuration to maintain concurrently on the instance. Server process configurations make
          up a fleet's ``  RuntimeConfiguration `` .
          - **LaunchPath** *(string) --*

            Location of the server executable in a custom game build or the name of the Realtime
            script file that contains the ``Init()`` function. Game builds and Realtime scripts are
            installed on instances at the root:
            * Windows (for custom game builds only): ``C:\\game`` . Example:
            "``C:\\game\\MyGame\\server.exe`` "
            * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
            "``/local/game/MyRealtimeScript.js`` "
    """


_ClientDescribeRuntimeConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeRuntimeConfigurationResponseTypeDef",
    {"RuntimeConfiguration": ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef},
    total=False,
)


class ClientDescribeRuntimeConfigurationResponseTypeDef(
    _ClientDescribeRuntimeConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **RuntimeConfiguration** *(dict) --*

        Instructions describing how server processes should be launched and maintained on each
        instance in the fleet.
        - **ServerProcesses** *(list) --*

          Collection of server process configurations that describe which server processes to run on
          each instance in a fleet.
          - *(dict) --*

            A set of instructions for launching server processes on each instance in a fleet. Server
            processes run either a custom game build executable or a Realtime Servers script. Each
            instruction set identifies the location of the custom game build executable or Realtime
            launch script, optional launch parameters, and the number of server processes with this
            configuration to maintain concurrently on the instance. Server process configurations
            make up a fleet's ``  RuntimeConfiguration `` .
            - **LaunchPath** *(string) --*

              Location of the server executable in a custom game build or the name of the Realtime
              script file that contains the ``Init()`` function. Game builds and Realtime scripts
              are installed on instances at the root:
              * Windows (for custom game builds only): ``C:\\game`` . Example:
              "``C:\\game\\MyGame\\server.exe`` "
              * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
              "``/local/game/MyRealtimeScript.js`` "
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef",
    {"TargetValue": float},
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef
):
    pass


_ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
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


class ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef
):
    """
    - *(dict) --*

      Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the
      combination of name and fleet ID.
      *  DescribeFleetCapacity
      *  UpdateFleetCapacity
      *  DescribeEC2InstanceLimits
      * Manage scaling policies:

        *  PutScalingPolicy (auto-scaling)
        *  DescribeScalingPolicies (auto-scaling)
        *  DeleteScalingPolicy (auto-scaling)
    """


_ClientDescribeScalingPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseTypeDef(_ClientDescribeScalingPoliciesResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **ScalingPolicies** *(list) --*

        Collection of objects containing the scaling policies matching the request.
        - *(dict) --*

          Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the
          combination of name and fleet ID.
          *  DescribeFleetCapacity
          *  UpdateFleetCapacity
          *  DescribeEC2InstanceLimits
          * Manage scaling policies:

            *  PutScalingPolicy (auto-scaling)
            *  DescribeScalingPolicies (auto-scaling)
            *  DeleteScalingPolicy (auto-scaling)
    """


_ClientDescribeScriptResponseScriptStorageLocationTypeDef = TypedDict(
    "_ClientDescribeScriptResponseScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientDescribeScriptResponseScriptStorageLocationTypeDef(
    _ClientDescribeScriptResponseScriptStorageLocationTypeDef
):
    pass


_ClientDescribeScriptResponseScriptTypeDef = TypedDict(
    "_ClientDescribeScriptResponseScriptTypeDef",
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


class ClientDescribeScriptResponseScriptTypeDef(_ClientDescribeScriptResponseScriptTypeDef):
    """
    - **Script** *(dict) --*

      Set of properties describing the requested script.
      - **ScriptId** *(string) --*

        Unique identifier for a Realtime script
    """


_ClientDescribeScriptResponseTypeDef = TypedDict(
    "_ClientDescribeScriptResponseTypeDef",
    {"Script": ClientDescribeScriptResponseScriptTypeDef},
    total=False,
)


class ClientDescribeScriptResponseTypeDef(_ClientDescribeScriptResponseTypeDef):
    """
    - *(dict) --*

      - **Script** *(dict) --*

        Set of properties describing the requested script.
        - **ScriptId** *(string) --*

          Unique identifier for a Realtime script
    """


_ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)


class ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef(
    _ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef
):
    """
    - *(dict) --*

      Represents an authorization for a VPC peering connection between the VPC for an Amazon
      GameLift fleet and another VPC on an account you have access to. This authorization must exist
      and be valid for the peering connection to be established. Authorizations are valid for 24
      hours after they are issued.
      *  CreateVpcPeeringAuthorization
      *  DescribeVpcPeeringAuthorizations
      *  DeleteVpcPeeringAuthorization
      *  CreateVpcPeeringConnection
      *  DescribeVpcPeeringConnections
      *  DeleteVpcPeeringConnection
      - **GameLiftAwsAccountId** *(string) --*

        Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You
        can find your Account ID in the AWS Management Console under account settings.
    """


_ClientDescribeVpcPeeringAuthorizationsResponseTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringAuthorizationsResponseTypeDef",
    {
        "VpcPeeringAuthorizations": List[
            ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeVpcPeeringAuthorizationsResponseTypeDef(
    _ClientDescribeVpcPeeringAuthorizationsResponseTypeDef
):
    """
    - *(dict) --*

      - **VpcPeeringAuthorizations** *(list) --*

        Collection of objects that describe all valid VPC peering operations for the current AWS
        account.
        - *(dict) --*

          Represents an authorization for a VPC peering connection between the VPC for an Amazon
          GameLift fleet and another VPC on an account you have access to. This authorization must
          exist and be valid for the peering connection to be established. Authorizations are valid
          for 24 hours after they are issued.
          *  CreateVpcPeeringAuthorization
          *  DescribeVpcPeeringAuthorizations
          *  DeleteVpcPeeringAuthorization
          *  CreateVpcPeeringConnection
          *  DescribeVpcPeeringConnections
          *  DeleteVpcPeeringConnection
          - **GameLiftAwsAccountId** *(string) --*

            Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet.
            You can find your Account ID in the AWS Management Console under account settings.
    """


_ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef(
    _ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef
):
    pass


_ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef",
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


class ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef(
    _ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef
):
    """
    - *(dict) --*

      Represents a peering connection between a VPC on one of your AWS accounts and the VPC for your
      Amazon GameLift fleets. This record may be for an active peering connection or a pending
      connection that has not yet been established.
      *  CreateVpcPeeringAuthorization
      *  DescribeVpcPeeringAuthorizations
      *  DeleteVpcPeeringAuthorization
      *  CreateVpcPeeringConnection
      *  DescribeVpcPeeringConnections
      *  DeleteVpcPeeringConnection
      - **FleetId** *(string) --*

        Unique identifier for a fleet. This ID determines the ID of the Amazon GameLift VPC for your
        fleet.
    """


_ClientDescribeVpcPeeringConnectionsResponseTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringConnectionsResponseTypeDef",
    {
        "VpcPeeringConnections": List[
            ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeVpcPeeringConnectionsResponseTypeDef(
    _ClientDescribeVpcPeeringConnectionsResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **VpcPeeringConnections** *(list) --*

        Collection of VPC peering connection records that match the request.
        - *(dict) --*

          Represents a peering connection between a VPC on one of your AWS accounts and the VPC for
          your Amazon GameLift fleets. This record may be for an active peering connection or a
          pending connection that has not yet been established.
          *  CreateVpcPeeringAuthorization
          *  DescribeVpcPeeringAuthorizations
          *  DeleteVpcPeeringAuthorization
          *  CreateVpcPeeringConnection
          *  DescribeVpcPeeringConnections
          *  DeleteVpcPeeringConnection
          - **FleetId** *(string) --*

            Unique identifier for a fleet. This ID determines the ID of the Amazon GameLift VPC for
            your fleet.
    """


_ClientGetGameSessionLogUrlResponseTypeDef = TypedDict(
    "_ClientGetGameSessionLogUrlResponseTypeDef", {"PreSignedUrl": str}, total=False
)


class ClientGetGameSessionLogUrlResponseTypeDef(_ClientGetGameSessionLogUrlResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **PreSignedUrl** *(string) --*

        Location of the requested game session logs, available for download. This URL is valid for
        15 minutes, after which S3 will reject any download request using this URL. You can request
        a new URL any time within the 14-day period that the logs are retained.
    """


_ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef = TypedDict(
    "_ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef",
    {"UserName": str, "Secret": str},
    total=False,
)


class ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef(
    _ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef
):
    pass


_ClientGetInstanceAccessResponseInstanceAccessTypeDef = TypedDict(
    "_ClientGetInstanceAccessResponseInstanceAccessTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "Credentials": ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef,
    },
    total=False,
)


class ClientGetInstanceAccessResponseInstanceAccessTypeDef(
    _ClientGetInstanceAccessResponseInstanceAccessTypeDef
):
    """
    - **InstanceAccess** *(dict) --*

      Object that contains connection information for a fleet instance, including IP address and
      access credentials.
      - **FleetId** *(string) --*

        Unique identifier for a fleet containing the instance being accessed.
    """


_ClientGetInstanceAccessResponseTypeDef = TypedDict(
    "_ClientGetInstanceAccessResponseTypeDef",
    {"InstanceAccess": ClientGetInstanceAccessResponseInstanceAccessTypeDef},
    total=False,
)


class ClientGetInstanceAccessResponseTypeDef(_ClientGetInstanceAccessResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **InstanceAccess** *(dict) --*

        Object that contains connection information for a fleet instance, including IP address and
        access credentials.
        - **FleetId** *(string) --*

          Unique identifier for a fleet containing the instance being accessed.
    """


_ClientListAliasesResponseAliasesRoutingStrategyTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)


class ClientListAliasesResponseAliasesRoutingStrategyTypeDef(
    _ClientListAliasesResponseAliasesRoutingStrategyTypeDef
):
    pass


_ClientListAliasesResponseAliasesTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesTypeDef",
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


class ClientListAliasesResponseAliasesTypeDef(_ClientListAliasesResponseAliasesTypeDef):
    """
    - *(dict) --*

      Properties describing a fleet alias.
      *  CreateAlias
      *  ListAliases
      *  DescribeAlias
      *  UpdateAlias
      *  DeleteAlias
      *  ResolveAlias
      - **AliasId** *(string) --*

        Unique identifier for an alias; alias IDs are unique within a region.
    """


_ClientListAliasesResponseTypeDef = TypedDict(
    "_ClientListAliasesResponseTypeDef",
    {"Aliases": List[ClientListAliasesResponseAliasesTypeDef], "NextToken": str},
    total=False,
)


class ClientListAliasesResponseTypeDef(_ClientListAliasesResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Aliases** *(list) --*

        Collection of alias records that match the list request.
        - *(dict) --*

          Properties describing a fleet alias.
          *  CreateAlias
          *  ListAliases
          *  DescribeAlias
          *  UpdateAlias
          *  DeleteAlias
          *  ResolveAlias
          - **AliasId** *(string) --*

            Unique identifier for an alias; alias IDs are unique within a region.
    """


_ClientListBuildsResponseBuildsTypeDef = TypedDict(
    "_ClientListBuildsResponseBuildsTypeDef",
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


class ClientListBuildsResponseBuildsTypeDef(_ClientListBuildsResponseBuildsTypeDef):
    """
    - *(dict) --*

      Properties describing a custom game build.

        **Related operations**
    """


_ClientListBuildsResponseTypeDef = TypedDict(
    "_ClientListBuildsResponseTypeDef",
    {"Builds": List[ClientListBuildsResponseBuildsTypeDef], "NextToken": str},
    total=False,
)


class ClientListBuildsResponseTypeDef(_ClientListBuildsResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Builds** *(list) --*

        Collection of build records that match the request.
        - *(dict) --*

          Properties describing a custom game build.

            **Related operations**
    """


_ClientListFleetsResponseTypeDef = TypedDict(
    "_ClientListFleetsResponseTypeDef", {"FleetIds": List[str], "NextToken": str}, total=False
)


class ClientListFleetsResponseTypeDef(_ClientListFleetsResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetIds** *(list) --*

        Set of fleet IDs matching the list request. You can retrieve additional information about
        all returned fleets by passing this result set to a call to  DescribeFleetAttributes ,
        DescribeFleetCapacity , or  DescribeFleetUtilization .
        - *(string) --*
    """


_ClientListScriptsResponseScriptsStorageLocationTypeDef = TypedDict(
    "_ClientListScriptsResponseScriptsStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientListScriptsResponseScriptsStorageLocationTypeDef(
    _ClientListScriptsResponseScriptsStorageLocationTypeDef
):
    pass


_ClientListScriptsResponseScriptsTypeDef = TypedDict(
    "_ClientListScriptsResponseScriptsTypeDef",
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


class ClientListScriptsResponseScriptsTypeDef(_ClientListScriptsResponseScriptsTypeDef):
    """
    - *(dict) --*

      Properties describing a Realtime script.

        **Related operations**
    """


_ClientListScriptsResponseTypeDef = TypedDict(
    "_ClientListScriptsResponseTypeDef",
    {"Scripts": List[ClientListScriptsResponseScriptsTypeDef], "NextToken": str},
    total=False,
)


class ClientListScriptsResponseTypeDef(_ClientListScriptsResponseTypeDef):
    """
    - *(dict) --*

      - **Scripts** *(list) --*

        Set of properties describing the requested script.
        - *(dict) --*

          Properties describing a Realtime script.

            **Related operations**
    """


_ClientPutScalingPolicyResponseTypeDef = TypedDict(
    "_ClientPutScalingPolicyResponseTypeDef", {"Name": str}, total=False
)


class ClientPutScalingPolicyResponseTypeDef(_ClientPutScalingPolicyResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Name** *(string) --*

        Descriptive label that is associated with a scaling policy. Policy names do not need to be
        unique.
    """


_ClientPutScalingPolicyTargetConfigurationTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetConfigurationTypeDef", {"TargetValue": float}
)


class ClientPutScalingPolicyTargetConfigurationTypeDef(
    _ClientPutScalingPolicyTargetConfigurationTypeDef
):
    """
    Object that contains settings for a target-based scaling policy.
    - **TargetValue** *(float) --***[REQUIRED]**

      Desired value to use with a target-based scaling policy. The value must be relevant for
      whatever metric the scaling policy is using. For example, in a policy using the metric
      PercentAvailableGameSessions, the target value should be the preferred size of the fleet's
      buffer (the percent of capacity that should be idle and ready for new game sessions).
    """


_ClientRequestUploadCredentialsResponseStorageLocationTypeDef = TypedDict(
    "_ClientRequestUploadCredentialsResponseStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientRequestUploadCredentialsResponseStorageLocationTypeDef(
    _ClientRequestUploadCredentialsResponseStorageLocationTypeDef
):
    pass


_ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef = TypedDict(
    "_ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str},
    total=False,
)


class ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef(
    _ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef
):
    """
    - **UploadCredentials** *(dict) --*

      AWS credentials required when uploading a game build to the storage location. These
      credentials have a limited lifespan and are valid only for the build they were issued for.
      - **AccessKeyId** *(string) --*

        Temporary key allowing access to the Amazon GameLift S3 account.
    """


_ClientRequestUploadCredentialsResponseTypeDef = TypedDict(
    "_ClientRequestUploadCredentialsResponseTypeDef",
    {
        "UploadCredentials": ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef,
        "StorageLocation": ClientRequestUploadCredentialsResponseStorageLocationTypeDef,
    },
    total=False,
)


class ClientRequestUploadCredentialsResponseTypeDef(_ClientRequestUploadCredentialsResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **UploadCredentials** *(dict) --*

        AWS credentials required when uploading a game build to the storage location. These
        credentials have a limited lifespan and are valid only for the build they were issued for.
        - **AccessKeyId** *(string) --*

          Temporary key allowing access to the Amazon GameLift S3 account.
    """


_ClientResolveAliasResponseTypeDef = TypedDict(
    "_ClientResolveAliasResponseTypeDef", {"FleetId": str}, total=False
)


class ClientResolveAliasResponseTypeDef(_ClientResolveAliasResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetId** *(string) --*

        Fleet identifier that is associated with the requested alias.
    """


_ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "_ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef(
    _ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef
):
    pass


_ClientSearchGameSessionsResponseGameSessionsTypeDef = TypedDict(
    "_ClientSearchGameSessionsResponseGameSessionsTypeDef",
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


class ClientSearchGameSessionsResponseGameSessionsTypeDef(
    _ClientSearchGameSessionsResponseGameSessionsTypeDef
):
    """
    - *(dict) --*

      Properties describing a game session.
      A game session in ACTIVE status can host players. When a game session ends, its status is set
      to ``TERMINATED`` .
      Once the session ends, the game session object is retained for 30 days. This means you can
      reuse idempotency token values after this time. Game session logs are retained for 14 days.
      *  CreateGameSession
      *  DescribeGameSessions
      *  DescribeGameSessionDetails
      *  SearchGameSessions
      *  UpdateGameSession
      *  GetGameSessionLogUrl
      * Game session placements

        *  StartGameSessionPlacement
        *  DescribeGameSessionPlacement
        *  StopGameSessionPlacement
    """


_ClientSearchGameSessionsResponseTypeDef = TypedDict(
    "_ClientSearchGameSessionsResponseTypeDef",
    {"GameSessions": List[ClientSearchGameSessionsResponseGameSessionsTypeDef], "NextToken": str},
    total=False,
)


class ClientSearchGameSessionsResponseTypeDef(_ClientSearchGameSessionsResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessions** *(list) --*

        Collection of objects containing game session properties for each session matching the
        request.
        - *(dict) --*

          Properties describing a game session.
          A game session in ACTIVE status can host players. When a game session ends, its status is
          set to ``TERMINATED`` .
          Once the session ends, the game session object is retained for 30 days. This means you can
          reuse idempotency token values after this time. Game session logs are retained for 14
          days.
          *  CreateGameSession
          *  DescribeGameSessions
          *  DescribeGameSessionDetails
          *  SearchGameSessions
          *  UpdateGameSession
          *  GetGameSessionLogUrl
          * Game session placements

            *  StartGameSessionPlacement
            *  DescribeGameSessionPlacement
            *  StopGameSessionPlacement
    """


_ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerData": str},
    total=False,
)


class ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef(
    _ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef
):
    """
    - *(dict) --*

      Player information for use when creating player sessions using a game session placement
      request with  StartGameSessionPlacement .
      - **PlayerId** *(string) --*

        Unique identifier for a player to associate with the player session.
    """


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
    """
    - *(dict) --*

      Set of key-value pairs that contain information about a game session. When included in a game
      session request, these properties communicate details to be used when setting up the new game
      session, such as to specify a game mode, level, or map. Game properties are passed to the game
      server process when initiating a new game session; the server process uses the properties as
      appropriate. For more information, see the `Amazon GameLift Developer Guide
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
      .
      - **Key** *(string) --***[REQUIRED]**

        Game property identifier.
    """


_ClientStartGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": Any},
    total=False,
)


class ClientStartGameSessionPlacementPlayerLatenciesTypeDef(
    _ClientStartGameSessionPlacementPlayerLatenciesTypeDef
):
    """
    - *(dict) --*

      Regional latency information for a player, used when requesting a new game session with
      StartGameSessionPlacement . This value indicates the amount of time lag that exists when the
      player is connected to a fleet in the specified region. The relative difference between a
      player's latency values for multiple regions are used to determine which fleets are best
      suited to place a new game session for the player.
      - **PlayerId** *(string) --*

        Unique identifier for a player associated with the latency data.
    """


_ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef(
    _ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
):
    pass


_ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef(
    _ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
):
    pass


_ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": Any},
    total=False,
)


class ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef(
    _ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
):
    pass


_ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef",
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


class ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef(
    _ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef
):
    """
    - **GameSessionPlacement** *(dict) --*

      Object that describes the newly created game session placement. This object includes all the
      information provided in the request, as well as start/end time stamps and placement status.
      - **PlacementId** *(string) --*

        Unique identifier for a game session placement.
    """


_ClientStartGameSessionPlacementResponseTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseTypeDef",
    {"GameSessionPlacement": ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef},
    total=False,
)


class ClientStartGameSessionPlacementResponseTypeDef(
    _ClientStartGameSessionPlacementResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessionPlacement** *(dict) --*

        Object that describes the newly created game session placement. This object includes all the
        information provided in the request, as well as start/end time stamps and placement status.
        - **PlacementId** *(string) --*

          Unique identifier for a game session placement.
    """


_ClientStartMatchBackfillPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientStartMatchBackfillPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientStartMatchBackfillPlayersPlayerAttributesTypeDef(
    _ClientStartMatchBackfillPlayersPlayerAttributesTypeDef
):
    pass


_ClientStartMatchBackfillPlayersTypeDef = TypedDict(
    "_ClientStartMatchBackfillPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[str, ClientStartMatchBackfillPlayersPlayerAttributesTypeDef],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)


class ClientStartMatchBackfillPlayersTypeDef(_ClientStartMatchBackfillPlayersTypeDef):
    """
    - *(dict) --*

      Represents a player in matchmaking. When starting a matchmaking request, a player has a player
      ID, attributes, and may have latency data. Team information is added after a match has been
      successfully completed.
      - **PlayerId** *(string) --*

        Unique identifier for a player
    """


_ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
):
    pass


_ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
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


class ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef
):
    pass


_ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef
):
    pass


_ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef",
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


class ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef
):
    pass


_ClientStartMatchBackfillResponseMatchmakingTicketTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketTypeDef",
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


class ClientStartMatchBackfillResponseMatchmakingTicketTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketTypeDef
):
    """
    - **MatchmakingTicket** *(dict) --*

      Ticket representing the backfill matchmaking request. This object includes the information in
      the request, ticket status, and match results as generated during the matchmaking process.
      - **TicketId** *(string) --*

        Unique identifier for a matchmaking ticket.
    """


_ClientStartMatchBackfillResponseTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseTypeDef",
    {"MatchmakingTicket": ClientStartMatchBackfillResponseMatchmakingTicketTypeDef},
    total=False,
)


class ClientStartMatchBackfillResponseTypeDef(_ClientStartMatchBackfillResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **MatchmakingTicket** *(dict) --*

        Ticket representing the backfill matchmaking request. This object includes the information
        in the request, ticket status, and match results as generated during the matchmaking
        process.
        - **TicketId** *(string) --*

          Unique identifier for a matchmaking ticket.
    """


_ClientStartMatchmakingPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientStartMatchmakingPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientStartMatchmakingPlayersPlayerAttributesTypeDef(
    _ClientStartMatchmakingPlayersPlayerAttributesTypeDef
):
    pass


_ClientStartMatchmakingPlayersTypeDef = TypedDict(
    "_ClientStartMatchmakingPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[str, ClientStartMatchmakingPlayersPlayerAttributesTypeDef],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)


class ClientStartMatchmakingPlayersTypeDef(_ClientStartMatchmakingPlayersTypeDef):
    """
    - *(dict) --*

      Represents a player in matchmaking. When starting a matchmaking request, a player has a player
      ID, attributes, and may have latency data. Team information is added after a match has been
      successfully completed.
      - **PlayerId** *(string) --*

        Unique identifier for a player
    """


_ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
):
    pass


_ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
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


class ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef
):
    pass


_ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef
):
    pass


_ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef",
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


class ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef
):
    pass


_ClientStartMatchmakingResponseMatchmakingTicketTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketTypeDef",
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


class ClientStartMatchmakingResponseMatchmakingTicketTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketTypeDef
):
    """
    - **MatchmakingTicket** *(dict) --*

      Ticket representing the matchmaking request. This object include the information included in
      the request, ticket status, and match results as generated during the matchmaking process.
      - **TicketId** *(string) --*

        Unique identifier for a matchmaking ticket.
    """


_ClientStartMatchmakingResponseTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseTypeDef",
    {"MatchmakingTicket": ClientStartMatchmakingResponseMatchmakingTicketTypeDef},
    total=False,
)


class ClientStartMatchmakingResponseTypeDef(_ClientStartMatchmakingResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **MatchmakingTicket** *(dict) --*

        Ticket representing the matchmaking request. This object include the information included in
        the request, ticket status, and match results as generated during the matchmaking process.
        - **TicketId** *(string) --*

          Unique identifier for a matchmaking ticket.
    """


_ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef(
    _ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
):
    pass


_ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef(
    _ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
):
    pass


_ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": Any},
    total=False,
)


class ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef(
    _ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
):
    pass


_ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef",
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


class ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef(
    _ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef
):
    """
    - **GameSessionPlacement** *(dict) --*

      Object that describes the canceled game session placement, with ``CANCELLED`` status and an
      end time stamp.
      - **PlacementId** *(string) --*

        Unique identifier for a game session placement.
    """


_ClientStopGameSessionPlacementResponseTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseTypeDef",
    {"GameSessionPlacement": ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef},
    total=False,
)


class ClientStopGameSessionPlacementResponseTypeDef(_ClientStopGameSessionPlacementResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessionPlacement** *(dict) --*

        Object that describes the canceled game session placement, with ``CANCELLED`` status and an
        end time stamp.
        - **PlacementId** *(string) --*

          Unique identifier for a game session placement.
    """


_ClientUpdateAliasResponseAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientUpdateAliasResponseAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)


class ClientUpdateAliasResponseAliasRoutingStrategyTypeDef(
    _ClientUpdateAliasResponseAliasRoutingStrategyTypeDef
):
    pass


_ClientUpdateAliasResponseAliasTypeDef = TypedDict(
    "_ClientUpdateAliasResponseAliasTypeDef",
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


class ClientUpdateAliasResponseAliasTypeDef(_ClientUpdateAliasResponseAliasTypeDef):
    """
    - **Alias** *(dict) --*

      Object that contains the updated alias configuration.
      - **AliasId** *(string) --*

        Unique identifier for an alias; alias IDs are unique within a region.
    """


_ClientUpdateAliasResponseTypeDef = TypedDict(
    "_ClientUpdateAliasResponseTypeDef",
    {"Alias": ClientUpdateAliasResponseAliasTypeDef},
    total=False,
)


class ClientUpdateAliasResponseTypeDef(_ClientUpdateAliasResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Alias** *(dict) --*

        Object that contains the updated alias configuration.
        - **AliasId** *(string) --*

          Unique identifier for an alias; alias IDs are unique within a region.
    """


_ClientUpdateAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientUpdateAliasRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)


class ClientUpdateAliasRoutingStrategyTypeDef(_ClientUpdateAliasRoutingStrategyTypeDef):
    """
    Object that specifies the fleet and routing type to use for the alias.
    - **Type** *(string) --*

      Type of routing strategy.
      Possible routing types include the following:
      * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active
      fleets.
      * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a
      message to the user. A terminal alias throws a TerminalRoutingStrategyException with the
      RoutingStrategy message embedded.
    """


_ClientUpdateBuildResponseBuildTypeDef = TypedDict(
    "_ClientUpdateBuildResponseBuildTypeDef",
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


class ClientUpdateBuildResponseBuildTypeDef(_ClientUpdateBuildResponseBuildTypeDef):
    """
    - **Build** *(dict) --*

      Object that contains the updated build record.
      - **BuildId** *(string) --*

        Unique identifier for a build.
    """


_ClientUpdateBuildResponseTypeDef = TypedDict(
    "_ClientUpdateBuildResponseTypeDef",
    {"Build": ClientUpdateBuildResponseBuildTypeDef},
    total=False,
)


class ClientUpdateBuildResponseTypeDef(_ClientUpdateBuildResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Build** *(dict) --*

        Object that contains the updated build record.
        - **BuildId** *(string) --*

          Unique identifier for a build.
    """


_ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "_ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef(
    _ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef
):
    """
    Policy that limits the number of game sessions an individual player can create over a span of
    time.
    - **NewGameSessionsPerCreator** *(integer) --*

      Maximum number of game sessions that an individual can create during the policy period.
    """


_ClientUpdateFleetAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateFleetAttributesResponseTypeDef", {"FleetId": str}, total=False
)


class ClientUpdateFleetAttributesResponseTypeDef(_ClientUpdateFleetAttributesResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetId** *(string) --*

        Unique identifier for a fleet that was updated.
    """


_ClientUpdateFleetCapacityResponseTypeDef = TypedDict(
    "_ClientUpdateFleetCapacityResponseTypeDef", {"FleetId": str}, total=False
)


class ClientUpdateFleetCapacityResponseTypeDef(_ClientUpdateFleetCapacityResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetId** *(string) --*

        Unique identifier for a fleet that was updated.
    """


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
    """
    - *(dict) --*

      A range of IP addresses and port settings that allow inbound traffic to connect to server
      processes on an Amazon GameLift. New game sessions that are started on the fleet are assigned
      an IP address/port number combination, which must fall into the fleet's allowed ranges. For
      fleets created with a custom game server, the ranges reflect the server's game session
      assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges,
      one for TCP messaging and one for UDP for use by the Realtime servers.
      - **FromPort** *(integer) --***[REQUIRED]**

        Starting value for a range of allowed port numbers.
    """


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
    """
    - *(dict) --*

      A range of IP addresses and port settings that allow inbound traffic to connect to server
      processes on an Amazon GameLift. New game sessions that are started on the fleet are assigned
      an IP address/port number combination, which must fall into the fleet's allowed ranges. For
      fleets created with a custom game server, the ranges reflect the server's game session
      assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges,
      one for TCP messaging and one for UDP for use by the Realtime servers.
      - **FromPort** *(integer) --***[REQUIRED]**

        Starting value for a range of allowed port numbers.
    """


_ClientUpdateFleetPortSettingsResponseTypeDef = TypedDict(
    "_ClientUpdateFleetPortSettingsResponseTypeDef", {"FleetId": str}, total=False
)


class ClientUpdateFleetPortSettingsResponseTypeDef(_ClientUpdateFleetPortSettingsResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetId** *(string) --*

        Unique identifier for a fleet that was updated.
    """


_ClientUpdateGameSessionQueueDestinationsTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueDestinationsTypeDef", {"DestinationArn": str}, total=False
)


class ClientUpdateGameSessionQueueDestinationsTypeDef(
    _ClientUpdateGameSessionQueueDestinationsTypeDef
):
    """
    - *(dict) --*

      Fleet designated in a game session queue. Requests for new game sessions in the queue are
      fulfilled by starting a new game session on any destination configured for a queue.
      *  CreateGameSessionQueue
      *  DescribeGameSessionQueues
      *  UpdateGameSessionQueue
      *  DeleteGameSessionQueue
      - **DestinationArn** *(string) --*

        Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID
        or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef(
    _ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef
):
    """
    - *(dict) --*

      Queue setting that determines the highest latency allowed for individual players when placing
      a game session. When a latency policy is in force, a game session cannot be placed at any
      destination in a region where a player is reporting latency higher than the cap. Latency
      policies are only enforced when the placement request contains player latency information.
      *  CreateGameSessionQueue
      *  DescribeGameSessionQueues
      *  UpdateGameSessionQueue
      *  DeleteGameSessionQueue
      - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

        The maximum latency value that is allowed for any player, in milliseconds. All policies must
        have a value set for this property.
    """


_ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef(
    _ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef
):
    pass


_ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef(
    _ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef
):
    pass


_ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef",
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


class ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef(
    _ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef
):
    """
    - **GameSessionQueue** *(dict) --*

      Object that describes the newly updated game session queue.
      - **Name** *(string) --*

        Descriptive label that is associated with game session queue. Queue names must be unique
        within each region.
    """


_ClientUpdateGameSessionQueueResponseTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueResponseTypeDef",
    {"GameSessionQueue": ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef},
    total=False,
)


class ClientUpdateGameSessionQueueResponseTypeDef(_ClientUpdateGameSessionQueueResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessionQueue** *(dict) --*

        Object that describes the newly updated game session queue.
        - **Name** *(string) --*

          Descriptive label that is associated with game session queue. Queue names must be unique
          within each region.
    """


_ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef = TypedDict(
    "_ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef(
    _ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef
):
    pass


_ClientUpdateGameSessionResponseGameSessionTypeDef = TypedDict(
    "_ClientUpdateGameSessionResponseGameSessionTypeDef",
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


class ClientUpdateGameSessionResponseGameSessionTypeDef(
    _ClientUpdateGameSessionResponseGameSessionTypeDef
):
    """
    - **GameSession** *(dict) --*

      Object that contains the updated game session metadata.
      - **GameSessionId** *(string) --*

        Unique identifier for the game session. A game session ARN has the following format:
        ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
        token>`` .
    """


_ClientUpdateGameSessionResponseTypeDef = TypedDict(
    "_ClientUpdateGameSessionResponseTypeDef",
    {"GameSession": ClientUpdateGameSessionResponseGameSessionTypeDef},
    total=False,
)


class ClientUpdateGameSessionResponseTypeDef(_ClientUpdateGameSessionResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSession** *(dict) --*

        Object that contains the updated game session metadata.
        - **GameSessionId** *(string) --*

          Unique identifier for the game session. A game session ARN has the following format:
          ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
          token>`` .
    """


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
    """
    - *(dict) --*

      Set of key-value pairs that contain information about a game session. When included in a game
      session request, these properties communicate details to be used when setting up the new game
      session, such as to specify a game mode, level, or map. Game properties are passed to the game
      server process when initiating a new game session; the server process uses the properties as
      appropriate. For more information, see the `Amazon GameLift Developer Guide
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
      .
      - **Key** *(string) --***[REQUIRED]**

        Game property identifier.
    """


_ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef = TypedDict(
    "_ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef(
    _ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef
):
    pass


_ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef = TypedDict(
    "_ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef",
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


class ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef(
    _ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef
):
    """
    - **Configuration** *(dict) --*

      Object that describes the updated matchmaking configuration.
      - **Name** *(string) --*

        Unique identifier for a matchmaking configuration. This name is used to identify the
        configuration associated with a matchmaking request or ticket.
    """


_ClientUpdateMatchmakingConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateMatchmakingConfigurationResponseTypeDef",
    {"Configuration": ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef},
    total=False,
)


class ClientUpdateMatchmakingConfigurationResponseTypeDef(
    _ClientUpdateMatchmakingConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Configuration** *(dict) --*

        Object that describes the updated matchmaking configuration.
        - **Name** *(string) --*

          Unique identifier for a matchmaking configuration. This name is used to identify the
          configuration associated with a matchmaking request or ticket.
    """


_ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    {"LaunchPath": str, "Parameters": str, "ConcurrentExecutions": int},
    total=False,
)


class ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef(
    _ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
):
    """
    - *(dict) --*

      A set of instructions for launching server processes on each instance in a fleet. Server
      processes run either a custom game build executable or a Realtime Servers script. Each
      instruction set identifies the location of the custom game build executable or Realtime launch
      script, optional launch parameters, and the number of server processes with this configuration
      to maintain concurrently on the instance. Server process configurations make up a fleet's ``
      RuntimeConfiguration `` .
      - **LaunchPath** *(string) --*

        Location of the server executable in a custom game build or the name of the Realtime script
        file that contains the ``Init()`` function. Game builds and Realtime scripts are installed
        on instances at the root:
        * Windows (for custom game builds only): ``C:\\game`` . Example:
        "``C:\\game\\MyGame\\server.exe`` "
        * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
        "``/local/game/MyRealtimeScript.js`` "
    """


_ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef = TypedDict(
    "_ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)


class ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef(
    _ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef
):
    """
    - **RuntimeConfiguration** *(dict) --*

      The run-time configuration currently in force. If the update was successful, this object
      matches the one in the request.
      - **ServerProcesses** *(list) --*

        Collection of server process configurations that describe which server processes to run on
        each instance in a fleet.
        - *(dict) --*

          A set of instructions for launching server processes on each instance in a fleet. Server
          processes run either a custom game build executable or a Realtime Servers script. Each
          instruction set identifies the location of the custom game build executable or Realtime
          launch script, optional launch parameters, and the number of server processes with this
          configuration to maintain concurrently on the instance. Server process configurations make
          up a fleet's ``  RuntimeConfiguration `` .
          - **LaunchPath** *(string) --*

            Location of the server executable in a custom game build or the name of the Realtime
            script file that contains the ``Init()`` function. Game builds and Realtime scripts are
            installed on instances at the root:
            * Windows (for custom game builds only): ``C:\\game`` . Example:
            "``C:\\game\\MyGame\\server.exe`` "
            * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
            "``/local/game/MyRealtimeScript.js`` "
    """


_ClientUpdateRuntimeConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateRuntimeConfigurationResponseTypeDef",
    {"RuntimeConfiguration": ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef},
    total=False,
)


class ClientUpdateRuntimeConfigurationResponseTypeDef(
    _ClientUpdateRuntimeConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **RuntimeConfiguration** *(dict) --*

        The run-time configuration currently in force. If the update was successful, this object
        matches the one in the request.
        - **ServerProcesses** *(list) --*

          Collection of server process configurations that describe which server processes to run on
          each instance in a fleet.
          - *(dict) --*

            A set of instructions for launching server processes on each instance in a fleet. Server
            processes run either a custom game build executable or a Realtime Servers script. Each
            instruction set identifies the location of the custom game build executable or Realtime
            launch script, optional launch parameters, and the number of server processes with this
            configuration to maintain concurrently on the instance. Server process configurations
            make up a fleet's ``  RuntimeConfiguration `` .
            - **LaunchPath** *(string) --*

              Location of the server executable in a custom game build or the name of the Realtime
              script file that contains the ``Init()`` function. Game builds and Realtime scripts
              are installed on instances at the root:
              * Windows (for custom game builds only): ``C:\\game`` . Example:
              "``C:\\game\\MyGame\\server.exe`` "
              * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
              "``/local/game/MyRealtimeScript.js`` "
    """


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
    """
    - *(dict) --*

      A set of instructions for launching server processes on each instance in a fleet. Server
      processes run either a custom game build executable or a Realtime Servers script. Each
      instruction set identifies the location of the custom game build executable or Realtime launch
      script, optional launch parameters, and the number of server processes with this configuration
      to maintain concurrently on the instance. Server process configurations make up a fleet's ``
      RuntimeConfiguration `` .
      - **LaunchPath** *(string) --***[REQUIRED]**

        Location of the server executable in a custom game build or the name of the Realtime script
        file that contains the ``Init()`` function. Game builds and Realtime scripts are installed
        on instances at the root:
        * Windows (for custom game builds only): ``C:\\game`` . Example:
        "``C:\\game\\MyGame\\server.exe`` "
        * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
        "``/local/game/MyRealtimeScript.js`` "
    """


_ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef = TypedDict(
    "_ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)


class ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef(
    _ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef
):
    """
    Instructions for launching server processes on each instance in the fleet. Server processes run
    either a custom game build executable or a Realtime Servers script. The run-time configuration
    lists the types of server processes to run on an instance and includes the following
    configuration settings: the server executable or launch script file, launch parameters, and the
    number of processes to run concurrently on each instance. A CreateFleet request must include a
    run-time configuration with at least one server process configuration.
    - **ServerProcesses** *(list) --*

      Collection of server process configurations that describe which server processes to run on
      each instance in a fleet.
      - *(dict) --*

        A set of instructions for launching server processes on each instance in a fleet. Server
        processes run either a custom game build executable or a Realtime Servers script. Each
        instruction set identifies the location of the custom game build executable or Realtime
        launch script, optional launch parameters, and the number of server processes with this
        configuration to maintain concurrently on the instance. Server process configurations make
        up a fleet's ``  RuntimeConfiguration `` .
        - **LaunchPath** *(string) --***[REQUIRED]**

          Location of the server executable in a custom game build or the name of the Realtime
          script file that contains the ``Init()`` function. Game builds and Realtime scripts are
          installed on instances at the root:
          * Windows (for custom game builds only): ``C:\\game`` . Example:
          "``C:\\game\\MyGame\\server.exe`` "
          * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
          "``/local/game/MyRealtimeScript.js`` "
    """


_ClientUpdateScriptResponseScriptStorageLocationTypeDef = TypedDict(
    "_ClientUpdateScriptResponseScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientUpdateScriptResponseScriptStorageLocationTypeDef(
    _ClientUpdateScriptResponseScriptStorageLocationTypeDef
):
    pass


_ClientUpdateScriptResponseScriptTypeDef = TypedDict(
    "_ClientUpdateScriptResponseScriptTypeDef",
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


class ClientUpdateScriptResponseScriptTypeDef(_ClientUpdateScriptResponseScriptTypeDef):
    """
    - **Script** *(dict) --*

      The newly created script record with a unique script ID. The new script's storage location
      reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your
      account, the storage location reflects the information that was provided in the *CreateScript*
      request; (2) If the script file was uploaded from a local zip file, the storage location
      reflects an S3 location controls by the Amazon GameLift service.
      - **ScriptId** *(string) --*

        Unique identifier for a Realtime script
    """


_ClientUpdateScriptResponseTypeDef = TypedDict(
    "_ClientUpdateScriptResponseTypeDef",
    {"Script": ClientUpdateScriptResponseScriptTypeDef},
    total=False,
)


class ClientUpdateScriptResponseTypeDef(_ClientUpdateScriptResponseTypeDef):
    """
    - *(dict) --*

      - **Script** *(dict) --*

        The newly created script record with a unique script ID. The new script's storage location
        reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your
        account, the storage location reflects the information that was provided in the
        *CreateScript* request; (2) If the script file was uploaded from a local zip file, the
        storage location reflects an S3 location controls by the Amazon GameLift service.
        - **ScriptId** *(string) --*

          Unique identifier for a Realtime script
    """


_ClientUpdateScriptStorageLocationTypeDef = TypedDict(
    "_ClientUpdateScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientUpdateScriptStorageLocationTypeDef(_ClientUpdateScriptStorageLocationTypeDef):
    """
    Location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored.
    The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and
    a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket
    must be in the same region where you want to create a new script. By default, Amazon GameLift
    uploads the latest version of the zip file; if you have S3 object versioning turned on, you can
    use the ``ObjectVersion`` parameter to specify an earlier version.
    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.
    """


_ClientValidateMatchmakingRuleSetResponseTypeDef = TypedDict(
    "_ClientValidateMatchmakingRuleSetResponseTypeDef", {"Valid": bool}, total=False
)


class ClientValidateMatchmakingRuleSetResponseTypeDef(
    _ClientValidateMatchmakingRuleSetResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Valid** *(boolean) --*

        Response indicating whether the rule set is valid.
    """


_DescribeFleetAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFleetAttributesPaginatePaginationConfigTypeDef(
    _DescribeFleetAttributesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef",
    {"CertificateType": Literal["DISABLED", "GENERATED"]},
    total=False,
)


class DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef(
    _DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef
):
    pass


_DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef(
    _DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef
):
    pass


_DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef",
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


class DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef(
    _DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef
):
    """
    - *(dict) --*

      General properties describing a fleet.
      *  CreateFleet
      *  ListFleets
      *  DeleteFleet
      * Describe fleets:

        *  DescribeFleetAttributes
        *  DescribeFleetCapacity
        *  DescribeFleetPortSettings
        *  DescribeFleetUtilization
        *  DescribeRuntimeConfiguration
        *  DescribeEC2InstanceLimits
        *  DescribeFleetEvents
    """


_DescribeFleetAttributesPaginateResponseTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginateResponseTypeDef",
    {"FleetAttributes": List[DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef]},
    total=False,
)


class DescribeFleetAttributesPaginateResponseTypeDef(
    _DescribeFleetAttributesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetAttributes** *(list) --*

        Collection of objects containing attribute metadata for each requested fleet ID.
        - *(dict) --*

          General properties describing a fleet.
          *  CreateFleet
          *  ListFleets
          *  DeleteFleet
          * Describe fleets:

            *  DescribeFleetAttributes
            *  DescribeFleetCapacity
            *  DescribeFleetPortSettings
            *  DescribeFleetUtilization
            *  DescribeRuntimeConfiguration
            *  DescribeEC2InstanceLimits
            *  DescribeFleetEvents
    """


_DescribeFleetCapacityPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetCapacityPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFleetCapacityPaginatePaginationConfigTypeDef(
    _DescribeFleetCapacityPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef = TypedDict(
    "_DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef",
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


class DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef(
    _DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef
):
    pass


_DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef = TypedDict(
    "_DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef",
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


class DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef(
    _DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef
):
    """
    - *(dict) --*

      Information about the fleet's capacity. Fleet capacity is measured in EC2 instances. By
      default, new fleets have a capacity of one instance, but can be updated as needed. The maximum
      number of instances for a fleet is determined by the fleet's instance type.
      *  CreateFleet
      *  ListFleets
      *  DeleteFleet
      * Describe fleets:

        *  DescribeFleetAttributes
        *  DescribeFleetCapacity
        *  DescribeFleetPortSettings
        *  DescribeFleetUtilization
        *  DescribeRuntimeConfiguration
        *  DescribeEC2InstanceLimits
        *  DescribeFleetEvents
    """


_DescribeFleetCapacityPaginateResponseTypeDef = TypedDict(
    "_DescribeFleetCapacityPaginateResponseTypeDef",
    {"FleetCapacity": List[DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef]},
    total=False,
)


class DescribeFleetCapacityPaginateResponseTypeDef(_DescribeFleetCapacityPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetCapacity** *(list) --*

        Collection of objects containing capacity information for each requested fleet ID. Leave
        this parameter empty to retrieve capacity information for all fleets.
        - *(dict) --*

          Information about the fleet's capacity. Fleet capacity is measured in EC2 instances. By
          default, new fleets have a capacity of one instance, but can be updated as needed. The
          maximum number of instances for a fleet is determined by the fleet's instance type.
          *  CreateFleet
          *  ListFleets
          *  DeleteFleet
          * Describe fleets:

            *  DescribeFleetAttributes
            *  DescribeFleetCapacity
            *  DescribeFleetPortSettings
            *  DescribeFleetUtilization
            *  DescribeRuntimeConfiguration
            *  DescribeEC2InstanceLimits
            *  DescribeFleetEvents
    """


_DescribeFleetEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFleetEventsPaginatePaginationConfigTypeDef(
    _DescribeFleetEventsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeFleetEventsPaginateResponseEventsTypeDef = TypedDict(
    "_DescribeFleetEventsPaginateResponseEventsTypeDef",
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


class DescribeFleetEventsPaginateResponseEventsTypeDef(
    _DescribeFleetEventsPaginateResponseEventsTypeDef
):
    """
    - *(dict) --*

      Log entry describing an event that involves Amazon GameLift resources (such as a fleet). In
      addition to tracking activity, event codes and messages can provide additional information for
      troubleshooting and debugging problems.
      - **EventId** *(string) --*

        Unique identifier for a fleet event.
    """


_DescribeFleetEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeFleetEventsPaginateResponseTypeDef",
    {"Events": List[DescribeFleetEventsPaginateResponseEventsTypeDef]},
    total=False,
)


class DescribeFleetEventsPaginateResponseTypeDef(_DescribeFleetEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Events** *(list) --*

        Collection of objects containing event log entries for the specified fleet.
        - *(dict) --*

          Log entry describing an event that involves Amazon GameLift resources (such as a fleet).
          In addition to tracking activity, event codes and messages can provide additional
          information for troubleshooting and debugging problems.
          - **EventId** *(string) --*

            Unique identifier for a fleet event.
    """


_DescribeFleetUtilizationPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetUtilizationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFleetUtilizationPaginatePaginationConfigTypeDef(
    _DescribeFleetUtilizationPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef = TypedDict(
    "_DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef",
    {
        "FleetId": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
    },
    total=False,
)


class DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef(
    _DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef
):
    """
    - *(dict) --*

      Current status of fleet utilization, including the number of game and player sessions being
      hosted.
      *  CreateFleet
      *  ListFleets
      *  DeleteFleet
      * Describe fleets:

        *  DescribeFleetAttributes
        *  DescribeFleetCapacity
        *  DescribeFleetPortSettings
        *  DescribeFleetUtilization
        *  DescribeRuntimeConfiguration
        *  DescribeEC2InstanceLimits
        *  DescribeFleetEvents
    """


_DescribeFleetUtilizationPaginateResponseTypeDef = TypedDict(
    "_DescribeFleetUtilizationPaginateResponseTypeDef",
    {"FleetUtilization": List[DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef]},
    total=False,
)


class DescribeFleetUtilizationPaginateResponseTypeDef(
    _DescribeFleetUtilizationPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetUtilization** *(list) --*

        Collection of objects containing utilization information for each requested fleet ID.
        - *(dict) --*

          Current status of fleet utilization, including the number of game and player sessions
          being hosted.
          *  CreateFleet
          *  ListFleets
          *  DeleteFleet
          * Describe fleets:

            *  DescribeFleetAttributes
            *  DescribeFleetCapacity
            *  DescribeFleetPortSettings
            *  DescribeFleetUtilization
            *  DescribeRuntimeConfiguration
            *  DescribeEC2InstanceLimits
            *  DescribeFleetEvents
    """


_DescribeGameSessionDetailsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeGameSessionDetailsPaginatePaginationConfigTypeDef(
    _DescribeGameSessionDetailsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef(
    _DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef
):
    pass


_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef",
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


class DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef(
    _DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef
):
    """
    - **GameSession** *(dict) --*

      Object that describes a game session.
      - **GameSessionId** *(string) --*

        Unique identifier for the game session. A game session ARN has the following format:
        ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
        token>`` .
    """


_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef",
    {
        "GameSession": DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef,
        "ProtectionPolicy": Literal["NoProtection", "FullProtection"],
    },
    total=False,
)


class DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef(
    _DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef
):
    """
    - *(dict) --*

      A game session's properties plus the protection policy currently in force.
      - **GameSession** *(dict) --*

        Object that describes a game session.
        - **GameSessionId** *(string) --*

          Unique identifier for the game session. A game session ARN has the following format:
          ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
          token>`` .
    """


_DescribeGameSessionDetailsPaginateResponseTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginateResponseTypeDef",
    {
        "GameSessionDetails": List[
            DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef
        ]
    },
    total=False,
)


class DescribeGameSessionDetailsPaginateResponseTypeDef(
    _DescribeGameSessionDetailsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessionDetails** *(list) --*

        Collection of objects containing game session properties and the protection policy currently
        in force for each session matching the request.
        - *(dict) --*

          A game session's properties plus the protection policy currently in force.
          - **GameSession** *(dict) --*

            Object that describes a game session.
            - **GameSessionId** *(string) --*

              Unique identifier for the game session. A game session ARN has the following format:
              ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
              token>`` .
    """


_DescribeGameSessionQueuesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeGameSessionQueuesPaginatePaginationConfigTypeDef(
    _DescribeGameSessionQueuesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef(
    _DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef
):
    pass


_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef(
    _DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef
):
    pass


_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef",
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


class DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef(
    _DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef
):
    """
    - *(dict) --*

      Configuration of a queue that is used to process game session placement requests. The queue
      configuration identifies several game features:
      * The destinations where a new game session can potentially be hosted. Amazon GameLift tries
      these destinations in an order based on either the queue's default order or player latency
      information, if provided in a placement request. With latency information, Amazon GameLift can
      place game sessions where the majority of players are reporting the lowest possible latency.
      * The length of time that placement requests can wait in the queue before timing out.
      * A set of optional latency policies that protect individual players from high latencies,
      preventing game sessions from being placed where any individual player is reporting latency
      higher than a policy's maximum.
      *  CreateGameSessionQueue
      *  DescribeGameSessionQueues
      *  UpdateGameSessionQueue
      *  DeleteGameSessionQueue
      - **Name** *(string) --*

        Descriptive label that is associated with game session queue. Queue names must be unique
        within each region.
    """


_DescribeGameSessionQueuesPaginateResponseTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginateResponseTypeDef",
    {"GameSessionQueues": List[DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef]},
    total=False,
)


class DescribeGameSessionQueuesPaginateResponseTypeDef(
    _DescribeGameSessionQueuesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessionQueues** *(list) --*

        Collection of objects that describes the requested game session queues.
        - *(dict) --*

          Configuration of a queue that is used to process game session placement requests. The
          queue configuration identifies several game features:
          * The destinations where a new game session can potentially be hosted. Amazon GameLift
          tries these destinations in an order based on either the queue's default order or player
          latency information, if provided in a placement request. With latency information, Amazon
          GameLift can place game sessions where the majority of players are reporting the lowest
          possible latency.
          * The length of time that placement requests can wait in the queue before timing out.
          * A set of optional latency policies that protect individual players from high latencies,
          preventing game sessions from being placed where any individual player is reporting
          latency higher than a policy's maximum.
          *  CreateGameSessionQueue
          *  DescribeGameSessionQueues
          *  UpdateGameSessionQueue
          *  DeleteGameSessionQueue
          - **Name** *(string) --*

            Descriptive label that is associated with game session queue. Queue names must be unique
            within each region.
    """


_DescribeGameSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeGameSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeGameSessionsPaginatePaginationConfigTypeDef(
    _DescribeGameSessionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "_DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef(
    _DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef
):
    pass


_DescribeGameSessionsPaginateResponseGameSessionsTypeDef = TypedDict(
    "_DescribeGameSessionsPaginateResponseGameSessionsTypeDef",
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


class DescribeGameSessionsPaginateResponseGameSessionsTypeDef(
    _DescribeGameSessionsPaginateResponseGameSessionsTypeDef
):
    """
    - *(dict) --*

      Properties describing a game session.
      A game session in ACTIVE status can host players. When a game session ends, its status is set
      to ``TERMINATED`` .
      Once the session ends, the game session object is retained for 30 days. This means you can
      reuse idempotency token values after this time. Game session logs are retained for 14 days.
      *  CreateGameSession
      *  DescribeGameSessions
      *  DescribeGameSessionDetails
      *  SearchGameSessions
      *  UpdateGameSession
      *  GetGameSessionLogUrl
      * Game session placements

        *  StartGameSessionPlacement
        *  DescribeGameSessionPlacement
        *  StopGameSessionPlacement
    """


_DescribeGameSessionsPaginateResponseTypeDef = TypedDict(
    "_DescribeGameSessionsPaginateResponseTypeDef",
    {"GameSessions": List[DescribeGameSessionsPaginateResponseGameSessionsTypeDef]},
    total=False,
)


class DescribeGameSessionsPaginateResponseTypeDef(_DescribeGameSessionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessions** *(list) --*

        Collection of objects containing game session properties for each session matching the
        request.
        - *(dict) --*

          Properties describing a game session.
          A game session in ACTIVE status can host players. When a game session ends, its status is
          set to ``TERMINATED`` .
          Once the session ends, the game session object is retained for 30 days. This means you can
          reuse idempotency token values after this time. Game session logs are retained for 14
          days.
          *  CreateGameSession
          *  DescribeGameSessions
          *  DescribeGameSessionDetails
          *  SearchGameSessions
          *  UpdateGameSession
          *  GetGameSessionLogUrl
          * Game session placements

            *  StartGameSessionPlacement
            *  DescribeGameSessionPlacement
            *  StopGameSessionPlacement
    """


_DescribeInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeInstancesPaginatePaginationConfigTypeDef(
    _DescribeInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeInstancesPaginateResponseInstancesTypeDef = TypedDict(
    "_DescribeInstancesPaginateResponseInstancesTypeDef",
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


class DescribeInstancesPaginateResponseInstancesTypeDef(
    _DescribeInstancesPaginateResponseInstancesTypeDef
):
    """
    - *(dict) --*

      Properties that describe an instance of a virtual computing resource that hosts one or more
      game servers. A fleet may contain zero or more instances.
      - **FleetId** *(string) --*

        Unique identifier for a fleet that the instance is in.
    """


_DescribeInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeInstancesPaginateResponseTypeDef",
    {"Instances": List[DescribeInstancesPaginateResponseInstancesTypeDef]},
    total=False,
)


class DescribeInstancesPaginateResponseTypeDef(_DescribeInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Instances** *(list) --*

        Collection of objects containing properties for each instance returned.
        - *(dict) --*

          Properties that describe an instance of a virtual computing resource that hosts one or
          more game servers. A fleet may contain zero or more instances.
          - **FleetId** *(string) --*

            Unique identifier for a fleet that the instance is in.
    """


_DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef = TypedDict(
    "_DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef(
    _DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef
):
    pass


_DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef = TypedDict(
    "_DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef",
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


class DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef(
    _DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef
):
    """
    - *(dict) --*

      Guidelines for use with FlexMatch to match players into games. All matchmaking requests must
      specify a matchmaking configuration.
      - **Name** *(string) --*

        Unique identifier for a matchmaking configuration. This name is used to identify the
        configuration associated with a matchmaking request or ticket.
    """


_DescribeMatchmakingConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeMatchmakingConfigurationsPaginateResponseTypeDef",
    {
        "Configurations": List[
            DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef
        ]
    },
    total=False,
)


class DescribeMatchmakingConfigurationsPaginateResponseTypeDef(
    _DescribeMatchmakingConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Configurations** *(list) --*

        Collection of requested matchmaking configuration objects.
        - *(dict) --*

          Guidelines for use with FlexMatch to match players into games. All matchmaking requests
          must specify a matchmaking configuration.
          - **Name** *(string) --*

            Unique identifier for a matchmaking configuration. This name is used to identify the
            configuration associated with a matchmaking request or ticket.
    """


_DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef(
    _DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef = TypedDict(
    "_DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef",
    {"RuleSetName": str, "RuleSetBody": str, "CreationTime": datetime},
    total=False,
)


class DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef(
    _DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef
):
    """
    - *(dict) --*

      Set of rule statements, used with FlexMatch, that determine how to build your player matches.
      Each rule set describes a type of group to be created and defines the parameters for
      acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.
      A rule set may define the following elements for a match. For detailed information and
      examples showing how to construct a rule set, see `Build a FlexMatch Rule Set
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ .
      * Teams -- Required. A rule set must define one or multiple teams for the match and set
      minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that
      requires all eight slots to be filled.
      * Player attributes -- Optional. These attributes specify a set of player characteristics to
      evaluate when looking for a match. Matchmaking requests that use a rule set with player
      attributes must provide the corresponding attribute values. For example, an attribute might
      specify a player's skill or level.
      * Rules -- Optional. Rules define how to evaluate potential players for a match based on
      player attributes. A rule might specify minimum requirements for individual players, teams, or
      entire matches. For example, a rule might require each player to meet a certain skill level,
      each team to have at least one player in a certain role, or the match to have a minimum
      average skill level. or may describe an entire group--such as all teams must be evenly matched
      or have at least one player in a certain role.
      * Expansions -- Optional. Expansions allow you to relax the rules after a period of time when
      no acceptable matches are found. This feature lets you balance getting players into games in a
      reasonable amount of time instead of making them wait indefinitely for the best possible
      match. For example, you might use an expansion to increase the maximum skill variance between
      players after 30 seconds.
      - **RuleSetName** *(string) --*

        Unique identifier for a matchmaking rule set
    """


_DescribeMatchmakingRuleSetsPaginateResponseTypeDef = TypedDict(
    "_DescribeMatchmakingRuleSetsPaginateResponseTypeDef",
    {"RuleSets": List[DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef]},
    total=False,
)


class DescribeMatchmakingRuleSetsPaginateResponseTypeDef(
    _DescribeMatchmakingRuleSetsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **RuleSets** *(list) --*

        Collection of requested matchmaking rule set objects.
        - *(dict) --*

          Set of rule statements, used with FlexMatch, that determine how to build your player
          matches. Each rule set describes a type of group to be created and defines the parameters
          for acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.
          A rule set may define the following elements for a match. For detailed information and
          examples showing how to construct a rule set, see `Build a FlexMatch Rule Set
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ .
          * Teams -- Required. A rule set must define one or multiple teams for the match and set
          minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that
          requires all eight slots to be filled.
          * Player attributes -- Optional. These attributes specify a set of player characteristics
          to evaluate when looking for a match. Matchmaking requests that use a rule set with player
          attributes must provide the corresponding attribute values. For example, an attribute
          might specify a player's skill or level.
          * Rules -- Optional. Rules define how to evaluate potential players for a match based on
          player attributes. A rule might specify minimum requirements for individual players,
          teams, or entire matches. For example, a rule might require each player to meet a certain
          skill level, each team to have at least one player in a certain role, or the match to have
          a minimum average skill level. or may describe an entire group--such as all teams must be
          evenly matched or have at least one player in a certain role.
          * Expansions -- Optional. Expansions allow you to relax the rules after a period of time
          when no acceptable matches are found. This feature lets you balance getting players into
          games in a reasonable amount of time instead of making them wait indefinitely for the best
          possible match. For example, you might use an expansion to increase the maximum skill
          variance between players after 30 seconds.
          - **RuleSetName** *(string) --*

            Unique identifier for a matchmaking rule set
    """


_DescribePlayerSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePlayerSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePlayerSessionsPaginatePaginationConfigTypeDef(
    _DescribePlayerSessionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef = TypedDict(
    "_DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef",
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


class DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef(
    _DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef
):
    """
    - *(dict) --*

      Properties describing a player session. Player session objects are created either by creating
      a player session for a specific game session, or as part of a game session placement. A player
      session represents either a player reservation for a game session (status ``RESERVED`` ) or
      actual player activity in a game session (status ``ACTIVE`` ). A player session object
      (including player data) is automatically passed to a game session when the player connects to
      the game session and is validated.
      When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
      session ends, the player session object is retained for 30 days and then removed.
      *  CreatePlayerSession
      *  CreatePlayerSessions
      *  DescribePlayerSessions
      * Game session placements

        *  StartGameSessionPlacement
        *  DescribeGameSessionPlacement
        *  StopGameSessionPlacement
    """


_DescribePlayerSessionsPaginateResponseTypeDef = TypedDict(
    "_DescribePlayerSessionsPaginateResponseTypeDef",
    {"PlayerSessions": List[DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef]},
    total=False,
)


class DescribePlayerSessionsPaginateResponseTypeDef(_DescribePlayerSessionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **PlayerSessions** *(list) --*

        Collection of objects containing properties for each player session that matches the
        request.
        - *(dict) --*

          Properties describing a player session. Player session objects are created either by
          creating a player session for a specific game session, or as part of a game session
          placement. A player session represents either a player reservation for a game session
          (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A
          player session object (including player data) is automatically passed to a game session
          when the player connects to the game session and is validated.
          When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
          session ends, the player session object is retained for 30 days and then removed.
          *  CreatePlayerSession
          *  CreatePlayerSessions
          *  DescribePlayerSessions
          * Game session placements

            *  StartGameSessionPlacement
            *  DescribeGameSessionPlacement
            *  StopGameSessionPlacement
    """


_DescribeScalingPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingPoliciesPaginatePaginationConfigTypeDef(
    _DescribeScalingPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef",
    {"TargetValue": float},
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef
):
    pass


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
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


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef
):
    """
    - *(dict) --*

      Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the
      combination of name and fleet ID.
      *  DescribeFleetCapacity
      *  UpdateFleetCapacity
      *  DescribeEC2InstanceLimits
      * Manage scaling policies:

        *  PutScalingPolicy (auto-scaling)
        *  DescribeScalingPolicies (auto-scaling)
        *  DeleteScalingPolicy (auto-scaling)
    """


_DescribeScalingPoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseTypeDef",
    {"ScalingPolicies": List[DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef]},
    total=False,
)


class DescribeScalingPoliciesPaginateResponseTypeDef(
    _DescribeScalingPoliciesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **ScalingPolicies** *(list) --*

        Collection of objects containing the scaling policies matching the request.
        - *(dict) --*

          Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the
          combination of name and fleet ID.
          *  DescribeFleetCapacity
          *  UpdateFleetCapacity
          *  DescribeEC2InstanceLimits
          * Manage scaling policies:

            *  PutScalingPolicy (auto-scaling)
            *  DescribeScalingPolicies (auto-scaling)
            *  DeleteScalingPolicy (auto-scaling)
    """


_ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAliasesPaginatePaginationConfigTypeDef(_ListAliasesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)


class ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef(
    _ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef
):
    pass


_ListAliasesPaginateResponseAliasesTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesTypeDef",
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


class ListAliasesPaginateResponseAliasesTypeDef(_ListAliasesPaginateResponseAliasesTypeDef):
    """
    - *(dict) --*

      Properties describing a fleet alias.
      *  CreateAlias
      *  ListAliases
      *  DescribeAlias
      *  UpdateAlias
      *  DeleteAlias
      *  ResolveAlias
      - **AliasId** *(string) --*

        Unique identifier for an alias; alias IDs are unique within a region.
    """


_ListAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAliasesPaginateResponseTypeDef",
    {"Aliases": List[ListAliasesPaginateResponseAliasesTypeDef]},
    total=False,
)


class ListAliasesPaginateResponseTypeDef(_ListAliasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Aliases** *(list) --*

        Collection of alias records that match the list request.
        - *(dict) --*

          Properties describing a fleet alias.
          *  CreateAlias
          *  ListAliases
          *  DescribeAlias
          *  UpdateAlias
          *  DeleteAlias
          *  ResolveAlias
          - **AliasId** *(string) --*

            Unique identifier for an alias; alias IDs are unique within a region.
    """


_ListBuildsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBuildsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBuildsPaginatePaginationConfigTypeDef(_ListBuildsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBuildsPaginateResponseBuildsTypeDef = TypedDict(
    "_ListBuildsPaginateResponseBuildsTypeDef",
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


class ListBuildsPaginateResponseBuildsTypeDef(_ListBuildsPaginateResponseBuildsTypeDef):
    """
    - *(dict) --*

      Properties describing a custom game build.

        **Related operations**
    """


_ListBuildsPaginateResponseTypeDef = TypedDict(
    "_ListBuildsPaginateResponseTypeDef",
    {"Builds": List[ListBuildsPaginateResponseBuildsTypeDef]},
    total=False,
)


class ListBuildsPaginateResponseTypeDef(_ListBuildsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **Builds** *(list) --*

        Collection of build records that match the request.
        - *(dict) --*

          Properties describing a custom game build.

            **Related operations**
    """


_ListFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFleetsPaginatePaginationConfigTypeDef(_ListFleetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFleetsPaginateResponseTypeDef = TypedDict(
    "_ListFleetsPaginateResponseTypeDef", {"FleetIds": List[str]}, total=False
)


class ListFleetsPaginateResponseTypeDef(_ListFleetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **FleetIds** *(list) --*

        Set of fleet IDs matching the list request. You can retrieve additional information about
        all returned fleets by passing this result set to a call to  DescribeFleetAttributes ,
        DescribeFleetCapacity , or  DescribeFleetUtilization .
        - *(string) --*
    """


_SearchGameSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchGameSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchGameSessionsPaginatePaginationConfigTypeDef(
    _SearchGameSessionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "_SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef(
    _SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef
):
    pass


_SearchGameSessionsPaginateResponseGameSessionsTypeDef = TypedDict(
    "_SearchGameSessionsPaginateResponseGameSessionsTypeDef",
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


class SearchGameSessionsPaginateResponseGameSessionsTypeDef(
    _SearchGameSessionsPaginateResponseGameSessionsTypeDef
):
    """
    - *(dict) --*

      Properties describing a game session.
      A game session in ACTIVE status can host players. When a game session ends, its status is set
      to ``TERMINATED`` .
      Once the session ends, the game session object is retained for 30 days. This means you can
      reuse idempotency token values after this time. Game session logs are retained for 14 days.
      *  CreateGameSession
      *  DescribeGameSessions
      *  DescribeGameSessionDetails
      *  SearchGameSessions
      *  UpdateGameSession
      *  GetGameSessionLogUrl
      * Game session placements

        *  StartGameSessionPlacement
        *  DescribeGameSessionPlacement
        *  StopGameSessionPlacement
    """


_SearchGameSessionsPaginateResponseTypeDef = TypedDict(
    "_SearchGameSessionsPaginateResponseTypeDef",
    {"GameSessions": List[SearchGameSessionsPaginateResponseGameSessionsTypeDef]},
    total=False,
)


class SearchGameSessionsPaginateResponseTypeDef(_SearchGameSessionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the returned data in response to a request action.
      - **GameSessions** *(list) --*

        Collection of objects containing game session properties for each session matching the
        request.
        - *(dict) --*

          Properties describing a game session.
          A game session in ACTIVE status can host players. When a game session ends, its status is
          set to ``TERMINATED`` .
          Once the session ends, the game session object is retained for 30 days. This means you can
          reuse idempotency token values after this time. Game session logs are retained for 14
          days.
          *  CreateGameSession
          *  DescribeGameSessions
          *  DescribeGameSessionDetails
          *  SearchGameSessions
          *  UpdateGameSession
          *  GetGameSessionLogUrl
          * Game session placements

            *  StartGameSessionPlacement
            *  DescribeGameSessionPlacement
            *  StopGameSessionPlacement
    """
