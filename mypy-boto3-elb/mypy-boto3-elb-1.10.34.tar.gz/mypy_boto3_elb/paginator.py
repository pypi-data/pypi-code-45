"Main interface for elb service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elb.type_defs import (
    DescribeAccountLimitsPaginatePaginationConfigTypeDef,
    DescribeAccountLimitsPaginateResponseTypeDef,
    DescribeLoadBalancersPaginatePaginationConfigTypeDef,
    DescribeLoadBalancersPaginateResponseTypeDef,
)


__all__ = ("DescribeAccountLimitsPaginator", "DescribeLoadBalancersPaginator")


class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    Paginator for `describe_account_limits`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeAccountLimitsPaginatePaginationConfigTypeDef = None
    ) -> DescribeAccountLimitsPaginateResponseTypeDef:
        """
        [DescribeAccountLimits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits.paginate)
        """


class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    Paginator for `describe_load_balancers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LoadBalancerNames: List[str] = None,
        PaginationConfig: DescribeLoadBalancersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLoadBalancersPaginateResponseTypeDef:
        """
        [DescribeLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers.paginate)
        """
