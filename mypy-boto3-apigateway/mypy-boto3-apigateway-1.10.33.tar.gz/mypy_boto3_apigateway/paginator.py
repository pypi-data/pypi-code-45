"Main interface for apigateway service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_apigateway.type_defs import (
    GetApiKeysPaginatePaginationConfigTypeDef,
    GetApiKeysPaginateResponseTypeDef,
    GetAuthorizersPaginatePaginationConfigTypeDef,
    GetAuthorizersPaginateResponseTypeDef,
    GetBasePathMappingsPaginatePaginationConfigTypeDef,
    GetBasePathMappingsPaginateResponseTypeDef,
    GetClientCertificatesPaginatePaginationConfigTypeDef,
    GetClientCertificatesPaginateResponseTypeDef,
    GetDeploymentsPaginatePaginationConfigTypeDef,
    GetDeploymentsPaginateResponseTypeDef,
    GetDocumentationPartsPaginatePaginationConfigTypeDef,
    GetDocumentationPartsPaginateResponseTypeDef,
    GetDocumentationVersionsPaginatePaginationConfigTypeDef,
    GetDocumentationVersionsPaginateResponseTypeDef,
    GetDomainNamesPaginatePaginationConfigTypeDef,
    GetDomainNamesPaginateResponseTypeDef,
    GetGatewayResponsesPaginatePaginationConfigTypeDef,
    GetGatewayResponsesPaginateResponseTypeDef,
    GetModelsPaginatePaginationConfigTypeDef,
    GetModelsPaginateResponseTypeDef,
    GetRequestValidatorsPaginatePaginationConfigTypeDef,
    GetRequestValidatorsPaginateResponseTypeDef,
    GetResourcesPaginatePaginationConfigTypeDef,
    GetResourcesPaginateResponseTypeDef,
    GetRestApisPaginatePaginationConfigTypeDef,
    GetRestApisPaginateResponseTypeDef,
    GetSdkTypesPaginatePaginationConfigTypeDef,
    GetSdkTypesPaginateResponseTypeDef,
    GetUsagePaginatePaginationConfigTypeDef,
    GetUsagePaginateResponseTypeDef,
    GetUsagePlanKeysPaginatePaginationConfigTypeDef,
    GetUsagePlanKeysPaginateResponseTypeDef,
    GetUsagePlansPaginatePaginationConfigTypeDef,
    GetUsagePlansPaginateResponseTypeDef,
    GetVpcLinksPaginatePaginationConfigTypeDef,
    GetVpcLinksPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetApiKeysPaginator",
    "GetAuthorizersPaginator",
    "GetBasePathMappingsPaginator",
    "GetClientCertificatesPaginator",
    "GetDeploymentsPaginator",
    "GetDocumentationPartsPaginator",
    "GetDocumentationVersionsPaginator",
    "GetDomainNamesPaginator",
    "GetGatewayResponsesPaginator",
    "GetModelsPaginator",
    "GetRequestValidatorsPaginator",
    "GetResourcesPaginator",
    "GetRestApisPaginator",
    "GetSdkTypesPaginator",
    "GetUsagePaginator",
    "GetUsagePlanKeysPaginator",
    "GetUsagePlansPaginator",
    "GetVpcLinksPaginator",
)


class GetApiKeysPaginator(Boto3Paginator):
    """
    Paginator for `get_api_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
        PaginationConfig: GetApiKeysPaginatePaginationConfigTypeDef = None,
    ) -> GetApiKeysPaginateResponseTypeDef:
        """
        [GetApiKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys.paginate)
        """


class GetAuthorizersPaginator(Boto3Paginator):
    """
    Paginator for `get_authorizers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: GetAuthorizersPaginatePaginationConfigTypeDef = None
    ) -> GetAuthorizersPaginateResponseTypeDef:
        """
        [GetAuthorizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers.paginate)
        """


class GetBasePathMappingsPaginator(Boto3Paginator):
    """
    Paginator for `get_base_path_mappings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domainName: str,
        PaginationConfig: GetBasePathMappingsPaginatePaginationConfigTypeDef = None,
    ) -> GetBasePathMappingsPaginateResponseTypeDef:
        """
        [GetBasePathMappings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings.paginate)
        """


class GetClientCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `get_client_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetClientCertificatesPaginatePaginationConfigTypeDef = None
    ) -> GetClientCertificatesPaginateResponseTypeDef:
        """
        [GetClientCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates.paginate)
        """


class GetDeploymentsPaginator(Boto3Paginator):
    """
    Paginator for `get_deployments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: GetDeploymentsPaginatePaginationConfigTypeDef = None
    ) -> GetDeploymentsPaginateResponseTypeDef:
        """
        [GetDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments.paginate)
        """


