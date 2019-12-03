"Main interface for s3control service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateJobManifestLocationTypeDef",
    "ClientCreateJobManifestSpecTypeDef",
    "ClientCreateJobManifestTypeDef",
    "ClientCreateJobOperationLambdaInvokeTypeDef",
    "ClientCreateJobOperationS3InitiateRestoreObjectTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    "ClientCreateJobOperationS3PutObjectAclTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyTypeDef",
    "ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef",
    "ClientCreateJobOperationS3PutObjectTaggingTypeDef",
    "ClientCreateJobOperationTypeDef",
    "ClientCreateJobReportTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientDescribeJobResponseJobFailureReasonsTypeDef",
    "ClientDescribeJobResponseJobManifestLocationTypeDef",
    "ClientDescribeJobResponseJobManifestSpecTypeDef",
    "ClientDescribeJobResponseJobManifestTypeDef",
    "ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef",
    "ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef",
    "ClientDescribeJobResponseJobOperationTypeDef",
    "ClientDescribeJobResponseJobProgressSummaryTypeDef",
    "ClientDescribeJobResponseJobReportTypeDef",
    "ClientDescribeJobResponseJobTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    "ClientGetPublicAccessBlockResponseTypeDef",
    "ClientListJobsResponseJobsProgressSummaryTypeDef",
    "ClientListJobsResponseJobsTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    "ClientUpdateJobPriorityResponseTypeDef",
    "ClientUpdateJobStatusResponseTypeDef",
)


_ClientCreateJobManifestLocationTypeDef = TypedDict(
    "_ClientCreateJobManifestLocationTypeDef",
    {"ObjectArn": str, "ObjectVersionId": str, "ETag": str},
    total=False,
)


class ClientCreateJobManifestLocationTypeDef(_ClientCreateJobManifestLocationTypeDef):
    pass


_RequiredClientCreateJobManifestSpecTypeDef = TypedDict(
    "_RequiredClientCreateJobManifestSpecTypeDef",
    {"Format": Literal["S3BatchOperations_CSV_20180820", "S3InventoryReport_CSV_20161130"]},
)
_OptionalClientCreateJobManifestSpecTypeDef = TypedDict(
    "_OptionalClientCreateJobManifestSpecTypeDef",
    {"Fields": List[Literal["Ignore", "Bucket", "Key", "VersionId"]]},
    total=False,
)


class ClientCreateJobManifestSpecTypeDef(
    _RequiredClientCreateJobManifestSpecTypeDef, _OptionalClientCreateJobManifestSpecTypeDef
):
    """
    - **Spec** *(dict) --***[REQUIRED]**

      Describes the format of the specified job's manifest. If the manifest is in CSV format, also
      describes the columns contained within the manifest.
      - **Format** *(string) --***[REQUIRED]**

        Indicates which of the available formats the specified manifest uses.
    """


_RequiredClientCreateJobManifestTypeDef = TypedDict(
    "_RequiredClientCreateJobManifestTypeDef", {"Spec": ClientCreateJobManifestSpecTypeDef}
)
_OptionalClientCreateJobManifestTypeDef = TypedDict(
    "_OptionalClientCreateJobManifestTypeDef",
    {"Location": ClientCreateJobManifestLocationTypeDef},
    total=False,
)


class ClientCreateJobManifestTypeDef(
    _RequiredClientCreateJobManifestTypeDef, _OptionalClientCreateJobManifestTypeDef
):
    """
    Configuration parameters for the manifest.
    - **Spec** *(dict) --***[REQUIRED]**

      Describes the format of the specified job's manifest. If the manifest is in CSV format, also
      describes the columns contained within the manifest.
      - **Format** *(string) --***[REQUIRED]**

        Indicates which of the available formats the specified manifest uses.
    """


_ClientCreateJobOperationLambdaInvokeTypeDef = TypedDict(
    "_ClientCreateJobOperationLambdaInvokeTypeDef", {"FunctionArn": str}, total=False
)


class ClientCreateJobOperationLambdaInvokeTypeDef(_ClientCreateJobOperationLambdaInvokeTypeDef):
    """
    - **LambdaInvoke** *(dict) --*

      Directs the specified job to invoke an AWS Lambda function on each object in the manifest.
      - **FunctionArn** *(string) --*

        The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will
        invoke for each object in the manifest.
    """


_ClientCreateJobOperationS3InitiateRestoreObjectTypeDef = TypedDict(
    "_ClientCreateJobOperationS3InitiateRestoreObjectTypeDef",
    {"ExpirationInDays": int, "GlacierJobTier": Literal["BULK", "STANDARD"]},
    total=False,
)


