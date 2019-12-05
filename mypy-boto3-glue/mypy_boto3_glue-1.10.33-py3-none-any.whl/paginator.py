"Main interface for glue service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_glue.type_defs import (
    GetClassifiersPaginatePaginationConfigTypeDef,
    GetClassifiersPaginateResponseTypeDef,
    GetConnectionsPaginateFilterTypeDef,
    GetConnectionsPaginatePaginationConfigTypeDef,
    GetConnectionsPaginateResponseTypeDef,
    GetCrawlerMetricsPaginatePaginationConfigTypeDef,
    GetCrawlerMetricsPaginateResponseTypeDef,
    GetCrawlersPaginatePaginationConfigTypeDef,
    GetCrawlersPaginateResponseTypeDef,
    GetDatabasesPaginatePaginationConfigTypeDef,
    GetDatabasesPaginateResponseTypeDef,
    GetDevEndpointsPaginatePaginationConfigTypeDef,
    GetDevEndpointsPaginateResponseTypeDef,
    GetJobRunsPaginatePaginationConfigTypeDef,
    GetJobRunsPaginateResponseTypeDef,
    GetJobsPaginatePaginationConfigTypeDef,
    GetJobsPaginateResponseTypeDef,
    GetPartitionsPaginatePaginationConfigTypeDef,
    GetPartitionsPaginateResponseTypeDef,
    GetPartitionsPaginateSegmentTypeDef,
    GetSecurityConfigurationsPaginatePaginationConfigTypeDef,
    GetSecurityConfigurationsPaginateResponseTypeDef,
    GetTableVersionsPaginatePaginationConfigTypeDef,
    GetTableVersionsPaginateResponseTypeDef,
    GetTablesPaginatePaginationConfigTypeDef,
    GetTablesPaginateResponseTypeDef,
    GetTriggersPaginatePaginationConfigTypeDef,
    GetTriggersPaginateResponseTypeDef,
    GetUserDefinedFunctionsPaginatePaginationConfigTypeDef,
    GetUserDefinedFunctionsPaginateResponseTypeDef,
)


__all__ = (
    "GetClassifiersPaginator",
    "GetConnectionsPaginator",
    "GetCrawlerMetricsPaginator",
    "GetCrawlersPaginator",
    "GetDatabasesPaginator",
    "GetDevEndpointsPaginator",
    "GetJobRunsPaginator",
    "GetJobsPaginator",
    "GetPartitionsPaginator",
    "GetSecurityConfigurationsPaginator",
    "GetTableVersionsPaginator",
    "GetTablesPaginator",
    "GetTriggersPaginator",
    "GetUserDefinedFunctionsPaginator",
)


class GetClassifiersPaginator(Boto3Paginator):
    """
    Paginator for `get_classifiers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetClassifiersPaginatePaginationConfigTypeDef = None
    ) -> GetClassifiersPaginateResponseTypeDef:
        """
        [GetClassifiers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetClassifiers.paginate)
        """


class GetConnectionsPaginator(Boto3Paginator):
    """
    Paginator for `get_connections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CatalogId: str = None,
        Filter: GetConnectionsPaginateFilterTypeDef = None,
        HidePassword: bool = None,
        PaginationConfig: GetConnectionsPaginatePaginationConfigTypeDef = None,
    ) -> GetConnectionsPaginateResponseTypeDef:
        """
        [GetConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetConnections.paginate)
        """


class GetCrawlerMetricsPaginator(Boto3Paginator):
    """
    Paginator for `get_crawler_metrics`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CrawlerNameList: List[str] = None,
        PaginationConfig: GetCrawlerMetricsPaginatePaginationConfigTypeDef = None,
    ) -> GetCrawlerMetricsPaginateResponseTypeDef:
        """
        [GetCrawlerMetrics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics.paginate)
        """


class GetCrawlersPaginator(Boto3Paginator):
    """
    Paginator for `get_crawlers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetCrawlersPaginatePaginationConfigTypeDef = None
    ) -> GetCrawlersPaginateResponseTypeDef:
        """
        [GetCrawlers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetCrawlers.paginate)
        """


class GetDatabasesPaginator(Boto3Paginator):
    """
    Paginator for `get_databases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CatalogId: str = None,
        PaginationConfig: GetDatabasesPaginatePaginationConfigTypeDef = None,
    ) -> GetDatabasesPaginateResponseTypeDef:
        """
        [GetDatabases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetDatabases.paginate)
        """


class GetDevEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `get_dev_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetDevEndpointsPaginatePaginationConfigTypeDef = None
    ) -> GetDevEndpointsPaginateResponseTypeDef:
        """
        [GetDevEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetDevEndpoints.paginate)
        """


class GetJobRunsPaginator(Boto3Paginator):
    """
    Paginator for `get_job_runs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, JobName: str, PaginationConfig: GetJobRunsPaginatePaginationConfigTypeDef = None
    ) -> GetJobRunsPaginateResponseTypeDef:
        """
        [GetJobRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetJobRuns.paginate)
        """


class GetJobsPaginator(Boto3Paginator):
    """
    Paginator for `get_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetJobsPaginatePaginationConfigTypeDef = None
    ) -> GetJobsPaginateResponseTypeDef:
        """
        [GetJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetJobs.paginate)
        """


class GetPartitionsPaginator(Boto3Paginator):
    """
    Paginator for `get_partitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        Segment: GetPartitionsPaginateSegmentTypeDef = None,
        PaginationConfig: GetPartitionsPaginatePaginationConfigTypeDef = None,
    ) -> GetPartitionsPaginateResponseTypeDef:
        """
        [GetPartitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetPartitions.paginate)
        """


class GetSecurityConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `get_security_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetSecurityConfigurationsPaginatePaginationConfigTypeDef = None
    ) -> GetSecurityConfigurationsPaginateResponseTypeDef:
        """
        [GetSecurityConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations.paginate)
        """


class GetTableVersionsPaginator(Boto3Paginator):
    """
    Paginator for `get_table_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        PaginationConfig: GetTableVersionsPaginatePaginationConfigTypeDef = None,
    ) -> GetTableVersionsPaginateResponseTypeDef:
        """
        [GetTableVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetTableVersions.paginate)
        """


class GetTablesPaginator(Boto3Paginator):
    """
    Paginator for `get_tables`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        PaginationConfig: GetTablesPaginatePaginationConfigTypeDef = None,
    ) -> GetTablesPaginateResponseTypeDef:
        """
        [GetTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetTables.paginate)
        """


class GetTriggersPaginator(Boto3Paginator):
    """
    Paginator for `get_triggers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DependentJobName: str = None,
        PaginationConfig: GetTriggersPaginatePaginationConfigTypeDef = None,
    ) -> GetTriggersPaginateResponseTypeDef:
        """
        [GetTriggers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetTriggers.paginate)
        """


class GetUserDefinedFunctionsPaginator(Boto3Paginator):
    """
    Paginator for `get_user_defined_functions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: str = None,
        PaginationConfig: GetUserDefinedFunctionsPaginatePaginationConfigTypeDef = None,
    ) -> GetUserDefinedFunctionsPaginateResponseTypeDef:
        """
        [GetUserDefinedFunctions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions.paginate)
        """
