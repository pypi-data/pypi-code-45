"Main interface for kinesis service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.eventstream import EventStream
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeLimitsResponseTypeDef",
    "ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef",
    "ClientDescribeStreamConsumerResponseTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionTypeDef",
    "ClientDescribeStreamResponseTypeDef",
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef",
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef",
    "ClientDescribeStreamSummaryResponseTypeDef",
    "ClientDisableEnhancedMonitoringResponseTypeDef",
    "ClientEnableEnhancedMonitoringResponseTypeDef",
    "ClientGetRecordsResponseRecordsTypeDef",
    "ClientGetRecordsResponseTypeDef",
    "ClientGetShardIteratorResponseTypeDef",
    "ClientListShardsResponseShardsHashKeyRangeTypeDef",
    "ClientListShardsResponseShardsSequenceNumberRangeTypeDef",
    "ClientListShardsResponseShardsTypeDef",
    "ClientListShardsResponseTypeDef",
    "ClientListStreamConsumersResponseConsumersTypeDef",
    "ClientListStreamConsumersResponseTypeDef",
    "ClientListStreamsResponseTypeDef",
    "ClientListTagsForStreamResponseTagsTypeDef",
    "ClientListTagsForStreamResponseTypeDef",
    "ClientPutRecordResponseTypeDef",
    "ClientPutRecordsRecordsTypeDef",
    "ClientPutRecordsResponseRecordsTypeDef",
    "ClientPutRecordsResponseTypeDef",
    "ClientRegisterStreamConsumerResponseConsumerTypeDef",
    "ClientRegisterStreamConsumerResponseTypeDef",
    "ClientSubscribeToShardResponseTypeDef",
    "ClientSubscribeToShardStartingPositionTypeDef",
    "ClientUpdateShardCountResponseTypeDef",
    "DescribeStreamPaginatePaginationConfigTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionTypeDef",
    "DescribeStreamPaginateResponseTypeDef",
    "ListShardsPaginatePaginationConfigTypeDef",
    "ListShardsPaginateResponseShardsHashKeyRangeTypeDef",
    "ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef",
    "ListShardsPaginateResponseShardsTypeDef",
    "ListShardsPaginateResponseTypeDef",
    "ListStreamConsumersPaginatePaginationConfigTypeDef",
    "ListStreamConsumersPaginateResponseConsumersTypeDef",
    "ListStreamConsumersPaginateResponseTypeDef",
    "ListStreamsPaginatePaginationConfigTypeDef",
    "ListStreamsPaginateResponseTypeDef",
    "StreamExistsWaitWaiterConfigTypeDef",
    "StreamNotExistsWaitWaiterConfigTypeDef",
)


_ClientDescribeLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeLimitsResponseTypeDef", {"ShardLimit": int, "OpenShardCount": int}, total=False
)


class ClientDescribeLimitsResponseTypeDef(_ClientDescribeLimitsResponseTypeDef):
    """
    - *(dict) --*

      - **ShardLimit** *(integer) --*

        The maximum number of shards.
    """


_ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef = TypedDict(
    "_ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
    total=False,
)


class ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef(
    _ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef
):
    """
    - **ConsumerDescription** *(dict) --*

      An object that represents the details of the consumer.
      - **ConsumerName** *(string) --*

        The name of the consumer is something you choose when you register the consumer.
    """


_ClientDescribeStreamConsumerResponseTypeDef = TypedDict(
    "_ClientDescribeStreamConsumerResponseTypeDef",
    {"ConsumerDescription": ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef},
    total=False,
)


class ClientDescribeStreamConsumerResponseTypeDef(_ClientDescribeStreamConsumerResponseTypeDef):
    """
    - *(dict) --*

      - **ConsumerDescription** *(dict) --*

        An object that represents the details of the consumer.
        - **ConsumerName** *(string) --*

          The name of the consumer is something you choose when you register the consumer.
    """


_ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef",
    {
        "ShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ]
    },
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef
):
    pass


_ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef
):
    pass


_ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef
):
    pass


_ClientDescribeStreamResponseStreamDescriptionShardsTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionShardsTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionShardsTypeDef
):
    pass


