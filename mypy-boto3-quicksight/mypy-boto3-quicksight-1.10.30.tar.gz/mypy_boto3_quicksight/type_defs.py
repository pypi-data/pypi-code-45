"Main interface for quicksight service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCancelIngestionResponseTypeDef",
    "ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef",
    "ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef",
    "ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef",
    "ClientCreateDashboardDashboardPublishOptionsTypeDef",
    "ClientCreateDashboardParametersDateTimeParametersTypeDef",
    "ClientCreateDashboardParametersDecimalParametersTypeDef",
    "ClientCreateDashboardParametersIntegerParametersTypeDef",
    "ClientCreateDashboardParametersStringParametersTypeDef",
    "ClientCreateDashboardParametersTypeDef",
    "ClientCreateDashboardPermissionsTypeDef",
    "ClientCreateDashboardResponseTypeDef",
    "ClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    "ClientCreateDashboardSourceEntitySourceTemplateTypeDef",
    "ClientCreateDashboardSourceEntityTypeDef",
    "ClientCreateDashboardTagsTypeDef",
    "ClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    "ClientCreateDataSetColumnGroupsTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsTypeDef",
    "ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    "ClientCreateDataSetLogicalTableMapSourceTypeDef",
    "ClientCreateDataSetLogicalTableMapTypeDef",
    "ClientCreateDataSetPermissionsTypeDef",
    "ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    "ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef",
    "ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    "ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef",
    "ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    "ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    "ClientCreateDataSetPhysicalTableMapS3SourceTypeDef",
    "ClientCreateDataSetPhysicalTableMapTypeDef",
    "ClientCreateDataSetResponseTypeDef",
    "ClientCreateDataSetRowLevelPermissionDataSetTypeDef",
    "ClientCreateDataSetTagsTypeDef",
    "ClientCreateDataSourceCredentialsCredentialPairTypeDef",
    "ClientCreateDataSourceCredentialsTypeDef",
    "ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    "ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersTypeDef",
    "ClientCreateDataSourcePermissionsTypeDef",
    "ClientCreateDataSourceResponseTypeDef",
    "ClientCreateDataSourceSslPropertiesTypeDef",
    "ClientCreateDataSourceTagsTypeDef",
    "ClientCreateDataSourceVpcConnectionPropertiesTypeDef",
    "ClientCreateGroupMembershipResponseGroupMemberTypeDef",
    "ClientCreateGroupMembershipResponseTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateIamPolicyAssignmentResponseTypeDef",
    "ClientCreateIngestionResponseTypeDef",
    "ClientCreateTemplateAliasResponseTemplateAliasTypeDef",
    "ClientCreateTemplateAliasResponseTypeDef",
    "ClientCreateTemplatePermissionsTypeDef",
    "ClientCreateTemplateResponseTypeDef",
    "ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef",
    "ClientCreateTemplateSourceEntitySourceAnalysisTypeDef",
    "ClientCreateTemplateSourceEntitySourceTemplateTypeDef",
    "ClientCreateTemplateSourceEntityTypeDef",
    "ClientCreateTemplateTagsTypeDef",
    "ClientDeleteDashboardResponseTypeDef",
    "ClientDeleteDataSetResponseTypeDef",
    "ClientDeleteDataSourceResponseTypeDef",
    "ClientDeleteGroupMembershipResponseTypeDef",
    "ClientDeleteGroupResponseTypeDef",
    "ClientDeleteIamPolicyAssignmentResponseTypeDef",
    "ClientDeleteTemplateAliasResponseTypeDef",
    "ClientDeleteTemplateResponseTypeDef",
    "ClientDeleteUserByPrincipalIdResponseTypeDef",
    "ClientDeleteUserResponseTypeDef",
    "ClientDescribeDashboardPermissionsResponsePermissionsTypeDef",
    "ClientDescribeDashboardPermissionsResponseTypeDef",
    "ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef",
    "ClientDescribeDashboardResponseDashboardVersionTypeDef",
    "ClientDescribeDashboardResponseDashboardTypeDef",
    "ClientDescribeDashboardResponseTypeDef",
    "ClientDescribeDataSetPermissionsResponsePermissionsTypeDef",
    "ClientDescribeDataSetPermissionsResponseTypeDef",
    "ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    "ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef",
    "ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef",
    "ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef",
    "ClientDescribeDataSetResponseDataSetTypeDef",
    "ClientDescribeDataSetResponseTypeDef",
    "ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef",
    "ClientDescribeDataSourcePermissionsResponseTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef",
    "ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef",
    "ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef",
    "ClientDescribeDataSourceResponseDataSourceTypeDef",
    "ClientDescribeDataSourceResponseTypeDef",
    "ClientDescribeGroupResponseGroupTypeDef",
    "ClientDescribeGroupResponseTypeDef",
    "ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef",
    "ClientDescribeIamPolicyAssignmentResponseTypeDef",
    "ClientDescribeIngestionResponseIngestionErrorInfoTypeDef",
    "ClientDescribeIngestionResponseIngestionQueueInfoTypeDef",
    "ClientDescribeIngestionResponseIngestionRowInfoTypeDef",
    "ClientDescribeIngestionResponseIngestionTypeDef",
    "ClientDescribeIngestionResponseTypeDef",
    "ClientDescribeTemplateAliasResponseTemplateAliasTypeDef",
    "ClientDescribeTemplateAliasResponseTypeDef",
    "ClientDescribeTemplatePermissionsResponsePermissionsTypeDef",
    "ClientDescribeTemplatePermissionsResponseTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionTypeDef",
    "ClientDescribeTemplateResponseTemplateTypeDef",
    "ClientDescribeTemplateResponseTypeDef",
    "ClientDescribeUserResponseUserTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientGetDashboardEmbedUrlResponseTypeDef",
    "ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef",
    "ClientListDashboardVersionsResponseTypeDef",
    "ClientListDashboardsResponseDashboardSummaryListTypeDef",
    "ClientListDashboardsResponseTypeDef",
    "ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef",
    "ClientListDataSetsResponseDataSetSummariesTypeDef",
    "ClientListDataSetsResponseTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef",
    "ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef",
    "ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef",
    "ClientListDataSourcesResponseDataSourcesTypeDef",
    "ClientListDataSourcesResponseTypeDef",
    "ClientListGroupMembershipsResponseGroupMemberListTypeDef",
    "ClientListGroupMembershipsResponseTypeDef",
    "ClientListGroupsResponseGroupListTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef",
    "ClientListIamPolicyAssignmentsForUserResponseTypeDef",
    "ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef",
    "ClientListIamPolicyAssignmentsResponseTypeDef",
    "ClientListIngestionsResponseIngestionsErrorInfoTypeDef",
    "ClientListIngestionsResponseIngestionsQueueInfoTypeDef",
    "ClientListIngestionsResponseIngestionsRowInfoTypeDef",
    "ClientListIngestionsResponseIngestionsTypeDef",
    "ClientListIngestionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTemplateAliasesResponseTemplateAliasListTypeDef",
    "ClientListTemplateAliasesResponseTypeDef",
    "ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef",
    "ClientListTemplateVersionsResponseTypeDef",
    "ClientListTemplatesResponseTemplateSummaryListTypeDef",
    "ClientListTemplatesResponseTypeDef",
    "ClientListUserGroupsResponseGroupListTypeDef",
    "ClientListUserGroupsResponseTypeDef",
    "ClientListUsersResponseUserListTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientRegisterUserResponseUserTypeDef",
    "ClientRegisterUserResponseTypeDef",
    "ClientTagResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUntagResourceResponseTypeDef",
    "ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef",
    "ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef",
    "ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef",
    "ClientUpdateDashboardDashboardPublishOptionsTypeDef",
    "ClientUpdateDashboardParametersDateTimeParametersTypeDef",
    "ClientUpdateDashboardParametersDecimalParametersTypeDef",
    "ClientUpdateDashboardParametersIntegerParametersTypeDef",
    "ClientUpdateDashboardParametersStringParametersTypeDef",
    "ClientUpdateDashboardParametersTypeDef",
    "ClientUpdateDashboardPermissionsGrantPermissionsTypeDef",
    "ClientUpdateDashboardPermissionsResponsePermissionsTypeDef",
    "ClientUpdateDashboardPermissionsResponseTypeDef",
    "ClientUpdateDashboardPermissionsRevokePermissionsTypeDef",
    "ClientUpdateDashboardPublishedVersionResponseTypeDef",
    "ClientUpdateDashboardResponseTypeDef",
    "ClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    "ClientUpdateDashboardSourceEntitySourceTemplateTypeDef",
    "ClientUpdateDashboardSourceEntityTypeDef",
    "ClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    "ClientUpdateDataSetColumnGroupsTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef",
    "ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    "ClientUpdateDataSetLogicalTableMapSourceTypeDef",
    "ClientUpdateDataSetLogicalTableMapTypeDef",
    "ClientUpdateDataSetPermissionsGrantPermissionsTypeDef",
    "ClientUpdateDataSetPermissionsResponseTypeDef",
    "ClientUpdateDataSetPermissionsRevokePermissionsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef",
    "ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef",
    "ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef",
    "ClientUpdateDataSetPhysicalTableMapTypeDef",
    "ClientUpdateDataSetResponseTypeDef",
    "ClientUpdateDataSetRowLevelPermissionDataSetTypeDef",
    "ClientUpdateDataSourceCredentialsCredentialPairTypeDef",
    "ClientUpdateDataSourceCredentialsTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    "ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersTypeDef",
    "ClientUpdateDataSourcePermissionsGrantPermissionsTypeDef",
    "ClientUpdateDataSourcePermissionsResponseTypeDef",
    "ClientUpdateDataSourcePermissionsRevokePermissionsTypeDef",
    "ClientUpdateDataSourceResponseTypeDef",
    "ClientUpdateDataSourceSslPropertiesTypeDef",
    "ClientUpdateDataSourceVpcConnectionPropertiesTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ClientUpdateIamPolicyAssignmentResponseTypeDef",
    "ClientUpdateTemplateAliasResponseTemplateAliasTypeDef",
    "ClientUpdateTemplateAliasResponseTypeDef",
    "ClientUpdateTemplatePermissionsGrantPermissionsTypeDef",
    "ClientUpdateTemplatePermissionsResponsePermissionsTypeDef",
    "ClientUpdateTemplatePermissionsResponseTypeDef",
    "ClientUpdateTemplatePermissionsRevokePermissionsTypeDef",
    "ClientUpdateTemplateResponseTypeDef",
    "ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef",
    "ClientUpdateTemplateSourceEntitySourceAnalysisTypeDef",
    "ClientUpdateTemplateSourceEntitySourceTemplateTypeDef",
    "ClientUpdateTemplateSourceEntityTypeDef",
    "ClientUpdateUserResponseUserTypeDef",
    "ClientUpdateUserResponseTypeDef",
)


_ClientCancelIngestionResponseTypeDef = TypedDict(
    "_ClientCancelIngestionResponseTypeDef",
    {"Arn": str, "IngestionId": str, "RequestId": str, "Status": int},
    total=False,
)


class ClientCancelIngestionResponseTypeDef(_ClientCancelIngestionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the data ingestion.
    """


_ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef = TypedDict(
    "_ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef",
    {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef(
    _ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef
):
    """
    - **AdHocFilteringOption** *(dict) --*

      Ad hoc filtering option.
      - **AvailabilityStatus** *(string) --*

        Availability status.
    """


_ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef = TypedDict(
    "_ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef",
    {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef(
    _ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef
):
    pass


_ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef = TypedDict(
    "_ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef",
    {"VisibilityState": Literal["EXPANDED", "COLLAPSED"]},
    total=False,
)


class ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef(
    _ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef
):
    pass


_ClientCreateDashboardDashboardPublishOptionsTypeDef = TypedDict(
    "_ClientCreateDashboardDashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef,
        "ExportToCSVOption": ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef,
        "SheetControlsOption": ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef,
    },
    total=False,
)


class ClientCreateDashboardDashboardPublishOptionsTypeDef(
    _ClientCreateDashboardDashboardPublishOptionsTypeDef
):
    """
    Publishing options when creating dashboard.
    * AvailabilityStatus for AdHocFilteringOption - This can be either ``ENABLED`` or ``DISABLED`` .
    When This is set to set to ``DISABLED`` , QuickSight disables the left filter pane on the
    published dashboard, which can be used for AdHoc filtering. Enabled by default.
    * AvailabilityStatus for ExportToCSVOption - This can be either ``ENABLED`` or ``DISABLED`` .
    The visual option to export data to CSV is disabled when this is set to ``DISABLED`` . Enabled
    by default.
    * VisibilityState for SheetControlsOption - This can be either ``COLLAPSED`` or ``EXPANDED`` .
    The sheet controls pane is collapsed by default when set to true. Collapsed by default.
    - **AdHocFilteringOption** *(dict) --*

      Ad hoc filtering option.
      - **AvailabilityStatus** *(string) --*

        Availability status.
    """


_ClientCreateDashboardParametersDateTimeParametersTypeDef = TypedDict(
    "_ClientCreateDashboardParametersDateTimeParametersTypeDef",
    {"Name": str, "Values": List[datetime]},
    total=False,
)


class ClientCreateDashboardParametersDateTimeParametersTypeDef(
    _ClientCreateDashboardParametersDateTimeParametersTypeDef
):
    pass


_ClientCreateDashboardParametersDecimalParametersTypeDef = TypedDict(
    "_ClientCreateDashboardParametersDecimalParametersTypeDef",
    {"Name": str, "Values": List[float]},
    total=False,
)


class ClientCreateDashboardParametersDecimalParametersTypeDef(
    _ClientCreateDashboardParametersDecimalParametersTypeDef
):
    pass


_ClientCreateDashboardParametersIntegerParametersTypeDef = TypedDict(
    "_ClientCreateDashboardParametersIntegerParametersTypeDef",
    {"Name": str, "Values": List[int]},
    total=False,
)


class ClientCreateDashboardParametersIntegerParametersTypeDef(
    _ClientCreateDashboardParametersIntegerParametersTypeDef
):
    pass


_RequiredClientCreateDashboardParametersStringParametersTypeDef = TypedDict(
    "_RequiredClientCreateDashboardParametersStringParametersTypeDef", {"Name": str}
)
_OptionalClientCreateDashboardParametersStringParametersTypeDef = TypedDict(
    "_OptionalClientCreateDashboardParametersStringParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateDashboardParametersStringParametersTypeDef(
    _RequiredClientCreateDashboardParametersStringParametersTypeDef,
    _OptionalClientCreateDashboardParametersStringParametersTypeDef,
):
    """
    - *(dict) --*

      String parameter.
      - **Name** *(string) --***[REQUIRED]**

        A display name for the dataset.
    """


_ClientCreateDashboardParametersTypeDef = TypedDict(
    "_ClientCreateDashboardParametersTypeDef",
    {
        "StringParameters": List[ClientCreateDashboardParametersStringParametersTypeDef],
        "IntegerParameters": List[ClientCreateDashboardParametersIntegerParametersTypeDef],
        "DecimalParameters": List[ClientCreateDashboardParametersDecimalParametersTypeDef],
        "DateTimeParameters": List[ClientCreateDashboardParametersDateTimeParametersTypeDef],
    },
    total=False,
)


class ClientCreateDashboardParametersTypeDef(_ClientCreateDashboardParametersTypeDef):
    """
    A structure that contains the parameters of the dashboard. These are parameter overrides for a
    dashboard. A dashboard can have any type of parameters and some parameters might accept multiple
    values. You could use the following structure to override two string parameters that accept
    multiple values:
    - **StringParameters** *(list) --*

      String parameters.
      - *(dict) --*

        String parameter.
        - **Name** *(string) --***[REQUIRED]**

          A display name for the dataset.
    """


_RequiredClientCreateDashboardPermissionsTypeDef = TypedDict(
    "_RequiredClientCreateDashboardPermissionsTypeDef", {"Principal": str}
)
_OptionalClientCreateDashboardPermissionsTypeDef = TypedDict(
    "_OptionalClientCreateDashboardPermissionsTypeDef", {"Actions": List[str]}, total=False
)


class ClientCreateDashboardPermissionsTypeDef(
    _RequiredClientCreateDashboardPermissionsTypeDef,
    _OptionalClientCreateDashboardPermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientCreateDashboardResponseTypeDef = TypedDict(
    "_ClientCreateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientCreateDashboardResponseTypeDef(_ClientCreateDashboardResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the dashboard.
    """


_RequiredClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef = TypedDict(
    "_RequiredClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    {"DataSetPlaceholder": str},
)
_OptionalClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef = TypedDict(
    "_OptionalClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    {"DataSetArn": str},
    total=False,
)


class ClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef(
    _RequiredClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef,
    _OptionalClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef,
):
    """
    - *(dict) --*

      Dataset reference.
      - **DataSetPlaceholder** *(string) --***[REQUIRED]**

        Dataset placeholder.
    """


_RequiredClientCreateDashboardSourceEntitySourceTemplateTypeDef = TypedDict(
    "_RequiredClientCreateDashboardSourceEntitySourceTemplateTypeDef",
    {
        "DataSetReferences": List[
            ClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef
        ]
    },
)
_OptionalClientCreateDashboardSourceEntitySourceTemplateTypeDef = TypedDict(
    "_OptionalClientCreateDashboardSourceEntitySourceTemplateTypeDef", {"Arn": str}, total=False
)


class ClientCreateDashboardSourceEntitySourceTemplateTypeDef(
    _RequiredClientCreateDashboardSourceEntitySourceTemplateTypeDef,
    _OptionalClientCreateDashboardSourceEntitySourceTemplateTypeDef,
):
    """
    - **SourceTemplate** *(dict) --*

      Source template.
      - **DataSetReferences** *(list) --***[REQUIRED]**

        Dataset references.
        - *(dict) --*

          Dataset reference.
          - **DataSetPlaceholder** *(string) --***[REQUIRED]**

            Dataset placeholder.
    """


_ClientCreateDashboardSourceEntityTypeDef = TypedDict(
    "_ClientCreateDashboardSourceEntityTypeDef",
    {"SourceTemplate": ClientCreateDashboardSourceEntitySourceTemplateTypeDef},
    total=False,
)


class ClientCreateDashboardSourceEntityTypeDef(_ClientCreateDashboardSourceEntityTypeDef):
    """
    Source entity from which the dashboard is created. The souce entity accepts the Amazon Resource
    Name (ARN) of the source template or analysis and also references the replacement datasets for
    the placeholders set when creating the template. The replacement datasets need to follow the
    same schema as the datasets for which placeholders were created when creating the template.
    If you are creating a dashboard from a source entity in a different AWS account, use the ARN of
    the source template.
    - **SourceTemplate** *(dict) --*

      Source template.
      - **DataSetReferences** *(list) --***[REQUIRED]**

        Dataset references.
        - *(dict) --*

          Dataset reference.
          - **DataSetPlaceholder** *(string) --***[REQUIRED]**

            Dataset placeholder.
    """


_RequiredClientCreateDashboardTagsTypeDef = TypedDict(
    "_RequiredClientCreateDashboardTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDashboardTagsTypeDef = TypedDict(
    "_OptionalClientCreateDashboardTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDashboardTagsTypeDef(
    _RequiredClientCreateDashboardTagsTypeDef, _OptionalClientCreateDashboardTagsTypeDef
):
    """
    - *(dict) --*

      The keys of the key-value pairs for the resource tag or tags assigned to the resource.
      - **Key** *(string) --***[REQUIRED]**

        Tag key.
    """


_RequiredClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "_RequiredClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef", {"Name": str}
)
_OptionalClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "_OptionalClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    {"CountryCode": str, "Columns": List[str]},
    total=False,
)


class ClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef(
    _RequiredClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef,
    _OptionalClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef,
):
    """
    - **GeoSpatialColumnGroup** *(dict) --*

      Geospatial column group that denotes a hierarchy.
      - **Name** *(string) --***[REQUIRED]**

        A display name for the hierarchy.
    """


_ClientCreateDataSetColumnGroupsTypeDef = TypedDict(
    "_ClientCreateDataSetColumnGroupsTypeDef",
    {"GeoSpatialColumnGroup": ClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef},
    total=False,
)


class ClientCreateDataSetColumnGroupsTypeDef(_ClientCreateDataSetColumnGroupsTypeDef):
    """
    - *(dict) --*

      Groupings of columns that work together in certain QuickSight features. This is a variant type
      structure. No more than one of the attributes should be non-null for this structure to be
      valid.
      - **GeoSpatialColumnGroup** *(dict) --*

        Geospatial column group that denotes a hierarchy.
        - **Name** *(string) --***[REQUIRED]**

          A display name for the hierarchy.
    """


_ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"],
        "Format": str,
    },
    total=False,
)


class ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef(
    _ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    {"ColumnName": str, "ColumnId": str, "Expression": str},
    total=False,
)


class ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef(
    _ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    {
        "Columns": List[
            ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef
        ]
    },
    total=False,
)


class ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef(
    _ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    {"ConditionExpression": str},
    total=False,
)


class ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef(
    _ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    {"ProjectedColumns": List[str]},
    total=False,
)


class ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef(
    _ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    {"ColumnName": str, "NewColumnName": str},
    total=False,
)


class ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef(
    _ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    {
        "ColumnGeographicRole": Literal[
            "COUNTRY", "STATE", "COUNTY", "CITY", "POSTCODE", "LONGITUDE", "LATITUDE"
        ]
    },
    total=False,
)


class ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef(
    _ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": List[ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef],
    },
    total=False,
)


class ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef(
    _ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapDataTransformsTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapDataTransformsTypeDef",
    {
        "ProjectOperation": ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef,
        "FilterOperation": ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef,
        "CreateColumnsOperation": ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef,
        "RenameColumnOperation": ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef,
        "CastColumnTypeOperation": ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef,
        "TagColumnOperation": ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef,
    },
    total=False,
)


class ClientCreateDataSetLogicalTableMapDataTransformsTypeDef(
    _ClientCreateDataSetLogicalTableMapDataTransformsTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": Literal["INNER", "OUTER", "LEFT", "RIGHT"],
        "OnClause": str,
    },
    total=False,
)


class ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef(
    _ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapSourceTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapSourceTypeDef",
    {
        "JoinInstruction": ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef,
        "PhysicalTableId": str,
    },
    total=False,
)


class ClientCreateDataSetLogicalTableMapSourceTypeDef(
    _ClientCreateDataSetLogicalTableMapSourceTypeDef
):
    pass


_ClientCreateDataSetLogicalTableMapTypeDef = TypedDict(
    "_ClientCreateDataSetLogicalTableMapTypeDef",
    {
        "Alias": str,
        "DataTransforms": List[ClientCreateDataSetLogicalTableMapDataTransformsTypeDef],
        "Source": ClientCreateDataSetLogicalTableMapSourceTypeDef,
    },
    total=False,
)


class ClientCreateDataSetLogicalTableMapTypeDef(_ClientCreateDataSetLogicalTableMapTypeDef):
    pass


_RequiredClientCreateDataSetPermissionsTypeDef = TypedDict(
    "_RequiredClientCreateDataSetPermissionsTypeDef", {"Principal": str}
)
_OptionalClientCreateDataSetPermissionsTypeDef = TypedDict(
    "_OptionalClientCreateDataSetPermissionsTypeDef", {"Actions": List[str]}, total=False
)


class ClientCreateDataSetPermissionsTypeDef(
    _RequiredClientCreateDataSetPermissionsTypeDef, _OptionalClientCreateDataSetPermissionsTypeDef
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef = TypedDict(
    "_ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)


class ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef(
    _ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef
):
    pass


_ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef = TypedDict(
    "_ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
        "Columns": List[ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef],
    },
    total=False,
)


class ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef(
    _ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef
):
    pass


_ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef = TypedDict(
    "_ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)


class ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef(
    _ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef
):
    pass


_ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef = TypedDict(
    "_ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Schema": str,
        "Name": str,
        "InputColumns": List[ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef],
    },
    total=False,
)


class ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef(
    _ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef
):
    pass


_ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef = TypedDict(
    "_ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)


class ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef(
    _ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef
):
    pass


_ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef = TypedDict(
    "_ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    {
        "Format": Literal["CSV", "TSV", "CLF", "ELF", "XLSX", "JSON"],
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"],
        "Delimiter": str,
    },
    total=False,
)


class ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef(
    _ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef
):
    pass


_ClientCreateDataSetPhysicalTableMapS3SourceTypeDef = TypedDict(
    "_ClientCreateDataSetPhysicalTableMapS3SourceTypeDef",
    {
        "DataSourceArn": str,
        "UploadSettings": ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef,
        "InputColumns": List[ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef],
    },
    total=False,
)


class ClientCreateDataSetPhysicalTableMapS3SourceTypeDef(
    _ClientCreateDataSetPhysicalTableMapS3SourceTypeDef
):
    pass


_ClientCreateDataSetPhysicalTableMapTypeDef = TypedDict(
    "_ClientCreateDataSetPhysicalTableMapTypeDef",
    {
        "RelationalTable": ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef,
        "CustomSql": ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef,
        "S3Source": ClientCreateDataSetPhysicalTableMapS3SourceTypeDef,
    },
    total=False,
)


class ClientCreateDataSetPhysicalTableMapTypeDef(_ClientCreateDataSetPhysicalTableMapTypeDef):
    pass


_ClientCreateDataSetResponseTypeDef = TypedDict(
    "_ClientCreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientCreateDataSetResponseTypeDef(_ClientCreateDataSetResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset.
    """


_RequiredClientCreateDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "_RequiredClientCreateDataSetRowLevelPermissionDataSetTypeDef", {"Arn": str}
)
_OptionalClientCreateDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "_OptionalClientCreateDataSetRowLevelPermissionDataSetTypeDef",
    {"PermissionPolicy": Literal["GRANT_ACCESS", "DENY_ACCESS"]},
    total=False,
)


class ClientCreateDataSetRowLevelPermissionDataSetTypeDef(
    _RequiredClientCreateDataSetRowLevelPermissionDataSetTypeDef,
    _OptionalClientCreateDataSetRowLevelPermissionDataSetTypeDef,
):
    """
    Row-level security configuration on the data you want to create.
    - **Arn** *(string) --***[REQUIRED]**

      The Amazon Resource name (ARN) of the permission dataset.
    """


_RequiredClientCreateDataSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateDataSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDataSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateDataSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDataSetTagsTypeDef(
    _RequiredClientCreateDataSetTagsTypeDef, _OptionalClientCreateDataSetTagsTypeDef
):
    """
    - *(dict) --*

      The keys of the key-value pairs for the resource tag or tags assigned to the resource.
      - **Key** *(string) --***[REQUIRED]**

        Tag key.
    """


_RequiredClientCreateDataSourceCredentialsCredentialPairTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceCredentialsCredentialPairTypeDef", {"Username": str}
)
_OptionalClientCreateDataSourceCredentialsCredentialPairTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceCredentialsCredentialPairTypeDef",
    {"Password": str},
    total=False,
)


class ClientCreateDataSourceCredentialsCredentialPairTypeDef(
    _RequiredClientCreateDataSourceCredentialsCredentialPairTypeDef,
    _OptionalClientCreateDataSourceCredentialsCredentialPairTypeDef,
):
    """
    - **CredentialPair** *(dict) --*

      Credential pair.
      - **Username** *(string) --***[REQUIRED]**

        Username.
    """


_ClientCreateDataSourceCredentialsTypeDef = TypedDict(
    "_ClientCreateDataSourceCredentialsTypeDef",
    {"CredentialPair": ClientCreateDataSourceCredentialsCredentialPairTypeDef},
    total=False,
)


class ClientCreateDataSourceCredentialsTypeDef(_ClientCreateDataSourceCredentialsTypeDef):
    """
    The credentials QuickSight that uses to connect to your underlying source. Currently, only
    credentials based on user name and password are supported.
    - **CredentialPair** *(dict) --*

      Credential pair.
      - **Username** *(string) --***[REQUIRED]**

        Username.
    """


_ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    {"Domain": str},
)


class ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef
):
    """
    - **AmazonElasticsearchParameters** *(dict) --*

      Amazon Elasticsearch parameters.
      - **Domain** *(string) --***[REQUIRED]**

        The Amazon Elasticsearch Service domain.
    """


_ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef",
    {"WorkGroup": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    {"DataSetName": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef",
    {"Host": str, "Port": int, "Catalog": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef",
    {"InstanceId": str, "Database": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef",
    {"Host": str, "Port": int, "Database": str, "ClusterId": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef(
    _ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef",
    {
        "ManifestFileLocation": ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef
    },
    total=False,
)


class ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    {"Host": str, "Database": str, "Warehouse": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef",
    {"Host": str, "Port": int},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef",
    {"Query": str, "MaxRows": int},
    total=False,
)


class ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef
):
    pass


_ClientCreateDataSourceDataSourceParametersTypeDef = TypedDict(
    "_ClientCreateDataSourceDataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef,
        "AthenaParameters": ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef,
        "AuroraParameters": ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef,
        "AuroraPostgreSqlParameters": ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef,
        "AwsIotAnalyticsParameters": ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef,
        "JiraParameters": ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef,
        "MariaDbParameters": ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef,
        "MySqlParameters": ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef,
        "PostgreSqlParameters": ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef,
        "PrestoParameters": ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef,
        "RdsParameters": ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef,
        "RedshiftParameters": ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef,
        "S3Parameters": ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef,
        "ServiceNowParameters": ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef,
        "SnowflakeParameters": ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef,
        "SparkParameters": ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef,
        "SqlServerParameters": ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef,
        "TeradataParameters": ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef,
        "TwitterParameters": ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef,
    },
    total=False,
)


class ClientCreateDataSourceDataSourceParametersTypeDef(
    _ClientCreateDataSourceDataSourceParametersTypeDef
):
    """
    The parameters that QuickSight uses to connect to your underlying source.
    - **AmazonElasticsearchParameters** *(dict) --*

      Amazon Elasticsearch parameters.
      - **Domain** *(string) --***[REQUIRED]**

        The Amazon Elasticsearch Service domain.
    """


_RequiredClientCreateDataSourcePermissionsTypeDef = TypedDict(
    "_RequiredClientCreateDataSourcePermissionsTypeDef", {"Principal": str}
)
_OptionalClientCreateDataSourcePermissionsTypeDef = TypedDict(
    "_OptionalClientCreateDataSourcePermissionsTypeDef", {"Actions": List[str]}, total=False
)


class ClientCreateDataSourcePermissionsTypeDef(
    _RequiredClientCreateDataSourcePermissionsTypeDef,
    _OptionalClientCreateDataSourcePermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientCreateDataSourceResponseTypeDef = TypedDict(
    "_ClientCreateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientCreateDataSourceResponseTypeDef(_ClientCreateDataSourceResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the data source.
    """


_ClientCreateDataSourceSslPropertiesTypeDef = TypedDict(
    "_ClientCreateDataSourceSslPropertiesTypeDef", {"DisableSsl": bool}, total=False
)


class ClientCreateDataSourceSslPropertiesTypeDef(_ClientCreateDataSourceSslPropertiesTypeDef):
    """
    Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying
    source.
    - **DisableSsl** *(boolean) --*

      A boolean flag to control whether SSL should be disabled.
    """


_RequiredClientCreateDataSourceTagsTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDataSourceTagsTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDataSourceTagsTypeDef(
    _RequiredClientCreateDataSourceTagsTypeDef, _OptionalClientCreateDataSourceTagsTypeDef
):
    """
    - *(dict) --*

      The keys of the key-value pairs for the resource tag or tags assigned to the resource.
      - **Key** *(string) --***[REQUIRED]**

        Tag key.
    """


_ClientCreateDataSourceVpcConnectionPropertiesTypeDef = TypedDict(
    "_ClientCreateDataSourceVpcConnectionPropertiesTypeDef", {"VpcConnectionArn": str}
)


class ClientCreateDataSourceVpcConnectionPropertiesTypeDef(
    _ClientCreateDataSourceVpcConnectionPropertiesTypeDef
):
    """
    Use this parameter only when you want QuickSight to use a VPC connection when connecting to your
    underlying source.
    - **VpcConnectionArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) for the VPC connection.
    """


_ClientCreateGroupMembershipResponseGroupMemberTypeDef = TypedDict(
    "_ClientCreateGroupMembershipResponseGroupMemberTypeDef",
    {"Arn": str, "MemberName": str},
    total=False,
)


class ClientCreateGroupMembershipResponseGroupMemberTypeDef(
    _ClientCreateGroupMembershipResponseGroupMemberTypeDef
):
    """
    - **GroupMember** *(dict) --*

      The group member.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the group member (user).
    """


_ClientCreateGroupMembershipResponseTypeDef = TypedDict(
    "_ClientCreateGroupMembershipResponseTypeDef",
    {
        "GroupMember": ClientCreateGroupMembershipResponseGroupMemberTypeDef,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientCreateGroupMembershipResponseTypeDef(_ClientCreateGroupMembershipResponseTypeDef):
    """
    - *(dict) --*

      - **GroupMember** *(dict) --*

        The group member.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) for the group member (user).
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The name of the group.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the group.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    - *(dict) --*

      The response object for this operation.
      - **Group** *(dict) --*

        The name of the group.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) for the group.
    """


_ClientCreateIamPolicyAssignmentResponseTypeDef = TypedDict(
    "_ClientCreateIamPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"],
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientCreateIamPolicyAssignmentResponseTypeDef(
    _ClientCreateIamPolicyAssignmentResponseTypeDef
):
    """
    - *(dict) --*

      - **AssignmentName** *(string) --*

        The name of the assignment. Must be unique within an AWS account.
    """


_ClientCreateIngestionResponseTypeDef = TypedDict(
    "_ClientCreateIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": Literal[
            "INITIALIZED", "QUEUED", "RUNNING", "FAILED", "COMPLETED", "CANCELLED"
        ],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientCreateIngestionResponseTypeDef(_ClientCreateIngestionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the data ingestion.
    """


_ClientCreateTemplateAliasResponseTemplateAliasTypeDef = TypedDict(
    "_ClientCreateTemplateAliasResponseTemplateAliasTypeDef",
    {"AliasName": str, "Arn": str, "TemplateVersionNumber": int},
    total=False,
)


class ClientCreateTemplateAliasResponseTemplateAliasTypeDef(
    _ClientCreateTemplateAliasResponseTemplateAliasTypeDef
):
    """
    - **TemplateAlias** *(dict) --*

      Information on the template alias.
      - **AliasName** *(string) --*

        The display name of the template alias.
    """


_ClientCreateTemplateAliasResponseTypeDef = TypedDict(
    "_ClientCreateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": ClientCreateTemplateAliasResponseTemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientCreateTemplateAliasResponseTypeDef(_ClientCreateTemplateAliasResponseTypeDef):
    """
    - *(dict) --*

      - **TemplateAlias** *(dict) --*

        Information on the template alias.
        - **AliasName** *(string) --*

          The display name of the template alias.
    """


_RequiredClientCreateTemplatePermissionsTypeDef = TypedDict(
    "_RequiredClientCreateTemplatePermissionsTypeDef", {"Principal": str}
)
_OptionalClientCreateTemplatePermissionsTypeDef = TypedDict(
    "_OptionalClientCreateTemplatePermissionsTypeDef", {"Actions": List[str]}, total=False
)


class ClientCreateTemplatePermissionsTypeDef(
    _RequiredClientCreateTemplatePermissionsTypeDef, _OptionalClientCreateTemplatePermissionsTypeDef
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientCreateTemplateResponseTypeDef = TypedDict(
    "_ClientCreateTemplateResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "TemplateId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientCreateTemplateResponseTypeDef(_ClientCreateTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the template.
    """


_ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef = TypedDict(
    "_ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef",
    {"DataSetPlaceholder": str, "DataSetArn": str},
    total=False,
)


class ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef(
    _ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef
):
    pass


_RequiredClientCreateTemplateSourceEntitySourceAnalysisTypeDef = TypedDict(
    "_RequiredClientCreateTemplateSourceEntitySourceAnalysisTypeDef", {"Arn": str}
)
_OptionalClientCreateTemplateSourceEntitySourceAnalysisTypeDef = TypedDict(
    "_OptionalClientCreateTemplateSourceEntitySourceAnalysisTypeDef",
    {
        "DataSetReferences": List[
            ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef
        ]
    },
    total=False,
)


class ClientCreateTemplateSourceEntitySourceAnalysisTypeDef(
    _RequiredClientCreateTemplateSourceEntitySourceAnalysisTypeDef,
    _OptionalClientCreateTemplateSourceEntitySourceAnalysisTypeDef,
):
    """
    - **SourceAnalysis** *(dict) --*

      The source analysis, if it is based on an analysis.
      - **Arn** *(string) --***[REQUIRED]**

        The Amazon Resource name (ARN) of the resource.
    """


_ClientCreateTemplateSourceEntitySourceTemplateTypeDef = TypedDict(
    "_ClientCreateTemplateSourceEntitySourceTemplateTypeDef", {"Arn": str}, total=False
)


class ClientCreateTemplateSourceEntitySourceTemplateTypeDef(
    _ClientCreateTemplateSourceEntitySourceTemplateTypeDef
):
    pass


_ClientCreateTemplateSourceEntityTypeDef = TypedDict(
    "_ClientCreateTemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": ClientCreateTemplateSourceEntitySourceAnalysisTypeDef,
        "SourceTemplate": ClientCreateTemplateSourceEntitySourceTemplateTypeDef,
    },
    total=False,
)


class ClientCreateTemplateSourceEntityTypeDef(_ClientCreateTemplateSourceEntityTypeDef):
    """
    The Amazon Resource Name (ARN) of the source entity from which this template is being created.
    Templates can be currently created from an analysis or another template. If the ARN is for an
    analysis, you must include its dataset references.
    - **SourceAnalysis** *(dict) --*

      The source analysis, if it is based on an analysis.
      - **Arn** *(string) --***[REQUIRED]**

        The Amazon Resource name (ARN) of the resource.
    """


_RequiredClientCreateTemplateTagsTypeDef = TypedDict(
    "_RequiredClientCreateTemplateTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTemplateTagsTypeDef = TypedDict(
    "_OptionalClientCreateTemplateTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTemplateTagsTypeDef(
    _RequiredClientCreateTemplateTagsTypeDef, _OptionalClientCreateTemplateTagsTypeDef
):
    """
    - *(dict) --*

      The keys of the key-value pairs for the resource tag or tags assigned to the resource.
      - **Key** *(string) --***[REQUIRED]**

        Tag key.
    """


_ClientDeleteDashboardResponseTypeDef = TypedDict(
    "_ClientDeleteDashboardResponseTypeDef",
    {"Status": int, "Arn": str, "DashboardId": str, "RequestId": str},
    total=False,
)


class ClientDeleteDashboardResponseTypeDef(_ClientDeleteDashboardResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(integer) --*

        The HTTP status of the request.
    """


_ClientDeleteDataSetResponseTypeDef = TypedDict(
    "_ClientDeleteDataSetResponseTypeDef",
    {"Arn": str, "DataSetId": str, "RequestId": str, "Status": int},
    total=False,
)


class ClientDeleteDataSetResponseTypeDef(_ClientDeleteDataSetResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset.
    """


_ClientDeleteDataSourceResponseTypeDef = TypedDict(
    "_ClientDeleteDataSourceResponseTypeDef",
    {"Arn": str, "DataSourceId": str, "RequestId": str, "Status": int},
    total=False,
)


class ClientDeleteDataSourceResponseTypeDef(_ClientDeleteDataSourceResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the data source that you deleted.
    """


_ClientDeleteGroupMembershipResponseTypeDef = TypedDict(
    "_ClientDeleteGroupMembershipResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)


class ClientDeleteGroupMembershipResponseTypeDef(_ClientDeleteGroupMembershipResponseTypeDef):
    """
    - *(dict) --*

      - **RequestId** *(string) --*

        The AWS request ID for this operation.
    """


_ClientDeleteGroupResponseTypeDef = TypedDict(
    "_ClientDeleteGroupResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)


class ClientDeleteGroupResponseTypeDef(_ClientDeleteGroupResponseTypeDef):
    """
    - *(dict) --*

      - **RequestId** *(string) --*

        The AWS request ID for this operation.
    """


_ClientDeleteIamPolicyAssignmentResponseTypeDef = TypedDict(
    "_ClientDeleteIamPolicyAssignmentResponseTypeDef",
    {"AssignmentName": str, "RequestId": str, "Status": int},
    total=False,
)


class ClientDeleteIamPolicyAssignmentResponseTypeDef(
    _ClientDeleteIamPolicyAssignmentResponseTypeDef
):
    """
    - *(dict) --*

      - **AssignmentName** *(string) --*

        The name of the assignment.
    """


_ClientDeleteTemplateAliasResponseTypeDef = TypedDict(
    "_ClientDeleteTemplateAliasResponseTypeDef",
    {"Status": int, "TemplateId": str, "AliasName": str, "Arn": str, "RequestId": str},
    total=False,
)


class ClientDeleteTemplateAliasResponseTypeDef(_ClientDeleteTemplateAliasResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(integer) --*

        The HTTP status of the request.
    """


_ClientDeleteTemplateResponseTypeDef = TypedDict(
    "_ClientDeleteTemplateResponseTypeDef",
    {"RequestId": str, "Arn": str, "TemplateId": str, "Status": int},
    total=False,
)


class ClientDeleteTemplateResponseTypeDef(_ClientDeleteTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **RequestId** *(string) --*

        The AWS request ID for this operation.
    """


_ClientDeleteUserByPrincipalIdResponseTypeDef = TypedDict(
    "_ClientDeleteUserByPrincipalIdResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)


class ClientDeleteUserByPrincipalIdResponseTypeDef(_ClientDeleteUserByPrincipalIdResponseTypeDef):
    """
    - *(dict) --*

      - **RequestId** *(string) --*

        The AWS request ID for this operation.
    """


_ClientDeleteUserResponseTypeDef = TypedDict(
    "_ClientDeleteUserResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)


class ClientDeleteUserResponseTypeDef(_ClientDeleteUserResponseTypeDef):
    """
    - *(dict) --*

      - **RequestId** *(string) --*

        The AWS request ID for this operation.
    """


_ClientDescribeDashboardPermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientDescribeDashboardPermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)


class ClientDescribeDashboardPermissionsResponsePermissionsTypeDef(
    _ClientDescribeDashboardPermissionsResponsePermissionsTypeDef
):
    pass


_ClientDescribeDashboardPermissionsResponseTypeDef = TypedDict(
    "_ClientDescribeDashboardPermissionsResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Permissions": List[ClientDescribeDashboardPermissionsResponsePermissionsTypeDef],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientDescribeDashboardPermissionsResponseTypeDef(
    _ClientDescribeDashboardPermissionsResponseTypeDef
):
    """
    - *(dict) --*

      - **DashboardId** *(string) --*

        The ID for the dashboard.
    """


_ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef = TypedDict(
    "_ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef",
    {
        "Type": Literal[
            "DATA_SET_NOT_FOUND",
            "INTERNAL_FAILURE",
            "PARAMETER_VALUE_INCOMPATIBLE",
            "PARAMETER_TYPE_INVALID",
            "PARAMETER_NOT_FOUND",
            "COLUMN_TYPE_MISMATCH",
            "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
            "COLUMN_REPLACEMENT_MISSING",
        ],
        "Message": str,
    },
    total=False,
)


class ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef(
    _ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef
):
    pass


_ClientDescribeDashboardResponseDashboardVersionTypeDef = TypedDict(
    "_ClientDescribeDashboardResponseDashboardVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List[ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef],
        "VersionNumber": int,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Arn": str,
        "SourceEntityArn": str,
        "Description": str,
    },
    total=False,
)


class ClientDescribeDashboardResponseDashboardVersionTypeDef(
    _ClientDescribeDashboardResponseDashboardVersionTypeDef
):
    pass


_ClientDescribeDashboardResponseDashboardTypeDef = TypedDict(
    "_ClientDescribeDashboardResponseDashboardTypeDef",
    {
        "DashboardId": str,
        "Arn": str,
        "Name": str,
        "Version": ClientDescribeDashboardResponseDashboardVersionTypeDef,
        "CreatedTime": datetime,
        "LastPublishedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeDashboardResponseDashboardTypeDef(
    _ClientDescribeDashboardResponseDashboardTypeDef
):
    """
    - **Dashboard** *(dict) --*

      Information about the dashboard.
      - **DashboardId** *(string) --*

        Dashboard ID.
    """


_ClientDescribeDashboardResponseTypeDef = TypedDict(
    "_ClientDescribeDashboardResponseTypeDef",
    {"Dashboard": ClientDescribeDashboardResponseDashboardTypeDef, "Status": int, "RequestId": str},
    total=False,
)


class ClientDescribeDashboardResponseTypeDef(_ClientDescribeDashboardResponseTypeDef):
    """
    - *(dict) --*

      - **Dashboard** *(dict) --*

        Information about the dashboard.
        - **DashboardId** *(string) --*

          Dashboard ID.
    """


_ClientDescribeDataSetPermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientDescribeDataSetPermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)


class ClientDescribeDataSetPermissionsResponsePermissionsTypeDef(
    _ClientDescribeDataSetPermissionsResponsePermissionsTypeDef
):
    pass


_ClientDescribeDataSetPermissionsResponseTypeDef = TypedDict(
    "_ClientDescribeDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "Permissions": List[ClientDescribeDataSetPermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientDescribeDataSetPermissionsResponseTypeDef(
    _ClientDescribeDataSetPermissionsResponseTypeDef
):
    """
    - *(dict) --*

      - **DataSetArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset.
    """


_ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    {"Name": str, "CountryCode": str, "Columns": List[str]},
    total=False,
)


class ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef(
    _ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef",
    {
        "GeoSpatialColumnGroup": ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef(
    _ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"],
        "Format": str,
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    {"ColumnName": str, "ColumnId": str, "Expression": str},
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    {
        "Columns": List[
            ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    {"ConditionExpression": str},
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    {"ProjectedColumns": List[str]},
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    {"ColumnName": str, "NewColumnName": str},
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    {
        "ColumnGeographicRole": Literal[
            "COUNTRY", "STATE", "COUNTY", "CITY", "POSTCODE", "LONGITUDE", "LATITUDE"
        ]
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": List[
            ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef",
    {
        "ProjectOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef,
        "FilterOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef,
        "CreateColumnsOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef,
        "RenameColumnOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef,
        "CastColumnTypeOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef,
        "TagColumnOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef,
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": Literal["INNER", "OUTER", "LEFT", "RIGHT"],
        "OnClause": str,
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef",
    {
        "JoinInstruction": ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef,
        "PhysicalTableId": str,
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef",
    {
        "Alias": str,
        "DataTransforms": List[
            ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef
        ],
        "Source": ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef,
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef(
    _ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef",
    {"Name": str, "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"]},
    total=False,
)


class ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef(
    _ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef(
    _ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
        "Columns": List[
            ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef(
    _ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef(
    _ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Schema": str,
        "Name": str,
        "InputColumns": List[
            ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef(
    _ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef(
    _ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    {
        "Format": Literal["CSV", "TSV", "CLF", "ELF", "XLSX", "JSON"],
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"],
        "Delimiter": str,
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef(
    _ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef",
    {
        "DataSourceArn": str,
        "UploadSettings": ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef,
        "InputColumns": List[
            ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef(
    _ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef",
    {
        "RelationalTable": ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef,
        "CustomSql": ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef,
        "S3Source": ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef,
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef(
    _ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef",
    {"Arn": str, "PermissionPolicy": Literal["GRANT_ACCESS", "DENY_ACCESS"]},
    total=False,
)


class ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef(
    _ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef
):
    pass


_ClientDescribeDataSetResponseDataSetTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseDataSetTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PhysicalTableMap": Dict[str, ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef],
        "LogicalTableMap": Dict[str, ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef],
        "OutputColumns": List[ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef],
        "ImportMode": Literal["SPICE", "DIRECT_QUERY"],
        "ConsumedSpiceCapacityInBytes": int,
        "ColumnGroups": List[ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef],
        "RowLevelPermissionDataSet": ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef,
    },
    total=False,
)


class ClientDescribeDataSetResponseDataSetTypeDef(_ClientDescribeDataSetResponseDataSetTypeDef):
    """
    - **DataSet** *(dict) --*

      Information on the dataset.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) of the resource.
    """


_ClientDescribeDataSetResponseTypeDef = TypedDict(
    "_ClientDescribeDataSetResponseTypeDef",
    {"DataSet": ClientDescribeDataSetResponseDataSetTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientDescribeDataSetResponseTypeDef(_ClientDescribeDataSetResponseTypeDef):
    """
    - *(dict) --*

      - **DataSet** *(dict) --*

        Information on the dataset.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) of the resource.
    """


_ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)


class ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef(
    _ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef
):
    pass


_ClientDescribeDataSourcePermissionsResponseTypeDef = TypedDict(
    "_ClientDescribeDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "Permissions": List[ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientDescribeDataSourcePermissionsResponseTypeDef(
    _ClientDescribeDataSourcePermissionsResponseTypeDef
):
    """
    - *(dict) --*

      - **DataSourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the data source.
    """


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    {"Domain": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef",
    {"WorkGroup": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    {"DataSetName": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef",
    {"Host": str, "Port": int, "Catalog": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef",
    {"InstanceId": str, "Database": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef",
    {"Host": str, "Port": int, "Database": str, "ClusterId": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef",
    {
        "ManifestFileLocation": ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef
    },
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    {"Host": str, "Database": str, "Warehouse": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef",
    {"Host": str, "Port": int},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef",
    {"Query": str, "MaxRows": int},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef,
        "AthenaParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef,
        "AuroraParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef,
        "AuroraPostgreSqlParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef,
        "AwsIotAnalyticsParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef,
        "JiraParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef,
        "MariaDbParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef,
        "MySqlParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef,
        "PostgreSqlParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef,
        "PrestoParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef,
        "RdsParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef,
        "RedshiftParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef,
        "S3Parameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef,
        "ServiceNowParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef,
        "SnowflakeParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef,
        "SparkParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef,
        "SqlServerParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef,
        "TeradataParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef,
        "TwitterParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef,
    },
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef(
    _ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef",
    {
        "Type": Literal[
            "TIMEOUT",
            "ENGINE_VERSION_NOT_SUPPORTED",
            "UNKNOWN_HOST",
            "GENERIC_SQL_FAILURE",
            "CONFLICT",
            "UNKNOWN",
        ],
        "Message": str,
    },
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef(
    _ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef",
    {"DisableSsl": bool},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef(
    _ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef",
    {"VpcConnectionArn": str},
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef(
    _ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef
):
    pass


_ClientDescribeDataSourceResponseDataSourceTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseDataSourceTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": Literal[
            "ADOBE_ANALYTICS",
            "AMAZON_ELASTICSEARCH",
            "ATHENA",
            "AURORA",
            "AURORA_POSTGRESQL",
            "AWS_IOT_ANALYTICS",
            "GITHUB",
            "JIRA",
            "MARIADB",
            "MYSQL",
            "POSTGRESQL",
            "PRESTO",
            "REDSHIFT",
            "S3",
            "SALESFORCE",
            "SERVICENOW",
            "SNOWFLAKE",
            "SPARK",
            "SQLSERVER",
            "TERADATA",
            "TWITTER",
        ],
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "DataSourceParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef,
        "VpcConnectionProperties": ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef,
        "SslProperties": ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef,
        "ErrorInfo": ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef,
    },
    total=False,
)


class ClientDescribeDataSourceResponseDataSourceTypeDef(
    _ClientDescribeDataSourceResponseDataSourceTypeDef
):
    """
    - **DataSource** *(dict) --*

      The information on the data source.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) of the data source.
    """


_ClientDescribeDataSourceResponseTypeDef = TypedDict(
    "_ClientDescribeDataSourceResponseTypeDef",
    {
        "DataSource": ClientDescribeDataSourceResponseDataSourceTypeDef,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientDescribeDataSourceResponseTypeDef(_ClientDescribeDataSourceResponseTypeDef):
    """
    - *(dict) --*

      - **DataSource** *(dict) --*

        The information on the data source.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) of the data source.
    """


_ClientDescribeGroupResponseGroupTypeDef = TypedDict(
    "_ClientDescribeGroupResponseGroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientDescribeGroupResponseGroupTypeDef(_ClientDescribeGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The name of the group.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the group.
    """


_ClientDescribeGroupResponseTypeDef = TypedDict(
    "_ClientDescribeGroupResponseTypeDef",
    {"Group": ClientDescribeGroupResponseGroupTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientDescribeGroupResponseTypeDef(_ClientDescribeGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        The name of the group.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) for the group.
    """


_ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef = TypedDict(
    "_ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentId": str,
        "AssignmentName": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"],
    },
    total=False,
)


class ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef(
    _ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef
):
    """
    - **IAMPolicyAssignment** *(dict) --*

      Information describing the IAM policy assignment.
      - **AwsAccountId** *(string) --*

        AWS account ID.
    """


_ClientDescribeIamPolicyAssignmentResponseTypeDef = TypedDict(
    "_ClientDescribeIamPolicyAssignmentResponseTypeDef",
    {
        "IAMPolicyAssignment": ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientDescribeIamPolicyAssignmentResponseTypeDef(
    _ClientDescribeIamPolicyAssignmentResponseTypeDef
):
    """
    - *(dict) --*

      - **IAMPolicyAssignment** *(dict) --*

        Information describing the IAM policy assignment.
        - **AwsAccountId** *(string) --*

          AWS account ID.
    """


_ClientDescribeIngestionResponseIngestionErrorInfoTypeDef = TypedDict(
    "_ClientDescribeIngestionResponseIngestionErrorInfoTypeDef",
    {
        "Type": Literal[
            "FAILURE_TO_ASSUME_ROLE",
            "INGESTION_SUPERSEDED",
            "INGESTION_CANCELED",
            "DATA_SET_DELETED",
            "DATA_SET_NOT_SPICE",
            "S3_UPLOADED_FILE_DELETED",
            "S3_MANIFEST_ERROR",
            "DATA_TOLERANCE_EXCEPTION",
            "SPICE_TABLE_NOT_FOUND",
            "DATA_SET_SIZE_LIMIT_EXCEEDED",
            "ROW_SIZE_LIMIT_EXCEEDED",
            "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
            "CUSTOMER_ERROR",
            "DATA_SOURCE_NOT_FOUND",
            "IAM_ROLE_NOT_AVAILABLE",
            "CONNECTION_FAILURE",
            "SQL_TABLE_NOT_FOUND",
            "PERMISSION_DENIED",
            "SSL_CERTIFICATE_VALIDATION_FAILURE",
            "OAUTH_TOKEN_FAILURE",
            "SOURCE_API_LIMIT_EXCEEDED_FAILURE",
            "PASSWORD_AUTHENTICATION_FAILURE",
            "SQL_SCHEMA_MISMATCH_ERROR",
            "INVALID_DATE_FORMAT",
            "INVALID_DATAPREP_SYNTAX",
            "SOURCE_RESOURCE_LIMIT_EXCEEDED",
            "SQL_INVALID_PARAMETER_VALUE",
            "QUERY_TIMEOUT",
            "SQL_NUMERIC_OVERFLOW",
            "UNRESOLVABLE_HOST",
            "UNROUTABLE_HOST",
            "SQL_EXCEPTION",
            "S3_FILE_INACCESSIBLE",
            "IOT_FILE_NOT_FOUND",
            "IOT_DATA_SET_FILE_EMPTY",
            "INVALID_DATA_SOURCE_CONFIG",
            "DATA_SOURCE_AUTH_FAILED",
            "DATA_SOURCE_CONNECTION_FAILED",
            "FAILURE_TO_PROCESS_JSON_FILE",
            "INTERNAL_SERVICE_ERROR",
        ],
        "Message": str,
    },
    total=False,
)


class ClientDescribeIngestionResponseIngestionErrorInfoTypeDef(
    _ClientDescribeIngestionResponseIngestionErrorInfoTypeDef
):
    pass


_ClientDescribeIngestionResponseIngestionQueueInfoTypeDef = TypedDict(
    "_ClientDescribeIngestionResponseIngestionQueueInfoTypeDef",
    {"WaitingOnIngestion": str, "QueuedIngestion": str},
    total=False,
)


class ClientDescribeIngestionResponseIngestionQueueInfoTypeDef(
    _ClientDescribeIngestionResponseIngestionQueueInfoTypeDef
):
    pass


_ClientDescribeIngestionResponseIngestionRowInfoTypeDef = TypedDict(
    "_ClientDescribeIngestionResponseIngestionRowInfoTypeDef",
    {"RowsIngested": int, "RowsDropped": int},
    total=False,
)


class ClientDescribeIngestionResponseIngestionRowInfoTypeDef(
    _ClientDescribeIngestionResponseIngestionRowInfoTypeDef
):
    pass


_ClientDescribeIngestionResponseIngestionTypeDef = TypedDict(
    "_ClientDescribeIngestionResponseIngestionTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": Literal[
            "INITIALIZED", "QUEUED", "RUNNING", "FAILED", "COMPLETED", "CANCELLED"
        ],
        "ErrorInfo": ClientDescribeIngestionResponseIngestionErrorInfoTypeDef,
        "RowInfo": ClientDescribeIngestionResponseIngestionRowInfoTypeDef,
        "QueueInfo": ClientDescribeIngestionResponseIngestionQueueInfoTypeDef,
        "CreatedTime": datetime,
        "IngestionTimeInSeconds": int,
        "IngestionSizeInBytes": int,
        "RequestSource": Literal["MANUAL", "SCHEDULED"],
        "RequestType": Literal["INITIAL_INGESTION", "EDIT", "INCREMENTAL_REFRESH", "FULL_REFRESH"],
    },
    total=False,
)


class ClientDescribeIngestionResponseIngestionTypeDef(
    _ClientDescribeIngestionResponseIngestionTypeDef
):
    """
    - **Ingestion** *(dict) --*

      Information about the ingestion.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) of the resource.
    """


_ClientDescribeIngestionResponseTypeDef = TypedDict(
    "_ClientDescribeIngestionResponseTypeDef",
    {"Ingestion": ClientDescribeIngestionResponseIngestionTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientDescribeIngestionResponseTypeDef(_ClientDescribeIngestionResponseTypeDef):
    """
    - *(dict) --*

      - **Ingestion** *(dict) --*

        Information about the ingestion.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) of the resource.
    """


_ClientDescribeTemplateAliasResponseTemplateAliasTypeDef = TypedDict(
    "_ClientDescribeTemplateAliasResponseTemplateAliasTypeDef",
    {"AliasName": str, "Arn": str, "TemplateVersionNumber": int},
    total=False,
)


class ClientDescribeTemplateAliasResponseTemplateAliasTypeDef(
    _ClientDescribeTemplateAliasResponseTemplateAliasTypeDef
):
    """
    - **TemplateAlias** *(dict) --*

      Information about the template alias.
      - **AliasName** *(string) --*

        The display name of the template alias.
    """


_ClientDescribeTemplateAliasResponseTypeDef = TypedDict(
    "_ClientDescribeTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": ClientDescribeTemplateAliasResponseTemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientDescribeTemplateAliasResponseTypeDef(_ClientDescribeTemplateAliasResponseTypeDef):
    """
    - *(dict) --*

      - **TemplateAlias** *(dict) --*

        Information about the template alias.
        - **AliasName** *(string) --*

          The display name of the template alias.
    """


_ClientDescribeTemplatePermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientDescribeTemplatePermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)


class ClientDescribeTemplatePermissionsResponsePermissionsTypeDef(
    _ClientDescribeTemplatePermissionsResponsePermissionsTypeDef
):
    pass


_ClientDescribeTemplatePermissionsResponseTypeDef = TypedDict(
    "_ClientDescribeTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List[ClientDescribeTemplatePermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientDescribeTemplatePermissionsResponseTypeDef(
    _ClientDescribeTemplatePermissionsResponseTypeDef
):
    """
    - *(dict) --*

      - **TemplateId** *(string) --*

        The ID for the template.
    """


_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef = TypedDict(
    "_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef(
    _ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef
):
    pass


_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef = TypedDict(
    "_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef",
    {
        "Name": str,
        "ColumnGroupColumnSchemaList": List[
            ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef(
    _ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef
):
    pass


_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef = TypedDict(
    "_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef",
    {"Name": str, "DataType": str, "GeographicRole": str},
    total=False,
)


class ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef(
    _ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef
):
    pass


_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef = TypedDict(
    "_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef",
    {
        "ColumnSchemaList": List[
            ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef(
    _ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef
):
    pass


_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef = TypedDict(
    "_ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef",
    {
        "Placeholder": str,
        "DataSetSchema": ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef,
        "ColumnGroupSchemaList": List[
            ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef(
    _ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef
):
    pass


_ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef = TypedDict(
    "_ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef",
    {"Type": Literal["DATA_SET_NOT_FOUND", "INTERNAL_FAILURE"], "Message": str},
    total=False,
)


class ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef(
    _ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef
):
    pass


_ClientDescribeTemplateResponseTemplateVersionTypeDef = TypedDict(
    "_ClientDescribeTemplateResponseTemplateVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List[ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef],
        "VersionNumber": int,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "DataSetConfigurations": List[
            ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef
        ],
        "Description": str,
        "SourceEntityArn": str,
    },
    total=False,
)


class ClientDescribeTemplateResponseTemplateVersionTypeDef(
    _ClientDescribeTemplateResponseTemplateVersionTypeDef
):
    pass


_ClientDescribeTemplateResponseTemplateTypeDef = TypedDict(
    "_ClientDescribeTemplateResponseTemplateTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Version": ClientDescribeTemplateResponseTemplateVersionTypeDef,
        "TemplateId": str,
        "LastUpdatedTime": datetime,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientDescribeTemplateResponseTemplateTypeDef(_ClientDescribeTemplateResponseTemplateTypeDef):
    """
    - **Template** *(dict) --*

      The template structure of the object you want to describe.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the template.
    """


_ClientDescribeTemplateResponseTypeDef = TypedDict(
    "_ClientDescribeTemplateResponseTypeDef",
    {"Template": ClientDescribeTemplateResponseTemplateTypeDef, "Status": int},
    total=False,
)


class ClientDescribeTemplateResponseTypeDef(_ClientDescribeTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **Template** *(dict) --*

        The template structure of the object you want to describe.
        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the template.
    """


_ClientDescribeUserResponseUserTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        "IdentityType": Literal["IAM", "QUICKSIGHT"],
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)


class ClientDescribeUserResponseUserTypeDef(_ClientDescribeUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The user name.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the user.
    """


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {"User": ClientDescribeUserResponseUserTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        The user name.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) for the user.
    """


_ClientGetDashboardEmbedUrlResponseTypeDef = TypedDict(
    "_ClientGetDashboardEmbedUrlResponseTypeDef",
    {"EmbedUrl": str, "Status": int, "RequestId": str},
    total=False,
)


class ClientGetDashboardEmbedUrlResponseTypeDef(_ClientGetDashboardEmbedUrlResponseTypeDef):
    """
    - *(dict) --*

      - **EmbedUrl** *(string) --*

        URL that you can put into your server-side webpage to embed your dashboard. This URL is
        valid for 5 minutes, and the resulting session is valid for 10 hours. The API provides the
        URL with an auth_code that enables a single-signon session.
    """


_ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef = TypedDict(
    "_ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "VersionNumber": int,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "SourceEntityArn": str,
        "Description": str,
    },
    total=False,
)


class ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef(
    _ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef
):
    """
    - *(dict) --*

      Dashboard version summary.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) of the resource.
    """


_ClientListDashboardVersionsResponseTypeDef = TypedDict(
    "_ClientListDashboardVersionsResponseTypeDef",
    {
        "DashboardVersionSummaryList": List[
            ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef
        ],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientListDashboardVersionsResponseTypeDef(_ClientListDashboardVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **DashboardVersionSummaryList** *(list) --*

        A structure that contains information about each version of the dashboard.
        - *(dict) --*

          Dashboard version summary.
          - **Arn** *(string) --*

            The Amazon Resource name (ARN) of the resource.
    """


_ClientListDashboardsResponseDashboardSummaryListTypeDef = TypedDict(
    "_ClientListDashboardsResponseDashboardSummaryListTypeDef",
    {
        "Arn": str,
        "DashboardId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PublishedVersionNumber": int,
        "LastPublishedTime": datetime,
    },
    total=False,
)


class ClientListDashboardsResponseDashboardSummaryListTypeDef(
    _ClientListDashboardsResponseDashboardSummaryListTypeDef
):
    """
    - *(dict) --*

      Dashboard summary.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) of the resource.
    """


_ClientListDashboardsResponseTypeDef = TypedDict(
    "_ClientListDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List[ClientListDashboardsResponseDashboardSummaryListTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientListDashboardsResponseTypeDef(_ClientListDashboardsResponseTypeDef):
    """
    - *(dict) --*

      - **DashboardSummaryList** *(list) --*

        A structure that contains all of the dashboards shared with the user. Provides basic
        information about the dashboards.
        - *(dict) --*

          Dashboard summary.
          - **Arn** *(string) --*

            The Amazon Resource name (ARN) of the resource.
    """


_ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef = TypedDict(
    "_ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef",
    {"Arn": str, "PermissionPolicy": Literal["GRANT_ACCESS", "DENY_ACCESS"]},
    total=False,
)


class ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef(
    _ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef
):
    pass


_ClientListDataSetsResponseDataSetSummariesTypeDef = TypedDict(
    "_ClientListDataSetsResponseDataSetSummariesTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "ImportMode": Literal["SPICE", "DIRECT_QUERY"],
        "RowLevelPermissionDataSet": ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef,
    },
    total=False,
)


class ClientListDataSetsResponseDataSetSummariesTypeDef(
    _ClientListDataSetsResponseDataSetSummariesTypeDef
):
    """
    - *(dict) --*

      Dataset summary.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) of the dataset.
    """


_ClientListDataSetsResponseTypeDef = TypedDict(
    "_ClientListDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List[ClientListDataSetsResponseDataSetSummariesTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListDataSetsResponseTypeDef(_ClientListDataSetsResponseTypeDef):
    """
    - *(dict) --*

      - **DataSetSummaries** *(list) --*

        The list of dataset summaries.
        - *(dict) --*

          Dataset summary.
          - **Arn** *(string) --*

            The Amazon Resource name (ARN) of the dataset.
    """


_ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef",
    {"Domain": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef",
    {"WorkGroup": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    {"DataSetName": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef",
    {"Host": str, "Port": int, "Catalog": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef",
    {"InstanceId": str, "Database": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef",
    {"Host": str, "Port": int, "Database": str, "ClusterId": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef",
    {
        "ManifestFileLocation": ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef
    },
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef",
    {"Host": str, "Database": str, "Warehouse": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef",
    {"Host": str, "Port": int},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef",
    {"Query": str, "MaxRows": int},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef,
        "AthenaParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef,
        "AuroraParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef,
        "AuroraPostgreSqlParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef,
        "AwsIotAnalyticsParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef,
        "JiraParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef,
        "MariaDbParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef,
        "MySqlParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef,
        "PostgreSqlParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef,
        "PrestoParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef,
        "RdsParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef,
        "RedshiftParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef,
        "S3Parameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef,
        "ServiceNowParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef,
        "SnowflakeParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef,
        "SparkParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef,
        "SqlServerParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef,
        "TeradataParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef,
        "TwitterParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef,
    },
    total=False,
)


class ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef(
    _ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef",
    {
        "Type": Literal[
            "TIMEOUT",
            "ENGINE_VERSION_NOT_SUPPORTED",
            "UNKNOWN_HOST",
            "GENERIC_SQL_FAILURE",
            "CONFLICT",
            "UNKNOWN",
        ],
        "Message": str,
    },
    total=False,
)


class ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef(
    _ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef",
    {"DisableSsl": bool},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef(
    _ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef",
    {"VpcConnectionArn": str},
    total=False,
)


class ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef(
    _ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef
):
    pass


_ClientListDataSourcesResponseDataSourcesTypeDef = TypedDict(
    "_ClientListDataSourcesResponseDataSourcesTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": Literal[
            "ADOBE_ANALYTICS",
            "AMAZON_ELASTICSEARCH",
            "ATHENA",
            "AURORA",
            "AURORA_POSTGRESQL",
            "AWS_IOT_ANALYTICS",
            "GITHUB",
            "JIRA",
            "MARIADB",
            "MYSQL",
            "POSTGRESQL",
            "PRESTO",
            "REDSHIFT",
            "S3",
            "SALESFORCE",
            "SERVICENOW",
            "SNOWFLAKE",
            "SPARK",
            "SQLSERVER",
            "TERADATA",
            "TWITTER",
        ],
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "DataSourceParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef,
        "VpcConnectionProperties": ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef,
        "SslProperties": ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef,
        "ErrorInfo": ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef,
    },
    total=False,
)


class ClientListDataSourcesResponseDataSourcesTypeDef(
    _ClientListDataSourcesResponseDataSourcesTypeDef
):
    """
    - *(dict) --*

      The structure of a data source.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) of the data source.
    """


_ClientListDataSourcesResponseTypeDef = TypedDict(
    "_ClientListDataSourcesResponseTypeDef",
    {
        "DataSources": List[ClientListDataSourcesResponseDataSourcesTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListDataSourcesResponseTypeDef(_ClientListDataSourcesResponseTypeDef):
    """
    - *(dict) --*

      - **DataSources** *(list) --*

        A list of data sources.
        - *(dict) --*

          The structure of a data source.
          - **Arn** *(string) --*

            The Amazon Resource name (ARN) of the data source.
    """


_ClientListGroupMembershipsResponseGroupMemberListTypeDef = TypedDict(
    "_ClientListGroupMembershipsResponseGroupMemberListTypeDef",
    {"Arn": str, "MemberName": str},
    total=False,
)


class ClientListGroupMembershipsResponseGroupMemberListTypeDef(
    _ClientListGroupMembershipsResponseGroupMemberListTypeDef
):
    """
    - *(dict) --*

      A member of an Amazon QuickSight group. Currently, group members must be users. Groups can't
      be members of another group. .
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the group member (user).
    """


_ClientListGroupMembershipsResponseTypeDef = TypedDict(
    "_ClientListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberList": List[ClientListGroupMembershipsResponseGroupMemberListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListGroupMembershipsResponseTypeDef(_ClientListGroupMembershipsResponseTypeDef):
    """
    - *(dict) --*

      - **GroupMemberList** *(list) --*

        The list of the members of the group.
        - *(dict) --*

          A member of an Amazon QuickSight group. Currently, group members must be users. Groups
          can't be members of another group. .
          - **Arn** *(string) --*

            The Amazon Resource name (ARN) for the group member (user).
    """


_ClientListGroupsResponseGroupListTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupListTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientListGroupsResponseGroupListTypeDef(_ClientListGroupsResponseGroupListTypeDef):
    """
    - *(dict) --*

      A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it
      easier to manage access and security. Currently, an Amazon QuickSight subscription can't
      contain more than 500 Amazon QuickSight groups.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the group.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {
        "GroupList": List[ClientListGroupsResponseGroupListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **GroupList** *(list) --*

        The list of the groups.
        - *(dict) --*

          A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it
          easier to manage access and security. Currently, an Amazon QuickSight subscription can't
          contain more than 500 Amazon QuickSight groups.
          - **Arn** *(string) --*

            The Amazon Resource name (ARN) for the group.
    """


_ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef = TypedDict(
    "_ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef",
    {"AssignmentName": str, "PolicyArn": str},
    total=False,
)


class ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef(
    _ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef
):
    """
    - *(dict) --*

      The active AWS Identity and Access Management (IAM) policy assignment.
      - **AssignmentName** *(string) --*

        A name for the IAM policy assignment.
    """


_ClientListIamPolicyAssignmentsForUserResponseTypeDef = TypedDict(
    "_ClientListIamPolicyAssignmentsForUserResponseTypeDef",
    {
        "ActiveAssignments": List[
            ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef
        ],
        "RequestId": str,
        "NextToken": str,
        "Status": int,
    },
    total=False,
)


class ClientListIamPolicyAssignmentsForUserResponseTypeDef(
    _ClientListIamPolicyAssignmentsForUserResponseTypeDef
):
    """
    - *(dict) --*

      - **ActiveAssignments** *(list) --*

        Active assignments for this user.
        - *(dict) --*

          The active AWS Identity and Access Management (IAM) policy assignment.
          - **AssignmentName** *(string) --*

            A name for the IAM policy assignment.
    """


_ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef = TypedDict(
    "_ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef",
    {"AssignmentName": str, "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"]},
    total=False,
)


class ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef(
    _ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef
):
    """
    - *(dict) --*

      IAM policy assignment Summary.
      - **AssignmentName** *(string) --*

        Assignment name.
    """


_ClientListIamPolicyAssignmentsResponseTypeDef = TypedDict(
    "_ClientListIamPolicyAssignmentsResponseTypeDef",
    {
        "IAMPolicyAssignments": List[
            ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef
        ],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListIamPolicyAssignmentsResponseTypeDef(_ClientListIamPolicyAssignmentsResponseTypeDef):
    """
    - *(dict) --*

      - **IAMPolicyAssignments** *(list) --*

        Information describing the IAM policy assignments.
        - *(dict) --*

          IAM policy assignment Summary.
          - **AssignmentName** *(string) --*

            Assignment name.
    """


_ClientListIngestionsResponseIngestionsErrorInfoTypeDef = TypedDict(
    "_ClientListIngestionsResponseIngestionsErrorInfoTypeDef",
    {
        "Type": Literal[
            "FAILURE_TO_ASSUME_ROLE",
            "INGESTION_SUPERSEDED",
            "INGESTION_CANCELED",
            "DATA_SET_DELETED",
            "DATA_SET_NOT_SPICE",
            "S3_UPLOADED_FILE_DELETED",
            "S3_MANIFEST_ERROR",
            "DATA_TOLERANCE_EXCEPTION",
            "SPICE_TABLE_NOT_FOUND",
            "DATA_SET_SIZE_LIMIT_EXCEEDED",
            "ROW_SIZE_LIMIT_EXCEEDED",
            "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
            "CUSTOMER_ERROR",
            "DATA_SOURCE_NOT_FOUND",
            "IAM_ROLE_NOT_AVAILABLE",
            "CONNECTION_FAILURE",
            "SQL_TABLE_NOT_FOUND",
            "PERMISSION_DENIED",
            "SSL_CERTIFICATE_VALIDATION_FAILURE",
            "OAUTH_TOKEN_FAILURE",
            "SOURCE_API_LIMIT_EXCEEDED_FAILURE",
            "PASSWORD_AUTHENTICATION_FAILURE",
            "SQL_SCHEMA_MISMATCH_ERROR",
            "INVALID_DATE_FORMAT",
            "INVALID_DATAPREP_SYNTAX",
            "SOURCE_RESOURCE_LIMIT_EXCEEDED",
            "SQL_INVALID_PARAMETER_VALUE",
            "QUERY_TIMEOUT",
            "SQL_NUMERIC_OVERFLOW",
            "UNRESOLVABLE_HOST",
            "UNROUTABLE_HOST",
            "SQL_EXCEPTION",
            "S3_FILE_INACCESSIBLE",
            "IOT_FILE_NOT_FOUND",
            "IOT_DATA_SET_FILE_EMPTY",
            "INVALID_DATA_SOURCE_CONFIG",
            "DATA_SOURCE_AUTH_FAILED",
            "DATA_SOURCE_CONNECTION_FAILED",
            "FAILURE_TO_PROCESS_JSON_FILE",
            "INTERNAL_SERVICE_ERROR",
        ],
        "Message": str,
    },
    total=False,
)


class ClientListIngestionsResponseIngestionsErrorInfoTypeDef(
    _ClientListIngestionsResponseIngestionsErrorInfoTypeDef
):
    pass


_ClientListIngestionsResponseIngestionsQueueInfoTypeDef = TypedDict(
    "_ClientListIngestionsResponseIngestionsQueueInfoTypeDef",
    {"WaitingOnIngestion": str, "QueuedIngestion": str},
    total=False,
)


class ClientListIngestionsResponseIngestionsQueueInfoTypeDef(
    _ClientListIngestionsResponseIngestionsQueueInfoTypeDef
):
    pass


_ClientListIngestionsResponseIngestionsRowInfoTypeDef = TypedDict(
    "_ClientListIngestionsResponseIngestionsRowInfoTypeDef",
    {"RowsIngested": int, "RowsDropped": int},
    total=False,
)


class ClientListIngestionsResponseIngestionsRowInfoTypeDef(
    _ClientListIngestionsResponseIngestionsRowInfoTypeDef
):
    pass


_ClientListIngestionsResponseIngestionsTypeDef = TypedDict(
    "_ClientListIngestionsResponseIngestionsTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": Literal[
            "INITIALIZED", "QUEUED", "RUNNING", "FAILED", "COMPLETED", "CANCELLED"
        ],
        "ErrorInfo": ClientListIngestionsResponseIngestionsErrorInfoTypeDef,
        "RowInfo": ClientListIngestionsResponseIngestionsRowInfoTypeDef,
        "QueueInfo": ClientListIngestionsResponseIngestionsQueueInfoTypeDef,
        "CreatedTime": datetime,
        "IngestionTimeInSeconds": int,
        "IngestionSizeInBytes": int,
        "RequestSource": Literal["MANUAL", "SCHEDULED"],
        "RequestType": Literal["INITIAL_INGESTION", "EDIT", "INCREMENTAL_REFRESH", "FULL_REFRESH"],
    },
    total=False,
)


class ClientListIngestionsResponseIngestionsTypeDef(_ClientListIngestionsResponseIngestionsTypeDef):
    """
    - *(dict) --*

      Information on the SPICE ingestion for a dataset.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) of the resource.
    """


_ClientListIngestionsResponseTypeDef = TypedDict(
    "_ClientListIngestionsResponseTypeDef",
    {
        "Ingestions": List[ClientListIngestionsResponseIngestionsTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListIngestionsResponseTypeDef(_ClientListIngestionsResponseTypeDef):
    """
    - *(dict) --*

      - **Ingestions** *(list) --*

        A list of the ingestions.
        - *(dict) --*

          Information on the SPICE ingestion for a dataset.
          - **Arn** *(string) --*

            The Amazon Resource name (ARN) of the resource.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      The keys of the key-value pairs for the resource tag or tags assigned to the resource.
      - **Key** *(string) --*

        Tag key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "RequestId": str, "Status": int},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.
        - *(dict) --*

          The keys of the key-value pairs for the resource tag or tags assigned to the resource.
          - **Key** *(string) --*

            Tag key.
    """


_ClientListTemplateAliasesResponseTemplateAliasListTypeDef = TypedDict(
    "_ClientListTemplateAliasesResponseTemplateAliasListTypeDef",
    {"AliasName": str, "Arn": str, "TemplateVersionNumber": int},
    total=False,
)


class ClientListTemplateAliasesResponseTemplateAliasListTypeDef(
    _ClientListTemplateAliasesResponseTemplateAliasListTypeDef
):
    """
    - *(dict) --*

      The template alias.
      - **AliasName** *(string) --*

        The display name of the template alias.
    """


_ClientListTemplateAliasesResponseTypeDef = TypedDict(
    "_ClientListTemplateAliasesResponseTypeDef",
    {
        "TemplateAliasList": List[ClientListTemplateAliasesResponseTemplateAliasListTypeDef],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
    },
    total=False,
)


class ClientListTemplateAliasesResponseTypeDef(_ClientListTemplateAliasesResponseTypeDef):
    """
    - *(dict) --*

      - **TemplateAliasList** *(list) --*

        A structure containing the list of the template's aliases.
        - *(dict) --*

          The template alias.
          - **AliasName** *(string) --*

            The display name of the template alias.
    """


_ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef = TypedDict(
    "_ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef",
    {
        "Arn": str,
        "VersionNumber": int,
        "CreatedTime": datetime,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Description": str,
    },
    total=False,
)


class ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef(
    _ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef
):
    """
    - *(dict) --*

      The template version.
      - **Arn** *(string) --*

        The ARN of the template version.
    """


_ClientListTemplateVersionsResponseTypeDef = TypedDict(
    "_ClientListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionSummaryList": List[
            ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef
        ],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientListTemplateVersionsResponseTypeDef(_ClientListTemplateVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **TemplateVersionSummaryList** *(list) --*

        A structure containing a list of all the versions of the specified template.
        - *(dict) --*

          The template version.
          - **Arn** *(string) --*

            The ARN of the template version.
    """


_ClientListTemplatesResponseTemplateSummaryListTypeDef = TypedDict(
    "_ClientListTemplatesResponseTemplateSummaryListTypeDef",
    {
        "Arn": str,
        "TemplateId": str,
        "Name": str,
        "LatestVersionNumber": int,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientListTemplatesResponseTemplateSummaryListTypeDef(
    _ClientListTemplatesResponseTemplateSummaryListTypeDef
):
    """
    - *(dict) --*

      The template summary.
      - **Arn** *(string) --*

        A summary of a template.
    """


_ClientListTemplatesResponseTypeDef = TypedDict(
    "_ClientListTemplatesResponseTypeDef",
    {
        "TemplateSummaryList": List[ClientListTemplatesResponseTemplateSummaryListTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientListTemplatesResponseTypeDef(_ClientListTemplatesResponseTypeDef):
    """
    - *(dict) --*

      - **TemplateSummaryList** *(list) --*

        A structure containing information about the templates in the list.
        - *(dict) --*

          The template summary.
          - **Arn** *(string) --*

            A summary of a template.
    """


_ClientListUserGroupsResponseGroupListTypeDef = TypedDict(
    "_ClientListUserGroupsResponseGroupListTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientListUserGroupsResponseGroupListTypeDef(_ClientListUserGroupsResponseGroupListTypeDef):
    """
    - *(dict) --*

      A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it
      easier to manage access and security. Currently, an Amazon QuickSight subscription can't
      contain more than 500 Amazon QuickSight groups.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the group.
    """


_ClientListUserGroupsResponseTypeDef = TypedDict(
    "_ClientListUserGroupsResponseTypeDef",
    {
        "GroupList": List[ClientListUserGroupsResponseGroupListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListUserGroupsResponseTypeDef(_ClientListUserGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **GroupList** *(list) --*

        The list of groups the user is a member of.
        - *(dict) --*

          A *group* in Amazon QuickSight consists of a set of users. You can use groups to make it
          easier to manage access and security. Currently, an Amazon QuickSight subscription can't
          contain more than 500 Amazon QuickSight groups.
          - **Arn** *(string) --*

            The Amazon Resource name (ARN) for the group.
    """


_ClientListUsersResponseUserListTypeDef = TypedDict(
    "_ClientListUsersResponseUserListTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        "IdentityType": Literal["IAM", "QUICKSIGHT"],
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)


class ClientListUsersResponseUserListTypeDef(_ClientListUsersResponseUserListTypeDef):
    """
    - *(dict) --*

      A registered user of Amazon QuickSight. Currently, an Amazon QuickSight subscription can't
      contain more than 20 million users.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the user.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {
        "UserList": List[ClientListUsersResponseUserListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    - *(dict) --*

      - **UserList** *(list) --*

        The list of users.
        - *(dict) --*

          A registered user of Amazon QuickSight. Currently, an Amazon QuickSight subscription can't
          contain more than 20 million users.
          - **Arn** *(string) --*

            The Amazon Resource name (ARN) for the user.
    """


_ClientRegisterUserResponseUserTypeDef = TypedDict(
    "_ClientRegisterUserResponseUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        "IdentityType": Literal["IAM", "QUICKSIGHT"],
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)


class ClientRegisterUserResponseUserTypeDef(_ClientRegisterUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The user name.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the user.
    """


_ClientRegisterUserResponseTypeDef = TypedDict(
    "_ClientRegisterUserResponseTypeDef",
    {
        "User": ClientRegisterUserResponseUserTypeDef,
        "UserInvitationUrl": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientRegisterUserResponseTypeDef(_ClientRegisterUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        The user name.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) for the user.
    """


_ClientTagResourceResponseTypeDef = TypedDict(
    "_ClientTagResourceResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)


class ClientTagResourceResponseTypeDef(_ClientTagResourceResponseTypeDef):
    """
    - *(dict) --*

      - **RequestId** *(string) --*

        The AWS request ID for this operation.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      The keys of the key-value pairs for the resource tag or tags assigned to the resource.
      - **Key** *(string) --***[REQUIRED]**

        Tag key.
    """


_ClientUntagResourceResponseTypeDef = TypedDict(
    "_ClientUntagResourceResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)


class ClientUntagResourceResponseTypeDef(_ClientUntagResourceResponseTypeDef):
    """
    - *(dict) --*

      - **RequestId** *(string) --*

        The AWS request ID for this operation.
    """


_ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef = TypedDict(
    "_ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef",
    {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef(
    _ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef
):
    """
    - **AdHocFilteringOption** *(dict) --*

      Ad hoc filtering option.
      - **AvailabilityStatus** *(string) --*

        Availability status.
    """


_ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef = TypedDict(
    "_ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef",
    {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef(
    _ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef
):
    pass


_ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef = TypedDict(
    "_ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef",
    {"VisibilityState": Literal["EXPANDED", "COLLAPSED"]},
    total=False,
)


class ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef(
    _ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef
):
    pass


_ClientUpdateDashboardDashboardPublishOptionsTypeDef = TypedDict(
    "_ClientUpdateDashboardDashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef,
        "ExportToCSVOption": ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef,
        "SheetControlsOption": ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef,
    },
    total=False,
)


class ClientUpdateDashboardDashboardPublishOptionsTypeDef(
    _ClientUpdateDashboardDashboardPublishOptionsTypeDef
):
    """
    Publishing options when creating a dashboard.
    * AvailabilityStatus for AdHocFilteringOption - This can be either ``ENABLED`` or ``DISABLED`` .
    When This is set to set to ``DISABLED`` , QuickSight disables the left filter pane on the
    published dashboard, which can be used for AdHoc filtering. Enabled by default.
    * AvailabilityStatus for ExportToCSVOption - This can be either ``ENABLED`` or ``DISABLED`` .
    The visual option to export data to CSV is disabled when this is set to ``DISABLED`` . Enabled
    by default.
    * VisibilityState for SheetControlsOption - This can be either ``COLLAPSED`` or ``EXPANDED`` .
    The sheet controls pane is collapsed by default when set to true. Collapsed by default.
    - **AdHocFilteringOption** *(dict) --*

      Ad hoc filtering option.
      - **AvailabilityStatus** *(string) --*

        Availability status.
    """


_ClientUpdateDashboardParametersDateTimeParametersTypeDef = TypedDict(
    "_ClientUpdateDashboardParametersDateTimeParametersTypeDef",
    {"Name": str, "Values": List[datetime]},
    total=False,
)


class ClientUpdateDashboardParametersDateTimeParametersTypeDef(
    _ClientUpdateDashboardParametersDateTimeParametersTypeDef
):
    pass


_ClientUpdateDashboardParametersDecimalParametersTypeDef = TypedDict(
    "_ClientUpdateDashboardParametersDecimalParametersTypeDef",
    {"Name": str, "Values": List[float]},
    total=False,
)


class ClientUpdateDashboardParametersDecimalParametersTypeDef(
    _ClientUpdateDashboardParametersDecimalParametersTypeDef
):
    pass


_ClientUpdateDashboardParametersIntegerParametersTypeDef = TypedDict(
    "_ClientUpdateDashboardParametersIntegerParametersTypeDef",
    {"Name": str, "Values": List[int]},
    total=False,
)


class ClientUpdateDashboardParametersIntegerParametersTypeDef(
    _ClientUpdateDashboardParametersIntegerParametersTypeDef
):
    pass


_RequiredClientUpdateDashboardParametersStringParametersTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardParametersStringParametersTypeDef", {"Name": str}
)
_OptionalClientUpdateDashboardParametersStringParametersTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardParametersStringParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientUpdateDashboardParametersStringParametersTypeDef(
    _RequiredClientUpdateDashboardParametersStringParametersTypeDef,
    _OptionalClientUpdateDashboardParametersStringParametersTypeDef,
):
    """
    - *(dict) --*

      String parameter.
      - **Name** *(string) --***[REQUIRED]**

        A display name for the dataset.
    """


_ClientUpdateDashboardParametersTypeDef = TypedDict(
    "_ClientUpdateDashboardParametersTypeDef",
    {
        "StringParameters": List[ClientUpdateDashboardParametersStringParametersTypeDef],
        "IntegerParameters": List[ClientUpdateDashboardParametersIntegerParametersTypeDef],
        "DecimalParameters": List[ClientUpdateDashboardParametersDecimalParametersTypeDef],
        "DateTimeParameters": List[ClientUpdateDashboardParametersDateTimeParametersTypeDef],
    },
    total=False,
)


class ClientUpdateDashboardParametersTypeDef(_ClientUpdateDashboardParametersTypeDef):
    """
    A structure that contains the parameters of the dashboard.
    - **StringParameters** *(list) --*

      String parameters.
      - *(dict) --*

        String parameter.
        - **Name** *(string) --***[REQUIRED]**

          A display name for the dataset.
    """


_RequiredClientUpdateDashboardPermissionsGrantPermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardPermissionsGrantPermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDashboardPermissionsGrantPermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardPermissionsGrantPermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDashboardPermissionsGrantPermissionsTypeDef(
    _RequiredClientUpdateDashboardPermissionsGrantPermissionsTypeDef,
    _OptionalClientUpdateDashboardPermissionsGrantPermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientUpdateDashboardPermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientUpdateDashboardPermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)


class ClientUpdateDashboardPermissionsResponsePermissionsTypeDef(
    _ClientUpdateDashboardPermissionsResponsePermissionsTypeDef
):
    pass


_ClientUpdateDashboardPermissionsResponseTypeDef = TypedDict(
    "_ClientUpdateDashboardPermissionsResponseTypeDef",
    {
        "DashboardArn": str,
        "DashboardId": str,
        "Permissions": List[ClientUpdateDashboardPermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientUpdateDashboardPermissionsResponseTypeDef(
    _ClientUpdateDashboardPermissionsResponseTypeDef
):
    """
    - *(dict) --*

      - **DashboardArn** *(string) --*

        The Amazon Resource Name (ARN) of the dashboard.
    """


_RequiredClientUpdateDashboardPermissionsRevokePermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardPermissionsRevokePermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDashboardPermissionsRevokePermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardPermissionsRevokePermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDashboardPermissionsRevokePermissionsTypeDef(
    _RequiredClientUpdateDashboardPermissionsRevokePermissionsTypeDef,
    _OptionalClientUpdateDashboardPermissionsRevokePermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientUpdateDashboardPublishedVersionResponseTypeDef = TypedDict(
    "_ClientUpdateDashboardPublishedVersionResponseTypeDef",
    {"DashboardId": str, "DashboardArn": str, "Status": int, "RequestId": str},
    total=False,
)


class ClientUpdateDashboardPublishedVersionResponseTypeDef(
    _ClientUpdateDashboardPublishedVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **DashboardId** *(string) --*

        The ID for the dashboard.
    """


_ClientUpdateDashboardResponseTypeDef = TypedDict(
    "_ClientUpdateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientUpdateDashboardResponseTypeDef(_ClientUpdateDashboardResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_RequiredClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    {"DataSetPlaceholder": str},
)
_OptionalClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    {"DataSetArn": str},
    total=False,
)


class ClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef(
    _RequiredClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef,
    _OptionalClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef,
):
    """
    - *(dict) --*

      Dataset reference.
      - **DataSetPlaceholder** *(string) --***[REQUIRED]**

        Dataset placeholder.
    """


_RequiredClientUpdateDashboardSourceEntitySourceTemplateTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardSourceEntitySourceTemplateTypeDef",
    {
        "DataSetReferences": List[
            ClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef
        ]
    },
)
_OptionalClientUpdateDashboardSourceEntitySourceTemplateTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardSourceEntitySourceTemplateTypeDef", {"Arn": str}, total=False
)


class ClientUpdateDashboardSourceEntitySourceTemplateTypeDef(
    _RequiredClientUpdateDashboardSourceEntitySourceTemplateTypeDef,
    _OptionalClientUpdateDashboardSourceEntitySourceTemplateTypeDef,
):
    """
    - **SourceTemplate** *(dict) --*

      Source template.
      - **DataSetReferences** *(list) --***[REQUIRED]**

        Dataset references.
        - *(dict) --*

          Dataset reference.
          - **DataSetPlaceholder** *(string) --***[REQUIRED]**

            Dataset placeholder.
    """


_ClientUpdateDashboardSourceEntityTypeDef = TypedDict(
    "_ClientUpdateDashboardSourceEntityTypeDef",
    {"SourceTemplate": ClientUpdateDashboardSourceEntitySourceTemplateTypeDef},
    total=False,
)


class ClientUpdateDashboardSourceEntityTypeDef(_ClientUpdateDashboardSourceEntityTypeDef):
    """
    The template or analysis from which the dashboard is created. The SouceTemplate entity accepts
    the Arn of the template and also references to replacement datasets for the placeholders set
    when creating the template. The replacement datasets need to follow the same schema as the
    datasets for which placeholders were created when creating the template.
    - **SourceTemplate** *(dict) --*

      Source template.
      - **DataSetReferences** *(list) --***[REQUIRED]**

        Dataset references.
        - *(dict) --*

          Dataset reference.
          - **DataSetPlaceholder** *(string) --***[REQUIRED]**

            Dataset placeholder.
    """


_RequiredClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "_RequiredClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef", {"Name": str}
)
_OptionalClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "_OptionalClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    {"CountryCode": str, "Columns": List[str]},
    total=False,
)


class ClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef(
    _RequiredClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef,
    _OptionalClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef,
):
    """
    - **GeoSpatialColumnGroup** *(dict) --*

      Geospatial column group that denotes a hierarchy.
      - **Name** *(string) --***[REQUIRED]**

        A display name for the hierarchy.
    """


_ClientUpdateDataSetColumnGroupsTypeDef = TypedDict(
    "_ClientUpdateDataSetColumnGroupsTypeDef",
    {"GeoSpatialColumnGroup": ClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef},
    total=False,
)


class ClientUpdateDataSetColumnGroupsTypeDef(_ClientUpdateDataSetColumnGroupsTypeDef):
    """
    - *(dict) --*

      Groupings of columns that work together in certain QuickSight features. This is a variant type
      structure. No more than one of the attributes should be non-null for this structure to be
      valid.
      - **GeoSpatialColumnGroup** *(dict) --*

        Geospatial column group that denotes a hierarchy.
        - **Name** *(string) --***[REQUIRED]**

          A display name for the hierarchy.
    """


_ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"],
        "Format": str,
    },
    total=False,
)


class ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef(
    _ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    {"ColumnName": str, "ColumnId": str, "Expression": str},
    total=False,
)


class ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef(
    _ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    {
        "Columns": List[
            ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef(
    _ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    {"ConditionExpression": str},
    total=False,
)


class ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef(
    _ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    {"ProjectedColumns": List[str]},
    total=False,
)


class ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef(
    _ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    {"ColumnName": str, "NewColumnName": str},
    total=False,
)


class ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef(
    _ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    {
        "ColumnGeographicRole": Literal[
            "COUNTRY", "STATE", "COUNTY", "CITY", "POSTCODE", "LONGITUDE", "LATITUDE"
        ]
    },
    total=False,
)


class ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef(
    _ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": List[ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef],
    },
    total=False,
)


class ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef(
    _ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef",
    {
        "ProjectOperation": ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef,
        "FilterOperation": ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef,
        "CreateColumnsOperation": ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef,
        "RenameColumnOperation": ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef,
        "CastColumnTypeOperation": ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef,
        "TagColumnOperation": ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef,
    },
    total=False,
)


class ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef(
    _ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": Literal["INNER", "OUTER", "LEFT", "RIGHT"],
        "OnClause": str,
    },
    total=False,
)


class ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef(
    _ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapSourceTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapSourceTypeDef",
    {
        "JoinInstruction": ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef,
        "PhysicalTableId": str,
    },
    total=False,
)


class ClientUpdateDataSetLogicalTableMapSourceTypeDef(
    _ClientUpdateDataSetLogicalTableMapSourceTypeDef
):
    pass


_ClientUpdateDataSetLogicalTableMapTypeDef = TypedDict(
    "_ClientUpdateDataSetLogicalTableMapTypeDef",
    {
        "Alias": str,
        "DataTransforms": List[ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef],
        "Source": ClientUpdateDataSetLogicalTableMapSourceTypeDef,
    },
    total=False,
)


class ClientUpdateDataSetLogicalTableMapTypeDef(_ClientUpdateDataSetLogicalTableMapTypeDef):
    pass


_RequiredClientUpdateDataSetPermissionsGrantPermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDataSetPermissionsGrantPermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDataSetPermissionsGrantPermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDataSetPermissionsGrantPermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDataSetPermissionsGrantPermissionsTypeDef(
    _RequiredClientUpdateDataSetPermissionsGrantPermissionsTypeDef,
    _OptionalClientUpdateDataSetPermissionsGrantPermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientUpdateDataSetPermissionsResponseTypeDef = TypedDict(
    "_ClientUpdateDataSetPermissionsResponseTypeDef",
    {"DataSetArn": str, "DataSetId": str, "RequestId": str, "Status": int},
    total=False,
)


class ClientUpdateDataSetPermissionsResponseTypeDef(_ClientUpdateDataSetPermissionsResponseTypeDef):
    """
    - *(dict) --*

      - **DataSetArn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset.
    """


_RequiredClientUpdateDataSetPermissionsRevokePermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDataSetPermissionsRevokePermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDataSetPermissionsRevokePermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDataSetPermissionsRevokePermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDataSetPermissionsRevokePermissionsTypeDef(
    _RequiredClientUpdateDataSetPermissionsRevokePermissionsTypeDef,
    _OptionalClientUpdateDataSetPermissionsRevokePermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef = TypedDict(
    "_ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)


class ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef(
    _ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef
):
    pass


_ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef = TypedDict(
    "_ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
        "Columns": List[ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef],
    },
    total=False,
)


class ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef(
    _ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef
):
    pass


_ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef = TypedDict(
    "_ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)


class ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef(
    _ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef
):
    pass


_ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef = TypedDict(
    "_ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Schema": str,
        "Name": str,
        "InputColumns": List[ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef],
    },
    total=False,
)


class ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef(
    _ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef
):
    pass


_ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef = TypedDict(
    "_ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)


class ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef(
    _ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef
):
    pass


_ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef = TypedDict(
    "_ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    {
        "Format": Literal["CSV", "TSV", "CLF", "ELF", "XLSX", "JSON"],
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"],
        "Delimiter": str,
    },
    total=False,
)


class ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef(
    _ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef
):
    pass


_ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef = TypedDict(
    "_ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef",
    {
        "DataSourceArn": str,
        "UploadSettings": ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef,
        "InputColumns": List[ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef],
    },
    total=False,
)


class ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef(
    _ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef
):
    pass


_ClientUpdateDataSetPhysicalTableMapTypeDef = TypedDict(
    "_ClientUpdateDataSetPhysicalTableMapTypeDef",
    {
        "RelationalTable": ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef,
        "CustomSql": ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef,
        "S3Source": ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef,
    },
    total=False,
)


class ClientUpdateDataSetPhysicalTableMapTypeDef(_ClientUpdateDataSetPhysicalTableMapTypeDef):
    pass


_ClientUpdateDataSetResponseTypeDef = TypedDict(
    "_ClientUpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientUpdateDataSetResponseTypeDef(_ClientUpdateDataSetResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the dataset.
    """


_RequiredClientUpdateDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "_RequiredClientUpdateDataSetRowLevelPermissionDataSetTypeDef", {"Arn": str}
)
_OptionalClientUpdateDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "_OptionalClientUpdateDataSetRowLevelPermissionDataSetTypeDef",
    {"PermissionPolicy": Literal["GRANT_ACCESS", "DENY_ACCESS"]},
    total=False,
)


class ClientUpdateDataSetRowLevelPermissionDataSetTypeDef(
    _RequiredClientUpdateDataSetRowLevelPermissionDataSetTypeDef,
    _OptionalClientUpdateDataSetRowLevelPermissionDataSetTypeDef,
):
    """
    Row-level security configuration on the data you want to create.
    - **Arn** *(string) --***[REQUIRED]**

      The Amazon Resource name (ARN) of the permission dataset.
    """


_RequiredClientUpdateDataSourceCredentialsCredentialPairTypeDef = TypedDict(
    "_RequiredClientUpdateDataSourceCredentialsCredentialPairTypeDef", {"Username": str}
)
_OptionalClientUpdateDataSourceCredentialsCredentialPairTypeDef = TypedDict(
    "_OptionalClientUpdateDataSourceCredentialsCredentialPairTypeDef",
    {"Password": str},
    total=False,
)


class ClientUpdateDataSourceCredentialsCredentialPairTypeDef(
    _RequiredClientUpdateDataSourceCredentialsCredentialPairTypeDef,
    _OptionalClientUpdateDataSourceCredentialsCredentialPairTypeDef,
):
    """
    - **CredentialPair** *(dict) --*

      Credential pair.
      - **Username** *(string) --***[REQUIRED]**

        Username.
    """


_ClientUpdateDataSourceCredentialsTypeDef = TypedDict(
    "_ClientUpdateDataSourceCredentialsTypeDef",
    {"CredentialPair": ClientUpdateDataSourceCredentialsCredentialPairTypeDef},
    total=False,
)


class ClientUpdateDataSourceCredentialsTypeDef(_ClientUpdateDataSourceCredentialsTypeDef):
    """
    The credentials that QuickSight that uses to connect to your underlying source. Currently, only
    credentials based on user name and password are supported.
    - **CredentialPair** *(dict) --*

      Credential pair.
      - **Username** *(string) --***[REQUIRED]**

        Username.
    """


_ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    {"Domain": str},
)


class ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef
):
    """
    - **AmazonElasticsearchParameters** *(dict) --*

      Amazon Elasticsearch parameters.
      - **Domain** *(string) --***[REQUIRED]**

        The Amazon Elasticsearch Service domain.
    """


_ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef",
    {"WorkGroup": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    {"DataSetName": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef",
    {"Host": str, "Port": int, "Catalog": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef",
    {"InstanceId": str, "Database": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef",
    {"Host": str, "Port": int, "Database": str, "ClusterId": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef(
    _ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef",
    {
        "ManifestFileLocation": ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef
    },
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    {"Host": str, "Database": str, "Warehouse": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef",
    {"Host": str, "Port": int},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef",
    {"Query": str, "MaxRows": int},
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef
):
    pass


_ClientUpdateDataSourceDataSourceParametersTypeDef = TypedDict(
    "_ClientUpdateDataSourceDataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef,
        "AthenaParameters": ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef,
        "AuroraParameters": ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef,
        "AuroraPostgreSqlParameters": ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef,
        "AwsIotAnalyticsParameters": ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef,
        "JiraParameters": ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef,
        "MariaDbParameters": ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef,
        "MySqlParameters": ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef,
        "PostgreSqlParameters": ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef,
        "PrestoParameters": ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef,
        "RdsParameters": ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef,
        "RedshiftParameters": ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef,
        "S3Parameters": ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef,
        "ServiceNowParameters": ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef,
        "SnowflakeParameters": ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef,
        "SparkParameters": ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef,
        "SqlServerParameters": ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef,
        "TeradataParameters": ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef,
        "TwitterParameters": ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef,
    },
    total=False,
)


class ClientUpdateDataSourceDataSourceParametersTypeDef(
    _ClientUpdateDataSourceDataSourceParametersTypeDef
):
    """
    The parameters that QuickSight uses to connect to your underlying source.
    - **AmazonElasticsearchParameters** *(dict) --*

      Amazon Elasticsearch parameters.
      - **Domain** *(string) --***[REQUIRED]**

        The Amazon Elasticsearch Service domain.
    """


_RequiredClientUpdateDataSourcePermissionsGrantPermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDataSourcePermissionsGrantPermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDataSourcePermissionsGrantPermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDataSourcePermissionsGrantPermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDataSourcePermissionsGrantPermissionsTypeDef(
    _RequiredClientUpdateDataSourcePermissionsGrantPermissionsTypeDef,
    _OptionalClientUpdateDataSourcePermissionsGrantPermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientUpdateDataSourcePermissionsResponseTypeDef = TypedDict(
    "_ClientUpdateDataSourcePermissionsResponseTypeDef",
    {"DataSourceArn": str, "DataSourceId": str, "RequestId": str, "Status": int},
    total=False,
)


class ClientUpdateDataSourcePermissionsResponseTypeDef(
    _ClientUpdateDataSourcePermissionsResponseTypeDef
):
    """
    - *(dict) --*

      - **DataSourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the data source.
    """


_RequiredClientUpdateDataSourcePermissionsRevokePermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDataSourcePermissionsRevokePermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDataSourcePermissionsRevokePermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDataSourcePermissionsRevokePermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDataSourcePermissionsRevokePermissionsTypeDef(
    _RequiredClientUpdateDataSourcePermissionsRevokePermissionsTypeDef,
    _OptionalClientUpdateDataSourcePermissionsRevokePermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientUpdateDataSourceResponseTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "UpdateStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientUpdateDataSourceResponseTypeDef(_ClientUpdateDataSourceResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the data source.
    """


_ClientUpdateDataSourceSslPropertiesTypeDef = TypedDict(
    "_ClientUpdateDataSourceSslPropertiesTypeDef", {"DisableSsl": bool}, total=False
)


class ClientUpdateDataSourceSslPropertiesTypeDef(_ClientUpdateDataSourceSslPropertiesTypeDef):
    """
    Secure Socket Layer (SSL) properties that apply when QuickSight connects to your underlying
    source.
    - **DisableSsl** *(boolean) --*

      A boolean flag to control whether SSL should be disabled.
    """


_ClientUpdateDataSourceVpcConnectionPropertiesTypeDef = TypedDict(
    "_ClientUpdateDataSourceVpcConnectionPropertiesTypeDef", {"VpcConnectionArn": str}
)


class ClientUpdateDataSourceVpcConnectionPropertiesTypeDef(
    _ClientUpdateDataSourceVpcConnectionPropertiesTypeDef
):
    """
    Use this parameter only when you want QuickSight to use a VPC connection when connecting to your
    underlying source.
    - **VpcConnectionArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) for the VPC connection.
    """


_ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "_ClientUpdateGroupResponseGroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)


class ClientUpdateGroupResponseGroupTypeDef(_ClientUpdateGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The name of the group.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the group.
    """


_ClientUpdateGroupResponseTypeDef = TypedDict(
    "_ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientUpdateGroupResponseTypeDef(_ClientUpdateGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        The name of the group.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) for the group.
    """


_ClientUpdateIamPolicyAssignmentResponseTypeDef = TypedDict(
    "_ClientUpdateIamPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientUpdateIamPolicyAssignmentResponseTypeDef(
    _ClientUpdateIamPolicyAssignmentResponseTypeDef
):
    """
    - *(dict) --*

      - **AssignmentName** *(string) --*

        The name of the assignment.
    """


_ClientUpdateTemplateAliasResponseTemplateAliasTypeDef = TypedDict(
    "_ClientUpdateTemplateAliasResponseTemplateAliasTypeDef",
    {"AliasName": str, "Arn": str, "TemplateVersionNumber": int},
    total=False,
)


class ClientUpdateTemplateAliasResponseTemplateAliasTypeDef(
    _ClientUpdateTemplateAliasResponseTemplateAliasTypeDef
):
    """
    - **TemplateAlias** *(dict) --*

      The template alias.
      - **AliasName** *(string) --*

        The display name of the template alias.
    """


_ClientUpdateTemplateAliasResponseTypeDef = TypedDict(
    "_ClientUpdateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": ClientUpdateTemplateAliasResponseTemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientUpdateTemplateAliasResponseTypeDef(_ClientUpdateTemplateAliasResponseTypeDef):
    """
    - *(dict) --*

      - **TemplateAlias** *(dict) --*

        The template alias.
        - **AliasName** *(string) --*

          The display name of the template alias.
    """


_RequiredClientUpdateTemplatePermissionsGrantPermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateTemplatePermissionsGrantPermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateTemplatePermissionsGrantPermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateTemplatePermissionsGrantPermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateTemplatePermissionsGrantPermissionsTypeDef(
    _RequiredClientUpdateTemplatePermissionsGrantPermissionsTypeDef,
    _OptionalClientUpdateTemplatePermissionsGrantPermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientUpdateTemplatePermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientUpdateTemplatePermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)


class ClientUpdateTemplatePermissionsResponsePermissionsTypeDef(
    _ClientUpdateTemplatePermissionsResponsePermissionsTypeDef
):
    pass


_ClientUpdateTemplatePermissionsResponseTypeDef = TypedDict(
    "_ClientUpdateTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List[ClientUpdateTemplatePermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)


class ClientUpdateTemplatePermissionsResponseTypeDef(
    _ClientUpdateTemplatePermissionsResponseTypeDef
):
    """
    - *(dict) --*

      - **TemplateId** *(string) --*

        The ID for the template.
    """


_RequiredClientUpdateTemplatePermissionsRevokePermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateTemplatePermissionsRevokePermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateTemplatePermissionsRevokePermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateTemplatePermissionsRevokePermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateTemplatePermissionsRevokePermissionsTypeDef(
    _RequiredClientUpdateTemplatePermissionsRevokePermissionsTypeDef,
    _OptionalClientUpdateTemplatePermissionsRevokePermissionsTypeDef,
):
    """
    - *(dict) --*

      Permission for the resource.
      - **Principal** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of a QuickSight user or group, or an IAM ARN. If you are
        using cross-account resource sharing, this is the IAM ARN of an account root. Otherwise, it
        is the ARN of a QuickSight user or group. .
    """


_ClientUpdateTemplateResponseTypeDef = TypedDict(
    "_ClientUpdateTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)


class ClientUpdateTemplateResponseTypeDef(_ClientUpdateTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **TemplateId** *(string) --*

        The ID for the template.
    """


_ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef = TypedDict(
    "_ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef",
    {"DataSetPlaceholder": str, "DataSetArn": str},
    total=False,
)


class ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef(
    _ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef
):
    pass


_RequiredClientUpdateTemplateSourceEntitySourceAnalysisTypeDef = TypedDict(
    "_RequiredClientUpdateTemplateSourceEntitySourceAnalysisTypeDef", {"Arn": str}
)
_OptionalClientUpdateTemplateSourceEntitySourceAnalysisTypeDef = TypedDict(
    "_OptionalClientUpdateTemplateSourceEntitySourceAnalysisTypeDef",
    {
        "DataSetReferences": List[
            ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef
        ]
    },
    total=False,
)


class ClientUpdateTemplateSourceEntitySourceAnalysisTypeDef(
    _RequiredClientUpdateTemplateSourceEntitySourceAnalysisTypeDef,
    _OptionalClientUpdateTemplateSourceEntitySourceAnalysisTypeDef,
):
    """
    - **SourceAnalysis** *(dict) --*

      The source analysis, if it is based on an analysis.
      - **Arn** *(string) --***[REQUIRED]**

        The Amazon Resource name (ARN) of the resource.
    """


_ClientUpdateTemplateSourceEntitySourceTemplateTypeDef = TypedDict(
    "_ClientUpdateTemplateSourceEntitySourceTemplateTypeDef", {"Arn": str}, total=False
)


class ClientUpdateTemplateSourceEntitySourceTemplateTypeDef(
    _ClientUpdateTemplateSourceEntitySourceTemplateTypeDef
):
    pass


_ClientUpdateTemplateSourceEntityTypeDef = TypedDict(
    "_ClientUpdateTemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": ClientUpdateTemplateSourceEntitySourceAnalysisTypeDef,
        "SourceTemplate": ClientUpdateTemplateSourceEntitySourceTemplateTypeDef,
    },
    total=False,
)


class ClientUpdateTemplateSourceEntityTypeDef(_ClientUpdateTemplateSourceEntityTypeDef):
    """
    The source QuickSight entity from which this template is being created. Templates can be
    currently created from an Analysis or another template.
    - **SourceAnalysis** *(dict) --*

      The source analysis, if it is based on an analysis.
      - **Arn** *(string) --***[REQUIRED]**

        The Amazon Resource name (ARN) of the resource.
    """


_ClientUpdateUserResponseUserTypeDef = TypedDict(
    "_ClientUpdateUserResponseUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        "IdentityType": Literal["IAM", "QUICKSIGHT"],
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)


class ClientUpdateUserResponseUserTypeDef(_ClientUpdateUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      The Amazon QuickSight user.
      - **Arn** *(string) --*

        The Amazon Resource name (ARN) for the user.
    """


_ClientUpdateUserResponseTypeDef = TypedDict(
    "_ClientUpdateUserResponseTypeDef",
    {"User": ClientUpdateUserResponseUserTypeDef, "RequestId": str, "Status": int},
    total=False,
)


class ClientUpdateUserResponseTypeDef(_ClientUpdateUserResponseTypeDef):
    """
    - *(dict) --*

      - **User** *(dict) --*

        The Amazon QuickSight user.
        - **Arn** *(string) --*

          The Amazon Resource name (ARN) for the user.
    """
