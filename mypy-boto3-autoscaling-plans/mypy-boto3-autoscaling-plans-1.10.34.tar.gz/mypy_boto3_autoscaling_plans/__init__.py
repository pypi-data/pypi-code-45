"Main interface for autoscaling-plans service"

from mypy_boto3_autoscaling_plans.client import Client
from mypy_boto3_autoscaling_plans.paginator import (
    DescribeScalingPlanResourcesPaginator,
    DescribeScalingPlansPaginator,
)


__all__ = ("Client", "DescribeScalingPlanResourcesPaginator", "DescribeScalingPlansPaginator")
