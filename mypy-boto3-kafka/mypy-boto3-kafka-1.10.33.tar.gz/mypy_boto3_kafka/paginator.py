"Main interface for kafka service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kafka.type_defs import (
    ListClusterOperationsPaginatePaginationConfigTypeDef,
    ListClusterOperationsPaginateResponseTypeDef,
    ListClustersPaginatePaginationConfigTypeDef,
    ListClustersPaginateResponseTypeDef,
    ListConfigurationRevisionsPaginatePaginationConfigTypeDef,
    ListConfigurationRevisionsPaginateResponseTypeDef,
    ListConfigurationsPaginatePaginationConfigTypeDef,
    ListConfigurationsPaginateResponseTypeDef,
    ListNodesPaginatePaginationConfigTypeDef,
    ListNodesPaginateResponseTypeDef,
)


__all__ = (
    "ListClusterOperationsPaginator",
    "ListClustersPaginator",
    "ListConfigurationRevisionsPaginator",
    "ListConfigurationsPaginator",
    "ListNodesPaginator",
)


class ListClusterOperationsPaginator(Boto3Paginator):
    """
    Paginator for `list_cluster_operations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterArn: str,
        PaginationConfig: ListClusterOperationsPaginatePaginationConfigTypeDef = None,
    ) -> ListClusterOperationsPaginateResponseTypeDef:
        """
        [ListClusterOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    Paginator for `list_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterNameFilter: str = None,
        PaginationConfig: ListClustersPaginatePaginationConfigTypeDef = None,
    ) -> ListClustersPaginateResponseTypeDef:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kafka.html#Kafka.Paginator.ListClusters.paginate)
        """


class ListConfigurationRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `list_configuration_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Arn: str,
        PaginationConfig: ListConfigurationRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> ListConfigurationRevisionsPaginateResponseTypeDef:
        """
        [ListConfigurationRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions.paginate)
        """


class ListConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListConfigurationsPaginatePaginationConfigTypeDef = None
    ) -> ListConfigurationsPaginateResponseTypeDef:
        """
        [ListConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kafka.html#Kafka.Paginator.ListConfigurations.paginate)
        """


class ListNodesPaginator(Boto3Paginator):
    """
    Paginator for `list_nodes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ClusterArn: str, PaginationConfig: ListNodesPaginatePaginationConfigTypeDef = None
    ) -> ListNodesPaginateResponseTypeDef:
        """
        [ListNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/kafka.html#Kafka.Paginator.ListNodes.paginate)
        """
