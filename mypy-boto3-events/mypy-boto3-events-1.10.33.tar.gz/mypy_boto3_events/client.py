"Main interface for events service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_events.client as client_scope

# pylint: disable=import-self
import mypy_boto3_events.paginator as paginator_scope
from mypy_boto3_events.type_defs import (
    ClientCreateEventBusResponseTypeDef,
    ClientCreatePartnerEventSourceResponseTypeDef,
    ClientDescribeEventBusResponseTypeDef,
    ClientDescribeEventSourceResponseTypeDef,
    ClientDescribePartnerEventSourceResponseTypeDef,
    ClientDescribeRuleResponseTypeDef,
    ClientListEventBusesResponseTypeDef,
    ClientListEventSourcesResponseTypeDef,
    ClientListPartnerEventSourceAccountsResponseTypeDef,
    ClientListPartnerEventSourcesResponseTypeDef,
    ClientListRuleNamesByTargetResponseTypeDef,
    ClientListRulesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTargetsByRuleResponseTypeDef,
    ClientPutEventsEntriesTypeDef,
    ClientPutEventsResponseTypeDef,
    ClientPutPartnerEventsEntriesTypeDef,
    ClientPutPartnerEventsResponseTypeDef,
    ClientPutPermissionConditionTypeDef,
    ClientPutRuleResponseTypeDef,
    ClientPutRuleTagsTypeDef,
    ClientPutTargetsResponseTypeDef,
    ClientPutTargetsTargetsTypeDef,
    ClientRemoveTargetsResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientTestEventPatternResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [EventBridge.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate_event_source(self, Name: str) -> None:
        """
        [Client.activate_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.activate_event_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_event_bus(
        self, Name: str, EventSourceName: str = None
    ) -> ClientCreateEventBusResponseTypeDef:
        """
        [Client.create_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.create_event_bus)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_partner_event_source(
        self, Name: str, Account: str
    ) -> ClientCreatePartnerEventSourceResponseTypeDef:
        """
        [Client.create_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.create_partner_event_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate_event_source(self, Name: str) -> None:
        """
        [Client.deactivate_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.deactivate_event_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_event_bus(self, Name: str) -> None:
        """
        [Client.delete_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.delete_event_bus)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_partner_event_source(self, Name: str, Account: str) -> None:
        """
        [Client.delete_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.delete_partner_event_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_rule(self, Name: str, EventBusName: str = None, Force: bool = None) -> None:
        """
        [Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.delete_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_bus(self, Name: str = None) -> ClientDescribeEventBusResponseTypeDef:
        """
        [Client.describe_event_bus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.describe_event_bus)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_source(self, Name: str) -> ClientDescribeEventSourceResponseTypeDef:
        """
        [Client.describe_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.describe_event_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_partner_event_source(
        self, Name: str
    ) -> ClientDescribePartnerEventSourceResponseTypeDef:
        """
        [Client.describe_partner_event_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.describe_partner_event_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_rule(
        self, Name: str, EventBusName: str = None
    ) -> ClientDescribeRuleResponseTypeDef:
        """
        [Client.describe_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.describe_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_rule(self, Name: str, EventBusName: str = None) -> None:
        """
        [Client.disable_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.disable_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_rule(self, Name: str, EventBusName: str = None) -> None:
        """
        [Client.enable_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.enable_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_event_buses(
        self, NamePrefix: str = None, NextToken: str = None, Limit: int = None
    ) -> ClientListEventBusesResponseTypeDef:
        """
        [Client.list_event_buses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.list_event_buses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_event_sources(
        self, NamePrefix: str = None, NextToken: str = None, Limit: int = None
    ) -> ClientListEventSourcesResponseTypeDef:
        """
        [Client.list_event_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.list_event_sources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_partner_event_source_accounts(
        self, EventSourceName: str, NextToken: str = None, Limit: int = None
    ) -> ClientListPartnerEventSourceAccountsResponseTypeDef:
        """
        [Client.list_partner_event_source_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.list_partner_event_source_accounts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_partner_event_sources(
        self, NamePrefix: str, NextToken: str = None, Limit: int = None
    ) -> ClientListPartnerEventSourcesResponseTypeDef:
        """
        [Client.list_partner_event_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.list_partner_event_sources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_rule_names_by_target(
        self, TargetArn: str, EventBusName: str = None, NextToken: str = None, Limit: int = None
    ) -> ClientListRuleNamesByTargetResponseTypeDef:
        """
        [Client.list_rule_names_by_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.list_rule_names_by_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_rules(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ClientListRulesResponseTypeDef:
        """
        [Client.list_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.list_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceARN: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_targets_by_rule(
        self, Rule: str, EventBusName: str = None, NextToken: str = None, Limit: int = None
    ) -> ClientListTargetsByRuleResponseTypeDef:
        """
        [Client.list_targets_by_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.list_targets_by_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_events(
        self, Entries: List[ClientPutEventsEntriesTypeDef]
    ) -> ClientPutEventsResponseTypeDef:
        """
        [Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.put_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_partner_events(
        self, Entries: List[ClientPutPartnerEventsEntriesTypeDef]
    ) -> ClientPutPartnerEventsResponseTypeDef:
        """
        [Client.put_partner_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.put_partner_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_permission(
        self,
        Action: str,
        Principal: str,
        StatementId: str,
        EventBusName: str = None,
        Condition: ClientPutPermissionConditionTypeDef = None,
    ) -> None:
        """
        [Client.put_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.put_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_rule(
        self,
        Name: str,
        ScheduleExpression: str = None,
        EventPattern: str = None,
        State: Literal["ENABLED", "DISABLED"] = None,
        Description: str = None,
        RoleArn: str = None,
        Tags: List[ClientPutRuleTagsTypeDef] = None,
        EventBusName: str = None,
    ) -> ClientPutRuleResponseTypeDef:
        """
        [Client.put_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.put_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_targets(
        self, Rule: str, Targets: List[ClientPutTargetsTargetsTypeDef], EventBusName: str = None
    ) -> ClientPutTargetsResponseTypeDef:
        """
        [Client.put_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.put_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_permission(self, StatementId: str, EventBusName: str = None) -> None:
        """
        [Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.remove_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_targets(
        self, Rule: str, Ids: List[str], EventBusName: str = None, Force: bool = None
    ) -> ClientRemoveTargetsResponseTypeDef:
        """
        [Client.remove_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.remove_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_event_pattern(
        self, EventPattern: str, Event: str
    ) -> ClientTestEventPatternResponseTypeDef:
        """
        [Client.test_event_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.test_event_pattern)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Client.untag_resource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_rule_names_by_target"]
    ) -> paginator_scope.ListRuleNamesByTargetPaginator:
        """
        [Paginator.ListRuleNamesByTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_rules"]
    ) -> paginator_scope.ListRulesPaginator:
        """
        [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Paginator.ListRules)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_targets_by_rule"]
    ) -> paginator_scope.ListTargetsByRulePaginator:
        """
        [Paginator.ListTargetsByRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidEventPatternException: Boto3ClientError
    InvalidStateException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ManagedRuleException: Boto3ClientError
    PolicyLengthExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
