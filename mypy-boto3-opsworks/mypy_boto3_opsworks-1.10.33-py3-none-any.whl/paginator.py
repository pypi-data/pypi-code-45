"Main interface for opsworks service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_opsworks.type_defs import (
    DescribeEcsClustersPaginatePaginationConfigTypeDef,
    DescribeEcsClustersPaginateResponseTypeDef,
)


__all__ = ("DescribeEcsClustersPaginator",)


class DescribeEcsClustersPaginator(Boto3Paginator):
    """
    Paginator for `describe_ecs_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EcsClusterArns: List[str] = None,
        StackId: str = None,
        PaginationConfig: DescribeEcsClustersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEcsClustersPaginateResponseTypeDef:
        """
        [DescribeEcsClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters.paginate)
        """
