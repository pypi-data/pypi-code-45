"Main interface for signer service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_signer.type_defs import SuccessfulSigningJobWaitWaiterConfigTypeDef


__all__ = ("SuccessfulSigningJobWaiter",)


class SuccessfulSigningJobWaiter(Boto3Waiter):
    """
    Waiter for `successful_signing_job` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, jobId: str, WaiterConfig: SuccessfulSigningJobWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [successful_signing_job.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/signer.html#Signer.Waiter.successful_signing_job.wait)
        """
