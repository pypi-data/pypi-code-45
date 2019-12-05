"Main interface for servicediscovery service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_servicediscovery.type_defs import (
    ListInstancesPaginatePaginationConfigTypeDef,
    ListInstancesPaginateResponseTypeDef,
    ListNamespacesPaginateFiltersTypeDef,
    ListNamespacesPaginatePaginationConfigTypeDef,
    ListNamespacesPaginateResponseTypeDef,
    ListOperationsPaginateFiltersTypeDef,
    ListOperationsPaginatePaginationConfigTypeDef,
    ListOperationsPaginateResponseTypeDef,
    ListServicesPaginateFiltersTypeDef,
    ListServicesPaginatePaginationConfigTypeDef,
    ListServicesPaginateResponseTypeDef,
)


__all__ = (
    "ListInstancesPaginator",
    "ListNamespacesPaginator",
    "ListOperationsPaginator",
    "ListServicesPaginator",
)


class ListInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ServiceId: str, PaginationConfig: ListInstancesPaginatePaginationConfigTypeDef = None
    ) -> ListInstancesPaginateResponseTypeDef:
        """
        [ListInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances.paginate)
        """


class ListNamespacesPaginator(Boto3Paginator):
    """
    Paginator for `list_namespaces`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListNamespacesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListNamespacesPaginatePaginationConfigTypeDef = None,
    ) -> ListNamespacesPaginateResponseTypeDef:
        """
        [ListNamespaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces.paginate)
        """


class ListOperationsPaginator(Boto3Paginator):
    """
    Paginator for `list_operations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListOperationsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListOperationsPaginatePaginationConfigTypeDef = None,
    ) -> ListOperationsPaginateResponseTypeDef:
        """
        [ListOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    Paginator for `list_services`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListServicesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListServicesPaginatePaginationConfigTypeDef = None,
    ) -> ListServicesPaginateResponseTypeDef:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices.paginate)
        """
