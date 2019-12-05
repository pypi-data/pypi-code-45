"Main interface for glacier service type defs"
from __future__ import annotations

import sys
from typing import Dict, List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCompleteMultipartUploadResponseTypeDef = TypedDict(
    "ClientCompleteMultipartUploadResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)

ClientCreateVaultResponseTypeDef = TypedDict(
    "ClientCreateVaultResponseTypeDef", {"location": str}, total=False
)

ClientDescribeJobResponseInventoryRetrievalParametersTypeDef = TypedDict(
    "ClientDescribeJobResponseInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)

ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)

ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ClientDescribeJobResponseOutputLocationS3TypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationS3TypeDef",
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

ClientDescribeJobResponseOutputLocationTypeDef = TypedDict(
    "ClientDescribeJobResponseOutputLocationTypeDef",
    {"S3": ClientDescribeJobResponseOutputLocationS3TypeDef},
    total=False,
)

ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef",
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

ClientDescribeJobResponseSelectParametersInputSerializationTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersInputSerializationTypeDef",
    {"csv": ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef},
    total=False,
)

ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef",
    {"csv": ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)

ClientDescribeJobResponseSelectParametersTypeDef = TypedDict(
    "ClientDescribeJobResponseSelectParametersTypeDef",
    {
        "InputSerialization": ClientDescribeJobResponseSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ClientDescribeJobResponseTypeDef = TypedDict(
    "ClientDescribeJobResponseTypeDef",
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

ClientDescribeVaultResponseTypeDef = TypedDict(
    "ClientDescribeVaultResponseTypeDef",
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

ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef = TypedDict(
    "ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef",
    {"Strategy": str, "BytesPerHour": int},
    total=False,
)

ClientGetDataRetrievalPolicyResponsePolicyTypeDef = TypedDict(
    "ClientGetDataRetrievalPolicyResponsePolicyTypeDef",
    {"Rules": List[ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef]},
    total=False,
)

ClientGetDataRetrievalPolicyResponseTypeDef = TypedDict(
    "ClientGetDataRetrievalPolicyResponseTypeDef",
    {"Policy": ClientGetDataRetrievalPolicyResponsePolicyTypeDef},
    total=False,
)

ClientGetJobOutputResponseTypeDef = TypedDict(
    "ClientGetJobOutputResponseTypeDef",
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

ClientGetVaultAccessPolicyResponsepolicyTypeDef = TypedDict(
    "ClientGetVaultAccessPolicyResponsepolicyTypeDef", {"Policy": str}, total=False
)

ClientGetVaultAccessPolicyResponseTypeDef = TypedDict(
    "ClientGetVaultAccessPolicyResponseTypeDef",
    {"policy": ClientGetVaultAccessPolicyResponsepolicyTypeDef},
    total=False,
)

ClientGetVaultLockResponseTypeDef = TypedDict(
    "ClientGetVaultLockResponseTypeDef",
    {"Policy": str, "State": str, "ExpirationDate": str, "CreationDate": str},
    total=False,
)

ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef = TypedDict(
    "ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)

ClientGetVaultNotificationsResponseTypeDef = TypedDict(
    "ClientGetVaultNotificationsResponseTypeDef",
    {"vaultNotificationConfig": ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef},
    total=False,
)

ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef = TypedDict(
    "ClientInitiateJobJobParametersInventoryRetrievalParametersTypeDef",
    {"StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)

ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)

ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientInitiateJobJobParametersOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ClientInitiateJobJobParametersOutputLocationS3TypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationS3TypeDef",
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

ClientInitiateJobJobParametersOutputLocationTypeDef = TypedDict(
    "ClientInitiateJobJobParametersOutputLocationTypeDef",
    {"S3": ClientInitiateJobJobParametersOutputLocationS3TypeDef},
    total=False,
)

ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef",
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

ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef",
    {"csv": ClientInitiateJobJobParametersSelectParametersInputSerializationcsvTypeDef},
    total=False,
)

ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef",
    {"csv": ClientInitiateJobJobParametersSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)

ClientInitiateJobJobParametersSelectParametersTypeDef = TypedDict(
    "ClientInitiateJobJobParametersSelectParametersTypeDef",
    {
        "InputSerialization": ClientInitiateJobJobParametersSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientInitiateJobJobParametersSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ClientInitiateJobJobParametersTypeDef = TypedDict(
    "ClientInitiateJobJobParametersTypeDef",
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

ClientInitiateJobResponseTypeDef = TypedDict(
    "ClientInitiateJobResponseTypeDef",
    {"location": str, "jobId": str, "jobOutputPath": str},
    total=False,
)

ClientInitiateMultipartUploadResponseTypeDef = TypedDict(
    "ClientInitiateMultipartUploadResponseTypeDef", {"location": str, "uploadId": str}, total=False
)

ClientInitiateVaultLockPolicyTypeDef = TypedDict(
    "ClientInitiateVaultLockPolicyTypeDef", {"Policy": str}, total=False
)

ClientInitiateVaultLockResponseTypeDef = TypedDict(
    "ClientInitiateVaultLockResponseTypeDef", {"lockId": str}, total=False
)

ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef = TypedDict(
    "ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)

ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)

ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ClientListJobsResponseJobListOutputLocationS3TypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationS3TypeDef",
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

ClientListJobsResponseJobListOutputLocationTypeDef = TypedDict(
    "ClientListJobsResponseJobListOutputLocationTypeDef",
    {"S3": ClientListJobsResponseJobListOutputLocationS3TypeDef},
    total=False,
)

ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef",
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

ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef",
    {"csv": ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef},
    total=False,
)

ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef",
    {"csv": ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)

ClientListJobsResponseJobListSelectParametersTypeDef = TypedDict(
    "ClientListJobsResponseJobListSelectParametersTypeDef",
    {
        "InputSerialization": ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ClientListJobsResponseJobListTypeDef = TypedDict(
    "ClientListJobsResponseJobListTypeDef",
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

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"JobList": List[ClientListJobsResponseJobListTypeDef], "Marker": str},
    total=False,
)

ClientListMultipartUploadsResponseUploadsListTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseUploadsListTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)

ClientListMultipartUploadsResponseTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseTypeDef",
    {"UploadsList": List[ClientListMultipartUploadsResponseUploadsListTypeDef], "Marker": str},
    total=False,
)

ClientListPartsResponsePartsTypeDef = TypedDict(
    "ClientListPartsResponsePartsTypeDef", {"RangeInBytes": str, "SHA256TreeHash": str}, total=False
)

ClientListPartsResponseTypeDef = TypedDict(
    "ClientListPartsResponseTypeDef",
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

ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef = TypedDict(
    "ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef",
    {"CapacityId": str, "StartDate": str, "ExpirationDate": str},
    total=False,
)

ClientListProvisionedCapacityResponseTypeDef = TypedDict(
    "ClientListProvisionedCapacityResponseTypeDef",
    {
        "ProvisionedCapacityList": List[
            ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef
        ]
    },
    total=False,
)

ClientListTagsForVaultResponseTypeDef = TypedDict(
    "ClientListTagsForVaultResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientListVaultsResponseVaultListTypeDef = TypedDict(
    "ClientListVaultsResponseVaultListTypeDef",
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

ClientListVaultsResponseTypeDef = TypedDict(
    "ClientListVaultsResponseTypeDef",
    {"VaultList": List[ClientListVaultsResponseVaultListTypeDef], "Marker": str},
    total=False,
)

ClientPurchaseProvisionedCapacityResponseTypeDef = TypedDict(
    "ClientPurchaseProvisionedCapacityResponseTypeDef", {"capacityId": str}, total=False
)

ClientSetDataRetrievalPolicyPolicyRulesTypeDef = TypedDict(
    "ClientSetDataRetrievalPolicyPolicyRulesTypeDef",
    {"Strategy": str, "BytesPerHour": int},
    total=False,
)

ClientSetDataRetrievalPolicyPolicyTypeDef = TypedDict(
    "ClientSetDataRetrievalPolicyPolicyTypeDef",
    {"Rules": List[ClientSetDataRetrievalPolicyPolicyRulesTypeDef]},
    total=False,
)

ClientSetVaultAccessPolicyPolicyTypeDef = TypedDict(
    "ClientSetVaultAccessPolicyPolicyTypeDef", {"Policy": str}, total=False
)

ClientSetVaultNotificationsVaultNotificationConfigTypeDef = TypedDict(
    "ClientSetVaultNotificationsVaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)

ClientUploadArchiveResponseTypeDef = TypedDict(
    "ClientUploadArchiveResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)

ClientUploadMultipartPartResponseTypeDef = TypedDict(
    "ClientUploadMultipartPartResponseTypeDef", {"checksum": str}, total=False
)

JobGetOutputResponseTypeDef = TypedDict(
    "JobGetOutputResponseTypeDef",
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

ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)

ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "Type": Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"],
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)

ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["aws:kms", "AES256"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ListJobsPaginateResponseJobListOutputLocationS3TypeDef = TypedDict(
    "ListJobsPaginateResponseJobListOutputLocationS3TypeDef",
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

ListJobsPaginateResponseJobListOutputLocationTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListOutputLocationTypeDef",
    {"S3": ListJobsPaginateResponseJobListOutputLocationS3TypeDef},
    total=False,
)

ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef",
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

ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef",
    {"csv": ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef},
    total=False,
)

ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef",
    {"csv": ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)

ListJobsPaginateResponseJobListSelectParametersTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListSelectParametersTypeDef",
    {
        "InputSerialization": ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ListJobsPaginateResponseJobListTypeDef = TypedDict(
    "ListJobsPaginateResponseJobListTypeDef",
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

ListJobsPaginateResponseTypeDef = TypedDict(
    "ListJobsPaginateResponseTypeDef",
    {"JobList": List[ListJobsPaginateResponseJobListTypeDef], "NextToken": str},
    total=False,
)

ListMultipartUploadsPaginatePaginationConfigTypeDef = TypedDict(
    "ListMultipartUploadsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListMultipartUploadsPaginateResponseUploadsListTypeDef = TypedDict(
    "ListMultipartUploadsPaginateResponseUploadsListTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)

ListMultipartUploadsPaginateResponseTypeDef = TypedDict(
    "ListMultipartUploadsPaginateResponseTypeDef",
    {"UploadsList": List[ListMultipartUploadsPaginateResponseUploadsListTypeDef], "NextToken": str},
    total=False,
)

ListPartsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPartsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPartsPaginateResponsePartsTypeDef = TypedDict(
    "ListPartsPaginateResponsePartsTypeDef",
    {"RangeInBytes": str, "SHA256TreeHash": str},
    total=False,
)

ListPartsPaginateResponseTypeDef = TypedDict(
    "ListPartsPaginateResponseTypeDef",
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

ListVaultsPaginatePaginationConfigTypeDef = TypedDict(
    "ListVaultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListVaultsPaginateResponseVaultListTypeDef = TypedDict(
    "ListVaultsPaginateResponseVaultListTypeDef",
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

ListVaultsPaginateResponseTypeDef = TypedDict(
    "ListVaultsPaginateResponseTypeDef",
    {"VaultList": List[ListVaultsPaginateResponseVaultListTypeDef], "NextToken": str},
    total=False,
)

MultipartUploadCompleteResponseTypeDef = TypedDict(
    "MultipartUploadCompleteResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)

MultipartUploadPartsResponsePartsTypeDef = TypedDict(
    "MultipartUploadPartsResponsePartsTypeDef",
    {"RangeInBytes": str, "SHA256TreeHash": str},
    total=False,
)

MultipartUploadPartsResponseTypeDef = TypedDict(
    "MultipartUploadPartsResponseTypeDef",
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

MultipartUploadUploadPartResponseTypeDef = TypedDict(
    "MultipartUploadUploadPartResponseTypeDef", {"checksum": str}, total=False
)

NotificationSetVaultNotificationConfigTypeDef = TypedDict(
    "NotificationSetVaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)

VaultCreateResponseTypeDef = TypedDict("VaultCreateResponseTypeDef", {"location": str}, total=False)

VaultExistsWaitWaiterConfigTypeDef = TypedDict(
    "VaultExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

VaultNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "VaultNotExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
