"Main interface for cloudformation service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ChangeSetCreateCompleteWaitWaiterConfigTypeDef = TypedDict(
    "ChangeSetCreateCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)

ClientCreateChangeSetParametersTypeDef = TypedDict(
    "ClientCreateChangeSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

_RequiredClientCreateChangeSetResourcesToImportTypeDef = TypedDict(
    "_RequiredClientCreateChangeSetResourcesToImportTypeDef", {"ResourceType": str}
)
_OptionalClientCreateChangeSetResourcesToImportTypeDef = TypedDict(
    "_OptionalClientCreateChangeSetResourcesToImportTypeDef",
    {"LogicalResourceId": str, "ResourceIdentifier": Dict[str, str]},
    total=False,
)


class ClientCreateChangeSetResourcesToImportTypeDef(
    _RequiredClientCreateChangeSetResourcesToImportTypeDef,
    _OptionalClientCreateChangeSetResourcesToImportTypeDef,
):
    pass


ClientCreateChangeSetResponseTypeDef = TypedDict(
    "ClientCreateChangeSetResponseTypeDef", {"Id": str, "StackId": str}, total=False
)

_RequiredClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef,
):
    pass


ClientCreateChangeSetRollbackConfigurationTypeDef = TypedDict(
    "ClientCreateChangeSetRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

_RequiredClientCreateChangeSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateChangeSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateChangeSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateChangeSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateChangeSetTagsTypeDef(
    _RequiredClientCreateChangeSetTagsTypeDef, _OptionalClientCreateChangeSetTagsTypeDef
):
    pass


ClientCreateStackInstancesOperationPreferencesTypeDef = TypedDict(
    "ClientCreateStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientCreateStackInstancesParameterOverridesTypeDef = TypedDict(
    "ClientCreateStackInstancesParameterOverridesTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientCreateStackInstancesResponseTypeDef = TypedDict(
    "ClientCreateStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)

ClientCreateStackParametersTypeDef = TypedDict(
    "ClientCreateStackParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientCreateStackResponseTypeDef = TypedDict(
    "ClientCreateStackResponseTypeDef", {"StackId": str}, total=False
)

_RequiredClientCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredClientCreateStackRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalClientCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalClientCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredClientCreateStackRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalClientCreateStackRollbackConfigurationRollbackTriggersTypeDef,
):
    pass


ClientCreateStackRollbackConfigurationTypeDef = TypedDict(
    "ClientCreateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

ClientCreateStackSetParametersTypeDef = TypedDict(
    "ClientCreateStackSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientCreateStackSetResponseTypeDef = TypedDict(
    "ClientCreateStackSetResponseTypeDef", {"StackSetId": str}, total=False
)

_RequiredClientCreateStackSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateStackSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateStackSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateStackSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateStackSetTagsTypeDef(
    _RequiredClientCreateStackSetTagsTypeDef, _OptionalClientCreateStackSetTagsTypeDef
):
    pass


_RequiredClientCreateStackTagsTypeDef = TypedDict(
    "_RequiredClientCreateStackTagsTypeDef", {"Key": str}
)
_OptionalClientCreateStackTagsTypeDef = TypedDict(
    "_OptionalClientCreateStackTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateStackTagsTypeDef(
    _RequiredClientCreateStackTagsTypeDef, _OptionalClientCreateStackTagsTypeDef
):
    pass


ClientDeleteStackInstancesOperationPreferencesTypeDef = TypedDict(
    "ClientDeleteStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientDeleteStackInstancesResponseTypeDef = TypedDict(
    "ClientDeleteStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)

ClientDescribeAccountLimitsResponseAccountLimitsTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseAccountLimitsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)

ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseTypeDef",
    {
        "AccountLimits": List[ClientDescribeAccountLimitsResponseAccountLimitsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef",
    {
        "Attribute": Literal[
            "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
        ],
        "Name": str,
        "RequiresRecreation": Literal["Never", "Conditionally", "Always"],
    },
    total=False,
)

ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef",
    {
        "Target": ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef,
        "Evaluation": Literal["Static", "Dynamic"],
        "ChangeSource": Literal[
            "ResourceReference",
            "ParameterReference",
            "ResourceAttribute",
            "DirectModification",
            "Automatic",
        ],
        "CausingEntity": str,
    },
    total=False,
)

ClientDescribeChangeSetResponseChangesResourceChangeTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangesResourceChangeTypeDef",
    {
        "Action": Literal["Add", "Modify", "Remove", "Import"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["True", "False", "Conditional"],
        "Scope": List[
            Literal[
                "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
            ]
        ],
        "Details": List[ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef],
    },
    total=False,
)

ClientDescribeChangeSetResponseChangesTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseChangesTypeDef",
    {"Type": str, "ResourceChange": ClientDescribeChangeSetResponseChangesResourceChangeTypeDef},
    total=False,
)

ClientDescribeChangeSetResponseParametersTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)

ClientDescribeChangeSetResponseRollbackConfigurationTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

ClientDescribeChangeSetResponseTagsTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeChangeSetResponseTypeDef = TypedDict(
    "ClientDescribeChangeSetResponseTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List[ClientDescribeChangeSetResponseParametersTypeDef],
        "CreationTime": datetime,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": ClientDescribeChangeSetResponseRollbackConfigurationTypeDef,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List[ClientDescribeChangeSetResponseTagsTypeDef],
        "Changes": List[ClientDescribeChangeSetResponseChangesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeStackDriftDetectionStatusResponseTypeDef = TypedDict(
    "ClientDescribeStackDriftDetectionStatusResponseTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "DetectionStatus": Literal[
            "DETECTION_IN_PROGRESS", "DETECTION_FAILED", "DETECTION_COMPLETE"
        ],
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
        "Timestamp": datetime,
    },
    total=False,
)

ClientDescribeStackEventsResponseStackEventsTypeDef = TypedDict(
    "ClientDescribeStackEventsResponseStackEventsTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)

ClientDescribeStackEventsResponseTypeDef = TypedDict(
    "ClientDescribeStackEventsResponseTypeDef",
    {"StackEvents": List[ClientDescribeStackEventsResponseStackEventsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef = TypedDict(
    "ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientDescribeStackInstanceResponseStackInstanceTypeDef = TypedDict(
    "ClientDescribeStackInstanceResponseStackInstanceTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "ParameterOverrides": List[
            ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef
        ],
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ClientDescribeStackInstanceResponseTypeDef = TypedDict(
    "ClientDescribeStackInstanceResponseTypeDef",
    {"StackInstance": ClientDescribeStackInstanceResponseStackInstanceTypeDef},
    total=False,
)

ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef = TypedDict(
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef = TypedDict(
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": Literal["ADD", "REMOVE", "NOT_EQUAL"],
    },
    total=False,
)

ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef = TypedDict(
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef
        ],
        "ResourceType": str,
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef
        ],
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "Timestamp": datetime,
    },
    total=False,
)

ClientDescribeStackResourceDriftsResponseTypeDef = TypedDict(
    "ClientDescribeStackResourceDriftsResponseTypeDef",
    {
        "StackResourceDrifts": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef = TypedDict(
    "ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientDescribeStackResourceResponseStackResourceDetailTypeDef = TypedDict(
    "ClientDescribeStackResourceResponseStackResourceDetailTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "Description": str,
        "Metadata": str,
        "DriftInformation": ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef,
    },
    total=False,
)

ClientDescribeStackResourceResponseTypeDef = TypedDict(
    "ClientDescribeStackResourceResponseTypeDef",
    {"StackResourceDetail": ClientDescribeStackResourceResponseStackResourceDetailTypeDef},
    total=False,
)

ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef = TypedDict(
    "ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientDescribeStackResourcesResponseStackResourcesTypeDef = TypedDict(
    "ClientDescribeStackResourcesResponseStackResourcesTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "Description": str,
        "DriftInformation": ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef,
    },
    total=False,
)

ClientDescribeStackResourcesResponseTypeDef = TypedDict(
    "ClientDescribeStackResourcesResponseTypeDef",
    {"StackResources": List[ClientDescribeStackResourcesResponseStackResourcesTypeDef]},
    total=False,
)

ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef = TypedDict(
    "ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef = TypedDict(
    "ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"],
        "DriftDetectionStatus": Literal[
            "COMPLETED", "FAILED", "PARTIAL_SUCCESS", "IN_PROGRESS", "STOPPED"
        ],
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)

