"Main interface for elasticbeanstalk service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elasticbeanstalk.type_defs import (
    DescribeApplicationVersionsPaginatePaginationConfigTypeDef,
    DescribeApplicationVersionsPaginateResponseTypeDef,
    DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef,
    DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef,
    DescribeEnvironmentsPaginatePaginationConfigTypeDef,
    DescribeEnvironmentsPaginateResponseTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    ListPlatformVersionsPaginateFiltersTypeDef,
    ListPlatformVersionsPaginatePaginationConfigTypeDef,
    ListPlatformVersionsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeApplicationVersionsPaginator",
    "DescribeEnvironmentManagedActionHistoryPaginator",
    "DescribeEnvironmentsPaginator",
    "DescribeEventsPaginator",
    "ListPlatformVersionsPaginator",
)


class DescribeApplicationVersionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_application_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabels: List[str] = None,
        PaginationConfig: DescribeApplicationVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeApplicationVersionsPaginateResponseTypeDef:
        """
        [DescribeApplicationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions.paginate)
        """


class DescribeEnvironmentManagedActionHistoryPaginator(Boto3Paginator):
    """
    Paginator for `describe_environment_managed_action_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PaginationConfig: DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef:
        """
        [DescribeEnvironmentManagedActionHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory.paginate)
        """


class DescribeEnvironmentsPaginator(Boto3Paginator):
    """
    Paginator for `describe_environments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        PaginationConfig: DescribeEnvironmentsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEnvironmentsPaginateResponseTypeDef:
        """
        [DescribeEnvironments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PlatformArn: str = None,
        RequestId: str = None,
        Severity: Literal["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents.paginate)
        """


class ListPlatformVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_platform_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListPlatformVersionsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListPlatformVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListPlatformVersionsPaginateResponseTypeDef:
        """
        [ListPlatformVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions.paginate)
        """
