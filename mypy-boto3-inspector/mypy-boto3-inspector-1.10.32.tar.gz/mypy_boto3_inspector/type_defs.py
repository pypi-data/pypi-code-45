"Main interface for inspector service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddAttributesToFindingsAttributesTypeDef",
    "ClientAddAttributesToFindingsResponsefailedItemsTypeDef",
    "ClientAddAttributesToFindingsResponseTypeDef",
    "ClientCreateAssessmentTargetResponseTypeDef",
    "ClientCreateAssessmentTemplateResponseTypeDef",
    "ClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef",
    "ClientCreateExclusionsPreviewResponseTypeDef",
    "ClientCreateResourceGroupResourceGroupTagsTypeDef",
    "ClientCreateResourceGroupResponseTypeDef",
    "ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef",
    "ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef",
    "ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef",
    "ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef",
    "ClientDescribeAssessmentRunsResponsefailedItemsTypeDef",
    "ClientDescribeAssessmentRunsResponseTypeDef",
    "ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef",
    "ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef",
    "ClientDescribeAssessmentTargetsResponseTypeDef",
    "ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef",
    "ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef",
    "ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef",
    "ClientDescribeAssessmentTemplatesResponseTypeDef",
    "ClientDescribeCrossAccountAccessRoleResponseTypeDef",
    "ClientDescribeExclusionsResponseexclusionsattributesTypeDef",
    "ClientDescribeExclusionsResponseexclusionsscopesTypeDef",
    "ClientDescribeExclusionsResponseexclusionsTypeDef",
    "ClientDescribeExclusionsResponsefailedItemsTypeDef",
    "ClientDescribeExclusionsResponseTypeDef",
    "ClientDescribeFindingsResponsefailedItemsTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef",
    "ClientDescribeFindingsResponsefindingsassetAttributesTypeDef",
    "ClientDescribeFindingsResponsefindingsattributesTypeDef",
    "ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef",
    "ClientDescribeFindingsResponsefindingsuserAttributesTypeDef",
    "ClientDescribeFindingsResponsefindingsTypeDef",
    "ClientDescribeFindingsResponseTypeDef",
    "ClientDescribeResourceGroupsResponsefailedItemsTypeDef",
    "ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef",
    "ClientDescribeResourceGroupsResponseresourceGroupsTypeDef",
    "ClientDescribeResourceGroupsResponseTypeDef",
    "ClientDescribeRulesPackagesResponsefailedItemsTypeDef",
    "ClientDescribeRulesPackagesResponserulesPackagesTypeDef",
    "ClientDescribeRulesPackagesResponseTypeDef",
    "ClientGetAssessmentReportResponseTypeDef",
    "ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef",
    "ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef",
    "ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef",
    "ClientGetExclusionsPreviewResponseTypeDef",
    "ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef",
    "ClientGetTelemetryMetadataResponseTypeDef",
    "ClientListAssessmentRunAgentsFilterTypeDef",
    "ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef",
    "ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef",
    "ClientListAssessmentRunAgentsResponseTypeDef",
    "ClientListAssessmentRunsFiltercompletionTimeRangeTypeDef",
    "ClientListAssessmentRunsFilterdurationRangeTypeDef",
    "ClientListAssessmentRunsFilterstartTimeRangeTypeDef",
    "ClientListAssessmentRunsFilterstateChangeTimeRangeTypeDef",
    "ClientListAssessmentRunsFilterTypeDef",
    "ClientListAssessmentRunsResponseTypeDef",
    "ClientListAssessmentTargetsFilterTypeDef",
    "ClientListAssessmentTargetsResponseTypeDef",
    "ClientListAssessmentTemplatesFilterdurationRangeTypeDef",
    "ClientListAssessmentTemplatesFilterTypeDef",
    "ClientListAssessmentTemplatesResponseTypeDef",
    "ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef",
    "ClientListEventSubscriptionsResponsesubscriptionsTypeDef",
    "ClientListEventSubscriptionsResponseTypeDef",
    "ClientListExclusionsResponseTypeDef",
    "ClientListFindingsFilterattributesTypeDef",
    "ClientListFindingsFiltercreationTimeRangeTypeDef",
    "ClientListFindingsFilteruserAttributesTypeDef",
    "ClientListFindingsFilterTypeDef",
    "ClientListFindingsResponseTypeDef",
    "ClientListRulesPackagesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPreviewAgentsResponseagentPreviewsTypeDef",
    "ClientPreviewAgentsResponseTypeDef",
    "ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef",
    "ClientRemoveAttributesFromFindingsResponseTypeDef",
    "ClientSetTagsForResourceTagsTypeDef",
    "ClientStartAssessmentRunResponseTypeDef",
    "ListAssessmentRunAgentsPaginateFilterTypeDef",
    "ListAssessmentRunAgentsPaginatePaginationConfigTypeDef",
    "ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef",
    "ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef",
    "ListAssessmentRunAgentsPaginateResponseTypeDef",
    "ListAssessmentRunsPaginateFiltercompletionTimeRangeTypeDef",
    "ListAssessmentRunsPaginateFilterdurationRangeTypeDef",
    "ListAssessmentRunsPaginateFilterstartTimeRangeTypeDef",
    "ListAssessmentRunsPaginateFilterstateChangeTimeRangeTypeDef",
    "ListAssessmentRunsPaginateFilterTypeDef",
    "ListAssessmentRunsPaginatePaginationConfigTypeDef",
    "ListAssessmentRunsPaginateResponseTypeDef",
    "ListAssessmentTargetsPaginateFilterTypeDef",
    "ListAssessmentTargetsPaginatePaginationConfigTypeDef",
    "ListAssessmentTargetsPaginateResponseTypeDef",
    "ListAssessmentTemplatesPaginateFilterdurationRangeTypeDef",
    "ListAssessmentTemplatesPaginateFilterTypeDef",
    "ListAssessmentTemplatesPaginatePaginationConfigTypeDef",
    "ListAssessmentTemplatesPaginateResponseTypeDef",
    "ListEventSubscriptionsPaginatePaginationConfigTypeDef",
    "ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef",
    "ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef",
    "ListEventSubscriptionsPaginateResponseTypeDef",
    "ListExclusionsPaginatePaginationConfigTypeDef",
    "ListExclusionsPaginateResponseTypeDef",
    "ListFindingsPaginateFilterattributesTypeDef",
    "ListFindingsPaginateFiltercreationTimeRangeTypeDef",
    "ListFindingsPaginateFilteruserAttributesTypeDef",
    "ListFindingsPaginateFilterTypeDef",
    "ListFindingsPaginatePaginationConfigTypeDef",
    "ListFindingsPaginateResponseTypeDef",
    "ListRulesPackagesPaginatePaginationConfigTypeDef",
    "ListRulesPackagesPaginateResponseTypeDef",
    "PreviewAgentsPaginatePaginationConfigTypeDef",
    "PreviewAgentsPaginateResponseagentPreviewsTypeDef",
    "PreviewAgentsPaginateResponseTypeDef",
)


_RequiredClientAddAttributesToFindingsAttributesTypeDef = TypedDict(
    "_RequiredClientAddAttributesToFindingsAttributesTypeDef", {"key": str}
)
_OptionalClientAddAttributesToFindingsAttributesTypeDef = TypedDict(
    "_OptionalClientAddAttributesToFindingsAttributesTypeDef", {"value": str}, total=False
)


class ClientAddAttributesToFindingsAttributesTypeDef(
    _RequiredClientAddAttributesToFindingsAttributesTypeDef,
    _OptionalClientAddAttributesToFindingsAttributesTypeDef,
):
    """
    - *(dict) --*

      This data type is used as a request parameter in the  AddAttributesToFindings and
      CreateAssessmentTemplate actions.
      - **key** *(string) --***[REQUIRED]**

        The attribute key.
    """


_ClientAddAttributesToFindingsResponsefailedItemsTypeDef = TypedDict(
    "_ClientAddAttributesToFindingsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)


class ClientAddAttributesToFindingsResponsefailedItemsTypeDef(
    _ClientAddAttributesToFindingsResponsefailedItemsTypeDef
):
    pass


_ClientAddAttributesToFindingsResponseTypeDef = TypedDict(
    "_ClientAddAttributesToFindingsResponseTypeDef",
    {"failedItems": Dict[str, ClientAddAttributesToFindingsResponsefailedItemsTypeDef]},
    total=False,
)


class ClientAddAttributesToFindingsResponseTypeDef(_ClientAddAttributesToFindingsResponseTypeDef):
    """
    - *(dict) --*

      - **failedItems** *(dict) --*

        Attribute details that cannot be described. An error code is provided for each failed item.
        - *(string) --*

          - *(dict) --*

            Includes details about the failed items.
            - **failureCode** *(string) --*

              The status code of a failed item.
    """


_ClientCreateAssessmentTargetResponseTypeDef = TypedDict(
    "_ClientCreateAssessmentTargetResponseTypeDef", {"assessmentTargetArn": str}, total=False
)


class ClientCreateAssessmentTargetResponseTypeDef(_ClientCreateAssessmentTargetResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentTargetArn** *(string) --*

        The ARN that specifies the assessment target that is created.
    """


_ClientCreateAssessmentTemplateResponseTypeDef = TypedDict(
    "_ClientCreateAssessmentTemplateResponseTypeDef", {"assessmentTemplateArn": str}, total=False
)


class ClientCreateAssessmentTemplateResponseTypeDef(_ClientCreateAssessmentTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentTemplateArn** *(string) --*

        The ARN that specifies the assessment template that is created.
    """


_RequiredClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef = TypedDict(
    "_RequiredClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef", {"key": str}
)
_OptionalClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef = TypedDict(
    "_OptionalClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef",
    {"value": str},
    total=False,
)


class ClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef(
    _RequiredClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef,
    _OptionalClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef,
):
    """
    - *(dict) --*

      This data type is used as a request parameter in the  AddAttributesToFindings and
      CreateAssessmentTemplate actions.
      - **key** *(string) --***[REQUIRED]**

        The attribute key.
    """


_ClientCreateExclusionsPreviewResponseTypeDef = TypedDict(
    "_ClientCreateExclusionsPreviewResponseTypeDef", {"previewToken": str}, total=False
)


class ClientCreateExclusionsPreviewResponseTypeDef(_ClientCreateExclusionsPreviewResponseTypeDef):
    """
    - *(dict) --*

      - **previewToken** *(string) --*

        Specifies the unique identifier of the requested exclusions preview. You can use the unique
        identifier to retrieve the exclusions preview when running the GetExclusionsPreview API.
    """


_RequiredClientCreateResourceGroupResourceGroupTagsTypeDef = TypedDict(
    "_RequiredClientCreateResourceGroupResourceGroupTagsTypeDef", {"key": str}
)
_OptionalClientCreateResourceGroupResourceGroupTagsTypeDef = TypedDict(
    "_OptionalClientCreateResourceGroupResourceGroupTagsTypeDef", {"value": str}, total=False
)


class ClientCreateResourceGroupResourceGroupTagsTypeDef(
    _RequiredClientCreateResourceGroupResourceGroupTagsTypeDef,
    _OptionalClientCreateResourceGroupResourceGroupTagsTypeDef,
):
    """
    - *(dict) --*

      This data type is used as one of the elements of the  ResourceGroup data type.
      - **key** *(string) --***[REQUIRED]**

        A tag key.
    """


_ClientCreateResourceGroupResponseTypeDef = TypedDict(
    "_ClientCreateResourceGroupResponseTypeDef", {"resourceGroupArn": str}, total=False
)


class ClientCreateResourceGroupResponseTypeDef(_ClientCreateResourceGroupResponseTypeDef):
    """
    - *(dict) --*

      - **resourceGroupArn** *(string) --*

        The ARN that specifies the resource group that is created.
    """


_ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef",
    {
        "date": datetime,
        "event": Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        "message": str,
        "error": bool,
        "snsTopicArn": str,
        "snsPublishStatusCode": Literal[
            "SUCCESS", "TOPIC_DOES_NOT_EXIST", "ACCESS_DENIED", "INTERNAL_ERROR"
        ],
    },
    total=False,
)


class ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef(
    _ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef
):
    pass


_ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef",
    {
        "stateChangedAt": datetime,
        "state": Literal[
            "CREATED",
            "START_DATA_COLLECTION_PENDING",
            "START_DATA_COLLECTION_IN_PROGRESS",
            "COLLECTING_DATA",
            "STOP_DATA_COLLECTION_PENDING",
            "DATA_COLLECTED",
            "START_EVALUATING_RULES_PENDING",
            "EVALUATING_RULES",
            "FAILED",
            "ERROR",
            "COMPLETED",
            "COMPLETED_WITH_ERRORS",
            "CANCELED",
        ],
    },
    total=False,
)


class ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef(
    _ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef
):
    pass


_ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef(
    _ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef
):
    pass


_ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTemplateArn": str,
        "state": Literal[
            "CREATED",
            "START_DATA_COLLECTION_PENDING",
            "START_DATA_COLLECTION_IN_PROGRESS",
            "COLLECTING_DATA",
            "STOP_DATA_COLLECTION_PENDING",
            "DATA_COLLECTED",
            "START_EVALUATING_RULES_PENDING",
            "EVALUATING_RULES",
            "FAILED",
            "ERROR",
            "COMPLETED",
            "COMPLETED_WITH_ERRORS",
            "CANCELED",
        ],
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List[
            ClientDescribeAssessmentRunsResponseassessmentRunsuserAttributesForFindingsTypeDef
        ],
        "createdAt": datetime,
        "startedAt": datetime,
        "completedAt": datetime,
        "stateChangedAt": datetime,
        "dataCollected": bool,
        "stateChanges": List[ClientDescribeAssessmentRunsResponseassessmentRunsstateChangesTypeDef],
        "notifications": List[
            ClientDescribeAssessmentRunsResponseassessmentRunsnotificationsTypeDef
        ],
        "findingCounts": Dict[str, int],
    },
    total=False,
)


class ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef(
    _ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef
):
    """
    - *(dict) --*

      A snapshot of an Amazon Inspector assessment run that contains the findings of the assessment
      run .
      Used as the response element in the  DescribeAssessmentRuns action.
      - **arn** *(string) --*

        The ARN of the assessment run.
    """


_ClientDescribeAssessmentRunsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)


class ClientDescribeAssessmentRunsResponsefailedItemsTypeDef(
    _ClientDescribeAssessmentRunsResponsefailedItemsTypeDef
):
    pass


