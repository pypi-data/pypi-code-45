"Main interface for rekognition service"

from mypy_boto3_rekognition.client import Client
from mypy_boto3_rekognition.paginator import (
    DescribeProjectVersionsPaginator,
    DescribeProjectsPaginator,
    ListCollectionsPaginator,
    ListFacesPaginator,
    ListStreamProcessorsPaginator,
)
from mypy_boto3_rekognition.waiter import (
    ProjectVersionRunningWaiter,
    ProjectVersionTrainingCompletedWaiter,
)


__all__ = (
    "Client",
    "ProjectVersionRunningWaiter",
    "ProjectVersionTrainingCompletedWaiter",
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListFacesPaginator",
    "ListStreamProcessorsPaginator",
)
