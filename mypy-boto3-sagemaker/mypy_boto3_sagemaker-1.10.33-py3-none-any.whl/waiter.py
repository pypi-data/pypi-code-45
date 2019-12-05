"Main interface for sagemaker service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_sagemaker.type_defs import (
    EndpointDeletedWaitWaiterConfigTypeDef,
    EndpointInServiceWaitWaiterConfigTypeDef,
    NotebookInstanceDeletedWaitWaiterConfigTypeDef,
    NotebookInstanceInServiceWaitWaiterConfigTypeDef,
    NotebookInstanceStoppedWaitWaiterConfigTypeDef,
    ProcessingJobCompletedOrStoppedWaitWaiterConfigTypeDef,
    TrainingJobCompletedOrStoppedWaitWaiterConfigTypeDef,
    TransformJobCompletedOrStoppedWaitWaiterConfigTypeDef,
)


__all__ = (
    "EndpointDeletedWaiter",
    "EndpointInServiceWaiter",
    "NotebookInstanceDeletedWaiter",
    "NotebookInstanceInServiceWaiter",
    "NotebookInstanceStoppedWaiter",
    "ProcessingJobCompletedOrStoppedWaiter",
    "TrainingJobCompletedOrStoppedWaiter",
    "TransformJobCompletedOrStoppedWaiter",
)


class EndpointDeletedWaiter(Boto3Waiter):
    """
    Waiter for `endpoint_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, EndpointName: str, WaiterConfig: EndpointDeletedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [endpoint_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Waiter.endpoint_deleted.wait)
        """


class EndpointInServiceWaiter(Boto3Waiter):
    """
    Waiter for `endpoint_in_service` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, EndpointName: str, WaiterConfig: EndpointInServiceWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        [endpoint_in_service.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Waiter.endpoint_in_service.wait)
        """


class NotebookInstanceDeletedWaiter(Boto3Waiter):
    """
    Waiter for `notebook_instance_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: NotebookInstanceDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [notebook_instance_deleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Waiter.notebook_instance_deleted.wait)
        """


class NotebookInstanceInServiceWaiter(Boto3Waiter):
    """
    Waiter for `notebook_instance_in_service` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: NotebookInstanceInServiceWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [notebook_instance_in_service.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Waiter.notebook_instance_in_service.wait)
        """


class NotebookInstanceStoppedWaiter(Boto3Waiter):
    """
    Waiter for `notebook_instance_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: NotebookInstanceStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [notebook_instance_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Waiter.notebook_instance_stopped.wait)
        """


class ProcessingJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    Waiter for `processing_job_completed_or_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ProcessingJobName: str,
        WaiterConfig: ProcessingJobCompletedOrStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [processing_job_completed_or_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Waiter.processing_job_completed_or_stopped.wait)
        """


class TrainingJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    Waiter for `training_job_completed_or_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        TrainingJobName: str,
        WaiterConfig: TrainingJobCompletedOrStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [training_job_completed_or_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Waiter.training_job_completed_or_stopped.wait)
        """


class TransformJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    Waiter for `transform_job_completed_or_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        TransformJobName: str,
        WaiterConfig: TransformJobCompletedOrStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [transform_job_completed_or_stopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sagemaker.html#SageMaker.Waiter.transform_job_completed_or_stopped.wait)
        """
