"Main interface for batch service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_batch.type_defs import (
    DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef,
    DescribeComputeEnvironmentsPaginateResponseTypeDef,
    DescribeJobDefinitionsPaginatePaginationConfigTypeDef,
    DescribeJobDefinitionsPaginateResponseTypeDef,
    DescribeJobQueuesPaginatePaginationConfigTypeDef,
    DescribeJobQueuesPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeComputeEnvironmentsPaginator",
    "DescribeJobDefinitionsPaginator",
    "DescribeJobQueuesPaginator",
    "ListJobsPaginator",
)


class DescribeComputeEnvironmentsPaginator(Boto3Paginator):
    """
    Paginator for `describe_compute_environments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        computeEnvironments: List[str] = None,
        PaginationConfig: DescribeComputeEnvironmentsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeComputeEnvironmentsPaginateResponseTypeDef:
        """
        [DescribeComputeEnvironments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments.paginate)
        """


class DescribeJobDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_job_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        jobDefinitions: List[str] = None,
        jobDefinitionName: str = None,
        status: str = None,
        PaginationConfig: DescribeJobDefinitionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeJobDefinitionsPaginateResponseTypeDef:
        """
        [DescribeJobDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions.paginate)
        """


class DescribeJobQueuesPaginator(Boto3Paginator):
    """
    Paginator for `describe_job_queues`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        jobQueues: List[str] = None,
        PaginationConfig: DescribeJobQueuesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeJobQueuesPaginateResponseTypeDef:
        """
        [DescribeJobQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/batch.html#Batch.Paginator.DescribeJobQueues.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ] = None,
        PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListJobsPaginateResponseTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/batch.html#Batch.Paginator.ListJobs.paginate)
        """
