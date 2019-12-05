"Main interface for elastictranscoder service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elastictranscoder.type_defs import JobCompleteWaitWaiterConfigTypeDef


__all__ = ("JobCompleteWaiter",)


class JobCompleteWaiter(Boto3Waiter):
    """
    Waiter for `job_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, Id: str, WaiterConfig: JobCompleteWaitWaiterConfigTypeDef = None) -> None:
        """
        [job_complete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.job_complete.wait)
        """
