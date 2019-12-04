"Main interface for sqs service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientChangeMessageVisibilityBatchEntriesTypeDef",
    "ClientChangeMessageVisibilityBatchResponseFailedTypeDef",
    "ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef",
    "ClientChangeMessageVisibilityBatchResponseTypeDef",
    "ClientCreateQueueResponseTypeDef",
    "ClientDeleteMessageBatchEntriesTypeDef",
    "ClientDeleteMessageBatchResponseFailedTypeDef",
    "ClientDeleteMessageBatchResponseSuccessfulTypeDef",
    "ClientDeleteMessageBatchResponseTypeDef",
    "ClientGetQueueAttributesResponseTypeDef",
    "ClientGetQueueUrlResponseTypeDef",
    "ClientListDeadLetterSourceQueuesResponseTypeDef",
    "ClientListQueueTagsResponseTypeDef",
    "ClientListQueuesResponseTypeDef",
    "ClientReceiveMessageResponseMessagesMessageAttributesTypeDef",
    "ClientReceiveMessageResponseMessagesTypeDef",
    "ClientReceiveMessageResponseTypeDef",
    "ClientSendMessageBatchEntriesMessageAttributesTypeDef",
    "ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef",
    "ClientSendMessageBatchEntriesTypeDef",
    "ClientSendMessageBatchResponseFailedTypeDef",
    "ClientSendMessageBatchResponseSuccessfulTypeDef",
    "ClientSendMessageBatchResponseTypeDef",
    "ClientSendMessageMessageAttributesTypeDef",
    "ClientSendMessageMessageSystemAttributesTypeDef",
    "ClientSendMessageResponseTypeDef",
    "QueueChangeMessageVisibilityBatchEntriesTypeDef",
    "QueueChangeMessageVisibilityBatchResponseFailedTypeDef",
    "QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef",
    "QueueChangeMessageVisibilityBatchResponseTypeDef",
    "QueueDeleteMessagesEntriesTypeDef",
    "QueueDeleteMessagesResponseFailedTypeDef",
    "QueueDeleteMessagesResponseSuccessfulTypeDef",
    "QueueDeleteMessagesResponseTypeDef",
    "QueueSendMessageMessageAttributesTypeDef",
    "QueueSendMessageMessageSystemAttributesTypeDef",
    "QueueSendMessageResponseTypeDef",
    "QueueSendMessagesEntriesMessageAttributesTypeDef",
    "QueueSendMessagesEntriesMessageSystemAttributesTypeDef",
    "QueueSendMessagesEntriesTypeDef",
    "QueueSendMessagesResponseFailedTypeDef",
    "QueueSendMessagesResponseSuccessfulTypeDef",
    "QueueSendMessagesResponseTypeDef",
)


_ClientChangeMessageVisibilityBatchEntriesTypeDef = TypedDict(
    "_ClientChangeMessageVisibilityBatchEntriesTypeDef",
    {"Id": str, "ReceiptHandle": str, "VisibilityTimeout": int},
    total=False,
)


class ClientChangeMessageVisibilityBatchEntriesTypeDef(
    _ClientChangeMessageVisibilityBatchEntriesTypeDef
):
    """
    - *(dict) --*

      Encloses a receipt handle and an entry id for each message in ``  ChangeMessageVisibilityBatch
      .``
      .. warning::

        All of the following list parameters must be prefixed with
        ``ChangeMessageVisibilityBatchRequestEntry.n`` , where ``n`` is an integer value starting
        with ``1`` . For example, a parameter list for this action might look like this:
        ``&ChangeMessageVisibilityBatchRequestEntry.1.Id=change_visibility_msg_2``
        ``&ChangeMessageVisibilityBatchRequestEntry.1.ReceiptHandle=your_receipt_handle``
        ``&ChangeMessageVisibilityBatchRequestEntry.1.VisibilityTimeout=45``
    """


_ClientChangeMessageVisibilityBatchResponseFailedTypeDef = TypedDict(
    "_ClientChangeMessageVisibilityBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class ClientChangeMessageVisibilityBatchResponseFailedTypeDef(
    _ClientChangeMessageVisibilityBatchResponseFailedTypeDef
):
    pass


_ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef = TypedDict(
    "_ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef", {"Id": str}, total=False
)


class ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef(
    _ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef
):
    """
    - *(dict) --*

      Encloses the ``Id`` of an entry in ``  ChangeMessageVisibilityBatch .``
      - **Id** *(string) --*

        Represents a message whose visibility timeout has been changed successfully.
    """


_ClientChangeMessageVisibilityBatchResponseTypeDef = TypedDict(
    "_ClientChangeMessageVisibilityBatchResponseTypeDef",
    {
        "Successful": List[ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientChangeMessageVisibilityBatchResponseFailedTypeDef],
    },
    total=False,
)


class ClientChangeMessageVisibilityBatchResponseTypeDef(
    _ClientChangeMessageVisibilityBatchResponseTypeDef
):
    """
    - *(dict) --*

      For each message in the batch, the response contains a ``
      ChangeMessageVisibilityBatchResultEntry `` tag if the message succeeds or a ``
      BatchResultErrorEntry `` tag if the message fails.
      - **Successful** *(list) --*

        A list of ``  ChangeMessageVisibilityBatchResultEntry `` items.
        - *(dict) --*

          Encloses the ``Id`` of an entry in ``  ChangeMessageVisibilityBatch .``
          - **Id** *(string) --*

            Represents a message whose visibility timeout has been changed successfully.
    """


_ClientCreateQueueResponseTypeDef = TypedDict(
    "_ClientCreateQueueResponseTypeDef", {"QueueUrl": str}, total=False
)


class ClientCreateQueueResponseTypeDef(_ClientCreateQueueResponseTypeDef):
    """
    - *(dict) --*

      Returns the ``QueueUrl`` attribute of the created queue.
      - **QueueUrl** *(string) --*

        The URL of the created Amazon SQS queue.
    """


_RequiredClientDeleteMessageBatchEntriesTypeDef = TypedDict(
    "_RequiredClientDeleteMessageBatchEntriesTypeDef", {"Id": str}
)
_OptionalClientDeleteMessageBatchEntriesTypeDef = TypedDict(
    "_OptionalClientDeleteMessageBatchEntriesTypeDef", {"ReceiptHandle": str}, total=False
)


class ClientDeleteMessageBatchEntriesTypeDef(
    _RequiredClientDeleteMessageBatchEntriesTypeDef, _OptionalClientDeleteMessageBatchEntriesTypeDef
):
    """
    - *(dict) --*

      Encloses a receipt handle and an identifier for it.
      - **Id** *(string) --***[REQUIRED]**

        An identifier for this particular receipt handle. This is used to communicate the result.
        .. note::

          The ``Id`` s of a batch request need to be unique within a request
    """


