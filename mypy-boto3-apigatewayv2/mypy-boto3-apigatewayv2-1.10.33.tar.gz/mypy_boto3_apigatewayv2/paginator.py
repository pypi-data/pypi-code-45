"Main interface for apigatewayv2 service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_apigatewayv2.type_defs import (
    GetApisPaginatePaginationConfigTypeDef,
    GetApisPaginateResponseTypeDef,
    GetAuthorizersPaginatePaginationConfigTypeDef,
    GetAuthorizersPaginateResponseTypeDef,
    GetDeploymentsPaginatePaginationConfigTypeDef,
    GetDeploymentsPaginateResponseTypeDef,
    GetDomainNamesPaginatePaginationConfigTypeDef,
    GetDomainNamesPaginateResponseTypeDef,
    GetIntegrationResponsesPaginatePaginationConfigTypeDef,
    GetIntegrationResponsesPaginateResponseTypeDef,
    GetIntegrationsPaginatePaginationConfigTypeDef,
    GetIntegrationsPaginateResponseTypeDef,
    GetModelsPaginatePaginationConfigTypeDef,
    GetModelsPaginateResponseTypeDef,
    GetRouteResponsesPaginatePaginationConfigTypeDef,
    GetRouteResponsesPaginateResponseTypeDef,
    GetRoutesPaginatePaginationConfigTypeDef,
    GetRoutesPaginateResponseTypeDef,
    GetStagesPaginatePaginationConfigTypeDef,
    GetStagesPaginateResponseTypeDef,
)


__all__ = (
    "GetApisPaginator",
    "GetAuthorizersPaginator",
    "GetDeploymentsPaginator",
    "GetDomainNamesPaginator",
    "GetIntegrationResponsesPaginator",
    "GetIntegrationsPaginator",
    "GetModelsPaginator",
    "GetRouteResponsesPaginator",
    "GetRoutesPaginator",
    "GetStagesPaginator",
)


class GetApisPaginator(Boto3Paginator):
    """
    Paginator for `get_apis`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetApisPaginatePaginationConfigTypeDef = None
    ) -> GetApisPaginateResponseTypeDef:
        """
        [GetApis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetApis.paginate)
        """


class GetAuthorizersPaginator(Boto3Paginator):
    """
    Paginator for `get_authorizers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetAuthorizersPaginatePaginationConfigTypeDef = None
    ) -> GetAuthorizersPaginateResponseTypeDef:
        """
        [GetAuthorizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetAuthorizers.paginate)
        """


class GetDeploymentsPaginator(Boto3Paginator):
    """
    Paginator for `get_deployments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetDeploymentsPaginatePaginationConfigTypeDef = None
    ) -> GetDeploymentsPaginateResponseTypeDef:
        """
        [GetDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDeployments.paginate)
        """


class GetDomainNamesPaginator(Boto3Paginator):
    """
    Paginator for `get_domain_names`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetDomainNamesPaginatePaginationConfigTypeDef = None
    ) -> GetDomainNamesPaginateResponseTypeDef:
        """
        [GetDomainNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDomainNames.paginate)
        """


class GetIntegrationResponsesPaginator(Boto3Paginator):
    """
    Paginator for `get_integration_responses`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApiId: str,
        IntegrationId: str,
        PaginationConfig: GetIntegrationResponsesPaginatePaginationConfigTypeDef = None,
    ) -> GetIntegrationResponsesPaginateResponseTypeDef:
        """
        [GetIntegrationResponses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrationResponses.paginate)
        """


class GetIntegrationsPaginator(Boto3Paginator):
    """
    Paginator for `get_integrations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetIntegrationsPaginatePaginationConfigTypeDef = None
    ) -> GetIntegrationsPaginateResponseTypeDef:
        """
        [GetIntegrations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrations.paginate)
        """


class GetModelsPaginator(Boto3Paginator):
    """
    Paginator for `get_models`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetModelsPaginatePaginationConfigTypeDef = None
    ) -> GetModelsPaginateResponseTypeDef:
        """
        [GetModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetModels.paginate)
        """


class GetRouteResponsesPaginator(Boto3Paginator):
    """
    Paginator for `get_route_responses`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApiId: str,
        RouteId: str,
        PaginationConfig: GetRouteResponsesPaginatePaginationConfigTypeDef = None,
    ) -> GetRouteResponsesPaginateResponseTypeDef:
        """
        [GetRouteResponses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRouteResponses.paginate)
        """


class GetRoutesPaginator(Boto3Paginator):
    """
    Paginator for `get_routes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetRoutesPaginatePaginationConfigTypeDef = None
    ) -> GetRoutesPaginateResponseTypeDef:
        """
        [GetRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRoutes.paginate)
        """


class GetStagesPaginator(Boto3Paginator):
    """
    Paginator for `get_stages`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetStagesPaginatePaginationConfigTypeDef = None
    ) -> GetStagesPaginateResponseTypeDef:
        """
        [GetStages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetStages.paginate)
        """
