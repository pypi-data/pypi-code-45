"Main interface for dynamodb service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientBatchGetItemRequestItemsKeysTypeDef = TypedDict(
    "ClientBatchGetItemRequestItemsKeysTypeDef",
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

ClientBatchGetItemRequestItemsTypeDef = TypedDict(
    "ClientBatchGetItemRequestItemsTypeDef",
    {
        "Keys": List[Dict[str, ClientBatchGetItemRequestItemsKeysTypeDef]],
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)

ClientBatchGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientBatchGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientBatchGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientBatchGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientBatchGetItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientBatchGetItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientBatchGetItemResponseConsumedCapacityTypeDef = TypedDict(
    "ClientBatchGetItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientBatchGetItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientBatchGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientBatchGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientBatchGetItemResponseResponsesTypeDef = TypedDict(
    "ClientBatchGetItemResponseResponsesTypeDef",
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

ClientBatchGetItemResponseUnprocessedKeysKeysTypeDef = TypedDict(
    "ClientBatchGetItemResponseUnprocessedKeysKeysTypeDef",
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

ClientBatchGetItemResponseUnprocessedKeysTypeDef = TypedDict(
    "ClientBatchGetItemResponseUnprocessedKeysTypeDef",
    {
        "Keys": List[Dict[str, ClientBatchGetItemResponseUnprocessedKeysKeysTypeDef]],
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)

ClientBatchGetItemResponseTypeDef = TypedDict(
    "ClientBatchGetItemResponseTypeDef",
    {
        "Responses": Dict[str, List[Dict[str, ClientBatchGetItemResponseResponsesTypeDef]]],
        "UnprocessedKeys": Dict[str, ClientBatchGetItemResponseUnprocessedKeysTypeDef],
        "ConsumedCapacity": List[ClientBatchGetItemResponseConsumedCapacityTypeDef],
    },
    total=False,
)

ClientBatchWriteItemRequestItemsDeleteRequestKeyTypeDef = TypedDict(
    "ClientBatchWriteItemRequestItemsDeleteRequestKeyTypeDef",
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

ClientBatchWriteItemRequestItemsDeleteRequestTypeDef = TypedDict(
    "ClientBatchWriteItemRequestItemsDeleteRequestTypeDef",
    {"Key": Dict[str, ClientBatchWriteItemRequestItemsDeleteRequestKeyTypeDef]},
    total=False,
)

ClientBatchWriteItemRequestItemsPutRequestItemTypeDef = TypedDict(
    "ClientBatchWriteItemRequestItemsPutRequestItemTypeDef",
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

ClientBatchWriteItemRequestItemsPutRequestTypeDef = TypedDict(
    "ClientBatchWriteItemRequestItemsPutRequestTypeDef",
    {"Item": Dict[str, ClientBatchWriteItemRequestItemsPutRequestItemTypeDef]},
    total=False,
)

ClientBatchWriteItemRequestItemsTypeDef = TypedDict(
    "ClientBatchWriteItemRequestItemsTypeDef",
    {
        "PutRequest": ClientBatchWriteItemRequestItemsPutRequestTypeDef,
        "DeleteRequest": ClientBatchWriteItemRequestItemsDeleteRequestTypeDef,
    },
    total=False,
)

ClientBatchWriteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientBatchWriteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientBatchWriteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientBatchWriteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientBatchWriteItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientBatchWriteItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientBatchWriteItemResponseConsumedCapacityTypeDef = TypedDict(
    "ClientBatchWriteItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientBatchWriteItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientBatchWriteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientBatchWriteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientBatchWriteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef = TypedDict(
    "ClientBatchWriteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef",
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

ClientBatchWriteItemResponseItemCollectionMetricsTypeDef = TypedDict(
    "ClientBatchWriteItemResponseItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str, ClientBatchWriteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ClientBatchWriteItemResponseUnprocessedItemsDeleteRequestKeyTypeDef = TypedDict(
    "ClientBatchWriteItemResponseUnprocessedItemsDeleteRequestKeyTypeDef",
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

ClientBatchWriteItemResponseUnprocessedItemsDeleteRequestTypeDef = TypedDict(
    "ClientBatchWriteItemResponseUnprocessedItemsDeleteRequestTypeDef",
    {"Key": Dict[str, ClientBatchWriteItemResponseUnprocessedItemsDeleteRequestKeyTypeDef]},
    total=False,
)

ClientBatchWriteItemResponseUnprocessedItemsPutRequestItemTypeDef = TypedDict(
    "ClientBatchWriteItemResponseUnprocessedItemsPutRequestItemTypeDef",
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

ClientBatchWriteItemResponseUnprocessedItemsPutRequestTypeDef = TypedDict(
    "ClientBatchWriteItemResponseUnprocessedItemsPutRequestTypeDef",
    {"Item": Dict[str, ClientBatchWriteItemResponseUnprocessedItemsPutRequestItemTypeDef]},
    total=False,
)

ClientBatchWriteItemResponseUnprocessedItemsTypeDef = TypedDict(
    "ClientBatchWriteItemResponseUnprocessedItemsTypeDef",
    {
        "PutRequest": ClientBatchWriteItemResponseUnprocessedItemsPutRequestTypeDef,
        "DeleteRequest": ClientBatchWriteItemResponseUnprocessedItemsDeleteRequestTypeDef,
    },
    total=False,
)

ClientBatchWriteItemResponseTypeDef = TypedDict(
    "ClientBatchWriteItemResponseTypeDef",
    {
        "UnprocessedItems": Dict[str, List[ClientBatchWriteItemResponseUnprocessedItemsTypeDef]],
        "ItemCollectionMetrics": Dict[
            str, List[ClientBatchWriteItemResponseItemCollectionMetricsTypeDef]
        ],
        "ConsumedCapacity": List[ClientBatchWriteItemResponseConsumedCapacityTypeDef],
    },
    total=False,
)

ClientCreateBackupResponseBackupDetailsTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupSizeBytes": int,
        "BackupStatus": Literal["CREATING", "DELETED", "AVAILABLE"],
        "BackupType": Literal["USER", "SYSTEM", "AWS_BACKUP"],
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
    },
    total=False,
)

ClientCreateBackupResponseTypeDef = TypedDict(
    "ClientCreateBackupResponseTypeDef",
    {"BackupDetails": ClientCreateBackupResponseBackupDetailsTypeDef},
    total=False,
)

ClientCreateGlobalTableReplicationGroupTypeDef = TypedDict(
    "ClientCreateGlobalTableReplicationGroupTypeDef", {"RegionName": str}, total=False
)

ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupTypeDef = TypedDict(
    "ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientCreateGlobalTableResponseGlobalTableDescriptionTypeDef = TypedDict(
    "ClientCreateGlobalTableResponseGlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": List[
            ClientCreateGlobalTableResponseGlobalTableDescriptionReplicationGroupTypeDef
        ],
        "GlobalTableArn": str,
        "CreationDateTime": datetime,
        "GlobalTableStatus": Literal["CREATING", "ACTIVE", "DELETING", "UPDATING"],
        "GlobalTableName": str,
    },
    total=False,
)

ClientCreateGlobalTableResponseTypeDef = TypedDict(
    "ClientCreateGlobalTableResponseTypeDef",
    {"GlobalTableDescription": ClientCreateGlobalTableResponseGlobalTableDescriptionTypeDef},
    total=False,
)

_RequiredClientCreateTableAttributeDefinitionsTypeDef = TypedDict(
    "_RequiredClientCreateTableAttributeDefinitionsTypeDef", {"AttributeName": str}
)
_OptionalClientCreateTableAttributeDefinitionsTypeDef = TypedDict(
    "_OptionalClientCreateTableAttributeDefinitionsTypeDef",
    {"AttributeType": Literal["S", "N", "B"]},
    total=False,
)


class ClientCreateTableAttributeDefinitionsTypeDef(
    _RequiredClientCreateTableAttributeDefinitionsTypeDef,
    _OptionalClientCreateTableAttributeDefinitionsTypeDef,
):
    pass


ClientCreateTableGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientCreateTableGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientCreateTableGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientCreateTableGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientCreateTableGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ClientCreateTableGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

ClientCreateTableGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientCreateTableGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[ClientCreateTableGlobalSecondaryIndexesKeySchemaTypeDef],
        "Projection": ClientCreateTableGlobalSecondaryIndexesProjectionTypeDef,
        "ProvisionedThroughput": ClientCreateTableGlobalSecondaryIndexesProvisionedThroughputTypeDef,
    },
    total=False,
)

ClientCreateTableKeySchemaTypeDef = TypedDict(
    "ClientCreateTableKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientCreateTableLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientCreateTableLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientCreateTableLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientCreateTableLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientCreateTableLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientCreateTableLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[ClientCreateTableLocalSecondaryIndexesKeySchemaTypeDef],
        "Projection": ClientCreateTableLocalSecondaryIndexesProjectionTypeDef,
    },
    total=False,
)

_RequiredClientCreateTableProvisionedThroughputTypeDef = TypedDict(
    "_RequiredClientCreateTableProvisionedThroughputTypeDef", {"ReadCapacityUnits": int}
)
_OptionalClientCreateTableProvisionedThroughputTypeDef = TypedDict(
    "_OptionalClientCreateTableProvisionedThroughputTypeDef",
    {"WriteCapacityUnits": int},
    total=False,
)


class ClientCreateTableProvisionedThroughputTypeDef(
    _RequiredClientCreateTableProvisionedThroughputTypeDef,
    _OptionalClientCreateTableProvisionedThroughputTypeDef,
):
    pass


ClientCreateTableResponseTableDescriptionArchivalSummaryTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionArchivalSummaryTypeDef",
    {"ArchivalDateTime": datetime, "ArchivalReason": str, "ArchivalBackupArn": str},
    total=False,
)

ClientCreateTableResponseTableDescriptionAttributeDefinitionsTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionAttributeDefinitionsTypeDef",
    {"AttributeName": str, "AttributeType": Literal["S", "N", "B"]},
    total=False,
)

ClientCreateTableResponseTableDescriptionBillingModeSummaryTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionBillingModeSummaryTypeDef",
    {
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "Backfilling": bool,
        "ProvisionedThroughput": ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionKeySchemaTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientCreateTableResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientCreateTableResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientCreateTableResponseTableDescriptionLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientCreateTableResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientCreateTableResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionProvisionedThroughputTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientCreateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientCreateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientCreateTableResponseTableDescriptionReplicasTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionReplicasTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientCreateTableResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientCreateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionRestoreSummaryTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionSSEDescriptionTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionSSEDescriptionTypeDef",
    {
        "Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING"],
        "SSEType": Literal["AES256", "KMS"],
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionStreamSpecificationTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientCreateTableResponseTableDescriptionTypeDef = TypedDict(
    "ClientCreateTableResponseTableDescriptionTypeDef",
    {
        "AttributeDefinitions": List[
            ClientCreateTableResponseTableDescriptionAttributeDefinitionsTypeDef
        ],
        "TableName": str,
        "KeySchema": List[ClientCreateTableResponseTableDescriptionKeySchemaTypeDef],
        "TableStatus": Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ],
        "CreationDateTime": datetime,
        "ProvisionedThroughput": ClientCreateTableResponseTableDescriptionProvisionedThroughputTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": ClientCreateTableResponseTableDescriptionBillingModeSummaryTypeDef,
        "LocalSecondaryIndexes": List[
            ClientCreateTableResponseTableDescriptionLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": List[
            ClientCreateTableResponseTableDescriptionGlobalSecondaryIndexesTypeDef
        ],
        "StreamSpecification": ClientCreateTableResponseTableDescriptionStreamSpecificationTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[ClientCreateTableResponseTableDescriptionReplicasTypeDef],
        "RestoreSummary": ClientCreateTableResponseTableDescriptionRestoreSummaryTypeDef,
        "SSEDescription": ClientCreateTableResponseTableDescriptionSSEDescriptionTypeDef,
        "ArchivalSummary": ClientCreateTableResponseTableDescriptionArchivalSummaryTypeDef,
    },
    total=False,
)

ClientCreateTableResponseTypeDef = TypedDict(
    "ClientCreateTableResponseTypeDef",
    {"TableDescription": ClientCreateTableResponseTableDescriptionTypeDef},
    total=False,
)

ClientCreateTableSSESpecificationTypeDef = TypedDict(
    "ClientCreateTableSSESpecificationTypeDef",
    {"Enabled": bool, "SSEType": Literal["AES256", "KMS"], "KMSMasterKeyId": str},
    total=False,
)

ClientCreateTableStreamSpecificationTypeDef = TypedDict(
    "ClientCreateTableStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

_RequiredClientCreateTableTagsTypeDef = TypedDict(
    "_RequiredClientCreateTableTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTableTagsTypeDef = TypedDict(
    "_OptionalClientCreateTableTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTableTagsTypeDef(
    _RequiredClientCreateTableTagsTypeDef, _OptionalClientCreateTableTagsTypeDef
):
    pass


ClientDeleteBackupResponseBackupDescriptionBackupDetailsTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionBackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupSizeBytes": int,
        "BackupStatus": Literal["CREATING", "DELETED", "AVAILABLE"],
        "BackupType": Literal["USER", "SYSTEM", "AWS_BACKUP"],
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
    },
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableDetailsKeySchemaTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableDetailsKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableDetailsProvisionedThroughputTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableDetailsProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableDetailsTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableDetailsTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "TableSizeBytes": int,
        "KeySchema": List[
            ClientDeleteBackupResponseBackupDescriptionSourceTableDetailsKeySchemaTypeDef
        ],
        "TableCreationDateTime": datetime,
        "ProvisionedThroughput": ClientDeleteBackupResponseBackupDescriptionSourceTableDetailsProvisionedThroughputTypeDef,
        "ItemCount": int,
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
    },
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProjectionTypeDef,
        "ProvisionedThroughput": ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProvisionedThroughputTypeDef,
    },
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesProjectionTypeDef,
    },
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsSSEDescriptionTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsSSEDescriptionTypeDef",
    {
        "Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING"],
        "SSEType": Literal["AES256", "KMS"],
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsStreamDescriptionTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsStreamDescriptionTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsTimeToLiveDescriptionTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsTimeToLiveDescriptionTypeDef",
    {
        "TimeToLiveStatus": Literal["ENABLING", "DISABLING", "ENABLED", "DISABLED"],
        "AttributeName": str,
    },
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsTypeDef",
    {
        "LocalSecondaryIndexes": List[
            ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": List[
            ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesTypeDef
        ],
        "StreamDescription": ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsStreamDescriptionTypeDef,
        "TimeToLiveDescription": ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsTimeToLiveDescriptionTypeDef,
        "SSEDescription": ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsSSEDescriptionTypeDef,
    },
    total=False,
)

