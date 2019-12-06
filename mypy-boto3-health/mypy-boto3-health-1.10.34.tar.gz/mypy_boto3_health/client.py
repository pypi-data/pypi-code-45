"Main interface for health service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_health.client as client_scope

# pylint: disable=import-self
import mypy_boto3_health.paginator as paginator_scope
from mypy_boto3_health.type_defs import (
    ClientDescribeAffectedEntitiesFilterTypeDef,
    ClientDescribeAffectedEntitiesResponseTypeDef,
    ClientDescribeEntityAggregatesResponseTypeDef,
    ClientDescribeEventAggregatesFilterTypeDef,
    ClientDescribeEventAggregatesResponseTypeDef,
    ClientDescribeEventDetailsResponseTypeDef,
    ClientDescribeEventTypesFilterTypeDef,
    ClientDescribeEventTypesResponseTypeDef,
    ClientDescribeEventsFilterTypeDef,
    ClientDescribeEventsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [Health.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_affected_entities(
        self,
        filter: ClientDescribeAffectedEntitiesFilterTypeDef,
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeAffectedEntitiesResponseTypeDef:
        """
        [Client.describe_affected_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Client.describe_affected_entities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_entity_aggregates(
        self, eventArns: List[str] = None
    ) -> ClientDescribeEntityAggregatesResponseTypeDef:
        """
        [Client.describe_entity_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Client.describe_entity_aggregates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_aggregates(
        self,
        aggregateField: str,
        filter: ClientDescribeEventAggregatesFilterTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeEventAggregatesResponseTypeDef:
        """
        [Client.describe_event_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Client.describe_event_aggregates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_details(
        self, eventArns: List[str], locale: str = None
    ) -> ClientDescribeEventDetailsResponseTypeDef:
        """
        [Client.describe_event_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Client.describe_event_details)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_types(
        self,
        filter: ClientDescribeEventTypesFilterTypeDef = None,
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeEventTypesResponseTypeDef:
        """
        [Client.describe_event_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Client.describe_event_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_events(
        self,
        filter: ClientDescribeEventsFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
        locale: str = None,
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Client.describe_events)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Client.generate_presigned_url)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_affected_entities"]
    ) -> paginator_scope.DescribeAffectedEntitiesPaginator:
        """
        [Paginator.DescribeAffectedEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Paginator.DescribeAffectedEntities)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_event_aggregates"]
    ) -> paginator_scope.DescribeEventAggregatesPaginator:
        """
        [Paginator.DescribeEventAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Paginator.DescribeEventAggregates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_event_types"]
    ) -> paginator_scope.DescribeEventTypesPaginator:
        """
        [Paginator.DescribeEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Paginator.DescribeEventTypes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/health.html#Health.Paginator.DescribeEvents)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidPaginationToken: Boto3ClientError
    UnsupportedLocale: Boto3ClientError
