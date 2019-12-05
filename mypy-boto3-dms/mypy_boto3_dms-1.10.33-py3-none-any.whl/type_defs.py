"Main interface for dms service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)

ClientApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
    },
    total=False,
)

ClientCreateEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientCreateEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientCreateEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientCreateEndpointDynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str}
)

_RequiredClientCreateEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointElasticsearchSettingsTypeDef", {"ServiceAccessRoleArn": str}
)
_OptionalClientCreateEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointElasticsearchSettingsTypeDef",
    {"EndpointUri": str, "FullLoadErrorPercentage": int, "ErrorRetryDuration": int},
    total=False,
)


class ClientCreateEndpointElasticsearchSettingsTypeDef(
    _RequiredClientCreateEndpointElasticsearchSettingsTypeDef,
    _OptionalClientCreateEndpointElasticsearchSettingsTypeDef,
):
    pass


ClientCreateEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientCreateEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientCreateEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientCreateEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientCreateEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientCreateEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)

ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef,
        "S3Settings": ClientCreateEndpointResponseEndpointS3SettingsTypeDef,
        "DmsTransferSettings": ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef,
        "KinesisSettings": ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef,
    },
    total=False,
)

ClientCreateEndpointResponseTypeDef = TypedDict(
    "ClientCreateEndpointResponseTypeDef",
    {"Endpoint": ClientCreateEndpointResponseEndpointTypeDef},
    total=False,
)

ClientCreateEndpointS3SettingsTypeDef = TypedDict(
    "ClientCreateEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientCreateEndpointTagsTypeDef = TypedDict(
    "ClientCreateEndpointTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

ClientCreateEventSubscriptionResponseTypeDef = TypedDict(
    "ClientCreateEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)

ClientCreateEventSubscriptionTagsTypeDef = TypedDict(
    "ClientCreateEventSubscriptionTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientCreateReplicationInstanceResponseTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)

ClientCreateReplicationInstanceTagsTypeDef = TypedDict(
    "ClientCreateReplicationInstanceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientCreateReplicationSubnetGroupResponseTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
    },
    total=False,
)

ClientCreateReplicationSubnetGroupTagsTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientCreateReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientCreateReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientCreateReplicationTaskResponseTypeDef = TypedDict(
    "ClientCreateReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientCreateReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientCreateReplicationTaskTagsTypeDef = TypedDict(
    "ClientCreateReplicationTaskTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteCertificateResponseCertificateTypeDef = TypedDict(
    "ClientDeleteCertificateResponseCertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

ClientDeleteCertificateResponseTypeDef = TypedDict(
    "ClientDeleteCertificateResponseTypeDef",
    {"Certificate": ClientDeleteCertificateResponseCertificateTypeDef},
    total=False,
)

ClientDeleteConnectionResponseConnectionTypeDef = TypedDict(
    "ClientDeleteConnectionResponseConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

ClientDeleteConnectionResponseTypeDef = TypedDict(
    "ClientDeleteConnectionResponseTypeDef",
    {"Connection": ClientDeleteConnectionResponseConnectionTypeDef},
    total=False,
)

ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)

ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientDeleteEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientDeleteEndpointResponseEndpointTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef,
        "S3Settings": ClientDeleteEndpointResponseEndpointS3SettingsTypeDef,
        "DmsTransferSettings": ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef,
        "KinesisSettings": ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef,
    },
    total=False,
)

ClientDeleteEndpointResponseTypeDef = TypedDict(
    "ClientDeleteEndpointResponseTypeDef",
    {"Endpoint": ClientDeleteEndpointResponseEndpointTypeDef},
    total=False,
)

ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

ClientDeleteEventSubscriptionResponseTypeDef = TypedDict(
    "ClientDeleteEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientDeleteReplicationInstanceResponseTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)

ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientDeleteReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientDeleteReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientDeleteReplicationTaskResponseTypeDef = TypedDict(
    "ClientDeleteReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientDeleteReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientDescribeAccountAttributesResponseAccountQuotasTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    {"AccountQuotaName": str, "Used": int, "Max": int},
    total=False,
)

ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseTypeDef",
    {
        "AccountQuotas": List[ClientDescribeAccountAttributesResponseAccountQuotasTypeDef],
        "UniqueAccountIdentifier": str,
    },
    total=False,
)

_RequiredClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeCertificatesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeCertificatesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeCertificatesFiltersTypeDef(
    _RequiredClientDescribeCertificatesFiltersTypeDef,
    _OptionalClientDescribeCertificatesFiltersTypeDef,
):
    pass


ClientDescribeCertificatesResponseCertificatesTypeDef = TypedDict(
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

ClientDescribeCertificatesResponseTypeDef = TypedDict(
    "ClientDescribeCertificatesResponseTypeDef",
    {"Marker": str, "Certificates": List[ClientDescribeCertificatesResponseCertificatesTypeDef]},
    total=False,
)

_RequiredClientDescribeConnectionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeConnectionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeConnectionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeConnectionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeConnectionsFiltersTypeDef(
    _RequiredClientDescribeConnectionsFiltersTypeDef,
    _OptionalClientDescribeConnectionsFiltersTypeDef,
):
    pass


ClientDescribeConnectionsResponseConnectionsTypeDef = TypedDict(
    "ClientDescribeConnectionsResponseConnectionsTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

ClientDescribeConnectionsResponseTypeDef = TypedDict(
    "ClientDescribeConnectionsResponseTypeDef",
    {"Marker": str, "Connections": List[ClientDescribeConnectionsResponseConnectionsTypeDef]},
    total=False,
)

_RequiredClientDescribeEndpointTypesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEndpointTypesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEndpointTypesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEndpointTypesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEndpointTypesFiltersTypeDef(
    _RequiredClientDescribeEndpointTypesFiltersTypeDef,
    _OptionalClientDescribeEndpointTypesFiltersTypeDef,
):
    pass


ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef = TypedDict(
    "ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": Literal["source", "target"],
        "EngineDisplayName": str,
    },
    total=False,
)

ClientDescribeEndpointTypesResponseTypeDef = TypedDict(
    "ClientDescribeEndpointTypesResponseTypeDef",
    {
        "Marker": str,
        "SupportedEndpointTypes": List[
            ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeEndpointsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEndpointsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEndpointsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEndpointsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEndpointsFiltersTypeDef(
    _RequiredClientDescribeEndpointsFiltersTypeDef, _OptionalClientDescribeEndpointsFiltersTypeDef
):
    pass


ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)

ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientDescribeEndpointsResponseEndpointsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef,
        "S3Settings": ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef,
        "DmsTransferSettings": ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef,
        "KinesisSettings": ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef,
    },
    total=False,
)

ClientDescribeEndpointsResponseTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseTypeDef",
    {"Marker": str, "Endpoints": List[ClientDescribeEndpointsResponseEndpointsTypeDef]},
    total=False,
)

_RequiredClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventCategoriesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventCategoriesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventCategoriesFiltersTypeDef(
    _RequiredClientDescribeEventCategoriesFiltersTypeDef,
    _OptionalClientDescribeEventCategoriesFiltersTypeDef,
):
    pass


ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef = TypedDict(
    "ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef",
    {"SourceType": str, "EventCategories": List[str]},
    total=False,
)

ClientDescribeEventCategoriesResponseTypeDef = TypedDict(
    "ClientDescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoryGroupList": List[
            ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef
        ]
    },
    total=False,
)

_RequiredClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventSubscriptionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventSubscriptionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventSubscriptionsFiltersTypeDef(
    _RequiredClientDescribeEventSubscriptionsFiltersTypeDef,
    _OptionalClientDescribeEventSubscriptionsFiltersTypeDef,
):
    pass


ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef = TypedDict(
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

ClientDescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "ClientDescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[
            ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeEventsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventsFiltersTypeDef(
    _RequiredClientDescribeEventsFiltersTypeDef, _OptionalClientDescribeEventsFiltersTypeDef
):
    pass


ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)

ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef = TypedDict(
    "ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef",
    {
        "EngineVersion": str,
        "ReplicationInstanceClass": str,
        "StorageType": str,
        "MinAllocatedStorage": int,
        "MaxAllocatedStorage": int,
        "DefaultAllocatedStorage": int,
        "IncludedAllocatedStorage": int,
        "AvailabilityZones": List[str],
        "ReleaseStatus": str,
    },
    total=False,
)

ClientDescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "ClientDescribeOrderableReplicationInstancesResponseTypeDef",
    {
        "OrderableReplicationInstances": List[
            ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

_RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribePendingMaintenanceActionsFiltersTypeDef(
    _RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef,
    _OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef,
):
    pass


ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)

ClientDescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef = TypedDict(
    "ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": Literal["successful", "failed", "refreshing"],
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

ClientDescribeRefreshSchemasStatusResponseTypeDef = TypedDict(
    "ClientDescribeRefreshSchemasStatusResponseTypeDef",
    {"RefreshSchemasStatus": ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef},
    total=False,
)

ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef = TypedDict(
    "ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef",
    {"ReplicationTaskName": str, "ReplicationTaskArn": str, "ReplicationInstanceTaskLogSize": int},
    total=False,
)

ClientDescribeReplicationInstanceTaskLogsResponseTypeDef = TypedDict(
    "ClientDescribeReplicationInstanceTaskLogsResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List[
            ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

_RequiredClientDescribeReplicationInstancesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeReplicationInstancesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeReplicationInstancesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeReplicationInstancesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeReplicationInstancesFiltersTypeDef(
    _RequiredClientDescribeReplicationInstancesFiltersTypeDef,
    _OptionalClientDescribeReplicationInstancesFiltersTypeDef,
):
    pass


ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientDescribeReplicationInstancesResponseTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReplicationInstances": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeReplicationSubnetGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeReplicationSubnetGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeReplicationSubnetGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeReplicationSubnetGroupsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeReplicationSubnetGroupsFiltersTypeDef(
    _RequiredClientDescribeReplicationSubnetGroupsFiltersTypeDef,
    _OptionalClientDescribeReplicationSubnetGroupsFiltersTypeDef,
):
    pass


ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef = TypedDict(
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef = TypedDict(
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeReplicationSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationSubnetGroups": List[
            ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef = TypedDict(
    "ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskLastAssessmentDate": datetime,
        "AssessmentStatus": str,
        "AssessmentResultsFile": str,
        "AssessmentResults": str,
        "S3ObjectUrl": str,
    },
    total=False,
)

ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List[
            ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeReplicationTasksFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeReplicationTasksFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeReplicationTasksFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeReplicationTasksFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeReplicationTasksFiltersTypeDef(
    _RequiredClientDescribeReplicationTasksFiltersTypeDef,
    _OptionalClientDescribeReplicationTasksFiltersTypeDef,
):
    pass


ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef = TypedDict(
    "ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientDescribeReplicationTasksResponseReplicationTasksTypeDef = TypedDict(
    "ClientDescribeReplicationTasksResponseReplicationTasksTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientDescribeReplicationTasksResponseTypeDef = TypedDict(
    "ClientDescribeReplicationTasksResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTasks": List[ClientDescribeReplicationTasksResponseReplicationTasksTypeDef],
    },
    total=False,
)

ClientDescribeSchemasResponseTypeDef = TypedDict(
    "ClientDescribeSchemasResponseTypeDef", {"Marker": str, "Schemas": List[str]}, total=False
)

_RequiredClientDescribeTableStatisticsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeTableStatisticsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeTableStatisticsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeTableStatisticsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeTableStatisticsFiltersTypeDef(
    _RequiredClientDescribeTableStatisticsFiltersTypeDef,
    _OptionalClientDescribeTableStatisticsFiltersTypeDef,
):
    pass


ClientDescribeTableStatisticsResponseTableStatisticsTypeDef = TypedDict(
    "ClientDescribeTableStatisticsResponseTableStatisticsTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
        "Inserts": int,
        "Deletes": int,
        "Updates": int,
        "Ddls": int,
        "FullLoadRows": int,
        "FullLoadCondtnlChkFailedRows": int,
        "FullLoadErrorRows": int,
        "LastUpdateTime": datetime,
        "TableState": str,
        "ValidationPendingRecords": int,
        "ValidationFailedRecords": int,
        "ValidationSuspendedRecords": int,
        "ValidationState": str,
        "ValidationStateDetails": str,
    },
    total=False,
)

ClientDescribeTableStatisticsResponseTypeDef = TypedDict(
    "ClientDescribeTableStatisticsResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List[ClientDescribeTableStatisticsResponseTableStatisticsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientImportCertificateResponseCertificateTypeDef = TypedDict(
    "ClientImportCertificateResponseCertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

ClientImportCertificateResponseTypeDef = TypedDict(
    "ClientImportCertificateResponseTypeDef",
    {"Certificate": ClientImportCertificateResponseCertificateTypeDef},
    total=False,
)

ClientImportCertificateTagsTypeDef = TypedDict(
    "ClientImportCertificateTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

ClientModifyEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientModifyEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientModifyEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientModifyEndpointDynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str}
)

_RequiredClientModifyEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredClientModifyEndpointElasticsearchSettingsTypeDef", {"ServiceAccessRoleArn": str}
)
_OptionalClientModifyEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalClientModifyEndpointElasticsearchSettingsTypeDef",
    {"EndpointUri": str, "FullLoadErrorPercentage": int, "ErrorRetryDuration": int},
    total=False,
)