ClientDeleteBackupResponseBackupDescriptionTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupDescriptionTypeDef",
    {
        "BackupDetails": ClientDeleteBackupResponseBackupDescriptionBackupDetailsTypeDef,
        "SourceTableDetails": ClientDeleteBackupResponseBackupDescriptionSourceTableDetailsTypeDef,
        "SourceTableFeatureDetails": ClientDeleteBackupResponseBackupDescriptionSourceTableFeatureDetailsTypeDef,
    },
    total=False,
)

ClientDeleteBackupResponseTypeDef = TypedDict(
    "ClientDeleteBackupResponseTypeDef",
    {"BackupDescription": ClientDeleteBackupResponseBackupDescriptionTypeDef},
    total=False,
)

ClientDeleteItemExpectedAttributeValueListTypeDef = TypedDict(
    "ClientDeleteItemExpectedAttributeValueListTypeDef",
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

ClientDeleteItemExpectedValueTypeDef = TypedDict(
    "ClientDeleteItemExpectedValueTypeDef",
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

ClientDeleteItemExpectedTypeDef = TypedDict(
    "ClientDeleteItemExpectedTypeDef",
    {
        "Value": ClientDeleteItemExpectedValueTypeDef,
        "Exists": bool,
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
        "AttributeValueList": List[ClientDeleteItemExpectedAttributeValueListTypeDef],
    },
    total=False,
)

ClientDeleteItemExpressionAttributeValuesTypeDef = TypedDict(
    "ClientDeleteItemExpressionAttributeValuesTypeDef",
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

ClientDeleteItemKeyTypeDef = TypedDict(
    "ClientDeleteItemKeyTypeDef",
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

ClientDeleteItemResponseAttributesTypeDef = TypedDict(
    "ClientDeleteItemResponseAttributesTypeDef",
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

ClientDeleteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientDeleteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientDeleteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientDeleteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientDeleteItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientDeleteItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientDeleteItemResponseConsumedCapacityTypeDef = TypedDict(
    "ClientDeleteItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientDeleteItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientDeleteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientDeleteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientDeleteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef = TypedDict(
    "ClientDeleteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef",
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

ClientDeleteItemResponseItemCollectionMetricsTypeDef = TypedDict(
    "ClientDeleteItemResponseItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str, ClientDeleteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ClientDeleteItemResponseTypeDef = TypedDict(
    "ClientDeleteItemResponseTypeDef",
    {
        "Attributes": Dict[str, ClientDeleteItemResponseAttributesTypeDef],
        "ConsumedCapacity": ClientDeleteItemResponseConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ClientDeleteItemResponseItemCollectionMetricsTypeDef,
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionArchivalSummaryTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionArchivalSummaryTypeDef",
    {"ArchivalDateTime": datetime, "ArchivalReason": str, "ArchivalBackupArn": str},
    total=False,
)

ClientDeleteTableResponseTableDescriptionAttributeDefinitionsTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionAttributeDefinitionsTypeDef",
    {"AttributeName": str, "AttributeType": Literal["S", "N", "B"]},
    total=False,
)

ClientDeleteTableResponseTableDescriptionBillingModeSummaryTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionBillingModeSummaryTypeDef",
    {
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "Backfilling": bool,
        "ProvisionedThroughput": ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionKeySchemaTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDeleteTableResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDeleteTableResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientDeleteTableResponseTableDescriptionLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientDeleteTableResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientDeleteTableResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionProvisionedThroughputTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientDeleteTableResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientDeleteTableResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientDeleteTableResponseTableDescriptionReplicasTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionReplicasTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientDeleteTableResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientDeleteTableResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionRestoreSummaryTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionSSEDescriptionTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionSSEDescriptionTypeDef",
    {
        "Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING"],
        "SSEType": Literal["AES256", "KMS"],
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionStreamSpecificationTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientDeleteTableResponseTableDescriptionTypeDef = TypedDict(
    "ClientDeleteTableResponseTableDescriptionTypeDef",
    {
        "AttributeDefinitions": List[
            ClientDeleteTableResponseTableDescriptionAttributeDefinitionsTypeDef
        ],
        "TableName": str,
        "KeySchema": List[ClientDeleteTableResponseTableDescriptionKeySchemaTypeDef],
        "TableStatus": Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ],
        "CreationDateTime": datetime,
        "ProvisionedThroughput": ClientDeleteTableResponseTableDescriptionProvisionedThroughputTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": ClientDeleteTableResponseTableDescriptionBillingModeSummaryTypeDef,
        "LocalSecondaryIndexes": List[
            ClientDeleteTableResponseTableDescriptionLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": List[
            ClientDeleteTableResponseTableDescriptionGlobalSecondaryIndexesTypeDef
        ],
        "StreamSpecification": ClientDeleteTableResponseTableDescriptionStreamSpecificationTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[ClientDeleteTableResponseTableDescriptionReplicasTypeDef],
        "RestoreSummary": ClientDeleteTableResponseTableDescriptionRestoreSummaryTypeDef,
        "SSEDescription": ClientDeleteTableResponseTableDescriptionSSEDescriptionTypeDef,
        "ArchivalSummary": ClientDeleteTableResponseTableDescriptionArchivalSummaryTypeDef,
    },
    total=False,
)

ClientDeleteTableResponseTypeDef = TypedDict(
    "ClientDeleteTableResponseTypeDef",
    {"TableDescription": ClientDeleteTableResponseTableDescriptionTypeDef},
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionBackupDetailsTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionBackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupSizeBytes": int,
        "BackupStatus": Literal["CREATING", "DELETED", "AVAILABLE"],
        "BackupType": Literal["USER", "SYSTEM", "AWS_BACKUP"],
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
    },
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableDetailsKeySchemaTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableDetailsKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableDetailsProvisionedThroughputTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableDetailsProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableDetailsTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableDetailsTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "TableSizeBytes": int,
        "KeySchema": List[
            ClientDescribeBackupResponseBackupDescriptionSourceTableDetailsKeySchemaTypeDef
        ],
        "TableCreationDateTime": datetime,
        "ProvisionedThroughput": ClientDescribeBackupResponseBackupDescriptionSourceTableDetailsProvisionedThroughputTypeDef,
        "ItemCount": int,
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
    },
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProjectionTypeDef,
        "ProvisionedThroughput": ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesProvisionedThroughputTypeDef,
    },
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesProjectionTypeDef,
    },
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsSSEDescriptionTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsSSEDescriptionTypeDef",
    {
        "Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING"],
        "SSEType": Literal["AES256", "KMS"],
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsStreamDescriptionTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsStreamDescriptionTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsTimeToLiveDescriptionTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsTimeToLiveDescriptionTypeDef",
    {
        "TimeToLiveStatus": Literal["ENABLING", "DISABLING", "ENABLED", "DISABLED"],
        "AttributeName": str,
    },
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsTypeDef",
    {
        "LocalSecondaryIndexes": List[
            ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": List[
            ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsGlobalSecondaryIndexesTypeDef
        ],
        "StreamDescription": ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsStreamDescriptionTypeDef,
        "TimeToLiveDescription": ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsTimeToLiveDescriptionTypeDef,
        "SSEDescription": ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsSSEDescriptionTypeDef,
    },
    total=False,
)

ClientDescribeBackupResponseBackupDescriptionTypeDef = TypedDict(
    "ClientDescribeBackupResponseBackupDescriptionTypeDef",
    {
        "BackupDetails": ClientDescribeBackupResponseBackupDescriptionBackupDetailsTypeDef,
        "SourceTableDetails": ClientDescribeBackupResponseBackupDescriptionSourceTableDetailsTypeDef,
        "SourceTableFeatureDetails": ClientDescribeBackupResponseBackupDescriptionSourceTableFeatureDetailsTypeDef,
    },
    total=False,
)

ClientDescribeBackupResponseTypeDef = TypedDict(
    "ClientDescribeBackupResponseTypeDef",
    {"BackupDescription": ClientDescribeBackupResponseBackupDescriptionTypeDef},
    total=False,
)

ClientDescribeContinuousBackupsResponseContinuousBackupsDescriptionPointInTimeRecoveryDescriptionTypeDef = TypedDict(
    "ClientDescribeContinuousBackupsResponseContinuousBackupsDescriptionPointInTimeRecoveryDescriptionTypeDef",
    {
        "PointInTimeRecoveryStatus": Literal["ENABLED", "DISABLED"],
        "EarliestRestorableDateTime": datetime,
        "LatestRestorableDateTime": datetime,
    },
    total=False,
)

ClientDescribeContinuousBackupsResponseContinuousBackupsDescriptionTypeDef = TypedDict(
    "ClientDescribeContinuousBackupsResponseContinuousBackupsDescriptionTypeDef",
    {
        "ContinuousBackupsStatus": Literal["ENABLED", "DISABLED"],
        "PointInTimeRecoveryDescription": ClientDescribeContinuousBackupsResponseContinuousBackupsDescriptionPointInTimeRecoveryDescriptionTypeDef,
    },
    total=False,
)

ClientDescribeContinuousBackupsResponseTypeDef = TypedDict(
    "ClientDescribeContinuousBackupsResponseTypeDef",
    {
        "ContinuousBackupsDescription": ClientDescribeContinuousBackupsResponseContinuousBackupsDescriptionTypeDef
    },
    total=False,
)

ClientDescribeContributorInsightsResponseFailureExceptionTypeDef = TypedDict(
    "ClientDescribeContributorInsightsResponseFailureExceptionTypeDef",
    {"ExceptionName": str, "ExceptionDescription": str},
    total=False,
)

ClientDescribeContributorInsightsResponseTypeDef = TypedDict(
    "ClientDescribeContributorInsightsResponseTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsRuleList": List[str],
        "ContributorInsightsStatus": Literal[
            "ENABLING", "ENABLED", "DISABLING", "DISABLED", "FAILED"
        ],
        "LastUpdateDateTime": datetime,
        "FailureException": ClientDescribeContributorInsightsResponseFailureExceptionTypeDef,
    },
    total=False,
)

ClientDescribeEndpointsResponseEndpointsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsTypeDef",
    {"Address": str, "CachePeriodInMinutes": int},
    total=False,
)

ClientDescribeEndpointsResponseTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseTypeDef",
    {"Endpoints": List[ClientDescribeEndpointsResponseEndpointsTypeDef]},
    total=False,
)

ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupTypeDef = TypedDict(
    "ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientDescribeGlobalTableResponseGlobalTableDescriptionTypeDef = TypedDict(
    "ClientDescribeGlobalTableResponseGlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": List[
            ClientDescribeGlobalTableResponseGlobalTableDescriptionReplicationGroupTypeDef
        ],
        "GlobalTableArn": str,
        "CreationDateTime": datetime,
        "GlobalTableStatus": Literal["CREATING", "ACTIVE", "DELETING", "UPDATING"],
        "GlobalTableName": str,
    },
    total=False,
)

ClientDescribeGlobalTableResponseTypeDef = TypedDict(
    "ClientDescribeGlobalTableResponseTypeDef",
    {"GlobalTableDescription": ClientDescribeGlobalTableResponseGlobalTableDescriptionTypeDef},
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaBillingModeSummaryTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaBillingModeSummaryTypeDef",
    {
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsTypeDef",
    {
        "IndexName": str,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettings": ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsTypeDef,
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettings": ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsTypeDef,
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseReplicaSettingsTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseReplicaSettingsTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaBillingModeSummary": ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaBillingModeSummaryTypeDef,
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettings": ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef,
        "ReplicaProvisionedWriteCapacityUnits": int,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef,
        "ReplicaGlobalSecondaryIndexSettings": List[
            ClientDescribeGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsTypeDef
        ],
    },
    total=False,
)

ClientDescribeGlobalTableSettingsResponseTypeDef = TypedDict(
    "ClientDescribeGlobalTableSettingsResponseTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List[ClientDescribeGlobalTableSettingsResponseReplicaSettingsTypeDef],
    },
    total=False,
)

