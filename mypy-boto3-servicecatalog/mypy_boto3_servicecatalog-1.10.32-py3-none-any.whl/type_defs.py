"Main interface for servicecatalog service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    "ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef",
    "ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef",
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef",
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef",
    "ClientCopyProductResponseTypeDef",
    "ClientCreateConstraintResponseConstraintDetailTypeDef",
    "ClientCreateConstraintResponseTypeDef",
    "ClientCreatePortfolioResponsePortfolioDetailTypeDef",
    "ClientCreatePortfolioResponseTagsTypeDef",
    "ClientCreatePortfolioResponseTypeDef",
    "ClientCreatePortfolioShareOrganizationNodeTypeDef",
    "ClientCreatePortfolioShareResponseTypeDef",
    "ClientCreatePortfolioTagsTypeDef",
    "ClientCreateProductProvisioningArtifactParametersTypeDef",
    "ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef",
    "ClientCreateProductResponseProductViewDetailTypeDef",
    "ClientCreateProductResponseProvisioningArtifactDetailTypeDef",
    "ClientCreateProductResponseTagsTypeDef",
    "ClientCreateProductResponseTypeDef",
    "ClientCreateProductTagsTypeDef",
    "ClientCreateProvisionedProductPlanProvisioningParametersTypeDef",
    "ClientCreateProvisionedProductPlanResponseTypeDef",
    "ClientCreateProvisionedProductPlanTagsTypeDef",
    "ClientCreateProvisioningArtifactParametersTypeDef",
    "ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    "ClientCreateProvisioningArtifactResponseTypeDef",
    "ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    "ClientCreateServiceActionResponseServiceActionDetailTypeDef",
    "ClientCreateServiceActionResponseTypeDef",
    "ClientCreateTagOptionResponseTagOptionDetailTypeDef",
    "ClientCreateTagOptionResponseTypeDef",
    "ClientDeletePortfolioShareOrganizationNodeTypeDef",
    "ClientDeletePortfolioShareResponseTypeDef",
    "ClientDescribeConstraintResponseConstraintDetailTypeDef",
    "ClientDescribeConstraintResponseTypeDef",
    "ClientDescribeCopyProductStatusResponseTypeDef",
    "ClientDescribePortfolioResponseBudgetsTypeDef",
    "ClientDescribePortfolioResponsePortfolioDetailTypeDef",
    "ClientDescribePortfolioResponseTagOptionsTypeDef",
    "ClientDescribePortfolioResponseTagsTypeDef",
    "ClientDescribePortfolioResponseTypeDef",
    "ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef",
    "ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef",
    "ClientDescribePortfolioShareStatusResponseTypeDef",
    "ClientDescribeProductAsAdminResponseBudgetsTypeDef",
    "ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef",
    "ClientDescribeProductAsAdminResponseProductViewDetailTypeDef",
    "ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef",
    "ClientDescribeProductAsAdminResponseTagOptionsTypeDef",
    "ClientDescribeProductAsAdminResponseTagsTypeDef",
    "ClientDescribeProductAsAdminResponseTypeDef",
    "ClientDescribeProductResponseBudgetsTypeDef",
    "ClientDescribeProductResponseProductViewSummaryTypeDef",
    "ClientDescribeProductResponseProvisioningArtifactsTypeDef",
    "ClientDescribeProductResponseTypeDef",
    "ClientDescribeProductViewResponseProductViewSummaryTypeDef",
    "ClientDescribeProductViewResponseProvisioningArtifactsTypeDef",
    "ClientDescribeProductViewResponseTypeDef",
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef",
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef",
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef",
    "ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef",
    "ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef",
    "ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef",
    "ClientDescribeProvisionedProductPlanResponseTypeDef",
    "ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef",
    "ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef",
    "ClientDescribeProvisionedProductResponseTypeDef",
    "ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    "ClientDescribeProvisioningArtifactResponseTypeDef",
    "ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef",
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef",
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef",
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef",
    "ClientDescribeProvisioningParametersResponseTagOptionsTypeDef",
    "ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef",
    "ClientDescribeProvisioningParametersResponseTypeDef",
    "ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef",
    "ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef",
    "ClientDescribeRecordResponseRecordDetailTypeDef",
    "ClientDescribeRecordResponseRecordOutputsTypeDef",
    "ClientDescribeRecordResponseTypeDef",
    "ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef",
    "ClientDescribeServiceActionExecutionParametersResponseTypeDef",
    "ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    "ClientDescribeServiceActionResponseServiceActionDetailTypeDef",
    "ClientDescribeServiceActionResponseTypeDef",
    "ClientDescribeTagOptionResponseTagOptionDetailTypeDef",
    "ClientDescribeTagOptionResponseTypeDef",
    "ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef",
    "ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef",
    "ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef",
    "ClientExecuteProvisionedProductPlanResponseTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseTypeDef",
    "ClientGetAwsOrganizationsAccessStatusResponseTypeDef",
    "ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef",
    "ClientListAcceptedPortfolioSharesResponseTypeDef",
    "ClientListBudgetsForResourceResponseBudgetsTypeDef",
    "ClientListBudgetsForResourceResponseTypeDef",
    "ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef",
    "ClientListConstraintsForPortfolioResponseTypeDef",
    "ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef",
    "ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef",
    "ClientListLaunchPathsResponseLaunchPathSummariesTypeDef",
    "ClientListLaunchPathsResponseTypeDef",
    "ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef",
    "ClientListOrganizationPortfolioAccessResponseTypeDef",
    "ClientListPortfolioAccessResponseTypeDef",
    "ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef",
    "ClientListPortfoliosForProductResponseTypeDef",
    "ClientListPortfoliosResponsePortfolioDetailsTypeDef",
    "ClientListPortfoliosResponseTypeDef",
    "ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef",
    "ClientListPrincipalsForPortfolioResponseTypeDef",
    "ClientListProvisionedProductPlansAccessLevelFilterTypeDef",
    "ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef",
    "ClientListProvisionedProductPlansResponseTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseTypeDef",
    "ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef",
    "ClientListProvisioningArtifactsResponseTypeDef",
    "ClientListRecordHistoryAccessLevelFilterTypeDef",
    "ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef",
    "ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef",
    "ClientListRecordHistoryResponseRecordDetailsTypeDef",
    "ClientListRecordHistoryResponseTypeDef",
    "ClientListRecordHistorySearchFilterTypeDef",
    "ClientListResourcesForTagOptionResponseResourceDetailsTypeDef",
    "ClientListResourcesForTagOptionResponseTypeDef",
    "ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef",
    "ClientListServiceActionsForProvisioningArtifactResponseTypeDef",
    "ClientListServiceActionsResponseServiceActionSummariesTypeDef",
    "ClientListServiceActionsResponseTypeDef",
    "ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef",
    "ClientListStackInstancesForProvisionedProductResponseTypeDef",
    "ClientListTagOptionsFiltersTypeDef",
    "ClientListTagOptionsResponseTagOptionDetailsTypeDef",
    "ClientListTagOptionsResponseTypeDef",
    "ClientProvisionProductProvisioningParametersTypeDef",
    "ClientProvisionProductProvisioningPreferencesTypeDef",
    "ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef",
    "ClientProvisionProductResponseRecordDetailRecordTagsTypeDef",
    "ClientProvisionProductResponseRecordDetailTypeDef",
    "ClientProvisionProductResponseTypeDef",
    "ClientProvisionProductTagsTypeDef",
    "ClientScanProvisionedProductsAccessLevelFilterTypeDef",
    "ClientScanProvisionedProductsResponseProvisionedProductsTypeDef",
    "ClientScanProvisionedProductsResponseTypeDef",
    "ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef",
    "ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef",
    "ClientSearchProductsAsAdminResponseTypeDef",
    "ClientSearchProductsResponseProductViewAggregationsTypeDef",
    "ClientSearchProductsResponseProductViewSummariesTypeDef",
    "ClientSearchProductsResponseTypeDef",
    "ClientSearchProvisionedProductsAccessLevelFilterTypeDef",
    "ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef",
    "ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef",
    "ClientSearchProvisionedProductsResponseTypeDef",
    "ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    "ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    "ClientTerminateProvisionedProductResponseRecordDetailTypeDef",
    "ClientTerminateProvisionedProductResponseTypeDef",
    "ClientUpdateConstraintResponseConstraintDetailTypeDef",
    "ClientUpdateConstraintResponseTypeDef",
    "ClientUpdatePortfolioAddTagsTypeDef",
    "ClientUpdatePortfolioResponsePortfolioDetailTypeDef",
    "ClientUpdatePortfolioResponseTagsTypeDef",
    "ClientUpdatePortfolioResponseTypeDef",
    "ClientUpdateProductAddTagsTypeDef",
    "ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef",
    "ClientUpdateProductResponseProductViewDetailTypeDef",
    "ClientUpdateProductResponseTagsTypeDef",
    "ClientUpdateProductResponseTypeDef",
    "ClientUpdateProvisionedProductPropertiesResponseTypeDef",
    "ClientUpdateProvisionedProductProvisioningParametersTypeDef",
    "ClientUpdateProvisionedProductProvisioningPreferencesTypeDef",
    "ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    "ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    "ClientUpdateProvisionedProductResponseRecordDetailTypeDef",
    "ClientUpdateProvisionedProductResponseTypeDef",
    "ClientUpdateProvisionedProductTagsTypeDef",
    "ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    "ClientUpdateProvisioningArtifactResponseTypeDef",
    "ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    "ClientUpdateServiceActionResponseServiceActionDetailTypeDef",
    "ClientUpdateServiceActionResponseTypeDef",
    "ClientUpdateTagOptionResponseTagOptionDetailTypeDef",
    "ClientUpdateTagOptionResponseTypeDef",
    "ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef",
    "ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef",
    "ListAcceptedPortfolioSharesPaginateResponseTypeDef",
    "ListConstraintsForPortfolioPaginatePaginationConfigTypeDef",
    "ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef",
    "ListConstraintsForPortfolioPaginateResponseTypeDef",
    "ListLaunchPathsPaginatePaginationConfigTypeDef",
    "ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef",
    "ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef",
    "ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef",
    "ListLaunchPathsPaginateResponseTypeDef",
    "ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef",
    "ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef",
    "ListOrganizationPortfolioAccessPaginateResponseTypeDef",
    "ListPortfoliosForProductPaginatePaginationConfigTypeDef",
    "ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef",
    "ListPortfoliosForProductPaginateResponseTypeDef",
    "ListPortfoliosPaginatePaginationConfigTypeDef",
    "ListPortfoliosPaginateResponsePortfolioDetailsTypeDef",
    "ListPortfoliosPaginateResponseTypeDef",
    "ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef",
    "ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef",
    "ListPrincipalsForPortfolioPaginateResponseTypeDef",
    "ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef",
    "ListProvisionedProductPlansPaginatePaginationConfigTypeDef",
    "ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef",
    "ListProvisionedProductPlansPaginateResponseTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef",
    "ListRecordHistoryPaginateAccessLevelFilterTypeDef",
    "ListRecordHistoryPaginatePaginationConfigTypeDef",
    "ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef",
    "ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef",
    "ListRecordHistoryPaginateResponseRecordDetailsTypeDef",
    "ListRecordHistoryPaginateResponseTypeDef",
    "ListRecordHistoryPaginateSearchFilterTypeDef",
    "ListResourcesForTagOptionPaginatePaginationConfigTypeDef",
    "ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef",
    "ListResourcesForTagOptionPaginateResponseTypeDef",
    "ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef",
    "ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef",
    "ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef",
    "ListServiceActionsPaginatePaginationConfigTypeDef",
    "ListServiceActionsPaginateResponseServiceActionSummariesTypeDef",
    "ListServiceActionsPaginateResponseTypeDef",
    "ListTagOptionsPaginateFiltersTypeDef",
    "ListTagOptionsPaginatePaginationConfigTypeDef",
    "ListTagOptionsPaginateResponseTagOptionDetailsTypeDef",
    "ListTagOptionsPaginateResponseTypeDef",
    "ScanProvisionedProductsPaginateAccessLevelFilterTypeDef",
    "ScanProvisionedProductsPaginatePaginationConfigTypeDef",
    "ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef",
    "ScanProvisionedProductsPaginateResponseTypeDef",
    "SearchProductsAsAdminPaginatePaginationConfigTypeDef",
    "SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef",
    "SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef",
    "SearchProductsAsAdminPaginateResponseTypeDef",
)


_ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef = TypedDict(
    "_ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ErrorCode": Literal[
            "DUPLICATE_RESOURCE",
            "INTERNAL_FAILURE",
            "LIMIT_EXCEEDED",
            "RESOURCE_NOT_FOUND",
            "THROTTLING",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef(
    _ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
):
    """
    - *(dict) --*

      An object containing information about the error, along with identifying information about the
      self-service action and its associations.
      - **ServiceActionId** *(string) --*

        The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
    """


_ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef",
    {
        "FailedServiceActionAssociations": List[
            ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
        ]
    },
    total=False,
)


class ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef(
    _ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef
):
    """
    - *(dict) --*

      - **FailedServiceActionAssociations** *(list) --*

        An object that contains a list of errors, along with information to help you identify the
        self-service action.
        - *(dict) --*

          An object containing information about the error, along with identifying information about
          the self-service action and its associations.
          - **ServiceActionId** *(string) --*

            The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
    """


_RequiredClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_RequiredClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ServiceActionId": str},
)
_OptionalClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_OptionalClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ProductId": str, "ProvisioningArtifactId": str},
    total=False,
)


class ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef(
    _RequiredClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef,
    _OptionalClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef,
):
    """
    - *(dict) --*

      A self-service action association consisting of the Action ID, the Product ID, and the
      Provisioning Artifact ID.
      - **ServiceActionId** *(string) --***[REQUIRED]**

        The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
    """


_ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef = TypedDict(
    "_ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ErrorCode": Literal[
            "DUPLICATE_RESOURCE",
            "INTERNAL_FAILURE",
            "LIMIT_EXCEEDED",
            "RESOURCE_NOT_FOUND",
            "THROTTLING",
        ],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef(
    _ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
):
    """
    - *(dict) --*

      An object containing information about the error, along with identifying information about the
      self-service action and its associations.
      - **ServiceActionId** *(string) --*

        The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
    """


_ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef",
    {
        "FailedServiceActionAssociations": List[
            ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef(
    _ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef
):
    """
    - *(dict) --*

      - **FailedServiceActionAssociations** *(list) --*

        An object that contains a list of errors, along with information to help you identify the
        self-service action.
        - *(dict) --*

          An object containing information about the error, along with identifying information about
          the self-service action and its associations.
          - **ServiceActionId** *(string) --*

            The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
    """


_RequiredClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_RequiredClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ServiceActionId": str},
)
_OptionalClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_OptionalClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ProductId": str, "ProvisioningArtifactId": str},
    total=False,
)


class ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef(
    _RequiredClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef,
    _OptionalClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef,
):
    """
    - *(dict) --*

      A self-service action association consisting of the Action ID, the Product ID, and the
      Provisioning Artifact ID.
      - **ServiceActionId** *(string) --***[REQUIRED]**

        The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .
    """


_ClientCopyProductResponseTypeDef = TypedDict(
    "_ClientCopyProductResponseTypeDef", {"CopyProductToken": str}, total=False
)


class ClientCopyProductResponseTypeDef(_ClientCopyProductResponseTypeDef):
    """
    - *(dict) --*

      - **CopyProductToken** *(string) --*

        The token to use to track the progress of the operation.
    """


_ClientCreateConstraintResponseConstraintDetailTypeDef = TypedDict(
    "_ClientCreateConstraintResponseConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ClientCreateConstraintResponseConstraintDetailTypeDef(
    _ClientCreateConstraintResponseConstraintDetailTypeDef
):
    """
    - **ConstraintDetail** *(dict) --*

      Information about the constraint.
      - **ConstraintId** *(string) --*

        The identifier of the constraint.
    """


_ClientCreateConstraintResponseTypeDef = TypedDict(
    "_ClientCreateConstraintResponseTypeDef",
    {
        "ConstraintDetail": ClientCreateConstraintResponseConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)


class ClientCreateConstraintResponseTypeDef(_ClientCreateConstraintResponseTypeDef):
    """
    - *(dict) --*

      - **ConstraintDetail** *(dict) --*

        Information about the constraint.
        - **ConstraintId** *(string) --*

          The identifier of the constraint.
    """


_ClientCreatePortfolioResponsePortfolioDetailTypeDef = TypedDict(
    "_ClientCreatePortfolioResponsePortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientCreatePortfolioResponsePortfolioDetailTypeDef(
    _ClientCreatePortfolioResponsePortfolioDetailTypeDef
):
    """
    - **PortfolioDetail** *(dict) --*

      Information about the portfolio.
      - **Id** *(string) --*

        The portfolio identifier.
    """


_ClientCreatePortfolioResponseTagsTypeDef = TypedDict(
    "_ClientCreatePortfolioResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreatePortfolioResponseTagsTypeDef(_ClientCreatePortfolioResponseTagsTypeDef):
    pass


_ClientCreatePortfolioResponseTypeDef = TypedDict(
    "_ClientCreatePortfolioResponseTypeDef",
    {
        "PortfolioDetail": ClientCreatePortfolioResponsePortfolioDetailTypeDef,
        "Tags": List[ClientCreatePortfolioResponseTagsTypeDef],
    },
    total=False,
)


class ClientCreatePortfolioResponseTypeDef(_ClientCreatePortfolioResponseTypeDef):
    """
    - *(dict) --*

      - **PortfolioDetail** *(dict) --*

        Information about the portfolio.
        - **Id** *(string) --*

          The portfolio identifier.
    """


_ClientCreatePortfolioShareOrganizationNodeTypeDef = TypedDict(
    "_ClientCreatePortfolioShareOrganizationNodeTypeDef",
    {"Type": Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"], "Value": str},
    total=False,
)


class ClientCreatePortfolioShareOrganizationNodeTypeDef(
    _ClientCreatePortfolioShareOrganizationNodeTypeDef
):
    """
    The organization node to whom you are going to share. If ``OrganizationNode`` is passed in,
    ``PortfolioShare`` will be created for the node and its children (when applies), and a
    ``PortfolioShareToken`` will be returned in the output in order for the administrator to monitor
    the status of the ``PortfolioShare`` creation process.
    - **Type** *(string) --*

      The organization node type.
    """


_ClientCreatePortfolioShareResponseTypeDef = TypedDict(
    "_ClientCreatePortfolioShareResponseTypeDef", {"PortfolioShareToken": str}, total=False
)


class ClientCreatePortfolioShareResponseTypeDef(_ClientCreatePortfolioShareResponseTypeDef):
    """
    - *(dict) --*

      - **PortfolioShareToken** *(string) --*

        The portfolio share unique identifier. This will only be returned if portfolio is shared to
        an organization node.
    """


_RequiredClientCreatePortfolioTagsTypeDef = TypedDict(
    "_RequiredClientCreatePortfolioTagsTypeDef", {"Key": str}
)
_OptionalClientCreatePortfolioTagsTypeDef = TypedDict(
    "_OptionalClientCreatePortfolioTagsTypeDef", {"Value": str}, total=False
)


class ClientCreatePortfolioTagsTypeDef(
    _RequiredClientCreatePortfolioTagsTypeDef, _OptionalClientCreatePortfolioTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
      created when provisioning a product.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientCreateProductProvisioningArtifactParametersTypeDef = TypedDict(
    "_ClientCreateProductProvisioningArtifactParametersTypeDef",
    {
        "Name": str,
        "Description": str,
        "Info": Dict[str, str],
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "DisableTemplateValidation": bool,
    },
    total=False,
)


class ClientCreateProductProvisioningArtifactParametersTypeDef(
    _ClientCreateProductProvisioningArtifactParametersTypeDef
):
    """
    The configuration of the provisioning artifact.
    - **Name** *(string) --*

      The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.
    """


_ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef = TypedDict(
    "_ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef(
    _ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef
):
    """
    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.
      - **Id** *(string) --*

        The product view identifier.
    """


_ClientCreateProductResponseProductViewDetailTypeDef = TypedDict(
    "_ClientCreateProductResponseProductViewDetailTypeDef",
    {
        "ProductViewSummary": ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientCreateProductResponseProductViewDetailTypeDef(
    _ClientCreateProductResponseProductViewDetailTypeDef
):
    """
    - **ProductViewDetail** *(dict) --*

      Information about the product view.
      - **ProductViewSummary** *(dict) --*

        Summary information about the product view.
        - **Id** *(string) --*

          The product view identifier.
    """


_ClientCreateProductResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "_ClientCreateProductResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)


class ClientCreateProductResponseProvisioningArtifactDetailTypeDef(
    _ClientCreateProductResponseProvisioningArtifactDetailTypeDef
):
    pass


_ClientCreateProductResponseTagsTypeDef = TypedDict(
    "_ClientCreateProductResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateProductResponseTagsTypeDef(_ClientCreateProductResponseTagsTypeDef):
    pass


_ClientCreateProductResponseTypeDef = TypedDict(
    "_ClientCreateProductResponseTypeDef",
    {
        "ProductViewDetail": ClientCreateProductResponseProductViewDetailTypeDef,
        "ProvisioningArtifactDetail": ClientCreateProductResponseProvisioningArtifactDetailTypeDef,
        "Tags": List[ClientCreateProductResponseTagsTypeDef],
    },
    total=False,
)


class ClientCreateProductResponseTypeDef(_ClientCreateProductResponseTypeDef):
    """
    - *(dict) --*

      - **ProductViewDetail** *(dict) --*

        Information about the product view.
        - **ProductViewSummary** *(dict) --*

          Summary information about the product view.
          - **Id** *(string) --*

            The product view identifier.
    """


_RequiredClientCreateProductTagsTypeDef = TypedDict(
    "_RequiredClientCreateProductTagsTypeDef", {"Key": str}
)
_OptionalClientCreateProductTagsTypeDef = TypedDict(
    "_OptionalClientCreateProductTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateProductTagsTypeDef(
    _RequiredClientCreateProductTagsTypeDef, _OptionalClientCreateProductTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
      created when provisioning a product.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientCreateProvisionedProductPlanProvisioningParametersTypeDef = TypedDict(
    "_ClientCreateProvisionedProductPlanProvisioningParametersTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)


class ClientCreateProvisionedProductPlanProvisioningParametersTypeDef(
    _ClientCreateProvisionedProductPlanProvisioningParametersTypeDef
):
    """
    - *(dict) --*

      The parameter key-value pair used to update a provisioned product.
      - **Key** *(string) --*

        The parameter key.
    """


_ClientCreateProvisionedProductPlanResponseTypeDef = TypedDict(
    "_ClientCreateProvisionedProductPlanResponseTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ClientCreateProvisionedProductPlanResponseTypeDef(
    _ClientCreateProvisionedProductPlanResponseTypeDef
):
    """
    - *(dict) --*

      - **PlanName** *(string) --*

        The name of the plan.
    """


_RequiredClientCreateProvisionedProductPlanTagsTypeDef = TypedDict(
    "_RequiredClientCreateProvisionedProductPlanTagsTypeDef", {"Key": str}
)
_OptionalClientCreateProvisionedProductPlanTagsTypeDef = TypedDict(
    "_OptionalClientCreateProvisionedProductPlanTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateProvisionedProductPlanTagsTypeDef(
    _RequiredClientCreateProvisionedProductPlanTagsTypeDef,
    _OptionalClientCreateProvisionedProductPlanTagsTypeDef,
):
    """
    - *(dict) --*

      Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
      created when provisioning a product.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientCreateProvisioningArtifactParametersTypeDef = TypedDict(
    "_ClientCreateProvisioningArtifactParametersTypeDef",
    {
        "Name": str,
        "Description": str,
        "Info": Dict[str, str],
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "DisableTemplateValidation": bool,
    },
    total=False,
)


class ClientCreateProvisioningArtifactParametersTypeDef(
    _ClientCreateProvisioningArtifactParametersTypeDef
):
    """
    The configuration for the provisioning artifact.
    - **Name** *(string) --*

      The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.
    """


_ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "_ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)


class ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef(
    _ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef
):
    """
    - **ProvisioningArtifactDetail** *(dict) --*

      Information about the provisioning artifact.
      - **Id** *(string) --*

        The identifier of the provisioning artifact.
    """


_ClientCreateProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientCreateProvisioningArtifactResponseTypeDef",
    {
        "ProvisioningArtifactDetail": ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)


class ClientCreateProvisioningArtifactResponseTypeDef(
    _ClientCreateProvisioningArtifactResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisioningArtifactDetail** *(dict) --*

        Information about the provisioning artifact.
        - **Id** *(string) --*

          The identifier of the provisioning artifact.
    """


_ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef = TypedDict(
    "_ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef(
    _ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef
):
    """
    - **ServiceActionSummary** *(dict) --*

      Summary information about the self-service action.
      - **Id** *(string) --*

        The self-service action identifier.
    """


_ClientCreateServiceActionResponseServiceActionDetailTypeDef = TypedDict(
    "_ClientCreateServiceActionResponseServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef,
        "Definition": Dict[str, str],
    },
    total=False,
)


class ClientCreateServiceActionResponseServiceActionDetailTypeDef(
    _ClientCreateServiceActionResponseServiceActionDetailTypeDef
):
    """
    - **ServiceActionDetail** *(dict) --*

      An object containing information about the self-service action.
      - **ServiceActionSummary** *(dict) --*

        Summary information about the self-service action.
        - **Id** *(string) --*

          The self-service action identifier.
    """


_ClientCreateServiceActionResponseTypeDef = TypedDict(
    "_ClientCreateServiceActionResponseTypeDef",
    {"ServiceActionDetail": ClientCreateServiceActionResponseServiceActionDetailTypeDef},
    total=False,
)


class ClientCreateServiceActionResponseTypeDef(_ClientCreateServiceActionResponseTypeDef):
    """
    - *(dict) --*

      - **ServiceActionDetail** *(dict) --*

        An object containing information about the self-service action.
        - **ServiceActionSummary** *(dict) --*

          Summary information about the self-service action.
          - **Id** *(string) --*

            The self-service action identifier.
    """


_ClientCreateTagOptionResponseTagOptionDetailTypeDef = TypedDict(
    "_ClientCreateTagOptionResponseTagOptionDetailTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientCreateTagOptionResponseTagOptionDetailTypeDef(
    _ClientCreateTagOptionResponseTagOptionDetailTypeDef
):
    """
    - **TagOptionDetail** *(dict) --*

      Information about the TagOption.
      - **Key** *(string) --*

        The TagOption key.
    """


_ClientCreateTagOptionResponseTypeDef = TypedDict(
    "_ClientCreateTagOptionResponseTypeDef",
    {"TagOptionDetail": ClientCreateTagOptionResponseTagOptionDetailTypeDef},
    total=False,
)


class ClientCreateTagOptionResponseTypeDef(_ClientCreateTagOptionResponseTypeDef):
    """
    - *(dict) --*

      - **TagOptionDetail** *(dict) --*

        Information about the TagOption.
        - **Key** *(string) --*

          The TagOption key.
    """


_ClientDeletePortfolioShareOrganizationNodeTypeDef = TypedDict(
    "_ClientDeletePortfolioShareOrganizationNodeTypeDef",
    {"Type": Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"], "Value": str},
    total=False,
)


class ClientDeletePortfolioShareOrganizationNodeTypeDef(
    _ClientDeletePortfolioShareOrganizationNodeTypeDef
):
    """
    The organization node to whom you are going to stop sharing.
    - **Type** *(string) --*

      The organization node type.
    """


_ClientDeletePortfolioShareResponseTypeDef = TypedDict(
    "_ClientDeletePortfolioShareResponseTypeDef", {"PortfolioShareToken": str}, total=False
)


class ClientDeletePortfolioShareResponseTypeDef(_ClientDeletePortfolioShareResponseTypeDef):
    """
    - *(dict) --*

      - **PortfolioShareToken** *(string) --*

        The portfolio share unique identifier. This will only be returned if delete is made to an
        organization node.
    """


_ClientDescribeConstraintResponseConstraintDetailTypeDef = TypedDict(
    "_ClientDescribeConstraintResponseConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ClientDescribeConstraintResponseConstraintDetailTypeDef(
    _ClientDescribeConstraintResponseConstraintDetailTypeDef
):
    """
    - **ConstraintDetail** *(dict) --*

      Information about the constraint.
      - **ConstraintId** *(string) --*

        The identifier of the constraint.
    """


_ClientDescribeConstraintResponseTypeDef = TypedDict(
    "_ClientDescribeConstraintResponseTypeDef",
    {
        "ConstraintDetail": ClientDescribeConstraintResponseConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)


class ClientDescribeConstraintResponseTypeDef(_ClientDescribeConstraintResponseTypeDef):
    """
    - *(dict) --*

      - **ConstraintDetail** *(dict) --*

        Information about the constraint.
        - **ConstraintId** *(string) --*

          The identifier of the constraint.
    """


_ClientDescribeCopyProductStatusResponseTypeDef = TypedDict(
    "_ClientDescribeCopyProductStatusResponseTypeDef",
    {
        "CopyProductStatus": Literal["SUCCEEDED", "IN_PROGRESS", "FAILED"],
        "TargetProductId": str,
        "StatusDetail": str,
    },
    total=False,
)


class ClientDescribeCopyProductStatusResponseTypeDef(
    _ClientDescribeCopyProductStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **CopyProductStatus** *(string) --*

        The status of the copy product operation.
    """


_ClientDescribePortfolioResponseBudgetsTypeDef = TypedDict(
    "_ClientDescribePortfolioResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)


class ClientDescribePortfolioResponseBudgetsTypeDef(_ClientDescribePortfolioResponseBudgetsTypeDef):
    pass


_ClientDescribePortfolioResponsePortfolioDetailTypeDef = TypedDict(
    "_ClientDescribePortfolioResponsePortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientDescribePortfolioResponsePortfolioDetailTypeDef(
    _ClientDescribePortfolioResponsePortfolioDetailTypeDef
):
    """
    - **PortfolioDetail** *(dict) --*

      Information about the portfolio.
      - **Id** *(string) --*

        The portfolio identifier.
    """


_ClientDescribePortfolioResponseTagOptionsTypeDef = TypedDict(
    "_ClientDescribePortfolioResponseTagOptionsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientDescribePortfolioResponseTagOptionsTypeDef(
    _ClientDescribePortfolioResponseTagOptionsTypeDef
):
    pass


_ClientDescribePortfolioResponseTagsTypeDef = TypedDict(
    "_ClientDescribePortfolioResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribePortfolioResponseTagsTypeDef(_ClientDescribePortfolioResponseTagsTypeDef):
    pass


_ClientDescribePortfolioResponseTypeDef = TypedDict(
    "_ClientDescribePortfolioResponseTypeDef",
    {
        "PortfolioDetail": ClientDescribePortfolioResponsePortfolioDetailTypeDef,
        "Tags": List[ClientDescribePortfolioResponseTagsTypeDef],
        "TagOptions": List[ClientDescribePortfolioResponseTagOptionsTypeDef],
        "Budgets": List[ClientDescribePortfolioResponseBudgetsTypeDef],
    },
    total=False,
)


class ClientDescribePortfolioResponseTypeDef(_ClientDescribePortfolioResponseTypeDef):
    """
    - *(dict) --*

      - **PortfolioDetail** *(dict) --*

        Information about the portfolio.
        - **Id** *(string) --*

          The portfolio identifier.
    """


_ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef = TypedDict(
    "_ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef",
    {"Accounts": List[str], "Message": str, "Error": str},
    total=False,
)


class ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef(
    _ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef
):
    pass


_ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef = TypedDict(
    "_ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef",
    {
        "SuccessfulShares": List[str],
        "ShareErrors": List[
            ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef
        ],
    },
    total=False,
)


class ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef(
    _ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef
):
    pass


_ClientDescribePortfolioShareStatusResponseTypeDef = TypedDict(
    "_ClientDescribePortfolioShareStatusResponseTypeDef",
    {
        "PortfolioShareToken": str,
        "PortfolioId": str,
        "OrganizationNodeValue": str,
        "Status": Literal[
            "NOT_STARTED", "IN_PROGRESS", "COMPLETED", "COMPLETED_WITH_ERRORS", "ERROR"
        ],
        "ShareDetails": ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef,
    },
    total=False,
)


class ClientDescribePortfolioShareStatusResponseTypeDef(
    _ClientDescribePortfolioShareStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **PortfolioShareToken** *(string) --*

        The token for the portfolio share operation. For example, ``share-6v24abcdefghi`` .
    """


_ClientDescribeProductAsAdminResponseBudgetsTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)


class ClientDescribeProductAsAdminResponseBudgetsTypeDef(
    _ClientDescribeProductAsAdminResponseBudgetsTypeDef
):
    pass


_ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef(
    _ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef
):
    """
    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.
      - **Id** *(string) --*

        The product view identifier.
    """


_ClientDescribeProductAsAdminResponseProductViewDetailTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseProductViewDetailTypeDef",
    {
        "ProductViewSummary": ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientDescribeProductAsAdminResponseProductViewDetailTypeDef(
    _ClientDescribeProductAsAdminResponseProductViewDetailTypeDef
):
    """
    - **ProductViewDetail** *(dict) --*

      Information about the product view.
      - **ProductViewSummary** *(dict) --*

        Summary information about the product view.
        - **Id** *(string) --*

          The product view identifier.
    """


_ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProvisioningArtifactMetadata": Dict[str, str],
    },
    total=False,
)


class ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef(
    _ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef
):
    pass


_ClientDescribeProductAsAdminResponseTagOptionsTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseTagOptionsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientDescribeProductAsAdminResponseTagOptionsTypeDef(
    _ClientDescribeProductAsAdminResponseTagOptionsTypeDef
):
    pass


_ClientDescribeProductAsAdminResponseTagsTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeProductAsAdminResponseTagsTypeDef(
    _ClientDescribeProductAsAdminResponseTagsTypeDef
):
    pass


_ClientDescribeProductAsAdminResponseTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseTypeDef",
    {
        "ProductViewDetail": ClientDescribeProductAsAdminResponseProductViewDetailTypeDef,
        "ProvisioningArtifactSummaries": List[
            ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef
        ],
        "Tags": List[ClientDescribeProductAsAdminResponseTagsTypeDef],
        "TagOptions": List[ClientDescribeProductAsAdminResponseTagOptionsTypeDef],
        "Budgets": List[ClientDescribeProductAsAdminResponseBudgetsTypeDef],
    },
    total=False,
)


class ClientDescribeProductAsAdminResponseTypeDef(_ClientDescribeProductAsAdminResponseTypeDef):
    """
    - *(dict) --*

      - **ProductViewDetail** *(dict) --*

        Information about the product view.
        - **ProductViewSummary** *(dict) --*

          Summary information about the product view.
          - **Id** *(string) --*

            The product view identifier.
    """


_ClientDescribeProductResponseBudgetsTypeDef = TypedDict(
    "_ClientDescribeProductResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)


class ClientDescribeProductResponseBudgetsTypeDef(_ClientDescribeProductResponseBudgetsTypeDef):
    pass


_ClientDescribeProductResponseProductViewSummaryTypeDef = TypedDict(
    "_ClientDescribeProductResponseProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientDescribeProductResponseProductViewSummaryTypeDef(
    _ClientDescribeProductResponseProductViewSummaryTypeDef
):
    """
    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.
      - **Id** *(string) --*

        The product view identifier.
    """


_ClientDescribeProductResponseProvisioningArtifactsTypeDef = TypedDict(
    "_ClientDescribeProductResponseProvisioningArtifactsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)


class ClientDescribeProductResponseProvisioningArtifactsTypeDef(
    _ClientDescribeProductResponseProvisioningArtifactsTypeDef
):
    pass


_ClientDescribeProductResponseTypeDef = TypedDict(
    "_ClientDescribeProductResponseTypeDef",
    {
        "ProductViewSummary": ClientDescribeProductResponseProductViewSummaryTypeDef,
        "ProvisioningArtifacts": List[ClientDescribeProductResponseProvisioningArtifactsTypeDef],
        "Budgets": List[ClientDescribeProductResponseBudgetsTypeDef],
    },
    total=False,
)


class ClientDescribeProductResponseTypeDef(_ClientDescribeProductResponseTypeDef):
    """
    - *(dict) --*

      - **ProductViewSummary** *(dict) --*

        Summary information about the product view.
        - **Id** *(string) --*

          The product view identifier.
    """


_ClientDescribeProductViewResponseProductViewSummaryTypeDef = TypedDict(
    "_ClientDescribeProductViewResponseProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientDescribeProductViewResponseProductViewSummaryTypeDef(
    _ClientDescribeProductViewResponseProductViewSummaryTypeDef
):
    """
    - **ProductViewSummary** *(dict) --*

      Summary information about the product.
      - **Id** *(string) --*

        The product view identifier.
    """


_ClientDescribeProductViewResponseProvisioningArtifactsTypeDef = TypedDict(
    "_ClientDescribeProductViewResponseProvisioningArtifactsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)


class ClientDescribeProductViewResponseProvisioningArtifactsTypeDef(
    _ClientDescribeProductViewResponseProvisioningArtifactsTypeDef
):
    pass


_ClientDescribeProductViewResponseTypeDef = TypedDict(
    "_ClientDescribeProductViewResponseTypeDef",
    {
        "ProductViewSummary": ClientDescribeProductViewResponseProductViewSummaryTypeDef,
        "ProvisioningArtifacts": List[
            ClientDescribeProductViewResponseProvisioningArtifactsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeProductViewResponseTypeDef(_ClientDescribeProductViewResponseTypeDef):
    """
    - *(dict) --*

      - **ProductViewSummary** *(dict) --*

        Summary information about the product.
        - **Id** *(string) --*

          The product view identifier.
    """


_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef(
    _ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef
):
    pass


_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef(
    _ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef
):
    pass


_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef",
    {
        "CreatedTime": datetime,
        "PathId": str,
        "ProductId": str,
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": str,
        "ProvisioningArtifactId": str,
        "Status": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_SUCCESS",
            "CREATE_FAILED",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_SUCCESS",
            "EXECUTE_FAILED",
        ],
        "UpdatedTime": datetime,
        "NotificationArns": List[str],
        "ProvisioningParameters": List[
            ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef
        ],
        "Tags": List[
            ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef
        ],
        "StatusMessage": str,
    },
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef(
    _ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef
):
    """
    - **ProvisionedProductPlanDetails** *(dict) --*

      Information about the plan.
      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.
    """


_ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef",
    {
        "Attribute": Literal[
            "PROPERTIES", "METADATA", "CREATIONPOLICY", "UPDATEPOLICY", "DELETIONPOLICY", "TAGS"
        ],
        "Name": str,
        "RequiresRecreation": Literal["NEVER", "CONDITIONALLY", "ALWAYS"],
    },
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef(
    _ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef
):
    pass


_ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef",
    {
        "Target": ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef,
        "Evaluation": Literal["STATIC", "DYNAMIC"],
        "CausingEntity": str,
    },
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef(
    _ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef
):
    pass


_ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef",
    {
        "Action": Literal["ADD", "MODIFY", "REMOVE"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "Scope": List[
            Literal[
                "PROPERTIES", "METADATA", "CREATIONPOLICY", "UPDATEPOLICY", "DELETIONPOLICY", "TAGS"
            ]
        ],
        "Details": List[ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef],
    },
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef(
    _ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef
):
    pass


_ClientDescribeProvisionedProductPlanResponseTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseTypeDef",
    {
        "ProvisionedProductPlanDetails": ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef,
        "ResourceChanges": List[ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseTypeDef(
    _ClientDescribeProvisionedProductPlanResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisionedProductPlanDetails** *(dict) --*

        Information about the plan.
        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.
    """


_ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef(
    _ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef
):
    pass


_ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef(
    _ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef
):
    """
    - **ProvisionedProductDetail** *(dict) --*

      Information about the provisioned product.
      - **Name** *(string) --*

        The user-friendly name of the provisioned product.
    """


_ClientDescribeProvisionedProductResponseTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductResponseTypeDef",
    {
        "ProvisionedProductDetail": ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef,
        "CloudWatchDashboards": List[
            ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeProvisionedProductResponseTypeDef(
    _ClientDescribeProvisionedProductResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisionedProductDetail** *(dict) --*

        Information about the provisioned product.
        - **Name** *(string) --*

          The user-friendly name of the provisioned product.
    """


_ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "_ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)


class ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef(
    _ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef
):
    """
    - **ProvisioningArtifactDetail** *(dict) --*

      Information about the provisioning artifact.
      - **Id** *(string) --*

        The identifier of the provisioning artifact.
    """


_ClientDescribeProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientDescribeProvisioningArtifactResponseTypeDef",
    {
        "ProvisioningArtifactDetail": ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)


class ClientDescribeProvisioningArtifactResponseTypeDef(
    _ClientDescribeProvisioningArtifactResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisioningArtifactDetail** *(dict) --*

        Information about the provisioning artifact.
        - **Id** *(string) --*

          The identifier of the provisioning artifact.
    """


_ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef",
    {"Type": str, "Description": str},
    total=False,
)


class ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef(
    _ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef
):
    pass


_ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef",
    {"AllowedValues": List[str]},
    total=False,
)


class ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef(
    _ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef
):
    pass


_ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "IsNoEcho": bool,
        "Description": str,
        "ParameterConstraints": ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef,
    },
    total=False,
)


class ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef(
    _ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef
):
    """
    - *(dict) --*

      Information about a parameter used to provision a product.
      - **ParameterKey** *(string) --*

        The parameter key.
    """


_ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef",
    {"StackSetAccounts": List[str], "StackSetRegions": List[str]},
    total=False,
)


class ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef(
    _ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef
):
    pass


_ClientDescribeProvisioningParametersResponseTagOptionsTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseTagOptionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeProvisioningParametersResponseTagOptionsTypeDef(
    _ClientDescribeProvisioningParametersResponseTagOptionsTypeDef
):
    pass


_ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef(
    _ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef
):
    pass


_ClientDescribeProvisioningParametersResponseTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseTypeDef",
    {
        "ProvisioningArtifactParameters": List[
            ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef
        ],
        "ConstraintSummaries": List[
            ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef
        ],
        "UsageInstructions": List[
            ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef
        ],
        "TagOptions": List[ClientDescribeProvisioningParametersResponseTagOptionsTypeDef],
        "ProvisioningArtifactPreferences": ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef,
    },
    total=False,
)


class ClientDescribeProvisioningParametersResponseTypeDef(
    _ClientDescribeProvisioningParametersResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisioningArtifactParameters** *(list) --*

        Information about the parameters used to provision the product.
        - *(dict) --*

          Information about a parameter used to provision a product.
          - **ParameterKey** *(string) --*

            The parameter key.
    """


_ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef(
    _ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef
):
    pass


_ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef(
    _ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef
):
    pass


_ClientDescribeRecordResponseRecordDetailTypeDef = TypedDict(
    "_ClientDescribeRecordResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef],
        "RecordTags": List[ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)


class ClientDescribeRecordResponseRecordDetailTypeDef(
    _ClientDescribeRecordResponseRecordDetailTypeDef
):
    """
    - **RecordDetail** *(dict) --*

      Information about the product.
      - **RecordId** *(string) --*

        The identifier of the record.
    """


_ClientDescribeRecordResponseRecordOutputsTypeDef = TypedDict(
    "_ClientDescribeRecordResponseRecordOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str},
    total=False,
)


class ClientDescribeRecordResponseRecordOutputsTypeDef(
    _ClientDescribeRecordResponseRecordOutputsTypeDef
):
    pass


_ClientDescribeRecordResponseTypeDef = TypedDict(
    "_ClientDescribeRecordResponseTypeDef",
    {
        "RecordDetail": ClientDescribeRecordResponseRecordDetailTypeDef,
        "RecordOutputs": List[ClientDescribeRecordResponseRecordOutputsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientDescribeRecordResponseTypeDef(_ClientDescribeRecordResponseTypeDef):
    """
    - *(dict) --*

      - **RecordDetail** *(dict) --*

        Information about the product.
        - **RecordId** *(string) --*

          The identifier of the record.
    """


_ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef = TypedDict(
    "_ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef",
    {"Name": str, "Type": str, "DefaultValues": List[str]},
    total=False,
)


class ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef(
    _ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --*
      - **Type** *(string) --*
      - **DefaultValues** *(list) --*

        - *(string) --*
    """


_ClientDescribeServiceActionExecutionParametersResponseTypeDef = TypedDict(
    "_ClientDescribeServiceActionExecutionParametersResponseTypeDef",
    {
        "ServiceActionParameters": List[
            ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef
        ]
    },
    total=False,
)


class ClientDescribeServiceActionExecutionParametersResponseTypeDef(
    _ClientDescribeServiceActionExecutionParametersResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceActionParameters** *(list) --*

        - *(dict) --*

          - **Name** *(string) --*
          - **Type** *(string) --*
          - **DefaultValues** *(list) --*

            - *(string) --*
    """


_ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef = TypedDict(
    "_ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef(
    _ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef
):
    """
    - **ServiceActionSummary** *(dict) --*

      Summary information about the self-service action.
      - **Id** *(string) --*

        The self-service action identifier.
    """


_ClientDescribeServiceActionResponseServiceActionDetailTypeDef = TypedDict(
    "_ClientDescribeServiceActionResponseServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef,
        "Definition": Dict[str, str],
    },
    total=False,
)


class ClientDescribeServiceActionResponseServiceActionDetailTypeDef(
    _ClientDescribeServiceActionResponseServiceActionDetailTypeDef
):
    """
    - **ServiceActionDetail** *(dict) --*

      Detailed information about the self-service action.
      - **ServiceActionSummary** *(dict) --*

        Summary information about the self-service action.
        - **Id** *(string) --*

          The self-service action identifier.
    """


_ClientDescribeServiceActionResponseTypeDef = TypedDict(
    "_ClientDescribeServiceActionResponseTypeDef",
    {"ServiceActionDetail": ClientDescribeServiceActionResponseServiceActionDetailTypeDef},
    total=False,
)


class ClientDescribeServiceActionResponseTypeDef(_ClientDescribeServiceActionResponseTypeDef):
    """
    - *(dict) --*

      - **ServiceActionDetail** *(dict) --*

        Detailed information about the self-service action.
        - **ServiceActionSummary** *(dict) --*

          Summary information about the self-service action.
          - **Id** *(string) --*

            The self-service action identifier.
    """


_ClientDescribeTagOptionResponseTagOptionDetailTypeDef = TypedDict(
    "_ClientDescribeTagOptionResponseTagOptionDetailTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientDescribeTagOptionResponseTagOptionDetailTypeDef(
    _ClientDescribeTagOptionResponseTagOptionDetailTypeDef
):
    """
    - **TagOptionDetail** *(dict) --*

      Information about the TagOption.
      - **Key** *(string) --*

        The TagOption key.
    """


_ClientDescribeTagOptionResponseTypeDef = TypedDict(
    "_ClientDescribeTagOptionResponseTypeDef",
    {"TagOptionDetail": ClientDescribeTagOptionResponseTagOptionDetailTypeDef},
    total=False,
)


class ClientDescribeTagOptionResponseTypeDef(_ClientDescribeTagOptionResponseTypeDef):
    """
    - *(dict) --*

      - **TagOptionDetail** *(dict) --*

        Information about the TagOption.
        - **Key** *(string) --*

          The TagOption key.
    """


_ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef(
    _ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef
):
    pass


_ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef(
    _ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef
):
    pass


_ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef
        ],
    },
    total=False,
)


class ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef(
    _ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef
):
    """
    - **RecordDetail** *(dict) --*

      Information about the result of provisioning the product.
      - **RecordId** *(string) --*

        The identifier of the record.
    """


_ClientExecuteProvisionedProductPlanResponseTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductPlanResponseTypeDef",
    {"RecordDetail": ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef},
    total=False,
)


class ClientExecuteProvisionedProductPlanResponseTypeDef(
    _ClientExecuteProvisionedProductPlanResponseTypeDef
):
    """
    - *(dict) --*

      - **RecordDetail** *(dict) --*

        Information about the result of provisioning the product.
        - **RecordId** *(string) --*

          The identifier of the record.
    """


_ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef(
    _ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef
):
    pass


_ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef(
    _ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef
):
    pass


_ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef
        ],
    },
    total=False,
)


class ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef(
    _ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef
):
    """
    - **RecordDetail** *(dict) --*

      An object containing detailed information about the result of provisioning the product.
      - **RecordId** *(string) --*

        The identifier of the record.
    """


_ClientExecuteProvisionedProductServiceActionResponseTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductServiceActionResponseTypeDef",
    {"RecordDetail": ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef},
    total=False,
)


class ClientExecuteProvisionedProductServiceActionResponseTypeDef(
    _ClientExecuteProvisionedProductServiceActionResponseTypeDef
):
    """
    - *(dict) --*

      - **RecordDetail** *(dict) --*

        An object containing detailed information about the result of provisioning the product.
        - **RecordId** *(string) --*

          The identifier of the record.
    """


_ClientGetAwsOrganizationsAccessStatusResponseTypeDef = TypedDict(
    "_ClientGetAwsOrganizationsAccessStatusResponseTypeDef",
    {"AccessStatus": Literal["ENABLED", "UNDER_CHANGE", "DISABLED"]},
    total=False,
)


class ClientGetAwsOrganizationsAccessStatusResponseTypeDef(
    _ClientGetAwsOrganizationsAccessStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **AccessStatus** *(string) --*

        The status of the portfolio share feature.
    """


_ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef = TypedDict(
    "_ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef(
    _ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a portfolio.
      - **Id** *(string) --*

        The portfolio identifier.
    """


_ClientListAcceptedPortfolioSharesResponseTypeDef = TypedDict(
    "_ClientListAcceptedPortfolioSharesResponseTypeDef",
    {
        "PortfolioDetails": List[ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListAcceptedPortfolioSharesResponseTypeDef(
    _ClientListAcceptedPortfolioSharesResponseTypeDef
):
    """
    - *(dict) --*

      - **PortfolioDetails** *(list) --*

        Information about the portfolios.
        - *(dict) --*

          Information about a portfolio.
          - **Id** *(string) --*

            The portfolio identifier.
    """


_ClientListBudgetsForResourceResponseBudgetsTypeDef = TypedDict(
    "_ClientListBudgetsForResourceResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)


class ClientListBudgetsForResourceResponseBudgetsTypeDef(
    _ClientListBudgetsForResourceResponseBudgetsTypeDef
):
    """
    - *(dict) --*

      Information about a budget.
      - **BudgetName** *(string) --*

        Name of the associated budget.
    """


_ClientListBudgetsForResourceResponseTypeDef = TypedDict(
    "_ClientListBudgetsForResourceResponseTypeDef",
    {"Budgets": List[ClientListBudgetsForResourceResponseBudgetsTypeDef], "NextPageToken": str},
    total=False,
)


class ClientListBudgetsForResourceResponseTypeDef(_ClientListBudgetsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Budgets** *(list) --*

        Information about the associated budgets.
        - *(dict) --*

          Information about a budget.
          - **BudgetName** *(string) --*

            Name of the associated budget.
    """


_ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef = TypedDict(
    "_ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef(
    _ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a constraint.
      - **ConstraintId** *(string) --*

        The identifier of the constraint.
    """


_ClientListConstraintsForPortfolioResponseTypeDef = TypedDict(
    "_ClientListConstraintsForPortfolioResponseTypeDef",
    {
        "ConstraintDetails": List[
            ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListConstraintsForPortfolioResponseTypeDef(
    _ClientListConstraintsForPortfolioResponseTypeDef
):
    """
    - *(dict) --*

      - **ConstraintDetails** *(list) --*

        Information about the constraints.
        - *(dict) --*

          Information about a constraint.
          - **ConstraintId** *(string) --*

            The identifier of the constraint.
    """


_ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef = TypedDict(
    "_ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef",
    {"Type": str, "Description": str},
    total=False,
)


class ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef(
    _ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef
):
    pass


_ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef = TypedDict(
    "_ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef(
    _ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef
):
    pass


_ClientListLaunchPathsResponseLaunchPathSummariesTypeDef = TypedDict(
    "_ClientListLaunchPathsResponseLaunchPathSummariesTypeDef",
    {
        "Id": str,
        "ConstraintSummaries": List[
            ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef
        ],
        "Tags": List[ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef],
        "Name": str,
    },
    total=False,
)


class ClientListLaunchPathsResponseLaunchPathSummariesTypeDef(
    _ClientListLaunchPathsResponseLaunchPathSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information about a product path for a user.
      - **Id** *(string) --*

        The identifier of the product path.
    """


_ClientListLaunchPathsResponseTypeDef = TypedDict(
    "_ClientListLaunchPathsResponseTypeDef",
    {
        "LaunchPathSummaries": List[ClientListLaunchPathsResponseLaunchPathSummariesTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListLaunchPathsResponseTypeDef(_ClientListLaunchPathsResponseTypeDef):
    """
    - *(dict) --*

      - **LaunchPathSummaries** *(list) --*

        Information about the launch path.
        - *(dict) --*

          Summary information about a product path for a user.
          - **Id** *(string) --*

            The identifier of the product path.
    """


_ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef = TypedDict(
    "_ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef",
    {"Type": Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"], "Value": str},
    total=False,
)


class ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef(
    _ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef
):
    """
    - *(dict) --*

      Information about the organization node.
      - **Type** *(string) --*

        The organization node type.
    """


_ClientListOrganizationPortfolioAccessResponseTypeDef = TypedDict(
    "_ClientListOrganizationPortfolioAccessResponseTypeDef",
    {
        "OrganizationNodes": List[
            ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListOrganizationPortfolioAccessResponseTypeDef(
    _ClientListOrganizationPortfolioAccessResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationNodes** *(list) --*

        Displays information about the organization nodes.
        - *(dict) --*

          Information about the organization node.
          - **Type** *(string) --*

            The organization node type.
    """


_ClientListPortfolioAccessResponseTypeDef = TypedDict(
    "_ClientListPortfolioAccessResponseTypeDef",
    {"AccountIds": List[str], "NextPageToken": str},
    total=False,
)


class ClientListPortfolioAccessResponseTypeDef(_ClientListPortfolioAccessResponseTypeDef):
    """
    - *(dict) --*

      - **AccountIds** *(list) --*

        Information about the AWS accounts with access to the portfolio.
        - *(string) --*
    """


_ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef = TypedDict(
    "_ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef(
    _ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a portfolio.
      - **Id** *(string) --*

        The portfolio identifier.
    """


_ClientListPortfoliosForProductResponseTypeDef = TypedDict(
    "_ClientListPortfoliosForProductResponseTypeDef",
    {
        "PortfolioDetails": List[ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListPortfoliosForProductResponseTypeDef(_ClientListPortfoliosForProductResponseTypeDef):
    """
    - *(dict) --*

      - **PortfolioDetails** *(list) --*

        Information about the portfolios.
        - *(dict) --*

          Information about a portfolio.
          - **Id** *(string) --*

            The portfolio identifier.
    """


_ClientListPortfoliosResponsePortfolioDetailsTypeDef = TypedDict(
    "_ClientListPortfoliosResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientListPortfoliosResponsePortfolioDetailsTypeDef(
    _ClientListPortfoliosResponsePortfolioDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a portfolio.
      - **Id** *(string) --*

        The portfolio identifier.
    """


_ClientListPortfoliosResponseTypeDef = TypedDict(
    "_ClientListPortfoliosResponseTypeDef",
    {
        "PortfolioDetails": List[ClientListPortfoliosResponsePortfolioDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListPortfoliosResponseTypeDef(_ClientListPortfoliosResponseTypeDef):
    """
    - *(dict) --*

      - **PortfolioDetails** *(list) --*

        Information about the portfolios.
        - *(dict) --*

          Information about a portfolio.
          - **Id** *(string) --*

            The portfolio identifier.
    """


_ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef = TypedDict(
    "_ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef",
    {"PrincipalARN": str, "PrincipalType": str},
    total=False,
)


class ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef(
    _ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef
):
    """
    - *(dict) --*

      Information about a principal.
      - **PrincipalARN** *(string) --*

        The ARN of the principal (IAM user, role, or group).
    """


_ClientListPrincipalsForPortfolioResponseTypeDef = TypedDict(
    "_ClientListPrincipalsForPortfolioResponseTypeDef",
    {
        "Principals": List[ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListPrincipalsForPortfolioResponseTypeDef(
    _ClientListPrincipalsForPortfolioResponseTypeDef
):
    """
    - *(dict) --*

      - **Principals** *(list) --*

        The IAM principals (users or roles) associated with the portfolio.
        - *(dict) --*

          Information about a principal.
          - **PrincipalARN** *(string) --*

            The ARN of the principal (IAM user, role, or group).
    """


_ClientListProvisionedProductPlansAccessLevelFilterTypeDef = TypedDict(
    "_ClientListProvisionedProductPlansAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)


class ClientListProvisionedProductPlansAccessLevelFilterTypeDef(
    _ClientListProvisionedProductPlansAccessLevelFilterTypeDef
):
    """
    The access level to use to obtain results. The default is ``User`` .
    - **Key** *(string) --*

      The access level.
      * ``Account`` - Filter results based on the account.
      * ``Role`` - Filter results based on the federated role of the specified user.
      * ``User`` - Filter results based on the specified user.
    """


_ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef = TypedDict(
    "_ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef(
    _ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef
):
    """
    - *(dict) --*

      Summary information about a plan.
      - **PlanName** *(string) --*

        The name of the plan.
    """


_ClientListProvisionedProductPlansResponseTypeDef = TypedDict(
    "_ClientListProvisionedProductPlansResponseTypeDef",
    {
        "ProvisionedProductPlans": List[
            ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListProvisionedProductPlansResponseTypeDef(
    _ClientListProvisionedProductPlansResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisionedProductPlans** *(list) --*

        Information about the plans.
        - *(dict) --*

          Summary information about a plan.
          - **PlanName** *(string) --*

            The name of the plan.
    """


_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef(
    _ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef
):
    """
    - **ProductViewSummary** *(dict) --*

      Summary information about a product view.
      - **Id** *(string) --*

        The product view identifier.
    """


_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)


class ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef(
    _ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef
):
    pass


_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef",
    {
        "ProductViewSummary": ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef,
        "ProvisioningArtifact": ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef,
    },
    total=False,
)


class ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef(
    _ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a product view and a provisioning artifact.
      - **ProductViewSummary** *(dict) --*

        Summary information about a product view.
        - **Id** *(string) --*

          The product view identifier.
    """


_ClientListProvisioningArtifactsForServiceActionResponseTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsForServiceActionResponseTypeDef",
    {
        "ProvisioningArtifactViews": List[
            ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListProvisioningArtifactsForServiceActionResponseTypeDef(
    _ClientListProvisioningArtifactsForServiceActionResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisioningArtifactViews** *(list) --*

        An array of objects with information about product views and provisioning artifacts.
        - *(dict) --*

          An object that contains summary information about a product view and a provisioning
          artifact.
          - **ProductViewSummary** *(dict) --*

            Summary information about a product view.
            - **Id** *(string) --*

              The product view identifier.
    """


_ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)


class ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef(
    _ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a provisioning artifact (also known as a version) for a product.
      - **Id** *(string) --*

        The identifier of the provisioning artifact.
    """


_ClientListProvisioningArtifactsResponseTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsResponseTypeDef",
    {
        "ProvisioningArtifactDetails": List[
            ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListProvisioningArtifactsResponseTypeDef(
    _ClientListProvisioningArtifactsResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisioningArtifactDetails** *(list) --*

        Information about the provisioning artifacts.
        - *(dict) --*

          Information about a provisioning artifact (also known as a version) for a product.
          - **Id** *(string) --*

            The identifier of the provisioning artifact.
    """


_ClientListRecordHistoryAccessLevelFilterTypeDef = TypedDict(
    "_ClientListRecordHistoryAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)


class ClientListRecordHistoryAccessLevelFilterTypeDef(
    _ClientListRecordHistoryAccessLevelFilterTypeDef
):
    """
    The access level to use to obtain results. The default is ``User`` .
    - **Key** *(string) --*

      The access level.
      * ``Account`` - Filter results based on the account.
      * ``Role`` - Filter results based on the federated role of the specified user.
      * ``User`` - Filter results based on the specified user.
    """


_ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef = TypedDict(
    "_ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef(
    _ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef
):
    pass


_ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef = TypedDict(
    "_ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef(
    _ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef
):
    pass


_ClientListRecordHistoryResponseRecordDetailsTypeDef = TypedDict(
    "_ClientListRecordHistoryResponseRecordDetailsTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef],
        "RecordTags": List[ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef],
    },
    total=False,
)


class ClientListRecordHistoryResponseRecordDetailsTypeDef(
    _ClientListRecordHistoryResponseRecordDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a request operation.
      - **RecordId** *(string) --*

        The identifier of the record.
    """


_ClientListRecordHistoryResponseTypeDef = TypedDict(
    "_ClientListRecordHistoryResponseTypeDef",
    {
        "RecordDetails": List[ClientListRecordHistoryResponseRecordDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListRecordHistoryResponseTypeDef(_ClientListRecordHistoryResponseTypeDef):
    """
    - *(dict) --*

      - **RecordDetails** *(list) --*

        The records, in reverse chronological order.
        - *(dict) --*

          Information about a request operation.
          - **RecordId** *(string) --*

            The identifier of the record.
    """


_ClientListRecordHistorySearchFilterTypeDef = TypedDict(
    "_ClientListRecordHistorySearchFilterTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListRecordHistorySearchFilterTypeDef(_ClientListRecordHistorySearchFilterTypeDef):
    """
    The search filter to scope the results.
    - **Key** *(string) --*

      The filter key.
      * ``product`` - Filter results based on the specified product identifier.
      * ``provisionedproduct`` - Filter results based on the provisioned product identifier.
    """


_ClientListResourcesForTagOptionResponseResourceDetailsTypeDef = TypedDict(
    "_ClientListResourcesForTagOptionResponseResourceDetailsTypeDef",
    {"Id": str, "ARN": str, "Name": str, "Description": str, "CreatedTime": datetime},
    total=False,
)


class ClientListResourcesForTagOptionResponseResourceDetailsTypeDef(
    _ClientListResourcesForTagOptionResponseResourceDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a resource.
      - **Id** *(string) --*

        The identifier of the resource.
    """


_ClientListResourcesForTagOptionResponseTypeDef = TypedDict(
    "_ClientListResourcesForTagOptionResponseTypeDef",
    {
        "ResourceDetails": List[ClientListResourcesForTagOptionResponseResourceDetailsTypeDef],
        "PageToken": str,
    },
    total=False,
)


class ClientListResourcesForTagOptionResponseTypeDef(
    _ClientListResourcesForTagOptionResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourceDetails** *(list) --*

        Information about the resources.
        - *(dict) --*

          Information about a resource.
          - **Id** *(string) --*

            The identifier of the resource.
    """


_ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef = TypedDict(
    "_ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef(
    _ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef
):
    """
    - *(dict) --*

      Detailed information about the self-service action.
      - **Id** *(string) --*

        The self-service action identifier.
    """


_ClientListServiceActionsForProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientListServiceActionsForProvisioningArtifactResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListServiceActionsForProvisioningArtifactResponseTypeDef(
    _ClientListServiceActionsForProvisioningArtifactResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceActionSummaries** *(list) --*

        An object containing information about the self-service actions associated with the
        provisioning artifact.
        - *(dict) --*

          Detailed information about the self-service action.
          - **Id** *(string) --*

            The self-service action identifier.
    """


_ClientListServiceActionsResponseServiceActionSummariesTypeDef = TypedDict(
    "_ClientListServiceActionsResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientListServiceActionsResponseServiceActionSummariesTypeDef(
    _ClientListServiceActionsResponseServiceActionSummariesTypeDef
):
    """
    - *(dict) --*

      Detailed information about the self-service action.
      - **Id** *(string) --*

        The self-service action identifier.
    """


_ClientListServiceActionsResponseTypeDef = TypedDict(
    "_ClientListServiceActionsResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ClientListServiceActionsResponseServiceActionSummariesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListServiceActionsResponseTypeDef(_ClientListServiceActionsResponseTypeDef):
    """
    - *(dict) --*

      - **ServiceActionSummaries** *(list) --*

        An object containing information about the service actions associated with the provisioning
        artifact.
        - *(dict) --*

          Detailed information about the self-service action.
          - **Id** *(string) --*

            The self-service action identifier.
    """


_ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef = TypedDict(
    "_ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef",
    {
        "Account": str,
        "Region": str,
        "StackInstanceStatus": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
    },
    total=False,
)


class ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef(
    _ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef
):
    """
    - *(dict) --*

      An AWS CloudFormation stack, in a specific account and region, that's part of a stack set
      operation. A stack instance is a reference to an attempted or actual stack in a given account
      within a given region. A stack instance can exist without a stack—for example, if the stack
      couldn't be created for some reason. A stack instance is associated with only one stack set.
      Each stack instance contains the ID of its associated stack set, as well as the ID of the
      actual stack and the stack status.
      - **Account** *(string) --*

        The name of the AWS account that the stack instance is associated with.
    """


_ClientListStackInstancesForProvisionedProductResponseTypeDef = TypedDict(
    "_ClientListStackInstancesForProvisionedProductResponseTypeDef",
    {
        "StackInstances": List[
            ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListStackInstancesForProvisionedProductResponseTypeDef(
    _ClientListStackInstancesForProvisionedProductResponseTypeDef
):
    """
    - *(dict) --*

      - **StackInstances** *(list) --*

        List of stack instances.
        - *(dict) --*

          An AWS CloudFormation stack, in a specific account and region, that's part of a stack set
          operation. A stack instance is a reference to an attempted or actual stack in a given
          account within a given region. A stack instance can exist without a stack—for example, if
          the stack couldn't be created for some reason. A stack instance is associated with only
          one stack set. Each stack instance contains the ID of its associated stack set, as well as
          the ID of the actual stack and the stack status.
          - **Account** *(string) --*

            The name of the AWS account that the stack instance is associated with.
    """


_ClientListTagOptionsFiltersTypeDef = TypedDict(
    "_ClientListTagOptionsFiltersTypeDef", {"Key": str, "Value": str, "Active": bool}, total=False
)


class ClientListTagOptionsFiltersTypeDef(_ClientListTagOptionsFiltersTypeDef):
    """
    The search filters. If no search filters are specified, the output includes all TagOptions.
    - **Key** *(string) --*

      The TagOption key.
    """


_ClientListTagOptionsResponseTagOptionDetailsTypeDef = TypedDict(
    "_ClientListTagOptionsResponseTagOptionDetailsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientListTagOptionsResponseTagOptionDetailsTypeDef(
    _ClientListTagOptionsResponseTagOptionDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a TagOption.
      - **Key** *(string) --*

        The TagOption key.
    """


_ClientListTagOptionsResponseTypeDef = TypedDict(
    "_ClientListTagOptionsResponseTypeDef",
    {
        "TagOptionDetails": List[ClientListTagOptionsResponseTagOptionDetailsTypeDef],
        "PageToken": str,
    },
    total=False,
)


class ClientListTagOptionsResponseTypeDef(_ClientListTagOptionsResponseTypeDef):
    """
    - *(dict) --*

      - **TagOptionDetails** *(list) --*

        Information about the TagOptions.
        - *(dict) --*

          Information about a TagOption.
          - **Key** *(string) --*

            The TagOption key.
    """


_ClientProvisionProductProvisioningParametersTypeDef = TypedDict(
    "_ClientProvisionProductProvisioningParametersTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientProvisionProductProvisioningParametersTypeDef(
    _ClientProvisionProductProvisioningParametersTypeDef
):
    """
    - *(dict) --*

      Information about a parameter used to provision a product.
      - **Key** *(string) --*

        The parameter key.
    """


_ClientProvisionProductProvisioningPreferencesTypeDef = TypedDict(
    "_ClientProvisionProductProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
    },
    total=False,
)


class ClientProvisionProductProvisioningPreferencesTypeDef(
    _ClientProvisionProductProvisioningPreferencesTypeDef
):
    """
    An object that contains information about the provisioning preferences for a stack set.
    - **StackSetAccounts** *(list) --*

      One or more AWS accounts that will have access to the provisioned product.
      Applicable only to a ``CFN_STACKSET`` provisioned product type.
      The AWS accounts specified should be within the list of accounts in the ``STACKSET``
      constraint. To get the list of accounts in the ``STACKSET`` constraint, use the
      ``DescribeProvisioningParameters`` operation.
      If no values are specified, the default value is all accounts from the ``STACKSET``
      constraint.
      - *(string) --*
    """


_ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef(
    _ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef
):
    pass


_ClientProvisionProductResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientProvisionProductResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientProvisionProductResponseRecordDetailRecordTagsTypeDef(
    _ClientProvisionProductResponseRecordDetailRecordTagsTypeDef
):
    pass


_ClientProvisionProductResponseRecordDetailTypeDef = TypedDict(
    "_ClientProvisionProductResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef],
        "RecordTags": List[ClientProvisionProductResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)


class ClientProvisionProductResponseRecordDetailTypeDef(
    _ClientProvisionProductResponseRecordDetailTypeDef
):
    """
    - **RecordDetail** *(dict) --*

      Information about the result of provisioning the product.
      - **RecordId** *(string) --*

        The identifier of the record.
    """


_ClientProvisionProductResponseTypeDef = TypedDict(
    "_ClientProvisionProductResponseTypeDef",
    {"RecordDetail": ClientProvisionProductResponseRecordDetailTypeDef},
    total=False,
)


class ClientProvisionProductResponseTypeDef(_ClientProvisionProductResponseTypeDef):
    """
    - *(dict) --*

      - **RecordDetail** *(dict) --*

        Information about the result of provisioning the product.
        - **RecordId** *(string) --*

          The identifier of the record.
    """


_RequiredClientProvisionProductTagsTypeDef = TypedDict(
    "_RequiredClientProvisionProductTagsTypeDef", {"Key": str}
)
_OptionalClientProvisionProductTagsTypeDef = TypedDict(
    "_OptionalClientProvisionProductTagsTypeDef", {"Value": str}, total=False
)


class ClientProvisionProductTagsTypeDef(
    _RequiredClientProvisionProductTagsTypeDef, _OptionalClientProvisionProductTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
      created when provisioning a product.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientScanProvisionedProductsAccessLevelFilterTypeDef = TypedDict(
    "_ClientScanProvisionedProductsAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)


class ClientScanProvisionedProductsAccessLevelFilterTypeDef(
    _ClientScanProvisionedProductsAccessLevelFilterTypeDef
):
    """
    The access level to use to obtain results. The default is ``User`` .
    - **Key** *(string) --*

      The access level.
      * ``Account`` - Filter results based on the account.
      * ``Role`` - Filter results based on the federated role of the specified user.
      * ``User`` - Filter results based on the specified user.
    """


_ClientScanProvisionedProductsResponseProvisionedProductsTypeDef = TypedDict(
    "_ClientScanProvisionedProductsResponseProvisionedProductsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ClientScanProvisionedProductsResponseProvisionedProductsTypeDef(
    _ClientScanProvisionedProductsResponseProvisionedProductsTypeDef
):
    """
    - *(dict) --*

      Information about a provisioned product.
      - **Name** *(string) --*

        The user-friendly name of the provisioned product.
    """


_ClientScanProvisionedProductsResponseTypeDef = TypedDict(
    "_ClientScanProvisionedProductsResponseTypeDef",
    {
        "ProvisionedProducts": List[
            ClientScanProvisionedProductsResponseProvisionedProductsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientScanProvisionedProductsResponseTypeDef(_ClientScanProvisionedProductsResponseTypeDef):
    """
    - *(dict) --*

      - **ProvisionedProducts** *(list) --*

        Information about the provisioned products.
        - *(dict) --*

          Information about a provisioned product.
          - **Name** *(string) --*

            The user-friendly name of the provisioned product.
    """


_ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef = TypedDict(
    "_ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef(
    _ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef
):
    """
    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.
      - **Id** *(string) --*

        The product view identifier.
    """


_ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef = TypedDict(
    "_ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef",
    {
        "ProductViewSummary": ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef(
    _ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a product view.
      - **ProductViewSummary** *(dict) --*

        Summary information about the product view.
        - **Id** *(string) --*

          The product view identifier.
    """


_ClientSearchProductsAsAdminResponseTypeDef = TypedDict(
    "_ClientSearchProductsAsAdminResponseTypeDef",
    {
        "ProductViewDetails": List[ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientSearchProductsAsAdminResponseTypeDef(_ClientSearchProductsAsAdminResponseTypeDef):
    """
    - *(dict) --*

      - **ProductViewDetails** *(list) --*

        Information about the product views.
        - *(dict) --*

          Information about a product view.
          - **ProductViewSummary** *(dict) --*

            Summary information about the product view.
            - **Id** *(string) --*

              The product view identifier.
    """


_ClientSearchProductsResponseProductViewAggregationsTypeDef = TypedDict(
    "_ClientSearchProductsResponseProductViewAggregationsTypeDef",
    {"Value": str, "ApproximateCount": int},
    total=False,
)


class ClientSearchProductsResponseProductViewAggregationsTypeDef(
    _ClientSearchProductsResponseProductViewAggregationsTypeDef
):
    pass


_ClientSearchProductsResponseProductViewSummariesTypeDef = TypedDict(
    "_ClientSearchProductsResponseProductViewSummariesTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientSearchProductsResponseProductViewSummariesTypeDef(
    _ClientSearchProductsResponseProductViewSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information about a product view.
      - **Id** *(string) --*

        The product view identifier.
    """


_ClientSearchProductsResponseTypeDef = TypedDict(
    "_ClientSearchProductsResponseTypeDef",
    {
        "ProductViewSummaries": List[ClientSearchProductsResponseProductViewSummariesTypeDef],
        "ProductViewAggregations": Dict[
            str, List[ClientSearchProductsResponseProductViewAggregationsTypeDef]
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientSearchProductsResponseTypeDef(_ClientSearchProductsResponseTypeDef):
    """
    - *(dict) --*

      - **ProductViewSummaries** *(list) --*

        Information about the product views.
        - *(dict) --*

          Summary information about a product view.
          - **Id** *(string) --*

            The product view identifier.
    """


_ClientSearchProvisionedProductsAccessLevelFilterTypeDef = TypedDict(
    "_ClientSearchProvisionedProductsAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)


class ClientSearchProvisionedProductsAccessLevelFilterTypeDef(
    _ClientSearchProvisionedProductsAccessLevelFilterTypeDef
):
    """
    The access level to use to obtain results. The default is ``User`` .
    - **Key** *(string) --*

      The access level.
      * ``Account`` - Filter results based on the account.
      * ``Role`` - Filter results based on the federated role of the specified user.
      * ``User`` - Filter results based on the specified user.
    """


_ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef = TypedDict(
    "_ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef(
    _ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef
):
    pass


_ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef = TypedDict(
    "_ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "Tags": List[ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef],
        "PhysicalId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "UserArn": str,
        "UserArnSession": str,
    },
    total=False,
)


class ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef(
    _ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef
):
    """
    - *(dict) --*

      Information about a provisioned product.
      - **Name** *(string) --*

        The user-friendly name of the provisioned product.
    """


_ClientSearchProvisionedProductsResponseTypeDef = TypedDict(
    "_ClientSearchProvisionedProductsResponseTypeDef",
    {
        "ProvisionedProducts": List[
            ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef
        ],
        "TotalResultsCount": int,
        "NextPageToken": str,
    },
    total=False,
)


class ClientSearchProvisionedProductsResponseTypeDef(
    _ClientSearchProvisionedProductsResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisionedProducts** *(list) --*

        Information about the provisioned products.
        - *(dict) --*

          Information about a provisioned product.
          - **Name** *(string) --*

            The user-friendly name of the provisioned product.
    """


_ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef(
    _ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef
):
    pass


_ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef(
    _ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef
):
    pass


_ClientTerminateProvisionedProductResponseRecordDetailTypeDef = TypedDict(
    "_ClientTerminateProvisionedProductResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)


class ClientTerminateProvisionedProductResponseRecordDetailTypeDef(
    _ClientTerminateProvisionedProductResponseRecordDetailTypeDef
):
    """
    - **RecordDetail** *(dict) --*

      Information about the result of this request.
      - **RecordId** *(string) --*

        The identifier of the record.
    """


_ClientTerminateProvisionedProductResponseTypeDef = TypedDict(
    "_ClientTerminateProvisionedProductResponseTypeDef",
    {"RecordDetail": ClientTerminateProvisionedProductResponseRecordDetailTypeDef},
    total=False,
)


class ClientTerminateProvisionedProductResponseTypeDef(
    _ClientTerminateProvisionedProductResponseTypeDef
):
    """
    - *(dict) --*

      - **RecordDetail** *(dict) --*

        Information about the result of this request.
        - **RecordId** *(string) --*

          The identifier of the record.
    """


_ClientUpdateConstraintResponseConstraintDetailTypeDef = TypedDict(
    "_ClientUpdateConstraintResponseConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ClientUpdateConstraintResponseConstraintDetailTypeDef(
    _ClientUpdateConstraintResponseConstraintDetailTypeDef
):
    """
    - **ConstraintDetail** *(dict) --*

      Information about the constraint.
      - **ConstraintId** *(string) --*

        The identifier of the constraint.
    """


_ClientUpdateConstraintResponseTypeDef = TypedDict(
    "_ClientUpdateConstraintResponseTypeDef",
    {
        "ConstraintDetail": ClientUpdateConstraintResponseConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)


class ClientUpdateConstraintResponseTypeDef(_ClientUpdateConstraintResponseTypeDef):
    """
    - *(dict) --*

      - **ConstraintDetail** *(dict) --*

        Information about the constraint.
        - **ConstraintId** *(string) --*

          The identifier of the constraint.
    """


_RequiredClientUpdatePortfolioAddTagsTypeDef = TypedDict(
    "_RequiredClientUpdatePortfolioAddTagsTypeDef", {"Key": str}
)
_OptionalClientUpdatePortfolioAddTagsTypeDef = TypedDict(
    "_OptionalClientUpdatePortfolioAddTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdatePortfolioAddTagsTypeDef(
    _RequiredClientUpdatePortfolioAddTagsTypeDef, _OptionalClientUpdatePortfolioAddTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
      created when provisioning a product.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientUpdatePortfolioResponsePortfolioDetailTypeDef = TypedDict(
    "_ClientUpdatePortfolioResponsePortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientUpdatePortfolioResponsePortfolioDetailTypeDef(
    _ClientUpdatePortfolioResponsePortfolioDetailTypeDef
):
    """
    - **PortfolioDetail** *(dict) --*

      Information about the portfolio.
      - **Id** *(string) --*

        The portfolio identifier.
    """


_ClientUpdatePortfolioResponseTagsTypeDef = TypedDict(
    "_ClientUpdatePortfolioResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdatePortfolioResponseTagsTypeDef(_ClientUpdatePortfolioResponseTagsTypeDef):
    pass


_ClientUpdatePortfolioResponseTypeDef = TypedDict(
    "_ClientUpdatePortfolioResponseTypeDef",
    {
        "PortfolioDetail": ClientUpdatePortfolioResponsePortfolioDetailTypeDef,
        "Tags": List[ClientUpdatePortfolioResponseTagsTypeDef],
    },
    total=False,
)


class ClientUpdatePortfolioResponseTypeDef(_ClientUpdatePortfolioResponseTypeDef):
    """
    - *(dict) --*

      - **PortfolioDetail** *(dict) --*

        Information about the portfolio.
        - **Id** *(string) --*

          The portfolio identifier.
    """


_RequiredClientUpdateProductAddTagsTypeDef = TypedDict(
    "_RequiredClientUpdateProductAddTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateProductAddTagsTypeDef = TypedDict(
    "_OptionalClientUpdateProductAddTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateProductAddTagsTypeDef(
    _RequiredClientUpdateProductAddTagsTypeDef, _OptionalClientUpdateProductAddTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
      created when provisioning a product.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef = TypedDict(
    "_ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef(
    _ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef
):
    """
    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.
      - **Id** *(string) --*

        The product view identifier.
    """


_ClientUpdateProductResponseProductViewDetailTypeDef = TypedDict(
    "_ClientUpdateProductResponseProductViewDetailTypeDef",
    {
        "ProductViewSummary": ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientUpdateProductResponseProductViewDetailTypeDef(
    _ClientUpdateProductResponseProductViewDetailTypeDef
):
    """
    - **ProductViewDetail** *(dict) --*

      Information about the product view.
      - **ProductViewSummary** *(dict) --*

        Summary information about the product view.
        - **Id** *(string) --*

          The product view identifier.
    """


_ClientUpdateProductResponseTagsTypeDef = TypedDict(
    "_ClientUpdateProductResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdateProductResponseTagsTypeDef(_ClientUpdateProductResponseTagsTypeDef):
    pass


_ClientUpdateProductResponseTypeDef = TypedDict(
    "_ClientUpdateProductResponseTypeDef",
    {
        "ProductViewDetail": ClientUpdateProductResponseProductViewDetailTypeDef,
        "Tags": List[ClientUpdateProductResponseTagsTypeDef],
    },
    total=False,
)


class ClientUpdateProductResponseTypeDef(_ClientUpdateProductResponseTypeDef):
    """
    - *(dict) --*

      - **ProductViewDetail** *(dict) --*

        Information about the product view.
        - **ProductViewSummary** *(dict) --*

          Summary information about the product view.
          - **Id** *(string) --*

            The product view identifier.
    """


_ClientUpdateProvisionedProductPropertiesResponseTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductPropertiesResponseTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[str, str],
        "RecordId": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
    },
    total=False,
)


class ClientUpdateProvisionedProductPropertiesResponseTypeDef(
    _ClientUpdateProvisionedProductPropertiesResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisionedProductId** *(string) --*

        The provisioned product identifier.
    """


_ClientUpdateProvisionedProductProvisioningParametersTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductProvisioningParametersTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)


class ClientUpdateProvisionedProductProvisioningParametersTypeDef(
    _ClientUpdateProvisionedProductProvisioningParametersTypeDef
):
    """
    - *(dict) --*

      The parameter key-value pair used to update a provisioned product.
      - **Key** *(string) --*

        The parameter key.
    """


_ClientUpdateProvisionedProductProvisioningPreferencesTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
        "StackSetOperationType": Literal["CREATE", "UPDATE", "DELETE"],
    },
    total=False,
)


class ClientUpdateProvisionedProductProvisioningPreferencesTypeDef(
    _ClientUpdateProvisionedProductProvisioningPreferencesTypeDef
):
    """
    An object that contains information about the provisioning preferences for a stack set.
    - **StackSetAccounts** *(list) --*

      One or more AWS accounts that will have access to the provisioned product.
      Applicable only to a ``CFN_STACKSET`` provisioned product type.
      The AWS accounts specified should be within the list of accounts in the ``STACKSET``
      constraint. To get the list of accounts in the ``STACKSET`` constraint, use the
      ``DescribeProvisioningParameters`` operation.
      If no values are specified, the default value is all accounts from the ``STACKSET``
      constraint.
      - *(string) --*
    """


_ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef(
    _ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef
):
    pass


_ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef(
    _ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef
):
    pass


_ClientUpdateProvisionedProductResponseRecordDetailTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef],
        "RecordTags": List[ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)


class ClientUpdateProvisionedProductResponseRecordDetailTypeDef(
    _ClientUpdateProvisionedProductResponseRecordDetailTypeDef
):
    """
    - **RecordDetail** *(dict) --*

      Information about the result of the request.
      - **RecordId** *(string) --*

        The identifier of the record.
    """


_ClientUpdateProvisionedProductResponseTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductResponseTypeDef",
    {"RecordDetail": ClientUpdateProvisionedProductResponseRecordDetailTypeDef},
    total=False,
)


class ClientUpdateProvisionedProductResponseTypeDef(_ClientUpdateProvisionedProductResponseTypeDef):
    """
    - *(dict) --*

      - **RecordDetail** *(dict) --*

        Information about the result of the request.
        - **RecordId** *(string) --*

          The identifier of the record.
    """


_RequiredClientUpdateProvisionedProductTagsTypeDef = TypedDict(
    "_RequiredClientUpdateProvisionedProductTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateProvisionedProductTagsTypeDef = TypedDict(
    "_OptionalClientUpdateProvisionedProductTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateProvisionedProductTagsTypeDef(
    _RequiredClientUpdateProvisionedProductTagsTypeDef,
    _OptionalClientUpdateProvisionedProductTagsTypeDef,
):
    """
    - *(dict) --*

      Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
      created when provisioning a product.
      - **Key** *(string) --***[REQUIRED]**

        The tag key.
    """


_ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "_ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)


class ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef(
    _ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef
):
    """
    - **ProvisioningArtifactDetail** *(dict) --*

      Information about the provisioning artifact.
      - **Id** *(string) --*

        The identifier of the provisioning artifact.
    """


_ClientUpdateProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientUpdateProvisioningArtifactResponseTypeDef",
    {
        "ProvisioningArtifactDetail": ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)


class ClientUpdateProvisioningArtifactResponseTypeDef(
    _ClientUpdateProvisioningArtifactResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisioningArtifactDetail** *(dict) --*

        Information about the provisioning artifact.
        - **Id** *(string) --*

          The identifier of the provisioning artifact.
    """


_ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef = TypedDict(
    "_ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef(
    _ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef
):
    """
    - **ServiceActionSummary** *(dict) --*

      Summary information about the self-service action.
      - **Id** *(string) --*

        The self-service action identifier.
    """


_ClientUpdateServiceActionResponseServiceActionDetailTypeDef = TypedDict(
    "_ClientUpdateServiceActionResponseServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef,
        "Definition": Dict[str, str],
    },
    total=False,
)


class ClientUpdateServiceActionResponseServiceActionDetailTypeDef(
    _ClientUpdateServiceActionResponseServiceActionDetailTypeDef
):
    """
    - **ServiceActionDetail** *(dict) --*

      Detailed information about the self-service action.
      - **ServiceActionSummary** *(dict) --*

        Summary information about the self-service action.
        - **Id** *(string) --*

          The self-service action identifier.
    """


_ClientUpdateServiceActionResponseTypeDef = TypedDict(
    "_ClientUpdateServiceActionResponseTypeDef",
    {"ServiceActionDetail": ClientUpdateServiceActionResponseServiceActionDetailTypeDef},
    total=False,
)


class ClientUpdateServiceActionResponseTypeDef(_ClientUpdateServiceActionResponseTypeDef):
    """
    - *(dict) --*

      - **ServiceActionDetail** *(dict) --*

        Detailed information about the self-service action.
        - **ServiceActionSummary** *(dict) --*

          Summary information about the self-service action.
          - **Id** *(string) --*

            The self-service action identifier.
    """


_ClientUpdateTagOptionResponseTagOptionDetailTypeDef = TypedDict(
    "_ClientUpdateTagOptionResponseTagOptionDetailTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientUpdateTagOptionResponseTagOptionDetailTypeDef(
    _ClientUpdateTagOptionResponseTagOptionDetailTypeDef
):
    """
    - **TagOptionDetail** *(dict) --*

      Information about the TagOption.
      - **Key** *(string) --*

        The TagOption key.
    """


_ClientUpdateTagOptionResponseTypeDef = TypedDict(
    "_ClientUpdateTagOptionResponseTypeDef",
    {"TagOptionDetail": ClientUpdateTagOptionResponseTagOptionDetailTypeDef},
    total=False,
)


class ClientUpdateTagOptionResponseTypeDef(_ClientUpdateTagOptionResponseTypeDef):
    """
    - *(dict) --*

      - **TagOptionDetail** *(dict) --*

        Information about the TagOption.
        - **Key** *(string) --*

          The TagOption key.
    """


_ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef(
    _ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef = TypedDict(
    "_ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef(
    _ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a portfolio.
      - **Id** *(string) --*

        The portfolio identifier.
    """


_ListAcceptedPortfolioSharesPaginateResponseTypeDef = TypedDict(
    "_ListAcceptedPortfolioSharesPaginateResponseTypeDef",
    {
        "PortfolioDetails": List[
            ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListAcceptedPortfolioSharesPaginateResponseTypeDef(
    _ListAcceptedPortfolioSharesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **PortfolioDetails** *(list) --*

        Information about the portfolios.
        - *(dict) --*

          Information about a portfolio.
          - **Id** *(string) --*

            The portfolio identifier.
    """


_ListConstraintsForPortfolioPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConstraintsForPortfolioPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConstraintsForPortfolioPaginatePaginationConfigTypeDef(
    _ListConstraintsForPortfolioPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef = TypedDict(
    "_ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef(
    _ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a constraint.
      - **ConstraintId** *(string) --*

        The identifier of the constraint.
    """


_ListConstraintsForPortfolioPaginateResponseTypeDef = TypedDict(
    "_ListConstraintsForPortfolioPaginateResponseTypeDef",
    {
        "ConstraintDetails": List[
            ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListConstraintsForPortfolioPaginateResponseTypeDef(
    _ListConstraintsForPortfolioPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ConstraintDetails** *(list) --*

        Information about the constraints.
        - *(dict) --*

          Information about a constraint.
          - **ConstraintId** *(string) --*

            The identifier of the constraint.
    """


_ListLaunchPathsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLaunchPathsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLaunchPathsPaginatePaginationConfigTypeDef(
    _ListLaunchPathsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef = TypedDict(
    "_ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef",
    {"Type": str, "Description": str},
    total=False,
)


class ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef(
    _ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef
):
    pass


_ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef = TypedDict(
    "_ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef(
    _ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef
):
    pass


_ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef = TypedDict(
    "_ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef",
    {
        "Id": str,
        "ConstraintSummaries": List[
            ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef
        ],
        "Tags": List[ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef],
        "Name": str,
    },
    total=False,
)


class ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef(
    _ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information about a product path for a user.
      - **Id** *(string) --*

        The identifier of the product path.
    """


_ListLaunchPathsPaginateResponseTypeDef = TypedDict(
    "_ListLaunchPathsPaginateResponseTypeDef",
    {
        "LaunchPathSummaries": List[ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListLaunchPathsPaginateResponseTypeDef(_ListLaunchPathsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **LaunchPathSummaries** *(list) --*

        Information about the launch path.
        - *(dict) --*

          Summary information about a product path for a user.
          - **Id** *(string) --*

            The identifier of the product path.
    """


_ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef(
    _ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef = TypedDict(
    "_ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef",
    {"Type": Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"], "Value": str},
    total=False,
)


class ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef(
    _ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef
):
    """
    - *(dict) --*

      Information about the organization node.
      - **Type** *(string) --*

        The organization node type.
    """


_ListOrganizationPortfolioAccessPaginateResponseTypeDef = TypedDict(
    "_ListOrganizationPortfolioAccessPaginateResponseTypeDef",
    {
        "OrganizationNodes": List[
            ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListOrganizationPortfolioAccessPaginateResponseTypeDef(
    _ListOrganizationPortfolioAccessPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationNodes** *(list) --*

        Displays information about the organization nodes.
        - *(dict) --*

          Information about the organization node.
          - **Type** *(string) --*

            The organization node type.
    """


_ListPortfoliosForProductPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPortfoliosForProductPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPortfoliosForProductPaginatePaginationConfigTypeDef(
    _ListPortfoliosForProductPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef = TypedDict(
    "_ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef(
    _ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a portfolio.
      - **Id** *(string) --*

        The portfolio identifier.
    """


_ListPortfoliosForProductPaginateResponseTypeDef = TypedDict(
    "_ListPortfoliosForProductPaginateResponseTypeDef",
    {
        "PortfolioDetails": List[ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPortfoliosForProductPaginateResponseTypeDef(
    _ListPortfoliosForProductPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **PortfolioDetails** *(list) --*

        Information about the portfolios.
        - *(dict) --*

          Information about a portfolio.
          - **Id** *(string) --*

            The portfolio identifier.
    """


_ListPortfoliosPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPortfoliosPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPortfoliosPaginatePaginationConfigTypeDef(_ListPortfoliosPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPortfoliosPaginateResponsePortfolioDetailsTypeDef = TypedDict(
    "_ListPortfoliosPaginateResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ListPortfoliosPaginateResponsePortfolioDetailsTypeDef(
    _ListPortfoliosPaginateResponsePortfolioDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a portfolio.
      - **Id** *(string) --*

        The portfolio identifier.
    """


_ListPortfoliosPaginateResponseTypeDef = TypedDict(
    "_ListPortfoliosPaginateResponseTypeDef",
    {
        "PortfolioDetails": List[ListPortfoliosPaginateResponsePortfolioDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPortfoliosPaginateResponseTypeDef(_ListPortfoliosPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **PortfolioDetails** *(list) --*

        Information about the portfolios.
        - *(dict) --*

          Information about a portfolio.
          - **Id** *(string) --*

            The portfolio identifier.
    """


_ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef(
    _ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef = TypedDict(
    "_ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef",
    {"PrincipalARN": str, "PrincipalType": str},
    total=False,
)


class ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef(
    _ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef
):
    """
    - *(dict) --*

      Information about a principal.
      - **PrincipalARN** *(string) --*

        The ARN of the principal (IAM user, role, or group).
    """


_ListPrincipalsForPortfolioPaginateResponseTypeDef = TypedDict(
    "_ListPrincipalsForPortfolioPaginateResponseTypeDef",
    {
        "Principals": List[ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPrincipalsForPortfolioPaginateResponseTypeDef(
    _ListPrincipalsForPortfolioPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Principals** *(list) --*

        The IAM principals (users or roles) associated with the portfolio.
        - *(dict) --*

          Information about a principal.
          - **PrincipalARN** *(string) --*

            The ARN of the principal (IAM user, role, or group).
    """


_ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef = TypedDict(
    "_ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)


class ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef(
    _ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef
):
    """
    The access level to use to obtain results. The default is ``User`` .
    - **Key** *(string) --*

      The access level.
      * ``Account`` - Filter results based on the account.
      * ``Role`` - Filter results based on the federated role of the specified user.
      * ``User`` - Filter results based on the specified user.
    """


_ListProvisionedProductPlansPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProvisionedProductPlansPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProvisionedProductPlansPaginatePaginationConfigTypeDef(
    _ListProvisionedProductPlansPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef = TypedDict(
    "_ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef(
    _ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef
):
    """
    - *(dict) --*

      Summary information about a plan.
      - **PlanName** *(string) --*

        The name of the plan.
    """


_ListProvisionedProductPlansPaginateResponseTypeDef = TypedDict(
    "_ListProvisionedProductPlansPaginateResponseTypeDef",
    {
        "ProvisionedProductPlans": List[
            ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListProvisionedProductPlansPaginateResponseTypeDef(
    _ListProvisionedProductPlansPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisionedProductPlans** *(list) --*

        Information about the plans.
        - *(dict) --*

          Summary information about a plan.
          - **PlanName** *(string) --*

            The name of the plan.
    """


_ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef
):
    """
    - **ProductViewSummary** *(dict) --*

      Summary information about a product view.
      - **Id** *(string) --*

        The product view identifier.
    """


_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef
):
    pass


_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef",
    {
        "ProductViewSummary": ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef,
        "ProvisioningArtifact": ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef,
    },
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a product view and a provisioning artifact.
      - **ProductViewSummary** *(dict) --*

        Summary information about a product view.
        - **Id** *(string) --*

          The product view identifier.
    """


_ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef",
    {
        "ProvisioningArtifactViews": List[
            ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisioningArtifactViews** *(list) --*

        An array of objects with information about product views and provisioning artifacts.
        - *(dict) --*

          An object that contains summary information about a product view and a provisioning
          artifact.
          - **ProductViewSummary** *(dict) --*

            Summary information about a product view.
            - **Id** *(string) --*

              The product view identifier.
    """


_ListRecordHistoryPaginateAccessLevelFilterTypeDef = TypedDict(
    "_ListRecordHistoryPaginateAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)


class ListRecordHistoryPaginateAccessLevelFilterTypeDef(
    _ListRecordHistoryPaginateAccessLevelFilterTypeDef
):
    """
    The access level to use to obtain results. The default is ``User`` .
    - **Key** *(string) --*

      The access level.
      * ``Account`` - Filter results based on the account.
      * ``Role`` - Filter results based on the federated role of the specified user.
      * ``User`` - Filter results based on the specified user.
    """


_ListRecordHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRecordHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRecordHistoryPaginatePaginationConfigTypeDef(
    _ListRecordHistoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef = TypedDict(
    "_ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef(
    _ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef
):
    pass


_ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef = TypedDict(
    "_ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef(
    _ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef
):
    pass


_ListRecordHistoryPaginateResponseRecordDetailsTypeDef = TypedDict(
    "_ListRecordHistoryPaginateResponseRecordDetailsTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef],
        "RecordTags": List[ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef],
    },
    total=False,
)


class ListRecordHistoryPaginateResponseRecordDetailsTypeDef(
    _ListRecordHistoryPaginateResponseRecordDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a request operation.
      - **RecordId** *(string) --*

        The identifier of the record.
    """


_ListRecordHistoryPaginateResponseTypeDef = TypedDict(
    "_ListRecordHistoryPaginateResponseTypeDef",
    {
        "RecordDetails": List[ListRecordHistoryPaginateResponseRecordDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListRecordHistoryPaginateResponseTypeDef(_ListRecordHistoryPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **RecordDetails** *(list) --*

        The records, in reverse chronological order.
        - *(dict) --*

          Information about a request operation.
          - **RecordId** *(string) --*

            The identifier of the record.
    """


_ListRecordHistoryPaginateSearchFilterTypeDef = TypedDict(
    "_ListRecordHistoryPaginateSearchFilterTypeDef", {"Key": str, "Value": str}, total=False
)


class ListRecordHistoryPaginateSearchFilterTypeDef(_ListRecordHistoryPaginateSearchFilterTypeDef):
    """
    The search filter to scope the results.
    - **Key** *(string) --*

      The filter key.
      * ``product`` - Filter results based on the specified product identifier.
      * ``provisionedproduct`` - Filter results based on the provisioned product identifier.
    """


_ListResourcesForTagOptionPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourcesForTagOptionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourcesForTagOptionPaginatePaginationConfigTypeDef(
    _ListResourcesForTagOptionPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef = TypedDict(
    "_ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef",
    {"Id": str, "ARN": str, "Name": str, "Description": str, "CreatedTime": datetime},
    total=False,
)


class ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef(
    _ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a resource.
      - **Id** *(string) --*

        The identifier of the resource.
    """


_ListResourcesForTagOptionPaginateResponseTypeDef = TypedDict(
    "_ListResourcesForTagOptionPaginateResponseTypeDef",
    {
        "ResourceDetails": List[ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListResourcesForTagOptionPaginateResponseTypeDef(
    _ListResourcesForTagOptionPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourceDetails** *(list) --*

        Information about the resources.
        - *(dict) --*

          Information about a resource.
          - **Id** *(string) --*

            The identifier of the resource.
    """


_ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef(
    _ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef = TypedDict(
    "_ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef(
    _ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef
):
    """
    - *(dict) --*

      Detailed information about the self-service action.
      - **Id** *(string) --*

        The self-service action identifier.
    """


_ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef = TypedDict(
    "_ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef(
    _ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceActionSummaries** *(list) --*

        An object containing information about the self-service actions associated with the
        provisioning artifact.
        - *(dict) --*

          Detailed information about the self-service action.
          - **Id** *(string) --*

            The self-service action identifier.
    """


_ListServiceActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServiceActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServiceActionsPaginatePaginationConfigTypeDef(
    _ListServiceActionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListServiceActionsPaginateResponseServiceActionSummariesTypeDef = TypedDict(
    "_ListServiceActionsPaginateResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ListServiceActionsPaginateResponseServiceActionSummariesTypeDef(
    _ListServiceActionsPaginateResponseServiceActionSummariesTypeDef
):
    """
    - *(dict) --*

      Detailed information about the self-service action.
      - **Id** *(string) --*

        The self-service action identifier.
    """


_ListServiceActionsPaginateResponseTypeDef = TypedDict(
    "_ListServiceActionsPaginateResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ListServiceActionsPaginateResponseServiceActionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListServiceActionsPaginateResponseTypeDef(_ListServiceActionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ServiceActionSummaries** *(list) --*

        An object containing information about the service actions associated with the provisioning
        artifact.
        - *(dict) --*

          Detailed information about the self-service action.
          - **Id** *(string) --*

            The self-service action identifier.
    """


_ListTagOptionsPaginateFiltersTypeDef = TypedDict(
    "_ListTagOptionsPaginateFiltersTypeDef", {"Key": str, "Value": str, "Active": bool}, total=False
)


class ListTagOptionsPaginateFiltersTypeDef(_ListTagOptionsPaginateFiltersTypeDef):
    """
    The search filters. If no search filters are specified, the output includes all TagOptions.
    - **Key** *(string) --*

      The TagOption key.
    """


_ListTagOptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagOptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagOptionsPaginatePaginationConfigTypeDef(_ListTagOptionsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagOptionsPaginateResponseTagOptionDetailsTypeDef = TypedDict(
    "_ListTagOptionsPaginateResponseTagOptionDetailsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ListTagOptionsPaginateResponseTagOptionDetailsTypeDef(
    _ListTagOptionsPaginateResponseTagOptionDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a TagOption.
      - **Key** *(string) --*

        The TagOption key.
    """


_ListTagOptionsPaginateResponseTypeDef = TypedDict(
    "_ListTagOptionsPaginateResponseTypeDef",
    {
        "TagOptionDetails": List[ListTagOptionsPaginateResponseTagOptionDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListTagOptionsPaginateResponseTypeDef(_ListTagOptionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TagOptionDetails** *(list) --*

        Information about the TagOptions.
        - *(dict) --*

          Information about a TagOption.
          - **Key** *(string) --*

            The TagOption key.
    """


_ScanProvisionedProductsPaginateAccessLevelFilterTypeDef = TypedDict(
    "_ScanProvisionedProductsPaginateAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)


class ScanProvisionedProductsPaginateAccessLevelFilterTypeDef(
    _ScanProvisionedProductsPaginateAccessLevelFilterTypeDef
):
    """
    The access level to use to obtain results. The default is ``User`` .
    - **Key** *(string) --*

      The access level.
      * ``Account`` - Filter results based on the account.
      * ``Role`` - Filter results based on the federated role of the specified user.
      * ``User`` - Filter results based on the specified user.
    """


_ScanProvisionedProductsPaginatePaginationConfigTypeDef = TypedDict(
    "_ScanProvisionedProductsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ScanProvisionedProductsPaginatePaginationConfigTypeDef(
    _ScanProvisionedProductsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef = TypedDict(
    "_ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef(
    _ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef
):
    """
    - *(dict) --*

      Information about a provisioned product.
      - **Name** *(string) --*

        The user-friendly name of the provisioned product.
    """


_ScanProvisionedProductsPaginateResponseTypeDef = TypedDict(
    "_ScanProvisionedProductsPaginateResponseTypeDef",
    {
        "ProvisionedProducts": List[
            ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ScanProvisionedProductsPaginateResponseTypeDef(
    _ScanProvisionedProductsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ProvisionedProducts** *(list) --*

        Information about the provisioned products.
        - *(dict) --*

          Information about a provisioned product.
          - **Name** *(string) --*

            The user-friendly name of the provisioned product.
    """


_SearchProductsAsAdminPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchProductsAsAdminPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchProductsAsAdminPaginatePaginationConfigTypeDef(
    _SearchProductsAsAdminPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef = TypedDict(
    "_SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef(
    _SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef
):
    """
    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.
      - **Id** *(string) --*

        The product view identifier.
    """


_SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef = TypedDict(
    "_SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef",
    {
        "ProductViewSummary": SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef(
    _SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef
):
    """
    - *(dict) --*

      Information about a product view.
      - **ProductViewSummary** *(dict) --*

        Summary information about the product view.
        - **Id** *(string) --*

          The product view identifier.
    """


_SearchProductsAsAdminPaginateResponseTypeDef = TypedDict(
    "_SearchProductsAsAdminPaginateResponseTypeDef",
    {
        "ProductViewDetails": List[SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class SearchProductsAsAdminPaginateResponseTypeDef(_SearchProductsAsAdminPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ProductViewDetails** *(list) --*

        Information about the product views.
        - *(dict) --*

          Information about a product view.
          - **ProductViewSummary** *(dict) --*

            Summary information about the product view.
            - **Id** *(string) --*

              The product view identifier.
    """