class GetDocumentationPartsPaginator(Boto3Paginator):
    """
    Paginator for `get_documentation_parts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        type: Literal[
            "API",
            "AUTHORIZER",
            "MODEL",
            "RESOURCE",
            "METHOD",
            "PATH_PARAMETER",
            "QUERY_PARAMETER",
            "REQUEST_HEADER",
            "REQUEST_BODY",
            "RESPONSE",
            "RESPONSE_HEADER",
            "RESPONSE_BODY",
        ] = None,
        nameQuery: str = None,
        path: str = None,
        locationStatus: Literal["DOCUMENTED", "UNDOCUMENTED"] = None,
        PaginationConfig: GetDocumentationPartsPaginatePaginationConfigTypeDef = None,
    ) -> GetDocumentationPartsPaginateResponseTypeDef:
        """
        [GetDocumentationParts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts.paginate)
        """


class GetDocumentationVersionsPaginator(Boto3Paginator):
    """
    Paginator for `get_documentation_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: GetDocumentationVersionsPaginatePaginationConfigTypeDef = None,
    ) -> GetDocumentationVersionsPaginateResponseTypeDef:
        """
        [GetDocumentationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions.paginate)
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
        [GetDomainNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames.paginate)
        """


class GetGatewayResponsesPaginator(Boto3Paginator):
    """
    Paginator for `get_gateway_responses`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: GetGatewayResponsesPaginatePaginationConfigTypeDef = None,
    ) -> GetGatewayResponsesPaginateResponseTypeDef:
        """
        [GetGatewayResponses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses.paginate)
        """


class GetModelsPaginator(Boto3Paginator):
    """
    Paginator for `get_models`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: GetModelsPaginatePaginationConfigTypeDef = None
    ) -> GetModelsPaginateResponseTypeDef:
        """
        [GetModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetModels.paginate)
        """


class GetRequestValidatorsPaginator(Boto3Paginator):
    """
    Paginator for `get_request_validators`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: GetRequestValidatorsPaginatePaginationConfigTypeDef = None,
    ) -> GetRequestValidatorsPaginateResponseTypeDef:
        """
        [GetRequestValidators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators.paginate)
        """


class GetResourcesPaginator(Boto3Paginator):
    """
    Paginator for `get_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        embed: List[str] = None,
        PaginationConfig: GetResourcesPaginatePaginationConfigTypeDef = None,
    ) -> GetResourcesPaginateResponseTypeDef:
        """
        [GetResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetResources.paginate)
        """


class GetRestApisPaginator(Boto3Paginator):
    """
    Paginator for `get_rest_apis`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetRestApisPaginatePaginationConfigTypeDef = None
    ) -> GetRestApisPaginateResponseTypeDef:
        """
        [GetRestApis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis.paginate)
        """


class GetSdkTypesPaginator(Boto3Paginator):
    """
    Paginator for `get_sdk_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetSdkTypesPaginatePaginationConfigTypeDef = None
    ) -> GetSdkTypesPaginateResponseTypeDef:
        """
        [GetSdkTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes.paginate)
        """


class GetUsagePaginator(Boto3Paginator):
    """
    Paginator for `get_usage`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        PaginationConfig: GetUsagePaginatePaginationConfigTypeDef = None,
    ) -> GetUsagePaginateResponseTypeDef:
        """
        [GetUsage.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetUsage.paginate)
        """


class GetUsagePlanKeysPaginator(Boto3Paginator):
    """
    Paginator for `get_usage_plan_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        usagePlanId: str,
        nameQuery: str = None,
        PaginationConfig: GetUsagePlanKeysPaginatePaginationConfigTypeDef = None,
    ) -> GetUsagePlanKeysPaginateResponseTypeDef:
        """
        [GetUsagePlanKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys.paginate)
        """


class GetUsagePlansPaginator(Boto3Paginator):
    """
    Paginator for `get_usage_plans`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        keyId: str = None,
        PaginationConfig: GetUsagePlansPaginatePaginationConfigTypeDef = None,
    ) -> GetUsagePlansPaginateResponseTypeDef:
        """
        [GetUsagePlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans.paginate)
        """


class GetVpcLinksPaginator(Boto3Paginator):
    """
    Paginator for `get_vpc_links`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetVpcLinksPaginatePaginationConfigTypeDef = None
    ) -> GetVpcLinksPaginateResponseTypeDef:
        """
        [GetVpcLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks.paginate)
        """