ClientDescribeLimitsResponseTypeDef = TypedDict(
    "ClientDescribeLimitsResponseTypeDef",
    {
        "AccountMaxReadCapacityUnits": int,
        "AccountMaxWriteCapacityUnits": int,
        "TableMaxReadCapacityUnits": int,
        "TableMaxWriteCapacityUnits": int,
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "ProvisionedReadCapacityAutoScalingSettings": ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsTypeDef,
        "ProvisionedWriteCapacityAutoScalingSettings": ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsTypeDef,
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasTypeDef",
    {
        "RegionName": str,
        "GlobalSecondaryIndexes": List[
            ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesTypeDef
        ],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionTypeDef",
    {
        "TableName": str,
        "TableStatus": Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ],
        "Replicas": List[
            ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasTypeDef
        ],
    },
    total=False,
)

ClientDescribeTableReplicaAutoScalingResponseTypeDef = TypedDict(
    "ClientDescribeTableReplicaAutoScalingResponseTypeDef",
    {
        "TableAutoScalingDescription": ClientDescribeTableReplicaAutoScalingResponseTableAutoScalingDescriptionTypeDef
    },
    total=False,
)

ClientDescribeTableResponseTableArchivalSummaryTypeDef = TypedDict(
    "ClientDescribeTableResponseTableArchivalSummaryTypeDef",
    {"ArchivalDateTime": datetime, "ArchivalReason": str, "ArchivalBackupArn": str},
    total=False,
)

ClientDescribeTableResponseTableAttributeDefinitionsTypeDef = TypedDict(
    "ClientDescribeTableResponseTableAttributeDefinitionsTypeDef",
    {"AttributeName": str, "AttributeType": Literal["S", "N", "B"]},
    total=False,
)

ClientDescribeTableResponseTableBillingModeSummaryTypeDef = TypedDict(
    "ClientDescribeTableResponseTableBillingModeSummaryTypeDef",
    {
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

ClientDescribeTableResponseTableGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientDescribeTableResponseTableGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDescribeTableResponseTableGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientDescribeTableResponseTableGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientDescribeTableResponseTableGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ClientDescribeTableResponseTableGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientDescribeTableResponseTableGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientDescribeTableResponseTableGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[ClientDescribeTableResponseTableGlobalSecondaryIndexesKeySchemaTypeDef],
        "Projection": ClientDescribeTableResponseTableGlobalSecondaryIndexesProjectionTypeDef,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "Backfilling": bool,
        "ProvisionedThroughput": ClientDescribeTableResponseTableGlobalSecondaryIndexesProvisionedThroughputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientDescribeTableResponseTableKeySchemaTypeDef = TypedDict(
    "ClientDescribeTableResponseTableKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDescribeTableResponseTableLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientDescribeTableResponseTableLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDescribeTableResponseTableLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientDescribeTableResponseTableLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientDescribeTableResponseTableLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientDescribeTableResponseTableLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[ClientDescribeTableResponseTableLocalSecondaryIndexesKeySchemaTypeDef],
        "Projection": ClientDescribeTableResponseTableLocalSecondaryIndexesProjectionTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientDescribeTableResponseTableProvisionedThroughputTypeDef = TypedDict(
    "ClientDescribeTableResponseTableProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientDescribeTableResponseTableReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientDescribeTableResponseTableReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientDescribeTableResponseTableReplicasGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientDescribeTableResponseTableReplicasGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientDescribeTableResponseTableReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientDescribeTableResponseTableReplicasProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientDescribeTableResponseTableReplicasProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientDescribeTableResponseTableReplicasTypeDef = TypedDict(
    "ClientDescribeTableResponseTableReplicasTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientDescribeTableResponseTableReplicasProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientDescribeTableResponseTableReplicasGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientDescribeTableResponseTableRestoreSummaryTypeDef = TypedDict(
    "ClientDescribeTableResponseTableRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
    total=False,
)

ClientDescribeTableResponseTableSSEDescriptionTypeDef = TypedDict(
    "ClientDescribeTableResponseTableSSEDescriptionTypeDef",
    {
        "Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING"],
        "SSEType": Literal["AES256", "KMS"],
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

ClientDescribeTableResponseTableStreamSpecificationTypeDef = TypedDict(
    "ClientDescribeTableResponseTableStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientDescribeTableResponseTableTypeDef = TypedDict(
    "ClientDescribeTableResponseTableTypeDef",
    {
        "AttributeDefinitions": List[ClientDescribeTableResponseTableAttributeDefinitionsTypeDef],
        "TableName": str,
        "KeySchema": List[ClientDescribeTableResponseTableKeySchemaTypeDef],
        "TableStatus": Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ],
        "CreationDateTime": datetime,
        "ProvisionedThroughput": ClientDescribeTableResponseTableProvisionedThroughputTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": ClientDescribeTableResponseTableBillingModeSummaryTypeDef,
        "LocalSecondaryIndexes": List[ClientDescribeTableResponseTableLocalSecondaryIndexesTypeDef],
        "GlobalSecondaryIndexes": List[
            ClientDescribeTableResponseTableGlobalSecondaryIndexesTypeDef
        ],
        "StreamSpecification": ClientDescribeTableResponseTableStreamSpecificationTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[ClientDescribeTableResponseTableReplicasTypeDef],
        "RestoreSummary": ClientDescribeTableResponseTableRestoreSummaryTypeDef,
        "SSEDescription": ClientDescribeTableResponseTableSSEDescriptionTypeDef,
        "ArchivalSummary": ClientDescribeTableResponseTableArchivalSummaryTypeDef,
    },
    total=False,
)

ClientDescribeTableResponseTypeDef = TypedDict(
    "ClientDescribeTableResponseTypeDef",
    {"Table": ClientDescribeTableResponseTableTypeDef},
    total=False,
)

ClientDescribeTimeToLiveResponseTimeToLiveDescriptionTypeDef = TypedDict(
    "ClientDescribeTimeToLiveResponseTimeToLiveDescriptionTypeDef",
    {
        "TimeToLiveStatus": Literal["ENABLING", "DISABLING", "ENABLED", "DISABLED"],
        "AttributeName": str,
    },
    total=False,
)

ClientDescribeTimeToLiveResponseTypeDef = TypedDict(
    "ClientDescribeTimeToLiveResponseTypeDef",
    {"TimeToLiveDescription": ClientDescribeTimeToLiveResponseTimeToLiveDescriptionTypeDef},
    total=False,
)

ClientGetItemKeyTypeDef = TypedDict(
    "ClientGetItemKeyTypeDef",
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

ClientGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientGetItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientGetItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientGetItemResponseConsumedCapacityTypeDef = TypedDict(
    "ClientGetItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientGetItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientGetItemResponseItemTypeDef = TypedDict(
    "ClientGetItemResponseItemTypeDef",
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

ClientGetItemResponseTypeDef = TypedDict(
    "ClientGetItemResponseTypeDef",
    {
        "Item": Dict[str, ClientGetItemResponseItemTypeDef],
        "ConsumedCapacity": ClientGetItemResponseConsumedCapacityTypeDef,
    },
    total=False,
)

ClientListBackupsResponseBackupSummariesTypeDef = TypedDict(
    "ClientListBackupsResponseBackupSummariesTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "BackupArn": str,
        "BackupName": str,
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
        "BackupStatus": Literal["CREATING", "DELETED", "AVAILABLE"],
        "BackupType": Literal["USER", "SYSTEM", "AWS_BACKUP"],
        "BackupSizeBytes": int,
    },
    total=False,
)

ClientListBackupsResponseTypeDef = TypedDict(
    "ClientListBackupsResponseTypeDef",
    {
        "BackupSummaries": List[ClientListBackupsResponseBackupSummariesTypeDef],
        "LastEvaluatedBackupArn": str,
    },
    total=False,
)

ClientListContributorInsightsResponseContributorInsightsSummariesTypeDef = TypedDict(
    "ClientListContributorInsightsResponseContributorInsightsSummariesTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": Literal[
            "ENABLING", "ENABLED", "DISABLING", "DISABLED", "FAILED"
        ],
    },
    total=False,
)

ClientListContributorInsightsResponseTypeDef = TypedDict(
    "ClientListContributorInsightsResponseTypeDef",
    {
        "ContributorInsightsSummaries": List[
            ClientListContributorInsightsResponseContributorInsightsSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListGlobalTablesResponseGlobalTablesReplicationGroupTypeDef = TypedDict(
    "ClientListGlobalTablesResponseGlobalTablesReplicationGroupTypeDef",
    {"RegionName": str},
    total=False,
)

ClientListGlobalTablesResponseGlobalTablesTypeDef = TypedDict(
    "ClientListGlobalTablesResponseGlobalTablesTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": List[ClientListGlobalTablesResponseGlobalTablesReplicationGroupTypeDef],
    },
    total=False,
)

ClientListGlobalTablesResponseTypeDef = TypedDict(
    "ClientListGlobalTablesResponseTypeDef",
    {
        "GlobalTables": List[ClientListGlobalTablesResponseGlobalTablesTypeDef],
        "LastEvaluatedGlobalTableName": str,
    },
    total=False,
)

ClientListTablesResponseTypeDef = TypedDict(
    "ClientListTablesResponseTypeDef",
    {"TableNames": List[str], "LastEvaluatedTableName": str},
    total=False,
)

ClientListTagsOfResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsOfResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsOfResourceResponseTypeDef = TypedDict(
    "ClientListTagsOfResourceResponseTypeDef",
    {"Tags": List[ClientListTagsOfResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientPutItemExpectedAttributeValueListTypeDef = TypedDict(
    "ClientPutItemExpectedAttributeValueListTypeDef",
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

ClientPutItemExpectedValueTypeDef = TypedDict(
    "ClientPutItemExpectedValueTypeDef",
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

ClientPutItemExpectedTypeDef = TypedDict(
    "ClientPutItemExpectedTypeDef",
    {
        "Value": ClientPutItemExpectedValueTypeDef,
        "Exists": bool,
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
        "AttributeValueList": List[ClientPutItemExpectedAttributeValueListTypeDef],
    },
    total=False,
)

ClientPutItemExpressionAttributeValuesTypeDef = TypedDict(
    "ClientPutItemExpressionAttributeValuesTypeDef",
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

ClientPutItemItemTypeDef = TypedDict(
    "ClientPutItemItemTypeDef",
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

ClientPutItemResponseAttributesTypeDef = TypedDict(
    "ClientPutItemResponseAttributesTypeDef",
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

ClientPutItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientPutItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientPutItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientPutItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientPutItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientPutItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientPutItemResponseConsumedCapacityTypeDef = TypedDict(
    "ClientPutItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientPutItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientPutItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientPutItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientPutItemResponseItemCollectionMetricsItemCollectionKeyTypeDef = TypedDict(
    "ClientPutItemResponseItemCollectionMetricsItemCollectionKeyTypeDef",
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

ClientPutItemResponseItemCollectionMetricsTypeDef = TypedDict(
    "ClientPutItemResponseItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str, ClientPutItemResponseItemCollectionMetricsItemCollectionKeyTypeDef
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ClientPutItemResponseTypeDef = TypedDict(
    "ClientPutItemResponseTypeDef",
    {
        "Attributes": Dict[str, ClientPutItemResponseAttributesTypeDef],
        "ConsumedCapacity": ClientPutItemResponseConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ClientPutItemResponseItemCollectionMetricsTypeDef,
    },
    total=False,
)

ClientQueryExclusiveStartKeyTypeDef = TypedDict(
    "ClientQueryExclusiveStartKeyTypeDef",
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

ClientQueryExpressionAttributeValuesTypeDef = TypedDict(
    "ClientQueryExpressionAttributeValuesTypeDef",
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

ClientQueryKeyConditionsAttributeValueListTypeDef = TypedDict(
    "ClientQueryKeyConditionsAttributeValueListTypeDef",
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

ClientQueryKeyConditionsTypeDef = TypedDict(
    "ClientQueryKeyConditionsTypeDef",
    {
        "AttributeValueList": List[ClientQueryKeyConditionsAttributeValueListTypeDef],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
    },
    total=False,
)

ClientQueryQueryFilterAttributeValueListTypeDef = TypedDict(
    "ClientQueryQueryFilterAttributeValueListTypeDef",
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

ClientQueryQueryFilterTypeDef = TypedDict(
    "ClientQueryQueryFilterTypeDef",
    {
        "AttributeValueList": List[ClientQueryQueryFilterAttributeValueListTypeDef],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
    },
    total=False,
)

ClientQueryResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientQueryResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientQueryResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientQueryResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientQueryResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientQueryResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientQueryResponseConsumedCapacityTypeDef = TypedDict(
    "ClientQueryResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientQueryResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientQueryResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientQueryResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientQueryResponseItemsTypeDef = TypedDict(
    "ClientQueryResponseItemsTypeDef",
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

ClientQueryResponseLastEvaluatedKeyTypeDef = TypedDict(
    "ClientQueryResponseLastEvaluatedKeyTypeDef",
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

ClientQueryResponseTypeDef = TypedDict(
    "ClientQueryResponseTypeDef",
    {
        "Items": List[Dict[str, ClientQueryResponseItemsTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, ClientQueryResponseLastEvaluatedKeyTypeDef],
        "ConsumedCapacity": ClientQueryResponseConsumedCapacityTypeDef,
    },
    total=False,
)

ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideProjectionTypeDef = TypedDict(
    "ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideProvisionedThroughputTypeDef = TypedDict(
    "ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

_RequiredClientRestoreTableFromBackupGlobalSecondaryIndexOverrideTypeDef = TypedDict(
    "_RequiredClientRestoreTableFromBackupGlobalSecondaryIndexOverrideTypeDef", {"IndexName": str}
)
_OptionalClientRestoreTableFromBackupGlobalSecondaryIndexOverrideTypeDef = TypedDict(
    "_OptionalClientRestoreTableFromBackupGlobalSecondaryIndexOverrideTypeDef",
    {
        "KeySchema": List[ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideKeySchemaTypeDef],
        "Projection": ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideProjectionTypeDef,
        "ProvisionedThroughput": ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideProvisionedThroughputTypeDef,
    },
    total=False,
)


class ClientRestoreTableFromBackupGlobalSecondaryIndexOverrideTypeDef(
    _RequiredClientRestoreTableFromBackupGlobalSecondaryIndexOverrideTypeDef,
    _OptionalClientRestoreTableFromBackupGlobalSecondaryIndexOverrideTypeDef,
):
    pass


ClientRestoreTableFromBackupLocalSecondaryIndexOverrideKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableFromBackupLocalSecondaryIndexOverrideKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableFromBackupLocalSecondaryIndexOverrideProjectionTypeDef = TypedDict(
    "ClientRestoreTableFromBackupLocalSecondaryIndexOverrideProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

_RequiredClientRestoreTableFromBackupLocalSecondaryIndexOverrideTypeDef = TypedDict(
    "_RequiredClientRestoreTableFromBackupLocalSecondaryIndexOverrideTypeDef", {"IndexName": str}
)
_OptionalClientRestoreTableFromBackupLocalSecondaryIndexOverrideTypeDef = TypedDict(
    "_OptionalClientRestoreTableFromBackupLocalSecondaryIndexOverrideTypeDef",
    {
        "KeySchema": List[ClientRestoreTableFromBackupLocalSecondaryIndexOverrideKeySchemaTypeDef],
        "Projection": ClientRestoreTableFromBackupLocalSecondaryIndexOverrideProjectionTypeDef,
    },
    total=False,
)


class ClientRestoreTableFromBackupLocalSecondaryIndexOverrideTypeDef(
    _RequiredClientRestoreTableFromBackupLocalSecondaryIndexOverrideTypeDef,
    _OptionalClientRestoreTableFromBackupLocalSecondaryIndexOverrideTypeDef,
):
    pass


_RequiredClientRestoreTableFromBackupProvisionedThroughputOverrideTypeDef = TypedDict(
    "_RequiredClientRestoreTableFromBackupProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
)
_OptionalClientRestoreTableFromBackupProvisionedThroughputOverrideTypeDef = TypedDict(
    "_OptionalClientRestoreTableFromBackupProvisionedThroughputOverrideTypeDef",
    {"WriteCapacityUnits": int},
    total=False,
)


class ClientRestoreTableFromBackupProvisionedThroughputOverrideTypeDef(
    _RequiredClientRestoreTableFromBackupProvisionedThroughputOverrideTypeDef,
    _OptionalClientRestoreTableFromBackupProvisionedThroughputOverrideTypeDef,
):
    pass


ClientRestoreTableFromBackupResponseTableDescriptionArchivalSummaryTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionArchivalSummaryTypeDef",
    {"ArchivalDateTime": datetime, "ArchivalReason": str, "ArchivalBackupArn": str},
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionAttributeDefinitionsTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionAttributeDefinitionsTypeDef",
    {"AttributeName": str, "AttributeType": Literal["S", "N", "B"]},
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionBillingModeSummaryTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionBillingModeSummaryTypeDef",
    {
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "Backfilling": bool,
        "ProvisionedThroughput": ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientRestoreTableFromBackupResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientRestoreTableFromBackupResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionProvisionedThroughputTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientRestoreTableFromBackupResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionReplicasTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionReplicasTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientRestoreTableFromBackupResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientRestoreTableFromBackupResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionRestoreSummaryTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionSSEDescriptionTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionSSEDescriptionTypeDef",
    {
        "Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING"],
        "SSEType": Literal["AES256", "KMS"],
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionStreamSpecificationTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTableDescriptionTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTableDescriptionTypeDef",
    {
        "AttributeDefinitions": List[
            ClientRestoreTableFromBackupResponseTableDescriptionAttributeDefinitionsTypeDef
        ],
        "TableName": str,
        "KeySchema": List[ClientRestoreTableFromBackupResponseTableDescriptionKeySchemaTypeDef],
        "TableStatus": Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ],
        "CreationDateTime": datetime,
        "ProvisionedThroughput": ClientRestoreTableFromBackupResponseTableDescriptionProvisionedThroughputTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": ClientRestoreTableFromBackupResponseTableDescriptionBillingModeSummaryTypeDef,
        "LocalSecondaryIndexes": List[
            ClientRestoreTableFromBackupResponseTableDescriptionLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": List[
            ClientRestoreTableFromBackupResponseTableDescriptionGlobalSecondaryIndexesTypeDef
        ],
        "StreamSpecification": ClientRestoreTableFromBackupResponseTableDescriptionStreamSpecificationTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[ClientRestoreTableFromBackupResponseTableDescriptionReplicasTypeDef],
        "RestoreSummary": ClientRestoreTableFromBackupResponseTableDescriptionRestoreSummaryTypeDef,
        "SSEDescription": ClientRestoreTableFromBackupResponseTableDescriptionSSEDescriptionTypeDef,
        "ArchivalSummary": ClientRestoreTableFromBackupResponseTableDescriptionArchivalSummaryTypeDef,
    },
    total=False,
)

ClientRestoreTableFromBackupResponseTypeDef = TypedDict(
    "ClientRestoreTableFromBackupResponseTypeDef",
    {"TableDescription": ClientRestoreTableFromBackupResponseTableDescriptionTypeDef},
    total=False,
)

ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideProjectionTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideProvisionedThroughputTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

_RequiredClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideTypeDef = TypedDict(
    "_RequiredClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideTypeDef",
    {"IndexName": str},
)
_OptionalClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideTypeDef = TypedDict(
    "_OptionalClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideTypeDef",
    {
        "KeySchema": List[
            ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideKeySchemaTypeDef
        ],
        "Projection": ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideProjectionTypeDef,
        "ProvisionedThroughput": ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideProvisionedThroughputTypeDef,
    },
    total=False,
)


class ClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideTypeDef(
    _RequiredClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideTypeDef,
    _OptionalClientRestoreTableToPointInTimeGlobalSecondaryIndexOverrideTypeDef,
):
    pass


ClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideProjectionTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

_RequiredClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideTypeDef = TypedDict(
    "_RequiredClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideTypeDef", {"IndexName": str}
)
_OptionalClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideTypeDef = TypedDict(
    "_OptionalClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideTypeDef",
    {
        "KeySchema": List[
            ClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideKeySchemaTypeDef
        ],
        "Projection": ClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideProjectionTypeDef,
    },
    total=False,
)


class ClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideTypeDef(
    _RequiredClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideTypeDef,
    _OptionalClientRestoreTableToPointInTimeLocalSecondaryIndexOverrideTypeDef,
):
    pass


_RequiredClientRestoreTableToPointInTimeProvisionedThroughputOverrideTypeDef = TypedDict(
    "_RequiredClientRestoreTableToPointInTimeProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
)
_OptionalClientRestoreTableToPointInTimeProvisionedThroughputOverrideTypeDef = TypedDict(
    "_OptionalClientRestoreTableToPointInTimeProvisionedThroughputOverrideTypeDef",
    {"WriteCapacityUnits": int},
    total=False,
)


class ClientRestoreTableToPointInTimeProvisionedThroughputOverrideTypeDef(
    _RequiredClientRestoreTableToPointInTimeProvisionedThroughputOverrideTypeDef,
    _OptionalClientRestoreTableToPointInTimeProvisionedThroughputOverrideTypeDef,
):
    pass


ClientRestoreTableToPointInTimeResponseTableDescriptionArchivalSummaryTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionArchivalSummaryTypeDef",
    {"ArchivalDateTime": datetime, "ArchivalReason": str, "ArchivalBackupArn": str},
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionAttributeDefinitionsTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionAttributeDefinitionsTypeDef",
    {"AttributeName": str, "AttributeType": Literal["S", "N", "B"]},
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionBillingModeSummaryTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionBillingModeSummaryTypeDef",
    {
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "Backfilling": bool,
        "ProvisionedThroughput": ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientRestoreTableToPointInTimeResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientRestoreTableToPointInTimeResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionProvisionedThroughputTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionRestoreSummaryTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionSSEDescriptionTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionSSEDescriptionTypeDef",
    {
        "Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING"],
        "SSEType": Literal["AES256", "KMS"],
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionStreamSpecificationTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTableDescriptionTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTableDescriptionTypeDef",
    {
        "AttributeDefinitions": List[
            ClientRestoreTableToPointInTimeResponseTableDescriptionAttributeDefinitionsTypeDef
        ],
        "TableName": str,
        "KeySchema": List[ClientRestoreTableToPointInTimeResponseTableDescriptionKeySchemaTypeDef],
        "TableStatus": Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ],
        "CreationDateTime": datetime,
        "ProvisionedThroughput": ClientRestoreTableToPointInTimeResponseTableDescriptionProvisionedThroughputTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": ClientRestoreTableToPointInTimeResponseTableDescriptionBillingModeSummaryTypeDef,
        "LocalSecondaryIndexes": List[
            ClientRestoreTableToPointInTimeResponseTableDescriptionLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": List[
            ClientRestoreTableToPointInTimeResponseTableDescriptionGlobalSecondaryIndexesTypeDef
        ],
        "StreamSpecification": ClientRestoreTableToPointInTimeResponseTableDescriptionStreamSpecificationTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[ClientRestoreTableToPointInTimeResponseTableDescriptionReplicasTypeDef],
        "RestoreSummary": ClientRestoreTableToPointInTimeResponseTableDescriptionRestoreSummaryTypeDef,
        "SSEDescription": ClientRestoreTableToPointInTimeResponseTableDescriptionSSEDescriptionTypeDef,
        "ArchivalSummary": ClientRestoreTableToPointInTimeResponseTableDescriptionArchivalSummaryTypeDef,
    },
    total=False,
)

ClientRestoreTableToPointInTimeResponseTypeDef = TypedDict(
    "ClientRestoreTableToPointInTimeResponseTypeDef",
    {"TableDescription": ClientRestoreTableToPointInTimeResponseTableDescriptionTypeDef},
    total=False,
)

ClientScanExclusiveStartKeyTypeDef = TypedDict(
    "ClientScanExclusiveStartKeyTypeDef",
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

ClientScanExpressionAttributeValuesTypeDef = TypedDict(
    "ClientScanExpressionAttributeValuesTypeDef",
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

ClientScanResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientScanResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientScanResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientScanResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientScanResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientScanResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientScanResponseConsumedCapacityTypeDef = TypedDict(
    "ClientScanResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientScanResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientScanResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientScanResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientScanResponseItemsTypeDef = TypedDict(
    "ClientScanResponseItemsTypeDef",
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

ClientScanResponseLastEvaluatedKeyTypeDef = TypedDict(
    "ClientScanResponseLastEvaluatedKeyTypeDef",
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

ClientScanResponseTypeDef = TypedDict(
    "ClientScanResponseTypeDef",
    {
        "Items": List[Dict[str, ClientScanResponseItemsTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, ClientScanResponseLastEvaluatedKeyTypeDef],
        "ConsumedCapacity": ClientScanResponseConsumedCapacityTypeDef,
    },
    total=False,
)

ClientScanScanFilterAttributeValueListTypeDef = TypedDict(
    "ClientScanScanFilterAttributeValueListTypeDef",
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

ClientScanScanFilterTypeDef = TypedDict(
    "ClientScanScanFilterTypeDef",
    {
        "AttributeValueList": List[ClientScanScanFilterAttributeValueListTypeDef],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
    },
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientTransactGetItemsResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientTransactGetItemsResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientTransactGetItemsResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientTransactGetItemsResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientTransactGetItemsResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientTransactGetItemsResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientTransactGetItemsResponseConsumedCapacityTypeDef = TypedDict(
    "ClientTransactGetItemsResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientTransactGetItemsResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientTransactGetItemsResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientTransactGetItemsResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientTransactGetItemsResponseResponsesItemTypeDef = TypedDict(
    "ClientTransactGetItemsResponseResponsesItemTypeDef",
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

ClientTransactGetItemsResponseResponsesTypeDef = TypedDict(
    "ClientTransactGetItemsResponseResponsesTypeDef",
    {"Item": Dict[str, ClientTransactGetItemsResponseResponsesItemTypeDef]},
    total=False,
)

ClientTransactGetItemsResponseTypeDef = TypedDict(
    "ClientTransactGetItemsResponseTypeDef",
    {
        "ConsumedCapacity": List[ClientTransactGetItemsResponseConsumedCapacityTypeDef],
        "Responses": List[ClientTransactGetItemsResponseResponsesTypeDef],
    },
    total=False,
)

ClientTransactGetItemsTransactItemsGetKeyTypeDef = TypedDict(
    "ClientTransactGetItemsTransactItemsGetKeyTypeDef",
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

_RequiredClientTransactGetItemsTransactItemsGetTypeDef = TypedDict(
    "_RequiredClientTransactGetItemsTransactItemsGetTypeDef",
    {"Key": Dict[str, ClientTransactGetItemsTransactItemsGetKeyTypeDef]},
)
_OptionalClientTransactGetItemsTransactItemsGetTypeDef = TypedDict(
    "_OptionalClientTransactGetItemsTransactItemsGetTypeDef",
    {"TableName": str, "ProjectionExpression": str, "ExpressionAttributeNames": Dict[str, str]},
    total=False,
)


class ClientTransactGetItemsTransactItemsGetTypeDef(
    _RequiredClientTransactGetItemsTransactItemsGetTypeDef,
    _OptionalClientTransactGetItemsTransactItemsGetTypeDef,
):
    pass


ClientTransactGetItemsTransactItemsTypeDef = TypedDict(
    "ClientTransactGetItemsTransactItemsTypeDef",
    {"Get": ClientTransactGetItemsTransactItemsGetTypeDef},
)

ClientTransactWriteItemsResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientTransactWriteItemsResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientTransactWriteItemsResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientTransactWriteItemsResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientTransactWriteItemsResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientTransactWriteItemsResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientTransactWriteItemsResponseConsumedCapacityTypeDef = TypedDict(
    "ClientTransactWriteItemsResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientTransactWriteItemsResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientTransactWriteItemsResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientTransactWriteItemsResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientTransactWriteItemsResponseItemCollectionMetricsItemCollectionKeyTypeDef = TypedDict(
    "ClientTransactWriteItemsResponseItemCollectionMetricsItemCollectionKeyTypeDef",
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

ClientTransactWriteItemsResponseItemCollectionMetricsTypeDef = TypedDict(
    "ClientTransactWriteItemsResponseItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str, ClientTransactWriteItemsResponseItemCollectionMetricsItemCollectionKeyTypeDef
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ClientTransactWriteItemsResponseTypeDef = TypedDict(
    "ClientTransactWriteItemsResponseTypeDef",
    {
        "ConsumedCapacity": List[ClientTransactWriteItemsResponseConsumedCapacityTypeDef],
        "ItemCollectionMetrics": Dict[
            str, List[ClientTransactWriteItemsResponseItemCollectionMetricsTypeDef]
        ],
    },
    total=False,
)

ClientTransactWriteItemsTransactItemsConditionCheckExpressionAttributeValuesTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsConditionCheckExpressionAttributeValuesTypeDef",
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

ClientTransactWriteItemsTransactItemsConditionCheckKeyTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsConditionCheckKeyTypeDef",
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

_RequiredClientTransactWriteItemsTransactItemsConditionCheckTypeDef = TypedDict(
    "_RequiredClientTransactWriteItemsTransactItemsConditionCheckTypeDef",
    {"Key": Dict[str, ClientTransactWriteItemsTransactItemsConditionCheckKeyTypeDef]},
)
_OptionalClientTransactWriteItemsTransactItemsConditionCheckTypeDef = TypedDict(
    "_OptionalClientTransactWriteItemsTransactItemsConditionCheckTypeDef",
    {
        "TableName": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str, ClientTransactWriteItemsTransactItemsConditionCheckExpressionAttributeValuesTypeDef
        ],
        "ReturnValuesOnConditionCheckFailure": Literal["ALL_OLD", "NONE"],
    },
    total=False,
)


class ClientTransactWriteItemsTransactItemsConditionCheckTypeDef(
    _RequiredClientTransactWriteItemsTransactItemsConditionCheckTypeDef,
    _OptionalClientTransactWriteItemsTransactItemsConditionCheckTypeDef,
):
    pass


ClientTransactWriteItemsTransactItemsDeleteExpressionAttributeValuesTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsDeleteExpressionAttributeValuesTypeDef",
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

ClientTransactWriteItemsTransactItemsDeleteKeyTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsDeleteKeyTypeDef",
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

ClientTransactWriteItemsTransactItemsDeleteTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsDeleteTypeDef",
    {
        "Key": Dict[str, ClientTransactWriteItemsTransactItemsDeleteKeyTypeDef],
        "TableName": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str, ClientTransactWriteItemsTransactItemsDeleteExpressionAttributeValuesTypeDef
        ],
        "ReturnValuesOnConditionCheckFailure": Literal["ALL_OLD", "NONE"],
    },
    total=False,
)

ClientTransactWriteItemsTransactItemsPutExpressionAttributeValuesTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsPutExpressionAttributeValuesTypeDef",
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

ClientTransactWriteItemsTransactItemsPutItemTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsPutItemTypeDef",
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

ClientTransactWriteItemsTransactItemsPutTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsPutTypeDef",
    {
        "Item": Dict[str, ClientTransactWriteItemsTransactItemsPutItemTypeDef],
        "TableName": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str, ClientTransactWriteItemsTransactItemsPutExpressionAttributeValuesTypeDef
        ],
        "ReturnValuesOnConditionCheckFailure": Literal["ALL_OLD", "NONE"],
    },
    total=False,
)

ClientTransactWriteItemsTransactItemsUpdateExpressionAttributeValuesTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsUpdateExpressionAttributeValuesTypeDef",
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

ClientTransactWriteItemsTransactItemsUpdateKeyTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsUpdateKeyTypeDef",
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

ClientTransactWriteItemsTransactItemsUpdateTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsUpdateTypeDef",
    {
        "Key": Dict[str, ClientTransactWriteItemsTransactItemsUpdateKeyTypeDef],
        "UpdateExpression": str,
        "TableName": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str, ClientTransactWriteItemsTransactItemsUpdateExpressionAttributeValuesTypeDef
        ],
        "ReturnValuesOnConditionCheckFailure": Literal["ALL_OLD", "NONE"],
    },
    total=False,
)

ClientTransactWriteItemsTransactItemsTypeDef = TypedDict(
    "ClientTransactWriteItemsTransactItemsTypeDef",
    {
        "ConditionCheck": ClientTransactWriteItemsTransactItemsConditionCheckTypeDef,
        "Put": ClientTransactWriteItemsTransactItemsPutTypeDef,
        "Delete": ClientTransactWriteItemsTransactItemsDeleteTypeDef,
        "Update": ClientTransactWriteItemsTransactItemsUpdateTypeDef,
    },
    total=False,
)

ClientUpdateContinuousBackupsPointInTimeRecoverySpecificationTypeDef = TypedDict(
    "ClientUpdateContinuousBackupsPointInTimeRecoverySpecificationTypeDef",
    {"PointInTimeRecoveryEnabled": bool},
)

ClientUpdateContinuousBackupsResponseContinuousBackupsDescriptionPointInTimeRecoveryDescriptionTypeDef = TypedDict(
    "ClientUpdateContinuousBackupsResponseContinuousBackupsDescriptionPointInTimeRecoveryDescriptionTypeDef",
    {
        "PointInTimeRecoveryStatus": Literal["ENABLED", "DISABLED"],
        "EarliestRestorableDateTime": datetime,
        "LatestRestorableDateTime": datetime,
    },
    total=False,
)

ClientUpdateContinuousBackupsResponseContinuousBackupsDescriptionTypeDef = TypedDict(
    "ClientUpdateContinuousBackupsResponseContinuousBackupsDescriptionTypeDef",
    {
        "ContinuousBackupsStatus": Literal["ENABLED", "DISABLED"],
        "PointInTimeRecoveryDescription": ClientUpdateContinuousBackupsResponseContinuousBackupsDescriptionPointInTimeRecoveryDescriptionTypeDef,
    },
    total=False,
)

ClientUpdateContinuousBackupsResponseTypeDef = TypedDict(
    "ClientUpdateContinuousBackupsResponseTypeDef",
    {
        "ContinuousBackupsDescription": ClientUpdateContinuousBackupsResponseContinuousBackupsDescriptionTypeDef
    },
    total=False,
)

ClientUpdateContributorInsightsResponseTypeDef = TypedDict(
    "ClientUpdateContributorInsightsResponseTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": Literal[
            "ENABLING", "ENABLED", "DISABLING", "DISABLED", "FAILED"
        ],
    },
    total=False,
)

ClientUpdateGlobalTableReplicaUpdatesCreateTypeDef = TypedDict(
    "ClientUpdateGlobalTableReplicaUpdatesCreateTypeDef", {"RegionName": str}
)

ClientUpdateGlobalTableReplicaUpdatesDeleteTypeDef = TypedDict(
    "ClientUpdateGlobalTableReplicaUpdatesDeleteTypeDef", {"RegionName": str}, total=False
)

ClientUpdateGlobalTableReplicaUpdatesTypeDef = TypedDict(
    "ClientUpdateGlobalTableReplicaUpdatesTypeDef",
    {
        "Create": ClientUpdateGlobalTableReplicaUpdatesCreateTypeDef,
        "Delete": ClientUpdateGlobalTableReplicaUpdatesDeleteTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupTypeDef = TypedDict(
    "ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientUpdateGlobalTableResponseGlobalTableDescriptionTypeDef = TypedDict(
    "ClientUpdateGlobalTableResponseGlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": List[
            ClientUpdateGlobalTableResponseGlobalTableDescriptionReplicationGroupTypeDef
        ],
        "GlobalTableArn": str,
        "CreationDateTime": datetime,
        "GlobalTableStatus": Literal["CREATING", "ACTIVE", "DELETING", "UPDATING"],
        "GlobalTableName": str,
    },
    total=False,
)

ClientUpdateGlobalTableResponseTypeDef = TypedDict(
    "ClientUpdateGlobalTableResponseTypeDef",
    {"GlobalTableDescription": ClientUpdateGlobalTableResponseGlobalTableDescriptionTypeDef},
    total=False,
)

ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateProvisionedWriteCapacityAutoScalingSettingsUpdateTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateProvisionedWriteCapacityAutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef,
    },
    total=False,
)

_RequiredClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {"IndexName": str},
)
_OptionalClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettingsUpdate": ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateProvisionedWriteCapacityAutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalClientUpdateGlobalTableSettingsGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass


ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": ClientUpdateGlobalTableSettingsGlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateProvisionedReadCapacityAutoScalingSettingsUpdateTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateProvisionedReadCapacityAutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettingsUpdate": ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateProvisionedReadCapacityAutoScalingSettingsUpdateTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaProvisionedReadCapacityAutoScalingSettingsUpdateTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaProvisionedReadCapacityAutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaProvisionedReadCapacityAutoScalingSettingsUpdateScalingPolicyUpdateTypeDef,
    },
    total=False,
)

_RequiredClientUpdateGlobalTableSettingsReplicaSettingsUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateGlobalTableSettingsReplicaSettingsUpdateTypeDef", {"RegionName": str}
)
_OptionalClientUpdateGlobalTableSettingsReplicaSettingsUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateGlobalTableSettingsReplicaSettingsUpdateTypeDef",
    {
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate": ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaProvisionedReadCapacityAutoScalingSettingsUpdateTypeDef,
        "ReplicaGlobalSecondaryIndexSettingsUpdate": List[
            ClientUpdateGlobalTableSettingsReplicaSettingsUpdateReplicaGlobalSecondaryIndexSettingsUpdateTypeDef
        ],
    },
    total=False,
)


class ClientUpdateGlobalTableSettingsReplicaSettingsUpdateTypeDef(
    _RequiredClientUpdateGlobalTableSettingsReplicaSettingsUpdateTypeDef,
    _OptionalClientUpdateGlobalTableSettingsReplicaSettingsUpdateTypeDef,
):
    pass


ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaBillingModeSummaryTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaBillingModeSummaryTypeDef",
    {
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsTypeDef",
    {
        "IndexName": str,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettings": ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedReadCapacityAutoScalingSettingsTypeDef,
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettings": ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsProvisionedWriteCapacityAutoScalingSettingsTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseReplicaSettingsTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseReplicaSettingsTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaBillingModeSummary": ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaBillingModeSummaryTypeDef,
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettings": ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef,
        "ReplicaProvisionedWriteCapacityUnits": int,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef,
        "ReplicaGlobalSecondaryIndexSettings": List[
            ClientUpdateGlobalTableSettingsResponseReplicaSettingsReplicaGlobalSecondaryIndexSettingsTypeDef
        ],
    },
    total=False,
)

ClientUpdateGlobalTableSettingsResponseTypeDef = TypedDict(
    "ClientUpdateGlobalTableSettingsResponseTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List[ClientUpdateGlobalTableSettingsResponseReplicaSettingsTypeDef],
    },
    total=False,
)

ClientUpdateItemAttributeUpdatesValueTypeDef = TypedDict(
    "ClientUpdateItemAttributeUpdatesValueTypeDef",
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

ClientUpdateItemAttributeUpdatesTypeDef = TypedDict(
    "ClientUpdateItemAttributeUpdatesTypeDef",
    {
        "Value": ClientUpdateItemAttributeUpdatesValueTypeDef,
        "Action": Literal["ADD", "PUT", "DELETE"],
    },
    total=False,
)

ClientUpdateItemExpectedAttributeValueListTypeDef = TypedDict(
    "ClientUpdateItemExpectedAttributeValueListTypeDef",
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

ClientUpdateItemExpectedValueTypeDef = TypedDict(
    "ClientUpdateItemExpectedValueTypeDef",
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

ClientUpdateItemExpectedTypeDef = TypedDict(
    "ClientUpdateItemExpectedTypeDef",
    {
        "Value": ClientUpdateItemExpectedValueTypeDef,
        "Exists": bool,
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
        "AttributeValueList": List[ClientUpdateItemExpectedAttributeValueListTypeDef],
    },
    total=False,
)

ClientUpdateItemExpressionAttributeValuesTypeDef = TypedDict(
    "ClientUpdateItemExpressionAttributeValuesTypeDef",
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

ClientUpdateItemKeyTypeDef = TypedDict(
    "ClientUpdateItemKeyTypeDef",
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

ClientUpdateItemResponseAttributesTypeDef = TypedDict(
    "ClientUpdateItemResponseAttributesTypeDef",
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

ClientUpdateItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientUpdateItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientUpdateItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientUpdateItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientUpdateItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "ClientUpdateItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ClientUpdateItemResponseConsumedCapacityTypeDef = TypedDict(
    "ClientUpdateItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ClientUpdateItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ClientUpdateItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ClientUpdateItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientUpdateItemResponseItemCollectionMetricsItemCollectionKeyTypeDef = TypedDict(
    "ClientUpdateItemResponseItemCollectionMetricsItemCollectionKeyTypeDef",
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

ClientUpdateItemResponseItemCollectionMetricsTypeDef = TypedDict(
    "ClientUpdateItemResponseItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str, ClientUpdateItemResponseItemCollectionMetricsItemCollectionKeyTypeDef
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ClientUpdateItemResponseTypeDef = TypedDict(
    "ClientUpdateItemResponseTypeDef",
    {
        "Attributes": Dict[str, ClientUpdateItemResponseAttributesTypeDef],
        "ConsumedCapacity": ClientUpdateItemResponseConsumedCapacityTypeDef,
        "ItemCollectionMetrics": ClientUpdateItemResponseItemCollectionMetricsTypeDef,
    },
    total=False,
)

_RequiredClientUpdateTableAttributeDefinitionsTypeDef = TypedDict(
    "_RequiredClientUpdateTableAttributeDefinitionsTypeDef", {"AttributeName": str}
)
_OptionalClientUpdateTableAttributeDefinitionsTypeDef = TypedDict(
    "_OptionalClientUpdateTableAttributeDefinitionsTypeDef",
    {"AttributeType": Literal["S", "N", "B"]},
    total=False,
)


class ClientUpdateTableAttributeDefinitionsTypeDef(
    _RequiredClientUpdateTableAttributeDefinitionsTypeDef,
    _OptionalClientUpdateTableAttributeDefinitionsTypeDef,
):
    pass


ClientUpdateTableGlobalSecondaryIndexUpdatesCreateKeySchemaTypeDef = TypedDict(
    "ClientUpdateTableGlobalSecondaryIndexUpdatesCreateKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientUpdateTableGlobalSecondaryIndexUpdatesCreateProjectionTypeDef = TypedDict(
    "ClientUpdateTableGlobalSecondaryIndexUpdatesCreateProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientUpdateTableGlobalSecondaryIndexUpdatesCreateProvisionedThroughputTypeDef = TypedDict(
    "ClientUpdateTableGlobalSecondaryIndexUpdatesCreateProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

ClientUpdateTableGlobalSecondaryIndexUpdatesCreateTypeDef = TypedDict(
    "ClientUpdateTableGlobalSecondaryIndexUpdatesCreateTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[ClientUpdateTableGlobalSecondaryIndexUpdatesCreateKeySchemaTypeDef],
        "Projection": ClientUpdateTableGlobalSecondaryIndexUpdatesCreateProjectionTypeDef,
        "ProvisionedThroughput": ClientUpdateTableGlobalSecondaryIndexUpdatesCreateProvisionedThroughputTypeDef,
    },
    total=False,
)

ClientUpdateTableGlobalSecondaryIndexUpdatesDeleteTypeDef = TypedDict(
    "ClientUpdateTableGlobalSecondaryIndexUpdatesDeleteTypeDef", {"IndexName": str}, total=False
)

ClientUpdateTableGlobalSecondaryIndexUpdatesUpdateProvisionedThroughputTypeDef = TypedDict(
    "ClientUpdateTableGlobalSecondaryIndexUpdatesUpdateProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

_RequiredClientUpdateTableGlobalSecondaryIndexUpdatesUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateTableGlobalSecondaryIndexUpdatesUpdateTypeDef", {"IndexName": str}
)
_OptionalClientUpdateTableGlobalSecondaryIndexUpdatesUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateTableGlobalSecondaryIndexUpdatesUpdateTypeDef",
    {
        "ProvisionedThroughput": ClientUpdateTableGlobalSecondaryIndexUpdatesUpdateProvisionedThroughputTypeDef
    },
    total=False,
)


class ClientUpdateTableGlobalSecondaryIndexUpdatesUpdateTypeDef(
    _RequiredClientUpdateTableGlobalSecondaryIndexUpdatesUpdateTypeDef,
    _OptionalClientUpdateTableGlobalSecondaryIndexUpdatesUpdateTypeDef,
):
    pass


ClientUpdateTableGlobalSecondaryIndexUpdatesTypeDef = TypedDict(
    "ClientUpdateTableGlobalSecondaryIndexUpdatesTypeDef",
    {
        "Update": ClientUpdateTableGlobalSecondaryIndexUpdatesUpdateTypeDef,
        "Create": ClientUpdateTableGlobalSecondaryIndexUpdatesCreateTypeDef,
        "Delete": ClientUpdateTableGlobalSecondaryIndexUpdatesDeleteTypeDef,
    },
    total=False,
)

_RequiredClientUpdateTableProvisionedThroughputTypeDef = TypedDict(
    "_RequiredClientUpdateTableProvisionedThroughputTypeDef", {"ReadCapacityUnits": int}
)
_OptionalClientUpdateTableProvisionedThroughputTypeDef = TypedDict(
    "_OptionalClientUpdateTableProvisionedThroughputTypeDef",
    {"WriteCapacityUnits": int},
    total=False,
)


class ClientUpdateTableProvisionedThroughputTypeDef(
    _RequiredClientUpdateTableProvisionedThroughputTypeDef,
    _OptionalClientUpdateTableProvisionedThroughputTypeDef,
):
    pass


ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesProvisionedWriteCapacityAutoScalingUpdateTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesProvisionedWriteCapacityAutoScalingUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesTypeDef",
    {
        "IndexName": str,
        "ProvisionedWriteCapacityAutoScalingUpdate": ClientUpdateTableReplicaAutoScalingGlobalSecondaryIndexUpdatesProvisionedWriteCapacityAutoScalingUpdateTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": ClientUpdateTableReplicaAutoScalingProvisionedWriteCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesProvisionedReadCapacityAutoScalingUpdateTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesProvisionedReadCapacityAutoScalingUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesTypeDef",
    {
        "IndexName": str,
        "ProvisionedReadCapacityAutoScalingUpdate": ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesProvisionedReadCapacityAutoScalingUpdateTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaProvisionedReadCapacityAutoScalingUpdateTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaProvisionedReadCapacityAutoScalingUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaProvisionedReadCapacityAutoScalingUpdateScalingPolicyUpdateTypeDef,
    },
    total=False,
)

_RequiredClientUpdateTableReplicaAutoScalingReplicaUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateTableReplicaAutoScalingReplicaUpdatesTypeDef", {"RegionName": str}
)
_OptionalClientUpdateTableReplicaAutoScalingReplicaUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateTableReplicaAutoScalingReplicaUpdatesTypeDef",
    {
        "ReplicaGlobalSecondaryIndexUpdates": List[
            ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaGlobalSecondaryIndexUpdatesTypeDef
        ],
        "ReplicaProvisionedReadCapacityAutoScalingUpdate": ClientUpdateTableReplicaAutoScalingReplicaUpdatesReplicaProvisionedReadCapacityAutoScalingUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateTableReplicaAutoScalingReplicaUpdatesTypeDef(
    _RequiredClientUpdateTableReplicaAutoScalingReplicaUpdatesTypeDef,
    _OptionalClientUpdateTableReplicaAutoScalingReplicaUpdatesTypeDef,
):
    pass


ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "ProvisionedReadCapacityAutoScalingSettings": ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedReadCapacityAutoScalingSettingsTypeDef,
        "ProvisionedWriteCapacityAutoScalingSettings": ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesProvisionedWriteCapacityAutoScalingSettingsTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int, "TargetValue": float},
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List[
            ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsScalingPoliciesTypeDef
        ],
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasTypeDef",
    {
        "RegionName": str,
        "GlobalSecondaryIndexes": List[
            ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasGlobalSecondaryIndexesTypeDef
        ],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedReadCapacityAutoScalingSettingsTypeDef,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasReplicaProvisionedWriteCapacityAutoScalingSettingsTypeDef,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionTypeDef",
    {
        "TableName": str,
        "TableStatus": Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ],
        "Replicas": List[
            ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionReplicasTypeDef
        ],
    },
    total=False,
)

ClientUpdateTableReplicaAutoScalingResponseTypeDef = TypedDict(
    "ClientUpdateTableReplicaAutoScalingResponseTypeDef",
    {
        "TableAutoScalingDescription": ClientUpdateTableReplicaAutoScalingResponseTableAutoScalingDescriptionTypeDef
    },
    total=False,
)

ClientUpdateTableReplicaUpdatesCreateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesCreateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientUpdateTableReplicaUpdatesCreateGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesCreateGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientUpdateTableReplicaUpdatesCreateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaUpdatesCreateProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesCreateProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientUpdateTableReplicaUpdatesCreateTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesCreateTypeDef",
    {
        "RegionName": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientUpdateTableReplicaUpdatesCreateProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientUpdateTableReplicaUpdatesCreateGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientUpdateTableReplicaUpdatesDeleteTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesDeleteTypeDef", {"RegionName": str}, total=False
)

ClientUpdateTableReplicaUpdatesUpdateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesUpdateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientUpdateTableReplicaUpdatesUpdateGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesUpdateGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientUpdateTableReplicaUpdatesUpdateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientUpdateTableReplicaUpdatesUpdateProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesUpdateProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientUpdateTableReplicaUpdatesUpdateTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesUpdateTypeDef",
    {
        "RegionName": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientUpdateTableReplicaUpdatesUpdateProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientUpdateTableReplicaUpdatesUpdateGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientUpdateTableReplicaUpdatesTypeDef = TypedDict(
    "ClientUpdateTableReplicaUpdatesTypeDef",
    {
        "Create": ClientUpdateTableReplicaUpdatesCreateTypeDef,
        "Update": ClientUpdateTableReplicaUpdatesUpdateTypeDef,
        "Delete": ClientUpdateTableReplicaUpdatesDeleteTypeDef,
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionArchivalSummaryTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionArchivalSummaryTypeDef",
    {"ArchivalDateTime": datetime, "ArchivalReason": str, "ArchivalBackupArn": str},
    total=False,
)

ClientUpdateTableResponseTableDescriptionAttributeDefinitionsTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionAttributeDefinitionsTypeDef",
    {"AttributeName": str, "AttributeType": Literal["S", "N", "B"]},
    total=False,
)

ClientUpdateTableResponseTableDescriptionBillingModeSummaryTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionBillingModeSummaryTypeDef",
    {
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "Backfilling": bool,
        "ProvisionedThroughput": ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionKeySchemaTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientUpdateTableResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientUpdateTableResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ClientUpdateTableResponseTableDescriptionLocalSecondaryIndexesTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            ClientUpdateTableResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": ClientUpdateTableResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionProvisionedThroughputTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientUpdateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": ClientUpdateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

ClientUpdateTableResponseTableDescriptionReplicasTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionReplicasTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": ClientUpdateTableResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            ClientUpdateTableResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionRestoreSummaryTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionSSEDescriptionTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionSSEDescriptionTypeDef",
    {
        "Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING"],
        "SSEType": Literal["AES256", "KMS"],
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionStreamSpecificationTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientUpdateTableResponseTableDescriptionTypeDef = TypedDict(
    "ClientUpdateTableResponseTableDescriptionTypeDef",
    {
        "AttributeDefinitions": List[
            ClientUpdateTableResponseTableDescriptionAttributeDefinitionsTypeDef
        ],
        "TableName": str,
        "KeySchema": List[ClientUpdateTableResponseTableDescriptionKeySchemaTypeDef],
        "TableStatus": Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ],
        "CreationDateTime": datetime,
        "ProvisionedThroughput": ClientUpdateTableResponseTableDescriptionProvisionedThroughputTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": ClientUpdateTableResponseTableDescriptionBillingModeSummaryTypeDef,
        "LocalSecondaryIndexes": List[
            ClientUpdateTableResponseTableDescriptionLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": List[
            ClientUpdateTableResponseTableDescriptionGlobalSecondaryIndexesTypeDef
        ],
        "StreamSpecification": ClientUpdateTableResponseTableDescriptionStreamSpecificationTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[ClientUpdateTableResponseTableDescriptionReplicasTypeDef],
        "RestoreSummary": ClientUpdateTableResponseTableDescriptionRestoreSummaryTypeDef,
        "SSEDescription": ClientUpdateTableResponseTableDescriptionSSEDescriptionTypeDef,
        "ArchivalSummary": ClientUpdateTableResponseTableDescriptionArchivalSummaryTypeDef,
    },
    total=False,
)

ClientUpdateTableResponseTypeDef = TypedDict(
    "ClientUpdateTableResponseTypeDef",
    {"TableDescription": ClientUpdateTableResponseTableDescriptionTypeDef},
    total=False,
)

ClientUpdateTableSSESpecificationTypeDef = TypedDict(
    "ClientUpdateTableSSESpecificationTypeDef",
    {"Enabled": bool, "SSEType": Literal["AES256", "KMS"], "KMSMasterKeyId": str},
    total=False,
)

ClientUpdateTableStreamSpecificationTypeDef = TypedDict(
    "ClientUpdateTableStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientUpdateTimeToLiveResponseTimeToLiveSpecificationTypeDef = TypedDict(
    "ClientUpdateTimeToLiveResponseTimeToLiveSpecificationTypeDef",
    {"Enabled": bool, "AttributeName": str},
    total=False,
)

ClientUpdateTimeToLiveResponseTypeDef = TypedDict(
    "ClientUpdateTimeToLiveResponseTypeDef",
    {"TimeToLiveSpecification": ClientUpdateTimeToLiveResponseTimeToLiveSpecificationTypeDef},
    total=False,
)

_RequiredClientUpdateTimeToLiveTimeToLiveSpecificationTypeDef = TypedDict(
    "_RequiredClientUpdateTimeToLiveTimeToLiveSpecificationTypeDef", {"Enabled": bool}
)
_OptionalClientUpdateTimeToLiveTimeToLiveSpecificationTypeDef = TypedDict(
    "_OptionalClientUpdateTimeToLiveTimeToLiveSpecificationTypeDef",
    {"AttributeName": str},
    total=False,
)


class ClientUpdateTimeToLiveTimeToLiveSpecificationTypeDef(
    _RequiredClientUpdateTimeToLiveTimeToLiveSpecificationTypeDef,
    _OptionalClientUpdateTimeToLiveTimeToLiveSpecificationTypeDef,
):
    pass


ListBackupsPaginatePaginationConfigTypeDef = TypedDict(
    "ListBackupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListBackupsPaginateResponseBackupSummariesTypeDef = TypedDict(
    "ListBackupsPaginateResponseBackupSummariesTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "BackupArn": str,
        "BackupName": str,
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
        "BackupStatus": Literal["CREATING", "DELETED", "AVAILABLE"],
        "BackupType": Literal["USER", "SYSTEM", "AWS_BACKUP"],
        "BackupSizeBytes": int,
    },
    total=False,
)

ListBackupsPaginateResponseTypeDef = TypedDict(
    "ListBackupsPaginateResponseTypeDef",
    {"BackupSummaries": List[ListBackupsPaginateResponseBackupSummariesTypeDef], "NextToken": str},
    total=False,
)

ListTablesPaginatePaginationConfigTypeDef = TypedDict(
    "ListTablesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTablesPaginateResponseTypeDef = TypedDict(
    "ListTablesPaginateResponseTypeDef", {"TableNames": List[str], "NextToken": str}, total=False
)

ListTagsOfResourcePaginatePaginationConfigTypeDef = TypedDict(
    "ListTagsOfResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListTagsOfResourcePaginateResponseTagsTypeDef = TypedDict(
    "ListTagsOfResourcePaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ListTagsOfResourcePaginateResponseTypeDef = TypedDict(
    "ListTagsOfResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsOfResourcePaginateResponseTagsTypeDef]},
    total=False,
)

QueryPaginateExpressionAttributeValuesTypeDef = TypedDict(
    "QueryPaginateExpressionAttributeValuesTypeDef",
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

QueryPaginateKeyConditionsAttributeValueListTypeDef = TypedDict(
    "QueryPaginateKeyConditionsAttributeValueListTypeDef",
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

QueryPaginateKeyConditionsTypeDef = TypedDict(
    "QueryPaginateKeyConditionsTypeDef",
    {
        "AttributeValueList": List[QueryPaginateKeyConditionsAttributeValueListTypeDef],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
    },
    total=False,
)

QueryPaginatePaginationConfigTypeDef = TypedDict(
    "QueryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

QueryPaginateQueryFilterAttributeValueListTypeDef = TypedDict(
    "QueryPaginateQueryFilterAttributeValueListTypeDef",
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

QueryPaginateQueryFilterTypeDef = TypedDict(
    "QueryPaginateQueryFilterTypeDef",
    {
        "AttributeValueList": List[QueryPaginateQueryFilterAttributeValueListTypeDef],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
    },
    total=False,
)

QueryPaginateResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "QueryPaginateResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

QueryPaginateResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "QueryPaginateResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

QueryPaginateResponseConsumedCapacityTableTypeDef = TypedDict(
    "QueryPaginateResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

QueryPaginateResponseConsumedCapacityTypeDef = TypedDict(
    "QueryPaginateResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": QueryPaginateResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, QueryPaginateResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, QueryPaginateResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

QueryPaginateResponseItemsTypeDef = TypedDict(
    "QueryPaginateResponseItemsTypeDef",
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

QueryPaginateResponseTypeDef = TypedDict(
    "QueryPaginateResponseTypeDef",
    {
        "Items": List[Dict[str, QueryPaginateResponseItemsTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "ConsumedCapacity": QueryPaginateResponseConsumedCapacityTypeDef,
        "NextToken": str,
    },
    total=False,
)

ScanPaginateExpressionAttributeValuesTypeDef = TypedDict(
    "ScanPaginateExpressionAttributeValuesTypeDef",
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

ScanPaginatePaginationConfigTypeDef = TypedDict(
    "ScanPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ScanPaginateResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ScanPaginateResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ScanPaginateResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ScanPaginateResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ScanPaginateResponseConsumedCapacityTableTypeDef = TypedDict(
    "ScanPaginateResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ScanPaginateResponseConsumedCapacityTypeDef = TypedDict(
    "ScanPaginateResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ScanPaginateResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ScanPaginateResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ScanPaginateResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ScanPaginateResponseItemsTypeDef = TypedDict(
    "ScanPaginateResponseItemsTypeDef",
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

ScanPaginateResponseTypeDef = TypedDict(
    "ScanPaginateResponseTypeDef",
    {
        "Items": List[Dict[str, ScanPaginateResponseItemsTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "ConsumedCapacity": ScanPaginateResponseConsumedCapacityTypeDef,
        "NextToken": str,
    },
    total=False,
)

ScanPaginateScanFilterAttributeValueListTypeDef = TypedDict(
    "ScanPaginateScanFilterAttributeValueListTypeDef",
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

ScanPaginateScanFilterTypeDef = TypedDict(
    "ScanPaginateScanFilterTypeDef",
    {
        "AttributeValueList": List[ScanPaginateScanFilterAttributeValueListTypeDef],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
    },
    total=False,
)

ServiceResourceBatchGetItemRequestItemsKeysTypeDef = TypedDict(
    "ServiceResourceBatchGetItemRequestItemsKeysTypeDef",
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

ServiceResourceBatchGetItemRequestItemsTypeDef = TypedDict(
    "ServiceResourceBatchGetItemRequestItemsTypeDef",
    {
        "Keys": List[Dict[str, ServiceResourceBatchGetItemRequestItemsKeysTypeDef]],
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)

ServiceResourceBatchGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ServiceResourceBatchGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ServiceResourceBatchGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ServiceResourceBatchGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ServiceResourceBatchGetItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "ServiceResourceBatchGetItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ServiceResourceBatchGetItemResponseConsumedCapacityTypeDef = TypedDict(
    "ServiceResourceBatchGetItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ServiceResourceBatchGetItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ServiceResourceBatchGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ServiceResourceBatchGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ServiceResourceBatchGetItemResponseResponsesTypeDef = TypedDict(
    "ServiceResourceBatchGetItemResponseResponsesTypeDef",
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

ServiceResourceBatchGetItemResponseUnprocessedKeysKeysTypeDef = TypedDict(
    "ServiceResourceBatchGetItemResponseUnprocessedKeysKeysTypeDef",
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

ServiceResourceBatchGetItemResponseUnprocessedKeysTypeDef = TypedDict(
    "ServiceResourceBatchGetItemResponseUnprocessedKeysTypeDef",
    {
        "Keys": List[Dict[str, ServiceResourceBatchGetItemResponseUnprocessedKeysKeysTypeDef]],
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)

ServiceResourceBatchGetItemResponseTypeDef = TypedDict(
    "ServiceResourceBatchGetItemResponseTypeDef",
    {
        "Responses": Dict[
            str, List[Dict[str, ServiceResourceBatchGetItemResponseResponsesTypeDef]]
        ],
        "UnprocessedKeys": Dict[str, ServiceResourceBatchGetItemResponseUnprocessedKeysTypeDef],
        "ConsumedCapacity": List[ServiceResourceBatchGetItemResponseConsumedCapacityTypeDef],
    },
    total=False,
)

ServiceResourceBatchWriteItemRequestItemsDeleteRequestKeyTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemRequestItemsDeleteRequestKeyTypeDef",
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

ServiceResourceBatchWriteItemRequestItemsDeleteRequestTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemRequestItemsDeleteRequestTypeDef",
    {"Key": Dict[str, ServiceResourceBatchWriteItemRequestItemsDeleteRequestKeyTypeDef]},
    total=False,
)

ServiceResourceBatchWriteItemRequestItemsPutRequestItemTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemRequestItemsPutRequestItemTypeDef",
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

ServiceResourceBatchWriteItemRequestItemsPutRequestTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemRequestItemsPutRequestTypeDef",
    {"Item": Dict[str, ServiceResourceBatchWriteItemRequestItemsPutRequestItemTypeDef]},
    total=False,
)

ServiceResourceBatchWriteItemRequestItemsTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemRequestItemsTypeDef",
    {
        "PutRequest": ServiceResourceBatchWriteItemRequestItemsPutRequestTypeDef,
        "DeleteRequest": ServiceResourceBatchWriteItemRequestItemsDeleteRequestTypeDef,
    },
    total=False,
)

ServiceResourceBatchWriteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ServiceResourceBatchWriteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ServiceResourceBatchWriteItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

ServiceResourceBatchWriteItemResponseConsumedCapacityTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": ServiceResourceBatchWriteItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, ServiceResourceBatchWriteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, ServiceResourceBatchWriteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

ServiceResourceBatchWriteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef",
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

ServiceResourceBatchWriteItemResponseItemCollectionMetricsTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str, ServiceResourceBatchWriteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ServiceResourceBatchWriteItemResponseUnprocessedItemsDeleteRequestKeyTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseUnprocessedItemsDeleteRequestKeyTypeDef",
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

ServiceResourceBatchWriteItemResponseUnprocessedItemsDeleteRequestTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseUnprocessedItemsDeleteRequestTypeDef",
    {
        "Key": Dict[
            str, ServiceResourceBatchWriteItemResponseUnprocessedItemsDeleteRequestKeyTypeDef
        ]
    },
    total=False,
)

ServiceResourceBatchWriteItemResponseUnprocessedItemsPutRequestItemTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseUnprocessedItemsPutRequestItemTypeDef",
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

ServiceResourceBatchWriteItemResponseUnprocessedItemsPutRequestTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseUnprocessedItemsPutRequestTypeDef",
    {"Item": Dict[str, ServiceResourceBatchWriteItemResponseUnprocessedItemsPutRequestItemTypeDef]},
    total=False,
)

ServiceResourceBatchWriteItemResponseUnprocessedItemsTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseUnprocessedItemsTypeDef",
    {
        "PutRequest": ServiceResourceBatchWriteItemResponseUnprocessedItemsPutRequestTypeDef,
        "DeleteRequest": ServiceResourceBatchWriteItemResponseUnprocessedItemsDeleteRequestTypeDef,
    },
    total=False,
)

ServiceResourceBatchWriteItemResponseTypeDef = TypedDict(
    "ServiceResourceBatchWriteItemResponseTypeDef",
    {
        "UnprocessedItems": Dict[
            str, List[ServiceResourceBatchWriteItemResponseUnprocessedItemsTypeDef]
        ],
        "ItemCollectionMetrics": Dict[
            str, List[ServiceResourceBatchWriteItemResponseItemCollectionMetricsTypeDef]
        ],
        "ConsumedCapacity": List[ServiceResourceBatchWriteItemResponseConsumedCapacityTypeDef],
    },
    total=False,
)

_RequiredServiceResourceCreateTableAttributeDefinitionsTypeDef = TypedDict(
    "_RequiredServiceResourceCreateTableAttributeDefinitionsTypeDef", {"AttributeName": str}
)
_OptionalServiceResourceCreateTableAttributeDefinitionsTypeDef = TypedDict(
    "_OptionalServiceResourceCreateTableAttributeDefinitionsTypeDef",
    {"AttributeType": Literal["S", "N", "B"]},
    total=False,
)


class ServiceResourceCreateTableAttributeDefinitionsTypeDef(
    _RequiredServiceResourceCreateTableAttributeDefinitionsTypeDef,
    _OptionalServiceResourceCreateTableAttributeDefinitionsTypeDef,
):
    pass


ServiceResourceCreateTableGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ServiceResourceCreateTableGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ServiceResourceCreateTableGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ServiceResourceCreateTableGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ServiceResourceCreateTableGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "ServiceResourceCreateTableGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

ServiceResourceCreateTableGlobalSecondaryIndexesTypeDef = TypedDict(
    "ServiceResourceCreateTableGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[ServiceResourceCreateTableGlobalSecondaryIndexesKeySchemaTypeDef],
        "Projection": ServiceResourceCreateTableGlobalSecondaryIndexesProjectionTypeDef,
        "ProvisionedThroughput": ServiceResourceCreateTableGlobalSecondaryIndexesProvisionedThroughputTypeDef,
    },
    total=False,
)

ServiceResourceCreateTableKeySchemaTypeDef = TypedDict(
    "ServiceResourceCreateTableKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ServiceResourceCreateTableLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "ServiceResourceCreateTableLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ServiceResourceCreateTableLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "ServiceResourceCreateTableLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

ServiceResourceCreateTableLocalSecondaryIndexesTypeDef = TypedDict(
    "ServiceResourceCreateTableLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[ServiceResourceCreateTableLocalSecondaryIndexesKeySchemaTypeDef],
        "Projection": ServiceResourceCreateTableLocalSecondaryIndexesProjectionTypeDef,
    },
    total=False,
)

_RequiredServiceResourceCreateTableProvisionedThroughputTypeDef = TypedDict(
    "_RequiredServiceResourceCreateTableProvisionedThroughputTypeDef", {"ReadCapacityUnits": int}
)
_OptionalServiceResourceCreateTableProvisionedThroughputTypeDef = TypedDict(
    "_OptionalServiceResourceCreateTableProvisionedThroughputTypeDef",
    {"WriteCapacityUnits": int},
    total=False,
)


class ServiceResourceCreateTableProvisionedThroughputTypeDef(
    _RequiredServiceResourceCreateTableProvisionedThroughputTypeDef,
    _OptionalServiceResourceCreateTableProvisionedThroughputTypeDef,
):
    pass


ServiceResourceCreateTableSSESpecificationTypeDef = TypedDict(
    "ServiceResourceCreateTableSSESpecificationTypeDef",
    {"Enabled": bool, "SSEType": Literal["AES256", "KMS"], "KMSMasterKeyId": str},
    total=False,
)

ServiceResourceCreateTableStreamSpecificationTypeDef = TypedDict(
    "ServiceResourceCreateTableStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

_RequiredServiceResourceCreateTableTagsTypeDef = TypedDict(
    "_RequiredServiceResourceCreateTableTagsTypeDef", {"Key": str}
)
_OptionalServiceResourceCreateTableTagsTypeDef = TypedDict(
    "_OptionalServiceResourceCreateTableTagsTypeDef", {"Value": str}, total=False
)


class ServiceResourceCreateTableTagsTypeDef(
    _RequiredServiceResourceCreateTableTagsTypeDef, _OptionalServiceResourceCreateTableTagsTypeDef
):
    pass


TableDeleteItemExpectedAttributeValueListTypeDef = TypedDict(
    "TableDeleteItemExpectedAttributeValueListTypeDef",
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

TableDeleteItemExpectedValueTypeDef = TypedDict(
    "TableDeleteItemExpectedValueTypeDef",
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

TableDeleteItemExpectedTypeDef = TypedDict(
    "TableDeleteItemExpectedTypeDef",
    {
        "Value": TableDeleteItemExpectedValueTypeDef,
        "Exists": bool,
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
        "AttributeValueList": List[TableDeleteItemExpectedAttributeValueListTypeDef],
    },
    total=False,
)

TableDeleteItemExpressionAttributeValuesTypeDef = TypedDict(
    "TableDeleteItemExpressionAttributeValuesTypeDef",
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

TableDeleteItemKeyTypeDef = TypedDict(
    "TableDeleteItemKeyTypeDef",
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

TableDeleteItemResponseAttributesTypeDef = TypedDict(
    "TableDeleteItemResponseAttributesTypeDef",
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

TableDeleteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "TableDeleteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableDeleteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "TableDeleteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableDeleteItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "TableDeleteItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableDeleteItemResponseConsumedCapacityTypeDef = TypedDict(
    "TableDeleteItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": TableDeleteItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, TableDeleteItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, TableDeleteItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

TableDeleteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef = TypedDict(
    "TableDeleteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef",
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

TableDeleteItemResponseItemCollectionMetricsTypeDef = TypedDict(
    "TableDeleteItemResponseItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str, TableDeleteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

TableDeleteItemResponseTypeDef = TypedDict(
    "TableDeleteItemResponseTypeDef",
    {
        "Attributes": Dict[str, TableDeleteItemResponseAttributesTypeDef],
        "ConsumedCapacity": TableDeleteItemResponseConsumedCapacityTypeDef,
        "ItemCollectionMetrics": TableDeleteItemResponseItemCollectionMetricsTypeDef,
    },
    total=False,
)

TableDeleteResponseTableDescriptionArchivalSummaryTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionArchivalSummaryTypeDef",
    {"ArchivalDateTime": datetime, "ArchivalReason": str, "ArchivalBackupArn": str},
    total=False,
)

TableDeleteResponseTableDescriptionAttributeDefinitionsTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionAttributeDefinitionsTypeDef",
    {"AttributeName": str, "AttributeType": Literal["S", "N", "B"]},
    total=False,
)

TableDeleteResponseTableDescriptionBillingModeSummaryTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionBillingModeSummaryTypeDef",
    {
        "BillingMode": Literal["PROVISIONED", "PAY_PER_REQUEST"],
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

TableDeleteResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

TableDeleteResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

TableDeleteResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

TableDeleteResponseTableDescriptionGlobalSecondaryIndexesTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[
            TableDeleteResponseTableDescriptionGlobalSecondaryIndexesKeySchemaTypeDef
        ],
        "Projection": TableDeleteResponseTableDescriptionGlobalSecondaryIndexesProjectionTypeDef,
        "IndexStatus": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"],
        "Backfilling": bool,
        "ProvisionedThroughput": TableDeleteResponseTableDescriptionGlobalSecondaryIndexesProvisionedThroughputTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

TableDeleteResponseTableDescriptionKeySchemaTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

TableDeleteResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

TableDeleteResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

TableDeleteResponseTableDescriptionLocalSecondaryIndexesTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionLocalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[TableDeleteResponseTableDescriptionLocalSecondaryIndexesKeySchemaTypeDef],
        "Projection": TableDeleteResponseTableDescriptionLocalSecondaryIndexesProjectionTypeDef,
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

TableDeleteResponseTableDescriptionProvisionedThroughputTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionProvisionedThroughputTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

TableDeleteResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

TableDeleteResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": TableDeleteResponseTableDescriptionReplicasGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

TableDeleteResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

TableDeleteResponseTableDescriptionReplicasTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionReplicasTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": Literal["CREATING", "CREATION_FAILED", "UPDATING", "DELETING", "ACTIVE"],
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": TableDeleteResponseTableDescriptionReplicasProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            TableDeleteResponseTableDescriptionReplicasGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

TableDeleteResponseTableDescriptionRestoreSummaryTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
    total=False,
)

TableDeleteResponseTableDescriptionSSEDescriptionTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionSSEDescriptionTypeDef",
    {
        "Status": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED", "UPDATING"],
        "SSEType": Literal["AES256", "KMS"],
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

TableDeleteResponseTableDescriptionStreamSpecificationTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

TableDeleteResponseTableDescriptionTypeDef = TypedDict(
    "TableDeleteResponseTableDescriptionTypeDef",
    {
        "AttributeDefinitions": List[
            TableDeleteResponseTableDescriptionAttributeDefinitionsTypeDef
        ],
        "TableName": str,
        "KeySchema": List[TableDeleteResponseTableDescriptionKeySchemaTypeDef],
        "TableStatus": Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ],
        "CreationDateTime": datetime,
        "ProvisionedThroughput": TableDeleteResponseTableDescriptionProvisionedThroughputTypeDef,
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": TableDeleteResponseTableDescriptionBillingModeSummaryTypeDef,
        "LocalSecondaryIndexes": List[
            TableDeleteResponseTableDescriptionLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": List[
            TableDeleteResponseTableDescriptionGlobalSecondaryIndexesTypeDef
        ],
        "StreamSpecification": TableDeleteResponseTableDescriptionStreamSpecificationTypeDef,
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List[TableDeleteResponseTableDescriptionReplicasTypeDef],
        "RestoreSummary": TableDeleteResponseTableDescriptionRestoreSummaryTypeDef,
        "SSEDescription": TableDeleteResponseTableDescriptionSSEDescriptionTypeDef,
        "ArchivalSummary": TableDeleteResponseTableDescriptionArchivalSummaryTypeDef,
    },
    total=False,
)

TableDeleteResponseTypeDef = TypedDict(
    "TableDeleteResponseTypeDef",
    {"TableDescription": TableDeleteResponseTableDescriptionTypeDef},
    total=False,
)

TableExistsWaitWaiterConfigTypeDef = TypedDict(
    "TableExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

TableGetItemKeyTypeDef = TypedDict(
    "TableGetItemKeyTypeDef",
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

TableGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "TableGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "TableGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableGetItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "TableGetItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableGetItemResponseConsumedCapacityTypeDef = TypedDict(
    "TableGetItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": TableGetItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, TableGetItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, TableGetItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

TableGetItemResponseItemTypeDef = TypedDict(
    "TableGetItemResponseItemTypeDef",
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

TableGetItemResponseTypeDef = TypedDict(
    "TableGetItemResponseTypeDef",
    {
        "Item": Dict[str, TableGetItemResponseItemTypeDef],
        "ConsumedCapacity": TableGetItemResponseConsumedCapacityTypeDef,
    },
    total=False,
)

TableNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "TableNotExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

TablePutItemExpectedAttributeValueListTypeDef = TypedDict(
    "TablePutItemExpectedAttributeValueListTypeDef",
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

TablePutItemExpectedValueTypeDef = TypedDict(
    "TablePutItemExpectedValueTypeDef",
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

TablePutItemExpectedTypeDef = TypedDict(
    "TablePutItemExpectedTypeDef",
    {
        "Value": TablePutItemExpectedValueTypeDef,
        "Exists": bool,
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
        "AttributeValueList": List[TablePutItemExpectedAttributeValueListTypeDef],
    },
    total=False,
)

TablePutItemExpressionAttributeValuesTypeDef = TypedDict(
    "TablePutItemExpressionAttributeValuesTypeDef",
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

TablePutItemItemTypeDef = TypedDict(
    "TablePutItemItemTypeDef",
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

TablePutItemResponseAttributesTypeDef = TypedDict(
    "TablePutItemResponseAttributesTypeDef",
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

TablePutItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "TablePutItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TablePutItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "TablePutItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TablePutItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "TablePutItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TablePutItemResponseConsumedCapacityTypeDef = TypedDict(
    "TablePutItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": TablePutItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, TablePutItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, TablePutItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

TablePutItemResponseItemCollectionMetricsItemCollectionKeyTypeDef = TypedDict(
    "TablePutItemResponseItemCollectionMetricsItemCollectionKeyTypeDef",
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

TablePutItemResponseItemCollectionMetricsTypeDef = TypedDict(
    "TablePutItemResponseItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str, TablePutItemResponseItemCollectionMetricsItemCollectionKeyTypeDef
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

TablePutItemResponseTypeDef = TypedDict(
    "TablePutItemResponseTypeDef",
    {
        "Attributes": Dict[str, TablePutItemResponseAttributesTypeDef],
        "ConsumedCapacity": TablePutItemResponseConsumedCapacityTypeDef,
        "ItemCollectionMetrics": TablePutItemResponseItemCollectionMetricsTypeDef,
    },
    total=False,
)

TableQueryExclusiveStartKeyTypeDef = TypedDict(
    "TableQueryExclusiveStartKeyTypeDef",
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

TableQueryExpressionAttributeValuesTypeDef = TypedDict(
    "TableQueryExpressionAttributeValuesTypeDef",
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

TableQueryKeyConditionsAttributeValueListTypeDef = TypedDict(
    "TableQueryKeyConditionsAttributeValueListTypeDef",
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

TableQueryKeyConditionsTypeDef = TypedDict(
    "TableQueryKeyConditionsTypeDef",
    {
        "AttributeValueList": List[TableQueryKeyConditionsAttributeValueListTypeDef],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
    },
    total=False,
)

TableQueryQueryFilterAttributeValueListTypeDef = TypedDict(
    "TableQueryQueryFilterAttributeValueListTypeDef",
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

TableQueryQueryFilterTypeDef = TypedDict(
    "TableQueryQueryFilterTypeDef",
    {
        "AttributeValueList": List[TableQueryQueryFilterAttributeValueListTypeDef],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
    },
    total=False,
)

TableQueryResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "TableQueryResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableQueryResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "TableQueryResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableQueryResponseConsumedCapacityTableTypeDef = TypedDict(
    "TableQueryResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableQueryResponseConsumedCapacityTypeDef = TypedDict(
    "TableQueryResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": TableQueryResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, TableQueryResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, TableQueryResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

TableQueryResponseItemsTypeDef = TypedDict(
    "TableQueryResponseItemsTypeDef",
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

TableQueryResponseLastEvaluatedKeyTypeDef = TypedDict(
    "TableQueryResponseLastEvaluatedKeyTypeDef",
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

TableQueryResponseTypeDef = TypedDict(
    "TableQueryResponseTypeDef",
    {
        "Items": List[Dict[str, TableQueryResponseItemsTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, TableQueryResponseLastEvaluatedKeyTypeDef],
        "ConsumedCapacity": TableQueryResponseConsumedCapacityTypeDef,
    },
    total=False,
)

TableScanExclusiveStartKeyTypeDef = TypedDict(
    "TableScanExclusiveStartKeyTypeDef",
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

TableScanExpressionAttributeValuesTypeDef = TypedDict(
    "TableScanExpressionAttributeValuesTypeDef",
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

TableScanResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "TableScanResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableScanResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "TableScanResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableScanResponseConsumedCapacityTableTypeDef = TypedDict(
    "TableScanResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableScanResponseConsumedCapacityTypeDef = TypedDict(
    "TableScanResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": TableScanResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, TableScanResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, TableScanResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

TableScanResponseItemsTypeDef = TypedDict(
    "TableScanResponseItemsTypeDef",
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

TableScanResponseLastEvaluatedKeyTypeDef = TypedDict(
    "TableScanResponseLastEvaluatedKeyTypeDef",
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

TableScanResponseTypeDef = TypedDict(
    "TableScanResponseTypeDef",
    {
        "Items": List[Dict[str, TableScanResponseItemsTypeDef]],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[str, TableScanResponseLastEvaluatedKeyTypeDef],
        "ConsumedCapacity": TableScanResponseConsumedCapacityTypeDef,
    },
    total=False,
)

TableScanScanFilterAttributeValueListTypeDef = TypedDict(
    "TableScanScanFilterAttributeValueListTypeDef",
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

TableScanScanFilterTypeDef = TypedDict(
    "TableScanScanFilterTypeDef",
    {
        "AttributeValueList": List[TableScanScanFilterAttributeValueListTypeDef],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
    },
    total=False,
)

_RequiredTableUpdateAttributeDefinitionsTypeDef = TypedDict(
    "_RequiredTableUpdateAttributeDefinitionsTypeDef", {"AttributeName": str}
)
_OptionalTableUpdateAttributeDefinitionsTypeDef = TypedDict(
    "_OptionalTableUpdateAttributeDefinitionsTypeDef",
    {"AttributeType": Literal["S", "N", "B"]},
    total=False,
)


class TableUpdateAttributeDefinitionsTypeDef(
    _RequiredTableUpdateAttributeDefinitionsTypeDef, _OptionalTableUpdateAttributeDefinitionsTypeDef
):
    pass


TableUpdateGlobalSecondaryIndexUpdatesCreateKeySchemaTypeDef = TypedDict(
    "TableUpdateGlobalSecondaryIndexUpdatesCreateKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

TableUpdateGlobalSecondaryIndexUpdatesCreateProjectionTypeDef = TypedDict(
    "TableUpdateGlobalSecondaryIndexUpdatesCreateProjectionTypeDef",
    {"ProjectionType": Literal["ALL", "KEYS_ONLY", "INCLUDE"], "NonKeyAttributes": List[str]},
    total=False,
)

TableUpdateGlobalSecondaryIndexUpdatesCreateProvisionedThroughputTypeDef = TypedDict(
    "TableUpdateGlobalSecondaryIndexUpdatesCreateProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

TableUpdateGlobalSecondaryIndexUpdatesCreateTypeDef = TypedDict(
    "TableUpdateGlobalSecondaryIndexUpdatesCreateTypeDef",
    {
        "IndexName": str,
        "KeySchema": List[TableUpdateGlobalSecondaryIndexUpdatesCreateKeySchemaTypeDef],
        "Projection": TableUpdateGlobalSecondaryIndexUpdatesCreateProjectionTypeDef,
        "ProvisionedThroughput": TableUpdateGlobalSecondaryIndexUpdatesCreateProvisionedThroughputTypeDef,
    },
    total=False,
)

TableUpdateGlobalSecondaryIndexUpdatesDeleteTypeDef = TypedDict(
    "TableUpdateGlobalSecondaryIndexUpdatesDeleteTypeDef", {"IndexName": str}, total=False
)

TableUpdateGlobalSecondaryIndexUpdatesUpdateProvisionedThroughputTypeDef = TypedDict(
    "TableUpdateGlobalSecondaryIndexUpdatesUpdateProvisionedThroughputTypeDef",
    {"ReadCapacityUnits": int, "WriteCapacityUnits": int},
    total=False,
)

_RequiredTableUpdateGlobalSecondaryIndexUpdatesUpdateTypeDef = TypedDict(
    "_RequiredTableUpdateGlobalSecondaryIndexUpdatesUpdateTypeDef", {"IndexName": str}
)
_OptionalTableUpdateGlobalSecondaryIndexUpdatesUpdateTypeDef = TypedDict(
    "_OptionalTableUpdateGlobalSecondaryIndexUpdatesUpdateTypeDef",
    {
        "ProvisionedThroughput": TableUpdateGlobalSecondaryIndexUpdatesUpdateProvisionedThroughputTypeDef
    },
    total=False,
)


class TableUpdateGlobalSecondaryIndexUpdatesUpdateTypeDef(
    _RequiredTableUpdateGlobalSecondaryIndexUpdatesUpdateTypeDef,
    _OptionalTableUpdateGlobalSecondaryIndexUpdatesUpdateTypeDef,
):
    pass


TableUpdateGlobalSecondaryIndexUpdatesTypeDef = TypedDict(
    "TableUpdateGlobalSecondaryIndexUpdatesTypeDef",
    {
        "Update": TableUpdateGlobalSecondaryIndexUpdatesUpdateTypeDef,
        "Create": TableUpdateGlobalSecondaryIndexUpdatesCreateTypeDef,
        "Delete": TableUpdateGlobalSecondaryIndexUpdatesDeleteTypeDef,
    },
    total=False,
)

TableUpdateItemAttributeUpdatesValueTypeDef = TypedDict(
    "TableUpdateItemAttributeUpdatesValueTypeDef",
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

TableUpdateItemAttributeUpdatesTypeDef = TypedDict(
    "TableUpdateItemAttributeUpdatesTypeDef",
    {
        "Value": TableUpdateItemAttributeUpdatesValueTypeDef,
        "Action": Literal["ADD", "PUT", "DELETE"],
    },
    total=False,
)

TableUpdateItemExpectedAttributeValueListTypeDef = TypedDict(
    "TableUpdateItemExpectedAttributeValueListTypeDef",
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

TableUpdateItemExpectedValueTypeDef = TypedDict(
    "TableUpdateItemExpectedValueTypeDef",
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

TableUpdateItemExpectedTypeDef = TypedDict(
    "TableUpdateItemExpectedTypeDef",
    {
        "Value": TableUpdateItemExpectedValueTypeDef,
        "Exists": bool,
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "IN",
            "LE",
            "LT",
            "GE",
            "GT",
            "BETWEEN",
            "NOT_NULL",
            "NULL",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
        ],
        "AttributeValueList": List[TableUpdateItemExpectedAttributeValueListTypeDef],
    },
    total=False,
)

TableUpdateItemExpressionAttributeValuesTypeDef = TypedDict(
    "TableUpdateItemExpressionAttributeValuesTypeDef",
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

TableUpdateItemKeyTypeDef = TypedDict(
    "TableUpdateItemKeyTypeDef",
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

TableUpdateItemResponseAttributesTypeDef = TypedDict(
    "TableUpdateItemResponseAttributesTypeDef",
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

TableUpdateItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef = TypedDict(
    "TableUpdateItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableUpdateItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef = TypedDict(
    "TableUpdateItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableUpdateItemResponseConsumedCapacityTableTypeDef = TypedDict(
    "TableUpdateItemResponseConsumedCapacityTableTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

TableUpdateItemResponseConsumedCapacityTypeDef = TypedDict(
    "TableUpdateItemResponseConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": TableUpdateItemResponseConsumedCapacityTableTypeDef,
        "LocalSecondaryIndexes": Dict[
            str, TableUpdateItemResponseConsumedCapacityLocalSecondaryIndexesTypeDef
        ],
        "GlobalSecondaryIndexes": Dict[
            str, TableUpdateItemResponseConsumedCapacityGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

TableUpdateItemResponseItemCollectionMetricsItemCollectionKeyTypeDef = TypedDict(
    "TableUpdateItemResponseItemCollectionMetricsItemCollectionKeyTypeDef",
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

TableUpdateItemResponseItemCollectionMetricsTypeDef = TypedDict(
    "TableUpdateItemResponseItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str, TableUpdateItemResponseItemCollectionMetricsItemCollectionKeyTypeDef
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

TableUpdateItemResponseTypeDef = TypedDict(
    "TableUpdateItemResponseTypeDef",
    {
        "Attributes": Dict[str, TableUpdateItemResponseAttributesTypeDef],
        "ConsumedCapacity": TableUpdateItemResponseConsumedCapacityTypeDef,
        "ItemCollectionMetrics": TableUpdateItemResponseItemCollectionMetricsTypeDef,
    },
    total=False,
)

_RequiredTableUpdateProvisionedThroughputTypeDef = TypedDict(
    "_RequiredTableUpdateProvisionedThroughputTypeDef", {"ReadCapacityUnits": int}
)
_OptionalTableUpdateProvisionedThroughputTypeDef = TypedDict(
    "_OptionalTableUpdateProvisionedThroughputTypeDef", {"WriteCapacityUnits": int}, total=False
)


class TableUpdateProvisionedThroughputTypeDef(
    _RequiredTableUpdateProvisionedThroughputTypeDef,
    _OptionalTableUpdateProvisionedThroughputTypeDef,
):
    pass


TableUpdateReplicaUpdatesCreateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesCreateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

TableUpdateReplicaUpdatesCreateGlobalSecondaryIndexesTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesCreateGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": TableUpdateReplicaUpdatesCreateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

TableUpdateReplicaUpdatesCreateProvisionedThroughputOverrideTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesCreateProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

TableUpdateReplicaUpdatesCreateTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesCreateTypeDef",
    {
        "RegionName": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": TableUpdateReplicaUpdatesCreateProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            TableUpdateReplicaUpdatesCreateGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

TableUpdateReplicaUpdatesDeleteTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesDeleteTypeDef", {"RegionName": str}, total=False
)

TableUpdateReplicaUpdatesUpdateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesUpdateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

TableUpdateReplicaUpdatesUpdateGlobalSecondaryIndexesTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesUpdateGlobalSecondaryIndexesTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": TableUpdateReplicaUpdatesUpdateGlobalSecondaryIndexesProvisionedThroughputOverrideTypeDef,
    },
    total=False,
)

TableUpdateReplicaUpdatesUpdateProvisionedThroughputOverrideTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesUpdateProvisionedThroughputOverrideTypeDef",
    {"ReadCapacityUnits": int},
    total=False,
)

TableUpdateReplicaUpdatesUpdateTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesUpdateTypeDef",
    {
        "RegionName": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": TableUpdateReplicaUpdatesUpdateProvisionedThroughputOverrideTypeDef,
        "GlobalSecondaryIndexes": List[
            TableUpdateReplicaUpdatesUpdateGlobalSecondaryIndexesTypeDef
        ],
    },
    total=False,
)

TableUpdateReplicaUpdatesTypeDef = TypedDict(
    "TableUpdateReplicaUpdatesTypeDef",
    {
        "Create": TableUpdateReplicaUpdatesCreateTypeDef,
        "Update": TableUpdateReplicaUpdatesUpdateTypeDef,
        "Delete": TableUpdateReplicaUpdatesDeleteTypeDef,
    },
    total=False,
)

TableUpdateSSESpecificationTypeDef = TypedDict(
    "TableUpdateSSESpecificationTypeDef",
    {"Enabled": bool, "SSEType": Literal["AES256", "KMS"], "KMSMasterKeyId": str},
    total=False,
)

TableUpdateStreamSpecificationTypeDef = TypedDict(
    "TableUpdateStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)
