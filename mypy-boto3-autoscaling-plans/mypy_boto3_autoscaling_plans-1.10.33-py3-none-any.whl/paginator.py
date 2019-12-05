"Main interface for autoscaling-plans service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_autoscaling_plans.type_defs import (
    DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef,
    DescribeScalingPlanResourcesPaginateResponseTypeDef,
    DescribeScalingPlansPaginateApplicationSourcesTypeDef,
    DescribeScalingPlansPaginatePaginationConfigTypeDef,
    DescribeScalingPlansPaginateResponseTypeDef,
)


__all__ = ("DescribeScalingPlanResourcesPaginator", "DescribeScalingPlansPaginator")


class DescribeScalingPlanResourcesPaginator(Boto3Paginator):
    """
    Paginator for `describe_scaling_plan_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        PaginationConfig: DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeScalingPlanResourcesPaginateResponseTypeDef:
        """
        [DescribeScalingPlanResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources.paginate)
        """


class DescribeScalingPlansPaginator(Boto3Paginator):
    """
    Paginator for `describe_scaling_plans`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ScalingPlanNames: List[str] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List[DescribeScalingPlansPaginateApplicationSourcesTypeDef] = None,
        PaginationConfig: DescribeScalingPlansPaginatePaginationConfigTypeDef = None,
    ) -> DescribeScalingPlansPaginateResponseTypeDef:
        """
        [DescribeScalingPlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans.paginate)
        """
