"Main interface for ssm service type defs"
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


ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCancelMaintenanceWindowExecutionResponseTypeDef = TypedDict(
    "ClientCancelMaintenanceWindowExecutionResponseTypeDef", {"WindowExecutionId": str}, total=False
)

ClientCreateActivationResponseTypeDef = TypedDict(
    "ClientCreateActivationResponseTypeDef",
    {"ActivationId": str, "ActivationCode": str},
    total=False,
)

ClientCreateActivationTagsTypeDef = TypedDict(
    "ClientCreateActivationTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationBatchEntriesOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchEntriesOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationBatchEntriesOutputLocationS3LocationTypeDef},
    total=False,
)

ClientCreateAssociationBatchEntriesTargetsTypeDef = TypedDict(
    "ClientCreateAssociationBatchEntriesTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

_RequiredClientCreateAssociationBatchEntriesTypeDef = TypedDict(
    "_RequiredClientCreateAssociationBatchEntriesTypeDef", {"Name": str}
)
_OptionalClientCreateAssociationBatchEntriesTypeDef = TypedDict(
    "_OptionalClientCreateAssociationBatchEntriesTypeDef",
    {
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "AutomationTargetParameterName": str,
        "DocumentVersion": str,
        "Targets": List[ClientCreateAssociationBatchEntriesTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationBatchEntriesOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)


class ClientCreateAssociationBatchEntriesTypeDef(
    _RequiredClientCreateAssociationBatchEntriesTypeDef,
    _OptionalClientCreateAssociationBatchEntriesTypeDef,
):
    pass


ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationBatchResponseFailedEntryOutputLocationS3LocationTypeDef},
    total=False,
)

ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateAssociationBatchResponseFailedEntryTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedEntryTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "AutomationTargetParameterName": str,
        "DocumentVersion": str,
        "Targets": List[ClientCreateAssociationBatchResponseFailedEntryTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationBatchResponseFailedEntryOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientCreateAssociationBatchResponseFailedTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseFailedTypeDef",
    {
        "Entry": ClientCreateAssociationBatchResponseFailedEntryTypeDef,
        "Message": str,
        "Fault": Literal["Client", "Server", "Unknown"],
    },
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationBatchResponseSuccessfulOutputLocationS3LocationTypeDef},
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateAssociationBatchResponseSuccessfulTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseSuccessfulTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientCreateAssociationBatchResponseSuccessfulStatusTypeDef,
        "Overview": ClientCreateAssociationBatchResponseSuccessfulOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientCreateAssociationBatchResponseSuccessfulTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationBatchResponseSuccessfulOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientCreateAssociationBatchResponseTypeDef = TypedDict(
    "ClientCreateAssociationBatchResponseTypeDef",
    {
        "Successful": List[ClientCreateAssociationBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientCreateAssociationBatchResponseFailedTypeDef],
    },
    total=False,
)

ClientCreateAssociationOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationOutputLocationTypeDef",
    {"S3Location": ClientCreateAssociationOutputLocationS3LocationTypeDef},
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientCreateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateAssociationResponseAssociationDescriptionTypeDef = TypedDict(
    "ClientCreateAssociationResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientCreateAssociationResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientCreateAssociationResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientCreateAssociationResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientCreateAssociationResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientCreateAssociationResponseTypeDef = TypedDict(
    "ClientCreateAssociationResponseTypeDef",
    {"AssociationDescription": ClientCreateAssociationResponseAssociationDescriptionTypeDef},
    total=False,
)

ClientCreateAssociationTargetsTypeDef = TypedDict(
    "ClientCreateAssociationTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientCreateDocumentAttachmentsTypeDef = TypedDict(
    "ClientCreateDocumentAttachmentsTypeDef",
    {"Key": Literal["SourceUrl", "S3FileUrl"], "Values": List[str], "Name": str},
    total=False,
)

_RequiredClientCreateDocumentRequiresTypeDef = TypedDict(
    "_RequiredClientCreateDocumentRequiresTypeDef", {"Name": str}
)
_OptionalClientCreateDocumentRequiresTypeDef = TypedDict(
    "_OptionalClientCreateDocumentRequiresTypeDef", {"Version": str}, total=False
)


class ClientCreateDocumentRequiresTypeDef(
    _RequiredClientCreateDocumentRequiresTypeDef, _OptionalClientCreateDocumentRequiresTypeDef
):
    pass


ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)

ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateDocumentResponseDocumentDescriptionTypeDef = TypedDict(
    "ClientCreateDocumentResponseDocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List[ClientCreateDocumentResponseDocumentDescriptionParametersTypeDef],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ClientCreateDocumentResponseDocumentDescriptionTagsTypeDef],
        "AttachmentsInformation": List[
            ClientCreateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef
        ],
        "Requires": List[ClientCreateDocumentResponseDocumentDescriptionRequiresTypeDef],
    },
    total=False,
)

ClientCreateDocumentResponseTypeDef = TypedDict(
    "ClientCreateDocumentResponseTypeDef",
    {"DocumentDescription": ClientCreateDocumentResponseDocumentDescriptionTypeDef},
    total=False,
)

ClientCreateDocumentTagsTypeDef = TypedDict(
    "ClientCreateDocumentTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientCreateMaintenanceWindowResponseTypeDef", {"WindowId": str}, total=False
)

ClientCreateMaintenanceWindowTagsTypeDef = TypedDict(
    "ClientCreateMaintenanceWindowTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateOpsItemNotificationsTypeDef = TypedDict(
    "ClientCreateOpsItemNotificationsTypeDef", {"Arn": str}, total=False
)

ClientCreateOpsItemOperationalDataTypeDef = TypedDict(
    "ClientCreateOpsItemOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)

ClientCreateOpsItemRelatedOpsItemsTypeDef = TypedDict(
    "ClientCreateOpsItemRelatedOpsItemsTypeDef", {"OpsItemId": str}
)

ClientCreateOpsItemResponseTypeDef = TypedDict(
    "ClientCreateOpsItemResponseTypeDef", {"OpsItemId": str}, total=False
)

ClientCreateOpsItemTagsTypeDef = TypedDict(
    "ClientCreateOpsItemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef(
    _RequiredClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
    _OptionalClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
):
    pass


ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
)

_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {"PatchFilterGroup": ClientCreatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef},
)
_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class ClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef(
    _RequiredClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef,
    _OptionalClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef,
):
    pass


ClientCreatePatchBaselineApprovalRulesTypeDef = TypedDict(
    "ClientCreatePatchBaselineApprovalRulesTypeDef",
    {"PatchRules": List[ClientCreatePatchBaselineApprovalRulesPatchRulesTypeDef]},
)

_RequiredClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef(
    _RequiredClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
    _OptionalClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
):
    pass


ClientCreatePatchBaselineGlobalFiltersTypeDef = TypedDict(
    "ClientCreatePatchBaselineGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientCreatePatchBaselineGlobalFiltersPatchFiltersTypeDef]},
)

ClientCreatePatchBaselineResponseTypeDef = TypedDict(
    "ClientCreatePatchBaselineResponseTypeDef", {"BaselineId": str}, total=False
)

_RequiredClientCreatePatchBaselineSourcesTypeDef = TypedDict(
    "_RequiredClientCreatePatchBaselineSourcesTypeDef", {"Name": str}
)
_OptionalClientCreatePatchBaselineSourcesTypeDef = TypedDict(
    "_OptionalClientCreatePatchBaselineSourcesTypeDef",
    {"Products": List[str], "Configuration": str},
    total=False,
)


class ClientCreatePatchBaselineSourcesTypeDef(
    _RequiredClientCreatePatchBaselineSourcesTypeDef,
    _OptionalClientCreatePatchBaselineSourcesTypeDef,
):
    pass


ClientCreatePatchBaselineTagsTypeDef = TypedDict(
    "ClientCreatePatchBaselineTagsTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredClientCreateResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_RequiredClientCreateResourceDataSyncS3DestinationTypeDef", {"BucketName": str}
)
_OptionalClientCreateResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_OptionalClientCreateResourceDataSyncS3DestinationTypeDef",
    {"Prefix": str, "SyncFormat": str, "Region": str, "AWSKMSKeyARN": str},
    total=False,
)


class ClientCreateResourceDataSyncS3DestinationTypeDef(
    _RequiredClientCreateResourceDataSyncS3DestinationTypeDef,
    _OptionalClientCreateResourceDataSyncS3DestinationTypeDef,
):
    pass


ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)

ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)

_RequiredClientCreateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_RequiredClientCreateResourceDataSyncSyncSourceTypeDef", {"SourceType": str}
)
_OptionalClientCreateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_OptionalClientCreateResourceDataSyncSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": ClientCreateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
    },
    total=False,
)


class ClientCreateResourceDataSyncSyncSourceTypeDef(
    _RequiredClientCreateResourceDataSyncSyncSourceTypeDef,
    _OptionalClientCreateResourceDataSyncSyncSourceTypeDef,
):
    pass


ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef = TypedDict(
    "ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)

ClientDeleteInventoryResponseDeletionSummaryTypeDef = TypedDict(
    "ClientDeleteInventoryResponseDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List[ClientDeleteInventoryResponseDeletionSummarySummaryItemsTypeDef],
    },
    total=False,
)

ClientDeleteInventoryResponseTypeDef = TypedDict(
    "ClientDeleteInventoryResponseTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionSummary": ClientDeleteInventoryResponseDeletionSummaryTypeDef,
    },
    total=False,
)

ClientDeleteMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientDeleteMaintenanceWindowResponseTypeDef", {"WindowId": str}, total=False
)

ClientDeleteParametersResponseTypeDef = TypedDict(
    "ClientDeleteParametersResponseTypeDef",
    {"DeletedParameters": List[str], "InvalidParameters": List[str]},
    total=False,
)

ClientDeletePatchBaselineResponseTypeDef = TypedDict(
    "ClientDeletePatchBaselineResponseTypeDef", {"BaselineId": str}, total=False
)

ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef = TypedDict(
    "ClientDeregisterPatchBaselineForPatchGroupResponseTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)

ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientDeregisterTargetFromMaintenanceWindowResponseTypeDef",
    {"WindowId": str, "WindowTargetId": str},
    total=False,
)

ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientDeregisterTaskFromMaintenanceWindowResponseTypeDef",
    {"WindowId": str, "WindowTaskId": str},
    total=False,
)

ClientDescribeActivationsFiltersTypeDef = TypedDict(
    "ClientDescribeActivationsFiltersTypeDef",
    {
        "FilterKey": Literal["ActivationIds", "DefaultInstanceName", "IamRole"],
        "FilterValues": List[str],
    },
    total=False,
)

ClientDescribeActivationsResponseActivationListTagsTypeDef = TypedDict(
    "ClientDescribeActivationsResponseActivationListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeActivationsResponseActivationListTypeDef = TypedDict(
    "ClientDescribeActivationsResponseActivationListTypeDef",
    {
        "ActivationId": str,
        "Description": str,
        "DefaultInstanceName": str,
        "IamRole": str,
        "RegistrationLimit": int,
        "RegistrationsCount": int,
        "ExpirationDate": datetime,
        "Expired": bool,
        "CreatedDate": datetime,
        "Tags": List[ClientDescribeActivationsResponseActivationListTagsTypeDef],
    },
    total=False,
)

ClientDescribeActivationsResponseTypeDef = TypedDict(
    "ClientDescribeActivationsResponseTypeDef",
    {
        "ActivationList": List[ClientDescribeActivationsResponseActivationListTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeAssociationExecutionTargetsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAssociationExecutionTargetsFiltersTypeDef",
    {"Key": Literal["Status", "ResourceId", "ResourceType"]},
)
_OptionalClientDescribeAssociationExecutionTargetsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAssociationExecutionTargetsFiltersTypeDef", {"Value": str}, total=False
)


class ClientDescribeAssociationExecutionTargetsFiltersTypeDef(
    _RequiredClientDescribeAssociationExecutionTargetsFiltersTypeDef,
    _OptionalClientDescribeAssociationExecutionTargetsFiltersTypeDef,
):
    pass


ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef",
    {"OutputSourceId": str, "OutputSourceType": str},
    total=False,
)

ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "ResourceId": str,
        "ResourceType": str,
        "Status": str,
        "DetailedStatus": str,
        "LastExecutionDate": datetime,
        "OutputSource": ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsOutputSourceTypeDef,
    },
    total=False,
)

ClientDescribeAssociationExecutionTargetsResponseTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionTargetsResponseTypeDef",
    {
        "AssociationExecutionTargets": List[
            ClientDescribeAssociationExecutionTargetsResponseAssociationExecutionTargetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeAssociationExecutionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAssociationExecutionsFiltersTypeDef",
    {"Key": Literal["ExecutionId", "Status", "CreatedTime"]},
)
_OptionalClientDescribeAssociationExecutionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAssociationExecutionsFiltersTypeDef",
    {"Value": str, "Type": Literal["EQUAL", "LESS_THAN", "GREATER_THAN"]},
    total=False,
)


class ClientDescribeAssociationExecutionsFiltersTypeDef(
    _RequiredClientDescribeAssociationExecutionsFiltersTypeDef,
    _OptionalClientDescribeAssociationExecutionsFiltersTypeDef,
):
    pass


ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "Status": str,
        "DetailedStatus": str,
        "CreatedTime": datetime,
        "LastExecutionDate": datetime,
        "ResourceCountByStatus": str,
    },
    total=False,
)

ClientDescribeAssociationExecutionsResponseTypeDef = TypedDict(
    "ClientDescribeAssociationExecutionsResponseTypeDef",
    {
        "AssociationExecutions": List[
            ClientDescribeAssociationExecutionsResponseAssociationExecutionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientDescribeAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeAssociationResponseAssociationDescriptionTypeDef = TypedDict(
    "ClientDescribeAssociationResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientDescribeAssociationResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientDescribeAssociationResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientDescribeAssociationResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientDescribeAssociationResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientDescribeAssociationResponseTypeDef = TypedDict(
    "ClientDescribeAssociationResponseTypeDef",
    {"AssociationDescription": ClientDescribeAssociationResponseAssociationDescriptionTypeDef},
    total=False,
)

_RequiredClientDescribeAutomationExecutionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAutomationExecutionsFiltersTypeDef",
    {
        "Key": Literal[
            "DocumentNamePrefix",
            "ExecutionStatus",
            "ExecutionId",
            "ParentExecutionId",
            "CurrentAction",
            "StartTimeBefore",
            "StartTimeAfter",
            "AutomationType",
        ]
    },
)
_OptionalClientDescribeAutomationExecutionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAutomationExecutionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeAutomationExecutionsFiltersTypeDef(
    _RequiredClientDescribeAutomationExecutionsFiltersTypeDef,
    _OptionalClientDescribeAutomationExecutionsFiltersTypeDef,
):
    pass


ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef = TypedDict(
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef",
    {"ParameterValues": List[str], "Truncated": bool},
    total=False,
)

ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef = TypedDict(
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef = TypedDict(
    "ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "FailureMessage": str,
        "TargetParameterName": str,
        "Targets": List[
            ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTargetsTypeDef
        ],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListResolvedTargetsTypeDef,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "AutomationType": Literal["CrossAccount", "Local"],
    },
    total=False,
)

ClientDescribeAutomationExecutionsResponseTypeDef = TypedDict(
    "ClientDescribeAutomationExecutionsResponseTypeDef",
    {
        "AutomationExecutionMetadataList": List[
            ClientDescribeAutomationExecutionsResponseAutomationExecutionMetadataListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeAutomationStepExecutionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeAutomationStepExecutionsFiltersTypeDef",
    {
        "Key": Literal[
            "StartTimeBefore",
            "StartTimeAfter",
            "StepExecutionStatus",
            "StepExecutionId",
            "StepName",
            "Action",
        ]
    },
)
_OptionalClientDescribeAutomationStepExecutionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeAutomationStepExecutionsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeAutomationStepExecutionsFiltersTypeDef(
    _RequiredClientDescribeAutomationStepExecutionsFiltersTypeDef,
    _OptionalClientDescribeAutomationStepExecutionsFiltersTypeDef,
):
    pass


ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)

ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": ClientDescribeAutomationStepExecutionsResponseStepExecutionsFailureDetailsTypeDef,
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List[ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetsTypeDef],
        "TargetLocation": ClientDescribeAutomationStepExecutionsResponseStepExecutionsTargetLocationTypeDef,
    },
    total=False,
)

ClientDescribeAutomationStepExecutionsResponseTypeDef = TypedDict(
    "ClientDescribeAutomationStepExecutionsResponseTypeDef",
    {
        "StepExecutions": List[ClientDescribeAutomationStepExecutionsResponseStepExecutionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAvailablePatchesFiltersTypeDef = TypedDict(
    "ClientDescribeAvailablePatchesFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribeAvailablePatchesResponsePatchesTypeDef = TypedDict(
    "ClientDescribeAvailablePatchesResponsePatchesTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)

ClientDescribeAvailablePatchesResponseTypeDef = TypedDict(
    "ClientDescribeAvailablePatchesResponseTypeDef",
    {"Patches": List[ClientDescribeAvailablePatchesResponsePatchesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef = TypedDict(
    "ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef",
    {"AccountId": str, "SharedDocumentVersion": str},
    total=False,
)

ClientDescribeDocumentPermissionResponseTypeDef = TypedDict(
    "ClientDescribeDocumentPermissionResponseTypeDef",
    {
        "AccountIds": List[str],
        "AccountSharingInfoList": List[
            ClientDescribeDocumentPermissionResponseAccountSharingInfoListTypeDef
        ],
    },
    total=False,
)

ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeDocumentResponseDocumentParametersTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentParametersTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)

ClientDescribeDocumentResponseDocumentRequiresTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientDescribeDocumentResponseDocumentTagsTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeDocumentResponseDocumentTypeDef = TypedDict(
    "ClientDescribeDocumentResponseDocumentTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List[ClientDescribeDocumentResponseDocumentParametersTypeDef],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ClientDescribeDocumentResponseDocumentTagsTypeDef],
        "AttachmentsInformation": List[
            ClientDescribeDocumentResponseDocumentAttachmentsInformationTypeDef
        ],
        "Requires": List[ClientDescribeDocumentResponseDocumentRequiresTypeDef],
    },
    total=False,
)

ClientDescribeDocumentResponseTypeDef = TypedDict(
    "ClientDescribeDocumentResponseTypeDef",
    {"Document": ClientDescribeDocumentResponseDocumentTypeDef},
    total=False,
)

ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef = TypedDict(
    "ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef",
    {"AssociationId": str, "InstanceId": str, "Content": str, "AssociationVersion": str},
    total=False,
)

ClientDescribeEffectiveInstanceAssociationsResponseTypeDef = TypedDict(
    "ClientDescribeEffectiveInstanceAssociationsResponseTypeDef",
    {
        "Associations": List[
            ClientDescribeEffectiveInstanceAssociationsResponseAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef = TypedDict(
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef",
    {
        "DeploymentStatus": Literal[
            "APPROVED", "PENDING_APPROVAL", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED"
        ],
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovalDate": datetime,
    },
    total=False,
)

ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef = TypedDict(
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)

ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef = TypedDict(
    "ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef",
    {
        "Patch": ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchTypeDef,
        "PatchStatus": ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesPatchStatusTypeDef,
    },
    total=False,
)

ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef = TypedDict(
    "ClientDescribeEffectivePatchesForPatchBaselineResponseTypeDef",
    {
        "EffectivePatches": List[
            ClientDescribeEffectivePatchesForPatchBaselineResponseEffectivePatchesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef = TypedDict(
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef",
    {"OutputUrl": str},
    total=False,
)

ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef = TypedDict(
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef",
    {
        "S3OutputUrl": ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef
    },
    total=False,
)

ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef = TypedDict(
    "ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef",
    {
        "AssociationId": str,
        "Name": str,
        "DocumentVersion": str,
        "AssociationVersion": str,
        "InstanceId": str,
        "ExecutionDate": datetime,
        "Status": str,
        "DetailedStatus": str,
        "ExecutionSummary": str,
        "ErrorCode": str,
        "OutputUrl": ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosOutputUrlTypeDef,
        "AssociationName": str,
    },
    total=False,
)

ClientDescribeInstanceAssociationsStatusResponseTypeDef = TypedDict(
    "ClientDescribeInstanceAssociationsStatusResponseTypeDef",
    {
        "InstanceAssociationStatusInfos": List[
            ClientDescribeInstanceAssociationsStatusResponseInstanceAssociationStatusInfosTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeInstanceInformationFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeInstanceInformationFiltersTypeDef", {"Key": str}
)
_OptionalClientDescribeInstanceInformationFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeInstanceInformationFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeInstanceInformationFiltersTypeDef(
    _RequiredClientDescribeInstanceInformationFiltersTypeDef,
    _OptionalClientDescribeInstanceInformationFiltersTypeDef,
):
    pass


_RequiredClientDescribeInstanceInformationInstanceInformationFilterListTypeDef = TypedDict(
    "_RequiredClientDescribeInstanceInformationInstanceInformationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceIds",
            "AgentVersion",
            "PingStatus",
            "PlatformTypes",
            "ActivationIds",
            "IamRole",
            "ResourceType",
            "AssociationStatus",
        ]
    },
)
_OptionalClientDescribeInstanceInformationInstanceInformationFilterListTypeDef = TypedDict(
    "_OptionalClientDescribeInstanceInformationInstanceInformationFilterListTypeDef",
    {"valueSet": List[str]},
    total=False,
)


class ClientDescribeInstanceInformationInstanceInformationFilterListTypeDef(
    _RequiredClientDescribeInstanceInformationInstanceInformationFilterListTypeDef,
    _OptionalClientDescribeInstanceInformationInstanceInformationFilterListTypeDef,
):
    pass


ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef = TypedDict(
    "ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef",
    {"DetailedStatus": str, "InstanceAssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef = TypedDict(
    "ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef",
    {
        "InstanceId": str,
        "PingStatus": Literal["Online", "ConnectionLost", "Inactive"],
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": Literal["Windows", "Linux"],
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": Literal["ManagedInstance", "Document", "EC2Instance"],
        "Name": str,
        "IPAddress": str,
        "ComputerName": str,
        "AssociationStatus": str,
        "LastAssociationExecutionDate": datetime,
        "LastSuccessfulAssociationExecutionDate": datetime,
        "AssociationOverview": ClientDescribeInstanceInformationResponseInstanceInformationListAssociationOverviewTypeDef,
    },
    total=False,
)

ClientDescribeInstanceInformationResponseTypeDef = TypedDict(
    "ClientDescribeInstanceInformationResponseTypeDef",
    {
        "InstanceInformationList": List[
            ClientDescribeInstanceInformationResponseInstanceInformationListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef", {"Key": str}
)
_OptionalClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef",
    {"Values": List[str], "Type": Literal["Equal", "NotEqual", "LessThan", "GreaterThan"]},
    total=False,
)


class ClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef(
    _RequiredClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef,
    _OptionalClientDescribeInstancePatchStatesForPatchGroupFiltersTypeDef,
):
    pass


ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef = TypedDict(
    "ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)

ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef = TypedDict(
    "ClientDescribeInstancePatchStatesForPatchGroupResponseTypeDef",
    {
        "InstancePatchStates": List[
            ClientDescribeInstancePatchStatesForPatchGroupResponseInstancePatchStatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef = TypedDict(
    "ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)

ClientDescribeInstancePatchStatesResponseTypeDef = TypedDict(
    "ClientDescribeInstancePatchStatesResponseTypeDef",
    {
        "InstancePatchStates": List[
            ClientDescribeInstancePatchStatesResponseInstancePatchStatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeInstancePatchesFiltersTypeDef = TypedDict(
    "ClientDescribeInstancePatchesFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribeInstancePatchesResponsePatchesTypeDef = TypedDict(
    "ClientDescribeInstancePatchesResponsePatchesTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": Literal[
            "INSTALLED",
            "INSTALLED_OTHER",
            "INSTALLED_PENDING_REBOOT",
            "INSTALLED_REJECTED",
            "MISSING",
            "NOT_APPLICABLE",
            "FAILED",
        ],
        "InstalledTime": datetime,
    },
    total=False,
)

ClientDescribeInstancePatchesResponseTypeDef = TypedDict(
    "ClientDescribeInstancePatchesResponseTypeDef",
    {"Patches": List[ClientDescribeInstancePatchesResponsePatchesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef = TypedDict(
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)

ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef = TypedDict(
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List[
            ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef
        ],
    },
    total=False,
)

ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef = TypedDict(
    "ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": Literal["InProgress", "Complete"],
        "LastStatusMessage": str,
        "DeletionSummary": ClientDescribeInventoryDeletionsResponseInventoryDeletionsDeletionSummaryTypeDef,
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)

ClientDescribeInventoryDeletionsResponseTypeDef = TypedDict(
    "ClientDescribeInventoryDeletionsResponseTypeDef",
    {
        "InventoryDeletions": List[
            ClientDescribeInventoryDeletionsResponseInventoryDeletionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            ClientDescribeMaintenanceWindowExecutionTaskInvocationsResponseWindowExecutionTaskInvocationIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTasksFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionTasksResponseTypeDef",
    {
        "WindowExecutionTaskIdentities": List[
            ClientDescribeMaintenanceWindowExecutionTasksResponseWindowExecutionTaskIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef",
    {
        "WindowId": str,
        "WindowExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ClientDescribeMaintenanceWindowExecutionsResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowExecutionsResponseTypeDef",
    {
        "WindowExecutions": List[
            ClientDescribeMaintenanceWindowExecutionsResponseWindowExecutionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowScheduleFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowScheduleFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef",
    {"WindowId": str, "Name": str, "ExecutionTime": str},
    total=False,
)

ClientDescribeMaintenanceWindowScheduleResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowScheduleResponseTypeDef",
    {
        "ScheduledWindowExecutions": List[
            ClientDescribeMaintenanceWindowScheduleResponseScheduledWindowExecutionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowScheduleTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowScheduleTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTargetsFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTargetsFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": Literal["INSTANCE", "RESOURCE_GROUP"],
        "Targets": List[ClientDescribeMaintenanceWindowTargetsResponseTargetsTargetsTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowTargetsResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTargetsResponseTypeDef",
    {
        "Targets": List[ClientDescribeMaintenanceWindowTargetsResponseTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowTasksFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Targets": List[ClientDescribeMaintenanceWindowTasksResponseTasksTargetsTypeDef],
        "TaskParameters": Dict[
            str, ClientDescribeMaintenanceWindowTasksResponseTasksTaskParametersTypeDef
        ],
        "Priority": int,
        "LoggingInfo": ClientDescribeMaintenanceWindowTasksResponseTasksLoggingInfoTypeDef,
        "ServiceRoleArn": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowTasksResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowTasksResponseTypeDef",
    {"Tasks": List[ClientDescribeMaintenanceWindowTasksResponseTasksTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeMaintenanceWindowsFiltersTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef",
    {"WindowId": str, "Name": str},
    total=False,
)

ClientDescribeMaintenanceWindowsForTargetResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsForTargetResponseTypeDef",
    {
        "WindowIdentities": List[
            ClientDescribeMaintenanceWindowsForTargetResponseWindowIdentitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsForTargetTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "Enabled": bool,
        "Duration": int,
        "Cutoff": int,
        "Schedule": str,
        "ScheduleTimezone": str,
        "EndDate": str,
        "StartDate": str,
        "NextExecutionTime": str,
    },
    total=False,
)

ClientDescribeMaintenanceWindowsResponseTypeDef = TypedDict(
    "ClientDescribeMaintenanceWindowsResponseTypeDef",
    {
        "WindowIdentities": List[ClientDescribeMaintenanceWindowsResponseWindowIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeOpsItemsOpsItemFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeOpsItemsOpsItemFiltersTypeDef",
    {
        "Key": Literal[
            "Status",
            "CreatedBy",
            "Source",
            "Priority",
            "Title",
            "OpsItemId",
            "CreatedTime",
            "LastModifiedTime",
            "OperationalData",
            "OperationalDataKey",
            "OperationalDataValue",
            "ResourceId",
            "AutomationId",
            "Category",
            "Severity",
        ]
    },
)
_OptionalClientDescribeOpsItemsOpsItemFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeOpsItemsOpsItemFiltersTypeDef",
    {"Values": List[str], "Operator": Literal["Equal", "Contains", "GreaterThan", "LessThan"]},
    total=False,
)


class ClientDescribeOpsItemsOpsItemFiltersTypeDef(
    _RequiredClientDescribeOpsItemsOpsItemFiltersTypeDef,
    _OptionalClientDescribeOpsItemsOpsItemFiltersTypeDef,
):
    pass


ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef = TypedDict(
    "ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)

ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef = TypedDict(
    "ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Priority": int,
        "Source": str,
        "Status": Literal["Open", "InProgress", "Resolved"],
        "OpsItemId": str,
        "Title": str,
        "OperationalData": Dict[
            str, ClientDescribeOpsItemsResponseOpsItemSummariesOperationalDataTypeDef
        ],
        "Category": str,
        "Severity": str,
    },
    total=False,
)

ClientDescribeOpsItemsResponseTypeDef = TypedDict(
    "ClientDescribeOpsItemsResponseTypeDef",
    {
        "NextToken": str,
        "OpsItemSummaries": List[ClientDescribeOpsItemsResponseOpsItemSummariesTypeDef],
    },
    total=False,
)

_RequiredClientDescribeParametersFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeParametersFiltersTypeDef", {"Key": Literal["Name", "Type", "KeyId"]}
)
_OptionalClientDescribeParametersFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeParametersFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeParametersFiltersTypeDef(
    _RequiredClientDescribeParametersFiltersTypeDef, _OptionalClientDescribeParametersFiltersTypeDef
):
    pass


ClientDescribeParametersParameterFiltersTypeDef = TypedDict(
    "ClientDescribeParametersParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)

ClientDescribeParametersResponseParametersPoliciesTypeDef = TypedDict(
    "ClientDescribeParametersResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)

ClientDescribeParametersResponseParametersTypeDef = TypedDict(
    "ClientDescribeParametersResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[ClientDescribeParametersResponseParametersPoliciesTypeDef],
    },
    total=False,
)

ClientDescribeParametersResponseTypeDef = TypedDict(
    "ClientDescribeParametersResponseTypeDef",
    {"Parameters": List[ClientDescribeParametersResponseParametersTypeDef], "NextToken": str},
    total=False,
)

ClientDescribePatchBaselinesFiltersTypeDef = TypedDict(
    "ClientDescribePatchBaselinesFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef = TypedDict(
    "ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

ClientDescribePatchBaselinesResponseTypeDef = TypedDict(
    "ClientDescribePatchBaselinesResponseTypeDef",
    {
        "BaselineIdentities": List[ClientDescribePatchBaselinesResponseBaselineIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribePatchGroupStateResponseTypeDef = TypedDict(
    "ClientDescribePatchGroupStateResponseTypeDef",
    {
        "Instances": int,
        "InstancesWithInstalledPatches": int,
        "InstancesWithInstalledOtherPatches": int,
        "InstancesWithInstalledPendingRebootPatches": int,
        "InstancesWithInstalledRejectedPatches": int,
        "InstancesWithMissingPatches": int,
        "InstancesWithFailedPatches": int,
        "InstancesWithNotApplicablePatches": int,
        "InstancesWithUnreportedNotApplicablePatches": int,
    },
    total=False,
)

ClientDescribePatchGroupsFiltersTypeDef = TypedDict(
    "ClientDescribePatchGroupsFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef = TypedDict(
    "ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

ClientDescribePatchGroupsResponseMappingsTypeDef = TypedDict(
    "ClientDescribePatchGroupsResponseMappingsTypeDef",
    {
        "PatchGroup": str,
        "BaselineIdentity": ClientDescribePatchGroupsResponseMappingsBaselineIdentityTypeDef,
    },
    total=False,
)

ClientDescribePatchGroupsResponseTypeDef = TypedDict(
    "ClientDescribePatchGroupsResponseTypeDef",
    {"Mappings": List[ClientDescribePatchGroupsResponseMappingsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribePatchPropertiesResponseTypeDef = TypedDict(
    "ClientDescribePatchPropertiesResponseTypeDef",
    {"Properties": List[Dict[str, str]], "NextToken": str},
    total=False,
)

_RequiredClientDescribeSessionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeSessionsFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Target", "Owner", "Status"]},
)
_OptionalClientDescribeSessionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeSessionsFiltersTypeDef", {"value": str}, total=False
)


class ClientDescribeSessionsFiltersTypeDef(
    _RequiredClientDescribeSessionsFiltersTypeDef, _OptionalClientDescribeSessionsFiltersTypeDef
):
    pass


ClientDescribeSessionsResponseSessionsOutputUrlTypeDef = TypedDict(
    "ClientDescribeSessionsResponseSessionsOutputUrlTypeDef",
    {"S3OutputUrl": str, "CloudWatchOutputUrl": str},
    total=False,
)

ClientDescribeSessionsResponseSessionsTypeDef = TypedDict(
    "ClientDescribeSessionsResponseSessionsTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": Literal[
            "Connected", "Connecting", "Disconnected", "Terminated", "Terminating", "Failed"
        ],
        "StartDate": datetime,
        "EndDate": datetime,
        "DocumentName": str,
        "Owner": str,
        "Details": str,
        "OutputUrl": ClientDescribeSessionsResponseSessionsOutputUrlTypeDef,
    },
    total=False,
)

ClientDescribeSessionsResponseTypeDef = TypedDict(
    "ClientDescribeSessionsResponseTypeDef",
    {"Sessions": List[ClientDescribeSessionsResponseSessionsTypeDef], "NextToken": str},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef",
    {
        "TotalSteps": int,
        "SuccessSteps": int,
        "FailedSteps": int,
        "CancelledSteps": int,
        "TimedOutSteps": int,
    },
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef",
    {"ParameterValues": List[str], "Truncated": bool},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsFailureDetailsTypeDef,
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List[
            ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetsTypeDef
        ],
        "TargetLocation": ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTargetLocationTypeDef,
    },
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetAutomationExecutionResponseAutomationExecutionTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseAutomationExecutionTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "StepExecutions": List[
            ClientGetAutomationExecutionResponseAutomationExecutionStepExecutionsTypeDef
        ],
        "StepExecutionsTruncated": bool,
        "Parameters": Dict[str, List[str]],
        "Outputs": Dict[str, List[str]],
        "FailureMessage": str,
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "ExecutedBy": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "TargetParameterName": str,
        "Targets": List[ClientGetAutomationExecutionResponseAutomationExecutionTargetsTypeDef],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": ClientGetAutomationExecutionResponseAutomationExecutionResolvedTargetsTypeDef,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "TargetLocations": List[
            ClientGetAutomationExecutionResponseAutomationExecutionTargetLocationsTypeDef
        ],
        "ProgressCounters": ClientGetAutomationExecutionResponseAutomationExecutionProgressCountersTypeDef,
    },
    total=False,
)

ClientGetAutomationExecutionResponseTypeDef = TypedDict(
    "ClientGetAutomationExecutionResponseTypeDef",
    {"AutomationExecution": ClientGetAutomationExecutionResponseAutomationExecutionTypeDef},
    total=False,
)

ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientGetCommandInvocationResponseTypeDef = TypedDict(
    "ClientGetCommandInvocationResponseTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "PluginName": str,
        "ResponseCode": int,
        "ExecutionStartDateTime": str,
        "ExecutionElapsedTime": str,
        "ExecutionEndDateTime": str,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "StandardOutputContent": str,
        "StandardOutputUrl": str,
        "StandardErrorContent": str,
        "StandardErrorUrl": str,
        "CloudWatchOutputConfig": ClientGetCommandInvocationResponseCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ClientGetConnectionStatusResponseTypeDef = TypedDict(
    "ClientGetConnectionStatusResponseTypeDef",
    {"Target": str, "Status": Literal["Connected", "NotConnected"]},
    total=False,
)

ClientGetDefaultPatchBaselineResponseTypeDef = TypedDict(
    "ClientGetDefaultPatchBaselineResponseTypeDef",
    {
        "BaselineId": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
    },
    total=False,
)

ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef = TypedDict(
    "ClientGetDeployablePatchSnapshotForInstanceResponseTypeDef",
    {"InstanceId": str, "SnapshotId": str, "SnapshotDownloadUrl": str, "Product": str},
    total=False,
)

ClientGetDocumentResponseAttachmentsContentTypeDef = TypedDict(
    "ClientGetDocumentResponseAttachmentsContentTypeDef",
    {"Name": str, "Size": int, "Hash": str, "HashType": str, "Url": str},
    total=False,
)

ClientGetDocumentResponseRequiresTypeDef = TypedDict(
    "ClientGetDocumentResponseRequiresTypeDef", {"Name": str, "Version": str}, total=False
)

ClientGetDocumentResponseTypeDef = TypedDict(
    "ClientGetDocumentResponseTypeDef",
    {
        "Name": str,
        "VersionName": str,
        "DocumentVersion": str,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "Content": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "DocumentFormat": Literal["YAML", "JSON"],
        "Requires": List[ClientGetDocumentResponseRequiresTypeDef],
        "AttachmentsContent": List[ClientGetDocumentResponseAttachmentsContentTypeDef],
    },
    total=False,
)

ClientGetInventoryAggregatorsGroupsFiltersTypeDef = TypedDict(
    "ClientGetInventoryAggregatorsGroupsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)

ClientGetInventoryAggregatorsGroupsTypeDef = TypedDict(
    "ClientGetInventoryAggregatorsGroupsTypeDef",
    {"Name": str, "Filters": List[ClientGetInventoryAggregatorsGroupsFiltersTypeDef]},
    total=False,
)

ClientGetInventoryAggregatorsTypeDef = TypedDict(
    "ClientGetInventoryAggregatorsTypeDef",
    {
        "Expression": str,
        "Aggregators": Any,
        "Groups": List[ClientGetInventoryAggregatorsGroupsTypeDef],
    },
    total=False,
)

_RequiredClientGetInventoryFiltersTypeDef = TypedDict(
    "_RequiredClientGetInventoryFiltersTypeDef", {"Key": str}
)
_OptionalClientGetInventoryFiltersTypeDef = TypedDict(
    "_OptionalClientGetInventoryFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientGetInventoryFiltersTypeDef(
    _RequiredClientGetInventoryFiltersTypeDef, _OptionalClientGetInventoryFiltersTypeDef
):
    pass


ClientGetInventoryResponseEntitiesDataTypeDef = TypedDict(
    "ClientGetInventoryResponseEntitiesDataTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": str,
        "Content": List[Dict[str, str]],
    },
    total=False,
)

ClientGetInventoryResponseEntitiesTypeDef = TypedDict(
    "ClientGetInventoryResponseEntitiesTypeDef",
    {"Id": str, "Data": Dict[str, ClientGetInventoryResponseEntitiesDataTypeDef]},
    total=False,
)

ClientGetInventoryResponseTypeDef = TypedDict(
    "ClientGetInventoryResponseTypeDef",
    {"Entities": List[ClientGetInventoryResponseEntitiesTypeDef], "NextToken": str},
    total=False,
)

ClientGetInventoryResultAttributesTypeDef = TypedDict(
    "ClientGetInventoryResultAttributesTypeDef", {"TypeName": str}
)

ClientGetInventorySchemaResponseSchemasAttributesTypeDef = TypedDict(
    "ClientGetInventorySchemaResponseSchemasAttributesTypeDef",
    {"Name": str, "DataType": Literal["string", "number"]},
    total=False,
)

ClientGetInventorySchemaResponseSchemasTypeDef = TypedDict(
    "ClientGetInventorySchemaResponseSchemasTypeDef",
    {
        "TypeName": str,
        "Version": str,
        "Attributes": List[ClientGetInventorySchemaResponseSchemasAttributesTypeDef],
        "DisplayName": str,
    },
    total=False,
)

ClientGetInventorySchemaResponseTypeDef = TypedDict(
    "ClientGetInventorySchemaResponseTypeDef",
    {"Schemas": List[ClientGetInventorySchemaResponseSchemasTypeDef], "NextToken": str},
    total=False,
)

ClientGetMaintenanceWindowExecutionResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowExecutionResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskIds": List[str],
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowExecutionTaskInvocationResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef = TypedDict(
    "ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientGetMaintenanceWindowExecutionTaskResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowExecutionTaskResponseTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "TaskArn": str,
        "ServiceRole": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "TaskParameters": List[
            Dict[str, ClientGetMaintenanceWindowExecutionTaskResponseTaskParametersTypeDef]
        ],
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ClientGetMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowResponseTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "NextExecutionTime": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
    },
    total=False,
)

ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTargetsTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "NotificationConfig": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientGetMaintenanceWindowTaskResponseTypeDef = TypedDict(
    "ClientGetMaintenanceWindowTaskResponseTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List[ClientGetMaintenanceWindowTaskResponseTargetsTypeDef],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "TaskParameters": Dict[str, ClientGetMaintenanceWindowTaskResponseTaskParametersTypeDef],
        "TaskInvocationParameters": ClientGetMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef,
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": ClientGetMaintenanceWindowTaskResponseLoggingInfoTypeDef,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientGetOpsItemResponseOpsItemNotificationsTypeDef = TypedDict(
    "ClientGetOpsItemResponseOpsItemNotificationsTypeDef", {"Arn": str}, total=False
)

ClientGetOpsItemResponseOpsItemOperationalDataTypeDef = TypedDict(
    "ClientGetOpsItemResponseOpsItemOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)

ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef = TypedDict(
    "ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef", {"OpsItemId": str}, total=False
)

ClientGetOpsItemResponseOpsItemTypeDef = TypedDict(
    "ClientGetOpsItemResponseOpsItemTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "Description": str,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Notifications": List[ClientGetOpsItemResponseOpsItemNotificationsTypeDef],
        "Priority": int,
        "RelatedOpsItems": List[ClientGetOpsItemResponseOpsItemRelatedOpsItemsTypeDef],
        "Status": Literal["Open", "InProgress", "Resolved"],
        "OpsItemId": str,
        "Version": str,
        "Title": str,
        "Source": str,
        "OperationalData": Dict[str, ClientGetOpsItemResponseOpsItemOperationalDataTypeDef],
        "Category": str,
        "Severity": str,
    },
    total=False,
)

ClientGetOpsItemResponseTypeDef = TypedDict(
    "ClientGetOpsItemResponseTypeDef",
    {"OpsItem": ClientGetOpsItemResponseOpsItemTypeDef},
    total=False,
)

ClientGetOpsSummaryAggregatorsFiltersTypeDef = TypedDict(
    "ClientGetOpsSummaryAggregatorsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)

ClientGetOpsSummaryAggregatorsTypeDef = TypedDict(
    "ClientGetOpsSummaryAggregatorsTypeDef",
    {
        "AggregatorType": str,
        "TypeName": str,
        "AttributeName": str,
        "Values": Dict[str, str],
        "Filters": List[ClientGetOpsSummaryAggregatorsFiltersTypeDef],
        "Aggregators": Any,
    },
    total=False,
)

_RequiredClientGetOpsSummaryFiltersTypeDef = TypedDict(
    "_RequiredClientGetOpsSummaryFiltersTypeDef", {"Key": str}
)
_OptionalClientGetOpsSummaryFiltersTypeDef = TypedDict(
    "_OptionalClientGetOpsSummaryFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientGetOpsSummaryFiltersTypeDef(
    _RequiredClientGetOpsSummaryFiltersTypeDef, _OptionalClientGetOpsSummaryFiltersTypeDef
):
    pass


ClientGetOpsSummaryResponseEntitiesDataTypeDef = TypedDict(
    "ClientGetOpsSummaryResponseEntitiesDataTypeDef",
    {"CaptureTime": str, "Content": List[Dict[str, str]]},
    total=False,
)

ClientGetOpsSummaryResponseEntitiesTypeDef = TypedDict(
    "ClientGetOpsSummaryResponseEntitiesTypeDef",
    {"Id": str, "Data": Dict[str, ClientGetOpsSummaryResponseEntitiesDataTypeDef]},
    total=False,
)

ClientGetOpsSummaryResponseTypeDef = TypedDict(
    "ClientGetOpsSummaryResponseTypeDef",
    {"Entities": List[ClientGetOpsSummaryResponseEntitiesTypeDef], "NextToken": str},
    total=False,
)

ClientGetOpsSummaryResultAttributesTypeDef = TypedDict(
    "ClientGetOpsSummaryResultAttributesTypeDef", {"TypeName": str}
)

ClientGetParameterHistoryResponseParametersPoliciesTypeDef = TypedDict(
    "ClientGetParameterHistoryResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)

ClientGetParameterHistoryResponseParametersTypeDef = TypedDict(
    "ClientGetParameterHistoryResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[ClientGetParameterHistoryResponseParametersPoliciesTypeDef],
    },
    total=False,
)

ClientGetParameterHistoryResponseTypeDef = TypedDict(
    "ClientGetParameterHistoryResponseTypeDef",
    {"Parameters": List[ClientGetParameterHistoryResponseParametersTypeDef], "NextToken": str},
    total=False,
)

ClientGetParameterResponseParameterTypeDef = TypedDict(
    "ClientGetParameterResponseParameterTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)

ClientGetParameterResponseTypeDef = TypedDict(
    "ClientGetParameterResponseTypeDef",
    {"Parameter": ClientGetParameterResponseParameterTypeDef},
    total=False,
)

ClientGetParametersByPathParameterFiltersTypeDef = TypedDict(
    "ClientGetParametersByPathParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)

ClientGetParametersByPathResponseParametersTypeDef = TypedDict(
    "ClientGetParametersByPathResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)

ClientGetParametersByPathResponseTypeDef = TypedDict(
    "ClientGetParametersByPathResponseTypeDef",
    {"Parameters": List[ClientGetParametersByPathResponseParametersTypeDef], "NextToken": str},
    total=False,
)

ClientGetParametersResponseParametersTypeDef = TypedDict(
    "ClientGetParametersResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)

ClientGetParametersResponseTypeDef = TypedDict(
    "ClientGetParametersResponseTypeDef",
    {
        "Parameters": List[ClientGetParametersResponseParametersTypeDef],
        "InvalidParameters": List[str],
    },
    total=False,
)

ClientGetPatchBaselineForPatchGroupResponseTypeDef = TypedDict(
    "ClientGetPatchBaselineForPatchGroupResponseTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
    },
    total=False,
)

ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)

ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
    total=False,
)

ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    {
        "PatchFilterGroup": ClientGetPatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef,
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "EnableNonSecurity": bool,
    },
    total=False,
)

ClientGetPatchBaselineResponseApprovalRulesTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseApprovalRulesTypeDef",
    {"PatchRules": List[ClientGetPatchBaselineResponseApprovalRulesPatchRulesTypeDef]},
    total=False,
)

ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)

ClientGetPatchBaselineResponseGlobalFiltersTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientGetPatchBaselineResponseGlobalFiltersPatchFiltersTypeDef]},
    total=False,
)

ClientGetPatchBaselineResponseSourcesTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseSourcesTypeDef",
    {"Name": str, "Products": List[str], "Configuration": str},
    total=False,
)

ClientGetPatchBaselineResponseTypeDef = TypedDict(
    "ClientGetPatchBaselineResponseTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "GlobalFilters": ClientGetPatchBaselineResponseGlobalFiltersTypeDef,
        "ApprovalRules": ClientGetPatchBaselineResponseApprovalRulesTypeDef,
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": Literal["ALLOW_AS_DEPENDENCY", "BLOCK"],
        "PatchGroups": List[str],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List[ClientGetPatchBaselineResponseSourcesTypeDef],
    },
    total=False,
)

ClientGetServiceSettingResponseServiceSettingTypeDef = TypedDict(
    "ClientGetServiceSettingResponseServiceSettingTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "ARN": str,
        "Status": str,
    },
    total=False,
)

ClientGetServiceSettingResponseTypeDef = TypedDict(
    "ClientGetServiceSettingResponseTypeDef",
    {"ServiceSetting": ClientGetServiceSettingResponseServiceSettingTypeDef},
    total=False,
)

ClientLabelParameterVersionResponseTypeDef = TypedDict(
    "ClientLabelParameterVersionResponseTypeDef",
    {"InvalidLabels": List[str], "ParameterVersion": int},
    total=False,
)

ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef",
    {
        "S3Location": ClientListAssociationVersionsResponseAssociationVersionsOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListAssociationVersionsResponseAssociationVersionsTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseAssociationVersionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "CreatedDate": datetime,
        "Name": str,
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List[ClientListAssociationVersionsResponseAssociationVersionsTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientListAssociationVersionsResponseAssociationVersionsOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientListAssociationVersionsResponseTypeDef = TypedDict(
    "ClientListAssociationVersionsResponseTypeDef",
    {
        "AssociationVersions": List[
            ClientListAssociationVersionsResponseAssociationVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListAssociationsAssociationFilterListTypeDef = TypedDict(
    "_RequiredClientListAssociationsAssociationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceId",
            "Name",
            "AssociationId",
            "AssociationStatusName",
            "LastExecutedBefore",
            "LastExecutedAfter",
            "AssociationName",
        ]
    },
)
_OptionalClientListAssociationsAssociationFilterListTypeDef = TypedDict(
    "_OptionalClientListAssociationsAssociationFilterListTypeDef", {"value": str}, total=False
)


class ClientListAssociationsAssociationFilterListTypeDef(
    _RequiredClientListAssociationsAssociationFilterListTypeDef,
    _OptionalClientListAssociationsAssociationFilterListTypeDef,
):
    pass


ClientListAssociationsResponseAssociationsOverviewTypeDef = TypedDict(
    "ClientListAssociationsResponseAssociationsOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientListAssociationsResponseAssociationsTargetsTypeDef = TypedDict(
    "ClientListAssociationsResponseAssociationsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListAssociationsResponseAssociationsTypeDef = TypedDict(
    "ClientListAssociationsResponseAssociationsTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
        "DocumentVersion": str,
        "Targets": List[ClientListAssociationsResponseAssociationsTargetsTypeDef],
        "LastExecutionDate": datetime,
        "Overview": ClientListAssociationsResponseAssociationsOverviewTypeDef,
        "ScheduleExpression": str,
        "AssociationName": str,
    },
    total=False,
)

ClientListAssociationsResponseTypeDef = TypedDict(
    "ClientListAssociationsResponseTypeDef",
    {"Associations": List[ClientListAssociationsResponseAssociationsTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientListCommandInvocationsFiltersTypeDef = TypedDict(
    "_RequiredClientListCommandInvocationsFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalClientListCommandInvocationsFiltersTypeDef = TypedDict(
    "_OptionalClientListCommandInvocationsFiltersTypeDef", {"value": str}, total=False
)


class ClientListCommandInvocationsFiltersTypeDef(
    _RequiredClientListCommandInvocationsFiltersTypeDef,
    _OptionalClientListCommandInvocationsFiltersTypeDef,
):
    pass


ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef",
    {
        "Name": str,
        "Status": Literal["Pending", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"],
        "StatusDetails": str,
        "ResponseCode": int,
        "ResponseStartDateTime": datetime,
        "ResponseFinishDateTime": datetime,
        "Output": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)

ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientListCommandInvocationsResponseCommandInvocationsTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseCommandInvocationsTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "InstanceName": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "TraceOutput": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "CommandPlugins": List[
            ClientListCommandInvocationsResponseCommandInvocationsCommandPluginsTypeDef
        ],
        "ServiceRole": str,
        "NotificationConfig": ClientListCommandInvocationsResponseCommandInvocationsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ClientListCommandInvocationsResponseCommandInvocationsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ClientListCommandInvocationsResponseTypeDef = TypedDict(
    "ClientListCommandInvocationsResponseTypeDef",
    {
        "CommandInvocations": List[ClientListCommandInvocationsResponseCommandInvocationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListCommandsFiltersTypeDef = TypedDict(
    "_RequiredClientListCommandsFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalClientListCommandsFiltersTypeDef = TypedDict(
    "_OptionalClientListCommandsFiltersTypeDef", {"value": str}, total=False
)


class ClientListCommandsFiltersTypeDef(
    _RequiredClientListCommandsFiltersTypeDef, _OptionalClientListCommandsFiltersTypeDef
):
    pass


ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientListCommandsResponseCommandsNotificationConfigTypeDef = TypedDict(
    "ClientListCommandsResponseCommandsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientListCommandsResponseCommandsTargetsTypeDef = TypedDict(
    "ClientListCommandsResponseCommandsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientListCommandsResponseCommandsTypeDef = TypedDict(
    "ClientListCommandsResponseCommandsTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List[ClientListCommandsResponseCommandsTargetsTypeDef],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": ClientListCommandsResponseCommandsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ClientListCommandsResponseCommandsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ClientListCommandsResponseTypeDef = TypedDict(
    "ClientListCommandsResponseTypeDef",
    {"Commands": List[ClientListCommandsResponseCommandsTypeDef], "NextToken": str},
    total=False,
)

ClientListComplianceItemsFiltersTypeDef = TypedDict(
    "ClientListComplianceItemsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)

ClientListComplianceItemsResponseComplianceItemsTypeDef = TypedDict(
    "ClientListComplianceItemsResponseComplianceItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Id": str,
        "Title": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "ExecutionSummary": ClientListComplianceItemsResponseComplianceItemsExecutionSummaryTypeDef,
        "Details": Dict[str, str],
    },
    total=False,
)

ClientListComplianceItemsResponseTypeDef = TypedDict(
    "ClientListComplianceItemsResponseTypeDef",
    {
        "ComplianceItems": List[ClientListComplianceItemsResponseComplianceItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListComplianceSummariesFiltersTypeDef = TypedDict(
    "ClientListComplianceSummariesFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "CompliantSummary": ClientListComplianceSummariesResponseComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ClientListComplianceSummariesResponseComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)

ClientListComplianceSummariesResponseTypeDef = TypedDict(
    "ClientListComplianceSummariesResponseTypeDef",
    {
        "ComplianceSummaryItems": List[
            ClientListComplianceSummariesResponseComplianceSummaryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListDocumentVersionsResponseDocumentVersionsTypeDef = TypedDict(
    "ClientListDocumentVersionsResponseDocumentVersionsTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": Literal["YAML", "JSON"],
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
    },
    total=False,
)

ClientListDocumentVersionsResponseTypeDef = TypedDict(
    "ClientListDocumentVersionsResponseTypeDef",
    {
        "DocumentVersions": List[ClientListDocumentVersionsResponseDocumentVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListDocumentsDocumentFilterListTypeDef = TypedDict(
    "_RequiredClientListDocumentsDocumentFilterListTypeDef",
    {"key": Literal["Name", "Owner", "PlatformTypes", "DocumentType"]},
)
_OptionalClientListDocumentsDocumentFilterListTypeDef = TypedDict(
    "_OptionalClientListDocumentsDocumentFilterListTypeDef", {"value": str}, total=False
)


class ClientListDocumentsDocumentFilterListTypeDef(
    _RequiredClientListDocumentsDocumentFilterListTypeDef,
    _OptionalClientListDocumentsDocumentFilterListTypeDef,
):
    pass


ClientListDocumentsFiltersTypeDef = TypedDict(
    "ClientListDocumentsFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef = TypedDict(
    "ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef = TypedDict(
    "ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListDocumentsResponseDocumentIdentifiersTypeDef = TypedDict(
    "ClientListDocumentsResponseDocumentIdentifiersTypeDef",
    {
        "Name": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentVersion": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ClientListDocumentsResponseDocumentIdentifiersTagsTypeDef],
        "Requires": List[ClientListDocumentsResponseDocumentIdentifiersRequiresTypeDef],
    },
    total=False,
)

ClientListDocumentsResponseTypeDef = TypedDict(
    "ClientListDocumentsResponseTypeDef",
    {
        "DocumentIdentifiers": List[ClientListDocumentsResponseDocumentIdentifiersTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListInventoryEntriesFiltersTypeDef = TypedDict(
    "_RequiredClientListInventoryEntriesFiltersTypeDef", {"Key": str}
)
_OptionalClientListInventoryEntriesFiltersTypeDef = TypedDict(
    "_OptionalClientListInventoryEntriesFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class ClientListInventoryEntriesFiltersTypeDef(
    _RequiredClientListInventoryEntriesFiltersTypeDef,
    _OptionalClientListInventoryEntriesFiltersTypeDef,
):
    pass


ClientListInventoryEntriesResponseTypeDef = TypedDict(
    "ClientListInventoryEntriesResponseTypeDef",
    {
        "TypeName": str,
        "InstanceId": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "Entries": List[Dict[str, str]],
        "NextToken": str,
    },
    total=False,
)

ClientListResourceComplianceSummariesFiltersTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "OverallSeverity": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ExecutionSummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef,
        "CompliantSummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)

ClientListResourceComplianceSummariesResponseTypeDef = TypedDict(
    "ClientListResourceComplianceSummariesResponseTypeDef",
    {
        "ResourceComplianceSummaryItems": List[
            ClientListResourceComplianceSummariesResponseResourceComplianceSummaryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef",
    {"BucketName": str, "Prefix": str, "SyncFormat": str, "Region": str, "AWSKMSKeyARN": str},
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef",
    {
        "SourceType": str,
        "AwsOrganizationsSource": ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
        "State": str,
    },
    total=False,
)

ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": ClientListResourceDataSyncResponseResourceDataSyncItemsSyncSourceTypeDef,
        "S3Destination": ClientListResourceDataSyncResponseResourceDataSyncItemsS3DestinationTypeDef,
        "LastSyncTime": datetime,
        "LastSuccessfulSyncTime": datetime,
        "SyncLastModifiedTime": datetime,
        "LastStatus": Literal["Successful", "Failed", "InProgress"],
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)

ClientListResourceDataSyncResponseTypeDef = TypedDict(
    "ClientListResourceDataSyncResponseTypeDef",
    {
        "ResourceDataSyncItems": List[
            ClientListResourceDataSyncResponseResourceDataSyncItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

_RequiredClientPutComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "_RequiredClientPutComplianceItemsExecutionSummaryTypeDef", {"ExecutionTime": datetime}
)
_OptionalClientPutComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "_OptionalClientPutComplianceItemsExecutionSummaryTypeDef",
    {"ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ClientPutComplianceItemsExecutionSummaryTypeDef(
    _RequiredClientPutComplianceItemsExecutionSummaryTypeDef,
    _OptionalClientPutComplianceItemsExecutionSummaryTypeDef,
):
    pass


ClientPutComplianceItemsItemsTypeDef = TypedDict(
    "ClientPutComplianceItemsItemsTypeDef",
    {
        "Id": str,
        "Title": str,
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Details": Dict[str, str],
    },
    total=False,
)

_RequiredClientPutInventoryItemsTypeDef = TypedDict(
    "_RequiredClientPutInventoryItemsTypeDef", {"TypeName": str}
)
_OptionalClientPutInventoryItemsTypeDef = TypedDict(
    "_OptionalClientPutInventoryItemsTypeDef",
    {
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": str,
        "Content": List[Dict[str, str]],
        "Context": Dict[str, str],
    },
    total=False,
)


class ClientPutInventoryItemsTypeDef(
    _RequiredClientPutInventoryItemsTypeDef, _OptionalClientPutInventoryItemsTypeDef
):
    pass


ClientPutInventoryResponseTypeDef = TypedDict(
    "ClientPutInventoryResponseTypeDef", {"Message": str}, total=False
)

ClientPutParameterResponseTypeDef = TypedDict(
    "ClientPutParameterResponseTypeDef",
    {"Version": int, "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"]},
    total=False,
)

ClientPutParameterTagsTypeDef = TypedDict(
    "ClientPutParameterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRegisterDefaultPatchBaselineResponseTypeDef = TypedDict(
    "ClientRegisterDefaultPatchBaselineResponseTypeDef", {"BaselineId": str}, total=False
)

ClientRegisterPatchBaselineForPatchGroupResponseTypeDef = TypedDict(
    "ClientRegisterPatchBaselineForPatchGroupResponseTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)

ClientRegisterTargetWithMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientRegisterTargetWithMaintenanceWindowResponseTypeDef", {"WindowTargetId": str}, total=False
)

ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef = TypedDict(
    "ClientRegisterTargetWithMaintenanceWindowTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowResponseTypeDef", {"WindowTaskId": str}, total=False
)

ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "NotificationConfig": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientRegisterTaskWithMaintenanceWindowTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)

ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef = TypedDict(
    "ClientRegisterTaskWithMaintenanceWindowTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientResetServiceSettingResponseServiceSettingTypeDef = TypedDict(
    "ClientResetServiceSettingResponseServiceSettingTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "ARN": str,
        "Status": str,
    },
    total=False,
)

ClientResetServiceSettingResponseTypeDef = TypedDict(
    "ClientResetServiceSettingResponseTypeDef",
    {"ServiceSetting": ClientResetServiceSettingResponseServiceSettingTypeDef},
    total=False,
)

ClientResumeSessionResponseTypeDef = TypedDict(
    "ClientResumeSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)

ClientSendCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientSendCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientSendCommandNotificationConfigTypeDef = TypedDict(
    "ClientSendCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef = TypedDict(
    "ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ClientSendCommandResponseCommandNotificationConfigTypeDef = TypedDict(
    "ClientSendCommandResponseCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientSendCommandResponseCommandTargetsTypeDef = TypedDict(
    "ClientSendCommandResponseCommandTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientSendCommandResponseCommandTypeDef = TypedDict(
    "ClientSendCommandResponseCommandTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List[ClientSendCommandResponseCommandTargetsTypeDef],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": ClientSendCommandResponseCommandNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ClientSendCommandResponseCommandCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ClientSendCommandResponseTypeDef = TypedDict(
    "ClientSendCommandResponseTypeDef",
    {"Command": ClientSendCommandResponseCommandTypeDef},
    total=False,
)

ClientSendCommandTargetsTypeDef = TypedDict(
    "ClientSendCommandTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientStartAutomationExecutionResponseTypeDef = TypedDict(
    "ClientStartAutomationExecutionResponseTypeDef", {"AutomationExecutionId": str}, total=False
)

ClientStartAutomationExecutionTargetLocationsTypeDef = TypedDict(
    "ClientStartAutomationExecutionTargetLocationsTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

ClientStartAutomationExecutionTargetsTypeDef = TypedDict(
    "ClientStartAutomationExecutionTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientStartSessionResponseTypeDef = TypedDict(
    "ClientStartSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)

ClientTerminateSessionResponseTypeDef = TypedDict(
    "ClientTerminateSessionResponseTypeDef", {"SessionId": str}, total=False
)

ClientUpdateAssociationOutputLocationS3LocationTypeDef = TypedDict(
    "ClientUpdateAssociationOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientUpdateAssociationOutputLocationTypeDef = TypedDict(
    "ClientUpdateAssociationOutputLocationTypeDef",
    {"S3Location": ClientUpdateAssociationOutputLocationS3LocationTypeDef},
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientUpdateAssociationResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateAssociationResponseAssociationDescriptionTypeDef = TypedDict(
    "ClientUpdateAssociationResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientUpdateAssociationResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientUpdateAssociationResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientUpdateAssociationResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientUpdateAssociationResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientUpdateAssociationResponseTypeDef = TypedDict(
    "ClientUpdateAssociationResponseTypeDef",
    {"AssociationDescription": ClientUpdateAssociationResponseAssociationDescriptionTypeDef},
    total=False,
)

_RequiredClientUpdateAssociationStatusAssociationStatusTypeDef = TypedDict(
    "_RequiredClientUpdateAssociationStatusAssociationStatusTypeDef", {"Date": datetime}
)
_OptionalClientUpdateAssociationStatusAssociationStatusTypeDef = TypedDict(
    "_OptionalClientUpdateAssociationStatusAssociationStatusTypeDef",
    {"Name": Literal["Pending", "Success", "Failed"], "Message": str, "AdditionalInfo": str},
    total=False,
)


class ClientUpdateAssociationStatusAssociationStatusTypeDef(
    _RequiredClientUpdateAssociationStatusAssociationStatusTypeDef,
    _OptionalClientUpdateAssociationStatusAssociationStatusTypeDef,
):
    pass


ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef",
    {
        "S3Location": ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationS3LocationTypeDef
    },
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef",
    {
        "Date": datetime,
        "Name": Literal["Pending", "Success", "Failed"],
        "Message": str,
        "AdditionalInfo": str,
    },
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": ClientUpdateAssociationStatusResponseAssociationDescriptionStatusTypeDef,
        "Overview": ClientUpdateAssociationStatusResponseAssociationDescriptionOverviewTypeDef,
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List[ClientUpdateAssociationStatusResponseAssociationDescriptionTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ClientUpdateAssociationStatusResponseAssociationDescriptionOutputLocationTypeDef,
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ClientUpdateAssociationStatusResponseTypeDef = TypedDict(
    "ClientUpdateAssociationStatusResponseTypeDef",
    {"AssociationDescription": ClientUpdateAssociationStatusResponseAssociationDescriptionTypeDef},
    total=False,
)

ClientUpdateAssociationTargetsTypeDef = TypedDict(
    "ClientUpdateAssociationTargetsTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientUpdateDocumentAttachmentsTypeDef = TypedDict(
    "ClientUpdateDocumentAttachmentsTypeDef",
    {"Key": Literal["SourceUrl", "S3FileUrl"], "Values": List[str], "Name": str},
    total=False,
)

ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef = TypedDict(
    "ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef",
    {"Name": str, "DefaultVersion": str, "DefaultVersionName": str},
    total=False,
)

ClientUpdateDocumentDefaultVersionResponseTypeDef = TypedDict(
    "ClientUpdateDocumentDefaultVersionResponseTypeDef",
    {"Description": ClientUpdateDocumentDefaultVersionResponseDescriptionTypeDef},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef",
    {"Name": str},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientUpdateDocumentResponseDocumentDescriptionTypeDef = TypedDict(
    "ClientUpdateDocumentResponseDocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List[ClientUpdateDocumentResponseDocumentDescriptionParametersTypeDef],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ClientUpdateDocumentResponseDocumentDescriptionTagsTypeDef],
        "AttachmentsInformation": List[
            ClientUpdateDocumentResponseDocumentDescriptionAttachmentsInformationTypeDef
        ],
        "Requires": List[ClientUpdateDocumentResponseDocumentDescriptionRequiresTypeDef],
    },
    total=False,
)

ClientUpdateDocumentResponseTypeDef = TypedDict(
    "ClientUpdateDocumentResponseTypeDef",
    {"DocumentDescription": ClientUpdateDocumentResponseDocumentDescriptionTypeDef},
    total=False,
)

ClientUpdateMaintenanceWindowResponseTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowResponseTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTargetResponseTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTargetResponseTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": List[ClientUpdateMaintenanceWindowTargetResponseTargetsTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTargetTargetsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTargetTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "NotificationConfig": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskResponseTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskResponseTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List[ClientUpdateMaintenanceWindowTaskResponseTargetsTypeDef],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, ClientUpdateMaintenanceWindowTaskResponseTaskParametersTypeDef],
        "TaskInvocationParameters": ClientUpdateMaintenanceWindowTaskResponseTaskInvocationParametersTypeDef,
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": ClientUpdateMaintenanceWindowTaskResponseLoggingInfoTypeDef,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskTargetsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef",
    {
        "Comment": str,
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "NotificationConfig": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandNotificationConfigTypeDef,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef",
    {"Input": str, "Name": str},
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskInvocationParametersTypeDef",
    {
        "RunCommand": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersRunCommandTypeDef,
        "Automation": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersAutomationTypeDef,
        "StepFunctions": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersStepFunctionsTypeDef,
        "Lambda": ClientUpdateMaintenanceWindowTaskTaskInvocationParametersLambdaTypeDef,
    },
    total=False,
)

ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef = TypedDict(
    "ClientUpdateMaintenanceWindowTaskTaskParametersTypeDef", {"Values": List[str]}, total=False
)

ClientUpdateOpsItemNotificationsTypeDef = TypedDict(
    "ClientUpdateOpsItemNotificationsTypeDef", {"Arn": str}, total=False
)

ClientUpdateOpsItemOperationalDataTypeDef = TypedDict(
    "ClientUpdateOpsItemOperationalDataTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)

ClientUpdateOpsItemRelatedOpsItemsTypeDef = TypedDict(
    "ClientUpdateOpsItemRelatedOpsItemsTypeDef", {"OpsItemId": str}
)

_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef(
    _RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
    _OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef,
):
    pass


ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
)

_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {"PatchFilterGroup": ClientUpdatePatchBaselineApprovalRulesPatchRulesPatchFilterGroupTypeDef},
)
_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef",
    {
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class ClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef(
    _RequiredClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef,
    _OptionalClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef,
):
    pass


ClientUpdatePatchBaselineApprovalRulesTypeDef = TypedDict(
    "ClientUpdatePatchBaselineApprovalRulesTypeDef",
    {"PatchRules": List[ClientUpdatePatchBaselineApprovalRulesPatchRulesTypeDef]},
)

_RequiredClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ]
    },
)
_OptionalClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef(
    _RequiredClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
    _OptionalClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef,
):
    pass


ClientUpdatePatchBaselineGlobalFiltersTypeDef = TypedDict(
    "ClientUpdatePatchBaselineGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientUpdatePatchBaselineGlobalFiltersPatchFiltersTypeDef]},
)

ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)

ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef",
    {
        "PatchFilters": List[
            ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupPatchFiltersTypeDef
        ]
    },
    total=False,
)

ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef",
    {
        "PatchFilterGroup": ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesPatchFilterGroupTypeDef,
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "EnableNonSecurity": bool,
    },
    total=False,
)

ClientUpdatePatchBaselineResponseApprovalRulesTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseApprovalRulesTypeDef",
    {"PatchRules": List[ClientUpdatePatchBaselineResponseApprovalRulesPatchRulesTypeDef]},
    total=False,
)

ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
    total=False,
)

ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef",
    {"PatchFilters": List[ClientUpdatePatchBaselineResponseGlobalFiltersPatchFiltersTypeDef]},
    total=False,
)

ClientUpdatePatchBaselineResponseSourcesTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseSourcesTypeDef",
    {"Name": str, "Products": List[str], "Configuration": str},
    total=False,
)

ClientUpdatePatchBaselineResponseTypeDef = TypedDict(
    "ClientUpdatePatchBaselineResponseTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "GlobalFilters": ClientUpdatePatchBaselineResponseGlobalFiltersTypeDef,
        "ApprovalRules": ClientUpdatePatchBaselineResponseApprovalRulesTypeDef,
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": Literal["ALLOW_AS_DEPENDENCY", "BLOCK"],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List[ClientUpdatePatchBaselineResponseSourcesTypeDef],
    },
    total=False,
)

_RequiredClientUpdatePatchBaselineSourcesTypeDef = TypedDict(
    "_RequiredClientUpdatePatchBaselineSourcesTypeDef", {"Name": str}
)
_OptionalClientUpdatePatchBaselineSourcesTypeDef = TypedDict(
    "_OptionalClientUpdatePatchBaselineSourcesTypeDef",
    {"Products": List[str], "Configuration": str},
    total=False,
)


class ClientUpdatePatchBaselineSourcesTypeDef(
    _RequiredClientUpdatePatchBaselineSourcesTypeDef,
    _OptionalClientUpdatePatchBaselineSourcesTypeDef,
):
    pass


ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)

ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)

_RequiredClientUpdateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_RequiredClientUpdateResourceDataSyncSyncSourceTypeDef", {"SourceType": str}
)
_OptionalClientUpdateResourceDataSyncSyncSourceTypeDef = TypedDict(
    "_OptionalClientUpdateResourceDataSyncSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": ClientUpdateResourceDataSyncSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
    },
    total=False,
)


class ClientUpdateResourceDataSyncSyncSourceTypeDef(
    _RequiredClientUpdateResourceDataSyncSyncSourceTypeDef,
    _OptionalClientUpdateResourceDataSyncSyncSourceTypeDef,
):
    pass


DescribeActivationsPaginateFiltersTypeDef = TypedDict(
    "DescribeActivationsPaginateFiltersTypeDef",
    {
        "FilterKey": Literal["ActivationIds", "DefaultInstanceName", "IamRole"],
        "FilterValues": List[str],
    },
    total=False,
)

DescribeActivationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeActivationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeActivationsPaginateResponseActivationListTagsTypeDef = TypedDict(
    "DescribeActivationsPaginateResponseActivationListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

DescribeActivationsPaginateResponseActivationListTypeDef = TypedDict(
    "DescribeActivationsPaginateResponseActivationListTypeDef",
    {
        "ActivationId": str,
        "Description": str,
        "DefaultInstanceName": str,
        "IamRole": str,
        "RegistrationLimit": int,
        "RegistrationsCount": int,
        "ExpirationDate": datetime,
        "Expired": bool,
        "CreatedDate": datetime,
        "Tags": List[DescribeActivationsPaginateResponseActivationListTagsTypeDef],
    },
    total=False,
)

DescribeActivationsPaginateResponseTypeDef = TypedDict(
    "DescribeActivationsPaginateResponseTypeDef",
    {"ActivationList": List[DescribeActivationsPaginateResponseActivationListTypeDef]},
    total=False,
)

_RequiredDescribeAssociationExecutionTargetsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeAssociationExecutionTargetsPaginateFiltersTypeDef",
    {"Key": Literal["Status", "ResourceId", "ResourceType"]},
)
_OptionalDescribeAssociationExecutionTargetsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeAssociationExecutionTargetsPaginateFiltersTypeDef",
    {"Value": str},
    total=False,
)


class DescribeAssociationExecutionTargetsPaginateFiltersTypeDef(
    _RequiredDescribeAssociationExecutionTargetsPaginateFiltersTypeDef,
    _OptionalDescribeAssociationExecutionTargetsPaginateFiltersTypeDef,
):
    pass


DescribeAssociationExecutionTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsOutputSourceTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsOutputSourceTypeDef",
    {"OutputSourceId": str, "OutputSourceType": str},
    total=False,
)

DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "ResourceId": str,
        "ResourceType": str,
        "Status": str,
        "DetailedStatus": str,
        "LastExecutionDate": datetime,
        "OutputSource": DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsOutputSourceTypeDef,
    },
    total=False,
)

DescribeAssociationExecutionTargetsPaginateResponseTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsPaginateResponseTypeDef",
    {
        "AssociationExecutionTargets": List[
            DescribeAssociationExecutionTargetsPaginateResponseAssociationExecutionTargetsTypeDef
        ]
    },
    total=False,
)

_RequiredDescribeAssociationExecutionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeAssociationExecutionsPaginateFiltersTypeDef",
    {"Key": Literal["ExecutionId", "Status", "CreatedTime"]},
)
_OptionalDescribeAssociationExecutionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeAssociationExecutionsPaginateFiltersTypeDef",
    {"Value": str, "Type": Literal["EQUAL", "LESS_THAN", "GREATER_THAN"]},
    total=False,
)


class DescribeAssociationExecutionsPaginateFiltersTypeDef(
    _RequiredDescribeAssociationExecutionsPaginateFiltersTypeDef,
    _OptionalDescribeAssociationExecutionsPaginateFiltersTypeDef,
):
    pass


DescribeAssociationExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAssociationExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAssociationExecutionsPaginateResponseAssociationExecutionsTypeDef = TypedDict(
    "DescribeAssociationExecutionsPaginateResponseAssociationExecutionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "Status": str,
        "DetailedStatus": str,
        "CreatedTime": datetime,
        "LastExecutionDate": datetime,
        "ResourceCountByStatus": str,
    },
    total=False,
)

DescribeAssociationExecutionsPaginateResponseTypeDef = TypedDict(
    "DescribeAssociationExecutionsPaginateResponseTypeDef",
    {
        "AssociationExecutions": List[
            DescribeAssociationExecutionsPaginateResponseAssociationExecutionsTypeDef
        ]
    },
    total=False,
)

_RequiredDescribeAutomationExecutionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeAutomationExecutionsPaginateFiltersTypeDef",
    {
        "Key": Literal[
            "DocumentNamePrefix",
            "ExecutionStatus",
            "ExecutionId",
            "ParentExecutionId",
            "CurrentAction",
            "StartTimeBefore",
            "StartTimeAfter",
            "AutomationType",
        ]
    },
)
_OptionalDescribeAutomationExecutionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeAutomationExecutionsPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeAutomationExecutionsPaginateFiltersTypeDef(
    _RequiredDescribeAutomationExecutionsPaginateFiltersTypeDef,
    _OptionalDescribeAutomationExecutionsPaginateFiltersTypeDef,
):
    pass


DescribeAutomationExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAutomationExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListResolvedTargetsTypeDef = TypedDict(
    "DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListResolvedTargetsTypeDef",
    {"ParameterValues": List[str], "Truncated": bool},
    total=False,
)

DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTargetsTypeDef = TypedDict(
    "DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTypeDef = TypedDict(
    "DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "FailureMessage": str,
        "TargetParameterName": str,
        "Targets": List[
            DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTargetsTypeDef
        ],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListResolvedTargetsTypeDef,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "AutomationType": Literal["CrossAccount", "Local"],
    },
    total=False,
)

DescribeAutomationExecutionsPaginateResponseTypeDef = TypedDict(
    "DescribeAutomationExecutionsPaginateResponseTypeDef",
    {
        "AutomationExecutionMetadataList": List[
            DescribeAutomationExecutionsPaginateResponseAutomationExecutionMetadataListTypeDef
        ]
    },
    total=False,
)

_RequiredDescribeAutomationStepExecutionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeAutomationStepExecutionsPaginateFiltersTypeDef",
    {
        "Key": Literal[
            "StartTimeBefore",
            "StartTimeAfter",
            "StepExecutionStatus",
            "StepExecutionId",
            "StepName",
            "Action",
        ]
    },
)
_OptionalDescribeAutomationStepExecutionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeAutomationStepExecutionsPaginateFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeAutomationStepExecutionsPaginateFiltersTypeDef(
    _RequiredDescribeAutomationStepExecutionsPaginateFiltersTypeDef,
    _OptionalDescribeAutomationStepExecutionsPaginateFiltersTypeDef,
):
    pass


DescribeAutomationStepExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAutomationStepExecutionsPaginateResponseStepExecutionsFailureDetailsTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsPaginateResponseStepExecutionsFailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)

DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetLocationTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetsTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": DescribeAutomationStepExecutionsPaginateResponseStepExecutionsFailureDetailsTypeDef,
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List[
            DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetsTypeDef
        ],
        "TargetLocation": DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTargetLocationTypeDef,
    },
    total=False,
)

DescribeAutomationStepExecutionsPaginateResponseTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsPaginateResponseTypeDef",
    {"StepExecutions": List[DescribeAutomationStepExecutionsPaginateResponseStepExecutionsTypeDef]},
    total=False,
)

DescribeAvailablePatchesPaginateFiltersTypeDef = TypedDict(
    "DescribeAvailablePatchesPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

DescribeAvailablePatchesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAvailablePatchesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAvailablePatchesPaginateResponsePatchesTypeDef = TypedDict(
    "DescribeAvailablePatchesPaginateResponsePatchesTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)

DescribeAvailablePatchesPaginateResponseTypeDef = TypedDict(
    "DescribeAvailablePatchesPaginateResponseTypeDef",
    {"Patches": List[DescribeAvailablePatchesPaginateResponsePatchesTypeDef]},
    total=False,
)

DescribeEffectiveInstanceAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEffectiveInstanceAssociationsPaginateResponseAssociationsTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsPaginateResponseAssociationsTypeDef",
    {"AssociationId": str, "InstanceId": str, "Content": str, "AssociationVersion": str},
    total=False,
)

DescribeEffectiveInstanceAssociationsPaginateResponseTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsPaginateResponseTypeDef",
    {
        "Associations": List[
            DescribeEffectiveInstanceAssociationsPaginateResponseAssociationsTypeDef
        ]
    },
    total=False,
)

DescribeEffectivePatchesForPatchBaselinePaginatePaginationConfigTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselinePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchStatusTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchStatusTypeDef",
    {
        "DeploymentStatus": Literal[
            "APPROVED", "PENDING_APPROVAL", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED"
        ],
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovalDate": datetime,
    },
    total=False,
)

DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)

DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesTypeDef",
    {
        "Patch": DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchTypeDef,
        "PatchStatus": DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesPatchStatusTypeDef,
    },
    total=False,
)

DescribeEffectivePatchesForPatchBaselinePaginateResponseTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselinePaginateResponseTypeDef",
    {
        "EffectivePatches": List[
            DescribeEffectivePatchesForPatchBaselinePaginateResponseEffectivePatchesTypeDef
        ]
    },
    total=False,
)

DescribeInstanceAssociationsStatusPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef",
    {"OutputUrl": str},
    total=False,
)

DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlTypeDef",
    {
        "S3OutputUrl": DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlS3OutputUrlTypeDef
    },
    total=False,
)

DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosTypeDef",
    {
        "AssociationId": str,
        "Name": str,
        "DocumentVersion": str,
        "AssociationVersion": str,
        "InstanceId": str,
        "ExecutionDate": datetime,
        "Status": str,
        "DetailedStatus": str,
        "ExecutionSummary": str,
        "ErrorCode": str,
        "OutputUrl": DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosOutputUrlTypeDef,
        "AssociationName": str,
    },
    total=False,
)

DescribeInstanceAssociationsStatusPaginateResponseTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusPaginateResponseTypeDef",
    {
        "InstanceAssociationStatusInfos": List[
            DescribeInstanceAssociationsStatusPaginateResponseInstanceAssociationStatusInfosTypeDef
        ]
    },
    total=False,
)

_RequiredDescribeInstanceInformationPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeInstanceInformationPaginateFiltersTypeDef", {"Key": str}
)
_OptionalDescribeInstanceInformationPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeInstanceInformationPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeInstanceInformationPaginateFiltersTypeDef(
    _RequiredDescribeInstanceInformationPaginateFiltersTypeDef,
    _OptionalDescribeInstanceInformationPaginateFiltersTypeDef,
):
    pass


_RequiredDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef = TypedDict(
    "_RequiredDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceIds",
            "AgentVersion",
            "PingStatus",
            "PlatformTypes",
            "ActivationIds",
            "IamRole",
            "ResourceType",
            "AssociationStatus",
        ]
    },
)
_OptionalDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef = TypedDict(
    "_OptionalDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef",
    {"valueSet": List[str]},
    total=False,
)


class DescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef(
    _RequiredDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef,
    _OptionalDescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef,
):
    pass


DescribeInstanceInformationPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeInstanceInformationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeInstanceInformationPaginateResponseInstanceInformationListAssociationOverviewTypeDef = TypedDict(
    "DescribeInstanceInformationPaginateResponseInstanceInformationListAssociationOverviewTypeDef",
    {"DetailedStatus": str, "InstanceAssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

DescribeInstanceInformationPaginateResponseInstanceInformationListTypeDef = TypedDict(
    "DescribeInstanceInformationPaginateResponseInstanceInformationListTypeDef",
    {
        "InstanceId": str,
        "PingStatus": Literal["Online", "ConnectionLost", "Inactive"],
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": Literal["Windows", "Linux"],
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": Literal["ManagedInstance", "Document", "EC2Instance"],
        "Name": str,
        "IPAddress": str,
        "ComputerName": str,
        "AssociationStatus": str,
        "LastAssociationExecutionDate": datetime,
        "LastSuccessfulAssociationExecutionDate": datetime,
        "AssociationOverview": DescribeInstanceInformationPaginateResponseInstanceInformationListAssociationOverviewTypeDef,
    },
    total=False,
)

DescribeInstanceInformationPaginateResponseTypeDef = TypedDict(
    "DescribeInstanceInformationPaginateResponseTypeDef",
    {
        "InstanceInformationList": List[
            DescribeInstanceInformationPaginateResponseInstanceInformationListTypeDef
        ]
    },
    total=False,
)

_RequiredDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef", {"Key": str}
)
_OptionalDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef",
    {"Values": List[str], "Type": Literal["Equal", "NotEqual", "LessThan", "GreaterThan"]},
    total=False,
)


class DescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef(
    _RequiredDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef,
    _OptionalDescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef,
):
    pass


DescribeInstancePatchStatesForPatchGroupPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeInstancePatchStatesForPatchGroupPaginateResponseInstancePatchStatesTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupPaginateResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)

DescribeInstancePatchStatesForPatchGroupPaginateResponseTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupPaginateResponseTypeDef",
    {
        "InstancePatchStates": List[
            DescribeInstancePatchStatesForPatchGroupPaginateResponseInstancePatchStatesTypeDef
        ]
    },
    total=False,
)

DescribeInstancePatchStatesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeInstancePatchStatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeInstancePatchStatesPaginateResponseInstancePatchStatesTypeDef = TypedDict(
    "DescribeInstancePatchStatesPaginateResponseInstancePatchStatesTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)

DescribeInstancePatchStatesPaginateResponseTypeDef = TypedDict(
    "DescribeInstancePatchStatesPaginateResponseTypeDef",
    {
        "InstancePatchStates": List[
            DescribeInstancePatchStatesPaginateResponseInstancePatchStatesTypeDef
        ]
    },
    total=False,
)

DescribeInstancePatchesPaginateFiltersTypeDef = TypedDict(
    "DescribeInstancePatchesPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

DescribeInstancePatchesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeInstancePatchesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeInstancePatchesPaginateResponsePatchesTypeDef = TypedDict(
    "DescribeInstancePatchesPaginateResponsePatchesTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": Literal[
            "INSTALLED",
            "INSTALLED_OTHER",
            "INSTALLED_PENDING_REBOOT",
            "INSTALLED_REJECTED",
            "MISSING",
            "NOT_APPLICABLE",
            "FAILED",
        ],
        "InstalledTime": datetime,
    },
    total=False,
)

DescribeInstancePatchesPaginateResponseTypeDef = TypedDict(
    "DescribeInstancePatchesPaginateResponseTypeDef",
    {"Patches": List[DescribeInstancePatchesPaginateResponsePatchesTypeDef]},
    total=False,
)

DescribeInventoryDeletionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeInventoryDeletionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef = TypedDict(
    "DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)

DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummaryTypeDef = TypedDict(
    "DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List[
            DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummarySummaryItemsTypeDef
        ],
    },
    total=False,
)

DescribeInventoryDeletionsPaginateResponseInventoryDeletionsTypeDef = TypedDict(
    "DescribeInventoryDeletionsPaginateResponseInventoryDeletionsTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": Literal["InProgress", "Complete"],
        "LastStatusMessage": str,
        "DeletionSummary": DescribeInventoryDeletionsPaginateResponseInventoryDeletionsDeletionSummaryTypeDef,
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)

DescribeInventoryDeletionsPaginateResponseTypeDef = TypedDict(
    "DescribeInventoryDeletionsPaginateResponseTypeDef",
    {
        "InventoryDeletions": List[
            DescribeInventoryDeletionsPaginateResponseInventoryDeletionsTypeDef
        ]
    },
    total=False,
)

DescribeMaintenanceWindowExecutionTaskInvocationsPaginateFiltersTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowExecutionTaskInvocationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseWindowExecutionTaskInvocationIdentitiesTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseWindowExecutionTaskInvocationIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseWindowExecutionTaskInvocationIdentitiesTypeDef
        ]
    },
    total=False,
)

DescribeMaintenanceWindowExecutionTasksPaginateFiltersTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowExecutionTasksPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMaintenanceWindowExecutionTasksPaginateResponseWindowExecutionTaskIdentitiesTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksPaginateResponseWindowExecutionTaskIdentitiesTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
    },
    total=False,
)

DescribeMaintenanceWindowExecutionTasksPaginateResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksPaginateResponseTypeDef",
    {
        "WindowExecutionTaskIdentities": List[
            DescribeMaintenanceWindowExecutionTasksPaginateResponseWindowExecutionTaskIdentitiesTypeDef
        ]
    },
    total=False,
)

DescribeMaintenanceWindowExecutionsPaginateFiltersTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMaintenanceWindowExecutionsPaginateResponseWindowExecutionsTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsPaginateResponseWindowExecutionsTypeDef",
    {
        "WindowId": str,
        "WindowExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

DescribeMaintenanceWindowExecutionsPaginateResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsPaginateResponseTypeDef",
    {
        "WindowExecutions": List[
            DescribeMaintenanceWindowExecutionsPaginateResponseWindowExecutionsTypeDef
        ]
    },
    total=False,
)

DescribeMaintenanceWindowSchedulePaginateFiltersTypeDef = TypedDict(
    "DescribeMaintenanceWindowSchedulePaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowSchedulePaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMaintenanceWindowSchedulePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMaintenanceWindowSchedulePaginateResponseScheduledWindowExecutionsTypeDef = TypedDict(
    "DescribeMaintenanceWindowSchedulePaginateResponseScheduledWindowExecutionsTypeDef",
    {"WindowId": str, "Name": str, "ExecutionTime": str},
    total=False,
)

DescribeMaintenanceWindowSchedulePaginateResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowSchedulePaginateResponseTypeDef",
    {
        "ScheduledWindowExecutions": List[
            DescribeMaintenanceWindowSchedulePaginateResponseScheduledWindowExecutionsTypeDef
        ]
    },
    total=False,
)

DescribeMaintenanceWindowSchedulePaginateTargetsTypeDef = TypedDict(
    "DescribeMaintenanceWindowSchedulePaginateTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowTargetsPaginateFiltersTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMaintenanceWindowTargetsPaginateResponseTargetsTargetsTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsPaginateResponseTargetsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowTargetsPaginateResponseTargetsTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsPaginateResponseTargetsTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": Literal["INSTANCE", "RESOURCE_GROUP"],
        "Targets": List[DescribeMaintenanceWindowTargetsPaginateResponseTargetsTargetsTypeDef],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

DescribeMaintenanceWindowTargetsPaginateResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsPaginateResponseTypeDef",
    {"Targets": List[DescribeMaintenanceWindowTargetsPaginateResponseTargetsTypeDef]},
    total=False,
)

DescribeMaintenanceWindowTasksPaginateFiltersTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowTasksPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMaintenanceWindowTasksPaginateResponseTasksLoggingInfoTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksPaginateResponseTasksLoggingInfoTypeDef",
    {"S3BucketName": str, "S3KeyPrefix": str, "S3Region": str},
    total=False,
)

DescribeMaintenanceWindowTasksPaginateResponseTasksTargetsTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksPaginateResponseTasksTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowTasksPaginateResponseTasksTaskParametersTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksPaginateResponseTasksTaskParametersTypeDef",
    {"Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowTasksPaginateResponseTasksTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksPaginateResponseTasksTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Targets": List[DescribeMaintenanceWindowTasksPaginateResponseTasksTargetsTypeDef],
        "TaskParameters": Dict[
            str, DescribeMaintenanceWindowTasksPaginateResponseTasksTaskParametersTypeDef
        ],
        "Priority": int,
        "LoggingInfo": DescribeMaintenanceWindowTasksPaginateResponseTasksLoggingInfoTypeDef,
        "ServiceRoleArn": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

DescribeMaintenanceWindowTasksPaginateResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksPaginateResponseTypeDef",
    {"Tasks": List[DescribeMaintenanceWindowTasksPaginateResponseTasksTypeDef]},
    total=False,
)

DescribeMaintenanceWindowsForTargetPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMaintenanceWindowsForTargetPaginateResponseWindowIdentitiesTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetPaginateResponseWindowIdentitiesTypeDef",
    {"WindowId": str, "Name": str},
    total=False,
)

DescribeMaintenanceWindowsForTargetPaginateResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetPaginateResponseTypeDef",
    {
        "WindowIdentities": List[
            DescribeMaintenanceWindowsForTargetPaginateResponseWindowIdentitiesTypeDef
        ]
    },
    total=False,
)

DescribeMaintenanceWindowsForTargetPaginateTargetsTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetPaginateTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowsPaginateFiltersTypeDef = TypedDict(
    "DescribeMaintenanceWindowsPaginateFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

DescribeMaintenanceWindowsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeMaintenanceWindowsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeMaintenanceWindowsPaginateResponseWindowIdentitiesTypeDef = TypedDict(
    "DescribeMaintenanceWindowsPaginateResponseWindowIdentitiesTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "Enabled": bool,
        "Duration": int,
        "Cutoff": int,
        "Schedule": str,
        "ScheduleTimezone": str,
        "EndDate": str,
        "StartDate": str,
        "NextExecutionTime": str,
    },
    total=False,
)

DescribeMaintenanceWindowsPaginateResponseTypeDef = TypedDict(
    "DescribeMaintenanceWindowsPaginateResponseTypeDef",
    {"WindowIdentities": List[DescribeMaintenanceWindowsPaginateResponseWindowIdentitiesTypeDef]},
    total=False,
)

_RequiredDescribeParametersPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeParametersPaginateFiltersTypeDef", {"Key": Literal["Name", "Type", "KeyId"]}
)
_OptionalDescribeParametersPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeParametersPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class DescribeParametersPaginateFiltersTypeDef(
    _RequiredDescribeParametersPaginateFiltersTypeDef,
    _OptionalDescribeParametersPaginateFiltersTypeDef,
):
    pass


DescribeParametersPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeParametersPaginateParameterFiltersTypeDef = TypedDict(
    "DescribeParametersPaginateParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)

DescribeParametersPaginateResponseParametersPoliciesTypeDef = TypedDict(
    "DescribeParametersPaginateResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)

DescribeParametersPaginateResponseParametersTypeDef = TypedDict(
    "DescribeParametersPaginateResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[DescribeParametersPaginateResponseParametersPoliciesTypeDef],
    },
    total=False,
)

DescribeParametersPaginateResponseTypeDef = TypedDict(
    "DescribeParametersPaginateResponseTypeDef",
    {"Parameters": List[DescribeParametersPaginateResponseParametersTypeDef]},
    total=False,
)

DescribePatchBaselinesPaginateFiltersTypeDef = TypedDict(
    "DescribePatchBaselinesPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

DescribePatchBaselinesPaginatePaginationConfigTypeDef = TypedDict(
    "DescribePatchBaselinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribePatchBaselinesPaginateResponseBaselineIdentitiesTypeDef = TypedDict(
    "DescribePatchBaselinesPaginateResponseBaselineIdentitiesTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

DescribePatchBaselinesPaginateResponseTypeDef = TypedDict(
    "DescribePatchBaselinesPaginateResponseTypeDef",
    {"BaselineIdentities": List[DescribePatchBaselinesPaginateResponseBaselineIdentitiesTypeDef]},
    total=False,
)

DescribePatchGroupsPaginateFiltersTypeDef = TypedDict(
    "DescribePatchGroupsPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

DescribePatchGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribePatchGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribePatchGroupsPaginateResponseMappingsBaselineIdentityTypeDef = TypedDict(
    "DescribePatchGroupsPaginateResponseMappingsBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

DescribePatchGroupsPaginateResponseMappingsTypeDef = TypedDict(
    "DescribePatchGroupsPaginateResponseMappingsTypeDef",
    {
        "PatchGroup": str,
        "BaselineIdentity": DescribePatchGroupsPaginateResponseMappingsBaselineIdentityTypeDef,
    },
    total=False,
)

DescribePatchGroupsPaginateResponseTypeDef = TypedDict(
    "DescribePatchGroupsPaginateResponseTypeDef",
    {"Mappings": List[DescribePatchGroupsPaginateResponseMappingsTypeDef]},
    total=False,
)

_RequiredDescribeSessionsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeSessionsPaginateFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Target", "Owner", "Status"]},
)
_OptionalDescribeSessionsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeSessionsPaginateFiltersTypeDef", {"value": str}, total=False
)


class DescribeSessionsPaginateFiltersTypeDef(
    _RequiredDescribeSessionsPaginateFiltersTypeDef, _OptionalDescribeSessionsPaginateFiltersTypeDef
):
    pass


DescribeSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeSessionsPaginateResponseSessionsOutputUrlTypeDef = TypedDict(
    "DescribeSessionsPaginateResponseSessionsOutputUrlTypeDef",
    {"S3OutputUrl": str, "CloudWatchOutputUrl": str},
    total=False,
)

DescribeSessionsPaginateResponseSessionsTypeDef = TypedDict(
    "DescribeSessionsPaginateResponseSessionsTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": Literal[
            "Connected", "Connecting", "Disconnected", "Terminated", "Terminating", "Failed"
        ],
        "StartDate": datetime,
        "EndDate": datetime,
        "DocumentName": str,
        "Owner": str,
        "Details": str,
        "OutputUrl": DescribeSessionsPaginateResponseSessionsOutputUrlTypeDef,
    },
    total=False,
)

DescribeSessionsPaginateResponseTypeDef = TypedDict(
    "DescribeSessionsPaginateResponseTypeDef",
    {"Sessions": List[DescribeSessionsPaginateResponseSessionsTypeDef]},
    total=False,
)

GetInventoryPaginateAggregatorsGroupsFiltersTypeDef = TypedDict(
    "GetInventoryPaginateAggregatorsGroupsFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)

GetInventoryPaginateAggregatorsGroupsTypeDef = TypedDict(
    "GetInventoryPaginateAggregatorsGroupsTypeDef",
    {"Name": str, "Filters": List[GetInventoryPaginateAggregatorsGroupsFiltersTypeDef]},
    total=False,
)

GetInventoryPaginateAggregatorsTypeDef = TypedDict(
    "GetInventoryPaginateAggregatorsTypeDef",
    {
        "Expression": str,
        "Aggregators": Any,
        "Groups": List[GetInventoryPaginateAggregatorsGroupsTypeDef],
    },
    total=False,
)

_RequiredGetInventoryPaginateFiltersTypeDef = TypedDict(
    "_RequiredGetInventoryPaginateFiltersTypeDef", {"Key": str}
)
_OptionalGetInventoryPaginateFiltersTypeDef = TypedDict(
    "_OptionalGetInventoryPaginateFiltersTypeDef",
    {
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"],
    },
    total=False,
)


class GetInventoryPaginateFiltersTypeDef(
    _RequiredGetInventoryPaginateFiltersTypeDef, _OptionalGetInventoryPaginateFiltersTypeDef
):
    pass


GetInventoryPaginatePaginationConfigTypeDef = TypedDict(
    "GetInventoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetInventoryPaginateResponseEntitiesDataTypeDef = TypedDict(
    "GetInventoryPaginateResponseEntitiesDataTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "ContentHash": str,
        "Content": List[Dict[str, str]],
    },
    total=False,
)

GetInventoryPaginateResponseEntitiesTypeDef = TypedDict(
    "GetInventoryPaginateResponseEntitiesTypeDef",
    {"Id": str, "Data": Dict[str, GetInventoryPaginateResponseEntitiesDataTypeDef]},
    total=False,
)

GetInventoryPaginateResponseTypeDef = TypedDict(
    "GetInventoryPaginateResponseTypeDef",
    {"Entities": List[GetInventoryPaginateResponseEntitiesTypeDef]},
    total=False,
)

GetInventoryPaginateResultAttributesTypeDef = TypedDict(
    "GetInventoryPaginateResultAttributesTypeDef", {"TypeName": str}
)

GetInventorySchemaPaginatePaginationConfigTypeDef = TypedDict(
    "GetInventorySchemaPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetInventorySchemaPaginateResponseSchemasAttributesTypeDef = TypedDict(
    "GetInventorySchemaPaginateResponseSchemasAttributesTypeDef",
    {"Name": str, "DataType": Literal["string", "number"]},
    total=False,
)

GetInventorySchemaPaginateResponseSchemasTypeDef = TypedDict(
    "GetInventorySchemaPaginateResponseSchemasTypeDef",
    {
        "TypeName": str,
        "Version": str,
        "Attributes": List[GetInventorySchemaPaginateResponseSchemasAttributesTypeDef],
        "DisplayName": str,
    },
    total=False,
)

GetInventorySchemaPaginateResponseTypeDef = TypedDict(
    "GetInventorySchemaPaginateResponseTypeDef",
    {"Schemas": List[GetInventorySchemaPaginateResponseSchemasTypeDef]},
    total=False,
)

GetParameterHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "GetParameterHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetParameterHistoryPaginateResponseParametersPoliciesTypeDef = TypedDict(
    "GetParameterHistoryPaginateResponseParametersPoliciesTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)

GetParameterHistoryPaginateResponseParametersTypeDef = TypedDict(
    "GetParameterHistoryPaginateResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List[GetParameterHistoryPaginateResponseParametersPoliciesTypeDef],
    },
    total=False,
)

GetParameterHistoryPaginateResponseTypeDef = TypedDict(
    "GetParameterHistoryPaginateResponseTypeDef",
    {"Parameters": List[GetParameterHistoryPaginateResponseParametersTypeDef]},
    total=False,
)

GetParametersByPathPaginatePaginationConfigTypeDef = TypedDict(
    "GetParametersByPathPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetParametersByPathPaginateParameterFiltersTypeDef = TypedDict(
    "GetParametersByPathPaginateParameterFiltersTypeDef",
    {"Key": str, "Option": str, "Values": List[str]},
    total=False,
)

GetParametersByPathPaginateResponseParametersTypeDef = TypedDict(
    "GetParametersByPathPaginateResponseParametersTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
    },
    total=False,
)

GetParametersByPathPaginateResponseTypeDef = TypedDict(
    "GetParametersByPathPaginateResponseTypeDef",
    {"Parameters": List[GetParametersByPathPaginateResponseParametersTypeDef]},
    total=False,
)

ListAssociationVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssociationVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationS3LocationTypeDef = TypedDict(
    "ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationS3LocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationTypeDef = TypedDict(
    "ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationTypeDef",
    {
        "S3Location": ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationS3LocationTypeDef
    },
    total=False,
)

ListAssociationVersionsPaginateResponseAssociationVersionsTargetsTypeDef = TypedDict(
    "ListAssociationVersionsPaginateResponseAssociationVersionsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ListAssociationVersionsPaginateResponseAssociationVersionsTypeDef = TypedDict(
    "ListAssociationVersionsPaginateResponseAssociationVersionsTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "CreatedDate": datetime,
        "Name": str,
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List[ListAssociationVersionsPaginateResponseAssociationVersionsTargetsTypeDef],
        "ScheduleExpression": str,
        "OutputLocation": ListAssociationVersionsPaginateResponseAssociationVersionsOutputLocationTypeDef,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
    },
    total=False,
)

ListAssociationVersionsPaginateResponseTypeDef = TypedDict(
    "ListAssociationVersionsPaginateResponseTypeDef",
    {
        "AssociationVersions": List[
            ListAssociationVersionsPaginateResponseAssociationVersionsTypeDef
        ]
    },
    total=False,
)

_RequiredListAssociationsPaginateAssociationFilterListTypeDef = TypedDict(
    "_RequiredListAssociationsPaginateAssociationFilterListTypeDef",
    {
        "key": Literal[
            "InstanceId",
            "Name",
            "AssociationId",
            "AssociationStatusName",
            "LastExecutedBefore",
            "LastExecutedAfter",
            "AssociationName",
        ]
    },
)
_OptionalListAssociationsPaginateAssociationFilterListTypeDef = TypedDict(
    "_OptionalListAssociationsPaginateAssociationFilterListTypeDef", {"value": str}, total=False
)


class ListAssociationsPaginateAssociationFilterListTypeDef(
    _RequiredListAssociationsPaginateAssociationFilterListTypeDef,
    _OptionalListAssociationsPaginateAssociationFilterListTypeDef,
):
    pass


ListAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAssociationsPaginateResponseAssociationsOverviewTypeDef = TypedDict(
    "ListAssociationsPaginateResponseAssociationsOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

ListAssociationsPaginateResponseAssociationsTargetsTypeDef = TypedDict(
    "ListAssociationsPaginateResponseAssociationsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ListAssociationsPaginateResponseAssociationsTypeDef = TypedDict(
    "ListAssociationsPaginateResponseAssociationsTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
        "DocumentVersion": str,
        "Targets": List[ListAssociationsPaginateResponseAssociationsTargetsTypeDef],
        "LastExecutionDate": datetime,
        "Overview": ListAssociationsPaginateResponseAssociationsOverviewTypeDef,
        "ScheduleExpression": str,
        "AssociationName": str,
    },
    total=False,
)

ListAssociationsPaginateResponseTypeDef = TypedDict(
    "ListAssociationsPaginateResponseTypeDef",
    {"Associations": List[ListAssociationsPaginateResponseAssociationsTypeDef]},
    total=False,
)

_RequiredListCommandInvocationsPaginateFiltersTypeDef = TypedDict(
    "_RequiredListCommandInvocationsPaginateFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalListCommandInvocationsPaginateFiltersTypeDef = TypedDict(
    "_OptionalListCommandInvocationsPaginateFiltersTypeDef", {"value": str}, total=False
)


class ListCommandInvocationsPaginateFiltersTypeDef(
    _RequiredListCommandInvocationsPaginateFiltersTypeDef,
    _OptionalListCommandInvocationsPaginateFiltersTypeDef,
):
    pass


ListCommandInvocationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListCommandInvocationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListCommandInvocationsPaginateResponseCommandInvocationsCloudWatchOutputConfigTypeDef = TypedDict(
    "ListCommandInvocationsPaginateResponseCommandInvocationsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ListCommandInvocationsPaginateResponseCommandInvocationsCommandPluginsTypeDef = TypedDict(
    "ListCommandInvocationsPaginateResponseCommandInvocationsCommandPluginsTypeDef",
    {
        "Name": str,
        "Status": Literal["Pending", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"],
        "StatusDetails": str,
        "ResponseCode": int,
        "ResponseStartDateTime": datetime,
        "ResponseFinishDateTime": datetime,
        "Output": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)

ListCommandInvocationsPaginateResponseCommandInvocationsNotificationConfigTypeDef = TypedDict(
    "ListCommandInvocationsPaginateResponseCommandInvocationsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ListCommandInvocationsPaginateResponseCommandInvocationsTypeDef = TypedDict(
    "ListCommandInvocationsPaginateResponseCommandInvocationsTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "InstanceName": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "TraceOutput": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "CommandPlugins": List[
            ListCommandInvocationsPaginateResponseCommandInvocationsCommandPluginsTypeDef
        ],
        "ServiceRole": str,
        "NotificationConfig": ListCommandInvocationsPaginateResponseCommandInvocationsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ListCommandInvocationsPaginateResponseCommandInvocationsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ListCommandInvocationsPaginateResponseTypeDef = TypedDict(
    "ListCommandInvocationsPaginateResponseTypeDef",
    {"CommandInvocations": List[ListCommandInvocationsPaginateResponseCommandInvocationsTypeDef]},
    total=False,
)

_RequiredListCommandsPaginateFiltersTypeDef = TypedDict(
    "_RequiredListCommandsPaginateFiltersTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"]},
)
_OptionalListCommandsPaginateFiltersTypeDef = TypedDict(
    "_OptionalListCommandsPaginateFiltersTypeDef", {"value": str}, total=False
)


class ListCommandsPaginateFiltersTypeDef(
    _RequiredListCommandsPaginateFiltersTypeDef, _OptionalListCommandsPaginateFiltersTypeDef
):
    pass


ListCommandsPaginatePaginationConfigTypeDef = TypedDict(
    "ListCommandsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListCommandsPaginateResponseCommandsCloudWatchOutputConfigTypeDef = TypedDict(
    "ListCommandsPaginateResponseCommandsCloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

ListCommandsPaginateResponseCommandsNotificationConfigTypeDef = TypedDict(
    "ListCommandsPaginateResponseCommandsNotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

ListCommandsPaginateResponseCommandsTargetsTypeDef = TypedDict(
    "ListCommandsPaginateResponseCommandsTargetsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ListCommandsPaginateResponseCommandsTypeDef = TypedDict(
    "ListCommandsPaginateResponseCommandsTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List[ListCommandsPaginateResponseCommandsTargetsTypeDef],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": ListCommandsPaginateResponseCommandsNotificationConfigTypeDef,
        "CloudWatchOutputConfig": ListCommandsPaginateResponseCommandsCloudWatchOutputConfigTypeDef,
    },
    total=False,
)

ListCommandsPaginateResponseTypeDef = TypedDict(
    "ListCommandsPaginateResponseTypeDef",
    {"Commands": List[ListCommandsPaginateResponseCommandsTypeDef]},
    total=False,
)

ListComplianceItemsPaginateFiltersTypeDef = TypedDict(
    "ListComplianceItemsPaginateFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

ListComplianceItemsPaginatePaginationConfigTypeDef = TypedDict(
    "ListComplianceItemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListComplianceItemsPaginateResponseComplianceItemsExecutionSummaryTypeDef = TypedDict(
    "ListComplianceItemsPaginateResponseComplianceItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)

ListComplianceItemsPaginateResponseComplianceItemsTypeDef = TypedDict(
    "ListComplianceItemsPaginateResponseComplianceItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Id": str,
        "Title": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "ExecutionSummary": ListComplianceItemsPaginateResponseComplianceItemsExecutionSummaryTypeDef,
        "Details": Dict[str, str],
    },
    total=False,
)

ListComplianceItemsPaginateResponseTypeDef = TypedDict(
    "ListComplianceItemsPaginateResponseTypeDef",
    {"ComplianceItems": List[ListComplianceItemsPaginateResponseComplianceItemsTypeDef]},
    total=False,
)

ListComplianceSummariesPaginateFiltersTypeDef = TypedDict(
    "ListComplianceSummariesPaginateFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

ListComplianceSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "ListComplianceSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ListComplianceSummariesPaginateResponseComplianceSummaryItemsTypeDef = TypedDict(
    "ListComplianceSummariesPaginateResponseComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "CompliantSummary": ListComplianceSummariesPaginateResponseComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ListComplianceSummariesPaginateResponseComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)

ListComplianceSummariesPaginateResponseTypeDef = TypedDict(
    "ListComplianceSummariesPaginateResponseTypeDef",
    {
        "ComplianceSummaryItems": List[
            ListComplianceSummariesPaginateResponseComplianceSummaryItemsTypeDef
        ]
    },
    total=False,
)

ListDocumentVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDocumentVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDocumentVersionsPaginateResponseDocumentVersionsTypeDef = TypedDict(
    "ListDocumentVersionsPaginateResponseDocumentVersionsTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": Literal["YAML", "JSON"],
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
    },
    total=False,
)

ListDocumentVersionsPaginateResponseTypeDef = TypedDict(
    "ListDocumentVersionsPaginateResponseTypeDef",
    {"DocumentVersions": List[ListDocumentVersionsPaginateResponseDocumentVersionsTypeDef]},
    total=False,
)

_RequiredListDocumentsPaginateDocumentFilterListTypeDef = TypedDict(
    "_RequiredListDocumentsPaginateDocumentFilterListTypeDef",
    {"key": Literal["Name", "Owner", "PlatformTypes", "DocumentType"]},
)
_OptionalListDocumentsPaginateDocumentFilterListTypeDef = TypedDict(
    "_OptionalListDocumentsPaginateDocumentFilterListTypeDef", {"value": str}, total=False
)


class ListDocumentsPaginateDocumentFilterListTypeDef(
    _RequiredListDocumentsPaginateDocumentFilterListTypeDef,
    _OptionalListDocumentsPaginateDocumentFilterListTypeDef,
):
    pass


ListDocumentsPaginateFiltersTypeDef = TypedDict(
    "ListDocumentsPaginateFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ListDocumentsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDocumentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDocumentsPaginateResponseDocumentIdentifiersRequiresTypeDef = TypedDict(
    "ListDocumentsPaginateResponseDocumentIdentifiersRequiresTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ListDocumentsPaginateResponseDocumentIdentifiersTagsTypeDef = TypedDict(
    "ListDocumentsPaginateResponseDocumentIdentifiersTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ListDocumentsPaginateResponseDocumentIdentifiersTypeDef = TypedDict(
    "ListDocumentsPaginateResponseDocumentIdentifiersTypeDef",
    {
        "Name": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentVersion": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
        ],
        "SchemaVersion": str,
        "DocumentFormat": Literal["YAML", "JSON"],
        "TargetType": str,
        "Tags": List[ListDocumentsPaginateResponseDocumentIdentifiersTagsTypeDef],
        "Requires": List[ListDocumentsPaginateResponseDocumentIdentifiersRequiresTypeDef],
    },
    total=False,
)

ListDocumentsPaginateResponseTypeDef = TypedDict(
    "ListDocumentsPaginateResponseTypeDef",
    {"DocumentIdentifiers": List[ListDocumentsPaginateResponseDocumentIdentifiersTypeDef]},
    total=False,
)

ListResourceComplianceSummariesPaginateFiltersTypeDef = TypedDict(
    "ListResourceComplianceSummariesPaginateFiltersTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

ListResourceComplianceSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "ListResourceComplianceSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef = TypedDict(
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef",
    {
        "CompliantCount": int,
        "SeveritySummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef = TypedDict(
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef",
    {"ExecutionTime": datetime, "ExecutionId": str, "ExecutionType": str},
    total=False,
)

ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef = TypedDict(
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef = TypedDict(
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummarySeveritySummaryTypeDef,
    },
    total=False,
)

ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsTypeDef = TypedDict(
    "ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "OverallSeverity": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ExecutionSummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsExecutionSummaryTypeDef,
        "CompliantSummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsCompliantSummaryTypeDef,
        "NonCompliantSummary": ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsNonCompliantSummaryTypeDef,
    },
    total=False,
)

ListResourceComplianceSummariesPaginateResponseTypeDef = TypedDict(
    "ListResourceComplianceSummariesPaginateResponseTypeDef",
    {
        "ResourceComplianceSummaryItems": List[
            ListResourceComplianceSummariesPaginateResponseResourceComplianceSummaryItemsTypeDef
        ]
    },
    total=False,
)

ListResourceDataSyncPaginatePaginationConfigTypeDef = TypedDict(
    "ListResourceDataSyncPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResourceDataSyncPaginateResponseResourceDataSyncItemsS3DestinationTypeDef = TypedDict(
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsS3DestinationTypeDef",
    {"BucketName": str, "Prefix": str, "SyncFormat": str, "Region": str, "AWSKMSKeyARN": str},
    total=False,
)

ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef = TypedDict(
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef",
    {"OrganizationalUnitId": str},
    total=False,
)

ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef = TypedDict(
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
        "OrganizationalUnits": List[
            ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceOrganizationalUnitsTypeDef
        ],
    },
    total=False,
)

ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceTypeDef = TypedDict(
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceTypeDef",
    {
        "SourceType": str,
        "AwsOrganizationsSource": ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceAwsOrganizationsSourceTypeDef,
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
        "State": str,
    },
    total=False,
)

ListResourceDataSyncPaginateResponseResourceDataSyncItemsTypeDef = TypedDict(
    "ListResourceDataSyncPaginateResponseResourceDataSyncItemsTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": ListResourceDataSyncPaginateResponseResourceDataSyncItemsSyncSourceTypeDef,
        "S3Destination": ListResourceDataSyncPaginateResponseResourceDataSyncItemsS3DestinationTypeDef,
        "LastSyncTime": datetime,
        "LastSuccessfulSyncTime": datetime,
        "SyncLastModifiedTime": datetime,
        "LastStatus": Literal["Successful", "Failed", "InProgress"],
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)

ListResourceDataSyncPaginateResponseTypeDef = TypedDict(
    "ListResourceDataSyncPaginateResponseTypeDef",
    {
        "ResourceDataSyncItems": List[
            ListResourceDataSyncPaginateResponseResourceDataSyncItemsTypeDef
        ]
    },
    total=False,
)
