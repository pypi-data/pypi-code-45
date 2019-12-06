"Main interface for dynamodb service ServiceResource"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_dynamodb.service_resource as service_resource_scope
from mypy_boto3_dynamodb.type_defs import (
    ServiceResourceBatchGetItemRequestItemsTypeDef,
    ServiceResourceBatchGetItemResponseTypeDef,
    ServiceResourceBatchWriteItemRequestItemsTypeDef,
    ServiceResourceBatchWriteItemResponseTypeDef,
    ServiceResourceCreateTableAttributeDefinitionsTypeDef,
    ServiceResourceCreateTableGlobalSecondaryIndexesTypeDef,
    ServiceResourceCreateTableKeySchemaTypeDef,
    ServiceResourceCreateTableLocalSecondaryIndexesTypeDef,
    ServiceResourceCreateTableProvisionedThroughputTypeDef,
    ServiceResourceCreateTableSSESpecificationTypeDef,
    ServiceResourceCreateTableStreamSpecificationTypeDef,
    ServiceResourceCreateTableTagsTypeDef,
    TableDeleteItemExpectedTypeDef,
    TableDeleteItemExpressionAttributeValuesTypeDef,
    TableDeleteItemKeyTypeDef,
    TableDeleteItemResponseTypeDef,
    TableDeleteResponseTypeDef,
    TableGetItemKeyTypeDef,
    TableGetItemResponseTypeDef,
    TablePutItemExpectedTypeDef,
    TablePutItemExpressionAttributeValuesTypeDef,
    TablePutItemItemTypeDef,
    TablePutItemResponseTypeDef,
    TableQueryExclusiveStartKeyTypeDef,
    TableQueryExpressionAttributeValuesTypeDef,
    TableQueryKeyConditionsTypeDef,
    TableQueryQueryFilterTypeDef,
    TableQueryResponseTypeDef,
    TableScanExclusiveStartKeyTypeDef,
    TableScanExpressionAttributeValuesTypeDef,
    TableScanResponseTypeDef,
    TableScanScanFilterTypeDef,
    TableUpdateAttributeDefinitionsTypeDef,
    TableUpdateGlobalSecondaryIndexUpdatesTypeDef,
    TableUpdateItemAttributeUpdatesTypeDef,
    TableUpdateItemExpectedTypeDef,
    TableUpdateItemExpressionAttributeValuesTypeDef,
    TableUpdateItemKeyTypeDef,
    TableUpdateItemResponseTypeDef,
    TableUpdateProvisionedThroughputTypeDef,
    TableUpdateReplicaUpdatesTypeDef,
    TableUpdateSSESpecificationTypeDef,
    TableUpdateStreamSpecificationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceResource", "Table", "ServiceResourceTablesCollection")


class ServiceResource(Boto3ServiceResource):
    """
    [DynamoDB.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dynamodb.html#DynamoDB.ServiceResource)
    """

    tables: service_resource_scope.ServiceResourceTablesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Table(self, name: str) -> service_resource_scope.Table:
        """
        [ServiceResource.Table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dynamodb.html#DynamoDB.ServiceResource.Table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_item(
        self,
        RequestItems: Dict[str, ServiceResourceBatchGetItemRequestItemsTypeDef],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
    ) -> ServiceResourceBatchGetItemResponseTypeDef:
        """
        [ServiceResource.batch_get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dynamodb.html#DynamoDB.ServiceResource.batch_get_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_write_item(
        self,
        RequestItems: Dict[str, List[ServiceResourceBatchWriteItemRequestItemsTypeDef]],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
    ) -> ServiceResourceBatchWriteItemResponseTypeDef:
        """
        [ServiceResource.batch_write_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dynamodb.html#DynamoDB.ServiceResource.batch_write_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_table(
        self,
        AttributeDefinitions: List[ServiceResourceCreateTableAttributeDefinitionsTypeDef],
        TableName: str,
        KeySchema: List[ServiceResourceCreateTableKeySchemaTypeDef],
        LocalSecondaryIndexes: List[ServiceResourceCreateTableLocalSecondaryIndexesTypeDef] = None,
        GlobalSecondaryIndexes: List[
            ServiceResourceCreateTableGlobalSecondaryIndexesTypeDef
        ] = None,
        BillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        ProvisionedThroughput: ServiceResourceCreateTableProvisionedThroughputTypeDef = None,
        StreamSpecification: ServiceResourceCreateTableStreamSpecificationTypeDef = None,
        SSESpecification: ServiceResourceCreateTableSSESpecificationTypeDef = None,
        Tags: List[ServiceResourceCreateTableTagsTypeDef] = None,
    ) -> service_resource_scope.Table:
        """
        [ServiceResource.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dynamodb.html#DynamoDB.ServiceResource.create_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dynamodb.html#DynamoDB.ServiceResource.get_available_subresources)
        """


class Table(Boto3ServiceResource):
    """
    [Table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dynamodb.html#DynamoDB.ServiceResource.Table)
    """

    attribute_definitions: List[Any]
    table_name: str
    key_schema: List[Any]
    table_status: str
    creation_date_time: datetime
    provisioned_throughput: Dict[str, Any]
    table_size_bytes: int
    item_count: int
    table_arn: str
    table_id: str
    billing_mode_summary: Dict[str, Any]
    local_secondary_indexes: List[Any]
    global_secondary_indexes: List[Any]
    stream_specification: Dict[str, Any]
    latest_stream_label: str
    latest_stream_arn: str
    global_table_version: str
    replicas: List[Any]
    restore_summary: Dict[str, Any]
    sse_description: Dict[str, Any]
    archival_summary: Dict[str, Any]
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_writer(self, overwrite_by_pkeys: List[str] = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> TableDeleteResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_item(
        self,
        Key: Dict[str, TableDeleteItemKeyTypeDef],
        Expected: Dict[str, TableDeleteItemExpectedTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
            str, TableDeleteItemExpressionAttributeValuesTypeDef
        ] = None,
    ) -> TableDeleteItemResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_item(
        self,
        Key: Dict[str, TableGetItemKeyTypeDef],
        AttributesToGet: List[str] = None,
        ConsistentRead: bool = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
    ) -> TableGetItemResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_item(
        self,
        Item: Dict[str, TablePutItemItemTypeDef],
        Expected: Dict[str, TablePutItemExpectedTypeDef] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, TablePutItemExpressionAttributeValuesTypeDef] = None,
    ) -> TablePutItemResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def query(
        self,
        IndexName: str = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, TableQueryKeyConditionsTypeDef] = None,
        QueryFilter: Dict[str, TableQueryQueryFilterTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ScanIndexForward: bool = None,
        ExclusiveStartKey: Dict[str, TableQueryExclusiveStartKeyTypeDef] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, TableQueryExpressionAttributeValuesTypeDef] = None,
    ) -> TableQueryResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def scan(
        self,
        IndexName: str = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        ScanFilter: Dict[str, TableScanScanFilterTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ExclusiveStartKey: Dict[str, TableScanExclusiveStartKeyTypeDef] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, TableScanExpressionAttributeValuesTypeDef] = None,
        ConsistentRead: bool = None,
    ) -> TableScanResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self,
        AttributeDefinitions: List[TableUpdateAttributeDefinitionsTypeDef] = None,
        BillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        ProvisionedThroughput: TableUpdateProvisionedThroughputTypeDef = None,
        GlobalSecondaryIndexUpdates: List[TableUpdateGlobalSecondaryIndexUpdatesTypeDef] = None,
        StreamSpecification: TableUpdateStreamSpecificationTypeDef = None,
        SSESpecification: TableUpdateSSESpecificationTypeDef = None,
        ReplicaUpdates: List[TableUpdateReplicaUpdatesTypeDef] = None,
    ) -> service_resource_scope.Table:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_item(
        self,
        Key: Dict[str, TableUpdateItemKeyTypeDef],
        AttributeUpdates: Dict[str, TableUpdateItemAttributeUpdatesTypeDef] = None,
        Expected: Dict[str, TableUpdateItemExpectedTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        UpdateExpression: str = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
            str, TableUpdateItemExpressionAttributeValuesTypeDef
        ] = None,
    ) -> TableUpdateItemResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_not_exists(self, *args: Any, **kwargs: Any) -> None:
        pass


class ServiceResourceTablesCollection(ResourceCollection):
    """
    [ServiceResource.tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dynamodb.html#DynamoDB.ServiceResource.tables)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Table]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, ExclusiveStartTableName: str = None, Limit: int = None
    ) -> List[service_resource_scope.Table]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Table]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Table]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass
