"Main interface for glue service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientBatchCreatePartitionPartitionInputListStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientBatchCreatePartitionPartitionInputListStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientBatchCreatePartitionPartitionInputListStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientBatchCreatePartitionPartitionInputListStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientBatchCreatePartitionPartitionInputListStorageDescriptorTypeDef = TypedDict(
    "ClientBatchCreatePartitionPartitionInputListStorageDescriptorTypeDef",
    {
        "Columns": List[
            ClientBatchCreatePartitionPartitionInputListStorageDescriptorColumnsTypeDef
        ],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientBatchCreatePartitionPartitionInputListStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientBatchCreatePartitionPartitionInputListStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientBatchCreatePartitionPartitionInputListStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientBatchCreatePartitionPartitionInputListTypeDef = TypedDict(
    "ClientBatchCreatePartitionPartitionInputListTypeDef",
    {
        "Values": List[str],
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientBatchCreatePartitionPartitionInputListStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)

ClientBatchCreatePartitionResponseErrorsErrorDetailTypeDef = TypedDict(
    "ClientBatchCreatePartitionResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchCreatePartitionResponseErrorsTypeDef = TypedDict(
    "ClientBatchCreatePartitionResponseErrorsTypeDef",
    {
        "PartitionValues": List[str],
        "ErrorDetail": ClientBatchCreatePartitionResponseErrorsErrorDetailTypeDef,
    },
    total=False,
)

ClientBatchCreatePartitionResponseTypeDef = TypedDict(
    "ClientBatchCreatePartitionResponseTypeDef",
    {"Errors": List[ClientBatchCreatePartitionResponseErrorsTypeDef]},
    total=False,
)

ClientBatchDeleteConnectionResponseErrorsTypeDef = TypedDict(
    "ClientBatchDeleteConnectionResponseErrorsTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDeleteConnectionResponseTypeDef = TypedDict(
    "ClientBatchDeleteConnectionResponseTypeDef",
    {"Succeeded": List[str], "Errors": Dict[str, ClientBatchDeleteConnectionResponseErrorsTypeDef]},
    total=False,
)

ClientBatchDeletePartitionPartitionsToDeleteTypeDef = TypedDict(
    "ClientBatchDeletePartitionPartitionsToDeleteTypeDef", {"Values": List[str]}
)

ClientBatchDeletePartitionResponseErrorsErrorDetailTypeDef = TypedDict(
    "ClientBatchDeletePartitionResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDeletePartitionResponseErrorsTypeDef = TypedDict(
    "ClientBatchDeletePartitionResponseErrorsTypeDef",
    {
        "PartitionValues": List[str],
        "ErrorDetail": ClientBatchDeletePartitionResponseErrorsErrorDetailTypeDef,
    },
    total=False,
)

ClientBatchDeletePartitionResponseTypeDef = TypedDict(
    "ClientBatchDeletePartitionResponseTypeDef",
    {"Errors": List[ClientBatchDeletePartitionResponseErrorsTypeDef]},
    total=False,
)

ClientBatchDeleteTableResponseErrorsErrorDetailTypeDef = TypedDict(
    "ClientBatchDeleteTableResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDeleteTableResponseErrorsTypeDef = TypedDict(
    "ClientBatchDeleteTableResponseErrorsTypeDef",
    {"TableName": str, "ErrorDetail": ClientBatchDeleteTableResponseErrorsErrorDetailTypeDef},
    total=False,
)

ClientBatchDeleteTableResponseTypeDef = TypedDict(
    "ClientBatchDeleteTableResponseTypeDef",
    {"Errors": List[ClientBatchDeleteTableResponseErrorsTypeDef]},
    total=False,
)

ClientBatchDeleteTableVersionResponseErrorsErrorDetailTypeDef = TypedDict(
    "ClientBatchDeleteTableVersionResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDeleteTableVersionResponseErrorsTypeDef = TypedDict(
    "ClientBatchDeleteTableVersionResponseErrorsTypeDef",
    {
        "TableName": str,
        "VersionId": str,
        "ErrorDetail": ClientBatchDeleteTableVersionResponseErrorsErrorDetailTypeDef,
    },
    total=False,
)

ClientBatchDeleteTableVersionResponseTypeDef = TypedDict(
    "ClientBatchDeleteTableVersionResponseTypeDef",
    {"Errors": List[ClientBatchDeleteTableVersionResponseErrorsTypeDef]},
    total=False,
)

ClientBatchGetCrawlersResponseCrawlersLastCrawlTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseCrawlersLastCrawlTypeDef",
    {
        "Status": Literal["SUCCEEDED", "CANCELLED", "FAILED"],
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)

ClientBatchGetCrawlersResponseCrawlersScheduleTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseCrawlersScheduleTypeDef",
    {"ScheduleExpression": str, "State": Literal["SCHEDULED", "NOT_SCHEDULED", "TRANSITIONING"]},
    total=False,
)

ClientBatchGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)

ClientBatchGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)

ClientBatchGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef",
    {"Path": str},
    total=False,
)

ClientBatchGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)

ClientBatchGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)

ClientBatchGetCrawlersResponseCrawlersTargetsTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseCrawlersTargetsTypeDef",
    {
        "S3Targets": List[ClientBatchGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientBatchGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[
            ClientBatchGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef
        ],
        "CatalogTargets": List[ClientBatchGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef],
    },
    total=False,
)

ClientBatchGetCrawlersResponseCrawlersTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseCrawlersTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": ClientBatchGetCrawlersResponseCrawlersTargetsTypeDef,
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "SchemaChangePolicy": ClientBatchGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef,
        "State": Literal["READY", "RUNNING", "STOPPING"],
        "TablePrefix": str,
        "Schedule": ClientBatchGetCrawlersResponseCrawlersScheduleTypeDef,
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": ClientBatchGetCrawlersResponseCrawlersLastCrawlTypeDef,
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)

ClientBatchGetCrawlersResponseTypeDef = TypedDict(
    "ClientBatchGetCrawlersResponseTypeDef",
    {
        "Crawlers": List[ClientBatchGetCrawlersResponseCrawlersTypeDef],
        "CrawlersNotFound": List[str],
    },
    total=False,
)

