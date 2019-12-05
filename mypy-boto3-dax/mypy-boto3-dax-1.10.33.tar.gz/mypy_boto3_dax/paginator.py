"Main interface for dax service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dax.type_defs import (
    DescribeClustersPaginatePaginationConfigTypeDef,
    DescribeClustersPaginateResponseTypeDef,
    DescribeDefaultParametersPaginatePaginationConfigTypeDef,
    DescribeDefaultParametersPaginateResponseTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    DescribeParameterGroupsPaginatePaginationConfigTypeDef,
    DescribeParameterGroupsPaginateResponseTypeDef,
    DescribeParametersPaginatePaginationConfigTypeDef,
    DescribeParametersPaginateResponseTypeDef,
    DescribeSubnetGroupsPaginatePaginationConfigTypeDef,
    DescribeSubnetGroupsPaginateResponseTypeDef,
    ListTagsPaginatePaginationConfigTypeDef,
    ListTagsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeClustersPaginator",
    "DescribeDefaultParametersPaginator",
    "DescribeEventsPaginator",
    "DescribeParameterGroupsPaginator",
    "DescribeParametersPaginator",
    "DescribeSubnetGroupsPaginator",
    "ListTagsPaginator",
)


class DescribeClustersPaginator(Boto3Paginator):
    """
    Paginator for `describe_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterNames: List[str] = None,
        PaginationConfig: DescribeClustersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeClustersPaginateResponseTypeDef:
        """
        [DescribeClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dax.html#DAX.Paginator.DescribeClusters.paginate)
        """


class DescribeDefaultParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_default_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeDefaultParametersPaginatePaginationConfigTypeDef = None
    ) -> DescribeDefaultParametersPaginateResponseTypeDef:
        """
        [DescribeDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceName: str = None,
        SourceType: Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dax.html#DAX.Paginator.DescribeEvents.paginate)
        """


class DescribeParameterGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_parameter_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParameterGroupNames: List[str] = None,
        PaginationConfig: DescribeParameterGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeParameterGroupsPaginateResponseTypeDef:
        """
        [DescribeParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups.paginate)
        """


class DescribeParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: DescribeParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeParametersPaginateResponseTypeDef:
        """
        [DescribeParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dax.html#DAX.Paginator.DescribeParameters.paginate)
        """


class DescribeSubnetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_subnet_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SubnetGroupNames: List[str] = None,
        PaginationConfig: DescribeSubnetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSubnetGroupsPaginateResponseTypeDef:
        """
        [DescribeSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    Paginator for `list_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceName: str, PaginationConfig: ListTagsPaginatePaginationConfigTypeDef = None
    ) -> ListTagsPaginateResponseTypeDef:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dax.html#DAX.Paginator.ListTags.paginate)
        """