class ClientCreateJobOperationS3InitiateRestoreObjectTypeDef(
    _ClientCreateJobOperationS3InitiateRestoreObjectTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    {"TypeIdentifier": Literal["id", "emailAddress", "uri"], "Identifier": str, "DisplayName": str},
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef(
    _ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    {
        "Grantee": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE", "READ_ACP", "WRITE_ACP"],
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef(
    _ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef(
    _ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    {
        "Owner": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef,
        "Grants": List[
            ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
        ],
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef(
    _ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    {
        "AccessControlList": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef,
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef(
    _ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectAclTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclTypeDef",
    {"AccessControlPolicy": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef},
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclTypeDef(_ClientCreateJobOperationS3PutObjectAclTypeDef):
    pass


_ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    {"TypeIdentifier": Literal["id", "emailAddress", "uri"], "Identifier": str, "DisplayName": str},
    total=False,
)


class ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    {
        "Grantee": ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE", "READ_ACP", "WRITE_ACP"],
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Dict[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": datetime,
        "RequesterCharged": bool,
        "SSEAlgorithm": Literal["AES256", "KMS"],
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectCopyTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlGrants": List[
            ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
        ],
        "MetadataDirective": Literal["COPY", "REPLACE"],
        "ModifiedSinceConstraint": datetime,
        "NewObjectMetadata": ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef,
        "NewObjectTagging": List[ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": Literal[
            "STANDARD",
            "STANDARD_IA",
            "ONEZONE_IA",
            "GLACIER",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "UnModifiedSinceConstraint": datetime,
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": Literal["OFF", "ON"],
        "ObjectLockMode": Literal["COMPLIANCE", "GOVERNANCE"],
        "ObjectLockRetainUntilDate": datetime,
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectCopyTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef(
    _ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef
):
    pass


_ClientCreateJobOperationS3PutObjectTaggingTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectTaggingTypeDef",
    {"TagSet": List[ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef]},
    total=False,
)


class ClientCreateJobOperationS3PutObjectTaggingTypeDef(
    _ClientCreateJobOperationS3PutObjectTaggingTypeDef
):
    pass


_ClientCreateJobOperationTypeDef = TypedDict(
    "_ClientCreateJobOperationTypeDef",
    {
        "LambdaInvoke": ClientCreateJobOperationLambdaInvokeTypeDef,
        "S3PutObjectCopy": ClientCreateJobOperationS3PutObjectCopyTypeDef,
        "S3PutObjectAcl": ClientCreateJobOperationS3PutObjectAclTypeDef,
        "S3PutObjectTagging": ClientCreateJobOperationS3PutObjectTaggingTypeDef,
        "S3InitiateRestoreObject": ClientCreateJobOperationS3InitiateRestoreObjectTypeDef,
    },
    total=False,
)


class ClientCreateJobOperationTypeDef(_ClientCreateJobOperationTypeDef):
    """
    The operation that you want this job to perform on each object listed in the manifest. For more
    information about the available operations, see `Available Operations
    <https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html>`__ in the *Amazon
    Simple Storage Service Developer Guide* .
    - **LambdaInvoke** *(dict) --*

      Directs the specified job to invoke an AWS Lambda function on each object in the manifest.
      - **FunctionArn** *(string) --*

        The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will
        invoke for each object in the manifest.
    """


_ClientCreateJobReportTypeDef = TypedDict(
    "_ClientCreateJobReportTypeDef",
    {
        "Bucket": str,
        "Format": str,
        "Enabled": bool,
        "Prefix": str,
        "ReportScope": Literal["AllTasks", "FailedTasksOnly"],
    },
    total=False,
)


class ClientCreateJobReportTypeDef(_ClientCreateJobReportTypeDef):
    """
    Configuration parameters for the optional job-completion report.
    - **Bucket** *(string) --*

      The bucket where specified job-completion report will be stored.
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef", {"JobId": str}, total=False
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The ID for this job. Amazon S3 generates this ID automatically and returns it after a
        successful ``Create Job`` request.
    """


_ClientDescribeJobResponseJobFailureReasonsTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobFailureReasonsTypeDef",
    {"FailureCode": str, "FailureReason": str},
    total=False,
)


class ClientDescribeJobResponseJobFailureReasonsTypeDef(
    _ClientDescribeJobResponseJobFailureReasonsTypeDef
):
    pass


_ClientDescribeJobResponseJobManifestLocationTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobManifestLocationTypeDef",
    {"ObjectArn": str, "ObjectVersionId": str, "ETag": str},
    total=False,
)


class ClientDescribeJobResponseJobManifestLocationTypeDef(
    _ClientDescribeJobResponseJobManifestLocationTypeDef
):
    pass


_ClientDescribeJobResponseJobManifestSpecTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobManifestSpecTypeDef",
    {
        "Format": Literal["S3BatchOperations_CSV_20180820", "S3InventoryReport_CSV_20161130"],
        "Fields": List[Literal["Ignore", "Bucket", "Key", "VersionId"]],
    },
    total=False,
)


class ClientDescribeJobResponseJobManifestSpecTypeDef(
    _ClientDescribeJobResponseJobManifestSpecTypeDef
):
    pass


_ClientDescribeJobResponseJobManifestTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobManifestTypeDef",
    {
        "Spec": ClientDescribeJobResponseJobManifestSpecTypeDef,
        "Location": ClientDescribeJobResponseJobManifestLocationTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseJobManifestTypeDef(_ClientDescribeJobResponseJobManifestTypeDef):
    pass


_ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef", {"FunctionArn": str}, total=False
)


class ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef(
    _ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef",
    {"ExpirationInDays": int, "GlacierJobTier": Literal["BULK", "STANDARD"]},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef(
    _ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    {"TypeIdentifier": Literal["id", "emailAddress", "uri"], "Identifier": str, "DisplayName": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    {
        "Grantee": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE", "READ_ACP", "WRITE_ACP"],
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    {
        "Owner": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef,
        "Grants": List[
            ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    {
        "AccessControlList": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef,
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef",
    {
        "AccessControlPolicy": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    {"TypeIdentifier": Literal["id", "emailAddress", "uri"], "Identifier": str, "DisplayName": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    {
        "Grantee": ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE", "READ_ACP", "WRITE_ACP"],
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Dict[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": datetime,
        "RequesterCharged": bool,
        "SSEAlgorithm": Literal["AES256", "KMS"],
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": Literal[
            "private",
            "public-read",
            "public-read-write",
            "aws-exec-read",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlGrants": List[
            ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
        ],
        "MetadataDirective": Literal["COPY", "REPLACE"],
        "ModifiedSinceConstraint": datetime,
        "NewObjectMetadata": ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef,
        "NewObjectTagging": List[
            ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef
        ],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": Literal[
            "STANDARD",
            "STANDARD_IA",
            "ONEZONE_IA",
            "GLACIER",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "UnModifiedSinceConstraint": datetime,
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": Literal["OFF", "ON"],
        "ObjectLockMode": Literal["COMPLIANCE", "GOVERNANCE"],
        "ObjectLockRetainUntilDate": datetime,
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef",
    {"TagSet": List[ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef]},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef
):
    pass


_ClientDescribeJobResponseJobOperationTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationTypeDef",
    {
        "LambdaInvoke": ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef,
        "S3PutObjectCopy": ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef,
        "S3PutObjectAcl": ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef,
        "S3PutObjectTagging": ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef,
        "S3InitiateRestoreObject": ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationTypeDef(_ClientDescribeJobResponseJobOperationTypeDef):
    pass


_ClientDescribeJobResponseJobProgressSummaryTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobProgressSummaryTypeDef",
    {"TotalNumberOfTasks": int, "NumberOfTasksSucceeded": int, "NumberOfTasksFailed": int},
    total=False,
)


class ClientDescribeJobResponseJobProgressSummaryTypeDef(
    _ClientDescribeJobResponseJobProgressSummaryTypeDef
):
    pass


_ClientDescribeJobResponseJobReportTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobReportTypeDef",
    {
        "Bucket": str,
        "Format": str,
        "Enabled": bool,
        "Prefix": str,
        "ReportScope": Literal["AllTasks", "FailedTasksOnly"],
    },
    total=False,
)


class ClientDescribeJobResponseJobReportTypeDef(_ClientDescribeJobResponseJobReportTypeDef):
    pass


_ClientDescribeJobResponseJobTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobTypeDef",
    {
        "JobId": str,
        "ConfirmationRequired": bool,
        "Description": str,
        "JobArn": str,
        "Status": Literal[
            "Active",
            "Cancelled",
            "Cancelling",
            "Complete",
            "Completing",
            "Failed",
            "Failing",
            "New",
            "Paused",
            "Pausing",
            "Preparing",
            "Ready",
            "Suspended",
        ],
        "Manifest": ClientDescribeJobResponseJobManifestTypeDef,
        "Operation": ClientDescribeJobResponseJobOperationTypeDef,
        "Priority": int,
        "ProgressSummary": ClientDescribeJobResponseJobProgressSummaryTypeDef,
        "StatusUpdateReason": str,
        "FailureReasons": List[ClientDescribeJobResponseJobFailureReasonsTypeDef],
        "Report": ClientDescribeJobResponseJobReportTypeDef,
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "RoleArn": str,
        "SuspendedDate": datetime,
        "SuspendedCause": str,
    },
    total=False,
)


class ClientDescribeJobResponseJobTypeDef(_ClientDescribeJobResponseJobTypeDef):
    """
    - **Job** *(dict) --*

      Contains the configuration parameters and status for the job specified in the ``Describe Job``
      request.
      - **JobId** *(string) --*

        The ID for the specified job.
    """


_ClientDescribeJobResponseTypeDef = TypedDict(
    "_ClientDescribeJobResponseTypeDef", {"Job": ClientDescribeJobResponseJobTypeDef}, total=False
)


class ClientDescribeJobResponseTypeDef(_ClientDescribeJobResponseTypeDef):
    """
    - *(dict) --*

      - **Job** *(dict) --*

        Contains the configuration parameters and status for the job specified in the ``Describe
        Job`` request.
        - **JobId** *(string) --*

          The ID for the specified job.
    """


_ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef = TypedDict(
    "_ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)


class ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef(
    _ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef
):
    """
    - **PublicAccessBlockConfiguration** *(dict) --*

      - **BlockPublicAcls** *(boolean) --*
      - **IgnorePublicAcls** *(boolean) --*
      - **BlockPublicPolicy** *(boolean) --*
      - **RestrictPublicBuckets** *(boolean) --*
    """


_ClientGetPublicAccessBlockResponseTypeDef = TypedDict(
    "_ClientGetPublicAccessBlockResponseTypeDef",
    {
        "PublicAccessBlockConfiguration": ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef
    },
    total=False,
)


class ClientGetPublicAccessBlockResponseTypeDef(_ClientGetPublicAccessBlockResponseTypeDef):
    """
    - *(dict) --*

      - **PublicAccessBlockConfiguration** *(dict) --*

        - **BlockPublicAcls** *(boolean) --*
        - **IgnorePublicAcls** *(boolean) --*
        - **BlockPublicPolicy** *(boolean) --*
        - **RestrictPublicBuckets** *(boolean) --*
    """


_ClientListJobsResponseJobsProgressSummaryTypeDef = TypedDict(
    "_ClientListJobsResponseJobsProgressSummaryTypeDef",
    {"TotalNumberOfTasks": int, "NumberOfTasksSucceeded": int, "NumberOfTasksFailed": int},
    total=False,
)


class ClientListJobsResponseJobsProgressSummaryTypeDef(
    _ClientListJobsResponseJobsProgressSummaryTypeDef
):
    pass


_ClientListJobsResponseJobsTypeDef = TypedDict(
    "_ClientListJobsResponseJobsTypeDef",
    {
        "JobId": str,
        "Description": str,
        "Operation": Literal[
            "LambdaInvoke",
            "S3PutObjectCopy",
            "S3PutObjectAcl",
            "S3PutObjectTagging",
            "S3InitiateRestoreObject",
        ],
        "Priority": int,
        "Status": Literal[
            "Active",
            "Cancelled",
            "Cancelling",
            "Complete",
            "Completing",
            "Failed",
            "Failing",
            "New",
            "Paused",
            "Pausing",
            "Preparing",
            "Ready",
            "Suspended",
        ],
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "ProgressSummary": ClientListJobsResponseJobsProgressSummaryTypeDef,
    },
    total=False,
)


class ClientListJobsResponseJobsTypeDef(_ClientListJobsResponseJobsTypeDef):
    pass


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"NextToken": str, "Jobs": List[ClientListJobsResponseJobsTypeDef]},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the ``List Jobs`` request produced more than the maximum number of results, you can pass
        this value into a subsequent ``List Jobs`` request in order to retrieve the next page of
        results.
    """


_ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef = TypedDict(
    "_ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)


class ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef(
    _ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef
):
    """
    - **BlockPublicAcls** *(boolean) --*
    - **IgnorePublicAcls** *(boolean) --*
    - **BlockPublicPolicy** *(boolean) --*
    - **RestrictPublicBuckets** *(boolean) --*
    """


_ClientUpdateJobPriorityResponseTypeDef = TypedDict(
    "_ClientUpdateJobPriorityResponseTypeDef", {"JobId": str, "Priority": int}, total=False
)


class ClientUpdateJobPriorityResponseTypeDef(_ClientUpdateJobPriorityResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The ID for the job whose priority Amazon S3 updated.
    """


_ClientUpdateJobStatusResponseTypeDef = TypedDict(
    "_ClientUpdateJobStatusResponseTypeDef",
    {
        "JobId": str,
        "Status": Literal[
            "Active",
            "Cancelled",
            "Cancelling",
            "Complete",
            "Completing",
            "Failed",
            "Failing",
            "New",
            "Paused",
            "Pausing",
            "Preparing",
            "Ready",
            "Suspended",
        ],
        "StatusUpdateReason": str,
    },
    total=False,
)


class ClientUpdateJobStatusResponseTypeDef(_ClientUpdateJobStatusResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The ID for the job whose status was updated.
    """
