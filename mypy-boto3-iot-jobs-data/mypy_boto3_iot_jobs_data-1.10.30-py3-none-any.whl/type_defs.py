"Main interface for iot-jobs-data service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeJobExecutionResponseexecutionTypeDef",
    "ClientDescribeJobExecutionResponseTypeDef",
    "ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef",
    "ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef",
    "ClientGetPendingJobExecutionsResponseTypeDef",
    "ClientStartNextPendingJobExecutionResponseexecutionTypeDef",
    "ClientStartNextPendingJobExecutionResponseTypeDef",
    "ClientUpdateJobExecutionResponseexecutionStateTypeDef",
    "ClientUpdateJobExecutionResponseTypeDef",
)


_ClientDescribeJobExecutionResponseexecutionTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseexecutionTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "statusDetails": Dict[str, str],
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "approximateSecondsBeforeTimedOut": int,
        "versionNumber": int,
        "executionNumber": int,
        "jobDocument": str,
    },
    total=False,
)


class ClientDescribeJobExecutionResponseexecutionTypeDef(
    _ClientDescribeJobExecutionResponseexecutionTypeDef
):
    """
    - **execution** *(dict) --*

      Contains data about a job execution.
      - **jobId** *(string) --*

        The unique identifier you assigned to this job when it was created.
    """


_ClientDescribeJobExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseTypeDef",
    {"execution": ClientDescribeJobExecutionResponseexecutionTypeDef},
    total=False,
)


class ClientDescribeJobExecutionResponseTypeDef(_ClientDescribeJobExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **execution** *(dict) --*

        Contains data about a job execution.
        - **jobId** *(string) --*

          The unique identifier you assigned to this job when it was created.
    """


_ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef = TypedDict(
    "_ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef",
    {
        "jobId": str,
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "versionNumber": int,
        "executionNumber": int,
    },
    total=False,
)


class ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef(
    _ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef
):
    """
    - *(dict) --*

      Contains a subset of information about a job execution.
      - **jobId** *(string) --*

        The unique identifier you assigned to this job when it was created.
    """


_ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef = TypedDict(
    "_ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef",
    {
        "jobId": str,
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "versionNumber": int,
        "executionNumber": int,
    },
    total=False,
)


class ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef(
    _ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef
):
    pass


_ClientGetPendingJobExecutionsResponseTypeDef = TypedDict(
    "_ClientGetPendingJobExecutionsResponseTypeDef",
    {
        "inProgressJobs": List[ClientGetPendingJobExecutionsResponseinProgressJobsTypeDef],
        "queuedJobs": List[ClientGetPendingJobExecutionsResponsequeuedJobsTypeDef],
    },
    total=False,
)


class ClientGetPendingJobExecutionsResponseTypeDef(_ClientGetPendingJobExecutionsResponseTypeDef):
    """
    - *(dict) --*

      - **inProgressJobs** *(list) --*

        A list of JobExecutionSummary objects with status IN_PROGRESS.
        - *(dict) --*

          Contains a subset of information about a job execution.
          - **jobId** *(string) --*

            The unique identifier you assigned to this job when it was created.
    """


_ClientStartNextPendingJobExecutionResponseexecutionTypeDef = TypedDict(
    "_ClientStartNextPendingJobExecutionResponseexecutionTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "statusDetails": Dict[str, str],
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "approximateSecondsBeforeTimedOut": int,
        "versionNumber": int,
        "executionNumber": int,
        "jobDocument": str,
    },
    total=False,
)


class ClientStartNextPendingJobExecutionResponseexecutionTypeDef(
    _ClientStartNextPendingJobExecutionResponseexecutionTypeDef
):
    """
    - **execution** *(dict) --*

      A JobExecution object.
      - **jobId** *(string) --*

        The unique identifier you assigned to this job when it was created.
    """


_ClientStartNextPendingJobExecutionResponseTypeDef = TypedDict(
    "_ClientStartNextPendingJobExecutionResponseTypeDef",
    {"execution": ClientStartNextPendingJobExecutionResponseexecutionTypeDef},
    total=False,
)


class ClientStartNextPendingJobExecutionResponseTypeDef(
    _ClientStartNextPendingJobExecutionResponseTypeDef
):
    """
    - *(dict) --*

      - **execution** *(dict) --*

        A JobExecution object.
        - **jobId** *(string) --*

          The unique identifier you assigned to this job when it was created.
    """


_ClientUpdateJobExecutionResponseexecutionStateTypeDef = TypedDict(
    "_ClientUpdateJobExecutionResponseexecutionStateTypeDef",
    {
        "status": Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ],
        "statusDetails": Dict[str, str],
        "versionNumber": int,
    },
    total=False,
)


class ClientUpdateJobExecutionResponseexecutionStateTypeDef(
    _ClientUpdateJobExecutionResponseexecutionStateTypeDef
):
    """
    - **executionState** *(dict) --*

      A JobExecutionState object.
      - **status** *(string) --*

        The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED",
        "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".
    """


_ClientUpdateJobExecutionResponseTypeDef = TypedDict(
    "_ClientUpdateJobExecutionResponseTypeDef",
    {"executionState": ClientUpdateJobExecutionResponseexecutionStateTypeDef, "jobDocument": str},
    total=False,
)


class ClientUpdateJobExecutionResponseTypeDef(_ClientUpdateJobExecutionResponseTypeDef):
    """
    - *(dict) --*

      - **executionState** *(dict) --*

        A JobExecutionState object.
        - **status** *(string) --*

          The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED",
          "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".
    """
