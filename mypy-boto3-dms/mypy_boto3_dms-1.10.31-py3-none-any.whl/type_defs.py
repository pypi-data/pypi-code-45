"Main interface for dms service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    "ClientCreateEndpointDmsTransferSettingsTypeDef",
    "ClientCreateEndpointDynamoDbSettingsTypeDef",
    "ClientCreateEndpointElasticsearchSettingsTypeDef",
    "ClientCreateEndpointKinesisSettingsTypeDef",
    "ClientCreateEndpointMongoDbSettingsTypeDef",
    "ClientCreateEndpointRedshiftSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointS3SettingsTypeDef",
    "ClientCreateEndpointResponseEndpointTypeDef",
    "ClientCreateEndpointResponseTypeDef",
    "ClientCreateEndpointS3SettingsTypeDef",
    "ClientCreateEndpointTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientCreateReplicationInstanceResponseTypeDef",
    "ClientCreateReplicationInstanceTagsTypeDef",
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    "ClientCreateReplicationSubnetGroupResponseTypeDef",
    "ClientCreateReplicationSubnetGroupTagsTypeDef",
    "ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientCreateReplicationTaskResponseReplicationTaskTypeDef",
    "ClientCreateReplicationTaskResponseTypeDef",
    "ClientCreateReplicationTaskTagsTypeDef",
    "ClientDeleteCertificateResponseCertificateTypeDef",
    "ClientDeleteCertificateResponseTypeDef",
    "ClientDeleteConnectionResponseConnectionTypeDef",
    "ClientDeleteConnectionResponseTypeDef",
    "ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointS3SettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointTypeDef",
    "ClientDeleteEndpointResponseTypeDef",
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientDeleteEventSubscriptionResponseTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientDeleteReplicationInstanceResponseTypeDef",
    "ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientDeleteReplicationTaskResponseReplicationTaskTypeDef",
    "ClientDeleteReplicationTaskResponseTypeDef",
    "ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeCertificatesFiltersTypeDef",
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    "ClientDescribeCertificatesResponseTypeDef",
    "ClientDescribeConnectionsFiltersTypeDef",
    "ClientDescribeConnectionsResponseConnectionsTypeDef",
    "ClientDescribeConnectionsResponseTypeDef",
    "ClientDescribeEndpointTypesFiltersTypeDef",
    "ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef",
    "ClientDescribeEndpointTypesResponseTypeDef",
    "ClientDescribeEndpointsFiltersTypeDef",
    "ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsTypeDef",
    "ClientDescribeEndpointsResponseTypeDef",
    "ClientDescribeEventCategoriesFiltersTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventSubscriptionsFiltersTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    "ClientDescribeEventSubscriptionsResponseTypeDef",
    "ClientDescribeEventsFiltersTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef",
    "ClientDescribeOrderableReplicationInstancesResponseTypeDef",
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    "ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef",
    "ClientDescribeRefreshSchemasStatusResponseTypeDef",
    "ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef",
    "ClientDescribeReplicationInstanceTaskLogsResponseTypeDef",
    "ClientDescribeReplicationInstancesFiltersTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef",
    "ClientDescribeReplicationInstancesResponseTypeDef",
    "ClientDescribeReplicationSubnetGroupsFiltersTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseTypeDef",
    "ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef",
    "ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "ClientDescribeReplicationTasksFiltersTypeDef",
    "ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef",
    "ClientDescribeReplicationTasksResponseReplicationTasksTypeDef",
    "ClientDescribeReplicationTasksResponseTypeDef",
    "ClientDescribeSchemasResponseTypeDef",
    "ClientDescribeTableStatisticsFiltersTypeDef",
    "ClientDescribeTableStatisticsResponseTableStatisticsTypeDef",
    "ClientDescribeTableStatisticsResponseTypeDef",
    "ClientImportCertificateResponseCertificateTypeDef",
    "ClientImportCertificateResponseTypeDef",
    "ClientImportCertificateTagsTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyEndpointDmsTransferSettingsTypeDef",
    "ClientModifyEndpointDynamoDbSettingsTypeDef",
    "ClientModifyEndpointElasticsearchSettingsTypeDef",
    "ClientModifyEndpointKinesisSettingsTypeDef",
    "ClientModifyEndpointMongoDbSettingsTypeDef",
    "ClientModifyEndpointRedshiftSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointS3SettingsTypeDef",
    "ClientModifyEndpointResponseEndpointTypeDef",
    "ClientModifyEndpointResponseTypeDef",
    "ClientModifyEndpointS3SettingsTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientModifyReplicationInstanceResponseTypeDef",
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    "ClientModifyReplicationSubnetGroupResponseTypeDef",
    "ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientModifyReplicationTaskResponseReplicationTaskTypeDef",
    "ClientModifyReplicationTaskResponseTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientRebootReplicationInstanceResponseTypeDef",
    "ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef",
    "ClientRefreshSchemasResponseTypeDef",
    "ClientReloadTablesResponseTypeDef",
    "ClientReloadTablesTablesToReloadTypeDef",
    "ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef",
    "ClientStartReplicationTaskAssessmentResponseTypeDef",
    "ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientStartReplicationTaskResponseReplicationTaskTypeDef",
    "ClientStartReplicationTaskResponseTypeDef",
    "ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientStopReplicationTaskResponseReplicationTaskTypeDef",
    "ClientStopReplicationTaskResponseTypeDef",
    "ClientTestConnectionResponseConnectionTypeDef",
    "ClientTestConnectionResponseTypeDef",
    "DescribeCertificatesPaginateFiltersTypeDef",
    "DescribeCertificatesPaginatePaginationConfigTypeDef",
    "DescribeCertificatesPaginateResponseCertificatesTypeDef",
    "DescribeCertificatesPaginateResponseTypeDef",
    "DescribeConnectionsPaginateFiltersTypeDef",
    "DescribeConnectionsPaginatePaginationConfigTypeDef",
    "DescribeConnectionsPaginateResponseConnectionsTypeDef",
    "DescribeConnectionsPaginateResponseTypeDef",
    "DescribeEndpointTypesPaginateFiltersTypeDef",
    "DescribeEndpointTypesPaginatePaginationConfigTypeDef",
    "DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef",
    "DescribeEndpointTypesPaginateResponseTypeDef",
    "DescribeEndpointsPaginateFiltersTypeDef",
    "DescribeEndpointsPaginatePaginationConfigTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef",
    "DescribeEndpointsPaginateResponseEndpointsTypeDef",
    "DescribeEndpointsPaginateResponseTypeDef",
    "DescribeEventSubscriptionsPaginateFiltersTypeDef",
    "DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    "DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    "DescribeEventSubscriptionsPaginateResponseTypeDef",
    "DescribeEventsPaginateFiltersTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef",
    "DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef",
    "DescribeOrderableReplicationInstancesPaginateResponseTypeDef",
    "DescribeReplicationInstancesPaginateFiltersTypeDef",
    "DescribeReplicationInstancesPaginatePaginationConfigTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    "DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef",
    "DescribeReplicationInstancesPaginateResponseTypeDef",
    "DescribeReplicationSubnetGroupsPaginateFiltersTypeDef",
    "DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef",
    "DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef",
    "DescribeReplicationSubnetGroupsPaginateResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef",
    "DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef",
    "DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef",
    "DescribeReplicationTasksPaginateFiltersTypeDef",
    "DescribeReplicationTasksPaginatePaginationConfigTypeDef",
    "DescribeReplicationTasksPaginateResponseReplicationTasksReplicationTaskStatsTypeDef",
    "DescribeReplicationTasksPaginateResponseReplicationTasksTypeDef",
    "DescribeReplicationTasksPaginateResponseTypeDef",
    "DescribeSchemasPaginatePaginationConfigTypeDef",
    "DescribeSchemasPaginateResponseTypeDef",
    "DescribeTableStatisticsPaginateFiltersTypeDef",
    "DescribeTableStatisticsPaginatePaginationConfigTypeDef",
    "DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef",
    "DescribeTableStatisticsPaginateResponseTypeDef",
    "EndpointDeletedWaitFiltersTypeDef",
    "EndpointDeletedWaitWaiterConfigTypeDef",
    "ReplicationInstanceAvailableWaitFiltersTypeDef",
    "ReplicationInstanceAvailableWaitWaiterConfigTypeDef",
    "ReplicationInstanceDeletedWaitFiltersTypeDef",
    "ReplicationInstanceDeletedWaitWaiterConfigTypeDef",
    "ReplicationTaskDeletedWaitFiltersTypeDef",
    "ReplicationTaskDeletedWaitWaiterConfigTypeDef",
    "ReplicationTaskReadyWaitFiltersTypeDef",
    "ReplicationTaskReadyWaitWaiterConfigTypeDef",
    "ReplicationTaskRunningWaitFiltersTypeDef",
    "ReplicationTaskRunningWaitWaiterConfigTypeDef",
    "ReplicationTaskStoppedWaitFiltersTypeDef",
    "ReplicationTaskStoppedWaitWaiterConfigTypeDef",
    "TestConnectionSucceedsWaitFiltersTypeDef",
    "TestConnectionSucceedsWaitWaiterConfigTypeDef",
)


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
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


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    pass


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
):
    """
    - **ResourcePendingMaintenanceActions** *(dict) --*

      The AWS DMS resource that the pending maintenance action will be applied to.
      - **ResourceIdentifier** *(string) --*

        The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
        applies to. For information about creating an ARN, see `Constructing an Amazon Resource Name
        (ARN) for AWS DMS
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in the
        DMS documentation.
    """


_ClientApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseTypeDef(
    _ClientApplyPendingMaintenanceActionResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourcePendingMaintenanceActions** *(dict) --*

        The AWS DMS resource that the pending maintenance action will be applied to.
        - **ResourceIdentifier** *(string) --*

          The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
          applies to. For information about creating an ARN, see `Constructing an Amazon Resource
          Name (ARN) for AWS DMS
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in
          the DMS documentation.
    """


_ClientCreateEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientCreateEndpointDmsTransferSettingsTypeDef(
    _ClientCreateEndpointDmsTransferSettingsTypeDef
):
    """
    The settings in JSON format for the DMS transfer type of source endpoint.
    Possible settings include the following:
    * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3 bucket.
    * ``BucketName`` - The name of the S3 bucket to use.
    * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To use
    GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't use this
    value.
    Shorthand syntax for these settings is as follows:
    ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``
    JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
    "BucketName": "string", "CompressionType": "none"|"gzip" }``
    - **ServiceAccessRoleArn** *(string) --*

      The IAM role that has permission to access the Amazon S3 bucket.
    """


_ClientCreateEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointDynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str}
)


class ClientCreateEndpointDynamoDbSettingsTypeDef(_ClientCreateEndpointDynamoDbSettingsTypeDef):
    """
    Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the
    available settings, see `Using Object Mapping to Migrate Data to DynamoDB
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html>`__ in the *AWS
    Database Migration Service User Guide.*
    - **ServiceAccessRoleArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


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
    """
    Settings in JSON format for the target Elasticsearch endpoint. For more information about the
    available settings, see `Extra Connection Attributes When Using Elasticsearch as a Target for
    AWS DMS
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`__
    in the *AWS Database Migration User Guide.*
    - **ServiceAccessRoleArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) used by service to access the IAM role.
    """


_ClientCreateEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientCreateEndpointKinesisSettingsTypeDef(_ClientCreateEndpointKinesisSettingsTypeDef):
    """
    Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. For more
    information about the available settings, see `Using Object Mapping to Migrate Data to a Kinesis
    Data Stream
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`__
    in the *AWS Database Migration User Guide.*
    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.
    """


_ClientCreateEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointMongoDbSettingsTypeDef",
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


class ClientCreateEndpointMongoDbSettingsTypeDef(_ClientCreateEndpointMongoDbSettingsTypeDef):
    """
    Settings in JSON format for the source MongoDB endpoint. For more information about the
    available settings, see the configuration properties section in `Using MongoDB as a Target for
    AWS Database Migration Service
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html>`__ in the *AWS
    Database Migration Service User Guide.*
    - **Username** *(string) --*

      The user name you use to access the MongoDB source endpoint.
    """


_ClientCreateEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointRedshiftSettingsTypeDef",
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


class ClientCreateEndpointRedshiftSettingsTypeDef(_ClientCreateEndpointRedshiftSettingsTypeDef):
    """
    - **AcceptAnyDate** *(boolean) --*

      A value that indicates to allow any date format, including invalid formats such as 00/00/00
      00:00:00, to be loaded without generating an error. You can choose ``true`` or ``false`` (the
      default).
      This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the
      DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
      specification, Amazon Redshift inserts a NULL value into that field.
    """


_ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef
):
    pass


_ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef
):
    pass


_ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef
):
    pass


_ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef
):
    pass


_ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef",
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


class ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef
):
    pass


_ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef",
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


class ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef(
    _ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef
):
    pass


_ClientCreateEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointS3SettingsTypeDef",
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


class ClientCreateEndpointResponseEndpointS3SettingsTypeDef(
    _ClientCreateEndpointResponseEndpointS3SettingsTypeDef
):
    pass


_ClientCreateEndpointResponseEndpointTypeDef = TypedDict(
    "_ClientCreateEndpointResponseEndpointTypeDef",
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


class ClientCreateEndpointResponseEndpointTypeDef(_ClientCreateEndpointResponseEndpointTypeDef):
    """
    - **Endpoint** *(dict) --*

      The endpoint that was created.
      - **EndpointIdentifier** *(string) --*

        The database endpoint identifier. Identifiers must begin with a letter; must contain only
        ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
        consecutive hyphens.
    """


_ClientCreateEndpointResponseTypeDef = TypedDict(
    "_ClientCreateEndpointResponseTypeDef",
    {"Endpoint": ClientCreateEndpointResponseEndpointTypeDef},
    total=False,
)


class ClientCreateEndpointResponseTypeDef(_ClientCreateEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **Endpoint** *(dict) --*

        The endpoint that was created.
        - **EndpointIdentifier** *(string) --*

          The database endpoint identifier. Identifiers must begin with a letter; must contain only
          ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
          consecutive hyphens.
    """


_ClientCreateEndpointS3SettingsTypeDef = TypedDict(
    "_ClientCreateEndpointS3SettingsTypeDef",
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


class ClientCreateEndpointS3SettingsTypeDef(_ClientCreateEndpointS3SettingsTypeDef):
    """
    Settings in JSON format for the target Amazon S3 endpoint. For more information about the
    available settings, see `Extra Connection Attributes When Using Amazon S3 as a Target for AWS
    DMS
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`__
    in the *AWS Database Migration Service User Guide.*
    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


_ClientCreateEndpointTagsTypeDef = TypedDict(
    "_ClientCreateEndpointTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEndpointTagsTypeDef(_ClientCreateEndpointTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
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


class ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      The event subscription that was created.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the AWS DMS event notification subscription.
    """


_ClientCreateEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)


class ClientCreateEventSubscriptionResponseTypeDef(_ClientCreateEventSubscriptionResponseTypeDef):
    """
    - *(dict) --*

      - **EventSubscription** *(dict) --*

        The event subscription that was created.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the AWS DMS event notification subscription.
    """


_ClientCreateEventSubscriptionTagsTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEventSubscriptionTagsTypeDef(_ClientCreateEventSubscriptionTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef
):
    pass


_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
):
    pass


_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
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


class ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef
):
    pass


_ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef",
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


class ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef(
    _ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef
):
    """
    - **ReplicationInstance** *(dict) --*

      The replication instance that was created.
      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.
        Constraints:
        * Must contain from 1 to 63 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
        Example: ``myrepinstance``
    """


_ClientCreateReplicationInstanceResponseTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)


class ClientCreateReplicationInstanceResponseTypeDef(
    _ClientCreateReplicationInstanceResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationInstance** *(dict) --*

        The replication instance that was created.
        - **ReplicationInstanceIdentifier** *(string) --*

          The replication instance identifier. This parameter is stored as a lowercase string.
          Constraints:
          * Must contain from 1 to 63 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``myrepinstance``
    """


_ClientCreateReplicationInstanceTagsTypeDef = TypedDict(
    "_ClientCreateReplicationInstanceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateReplicationInstanceTagsTypeDef(_ClientCreateReplicationInstanceTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef(
    _ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
):
    pass


_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
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


class ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef(
    _ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
):
    """
    - **ReplicationSubnetGroup** *(dict) --*

      The replication subnet group that was created.
      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.
    """


_ClientCreateReplicationSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
    },
    total=False,
)


class ClientCreateReplicationSubnetGroupResponseTypeDef(
    _ClientCreateReplicationSubnetGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationSubnetGroup** *(dict) --*

        The replication subnet group that was created.
        - **ReplicationSubnetGroupIdentifier** *(string) --*

          The identifier of the replication instance subnet group.
    """


_ClientCreateReplicationSubnetGroupTagsTypeDef = TypedDict(
    "_ClientCreateReplicationSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateReplicationSubnetGroupTagsTypeDef(_ClientCreateReplicationSubnetGroupTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "_ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
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


class ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef(
    _ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef
):
    pass


_ClientCreateReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "_ClientCreateReplicationTaskResponseReplicationTaskTypeDef",
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


class ClientCreateReplicationTaskResponseReplicationTaskTypeDef(
    _ClientCreateReplicationTaskResponseReplicationTaskTypeDef
):
    """
    - **ReplicationTask** *(dict) --*

      The replication task that was created.
      - **ReplicationTaskIdentifier** *(string) --*

        The user-assigned replication task identifier or name.
        Constraints:
        * Must contain from 1 to 255 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientCreateReplicationTaskResponseTypeDef = TypedDict(
    "_ClientCreateReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientCreateReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)


class ClientCreateReplicationTaskResponseTypeDef(_ClientCreateReplicationTaskResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationTask** *(dict) --*

        The replication task that was created.
        - **ReplicationTaskIdentifier** *(string) --*

          The user-assigned replication task identifier or name.
          Constraints:
          * Must contain from 1 to 255 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientCreateReplicationTaskTagsTypeDef = TypedDict(
    "_ClientCreateReplicationTaskTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateReplicationTaskTagsTypeDef(_ClientCreateReplicationTaskTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientDeleteCertificateResponseCertificateTypeDef = TypedDict(
    "_ClientDeleteCertificateResponseCertificateTypeDef",
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


class ClientDeleteCertificateResponseCertificateTypeDef(
    _ClientDeleteCertificateResponseCertificateTypeDef
):
    """
    - **Certificate** *(dict) --*

      The Secure Sockets Layer (SSL) certificate.
      - **CertificateIdentifier** *(string) --*

        A customer-assigned name for the certificate. Identifiers must begin with a letter; must
        contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
        two consecutive hyphens.
    """


_ClientDeleteCertificateResponseTypeDef = TypedDict(
    "_ClientDeleteCertificateResponseTypeDef",
    {"Certificate": ClientDeleteCertificateResponseCertificateTypeDef},
    total=False,
)


class ClientDeleteCertificateResponseTypeDef(_ClientDeleteCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **Certificate** *(dict) --*

        The Secure Sockets Layer (SSL) certificate.
        - **CertificateIdentifier** *(string) --*

          A customer-assigned name for the certificate. Identifiers must begin with a letter; must
          contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
          two consecutive hyphens.
    """


_ClientDeleteConnectionResponseConnectionTypeDef = TypedDict(
    "_ClientDeleteConnectionResponseConnectionTypeDef",
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


class ClientDeleteConnectionResponseConnectionTypeDef(
    _ClientDeleteConnectionResponseConnectionTypeDef
):
    """
    - **Connection** *(dict) --*

      The connection that is being deleted.
      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.
    """


_ClientDeleteConnectionResponseTypeDef = TypedDict(
    "_ClientDeleteConnectionResponseTypeDef",
    {"Connection": ClientDeleteConnectionResponseConnectionTypeDef},
    total=False,
)


class ClientDeleteConnectionResponseTypeDef(_ClientDeleteConnectionResponseTypeDef):
    """
    - *(dict) --*

      - **Connection** *(dict) --*

        The connection that is being deleted.
        - **ReplicationInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) of the replication instance.
    """


_ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef
):
    pass


_ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef
):
    pass


_ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef
):
    pass


_ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef
):
    pass


_ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef",
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


class ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef
):
    pass


_ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef",
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


class ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef
):
    pass


_ClientDeleteEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointS3SettingsTypeDef",
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


class ClientDeleteEndpointResponseEndpointS3SettingsTypeDef(
    _ClientDeleteEndpointResponseEndpointS3SettingsTypeDef
):
    pass


_ClientDeleteEndpointResponseEndpointTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseEndpointTypeDef",
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


class ClientDeleteEndpointResponseEndpointTypeDef(_ClientDeleteEndpointResponseEndpointTypeDef):
    """
    - **Endpoint** *(dict) --*

      The endpoint that was deleted.
      - **EndpointIdentifier** *(string) --*

        The database endpoint identifier. Identifiers must begin with a letter; must contain only
        ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
        consecutive hyphens.
    """


_ClientDeleteEndpointResponseTypeDef = TypedDict(
    "_ClientDeleteEndpointResponseTypeDef",
    {"Endpoint": ClientDeleteEndpointResponseEndpointTypeDef},
    total=False,
)


class ClientDeleteEndpointResponseTypeDef(_ClientDeleteEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **Endpoint** *(dict) --*

        The endpoint that was deleted.
        - **EndpointIdentifier** *(string) --*

          The database endpoint identifier. Identifiers must begin with a letter; must contain only
          ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
          consecutive hyphens.
    """


_ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
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


class ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      The event subscription that was deleted.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the AWS DMS event notification subscription.
    """


_ClientDeleteEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientDeleteEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)


class ClientDeleteEventSubscriptionResponseTypeDef(_ClientDeleteEventSubscriptionResponseTypeDef):
    """
    - *(dict) --*

      - **EventSubscription** *(dict) --*

        The event subscription that was deleted.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the AWS DMS event notification subscription.
    """


_ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef
):
    pass


_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
):
    pass


_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
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


class ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef
):
    pass


_ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef",
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


class ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef(
    _ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef
):
    """
    - **ReplicationInstance** *(dict) --*

      The replication instance that was deleted.
      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.
        Constraints:
        * Must contain from 1 to 63 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
        Example: ``myrepinstance``
    """


_ClientDeleteReplicationInstanceResponseTypeDef = TypedDict(
    "_ClientDeleteReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)


class ClientDeleteReplicationInstanceResponseTypeDef(
    _ClientDeleteReplicationInstanceResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationInstance** *(dict) --*

        The replication instance that was deleted.
        - **ReplicationInstanceIdentifier** *(string) --*

          The replication instance identifier. This parameter is stored as a lowercase string.
          Constraints:
          * Must contain from 1 to 63 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``myrepinstance``
    """


_ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "_ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
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


class ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef(
    _ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef
):
    pass


_ClientDeleteReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "_ClientDeleteReplicationTaskResponseReplicationTaskTypeDef",
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


class ClientDeleteReplicationTaskResponseReplicationTaskTypeDef(
    _ClientDeleteReplicationTaskResponseReplicationTaskTypeDef
):
    """
    - **ReplicationTask** *(dict) --*

      The deleted replication task.
      - **ReplicationTaskIdentifier** *(string) --*

        The user-assigned replication task identifier or name.
        Constraints:
        * Must contain from 1 to 255 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientDeleteReplicationTaskResponseTypeDef = TypedDict(
    "_ClientDeleteReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientDeleteReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)


class ClientDeleteReplicationTaskResponseTypeDef(_ClientDeleteReplicationTaskResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationTask** *(dict) --*

        The deleted replication task.
        - **ReplicationTaskIdentifier** *(string) --*

          The user-assigned replication task identifier or name.
          Constraints:
          * Must contain from 1 to 255 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientDescribeAccountAttributesResponseAccountQuotasTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    {"AccountQuotaName": str, "Used": int, "Max": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseAccountQuotasTypeDef(
    _ClientDescribeAccountAttributesResponseAccountQuotasTypeDef
):
    """
    - *(dict) --*

      Describes a quota for an AWS account, for example, the number of replication instances
      allowed.
      - **AccountQuotaName** *(string) --*

        The name of the AWS DMS quota for this AWS account.
    """


_ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseTypeDef",
    {
        "AccountQuotas": List[ClientDescribeAccountAttributesResponseAccountQuotasTypeDef],
        "UniqueAccountIdentifier": str,
    },
    total=False,
)


class ClientDescribeAccountAttributesResponseTypeDef(
    _ClientDescribeAccountAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **AccountQuotas** *(list) --*

        Account quota information.
        - *(dict) --*

          Describes a quota for an AWS account, for example, the number of replication instances
          allowed.
          - **AccountQuotaName** *(string) --*

            The name of the AWS DMS quota for this AWS account.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientDescribeCertificatesResponseCertificatesTypeDef",
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


class ClientDescribeCertificatesResponseCertificatesTypeDef(
    _ClientDescribeCertificatesResponseCertificatesTypeDef
):
    pass


_ClientDescribeCertificatesResponseTypeDef = TypedDict(
    "_ClientDescribeCertificatesResponseTypeDef",
    {"Marker": str, "Certificates": List[ClientDescribeCertificatesResponseCertificatesTypeDef]},
    total=False,
)


class ClientDescribeCertificatesResponseTypeDef(_ClientDescribeCertificatesResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        The pagination token.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeConnectionsResponseConnectionsTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseConnectionsTypeDef",
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


class ClientDescribeConnectionsResponseConnectionsTypeDef(
    _ClientDescribeConnectionsResponseConnectionsTypeDef
):
    pass


_ClientDescribeConnectionsResponseTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseTypeDef",
    {"Marker": str, "Connections": List[ClientDescribeConnectionsResponseConnectionsTypeDef]},
    total=False,
)


class ClientDescribeConnectionsResponseTypeDef(_ClientDescribeConnectionsResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef = TypedDict(
    "_ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": Literal["source", "target"],
        "EngineDisplayName": str,
    },
    total=False,
)


class ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef(
    _ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef
):
    pass


_ClientDescribeEndpointTypesResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointTypesResponseTypeDef",
    {
        "Marker": str,
        "SupportedEndpointTypes": List[
            ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEndpointTypesResponseTypeDef(_ClientDescribeEndpointTypesResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeEndpointsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEndpointsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEndpointsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEndpointsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEndpointsFiltersTypeDef(
    _RequiredClientDescribeEndpointsFiltersTypeDef, _OptionalClientDescribeEndpointsFiltersTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef
):
    pass


_ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef
):
    pass


_ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef
):
    pass


_ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef
):
    pass


_ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef",
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


class ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef
):
    pass


_ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef",
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


class ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef
):
    pass


_ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef",
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


class ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef
):
    pass


_ClientDescribeEndpointsResponseEndpointsTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseEndpointsTypeDef",
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


class ClientDescribeEndpointsResponseEndpointsTypeDef(
    _ClientDescribeEndpointsResponseEndpointsTypeDef
):
    pass


_ClientDescribeEndpointsResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointsResponseTypeDef",
    {"Marker": str, "Endpoints": List[ClientDescribeEndpointsResponseEndpointsTypeDef]},
    total=False,
)


class ClientDescribeEndpointsResponseTypeDef(_ClientDescribeEndpointsResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef",
    {"SourceType": str, "EventCategories": List[str]},
    total=False,
)


class ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef(
    _ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef
):
    """
    - *(dict) --*

      - **SourceType** *(string) --*

        The type of AWS DMS resource that generates events.
        Valid values: replication-instance | replication-server | security-group | replication-task
    """


_ClientDescribeEventCategoriesResponseTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoryGroupList": List[
            ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeEventCategoriesResponseTypeDef(_ClientDescribeEventCategoriesResponseTypeDef):
    """
    - *(dict) --*

      - **EventCategoryGroupList** *(list) --*

        A list of event categories.
        - *(dict) --*

          - **SourceType** *(string) --*

            The type of AWS DMS resource that generates events.
            Valid values: replication-instance | replication-server | security-group |
            replication-task
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
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


class ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef(
    _ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
):
    pass


_ClientDescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[
            ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEventSubscriptionsResponseTypeDef(
    _ClientDescribeEventSubscriptionsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_RequiredClientDescribeEventsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventsFiltersTypeDef(
    _RequiredClientDescribeEventsFiltersTypeDef, _OptionalClientDescribeEventsFiltersTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(_ClientDescribeEventsResponseEventsTypeDef):
    pass


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef = TypedDict(
    "_ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef",
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


class ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef(
    _ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef
):
    """
    - *(dict) --*

      - **EngineVersion** *(string) --*

        The version of the replication engine.
    """


_ClientDescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeOrderableReplicationInstancesResponseTypeDef",
    {
        "OrderableReplicationInstances": List[
            ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeOrderableReplicationInstancesResponseTypeDef(
    _ClientDescribeOrderableReplicationInstancesResponseTypeDef
):
    """
    - *(dict) --*

      - **OrderableReplicationInstances** *(list) --*

        The order-able replication instances available.
        - *(dict) --*

          - **EngineVersion** *(string) --*

            The version of the replication engine.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
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


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    pass


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
):
    """
    - *(dict) --*

      - **ResourceIdentifier** *(string) --*

        The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
        applies to. For information about creating an ARN, see `Constructing an Amazon Resource Name
        (ARN) for AWS DMS
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in the
        DMS documentation.
    """


_ClientDescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponseTypeDef(
    _ClientDescribePendingMaintenanceActionsResponseTypeDef
):
    """
    - *(dict) --*

      - **PendingMaintenanceActions** *(list) --*

        The pending maintenance action.
        - *(dict) --*

          - **ResourceIdentifier** *(string) --*

            The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
            applies to. For information about creating an ARN, see `Constructing an Amazon Resource
            Name (ARN) for AWS DMS
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in
            the DMS documentation.
    """


_ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef = TypedDict(
    "_ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": Literal["successful", "failed", "refreshing"],
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)


class ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef(
    _ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef
):
    """
    - **RefreshSchemasStatus** *(dict) --*

      The status of the schema.
      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
    """


_ClientDescribeRefreshSchemasStatusResponseTypeDef = TypedDict(
    "_ClientDescribeRefreshSchemasStatusResponseTypeDef",
    {"RefreshSchemasStatus": ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef},
    total=False,
)


class ClientDescribeRefreshSchemasStatusResponseTypeDef(
    _ClientDescribeRefreshSchemasStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **RefreshSchemasStatus** *(dict) --*

        The status of the schema.
        - **EndpointArn** *(string) --*

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
    """


_ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef = TypedDict(
    "_ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef",
    {"ReplicationTaskName": str, "ReplicationTaskArn": str, "ReplicationInstanceTaskLogSize": int},
    total=False,
)


class ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef(
    _ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef
):
    pass


_ClientDescribeReplicationInstanceTaskLogsResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationInstanceTaskLogsResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List[
            ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeReplicationInstanceTaskLogsResponseTypeDef(
    _ClientDescribeReplicationInstanceTaskLogsResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef
):
    pass


_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef
):
    pass


_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef",
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


class ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef
):
    pass


_ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef
):
    pass


_ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef",
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


class ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef(
    _ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef
):
    pass


_ClientDescribeReplicationInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReplicationInstances": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationInstancesResponseTypeDef(
    _ClientDescribeReplicationInstancesResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef(
    _ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef
):
    pass


_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef",
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


class ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef(
    _ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef
):
    pass


_ClientDescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationSubnetGroups": List[
            ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationSubnetGroupsResponseTypeDef(
    _ClientDescribeReplicationSubnetGroupsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef = TypedDict(
    "_ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef",
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


class ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef(
    _ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef
):
    pass


_ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List[
            ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef(
    _ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef
):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef = TypedDict(
    "_ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef",
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


class ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef(
    _ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef
):
    pass


_ClientDescribeReplicationTasksResponseReplicationTasksTypeDef = TypedDict(
    "_ClientDescribeReplicationTasksResponseReplicationTasksTypeDef",
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


class ClientDescribeReplicationTasksResponseReplicationTasksTypeDef(
    _ClientDescribeReplicationTasksResponseReplicationTasksTypeDef
):
    pass


_ClientDescribeReplicationTasksResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationTasksResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTasks": List[ClientDescribeReplicationTasksResponseReplicationTasksTypeDef],
    },
    total=False,
)


class ClientDescribeReplicationTasksResponseTypeDef(_ClientDescribeReplicationTasksResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


_ClientDescribeSchemasResponseTypeDef = TypedDict(
    "_ClientDescribeSchemasResponseTypeDef", {"Marker": str, "Schemas": List[str]}, total=False
)


class ClientDescribeSchemasResponseTypeDef(_ClientDescribeSchemasResponseTypeDef):
    """
    - *(dict) --*

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is specified,
        the response includes only records beyond the marker, up to the value specified by
        ``MaxRecords`` .
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ClientDescribeTableStatisticsResponseTableStatisticsTypeDef = TypedDict(
    "_ClientDescribeTableStatisticsResponseTableStatisticsTypeDef",
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


class ClientDescribeTableStatisticsResponseTableStatisticsTypeDef(
    _ClientDescribeTableStatisticsResponseTableStatisticsTypeDef
):
    pass


_ClientDescribeTableStatisticsResponseTypeDef = TypedDict(
    "_ClientDescribeTableStatisticsResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List[ClientDescribeTableStatisticsResponseTableStatisticsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeTableStatisticsResponseTypeDef(_ClientDescribeTableStatisticsResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationTaskArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication task.
    """


_ClientImportCertificateResponseCertificateTypeDef = TypedDict(
    "_ClientImportCertificateResponseCertificateTypeDef",
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


class ClientImportCertificateResponseCertificateTypeDef(
    _ClientImportCertificateResponseCertificateTypeDef
):
    """
    - **Certificate** *(dict) --*

      The certificate to be uploaded.
      - **CertificateIdentifier** *(string) --*

        A customer-assigned name for the certificate. Identifiers must begin with a letter; must
        contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
        two consecutive hyphens.
    """


_ClientImportCertificateResponseTypeDef = TypedDict(
    "_ClientImportCertificateResponseTypeDef",
    {"Certificate": ClientImportCertificateResponseCertificateTypeDef},
    total=False,
)


class ClientImportCertificateResponseTypeDef(_ClientImportCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **Certificate** *(dict) --*

        The certificate to be uploaded.
        - **CertificateIdentifier** *(string) --*

          A customer-assigned name for the certificate. Identifiers must begin with a letter; must
          contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
          two consecutive hyphens.
    """


_ClientImportCertificateTagsTypeDef = TypedDict(
    "_ClientImportCertificateTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientImportCertificateTagsTypeDef(_ClientImportCertificateTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    - *(dict) --*

      - **Key** *(string) --*

        A key is the required name of the tag. The string value can be from 1 to 128 Unicode
        characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
        contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
            ', '+', '-'
        (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **TagList** *(list) --*

        A list of tags for the resource.
        - *(dict) --*

          - **Key** *(string) --*

            A key is the required name of the tag. The string value can be from 1 to 128 Unicode
            characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
            contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=
                ', '+',
            '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientModifyEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientModifyEndpointDmsTransferSettingsTypeDef(
    _ClientModifyEndpointDmsTransferSettingsTypeDef
):
    """
    The settings in JSON format for the DMS transfer type of source endpoint.
    Attributes include the following:
    * serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.
    * BucketName - The name of the S3 bucket to use.
    * compressionType - An optional parameter to use GZIP to compress the target files. Set to NONE
    (the default) or do not use to leave the files uncompressed.
    Shorthand syntax: ServiceAccessRoleArn=string ,BucketName=string,CompressionType=string
    JSON syntax:
    { "ServiceAccessRoleArn": "string", "BucketName": "string", "CompressionType": "none"|"gzip" }
    - **ServiceAccessRoleArn** *(string) --*

      The IAM role that has permission to access the Amazon S3 bucket.
    """


_ClientModifyEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointDynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str}
)


class ClientModifyEndpointDynamoDbSettingsTypeDef(_ClientModifyEndpointDynamoDbSettingsTypeDef):
    """
    Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the
    available settings, see `Using Object Mapping to Migrate Data to DynamoDB
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html>`__ in the *AWS
    Database Migration Service User Guide.*
    - **ServiceAccessRoleArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


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
    """
    Settings in JSON format for the target Elasticsearch endpoint. For more information about the
    available settings, see `Extra Connection Attributes When Using Elasticsearch as a Target for
    AWS DMS
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`__
    in the *AWS Database Migration User Guide.*
    - **ServiceAccessRoleArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) used by service to access the IAM role.
    """


_ClientModifyEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientModifyEndpointKinesisSettingsTypeDef(_ClientModifyEndpointKinesisSettingsTypeDef):
    """
    Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. For more
    information about the available settings, see `Using Object Mapping to Migrate Data to a Kinesis
    Data Stream
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`__
    in the *AWS Database Migration User Guide.*
    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.
    """


_ClientModifyEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointMongoDbSettingsTypeDef",
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


class ClientModifyEndpointMongoDbSettingsTypeDef(_ClientModifyEndpointMongoDbSettingsTypeDef):
    """
    Settings in JSON format for the source MongoDB endpoint. For more information about the
    available settings, see the configuration properties section in `Using MongoDB as a Target for
    AWS Database Migration Service
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html>`__ in the *AWS
    Database Migration Service User Guide.*
    - **Username** *(string) --*

      The user name you use to access the MongoDB source endpoint.
    """


_ClientModifyEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointRedshiftSettingsTypeDef",
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


class ClientModifyEndpointRedshiftSettingsTypeDef(_ClientModifyEndpointRedshiftSettingsTypeDef):
    """
    - **AcceptAnyDate** *(boolean) --*

      A value that indicates to allow any date format, including invalid formats such as 00/00/00
      00:00:00, to be loaded without generating an error. You can choose ``true`` or ``false`` (the
      default).
      This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the
      DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
      specification, Amazon Redshift inserts a NULL value into that field.
    """


_ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef
):
    pass


_ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef
):
    pass


_ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef
):
    pass


_ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef
):
    pass


_ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef",
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


class ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef
):
    pass


_ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef",
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


class ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef(
    _ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef
):
    pass


_ClientModifyEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointS3SettingsTypeDef",
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


class ClientModifyEndpointResponseEndpointS3SettingsTypeDef(
    _ClientModifyEndpointResponseEndpointS3SettingsTypeDef
):
    pass


_ClientModifyEndpointResponseEndpointTypeDef = TypedDict(
    "_ClientModifyEndpointResponseEndpointTypeDef",
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


class ClientModifyEndpointResponseEndpointTypeDef(_ClientModifyEndpointResponseEndpointTypeDef):
    """
    - **Endpoint** *(dict) --*

      The modified endpoint.
      - **EndpointIdentifier** *(string) --*

        The database endpoint identifier. Identifiers must begin with a letter; must contain only
        ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
        consecutive hyphens.
    """


_ClientModifyEndpointResponseTypeDef = TypedDict(
    "_ClientModifyEndpointResponseTypeDef",
    {"Endpoint": ClientModifyEndpointResponseEndpointTypeDef},
    total=False,
)


class ClientModifyEndpointResponseTypeDef(_ClientModifyEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **Endpoint** *(dict) --*

        The modified endpoint.
        - **EndpointIdentifier** *(string) --*

          The database endpoint identifier. Identifiers must begin with a letter; must contain only
          ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
          consecutive hyphens.
    """


_ClientModifyEndpointS3SettingsTypeDef = TypedDict(
    "_ClientModifyEndpointS3SettingsTypeDef",
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


class ClientModifyEndpointS3SettingsTypeDef(_ClientModifyEndpointS3SettingsTypeDef):
    """
    Settings in JSON format for the target Amazon S3 endpoint. For more information about the
    available settings, see `Extra Connection Attributes When Using Amazon S3 as a Target for AWS
    DMS
    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`__
    in the *AWS Database Migration Service User Guide.*
    - **ServiceAccessRoleArn** *(string) --*

      The Amazon Resource Name (ARN) used by the service access IAM role.
    """


_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
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


class ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    - **EventSubscription** *(dict) --*

      The modified event subscription.
      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the AWS DMS event notification subscription.
    """


_ClientModifyEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)


class ClientModifyEventSubscriptionResponseTypeDef(_ClientModifyEventSubscriptionResponseTypeDef):
    """
    - *(dict) --*

      - **EventSubscription** *(dict) --*

        The modified event subscription.
        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the AWS DMS event notification subscription.
    """


_ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef
):
    pass


_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
):
    pass


_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
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


class ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef
):
    pass


_ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef",
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


class ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef(
    _ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef
):
    """
    - **ReplicationInstance** *(dict) --*

      The modified replication instance.
      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.
        Constraints:
        * Must contain from 1 to 63 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
        Example: ``myrepinstance``
    """


_ClientModifyReplicationInstanceResponseTypeDef = TypedDict(
    "_ClientModifyReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)


class ClientModifyReplicationInstanceResponseTypeDef(
    _ClientModifyReplicationInstanceResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationInstance** *(dict) --*

        The modified replication instance.
        - **ReplicationInstanceIdentifier** *(string) --*

          The replication instance identifier. This parameter is stored as a lowercase string.
          Constraints:
          * Must contain from 1 to 63 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``myrepinstance``
    """


_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef(
    _ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
):
    pass


_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
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


class ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef(
    _ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
):
    """
    - **ReplicationSubnetGroup** *(dict) --*

      The modified replication subnet group.
      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.
    """


_ClientModifyReplicationSubnetGroupResponseTypeDef = TypedDict(
    "_ClientModifyReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
    },
    total=False,
)


class ClientModifyReplicationSubnetGroupResponseTypeDef(
    _ClientModifyReplicationSubnetGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationSubnetGroup** *(dict) --*

        The modified replication subnet group.
        - **ReplicationSubnetGroupIdentifier** *(string) --*

          The identifier of the replication instance subnet group.
    """


_ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "_ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
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


class ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef(
    _ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef
):
    pass


_ClientModifyReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "_ClientModifyReplicationTaskResponseReplicationTaskTypeDef",
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


class ClientModifyReplicationTaskResponseReplicationTaskTypeDef(
    _ClientModifyReplicationTaskResponseReplicationTaskTypeDef
):
    """
    - **ReplicationTask** *(dict) --*

      The replication task that was modified.
      - **ReplicationTaskIdentifier** *(string) --*

        The user-assigned replication task identifier or name.
        Constraints:
        * Must contain from 1 to 255 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientModifyReplicationTaskResponseTypeDef = TypedDict(
    "_ClientModifyReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientModifyReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)


class ClientModifyReplicationTaskResponseTypeDef(_ClientModifyReplicationTaskResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationTask** *(dict) --*

        The replication task that was modified.
        - **ReplicationTaskIdentifier** *(string) --*

          The user-assigned replication task identifier or name.
          Constraints:
          * Must contain from 1 to 255 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef
):
    pass


_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
):
    pass


_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
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


class ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef
):
    pass


_ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
):
    pass


_ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef",
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


class ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef(
    _ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef
):
    """
    - **ReplicationInstance** *(dict) --*

      The replication instance that is being rebooted.
      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.
        Constraints:
        * Must contain from 1 to 63 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
        Example: ``myrepinstance``
    """


_ClientRebootReplicationInstanceResponseTypeDef = TypedDict(
    "_ClientRebootReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)


class ClientRebootReplicationInstanceResponseTypeDef(
    _ClientRebootReplicationInstanceResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationInstance** *(dict) --*

        The replication instance that is being rebooted.
        - **ReplicationInstanceIdentifier** *(string) --*

          The replication instance identifier. This parameter is stored as a lowercase string.
          Constraints:
          * Must contain from 1 to 63 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
          Example: ``myrepinstance``
    """


_ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef = TypedDict(
    "_ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": Literal["successful", "failed", "refreshing"],
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)


class ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef(
    _ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef
):
    """
    - **RefreshSchemasStatus** *(dict) --*

      The status of the refreshed schema.
      - **EndpointArn** *(string) --*

        The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
    """


_ClientRefreshSchemasResponseTypeDef = TypedDict(
    "_ClientRefreshSchemasResponseTypeDef",
    {"RefreshSchemasStatus": ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef},
    total=False,
)


class ClientRefreshSchemasResponseTypeDef(_ClientRefreshSchemasResponseTypeDef):
    """
    - *(dict) --*

      - **RefreshSchemasStatus** *(dict) --*

        The status of the refreshed schema.
        - **EndpointArn** *(string) --*

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
    """


_ClientReloadTablesResponseTypeDef = TypedDict(
    "_ClientReloadTablesResponseTypeDef", {"ReplicationTaskArn": str}, total=False
)


class ClientReloadTablesResponseTypeDef(_ClientReloadTablesResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationTaskArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication task.
    """


_ClientReloadTablesTablesToReloadTypeDef = TypedDict(
    "_ClientReloadTablesTablesToReloadTypeDef", {"SchemaName": str, "TableName": str}, total=False
)


class ClientReloadTablesTablesToReloadTypeDef(_ClientReloadTablesTablesToReloadTypeDef):
    """
    - *(dict) --*

      - **SchemaName** *(string) --*

        The schema name of the table to be reloaded.
    """


_ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "_ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef",
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


class ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef(
    _ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef
):
    pass


_ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef = TypedDict(
    "_ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef",
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


class ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef(
    _ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef
):
    """
    - **ReplicationTask** *(dict) --*

      The assessed replication task.
      - **ReplicationTaskIdentifier** *(string) --*

        The user-assigned replication task identifier or name.
        Constraints:
        * Must contain from 1 to 255 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientStartReplicationTaskAssessmentResponseTypeDef = TypedDict(
    "_ClientStartReplicationTaskAssessmentResponseTypeDef",
    {"ReplicationTask": ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef},
    total=False,
)


class ClientStartReplicationTaskAssessmentResponseTypeDef(
    _ClientStartReplicationTaskAssessmentResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationTask** *(dict) --*

        The assessed replication task.
        - **ReplicationTaskIdentifier** *(string) --*

          The user-assigned replication task identifier or name.
          Constraints:
          * Must contain from 1 to 255 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "_ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
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


class ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef(
    _ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef
):
    pass


_ClientStartReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "_ClientStartReplicationTaskResponseReplicationTaskTypeDef",
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


class ClientStartReplicationTaskResponseReplicationTaskTypeDef(
    _ClientStartReplicationTaskResponseReplicationTaskTypeDef
):
    """
    - **ReplicationTask** *(dict) --*

      The replication task started.
      - **ReplicationTaskIdentifier** *(string) --*

        The user-assigned replication task identifier or name.
        Constraints:
        * Must contain from 1 to 255 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientStartReplicationTaskResponseTypeDef = TypedDict(
    "_ClientStartReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientStartReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)


class ClientStartReplicationTaskResponseTypeDef(_ClientStartReplicationTaskResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationTask** *(dict) --*

        The replication task started.
        - **ReplicationTaskIdentifier** *(string) --*

          The user-assigned replication task identifier or name.
          Constraints:
          * Must contain from 1 to 255 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "_ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
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


class ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef(
    _ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef
):
    pass


_ClientStopReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "_ClientStopReplicationTaskResponseReplicationTaskTypeDef",
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


class ClientStopReplicationTaskResponseReplicationTaskTypeDef(
    _ClientStopReplicationTaskResponseReplicationTaskTypeDef
):
    """
    - **ReplicationTask** *(dict) --*

      The replication task stopped.
      - **ReplicationTaskIdentifier** *(string) --*

        The user-assigned replication task identifier or name.
        Constraints:
        * Must contain from 1 to 255 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientStopReplicationTaskResponseTypeDef = TypedDict(
    "_ClientStopReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientStopReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)


class ClientStopReplicationTaskResponseTypeDef(_ClientStopReplicationTaskResponseTypeDef):
    """
    - *(dict) --*

      - **ReplicationTask** *(dict) --*

        The replication task stopped.
        - **ReplicationTaskIdentifier** *(string) --*

          The user-assigned replication task identifier or name.
          Constraints:
          * Must contain from 1 to 255 alphanumeric characters or hyphens.
          * First character must be a letter.
          * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_ClientTestConnectionResponseConnectionTypeDef = TypedDict(
    "_ClientTestConnectionResponseConnectionTypeDef",
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


class ClientTestConnectionResponseConnectionTypeDef(_ClientTestConnectionResponseConnectionTypeDef):
    """
    - **Connection** *(dict) --*

      The connection tested.
      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.
    """


_ClientTestConnectionResponseTypeDef = TypedDict(
    "_ClientTestConnectionResponseTypeDef",
    {"Connection": ClientTestConnectionResponseConnectionTypeDef},
    total=False,
)


class ClientTestConnectionResponseTypeDef(_ClientTestConnectionResponseTypeDef):
    """
    - *(dict) --*

      - **Connection** *(dict) --*

        The connection tested.
        - **ReplicationInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) of the replication instance.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCertificatesPaginatePaginationConfigTypeDef(
    _DescribeCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeCertificatesPaginateResponseCertificatesTypeDef = TypedDict(
    "_DescribeCertificatesPaginateResponseCertificatesTypeDef",
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


class DescribeCertificatesPaginateResponseCertificatesTypeDef(
    _DescribeCertificatesPaginateResponseCertificatesTypeDef
):
    """
    - *(dict) --*

      The SSL certificate that can be used to encrypt connections between the endpoints and the
      replication instance.
      - **CertificateIdentifier** *(string) --*

        A customer-assigned name for the certificate. Identifiers must begin with a letter; must
        contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
        two consecutive hyphens.
    """


_DescribeCertificatesPaginateResponseTypeDef = TypedDict(
    "_DescribeCertificatesPaginateResponseTypeDef",
    {
        "Certificates": List[DescribeCertificatesPaginateResponseCertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeCertificatesPaginateResponseTypeDef(_DescribeCertificatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Certificates** *(list) --*

        The Secure Sockets Layer (SSL) certificates associated with the replication instance.
        - *(dict) --*

          The SSL certificate that can be used to encrypt connections between the endpoints and the
          replication instance.
          - **CertificateIdentifier** *(string) --*

            A customer-assigned name for the certificate. Identifiers must begin with a letter; must
            contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or
            contain two consecutive hyphens.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeConnectionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeConnectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeConnectionsPaginatePaginationConfigTypeDef(
    _DescribeConnectionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeConnectionsPaginateResponseConnectionsTypeDef = TypedDict(
    "_DescribeConnectionsPaginateResponseConnectionsTypeDef",
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


class DescribeConnectionsPaginateResponseConnectionsTypeDef(
    _DescribeConnectionsPaginateResponseConnectionsTypeDef
):
    """
    - *(dict) --*

      - **ReplicationInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication instance.
    """


_DescribeConnectionsPaginateResponseTypeDef = TypedDict(
    "_DescribeConnectionsPaginateResponseTypeDef",
    {"Connections": List[DescribeConnectionsPaginateResponseConnectionsTypeDef], "NextToken": str},
    total=False,
)


class DescribeConnectionsPaginateResponseTypeDef(_DescribeConnectionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Connections** *(list) --*

        A description of the connections.
        - *(dict) --*

          - **ReplicationInstanceArn** *(string) --*

            The Amazon Resource Name (ARN) of the replication instance.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeEndpointTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEndpointTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEndpointTypesPaginatePaginationConfigTypeDef(
    _DescribeEndpointTypesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef = TypedDict(
    "_DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": Literal["source", "target"],
        "EngineDisplayName": str,
    },
    total=False,
)


class DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef(
    _DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef
):
    """
    - *(dict) --*

      - **EngineName** *(string) --*

        The database engine name. Valid values, depending on the EndpointType, include mysql,
        oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
        dynamodb, mongodb, and sqlserver.
    """


_DescribeEndpointTypesPaginateResponseTypeDef = TypedDict(
    "_DescribeEndpointTypesPaginateResponseTypeDef",
    {
        "SupportedEndpointTypes": List[
            DescribeEndpointTypesPaginateResponseSupportedEndpointTypesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeEndpointTypesPaginateResponseTypeDef(_DescribeEndpointTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SupportedEndpointTypes** *(list) --*

        The types of endpoints that are supported.
        - *(dict) --*

          - **EngineName** *(string) --*

            The database engine name. Valid values, depending on the EndpointType, include mysql,
            oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb,
            sybase, dynamodb, mongodb, and sqlserver.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeEndpointsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEndpointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEndpointsPaginatePaginationConfigTypeDef(
    _DescribeEndpointsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsDmsTransferSettingsTypeDef
):
    pass


_DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsDynamoDbSettingsTypeDef
):
    pass


_DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsElasticsearchSettingsTypeDef
):
    pass


_DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)


class DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsKinesisSettingsTypeDef
):
    pass


_DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef",
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


class DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsMongoDbSettingsTypeDef
):
    pass


_DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef",
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


class DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsRedshiftSettingsTypeDef
):
    pass


_DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef",
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


class DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsS3SettingsTypeDef
):
    pass


_DescribeEndpointsPaginateResponseEndpointsTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseEndpointsTypeDef",
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


class DescribeEndpointsPaginateResponseEndpointsTypeDef(
    _DescribeEndpointsPaginateResponseEndpointsTypeDef
):
    """
    - *(dict) --*

      - **EndpointIdentifier** *(string) --*

        The database endpoint identifier. Identifiers must begin with a letter; must contain only
        ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
        consecutive hyphens.
    """


_DescribeEndpointsPaginateResponseTypeDef = TypedDict(
    "_DescribeEndpointsPaginateResponseTypeDef",
    {"Endpoints": List[DescribeEndpointsPaginateResponseEndpointsTypeDef], "NextToken": str},
    total=False,
)


class DescribeEndpointsPaginateResponseTypeDef(_DescribeEndpointsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Endpoints** *(list) --*

        Endpoint description.
        - *(dict) --*

          - **EndpointIdentifier** *(string) --*

            The database endpoint identifier. Identifiers must begin with a letter; must contain
            only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
            consecutive hyphens.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeEventSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventSubscriptionsPaginatePaginationConfigTypeDef(
    _DescribeEventSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
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


class DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef(
    _DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
):
    """
    - *(dict) --*

      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the AWS DMS event notification subscription.
    """


_DescribeEventSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseTypeDef",
    {
        "EventSubscriptionsList": List[
            DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeEventSubscriptionsPaginateResponseTypeDef(
    _DescribeEventSubscriptionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EventSubscriptionsList** *(list) --*

        A list of event subscriptions.
        - *(dict) --*

          - **CustomerAwsId** *(string) --*

            The AWS customer account associated with the AWS DMS event notification subscription.
    """


_RequiredDescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeEventsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalDescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeEventsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeEventsPaginateFiltersTypeDef(
    _RequiredDescribeEventsPaginateFiltersTypeDef, _OptionalDescribeEventsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(_DescribeEventsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(_DescribeEventsPaginateResponseEventsTypeDef):
    """
    - *(dict) --*

      - **SourceIdentifier** *(string) --*

        The identifier of an event source.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Events** *(list) --*

        The events described.
        - *(dict) --*

          - **SourceIdentifier** *(string) --*

            The identifier of an event source.
    """


_DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef(
    _DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef = TypedDict(
    "_DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef",
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


class DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef(
    _DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef
):
    """
    - *(dict) --*

      - **EngineVersion** *(string) --*

        The version of the replication engine.
    """


_DescribeOrderableReplicationInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeOrderableReplicationInstancesPaginateResponseTypeDef",
    {
        "OrderableReplicationInstances": List[
            DescribeOrderableReplicationInstancesPaginateResponseOrderableReplicationInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeOrderableReplicationInstancesPaginateResponseTypeDef(
    _DescribeOrderableReplicationInstancesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **OrderableReplicationInstances** *(list) --*

        The order-able replication instances available.
        - *(dict) --*

          - **EngineVersion** *(string) --*

            The version of the replication engine.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeReplicationInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationInstancesPaginatePaginationConfigTypeDef(
    _DescribeReplicationInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesPendingModifiedValuesTypeDef
):
    pass


_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef
):
    pass


_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef",
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


class DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesReplicationSubnetGroupTypeDef
):
    pass


_DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesVpcSecurityGroupsTypeDef
):
    pass


_DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef",
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


class DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef(
    _DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef
):
    """
    - *(dict) --*

      - **ReplicationInstanceIdentifier** *(string) --*

        The replication instance identifier. This parameter is stored as a lowercase string.
        Constraints:
        * Must contain from 1 to 63 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
        Example: ``myrepinstance``
    """


_DescribeReplicationInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeReplicationInstancesPaginateResponseTypeDef",
    {
        "ReplicationInstances": List[
            DescribeReplicationInstancesPaginateResponseReplicationInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReplicationInstancesPaginateResponseTypeDef(
    _DescribeReplicationInstancesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationInstances** *(list) --*

        The replication instances described.
        - *(dict) --*

          - **ReplicationInstanceIdentifier** *(string) --*

            The replication instance identifier. This parameter is stored as a lowercase string.
            Constraints:
            * Must contain from 1 to 63 alphanumeric characters or hyphens.
            * First character must be a letter.
            * Cannot end with a hyphen or contain two consecutive hyphens.
            Example: ``myrepinstance``
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    pass


_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef(
    _DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsSubnetsTypeDef
):
    pass


_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef",
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


class DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef(
    _DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef
):
    """
    - *(dict) --*

      - **ReplicationSubnetGroupIdentifier** *(string) --*

        The identifier of the replication instance subnet group.
    """


_DescribeReplicationSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeReplicationSubnetGroupsPaginateResponseTypeDef",
    {
        "ReplicationSubnetGroups": List[
            DescribeReplicationSubnetGroupsPaginateResponseReplicationSubnetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReplicationSubnetGroupsPaginateResponseTypeDef(
    _DescribeReplicationSubnetGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationSubnetGroups** *(list) --*

        A description of the replication subnet groups.
        - *(dict) --*

          - **ReplicationSubnetGroupIdentifier** *(string) --*

            The identifier of the replication instance subnet group.
    """


_DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef(
    _DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef = TypedDict(
    "_DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef",
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


class DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef(
    _DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef
):
    pass


_DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef = TypedDict(
    "_DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef",
    {
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List[
            DescribeReplicationTaskAssessmentResultsPaginateResponseReplicationTaskAssessmentResultsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef(
    _DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **BucketName** *(string) --*

        - The Amazon S3 bucket where the task assessment report is located.
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeReplicationTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationTasksPaginatePaginationConfigTypeDef(
    _DescribeReplicationTasksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReplicationTasksPaginateResponseReplicationTasksReplicationTaskStatsTypeDef = TypedDict(
    "_DescribeReplicationTasksPaginateResponseReplicationTasksReplicationTaskStatsTypeDef",
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


class DescribeReplicationTasksPaginateResponseReplicationTasksReplicationTaskStatsTypeDef(
    _DescribeReplicationTasksPaginateResponseReplicationTasksReplicationTaskStatsTypeDef
):
    pass


_DescribeReplicationTasksPaginateResponseReplicationTasksTypeDef = TypedDict(
    "_DescribeReplicationTasksPaginateResponseReplicationTasksTypeDef",
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


class DescribeReplicationTasksPaginateResponseReplicationTasksTypeDef(
    _DescribeReplicationTasksPaginateResponseReplicationTasksTypeDef
):
    """
    - *(dict) --*

      - **ReplicationTaskIdentifier** *(string) --*

        The user-assigned replication task identifier or name.
        Constraints:
        * Must contain from 1 to 255 alphanumeric characters or hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_DescribeReplicationTasksPaginateResponseTypeDef = TypedDict(
    "_DescribeReplicationTasksPaginateResponseTypeDef",
    {
        "ReplicationTasks": List[DescribeReplicationTasksPaginateResponseReplicationTasksTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeReplicationTasksPaginateResponseTypeDef(
    _DescribeReplicationTasksPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationTasks** *(list) --*

        A description of the replication tasks.
        - *(dict) --*

          - **ReplicationTaskIdentifier** *(string) --*

            The user-assigned replication task identifier or name.
            Constraints:
            * Must contain from 1 to 255 alphanumeric characters or hyphens.
            * First character must be a letter.
            * Cannot end with a hyphen or contain two consecutive hyphens.
    """


_DescribeSchemasPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSchemasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSchemasPaginatePaginationConfigTypeDef(
    _DescribeSchemasPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSchemasPaginateResponseTypeDef = TypedDict(
    "_DescribeSchemasPaginateResponseTypeDef", {"Schemas": List[str], "NextToken": str}, total=False
)


class DescribeSchemasPaginateResponseTypeDef(_DescribeSchemasPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Schemas** *(list) --*

        The described schema.
        - *(string) --*
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_DescribeTableStatisticsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTableStatisticsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTableStatisticsPaginatePaginationConfigTypeDef(
    _DescribeTableStatisticsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef = TypedDict(
    "_DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef",
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


class DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef(
    _DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef
):
    pass


_DescribeTableStatisticsPaginateResponseTypeDef = TypedDict(
    "_DescribeTableStatisticsPaginateResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List[DescribeTableStatisticsPaginateResponseTableStatisticsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeTableStatisticsPaginateResponseTypeDef(
    _DescribeTableStatisticsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ReplicationTaskArn** *(string) --*

        The Amazon Resource Name (ARN) of the replication task.
    """


_RequiredEndpointDeletedWaitFiltersTypeDef = TypedDict(
    "_RequiredEndpointDeletedWaitFiltersTypeDef", {"Name": str}
)
_OptionalEndpointDeletedWaitFiltersTypeDef = TypedDict(
    "_OptionalEndpointDeletedWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class EndpointDeletedWaitFiltersTypeDef(
    _RequiredEndpointDeletedWaitFiltersTypeDef, _OptionalEndpointDeletedWaitFiltersTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_EndpointDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_EndpointDeletedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class EndpointDeletedWaitWaiterConfigTypeDef(_EndpointDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ReplicationInstanceAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationInstanceAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationInstanceAvailableWaitWaiterConfigTypeDef(
    _ReplicationInstanceAvailableWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ReplicationInstanceDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationInstanceDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationInstanceDeletedWaitWaiterConfigTypeDef(
    _ReplicationInstanceDeletedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ReplicationTaskDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationTaskDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationTaskDeletedWaitWaiterConfigTypeDef(_ReplicationTaskDeletedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_RequiredReplicationTaskReadyWaitFiltersTypeDef = TypedDict(
    "_RequiredReplicationTaskReadyWaitFiltersTypeDef", {"Name": str}
)
_OptionalReplicationTaskReadyWaitFiltersTypeDef = TypedDict(
    "_OptionalReplicationTaskReadyWaitFiltersTypeDef", {"Values": List[str]}, total=False
)


class ReplicationTaskReadyWaitFiltersTypeDef(
    _RequiredReplicationTaskReadyWaitFiltersTypeDef, _OptionalReplicationTaskReadyWaitFiltersTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ReplicationTaskReadyWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationTaskReadyWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ReplicationTaskReadyWaitWaiterConfigTypeDef(_ReplicationTaskReadyWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ReplicationTaskRunningWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationTaskRunningWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationTaskRunningWaitWaiterConfigTypeDef(_ReplicationTaskRunningWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_ReplicationTaskStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationTaskStoppedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationTaskStoppedWaitWaiterConfigTypeDef(_ReplicationTaskStoppedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


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
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**

        The name of the filter.
    """


_TestConnectionSucceedsWaitWaiterConfigTypeDef = TypedDict(
    "_TestConnectionSucceedsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class TestConnectionSucceedsWaitWaiterConfigTypeDef(_TestConnectionSucceedsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """
