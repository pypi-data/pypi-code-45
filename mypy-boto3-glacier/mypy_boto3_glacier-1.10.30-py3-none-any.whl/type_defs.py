"Main interface for glacier service type defs"
from __future__ import annotations

from typing import Dict, List
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCompleteMultipartUploadResponseTypeDef",
    "ClientCreateVaultResponseTypeDef",
    "ClientDescribeJobResponseInventoryRetrievalParametersTypeDef",
    "ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef",
    "ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef",
    "ClientDescribeJobResponseOutputLocationS3TypeDef",
    "ClientDescribeJobResponseOutputLocationTypeDef",
    "ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef",
    "ClientDescribeJobResponseSelectParametersInputSerializationTypeDef",
    "ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef",
    "ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef",
    "ClientDescribeJobResponseSelectParametersTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientDescribeVaultResponseTypeDef",
    "ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef",
    "ClientGetDataRetrievalPolicyResponsePolicyTypeDef",
    "ClientGetDataRetrievalPolicyResponseTypeDef",
    "ClientGetJobOutputResponseTypeDef",
    "ClientGetVaultAccessPolicyResponsepolicyTypeDef",
    "ClientGetVaultAccessPolicyResponseTypeDef",
    "ClientGetVaultLockResponseTypeDef",
    "ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef",
    "ClientGetVaultNotificationsResponseTypeDef",
    "ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef",
    "ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef",
    "ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef",
    "ClientInitiateJobJobParametersOutputLocationS3TypeDef",
    "ClientInitiateJobJobParametersOutputLocationTypeDef",
    "ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef",
    "ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef",
    "ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef",
    "ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef",
    "ClientInitiateJobJobParametersSelectParametersTypeDef",
    "ClientInitiateJobJobParametersTypeDef",
    "ClientInitiateJobResponseTypeDef",
    "ClientInitiateMultipartUploadResponseTypeDef",
    "ClientInitiateVaultLockPolicyTypeDef",
    "ClientInitiateVaultLockResponseTypeDef",
    "ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3TypeDef",
    "ClientListJobsResponseJobListOutputLocationTypeDef",
    "ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef",
    "ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef",
    "ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    "ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef",
    "ClientListJobsResponseJobListSelectParametersTypeDef",
    "ClientListJobsResponseJobListTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientListMultipartUploadsResponseUploadsListTypeDef",
    "ClientListMultipartUploadsResponseTypeDef",
    "ClientListPartsResponsePartsTypeDef",
    "ClientListPartsResponseTypeDef",
    "ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef",
    "ClientListProvisionedCapacityResponseTypeDef",
    "ClientListTagsForVaultResponseTypeDef",
    "ClientListVaultsResponseVaultListTypeDef",
    "ClientListVaultsResponseTypeDef",
    "ClientPurchaseProvisionedCapacityResponseTypeDef",
    "ClientSetDataRetrievalPolicyPolicyRulesTypeDef",
    "ClientSetDataRetrievalPolicyPolicyTypeDef",
    "ClientSetVaultAccessPolicyPolicyTypeDef",
    "ClientSetVaultNotificationsVaultNotificationConfigTypeDef",
    "ClientUploadArchiveResponseTypeDef",
    "ClientUploadMultipartPartResponseTypeDef",
    "JobGetOutputResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef",
    "ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    "ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef",
    "ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef",
    "ListJobsPaginateResponseJobListOutputLocationS3TypeDef",
    "ListJobsPaginateResponseJobListOutputLocationTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersTypeDef",
    "ListJobsPaginateResponseJobListTypeDef",
    "ListJobsPaginateResponseTypeDef",
    "ListMultipartUploadsPaginatePaginationConfigTypeDef",
    "ListMultipartUploadsPaginateResponseUploadsListTypeDef",
    "ListMultipartUploadsPaginateResponseTypeDef",
    "ListPartsPaginatePaginationConfigTypeDef",
    "ListPartsPaginateResponsePartsTypeDef",
    "ListPartsPaginateResponseTypeDef",
    "ListVaultsPaginatePaginationConfigTypeDef",
    "ListVaultsPaginateResponseVaultListTypeDef",
    "ListVaultsPaginateResponseTypeDef",
    "MultipartUploadCompleteResponseTypeDef",
    "MultipartUploadPartsResponsePartsTypeDef",
    "MultipartUploadPartsResponseTypeDef",
    "MultipartUploadUploadPartResponseTypeDef",
    "NotificationSetVaultNotificationConfigTypeDef",
    "VaultCreateResponseTypeDef",
    "VaultExistsWaitWaiterConfigTypeDef",
    "VaultNotExistsWaitWaiterConfigTypeDef",
)


_ClientCompleteMultipartUploadResponseTypeDef = TypedDict(
    "_ClientCompleteMultipartUploadResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)


class ClientCompleteMultipartUploadResponseTypeDef(_ClientCompleteMultipartUploadResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      For information about the underlying REST API, see `Upload Archive
      <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For
      conceptual information, see `Working with Archives in Amazon S3 Glacier
      <https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .
      - **location** *(string) --*

        The relative URI path of the newly added archive resource.
    """


_ClientCreateVaultResponseTypeDef = TypedDict(
    "_ClientCreateVaultResponseTypeDef", {"location": str}, total=False
)


class ClientCreateVaultResponseTypeDef(_ClientCreateVaultResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **location** *(string) --*

        The URI of the vault that was created.
    """


_ClientDescribeJobResponseInventoryRetrievalParametersTypeDef = TypedDict(
    "_ClientDescribeJobResponseInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)


class ClientDescribeJobResponseInventoryRetrievalParametersTypeDef(
    _ClientDescribeJobResponseInventoryRetrievalParametersTypeDef
):
    pass


_ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)


class ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef(
    _ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef
):
    pass


_ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef(
    _ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef
):
    pass


_ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef(
    _ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef
):
    pass


_ClientDescribeJobResponseOutputLocationS3TypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA"],
    },
    total=False,
)


class ClientDescribeJobResponseOutputLocationS3TypeDef(
    _ClientDescribeJobResponseOutputLocationS3TypeDef
):
    pass


_ClientDescribeJobResponseOutputLocationTypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationTypeDef",
    {"S3": ClientDescribeJobResponseOutputLocationS3TypeDef},
    total=False,
)


class ClientDescribeJobResponseOutputLocationTypeDef(
    _ClientDescribeJobResponseOutputLocationTypeDef
):
    pass


_ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef(
    _ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef
):
    pass


_ClientDescribeJobResponseSelectParametersInputSerializationTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersInputSerializationTypeDef",
    {"csv": ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef},
    total=False,
)


class ClientDescribeJobResponseSelectParametersInputSerializationTypeDef(
    _ClientDescribeJobResponseSelectParametersInputSerializationTypeDef
):
    pass


_ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef(
    _ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef
):
    pass


_ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef",
    {"csv": ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)


class ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef(
    _ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef
):
    pass


_ClientDescribeJobResponseSelectParametersTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersTypeDef",
    {
        "InputSerialization": ClientDescribeJobResponseSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseSelectParametersTypeDef(
    _ClientDescribeJobResponseSelectParametersTypeDef
):
    pass


_ClientDescribeJobResponseTypeDef = TypedDict(
    "_ClientDescribeJobResponseTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"],
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": Literal["InProgress", "Succeeded", "Failed"],
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ClientDescribeJobResponseInventoryRetrievalParametersTypeDef,
        "JobOutputPath": str,
        "SelectParameters": ClientDescribeJobResponseSelectParametersTypeDef,
        "OutputLocation": ClientDescribeJobResponseOutputLocationTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseTypeDef(_ClientDescribeJobResponseTypeDef):
    """
    - *(dict) --*

      Contains the description of an Amazon S3 Glacier job.
      - **JobId** *(string) --*

        An opaque string that identifies an Amazon S3 Glacier job.
    """


_ClientDescribeVaultResponseTypeDef = TypedDict(
    "_ClientDescribeVaultResponseTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)


class ClientDescribeVaultResponseTypeDef(_ClientDescribeVaultResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **VaultARN** *(string) --*

        The Amazon Resource Name (ARN) of the vault.
    """


_ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef = TypedDict(
    "_ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef",
    {"Strategy": str, "BytesPerHour": int},
    total=False,
)


class ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef(
    _ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef
):
    """
    - *(dict) --*

      Data retrieval policy rule.
      - **Strategy** *(string) --*

        The type of data retrieval policy to set.
        Valid values: BytesPerHour|FreeTier|None
    """


_ClientGetDataRetrievalPolicyResponsePolicyTypeDef = TypedDict(
    "_ClientGetDataRetrievalPolicyResponsePolicyTypeDef",
    {"Rules": List[ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef]},
    total=False,
)


class ClientGetDataRetrievalPolicyResponsePolicyTypeDef(
    _ClientGetDataRetrievalPolicyResponsePolicyTypeDef
):
    """
    - **Policy** *(dict) --*

      Contains the returned data retrieval policy in JSON format.
      - **Rules** *(list) --*

        The policy rule. Although this is a list type, currently there must be only one rule, which
        contains a Strategy field and optionally a BytesPerHour field.
        - *(dict) --*

          Data retrieval policy rule.
          - **Strategy** *(string) --*

            The type of data retrieval policy to set.
            Valid values: BytesPerHour|FreeTier|None
    """


_ClientGetDataRetrievalPolicyResponseTypeDef = TypedDict(
    "_ClientGetDataRetrievalPolicyResponseTypeDef",
    {"Policy": ClientGetDataRetrievalPolicyResponsePolicyTypeDef},
    total=False,
)


class ClientGetDataRetrievalPolicyResponseTypeDef(_ClientGetDataRetrievalPolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to the ``GetDataRetrievalPolicy`` request.
      - **Policy** *(dict) --*

        Contains the returned data retrieval policy in JSON format.
        - **Rules** *(list) --*

          The policy rule. Although this is a list type, currently there must be only one rule,
          which contains a Strategy field and optionally a BytesPerHour field.
          - *(dict) --*

            Data retrieval policy rule.
            - **Strategy** *(string) --*

              The type of data retrieval policy to set.
              Valid values: BytesPerHour|FreeTier|None
    """


_ClientGetJobOutputResponseTypeDef = TypedDict(
    "_ClientGetJobOutputResponseTypeDef",
    {
        "body": StreamingBody,
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
    },
    total=False,
)


class ClientGetJobOutputResponseTypeDef(_ClientGetJobOutputResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **body** (:class:`.StreamingBody`) --

        The job data, either archive data or inventory data.
    """


_ClientGetVaultAccessPolicyResponsepolicyTypeDef = TypedDict(
    "_ClientGetVaultAccessPolicyResponsepolicyTypeDef", {"Policy": str}, total=False
)


class ClientGetVaultAccessPolicyResponsepolicyTypeDef(
    _ClientGetVaultAccessPolicyResponsepolicyTypeDef
):
    """
    - **policy** *(dict) --*

      Contains the returned vault access policy as a JSON string.
      - **Policy** *(string) --*

        The vault access policy.
    """


_ClientGetVaultAccessPolicyResponseTypeDef = TypedDict(
    "_ClientGetVaultAccessPolicyResponseTypeDef",
    {"policy": ClientGetVaultAccessPolicyResponsepolicyTypeDef},
    total=False,
)


class ClientGetVaultAccessPolicyResponseTypeDef(_ClientGetVaultAccessPolicyResponseTypeDef):
    """
    - *(dict) --*

      Output for GetVaultAccessPolicy.
      - **policy** *(dict) --*

        Contains the returned vault access policy as a JSON string.
        - **Policy** *(string) --*

          The vault access policy.
    """


_ClientGetVaultLockResponseTypeDef = TypedDict(
    "_ClientGetVaultLockResponseTypeDef",
    {"Policy": str, "State": str, "ExpirationDate": str, "CreationDate": str},
    total=False,
)


class ClientGetVaultLockResponseTypeDef(_ClientGetVaultLockResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **Policy** *(string) --*

        The vault lock policy as a JSON string, which uses "\\" as an escape character.
    """


_ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef = TypedDict(
    "_ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)


class ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef(
    _ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef
):
    """
    - **vaultNotificationConfig** *(dict) --*

      Returns the notification configuration set on the vault.
      - **SNSTopic** *(string) --*

        The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
    """


_ClientGetVaultNotificationsResponseTypeDef = TypedDict(
    "_ClientGetVaultNotificationsResponseTypeDef",
    {"vaultNotificationConfig": ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef},
    total=False,
)


class ClientGetVaultNotificationsResponseTypeDef(_ClientGetVaultNotificationsResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **vaultNotificationConfig** *(dict) --*

        Returns the notification configuration set on the vault.
        - **SNSTopic** *(string) --*

          The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
    """


_ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef",
    {"StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)


class ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef(
    _ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef
):
    pass


_ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)


class ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef(
    _ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef
):
    pass


_ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef(
    _ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef
):
    pass


_ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef(
    _ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef
):
    pass


_ClientInitiateJobJobParametersOutputLocationS3TypeDef = TypedDict(
    "_ClientInitiateJobJobParametersOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA"],
    },
    total=False,
)


class ClientInitiateJobJobParametersOutputLocationS3TypeDef(
    _ClientInitiateJobJobParametersOutputLocationS3TypeDef
):
    pass


_ClientInitiateJobJobParametersOutputLocationTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersOutputLocationTypeDef",
    {"S3": ClientInitiateJobJobParametersOutputLocationS3TypeDef},
    total=False,
)


class ClientInitiateJobJobParametersOutputLocationTypeDef(
    _ClientInitiateJobJobParametersOutputLocationTypeDef
):
    pass


_ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef(
    _ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef
):
    pass


_ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef",
    {"csv": ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef},
    total=False,
)


class ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef(
    _ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef
):
    pass


_ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef(
    _ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef
):
    pass


_ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef",
    {"csv": ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)


class ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef(
    _ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef
):
    pass


_ClientInitiateJobJobParametersSelectParametersTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersSelectParametersTypeDef",
    {
        "InputSerialization": ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ClientInitiateJobJobParametersSelectParametersTypeDef(
    _ClientInitiateJobJobParametersSelectParametersTypeDef
):
    pass


_ClientInitiateJobJobParametersTypeDef = TypedDict(
    "_ClientInitiateJobJobParametersTypeDef",
    {
        "Format": str,
        "Type": str,
        "ArchiveId": str,
        "Description": str,
        "SNSTopic": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef,
        "SelectParameters": ClientInitiateJobJobParametersSelectParametersTypeDef,
        "OutputLocation": ClientInitiateJobJobParametersOutputLocationTypeDef,
    },
    total=False,
)


class ClientInitiateJobJobParametersTypeDef(_ClientInitiateJobJobParametersTypeDef):
    """
    Provides options for specifying job information.
    - **Format** *(string) --*

      When initiating a job to retrieve a vault inventory, you can optionally add this parameter to
      your request to specify the output format. If you are initiating an inventory job and do not
      specify a Format field, JSON is the default format. Valid values are "CSV" and "JSON".
    """


_ClientInitiateJobResponseTypeDef = TypedDict(
    "_ClientInitiateJobResponseTypeDef",
    {"location": str, "jobId": str, "jobOutputPath": str},
    total=False,
)


class ClientInitiateJobResponseTypeDef(_ClientInitiateJobResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **location** *(string) --*

        The relative URI path of the job.
    """


_ClientInitiateMultipartUploadResponseTypeDef = TypedDict(
    "_ClientInitiateMultipartUploadResponseTypeDef", {"location": str, "uploadId": str}, total=False
)


class ClientInitiateMultipartUploadResponseTypeDef(_ClientInitiateMultipartUploadResponseTypeDef):
    """
    - *(dict) --*

      The Amazon S3 Glacier response to your request.
      - **location** *(string) --*

        The relative URI path of the multipart upload ID Amazon S3 Glacier created.
    """


_ClientInitiateVaultLockPolicyTypeDef = TypedDict(
    "_ClientInitiateVaultLockPolicyTypeDef", {"Policy": str}, total=False
)


class ClientInitiateVaultLockPolicyTypeDef(_ClientInitiateVaultLockPolicyTypeDef):
    """
    The vault lock policy as a JSON string, which uses "\\" as an escape character.
    - **Policy** *(string) --*

      The vault lock policy.
    """


_ClientInitiateVaultLockResponseTypeDef = TypedDict(
    "_ClientInitiateVaultLockResponseTypeDef", {"lockId": str}, total=False
)


class ClientInitiateVaultLockResponseTypeDef(_ClientInitiateVaultLockResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **lockId** *(string) --*

        The lock ID, which is used to complete the vault locking process.
    """


_ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef = TypedDict(
    "_ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)


class ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef(
    _ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef
):
    pass


_ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)


class ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef(
    _ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef
):
    pass


_ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef(
    _ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef
):
    pass


_ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef(
    _ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef
):
    pass


_ClientListJobsResponseJobListOutputLocationS3TypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA"],
    },
    total=False,
)


class ClientListJobsResponseJobListOutputLocationS3TypeDef(
    _ClientListJobsResponseJobListOutputLocationS3TypeDef
):
    pass


_ClientListJobsResponseJobListOutputLocationTypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationTypeDef",
    {"S3": ClientListJobsResponseJobListOutputLocationS3TypeDef},
    total=False,
)


class ClientListJobsResponseJobListOutputLocationTypeDef(
    _ClientListJobsResponseJobListOutputLocationTypeDef
):
    pass


_ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef(
    _ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef
):
    pass


_ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef",
    {"csv": ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef},
    total=False,
)


class ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef(
    _ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef
):
    pass


_ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef(
    _ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef
):
    pass


_ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef",
    {"csv": ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)


class ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef(
    _ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef
):
    pass


_ClientListJobsResponseJobListSelectParametersTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersTypeDef",
    {
        "InputSerialization": ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ClientListJobsResponseJobListSelectParametersTypeDef(
    _ClientListJobsResponseJobListSelectParametersTypeDef
):
    pass


_ClientListJobsResponseJobListTypeDef = TypedDict(
    "_ClientListJobsResponseJobListTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"],
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": Literal["InProgress", "Succeeded", "Failed"],
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef,
        "JobOutputPath": str,
        "SelectParameters": ClientListJobsResponseJobListSelectParametersTypeDef,
        "OutputLocation": ClientListJobsResponseJobListOutputLocationTypeDef,
    },
    total=False,
)


class ClientListJobsResponseJobListTypeDef(_ClientListJobsResponseJobListTypeDef):
    """
    - *(dict) --*

      Contains the description of an Amazon S3 Glacier job.
      - **JobId** *(string) --*

        An opaque string that identifies an Amazon S3 Glacier job.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"JobList": List[ClientListJobsResponseJobListTypeDef], "Marker": str},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **JobList** *(list) --*

        A list of job objects. Each job object contains metadata describing the job.
        - *(dict) --*

          Contains the description of an Amazon S3 Glacier job.
          - **JobId** *(string) --*

            An opaque string that identifies an Amazon S3 Glacier job.
    """


_ClientListMultipartUploadsResponseUploadsListTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseUploadsListTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)


class ClientListMultipartUploadsResponseUploadsListTypeDef(
    _ClientListMultipartUploadsResponseUploadsListTypeDef
):
    """
    - *(dict) --*

      A list of in-progress multipart uploads for a vault.
      - **MultipartUploadId** *(string) --*

        The ID of a multipart upload.
    """


_ClientListMultipartUploadsResponseTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseTypeDef",
    {"UploadsList": List[ClientListMultipartUploadsResponseUploadsListTypeDef], "Marker": str},
    total=False,
)


class ClientListMultipartUploadsResponseTypeDef(_ClientListMultipartUploadsResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **UploadsList** *(list) --*

        A list of in-progress multipart uploads.
        - *(dict) --*

          A list of in-progress multipart uploads for a vault.
          - **MultipartUploadId** *(string) --*

            The ID of a multipart upload.
    """


_ClientListPartsResponsePartsTypeDef = TypedDict(
    "_ClientListPartsResponsePartsTypeDef",
    {"RangeInBytes": str, "SHA256TreeHash": str},
    total=False,
)


class ClientListPartsResponsePartsTypeDef(_ClientListPartsResponsePartsTypeDef):
    pass


_ClientListPartsResponseTypeDef = TypedDict(
    "_ClientListPartsResponseTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List[ClientListPartsResponsePartsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientListPartsResponseTypeDef(_ClientListPartsResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **MultipartUploadId** *(string) --*

        The ID of the upload to which the parts are associated.
    """


_ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef = TypedDict(
    "_ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef",
    {"CapacityId": str, "StartDate": str, "ExpirationDate": str},
    total=False,
)


class ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef(
    _ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef
):
    """
    - *(dict) --*

      The definition for a provisioned capacity unit.
      - **CapacityId** *(string) --*

        The ID that identifies the provisioned capacity unit.
    """


_ClientListProvisionedCapacityResponseTypeDef = TypedDict(
    "_ClientListProvisionedCapacityResponseTypeDef",
    {
        "ProvisionedCapacityList": List[
            ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef
        ]
    },
    total=False,
)


class ClientListProvisionedCapacityResponseTypeDef(_ClientListProvisionedCapacityResponseTypeDef):
    """
    - *(dict) --*

      - **ProvisionedCapacityList** *(list) --*

        The response body contains the following JSON fields.
        - *(dict) --*

          The definition for a provisioned capacity unit.
          - **CapacityId** *(string) --*

            The ID that identifies the provisioned capacity unit.
    """


_ClientListTagsForVaultResponseTypeDef = TypedDict(
    "_ClientListTagsForVaultResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForVaultResponseTypeDef(_ClientListTagsForVaultResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **Tags** *(dict) --*

        The tags attached to the vault. Each tag is composed of a key and a value.
        - *(string) --*

          - *(string) --*
    """


_ClientListVaultsResponseVaultListTypeDef = TypedDict(
    "_ClientListVaultsResponseVaultListTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)


class ClientListVaultsResponseVaultListTypeDef(_ClientListVaultsResponseVaultListTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **VaultARN** *(string) --*

        The Amazon Resource Name (ARN) of the vault.
    """


_ClientListVaultsResponseTypeDef = TypedDict(
    "_ClientListVaultsResponseTypeDef",
    {"VaultList": List[ClientListVaultsResponseVaultListTypeDef], "Marker": str},
    total=False,
)


class ClientListVaultsResponseTypeDef(_ClientListVaultsResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **VaultList** *(list) --*

        List of vaults.
        - *(dict) --*

          Contains the Amazon S3 Glacier response to your request.
          - **VaultARN** *(string) --*

            The Amazon Resource Name (ARN) of the vault.
    """


_ClientPurchaseProvisionedCapacityResponseTypeDef = TypedDict(
    "_ClientPurchaseProvisionedCapacityResponseTypeDef", {"capacityId": str}, total=False
)


class ClientPurchaseProvisionedCapacityResponseTypeDef(
    _ClientPurchaseProvisionedCapacityResponseTypeDef
):
    """
    - *(dict) --*

      - **capacityId** *(string) --*

        The ID that identifies the provisioned capacity unit.
    """


_ClientSetDataRetrievalPolicyPolicyRulesTypeDef = TypedDict(
    "_ClientSetDataRetrievalPolicyPolicyRulesTypeDef",
    {"Strategy": str, "BytesPerHour": int},
    total=False,
)


class ClientSetDataRetrievalPolicyPolicyRulesTypeDef(
    _ClientSetDataRetrievalPolicyPolicyRulesTypeDef
):
    """
    - *(dict) --*

      Data retrieval policy rule.
      - **Strategy** *(string) --*

        The type of data retrieval policy to set.
        Valid values: BytesPerHour|FreeTier|None
    """


_ClientSetDataRetrievalPolicyPolicyTypeDef = TypedDict(
    "_ClientSetDataRetrievalPolicyPolicyTypeDef",
    {"Rules": List[ClientSetDataRetrievalPolicyPolicyRulesTypeDef]},
    total=False,
)


class ClientSetDataRetrievalPolicyPolicyTypeDef(_ClientSetDataRetrievalPolicyPolicyTypeDef):
    """
    The data retrieval policy in JSON format.
    - **Rules** *(list) --*

      The policy rule. Although this is a list type, currently there must be only one rule, which
      contains a Strategy field and optionally a BytesPerHour field.
      - *(dict) --*

        Data retrieval policy rule.
        - **Strategy** *(string) --*

          The type of data retrieval policy to set.
          Valid values: BytesPerHour|FreeTier|None
    """


_ClientSetVaultAccessPolicyPolicyTypeDef = TypedDict(
    "_ClientSetVaultAccessPolicyPolicyTypeDef", {"Policy": str}, total=False
)


class ClientSetVaultAccessPolicyPolicyTypeDef(_ClientSetVaultAccessPolicyPolicyTypeDef):
    """
    The vault access policy as a JSON string.
    - **Policy** *(string) --*

      The vault access policy.
    """


_ClientSetVaultNotificationsVaultNotificationConfigTypeDef = TypedDict(
    "_ClientSetVaultNotificationsVaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)


class ClientSetVaultNotificationsVaultNotificationConfigTypeDef(
    _ClientSetVaultNotificationsVaultNotificationConfigTypeDef
):
    """
    Provides options for specifying notification configuration.
    - **SNSTopic** *(string) --*

      The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
    """


_ClientUploadArchiveResponseTypeDef = TypedDict(
    "_ClientUploadArchiveResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)


class ClientUploadArchiveResponseTypeDef(_ClientUploadArchiveResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      For information about the underlying REST API, see `Upload Archive
      <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For
      conceptual information, see `Working with Archives in Amazon S3 Glacier
      <https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .
      - **location** *(string) --*

        The relative URI path of the newly added archive resource.
    """


_ClientUploadMultipartPartResponseTypeDef = TypedDict(
    "_ClientUploadMultipartPartResponseTypeDef", {"checksum": str}, total=False
)


class ClientUploadMultipartPartResponseTypeDef(_ClientUploadMultipartPartResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **checksum** *(string) --*

        The SHA256 tree hash that Amazon S3 Glacier computed for the uploaded part.
    """


_JobGetOutputResponseTypeDef = TypedDict(
    "_JobGetOutputResponseTypeDef",
    {
        "body": StreamingBody,
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
    },
    total=False,
)


class JobGetOutputResponseTypeDef(_JobGetOutputResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **body** (:class:`.StreamingBody`) --

        The job data, either archive data or inventory data.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)


class ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef(
    _ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef
):
    pass


_ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef(
    _ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef
):
    pass


_ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef(
    _ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef
):
    pass


_ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef(
    _ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef
):
    pass


_ListJobsPaginateResponseJobListOutputLocationS3TypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA"],
    },
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationS3TypeDef(
    _ListJobsPaginateResponseJobListOutputLocationS3TypeDef
):
    pass


_ListJobsPaginateResponseJobListOutputLocationTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationTypeDef",
    {"S3": ListJobsPaginateResponseJobListOutputLocationS3TypeDef},
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationTypeDef(
    _ListJobsPaginateResponseJobListOutputLocationTypeDef
):
    pass


_ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef
):
    pass


_ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef",
    {"csv": ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef},
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef
):
    pass


_ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef
):
    pass


_ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef",
    {"csv": ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef
):
    pass


_ListJobsPaginateResponseJobListSelectParametersTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersTypeDef",
    {
        "InputSerialization": ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersTypeDef
):
    pass


_ListJobsPaginateResponseJobListTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"],
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": Literal["InProgress", "Succeeded", "Failed"],
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef,
        "JobOutputPath": str,
        "SelectParameters": ListJobsPaginateResponseJobListSelectParametersTypeDef,
        "OutputLocation": ListJobsPaginateResponseJobListOutputLocationTypeDef,
    },
    total=False,
)


class ListJobsPaginateResponseJobListTypeDef(_ListJobsPaginateResponseJobListTypeDef):
    """
    - *(dict) --*

      Contains the description of an Amazon S3 Glacier job.
      - **JobId** *(string) --*

        An opaque string that identifies an Amazon S3 Glacier job.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"JobList": List[ListJobsPaginateResponseJobListTypeDef], "NextToken": str},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **JobList** *(list) --*

        A list of job objects. Each job object contains metadata describing the job.
        - *(dict) --*

          Contains the description of an Amazon S3 Glacier job.
          - **JobId** *(string) --*

            An opaque string that identifies an Amazon S3 Glacier job.
    """


_ListMultipartUploadsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMultipartUploadsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMultipartUploadsPaginatePaginationConfigTypeDef(
    _ListMultipartUploadsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMultipartUploadsPaginateResponseUploadsListTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseUploadsListTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)


class ListMultipartUploadsPaginateResponseUploadsListTypeDef(
    _ListMultipartUploadsPaginateResponseUploadsListTypeDef
):
    """
    - *(dict) --*

      A list of in-progress multipart uploads for a vault.
      - **MultipartUploadId** *(string) --*

        The ID of a multipart upload.
    """


_ListMultipartUploadsPaginateResponseTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseTypeDef",
    {"UploadsList": List[ListMultipartUploadsPaginateResponseUploadsListTypeDef], "NextToken": str},
    total=False,
)


class ListMultipartUploadsPaginateResponseTypeDef(_ListMultipartUploadsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **UploadsList** *(list) --*

        A list of in-progress multipart uploads.
        - *(dict) --*

          A list of in-progress multipart uploads for a vault.
          - **MultipartUploadId** *(string) --*

            The ID of a multipart upload.
    """


_ListPartsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPartsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPartsPaginatePaginationConfigTypeDef(_ListPartsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPartsPaginateResponsePartsTypeDef = TypedDict(
    "_ListPartsPaginateResponsePartsTypeDef",
    {"RangeInBytes": str, "SHA256TreeHash": str},
    total=False,
)


class ListPartsPaginateResponsePartsTypeDef(_ListPartsPaginateResponsePartsTypeDef):
    pass


_ListPartsPaginateResponseTypeDef = TypedDict(
    "_ListPartsPaginateResponseTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List[ListPartsPaginateResponsePartsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPartsPaginateResponseTypeDef(_ListPartsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **MultipartUploadId** *(string) --*

        The ID of the upload to which the parts are associated.
    """


_ListVaultsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVaultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVaultsPaginatePaginationConfigTypeDef(_ListVaultsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListVaultsPaginateResponseVaultListTypeDef = TypedDict(
    "_ListVaultsPaginateResponseVaultListTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)


class ListVaultsPaginateResponseVaultListTypeDef(_ListVaultsPaginateResponseVaultListTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **VaultARN** *(string) --*

        The Amazon Resource Name (ARN) of the vault.
    """


_ListVaultsPaginateResponseTypeDef = TypedDict(
    "_ListVaultsPaginateResponseTypeDef",
    {"VaultList": List[ListVaultsPaginateResponseVaultListTypeDef], "NextToken": str},
    total=False,
)


class ListVaultsPaginateResponseTypeDef(_ListVaultsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **VaultList** *(list) --*

        List of vaults.
        - *(dict) --*

          Contains the Amazon S3 Glacier response to your request.
          - **VaultARN** *(string) --*

            The Amazon Resource Name (ARN) of the vault.
    """


_MultipartUploadCompleteResponseTypeDef = TypedDict(
    "_MultipartUploadCompleteResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)


class MultipartUploadCompleteResponseTypeDef(_MultipartUploadCompleteResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      For information about the underlying REST API, see `Upload Archive
      <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For
      conceptual information, see `Working with Archives in Amazon S3 Glacier
      <https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .
      - **location** *(string) --*

        The relative URI path of the newly added archive resource.
    """


_MultipartUploadPartsResponsePartsTypeDef = TypedDict(
    "_MultipartUploadPartsResponsePartsTypeDef",
    {"RangeInBytes": str, "SHA256TreeHash": str},
    total=False,
)


class MultipartUploadPartsResponsePartsTypeDef(_MultipartUploadPartsResponsePartsTypeDef):
    pass


_MultipartUploadPartsResponseTypeDef = TypedDict(
    "_MultipartUploadPartsResponseTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List[MultipartUploadPartsResponsePartsTypeDef],
        "Marker": str,
    },
    total=False,
)


class MultipartUploadPartsResponseTypeDef(_MultipartUploadPartsResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **MultipartUploadId** *(string) --*

        The ID of the upload to which the parts are associated.
    """


_MultipartUploadUploadPartResponseTypeDef = TypedDict(
    "_MultipartUploadUploadPartResponseTypeDef", {"checksum": str}, total=False
)


class MultipartUploadUploadPartResponseTypeDef(_MultipartUploadUploadPartResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **checksum** *(string) --*

        The SHA256 tree hash that Amazon S3 Glacier computed for the uploaded part.
    """


_NotificationSetVaultNotificationConfigTypeDef = TypedDict(
    "_NotificationSetVaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)


class NotificationSetVaultNotificationConfigTypeDef(_NotificationSetVaultNotificationConfigTypeDef):
    """
    Provides options for specifying notification configuration.
    - **SNSTopic** *(string) --*

      The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).
    """


_VaultCreateResponseTypeDef = TypedDict(
    "_VaultCreateResponseTypeDef", {"location": str}, total=False
)


class VaultCreateResponseTypeDef(_VaultCreateResponseTypeDef):
    """
    - *(dict) --*

      Contains the Amazon S3 Glacier response to your request.
      - **location** *(string) --*

        The URI of the vault that was created.
    """


_VaultExistsWaitWaiterConfigTypeDef = TypedDict(
    "_VaultExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class VaultExistsWaitWaiterConfigTypeDef(_VaultExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3
    """


_VaultNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "_VaultNotExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class VaultNotExistsWaitWaiterConfigTypeDef(_VaultNotExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3
    """