_ClientDescribeStreamResponseStreamDescriptionTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": Literal["CREATING", "DELETING", "ACTIVE", "UPDATING"],
        "Shards": List[ClientDescribeStreamResponseStreamDescriptionShardsTypeDef],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[
            ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef
        ],
        "EncryptionType": Literal["NONE", "KMS"],
        "KeyId": str,
    },
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionTypeDef
):
    """
    - **StreamDescription** *(dict) --*

      The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard
      objects that comprise the stream, and whether there are more shards available.
      - **StreamName** *(string) --*

        The name of the stream being described.
    """


_ClientDescribeStreamResponseTypeDef = TypedDict(
    "_ClientDescribeStreamResponseTypeDef",
    {"StreamDescription": ClientDescribeStreamResponseStreamDescriptionTypeDef},
    total=False,
)


class ClientDescribeStreamResponseTypeDef(_ClientDescribeStreamResponseTypeDef):
    """
    - *(dict) --*

      Represents the output for ``DescribeStream`` .
      - **StreamDescription** *(dict) --*

        The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard
        objects that comprise the stream, and whether there are more shards available.
        - **StreamName** *(string) --*

          The name of the stream being described.
    """


_ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef = TypedDict(
    "_ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef",
    {
        "ShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ]
    },
    total=False,
)


class ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef(
    _ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef
):
    pass


_ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef = TypedDict(
    "_ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": Literal["CREATING", "DELETING", "ACTIVE", "UPDATING"],
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[
            ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef
        ],
        "EncryptionType": Literal["NONE", "KMS"],
        "KeyId": str,
        "OpenShardCount": int,
        "ConsumerCount": int,
    },
    total=False,
)


class ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef(
    _ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef
):
    """
    - **StreamDescriptionSummary** *(dict) --*

      A  StreamDescriptionSummary containing information about the stream.
      - **StreamName** *(string) --*

        The name of the stream being described.
    """


_ClientDescribeStreamSummaryResponseTypeDef = TypedDict(
    "_ClientDescribeStreamSummaryResponseTypeDef",
    {
        "StreamDescriptionSummary": ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef
    },
    total=False,
)


class ClientDescribeStreamSummaryResponseTypeDef(_ClientDescribeStreamSummaryResponseTypeDef):
    """
    - *(dict) --*

      - **StreamDescriptionSummary** *(dict) --*

        A  StreamDescriptionSummary containing information about the stream.
        - **StreamName** *(string) --*

          The name of the stream being described.
    """


_ClientDisableEnhancedMonitoringResponseTypeDef = TypedDict(
    "_ClientDisableEnhancedMonitoringResponseTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
        "DesiredShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
    },
    total=False,
)


