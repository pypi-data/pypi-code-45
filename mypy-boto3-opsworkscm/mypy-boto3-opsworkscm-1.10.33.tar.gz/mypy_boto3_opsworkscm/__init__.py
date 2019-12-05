"Main interface for opsworkscm service"

from mypy_boto3_opsworkscm.client import Client
from mypy_boto3_opsworkscm.paginator import (
    DescribeBackupsPaginator,
    DescribeEventsPaginator,
    DescribeServersPaginator,
)
from mypy_boto3_opsworkscm.waiter import NodeAssociatedWaiter


__all__ = (
    "Client",
    "NodeAssociatedWaiter",
    "DescribeBackupsPaginator",
    "DescribeEventsPaginator",
    "DescribeServersPaginator",
)
