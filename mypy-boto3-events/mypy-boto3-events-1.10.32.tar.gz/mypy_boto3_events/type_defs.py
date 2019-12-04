"Main interface for events service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateEventBusResponseTypeDef",
    "ClientCreatePartnerEventSourceResponseTypeDef",
    "ClientDescribeEventBusResponseTypeDef",
    "ClientDescribeEventSourceResponseTypeDef",
    "ClientDescribePartnerEventSourceResponseTypeDef",
    "ClientDescribeRuleResponseTypeDef",
    "ClientListEventBusesResponseEventBusesTypeDef",
    "ClientListEventBusesResponseTypeDef",
    "ClientListEventSourcesResponseEventSourcesTypeDef",
    "ClientListEventSourcesResponseTypeDef",
    "ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef",
    "ClientListPartnerEventSourceAccountsResponseTypeDef",
    "ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef",
    "ClientListPartnerEventSourcesResponseTypeDef",
    "ClientListRuleNamesByTargetResponseTypeDef",
    "ClientListRulesResponseRulesTypeDef",
    "ClientListRulesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef",
    "ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef",
    "ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    "ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef",
    "ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    "ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef",
    "ClientListTargetsByRuleResponseTargetsTypeDef",
    "ClientListTargetsByRuleResponseTypeDef",
    "ClientPutEventsEntriesTypeDef",
    "ClientPutEventsResponseEntriesTypeDef",
    "ClientPutEventsResponseTypeDef",
    "ClientPutPartnerEventsEntriesTypeDef",
    "ClientPutPartnerEventsResponseEntriesTypeDef",
    "ClientPutPartnerEventsResponseTypeDef",
    "ClientPutPermissionConditionTypeDef",
    "ClientPutRuleResponseTypeDef",
    "ClientPutRuleTagsTypeDef",
    "ClientPutTargetsResponseFailedEntriesTypeDef",
    "ClientPutTargetsResponseTypeDef",
    "ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef",
    "ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef",
    "ClientPutTargetsTargetsBatchParametersTypeDef",
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef",
    "ClientPutTargetsTargetsEcsParametersTypeDef",
    "ClientPutTargetsTargetsInputTransformerTypeDef",
    "ClientPutTargetsTargetsKinesisParametersTypeDef",
    "ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef",
    "ClientPutTargetsTargetsRunCommandParametersTypeDef",
    "ClientPutTargetsTargetsSqsParametersTypeDef",
    "ClientPutTargetsTargetsTypeDef",
    "ClientRemoveTargetsResponseFailedEntriesTypeDef",
    "ClientRemoveTargetsResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientTestEventPatternResponseTypeDef",
    "ListRuleNamesByTargetPaginatePaginationConfigTypeDef",
    "ListRuleNamesByTargetPaginateResponseTypeDef",
    "ListRulesPaginatePaginationConfigTypeDef",
    "ListRulesPaginateResponseRulesTypeDef",
    "ListRulesPaginateResponseTypeDef",
    "ListTargetsByRulePaginatePaginationConfigTypeDef",
    "ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef",
    "ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef",
    "ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    "ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    "ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef",
    "ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    "ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef",
    "ListTargetsByRulePaginateResponseTargetsTypeDef",
    "ListTargetsByRulePaginateResponseTypeDef",
)


_ClientCreateEventBusResponseTypeDef = TypedDict(
    "_ClientCreateEventBusResponseTypeDef", {"EventBusArn": str}, total=False
)


class ClientCreateEventBusResponseTypeDef(_ClientCreateEventBusResponseTypeDef):
    """
    - *(dict) --*

      - **EventBusArn** *(string) --*

        The ARN of the new event bus.
    """


_ClientCreatePartnerEventSourceResponseTypeDef = TypedDict(
    "_ClientCreatePartnerEventSourceResponseTypeDef", {"EventSourceArn": str}, total=False
)


class ClientCreatePartnerEventSourceResponseTypeDef(_ClientCreatePartnerEventSourceResponseTypeDef):
    """
    - *(dict) --*

      - **EventSourceArn** *(string) --*

        The ARN of the partner event source.
    """


