"Main interface for ecs service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ecs.type_defs import (
    ListAccountSettingsPaginatePaginationConfigTypeDef,
    ListAccountSettingsPaginateResponseTypeDef,
    ListAttributesPaginatePaginationConfigTypeDef,
    ListAttributesPaginateResponseTypeDef,
    ListClustersPaginatePaginationConfigTypeDef,
    ListClustersPaginateResponseTypeDef,
    ListContainerInstancesPaginatePaginationConfigTypeDef,
    ListContainerInstancesPaginateResponseTypeDef,
    ListServicesPaginatePaginationConfigTypeDef,
    ListServicesPaginateResponseTypeDef,
    ListTaskDefinitionFamiliesPaginatePaginationConfigTypeDef,
    ListTaskDefinitionFamiliesPaginateResponseTypeDef,
    ListTaskDefinitionsPaginatePaginationConfigTypeDef,
    ListTaskDefinitionsPaginateResponseTypeDef,
    ListTasksPaginatePaginationConfigTypeDef,
    ListTasksPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAccountSettingsPaginator",
    "ListAttributesPaginator",
    "ListClustersPaginator",
    "ListContainerInstancesPaginator",
    "ListServicesPaginator",
    "ListTaskDefinitionFamiliesPaginator",
    "ListTaskDefinitionsPaginator",
    "ListTasksPaginator",
)


class ListAccountSettingsPaginator(Boto3Paginator):
    """
    Paginator for `list_account_settings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ] = None,
        value: str = None,
        principalArn: str = None,
        effectiveSettings: bool = None,
        PaginationConfig: ListAccountSettingsPaginatePaginationConfigTypeDef = None,
    ) -> ListAccountSettingsPaginateResponseTypeDef:
        """
        [ListAccountSettings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ecs.html#ECS.Paginator.ListAccountSettings.paginate)
        """


class ListAttributesPaginator(Boto3Paginator):
    """
    Paginator for `list_attributes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        targetType: str,
        cluster: str = None,
        attributeName: str = None,
        attributeValue: str = None,
        PaginationConfig: ListAttributesPaginatePaginationConfigTypeDef = None,
    ) -> ListAttributesPaginateResponseTypeDef:
        """
        [ListAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ecs.html#ECS.Paginator.ListAttributes.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    Paginator for `list_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListClustersPaginatePaginationConfigTypeDef = None
    ) -> ListClustersPaginateResponseTypeDef:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ecs.html#ECS.Paginator.ListClusters.paginate)
        """


class ListContainerInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_container_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        cluster: str = None,
        filter: str = None,
        status: Literal[
            "ACTIVE", "DRAINING", "REGISTERING", "DEREGISTERING", "REGISTRATION_FAILED"
        ] = None,
        PaginationConfig: ListContainerInstancesPaginatePaginationConfigTypeDef = None,
    ) -> ListContainerInstancesPaginateResponseTypeDef:
        """
        [ListContainerInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ecs.html#ECS.Paginator.ListContainerInstances.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    Paginator for `list_services`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        cluster: str = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        schedulingStrategy: Literal["REPLICA", "DAEMON"] = None,
        PaginationConfig: ListServicesPaginatePaginationConfigTypeDef = None,
    ) -> ListServicesPaginateResponseTypeDef:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ecs.html#ECS.Paginator.ListServices.paginate)
        """


class ListTaskDefinitionFamiliesPaginator(Boto3Paginator):
    """
    Paginator for `list_task_definition_families`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE", "ALL"] = None,
        PaginationConfig: ListTaskDefinitionFamiliesPaginatePaginationConfigTypeDef = None,
    ) -> ListTaskDefinitionFamiliesPaginateResponseTypeDef:
        """
        [ListTaskDefinitionFamilies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies.paginate)
        """


class ListTaskDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `list_task_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        sort: Literal["ASC", "DESC"] = None,
        PaginationConfig: ListTaskDefinitionsPaginatePaginationConfigTypeDef = None,
    ) -> ListTaskDefinitionsPaginateResponseTypeDef:
        """
        [ListTaskDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions.paginate)
        """


class ListTasksPaginator(Boto3Paginator):
    """
    Paginator for `list_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        cluster: str = None,
        containerInstance: str = None,
        family: str = None,
        startedBy: str = None,
        serviceName: str = None,
        desiredStatus: Literal["RUNNING", "PENDING", "STOPPED"] = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        PaginationConfig: ListTasksPaginatePaginationConfigTypeDef = None,
    ) -> ListTasksPaginateResponseTypeDef:
        """
        [ListTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/ecs.html#ECS.Paginator.ListTasks.paginate)
        """
