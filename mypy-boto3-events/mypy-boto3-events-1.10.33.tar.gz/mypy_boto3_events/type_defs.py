"Main interface for events service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateEventBusResponseTypeDef = TypedDict(
    "ClientCreateEventBusResponseTypeDef", {"EventBusArn": str}, total=False
)

ClientCreatePartnerEventSourceResponseTypeDef = TypedDict(
    "ClientCreatePartnerEventSourceResponseTypeDef", {"EventSourceArn": str}, total=False
)

ClientDescribeEventBusResponseTypeDef = TypedDict(
    "ClientDescribeEventBusResponseTypeDef", {"Name": str, "Arn": str, "Policy": str}, total=False
)

ClientDescribeEventSourceResponseTypeDef = TypedDict(
    "ClientDescribeEventSourceResponseTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)

ClientDescribePartnerEventSourceResponseTypeDef = TypedDict(
    "ClientDescribePartnerEventSourceResponseTypeDef", {"Arn": str, "Name": str}, total=False
)

ClientDescribeRuleResponseTypeDef = TypedDict(
    "ClientDescribeRuleResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "ScheduleExpression": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

ClientListEventBusesResponseEventBusesTypeDef = TypedDict(
    "ClientListEventBusesResponseEventBusesTypeDef",
    {"Name": str, "Arn": str, "Policy": str},
    total=False,
)

ClientListEventBusesResponseTypeDef = TypedDict(
    "ClientListEventBusesResponseTypeDef",
    {"EventBuses": List[ClientListEventBusesResponseEventBusesTypeDef], "NextToken": str},
    total=False,
)

ClientListEventSourcesResponseEventSourcesTypeDef = TypedDict(
    "ClientListEventSourcesResponseEventSourcesTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)

ClientListEventSourcesResponseTypeDef = TypedDict(
    "ClientListEventSourcesResponseTypeDef",
    {"EventSources": List[ClientListEventSourcesResponseEventSourcesTypeDef], "NextToken": str},
    total=False,
)

ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef = TypedDict(
    "ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef",
    {
        "Account": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)

ClientListPartnerEventSourceAccountsResponseTypeDef = TypedDict(
    "ClientListPartnerEventSourceAccountsResponseTypeDef",
    {
        "PartnerEventSourceAccounts": List[
            ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef = TypedDict(
    "ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef",
    {"Arn": str, "Name": str},
    total=False,
)

ClientListPartnerEventSourcesResponseTypeDef = TypedDict(
    "ClientListPartnerEventSourcesResponseTypeDef",
    {
        "PartnerEventSources": List[
            ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListRuleNamesByTargetResponseTypeDef = TypedDict(
    "ClientListRuleNamesByTargetResponseTypeDef",
    {"RuleNames": List[str], "NextToken": str},
    total=False,
)

ClientListRulesResponseRulesTypeDef = TypedDict(
    "ClientListRulesResponseRulesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

ClientListRulesResponseTypeDef = TypedDict(
    "ClientListRulesResponseTypeDef",
    {"Rules": List[ClientListRulesResponseRulesTypeDef], "NextToken": str},
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

ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef",
    {"Size": int},
    total=False,
)

ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef",
    {"Attempts": int},
    total=False,
)

ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "AssignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": int,
        "LaunchType": Literal["EC2", "FARGATE"],
        "NetworkConfiguration": ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)

ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef",
    {"PartitionKeyPath": str},
    total=False,
)

ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)

ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef",
    {"MessageGroupId": str},
    total=False,
)

ClientListTargetsByRuleResponseTargetsTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTargetsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef,
        "KinesisParameters": ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef,
        "RunCommandParameters": ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef,
        "EcsParameters": ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef,
        "BatchParameters": ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef,
        "SqsParameters": ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef,
    },
    total=False,
)

ClientListTargetsByRuleResponseTypeDef = TypedDict(
    "ClientListTargetsByRuleResponseTypeDef",
    {"Targets": List[ClientListTargetsByRuleResponseTargetsTypeDef], "NextToken": str},
    total=False,
)

ClientPutEventsEntriesTypeDef = TypedDict(
    "ClientPutEventsEntriesTypeDef",
    {
        "Time": datetime,
        "Source": str,
        "Resources": List[str],
        "DetailType": str,
        "Detail": str,
        "EventBusName": str,
    },
    total=False,
)

ClientPutEventsResponseEntriesTypeDef = TypedDict(
    "ClientPutEventsResponseEntriesTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientPutEventsResponseTypeDef = TypedDict(
    "ClientPutEventsResponseTypeDef",
    {"FailedEntryCount": int, "Entries": List[ClientPutEventsResponseEntriesTypeDef]},
    total=False,
)

ClientPutPartnerEventsEntriesTypeDef = TypedDict(
    "ClientPutPartnerEventsEntriesTypeDef",
    {"Time": datetime, "Source": str, "Resources": List[str], "DetailType": str, "Detail": str},
    total=False,
)

ClientPutPartnerEventsResponseEntriesTypeDef = TypedDict(
    "ClientPutPartnerEventsResponseEntriesTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientPutPartnerEventsResponseTypeDef = TypedDict(
    "ClientPutPartnerEventsResponseTypeDef",
    {"FailedEntryCount": int, "Entries": List[ClientPutPartnerEventsResponseEntriesTypeDef]},
    total=False,
)

_RequiredClientPutPermissionConditionTypeDef = TypedDict(
    "_RequiredClientPutPermissionConditionTypeDef", {"Type": str}
)
_OptionalClientPutPermissionConditionTypeDef = TypedDict(
    "_OptionalClientPutPermissionConditionTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutPermissionConditionTypeDef(
    _RequiredClientPutPermissionConditionTypeDef, _OptionalClientPutPermissionConditionTypeDef
):
    pass


ClientPutRuleResponseTypeDef = TypedDict(
    "ClientPutRuleResponseTypeDef", {"RuleArn": str}, total=False
)

_RequiredClientPutRuleTagsTypeDef = TypedDict("_RequiredClientPutRuleTagsTypeDef", {"Key": str})
_OptionalClientPutRuleTagsTypeDef = TypedDict(
    "_OptionalClientPutRuleTagsTypeDef", {"Value": str}, total=False
)


class ClientPutRuleTagsTypeDef(
    _RequiredClientPutRuleTagsTypeDef, _OptionalClientPutRuleTagsTypeDef
):
    pass


ClientPutTargetsResponseFailedEntriesTypeDef = TypedDict(
    "ClientPutTargetsResponseFailedEntriesTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientPutTargetsResponseTypeDef = TypedDict(
    "ClientPutTargetsResponseTypeDef",
    {"FailedEntryCount": int, "FailedEntries": List[ClientPutTargetsResponseFailedEntriesTypeDef]},
    total=False,
)

ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef", {"Size": int}, total=False
)

ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef", {"Attempts": int}, total=False
)

ClientPutTargetsTargetsBatchParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)

ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "AssignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientPutTargetsTargetsEcsParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": int,
        "LaunchType": Literal["EC2", "FARGATE"],
        "NetworkConfiguration": ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)