ClientDescribeStackSetOperationResponseStackSetOperationTypeDef = TypedDict(
    "ClientDescribeStackSetOperationResponseStackSetOperationTypeDef",
    {
        "OperationId": str,
        "StackSetId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED"],
        "OperationPreferences": ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef,
        "RetainStacks": bool,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
        "StackSetDriftDetectionDetails": ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef,
    },
    total=False,
)

ClientDescribeStackSetOperationResponseTypeDef = TypedDict(
    "ClientDescribeStackSetOperationResponseTypeDef",
    {"StackSetOperation": ClientDescribeStackSetOperationResponseStackSetOperationTypeDef},
    total=False,
)

ClientDescribeStackSetResponseStackSetParametersTypeDef = TypedDict(
    "ClientDescribeStackSetResponseStackSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef = TypedDict(
    "ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"],
        "DriftDetectionStatus": Literal[
            "COMPLETED", "FAILED", "PARTIAL_SUCCESS", "IN_PROGRESS", "STOPPED"
        ],
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)

ClientDescribeStackSetResponseStackSetTagsTypeDef = TypedDict(
    "ClientDescribeStackSetResponseStackSetTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeStackSetResponseStackSetTypeDef = TypedDict(
    "ClientDescribeStackSetResponseStackSetTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "TemplateBody": str,
        "Parameters": List[ClientDescribeStackSetResponseStackSetParametersTypeDef],
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List[ClientDescribeStackSetResponseStackSetTagsTypeDef],
        "StackSetARN": str,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "StackSetDriftDetectionDetails": ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef,
    },
    total=False,
)

ClientDescribeStackSetResponseTypeDef = TypedDict(
    "ClientDescribeStackSetResponseTypeDef",
    {"StackSet": ClientDescribeStackSetResponseStackSetTypeDef},
    total=False,
)

ClientDescribeStacksResponseStacksDriftInformationTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientDescribeStacksResponseStacksOutputsTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str, "ExportName": str},
    total=False,
)

ClientDescribeStacksResponseStacksParametersTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)

ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

ClientDescribeStacksResponseStacksTagsTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List[ClientDescribeStacksResponseStacksParametersTypeDef],
        "CreationTime": datetime,
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Outputs": List[ClientDescribeStacksResponseStacksOutputsTypeDef],
        "RoleARN": str,
        "Tags": List[ClientDescribeStacksResponseStacksTagsTypeDef],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ClientDescribeStacksResponseStacksDriftInformationTypeDef,
    },
    total=False,
)

ClientDescribeStacksResponseTypeDef = TypedDict(
    "ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeTypeRegistrationResponseTypeDef = TypedDict(
    "ClientDescribeTypeRegistrationResponseTypeDef",
    {
        "ProgressStatus": Literal["COMPLETE", "IN_PROGRESS", "FAILED"],
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
    },
    total=False,
)

ClientDescribeTypeResponseLoggingConfigTypeDef = TypedDict(
    "ClientDescribeTypeResponseLoggingConfigTypeDef",
    {"LogRoleArn": str, "LogGroupName": str},
    total=False,
)

ClientDescribeTypeResponseTypeDef = TypedDict(
    "ClientDescribeTypeResponseTypeDef",
    {
        "Arn": str,
        "Type": str,
        "TypeName": str,
        "DefaultVersionId": str,
        "Description": str,
        "Schema": str,
        "ProvisioningType": Literal["NON_PROVISIONABLE", "IMMUTABLE", "FULLY_MUTABLE"],
        "DeprecatedStatus": Literal["LIVE", "DEPRECATED"],
        "LoggingConfig": ClientDescribeTypeResponseLoggingConfigTypeDef,
        "ExecutionRoleArn": str,
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
    },
    total=False,
)

ClientDetectStackDriftResponseTypeDef = TypedDict(
    "ClientDetectStackDriftResponseTypeDef", {"StackDriftDetectionId": str}, total=False
)

ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef = TypedDict(
    "ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef = TypedDict(
    "ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": Literal["ADD", "REMOVE", "NOT_EQUAL"],
    },
    total=False,
)

ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef = TypedDict(
    "ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List[
            ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef
        ],
        "ResourceType": str,
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List[
            ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef
        ],
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "Timestamp": datetime,
    },
    total=False,
)