class ClientDisableEnhancedMonitoringResponseTypeDef(
    _ClientDisableEnhancedMonitoringResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output for  EnableEnhancedMonitoring and  DisableEnhancedMonitoring .
      - **StreamName** *(string) --*

        The name of the Kinesis data stream.
    """


_ClientEnableEnhancedMonitoringResponseTypeDef = TypedDict(
    "_ClientEnableEnhancedMonitoringResponseTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
        "DesiredShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
    },
    total=False,
)


class ClientEnableEnhancedMonitoringResponseTypeDef(_ClientEnableEnhancedMonitoringResponseTypeDef):
    """
    - *(dict) --*

      Represents the output for  EnableEnhancedMonitoring and  DisableEnhancedMonitoring .
      - **StreamName** *(string) --*

        The name of the Kinesis data stream.
    """


_ClientGetRecordsResponseRecordsTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsTypeDef",
    {
        "SequenceNumber": str,
        "ApproximateArrivalTimestamp": datetime,
        "Data": bytes,
        "PartitionKey": str,
        "EncryptionType": Literal["NONE", "KMS"],
    },
    total=False,
)


class ClientGetRecordsResponseRecordsTypeDef(_ClientGetRecordsResponseRecordsTypeDef):
    """
    - *(dict) --*

      The unit of data of the Kinesis data stream, which is composed of a sequence number, a
      partition key, and a data blob.
      - **SequenceNumber** *(string) --*

        The unique identifier of the record within its shard.
    """


_ClientGetRecordsResponseTypeDef = TypedDict(
    "_ClientGetRecordsResponseTypeDef",
    {
        "Records": List[ClientGetRecordsResponseRecordsTypeDef],
        "NextShardIterator": str,
        "MillisBehindLatest": int,
    },
    total=False,
)


class ClientGetRecordsResponseTypeDef(_ClientGetRecordsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output for  GetRecords .
      - **Records** *(list) --*

        The data records retrieved from the shard.
        - *(dict) --*

          The unit of data of the Kinesis data stream, which is composed of a sequence number, a
          partition key, and a data blob.
          - **SequenceNumber** *(string) --*

            The unique identifier of the record within its shard.
    """


_ClientGetShardIteratorResponseTypeDef = TypedDict(
    "_ClientGetShardIteratorResponseTypeDef", {"ShardIterator": str}, total=False
)


class ClientGetShardIteratorResponseTypeDef(_ClientGetShardIteratorResponseTypeDef):
    """
    - *(dict) --*

      Represents the output for ``GetShardIterator`` .
      - **ShardIterator** *(string) --*

        The position in the shard from which to start reading data records sequentially. A shard
        iterator specifies this position using the sequence number of a data record in a shard.
    """


_ClientListShardsResponseShardsHashKeyRangeTypeDef = TypedDict(
    "_ClientListShardsResponseShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)


class ClientListShardsResponseShardsHashKeyRangeTypeDef(
    _ClientListShardsResponseShardsHashKeyRangeTypeDef
):
    pass


_ClientListShardsResponseShardsSequenceNumberRangeTypeDef = TypedDict(
    "_ClientListShardsResponseShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)


class ClientListShardsResponseShardsSequenceNumberRangeTypeDef(
    _ClientListShardsResponseShardsSequenceNumberRangeTypeDef
):
    pass


_ClientListShardsResponseShardsTypeDef = TypedDict(
    "_ClientListShardsResponseShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ClientListShardsResponseShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ClientListShardsResponseShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)


class ClientListShardsResponseShardsTypeDef(_ClientListShardsResponseShardsTypeDef):
    """
    - *(dict) --*

      A uniquely identified group of data records in a Kinesis data stream.
      - **ShardId** *(string) --*

        The unique identifier of the shard within the stream.
    """


_ClientListShardsResponseTypeDef = TypedDict(
    "_ClientListShardsResponseTypeDef",
    {"Shards": List[ClientListShardsResponseShardsTypeDef], "NextToken": str},
    total=False,
)


class ClientListShardsResponseTypeDef(_ClientListShardsResponseTypeDef):
    """
    - *(dict) --*

      - **Shards** *(list) --*

        An array of JSON objects. Each object represents one shard and specifies the IDs of the
        shard, the shard's parent, and the shard that's adjacent to the shard's parent. Each object
        also contains the starting and ending hash keys and the starting and ending sequence numbers
        for the shard.
        - *(dict) --*

          A uniquely identified group of data records in a Kinesis data stream.
          - **ShardId** *(string) --*

            The unique identifier of the shard within the stream.
    """


_ClientListStreamConsumersResponseConsumersTypeDef = TypedDict(
    "_ClientListStreamConsumersResponseConsumersTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)


class ClientListStreamConsumersResponseConsumersTypeDef(
    _ClientListStreamConsumersResponseConsumersTypeDef
):
    """
    - *(dict) --*

      An object that represents the details of the consumer you registered.
      - **ConsumerName** *(string) --*

        The name of the consumer is something you choose when you register the consumer.
    """


_ClientListStreamConsumersResponseTypeDef = TypedDict(
    "_ClientListStreamConsumersResponseTypeDef",
    {"Consumers": List[ClientListStreamConsumersResponseConsumersTypeDef], "NextToken": str},
    total=False,
)


class ClientListStreamConsumersResponseTypeDef(_ClientListStreamConsumersResponseTypeDef):
    """
    - *(dict) --*

      - **Consumers** *(list) --*

        An array of JSON objects. Each object represents one registered consumer.
        - *(dict) --*

          An object that represents the details of the consumer you registered.
          - **ConsumerName** *(string) --*

            The name of the consumer is something you choose when you register the consumer.
    """


_ClientListStreamsResponseTypeDef = TypedDict(
    "_ClientListStreamsResponseTypeDef",
    {"StreamNames": List[str], "HasMoreStreams": bool},
    total=False,
)


class ClientListStreamsResponseTypeDef(_ClientListStreamsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output for ``ListStreams`` .
      - **StreamNames** *(list) --*

        The names of the streams that are associated with the AWS account making the ``ListStreams``
        request.
        - *(string) --*
    """


_ClientListTagsForStreamResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForStreamResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForStreamResponseTagsTypeDef(_ClientListTagsForStreamResponseTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to the stream, consisting of a key-value pair.
      - **Key** *(string) --*

        A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode
        letters, digits, white space, _ . / = + - % @
    """


_ClientListTagsForStreamResponseTypeDef = TypedDict(
    "_ClientListTagsForStreamResponseTypeDef",
    {"Tags": List[ClientListTagsForStreamResponseTagsTypeDef], "HasMoreTags": bool},
    total=False,
)


class ClientListTagsForStreamResponseTypeDef(_ClientListTagsForStreamResponseTypeDef):
    """
    - *(dict) --*

      Represents the output for ``ListTagsForStream`` .
      - **Tags** *(list) --*

        A list of tags associated with ``StreamName`` , starting with the first tag after
        ``ExclusiveStartTagKey`` and up to the specified ``Limit`` .
        - *(dict) --*

          Metadata assigned to the stream, consisting of a key-value pair.
          - **Key** *(string) --*

            A unique identifier for the tag. Maximum length: 128 characters. Valid characters:
            Unicode letters, digits, white space, _ . / = + - % @
    """


_ClientPutRecordResponseTypeDef = TypedDict(
    "_ClientPutRecordResponseTypeDef",
    {"ShardId": str, "SequenceNumber": str, "EncryptionType": Literal["NONE", "KMS"]},
    total=False,
)


class ClientPutRecordResponseTypeDef(_ClientPutRecordResponseTypeDef):
    """
    - *(dict) --*

      Represents the output for ``PutRecord`` .
      - **ShardId** *(string) --*

        The shard ID of the shard where the data record was placed.
    """


_RequiredClientPutRecordsRecordsTypeDef = TypedDict(
    "_RequiredClientPutRecordsRecordsTypeDef", {"Data": bytes}
)
_OptionalClientPutRecordsRecordsTypeDef = TypedDict(
    "_OptionalClientPutRecordsRecordsTypeDef",
    {"ExplicitHashKey": str, "PartitionKey": str},
    total=False,
)


class ClientPutRecordsRecordsTypeDef(
    _RequiredClientPutRecordsRecordsTypeDef, _OptionalClientPutRecordsRecordsTypeDef
):
    """
    - *(dict) --*

      Represents the output for ``PutRecords`` .
      - **Data** *(bytes) --***[REQUIRED]**

        The data blob to put into the record, which is base64-encoded when the blob is serialized.
        When the data blob (the payload before base64-encoding) is added to the partition key size,
        the total size must not exceed the maximum record size (1 MB).
    """


_ClientPutRecordsResponseRecordsTypeDef = TypedDict(
    "_ClientPutRecordsResponseRecordsTypeDef",
    {"SequenceNumber": str, "ShardId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientPutRecordsResponseRecordsTypeDef(_ClientPutRecordsResponseRecordsTypeDef):
    pass


_ClientPutRecordsResponseTypeDef = TypedDict(
    "_ClientPutRecordsResponseTypeDef",
    {
        "FailedRecordCount": int,
        "Records": List[ClientPutRecordsResponseRecordsTypeDef],
        "EncryptionType": Literal["NONE", "KMS"],
    },
    total=False,
)


class ClientPutRecordsResponseTypeDef(_ClientPutRecordsResponseTypeDef):
    """
    - *(dict) --*

      ``PutRecords`` results.
      - **FailedRecordCount** *(integer) --*

        The number of unsuccessfully processed records in a ``PutRecords`` request.
    """


_ClientRegisterStreamConsumerResponseConsumerTypeDef = TypedDict(
    "_ClientRegisterStreamConsumerResponseConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)


class ClientRegisterStreamConsumerResponseConsumerTypeDef(
    _ClientRegisterStreamConsumerResponseConsumerTypeDef
):
    """
    - **Consumer** *(dict) --*

      An object that represents the details of the consumer you registered. When you register a
      consumer, it gets an ARN that is generated by Kinesis Data Streams.
      - **ConsumerName** *(string) --*

        The name of the consumer is something you choose when you register the consumer.
    """


_ClientRegisterStreamConsumerResponseTypeDef = TypedDict(
    "_ClientRegisterStreamConsumerResponseTypeDef",
    {"Consumer": ClientRegisterStreamConsumerResponseConsumerTypeDef},
    total=False,
)


class ClientRegisterStreamConsumerResponseTypeDef(_ClientRegisterStreamConsumerResponseTypeDef):
    """
    - *(dict) --*

      - **Consumer** *(dict) --*

        An object that represents the details of the consumer you registered. When you register a
        consumer, it gets an ARN that is generated by Kinesis Data Streams.
        - **ConsumerName** *(string) --*

          The name of the consumer is something you choose when you register the consumer.
    """


_ClientSubscribeToShardResponseTypeDef = TypedDict(
    "_ClientSubscribeToShardResponseTypeDef", {"EventStream": EventStream}, total=False
)


class ClientSubscribeToShardResponseTypeDef(_ClientSubscribeToShardResponseTypeDef):
    """
    - *(dict) --*

      - **EventStream** (:class:`.EventStream`) --

        The event stream that your consumer can use to read records from the shard.
        - **SubscribeToShardEvent** *(dict) --*

          After you call  SubscribeToShard , Kinesis Data Streams sends events of this type to your
          consumer.
          - **Records** *(list) --*

            - *(dict) --*

              The unit of data of the Kinesis data stream, which is composed of a sequence number, a
              partition key, and a data blob.
              - **SequenceNumber** *(string) --*

                The unique identifier of the record within its shard.
    """


_RequiredClientSubscribeToShardStartingPositionTypeDef = TypedDict(
    "_RequiredClientSubscribeToShardStartingPositionTypeDef",
    {
        "Type": Literal[
            "AT_SEQUENCE_NUMBER", "AFTER_SEQUENCE_NUMBER", "TRIM_HORIZON", "LATEST", "AT_TIMESTAMP"
        ]
    },
)
_OptionalClientSubscribeToShardStartingPositionTypeDef = TypedDict(
    "_OptionalClientSubscribeToShardStartingPositionTypeDef",
    {"SequenceNumber": str, "Timestamp": datetime},
    total=False,
)


class ClientSubscribeToShardStartingPositionTypeDef(
    _RequiredClientSubscribeToShardStartingPositionTypeDef,
    _OptionalClientSubscribeToShardStartingPositionTypeDef,
):
    """
    - **Type** *(string) --***[REQUIRED]**
    - **SequenceNumber** *(string) --*
    - **Timestamp** *(datetime) --*
    """


_ClientUpdateShardCountResponseTypeDef = TypedDict(
    "_ClientUpdateShardCountResponseTypeDef",
    {"StreamName": str, "CurrentShardCount": int, "TargetShardCount": int},
    total=False,
)


class ClientUpdateShardCountResponseTypeDef(_ClientUpdateShardCountResponseTypeDef):
    """
    - *(dict) --*

      - **StreamName** *(string) --*

        The name of the stream.
    """


_DescribeStreamPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeStreamPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeStreamPaginatePaginationConfigTypeDef(_DescribeStreamPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef",
    {
        "ShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ]
    },
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef
):
    pass


_DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef
):
    pass


_DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef
):
    pass


_DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef
):
    pass


_DescribeStreamPaginateResponseStreamDescriptionTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": Literal["CREATING", "DELETING", "ACTIVE", "UPDATING"],
        "Shards": List[DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[
            DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef
        ],
        "EncryptionType": Literal["NONE", "KMS"],
        "KeyId": str,
    },
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionTypeDef
):
    """
    - **StreamDescription** *(dict) --*

      The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard
      objects that comprise the stream, and whether there are more shards available.
      - **StreamName** *(string) --*

        The name of the stream being described.
    """


_DescribeStreamPaginateResponseTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseTypeDef",
    {"StreamDescription": DescribeStreamPaginateResponseStreamDescriptionTypeDef, "NextToken": str},
    total=False,
)


class DescribeStreamPaginateResponseTypeDef(_DescribeStreamPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output for ``DescribeStream`` .
      - **StreamDescription** *(dict) --*

        The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard
        objects that comprise the stream, and whether there are more shards available.
        - **StreamName** *(string) --*

          The name of the stream being described.
    """


_ListShardsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListShardsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListShardsPaginatePaginationConfigTypeDef(_ListShardsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListShardsPaginateResponseShardsHashKeyRangeTypeDef = TypedDict(
    "_ListShardsPaginateResponseShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)


class ListShardsPaginateResponseShardsHashKeyRangeTypeDef(
    _ListShardsPaginateResponseShardsHashKeyRangeTypeDef
):
    pass


_ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef = TypedDict(
    "_ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)


class ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef(
    _ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef
):
    pass


_ListShardsPaginateResponseShardsTypeDef = TypedDict(
    "_ListShardsPaginateResponseShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ListShardsPaginateResponseShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)


class ListShardsPaginateResponseShardsTypeDef(_ListShardsPaginateResponseShardsTypeDef):
    """
    - *(dict) --*

      A uniquely identified group of data records in a Kinesis data stream.
      - **ShardId** *(string) --*

        The unique identifier of the shard within the stream.
    """


_ListShardsPaginateResponseTypeDef = TypedDict(
    "_ListShardsPaginateResponseTypeDef",
    {"Shards": List[ListShardsPaginateResponseShardsTypeDef]},
    total=False,
)


class ListShardsPaginateResponseTypeDef(_ListShardsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Shards** *(list) --*

        An array of JSON objects. Each object represents one shard and specifies the IDs of the
        shard, the shard's parent, and the shard that's adjacent to the shard's parent. Each object
        also contains the starting and ending hash keys and the starting and ending sequence numbers
        for the shard.
        - *(dict) --*

          A uniquely identified group of data records in a Kinesis data stream.
          - **ShardId** *(string) --*

            The unique identifier of the shard within the stream.
    """


_ListStreamConsumersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamConsumersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamConsumersPaginatePaginationConfigTypeDef(
    _ListStreamConsumersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStreamConsumersPaginateResponseConsumersTypeDef = TypedDict(
    "_ListStreamConsumersPaginateResponseConsumersTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)


class ListStreamConsumersPaginateResponseConsumersTypeDef(
    _ListStreamConsumersPaginateResponseConsumersTypeDef
):
    """
    - *(dict) --*

      An object that represents the details of the consumer you registered.
      - **ConsumerName** *(string) --*

        The name of the consumer is something you choose when you register the consumer.
    """


_ListStreamConsumersPaginateResponseTypeDef = TypedDict(
    "_ListStreamConsumersPaginateResponseTypeDef",
    {"Consumers": List[ListStreamConsumersPaginateResponseConsumersTypeDef]},
    total=False,
)


class ListStreamConsumersPaginateResponseTypeDef(_ListStreamConsumersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Consumers** *(list) --*

        An array of JSON objects. Each object represents one registered consumer.
        - *(dict) --*

          An object that represents the details of the consumer you registered.
          - **ConsumerName** *(string) --*

            The name of the consumer is something you choose when you register the consumer.
    """


_ListStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamsPaginatePaginationConfigTypeDef(_ListStreamsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStreamsPaginateResponseTypeDef = TypedDict(
    "_ListStreamsPaginateResponseTypeDef",
    {"StreamNames": List[str], "HasMoreStreams": bool, "NextToken": str},
    total=False,
)


class ListStreamsPaginateResponseTypeDef(_ListStreamsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output for ``ListStreams`` .
      - **StreamNames** *(list) --*

        The names of the streams that are associated with the AWS account making the ``ListStreams``
        request.
        - *(string) --*
    """


_StreamExistsWaitWaiterConfigTypeDef = TypedDict(
    "_StreamExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class StreamExistsWaitWaiterConfigTypeDef(_StreamExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 10
    """


_StreamNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "_StreamNotExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class StreamNotExistsWaitWaiterConfigTypeDef(_StreamNotExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 10
    """
