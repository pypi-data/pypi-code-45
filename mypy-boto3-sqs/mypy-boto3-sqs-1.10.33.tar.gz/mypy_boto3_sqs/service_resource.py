"Main interface for sqs service ServiceResource"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_sqs.service_resource as service_resource_scope
from mypy_boto3_sqs.type_defs import (
    QueueChangeMessageVisibilityBatchEntriesTypeDef,
    QueueChangeMessageVisibilityBatchResponseTypeDef,
    QueueDeleteMessagesEntriesTypeDef,
    QueueDeleteMessagesResponseTypeDef,
    QueueSendMessageMessageAttributesTypeDef,
    QueueSendMessageMessageSystemAttributesTypeDef,
    QueueSendMessageResponseTypeDef,
    QueueSendMessagesEntriesTypeDef,
    QueueSendMessagesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ServiceResource",
    "Message",
    "Queue",
    "ServiceResourceQueuesCollection",
    "QueueDeadLetterSourceQueuesCollection",
)


class ServiceResource(Boto3ServiceResource):
    """
    [SQS.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.ServiceResource)
    """

    queues: service_resource_scope.ServiceResourceQueuesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Message(self, queue_url: str, receipt_handle: str) -> service_resource_scope.Message:
        """
        [ServiceResource.Message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.ServiceResource.Message)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Queue(self, url: str) -> service_resource_scope.Queue:
        """
        [ServiceResource.Queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.ServiceResource.Queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_queue(
        self, QueueName: str, Attributes: Dict[str, str] = None, tags: Dict[str, str] = None
    ) -> service_resource_scope.Queue:
        """
        [ServiceResource.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.ServiceResource.create_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.ServiceResource.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_queue_by_name(
        self, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> service_resource_scope.Queue:
        """
        [ServiceResource.get_queue_by_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.ServiceResource.get_queue_by_name)
        """


class Message(Boto3ServiceResource):
    """
    [Message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.ServiceResource.Message)
    """

    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict[str, Any]
    md5_of_message_attributes: str
    message_attributes: Dict[str, Any]
    queue_url: str
    receipt_handle: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_visibility(self, VisibilityTimeout: int) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class Queue(Boto3ServiceResource):
    """
    [Queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.ServiceResource.Queue)
    """

    attributes: Dict[str, Any]
    url: str
    dead_letter_source_queues: service_resource_scope.QueueDeadLetterSourceQueuesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_permission(self, Label: str, AWSAccountIds: List[str], Actions: List[str]) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_message_visibility_batch(
        self, Entries: List[QueueChangeMessageVisibilityBatchEntriesTypeDef]
    ) -> QueueChangeMessageVisibilityBatchResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_messages(
        self, Entries: List[QueueDeleteMessagesEntriesTypeDef]
    ) -> QueueDeleteMessagesResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purge(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def receive_messages(
        self,
        AttributeNames: List[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ]
        ] = None,
        MessageAttributeNames: List[str] = None,
        MaxNumberOfMessages: int = None,
        VisibilityTimeout: int = None,
        WaitTimeSeconds: int = None,
        ReceiveRequestAttemptId: str = None,
    ) -> List[service_resource_scope.Message]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_permission(self, Label: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_message(
        self,
        MessageBody: str,
        DelaySeconds: int = None,
        MessageAttributes: Dict[str, QueueSendMessageMessageAttributesTypeDef] = None,
        MessageSystemAttributes: Dict[str, QueueSendMessageMessageSystemAttributesTypeDef] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> QueueSendMessageResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_messages(
        self, Entries: List[QueueSendMessagesEntriesTypeDef]
    ) -> QueueSendMessagesResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        pass


class ServiceResourceQueuesCollection(ResourceCollection):
    """
    [ServiceResource.queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.ServiceResource.queues)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Queue]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, QueueNamePrefix: str = None) -> List[service_resource_scope.Queue]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Queue]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Queue]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class QueueDeadLetterSourceQueuesCollection(ResourceCollection):
    """
    [Queue.dead_letter_source_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sqs.html#SQS.Queue.dead_letter_source_queues)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Queue]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, **kwargs: Any) -> List[service_resource_scope.Queue]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Queue]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Queue]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass
