"Main interface for kendra service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_kendra.client as client_scope
from mypy_boto3_kendra.type_defs import (
    ClientBatchDeleteDocumentResponseTypeDef,
    ClientBatchPutDocumentDocumentsTypeDef,
    ClientBatchPutDocumentResponseTypeDef,
    ClientCreateDataSourceConfigurationTypeDef,
    ClientCreateDataSourceResponseTypeDef,
    ClientCreateFaqResponseTypeDef,
    ClientCreateFaqS3PathTypeDef,
    ClientCreateIndexResponseTypeDef,
    ClientCreateIndexServerSideEncryptionConfigurationTypeDef,
    ClientDescribeDataSourceResponseTypeDef,
    ClientDescribeFaqResponseTypeDef,
    ClientDescribeIndexResponseTypeDef,
    ClientListDataSourceSyncJobsResponseTypeDef,
    ClientListDataSourceSyncJobsStartTimeFilterTypeDef,
    ClientListDataSourcesResponseTypeDef,
    ClientListFaqsResponseTypeDef,
    ClientListIndicesResponseTypeDef,
    ClientQueryAttributeFilterTypeDef,
    ClientQueryFacetsTypeDef,
    ClientQueryResponseTypeDef,
    ClientStartDataSourceSyncJobResponseTypeDef,
    ClientSubmitFeedbackClickFeedbackItemsTypeDef,
    ClientSubmitFeedbackRelevanceFeedbackItemsTypeDef,
    ClientUpdateDataSourceConfigurationTypeDef,
    ClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [Kendra.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_document(
        self, IndexId: str, DocumentIdList: List[str]
    ) -> ClientBatchDeleteDocumentResponseTypeDef:
        """
        [Client.batch_delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.batch_delete_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_put_document(
        self,
        IndexId: str,
        Documents: List[ClientBatchPutDocumentDocumentsTypeDef],
        RoleArn: str = None,
    ) -> ClientBatchPutDocumentResponseTypeDef:
        """
        [Client.batch_put_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.batch_put_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_data_source(
        self,
        Name: str,
        IndexId: str,
        Type: Literal["S3", "SHAREPOINT", "DATABASE"],
        Configuration: ClientCreateDataSourceConfigurationTypeDef,
        RoleArn: str,
        Description: str = None,
        Schedule: str = None,
    ) -> ClientCreateDataSourceResponseTypeDef:
        """
        [Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.create_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_faq(
        self,
        IndexId: str,
        Name: str,
        S3Path: ClientCreateFaqS3PathTypeDef,
        RoleArn: str,
        Description: str = None,
    ) -> ClientCreateFaqResponseTypeDef:
        """
        [Client.create_faq documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.create_faq)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_index(
        self,
        Name: str,
        RoleArn: str,
        ServerSideEncryptionConfiguration: ClientCreateIndexServerSideEncryptionConfigurationTypeDef = None,
        Description: str = None,
    ) -> ClientCreateIndexResponseTypeDef:
        """
        [Client.create_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.create_index)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_faq(self, Id: str, IndexId: str) -> None:
        """
        [Client.delete_faq documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.delete_faq)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_index(self, Id: str) -> None:
        """
        [Client.delete_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.delete_index)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_data_source(
        self, Id: str, IndexId: str
    ) -> ClientDescribeDataSourceResponseTypeDef:
        """
        [Client.describe_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.describe_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_faq(self, Id: str, IndexId: str) -> ClientDescribeFaqResponseTypeDef:
        """
        [Client.describe_faq documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.describe_faq)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_index(self, Id: str) -> ClientDescribeIndexResponseTypeDef:
        """
        [Client.describe_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.describe_index)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_data_source_sync_jobs(
        self,
        Id: str,
        IndexId: str,
        NextToken: str = None,
        MaxResults: int = None,
        StartTimeFilter: ClientListDataSourceSyncJobsStartTimeFilterTypeDef = None,
        StatusFilter: Literal[
            "FAILED", "SUCCEEDED", "SYNCING", "INCOMPLETE", "STOPPING", "ABORTED"
        ] = None,
    ) -> ClientListDataSourceSyncJobsResponseTypeDef:
        """
        [Client.list_data_source_sync_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.list_data_source_sync_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_data_sources(
        self, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDataSourcesResponseTypeDef:
        """
        [Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.list_data_sources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_faqs(
        self, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListFaqsResponseTypeDef:
        """
        [Client.list_faqs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.list_faqs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_indices(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListIndicesResponseTypeDef:
        """
        [Client.list_indices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.list_indices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def query(
        self,
        IndexId: str,
        QueryText: str,
        AttributeFilter: ClientQueryAttributeFilterTypeDef = None,
        Facets: List[ClientQueryFacetsTypeDef] = None,
        RequestedDocumentAttributes: List[str] = None,
        QueryResultTypeFilter: Literal["DOCUMENT", "QUESTION_ANSWER", "ANSWER"] = None,
        PageNumber: int = None,
        PageSize: int = None,
    ) -> ClientQueryResponseTypeDef:
        """
        [Client.query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.query)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_data_source_sync_job(
        self, Id: str, IndexId: str
    ) -> ClientStartDataSourceSyncJobResponseTypeDef:
        """
        [Client.start_data_source_sync_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.start_data_source_sync_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_data_source_sync_job(self, Id: str, IndexId: str) -> None:
        """
        [Client.stop_data_source_sync_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.stop_data_source_sync_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def submit_feedback(
        self,
        IndexId: str,
        QueryId: str,
        ClickFeedbackItems: List[ClientSubmitFeedbackClickFeedbackItemsTypeDef] = None,
        RelevanceFeedbackItems: List[ClientSubmitFeedbackRelevanceFeedbackItemsTypeDef] = None,
    ) -> None:
        """
        [Client.submit_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.submit_feedback)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_data_source(
        self,
        Id: str,
        IndexId: str,
        Name: str = None,
        Configuration: ClientUpdateDataSourceConfigurationTypeDef = None,
        Description: str = None,
        Schedule: str = None,
        RoleArn: str = None,
    ) -> None:
        """
        [Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.update_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_index(
        self,
        Id: str,
        Name: str = None,
        RoleArn: str = None,
        Description: str = None,
        DocumentMetadataConfigurationUpdates: List[
            ClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef
        ] = None,
    ) -> None:
        """
        [Client.update_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kendra.html#Kendra.Client.update_index)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceAlreadyExistException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