_ClientDescribeAssessmentRunsResponseTypeDef = TypedDict(
    "_ClientDescribeAssessmentRunsResponseTypeDef",
    {
        "assessmentRuns": List[ClientDescribeAssessmentRunsResponseassessmentRunsTypeDef],
        "failedItems": Dict[str, ClientDescribeAssessmentRunsResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeAssessmentRunsResponseTypeDef(_ClientDescribeAssessmentRunsResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentRuns** *(list) --*

        Information about the assessment run.
        - *(dict) --*

          A snapshot of an Amazon Inspector assessment run that contains the findings of the
          assessment run .
          Used as the response element in the  DescribeAssessmentRuns action.
          - **arn** *(string) --*

            The ARN of the assessment run.
    """


_ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef = TypedDict(
    "_ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef",
    {
        "arn": str,
        "name": str,
        "resourceGroupArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)


class ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef(
    _ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef
):
    """
    - *(dict) --*

      Contains information about an Amazon Inspector application. This data type is used as the
      response element in the  DescribeAssessmentTargets action.
      - **arn** *(string) --*

        The ARN that specifies the Amazon Inspector assessment target.
    """


_ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)


class ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef(
    _ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef
):
    pass


_ClientDescribeAssessmentTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargets": List[ClientDescribeAssessmentTargetsResponseassessmentTargetsTypeDef],
        "failedItems": Dict[str, ClientDescribeAssessmentTargetsResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeAssessmentTargetsResponseTypeDef(
    _ClientDescribeAssessmentTargetsResponseTypeDef
):
    """
    - *(dict) --*

      - **assessmentTargets** *(list) --*

        Information about the assessment targets.
        - *(dict) --*

          Contains information about an Amazon Inspector application. This data type is used as the
          response element in the  DescribeAssessmentTargets action.
          - **arn** *(string) --*

            The ARN that specifies the Amazon Inspector assessment target.
    """


_ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef = TypedDict(
    "_ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef(
    _ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef
):
    pass


_ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef = TypedDict(
    "_ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTargetArn": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List[
            ClientDescribeAssessmentTemplatesResponseassessmentTemplatesuserAttributesForFindingsTypeDef
        ],
        "lastAssessmentRunArn": str,
        "assessmentRunCount": int,
        "createdAt": datetime,
    },
    total=False,
)


class ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef(
    _ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef
):
    """
    - *(dict) --*

      Contains information about an Amazon Inspector assessment template. This data type is used as
      the response element in the  DescribeAssessmentTemplates action.
      - **arn** *(string) --*

        The ARN of the assessment template.
    """


_ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)


class ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef(
    _ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef
):
    pass


_ClientDescribeAssessmentTemplatesResponseTypeDef = TypedDict(
    "_ClientDescribeAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplates": List[
            ClientDescribeAssessmentTemplatesResponseassessmentTemplatesTypeDef
        ],
        "failedItems": Dict[str, ClientDescribeAssessmentTemplatesResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeAssessmentTemplatesResponseTypeDef(
    _ClientDescribeAssessmentTemplatesResponseTypeDef
):
    """
    - *(dict) --*

      - **assessmentTemplates** *(list) --*

        Information about the assessment templates.
        - *(dict) --*

          Contains information about an Amazon Inspector assessment template. This data type is used
          as the response element in the  DescribeAssessmentTemplates action.
          - **arn** *(string) --*

            The ARN of the assessment template.
    """


_ClientDescribeCrossAccountAccessRoleResponseTypeDef = TypedDict(
    "_ClientDescribeCrossAccountAccessRoleResponseTypeDef",
    {"roleArn": str, "valid": bool, "registeredAt": datetime},
    total=False,
)


class ClientDescribeCrossAccountAccessRoleResponseTypeDef(
    _ClientDescribeCrossAccountAccessRoleResponseTypeDef
):
    """
    - *(dict) --*

      - **roleArn** *(string) --*

        The ARN that specifies the IAM role that Amazon Inspector uses to access your AWS account.
    """


_ClientDescribeExclusionsResponseexclusionsattributesTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponseexclusionsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeExclusionsResponseexclusionsattributesTypeDef(
    _ClientDescribeExclusionsResponseexclusionsattributesTypeDef
):
    pass


_ClientDescribeExclusionsResponseexclusionsscopesTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponseexclusionsscopesTypeDef",
    {"key": Literal["INSTANCE_ID", "RULES_PACKAGE_ARN"], "value": str},
    total=False,
)


class ClientDescribeExclusionsResponseexclusionsscopesTypeDef(
    _ClientDescribeExclusionsResponseexclusionsscopesTypeDef
):
    pass


_ClientDescribeExclusionsResponseexclusionsTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponseexclusionsTypeDef",
    {
        "arn": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List[ClientDescribeExclusionsResponseexclusionsscopesTypeDef],
        "attributes": List[ClientDescribeExclusionsResponseexclusionsattributesTypeDef],
    },
    total=False,
)


class ClientDescribeExclusionsResponseexclusionsTypeDef(
    _ClientDescribeExclusionsResponseexclusionsTypeDef
):
    pass


_ClientDescribeExclusionsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)


class ClientDescribeExclusionsResponsefailedItemsTypeDef(
    _ClientDescribeExclusionsResponsefailedItemsTypeDef
):
    pass


_ClientDescribeExclusionsResponseTypeDef = TypedDict(
    "_ClientDescribeExclusionsResponseTypeDef",
    {
        "exclusions": Dict[str, ClientDescribeExclusionsResponseexclusionsTypeDef],
        "failedItems": Dict[str, ClientDescribeExclusionsResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeExclusionsResponseTypeDef(_ClientDescribeExclusionsResponseTypeDef):
    """
    - *(dict) --*

      - **exclusions** *(dict) --*

        Information about the exclusions.
        - *(string) --*

          - *(dict) --*

            Contains information about what was excluded from an assessment run.
            - **arn** *(string) --*

              The ARN that specifies the exclusion.
    """


_ClientDescribeFindingsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)


class ClientDescribeFindingsResponsefailedItemsTypeDef(
    _ClientDescribeFindingsResponsefailedItemsTypeDef
):
    pass


_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef",
    {"privateDnsName": str, "privateIpAddress": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef
):
    pass


_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef",
    {"groupName": str, "groupId": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef
):
    pass


_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef",
    {
        "networkInterfaceId": str,
        "subnetId": str,
        "vpcId": str,
        "privateDnsName": str,
        "privateIpAddress": str,
        "privateIpAddresses": List[
            ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesprivateIpAddressesTypeDef
        ],
        "publicDnsName": str,
        "publicIp": str,
        "ipv6Addresses": List[str],
        "securityGroups": List[
            ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacessecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef
):
    pass


_ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef
):
    pass


_ClientDescribeFindingsResponsefindingsassetAttributesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsassetAttributesTypeDef",
    {
        "schemaVersion": int,
        "agentId": str,
        "autoScalingGroup": str,
        "amiId": str,
        "hostname": str,
        "ipv4Addresses": List[str],
        "tags": List[ClientDescribeFindingsResponsefindingsassetAttributestagsTypeDef],
        "networkInterfaces": List[
            ClientDescribeFindingsResponsefindingsassetAttributesnetworkInterfacesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeFindingsResponsefindingsassetAttributesTypeDef(
    _ClientDescribeFindingsResponsefindingsassetAttributesTypeDef
):
    pass


_ClientDescribeFindingsResponsefindingsattributesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsattributesTypeDef(
    _ClientDescribeFindingsResponsefindingsattributesTypeDef
):
    pass


_ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef",
    {"schemaVersion": int, "assessmentRunArn": str, "rulesPackageArn": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef(
    _ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef
):
    pass


_ClientDescribeFindingsResponsefindingsuserAttributesTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsuserAttributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeFindingsResponsefindingsuserAttributesTypeDef(
    _ClientDescribeFindingsResponsefindingsuserAttributesTypeDef
):
    pass


_ClientDescribeFindingsResponsefindingsTypeDef = TypedDict(
    "_ClientDescribeFindingsResponsefindingsTypeDef",
    {
        "arn": str,
        "schemaVersion": int,
        "service": str,
        "serviceAttributes": ClientDescribeFindingsResponsefindingsserviceAttributesTypeDef,
        "assetType": str,
        "assetAttributes": ClientDescribeFindingsResponsefindingsassetAttributesTypeDef,
        "id": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "severity": Literal["Low", "Medium", "High", "Informational", "Undefined"],
        "numericSeverity": float,
        "confidence": int,
        "indicatorOfCompromise": bool,
        "attributes": List[ClientDescribeFindingsResponsefindingsattributesTypeDef],
        "userAttributes": List[ClientDescribeFindingsResponsefindingsuserAttributesTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)


class ClientDescribeFindingsResponsefindingsTypeDef(_ClientDescribeFindingsResponsefindingsTypeDef):
    """
    - *(dict) --*

      Contains information about an Amazon Inspector finding. This data type is used as the response
      element in the  DescribeFindings action.
      - **arn** *(string) --*

        The ARN that specifies the finding.
    """


_ClientDescribeFindingsResponseTypeDef = TypedDict(
    "_ClientDescribeFindingsResponseTypeDef",
    {
        "findings": List[ClientDescribeFindingsResponsefindingsTypeDef],
        "failedItems": Dict[str, ClientDescribeFindingsResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeFindingsResponseTypeDef(_ClientDescribeFindingsResponseTypeDef):
    """
    - *(dict) --*

      - **findings** *(list) --*

        Information about the finding.
        - *(dict) --*

          Contains information about an Amazon Inspector finding. This data type is used as the
          response element in the  DescribeFindings action.
          - **arn** *(string) --*

            The ARN that specifies the finding.
    """


_ClientDescribeResourceGroupsResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeResourceGroupsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)


class ClientDescribeResourceGroupsResponsefailedItemsTypeDef(
    _ClientDescribeResourceGroupsResponsefailedItemsTypeDef
):
    pass


_ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef = TypedDict(
    "_ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef(
    _ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef
):
    pass


_ClientDescribeResourceGroupsResponseresourceGroupsTypeDef = TypedDict(
    "_ClientDescribeResourceGroupsResponseresourceGroupsTypeDef",
    {
        "arn": str,
        "tags": List[ClientDescribeResourceGroupsResponseresourceGroupstagsTypeDef],
        "createdAt": datetime,
    },
    total=False,
)


class ClientDescribeResourceGroupsResponseresourceGroupsTypeDef(
    _ClientDescribeResourceGroupsResponseresourceGroupsTypeDef
):
    """
    - *(dict) --*

      Contains information about a resource group. The resource group defines a set of tags that,
      when queried, identify the AWS resources that make up the assessment target. This data type is
      used as the response element in the  DescribeResourceGroups action.
      - **arn** *(string) --*

        The ARN of the resource group.
    """


_ClientDescribeResourceGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeResourceGroupsResponseTypeDef",
    {
        "resourceGroups": List[ClientDescribeResourceGroupsResponseresourceGroupsTypeDef],
        "failedItems": Dict[str, ClientDescribeResourceGroupsResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeResourceGroupsResponseTypeDef(_ClientDescribeResourceGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **resourceGroups** *(list) --*

        Information about a resource group.
        - *(dict) --*

          Contains information about a resource group. The resource group defines a set of tags
          that, when queried, identify the AWS resources that make up the assessment target. This
          data type is used as the response element in the  DescribeResourceGroups action.
          - **arn** *(string) --*

            The ARN of the resource group.
    """


_ClientDescribeRulesPackagesResponsefailedItemsTypeDef = TypedDict(
    "_ClientDescribeRulesPackagesResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)


class ClientDescribeRulesPackagesResponsefailedItemsTypeDef(
    _ClientDescribeRulesPackagesResponsefailedItemsTypeDef
):
    pass


_ClientDescribeRulesPackagesResponserulesPackagesTypeDef = TypedDict(
    "_ClientDescribeRulesPackagesResponserulesPackagesTypeDef",
    {"arn": str, "name": str, "version": str, "provider": str, "description": str},
    total=False,
)


class ClientDescribeRulesPackagesResponserulesPackagesTypeDef(
    _ClientDescribeRulesPackagesResponserulesPackagesTypeDef
):
    """
    - *(dict) --*

      Contains information about an Amazon Inspector rules package. This data type is used as the
      response element in the  DescribeRulesPackages action.
      - **arn** *(string) --*

        The ARN of the rules package.
    """


_ClientDescribeRulesPackagesResponseTypeDef = TypedDict(
    "_ClientDescribeRulesPackagesResponseTypeDef",
    {
        "rulesPackages": List[ClientDescribeRulesPackagesResponserulesPackagesTypeDef],
        "failedItems": Dict[str, ClientDescribeRulesPackagesResponsefailedItemsTypeDef],
    },
    total=False,
)


class ClientDescribeRulesPackagesResponseTypeDef(_ClientDescribeRulesPackagesResponseTypeDef):
    """
    - *(dict) --*

      - **rulesPackages** *(list) --*

        Information about the rules package.
        - *(dict) --*

          Contains information about an Amazon Inspector rules package. This data type is used as
          the response element in the  DescribeRulesPackages action.
          - **arn** *(string) --*

            The ARN of the rules package.
    """


_ClientGetAssessmentReportResponseTypeDef = TypedDict(
    "_ClientGetAssessmentReportResponseTypeDef",
    {"status": Literal["WORK_IN_PROGRESS", "FAILED", "COMPLETED"], "url": str},
    total=False,
)


class ClientGetAssessmentReportResponseTypeDef(_ClientGetAssessmentReportResponseTypeDef):
    """
    - *(dict) --*

      - **status** *(string) --*

        Specifies the status of the request to generate an assessment report.
    """


_ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef = TypedDict(
    "_ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef(
    _ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef
):
    pass


_ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef = TypedDict(
    "_ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef",
    {"key": Literal["INSTANCE_ID", "RULES_PACKAGE_ARN"], "value": str},
    total=False,
)


class ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef(
    _ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef
):
    pass


_ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef = TypedDict(
    "_ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef",
    {
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List[ClientGetExclusionsPreviewResponseexclusionPreviewsscopesTypeDef],
        "attributes": List[ClientGetExclusionsPreviewResponseexclusionPreviewsattributesTypeDef],
    },
    total=False,
)


class ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef(
    _ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef
):
    pass


_ClientGetExclusionsPreviewResponseTypeDef = TypedDict(
    "_ClientGetExclusionsPreviewResponseTypeDef",
    {
        "previewStatus": Literal["WORK_IN_PROGRESS", "COMPLETED"],
        "exclusionPreviews": List[ClientGetExclusionsPreviewResponseexclusionPreviewsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetExclusionsPreviewResponseTypeDef(_ClientGetExclusionsPreviewResponseTypeDef):
    """
    - *(dict) --*

      - **previewStatus** *(string) --*

        Specifies the status of the request to generate an exclusions preview.
    """


_ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef = TypedDict(
    "_ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef",
    {"messageType": str, "count": int, "dataSize": int},
    total=False,
)


class ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef(
    _ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef
):
    """
    - *(dict) --*

      The metadata about the Amazon Inspector application data metrics collected by the agent. This
      data type is used as the response element in the  GetTelemetryMetadata action.
      - **messageType** *(string) --*

        A specific type of behavioral data that is collected by the agent.
    """


_ClientGetTelemetryMetadataResponseTypeDef = TypedDict(
    "_ClientGetTelemetryMetadataResponseTypeDef",
    {"telemetryMetadata": List[ClientGetTelemetryMetadataResponsetelemetryMetadataTypeDef]},
    total=False,
)


class ClientGetTelemetryMetadataResponseTypeDef(_ClientGetTelemetryMetadataResponseTypeDef):
    """
    - *(dict) --*

      - **telemetryMetadata** *(list) --*

        Telemetry details.
        - *(dict) --*

          The metadata about the Amazon Inspector application data metrics collected by the agent.
          This data type is used as the response element in the  GetTelemetryMetadata action.
          - **messageType** *(string) --*

            A specific type of behavioral data that is collected by the agent.
    """


_RequiredClientListAssessmentRunAgentsFilterTypeDef = TypedDict(
    "_RequiredClientListAssessmentRunAgentsFilterTypeDef",
    {"agentHealths": List[Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]]},
)
_OptionalClientListAssessmentRunAgentsFilterTypeDef = TypedDict(
    "_OptionalClientListAssessmentRunAgentsFilterTypeDef",
    {
        "agentHealthCodes": List[
            Literal["IDLE", "RUNNING", "SHUTDOWN", "UNHEALTHY", "THROTTLED", "UNKNOWN"]
        ]
    },
    total=False,
)


class ClientListAssessmentRunAgentsFilterTypeDef(
    _RequiredClientListAssessmentRunAgentsFilterTypeDef,
    _OptionalClientListAssessmentRunAgentsFilterTypeDef,
):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **agentHealths** *(list) --***[REQUIRED]**

      The current health state of the agent. Values can be set to **HEALTHY** or **UNHEALTHY** .
      - *(string) --*
    """


_ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef = TypedDict(
    "_ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef",
    {"messageType": str, "count": int, "dataSize": int},
    total=False,
)


class ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef(
    _ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef
):
    pass


_ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef = TypedDict(
    "_ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "agentHealthCode": Literal[
            "IDLE", "RUNNING", "SHUTDOWN", "UNHEALTHY", "THROTTLED", "UNKNOWN"
        ],
        "agentHealthDetails": str,
        "autoScalingGroup": str,
        "telemetryMetadata": List[
            ClientListAssessmentRunAgentsResponseassessmentRunAgentstelemetryMetadataTypeDef
        ],
    },
    total=False,
)


class ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef(
    _ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef
):
    """
    - *(dict) --*

      Contains information about an Amazon Inspector agent. This data type is used as a response
      element in the  ListAssessmentRunAgents action.
      - **agentId** *(string) --*

        The AWS account of the EC2 instance where the agent is installed.
    """


_ClientListAssessmentRunAgentsResponseTypeDef = TypedDict(
    "_ClientListAssessmentRunAgentsResponseTypeDef",
    {
        "assessmentRunAgents": List[
            ClientListAssessmentRunAgentsResponseassessmentRunAgentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListAssessmentRunAgentsResponseTypeDef(_ClientListAssessmentRunAgentsResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentRunAgents** *(list) --*

        A list of ARNs that specifies the agents returned by the action.
        - *(dict) --*

          Contains information about an Amazon Inspector agent. This data type is used as a response
          element in the  ListAssessmentRunAgents action.
          - **agentId** *(string) --*

            The AWS account of the EC2 instance where the agent is installed.
    """


_ClientListAssessmentRunsFiltercompletionTimeRangeTypeDef = TypedDict(
    "_ClientListAssessmentRunsFiltercompletionTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ClientListAssessmentRunsFiltercompletionTimeRangeTypeDef(
    _ClientListAssessmentRunsFiltercompletionTimeRangeTypeDef
):
    pass


_ClientListAssessmentRunsFilterdurationRangeTypeDef = TypedDict(
    "_ClientListAssessmentRunsFilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)


class ClientListAssessmentRunsFilterdurationRangeTypeDef(
    _ClientListAssessmentRunsFilterdurationRangeTypeDef
):
    pass


_ClientListAssessmentRunsFilterstartTimeRangeTypeDef = TypedDict(
    "_ClientListAssessmentRunsFilterstartTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ClientListAssessmentRunsFilterstartTimeRangeTypeDef(
    _ClientListAssessmentRunsFilterstartTimeRangeTypeDef
):
    pass


_ClientListAssessmentRunsFilterstateChangeTimeRangeTypeDef = TypedDict(
    "_ClientListAssessmentRunsFilterstateChangeTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ClientListAssessmentRunsFilterstateChangeTimeRangeTypeDef(
    _ClientListAssessmentRunsFilterstateChangeTimeRangeTypeDef
):
    pass


_ClientListAssessmentRunsFilterTypeDef = TypedDict(
    "_ClientListAssessmentRunsFilterTypeDef",
    {
        "namePattern": str,
        "states": List[
            Literal[
                "CREATED",
                "START_DATA_COLLECTION_PENDING",
                "START_DATA_COLLECTION_IN_PROGRESS",
                "COLLECTING_DATA",
                "STOP_DATA_COLLECTION_PENDING",
                "DATA_COLLECTED",
                "START_EVALUATING_RULES_PENDING",
                "EVALUATING_RULES",
                "FAILED",
                "ERROR",
                "COMPLETED",
                "COMPLETED_WITH_ERRORS",
                "CANCELED",
            ]
        ],
        "durationRange": ClientListAssessmentRunsFilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
        "startTimeRange": ClientListAssessmentRunsFilterstartTimeRangeTypeDef,
        "completionTimeRange": ClientListAssessmentRunsFiltercompletionTimeRangeTypeDef,
        "stateChangeTimeRange": ClientListAssessmentRunsFilterstateChangeTimeRangeTypeDef,
    },
    total=False,
)


class ClientListAssessmentRunsFilterTypeDef(_ClientListAssessmentRunsFilterTypeDef):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **namePattern** *(string) --*

      For a record to match a filter, an explicit value or a string containing a wildcard that is
      specified for this data type property must match the value of the **assessmentRunName**
      property of the  AssessmentRun data type.
    """


_ClientListAssessmentRunsResponseTypeDef = TypedDict(
    "_ClientListAssessmentRunsResponseTypeDef",
    {"assessmentRunArns": List[str], "nextToken": str},
    total=False,
)


class ClientListAssessmentRunsResponseTypeDef(_ClientListAssessmentRunsResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentRunArns** *(list) --*

        A list of ARNs that specifies the assessment runs that are returned by the action.
        - *(string) --*
    """


_ClientListAssessmentTargetsFilterTypeDef = TypedDict(
    "_ClientListAssessmentTargetsFilterTypeDef", {"assessmentTargetNamePattern": str}, total=False
)


class ClientListAssessmentTargetsFilterTypeDef(_ClientListAssessmentTargetsFilterTypeDef):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **assessmentTargetNamePattern** *(string) --*

      For a record to match a filter, an explicit value or a string that contains a wildcard that is
      specified for this data type property must match the value of the **assessmentTargetName**
      property of the  AssessmentTarget data type.
    """


_ClientListAssessmentTargetsResponseTypeDef = TypedDict(
    "_ClientListAssessmentTargetsResponseTypeDef",
    {"assessmentTargetArns": List[str], "nextToken": str},
    total=False,
)


class ClientListAssessmentTargetsResponseTypeDef(_ClientListAssessmentTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentTargetArns** *(list) --*

        A list of ARNs that specifies the assessment targets that are returned by the action.
        - *(string) --*
    """


_ClientListAssessmentTemplatesFilterdurationRangeTypeDef = TypedDict(
    "_ClientListAssessmentTemplatesFilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)


class ClientListAssessmentTemplatesFilterdurationRangeTypeDef(
    _ClientListAssessmentTemplatesFilterdurationRangeTypeDef
):
    pass


_ClientListAssessmentTemplatesFilterTypeDef = TypedDict(
    "_ClientListAssessmentTemplatesFilterTypeDef",
    {
        "namePattern": str,
        "durationRange": ClientListAssessmentTemplatesFilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
    },
    total=False,
)


class ClientListAssessmentTemplatesFilterTypeDef(_ClientListAssessmentTemplatesFilterTypeDef):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **namePattern** *(string) --*

      For a record to match a filter, an explicit value or a string that contains a wildcard that is
      specified for this data type property must match the value of the **assessmentTemplateName**
      property of the  AssessmentTemplate data type.
    """


_ClientListAssessmentTemplatesResponseTypeDef = TypedDict(
    "_ClientListAssessmentTemplatesResponseTypeDef",
    {"assessmentTemplateArns": List[str], "nextToken": str},
    total=False,
)


class ClientListAssessmentTemplatesResponseTypeDef(_ClientListAssessmentTemplatesResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentTemplateArns** *(list) --*

        A list of ARNs that specifies the assessment templates returned by the action.
        - *(string) --*
    """


_ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef = TypedDict(
    "_ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef",
    {
        "event": Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        "subscribedAt": datetime,
    },
    total=False,
)


class ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef(
    _ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef
):
    pass


_ClientListEventSubscriptionsResponsesubscriptionsTypeDef = TypedDict(
    "_ClientListEventSubscriptionsResponsesubscriptionsTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List[
            ClientListEventSubscriptionsResponsesubscriptionseventSubscriptionsTypeDef
        ],
    },
    total=False,
)


class ClientListEventSubscriptionsResponsesubscriptionsTypeDef(
    _ClientListEventSubscriptionsResponsesubscriptionsTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element in the  ListEventSubscriptions action.
      - **resourceArn** *(string) --*

        The ARN of the assessment template that is used during the event for which the SNS
        notification is sent.
    """


_ClientListEventSubscriptionsResponseTypeDef = TypedDict(
    "_ClientListEventSubscriptionsResponseTypeDef",
    {
        "subscriptions": List[ClientListEventSubscriptionsResponsesubscriptionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListEventSubscriptionsResponseTypeDef(_ClientListEventSubscriptionsResponseTypeDef):
    """
    - *(dict) --*

      - **subscriptions** *(list) --*

        Details of the returned event subscriptions.
        - *(dict) --*

          This data type is used as a response element in the  ListEventSubscriptions action.
          - **resourceArn** *(string) --*

            The ARN of the assessment template that is used during the event for which the SNS
            notification is sent.
    """


_ClientListExclusionsResponseTypeDef = TypedDict(
    "_ClientListExclusionsResponseTypeDef",
    {"exclusionArns": List[str], "nextToken": str},
    total=False,
)


class ClientListExclusionsResponseTypeDef(_ClientListExclusionsResponseTypeDef):
    """
    - *(dict) --*

      - **exclusionArns** *(list) --*

        A list of exclusions' ARNs returned by the action.
        - *(string) --*
    """


_ClientListFindingsFilterattributesTypeDef = TypedDict(
    "_ClientListFindingsFilterattributesTypeDef", {"key": str, "value": str}, total=False
)


class ClientListFindingsFilterattributesTypeDef(_ClientListFindingsFilterattributesTypeDef):
    pass


_ClientListFindingsFiltercreationTimeRangeTypeDef = TypedDict(
    "_ClientListFindingsFiltercreationTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ClientListFindingsFiltercreationTimeRangeTypeDef(
    _ClientListFindingsFiltercreationTimeRangeTypeDef
):
    pass


_ClientListFindingsFilteruserAttributesTypeDef = TypedDict(
    "_ClientListFindingsFilteruserAttributesTypeDef", {"key": str, "value": str}, total=False
)


class ClientListFindingsFilteruserAttributesTypeDef(_ClientListFindingsFilteruserAttributesTypeDef):
    pass


_ClientListFindingsFilterTypeDef = TypedDict(
    "_ClientListFindingsFilterTypeDef",
    {
        "agentIds": List[str],
        "autoScalingGroups": List[str],
        "ruleNames": List[str],
        "severities": List[Literal["Low", "Medium", "High", "Informational", "Undefined"]],
        "rulesPackageArns": List[str],
        "attributes": List[ClientListFindingsFilterattributesTypeDef],
        "userAttributes": List[ClientListFindingsFilteruserAttributesTypeDef],
        "creationTimeRange": ClientListFindingsFiltercreationTimeRangeTypeDef,
    },
    total=False,
)


class ClientListFindingsFilterTypeDef(_ClientListFindingsFilterTypeDef):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **agentIds** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type
      property must be the exact match of the value of the **agentId** property of the  Finding data
      type.
      - *(string) --*
    """


_ClientListFindingsResponseTypeDef = TypedDict(
    "_ClientListFindingsResponseTypeDef", {"findingArns": List[str], "nextToken": str}, total=False
)


class ClientListFindingsResponseTypeDef(_ClientListFindingsResponseTypeDef):
    """
    - *(dict) --*

      - **findingArns** *(list) --*

        A list of ARNs that specifies the findings returned by the action.
        - *(string) --*
    """


_ClientListRulesPackagesResponseTypeDef = TypedDict(
    "_ClientListRulesPackagesResponseTypeDef",
    {"rulesPackageArns": List[str], "nextToken": str},
    total=False,
)


class ClientListRulesPackagesResponseTypeDef(_ClientListRulesPackagesResponseTypeDef):
    """
    - *(dict) --*

      - **rulesPackageArns** *(list) --*

        The list of ARNs that specifies the rules packages returned by the action.
        - *(string) --*
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    """
    - *(dict) --*

      A key and value pair. This data type is used as a request parameter in the  SetTagsForResource
      action and a response element in the  ListTagsForResource action.
      - **key** *(string) --*

        A tag key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        A collection of key and value pairs.
        - *(dict) --*

          A key and value pair. This data type is used as a request parameter in the
          SetTagsForResource action and a response element in the  ListTagsForResource action.
          - **key** *(string) --*

            A tag key.
    """


_ClientPreviewAgentsResponseagentPreviewsTypeDef = TypedDict(
    "_ClientPreviewAgentsResponseagentPreviewsTypeDef",
    {
        "hostname": str,
        "agentId": str,
        "autoScalingGroup": str,
        "agentHealth": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "agentVersion": str,
        "operatingSystem": str,
        "kernelVersion": str,
        "ipv4Address": str,
    },
    total=False,
)


class ClientPreviewAgentsResponseagentPreviewsTypeDef(
    _ClientPreviewAgentsResponseagentPreviewsTypeDef
):
    """
    - *(dict) --*

      Used as a response element in the  PreviewAgents action.
      - **hostname** *(string) --*

        The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.
    """


_ClientPreviewAgentsResponseTypeDef = TypedDict(
    "_ClientPreviewAgentsResponseTypeDef",
    {"agentPreviews": List[ClientPreviewAgentsResponseagentPreviewsTypeDef], "nextToken": str},
    total=False,
)


class ClientPreviewAgentsResponseTypeDef(_ClientPreviewAgentsResponseTypeDef):
    """
    - *(dict) --*

      - **agentPreviews** *(list) --*

        The resulting list of agents.
        - *(dict) --*

          Used as a response element in the  PreviewAgents action.
          - **hostname** *(string) --*

            The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.
    """


_ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef = TypedDict(
    "_ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef",
    {
        "failureCode": Literal[
            "INVALID_ARN",
            "DUPLICATE_ARN",
            "ITEM_DOES_NOT_EXIST",
            "ACCESS_DENIED",
            "LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "retryable": bool,
    },
    total=False,
)


class ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef(
    _ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef
):
    pass


_ClientRemoveAttributesFromFindingsResponseTypeDef = TypedDict(
    "_ClientRemoveAttributesFromFindingsResponseTypeDef",
    {"failedItems": Dict[str, ClientRemoveAttributesFromFindingsResponsefailedItemsTypeDef]},
    total=False,
)


class ClientRemoveAttributesFromFindingsResponseTypeDef(
    _ClientRemoveAttributesFromFindingsResponseTypeDef
):
    """
    - *(dict) --*

      - **failedItems** *(dict) --*

        Attributes details that cannot be described. An error code is provided for each failed item.
        - *(string) --*

          - *(dict) --*

            Includes details about the failed items.
            - **failureCode** *(string) --*

              The status code of a failed item.
    """


_RequiredClientSetTagsForResourceTagsTypeDef = TypedDict(
    "_RequiredClientSetTagsForResourceTagsTypeDef", {"key": str}
)
_OptionalClientSetTagsForResourceTagsTypeDef = TypedDict(
    "_OptionalClientSetTagsForResourceTagsTypeDef", {"value": str}, total=False
)


class ClientSetTagsForResourceTagsTypeDef(
    _RequiredClientSetTagsForResourceTagsTypeDef, _OptionalClientSetTagsForResourceTagsTypeDef
):
    """
    - *(dict) --*

      A key and value pair. This data type is used as a request parameter in the  SetTagsForResource
      action and a response element in the  ListTagsForResource action.
      - **key** *(string) --***[REQUIRED]**

        A tag key.
    """


_ClientStartAssessmentRunResponseTypeDef = TypedDict(
    "_ClientStartAssessmentRunResponseTypeDef", {"assessmentRunArn": str}, total=False
)


class ClientStartAssessmentRunResponseTypeDef(_ClientStartAssessmentRunResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentRunArn** *(string) --*

        The ARN of the assessment run that has been started.
    """


_RequiredListAssessmentRunAgentsPaginateFilterTypeDef = TypedDict(
    "_RequiredListAssessmentRunAgentsPaginateFilterTypeDef",
    {"agentHealths": List[Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]]},
)
_OptionalListAssessmentRunAgentsPaginateFilterTypeDef = TypedDict(
    "_OptionalListAssessmentRunAgentsPaginateFilterTypeDef",
    {
        "agentHealthCodes": List[
            Literal["IDLE", "RUNNING", "SHUTDOWN", "UNHEALTHY", "THROTTLED", "UNKNOWN"]
        ]
    },
    total=False,
)


class ListAssessmentRunAgentsPaginateFilterTypeDef(
    _RequiredListAssessmentRunAgentsPaginateFilterTypeDef,
    _OptionalListAssessmentRunAgentsPaginateFilterTypeDef,
):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **agentHealths** *(list) --***[REQUIRED]**

      The current health state of the agent. Values can be set to **HEALTHY** or **UNHEALTHY** .
      - *(string) --*
    """


_ListAssessmentRunAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssessmentRunAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssessmentRunAgentsPaginatePaginationConfigTypeDef(
    _ListAssessmentRunAgentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef = TypedDict(
    "_ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef",
    {"messageType": str, "count": int, "dataSize": int},
    total=False,
)


class ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef(
    _ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef
):
    pass


_ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef = TypedDict(
    "_ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "agentHealthCode": Literal[
            "IDLE", "RUNNING", "SHUTDOWN", "UNHEALTHY", "THROTTLED", "UNKNOWN"
        ],
        "agentHealthDetails": str,
        "autoScalingGroup": str,
        "telemetryMetadata": List[
            ListAssessmentRunAgentsPaginateResponseassessmentRunAgentstelemetryMetadataTypeDef
        ],
    },
    total=False,
)


class ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef(
    _ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef
):
    """
    - *(dict) --*

      Contains information about an Amazon Inspector agent. This data type is used as a response
      element in the  ListAssessmentRunAgents action.
      - **agentId** *(string) --*

        The AWS account of the EC2 instance where the agent is installed.
    """


_ListAssessmentRunAgentsPaginateResponseTypeDef = TypedDict(
    "_ListAssessmentRunAgentsPaginateResponseTypeDef",
    {
        "assessmentRunAgents": List[
            ListAssessmentRunAgentsPaginateResponseassessmentRunAgentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListAssessmentRunAgentsPaginateResponseTypeDef(
    _ListAssessmentRunAgentsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **assessmentRunAgents** *(list) --*

        A list of ARNs that specifies the agents returned by the action.
        - *(dict) --*

          Contains information about an Amazon Inspector agent. This data type is used as a response
          element in the  ListAssessmentRunAgents action.
          - **agentId** *(string) --*

            The AWS account of the EC2 instance where the agent is installed.
    """


_ListAssessmentRunsPaginateFiltercompletionTimeRangeTypeDef = TypedDict(
    "_ListAssessmentRunsPaginateFiltercompletionTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ListAssessmentRunsPaginateFiltercompletionTimeRangeTypeDef(
    _ListAssessmentRunsPaginateFiltercompletionTimeRangeTypeDef
):
    pass


_ListAssessmentRunsPaginateFilterdurationRangeTypeDef = TypedDict(
    "_ListAssessmentRunsPaginateFilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)


class ListAssessmentRunsPaginateFilterdurationRangeTypeDef(
    _ListAssessmentRunsPaginateFilterdurationRangeTypeDef
):
    pass


_ListAssessmentRunsPaginateFilterstartTimeRangeTypeDef = TypedDict(
    "_ListAssessmentRunsPaginateFilterstartTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ListAssessmentRunsPaginateFilterstartTimeRangeTypeDef(
    _ListAssessmentRunsPaginateFilterstartTimeRangeTypeDef
):
    pass


_ListAssessmentRunsPaginateFilterstateChangeTimeRangeTypeDef = TypedDict(
    "_ListAssessmentRunsPaginateFilterstateChangeTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ListAssessmentRunsPaginateFilterstateChangeTimeRangeTypeDef(
    _ListAssessmentRunsPaginateFilterstateChangeTimeRangeTypeDef
):
    pass


_ListAssessmentRunsPaginateFilterTypeDef = TypedDict(
    "_ListAssessmentRunsPaginateFilterTypeDef",
    {
        "namePattern": str,
        "states": List[
            Literal[
                "CREATED",
                "START_DATA_COLLECTION_PENDING",
                "START_DATA_COLLECTION_IN_PROGRESS",
                "COLLECTING_DATA",
                "STOP_DATA_COLLECTION_PENDING",
                "DATA_COLLECTED",
                "START_EVALUATING_RULES_PENDING",
                "EVALUATING_RULES",
                "FAILED",
                "ERROR",
                "COMPLETED",
                "COMPLETED_WITH_ERRORS",
                "CANCELED",
            ]
        ],
        "durationRange": ListAssessmentRunsPaginateFilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
        "startTimeRange": ListAssessmentRunsPaginateFilterstartTimeRangeTypeDef,
        "completionTimeRange": ListAssessmentRunsPaginateFiltercompletionTimeRangeTypeDef,
        "stateChangeTimeRange": ListAssessmentRunsPaginateFilterstateChangeTimeRangeTypeDef,
    },
    total=False,
)


class ListAssessmentRunsPaginateFilterTypeDef(_ListAssessmentRunsPaginateFilterTypeDef):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **namePattern** *(string) --*

      For a record to match a filter, an explicit value or a string containing a wildcard that is
      specified for this data type property must match the value of the **assessmentRunName**
      property of the  AssessmentRun data type.
    """


_ListAssessmentRunsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssessmentRunsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssessmentRunsPaginatePaginationConfigTypeDef(
    _ListAssessmentRunsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssessmentRunsPaginateResponseTypeDef = TypedDict(
    "_ListAssessmentRunsPaginateResponseTypeDef",
    {"assessmentRunArns": List[str], "NextToken": str},
    total=False,
)


class ListAssessmentRunsPaginateResponseTypeDef(_ListAssessmentRunsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentRunArns** *(list) --*

        A list of ARNs that specifies the assessment runs that are returned by the action.
        - *(string) --*
    """


_ListAssessmentTargetsPaginateFilterTypeDef = TypedDict(
    "_ListAssessmentTargetsPaginateFilterTypeDef", {"assessmentTargetNamePattern": str}, total=False
)


class ListAssessmentTargetsPaginateFilterTypeDef(_ListAssessmentTargetsPaginateFilterTypeDef):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **assessmentTargetNamePattern** *(string) --*

      For a record to match a filter, an explicit value or a string that contains a wildcard that is
      specified for this data type property must match the value of the **assessmentTargetName**
      property of the  AssessmentTarget data type.
    """


_ListAssessmentTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssessmentTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssessmentTargetsPaginatePaginationConfigTypeDef(
    _ListAssessmentTargetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssessmentTargetsPaginateResponseTypeDef = TypedDict(
    "_ListAssessmentTargetsPaginateResponseTypeDef",
    {"assessmentTargetArns": List[str], "NextToken": str},
    total=False,
)


class ListAssessmentTargetsPaginateResponseTypeDef(_ListAssessmentTargetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **assessmentTargetArns** *(list) --*

        A list of ARNs that specifies the assessment targets that are returned by the action.
        - *(string) --*
    """


_ListAssessmentTemplatesPaginateFilterdurationRangeTypeDef = TypedDict(
    "_ListAssessmentTemplatesPaginateFilterdurationRangeTypeDef",
    {"minSeconds": int, "maxSeconds": int},
    total=False,
)


class ListAssessmentTemplatesPaginateFilterdurationRangeTypeDef(
    _ListAssessmentTemplatesPaginateFilterdurationRangeTypeDef
):
    pass


_ListAssessmentTemplatesPaginateFilterTypeDef = TypedDict(
    "_ListAssessmentTemplatesPaginateFilterTypeDef",
    {
        "namePattern": str,
        "durationRange": ListAssessmentTemplatesPaginateFilterdurationRangeTypeDef,
        "rulesPackageArns": List[str],
    },
    total=False,
)


class ListAssessmentTemplatesPaginateFilterTypeDef(_ListAssessmentTemplatesPaginateFilterTypeDef):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **namePattern** *(string) --*

      For a record to match a filter, an explicit value or a string that contains a wildcard that is
      specified for this data type property must match the value of the **assessmentTemplateName**
      property of the  AssessmentTemplate data type.
    """


_ListAssessmentTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssessmentTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssessmentTemplatesPaginatePaginationConfigTypeDef(
    _ListAssessmentTemplatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssessmentTemplatesPaginateResponseTypeDef = TypedDict(
    "_ListAssessmentTemplatesPaginateResponseTypeDef",
    {"assessmentTemplateArns": List[str], "NextToken": str},
    total=False,
)


class ListAssessmentTemplatesPaginateResponseTypeDef(
    _ListAssessmentTemplatesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **assessmentTemplateArns** *(list) --*

        A list of ARNs that specifies the assessment templates returned by the action.
        - *(string) --*
    """


_ListEventSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEventSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEventSubscriptionsPaginatePaginationConfigTypeDef(
    _ListEventSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef = TypedDict(
    "_ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef",
    {
        "event": Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        "subscribedAt": datetime,
    },
    total=False,
)


class ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef(
    _ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef
):
    pass


_ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef = TypedDict(
    "_ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List[
            ListEventSubscriptionsPaginateResponsesubscriptionseventSubscriptionsTypeDef
        ],
    },
    total=False,
)


class ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef(
    _ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef
):
    """
    - *(dict) --*

      This data type is used as a response element in the  ListEventSubscriptions action.
      - **resourceArn** *(string) --*

        The ARN of the assessment template that is used during the event for which the SNS
        notification is sent.
    """


_ListEventSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_ListEventSubscriptionsPaginateResponseTypeDef",
    {
        "subscriptions": List[ListEventSubscriptionsPaginateResponsesubscriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListEventSubscriptionsPaginateResponseTypeDef(_ListEventSubscriptionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **subscriptions** *(list) --*

        Details of the returned event subscriptions.
        - *(dict) --*

          This data type is used as a response element in the  ListEventSubscriptions action.
          - **resourceArn** *(string) --*

            The ARN of the assessment template that is used during the event for which the SNS
            notification is sent.
    """


_ListExclusionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListExclusionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListExclusionsPaginatePaginationConfigTypeDef(_ListExclusionsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListExclusionsPaginateResponseTypeDef = TypedDict(
    "_ListExclusionsPaginateResponseTypeDef",
    {"exclusionArns": List[str], "NextToken": str},
    total=False,
)


class ListExclusionsPaginateResponseTypeDef(_ListExclusionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **exclusionArns** *(list) --*

        A list of exclusions' ARNs returned by the action.
        - *(string) --*
    """


_ListFindingsPaginateFilterattributesTypeDef = TypedDict(
    "_ListFindingsPaginateFilterattributesTypeDef", {"key": str, "value": str}, total=False
)


class ListFindingsPaginateFilterattributesTypeDef(_ListFindingsPaginateFilterattributesTypeDef):
    pass


_ListFindingsPaginateFiltercreationTimeRangeTypeDef = TypedDict(
    "_ListFindingsPaginateFiltercreationTimeRangeTypeDef",
    {"beginDate": datetime, "endDate": datetime},
    total=False,
)


class ListFindingsPaginateFiltercreationTimeRangeTypeDef(
    _ListFindingsPaginateFiltercreationTimeRangeTypeDef
):
    pass


_ListFindingsPaginateFilteruserAttributesTypeDef = TypedDict(
    "_ListFindingsPaginateFilteruserAttributesTypeDef", {"key": str, "value": str}, total=False
)


class ListFindingsPaginateFilteruserAttributesTypeDef(
    _ListFindingsPaginateFilteruserAttributesTypeDef
):
    pass


_ListFindingsPaginateFilterTypeDef = TypedDict(
    "_ListFindingsPaginateFilterTypeDef",
    {
        "agentIds": List[str],
        "autoScalingGroups": List[str],
        "ruleNames": List[str],
        "severities": List[Literal["Low", "Medium", "High", "Informational", "Undefined"]],
        "rulesPackageArns": List[str],
        "attributes": List[ListFindingsPaginateFilterattributesTypeDef],
        "userAttributes": List[ListFindingsPaginateFilteruserAttributesTypeDef],
        "creationTimeRange": ListFindingsPaginateFiltercreationTimeRangeTypeDef,
    },
    total=False,
)


class ListFindingsPaginateFilterTypeDef(_ListFindingsPaginateFilterTypeDef):
    """
    You can use this parameter to specify a subset of data to be included in the action's response.
    For a record to match a filter, all specified filter attributes must match. When multiple values
    are specified for a filter attribute, any of the values can match.
    - **agentIds** *(list) --*

      For a record to match a filter, one of the values that is specified for this data type
      property must be the exact match of the value of the **agentId** property of the  Finding data
      type.
      - *(string) --*
    """


_ListFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFindingsPaginatePaginationConfigTypeDef(_ListFindingsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFindingsPaginateResponseTypeDef = TypedDict(
    "_ListFindingsPaginateResponseTypeDef",
    {"findingArns": List[str], "NextToken": str},
    total=False,
)


class ListFindingsPaginateResponseTypeDef(_ListFindingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **findingArns** *(list) --*

        A list of ARNs that specifies the findings returned by the action.
        - *(string) --*
    """


_ListRulesPackagesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRulesPackagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRulesPackagesPaginatePaginationConfigTypeDef(
    _ListRulesPackagesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRulesPackagesPaginateResponseTypeDef = TypedDict(
    "_ListRulesPackagesPaginateResponseTypeDef",
    {"rulesPackageArns": List[str], "NextToken": str},
    total=False,
)


class ListRulesPackagesPaginateResponseTypeDef(_ListRulesPackagesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **rulesPackageArns** *(list) --*

        The list of ARNs that specifies the rules packages returned by the action.
        - *(string) --*
    """


_PreviewAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "_PreviewAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class PreviewAgentsPaginatePaginationConfigTypeDef(_PreviewAgentsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_PreviewAgentsPaginateResponseagentPreviewsTypeDef = TypedDict(
    "_PreviewAgentsPaginateResponseagentPreviewsTypeDef",
    {
        "hostname": str,
        "agentId": str,
        "autoScalingGroup": str,
        "agentHealth": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "agentVersion": str,
        "operatingSystem": str,
        "kernelVersion": str,
        "ipv4Address": str,
    },
    total=False,
)


class PreviewAgentsPaginateResponseagentPreviewsTypeDef(
    _PreviewAgentsPaginateResponseagentPreviewsTypeDef
):
    """
    - *(dict) --*

      Used as a response element in the  PreviewAgents action.
      - **hostname** *(string) --*

        The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.
    """


_PreviewAgentsPaginateResponseTypeDef = TypedDict(
    "_PreviewAgentsPaginateResponseTypeDef",
    {"agentPreviews": List[PreviewAgentsPaginateResponseagentPreviewsTypeDef], "NextToken": str},
    total=False,
)


class PreviewAgentsPaginateResponseTypeDef(_PreviewAgentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **agentPreviews** *(list) --*

        The resulting list of agents.
        - *(dict) --*

          Used as a response element in the  PreviewAgents action.
          - **hostname** *(string) --*

            The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.
    """
