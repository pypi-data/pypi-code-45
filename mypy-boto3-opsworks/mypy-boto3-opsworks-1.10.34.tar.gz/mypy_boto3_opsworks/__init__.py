"Main interface for opsworks service"

from mypy_boto3_opsworks.client import Client
from mypy_boto3_opsworks.paginator import DescribeEcsClustersPaginator
from mypy_boto3_opsworks.service_resource import ServiceResource
from mypy_boto3_opsworks.waiter import (
    AppExistsWaiter,
    DeploymentSuccessfulWaiter,
    InstanceOnlineWaiter,
    InstanceRegisteredWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
)


__all__ = (
    "Client",
    "ServiceResource",
    "AppExistsWaiter",
    "DeploymentSuccessfulWaiter",
    "InstanceOnlineWaiter",
    "InstanceRegisteredWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
    "DescribeEcsClustersPaginator",
)
