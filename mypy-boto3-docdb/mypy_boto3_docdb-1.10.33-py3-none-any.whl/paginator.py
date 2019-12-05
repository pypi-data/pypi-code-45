"Main interface for docdb service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_docdb.type_defs import (
    DescribeDBClustersPaginateFiltersTypeDef,
    DescribeDBClustersPaginatePaginationConfigTypeDef,
    DescribeDBClustersPaginateResponseTypeDef,
    DescribeDBEngineVersionsPaginateFiltersTypeDef,
    DescribeDBEngineVersionsPaginatePaginationConfigTypeDef,
    DescribeDBEngineVersionsPaginateResponseTypeDef,
    DescribeDBInstancesPaginateFiltersTypeDef,
    DescribeDBInstancesPaginatePaginationConfigTypeDef,
    DescribeDBInstancesPaginateResponseTypeDef,
    DescribeDBSubnetGroupsPaginateFiltersTypeDef,
    DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef,
    DescribeDBSubnetGroupsPaginateResponseTypeDef,
    DescribeEventsPaginateFiltersTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef,
    DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef,
    DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
)


class DescribeDBClustersPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[DescribeDBClustersPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBClustersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBClustersPaginateResponseTypeDef:
        """
        [DescribeDBClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusters.paginate)
        """


class DescribeDBEngineVersionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_engine_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[DescribeDBEngineVersionsPaginateFiltersTypeDef] = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        PaginationConfig: DescribeDBEngineVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBEngineVersionsPaginateResponseTypeDef:
        """
        [DescribeDBEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeDBEngineVersions.paginate)
        """


class DescribeDBInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[DescribeDBInstancesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBInstancesPaginateResponseTypeDef:
        """
        [DescribeDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeDBInstances.paginate)
        """


class DescribeDBSubnetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_db_subnet_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[DescribeDBSubnetGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeDBSubnetGroupsPaginateResponseTypeDef:
        """
        [DescribeDBSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeDBSubnetGroups.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[DescribeEventsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeEvents.paginate)
        """


class DescribeOrderableDBInstanceOptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_orderable_db_instance_options`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef:
        """
        [DescribeOrderableDBInstanceOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/docdb.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        """