ClientBatchGetDevEndpointsResponseDevEndpointsTypeDef = TypedDict(
    "ClientBatchGetDevEndpointsResponseDevEndpointsTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)

ClientBatchGetDevEndpointsResponseTypeDef = TypedDict(
    "ClientBatchGetDevEndpointsResponseTypeDef",
    {
        "DevEndpoints": List[ClientBatchGetDevEndpointsResponseDevEndpointsTypeDef],
        "DevEndpointsNotFound": List[str],
    },
    total=False,
)

ClientBatchGetJobsResponseJobsCommandTypeDef = TypedDict(
    "ClientBatchGetJobsResponseJobsCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)

ClientBatchGetJobsResponseJobsConnectionsTypeDef = TypedDict(
    "ClientBatchGetJobsResponseJobsConnectionsTypeDef", {"Connections": List[str]}, total=False
)

ClientBatchGetJobsResponseJobsExecutionPropertyTypeDef = TypedDict(
    "ClientBatchGetJobsResponseJobsExecutionPropertyTypeDef",
    {"MaxConcurrentRuns": int},
    total=False,
)

ClientBatchGetJobsResponseJobsNotificationPropertyTypeDef = TypedDict(
    "ClientBatchGetJobsResponseJobsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientBatchGetJobsResponseJobsTypeDef = TypedDict(
    "ClientBatchGetJobsResponseJobsTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": ClientBatchGetJobsResponseJobsExecutionPropertyTypeDef,
        "Command": ClientBatchGetJobsResponseJobsCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": ClientBatchGetJobsResponseJobsConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientBatchGetJobsResponseJobsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientBatchGetJobsResponseTypeDef = TypedDict(
    "ClientBatchGetJobsResponseTypeDef",
    {"Jobs": List[ClientBatchGetJobsResponseJobsTypeDef], "JobsNotFound": List[str]},
    total=False,
)

ClientBatchGetPartitionPartitionsToGetTypeDef = TypedDict(
    "ClientBatchGetPartitionPartitionsToGetTypeDef", {"Values": List[str]}
)

ClientBatchGetPartitionResponsePartitionsStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientBatchGetPartitionResponsePartitionsStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientBatchGetPartitionResponsePartitionsStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientBatchGetPartitionResponsePartitionsStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientBatchGetPartitionResponsePartitionsStorageDescriptorTypeDef = TypedDict(
    "ClientBatchGetPartitionResponsePartitionsStorageDescriptorTypeDef",
    {
        "Columns": List[ClientBatchGetPartitionResponsePartitionsStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientBatchGetPartitionResponsePartitionsStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientBatchGetPartitionResponsePartitionsStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientBatchGetPartitionResponsePartitionsStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientBatchGetPartitionResponsePartitionsTypeDef = TypedDict(
    "ClientBatchGetPartitionResponsePartitionsTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientBatchGetPartitionResponsePartitionsStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)

ClientBatchGetPartitionResponseUnprocessedKeysTypeDef = TypedDict(
    "ClientBatchGetPartitionResponseUnprocessedKeysTypeDef", {"Values": List[str]}, total=False
)

ClientBatchGetPartitionResponseTypeDef = TypedDict(
    "ClientBatchGetPartitionResponseTypeDef",
    {
        "Partitions": List[ClientBatchGetPartitionResponsePartitionsTypeDef],
        "UnprocessedKeys": List[ClientBatchGetPartitionResponseUnprocessedKeysTypeDef],
    },
    total=False,
)

ClientBatchGetTriggersResponseTriggersActionsNotificationPropertyTypeDef = TypedDict(
    "ClientBatchGetTriggersResponseTriggersActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientBatchGetTriggersResponseTriggersActionsTypeDef = TypedDict(
    "ClientBatchGetTriggersResponseTriggersActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientBatchGetTriggersResponseTriggersActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientBatchGetTriggersResponseTriggersPredicateConditionsTypeDef = TypedDict(
    "ClientBatchGetTriggersResponseTriggersPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientBatchGetTriggersResponseTriggersPredicateTypeDef = TypedDict(
    "ClientBatchGetTriggersResponseTriggersPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientBatchGetTriggersResponseTriggersPredicateConditionsTypeDef],
    },
    total=False,
)

ClientBatchGetTriggersResponseTriggersTypeDef = TypedDict(
    "ClientBatchGetTriggersResponseTriggersTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientBatchGetTriggersResponseTriggersActionsTypeDef],
        "Predicate": ClientBatchGetTriggersResponseTriggersPredicateTypeDef,
    },
    total=False,
)

ClientBatchGetTriggersResponseTypeDef = TypedDict(
    "ClientBatchGetTriggersResponseTypeDef",
    {
        "Triggers": List[ClientBatchGetTriggersResponseTriggersTypeDef],
        "TriggersNotFound": List[str],
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphEdgesTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientBatchGetWorkflowsResponseWorkflowsGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsGraphTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsGraphTypeDef",
    {
        "Nodes": List[ClientBatchGetWorkflowsResponseWorkflowsGraphNodesTypeDef],
        "Edges": List[ClientBatchGetWorkflowsResponseWorkflowsGraphEdgesTypeDef],
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphEdgesTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsTypeDef",
    {
        "Crawls": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsCrawlsTypeDef
        ]
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsTypeDef",
    {
        "JobRuns": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsJobRunsTypeDef
        ]
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTypeDef",
    {
        "Trigger": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTriggerTypeDef
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphTypeDef",
    {
        "Nodes": List[ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphNodesTypeDef],
        "Edges": List[ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphEdgesTypeDef],
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunStatisticsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsLastRunTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsLastRunTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": Literal["RUNNING", "COMPLETED"],
        "Statistics": ClientBatchGetWorkflowsResponseWorkflowsLastRunStatisticsTypeDef,
        "Graph": ClientBatchGetWorkflowsResponseWorkflowsLastRunGraphTypeDef,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseWorkflowsTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseWorkflowsTypeDef",
    {
        "Name": str,
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "LastRun": ClientBatchGetWorkflowsResponseWorkflowsLastRunTypeDef,
        "Graph": ClientBatchGetWorkflowsResponseWorkflowsGraphTypeDef,
    },
    total=False,
)

ClientBatchGetWorkflowsResponseTypeDef = TypedDict(
    "ClientBatchGetWorkflowsResponseTypeDef",
    {
        "Workflows": List[ClientBatchGetWorkflowsResponseWorkflowsTypeDef],
        "MissingWorkflows": List[str],
    },
    total=False,
)

ClientBatchStopJobRunResponseErrorsErrorDetailTypeDef = TypedDict(
    "ClientBatchStopJobRunResponseErrorsErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchStopJobRunResponseErrorsTypeDef = TypedDict(
    "ClientBatchStopJobRunResponseErrorsTypeDef",
    {
        "JobName": str,
        "JobRunId": str,
        "ErrorDetail": ClientBatchStopJobRunResponseErrorsErrorDetailTypeDef,
    },
    total=False,
)

ClientBatchStopJobRunResponseSuccessfulSubmissionsTypeDef = TypedDict(
    "ClientBatchStopJobRunResponseSuccessfulSubmissionsTypeDef",
    {"JobName": str, "JobRunId": str},
    total=False,
)

ClientBatchStopJobRunResponseTypeDef = TypedDict(
    "ClientBatchStopJobRunResponseTypeDef",
    {
        "SuccessfulSubmissions": List[ClientBatchStopJobRunResponseSuccessfulSubmissionsTypeDef],
        "Errors": List[ClientBatchStopJobRunResponseErrorsTypeDef],
    },
    total=False,
)

ClientCancelMlTaskRunResponseTypeDef = TypedDict(
    "ClientCancelMlTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
    },
    total=False,
)

_RequiredClientCreateClassifierCsvClassifierTypeDef = TypedDict(
    "_RequiredClientCreateClassifierCsvClassifierTypeDef", {"Name": str}
)
_OptionalClientCreateClassifierCsvClassifierTypeDef = TypedDict(
    "_OptionalClientCreateClassifierCsvClassifierTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class ClientCreateClassifierCsvClassifierTypeDef(
    _RequiredClientCreateClassifierCsvClassifierTypeDef,
    _OptionalClientCreateClassifierCsvClassifierTypeDef,
):
    pass


_RequiredClientCreateClassifierGrokClassifierTypeDef = TypedDict(
    "_RequiredClientCreateClassifierGrokClassifierTypeDef", {"Classification": str}
)
_OptionalClientCreateClassifierGrokClassifierTypeDef = TypedDict(
    "_OptionalClientCreateClassifierGrokClassifierTypeDef",
    {"Name": str, "GrokPattern": str, "CustomPatterns": str},
    total=False,
)


class ClientCreateClassifierGrokClassifierTypeDef(
    _RequiredClientCreateClassifierGrokClassifierTypeDef,
    _OptionalClientCreateClassifierGrokClassifierTypeDef,
):
    pass


_RequiredClientCreateClassifierJsonClassifierTypeDef = TypedDict(
    "_RequiredClientCreateClassifierJsonClassifierTypeDef", {"Name": str}
)
_OptionalClientCreateClassifierJsonClassifierTypeDef = TypedDict(
    "_OptionalClientCreateClassifierJsonClassifierTypeDef", {"JsonPath": str}, total=False
)


class ClientCreateClassifierJsonClassifierTypeDef(
    _RequiredClientCreateClassifierJsonClassifierTypeDef,
    _OptionalClientCreateClassifierJsonClassifierTypeDef,
):
    pass


_RequiredClientCreateClassifierXMLClassifierTypeDef = TypedDict(
    "_RequiredClientCreateClassifierXMLClassifierTypeDef", {"Classification": str}
)
_OptionalClientCreateClassifierXMLClassifierTypeDef = TypedDict(
    "_OptionalClientCreateClassifierXMLClassifierTypeDef", {"Name": str, "RowTag": str}, total=False
)


class ClientCreateClassifierXMLClassifierTypeDef(
    _RequiredClientCreateClassifierXMLClassifierTypeDef,
    _OptionalClientCreateClassifierXMLClassifierTypeDef,
):
    pass


ClientCreateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef = TypedDict(
    "ClientCreateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)

_RequiredClientCreateConnectionConnectionInputTypeDef = TypedDict(
    "_RequiredClientCreateConnectionConnectionInputTypeDef", {"Name": str}
)
_OptionalClientCreateConnectionConnectionInputTypeDef = TypedDict(
    "_OptionalClientCreateConnectionConnectionInputTypeDef",
    {
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": ClientCreateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef,
    },
    total=False,
)


class ClientCreateConnectionConnectionInputTypeDef(
    _RequiredClientCreateConnectionConnectionInputTypeDef,
    _OptionalClientCreateConnectionConnectionInputTypeDef,
):
    pass


ClientCreateCrawlerSchemaChangePolicyTypeDef = TypedDict(
    "ClientCreateCrawlerSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)

ClientCreateCrawlerTargetsCatalogTargetsTypeDef = TypedDict(
    "ClientCreateCrawlerTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)

ClientCreateCrawlerTargetsDynamoDBTargetsTypeDef = TypedDict(
    "ClientCreateCrawlerTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)

ClientCreateCrawlerTargetsJdbcTargetsTypeDef = TypedDict(
    "ClientCreateCrawlerTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)

ClientCreateCrawlerTargetsS3TargetsTypeDef = TypedDict(
    "ClientCreateCrawlerTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)

ClientCreateCrawlerTargetsTypeDef = TypedDict(
    "ClientCreateCrawlerTargetsTypeDef",
    {
        "S3Targets": List[ClientCreateCrawlerTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientCreateCrawlerTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[ClientCreateCrawlerTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[ClientCreateCrawlerTargetsCatalogTargetsTypeDef],
    },
    total=False,
)

ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef = TypedDict(
    "ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

_RequiredClientCreateDatabaseDatabaseInputTypeDef = TypedDict(
    "_RequiredClientCreateDatabaseDatabaseInputTypeDef", {"Name": str}
)
_OptionalClientCreateDatabaseDatabaseInputTypeDef = TypedDict(
    "_OptionalClientCreateDatabaseDatabaseInputTypeDef",
    {
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTableDefaultPermissions": List[
            ClientCreateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateDatabaseDatabaseInputTypeDef(
    _RequiredClientCreateDatabaseDatabaseInputTypeDef,
    _OptionalClientCreateDatabaseDatabaseInputTypeDef,
):
    pass


ClientCreateDevEndpointResponseTypeDef = TypedDict(
    "ClientCreateDevEndpointResponseTypeDef",
    {
        "EndpointName": str,
        "Status": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "RoleArn": str,
        "YarnEndpointAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "NumberOfNodes": int,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "SecurityConfiguration": str,
        "CreatedTimestamp": datetime,
        "Arguments": Dict[str, str],
    },
    total=False,
)

ClientCreateJobCommandTypeDef = TypedDict(
    "ClientCreateJobCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)

ClientCreateJobConnectionsTypeDef = TypedDict(
    "ClientCreateJobConnectionsTypeDef", {"Connections": List[str]}, total=False
)

ClientCreateJobExecutionPropertyTypeDef = TypedDict(
    "ClientCreateJobExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)

ClientCreateJobNotificationPropertyTypeDef = TypedDict(
    "ClientCreateJobNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)

ClientCreateJobResponseTypeDef = TypedDict(
    "ClientCreateJobResponseTypeDef", {"Name": str}, total=False
)

_RequiredClientCreateMlTransformInputRecordTablesTypeDef = TypedDict(
    "_RequiredClientCreateMlTransformInputRecordTablesTypeDef", {"DatabaseName": str}
)
_OptionalClientCreateMlTransformInputRecordTablesTypeDef = TypedDict(
    "_OptionalClientCreateMlTransformInputRecordTablesTypeDef",
    {"TableName": str, "CatalogId": str, "ConnectionName": str},
    total=False,
)


class ClientCreateMlTransformInputRecordTablesTypeDef(
    _RequiredClientCreateMlTransformInputRecordTablesTypeDef,
    _OptionalClientCreateMlTransformInputRecordTablesTypeDef,
):
    pass


ClientCreateMlTransformParametersFindMatchesParametersTypeDef = TypedDict(
    "ClientCreateMlTransformParametersFindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)

_RequiredClientCreateMlTransformParametersTypeDef = TypedDict(
    "_RequiredClientCreateMlTransformParametersTypeDef", {"TransformType": str}
)
_OptionalClientCreateMlTransformParametersTypeDef = TypedDict(
    "_OptionalClientCreateMlTransformParametersTypeDef",
    {"FindMatchesParameters": ClientCreateMlTransformParametersFindMatchesParametersTypeDef},
    total=False,
)


class ClientCreateMlTransformParametersTypeDef(
    _RequiredClientCreateMlTransformParametersTypeDef,
    _OptionalClientCreateMlTransformParametersTypeDef,
):
    pass


ClientCreateMlTransformResponseTypeDef = TypedDict(
    "ClientCreateMlTransformResponseTypeDef", {"TransformId": str}, total=False
)

ClientCreatePartitionPartitionInputStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientCreatePartitionPartitionInputStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientCreatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientCreatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientCreatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientCreatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientCreatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientCreatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientCreatePartitionPartitionInputStorageDescriptorTypeDef = TypedDict(
    "ClientCreatePartitionPartitionInputStorageDescriptorTypeDef",
    {
        "Columns": List[ClientCreatePartitionPartitionInputStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientCreatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientCreatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientCreatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientCreatePartitionPartitionInputTypeDef = TypedDict(
    "ClientCreatePartitionPartitionInputTypeDef",
    {
        "Values": List[str],
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientCreatePartitionPartitionInputStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)

_RequiredClientCreateScriptDagEdgesTypeDef = TypedDict(
    "_RequiredClientCreateScriptDagEdgesTypeDef", {"Source": str}
)
_OptionalClientCreateScriptDagEdgesTypeDef = TypedDict(
    "_OptionalClientCreateScriptDagEdgesTypeDef",
    {"Target": str, "TargetParameter": str},
    total=False,
)


class ClientCreateScriptDagEdgesTypeDef(
    _RequiredClientCreateScriptDagEdgesTypeDef, _OptionalClientCreateScriptDagEdgesTypeDef
):
    pass


ClientCreateScriptDagNodesArgsTypeDef = TypedDict(
    "ClientCreateScriptDagNodesArgsTypeDef", {"Name": str, "Value": str, "Param": bool}, total=False
)

_RequiredClientCreateScriptDagNodesTypeDef = TypedDict(
    "_RequiredClientCreateScriptDagNodesTypeDef", {"Id": str}
)
_OptionalClientCreateScriptDagNodesTypeDef = TypedDict(
    "_OptionalClientCreateScriptDagNodesTypeDef",
    {"NodeType": str, "Args": List[ClientCreateScriptDagNodesArgsTypeDef], "LineNumber": int},
    total=False,
)


class ClientCreateScriptDagNodesTypeDef(
    _RequiredClientCreateScriptDagNodesTypeDef, _OptionalClientCreateScriptDagNodesTypeDef
):
    pass


ClientCreateScriptResponseTypeDef = TypedDict(
    "ClientCreateScriptResponseTypeDef", {"PythonScript": str, "ScalaCode": str}, total=False
)

ClientCreateSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef = TypedDict(
    "ClientCreateSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef",
    {"CloudWatchEncryptionMode": Literal["DISABLED", "SSE-KMS"], "KmsKeyArn": str},
    total=False,
)

ClientCreateSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef = TypedDict(
    "ClientCreateSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    {"JobBookmarksEncryptionMode": Literal["DISABLED", "CSE-KMS"], "KmsKeyArn": str},
    total=False,
)

ClientCreateSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef = TypedDict(
    "ClientCreateSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef",
    {"S3EncryptionMode": Literal["DISABLED", "SSE-KMS", "SSE-S3"], "KmsKeyArn": str},
    total=False,
)

ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef",
    {
        "S3Encryption": List[
            ClientCreateSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef
        ],
        "CloudWatchEncryption": ClientCreateSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef,
        "JobBookmarksEncryption": ClientCreateSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef,
    },
    total=False,
)

ClientCreateSecurityConfigurationResponseTypeDef = TypedDict(
    "ClientCreateSecurityConfigurationResponseTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)

ClientCreateTableTableInputPartitionKeysTypeDef = TypedDict(
    "ClientCreateTableTableInputPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientCreateTableTableInputStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientCreateTableTableInputStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientCreateTableTableInputStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientCreateTableTableInputStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientCreateTableTableInputStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientCreateTableTableInputStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientCreateTableTableInputStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientCreateTableTableInputStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientCreateTableTableInputStorageDescriptorTypeDef = TypedDict(
    "ClientCreateTableTableInputStorageDescriptorTypeDef",
    {
        "Columns": List[ClientCreateTableTableInputStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientCreateTableTableInputStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientCreateTableTableInputStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientCreateTableTableInputStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

_RequiredClientCreateTableTableInputTypeDef = TypedDict(
    "_RequiredClientCreateTableTableInputTypeDef", {"Name": str}
)
_OptionalClientCreateTableTableInputTypeDef = TypedDict(
    "_OptionalClientCreateTableTableInputTypeDef",
    {
        "Description": str,
        "Owner": str,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientCreateTableTableInputStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientCreateTableTableInputPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientCreateTableTableInputTypeDef(
    _RequiredClientCreateTableTableInputTypeDef, _OptionalClientCreateTableTableInputTypeDef
):
    pass


ClientCreateTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "ClientCreateTriggerActionsNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)

ClientCreateTriggerActionsTypeDef = TypedDict(
    "ClientCreateTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientCreateTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientCreateTriggerPredicateConditionsTypeDef = TypedDict(
    "ClientCreateTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientCreateTriggerPredicateTypeDef = TypedDict(
    "ClientCreateTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientCreateTriggerPredicateConditionsTypeDef],
    },
    total=False,
)

ClientCreateTriggerResponseTypeDef = TypedDict(
    "ClientCreateTriggerResponseTypeDef", {"Name": str}, total=False
)

ClientCreateUserDefinedFunctionFunctionInputResourceUrisTypeDef = TypedDict(
    "ClientCreateUserDefinedFunctionFunctionInputResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)

ClientCreateUserDefinedFunctionFunctionInputTypeDef = TypedDict(
    "ClientCreateUserDefinedFunctionFunctionInputTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "ResourceUris": List[ClientCreateUserDefinedFunctionFunctionInputResourceUrisTypeDef],
    },
    total=False,
)

ClientCreateWorkflowResponseTypeDef = TypedDict(
    "ClientCreateWorkflowResponseTypeDef", {"Name": str}, total=False
)

ClientDeleteJobResponseTypeDef = TypedDict(
    "ClientDeleteJobResponseTypeDef", {"JobName": str}, total=False
)

ClientDeleteMlTransformResponseTypeDef = TypedDict(
    "ClientDeleteMlTransformResponseTypeDef", {"TransformId": str}, total=False
)

ClientDeleteTriggerResponseTypeDef = TypedDict(
    "ClientDeleteTriggerResponseTypeDef", {"Name": str}, total=False
)

ClientDeleteWorkflowResponseTypeDef = TypedDict(
    "ClientDeleteWorkflowResponseTypeDef", {"Name": str}, total=False
)

ClientGetCatalogImportStatusResponseImportStatusTypeDef = TypedDict(
    "ClientGetCatalogImportStatusResponseImportStatusTypeDef",
    {"ImportCompleted": bool, "ImportTime": datetime, "ImportedBy": str},
    total=False,
)

ClientGetCatalogImportStatusResponseTypeDef = TypedDict(
    "ClientGetCatalogImportStatusResponseTypeDef",
    {"ImportStatus": ClientGetCatalogImportStatusResponseImportStatusTypeDef},
    total=False,
)

ClientGetClassifierResponseClassifierCsvClassifierTypeDef = TypedDict(
    "ClientGetClassifierResponseClassifierCsvClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)

ClientGetClassifierResponseClassifierGrokClassifierTypeDef = TypedDict(
    "ClientGetClassifierResponseClassifierGrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "GrokPattern": str,
        "CustomPatterns": str,
    },
    total=False,
)

ClientGetClassifierResponseClassifierJsonClassifierTypeDef = TypedDict(
    "ClientGetClassifierResponseClassifierJsonClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "JsonPath": str,
    },
    total=False,
)

ClientGetClassifierResponseClassifierXMLClassifierTypeDef = TypedDict(
    "ClientGetClassifierResponseClassifierXMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "RowTag": str,
    },
    total=False,
)

ClientGetClassifierResponseClassifierTypeDef = TypedDict(
    "ClientGetClassifierResponseClassifierTypeDef",
    {
        "GrokClassifier": ClientGetClassifierResponseClassifierGrokClassifierTypeDef,
        "XMLClassifier": ClientGetClassifierResponseClassifierXMLClassifierTypeDef,
        "JsonClassifier": ClientGetClassifierResponseClassifierJsonClassifierTypeDef,
        "CsvClassifier": ClientGetClassifierResponseClassifierCsvClassifierTypeDef,
    },
    total=False,
)

ClientGetClassifierResponseTypeDef = TypedDict(
    "ClientGetClassifierResponseTypeDef",
    {"Classifier": ClientGetClassifierResponseClassifierTypeDef},
    total=False,
)

ClientGetClassifiersResponseClassifiersCsvClassifierTypeDef = TypedDict(
    "ClientGetClassifiersResponseClassifiersCsvClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)

ClientGetClassifiersResponseClassifiersGrokClassifierTypeDef = TypedDict(
    "ClientGetClassifiersResponseClassifiersGrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "GrokPattern": str,
        "CustomPatterns": str,
    },
    total=False,
)

ClientGetClassifiersResponseClassifiersJsonClassifierTypeDef = TypedDict(
    "ClientGetClassifiersResponseClassifiersJsonClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "JsonPath": str,
    },
    total=False,
)

ClientGetClassifiersResponseClassifiersXMLClassifierTypeDef = TypedDict(
    "ClientGetClassifiersResponseClassifiersXMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "RowTag": str,
    },
    total=False,
)

ClientGetClassifiersResponseClassifiersTypeDef = TypedDict(
    "ClientGetClassifiersResponseClassifiersTypeDef",
    {
        "GrokClassifier": ClientGetClassifiersResponseClassifiersGrokClassifierTypeDef,
        "XMLClassifier": ClientGetClassifiersResponseClassifiersXMLClassifierTypeDef,
        "JsonClassifier": ClientGetClassifiersResponseClassifiersJsonClassifierTypeDef,
        "CsvClassifier": ClientGetClassifiersResponseClassifiersCsvClassifierTypeDef,
    },
    total=False,
)

ClientGetClassifiersResponseTypeDef = TypedDict(
    "ClientGetClassifiersResponseTypeDef",
    {"Classifiers": List[ClientGetClassifiersResponseClassifiersTypeDef], "NextToken": str},
    total=False,
)

ClientGetConnectionResponseConnectionPhysicalConnectionRequirementsTypeDef = TypedDict(
    "ClientGetConnectionResponseConnectionPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)

ClientGetConnectionResponseConnectionTypeDef = TypedDict(
    "ClientGetConnectionResponseConnectionTypeDef",
    {
        "Name": str,
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": ClientGetConnectionResponseConnectionPhysicalConnectionRequirementsTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
    total=False,
)

ClientGetConnectionResponseTypeDef = TypedDict(
    "ClientGetConnectionResponseTypeDef",
    {"Connection": ClientGetConnectionResponseConnectionTypeDef},
    total=False,
)

ClientGetConnectionsFilterTypeDef = TypedDict(
    "ClientGetConnectionsFilterTypeDef",
    {"MatchCriteria": List[str], "ConnectionType": Literal["JDBC", "SFTP"]},
    total=False,
)

ClientGetConnectionsResponseConnectionListPhysicalConnectionRequirementsTypeDef = TypedDict(
    "ClientGetConnectionsResponseConnectionListPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)

ClientGetConnectionsResponseConnectionListTypeDef = TypedDict(
    "ClientGetConnectionsResponseConnectionListTypeDef",
    {
        "Name": str,
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": ClientGetConnectionsResponseConnectionListPhysicalConnectionRequirementsTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
    total=False,
)

ClientGetConnectionsResponseTypeDef = TypedDict(
    "ClientGetConnectionsResponseTypeDef",
    {"ConnectionList": List[ClientGetConnectionsResponseConnectionListTypeDef], "NextToken": str},
    total=False,
)

ClientGetCrawlerMetricsResponseCrawlerMetricsListTypeDef = TypedDict(
    "ClientGetCrawlerMetricsResponseCrawlerMetricsListTypeDef",
    {
        "CrawlerName": str,
        "TimeLeftSeconds": float,
        "StillEstimating": bool,
        "LastRuntimeSeconds": float,
        "MedianRuntimeSeconds": float,
        "TablesCreated": int,
        "TablesUpdated": int,
        "TablesDeleted": int,
    },
    total=False,
)

ClientGetCrawlerMetricsResponseTypeDef = TypedDict(
    "ClientGetCrawlerMetricsResponseTypeDef",
    {
        "CrawlerMetricsList": List[ClientGetCrawlerMetricsResponseCrawlerMetricsListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientGetCrawlerResponseCrawlerLastCrawlTypeDef = TypedDict(
    "ClientGetCrawlerResponseCrawlerLastCrawlTypeDef",
    {
        "Status": Literal["SUCCEEDED", "CANCELLED", "FAILED"],
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)

ClientGetCrawlerResponseCrawlerScheduleTypeDef = TypedDict(
    "ClientGetCrawlerResponseCrawlerScheduleTypeDef",
    {"ScheduleExpression": str, "State": Literal["SCHEDULED", "NOT_SCHEDULED", "TRANSITIONING"]},
    total=False,
)

ClientGetCrawlerResponseCrawlerSchemaChangePolicyTypeDef = TypedDict(
    "ClientGetCrawlerResponseCrawlerSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)

ClientGetCrawlerResponseCrawlerTargetsCatalogTargetsTypeDef = TypedDict(
    "ClientGetCrawlerResponseCrawlerTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)

ClientGetCrawlerResponseCrawlerTargetsDynamoDBTargetsTypeDef = TypedDict(
    "ClientGetCrawlerResponseCrawlerTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)

ClientGetCrawlerResponseCrawlerTargetsJdbcTargetsTypeDef = TypedDict(
    "ClientGetCrawlerResponseCrawlerTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)

ClientGetCrawlerResponseCrawlerTargetsS3TargetsTypeDef = TypedDict(
    "ClientGetCrawlerResponseCrawlerTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)

ClientGetCrawlerResponseCrawlerTargetsTypeDef = TypedDict(
    "ClientGetCrawlerResponseCrawlerTargetsTypeDef",
    {
        "S3Targets": List[ClientGetCrawlerResponseCrawlerTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientGetCrawlerResponseCrawlerTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[ClientGetCrawlerResponseCrawlerTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[ClientGetCrawlerResponseCrawlerTargetsCatalogTargetsTypeDef],
    },
    total=False,
)

ClientGetCrawlerResponseCrawlerTypeDef = TypedDict(
    "ClientGetCrawlerResponseCrawlerTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": ClientGetCrawlerResponseCrawlerTargetsTypeDef,
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "SchemaChangePolicy": ClientGetCrawlerResponseCrawlerSchemaChangePolicyTypeDef,
        "State": Literal["READY", "RUNNING", "STOPPING"],
        "TablePrefix": str,
        "Schedule": ClientGetCrawlerResponseCrawlerScheduleTypeDef,
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": ClientGetCrawlerResponseCrawlerLastCrawlTypeDef,
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)

ClientGetCrawlerResponseTypeDef = TypedDict(
    "ClientGetCrawlerResponseTypeDef",
    {"Crawler": ClientGetCrawlerResponseCrawlerTypeDef},
    total=False,
)

ClientGetCrawlersResponseCrawlersLastCrawlTypeDef = TypedDict(
    "ClientGetCrawlersResponseCrawlersLastCrawlTypeDef",
    {
        "Status": Literal["SUCCEEDED", "CANCELLED", "FAILED"],
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)

ClientGetCrawlersResponseCrawlersScheduleTypeDef = TypedDict(
    "ClientGetCrawlersResponseCrawlersScheduleTypeDef",
    {"ScheduleExpression": str, "State": Literal["SCHEDULED", "NOT_SCHEDULED", "TRANSITIONING"]},
    total=False,
)

ClientGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef = TypedDict(
    "ClientGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)

ClientGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef = TypedDict(
    "ClientGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)

ClientGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef = TypedDict(
    "ClientGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)

ClientGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef = TypedDict(
    "ClientGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)

ClientGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef = TypedDict(
    "ClientGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)

ClientGetCrawlersResponseCrawlersTargetsTypeDef = TypedDict(
    "ClientGetCrawlersResponseCrawlersTargetsTypeDef",
    {
        "S3Targets": List[ClientGetCrawlersResponseCrawlersTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientGetCrawlersResponseCrawlersTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[ClientGetCrawlersResponseCrawlersTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[ClientGetCrawlersResponseCrawlersTargetsCatalogTargetsTypeDef],
    },
    total=False,
)

ClientGetCrawlersResponseCrawlersTypeDef = TypedDict(
    "ClientGetCrawlersResponseCrawlersTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": ClientGetCrawlersResponseCrawlersTargetsTypeDef,
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "SchemaChangePolicy": ClientGetCrawlersResponseCrawlersSchemaChangePolicyTypeDef,
        "State": Literal["READY", "RUNNING", "STOPPING"],
        "TablePrefix": str,
        "Schedule": ClientGetCrawlersResponseCrawlersScheduleTypeDef,
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": ClientGetCrawlersResponseCrawlersLastCrawlTypeDef,
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)

ClientGetCrawlersResponseTypeDef = TypedDict(
    "ClientGetCrawlersResponseTypeDef",
    {"Crawlers": List[ClientGetCrawlersResponseCrawlersTypeDef], "NextToken": str},
    total=False,
)

ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef = TypedDict(
    "ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef",
    {"ReturnConnectionPasswordEncrypted": bool, "AwsKmsKeyId": str},
    total=False,
)

ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsEncryptionAtRestTypeDef = TypedDict(
    "ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsEncryptionAtRestTypeDef",
    {"CatalogEncryptionMode": Literal["DISABLED", "SSE-KMS"], "SseAwsKmsKeyId": str},
    total=False,
)

ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsTypeDef = TypedDict(
    "ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsTypeDef",
    {
        "EncryptionAtRest": ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsEncryptionAtRestTypeDef,
        "ConnectionPasswordEncryption": ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef,
    },
    total=False,
)

ClientGetDataCatalogEncryptionSettingsResponseTypeDef = TypedDict(
    "ClientGetDataCatalogEncryptionSettingsResponseTypeDef",
    {
        "DataCatalogEncryptionSettings": ClientGetDataCatalogEncryptionSettingsResponseDataCatalogEncryptionSettingsTypeDef
    },
    total=False,
)

ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsTypeDef = TypedDict(
    "ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientGetDatabaseResponseDatabaseTypeDef = TypedDict(
    "ClientGetDatabaseResponseDatabaseTypeDef",
    {
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTime": datetime,
        "CreateTableDefaultPermissions": List[
            ClientGetDatabaseResponseDatabaseCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)

ClientGetDatabaseResponseTypeDef = TypedDict(
    "ClientGetDatabaseResponseTypeDef",
    {"Database": ClientGetDatabaseResponseDatabaseTypeDef},
    total=False,
)

ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsTypeDef = TypedDict(
    "ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientGetDatabasesResponseDatabaseListTypeDef = TypedDict(
    "ClientGetDatabasesResponseDatabaseListTypeDef",
    {
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTime": datetime,
        "CreateTableDefaultPermissions": List[
            ClientGetDatabasesResponseDatabaseListCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)

ClientGetDatabasesResponseTypeDef = TypedDict(
    "ClientGetDatabasesResponseTypeDef",
    {"DatabaseList": List[ClientGetDatabasesResponseDatabaseListTypeDef], "NextToken": str},
    total=False,
)

ClientGetDataflowGraphResponseDagEdgesTypeDef = TypedDict(
    "ClientGetDataflowGraphResponseDagEdgesTypeDef",
    {"Source": str, "Target": str, "TargetParameter": str},
    total=False,
)

ClientGetDataflowGraphResponseDagNodesArgsTypeDef = TypedDict(
    "ClientGetDataflowGraphResponseDagNodesArgsTypeDef",
    {"Name": str, "Value": str, "Param": bool},
    total=False,
)

ClientGetDataflowGraphResponseDagNodesTypeDef = TypedDict(
    "ClientGetDataflowGraphResponseDagNodesTypeDef",
    {
        "Id": str,
        "NodeType": str,
        "Args": List[ClientGetDataflowGraphResponseDagNodesArgsTypeDef],
        "LineNumber": int,
    },
    total=False,
)

ClientGetDataflowGraphResponseTypeDef = TypedDict(
    "ClientGetDataflowGraphResponseTypeDef",
    {
        "DagNodes": List[ClientGetDataflowGraphResponseDagNodesTypeDef],
        "DagEdges": List[ClientGetDataflowGraphResponseDagEdgesTypeDef],
    },
    total=False,
)

ClientGetDevEndpointResponseDevEndpointTypeDef = TypedDict(
    "ClientGetDevEndpointResponseDevEndpointTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)

ClientGetDevEndpointResponseTypeDef = TypedDict(
    "ClientGetDevEndpointResponseTypeDef",
    {"DevEndpoint": ClientGetDevEndpointResponseDevEndpointTypeDef},
    total=False,
)

ClientGetDevEndpointsResponseDevEndpointsTypeDef = TypedDict(
    "ClientGetDevEndpointsResponseDevEndpointsTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)

ClientGetDevEndpointsResponseTypeDef = TypedDict(
    "ClientGetDevEndpointsResponseTypeDef",
    {"DevEndpoints": List[ClientGetDevEndpointsResponseDevEndpointsTypeDef], "NextToken": str},
    total=False,
)

ClientGetJobBookmarkResponseJobBookmarkEntryTypeDef = TypedDict(
    "ClientGetJobBookmarkResponseJobBookmarkEntryTypeDef",
    {
        "JobName": str,
        "Version": int,
        "Run": int,
        "Attempt": int,
        "PreviousRunId": str,
        "RunId": str,
        "JobBookmark": str,
    },
    total=False,
)

ClientGetJobBookmarkResponseTypeDef = TypedDict(
    "ClientGetJobBookmarkResponseTypeDef",
    {"JobBookmarkEntry": ClientGetJobBookmarkResponseJobBookmarkEntryTypeDef},
    total=False,
)

ClientGetJobResponseJobCommandTypeDef = TypedDict(
    "ClientGetJobResponseJobCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)

ClientGetJobResponseJobConnectionsTypeDef = TypedDict(
    "ClientGetJobResponseJobConnectionsTypeDef", {"Connections": List[str]}, total=False
)

ClientGetJobResponseJobExecutionPropertyTypeDef = TypedDict(
    "ClientGetJobResponseJobExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)

ClientGetJobResponseJobNotificationPropertyTypeDef = TypedDict(
    "ClientGetJobResponseJobNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)

ClientGetJobResponseJobTypeDef = TypedDict(
    "ClientGetJobResponseJobTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": ClientGetJobResponseJobExecutionPropertyTypeDef,
        "Command": ClientGetJobResponseJobCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": ClientGetJobResponseJobConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetJobResponseJobNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientGetJobResponseTypeDef = TypedDict(
    "ClientGetJobResponseTypeDef", {"Job": ClientGetJobResponseJobTypeDef}, total=False
)

ClientGetJobRunResponseJobRunNotificationPropertyTypeDef = TypedDict(
    "ClientGetJobRunResponseJobRunNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetJobRunResponseJobRunPredecessorRunsTypeDef = TypedDict(
    "ClientGetJobRunResponseJobRunPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)

ClientGetJobRunResponseJobRunTypeDef = TypedDict(
    "ClientGetJobRunResponseJobRunTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[ClientGetJobRunResponseJobRunPredecessorRunsTypeDef],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetJobRunResponseJobRunNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientGetJobRunResponseTypeDef = TypedDict(
    "ClientGetJobRunResponseTypeDef", {"JobRun": ClientGetJobRunResponseJobRunTypeDef}, total=False
)

ClientGetJobRunsResponseJobRunsNotificationPropertyTypeDef = TypedDict(
    "ClientGetJobRunsResponseJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetJobRunsResponseJobRunsPredecessorRunsTypeDef = TypedDict(
    "ClientGetJobRunsResponseJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)

ClientGetJobRunsResponseJobRunsTypeDef = TypedDict(
    "ClientGetJobRunsResponseJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[ClientGetJobRunsResponseJobRunsPredecessorRunsTypeDef],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetJobRunsResponseJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientGetJobRunsResponseTypeDef = TypedDict(
    "ClientGetJobRunsResponseTypeDef",
    {"JobRuns": List[ClientGetJobRunsResponseJobRunsTypeDef], "NextToken": str},
    total=False,
)

ClientGetJobsResponseJobsCommandTypeDef = TypedDict(
    "ClientGetJobsResponseJobsCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)

ClientGetJobsResponseJobsConnectionsTypeDef = TypedDict(
    "ClientGetJobsResponseJobsConnectionsTypeDef", {"Connections": List[str]}, total=False
)

ClientGetJobsResponseJobsExecutionPropertyTypeDef = TypedDict(
    "ClientGetJobsResponseJobsExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)

ClientGetJobsResponseJobsNotificationPropertyTypeDef = TypedDict(
    "ClientGetJobsResponseJobsNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)

ClientGetJobsResponseJobsTypeDef = TypedDict(
    "ClientGetJobsResponseJobsTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": ClientGetJobsResponseJobsExecutionPropertyTypeDef,
        "Command": ClientGetJobsResponseJobsCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": ClientGetJobsResponseJobsConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetJobsResponseJobsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientGetJobsResponseTypeDef = TypedDict(
    "ClientGetJobsResponseTypeDef",
    {"Jobs": List[ClientGetJobsResponseJobsTypeDef], "NextToken": str},
    total=False,
)

ClientGetMappingLocationDynamoDBTypeDef = TypedDict(
    "ClientGetMappingLocationDynamoDBTypeDef",
    {"Name": str, "Value": str, "Param": bool},
    total=False,
)

_RequiredClientGetMappingLocationJdbcTypeDef = TypedDict(
    "_RequiredClientGetMappingLocationJdbcTypeDef", {"Name": str}
)
_OptionalClientGetMappingLocationJdbcTypeDef = TypedDict(
    "_OptionalClientGetMappingLocationJdbcTypeDef", {"Value": str, "Param": bool}, total=False
)


class ClientGetMappingLocationJdbcTypeDef(
    _RequiredClientGetMappingLocationJdbcTypeDef, _OptionalClientGetMappingLocationJdbcTypeDef
):
    pass


ClientGetMappingLocationS3TypeDef = TypedDict(
    "ClientGetMappingLocationS3TypeDef", {"Name": str, "Value": str, "Param": bool}, total=False
)

ClientGetMappingLocationTypeDef = TypedDict(
    "ClientGetMappingLocationTypeDef",
    {
        "Jdbc": List[ClientGetMappingLocationJdbcTypeDef],
        "S3": List[ClientGetMappingLocationS3TypeDef],
        "DynamoDB": List[ClientGetMappingLocationDynamoDBTypeDef],
    },
    total=False,
)

ClientGetMappingResponseMappingTypeDef = TypedDict(
    "ClientGetMappingResponseMappingTypeDef",
    {
        "SourceTable": str,
        "SourcePath": str,
        "SourceType": str,
        "TargetTable": str,
        "TargetPath": str,
        "TargetType": str,
    },
    total=False,
)

ClientGetMappingResponseTypeDef = TypedDict(
    "ClientGetMappingResponseTypeDef",
    {"Mapping": List[ClientGetMappingResponseMappingTypeDef]},
    total=False,
)

_RequiredClientGetMappingSinksTypeDef = TypedDict(
    "_RequiredClientGetMappingSinksTypeDef", {"DatabaseName": str}
)
_OptionalClientGetMappingSinksTypeDef = TypedDict(
    "_OptionalClientGetMappingSinksTypeDef", {"TableName": str}, total=False
)


class ClientGetMappingSinksTypeDef(
    _RequiredClientGetMappingSinksTypeDef, _OptionalClientGetMappingSinksTypeDef
):
    pass


_RequiredClientGetMappingSourceTypeDef = TypedDict(
    "_RequiredClientGetMappingSourceTypeDef", {"DatabaseName": str}
)
_OptionalClientGetMappingSourceTypeDef = TypedDict(
    "_OptionalClientGetMappingSourceTypeDef", {"TableName": str}, total=False
)


class ClientGetMappingSourceTypeDef(
    _RequiredClientGetMappingSourceTypeDef, _OptionalClientGetMappingSourceTypeDef
):
    pass


ClientGetMlTaskRunResponsePropertiesExportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunResponsePropertiesExportLabelsTaskRunPropertiesTypeDef",
    {"OutputS3Path": str},
    total=False,
)

ClientGetMlTaskRunResponsePropertiesFindMatchesTaskRunPropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunResponsePropertiesFindMatchesTaskRunPropertiesTypeDef",
    {"JobId": str, "JobName": str, "JobRunId": str},
    total=False,
)

ClientGetMlTaskRunResponsePropertiesImportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunResponsePropertiesImportLabelsTaskRunPropertiesTypeDef",
    {"InputS3Path": str, "Replace": bool},
    total=False,
)

ClientGetMlTaskRunResponsePropertiesLabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunResponsePropertiesLabelingSetGenerationTaskRunPropertiesTypeDef",
    {"OutputS3Path": str},
    total=False,
)

ClientGetMlTaskRunResponsePropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunResponsePropertiesTypeDef",
    {
        "TaskType": Literal[
            "EVALUATION",
            "LABELING_SET_GENERATION",
            "IMPORT_LABELS",
            "EXPORT_LABELS",
            "FIND_MATCHES",
        ],
        "ImportLabelsTaskRunProperties": ClientGetMlTaskRunResponsePropertiesImportLabelsTaskRunPropertiesTypeDef,
        "ExportLabelsTaskRunProperties": ClientGetMlTaskRunResponsePropertiesExportLabelsTaskRunPropertiesTypeDef,
        "LabelingSetGenerationTaskRunProperties": ClientGetMlTaskRunResponsePropertiesLabelingSetGenerationTaskRunPropertiesTypeDef,
        "FindMatchesTaskRunProperties": ClientGetMlTaskRunResponsePropertiesFindMatchesTaskRunPropertiesTypeDef,
    },
    total=False,
)

ClientGetMlTaskRunResponseTypeDef = TypedDict(
    "ClientGetMlTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "LogGroupName": str,
        "Properties": ClientGetMlTaskRunResponsePropertiesTypeDef,
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
    },
    total=False,
)

ClientGetMlTaskRunsFilterTypeDef = TypedDict(
    "ClientGetMlTaskRunsFilterTypeDef",
    {
        "TaskRunType": Literal[
            "EVALUATION",
            "LABELING_SET_GENERATION",
            "IMPORT_LABELS",
            "EXPORT_LABELS",
            "FIND_MATCHES",
        ],
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "StartedBefore": datetime,
        "StartedAfter": datetime,
    },
    total=False,
)

ClientGetMlTaskRunsResponseTaskRunsPropertiesExportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesExportLabelsTaskRunPropertiesTypeDef",
    {"OutputS3Path": str},
    total=False,
)

ClientGetMlTaskRunsResponseTaskRunsPropertiesFindMatchesTaskRunPropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesFindMatchesTaskRunPropertiesTypeDef",
    {"JobId": str, "JobName": str, "JobRunId": str},
    total=False,
)

ClientGetMlTaskRunsResponseTaskRunsPropertiesImportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesImportLabelsTaskRunPropertiesTypeDef",
    {"InputS3Path": str, "Replace": bool},
    total=False,
)

ClientGetMlTaskRunsResponseTaskRunsPropertiesLabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesLabelingSetGenerationTaskRunPropertiesTypeDef",
    {"OutputS3Path": str},
    total=False,
)

ClientGetMlTaskRunsResponseTaskRunsPropertiesTypeDef = TypedDict(
    "ClientGetMlTaskRunsResponseTaskRunsPropertiesTypeDef",
    {
        "TaskType": Literal[
            "EVALUATION",
            "LABELING_SET_GENERATION",
            "IMPORT_LABELS",
            "EXPORT_LABELS",
            "FIND_MATCHES",
        ],
        "ImportLabelsTaskRunProperties": ClientGetMlTaskRunsResponseTaskRunsPropertiesImportLabelsTaskRunPropertiesTypeDef,
        "ExportLabelsTaskRunProperties": ClientGetMlTaskRunsResponseTaskRunsPropertiesExportLabelsTaskRunPropertiesTypeDef,
        "LabelingSetGenerationTaskRunProperties": ClientGetMlTaskRunsResponseTaskRunsPropertiesLabelingSetGenerationTaskRunPropertiesTypeDef,
        "FindMatchesTaskRunProperties": ClientGetMlTaskRunsResponseTaskRunsPropertiesFindMatchesTaskRunPropertiesTypeDef,
    },
    total=False,
)

ClientGetMlTaskRunsResponseTaskRunsTypeDef = TypedDict(
    "ClientGetMlTaskRunsResponseTaskRunsTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "LogGroupName": str,
        "Properties": ClientGetMlTaskRunsResponseTaskRunsPropertiesTypeDef,
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
    },
    total=False,
)

ClientGetMlTaskRunsResponseTypeDef = TypedDict(
    "ClientGetMlTaskRunsResponseTypeDef",
    {"TaskRuns": List[ClientGetMlTaskRunsResponseTaskRunsTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientGetMlTaskRunsSortTypeDef = TypedDict(
    "_RequiredClientGetMlTaskRunsSortTypeDef",
    {"Column": Literal["TASK_RUN_TYPE", "STATUS", "STARTED"]},
)
_OptionalClientGetMlTaskRunsSortTypeDef = TypedDict(
    "_OptionalClientGetMlTaskRunsSortTypeDef",
    {"SortDirection": Literal["DESCENDING", "ASCENDING"]},
    total=False,
)


class ClientGetMlTaskRunsSortTypeDef(
    _RequiredClientGetMlTaskRunsSortTypeDef, _OptionalClientGetMlTaskRunsSortTypeDef
):
    pass


ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef = TypedDict(
    "ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef",
    {
        "NumTruePositives": int,
        "NumFalsePositives": int,
        "NumTrueNegatives": int,
        "NumFalseNegatives": int,
    },
    total=False,
)

ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsTypeDef = TypedDict(
    "ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsTypeDef",
    {
        "AreaUnderPRCurve": float,
        "Precision": float,
        "Recall": float,
        "F1": float,
        "ConfusionMatrix": ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef,
    },
    total=False,
)

ClientGetMlTransformResponseEvaluationMetricsTypeDef = TypedDict(
    "ClientGetMlTransformResponseEvaluationMetricsTypeDef",
    {
        "TransformType": str,
        "FindMatchesMetrics": ClientGetMlTransformResponseEvaluationMetricsFindMatchesMetricsTypeDef,
    },
    total=False,
)

ClientGetMlTransformResponseInputRecordTablesTypeDef = TypedDict(
    "ClientGetMlTransformResponseInputRecordTablesTypeDef",
    {"DatabaseName": str, "TableName": str, "CatalogId": str, "ConnectionName": str},
    total=False,
)

ClientGetMlTransformResponseParametersFindMatchesParametersTypeDef = TypedDict(
    "ClientGetMlTransformResponseParametersFindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)

ClientGetMlTransformResponseParametersTypeDef = TypedDict(
    "ClientGetMlTransformResponseParametersTypeDef",
    {
        "TransformType": str,
        "FindMatchesParameters": ClientGetMlTransformResponseParametersFindMatchesParametersTypeDef,
    },
    total=False,
)

ClientGetMlTransformResponseSchemaTypeDef = TypedDict(
    "ClientGetMlTransformResponseSchemaTypeDef", {"Name": str, "DataType": str}, total=False
)

ClientGetMlTransformResponseTypeDef = TypedDict(
    "ClientGetMlTransformResponseTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": Literal["NOT_READY", "READY", "DELETING"],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List[ClientGetMlTransformResponseInputRecordTablesTypeDef],
        "Parameters": ClientGetMlTransformResponseParametersTypeDef,
        "EvaluationMetrics": ClientGetMlTransformResponseEvaluationMetricsTypeDef,
        "LabelCount": int,
        "Schema": List[ClientGetMlTransformResponseSchemaTypeDef],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
    },
    total=False,
)

ClientGetMlTransformsFilterSchemaTypeDef = TypedDict(
    "ClientGetMlTransformsFilterSchemaTypeDef", {"Name": str, "DataType": str}, total=False
)

ClientGetMlTransformsFilterTypeDef = TypedDict(
    "ClientGetMlTransformsFilterTypeDef",
    {
        "Name": str,
        "TransformType": str,
        "Status": Literal["NOT_READY", "READY", "DELETING"],
        "GlueVersion": str,
        "CreatedBefore": datetime,
        "CreatedAfter": datetime,
        "LastModifiedBefore": datetime,
        "LastModifiedAfter": datetime,
        "Schema": List[ClientGetMlTransformsFilterSchemaTypeDef],
    },
    total=False,
)

ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef = TypedDict(
    "ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef",
    {
        "NumTruePositives": int,
        "NumFalsePositives": int,
        "NumTrueNegatives": int,
        "NumFalseNegatives": int,
    },
    total=False,
)

ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsTypeDef = TypedDict(
    "ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsTypeDef",
    {
        "AreaUnderPRCurve": float,
        "Precision": float,
        "Recall": float,
        "F1": float,
        "ConfusionMatrix": ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsConfusionMatrixTypeDef,
    },
    total=False,
)

ClientGetMlTransformsResponseTransformsEvaluationMetricsTypeDef = TypedDict(
    "ClientGetMlTransformsResponseTransformsEvaluationMetricsTypeDef",
    {
        "TransformType": str,
        "FindMatchesMetrics": ClientGetMlTransformsResponseTransformsEvaluationMetricsFindMatchesMetricsTypeDef,
    },
    total=False,
)

ClientGetMlTransformsResponseTransformsInputRecordTablesTypeDef = TypedDict(
    "ClientGetMlTransformsResponseTransformsInputRecordTablesTypeDef",
    {"DatabaseName": str, "TableName": str, "CatalogId": str, "ConnectionName": str},
    total=False,
)

ClientGetMlTransformsResponseTransformsParametersFindMatchesParametersTypeDef = TypedDict(
    "ClientGetMlTransformsResponseTransformsParametersFindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)

ClientGetMlTransformsResponseTransformsParametersTypeDef = TypedDict(
    "ClientGetMlTransformsResponseTransformsParametersTypeDef",
    {
        "TransformType": str,
        "FindMatchesParameters": ClientGetMlTransformsResponseTransformsParametersFindMatchesParametersTypeDef,
    },
    total=False,
)

ClientGetMlTransformsResponseTransformsSchemaTypeDef = TypedDict(
    "ClientGetMlTransformsResponseTransformsSchemaTypeDef",
    {"Name": str, "DataType": str},
    total=False,
)

ClientGetMlTransformsResponseTransformsTypeDef = TypedDict(
    "ClientGetMlTransformsResponseTransformsTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": Literal["NOT_READY", "READY", "DELETING"],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List[ClientGetMlTransformsResponseTransformsInputRecordTablesTypeDef],
        "Parameters": ClientGetMlTransformsResponseTransformsParametersTypeDef,
        "EvaluationMetrics": ClientGetMlTransformsResponseTransformsEvaluationMetricsTypeDef,
        "LabelCount": int,
        "Schema": List[ClientGetMlTransformsResponseTransformsSchemaTypeDef],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
    },
    total=False,
)

ClientGetMlTransformsResponseTypeDef = TypedDict(
    "ClientGetMlTransformsResponseTypeDef",
    {"Transforms": List[ClientGetMlTransformsResponseTransformsTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientGetMlTransformsSortTypeDef = TypedDict(
    "_RequiredClientGetMlTransformsSortTypeDef",
    {"Column": Literal["NAME", "TRANSFORM_TYPE", "STATUS", "CREATED", "LAST_MODIFIED"]},
)
_OptionalClientGetMlTransformsSortTypeDef = TypedDict(
    "_OptionalClientGetMlTransformsSortTypeDef",
    {"SortDirection": Literal["DESCENDING", "ASCENDING"]},
    total=False,
)


class ClientGetMlTransformsSortTypeDef(
    _RequiredClientGetMlTransformsSortTypeDef, _OptionalClientGetMlTransformsSortTypeDef
):
    pass


ClientGetPartitionResponsePartitionStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientGetPartitionResponsePartitionStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetPartitionResponsePartitionStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientGetPartitionResponsePartitionStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetPartitionResponsePartitionStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientGetPartitionResponsePartitionStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientGetPartitionResponsePartitionStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientGetPartitionResponsePartitionStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientGetPartitionResponsePartitionStorageDescriptorTypeDef = TypedDict(
    "ClientGetPartitionResponsePartitionStorageDescriptorTypeDef",
    {
        "Columns": List[ClientGetPartitionResponsePartitionStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetPartitionResponsePartitionStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientGetPartitionResponsePartitionStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetPartitionResponsePartitionStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientGetPartitionResponsePartitionTypeDef = TypedDict(
    "ClientGetPartitionResponsePartitionTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientGetPartitionResponsePartitionStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)

ClientGetPartitionResponseTypeDef = TypedDict(
    "ClientGetPartitionResponseTypeDef",
    {"Partition": ClientGetPartitionResponsePartitionTypeDef},
    total=False,
)

ClientGetPartitionsResponsePartitionsStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientGetPartitionsResponsePartitionsStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetPartitionsResponsePartitionsStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientGetPartitionsResponsePartitionsStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetPartitionsResponsePartitionsStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientGetPartitionsResponsePartitionsStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientGetPartitionsResponsePartitionsStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientGetPartitionsResponsePartitionsStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientGetPartitionsResponsePartitionsStorageDescriptorTypeDef = TypedDict(
    "ClientGetPartitionsResponsePartitionsStorageDescriptorTypeDef",
    {
        "Columns": List[ClientGetPartitionsResponsePartitionsStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetPartitionsResponsePartitionsStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientGetPartitionsResponsePartitionsStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetPartitionsResponsePartitionsStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientGetPartitionsResponsePartitionsTypeDef = TypedDict(
    "ClientGetPartitionsResponsePartitionsTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientGetPartitionsResponsePartitionsStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)

ClientGetPartitionsResponseTypeDef = TypedDict(
    "ClientGetPartitionsResponseTypeDef",
    {"Partitions": List[ClientGetPartitionsResponsePartitionsTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientGetPartitionsSegmentTypeDef = TypedDict(
    "_RequiredClientGetPartitionsSegmentTypeDef", {"SegmentNumber": int}
)
_OptionalClientGetPartitionsSegmentTypeDef = TypedDict(
    "_OptionalClientGetPartitionsSegmentTypeDef", {"TotalSegments": int}, total=False
)


class ClientGetPartitionsSegmentTypeDef(
    _RequiredClientGetPartitionsSegmentTypeDef, _OptionalClientGetPartitionsSegmentTypeDef
):
    pass


ClientGetPlanLocationDynamoDBTypeDef = TypedDict(
    "ClientGetPlanLocationDynamoDBTypeDef", {"Name": str, "Value": str, "Param": bool}, total=False
)

_RequiredClientGetPlanLocationJdbcTypeDef = TypedDict(
    "_RequiredClientGetPlanLocationJdbcTypeDef", {"Name": str}
)
_OptionalClientGetPlanLocationJdbcTypeDef = TypedDict(
    "_OptionalClientGetPlanLocationJdbcTypeDef", {"Value": str, "Param": bool}, total=False
)


class ClientGetPlanLocationJdbcTypeDef(
    _RequiredClientGetPlanLocationJdbcTypeDef, _OptionalClientGetPlanLocationJdbcTypeDef
):
    pass


ClientGetPlanLocationS3TypeDef = TypedDict(
    "ClientGetPlanLocationS3TypeDef", {"Name": str, "Value": str, "Param": bool}, total=False
)

ClientGetPlanLocationTypeDef = TypedDict(
    "ClientGetPlanLocationTypeDef",
    {
        "Jdbc": List[ClientGetPlanLocationJdbcTypeDef],
        "S3": List[ClientGetPlanLocationS3TypeDef],
        "DynamoDB": List[ClientGetPlanLocationDynamoDBTypeDef],
    },
    total=False,
)

ClientGetPlanMappingTypeDef = TypedDict(
    "ClientGetPlanMappingTypeDef",
    {
        "SourceTable": str,
        "SourcePath": str,
        "SourceType": str,
        "TargetTable": str,
        "TargetPath": str,
        "TargetType": str,
    },
    total=False,
)

ClientGetPlanResponseTypeDef = TypedDict(
    "ClientGetPlanResponseTypeDef", {"PythonScript": str, "ScalaCode": str}, total=False
)

_RequiredClientGetPlanSinksTypeDef = TypedDict(
    "_RequiredClientGetPlanSinksTypeDef", {"DatabaseName": str}
)
_OptionalClientGetPlanSinksTypeDef = TypedDict(
    "_OptionalClientGetPlanSinksTypeDef", {"TableName": str}, total=False
)


class ClientGetPlanSinksTypeDef(
    _RequiredClientGetPlanSinksTypeDef, _OptionalClientGetPlanSinksTypeDef
):
    pass


_RequiredClientGetPlanSourceTypeDef = TypedDict(
    "_RequiredClientGetPlanSourceTypeDef", {"DatabaseName": str}
)
_OptionalClientGetPlanSourceTypeDef = TypedDict(
    "_OptionalClientGetPlanSourceTypeDef", {"TableName": str}, total=False
)


class ClientGetPlanSourceTypeDef(
    _RequiredClientGetPlanSourceTypeDef, _OptionalClientGetPlanSourceTypeDef
):
    pass


ClientGetResourcePolicyResponseTypeDef = TypedDict(
    "ClientGetResourcePolicyResponseTypeDef",
    {"PolicyInJson": str, "PolicyHash": str, "CreateTime": datetime, "UpdateTime": datetime},
    total=False,
)

ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef = TypedDict(
    "ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef",
    {"CloudWatchEncryptionMode": Literal["DISABLED", "SSE-KMS"], "KmsKeyArn": str},
    total=False,
)

ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef = TypedDict(
    "ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    {"JobBookmarksEncryptionMode": Literal["DISABLED", "CSE-KMS"], "KmsKeyArn": str},
    total=False,
)

ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef = TypedDict(
    "ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef",
    {"S3EncryptionMode": Literal["DISABLED", "SSE-KMS", "SSE-S3"], "KmsKeyArn": str},
    total=False,
)

ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationTypeDef",
    {
        "S3Encryption": List[
            ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationS3EncryptionTypeDef
        ],
        "CloudWatchEncryption": ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationCloudWatchEncryptionTypeDef,
        "JobBookmarksEncryption": ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionTypeDef,
    },
    total=False,
)

ClientGetSecurityConfigurationResponseSecurityConfigurationTypeDef = TypedDict(
    "ClientGetSecurityConfigurationResponseSecurityConfigurationTypeDef",
    {
        "Name": str,
        "CreatedTimeStamp": datetime,
        "EncryptionConfiguration": ClientGetSecurityConfigurationResponseSecurityConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientGetSecurityConfigurationResponseTypeDef = TypedDict(
    "ClientGetSecurityConfigurationResponseTypeDef",
    {"SecurityConfiguration": ClientGetSecurityConfigurationResponseSecurityConfigurationTypeDef},
    total=False,
)

ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef = TypedDict(
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef",
    {"CloudWatchEncryptionMode": Literal["DISABLED", "SSE-KMS"], "KmsKeyArn": str},
    total=False,
)

ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef = TypedDict(
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    {"JobBookmarksEncryptionMode": Literal["DISABLED", "CSE-KMS"], "KmsKeyArn": str},
    total=False,
)

ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef = TypedDict(
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef",
    {"S3EncryptionMode": Literal["DISABLED", "SSE-KMS", "SSE-S3"], "KmsKeyArn": str},
    total=False,
)

ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationTypeDef = TypedDict(
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationTypeDef",
    {
        "S3Encryption": List[
            ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef
        ],
        "CloudWatchEncryption": ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef,
        "JobBookmarksEncryption": ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef,
    },
    total=False,
)

ClientGetSecurityConfigurationsResponseSecurityConfigurationsTypeDef = TypedDict(
    "ClientGetSecurityConfigurationsResponseSecurityConfigurationsTypeDef",
    {
        "Name": str,
        "CreatedTimeStamp": datetime,
        "EncryptionConfiguration": ClientGetSecurityConfigurationsResponseSecurityConfigurationsEncryptionConfigurationTypeDef,
    },
    total=False,
)

ClientGetSecurityConfigurationsResponseTypeDef = TypedDict(
    "ClientGetSecurityConfigurationsResponseTypeDef",
    {
        "SecurityConfigurations": List[
            ClientGetSecurityConfigurationsResponseSecurityConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetTableResponseTablePartitionKeysTypeDef = TypedDict(
    "ClientGetTableResponseTablePartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTableResponseTableStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientGetTableResponseTableStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTableResponseTableStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientGetTableResponseTableStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTableResponseTableStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientGetTableResponseTableStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientGetTableResponseTableStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientGetTableResponseTableStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientGetTableResponseTableStorageDescriptorTypeDef = TypedDict(
    "ClientGetTableResponseTableStorageDescriptorTypeDef",
    {
        "Columns": List[ClientGetTableResponseTableStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetTableResponseTableStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientGetTableResponseTableStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetTableResponseTableStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientGetTableResponseTableTypeDef = TypedDict(
    "ClientGetTableResponseTableTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientGetTableResponseTableStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientGetTableResponseTablePartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)

ClientGetTableResponseTypeDef = TypedDict(
    "ClientGetTableResponseTypeDef", {"Table": ClientGetTableResponseTableTypeDef}, total=False
)

ClientGetTableVersionResponseTableVersionTablePartitionKeysTypeDef = TypedDict(
    "ClientGetTableVersionResponseTableVersionTablePartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTableVersionResponseTableVersionTableStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTableVersionResponseTableVersionTableStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTableVersionResponseTableVersionTableStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientGetTableVersionResponseTableVersionTableStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientGetTableVersionResponseTableVersionTableStorageDescriptorTypeDef = TypedDict(
    "ClientGetTableVersionResponseTableVersionTableStorageDescriptorTypeDef",
    {
        "Columns": List[
            ClientGetTableVersionResponseTableVersionTableStorageDescriptorColumnsTypeDef
        ],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetTableVersionResponseTableVersionTableStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientGetTableVersionResponseTableVersionTableStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetTableVersionResponseTableVersionTableStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientGetTableVersionResponseTableVersionTableTypeDef = TypedDict(
    "ClientGetTableVersionResponseTableVersionTableTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientGetTableVersionResponseTableVersionTableStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientGetTableVersionResponseTableVersionTablePartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)

ClientGetTableVersionResponseTableVersionTypeDef = TypedDict(
    "ClientGetTableVersionResponseTableVersionTypeDef",
    {"Table": ClientGetTableVersionResponseTableVersionTableTypeDef, "VersionId": str},
    total=False,
)

ClientGetTableVersionResponseTypeDef = TypedDict(
    "ClientGetTableVersionResponseTypeDef",
    {"TableVersion": ClientGetTableVersionResponseTableVersionTypeDef},
    total=False,
)

ClientGetTableVersionsResponseTableVersionsTablePartitionKeysTypeDef = TypedDict(
    "ClientGetTableVersionsResponseTableVersionsTablePartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorTypeDef = TypedDict(
    "ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorTypeDef",
    {
        "Columns": List[
            ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorColumnsTypeDef
        ],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientGetTableVersionsResponseTableVersionsTableTypeDef = TypedDict(
    "ClientGetTableVersionsResponseTableVersionsTableTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientGetTableVersionsResponseTableVersionsTableStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientGetTableVersionsResponseTableVersionsTablePartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)

ClientGetTableVersionsResponseTableVersionsTypeDef = TypedDict(
    "ClientGetTableVersionsResponseTableVersionsTypeDef",
    {"Table": ClientGetTableVersionsResponseTableVersionsTableTypeDef, "VersionId": str},
    total=False,
)

ClientGetTableVersionsResponseTypeDef = TypedDict(
    "ClientGetTableVersionsResponseTypeDef",
    {"TableVersions": List[ClientGetTableVersionsResponseTableVersionsTypeDef], "NextToken": str},
    total=False,
)

ClientGetTablesResponseTableListPartitionKeysTypeDef = TypedDict(
    "ClientGetTablesResponseTableListPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTablesResponseTableListStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientGetTablesResponseTableListStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTablesResponseTableListStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientGetTablesResponseTableListStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetTablesResponseTableListStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientGetTablesResponseTableListStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientGetTablesResponseTableListStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientGetTablesResponseTableListStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientGetTablesResponseTableListStorageDescriptorTypeDef = TypedDict(
    "ClientGetTablesResponseTableListStorageDescriptorTypeDef",
    {
        "Columns": List[ClientGetTablesResponseTableListStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientGetTablesResponseTableListStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientGetTablesResponseTableListStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientGetTablesResponseTableListStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientGetTablesResponseTableListTypeDef = TypedDict(
    "ClientGetTablesResponseTableListTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientGetTablesResponseTableListStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientGetTablesResponseTableListPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)

ClientGetTablesResponseTypeDef = TypedDict(
    "ClientGetTablesResponseTypeDef",
    {"TableList": List[ClientGetTablesResponseTableListTypeDef], "NextToken": str},
    total=False,
)

ClientGetTagsResponseTypeDef = TypedDict(
    "ClientGetTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientGetTriggerResponseTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "ClientGetTriggerResponseTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetTriggerResponseTriggerActionsTypeDef = TypedDict(
    "ClientGetTriggerResponseTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetTriggerResponseTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientGetTriggerResponseTriggerPredicateConditionsTypeDef = TypedDict(
    "ClientGetTriggerResponseTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientGetTriggerResponseTriggerPredicateTypeDef = TypedDict(
    "ClientGetTriggerResponseTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientGetTriggerResponseTriggerPredicateConditionsTypeDef],
    },
    total=False,
)

ClientGetTriggerResponseTriggerTypeDef = TypedDict(
    "ClientGetTriggerResponseTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientGetTriggerResponseTriggerActionsTypeDef],
        "Predicate": ClientGetTriggerResponseTriggerPredicateTypeDef,
    },
    total=False,
)

ClientGetTriggerResponseTypeDef = TypedDict(
    "ClientGetTriggerResponseTypeDef",
    {"Trigger": ClientGetTriggerResponseTriggerTypeDef},
    total=False,
)

ClientGetTriggersResponseTriggersActionsNotificationPropertyTypeDef = TypedDict(
    "ClientGetTriggersResponseTriggersActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetTriggersResponseTriggersActionsTypeDef = TypedDict(
    "ClientGetTriggersResponseTriggersActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetTriggersResponseTriggersActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientGetTriggersResponseTriggersPredicateConditionsTypeDef = TypedDict(
    "ClientGetTriggersResponseTriggersPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientGetTriggersResponseTriggersPredicateTypeDef = TypedDict(
    "ClientGetTriggersResponseTriggersPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientGetTriggersResponseTriggersPredicateConditionsTypeDef],
    },
    total=False,
)

ClientGetTriggersResponseTriggersTypeDef = TypedDict(
    "ClientGetTriggersResponseTriggersTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientGetTriggersResponseTriggersActionsTypeDef],
        "Predicate": ClientGetTriggersResponseTriggersPredicateTypeDef,
    },
    total=False,
)

ClientGetTriggersResponseTypeDef = TypedDict(
    "ClientGetTriggersResponseTypeDef",
    {"Triggers": List[ClientGetTriggersResponseTriggersTypeDef], "NextToken": str},
    total=False,
)

ClientGetUserDefinedFunctionResponseUserDefinedFunctionResourceUrisTypeDef = TypedDict(
    "ClientGetUserDefinedFunctionResponseUserDefinedFunctionResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)

ClientGetUserDefinedFunctionResponseUserDefinedFunctionTypeDef = TypedDict(
    "ClientGetUserDefinedFunctionResponseUserDefinedFunctionTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "CreateTime": datetime,
        "ResourceUris": List[
            ClientGetUserDefinedFunctionResponseUserDefinedFunctionResourceUrisTypeDef
        ],
    },
    total=False,
)

ClientGetUserDefinedFunctionResponseTypeDef = TypedDict(
    "ClientGetUserDefinedFunctionResponseTypeDef",
    {"UserDefinedFunction": ClientGetUserDefinedFunctionResponseUserDefinedFunctionTypeDef},
    total=False,
)

ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsResourceUrisTypeDef = TypedDict(
    "ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)

ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsTypeDef = TypedDict(
    "ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "CreateTime": datetime,
        "ResourceUris": List[
            ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsResourceUrisTypeDef
        ],
    },
    total=False,
)

ClientGetUserDefinedFunctionsResponseTypeDef = TypedDict(
    "ClientGetUserDefinedFunctionsResponseTypeDef",
    {
        "UserDefinedFunctions": List[
            ClientGetUserDefinedFunctionsResponseUserDefinedFunctionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphEdgesTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphNodesTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientGetWorkflowResponseWorkflowGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientGetWorkflowResponseWorkflowGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientGetWorkflowResponseWorkflowGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowGraphTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowGraphTypeDef",
    {
        "Nodes": List[ClientGetWorkflowResponseWorkflowGraphNodesTypeDef],
        "Edges": List[ClientGetWorkflowResponseWorkflowGraphEdgesTypeDef],
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphEdgesTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphNodesTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientGetWorkflowResponseWorkflowLastRunGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientGetWorkflowResponseWorkflowLastRunGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientGetWorkflowResponseWorkflowLastRunGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunGraphTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunGraphTypeDef",
    {
        "Nodes": List[ClientGetWorkflowResponseWorkflowLastRunGraphNodesTypeDef],
        "Edges": List[ClientGetWorkflowResponseWorkflowLastRunGraphEdgesTypeDef],
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunStatisticsTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowLastRunTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowLastRunTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": Literal["RUNNING", "COMPLETED"],
        "Statistics": ClientGetWorkflowResponseWorkflowLastRunStatisticsTypeDef,
        "Graph": ClientGetWorkflowResponseWorkflowLastRunGraphTypeDef,
    },
    total=False,
)

ClientGetWorkflowResponseWorkflowTypeDef = TypedDict(
    "ClientGetWorkflowResponseWorkflowTypeDef",
    {
        "Name": str,
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "LastRun": ClientGetWorkflowResponseWorkflowLastRunTypeDef,
        "Graph": ClientGetWorkflowResponseWorkflowGraphTypeDef,
    },
    total=False,
)

ClientGetWorkflowResponseTypeDef = TypedDict(
    "ClientGetWorkflowResponseTypeDef",
    {"Workflow": ClientGetWorkflowResponseWorkflowTypeDef},
    total=False,
)

ClientGetWorkflowRunPropertiesResponseTypeDef = TypedDict(
    "ClientGetWorkflowRunPropertiesResponseTypeDef", {"RunProperties": Dict[str, str]}, total=False
)

ClientGetWorkflowRunResponseRunGraphEdgesTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesJobDetailsTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientGetWorkflowRunResponseRunGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)

ClientGetWorkflowRunResponseRunGraphNodesTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientGetWorkflowRunResponseRunGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientGetWorkflowRunResponseRunGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientGetWorkflowRunResponseRunGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)

ClientGetWorkflowRunResponseRunGraphTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunGraphTypeDef",
    {
        "Nodes": List[ClientGetWorkflowRunResponseRunGraphNodesTypeDef],
        "Edges": List[ClientGetWorkflowRunResponseRunGraphEdgesTypeDef],
    },
    total=False,
)

ClientGetWorkflowRunResponseRunStatisticsTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)

ClientGetWorkflowRunResponseRunTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseRunTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": Literal["RUNNING", "COMPLETED"],
        "Statistics": ClientGetWorkflowRunResponseRunStatisticsTypeDef,
        "Graph": ClientGetWorkflowRunResponseRunGraphTypeDef,
    },
    total=False,
)

ClientGetWorkflowRunResponseTypeDef = TypedDict(
    "ClientGetWorkflowRunResponseTypeDef",
    {"Run": ClientGetWorkflowRunResponseRunTypeDef},
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphEdgesTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphEdgesTypeDef",
    {"SourceId": str, "DestinationId": str},
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsCrawlsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsCrawlsTypeDef",
    {
        "State": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsTypeDef",
    {"Crawls": List[ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsCrawlsTypeDef]},
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[
            ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsPredecessorRunsTypeDef
        ],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsTypeDef",
    {"JobRuns": List[ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsJobRunsTypeDef]},
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[
            ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateConditionsTypeDef
        ],
    },
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[
            ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerActionsTypeDef
        ],
        "Predicate": ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerPredicateTypeDef,
    },
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTypeDef",
    {"Trigger": ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTriggerTypeDef},
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphNodesTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphNodesTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": ClientGetWorkflowRunsResponseRunsGraphNodesTriggerDetailsTypeDef,
        "JobDetails": ClientGetWorkflowRunsResponseRunsGraphNodesJobDetailsTypeDef,
        "CrawlerDetails": ClientGetWorkflowRunsResponseRunsGraphNodesCrawlerDetailsTypeDef,
    },
    total=False,
)

ClientGetWorkflowRunsResponseRunsGraphTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsGraphTypeDef",
    {
        "Nodes": List[ClientGetWorkflowRunsResponseRunsGraphNodesTypeDef],
        "Edges": List[ClientGetWorkflowRunsResponseRunsGraphEdgesTypeDef],
    },
    total=False,
)

ClientGetWorkflowRunsResponseRunsStatisticsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)

ClientGetWorkflowRunsResponseRunsTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseRunsTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": Literal["RUNNING", "COMPLETED"],
        "Statistics": ClientGetWorkflowRunsResponseRunsStatisticsTypeDef,
        "Graph": ClientGetWorkflowRunsResponseRunsGraphTypeDef,
    },
    total=False,
)

ClientGetWorkflowRunsResponseTypeDef = TypedDict(
    "ClientGetWorkflowRunsResponseTypeDef",
    {"Runs": List[ClientGetWorkflowRunsResponseRunsTypeDef], "NextToken": str},
    total=False,
)

ClientListCrawlersResponseTypeDef = TypedDict(
    "ClientListCrawlersResponseTypeDef", {"CrawlerNames": List[str], "NextToken": str}, total=False
)

ClientListDevEndpointsResponseTypeDef = TypedDict(
    "ClientListDevEndpointsResponseTypeDef",
    {"DevEndpointNames": List[str], "NextToken": str},
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef", {"JobNames": List[str], "NextToken": str}, total=False
)

ClientListTriggersResponseTypeDef = TypedDict(
    "ClientListTriggersResponseTypeDef", {"TriggerNames": List[str], "NextToken": str}, total=False
)

ClientListWorkflowsResponseTypeDef = TypedDict(
    "ClientListWorkflowsResponseTypeDef", {"Workflows": List[str], "NextToken": str}, total=False
)

ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef = TypedDict(
    "ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef",
    {"ReturnConnectionPasswordEncrypted": bool, "AwsKmsKeyId": str},
    total=False,
)

_RequiredClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef = TypedDict(
    "_RequiredClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef",
    {"CatalogEncryptionMode": Literal["DISABLED", "SSE-KMS"]},
)
_OptionalClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef = TypedDict(
    "_OptionalClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef",
    {"SseAwsKmsKeyId": str},
    total=False,
)


class ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef(
    _RequiredClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef,
    _OptionalClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef,
):
    pass


ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef = TypedDict(
    "ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef",
    {
        "EncryptionAtRest": ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestTypeDef,
        "ConnectionPasswordEncryption": ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionTypeDef,
    },
    total=False,
)

ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "ClientPutResourcePolicyResponseTypeDef", {"PolicyHash": str}, total=False
)

ClientResetJobBookmarkResponseJobBookmarkEntryTypeDef = TypedDict(
    "ClientResetJobBookmarkResponseJobBookmarkEntryTypeDef",
    {
        "JobName": str,
        "Version": int,
        "Run": int,
        "Attempt": int,
        "PreviousRunId": str,
        "RunId": str,
        "JobBookmark": str,
    },
    total=False,
)

ClientResetJobBookmarkResponseTypeDef = TypedDict(
    "ClientResetJobBookmarkResponseTypeDef",
    {"JobBookmarkEntry": ClientResetJobBookmarkResponseJobBookmarkEntryTypeDef},
    total=False,
)

ClientSearchTablesFiltersTypeDef = TypedDict(
    "ClientSearchTablesFiltersTypeDef",
    {
        "Key": str,
        "Value": str,
        "Comparator": Literal[
            "EQUALS", "GREATER_THAN", "LESS_THAN", "GREATER_THAN_EQUALS", "LESS_THAN_EQUALS"
        ],
    },
    total=False,
)

ClientSearchTablesResponseTableListPartitionKeysTypeDef = TypedDict(
    "ClientSearchTablesResponseTableListPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientSearchTablesResponseTableListStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientSearchTablesResponseTableListStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientSearchTablesResponseTableListStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientSearchTablesResponseTableListStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientSearchTablesResponseTableListStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientSearchTablesResponseTableListStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientSearchTablesResponseTableListStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientSearchTablesResponseTableListStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientSearchTablesResponseTableListStorageDescriptorTypeDef = TypedDict(
    "ClientSearchTablesResponseTableListStorageDescriptorTypeDef",
    {
        "Columns": List[ClientSearchTablesResponseTableListStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientSearchTablesResponseTableListStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientSearchTablesResponseTableListStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientSearchTablesResponseTableListStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientSearchTablesResponseTableListTypeDef = TypedDict(
    "ClientSearchTablesResponseTableListTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientSearchTablesResponseTableListStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientSearchTablesResponseTableListPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)

ClientSearchTablesResponseTypeDef = TypedDict(
    "ClientSearchTablesResponseTypeDef",
    {"NextToken": str, "TableList": List[ClientSearchTablesResponseTableListTypeDef]},
    total=False,
)

ClientSearchTablesSortCriteriaTypeDef = TypedDict(
    "ClientSearchTablesSortCriteriaTypeDef",
    {"FieldName": str, "Sort": Literal["ASC", "DESC"]},
    total=False,
)

ClientStartExportLabelsTaskRunResponseTypeDef = TypedDict(
    "ClientStartExportLabelsTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)

ClientStartImportLabelsTaskRunResponseTypeDef = TypedDict(
    "ClientStartImportLabelsTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)

ClientStartJobRunNotificationPropertyTypeDef = TypedDict(
    "ClientStartJobRunNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)

ClientStartJobRunResponseTypeDef = TypedDict(
    "ClientStartJobRunResponseTypeDef", {"JobRunId": str}, total=False
)

ClientStartMlEvaluationTaskRunResponseTypeDef = TypedDict(
    "ClientStartMlEvaluationTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)

ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef = TypedDict(
    "ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)

ClientStartTriggerResponseTypeDef = TypedDict(
    "ClientStartTriggerResponseTypeDef", {"Name": str}, total=False
)

ClientStartWorkflowRunResponseTypeDef = TypedDict(
    "ClientStartWorkflowRunResponseTypeDef", {"RunId": str}, total=False
)

ClientStopTriggerResponseTypeDef = TypedDict(
    "ClientStopTriggerResponseTypeDef", {"Name": str}, total=False
)

_RequiredClientUpdateClassifierCsvClassifierTypeDef = TypedDict(
    "_RequiredClientUpdateClassifierCsvClassifierTypeDef", {"Name": str}
)
_OptionalClientUpdateClassifierCsvClassifierTypeDef = TypedDict(
    "_OptionalClientUpdateClassifierCsvClassifierTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class ClientUpdateClassifierCsvClassifierTypeDef(
    _RequiredClientUpdateClassifierCsvClassifierTypeDef,
    _OptionalClientUpdateClassifierCsvClassifierTypeDef,
):
    pass


_RequiredClientUpdateClassifierGrokClassifierTypeDef = TypedDict(
    "_RequiredClientUpdateClassifierGrokClassifierTypeDef", {"Name": str}
)
_OptionalClientUpdateClassifierGrokClassifierTypeDef = TypedDict(
    "_OptionalClientUpdateClassifierGrokClassifierTypeDef",
    {"Classification": str, "GrokPattern": str, "CustomPatterns": str},
    total=False,
)


class ClientUpdateClassifierGrokClassifierTypeDef(
    _RequiredClientUpdateClassifierGrokClassifierTypeDef,
    _OptionalClientUpdateClassifierGrokClassifierTypeDef,
):
    pass


_RequiredClientUpdateClassifierJsonClassifierTypeDef = TypedDict(
    "_RequiredClientUpdateClassifierJsonClassifierTypeDef", {"Name": str}
)
_OptionalClientUpdateClassifierJsonClassifierTypeDef = TypedDict(
    "_OptionalClientUpdateClassifierJsonClassifierTypeDef", {"JsonPath": str}, total=False
)


class ClientUpdateClassifierJsonClassifierTypeDef(
    _RequiredClientUpdateClassifierJsonClassifierTypeDef,
    _OptionalClientUpdateClassifierJsonClassifierTypeDef,
):
    pass


_RequiredClientUpdateClassifierXMLClassifierTypeDef = TypedDict(
    "_RequiredClientUpdateClassifierXMLClassifierTypeDef", {"Name": str}
)
_OptionalClientUpdateClassifierXMLClassifierTypeDef = TypedDict(
    "_OptionalClientUpdateClassifierXMLClassifierTypeDef",
    {"Classification": str, "RowTag": str},
    total=False,
)


class ClientUpdateClassifierXMLClassifierTypeDef(
    _RequiredClientUpdateClassifierXMLClassifierTypeDef,
    _OptionalClientUpdateClassifierXMLClassifierTypeDef,
):
    pass


ClientUpdateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef = TypedDict(
    "ClientUpdateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)

_RequiredClientUpdateConnectionConnectionInputTypeDef = TypedDict(
    "_RequiredClientUpdateConnectionConnectionInputTypeDef", {"Name": str}
)
_OptionalClientUpdateConnectionConnectionInputTypeDef = TypedDict(
    "_OptionalClientUpdateConnectionConnectionInputTypeDef",
    {
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": ClientUpdateConnectionConnectionInputPhysicalConnectionRequirementsTypeDef,
    },
    total=False,
)


class ClientUpdateConnectionConnectionInputTypeDef(
    _RequiredClientUpdateConnectionConnectionInputTypeDef,
    _OptionalClientUpdateConnectionConnectionInputTypeDef,
):
    pass


ClientUpdateCrawlerSchemaChangePolicyTypeDef = TypedDict(
    "ClientUpdateCrawlerSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)

ClientUpdateCrawlerTargetsCatalogTargetsTypeDef = TypedDict(
    "ClientUpdateCrawlerTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)

ClientUpdateCrawlerTargetsDynamoDBTargetsTypeDef = TypedDict(
    "ClientUpdateCrawlerTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)

ClientUpdateCrawlerTargetsJdbcTargetsTypeDef = TypedDict(
    "ClientUpdateCrawlerTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)

ClientUpdateCrawlerTargetsS3TargetsTypeDef = TypedDict(
    "ClientUpdateCrawlerTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)

ClientUpdateCrawlerTargetsTypeDef = TypedDict(
    "ClientUpdateCrawlerTargetsTypeDef",
    {
        "S3Targets": List[ClientUpdateCrawlerTargetsS3TargetsTypeDef],
        "JdbcTargets": List[ClientUpdateCrawlerTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[ClientUpdateCrawlerTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[ClientUpdateCrawlerTargetsCatalogTargetsTypeDef],
    },
    total=False,
)

ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef = TypedDict(
    "ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

_RequiredClientUpdateDatabaseDatabaseInputTypeDef = TypedDict(
    "_RequiredClientUpdateDatabaseDatabaseInputTypeDef", {"Name": str}
)
_OptionalClientUpdateDatabaseDatabaseInputTypeDef = TypedDict(
    "_OptionalClientUpdateDatabaseDatabaseInputTypeDef",
    {
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTableDefaultPermissions": List[
            ClientUpdateDatabaseDatabaseInputCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateDatabaseDatabaseInputTypeDef(
    _RequiredClientUpdateDatabaseDatabaseInputTypeDef,
    _OptionalClientUpdateDatabaseDatabaseInputTypeDef,
):
    pass


ClientUpdateDevEndpointCustomLibrariesTypeDef = TypedDict(
    "ClientUpdateDevEndpointCustomLibrariesTypeDef",
    {"ExtraPythonLibsS3Path": str, "ExtraJarsS3Path": str},
    total=False,
)

ClientUpdateJobJobUpdateCommandTypeDef = TypedDict(
    "ClientUpdateJobJobUpdateCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)

ClientUpdateJobJobUpdateConnectionsTypeDef = TypedDict(
    "ClientUpdateJobJobUpdateConnectionsTypeDef", {"Connections": List[str]}, total=False
)

ClientUpdateJobJobUpdateExecutionPropertyTypeDef = TypedDict(
    "ClientUpdateJobJobUpdateExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)

ClientUpdateJobJobUpdateNotificationPropertyTypeDef = TypedDict(
    "ClientUpdateJobJobUpdateNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)

ClientUpdateJobJobUpdateTypeDef = TypedDict(
    "ClientUpdateJobJobUpdateTypeDef",
    {
        "Description": str,
        "LogUri": str,
        "Role": str,
        "ExecutionProperty": ClientUpdateJobJobUpdateExecutionPropertyTypeDef,
        "Command": ClientUpdateJobJobUpdateCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": ClientUpdateJobJobUpdateConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientUpdateJobJobUpdateNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

ClientUpdateJobResponseTypeDef = TypedDict(
    "ClientUpdateJobResponseTypeDef", {"JobName": str}, total=False
)

ClientUpdateMlTransformParametersFindMatchesParametersTypeDef = TypedDict(
    "ClientUpdateMlTransformParametersFindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)

_RequiredClientUpdateMlTransformParametersTypeDef = TypedDict(
    "_RequiredClientUpdateMlTransformParametersTypeDef", {"TransformType": str}
)
_OptionalClientUpdateMlTransformParametersTypeDef = TypedDict(
    "_OptionalClientUpdateMlTransformParametersTypeDef",
    {"FindMatchesParameters": ClientUpdateMlTransformParametersFindMatchesParametersTypeDef},
    total=False,
)


class ClientUpdateMlTransformParametersTypeDef(
    _RequiredClientUpdateMlTransformParametersTypeDef,
    _OptionalClientUpdateMlTransformParametersTypeDef,
):
    pass


ClientUpdateMlTransformResponseTypeDef = TypedDict(
    "ClientUpdateMlTransformResponseTypeDef", {"TransformId": str}, total=False
)

ClientUpdatePartitionPartitionInputStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientUpdatePartitionPartitionInputStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientUpdatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientUpdatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientUpdatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientUpdatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientUpdatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientUpdatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientUpdatePartitionPartitionInputStorageDescriptorTypeDef = TypedDict(
    "ClientUpdatePartitionPartitionInputStorageDescriptorTypeDef",
    {
        "Columns": List[ClientUpdatePartitionPartitionInputStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientUpdatePartitionPartitionInputStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientUpdatePartitionPartitionInputStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientUpdatePartitionPartitionInputStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

ClientUpdatePartitionPartitionInputTypeDef = TypedDict(
    "ClientUpdatePartitionPartitionInputTypeDef",
    {
        "Values": List[str],
        "LastAccessTime": datetime,
        "StorageDescriptor": ClientUpdatePartitionPartitionInputStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)

ClientUpdateTableTableInputPartitionKeysTypeDef = TypedDict(
    "ClientUpdateTableTableInputPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientUpdateTableTableInputStorageDescriptorColumnsTypeDef = TypedDict(
    "ClientUpdateTableTableInputStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientUpdateTableTableInputStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "ClientUpdateTableTableInputStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientUpdateTableTableInputStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "ClientUpdateTableTableInputStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

ClientUpdateTableTableInputStorageDescriptorSortColumnsTypeDef = TypedDict(
    "ClientUpdateTableTableInputStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

ClientUpdateTableTableInputStorageDescriptorTypeDef = TypedDict(
    "ClientUpdateTableTableInputStorageDescriptorTypeDef",
    {
        "Columns": List[ClientUpdateTableTableInputStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": ClientUpdateTableTableInputStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[ClientUpdateTableTableInputStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": ClientUpdateTableTableInputStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

_RequiredClientUpdateTableTableInputTypeDef = TypedDict(
    "_RequiredClientUpdateTableTableInputTypeDef", {"Name": str}
)
_OptionalClientUpdateTableTableInputTypeDef = TypedDict(
    "_OptionalClientUpdateTableTableInputTypeDef",
    {
        "Description": str,
        "Owner": str,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": ClientUpdateTableTableInputStorageDescriptorTypeDef,
        "PartitionKeys": List[ClientUpdateTableTableInputPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientUpdateTableTableInputTypeDef(
    _RequiredClientUpdateTableTableInputTypeDef, _OptionalClientUpdateTableTableInputTypeDef
):
    pass


ClientUpdateTriggerResponseTriggerActionsNotificationPropertyTypeDef = TypedDict(
    "ClientUpdateTriggerResponseTriggerActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientUpdateTriggerResponseTriggerActionsTypeDef = TypedDict(
    "ClientUpdateTriggerResponseTriggerActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientUpdateTriggerResponseTriggerActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientUpdateTriggerResponseTriggerPredicateConditionsTypeDef = TypedDict(
    "ClientUpdateTriggerResponseTriggerPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientUpdateTriggerResponseTriggerPredicateTypeDef = TypedDict(
    "ClientUpdateTriggerResponseTriggerPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientUpdateTriggerResponseTriggerPredicateConditionsTypeDef],
    },
    total=False,
)

ClientUpdateTriggerResponseTriggerTypeDef = TypedDict(
    "ClientUpdateTriggerResponseTriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientUpdateTriggerResponseTriggerActionsTypeDef],
        "Predicate": ClientUpdateTriggerResponseTriggerPredicateTypeDef,
    },
    total=False,
)

ClientUpdateTriggerResponseTypeDef = TypedDict(
    "ClientUpdateTriggerResponseTypeDef",
    {"Trigger": ClientUpdateTriggerResponseTriggerTypeDef},
    total=False,
)

ClientUpdateTriggerTriggerUpdateActionsNotificationPropertyTypeDef = TypedDict(
    "ClientUpdateTriggerTriggerUpdateActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

ClientUpdateTriggerTriggerUpdateActionsTypeDef = TypedDict(
    "ClientUpdateTriggerTriggerUpdateActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": ClientUpdateTriggerTriggerUpdateActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

ClientUpdateTriggerTriggerUpdatePredicateConditionsTypeDef = TypedDict(
    "ClientUpdateTriggerTriggerUpdatePredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

ClientUpdateTriggerTriggerUpdatePredicateTypeDef = TypedDict(
    "ClientUpdateTriggerTriggerUpdatePredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[ClientUpdateTriggerTriggerUpdatePredicateConditionsTypeDef],
    },
    total=False,
)

ClientUpdateTriggerTriggerUpdateTypeDef = TypedDict(
    "ClientUpdateTriggerTriggerUpdateTypeDef",
    {
        "Name": str,
        "Description": str,
        "Schedule": str,
        "Actions": List[ClientUpdateTriggerTriggerUpdateActionsTypeDef],
        "Predicate": ClientUpdateTriggerTriggerUpdatePredicateTypeDef,
    },
    total=False,
)

ClientUpdateUserDefinedFunctionFunctionInputResourceUrisTypeDef = TypedDict(
    "ClientUpdateUserDefinedFunctionFunctionInputResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)

ClientUpdateUserDefinedFunctionFunctionInputTypeDef = TypedDict(
    "ClientUpdateUserDefinedFunctionFunctionInputTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "ResourceUris": List[ClientUpdateUserDefinedFunctionFunctionInputResourceUrisTypeDef],
    },
    total=False,
)

ClientUpdateWorkflowResponseTypeDef = TypedDict(
    "ClientUpdateWorkflowResponseTypeDef", {"Name": str}, total=False
)

GetClassifiersPaginatePaginationConfigTypeDef = TypedDict(
    "GetClassifiersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetClassifiersPaginateResponseClassifiersCsvClassifierTypeDef = TypedDict(
    "GetClassifiersPaginateResponseClassifiersCsvClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)

GetClassifiersPaginateResponseClassifiersGrokClassifierTypeDef = TypedDict(
    "GetClassifiersPaginateResponseClassifiersGrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "GrokPattern": str,
        "CustomPatterns": str,
    },
    total=False,
)

GetClassifiersPaginateResponseClassifiersJsonClassifierTypeDef = TypedDict(
    "GetClassifiersPaginateResponseClassifiersJsonClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "JsonPath": str,
    },
    total=False,
)

GetClassifiersPaginateResponseClassifiersXMLClassifierTypeDef = TypedDict(
    "GetClassifiersPaginateResponseClassifiersXMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "RowTag": str,
    },
    total=False,
)

GetClassifiersPaginateResponseClassifiersTypeDef = TypedDict(
    "GetClassifiersPaginateResponseClassifiersTypeDef",
    {
        "GrokClassifier": GetClassifiersPaginateResponseClassifiersGrokClassifierTypeDef,
        "XMLClassifier": GetClassifiersPaginateResponseClassifiersXMLClassifierTypeDef,
        "JsonClassifier": GetClassifiersPaginateResponseClassifiersJsonClassifierTypeDef,
        "CsvClassifier": GetClassifiersPaginateResponseClassifiersCsvClassifierTypeDef,
    },
    total=False,
)

GetClassifiersPaginateResponseTypeDef = TypedDict(
    "GetClassifiersPaginateResponseTypeDef",
    {"Classifiers": List[GetClassifiersPaginateResponseClassifiersTypeDef]},
    total=False,
)

GetConnectionsPaginateFilterTypeDef = TypedDict(
    "GetConnectionsPaginateFilterTypeDef",
    {"MatchCriteria": List[str], "ConnectionType": Literal["JDBC", "SFTP"]},
    total=False,
)

GetConnectionsPaginatePaginationConfigTypeDef = TypedDict(
    "GetConnectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetConnectionsPaginateResponseConnectionListPhysicalConnectionRequirementsTypeDef = TypedDict(
    "GetConnectionsPaginateResponseConnectionListPhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)

GetConnectionsPaginateResponseConnectionListTypeDef = TypedDict(
    "GetConnectionsPaginateResponseConnectionListTypeDef",
    {
        "Name": str,
        "Description": str,
        "ConnectionType": Literal["JDBC", "SFTP"],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[str, str],
        "PhysicalConnectionRequirements": GetConnectionsPaginateResponseConnectionListPhysicalConnectionRequirementsTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
    total=False,
)

GetConnectionsPaginateResponseTypeDef = TypedDict(
    "GetConnectionsPaginateResponseTypeDef",
    {"ConnectionList": List[GetConnectionsPaginateResponseConnectionListTypeDef]},
    total=False,
)

GetCrawlerMetricsPaginatePaginationConfigTypeDef = TypedDict(
    "GetCrawlerMetricsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetCrawlerMetricsPaginateResponseCrawlerMetricsListTypeDef = TypedDict(
    "GetCrawlerMetricsPaginateResponseCrawlerMetricsListTypeDef",
    {
        "CrawlerName": str,
        "TimeLeftSeconds": float,
        "StillEstimating": bool,
        "LastRuntimeSeconds": float,
        "MedianRuntimeSeconds": float,
        "TablesCreated": int,
        "TablesUpdated": int,
        "TablesDeleted": int,
    },
    total=False,
)

GetCrawlerMetricsPaginateResponseTypeDef = TypedDict(
    "GetCrawlerMetricsPaginateResponseTypeDef",
    {"CrawlerMetricsList": List[GetCrawlerMetricsPaginateResponseCrawlerMetricsListTypeDef]},
    total=False,
)

GetCrawlersPaginatePaginationConfigTypeDef = TypedDict(
    "GetCrawlersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetCrawlersPaginateResponseCrawlersLastCrawlTypeDef = TypedDict(
    "GetCrawlersPaginateResponseCrawlersLastCrawlTypeDef",
    {
        "Status": Literal["SUCCEEDED", "CANCELLED", "FAILED"],
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)

GetCrawlersPaginateResponseCrawlersScheduleTypeDef = TypedDict(
    "GetCrawlersPaginateResponseCrawlersScheduleTypeDef",
    {"ScheduleExpression": str, "State": Literal["SCHEDULED", "NOT_SCHEDULED", "TRANSITIONING"]},
    total=False,
)

GetCrawlersPaginateResponseCrawlersSchemaChangePolicyTypeDef = TypedDict(
    "GetCrawlersPaginateResponseCrawlersSchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)

GetCrawlersPaginateResponseCrawlersTargetsCatalogTargetsTypeDef = TypedDict(
    "GetCrawlersPaginateResponseCrawlersTargetsCatalogTargetsTypeDef",
    {"DatabaseName": str, "Tables": List[str]},
    total=False,
)

GetCrawlersPaginateResponseCrawlersTargetsDynamoDBTargetsTypeDef = TypedDict(
    "GetCrawlersPaginateResponseCrawlersTargetsDynamoDBTargetsTypeDef", {"Path": str}, total=False
)

GetCrawlersPaginateResponseCrawlersTargetsJdbcTargetsTypeDef = TypedDict(
    "GetCrawlersPaginateResponseCrawlersTargetsJdbcTargetsTypeDef",
    {"ConnectionName": str, "Path": str, "Exclusions": List[str]},
    total=False,
)

GetCrawlersPaginateResponseCrawlersTargetsS3TargetsTypeDef = TypedDict(
    "GetCrawlersPaginateResponseCrawlersTargetsS3TargetsTypeDef",
    {"Path": str, "Exclusions": List[str]},
    total=False,
)

GetCrawlersPaginateResponseCrawlersTargetsTypeDef = TypedDict(
    "GetCrawlersPaginateResponseCrawlersTargetsTypeDef",
    {
        "S3Targets": List[GetCrawlersPaginateResponseCrawlersTargetsS3TargetsTypeDef],
        "JdbcTargets": List[GetCrawlersPaginateResponseCrawlersTargetsJdbcTargetsTypeDef],
        "DynamoDBTargets": List[GetCrawlersPaginateResponseCrawlersTargetsDynamoDBTargetsTypeDef],
        "CatalogTargets": List[GetCrawlersPaginateResponseCrawlersTargetsCatalogTargetsTypeDef],
    },
    total=False,
)

GetCrawlersPaginateResponseCrawlersTypeDef = TypedDict(
    "GetCrawlersPaginateResponseCrawlersTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": GetCrawlersPaginateResponseCrawlersTargetsTypeDef,
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "SchemaChangePolicy": GetCrawlersPaginateResponseCrawlersSchemaChangePolicyTypeDef,
        "State": Literal["READY", "RUNNING", "STOPPING"],
        "TablePrefix": str,
        "Schedule": GetCrawlersPaginateResponseCrawlersScheduleTypeDef,
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": GetCrawlersPaginateResponseCrawlersLastCrawlTypeDef,
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)

GetCrawlersPaginateResponseTypeDef = TypedDict(
    "GetCrawlersPaginateResponseTypeDef",
    {"Crawlers": List[GetCrawlersPaginateResponseCrawlersTypeDef]},
    total=False,
)

GetDatabasesPaginatePaginationConfigTypeDef = TypedDict(
    "GetDatabasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsTypeDef = TypedDict(
    "GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

GetDatabasesPaginateResponseDatabaseListTypeDef = TypedDict(
    "GetDatabasesPaginateResponseDatabaseListTypeDef",
    {
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTime": datetime,
        "CreateTableDefaultPermissions": List[
            GetDatabasesPaginateResponseDatabaseListCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)

GetDatabasesPaginateResponseTypeDef = TypedDict(
    "GetDatabasesPaginateResponseTypeDef",
    {"DatabaseList": List[GetDatabasesPaginateResponseDatabaseListTypeDef]},
    total=False,
)

GetDevEndpointsPaginatePaginationConfigTypeDef = TypedDict(
    "GetDevEndpointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetDevEndpointsPaginateResponseDevEndpointsTypeDef = TypedDict(
    "GetDevEndpointsPaginateResponseDevEndpointsTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)

GetDevEndpointsPaginateResponseTypeDef = TypedDict(
    "GetDevEndpointsPaginateResponseTypeDef",
    {"DevEndpoints": List[GetDevEndpointsPaginateResponseDevEndpointsTypeDef]},
    total=False,
)

GetJobRunsPaginatePaginationConfigTypeDef = TypedDict(
    "GetJobRunsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetJobRunsPaginateResponseJobRunsNotificationPropertyTypeDef = TypedDict(
    "GetJobRunsPaginateResponseJobRunsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

GetJobRunsPaginateResponseJobRunsPredecessorRunsTypeDef = TypedDict(
    "GetJobRunsPaginateResponseJobRunsPredecessorRunsTypeDef",
    {"JobName": str, "RunId": str},
    total=False,
)

GetJobRunsPaginateResponseJobRunsTypeDef = TypedDict(
    "GetJobRunsPaginateResponseJobRunsTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List[GetJobRunsPaginateResponseJobRunsPredecessorRunsTypeDef],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": GetJobRunsPaginateResponseJobRunsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

GetJobRunsPaginateResponseTypeDef = TypedDict(
    "GetJobRunsPaginateResponseTypeDef",
    {"JobRuns": List[GetJobRunsPaginateResponseJobRunsTypeDef]},
    total=False,
)

GetJobsPaginatePaginationConfigTypeDef = TypedDict(
    "GetJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetJobsPaginateResponseJobsCommandTypeDef = TypedDict(
    "GetJobsPaginateResponseJobsCommandTypeDef",
    {"Name": str, "ScriptLocation": str, "PythonVersion": str},
    total=False,
)

GetJobsPaginateResponseJobsConnectionsTypeDef = TypedDict(
    "GetJobsPaginateResponseJobsConnectionsTypeDef", {"Connections": List[str]}, total=False
)

GetJobsPaginateResponseJobsExecutionPropertyTypeDef = TypedDict(
    "GetJobsPaginateResponseJobsExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)

GetJobsPaginateResponseJobsNotificationPropertyTypeDef = TypedDict(
    "GetJobsPaginateResponseJobsNotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)

GetJobsPaginateResponseJobsTypeDef = TypedDict(
    "GetJobsPaginateResponseJobsTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": GetJobsPaginateResponseJobsExecutionPropertyTypeDef,
        "Command": GetJobsPaginateResponseJobsCommandTypeDef,
        "DefaultArguments": Dict[str, str],
        "Connections": GetJobsPaginateResponseJobsConnectionsTypeDef,
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": GetJobsPaginateResponseJobsNotificationPropertyTypeDef,
        "GlueVersion": str,
    },
    total=False,
)

GetJobsPaginateResponseTypeDef = TypedDict(
    "GetJobsPaginateResponseTypeDef",
    {"Jobs": List[GetJobsPaginateResponseJobsTypeDef]},
    total=False,
)

GetPartitionsPaginatePaginationConfigTypeDef = TypedDict(
    "GetPartitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetPartitionsPaginateResponsePartitionsStorageDescriptorColumnsTypeDef = TypedDict(
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

GetPartitionsPaginateResponsePartitionsStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

GetPartitionsPaginateResponsePartitionsStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

GetPartitionsPaginateResponsePartitionsStorageDescriptorSortColumnsTypeDef = TypedDict(
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

GetPartitionsPaginateResponsePartitionsStorageDescriptorTypeDef = TypedDict(
    "GetPartitionsPaginateResponsePartitionsStorageDescriptorTypeDef",
    {
        "Columns": List[GetPartitionsPaginateResponsePartitionsStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": GetPartitionsPaginateResponsePartitionsStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            GetPartitionsPaginateResponsePartitionsStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": GetPartitionsPaginateResponsePartitionsStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

GetPartitionsPaginateResponsePartitionsTypeDef = TypedDict(
    "GetPartitionsPaginateResponsePartitionsTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": GetPartitionsPaginateResponsePartitionsStorageDescriptorTypeDef,
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)

GetPartitionsPaginateResponseTypeDef = TypedDict(
    "GetPartitionsPaginateResponseTypeDef",
    {"Partitions": List[GetPartitionsPaginateResponsePartitionsTypeDef]},
    total=False,
)

_RequiredGetPartitionsPaginateSegmentTypeDef = TypedDict(
    "_RequiredGetPartitionsPaginateSegmentTypeDef", {"SegmentNumber": int}
)
_OptionalGetPartitionsPaginateSegmentTypeDef = TypedDict(
    "_OptionalGetPartitionsPaginateSegmentTypeDef", {"TotalSegments": int}, total=False
)


class GetPartitionsPaginateSegmentTypeDef(
    _RequiredGetPartitionsPaginateSegmentTypeDef, _OptionalGetPartitionsPaginateSegmentTypeDef
):
    pass


GetSecurityConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "GetSecurityConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef = TypedDict(
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef",
    {"CloudWatchEncryptionMode": Literal["DISABLED", "SSE-KMS"], "KmsKeyArn": str},
    total=False,
)

GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef = TypedDict(
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef",
    {"JobBookmarksEncryptionMode": Literal["DISABLED", "CSE-KMS"], "KmsKeyArn": str},
    total=False,
)

GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef = TypedDict(
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef",
    {"S3EncryptionMode": Literal["DISABLED", "SSE-KMS", "SSE-S3"], "KmsKeyArn": str},
    total=False,
)

GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationTypeDef = TypedDict(
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationTypeDef",
    {
        "S3Encryption": List[
            GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationS3EncryptionTypeDef
        ],
        "CloudWatchEncryption": GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationCloudWatchEncryptionTypeDef,
        "JobBookmarksEncryption": GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationJobBookmarksEncryptionTypeDef,
    },
    total=False,
)

GetSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef = TypedDict(
    "GetSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef",
    {
        "Name": str,
        "CreatedTimeStamp": datetime,
        "EncryptionConfiguration": GetSecurityConfigurationsPaginateResponseSecurityConfigurationsEncryptionConfigurationTypeDef,
    },
    total=False,
)

GetSecurityConfigurationsPaginateResponseTypeDef = TypedDict(
    "GetSecurityConfigurationsPaginateResponseTypeDef",
    {
        "SecurityConfigurations": List[
            GetSecurityConfigurationsPaginateResponseSecurityConfigurationsTypeDef
        ]
    },
    total=False,
)

GetTableVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "GetTableVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetTableVersionsPaginateResponseTableVersionsTablePartitionKeysTypeDef = TypedDict(
    "GetTableVersionsPaginateResponseTableVersionsTablePartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorColumnsTypeDef = TypedDict(
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef = TypedDict(
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorTypeDef = TypedDict(
    "GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorTypeDef",
    {
        "Columns": List[
            GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorColumnsTypeDef
        ],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[
            GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSortColumnsTypeDef
        ],
        "Parameters": Dict[str, str],
        "SkewedInfo": GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

GetTableVersionsPaginateResponseTableVersionsTableTypeDef = TypedDict(
    "GetTableVersionsPaginateResponseTableVersionsTableTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": GetTableVersionsPaginateResponseTableVersionsTableStorageDescriptorTypeDef,
        "PartitionKeys": List[
            GetTableVersionsPaginateResponseTableVersionsTablePartitionKeysTypeDef
        ],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)

GetTableVersionsPaginateResponseTableVersionsTypeDef = TypedDict(
    "GetTableVersionsPaginateResponseTableVersionsTypeDef",
    {"Table": GetTableVersionsPaginateResponseTableVersionsTableTypeDef, "VersionId": str},
    total=False,
)

GetTableVersionsPaginateResponseTypeDef = TypedDict(
    "GetTableVersionsPaginateResponseTypeDef",
    {"TableVersions": List[GetTableVersionsPaginateResponseTableVersionsTypeDef]},
    total=False,
)

GetTablesPaginatePaginationConfigTypeDef = TypedDict(
    "GetTablesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetTablesPaginateResponseTableListPartitionKeysTypeDef = TypedDict(
    "GetTablesPaginateResponseTableListPartitionKeysTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

GetTablesPaginateResponseTableListStorageDescriptorColumnsTypeDef = TypedDict(
    "GetTablesPaginateResponseTableListStorageDescriptorColumnsTypeDef",
    {"Name": str, "Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)

GetTablesPaginateResponseTableListStorageDescriptorSerdeInfoTypeDef = TypedDict(
    "GetTablesPaginateResponseTableListStorageDescriptorSerdeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

GetTablesPaginateResponseTableListStorageDescriptorSkewedInfoTypeDef = TypedDict(
    "GetTablesPaginateResponseTableListStorageDescriptorSkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

GetTablesPaginateResponseTableListStorageDescriptorSortColumnsTypeDef = TypedDict(
    "GetTablesPaginateResponseTableListStorageDescriptorSortColumnsTypeDef",
    {"Column": str, "SortOrder": int},
    total=False,
)

GetTablesPaginateResponseTableListStorageDescriptorTypeDef = TypedDict(
    "GetTablesPaginateResponseTableListStorageDescriptorTypeDef",
    {
        "Columns": List[GetTablesPaginateResponseTableListStorageDescriptorColumnsTypeDef],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": GetTablesPaginateResponseTableListStorageDescriptorSerdeInfoTypeDef,
        "BucketColumns": List[str],
        "SortColumns": List[GetTablesPaginateResponseTableListStorageDescriptorSortColumnsTypeDef],
        "Parameters": Dict[str, str],
        "SkewedInfo": GetTablesPaginateResponseTableListStorageDescriptorSkewedInfoTypeDef,
        "StoredAsSubDirectories": bool,
    },
    total=False,
)

GetTablesPaginateResponseTableListTypeDef = TypedDict(
    "GetTablesPaginateResponseTableListTypeDef",
    {
        "Name": str,
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": GetTablesPaginateResponseTableListStorageDescriptorTypeDef,
        "PartitionKeys": List[GetTablesPaginateResponseTableListPartitionKeysTypeDef],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)

GetTablesPaginateResponseTypeDef = TypedDict(
    "GetTablesPaginateResponseTypeDef",
    {"TableList": List[GetTablesPaginateResponseTableListTypeDef]},
    total=False,
)

GetTriggersPaginatePaginationConfigTypeDef = TypedDict(
    "GetTriggersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetTriggersPaginateResponseTriggersActionsNotificationPropertyTypeDef = TypedDict(
    "GetTriggersPaginateResponseTriggersActionsNotificationPropertyTypeDef",
    {"NotifyDelayAfter": int},
    total=False,
)

GetTriggersPaginateResponseTriggersActionsTypeDef = TypedDict(
    "GetTriggersPaginateResponseTriggersActionsTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": GetTriggersPaginateResponseTriggersActionsNotificationPropertyTypeDef,
        "CrawlerName": str,
    },
    total=False,
)

GetTriggersPaginateResponseTriggersPredicateConditionsTypeDef = TypedDict(
    "GetTriggersPaginateResponseTriggersPredicateConditionsTypeDef",
    {
        "LogicalOperator": str,
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
    },
    total=False,
)

GetTriggersPaginateResponseTriggersPredicateTypeDef = TypedDict(
    "GetTriggersPaginateResponseTriggersPredicateTypeDef",
    {
        "Logical": Literal["AND", "ANY"],
        "Conditions": List[GetTriggersPaginateResponseTriggersPredicateConditionsTypeDef],
    },
    total=False,
)

GetTriggersPaginateResponseTriggersTypeDef = TypedDict(
    "GetTriggersPaginateResponseTriggersTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List[GetTriggersPaginateResponseTriggersActionsTypeDef],
        "Predicate": GetTriggersPaginateResponseTriggersPredicateTypeDef,
    },
    total=False,
)

GetTriggersPaginateResponseTypeDef = TypedDict(
    "GetTriggersPaginateResponseTypeDef",
    {"Triggers": List[GetTriggersPaginateResponseTriggersTypeDef]},
    total=False,
)

GetUserDefinedFunctionsPaginatePaginationConfigTypeDef = TypedDict(
    "GetUserDefinedFunctionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsResourceUrisTypeDef = TypedDict(
    "GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsResourceUrisTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)

GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsTypeDef = TypedDict(
    "GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "CreateTime": datetime,
        "ResourceUris": List[
            GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsResourceUrisTypeDef
        ],
    },
    total=False,
)

GetUserDefinedFunctionsPaginateResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionsPaginateResponseTypeDef",
    {
        "UserDefinedFunctions": List[
            GetUserDefinedFunctionsPaginateResponseUserDefinedFunctionsTypeDef
        ]
    },
    total=False,
)