ClientDetectStackResourceDriftResponseTypeDef = TypedDict(
    "ClientDetectStackResourceDriftResponseTypeDef",
    {"StackResourceDrift": ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef},
    total=False,
)

ClientDetectStackSetDriftOperationPreferencesTypeDef = TypedDict(
    "ClientDetectStackSetDriftOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientDetectStackSetDriftResponseTypeDef = TypedDict(
    "ClientDetectStackSetDriftResponseTypeDef", {"OperationId": str}, total=False
)

ClientEstimateTemplateCostParametersTypeDef = TypedDict(
    "ClientEstimateTemplateCostParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientEstimateTemplateCostResponseTypeDef = TypedDict(
    "ClientEstimateTemplateCostResponseTypeDef", {"Url": str}, total=False
)

ClientGetStackPolicyResponseTypeDef = TypedDict(
    "ClientGetStackPolicyResponseTypeDef", {"StackPolicyBody": str}, total=False
)

ClientGetTemplateResponseTypeDef = TypedDict(
    "ClientGetTemplateResponseTypeDef",
    {"TemplateBody": Dict[str, Any], "StagesAvailable": List[Literal["Original", "Processed"]]},
    total=False,
)

ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef = TypedDict(
    "ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef",
    {"AllowedValues": List[str]},
    total=False,
)

ClientGetTemplateSummaryResponseParametersTypeDef = TypedDict(
    "ClientGetTemplateSummaryResponseParametersTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "NoEcho": bool,
        "Description": str,
        "ParameterConstraints": ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef,
    },
    total=False,
)

ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef = TypedDict(
    "ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef",
    {"ResourceType": str, "LogicalResourceIds": List[str], "ResourceIdentifiers": List[str]},
    total=False,
)

ClientGetTemplateSummaryResponseTypeDef = TypedDict(
    "ClientGetTemplateSummaryResponseTypeDef",
    {
        "Parameters": List[ClientGetTemplateSummaryResponseParametersTypeDef],
        "Description": str,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List[
            ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef
        ],
    },
    total=False,
)

ClientListChangeSetsResponseSummariesTypeDef = TypedDict(
    "ClientListChangeSetsResponseSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
    },
    total=False,
)

ClientListChangeSetsResponseTypeDef = TypedDict(
    "ClientListChangeSetsResponseTypeDef",
    {"Summaries": List[ClientListChangeSetsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListExportsResponseExportsTypeDef = TypedDict(
    "ClientListExportsResponseExportsTypeDef",
    {"ExportingStackId": str, "Name": str, "Value": str},
    total=False,
)

ClientListExportsResponseTypeDef = TypedDict(
    "ClientListExportsResponseTypeDef",
    {"Exports": List[ClientListExportsResponseExportsTypeDef], "NextToken": str},
    total=False,
)

ClientListImportsResponseTypeDef = TypedDict(
    "ClientListImportsResponseTypeDef", {"Imports": List[str], "NextToken": str}, total=False
)

ClientListStackInstancesResponseSummariesTypeDef = TypedDict(
    "ClientListStackInstancesResponseSummariesTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ClientListStackInstancesResponseTypeDef = TypedDict(
    "ClientListStackInstancesResponseTypeDef",
    {"Summaries": List[ClientListStackInstancesResponseSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef = TypedDict(
    "ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientListStackResourcesResponseStackResourceSummariesTypeDef = TypedDict(
    "ClientListStackResourcesResponseStackResourceSummariesTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "DriftInformation": ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef,
    },
    total=False,
)

ClientListStackResourcesResponseTypeDef = TypedDict(
    "ClientListStackResourcesResponseTypeDef",
    {
        "StackResourceSummaries": List[
            ClientListStackResourcesResponseStackResourceSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef = TypedDict(
    "ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef",
    {"Status": Literal["SUCCEEDED", "FAILED", "SKIPPED"], "StatusReason": str},
    total=False,
)

ClientListStackSetOperationResultsResponseSummariesTypeDef = TypedDict(
    "ClientListStackSetOperationResultsResponseSummariesTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StatusReason": str,
        "AccountGateResult": ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef,
    },
    total=False,
)

ClientListStackSetOperationResultsResponseTypeDef = TypedDict(
    "ClientListStackSetOperationResultsResponseTypeDef",
    {
        "Summaries": List[ClientListStackSetOperationResultsResponseSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListStackSetOperationsResponseSummariesTypeDef = TypedDict(
    "ClientListStackSetOperationsResponseSummariesTypeDef",
    {
        "OperationId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED"],
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)

ClientListStackSetOperationsResponseTypeDef = TypedDict(
    "ClientListStackSetOperationsResponseTypeDef",
    {"Summaries": List[ClientListStackSetOperationsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListStackSetsResponseSummariesTypeDef = TypedDict(
    "ClientListStackSetsResponseSummariesTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ClientListStackSetsResponseTypeDef = TypedDict(
    "ClientListStackSetsResponseTypeDef",
    {"Summaries": List[ClientListStackSetsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListStacksResponseStackSummariesDriftInformationTypeDef = TypedDict(
    "ClientListStacksResponseStackSummariesDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ClientListStacksResponseStackSummariesTypeDef = TypedDict(
    "ClientListStacksResponseStackSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "TemplateDescription": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ClientListStacksResponseStackSummariesDriftInformationTypeDef,
    },
    total=False,
)

ClientListStacksResponseTypeDef = TypedDict(
    "ClientListStacksResponseTypeDef",
    {"StackSummaries": List[ClientListStacksResponseStackSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListTypeRegistrationsResponseTypeDef = TypedDict(
    "ClientListTypeRegistrationsResponseTypeDef",
    {"RegistrationTokenList": List[str], "NextToken": str},
    total=False,
)

ClientListTypeVersionsResponseTypeVersionSummariesTypeDef = TypedDict(
    "ClientListTypeVersionsResponseTypeVersionSummariesTypeDef",
    {
        "Type": str,
        "TypeName": str,
        "VersionId": str,
        "Arn": str,
        "TimeCreated": datetime,
        "Description": str,
    },
    total=False,
)

ClientListTypeVersionsResponseTypeDef = TypedDict(
    "ClientListTypeVersionsResponseTypeDef",
    {
        "TypeVersionSummaries": List[ClientListTypeVersionsResponseTypeVersionSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTypesResponseTypeSummariesTypeDef = TypedDict(
    "ClientListTypesResponseTypeSummariesTypeDef",
    {
        "Type": str,
        "TypeName": str,
        "DefaultVersionId": str,
        "TypeArn": str,
        "LastUpdated": datetime,
        "Description": str,
    },
    total=False,
)

ClientListTypesResponseTypeDef = TypedDict(
    "ClientListTypesResponseTypeDef",
    {"TypeSummaries": List[ClientListTypesResponseTypeSummariesTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientRegisterTypeLoggingConfigTypeDef = TypedDict(
    "_RequiredClientRegisterTypeLoggingConfigTypeDef", {"LogRoleArn": str}
)
_OptionalClientRegisterTypeLoggingConfigTypeDef = TypedDict(
    "_OptionalClientRegisterTypeLoggingConfigTypeDef", {"LogGroupName": str}, total=False
)


class ClientRegisterTypeLoggingConfigTypeDef(
    _RequiredClientRegisterTypeLoggingConfigTypeDef, _OptionalClientRegisterTypeLoggingConfigTypeDef
):
    pass


ClientRegisterTypeResponseTypeDef = TypedDict(
    "ClientRegisterTypeResponseTypeDef", {"RegistrationToken": str}, total=False
)

ClientUpdateStackInstancesOperationPreferencesTypeDef = TypedDict(
    "ClientUpdateStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientUpdateStackInstancesParameterOverridesTypeDef = TypedDict(
    "ClientUpdateStackInstancesParameterOverridesTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientUpdateStackInstancesResponseTypeDef = TypedDict(
    "ClientUpdateStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)

ClientUpdateStackParametersTypeDef = TypedDict(
    "ClientUpdateStackParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientUpdateStackResponseTypeDef = TypedDict(
    "ClientUpdateStackResponseTypeDef", {"StackId": str}, total=False
)

_RequiredClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef,
):
    pass


ClientUpdateStackRollbackConfigurationTypeDef = TypedDict(
    "ClientUpdateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

ClientUpdateStackSetOperationPreferencesTypeDef = TypedDict(
    "ClientUpdateStackSetOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

ClientUpdateStackSetParametersTypeDef = TypedDict(
    "ClientUpdateStackSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

ClientUpdateStackSetResponseTypeDef = TypedDict(
    "ClientUpdateStackSetResponseTypeDef", {"OperationId": str}, total=False
)

_RequiredClientUpdateStackSetTagsTypeDef = TypedDict(
    "_RequiredClientUpdateStackSetTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateStackSetTagsTypeDef = TypedDict(
    "_OptionalClientUpdateStackSetTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateStackSetTagsTypeDef(
    _RequiredClientUpdateStackSetTagsTypeDef, _OptionalClientUpdateStackSetTagsTypeDef
):
    pass


_RequiredClientUpdateStackTagsTypeDef = TypedDict(
    "_RequiredClientUpdateStackTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateStackTagsTypeDef = TypedDict(
    "_OptionalClientUpdateStackTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateStackTagsTypeDef(
    _RequiredClientUpdateStackTagsTypeDef, _OptionalClientUpdateStackTagsTypeDef
):
    pass


ClientUpdateTerminationProtectionResponseTypeDef = TypedDict(
    "ClientUpdateTerminationProtectionResponseTypeDef", {"StackId": str}, total=False
)

ClientValidateTemplateResponseParametersTypeDef = TypedDict(
    "ClientValidateTemplateResponseParametersTypeDef",
    {"ParameterKey": str, "DefaultValue": str, "NoEcho": bool, "Description": str},
    total=False,
)

ClientValidateTemplateResponseTypeDef = TypedDict(
    "ClientValidateTemplateResponseTypeDef",
    {
        "Parameters": List[ClientValidateTemplateResponseParametersTypeDef],
        "Description": str,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
    },
    total=False,
)

DescribeAccountLimitsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef = TypedDict(
    "DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)

DescribeAccountLimitsPaginateResponseTypeDef = TypedDict(
    "DescribeAccountLimitsPaginateResponseTypeDef",
    {"AccountLimits": List[DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef]},
    total=False,
)

DescribeChangeSetPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeChangeSetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef = TypedDict(
    "DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef",
    {
        "Attribute": Literal[
            "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
        ],
        "Name": str,
        "RequiresRecreation": Literal["Never", "Conditionally", "Always"],
    },
    total=False,
)

DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef = TypedDict(
    "DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef",
    {
        "Target": DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef,
        "Evaluation": Literal["Static", "Dynamic"],
        "ChangeSource": Literal[
            "ResourceReference",
            "ParameterReference",
            "ResourceAttribute",
            "DirectModification",
            "Automatic",
        ],
        "CausingEntity": str,
    },
    total=False,
)

DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef = TypedDict(
    "DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef",
    {
        "Action": Literal["Add", "Modify", "Remove", "Import"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["True", "False", "Conditional"],
        "Scope": List[
            Literal[
                "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
            ]
        ],
        "Details": List[DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef],
    },
    total=False,
)

DescribeChangeSetPaginateResponseChangesTypeDef = TypedDict(
    "DescribeChangeSetPaginateResponseChangesTypeDef",
    {"Type": str, "ResourceChange": DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef},
    total=False,
)

DescribeChangeSetPaginateResponseParametersTypeDef = TypedDict(
    "DescribeChangeSetPaginateResponseParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)

DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef = TypedDict(
    "DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

DescribeChangeSetPaginateResponseTagsTypeDef = TypedDict(
    "DescribeChangeSetPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

DescribeChangeSetPaginateResponseTypeDef = TypedDict(
    "DescribeChangeSetPaginateResponseTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List[DescribeChangeSetPaginateResponseParametersTypeDef],
        "CreationTime": datetime,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List[DescribeChangeSetPaginateResponseTagsTypeDef],
        "Changes": List[DescribeChangeSetPaginateResponseChangesTypeDef],
    },
    total=False,
)

DescribeStackEventsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeStackEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeStackEventsPaginateResponseStackEventsTypeDef = TypedDict(
    "DescribeStackEventsPaginateResponseStackEventsTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)

DescribeStackEventsPaginateResponseTypeDef = TypedDict(
    "DescribeStackEventsPaginateResponseTypeDef",
    {"StackEvents": List[DescribeStackEventsPaginateResponseStackEventsTypeDef]},
    total=False,
)

DescribeStacksPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeStacksPaginateResponseStacksDriftInformationTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

DescribeStacksPaginateResponseStacksOutputsTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str, "ExportName": str},
    total=False,
)

DescribeStacksPaginateResponseStacksParametersTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)

DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

DescribeStacksPaginateResponseStacksTagsTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksTagsTypeDef", {"Key": str, "Value": str}, total=False
)

DescribeStacksPaginateResponseStacksTypeDef = TypedDict(
    "DescribeStacksPaginateResponseStacksTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List[DescribeStacksPaginateResponseStacksParametersTypeDef],
        "CreationTime": datetime,
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Outputs": List[DescribeStacksPaginateResponseStacksOutputsTypeDef],
        "RoleARN": str,
        "Tags": List[DescribeStacksPaginateResponseStacksTagsTypeDef],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": DescribeStacksPaginateResponseStacksDriftInformationTypeDef,
    },
    total=False,
)

DescribeStacksPaginateResponseTypeDef = TypedDict(
    "DescribeStacksPaginateResponseTypeDef",
    {"Stacks": List[DescribeStacksPaginateResponseStacksTypeDef]},
    total=False,
)

ListChangeSetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListChangeSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListChangeSetsPaginateResponseSummariesTypeDef = TypedDict(
    "ListChangeSetsPaginateResponseSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
    },
    total=False,
)

ListChangeSetsPaginateResponseTypeDef = TypedDict(
    "ListChangeSetsPaginateResponseTypeDef",
    {"Summaries": List[ListChangeSetsPaginateResponseSummariesTypeDef]},
    total=False,
)

ListExportsPaginatePaginationConfigTypeDef = TypedDict(
    "ListExportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListExportsPaginateResponseExportsTypeDef = TypedDict(
    "ListExportsPaginateResponseExportsTypeDef",
    {"ExportingStackId": str, "Name": str, "Value": str},
    total=False,
)

ListExportsPaginateResponseTypeDef = TypedDict(
    "ListExportsPaginateResponseTypeDef",
    {"Exports": List[ListExportsPaginateResponseExportsTypeDef]},
    total=False,
)

ListImportsPaginatePaginationConfigTypeDef = TypedDict(
    "ListImportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListImportsPaginateResponseTypeDef = TypedDict(
    "ListImportsPaginateResponseTypeDef", {"Imports": List[str]}, total=False
)

ListStackInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "ListStackInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListStackInstancesPaginateResponseSummariesTypeDef = TypedDict(
    "ListStackInstancesPaginateResponseSummariesTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ListStackInstancesPaginateResponseTypeDef = TypedDict(
    "ListStackInstancesPaginateResponseTypeDef",
    {"Summaries": List[ListStackInstancesPaginateResponseSummariesTypeDef]},
    total=False,
)

ListStackResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "ListStackResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef = TypedDict(
    "ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ListStackResourcesPaginateResponseStackResourceSummariesTypeDef = TypedDict(
    "ListStackResourcesPaginateResponseStackResourceSummariesTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "DriftInformation": ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef,
    },
    total=False,
)

ListStackResourcesPaginateResponseTypeDef = TypedDict(
    "ListStackResourcesPaginateResponseTypeDef",
    {
        "StackResourceSummaries": List[
            ListStackResourcesPaginateResponseStackResourceSummariesTypeDef
        ]
    },
    total=False,
)

ListStackSetOperationResultsPaginatePaginationConfigTypeDef = TypedDict(
    "ListStackSetOperationResultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef = TypedDict(
    "ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef",
    {"Status": Literal["SUCCEEDED", "FAILED", "SKIPPED"], "StatusReason": str},
    total=False,
)

ListStackSetOperationResultsPaginateResponseSummariesTypeDef = TypedDict(
    "ListStackSetOperationResultsPaginateResponseSummariesTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StatusReason": str,
        "AccountGateResult": ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef,
    },
    total=False,
)

ListStackSetOperationResultsPaginateResponseTypeDef = TypedDict(
    "ListStackSetOperationResultsPaginateResponseTypeDef",
    {"Summaries": List[ListStackSetOperationResultsPaginateResponseSummariesTypeDef]},
    total=False,
)

ListStackSetOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListStackSetOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListStackSetOperationsPaginateResponseSummariesTypeDef = TypedDict(
    "ListStackSetOperationsPaginateResponseSummariesTypeDef",
    {
        "OperationId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED"],
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)

ListStackSetOperationsPaginateResponseTypeDef = TypedDict(
    "ListStackSetOperationsPaginateResponseTypeDef",
    {"Summaries": List[ListStackSetOperationsPaginateResponseSummariesTypeDef]},
    total=False,
)

ListStackSetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListStackSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListStackSetsPaginateResponseSummariesTypeDef = TypedDict(
    "ListStackSetsPaginateResponseSummariesTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

ListStackSetsPaginateResponseTypeDef = TypedDict(
    "ListStackSetsPaginateResponseTypeDef",
    {"Summaries": List[ListStackSetsPaginateResponseSummariesTypeDef]},
    total=False,
)

ListStacksPaginatePaginationConfigTypeDef = TypedDict(
    "ListStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListStacksPaginateResponseStackSummariesDriftInformationTypeDef = TypedDict(
    "ListStacksPaginateResponseStackSummariesDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)

ListStacksPaginateResponseStackSummariesTypeDef = TypedDict(
    "ListStacksPaginateResponseStackSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "TemplateDescription": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ListStacksPaginateResponseStackSummariesDriftInformationTypeDef,
    },
    total=False,
)

ListStacksPaginateResponseTypeDef = TypedDict(
    "ListStacksPaginateResponseTypeDef",
    {"StackSummaries": List[ListStacksPaginateResponseStackSummariesTypeDef]},
    total=False,
)

ServiceResourceCreateStackParametersTypeDef = TypedDict(
    "ServiceResourceCreateStackParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

_RequiredServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef,
):
    pass


ServiceResourceCreateStackRollbackConfigurationTypeDef = TypedDict(
    "ServiceResourceCreateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

_RequiredServiceResourceCreateStackTagsTypeDef = TypedDict(
    "_RequiredServiceResourceCreateStackTagsTypeDef", {"Key": str}
)
_OptionalServiceResourceCreateStackTagsTypeDef = TypedDict(
    "_OptionalServiceResourceCreateStackTagsTypeDef", {"Value": str}, total=False
)


class ServiceResourceCreateStackTagsTypeDef(
    _RequiredServiceResourceCreateStackTagsTypeDef, _OptionalServiceResourceCreateStackTagsTypeDef
):
    pass


StackCreateCompleteWaitWaiterConfigTypeDef = TypedDict(
    "StackCreateCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

StackDeleteCompleteWaitWaiterConfigTypeDef = TypedDict(
    "StackDeleteCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

StackExistsWaitWaiterConfigTypeDef = TypedDict(
    "StackExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

StackImportCompleteWaitWaiterConfigTypeDef = TypedDict(
    "StackImportCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

StackUpdateCompleteWaitWaiterConfigTypeDef = TypedDict(
    "StackUpdateCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

StackUpdateParametersTypeDef = TypedDict(
    "StackUpdateParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

StackUpdateResponseTypeDef = TypedDict("StackUpdateResponseTypeDef", {"StackId": str}, total=False)

_RequiredStackUpdateRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredStackUpdateRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalStackUpdateRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalStackUpdateRollbackConfigurationRollbackTriggersTypeDef", {"Type": str}, total=False
)


class StackUpdateRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredStackUpdateRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalStackUpdateRollbackConfigurationRollbackTriggersTypeDef,
):
    pass


StackUpdateRollbackConfigurationTypeDef = TypedDict(
    "StackUpdateRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[StackUpdateRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

_RequiredStackUpdateTagsTypeDef = TypedDict("_RequiredStackUpdateTagsTypeDef", {"Key": str})
_OptionalStackUpdateTagsTypeDef = TypedDict(
    "_OptionalStackUpdateTagsTypeDef", {"Value": str}, total=False
)


class StackUpdateTagsTypeDef(_RequiredStackUpdateTagsTypeDef, _OptionalStackUpdateTagsTypeDef):
    pass


TypeRegistrationCompleteWaitWaiterConfigTypeDef = TypedDict(
    "TypeRegistrationCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)
