"Main interface for sms service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sms.type_defs import (
    GetConnectorsPaginatePaginationConfigTypeDef,
    GetConnectorsPaginateResponseTypeDef,
    GetReplicationJobsPaginatePaginationConfigTypeDef,
    GetReplicationJobsPaginateResponseTypeDef,
    GetReplicationRunsPaginatePaginationConfigTypeDef,
    GetReplicationRunsPaginateResponseTypeDef,
    GetServersPaginatePaginationConfigTypeDef,
    GetServersPaginateResponseTypeDef,
    GetServersPaginateVmServerAddressListTypeDef,
    ListAppsPaginatePaginationConfigTypeDef,
    ListAppsPaginateResponseTypeDef,
)


__all__ = (
    "GetConnectorsPaginator",
    "GetReplicationJobsPaginator",
    "GetReplicationRunsPaginator",
    "GetServersPaginator",
    "ListAppsPaginator",
)


class GetConnectorsPaginator(Boto3Paginator):
    """
    Paginator for `get_connectors`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetConnectorsPaginatePaginationConfigTypeDef = None
    ) -> GetConnectorsPaginateResponseTypeDef:
        """
        [GetConnectors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.GetConnectors.paginate)
        """


class GetReplicationJobsPaginator(Boto3Paginator):
    """
    Paginator for `get_replication_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        replicationJobId: str = None,
        PaginationConfig: GetReplicationJobsPaginatePaginationConfigTypeDef = None,
    ) -> GetReplicationJobsPaginateResponseTypeDef:
        """
        [GetReplicationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.GetReplicationJobs.paginate)
        """


class GetReplicationRunsPaginator(Boto3Paginator):
    """
    Paginator for `get_replication_runs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        replicationJobId: str,
        PaginationConfig: GetReplicationRunsPaginatePaginationConfigTypeDef = None,
    ) -> GetReplicationRunsPaginateResponseTypeDef:
        """
        [GetReplicationRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.GetReplicationRuns.paginate)
        """


class GetServersPaginator(Boto3Paginator):
    """
    Paginator for `get_servers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        vmServerAddressList: List[GetServersPaginateVmServerAddressListTypeDef] = None,
        PaginationConfig: GetServersPaginatePaginationConfigTypeDef = None,
    ) -> GetServersPaginateResponseTypeDef:
        """
        [GetServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.GetServers.paginate)
        """


class ListAppsPaginator(Boto3Paginator):
    """
    Paginator for `list_apps`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        appIds: List[str] = None,
        PaginationConfig: ListAppsPaginatePaginationConfigTypeDef = None,
    ) -> ListAppsPaginateResponseTypeDef:
        """
        [ListApps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.ListApps.paginate)
        """