class ClientModifyEndpointElasticsearchSettingsTypeDef(
    _RequiredClientModifyEndpointElasticsearchSettingsTypeDef,
    _OptionalClientModifyEndpointElasticsearchSettingsTypeDef,
):
    pass


ClientModifyEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientModifyEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientModifyEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientModifyEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientModifyEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientModifyEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)

ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef,
        "S3Settings": ClientModifyEndpointResponseEndpointS3SettingsTypeDef,
        "DmsTransferSettings": ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef,
        "KinesisSettings": ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef,
    },
    total=False,
)

ClientModifyEndpointResponseTypeDef = TypedDict(
    "ClientModifyEndpointResponseTypeDef",
    {"Endpoint": ClientModifyEndpointResponseEndpointTypeDef},
    total=False,
)

ClientModifyEndpointS3SettingsTypeDef = TypedDict(
    "ClientModifyEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

ClientModifyEventSubscriptionResponseTypeDef = TypedDict(
    "ClientModifyEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientModifyReplicationInstanceResponseTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)

ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef = TypedDict(
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientModifyReplicationSubnetGroupResponseTypeDef = TypedDict(
    "ClientModifyReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
    },
    total=False,
)

ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientModifyReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientModifyReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientModifyReplicationTaskResponseTypeDef = TypedDict(
    "ClientModifyReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientModifyReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientRebootReplicationInstanceResponseTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)

ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef = TypedDict(
    "ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": Literal["successful", "failed", "refreshing"],
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

ClientRefreshSchemasResponseTypeDef = TypedDict(
    "ClientRefreshSchemasResponseTypeDef",
    {"RefreshSchemasStatus": ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef},
    total=False,
)

ClientReloadTablesResponseTypeDef = TypedDict(
    "ClientReloadTablesResponseTypeDef", {"ReplicationTaskArn": str}, total=False
)

ClientReloadTablesTablesToReloadTypeDef = TypedDict(
    "ClientReloadTablesTablesToReloadTypeDef", {"SchemaName": str, "TableName": str}, total=False
)

ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef = TypedDict(
    "ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientStartReplicationTaskAssessmentResponseTypeDef = TypedDict(
    "ClientStartReplicationTaskAssessmentResponseTypeDef",
    {"ReplicationTask": ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef},
    total=False,
)

ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientStartReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientStartReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientStartReplicationTaskResponseTypeDef = TypedDict(
    "ClientStartReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientStartReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientStopReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientStopReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientStopReplicationTaskResponseTypeDef = TypedDict(
    "ClientStopReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientStopReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientTestConnectionResponseConnectionTypeDef = TypedDict(
    "ClientTestConnectionResponseConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

ClientTestConnectionResponseTypeDef = TypedDict(
    "ClientTestConnectionResponseTypeDef",
    {"Connection": ClientTestConnectionResponseConnectionTypeDef},
    total=False,
)

_RequiredDescribeCertificatesPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeCertificatesPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeCertificatesPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeCertificatesPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeCertificatesPaginateFiltersTypeDef(
    _RequiredDescribeCertificatesPaginateFiltersTypeDef,
    _OptionalDescribeCertificatesPaginateFiltersTypeDef,
):
    pass


DescribeCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeCertificatesPaginateResponseCertificatesTypeDef = TypedDict(
    "DescribeCertificatesPaginateResponseCertificatesTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

DescribeCertificatesPaginateResponseTypeDef = TypedDict(
    "DescribeCertificatesPaginateResponseTypeDef",
    {
        "Certificates": List[DescribeCertificatesPaginateResponseCertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredDescribeConnectionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeConnectionsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeConnectionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeConnectionsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeConnectionsPaginateFiltersTypeDef(
    _RequiredDescribeConnectionsPaginateFiltersTypeDef,
    _OptionalDescribeConnectionsPaginateFiltersTypeDef,
):
    pass


DescribeConnectionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeConnectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeConnectionsPaginateResponseConnectionsTypeDef = TypedDict(
    "DescribeConnectionsPaginateResponseConnectionsTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

DescribeConnectionsPaginateResponseTypeDef = TypedDict(
    "DescribeConnectionsPaginateResponseTypeDef",
    {"Connections": List[DescribeConnectionsPaginateResponseConnectionsTypeDef], "NextToken": str},
    total=False,
)

_RequiredDescribeEndpointTypesPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeEndpointTypesPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeEndpointTypesPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeEndpointTypesPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeEndpointTypesPaginateFiltersTypeDef(
    _RequiredDescribeEndpointTypesPaginateFiltersTypeDef,
    _OptionalDescribeEndpointTypesPaginateFiltersTypeDef,
):
    pass


DescribeEndpointTypesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEndpointTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef = TypedDict(
    "DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": Literal["source", "target"],
        "EngineDisplayName": str,
    },
    total=False,
)

DescribeEndpointTypesPaginateResponseTypeDef = TypedDict(
    "DescribeEndpointTypesPaginateResponseTypeDef",
    {
        "SupportedEndpointTypes": List[
            DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredDescribeEndpointsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeEndpointsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeEndpointsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeEndpointsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeEndpointsPaginateFiltersTypeDef(
    _RequiredDescribeEndpointsPaginateFiltersTypeDef,
    _OptionalDescribeEndpointsPaginateFiltersTypeDef,
):
    pass


DescribeEndpointsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEndpointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef = TypedDict(
    "DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef = TypedDict(
    "DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)

DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef = TypedDict(
    "DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef = TypedDict(
    "DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef = TypedDict(
    "DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef = TypedDict(
    "DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef = TypedDict(
    "DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

DescribeEndpointsPaginateResponseEndpointsTypeDef = TypedDict(
    "DescribeEndpointsPaginateResponseEndpointsTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef,
        "S3Settings": DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef,
        "DmsTransferSettings": DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef,
        "MongoDbSettings": DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef,
        "KinesisSettings": DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef,
        "ElasticsearchSettings": DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef,
        "RedshiftSettings": DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef,
    },
    total=False,
)

DescribeEndpointsPaginateResponseTypeDef = TypedDict(
    "DescribeEndpointsPaginateResponseTypeDef",
    {"Endpoints": List[DescribeEndpointsPaginateResponseEndpointsTypeDef], "NextToken": str},
    total=False,
)

_RequiredDescribeEventSubscriptionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeEventSubscriptionsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeEventSubscriptionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeEventSubscriptionsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeEventSubscriptionsPaginateFiltersTypeDef(
    _RequiredDescribeEventSubscriptionsPaginateFiltersTypeDef,
    _OptionalDescribeEventSubscriptionsPaginateFiltersTypeDef,
):
    pass


DescribeEventSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef = TypedDict(
    "DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

DescribeEventSubscriptionsPaginateResponseTypeDef = TypedDict(
    "DescribeEventSubscriptionsPaginateResponseTypeDef",
    {
        "EventSubscriptionsList": List[
            DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredDescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeEventsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeEventsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeEventsPaginateFiltersTypeDef(
    _RequiredDescribeEventsPaginateFiltersTypeDef, _OptionalDescribeEventsPaginateFiltersTypeDef
):
    pass


DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "DescribeEventsPaginateResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)

DescribeEventsPaginateResponseTypeDef = TypedDict(
    "DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef], "NextToken": str},
    total=False,
)

DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef",
    {
        "EngineVersion": str,
        "ReplicationInstanceClass": str,
        "StorageType": str,
        "MinAllocatedStorage": int,
        "MaxAllocatedStorage": int,
        "DefaultAllocatedStorage": int,
        "IncludedAllocatedStorage": int,
        "AvailabilityZones": List[str],
        "ReleaseStatus": str,
    },
    total=False,
)

DescribeOrderableReplicationInstancesPaginateResponseTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesPaginateResponseTypeDef",
    {
        "OrderableReplicationInstances": List[
            DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredDescribeReplicationInstancesPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeReplicationInstancesPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeReplicationInstancesPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeReplicationInstancesPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeReplicationInstancesPaginateFiltersTypeDef(
    _RequiredDescribeReplicationInstancesPaginateFiltersTypeDef,
    _OptionalDescribeReplicationInstancesPaginateFiltersTypeDef,
):
    pass


DescribeReplicationInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeReplicationInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef = TypedDict(
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef = TypedDict(
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef = TypedDict(
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

DescribeReplicationInstancesPaginateResponseTypeDef = TypedDict(
    "DescribeReplicationInstancesPaginateResponseTypeDef",
    {
        "ReplicationInstances": List[
            DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredDescribeReplicationSubnetGroupsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeReplicationSubnetGroupsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeReplicationSubnetGroupsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeReplicationSubnetGroupsPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeReplicationSubnetGroupsPaginateFiltersTypeDef(
    _RequiredDescribeReplicationSubnetGroupsPaginateFiltersTypeDef,
    _OptionalDescribeReplicationSubnetGroupsPaginateFiltersTypeDef,
):
    pass


DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef
        ],
    },
    total=False,
)

DescribeReplicationSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsPaginateResponseTypeDef",
    {
        "ReplicationSubnetGroups": List[
            DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskLastAssessmentDate": datetime,
        "AssessmentStatus": str,
        "AssessmentResultsFile": str,
        "AssessmentResults": str,
        "S3ObjectUrl": str,
    },
    total=False,
)

DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef",
    {
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List[
            DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredDescribeReplicationTasksPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeReplicationTasksPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeReplicationTasksPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeReplicationTasksPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeReplicationTasksPaginateFiltersTypeDef(
    _RequiredDescribeReplicationTasksPaginateFiltersTypeDef,
    _OptionalDescribeReplicationTasksPaginateFiltersTypeDef,
):
    pass


DescribeReplicationTasksPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeReplicationTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeReplicationTasksPaginateResponseReplicationTasksReplicationTaskStatsTypeDef = TypedDict(
    "DescribeReplicationTasksPaginateResponseReplicationTasksReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

DescribeReplicationTasksPaginateResponseReplicationTasksTypeDef = TypedDict(
    "DescribeReplicationTasksPaginateResponseReplicationTasksTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": DescribeReplicationTasksPaginateResponseReplicationTasksReplicationTaskStatsTypeDef,
    },
    total=False,
)

DescribeReplicationTasksPaginateResponseTypeDef = TypedDict(
    "DescribeReplicationTasksPaginateResponseTypeDef",
    {
        "ReplicationTasks": List[DescribeReplicationTasksPaginateResponseReplicationTasksTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeSchemasPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeSchemasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeSchemasPaginateResponseTypeDef = TypedDict(
    "DescribeSchemasPaginateResponseTypeDef", {"Schemas": List[str], "NextToken": str}, total=False
)

_RequiredDescribeTableStatisticsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeTableStatisticsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeTableStatisticsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeTableStatisticsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeTableStatisticsPaginateFiltersTypeDef(
    _RequiredDescribeTableStatisticsPaginateFiltersTypeDef,
    _OptionalDescribeTableStatisticsPaginateFiltersTypeDef,
):
    pass


DescribeTableStatisticsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeTableStatisticsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef = TypedDict(
    "DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
        "Inserts": int,
        "Deletes": int,
        "Updates": int,
        "Ddls": int,
        "FullLoadRows": int,
        "FullLoadCondtnlChkFailedRows": int,
        "FullLoadErrorRows": int,
        "LastUpdateTime": datetime,
        "TableState": str,
        "ValidationPendingRecords": int,
        "ValidationFailedRecords": int,
        "ValidationSuspendedRecords": int,
        "ValidationState": str,
        "ValidationStateDetails": str,
    },
    total=False,
)

DescribeTableStatisticsPaginateResponseTypeDef = TypedDict(
    "DescribeTableStatisticsPaginateResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List[DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredEndpointDeletedWaitFiltersTypeDef = TypedDict(
    "_RequiredEndpointDeletedWaitFiltersTypeDef", {"Name": str}
)
_OptionalEndpointDeletedWaitFiltersTypeDef = TypedDict(
    "_OptionalEndpointDeletedWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class EndpointDeletedWaitFiltersTypeDef(
    _RequiredEndpointDeletedWaitFiltersTypeDef, _OptionalEndpointDeletedWaitFiltersTypeDef
):
    pass


EndpointDeletedWaitWaiterConfigTypeDef = TypedDict(
    "EndpointDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

_RequiredReplicationInstanceAvailableWaitFiltersTypeDef = TypedDict(
    "_RequiredReplicationInstanceAvailableWaitFiltersTypeDef", {"Name": str}
)
_OptionalReplicationInstanceAvailableWaitFiltersTypeDef = TypedDict(
    "_OptionalReplicationInstanceAvailableWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class ReplicationInstanceAvailableWaitFiltersTypeDef(
    _RequiredReplicationInstanceAvailableWaitFiltersTypeDef,
    _OptionalReplicationInstanceAvailableWaitFiltersTypeDef,
):
    pass


ReplicationInstanceAvailableWaitWaiterConfigTypeDef = TypedDict(
    "ReplicationInstanceAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)

_RequiredReplicationInstanceDeletedWaitFiltersTypeDef = TypedDict(
    "_RequiredReplicationInstanceDeletedWaitFiltersTypeDef", {"Name": str}
)
_OptionalReplicationInstanceDeletedWaitFiltersTypeDef = TypedDict(
    "_OptionalReplicationInstanceDeletedWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class ReplicationInstanceDeletedWaitFiltersTypeDef(
    _RequiredReplicationInstanceDeletedWaitFiltersTypeDef,
    _OptionalReplicationInstanceDeletedWaitFiltersTypeDef,
):
    pass


ReplicationInstanceDeletedWaitWaiterConfigTypeDef = TypedDict(
    "ReplicationInstanceDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)

_RequiredReplicationTaskDeletedWaitFiltersTypeDef = TypedDict(
    "_RequiredReplicationTaskDeletedWaitFiltersTypeDef", {"Name": str}
)
_OptionalReplicationTaskDeletedWaitFiltersTypeDef = TypedDict(
    "_OptionalReplicationTaskDeletedWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class ReplicationTaskDeletedWaitFiltersTypeDef(
    _RequiredReplicationTaskDeletedWaitFiltersTypeDef,
    _OptionalReplicationTaskDeletedWaitFiltersTypeDef,
):
    pass


ReplicationTaskDeletedWaitWaiterConfigTypeDef = TypedDict(
    "ReplicationTaskDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

_RequiredReplicationTaskReadyWaitFiltersTypeDef = TypedDict(
    "_RequiredReplicationTaskReadyWaitFiltersTypeDef", {"Name": str}
)
_OptionalReplicationTaskReadyWaitFiltersTypeDef = TypedDict(
    "_OptionalReplicationTaskReadyWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class ReplicationTaskReadyWaitFiltersTypeDef(
    _RequiredReplicationTaskReadyWaitFiltersTypeDef, _OptionalReplicationTaskReadyWaitFiltersTypeDef
):
    pass


ReplicationTaskReadyWaitWaiterConfigTypeDef = TypedDict(
    "ReplicationTaskReadyWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

_RequiredReplicationTaskRunningWaitFiltersTypeDef = TypedDict(
    "_RequiredReplicationTaskRunningWaitFiltersTypeDef", {"Name": str}
)
_OptionalReplicationTaskRunningWaitFiltersTypeDef = TypedDict(
    "_OptionalReplicationTaskRunningWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class ReplicationTaskRunningWaitFiltersTypeDef(
    _RequiredReplicationTaskRunningWaitFiltersTypeDef,
    _OptionalReplicationTaskRunningWaitFiltersTypeDef,
):
    pass


ReplicationTaskRunningWaitWaiterConfigTypeDef = TypedDict(
    "ReplicationTaskRunningWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

_RequiredReplicationTaskStoppedWaitFiltersTypeDef = TypedDict(
    "_RequiredReplicationTaskStoppedWaitFiltersTypeDef", {"Name": str}
)
_OptionalReplicationTaskStoppedWaitFiltersTypeDef = TypedDict(
    "_OptionalReplicationTaskStoppedWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class ReplicationTaskStoppedWaitFiltersTypeDef(
    _RequiredReplicationTaskStoppedWaitFiltersTypeDef,
    _OptionalReplicationTaskStoppedWaitFiltersTypeDef,
):
    pass


ReplicationTaskStoppedWaitWaiterConfigTypeDef = TypedDict(
    "ReplicationTaskStoppedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

_RequiredTestConnectionSucceedsWaitFiltersTypeDef = TypedDict(
    "_RequiredTestConnectionSucceedsWaitFiltersTypeDef", {"Name": str}
)
_OptionalTestConnectionSucceedsWaitFiltersTypeDef = TypedDict(
    "_OptionalTestConnectionSucceedsWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class TestConnectionSucceedsWaitFiltersTypeDef(
    _RequiredTestConnectionSucceedsWaitFiltersTypeDef,
    _OptionalTestConnectionSucceedsWaitFiltersTypeDef,
):
    pass


TestConnectionSucceedsWaitWaiterConfigTypeDef = TypedDict(
    "TestConnectionSucceedsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
