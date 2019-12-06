"Main interface for autoscaling service Paginators"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_autoscaling.type_defs import (
    DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef,
    DescribeAutoScalingGroupsPaginateResponseTypeDef,
    DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef,
    DescribeAutoScalingInstancesPaginateResponseTypeDef,
    DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef,
    DescribeLaunchConfigurationsPaginateResponseTypeDef,
    DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef,
    DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef,
    DescribeLoadBalancersPaginatePaginationConfigTypeDef,
    DescribeLoadBalancersPaginateResponseTypeDef,
    DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef,
    DescribeNotificationConfigurationsPaginateResponseTypeDef,
    DescribePoliciesPaginatePaginationConfigTypeDef,
    DescribePoliciesPaginateResponseTypeDef,
    DescribeScalingActivitiesPaginatePaginationConfigTypeDef,
    DescribeScalingActivitiesPaginateResponseTypeDef,
    DescribeScheduledActionsPaginatePaginationConfigTypeDef,
    DescribeScheduledActionsPaginateResponseTypeDef,
    DescribeTagsPaginateFiltersTypeDef,
    DescribeTagsPaginatePaginationConfigTypeDef,
    DescribeTagsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeAutoScalingGroupsPaginator",
    "DescribeAutoScalingInstancesPaginator",
    "DescribeLaunchConfigurationsPaginator",
    "DescribeLoadBalancerTargetGroupsPaginator",
    "DescribeLoadBalancersPaginator",
    "DescribeNotificationConfigurationsPaginator",
    "DescribePoliciesPaginator",
    "DescribeScalingActivitiesPaginator",
    "DescribeScheduledActionsPaginator",
    "DescribeTagsPaginator",
)


class DescribeAutoScalingGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_auto_scaling_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupNames: List[str] = None,
        PaginationConfig: DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAutoScalingGroupsPaginateResponseTypeDef:
        """
        [DescribeAutoScalingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups.paginate)
        """


class DescribeAutoScalingInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_auto_scaling_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceIds: List[str] = None,
        PaginationConfig: DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAutoScalingInstancesPaginateResponseTypeDef:
        """
        [DescribeAutoScalingInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances.paginate)
        """


class DescribeLaunchConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_launch_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LaunchConfigurationNames: List[str] = None,
        PaginationConfig: DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLaunchConfigurationsPaginateResponseTypeDef:
        """
        [DescribeLaunchConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations.paginate)
        """


class DescribeLoadBalancerTargetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_load_balancer_target_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupName: str,
        PaginationConfig: DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef:
        """
        [DescribeLoadBalancerTargetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups.paginate)
        """


class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    Paginator for `describe_load_balancers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupName: str,
        PaginationConfig: DescribeLoadBalancersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLoadBalancersPaginateResponseTypeDef:
        """
        [DescribeLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers.paginate)
        """


class DescribeNotificationConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_notification_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupNames: List[str] = None,
        PaginationConfig: DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeNotificationConfigurationsPaginateResponseTypeDef:
        """
        [DescribeNotificationConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations.paginate)
        """


class DescribePoliciesPaginator(Boto3Paginator):
    """
    Paginator for `describe_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupName: str = None,
        PolicyNames: List[str] = None,
        PolicyTypes: List[str] = None,
        PaginationConfig: DescribePoliciesPaginatePaginationConfigTypeDef = None,
    ) -> DescribePoliciesPaginateResponseTypeDef:
        """
        [DescribePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies.paginate)
        """


class DescribeScalingActivitiesPaginator(Boto3Paginator):
    """
    Paginator for `describe_scaling_activities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ActivityIds: List[str] = None,
        AutoScalingGroupName: str = None,
        PaginationConfig: DescribeScalingActivitiesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeScalingActivitiesPaginateResponseTypeDef:
        """
        [DescribeScalingActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities.paginate)
        """


class DescribeScheduledActionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_scheduled_actions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupName: str = None,
        ScheduledActionNames: List[str] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: DescribeScheduledActionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeScheduledActionsPaginateResponseTypeDef:
        """
        [DescribeScheduledActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    Paginator for `describe_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeTagsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeTagsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTagsPaginateResponseTypeDef:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags.paginate)
        """
