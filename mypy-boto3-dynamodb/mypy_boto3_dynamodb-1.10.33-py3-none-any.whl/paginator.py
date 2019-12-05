"Main interface for dynamodb service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dynamodb.type_defs import (
    ListBackupsPaginatePaginationConfigTypeDef,
    ListBackupsPaginateResponseTypeDef,
    ListTablesPaginatePaginationConfigTypeDef,
    ListTablesPaginateResponseTypeDef,
    ListTagsOfResourcePaginatePaginationConfigTypeDef,
    ListTagsOfResourcePaginateResponseTypeDef,
    QueryPaginateExpressionAttributeValuesTypeDef,
    QueryPaginateKeyConditionsTypeDef,
    QueryPaginatePaginationConfigTypeDef,
    QueryPaginateQueryFilterTypeDef,
    QueryPaginateResponseTypeDef,
    ScanPaginateExpressionAttributeValuesTypeDef,
    ScanPaginatePaginationConfigTypeDef,
    ScanPaginateResponseTypeDef,
    ScanPaginateScanFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListBackupsPaginator",
    "ListTablesPaginator",
    "ListTagsOfResourcePaginator",
    "QueryPaginator",
    "ScanPaginator",
)


class ListBackupsPaginator(Boto3Paginator):
    """
    Paginator for `list_backups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TableName: str = None,
        TimeRangeLowerBound: datetime = None,
        TimeRangeUpperBound: datetime = None,
        BackupType: Literal["USER", "SYSTEM", "AWS_BACKUP", "ALL"] = None,
        PaginationConfig: ListBackupsPaginatePaginationConfigTypeDef = None,
    ) -> ListBackupsPaginateResponseTypeDef:
        """
        [ListBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dynamodb.html#DynamoDB.Paginator.ListBackups.paginate)
        """


class ListTablesPaginator(Boto3Paginator):
    """
    Paginator for `list_tables`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListTablesPaginatePaginationConfigTypeDef = None
    ) -> ListTablesPaginateResponseTypeDef:
        """
        [ListTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dynamodb.html#DynamoDB.Paginator.ListTables.paginate)
        """


class ListTagsOfResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_of_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: ListTagsOfResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsOfResourcePaginateResponseTypeDef:
        """
        [ListTagsOfResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dynamodb.html#DynamoDB.Paginator.ListTagsOfResource.paginate)
        """


class QueryPaginator(Boto3Paginator):
    """
    Paginator for `query`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TableName: str,
        IndexName: str = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        AttributesToGet: List[str] = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, QueryPaginateKeyConditionsTypeDef] = None,
        QueryFilter: Dict[str, QueryPaginateQueryFilterTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ScanIndexForward: bool = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, QueryPaginateExpressionAttributeValuesTypeDef] = None,
        PaginationConfig: QueryPaginatePaginationConfigTypeDef = None,
    ) -> QueryPaginateResponseTypeDef:
        """
        [Query.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dynamodb.html#DynamoDB.Paginator.Query.paginate)
        """


class ScanPaginator(Boto3Paginator):
    """
    Paginator for `scan`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TableName: str,
        IndexName: str = None,
        AttributesToGet: List[str] = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        ScanFilter: Dict[str, ScanPaginateScanFilterTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, ScanPaginateExpressionAttributeValuesTypeDef] = None,
        ConsistentRead: bool = None,
        PaginationConfig: ScanPaginatePaginationConfigTypeDef = None,
    ) -> ScanPaginateResponseTypeDef:
        """
        [Scan.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/dynamodb.html#DynamoDB.Paginator.Scan.paginate)
        """
