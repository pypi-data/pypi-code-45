"Main interface for servicecatalog service Paginators"
from __future__ import annotations

import sys
from typing import Dict, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_servicecatalog.type_defs import (
    ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef,
    ListAcceptedPortfolioSharesPaginateResponseTypeDef,
    ListConstraintsForPortfolioPaginatePaginationConfigTypeDef,
    ListConstraintsForPortfolioPaginateResponseTypeDef,
    ListLaunchPathsPaginatePaginationConfigTypeDef,
    ListLaunchPathsPaginateResponseTypeDef,
    ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef,
    ListOrganizationPortfolioAccessPaginateResponseTypeDef,
    ListPortfoliosForProductPaginatePaginationConfigTypeDef,
    ListPortfoliosForProductPaginateResponseTypeDef,
    ListPortfoliosPaginatePaginationConfigTypeDef,
    ListPortfoliosPaginateResponseTypeDef,
    ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef,
    ListPrincipalsForPortfolioPaginateResponseTypeDef,
    ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef,
    ListProvisionedProductPlansPaginatePaginationConfigTypeDef,
    ListProvisionedProductPlansPaginateResponseTypeDef,
    ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef,
    ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef,
    ListRecordHistoryPaginateAccessLevelFilterTypeDef,
    ListRecordHistoryPaginatePaginationConfigTypeDef,
    ListRecordHistoryPaginateResponseTypeDef,
    ListRecordHistoryPaginateSearchFilterTypeDef,
    ListResourcesForTagOptionPaginatePaginationConfigTypeDef,
    ListResourcesForTagOptionPaginateResponseTypeDef,
    ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef,
    ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef,
    ListServiceActionsPaginatePaginationConfigTypeDef,
    ListServiceActionsPaginateResponseTypeDef,
    ListTagOptionsPaginateFiltersTypeDef,
    ListTagOptionsPaginatePaginationConfigTypeDef,
    ListTagOptionsPaginateResponseTypeDef,
    ScanProvisionedProductsPaginateAccessLevelFilterTypeDef,
    ScanProvisionedProductsPaginatePaginationConfigTypeDef,
    ScanProvisionedProductsPaginateResponseTypeDef,
    SearchProductsAsAdminPaginatePaginationConfigTypeDef,
    SearchProductsAsAdminPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAcceptedPortfolioSharesPaginator",
    "ListConstraintsForPortfolioPaginator",
    "ListLaunchPathsPaginator",
    "ListOrganizationPortfolioAccessPaginator",
    "ListPortfoliosPaginator",
    "ListPortfoliosForProductPaginator",
    "ListPrincipalsForPortfolioPaginator",
    "ListProvisionedProductPlansPaginator",
    "ListProvisioningArtifactsForServiceActionPaginator",
    "ListRecordHistoryPaginator",
    "ListResourcesForTagOptionPaginator",
    "ListServiceActionsPaginator",
    "ListServiceActionsForProvisioningArtifactPaginator",
    "ListTagOptionsPaginator",
    "ScanProvisionedProductsPaginator",
    "SearchProductsAsAdminPaginator",
)


class ListAcceptedPortfolioSharesPaginator(Boto3Paginator):
    """
    Paginator for `list_accepted_portfolio_shares`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        PortfolioShareType: Literal["IMPORTED", "AWS_SERVICECATALOG", "AWS_ORGANIZATIONS"] = None,
        PaginationConfig: ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef = None,
    ) -> ListAcceptedPortfolioSharesPaginateResponseTypeDef:
        """
        [ListAcceptedPortfolioShares.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares.paginate)
        """


class ListConstraintsForPortfolioPaginator(Boto3Paginator):
    """
    Paginator for `list_constraints_for_portfolio`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        PaginationConfig: ListConstraintsForPortfolioPaginatePaginationConfigTypeDef = None,
    ) -> ListConstraintsForPortfolioPaginateResponseTypeDef:
        """
        [ListConstraintsForPortfolio.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio.paginate)
        """


class ListLaunchPathsPaginator(Boto3Paginator):
    """
    Paginator for `list_launch_paths`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PaginationConfig: ListLaunchPathsPaginatePaginationConfigTypeDef = None,
    ) -> ListLaunchPathsPaginateResponseTypeDef:
        """
        [ListLaunchPaths.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListLaunchPaths.paginate)
        """


class ListOrganizationPortfolioAccessPaginator(Boto3Paginator):
    """
    Paginator for `list_organization_portfolio_access`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PortfolioId: str,
        OrganizationNodeType: Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"],
        AcceptLanguage: str = None,
        PaginationConfig: ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef = None,
    ) -> ListOrganizationPortfolioAccessPaginateResponseTypeDef:
        """
        [ListOrganizationPortfolioAccess.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess.paginate)
        """


class ListPortfoliosPaginator(Boto3Paginator):
    """
    Paginator for `list_portfolios`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        PaginationConfig: ListPortfoliosPaginatePaginationConfigTypeDef = None,
    ) -> ListPortfoliosPaginateResponseTypeDef:
        """
        [ListPortfolios.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfolios.paginate)
        """


class ListPortfoliosForProductPaginator(Boto3Paginator):
    """
    Paginator for `list_portfolios_for_product`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PaginationConfig: ListPortfoliosForProductPaginatePaginationConfigTypeDef = None,
    ) -> ListPortfoliosForProductPaginateResponseTypeDef:
        """
        [ListPortfoliosForProduct.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfoliosForProduct.paginate)
        """


class ListPrincipalsForPortfolioPaginator(Boto3Paginator):
    """
    Paginator for `list_principals_for_portfolio`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PaginationConfig: ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef = None,
    ) -> ListPrincipalsForPortfolioPaginateResponseTypeDef:
        """
        [ListPrincipalsForPortfolio.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio.paginate)
        """


class ListProvisionedProductPlansPaginator(Boto3Paginator):
    """
    Paginator for `list_provisioned_product_plans`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        ProvisionProductId: str = None,
        AccessLevelFilter: ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef = None,
        PaginationConfig: ListProvisionedProductPlansPaginatePaginationConfigTypeDef = None,
    ) -> ListProvisionedProductPlansPaginateResponseTypeDef:
        """
        [ListProvisionedProductPlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisionedProductPlans.paginate)
        """


class ListProvisioningArtifactsForServiceActionPaginator(Boto3Paginator):
    """
    Paginator for `list_provisioning_artifacts_for_service_action`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceActionId: str,
        AcceptLanguage: str = None,
        PaginationConfig: ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef = None,
    ) -> ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef:
        """
        [ListProvisioningArtifactsForServiceAction.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction.paginate)
        """


class ListRecordHistoryPaginator(Boto3Paginator):
    """
    Paginator for `list_record_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: ListRecordHistoryPaginateAccessLevelFilterTypeDef = None,
        SearchFilter: ListRecordHistoryPaginateSearchFilterTypeDef = None,
        PaginationConfig: ListRecordHistoryPaginatePaginationConfigTypeDef = None,
    ) -> ListRecordHistoryPaginateResponseTypeDef:
        """
        [ListRecordHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListRecordHistory.paginate)
        """


class ListResourcesForTagOptionPaginator(Boto3Paginator):
    """
    Paginator for `list_resources_for_tag_option`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TagOptionId: str,
        ResourceType: str = None,
        PaginationConfig: ListResourcesForTagOptionPaginatePaginationConfigTypeDef = None,
    ) -> ListResourcesForTagOptionPaginateResponseTypeDef:
        """
        [ListResourcesForTagOption.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListResourcesForTagOption.paginate)
        """


class ListServiceActionsPaginator(Boto3Paginator):
    """
    Paginator for `list_service_actions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        PaginationConfig: ListServiceActionsPaginatePaginationConfigTypeDef = None,
    ) -> ListServiceActionsPaginateResponseTypeDef:
        """
        [ListServiceActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActions.paginate)
        """


class ListServiceActionsForProvisioningArtifactPaginator(Boto3Paginator):
    """
    Paginator for `list_service_actions_for_provisioning_artifact`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        PaginationConfig: ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef = None,
    ) -> ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef:
        """
        [ListServiceActionsForProvisioningArtifact.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact.paginate)
        """


class ListTagOptionsPaginator(Boto3Paginator):
    """
    Paginator for `list_tag_options`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: ListTagOptionsPaginateFiltersTypeDef = None,
        PaginationConfig: ListTagOptionsPaginatePaginationConfigTypeDef = None,
    ) -> ListTagOptionsPaginateResponseTypeDef:
        """
        [ListTagOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListTagOptions.paginate)
        """


class ScanProvisionedProductsPaginator(Boto3Paginator):
    """
    Paginator for `scan_provisioned_products`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: ScanProvisionedProductsPaginateAccessLevelFilterTypeDef = None,
        PaginationConfig: ScanProvisionedProductsPaginatePaginationConfigTypeDef = None,
    ) -> ScanProvisionedProductsPaginateResponseTypeDef:
        """
        [ScanProvisionedProducts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ScanProvisionedProducts.paginate)
        """


class SearchProductsAsAdminPaginator(Boto3Paginator):
    """
    Paginator for `search_products_as_admin`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AcceptLanguage: str = None,
        PortfolioId: str = None,
        Filters: Dict[str, List[str]] = None,
        SortBy: Literal["Title", "VersionCount", "CreationDate"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        ProductSource: str = None,
        PaginationConfig: SearchProductsAsAdminPaginatePaginationConfigTypeDef = None,
    ) -> SearchProductsAsAdminPaginateResponseTypeDef:
        """
        [SearchProductsAsAdmin.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/servicecatalog.html#ServiceCatalog.Paginator.SearchProductsAsAdmin.paginate)
        """
