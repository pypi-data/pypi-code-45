"Main interface for elb service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elb.type_defs import (
    AnyInstanceInServiceWaitInstancesTypeDef,
    AnyInstanceInServiceWaitWaiterConfigTypeDef,
    InstanceDeregisteredWaitInstancesTypeDef,
    InstanceDeregisteredWaitWaiterConfigTypeDef,
    InstanceInServiceWaitInstancesTypeDef,
    InstanceInServiceWaitWaiterConfigTypeDef,
)


__all__ = ("AnyInstanceInServiceWaiter", "InstanceDeregisteredWaiter", "InstanceInServiceWaiter")


class AnyInstanceInServiceWaiter(Boto3Waiter):
    """
    Waiter for `any_instance_in_service` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List[AnyInstanceInServiceWaitInstancesTypeDef] = None,
        WaiterConfig: AnyInstanceInServiceWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [any_instance_in_service.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elb.html#ElasticLoadBalancing.Waiter.any_instance_in_service.wait)
        """


class InstanceDeregisteredWaiter(Boto3Waiter):
    """
    Waiter for `instance_deregistered` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List[InstanceDeregisteredWaitInstancesTypeDef] = None,
        WaiterConfig: InstanceDeregisteredWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_deregistered.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elb.html#ElasticLoadBalancing.Waiter.instance_deregistered.wait)
        """


class InstanceInServiceWaiter(Boto3Waiter):
    """
    Waiter for `instance_in_service` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List[InstanceInServiceWaitInstancesTypeDef] = None,
        WaiterConfig: InstanceInServiceWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [instance_in_service.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elb.html#ElasticLoadBalancing.Waiter.instance_in_service.wait)
        """
