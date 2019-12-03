"Main interface for qldb service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateLedgerResponseTypeDef",
    "ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef",
    "ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef",
    "ClientDescribeJournalS3ExportResponseTypeDef",
    "ClientDescribeLedgerResponseTypeDef",
    "ClientExportJournalToS3ResponseTypeDef",
    "ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientExportJournalToS3S3ExportConfigurationTypeDef",
    "ClientGetBlockBlockAddressTypeDef",
    "ClientGetBlockDigestTipAddressTypeDef",
    "ClientGetBlockResponseBlockTypeDef",
    "ClientGetBlockResponseProofTypeDef",
    "ClientGetBlockResponseTypeDef",
    "ClientGetDigestResponseDigestTipAddressTypeDef",
    "ClientGetDigestResponseTypeDef",
    "ClientGetRevisionBlockAddressTypeDef",
    "ClientGetRevisionDigestTipAddressTypeDef",
    "ClientGetRevisionResponseProofTypeDef",
    "ClientGetRevisionResponseRevisionTypeDef",
    "ClientGetRevisionResponseTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseTypeDef",
    "ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    "ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef",
    "ClientListJournalS3ExportsResponseTypeDef",
    "ClientListLedgersResponseLedgersTypeDef",
    "ClientListLedgersResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateLedgerResponseTypeDef",
)


_ClientCreateLedgerResponseTypeDef = TypedDict(
    "_ClientCreateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientCreateLedgerResponseTypeDef(_ClientCreateLedgerResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the ledger.
    """


_ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": Literal["SSE_KMS", "SSE_S3", "NO_ENCRYPTION"], "KmsKeyArn": str},
    total=False,
)


class ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef(
    _ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef
):
    pass


_ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef = TypedDict(
    "_ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef(
    _ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef
):
    pass


_ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef = TypedDict(
    "_ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": Literal["IN_PROGRESS", "COMPLETED", "CANCELLED"],
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)


class ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef(
    _ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef
):
    """
    - **ExportDescription** *(dict) --*

      Information about the journal export job returned by a ``DescribeJournalS3Export`` request.
      - **LedgerName** *(string) --*

        The name of the ledger.
    """


_ClientDescribeJournalS3ExportResponseTypeDef = TypedDict(
    "_ClientDescribeJournalS3ExportResponseTypeDef",
    {"ExportDescription": ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef},
    total=False,
)


class ClientDescribeJournalS3ExportResponseTypeDef(_ClientDescribeJournalS3ExportResponseTypeDef):
    """
    - *(dict) --*

      - **ExportDescription** *(dict) --*

        Information about the journal export job returned by a ``DescribeJournalS3Export`` request.
        - **LedgerName** *(string) --*

          The name of the ledger.
    """


_ClientDescribeLedgerResponseTypeDef = TypedDict(
    "_ClientDescribeLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientDescribeLedgerResponseTypeDef(_ClientDescribeLedgerResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the ledger.
    """


_ClientExportJournalToS3ResponseTypeDef = TypedDict(
    "_ClientExportJournalToS3ResponseTypeDef", {"ExportId": str}, total=False
)


class ClientExportJournalToS3ResponseTypeDef(_ClientExportJournalToS3ResponseTypeDef):
    """
    - *(dict) --*

      - **ExportId** *(string) --*

        The unique ID that QLDB assigns to each journal export job.
        To describe your export request and check the status of the job, you can use ``ExportId`` to
        call ``DescribeJournalS3Export`` .
    """


_ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": Literal["SSE_KMS", "SSE_S3", "NO_ENCRYPTION"], "KmsKeyArn": str},
    total=False,
)


class ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef(
    _ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef
):
    pass


_RequiredClientExportJournalToS3S3ExportConfigurationTypeDef = TypedDict(
    "_RequiredClientExportJournalToS3S3ExportConfigurationTypeDef", {"Bucket": str}
)
_OptionalClientExportJournalToS3S3ExportConfigurationTypeDef = TypedDict(
    "_OptionalClientExportJournalToS3S3ExportConfigurationTypeDef",
    {
        "Prefix": str,
        "EncryptionConfiguration": ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientExportJournalToS3S3ExportConfigurationTypeDef(
    _RequiredClientExportJournalToS3S3ExportConfigurationTypeDef,
    _OptionalClientExportJournalToS3S3ExportConfigurationTypeDef,
):
    """
    The configuration settings of the Amazon S3 bucket destination for your export request.
    - **Bucket** *(string) --***[REQUIRED]**

      The Amazon S3 bucket name in which a journal export job writes the journal contents.
      The bucket name must comply with the Amazon S3 bucket naming conventions. For more
      information, see `Bucket Restrictions and Limitations
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the *Amazon S3
      Developer Guide* .
    """


_ClientGetBlockBlockAddressTypeDef = TypedDict(
    "_ClientGetBlockBlockAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetBlockBlockAddressTypeDef(_ClientGetBlockBlockAddressTypeDef):
    """
    The location of the block that you want to request. An address is an Amazon Ion structure that
    has two fields: ``strandId`` and ``sequenceNo`` .
    For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:14}``
    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetBlockDigestTipAddressTypeDef = TypedDict(
    "_ClientGetBlockDigestTipAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetBlockDigestTipAddressTypeDef(_ClientGetBlockDigestTipAddressTypeDef):
    """
    The latest block location covered by the digest for which to request a proof. An address is an
    Amazon Ion structure that has two fields: ``strandId`` and ``sequenceNo`` .
    For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:49}``
    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetBlockResponseBlockTypeDef = TypedDict(
    "_ClientGetBlockResponseBlockTypeDef", {"IonText": str}, total=False
)


class ClientGetBlockResponseBlockTypeDef(_ClientGetBlockResponseBlockTypeDef):
    """
    - **Block** *(dict) --*

      The block data object in Amazon Ion format.
      - **IonText** *(string) --*

        An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetBlockResponseProofTypeDef = TypedDict(
    "_ClientGetBlockResponseProofTypeDef", {"IonText": str}, total=False
)


class ClientGetBlockResponseProofTypeDef(_ClientGetBlockResponseProofTypeDef):
    pass


_ClientGetBlockResponseTypeDef = TypedDict(
    "_ClientGetBlockResponseTypeDef",
    {"Block": ClientGetBlockResponseBlockTypeDef, "Proof": ClientGetBlockResponseProofTypeDef},
    total=False,
)


class ClientGetBlockResponseTypeDef(_ClientGetBlockResponseTypeDef):
    """
    - *(dict) --*

      - **Block** *(dict) --*

        The block data object in Amazon Ion format.
        - **IonText** *(string) --*

          An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetDigestResponseDigestTipAddressTypeDef = TypedDict(
    "_ClientGetDigestResponseDigestTipAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetDigestResponseDigestTipAddressTypeDef(
    _ClientGetDigestResponseDigestTipAddressTypeDef
):
    pass


_ClientGetDigestResponseTypeDef = TypedDict(
    "_ClientGetDigestResponseTypeDef",
    {"Digest": bytes, "DigestTipAddress": ClientGetDigestResponseDigestTipAddressTypeDef},
    total=False,
)


class ClientGetDigestResponseTypeDef(_ClientGetDigestResponseTypeDef):
    """
    - *(dict) --*

      - **Digest** *(bytes) --*

        The 256-bit hash value representing the digest returned by a ``GetDigest`` request.
    """


_ClientGetRevisionBlockAddressTypeDef = TypedDict(
    "_ClientGetRevisionBlockAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetRevisionBlockAddressTypeDef(_ClientGetRevisionBlockAddressTypeDef):
    """
    The block location of the document revision to be verified. An address is an Amazon Ion
    structure that has two fields: ``strandId`` and ``sequenceNo`` .
    For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:14}``
    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetRevisionDigestTipAddressTypeDef = TypedDict(
    "_ClientGetRevisionDigestTipAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetRevisionDigestTipAddressTypeDef(_ClientGetRevisionDigestTipAddressTypeDef):
    """
    The latest block location covered by the digest for which to request a proof. An address is an
    Amazon Ion structure that has two fields: ``strandId`` and ``sequenceNo`` .
    For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:49}``
    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetRevisionResponseProofTypeDef = TypedDict(
    "_ClientGetRevisionResponseProofTypeDef", {"IonText": str}, total=False
)


class ClientGetRevisionResponseProofTypeDef(_ClientGetRevisionResponseProofTypeDef):
    """
    - **Proof** *(dict) --*

      The proof object in Amazon Ion format returned by a ``GetRevision`` request. A proof contains
      the list of hash values that are required to recalculate the specified digest using a Merkle
      tree, starting with the specified document revision.
      - **IonText** *(string) --*

        An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetRevisionResponseRevisionTypeDef = TypedDict(
    "_ClientGetRevisionResponseRevisionTypeDef", {"IonText": str}, total=False
)


class ClientGetRevisionResponseRevisionTypeDef(_ClientGetRevisionResponseRevisionTypeDef):
    pass


_ClientGetRevisionResponseTypeDef = TypedDict(
    "_ClientGetRevisionResponseTypeDef",
    {
        "Proof": ClientGetRevisionResponseProofTypeDef,
        "Revision": ClientGetRevisionResponseRevisionTypeDef,
    },
    total=False,
)


class ClientGetRevisionResponseTypeDef(_ClientGetRevisionResponseTypeDef):
    """
    - *(dict) --*

      - **Proof** *(dict) --*

        The proof object in Amazon Ion format returned by a ``GetRevision`` request. A proof
        contains the list of hash values that are required to recalculate the specified digest using
        a Merkle tree, starting with the specified document revision.
        - **IonText** *(string) --*

          An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": Literal["SSE_KMS", "SSE_S3", "NO_ENCRYPTION"], "KmsKeyArn": str},
    total=False,
)


class ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef(
    _ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef
):
    pass


_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef = TypedDict(
    "_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef(
    _ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef
):
    pass


_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef = TypedDict(
    "_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": Literal["IN_PROGRESS", "COMPLETED", "CANCELLED"],
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)


class ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef(
    _ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef
):
    """
    - *(dict) --*

      The information about a journal export job, including the ledger name, export ID, when it was
      created, current status, and its start and end time export parameters.
      - **LedgerName** *(string) --*

        The name of the ledger.
    """


_ClientListJournalS3ExportsForLedgerResponseTypeDef = TypedDict(
    "_ClientListJournalS3ExportsForLedgerResponseTypeDef",
    {
        "JournalS3Exports": List[
            ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListJournalS3ExportsForLedgerResponseTypeDef(
    _ClientListJournalS3ExportsForLedgerResponseTypeDef
):
    """
    - *(dict) --*

      - **JournalS3Exports** *(list) --*

        The array of journal export job descriptions that are associated with the specified ledger.
        - *(dict) --*

          The information about a journal export job, including the ledger name, export ID, when it
          was created, current status, and its start and end time export parameters.
          - **LedgerName** *(string) --*

            The name of the ledger.
    """


_ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": Literal["SSE_KMS", "SSE_S3", "NO_ENCRYPTION"], "KmsKeyArn": str},
    total=False,
)


class ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef(
    _ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef
):
    pass


_ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef = TypedDict(
    "_ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef(
    _ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef
):
    pass


_ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef = TypedDict(
    "_ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": Literal["IN_PROGRESS", "COMPLETED", "CANCELLED"],
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)


class ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef(
    _ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef
):
    """
    - *(dict) --*

      The information about a journal export job, including the ledger name, export ID, when it was
      created, current status, and its start and end time export parameters.
      - **LedgerName** *(string) --*

        The name of the ledger.
    """


_ClientListJournalS3ExportsResponseTypeDef = TypedDict(
    "_ClientListJournalS3ExportsResponseTypeDef",
    {
        "JournalS3Exports": List[ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListJournalS3ExportsResponseTypeDef(_ClientListJournalS3ExportsResponseTypeDef):
    """
    - *(dict) --*

      - **JournalS3Exports** *(list) --*

        The array of journal export job descriptions for all ledgers that are associated with the
        current AWS account and Region.
        - *(dict) --*

          The information about a journal export job, including the ledger name, export ID, when it
          was created, current status, and its start and end time export parameters.
          - **LedgerName** *(string) --*

            The name of the ledger.
    """


_ClientListLedgersResponseLedgersTypeDef = TypedDict(
    "_ClientListLedgersResponseLedgersTypeDef",
    {
        "Name": str,
        "State": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "CreationDateTime": datetime,
    },
    total=False,
)


class ClientListLedgersResponseLedgersTypeDef(_ClientListLedgersResponseLedgersTypeDef):
    """
    - *(dict) --*

      Information about a ledger, including its name, state, and when it was created.
      - **Name** *(string) --*

        The name of the ledger.
    """


_ClientListLedgersResponseTypeDef = TypedDict(
    "_ClientListLedgersResponseTypeDef",
    {"Ledgers": List[ClientListLedgersResponseLedgersTypeDef], "NextToken": str},
    total=False,
)


class ClientListLedgersResponseTypeDef(_ClientListLedgersResponseTypeDef):
    """
    - *(dict) --*

      - **Ledgers** *(list) --*

        The array of ledger summaries that are associated with the current AWS account and Region.
        - *(dict) --*

          Information about a ledger, including its name, state, and when it was created.
          - **Name** *(string) --*

            The name of the ledger.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The tags that are currently associated with the specified Amazon QLDB resource.
        - *(string) --*

          - *(string) --*
    """


_ClientUpdateLedgerResponseTypeDef = TypedDict(
    "_ClientUpdateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientUpdateLedgerResponseTypeDef(_ClientUpdateLedgerResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the ledger.
    """
