"Main interface for kinesis service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.eventstream import EventStream

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientDescribeLimitsResponseTypeDef = TypedDict(
    "ClientDescribeLimitsResponseTypeDef", {"ShardLimit": int, "OpenShardCount": int}, total=False
)

ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef = TypedDict(
    "ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
    total=False,
)

ClientDescribeStreamConsumerResponseTypeDef = TypedDict(
    "ClientDescribeStreamConsumerResponseTypeDef",
    {"ConsumerDescription": ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef},
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef",
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

ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionShardsTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionTypeDef",
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

ClientDescribeStreamResponseTypeDef = TypedDict(
    "ClientDescribeStreamResponseTypeDef",
    {"StreamDescription": ClientDescribeStreamResponseStreamDescriptionTypeDef},
    total=False,
)

ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef = TypedDict(
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef",
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

ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef = TypedDict(
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef",
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

ClientDescribeStreamSummaryResponseTypeDef = TypedDict(
    "ClientDescribeStreamSummaryResponseTypeDef",
    {
        "StreamDescriptionSummary": ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef
    },
    total=False,
)

ClientDisableEnhancedMonitoringResponseTypeDef = TypedDict(
    "ClientDisableEnhancedMonitoringResponseTypeDef",
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

ClientEnableEnhancedMonitoringResponseTypeDef = TypedDict(
    "ClientEnableEnhancedMonitoringResponseTypeDef",
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

ClientGetRecordsResponseRecordsTypeDef = TypedDict(
    "ClientGetRecordsResponseRecordsTypeDef",
    {
        "SequenceNumber": str,
        "ApproximateArrivalTimestamp": datetime,
        "Data": bytes,
        "PartitionKey": str,
        "EncryptionType": Literal["NONE", "KMS"],
    },
    total=False,
)

ClientGetRecordsResponseTypeDef = TypedDict(
    "ClientGetRecordsResponseTypeDef",
    {
        "Records": List[ClientGetRecordsResponseRecordsTypeDef],
        "NextShardIterator": str,
        "MillisBehindLatest": int,
    },
    total=False,
)

ClientGetShardIteratorResponseTypeDef = TypedDict(
    "ClientGetShardIteratorResponseTypeDef", {"ShardIterator": str}, total=False
)

ClientListShardsResponseShardsHashKeyRangeTypeDef = TypedDict(
    "ClientListShardsResponseShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)

ClientListShardsResponseShardsSequenceNumberRangeTypeDef = TypedDict(
    "ClientListShardsResponseShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)

ClientListShardsResponseShardsTypeDef = TypedDict(
    "ClientListShardsResponseShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ClientListShardsResponseShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ClientListShardsResponseShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)

ClientListShardsResponseTypeDef = TypedDict(
    "ClientListShardsResponseTypeDef",
    {"Shards": List[ClientListShardsResponseShardsTypeDef], "NextToken": str},
    total=False,
)

ClientListStreamConsumersResponseConsumersTypeDef = TypedDict(
    "ClientListStreamConsumersResponseConsumersTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)

ClientListStreamConsumersResponseTypeDef = TypedDict(
    "ClientListStreamConsumersResponseTypeDef",
    {"Consumers": List[ClientListStreamConsumersResponseConsumersTypeDef], "NextToken": str},
    total=False,
)

ClientListStreamsResponseTypeDef = TypedDict(
    "ClientListStreamsResponseTypeDef",
    {"StreamNames": List[str], "HasMoreStreams": bool},
    total=False,
)

ClientListTagsForStreamResponseTagsTypeDef = TypedDict(
    "ClientListTagsForStreamResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForStreamResponseTypeDef = TypedDict(
    "ClientListTagsForStreamResponseTypeDef",
    {"Tags": List[ClientListTagsForStreamResponseTagsTypeDef], "HasMoreTags": bool},
    total=False,
)

ClientPutRecordResponseTypeDef = TypedDict(
    "ClientPutRecordResponseTypeDef",
    {"ShardId": str, "SequenceNumber": str, "EncryptionType": Literal["NONE", "KMS"]},
    total=False,
)

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
    pass


ClientPutRecordsResponseRecordsTypeDef = TypedDict(
    "ClientPutRecordsResponseRecordsTypeDef",
    {"SequenceNumber": str, "ShardId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientPutRecordsResponseTypeDef = TypedDict(
    "ClientPutRecordsResponseTypeDef",
    {
        "FailedRecordCount": int,
        "Records": List[ClientPutRecordsResponseRecordsTypeDef],
        "EncryptionType": Literal["NONE", "KMS"],
    },
    total=False,
)

ClientRegisterStreamConsumerResponseConsumerTypeDef = TypedDict(
    "ClientRegisterStreamConsumerResponseConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)

ClientRegisterStreamConsumerResponseTypeDef = TypedDict(
    "ClientRegisterStreamConsumerResponseTypeDef",
    {"Consumer": ClientRegisterStreamConsumerResponseConsumerTypeDef},
    total=False,
)

ClientSubscribeToShardResponseTypeDef = TypedDict(
    "ClientSubscribeToShardResponseTypeDef", {"EventStream": EventStream}, total=False
)

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
    pass


ClientUpdateShardCountResponseTypeDef = TypedDict(
    "ClientUpdateShardCountResponseTypeDef",
    {"StreamName": str, "CurrentShardCount": int, "TargetShardCount": int},
    total=False,
)

DescribeStreamPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeStreamPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef = TypedDict(
    "DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef",
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

DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef = TypedDict(
    "DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)

DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef = TypedDict(
    "DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)

DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef = TypedDict(
    "DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)

DescribeStreamPaginateResponseStreamDescriptionTypeDef = TypedDict(
    "DescribeStreamPaginateResponseStreamDescriptionTypeDef",
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

DescribeStreamPaginateResponseTypeDef = TypedDict(
    "DescribeStreamPaginateResponseTypeDef",
    {"StreamDescription": DescribeStreamPaginateResponseStreamDescriptionTypeDef, "NextToken": str},
    total=False,
)

ListShardsPaginatePaginationConfigTypeDef = TypedDict(
    "ListShardsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListShardsPaginateResponseShardsHashKeyRangeTypeDef = TypedDict(
    "ListShardsPaginateResponseShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)

ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef = TypedDict(
    "ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)

ListShardsPaginateResponseShardsTypeDef = TypedDict(
    "ListShardsPaginateResponseShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ListShardsPaginateResponseShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)

ListShardsPaginateResponseTypeDef = TypedDict(
    "ListShardsPaginateResponseTypeDef",
    {"Shards": List[ListShardsPaginateResponseShardsTypeDef]},
    total=False,
)

ListStreamConsumersPaginatePaginationConfigTypeDef = TypedDict(
    "ListStreamConsumersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListStreamConsumersPaginateResponseConsumersTypeDef = TypedDict(
    "ListStreamConsumersPaginateResponseConsumersTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)

ListStreamConsumersPaginateResponseTypeDef = TypedDict(
    "ListStreamConsumersPaginateResponseTypeDef",
    {"Consumers": List[ListStreamConsumersPaginateResponseConsumersTypeDef]},
    total=False,
)

ListStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "ListStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListStreamsPaginateResponseTypeDef = TypedDict(
    "ListStreamsPaginateResponseTypeDef",
    {"StreamNames": List[str], "HasMoreStreams": bool, "NextToken": str},
    total=False,
)

StreamExistsWaitWaiterConfigTypeDef = TypedDict(
    "StreamExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

StreamNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "StreamNotExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