ClientPutTargetsTargetsInputTransformerTypeDef = TypedDict(
    "ClientPutTargetsTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)

ClientPutTargetsTargetsKinesisParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsKinesisParametersTypeDef", {"PartitionKeyPath": str}, total=False
)

ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientPutTargetsTargetsRunCommandParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)

ClientPutTargetsTargetsSqsParametersTypeDef = TypedDict(
    "ClientPutTargetsTargetsSqsParametersTypeDef", {"MessageGroupId": str}, total=False
)

_RequiredClientPutTargetsTargetsTypeDef = TypedDict(
    "_RequiredClientPutTargetsTargetsTypeDef", {"Id": str}
)
_OptionalClientPutTargetsTargetsTypeDef = TypedDict(
    "_OptionalClientPutTargetsTargetsTypeDef",
    {
        "Arn": str,
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": ClientPutTargetsTargetsInputTransformerTypeDef,
        "KinesisParameters": ClientPutTargetsTargetsKinesisParametersTypeDef,
        "RunCommandParameters": ClientPutTargetsTargetsRunCommandParametersTypeDef,
        "EcsParameters": ClientPutTargetsTargetsEcsParametersTypeDef,
        "BatchParameters": ClientPutTargetsTargetsBatchParametersTypeDef,
        "SqsParameters": ClientPutTargetsTargetsSqsParametersTypeDef,
    },
    total=False,
)


class ClientPutTargetsTargetsTypeDef(
    _RequiredClientPutTargetsTargetsTypeDef, _OptionalClientPutTargetsTargetsTypeDef
):
    pass


ClientRemoveTargetsResponseFailedEntriesTypeDef = TypedDict(
    "ClientRemoveTargetsResponseFailedEntriesTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientRemoveTargetsResponseTypeDef = TypedDict(
    "ClientRemoveTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List[ClientRemoveTargetsResponseFailedEntriesTypeDef],
    },
    total=False,
)

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


ClientTestEventPatternResponseTypeDef = TypedDict(
    "ClientTestEventPatternResponseTypeDef", {"Result": bool}, total=False
)

ListRuleNamesByTargetPaginatePaginationConfigTypeDef = TypedDict(
    "ListRuleNamesByTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRuleNamesByTargetPaginateResponseTypeDef = TypedDict(
    "ListRuleNamesByTargetPaginateResponseTypeDef", {"RuleNames": List[str]}, total=False
)

ListRulesPaginatePaginationConfigTypeDef = TypedDict(
    "ListRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRulesPaginateResponseRulesTypeDef = TypedDict(
    "ListRulesPaginateResponseRulesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

ListRulesPaginateResponseTypeDef = TypedDict(
    "ListRulesPaginateResponseTypeDef",
    {"Rules": List[ListRulesPaginateResponseRulesTypeDef]},
    total=False,
)

ListTargetsByRulePaginatePaginationConfigTypeDef = TypedDict(
    "ListTargetsByRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef",
    {"Size": int},
    total=False,
)

ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef",
    {"Attempts": int},
    total=False,
)

ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)

ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "AssignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": int,
        "LaunchType": Literal["EC2", "FARGATE"],
        "NetworkConfiguration": ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef,
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)

ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)

ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef",
    {"PartitionKeyPath": str},
    total=False,
)

ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)

ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef",
    {"MessageGroupId": str},
    total=False,
)

ListTargetsByRulePaginateResponseTargetsTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTargetsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef,
        "KinesisParameters": ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef,
        "RunCommandParameters": ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef,
        "EcsParameters": ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef,
        "BatchParameters": ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef,
        "SqsParameters": ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef,
    },
    total=False,
)

ListTargetsByRulePaginateResponseTypeDef = TypedDict(
    "ListTargetsByRulePaginateResponseTypeDef",
    {"Targets": List[ListTargetsByRulePaginateResponseTargetsTypeDef]},
    total=False,
)
