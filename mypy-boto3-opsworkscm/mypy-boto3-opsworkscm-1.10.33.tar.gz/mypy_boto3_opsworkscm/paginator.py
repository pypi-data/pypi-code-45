"Main interface for opsworkscm service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_opsworkscm.type_defs import (
    DescribeBackupsPaginatePaginationConfigTypeDef,
    DescribeBackupsPaginateResponseTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    DescribeServersPaginatePaginationConfigTypeDef,
    DescribeServersPaginateResponseTypeDef,
)


__all__ = ("DescribeBackupsPaginator", "DescribeEventsPaginator", "DescribeServersPaginator")


class DescribeBackupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_backups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BackupId: str = None,
        ServerName: str = None,
        PaginationConfig: DescribeBackupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeBackupsPaginateResponseTypeDef:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServerName: str,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents.paginate)
        """


class DescribeServersPaginator(Boto3Paginator):
    """
    Paginator for `describe_servers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServerName: str = None,
        PaginationConfig: DescribeServersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeServersPaginateResponseTypeDef:
        """
        [DescribeServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers.paginate)
        """
