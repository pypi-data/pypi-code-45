"Main interface for codestar-notifications service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_codestar_notifications.client as client_scope

# pylint: disable=import-self
import mypy_boto3_codestar_notifications.paginator as paginator_scope
from mypy_boto3_codestar_notifications.type_defs import (
    ClientCreateNotificationRuleResponseTypeDef,
    ClientCreateNotificationRuleTargetsTypeDef,
    ClientDeleteNotificationRuleResponseTypeDef,
    ClientDescribeNotificationRuleResponseTypeDef,
    ClientListEventTypesFiltersTypeDef,
    ClientListEventTypesResponseTypeDef,
    ClientListNotificationRulesFiltersTypeDef,
    ClientListNotificationRulesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTargetsFiltersTypeDef,
    ClientListTargetsResponseTypeDef,
    ClientSubscribeResponseTypeDef,
    ClientSubscribeTargetTypeDef,
    ClientTagResourceResponseTypeDef,
    ClientUnsubscribeResponseTypeDef,
    ClientUpdateNotificationRuleTargetsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [CodeStarNotifications.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_notification_rule(
        self,
        Name: str,
        EventTypeIds: List[str],
        Resource: str,
        Targets: List[ClientCreateNotificationRuleTargetsTypeDef],
        DetailType: Literal["BASIC", "FULL"],
        ClientRequestToken: str = None,
        Tags: Dict[str, str] = None,
        Status: Literal["ENABLED", "DISABLED"] = None,
    ) -> ClientCreateNotificationRuleResponseTypeDef:
        """
        [Client.create_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.create_notification_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_notification_rule(self, Arn: str) -> ClientDeleteNotificationRuleResponseTypeDef:
        """
        [Client.delete_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.delete_notification_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_target(self, TargetAddress: str, ForceUnsubscribeAll: bool = None) -> Dict[str, Any]:
        """
        [Client.delete_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.delete_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_notification_rule(self, Arn: str) -> ClientDescribeNotificationRuleResponseTypeDef:
        """
        [Client.describe_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.describe_notification_rule)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_event_types(
        self,
        Filters: List[ClientListEventTypesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEventTypesResponseTypeDef:
        """
        [Client.list_event_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_event_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_notification_rules(
        self,
        Filters: List[ClientListNotificationRulesFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListNotificationRulesResponseTypeDef:
        """
        [Client.list_notification_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_notification_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, Arn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_targets(
        self,
        Filters: List[ClientListTargetsFiltersTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListTargetsResponseTypeDef:
        """
        [Client.list_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def subscribe(
        self, Arn: str, Target: ClientSubscribeTargetTypeDef, ClientRequestToken: str = None
    ) -> ClientSubscribeResponseTypeDef:
        """
        [Client.subscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.subscribe)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, Arn: str, Tags: Dict[str, str]) -> ClientTagResourceResponseTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unsubscribe(self, Arn: str, TargetAddress: str) -> ClientUnsubscribeResponseTypeDef:
        """
        [Client.unsubscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.unsubscribe)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, Arn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_notification_rule(
        self,
        Arn: str,
        Name: str = None,
        Status: Literal["ENABLED", "DISABLED"] = None,
        EventTypeIds: List[str] = None,
        Targets: List[ClientUpdateNotificationRuleTargetsTypeDef] = None,
        DetailType: Literal["BASIC", "FULL"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Client.update_notification_rule)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_event_types"]
    ) -> paginator_scope.ListEventTypesPaginator:
        """
        [Paginator.ListEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListEventTypes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_notification_rules"]
    ) -> paginator_scope.ListNotificationRulesPaginator:
        """
        [Paginator.ListNotificationRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListNotificationRules)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_targets"]
    ) -> paginator_scope.ListTargetsPaginator:
        """
        [Paginator.ListTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListTargets)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    ConfigurationException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError
