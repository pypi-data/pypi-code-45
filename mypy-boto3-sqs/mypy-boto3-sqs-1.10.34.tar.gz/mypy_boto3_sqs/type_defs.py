"Main interface for sqs service type defs"
from __future__ import annotations

import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientChangeMessageVisibilityBatchEntriesTypeDef = TypedDict(
    "ClientChangeMessageVisibilityBatchEntriesTypeDef",
    {"Id": str, "ReceiptHandle": str, "VisibilityTimeout": int},
    total=False,
)

ClientChangeMessageVisibilityBatchResponseFailedTypeDef = TypedDict(
    "ClientChangeMessageVisibilityBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)

ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef = TypedDict(
    "ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef", {"Id": str}, total=False
)

ClientChangeMessageVisibilityBatchResponseTypeDef = TypedDict(
    "ClientChangeMessageVisibilityBatchResponseTypeDef",
    {
        "Successful": List[ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientChangeMessageVisibilityBatchResponseFailedTypeDef],
    },
    total=False,
)

ClientCreateQueueResponseTypeDef = TypedDict(
    "ClientCreateQueueResponseTypeDef", {"QueueUrl": str}, total=False
)

_RequiredClientDeleteMessageBatchEntriesTypeDef = TypedDict(
    "_RequiredClientDeleteMessageBatchEntriesTypeDef", {"Id": str}
)
_OptionalClientDeleteMessageBatchEntriesTypeDef = TypedDict(
    "_OptionalClientDeleteMessageBatchEntriesTypeDef", {"ReceiptHandle": str}, total=False
)


class ClientDeleteMessageBatchEntriesTypeDef(
    _RequiredClientDeleteMessageBatchEntriesTypeDef, _OptionalClientDeleteMessageBatchEntriesTypeDef
):
    pass


ClientDeleteMessageBatchResponseFailedTypeDef = TypedDict(
    "ClientDeleteMessageBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)

ClientDeleteMessageBatchResponseSuccessfulTypeDef = TypedDict(
    "ClientDeleteMessageBatchResponseSuccessfulTypeDef", {"Id": str}, total=False
)

ClientDeleteMessageBatchResponseTypeDef = TypedDict(
    "ClientDeleteMessageBatchResponseTypeDef",
    {
        "Successful": List[ClientDeleteMessageBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientDeleteMessageBatchResponseFailedTypeDef],
    },
    total=False,
)

ClientGetQueueAttributesResponseTypeDef = TypedDict(
    "ClientGetQueueAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

ClientGetQueueUrlResponseTypeDef = TypedDict(
    "ClientGetQueueUrlResponseTypeDef", {"QueueUrl": str}, total=False
)

ClientListDeadLetterSourceQueuesResponseTypeDef = TypedDict(
    "ClientListDeadLetterSourceQueuesResponseTypeDef", {"queueUrls": List[str]}, total=False
)

ClientListQueueTagsResponseTypeDef = TypedDict(
    "ClientListQueueTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientListQueuesResponseTypeDef = TypedDict(
    "ClientListQueuesResponseTypeDef", {"QueueUrls": List[str]}, total=False
)

ClientReceiveMessageResponseMessagesMessageAttributesTypeDef = TypedDict(
    "ClientReceiveMessageResponseMessagesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

ClientReceiveMessageResponseMessagesTypeDef = TypedDict(
    "ClientReceiveMessageResponseMessagesTypeDef",
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

ClientReceiveMessageResponseTypeDef = TypedDict(
    "ClientReceiveMessageResponseTypeDef",
    {"Messages": List[ClientReceiveMessageResponseMessagesTypeDef]},
    total=False,
)

ClientSendMessageBatchEntriesMessageAttributesTypeDef = TypedDict(
    "ClientSendMessageBatchEntriesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef = TypedDict(
    "ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

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
    pass


ClientSendMessageBatchResponseFailedTypeDef = TypedDict(
    "ClientSendMessageBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)

ClientSendMessageBatchResponseSuccessfulTypeDef = TypedDict(
    "ClientSendMessageBatchResponseSuccessfulTypeDef",
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

ClientSendMessageBatchResponseTypeDef = TypedDict(
    "ClientSendMessageBatchResponseTypeDef",
    {
        "Successful": List[ClientSendMessageBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientSendMessageBatchResponseFailedTypeDef],
    },
    total=False,
)

ClientSendMessageMessageAttributesTypeDef = TypedDict(
    "ClientSendMessageMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

ClientSendMessageMessageSystemAttributesTypeDef = TypedDict(
    "ClientSendMessageMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

ClientSendMessageResponseTypeDef = TypedDict(
    "ClientSendMessageResponseTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
    },
    total=False,
)

QueueChangeMessageVisibilityBatchEntriesTypeDef = TypedDict(
    "QueueChangeMessageVisibilityBatchEntriesTypeDef",
    {"Id": str, "ReceiptHandle": str, "VisibilityTimeout": int},
    total=False,
)

QueueChangeMessageVisibilityBatchResponseFailedTypeDef = TypedDict(
    "QueueChangeMessageVisibilityBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)

QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef = TypedDict(
    "QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef", {"Id": str}, total=False
)

QueueChangeMessageVisibilityBatchResponseTypeDef = TypedDict(
    "QueueChangeMessageVisibilityBatchResponseTypeDef",
    {
        "Successful": List[QueueChangeMessageVisibilityBatchResponseSuccessfulTypeDef],
        "Failed": List[QueueChangeMessageVisibilityBatchResponseFailedTypeDef],
    },
    total=False,
)

_RequiredQueueDeleteMessagesEntriesTypeDef = TypedDict(
    "_RequiredQueueDeleteMessagesEntriesTypeDef", {"Id": str}
)
_OptionalQueueDeleteMessagesEntriesTypeDef = TypedDict(
    "_OptionalQueueDeleteMessagesEntriesTypeDef", {"ReceiptHandle": str}, total=False
)


class QueueDeleteMessagesEntriesTypeDef(
    _RequiredQueueDeleteMessagesEntriesTypeDef, _OptionalQueueDeleteMessagesEntriesTypeDef
):
    pass


QueueDeleteMessagesResponseFailedTypeDef = TypedDict(
    "QueueDeleteMessagesResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)

QueueDeleteMessagesResponseSuccessfulTypeDef = TypedDict(
    "QueueDeleteMessagesResponseSuccessfulTypeDef", {"Id": str}, total=False
)

QueueDeleteMessagesResponseTypeDef = TypedDict(
    "QueueDeleteMessagesResponseTypeDef",
    {
        "Successful": List[QueueDeleteMessagesResponseSuccessfulTypeDef],
        "Failed": List[QueueDeleteMessagesResponseFailedTypeDef],
    },
    total=False,
)

QueueSendMessageMessageAttributesTypeDef = TypedDict(
    "QueueSendMessageMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

QueueSendMessageMessageSystemAttributesTypeDef = TypedDict(
    "QueueSendMessageMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

QueueSendMessageResponseTypeDef = TypedDict(
    "QueueSendMessageResponseTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
    },
    total=False,
)

QueueSendMessagesEntriesMessageAttributesTypeDef = TypedDict(
    "QueueSendMessagesEntriesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

QueueSendMessagesEntriesMessageSystemAttributesTypeDef = TypedDict(
    "QueueSendMessagesEntriesMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

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
    pass


QueueSendMessagesResponseFailedTypeDef = TypedDict(
    "QueueSendMessagesResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)

QueueSendMessagesResponseSuccessfulTypeDef = TypedDict(
    "QueueSendMessagesResponseSuccessfulTypeDef",
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

QueueSendMessagesResponseTypeDef = TypedDict(
    "QueueSendMessagesResponseTypeDef",
    {
        "Successful": List[QueueSendMessagesResponseSuccessfulTypeDef],
        "Failed": List[QueueSendMessagesResponseFailedTypeDef],
    },
    total=False,
)
