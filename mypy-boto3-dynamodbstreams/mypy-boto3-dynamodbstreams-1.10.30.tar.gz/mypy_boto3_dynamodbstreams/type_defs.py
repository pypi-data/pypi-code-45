"Main interface for dynamodbstreams service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionTypeDef",
    "ClientDescribeStreamResponseTypeDef",
    "ClientGetRecordsResponseRecordsdynamodbKeysTypeDef",
    "ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef",
    "ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef",
    "ClientGetRecordsResponseRecordsdynamodbTypeDef",
    "ClientGetRecordsResponseRecordsuserIdentityTypeDef",
    "ClientGetRecordsResponseRecordsTypeDef",
    "ClientGetRecordsResponseTypeDef",
    "ClientGetShardIteratorResponseTypeDef",
    "ClientListStreamsResponseStreamsTypeDef",
    "ClientListStreamsResponseTypeDef",
)


_ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef
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
        "SequenceNumberRange": ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
        "ParentShardId": str,
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
        "StreamArn": str,
        "StreamLabel": str,
        "StreamStatus": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"],
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
        "CreationRequestDateTime": datetime,
        "TableName": str,
        "KeySchema": List[ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef],
        "Shards": List[ClientDescribeStreamResponseStreamDescriptionShardsTypeDef],
        "LastEvaluatedShardId": str,
    },
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionTypeDef
):
    """
    - **StreamDescription** *(dict) --*

      A complete description of the stream, including its creation date and time, the DynamoDB table
      associated with the stream, the shard IDs within the stream, and the beginning and ending
      sequence numbers of stream records within the shards.
      - **StreamArn** *(string) --*

        The Amazon Resource Name (ARN) for the stream.
    """


_ClientDescribeStreamResponseTypeDef = TypedDict(
    "_ClientDescribeStreamResponseTypeDef",
    {"StreamDescription": ClientDescribeStreamResponseStreamDescriptionTypeDef},
    total=False,
)


class ClientDescribeStreamResponseTypeDef(_ClientDescribeStreamResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``DescribeStream`` operation.
      - **StreamDescription** *(dict) --*

        A complete description of the stream, including its creation date and time, the DynamoDB
        table associated with the stream, the shard IDs within the stream, and the beginning and
        ending sequence numbers of stream records within the shards.
        - **StreamArn** *(string) --*

          The Amazon Resource Name (ARN) for the stream.
    """


_ClientGetRecordsResponseRecordsdynamodbKeysTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsdynamodbKeysTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Any],
        "L": List[Any],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsdynamodbKeysTypeDef(
    _ClientGetRecordsResponseRecordsdynamodbKeysTypeDef
):
    pass


_ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Any],
        "L": List[Any],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef(
    _ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef
):
    pass


_ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Any],
        "L": List[Any],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef(
    _ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef
):
    pass


_ClientGetRecordsResponseRecordsdynamodbTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsdynamodbTypeDef",
    {
        "ApproximateCreationDateTime": datetime,
        "Keys": Dict[str, ClientGetRecordsResponseRecordsdynamodbKeysTypeDef],
        "NewImage": Dict[str, ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef],
        "OldImage": Dict[str, ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef],
        "SequenceNumber": str,
        "SizeBytes": int,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)


class ClientGetRecordsResponseRecordsdynamodbTypeDef(
    _ClientGetRecordsResponseRecordsdynamodbTypeDef
):
    pass


_ClientGetRecordsResponseRecordsuserIdentityTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsuserIdentityTypeDef",
    {"PrincipalId": str, "Type": str},
    total=False,
)


class ClientGetRecordsResponseRecordsuserIdentityTypeDef(
    _ClientGetRecordsResponseRecordsuserIdentityTypeDef
):
    pass


_ClientGetRecordsResponseRecordsTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsTypeDef",
    {
        "eventID": str,
        "eventName": Literal["INSERT", "MODIFY", "REMOVE"],
        "eventVersion": str,
        "eventSource": str,
        "awsRegion": str,
        "dynamodb": ClientGetRecordsResponseRecordsdynamodbTypeDef,
        "userIdentity": ClientGetRecordsResponseRecordsuserIdentityTypeDef,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsTypeDef(_ClientGetRecordsResponseRecordsTypeDef):
    """
    - *(dict) --*

      A description of a unique event within a stream.
      - **eventID** *(string) --*

        A globally unique identifier for the event that was recorded in this stream record.
    """


_ClientGetRecordsResponseTypeDef = TypedDict(
    "_ClientGetRecordsResponseTypeDef",
    {"Records": List[ClientGetRecordsResponseRecordsTypeDef], "NextShardIterator": str},
    total=False,
)


class ClientGetRecordsResponseTypeDef(_ClientGetRecordsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetRecords`` operation.
      - **Records** *(list) --*

        The stream records from the shard, which were retrieved using the shard iterator.
        - *(dict) --*

          A description of a unique event within a stream.
          - **eventID** *(string) --*

            A globally unique identifier for the event that was recorded in this stream record.
    """


_ClientGetShardIteratorResponseTypeDef = TypedDict(
    "_ClientGetShardIteratorResponseTypeDef", {"ShardIterator": str}, total=False
)


class ClientGetShardIteratorResponseTypeDef(_ClientGetShardIteratorResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetShardIterator`` operation.
      - **ShardIterator** *(string) --*

        The position in the shard from which to start reading stream records sequentially. A shard
        iterator specifies this position using the sequence number of a stream record in a shard.
    """


_ClientListStreamsResponseStreamsTypeDef = TypedDict(
    "_ClientListStreamsResponseStreamsTypeDef",
    {"StreamArn": str, "TableName": str, "StreamLabel": str},
    total=False,
)


class ClientListStreamsResponseStreamsTypeDef(_ClientListStreamsResponseStreamsTypeDef):
    """
    - *(dict) --*

      Represents all of the data describing a particular stream.
      - **StreamArn** *(string) --*

        The Amazon Resource Name (ARN) for the stream.
    """


_ClientListStreamsResponseTypeDef = TypedDict(
    "_ClientListStreamsResponseTypeDef",
    {"Streams": List[ClientListStreamsResponseStreamsTypeDef], "LastEvaluatedStreamArn": str},
    total=False,
)


class ClientListStreamsResponseTypeDef(_ClientListStreamsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``ListStreams`` operation.
      - **Streams** *(list) --*

        A list of stream descriptors associated with the current account and endpoint.
        - *(dict) --*

          Represents all of the data describing a particular stream.
          - **StreamArn** *(string) --*

            The Amazon Resource Name (ARN) for the stream.
    """