_ClientDeleteMessageBatchResponseFailedTypeDef = TypedDict(
    "_ClientDeleteMessageBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class ClientDeleteMessageBatchResponseFailedTypeDef(_ClientDeleteMessageBatchResponseFailedTypeDef):
    pass


_ClientDeleteMessageBatchResponseSuccessfulTypeDef = TypedDict(
    "_ClientDeleteMessageBatchResponseSuccessfulTypeDef", {"Id": str}, total=False
)


class ClientDeleteMessageBatchResponseSuccessfulTypeDef(
    _ClientDeleteMessageBatchResponseSuccessfulTypeDef
):
    """
    - *(dict) --*

      Encloses the ``Id`` of an entry in ``  DeleteMessageBatch .``
      - **Id** *(string) --*

        Represents a successfully deleted message.
    """


_ClientDeleteMessageBatchResponseTypeDef = TypedDict(
    "_ClientDeleteMessageBatchResponseTypeDef",
    {
        "Successful": List[ClientDeleteMessageBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientDeleteMessageBatchResponseFailedTypeDef],
    },
    total=False,
)


class ClientDeleteMessageBatchResponseTypeDef(_ClientDeleteMessageBatchResponseTypeDef):
    """
    - *(dict) --*

      For each message in the batch, the response contains a ``  DeleteMessageBatchResultEntry ``
      tag if the message is deleted or a ``  BatchResultErrorEntry `` tag if the message can't be
      deleted.
      - **Successful** *(list) --*

        A list of ``  DeleteMessageBatchResultEntry `` items.
        - *(dict) --*

          Encloses the ``Id`` of an entry in ``  DeleteMessageBatch .``
          - **Id** *(string) --*

            Represents a successfully deleted message.
    """


_ClientGetQueueAttributesResponseTypeDef = TypedDict(
    "_ClientGetQueueAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)


class ClientGetQueueAttributesResponseTypeDef(_ClientGetQueueAttributesResponseTypeDef):
    """
    - *(dict) --*

      A list of returned queue attributes.
      - **Attributes** *(dict) --*

        A map of attributes to their respective values.
        - *(string) --*

          - *(string) --*
    """


_ClientGetQueueUrlResponseTypeDef = TypedDict(
    "_ClientGetQueueUrlResponseTypeDef", {"QueueUrl": str}, total=False
)


class ClientGetQueueUrlResponseTypeDef(_ClientGetQueueUrlResponseTypeDef):
    """
    - *(dict) --*

      For more information, see `Interpreting Responses
      <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-api-responses.html>`__
      in the *Amazon Simple Queue Service Developer Guide* .
      - **QueueUrl** *(string) --*

        The URL of the queue.
    """


_ClientListDeadLetterSourceQueuesResponseTypeDef = TypedDict(
    "_ClientListDeadLetterSourceQueuesResponseTypeDef", {"queueUrls": List[str]}, total=False
)


class ClientListDeadLetterSourceQueuesResponseTypeDef(
    _ClientListDeadLetterSourceQueuesResponseTypeDef
):
    """
    - *(dict) --*

      A list of your dead letter source queues.
      - **queueUrls** *(list) --*

        A list of source queue URLs that have the ``RedrivePolicy`` queue attribute configured with
        a dead-letter queue.
        - *(string) --*
    """


_ClientListQueueTagsResponseTypeDef = TypedDict(
    "_ClientListQueueTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListQueueTagsResponseTypeDef(_ClientListQueueTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The list of all tags added to the specified queue.
        - *(string) --*

          - *(string) --*
    """


_ClientListQueuesResponseTypeDef = TypedDict(
    "_ClientListQueuesResponseTypeDef", {"QueueUrls": List[str]}, total=False
)


class ClientListQueuesResponseTypeDef(_ClientListQueuesResponseTypeDef):
    """
    - *(dict) --*

      A list of your queues.
      - **QueueUrls** *(list) --*

        A list of queue URLs, up to 1,000 entries.
        - *(string) --*
    """


_ClientReceiveMessageResponseMessagesMessageAttributesTypeDef = TypedDict(
    "_ClientReceiveMessageResponseMessagesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class ClientReceiveMessageResponseMessagesMessageAttributesTypeDef(
    _ClientReceiveMessageResponseMessagesMessageAttributesTypeDef
):
    pass


_ClientReceiveMessageResponseMessagesTypeDef = TypedDict(
    "_ClientReceiveMessageResponseMessagesTypeDef",
    {
        "MessageId": str,
        "ReceiptHandle": str,
        "MD5OfBody": str,
        "Body": str,
        "Attributes": Dict[str, str],
        "MD5OfMessageAttributes": str,
        "MessageAttributes": Dict[
            str, ClientReceiveMessageResponseMessagesMessageAttributesTypeDef
        ],
    },
    total=False,
)


class ClientReceiveMessageResponseMessagesTypeDef(_ClientReceiveMessageResponseMessagesTypeDef):
    """
    - *(dict) --*

      An Amazon SQS message.
      - **MessageId** *(string) --*

        A unique identifier for the message. A ``MessageId`` is considered unique across all AWS
        accounts for an extended period of time.
    """


_ClientReceiveMessageResponseTypeDef = TypedDict(
    "_ClientReceiveMessageResponseTypeDef",
    {"Messages": List[ClientReceiveMessageResponseMessagesTypeDef]},
    total=False,
)


class ClientReceiveMessageResponseTypeDef(_ClientReceiveMessageResponseTypeDef):
    """
    - *(dict) --*

      A list of received messages.
      - **Messages** *(list) --*

        A list of messages.
        - *(dict) --*

          An Amazon SQS message.
          - **MessageId** *(string) --*

            A unique identifier for the message. A ``MessageId`` is considered unique across all AWS
            accounts for an extended period of time.
    """


_ClientSendMessageBatchEntriesMessageAttributesTypeDef = TypedDict(
    "_ClientSendMessageBatchEntriesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class ClientSendMessageBatchEntriesMessageAttributesTypeDef(
    _ClientSendMessageBatchEntriesMessageAttributesTypeDef
):
    pass


_ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef = TypedDict(
    "_ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef(
    _ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef
):
    pass


_RequiredClientSendMessageBatchEntriesTypeDef = TypedDict(
    "_RequiredClientSendMessageBatchEntriesTypeDef", {"Id": str}
)
_OptionalClientSendMessageBatchEntriesTypeDef = TypedDict(
    "_OptionalClientSendMessageBatchEntriesTypeDef",
    {
        "MessageBody": str,
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, ClientSendMessageBatchEntriesMessageAttributesTypeDef],
        "MessageSystemAttributes": Dict[
            str, ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class ClientSendMessageBatchEntriesTypeDef(
    _RequiredClientSendMessageBatchEntriesTypeDef, _OptionalClientSendMessageBatchEntriesTypeDef
):
    """
    - *(dict) --*

      Contains the details of a single Amazon SQS message along with an ``Id`` .
      - **Id** *(string) --***[REQUIRED]**

        An identifier for a message in this batch used to communicate the result.
        .. note::

          The ``Id`` s of a batch request need to be unique within a request
          This identifier can have up to 80 characters. The following characters are accepted:
          alphanumeric characters, hyphens(-), and underscores (_).
    """


_ClientSendMessageBatchResponseFailedTypeDef = TypedDict(
    "_ClientSendMessageBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class ClientSendMessageBatchResponseFailedTypeDef(_ClientSendMessageBatchResponseFailedTypeDef):
    pass


_ClientSendMessageBatchResponseSuccessfulTypeDef = TypedDict(
    "_ClientSendMessageBatchResponseSuccessfulTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "SequenceNumber": str,
    },
    total=False,
)


class ClientSendMessageBatchResponseSuccessfulTypeDef(
    _ClientSendMessageBatchResponseSuccessfulTypeDef
):
    """
    - *(dict) --*

      Encloses a ``MessageId`` for a successfully-enqueued message in a ``  SendMessageBatch .``
      - **Id** *(string) --*

        An identifier for the message in this batch.
    """


_ClientSendMessageBatchResponseTypeDef = TypedDict(
    "_ClientSendMessageBatchResponseTypeDef",
    {
        "Successful": List[ClientSendMessageBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientSendMessageBatchResponseFailedTypeDef],
    },
    total=False,
)


class ClientSendMessageBatchResponseTypeDef(_ClientSendMessageBatchResponseTypeDef):
    """
    - *(dict) --*

      For each message in the batch, the response contains a ``  SendMessageBatchResultEntry `` tag
      if the message succeeds or a ``  BatchResultErrorEntry `` tag if the message fails.
      - **Successful** *(list) --*

        A list of ``  SendMessageBatchResultEntry `` items.
        - *(dict) --*

          Encloses a ``MessageId`` for a successfully-enqueued message in a ``  SendMessageBatch .``
          - **Id** *(string) --*

            An identifier for the message in this batch.
    """


_ClientSendMessageMessageAttributesTypeDef = TypedDict(
    "_ClientSendMessageMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class ClientSendMessageMessageAttributesTypeDef(_ClientSendMessageMessageAttributesTypeDef):
    pass


_ClientSendMessageMessageSystemAttributesTypeDef = TypedDict(
    "_ClientSendMessageMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class ClientSendMessageMessageSystemAttributesTypeDef(
    _ClientSendMessageMessageSystemAttributesTypeDef
):
    pass


_ClientSendMessageResponseTypeDef = TypedDict(
    "_ClientSendMessageResponseTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
    },
    total=False,
)


class ClientSendMessageResponseTypeDef(_ClientSendMessageResponseTypeDef):
    """
    - *(dict) --*

      The ``MD5OfMessageBody`` and ``MessageId`` elements.
      - **MD5OfMessageBody** *(string) --*

        An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to
        verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message
        before creating the MD5 digest. For information about MD5, see `RFC1321
        <https://www.ietf.org/rfc/rfc1321.txt>`__ .
    """


_QueueChangeMessageVisibilityBatchEntriesTypeDef = TypedDict(
    "_QueueChangeMessageVisibilityBatchEntriesTypeDef",
    {"Id": str, "ReceiptHandle": str, "VisibilityTimeout": int},
    total=False,
)


class QueueChangeMessageVisibilityBatchEntriesTypeDef(
    _QueueChangeMessageVisibilityBatchEntriesTypeDef
):
    """
    - *(dict) --*

      Encloses a receipt handle and an entry id for each message in ``  ChangeMessageVisibilityBatch
      .``
      .. warning::

        All of the following list parameters must be prefixed with
        ``ChangeMessageVisibilityBatchRequestEntry.n`` , where ``n`` is an integer value starting
        with ``1`` . For example, a parameter list for this action might look like this:
        ``&ChangeMessageVisibilityBatchRequestEntry.1.Id=change_visibility_msg_2``
        ``&ChangeMessageVisibilityBatchRequestEntry.1.ReceiptHandle=your_receipt_handle``
        ``&ChangeMessageVisibilityBatchRequestEntry.1.VisibilityTimeout=45``
    """


_QueueChangeMessageVisibilityBatchResponseFailedTypeDef = TypedDict(
    "_QueueChangeMessageVisibilityBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class QueueChangeMessageVisibilityBatchResponseFailedTypeDef(
    _QueueChangeMessageVisibilityBatchResponseFailedTypeDef
):
    pass


_QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef = TypedDict(
    "_QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef", {"Id": str}, total=False
)


class QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef(
    _QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef
):
    """
    - *(dict) --*

      Encloses the ``Id`` of an entry in ``  ChangeMessageVisibilityBatch .``
      - **Id** *(string) --*

        Represents a message whose visibility timeout has been changed successfully.
    """


_QueueChangeMessageVisibilityBatchResponseTypeDef = TypedDict(
    "_QueueChangeMessageVisibilityBatchResponseTypeDef",
    {
        "Successful": List[QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef],
        "Failed": List[QueueChangeMessageVisibilityBatchResponseFailedTypeDef],
    },
    total=False,
)


class QueueChangeMessageVisibilityBatchResponseTypeDef(
    _QueueChangeMessageVisibilityBatchResponseTypeDef
):
    """
    - *(dict) --*

      For each message in the batch, the response contains a ``
      ChangeMessageVisibilityBatchResultEntry `` tag if the message succeeds or a ``
      BatchResultErrorEntry `` tag if the message fails.
      - **Successful** *(list) --*

        A list of ``  ChangeMessageVisibilityBatchResultEntry `` items.
        - *(dict) --*

          Encloses the ``Id`` of an entry in ``  ChangeMessageVisibilityBatch .``
          - **Id** *(string) --*

            Represents a message whose visibility timeout has been changed successfully.
    """


_RequiredQueueDeleteMessagesEntriesTypeDef = TypedDict(
    "_RequiredQueueDeleteMessagesEntriesTypeDef", {"Id": str}
)
_OptionalQueueDeleteMessagesEntriesTypeDef = TypedDict(
    "_OptionalQueueDeleteMessagesEntriesTypeDef", {"ReceiptHandle": str}, total=False
)


class QueueDeleteMessagesEntriesTypeDef(
    _RequiredQueueDeleteMessagesEntriesTypeDef, _OptionalQueueDeleteMessagesEntriesTypeDef
):
    """
    - *(dict) --*

      Encloses a receipt handle and an identifier for it.
      - **Id** *(string) --***[REQUIRED]**

        An identifier for this particular receipt handle. This is used to communicate the result.
        .. note::

          The ``Id`` s of a batch request need to be unique within a request
    """


_QueueDeleteMessagesResponseFailedTypeDef = TypedDict(
    "_QueueDeleteMessagesResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class QueueDeleteMessagesResponseFailedTypeDef(_QueueDeleteMessagesResponseFailedTypeDef):
    pass


_QueueDeleteMessagesResponseSuccessfulTypeDef = TypedDict(
    "_QueueDeleteMessagesResponseSuccessfulTypeDef", {"Id": str}, total=False
)


class QueueDeleteMessagesResponseSuccessfulTypeDef(_QueueDeleteMessagesResponseSuccessfulTypeDef):
    """
    - *(dict) --*

      Encloses the ``Id`` of an entry in ``  DeleteMessageBatch .``
      - **Id** *(string) --*

        Represents a successfully deleted message.
    """


_QueueDeleteMessagesResponseTypeDef = TypedDict(
    "_QueueDeleteMessagesResponseTypeDef",
    {
        "Successful": List[QueueDeleteMessagesResponseSuccessfulTypeDef],
        "Failed": List[QueueDeleteMessagesResponseFailedTypeDef],
    },
    total=False,
)


class QueueDeleteMessagesResponseTypeDef(_QueueDeleteMessagesResponseTypeDef):
    """
    - *(dict) --*

      For each message in the batch, the response contains a ``  DeleteMessageBatchResultEntry ``
      tag if the message is deleted or a ``  BatchResultErrorEntry `` tag if the message can't be
      deleted.
      - **Successful** *(list) --*

        A list of ``  DeleteMessageBatchResultEntry `` items.
        - *(dict) --*

          Encloses the ``Id`` of an entry in ``  DeleteMessageBatch .``
          - **Id** *(string) --*

            Represents a successfully deleted message.
    """


_QueueSendMessageMessageAttributesTypeDef = TypedDict(
    "_QueueSendMessageMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class QueueSendMessageMessageAttributesTypeDef(_QueueSendMessageMessageAttributesTypeDef):
    pass


_QueueSendMessageMessageSystemAttributesTypeDef = TypedDict(
    "_QueueSendMessageMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class QueueSendMessageMessageSystemAttributesTypeDef(
    _QueueSendMessageMessageSystemAttributesTypeDef
):
    pass


_QueueSendMessageResponseTypeDef = TypedDict(
    "_QueueSendMessageResponseTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
    },
    total=False,
)


class QueueSendMessageResponseTypeDef(_QueueSendMessageResponseTypeDef):
    """
    - *(dict) --*

      The ``MD5OfMessageBody`` and ``MessageId`` elements.
      - **MD5OfMessageBody** *(string) --*

        An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to
        verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message
        before creating the MD5 digest. For information about MD5, see `RFC1321
        <https://www.ietf.org/rfc/rfc1321.txt>`__ .
    """


_QueueSendMessagesEntriesMessageAttributesTypeDef = TypedDict(
    "_QueueSendMessagesEntriesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class QueueSendMessagesEntriesMessageAttributesTypeDef(
    _QueueSendMessagesEntriesMessageAttributesTypeDef
):
    pass


_QueueSendMessagesEntriesMessageSystemAttributesTypeDef = TypedDict(
    "_QueueSendMessagesEntriesMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)


class QueueSendMessagesEntriesMessageSystemAttributesTypeDef(
    _QueueSendMessagesEntriesMessageSystemAttributesTypeDef
):
    pass


_RequiredQueueSendMessagesEntriesTypeDef = TypedDict(
    "_RequiredQueueSendMessagesEntriesTypeDef", {"Id": str}
)
_OptionalQueueSendMessagesEntriesTypeDef = TypedDict(
    "_OptionalQueueSendMessagesEntriesTypeDef",
    {
        "MessageBody": str,
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, QueueSendMessagesEntriesMessageAttributesTypeDef],
        "MessageSystemAttributes": Dict[
            str, QueueSendMessagesEntriesMessageSystemAttributesTypeDef
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class QueueSendMessagesEntriesTypeDef(
    _RequiredQueueSendMessagesEntriesTypeDef, _OptionalQueueSendMessagesEntriesTypeDef
):
    """
    - *(dict) --*

      Contains the details of a single Amazon SQS message along with an ``Id`` .
      - **Id** *(string) --***[REQUIRED]**

        An identifier for a message in this batch used to communicate the result.
        .. note::

          The ``Id`` s of a batch request need to be unique within a request
          This identifier can have up to 80 characters. The following characters are accepted:
          alphanumeric characters, hyphens(-), and underscores (_).
    """


_QueueSendMessagesResponseFailedTypeDef = TypedDict(
    "_QueueSendMessagesResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)


class QueueSendMessagesResponseFailedTypeDef(_QueueSendMessagesResponseFailedTypeDef):
    pass


_QueueSendMessagesResponseSuccessfulTypeDef = TypedDict(
    "_QueueSendMessagesResponseSuccessfulTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "SequenceNumber": str,
    },
    total=False,
)


class QueueSendMessagesResponseSuccessfulTypeDef(_QueueSendMessagesResponseSuccessfulTypeDef):
    """
    - *(dict) --*

      Encloses a ``MessageId`` for a successfully-enqueued message in a ``  SendMessageBatch .``
      - **Id** *(string) --*

        An identifier for the message in this batch.
    """


_QueueSendMessagesResponseTypeDef = TypedDict(
    "_QueueSendMessagesResponseTypeDef",
    {
        "Successful": List[QueueSendMessagesResponseSuccessfulTypeDef],
        "Failed": List[QueueSendMessagesResponseFailedTypeDef],
    },
    total=False,
)


class QueueSendMessagesResponseTypeDef(_QueueSendMessagesResponseTypeDef):
    """
    - *(dict) --*

      For each message in the batch, the response contains a ``  SendMessageBatchResultEntry `` tag
      if the message succeeds or a ``  BatchResultErrorEntry `` tag if the message fails.
      - **Successful** *(list) --*

        A list of ``  SendMessageBatchResultEntry `` items.
        - *(dict) --*

          Encloses a ``MessageId`` for a successfully-enqueued message in a ``  SendMessageBatch .``
          - **Id** *(string) --*

            An identifier for the message in this batch.
    """