_ClientDescribeEventBusResponseTypeDef = TypedDict(
    "_ClientDescribeEventBusResponseTypeDef", {"Name": str, "Arn": str, "Policy": str}, total=False
)


class ClientDescribeEventBusResponseTypeDef(_ClientDescribeEventBusResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the event bus. Currently, this is always ``default`` .
    """


_ClientDescribeEventSourceResponseTypeDef = TypedDict(
    "_ClientDescribeEventSourceResponseTypeDef",
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


class ClientDescribeEventSourceResponseTypeDef(_ClientDescribeEventSourceResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The ARN of the partner event source.
    """


_ClientDescribePartnerEventSourceResponseTypeDef = TypedDict(
    "_ClientDescribePartnerEventSourceResponseTypeDef", {"Arn": str, "Name": str}, total=False
)


class ClientDescribePartnerEventSourceResponseTypeDef(
    _ClientDescribePartnerEventSourceResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The ARN of the event source.
    """


_ClientDescribeRuleResponseTypeDef = TypedDict(
    "_ClientDescribeRuleResponseTypeDef",
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


class ClientDescribeRuleResponseTypeDef(_ClientDescribeRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the rule.
    """


_ClientListEventBusesResponseEventBusesTypeDef = TypedDict(
    "_ClientListEventBusesResponseEventBusesTypeDef",
    {"Name": str, "Arn": str, "Policy": str},
    total=False,
)


class ClientListEventBusesResponseEventBusesTypeDef(_ClientListEventBusesResponseEventBusesTypeDef):
    """
    - *(dict) --*

      An event bus receives events from a source and routes them to rules associated with that event
      bus. Your account's default event bus receives rules from AWS services. A custom event bus can
      receive rules from AWS services as well as your custom applications and services. A partner
      event bus receives events from an event source created by an SaaS partner. These events come
      from the partners services or applications.
      - **Name** *(string) --*

        The name of the event bus.
    """


_ClientListEventBusesResponseTypeDef = TypedDict(
    "_ClientListEventBusesResponseTypeDef",
    {"EventBuses": List[ClientListEventBusesResponseEventBusesTypeDef], "NextToken": str},
    total=False,
)


class ClientListEventBusesResponseTypeDef(_ClientListEventBusesResponseTypeDef):
    """
    - *(dict) --*

      - **EventBuses** *(list) --*

        This list of event buses.
        - *(dict) --*

          An event bus receives events from a source and routes them to rules associated with that
          event bus. Your account's default event bus receives rules from AWS services. A custom
          event bus can receive rules from AWS services as well as your custom applications and
          services. A partner event bus receives events from an event source created by an SaaS
          partner. These events come from the partners services or applications.
          - **Name** *(string) --*

            The name of the event bus.
    """


_ClientListEventSourcesResponseEventSourcesTypeDef = TypedDict(
    "_ClientListEventSourcesResponseEventSourcesTypeDef",
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


class ClientListEventSourcesResponseEventSourcesTypeDef(
    _ClientListEventSourcesResponseEventSourcesTypeDef
):
    """
    - *(dict) --*

      A partner event source is created by an SaaS partner. If a customer creates a partner event
      bus that matches this event source, that AWS account can receive events from the partner's
      applications or services.
      - **Arn** *(string) --*

        The ARN of the event source.
    """


_ClientListEventSourcesResponseTypeDef = TypedDict(
    "_ClientListEventSourcesResponseTypeDef",
    {"EventSources": List[ClientListEventSourcesResponseEventSourcesTypeDef], "NextToken": str},
    total=False,
)


class ClientListEventSourcesResponseTypeDef(_ClientListEventSourcesResponseTypeDef):
    """
    - *(dict) --*

      - **EventSources** *(list) --*

        The list of event sources.
        - *(dict) --*

          A partner event source is created by an SaaS partner. If a customer creates a partner
          event bus that matches this event source, that AWS account can receive events from the
          partner's applications or services.
          - **Arn** *(string) --*

            The ARN of the event source.
    """


_ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef = TypedDict(
    "_ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef",
    {
        "Account": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)


class ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef(
    _ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef
):
    """
    - *(dict) --*

      The AWS account that a partner event source has been offered to.
      - **Account** *(string) --*

        The AWS account ID that the partner event source was offered to.
    """


_ClientListPartnerEventSourceAccountsResponseTypeDef = TypedDict(
    "_ClientListPartnerEventSourceAccountsResponseTypeDef",
    {
        "PartnerEventSourceAccounts": List[
            ClientListPartnerEventSourceAccountsResponsePartnerEventSourceAccountsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPartnerEventSourceAccountsResponseTypeDef(
    _ClientListPartnerEventSourceAccountsResponseTypeDef
):
    """
    - *(dict) --*

      - **PartnerEventSourceAccounts** *(list) --*

        The list of partner event sources returned by the operation.
        - *(dict) --*

          The AWS account that a partner event source has been offered to.
          - **Account** *(string) --*

            The AWS account ID that the partner event source was offered to.
    """


_ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef = TypedDict(
    "_ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef",
    {"Arn": str, "Name": str},
    total=False,
)


class ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef(
    _ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef
):
    """
    - *(dict) --*

      A partner event source is created by an SaaS partner. If a customer creates a partner event
      bus that matches this event source, that AWS account can receive events from the partner's
      applications or services.
      - **Arn** *(string) --*

        The ARN of the partner event source.
    """


_ClientListPartnerEventSourcesResponseTypeDef = TypedDict(
    "_ClientListPartnerEventSourcesResponseTypeDef",
    {
        "PartnerEventSources": List[
            ClientListPartnerEventSourcesResponsePartnerEventSourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPartnerEventSourcesResponseTypeDef(_ClientListPartnerEventSourcesResponseTypeDef):
    """
    - *(dict) --*

      - **PartnerEventSources** *(list) --*

        The list of partner event sources returned by the operation.
        - *(dict) --*

          A partner event source is created by an SaaS partner. If a customer creates a partner
          event bus that matches this event source, that AWS account can receive events from the
          partner's applications or services.
          - **Arn** *(string) --*

            The ARN of the partner event source.
    """


_ClientListRuleNamesByTargetResponseTypeDef = TypedDict(
    "_ClientListRuleNamesByTargetResponseTypeDef",
    {"RuleNames": List[str], "NextToken": str},
    total=False,
)


class ClientListRuleNamesByTargetResponseTypeDef(_ClientListRuleNamesByTargetResponseTypeDef):
    """
    - *(dict) --*

      - **RuleNames** *(list) --*

        The names of the rules that can invoke the given target.
        - *(string) --*
    """


_ClientListRulesResponseRulesTypeDef = TypedDict(
    "_ClientListRulesResponseRulesTypeDef",
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


class ClientListRulesResponseRulesTypeDef(_ClientListRulesResponseRulesTypeDef):
    """
    - *(dict) --*

      Contains information about a rule in Amazon EventBridge.
      - **Name** *(string) --*

        The name of the rule.
    """


_ClientListRulesResponseTypeDef = TypedDict(
    "_ClientListRulesResponseTypeDef",
    {"Rules": List[ClientListRulesResponseRulesTypeDef], "NextToken": str},
    total=False,
)


class ClientListRulesResponseTypeDef(_ClientListRulesResponseTypeDef):
    """
    - *(dict) --*

      - **Rules** *(list) --*

        The rules that match the specified criteria.
        - *(dict) --*

          Contains information about a rule in Amazon EventBridge.
          - **Name** *(string) --*

            The name of the rule.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      A key-value pair associated with an AWS resource. In EventBridge, rules support tagging.
      - **Key** *(string) --*

        A string that you can use to assign a value. The combination of tag keys and values can help
        you organize and categorize your resources.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The list of tag keys and values associated with the rule that you specified.
        - *(dict) --*

          A key-value pair associated with an AWS resource. In EventBridge, rules support tagging.
          - **Key** *(string) --*

            A string that you can use to assign a value. The combination of tag keys and values can
            help you organize and categorize your resources.
    """


_ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef",
    {"Size": int},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef(
    _ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef",
    {"Attempts": int},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef(
    _ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ClientListTargetsByRuleResponseTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ClientListTargetsByRuleResponseTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)


class ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsBatchParametersTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "AssignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef(
    _ClientListTargetsByRuleResponseTargetsEcsParametersNetworkConfigurationTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef",
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


class ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsEcsParametersTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef(
    _ClientListTargetsByRuleResponseTargetsInputTransformerTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef",
    {"PartitionKeyPath": str},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsKinesisParametersTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef(
    _ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ClientListTargetsByRuleResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)


class ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsRunCommandParametersTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef",
    {"MessageGroupId": str},
    total=False,
)


class ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef(
    _ClientListTargetsByRuleResponseTargetsSqsParametersTypeDef
):
    pass


_ClientListTargetsByRuleResponseTargetsTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTargetsTypeDef",
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


class ClientListTargetsByRuleResponseTargetsTypeDef(_ClientListTargetsByRuleResponseTargetsTypeDef):
    """
    - *(dict) --*

      Targets are the resources to be invoked when a rule is triggered. For a complete list of
      services and resources that can be set as a target, see  PutTargets .
      If you're setting the event bus of another account as the target and that account granted
      permission to your account through an organization instead of directly by the account ID, you
      must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For more
      information, see `Sending and Receiving Events Between AWS Accounts
      <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
      in the *Amazon EventBridge User Guide* .
      - **Id** *(string) --*

        A name for the target. Use a string that will help you identify the target. Each target
        associated with a rule must have an ``Id`` unique for that rule.
    """


_ClientListTargetsByRuleResponseTypeDef = TypedDict(
    "_ClientListTargetsByRuleResponseTypeDef",
    {"Targets": List[ClientListTargetsByRuleResponseTargetsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTargetsByRuleResponseTypeDef(_ClientListTargetsByRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        The targets assigned to the rule.
        - *(dict) --*

          Targets are the resources to be invoked when a rule is triggered. For a complete list of
          services and resources that can be set as a target, see  PutTargets .
          If you're setting the event bus of another account as the target and that account granted
          permission to your account through an organization instead of directly by the account ID,
          you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For
          more information, see `Sending and Receiving Events Between AWS Accounts
          <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
          in the *Amazon EventBridge User Guide* .
          - **Id** *(string) --*

            A name for the target. Use a string that will help you identify the target. Each target
            associated with a rule must have an ``Id`` unique for that rule.
    """


_ClientPutEventsEntriesTypeDef = TypedDict(
    "_ClientPutEventsEntriesTypeDef",
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


class ClientPutEventsEntriesTypeDef(_ClientPutEventsEntriesTypeDef):
    """
    - *(dict) --*

      Represents an event to be submitted.
      - **Time** *(datetime) --*

        The timestamp of the event, per `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339.txt>`__ .
        If no timestamp is provided, the timestamp of the  PutEvents call is used.
    """


_ClientPutEventsResponseEntriesTypeDef = TypedDict(
    "_ClientPutEventsResponseEntriesTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientPutEventsResponseEntriesTypeDef(_ClientPutEventsResponseEntriesTypeDef):
    pass


_ClientPutEventsResponseTypeDef = TypedDict(
    "_ClientPutEventsResponseTypeDef",
    {"FailedEntryCount": int, "Entries": List[ClientPutEventsResponseEntriesTypeDef]},
    total=False,
)


class ClientPutEventsResponseTypeDef(_ClientPutEventsResponseTypeDef):
    """
    - *(dict) --*

      - **FailedEntryCount** *(integer) --*

        The number of failed entries.
    """


_ClientPutPartnerEventsEntriesTypeDef = TypedDict(
    "_ClientPutPartnerEventsEntriesTypeDef",
    {"Time": datetime, "Source": str, "Resources": List[str], "DetailType": str, "Detail": str},
    total=False,
)


class ClientPutPartnerEventsEntriesTypeDef(_ClientPutPartnerEventsEntriesTypeDef):
    """
    - *(dict) --*

      The details about an event generated by an SaaS partner.
      - **Time** *(datetime) --*

        The date and time of the event.
    """


_ClientPutPartnerEventsResponseEntriesTypeDef = TypedDict(
    "_ClientPutPartnerEventsResponseEntriesTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientPutPartnerEventsResponseEntriesTypeDef(_ClientPutPartnerEventsResponseEntriesTypeDef):
    pass


_ClientPutPartnerEventsResponseTypeDef = TypedDict(
    "_ClientPutPartnerEventsResponseTypeDef",
    {"FailedEntryCount": int, "Entries": List[ClientPutPartnerEventsResponseEntriesTypeDef]},
    total=False,
)


class ClientPutPartnerEventsResponseTypeDef(_ClientPutPartnerEventsResponseTypeDef):
    """
    - *(dict) --*

      - **FailedEntryCount** *(integer) --*

        The number of events from this operation that couldn't be written to the partner event bus.
    """


_RequiredClientPutPermissionConditionTypeDef = TypedDict(
    "_RequiredClientPutPermissionConditionTypeDef", {"Type": str}
)
_OptionalClientPutPermissionConditionTypeDef = TypedDict(
    "_OptionalClientPutPermissionConditionTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutPermissionConditionTypeDef(
    _RequiredClientPutPermissionConditionTypeDef, _OptionalClientPutPermissionConditionTypeDef
):
    """
    This parameter enables you to limit the permission to accounts that fulfill a certain condition,
    such as being a member of a certain AWS organization. For more information about AWS
    Organizations, see `What Is AWS Organizations?
    <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html>`__ in the
    *AWS Organizations User Guide* .
    If you specify ``Condition`` with an AWS organization ID and specify "*" as the value for
    ``Principal`` , you grant permission to all the accounts in the named organization.
    The ``Condition`` is a JSON string that must contain ``Type`` , ``Key`` , and ``Value`` fields.
    - **Type** *(string) --***[REQUIRED]**

      The type of condition. Currently, the only supported value is ``StringEquals`` .
    """


_ClientPutRuleResponseTypeDef = TypedDict(
    "_ClientPutRuleResponseTypeDef", {"RuleArn": str}, total=False
)


class ClientPutRuleResponseTypeDef(_ClientPutRuleResponseTypeDef):
    """
    - *(dict) --*

      - **RuleArn** *(string) --*

        The Amazon Resource Name (ARN) of the rule.
    """


_RequiredClientPutRuleTagsTypeDef = TypedDict("_RequiredClientPutRuleTagsTypeDef", {"Key": str})
_OptionalClientPutRuleTagsTypeDef = TypedDict(
    "_OptionalClientPutRuleTagsTypeDef", {"Value": str}, total=False
)


class ClientPutRuleTagsTypeDef(
    _RequiredClientPutRuleTagsTypeDef, _OptionalClientPutRuleTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair associated with an AWS resource. In EventBridge, rules support tagging.
      - **Key** *(string) --***[REQUIRED]**

        A string that you can use to assign a value. The combination of tag keys and values can help
        you organize and categorize your resources.
    """


_ClientPutTargetsResponseFailedEntriesTypeDef = TypedDict(
    "_ClientPutTargetsResponseFailedEntriesTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientPutTargetsResponseFailedEntriesTypeDef(_ClientPutTargetsResponseFailedEntriesTypeDef):
    pass


_ClientPutTargetsResponseTypeDef = TypedDict(
    "_ClientPutTargetsResponseTypeDef",
    {"FailedEntryCount": int, "FailedEntries": List[ClientPutTargetsResponseFailedEntriesTypeDef]},
    total=False,
)


class ClientPutTargetsResponseTypeDef(_ClientPutTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **FailedEntryCount** *(integer) --*

        The number of failed entries.
    """


_ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "_ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef", {"Size": int}, total=False
)


class ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef(
    _ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef
):
    pass


_ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "_ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef", {"Attempts": int}, total=False
)


class ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef(
    _ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef
):
    pass


_ClientPutTargetsTargetsBatchParametersTypeDef = TypedDict(
    "_ClientPutTargetsTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ClientPutTargetsTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ClientPutTargetsTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)


class ClientPutTargetsTargetsBatchParametersTypeDef(_ClientPutTargetsTargetsBatchParametersTypeDef):
    pass


_ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "AssignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef(
    _ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "_ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientPutTargetsTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef(
    _ClientPutTargetsTargetsEcsParametersNetworkConfigurationTypeDef
):
    pass


_ClientPutTargetsTargetsEcsParametersTypeDef = TypedDict(
    "_ClientPutTargetsTargetsEcsParametersTypeDef",
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


class ClientPutTargetsTargetsEcsParametersTypeDef(_ClientPutTargetsTargetsEcsParametersTypeDef):
    pass


_ClientPutTargetsTargetsInputTransformerTypeDef = TypedDict(
    "_ClientPutTargetsTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)


class ClientPutTargetsTargetsInputTransformerTypeDef(
    _ClientPutTargetsTargetsInputTransformerTypeDef
):
    pass


_ClientPutTargetsTargetsKinesisParametersTypeDef = TypedDict(
    "_ClientPutTargetsTargetsKinesisParametersTypeDef", {"PartitionKeyPath": str}, total=False
)


class ClientPutTargetsTargetsKinesisParametersTypeDef(
    _ClientPutTargetsTargetsKinesisParametersTypeDef
):
    pass


_ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "_ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef(
    _ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef
):
    pass


_ClientPutTargetsTargetsRunCommandParametersTypeDef = TypedDict(
    "_ClientPutTargetsTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ClientPutTargetsTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)


class ClientPutTargetsTargetsRunCommandParametersTypeDef(
    _ClientPutTargetsTargetsRunCommandParametersTypeDef
):
    pass


_ClientPutTargetsTargetsSqsParametersTypeDef = TypedDict(
    "_ClientPutTargetsTargetsSqsParametersTypeDef", {"MessageGroupId": str}, total=False
)


class ClientPutTargetsTargetsSqsParametersTypeDef(_ClientPutTargetsTargetsSqsParametersTypeDef):
    pass


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
    """
    - *(dict) --*

      Targets are the resources to be invoked when a rule is triggered. For a complete list of
      services and resources that can be set as a target, see  PutTargets .
      If you're setting the event bus of another account as the target and that account granted
      permission to your account through an organization instead of directly by the account ID, you
      must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For more
      information, see `Sending and Receiving Events Between AWS Accounts
      <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
      in the *Amazon EventBridge User Guide* .
      - **Id** *(string) --***[REQUIRED]**

        A name for the target. Use a string that will help you identify the target. Each target
        associated with a rule must have an ``Id`` unique for that rule.
    """


_ClientRemoveTargetsResponseFailedEntriesTypeDef = TypedDict(
    "_ClientRemoveTargetsResponseFailedEntriesTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientRemoveTargetsResponseFailedEntriesTypeDef(
    _ClientRemoveTargetsResponseFailedEntriesTypeDef
):
    pass


_ClientRemoveTargetsResponseTypeDef = TypedDict(
    "_ClientRemoveTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List[ClientRemoveTargetsResponseFailedEntriesTypeDef],
    },
    total=False,
)


class ClientRemoveTargetsResponseTypeDef(_ClientRemoveTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **FailedEntryCount** *(integer) --*

        The number of failed entries.
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

      A key-value pair associated with an AWS resource. In EventBridge, rules support tagging.
      - **Key** *(string) --***[REQUIRED]**

        A string that you can use to assign a value. The combination of tag keys and values can help
        you organize and categorize your resources.
    """


_ClientTestEventPatternResponseTypeDef = TypedDict(
    "_ClientTestEventPatternResponseTypeDef", {"Result": bool}, total=False
)


class ClientTestEventPatternResponseTypeDef(_ClientTestEventPatternResponseTypeDef):
    """
    - *(dict) --*

      - **Result** *(boolean) --*

        Indicates whether the event matches the event pattern.
    """


_ListRuleNamesByTargetPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRuleNamesByTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRuleNamesByTargetPaginatePaginationConfigTypeDef(
    _ListRuleNamesByTargetPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRuleNamesByTargetPaginateResponseTypeDef = TypedDict(
    "_ListRuleNamesByTargetPaginateResponseTypeDef", {"RuleNames": List[str]}, total=False
)


class ListRuleNamesByTargetPaginateResponseTypeDef(_ListRuleNamesByTargetPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **RuleNames** *(list) --*

        The names of the rules that can invoke the given target.
        - *(string) --*
    """


_ListRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRulesPaginatePaginationConfigTypeDef(_ListRulesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRulesPaginateResponseRulesTypeDef = TypedDict(
    "_ListRulesPaginateResponseRulesTypeDef",
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


class ListRulesPaginateResponseRulesTypeDef(_ListRulesPaginateResponseRulesTypeDef):
    """
    - *(dict) --*

      Contains information about a rule in Amazon EventBridge.
      - **Name** *(string) --*

        The name of the rule.
    """


_ListRulesPaginateResponseTypeDef = TypedDict(
    "_ListRulesPaginateResponseTypeDef",
    {"Rules": List[ListRulesPaginateResponseRulesTypeDef]},
    total=False,
)


class ListRulesPaginateResponseTypeDef(_ListRulesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Rules** *(list) --*

        The rules that match the specified criteria.
        - *(dict) --*

          Contains information about a rule in Amazon EventBridge.
          - **Name** *(string) --*

            The name of the rule.
    """


_ListTargetsByRulePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsByRulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsByRulePaginatePaginationConfigTypeDef(
    _ListTargetsByRulePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef",
    {"Size": int},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef(
    _ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef",
    {"Attempts": int},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef(
    _ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": ListTargetsByRulePaginateResponseTargetsBatchParametersArrayPropertiesTypeDef,
        "RetryStrategy": ListTargetsByRulePaginateResponseTargetsBatchParametersRetryStrategyTypeDef,
    },
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsBatchParametersTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "AssignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef(
    _ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef(
    _ListTargetsByRulePaginateResponseTargetsEcsParametersNetworkConfigurationTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef",
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


class ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsEcsParametersTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef",
    {"InputPathsMap": Dict[str, str], "InputTemplate": str},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef(
    _ListTargetsByRulePaginateResponseTargetsInputTransformerTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef",
    {"PartitionKeyPath": str},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsKinesisParametersTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef(
    _ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef",
    {
        "RunCommandTargets": List[
            ListTargetsByRulePaginateResponseTargetsRunCommandParametersRunCommandTargetsTypeDef
        ]
    },
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsRunCommandParametersTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef",
    {"MessageGroupId": str},
    total=False,
)


class ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef(
    _ListTargetsByRulePaginateResponseTargetsSqsParametersTypeDef
):
    pass


_ListTargetsByRulePaginateResponseTargetsTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTargetsTypeDef",
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


class ListTargetsByRulePaginateResponseTargetsTypeDef(
    _ListTargetsByRulePaginateResponseTargetsTypeDef
):
    """
    - *(dict) --*

      Targets are the resources to be invoked when a rule is triggered. For a complete list of
      services and resources that can be set as a target, see  PutTargets .
      If you're setting the event bus of another account as the target and that account granted
      permission to your account through an organization instead of directly by the account ID, you
      must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For more
      information, see `Sending and Receiving Events Between AWS Accounts
      <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
      in the *Amazon EventBridge User Guide* .
      - **Id** *(string) --*

        A name for the target. Use a string that will help you identify the target. Each target
        associated with a rule must have an ``Id`` unique for that rule.
    """


_ListTargetsByRulePaginateResponseTypeDef = TypedDict(
    "_ListTargetsByRulePaginateResponseTypeDef",
    {"Targets": List[ListTargetsByRulePaginateResponseTargetsTypeDef]},
    total=False,
)


class ListTargetsByRulePaginateResponseTypeDef(_ListTargetsByRulePaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        The targets assigned to the rule.
        - *(dict) --*

          Targets are the resources to be invoked when a rule is triggered. For a complete list of
          services and resources that can be set as a target, see  PutTargets .
          If you're setting the event bus of another account as the target and that account granted
          permission to your account through an organization instead of directly by the account ID,
          you must specify a ``RoleArn`` with proper permissions in the ``Target`` structure. For
          more information, see `Sending and Receiving Events Between AWS Accounts
          <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html>`__
          in the *Amazon EventBridge User Guide* .
          - **Id** *(string) --*

            A name for the target. Use a string that will help you identify the target. Each target
            associated with a rule must have an ``Id`` unique for that rule.
    """
