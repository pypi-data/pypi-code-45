"Main interface for elbv2 service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elbv2.type_defs import (
    LoadBalancerAvailableWaitWaiterConfigTypeDef,
    LoadBalancerExistsWaitWaiterConfigTypeDef,
    LoadBalancersDeletedWaitWaiterConfigTypeDef,
    TargetDeregisteredWaitTargetsTypeDef,
    TargetDeregisteredWaitWaiterConfigTypeDef,
    TargetInServiceWaitTargetsTypeDef,
    TargetInServiceWaitWaiterConfigTypeDef,
)


__all__ = (
    "LoadBalancerAvailableWaiter",
    "LoadBalancerExistsWaiter",
    "LoadBalancersDeletedWaiter",
    "TargetDeregisteredWaiter",
    "TargetInServiceWaiter",
)


class LoadBalancerAvailableWaiter(Boto3Waiter):
    """
    Waiter for `load_balancer_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: LoadBalancerAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [load_balancer_available.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.load_balancer_available.wait)
        """


class LoadBalancerExistsWaiter(Boto3Waiter):
    """
    Waiter for `load_balancer_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: LoadBalancerExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [load_balancer_exists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.load_balancer_exists.wait)
        """


class LoadBalancersDeletedWaiter(Boto3Waiter):
    """
    Waiter for `load_balancers_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: LoadBalancersDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [load_balancers_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.load_balancers_deleted.wait)
        """


class TargetDeregisteredWaiter(Boto3Waiter):
    """
    Waiter for `target_deregistered` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        TargetGroupArn: str,
        Targets: List[TargetDeregisteredWaitTargetsTypeDef] = None,
        WaiterConfig: TargetDeregisteredWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [target_deregistered.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.target_deregistered.wait)
        """


class TargetInServiceWaiter(Boto3Waiter):
    """
    Waiter for `target_in_service` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        TargetGroupArn: str,
        Targets: List[TargetInServiceWaitTargetsTypeDef] = None,
        WaiterConfig: TargetInServiceWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [target_in_service.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.target_in_service.wait)
        """
