"Main interface for qldb service Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_qldb.client as client_scope
from mypy_boto3_qldb.type_defs import (
    ClientCreateLedgerResponseTypeDef,
    ClientDescribeJournalS3ExportResponseTypeDef,
    ClientDescribeLedgerResponseTypeDef,
    ClientExportJournalToS3ResponseTypeDef,
    ClientExportJournalToS3S3ExportConfigurationTypeDef,
    ClientGetBlockBlockAddressTypeDef,
    ClientGetBlockDigestTipAddressTypeDef,
    ClientGetBlockResponseTypeDef,
    ClientGetDigestResponseTypeDef,
    ClientGetRevisionBlockAddressTypeDef,
    ClientGetRevisionDigestTipAddressTypeDef,
    ClientGetRevisionResponseTypeDef,
    ClientListJournalS3ExportsForLedgerResponseTypeDef,
    ClientListJournalS3ExportsResponseTypeDef,
    ClientListLedgersResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateLedgerResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    """
    [QLDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ledger(
        self,
        Name: str,
        PermissionsMode: str,
        Tags: Dict[str, str] = None,
        DeletionProtection: bool = None,
    ) -> ClientCreateLedgerResponseTypeDef:
        """
        [Client.create_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.create_ledger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ledger(self, Name: str) -> None:
        """
        [Client.delete_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.delete_ledger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_journal_s3_export(
        self, Name: str, ExportId: str
    ) -> ClientDescribeJournalS3ExportResponseTypeDef:
        """
        [Client.describe_journal_s3_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.describe_journal_s3_export)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ledger(self, Name: str) -> ClientDescribeLedgerResponseTypeDef:
        """
        [Client.describe_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.describe_ledger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_journal_to_s3(
        self,
        Name: str,
        InclusiveStartTime: datetime,
        ExclusiveEndTime: datetime,
        S3ExportConfiguration: ClientExportJournalToS3S3ExportConfigurationTypeDef,
        RoleArn: str,
    ) -> ClientExportJournalToS3ResponseTypeDef:
        """
        [Client.export_journal_to_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.export_journal_to_s3)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_block(
        self,
        Name: str,
        BlockAddress: ClientGetBlockBlockAddressTypeDef,
        DigestTipAddress: ClientGetBlockDigestTipAddressTypeDef = None,
    ) -> ClientGetBlockResponseTypeDef:
        """
        [Client.get_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.get_block)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_digest(self, Name: str) -> ClientGetDigestResponseTypeDef:
        """
        [Client.get_digest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.get_digest)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_revision(
        self,
        Name: str,
        BlockAddress: ClientGetRevisionBlockAddressTypeDef,
        DocumentId: str,
        DigestTipAddress: ClientGetRevisionDigestTipAddressTypeDef = None,
    ) -> ClientGetRevisionResponseTypeDef:
        """
        [Client.get_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.get_revision)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_journal_s3_exports(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListJournalS3ExportsResponseTypeDef:
        """
        [Client.list_journal_s3_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_journal_s3_exports_for_ledger(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListJournalS3ExportsForLedgerResponseTypeDef:
        """
        [Client.list_journal_s3_exports_for_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports_for_ledger)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ledgers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListLedgersResponseTypeDef:
        """
        [Client.list_ledgers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.list_ledgers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_ledger(
        self, Name: str, DeletionProtection: bool = None
    ) -> ClientUpdateLedgerResponseTypeDef:
        """
        [Client.update_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/qldb.html#QLDB.Client.update_ledger)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourcePreconditionNotMetException: Boto3ClientError
