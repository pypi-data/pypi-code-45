"Main interface for apigateway service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateApiKeyResponseTypeDef",
    "ClientCreateApiKeyStageKeysTypeDef",
    "ClientCreateAuthorizerResponseTypeDef",
    "ClientCreateBasePathMappingResponseTypeDef",
    "ClientCreateDeploymentCanarySettingsTypeDef",
    "ClientCreateDeploymentResponseapiSummaryTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDocumentationPartLocationTypeDef",
    "ClientCreateDocumentationPartResponselocationTypeDef",
    "ClientCreateDocumentationPartResponseTypeDef",
    "ClientCreateDocumentationVersionResponseTypeDef",
    "ClientCreateDomainNameEndpointConfigurationTypeDef",
    "ClientCreateDomainNameResponseendpointConfigurationTypeDef",
    "ClientCreateDomainNameResponseTypeDef",
    "ClientCreateModelResponseTypeDef",
    "ClientCreateRequestValidatorResponseTypeDef",
    "ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    "ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef",
    "ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef",
    "ClientCreateResourceResponseresourceMethodsTypeDef",
    "ClientCreateResourceResponseTypeDef",
    "ClientCreateRestApiEndpointConfigurationTypeDef",
    "ClientCreateRestApiResponseendpointConfigurationTypeDef",
    "ClientCreateRestApiResponseTypeDef",
    "ClientCreateStageCanarySettingsTypeDef",
    "ClientCreateStageResponseaccessLogSettingsTypeDef",
    "ClientCreateStageResponsecanarySettingsTypeDef",
    "ClientCreateStageResponsemethodSettingsTypeDef",
    "ClientCreateStageResponseTypeDef",
    "ClientCreateUsagePlanApiStagesthrottleTypeDef",
    "ClientCreateUsagePlanApiStagesTypeDef",
    "ClientCreateUsagePlanKeyResponseTypeDef",
    "ClientCreateUsagePlanQuotaTypeDef",
    "ClientCreateUsagePlanResponseapiStagesthrottleTypeDef",
    "ClientCreateUsagePlanResponseapiStagesTypeDef",
    "ClientCreateUsagePlanResponsequotaTypeDef",
    "ClientCreateUsagePlanResponsethrottleTypeDef",
    "ClientCreateUsagePlanResponseTypeDef",
    "ClientCreateUsagePlanThrottleTypeDef",
    "ClientCreateVpcLinkResponseTypeDef",
    "ClientGenerateClientCertificateResponseTypeDef",
    "ClientGetAccountResponsethrottleSettingsTypeDef",
    "ClientGetAccountResponseTypeDef",
    "ClientGetApiKeyResponseTypeDef",
    "ClientGetApiKeysResponseitemsTypeDef",
    "ClientGetApiKeysResponseTypeDef",
    "ClientGetAuthorizerResponseTypeDef",
    "ClientGetAuthorizersResponseitemsTypeDef",
    "ClientGetAuthorizersResponseTypeDef",
    "ClientGetBasePathMappingResponseTypeDef",
    "ClientGetBasePathMappingsResponseitemsTypeDef",
    "ClientGetBasePathMappingsResponseTypeDef",
    "ClientGetClientCertificateResponseTypeDef",
    "ClientGetClientCertificatesResponseitemsTypeDef",
    "ClientGetClientCertificatesResponseTypeDef",
    "ClientGetDeploymentResponseapiSummaryTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentsResponseitemsapiSummaryTypeDef",
    "ClientGetDeploymentsResponseitemsTypeDef",
    "ClientGetDeploymentsResponseTypeDef",
    "ClientGetDocumentationPartResponselocationTypeDef",
    "ClientGetDocumentationPartResponseTypeDef",
    "ClientGetDocumentationPartsResponseitemslocationTypeDef",
    "ClientGetDocumentationPartsResponseitemsTypeDef",
    "ClientGetDocumentationPartsResponseTypeDef",
    "ClientGetDocumentationVersionResponseTypeDef",
    "ClientGetDocumentationVersionsResponseitemsTypeDef",
    "ClientGetDocumentationVersionsResponseTypeDef",
    "ClientGetDomainNameResponseendpointConfigurationTypeDef",
    "ClientGetDomainNameResponseTypeDef",
    "ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef",
    "ClientGetDomainNamesResponseitemsTypeDef",
    "ClientGetDomainNamesResponseTypeDef",
    "ClientGetExportResponseTypeDef",
    "ClientGetGatewayResponseResponseTypeDef",
    "ClientGetGatewayResponsesResponseitemsTypeDef",
    "ClientGetGatewayResponsesResponseTypeDef",
    "ClientGetIntegrationResponseResponseTypeDef",
    "ClientGetIntegrationResponseintegrationResponsesTypeDef",
    "ClientGetIntegrationResponseTypeDef",
    "ClientGetMethodResponseResponseTypeDef",
    "ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    "ClientGetMethodResponsemethodIntegrationTypeDef",
    "ClientGetMethodResponsemethodResponsesTypeDef",
    "ClientGetMethodResponseTypeDef",
    "ClientGetModelResponseTypeDef",
    "ClientGetModelTemplateResponseTypeDef",
    "ClientGetModelsResponseitemsTypeDef",
    "ClientGetModelsResponseTypeDef",
    "ClientGetRequestValidatorResponseTypeDef",
    "ClientGetRequestValidatorsResponseitemsTypeDef",
    "ClientGetRequestValidatorsResponseTypeDef",
    "ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    "ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef",
    "ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef",
    "ClientGetResourceResponseresourceMethodsTypeDef",
    "ClientGetResourceResponseTypeDef",
    "ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    "ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef",
    "ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef",
    "ClientGetResourcesResponseitemsresourceMethodsTypeDef",
    "ClientGetResourcesResponseitemsTypeDef",
    "ClientGetResourcesResponseTypeDef",
    "ClientGetRestApiResponseendpointConfigurationTypeDef",
    "ClientGetRestApiResponseTypeDef",
    "ClientGetRestApisResponseitemsendpointConfigurationTypeDef",
    "ClientGetRestApisResponseitemsTypeDef",
    "ClientGetRestApisResponseTypeDef",
    "ClientGetSdkResponseTypeDef",
    "ClientGetSdkTypeResponseconfigurationPropertiesTypeDef",
    "ClientGetSdkTypeResponseTypeDef",
    "ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef",
    "ClientGetSdkTypesResponseitemsTypeDef",
    "ClientGetSdkTypesResponseTypeDef",
    "ClientGetStageResponseaccessLogSettingsTypeDef",
    "ClientGetStageResponsecanarySettingsTypeDef",
    "ClientGetStageResponsemethodSettingsTypeDef",
    "ClientGetStageResponseTypeDef",
    "ClientGetStagesResponseitemaccessLogSettingsTypeDef",
    "ClientGetStagesResponseitemcanarySettingsTypeDef",
    "ClientGetStagesResponseitemmethodSettingsTypeDef",
    "ClientGetStagesResponseitemTypeDef",
    "ClientGetStagesResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientGetUsagePlanKeyResponseTypeDef",
    "ClientGetUsagePlanKeysResponseitemsTypeDef",
    "ClientGetUsagePlanKeysResponseTypeDef",
    "ClientGetUsagePlanResponseapiStagesthrottleTypeDef",
    "ClientGetUsagePlanResponseapiStagesTypeDef",
    "ClientGetUsagePlanResponsequotaTypeDef",
    "ClientGetUsagePlanResponsethrottleTypeDef",
    "ClientGetUsagePlanResponseTypeDef",
    "ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef",
    "ClientGetUsagePlansResponseitemsapiStagesTypeDef",
    "ClientGetUsagePlansResponseitemsquotaTypeDef",
    "ClientGetUsagePlansResponseitemsthrottleTypeDef",
    "ClientGetUsagePlansResponseitemsTypeDef",
    "ClientGetUsagePlansResponseTypeDef",
    "ClientGetUsageResponseTypeDef",
    "ClientGetVpcLinkResponseTypeDef",
    "ClientGetVpcLinksResponseitemsTypeDef",
    "ClientGetVpcLinksResponseTypeDef",
    "ClientImportApiKeysResponseTypeDef",
    "ClientImportDocumentationPartsResponseTypeDef",
    "ClientImportRestApiResponseendpointConfigurationTypeDef",
    "ClientImportRestApiResponseTypeDef",
    "ClientPutGatewayResponseResponseTypeDef",
    "ClientPutIntegrationResponseResponseTypeDef",
    "ClientPutIntegrationResponseintegrationResponsesTypeDef",
    "ClientPutIntegrationResponseTypeDef",
    "ClientPutMethodResponseResponseTypeDef",
    "ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    "ClientPutMethodResponsemethodIntegrationTypeDef",
    "ClientPutMethodResponsemethodResponsesTypeDef",
    "ClientPutMethodResponseTypeDef",
    "ClientPutRestApiResponseendpointConfigurationTypeDef",
    "ClientPutRestApiResponseTypeDef",
    "ClientTestInvokeAuthorizerResponseTypeDef",
    "ClientTestInvokeMethodResponseTypeDef",
    "ClientUpdateAccountPatchOperationsTypeDef",
    "ClientUpdateAccountResponsethrottleSettingsTypeDef",
    "ClientUpdateAccountResponseTypeDef",
    "ClientUpdateApiKeyPatchOperationsTypeDef",
    "ClientUpdateApiKeyResponseTypeDef",
    "ClientUpdateAuthorizerPatchOperationsTypeDef",
    "ClientUpdateAuthorizerResponseTypeDef",
    "ClientUpdateBasePathMappingPatchOperationsTypeDef",
    "ClientUpdateBasePathMappingResponseTypeDef",
    "ClientUpdateClientCertificatePatchOperationsTypeDef",
    "ClientUpdateClientCertificateResponseTypeDef",
    "ClientUpdateDeploymentPatchOperationsTypeDef",
    "ClientUpdateDeploymentResponseapiSummaryTypeDef",
    "ClientUpdateDeploymentResponseTypeDef",
    "ClientUpdateDocumentationPartPatchOperationsTypeDef",
    "ClientUpdateDocumentationPartResponselocationTypeDef",
    "ClientUpdateDocumentationPartResponseTypeDef",
    "ClientUpdateDocumentationVersionPatchOperationsTypeDef",
    "ClientUpdateDocumentationVersionResponseTypeDef",
    "ClientUpdateDomainNamePatchOperationsTypeDef",
    "ClientUpdateDomainNameResponseendpointConfigurationTypeDef",
    "ClientUpdateDomainNameResponseTypeDef",
    "ClientUpdateGatewayResponsePatchOperationsTypeDef",
    "ClientUpdateGatewayResponseResponseTypeDef",
    "ClientUpdateIntegrationPatchOperationsTypeDef",
    "ClientUpdateIntegrationResponsePatchOperationsTypeDef",
    "ClientUpdateIntegrationResponseResponseTypeDef",
    "ClientUpdateIntegrationResponseintegrationResponsesTypeDef",
    "ClientUpdateIntegrationResponseTypeDef",
    "ClientUpdateMethodPatchOperationsTypeDef",
    "ClientUpdateMethodResponsePatchOperationsTypeDef",
    "ClientUpdateMethodResponseResponseTypeDef",
    "ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    "ClientUpdateMethodResponsemethodIntegrationTypeDef",
    "ClientUpdateMethodResponsemethodResponsesTypeDef",
    "ClientUpdateMethodResponseTypeDef",
    "ClientUpdateModelPatchOperationsTypeDef",
    "ClientUpdateModelResponseTypeDef",
    "ClientUpdateRequestValidatorPatchOperationsTypeDef",
    "ClientUpdateRequestValidatorResponseTypeDef",
    "ClientUpdateResourcePatchOperationsTypeDef",
    "ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    "ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef",
    "ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef",
    "ClientUpdateResourceResponseresourceMethodsTypeDef",
    "ClientUpdateResourceResponseTypeDef",
    "ClientUpdateRestApiPatchOperationsTypeDef",
    "ClientUpdateRestApiResponseendpointConfigurationTypeDef",
    "ClientUpdateRestApiResponseTypeDef",
    "ClientUpdateStagePatchOperationsTypeDef",
    "ClientUpdateStageResponseaccessLogSettingsTypeDef",
    "ClientUpdateStageResponsecanarySettingsTypeDef",
    "ClientUpdateStageResponsemethodSettingsTypeDef",
    "ClientUpdateStageResponseTypeDef",
    "ClientUpdateUsagePatchOperationsTypeDef",
    "ClientUpdateUsagePlanPatchOperationsTypeDef",
    "ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef",
    "ClientUpdateUsagePlanResponseapiStagesTypeDef",
    "ClientUpdateUsagePlanResponsequotaTypeDef",
    "ClientUpdateUsagePlanResponsethrottleTypeDef",
    "ClientUpdateUsagePlanResponseTypeDef",
    "ClientUpdateUsageResponseTypeDef",
    "ClientUpdateVpcLinkPatchOperationsTypeDef",
    "ClientUpdateVpcLinkResponseTypeDef",
    "GetApiKeysPaginatePaginationConfigTypeDef",
    "GetApiKeysPaginateResponseitemsTypeDef",
    "GetApiKeysPaginateResponseTypeDef",
    "GetAuthorizersPaginatePaginationConfigTypeDef",
    "GetAuthorizersPaginateResponseitemsTypeDef",
    "GetAuthorizersPaginateResponseTypeDef",
    "GetBasePathMappingsPaginatePaginationConfigTypeDef",
    "GetBasePathMappingsPaginateResponseitemsTypeDef",
    "GetBasePathMappingsPaginateResponseTypeDef",
    "GetClientCertificatesPaginatePaginationConfigTypeDef",
    "GetClientCertificatesPaginateResponseitemsTypeDef",
    "GetClientCertificatesPaginateResponseTypeDef",
    "GetDeploymentsPaginatePaginationConfigTypeDef",
    "GetDeploymentsPaginateResponseitemsapiSummaryTypeDef",
    "GetDeploymentsPaginateResponseitemsTypeDef",
    "GetDeploymentsPaginateResponseTypeDef",
    "GetDocumentationPartsPaginatePaginationConfigTypeDef",
    "GetDocumentationPartsPaginateResponseitemslocationTypeDef",
    "GetDocumentationPartsPaginateResponseitemsTypeDef",
    "GetDocumentationPartsPaginateResponseTypeDef",
    "GetDocumentationVersionsPaginatePaginationConfigTypeDef",
    "GetDocumentationVersionsPaginateResponseitemsTypeDef",
    "GetDocumentationVersionsPaginateResponseTypeDef",
    "GetDomainNamesPaginatePaginationConfigTypeDef",
    "GetDomainNamesPaginateResponseitemsendpointConfigurationTypeDef",
    "GetDomainNamesPaginateResponseitemsTypeDef",
    "GetDomainNamesPaginateResponseTypeDef",
    "GetGatewayResponsesPaginatePaginationConfigTypeDef",
    "GetGatewayResponsesPaginateResponseitemsTypeDef",
    "GetGatewayResponsesPaginateResponseTypeDef",
    "GetModelsPaginatePaginationConfigTypeDef",
    "GetModelsPaginateResponseitemsTypeDef",
    "GetModelsPaginateResponseTypeDef",
    "GetRequestValidatorsPaginatePaginationConfigTypeDef",
    "GetRequestValidatorsPaginateResponseitemsTypeDef",
    "GetRequestValidatorsPaginateResponseTypeDef",
    "GetResourcesPaginatePaginationConfigTypeDef",
    "GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    "GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationTypeDef",
    "GetResourcesPaginateResponseitemsresourceMethodsmethodResponsesTypeDef",
    "GetResourcesPaginateResponseitemsresourceMethodsTypeDef",
    "GetResourcesPaginateResponseitemsTypeDef",
    "GetResourcesPaginateResponseTypeDef",
    "GetRestApisPaginatePaginationConfigTypeDef",
    "GetRestApisPaginateResponseitemsendpointConfigurationTypeDef",
    "GetRestApisPaginateResponseitemsTypeDef",
    "GetRestApisPaginateResponseTypeDef",
    "GetSdkTypesPaginatePaginationConfigTypeDef",
    "GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef",
    "GetSdkTypesPaginateResponseitemsTypeDef",
    "GetSdkTypesPaginateResponseTypeDef",
    "GetUsagePaginatePaginationConfigTypeDef",
    "GetUsagePaginateResponseTypeDef",
    "GetUsagePlanKeysPaginatePaginationConfigTypeDef",
    "GetUsagePlanKeysPaginateResponseitemsTypeDef",
    "GetUsagePlanKeysPaginateResponseTypeDef",
    "GetUsagePlansPaginatePaginationConfigTypeDef",
    "GetUsagePlansPaginateResponseitemsapiStagesthrottleTypeDef",
    "GetUsagePlansPaginateResponseitemsapiStagesTypeDef",
    "GetUsagePlansPaginateResponseitemsquotaTypeDef",
    "GetUsagePlansPaginateResponseitemsthrottleTypeDef",
    "GetUsagePlansPaginateResponseitemsTypeDef",
    "GetUsagePlansPaginateResponseTypeDef",
    "GetVpcLinksPaginatePaginationConfigTypeDef",
    "GetVpcLinksPaginateResponseitemsTypeDef",
    "GetVpcLinksPaginateResponseTypeDef",
)


_ClientCreateApiKeyResponseTypeDef = TypedDict(
    "_ClientCreateApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateApiKeyResponseTypeDef(_ClientCreateApiKeyResponseTypeDef):
    """
    - *(dict) --*

      A resource that can be distributed to callers for executing  Method resources that require an
      API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
      callers with the API key can make requests to that stage.

        `Use API Keys
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__
    """


_ClientCreateApiKeyStageKeysTypeDef = TypedDict(
    "_ClientCreateApiKeyStageKeysTypeDef", {"restApiId": str, "stageName": str}, total=False
)


class ClientCreateApiKeyStageKeysTypeDef(_ClientCreateApiKeyStageKeysTypeDef):
    """
    - *(dict) --*

      A reference to a unique stage identified in the format ``{restApiId}/{stage}`` .
      - **restApiId** *(string) --*

        The string identifier of the associated  RestApi .
    """


_ClientCreateAuthorizerResponseTypeDef = TypedDict(
    "_ClientCreateAuthorizerResponseTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)


class ClientCreateAuthorizerResponseTypeDef(_ClientCreateAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      Represents an authorization layer for methods. If enabled on a method, API Gateway will
      activate the authorizer when a client calls the method.

        `Use Lambda Function as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html>`__
        `Use Cognito User Pool as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html>`__
    """


_ClientCreateBasePathMappingResponseTypeDef = TypedDict(
    "_ClientCreateBasePathMappingResponseTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)


class ClientCreateBasePathMappingResponseTypeDef(_ClientCreateBasePathMappingResponseTypeDef):
    """
    - *(dict) --*

      Represents the base path that callers of the API must provide as part of the URL after the
      domain name.

        A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi
        in a given stage of the owner  Account .  `Use Custom Domain Names
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_ClientCreateDeploymentCanarySettingsTypeDef = TypedDict(
    "_ClientCreateDeploymentCanarySettingsTypeDef",
    {"percentTraffic": float, "stageVariableOverrides": Dict[str, str], "useStageCache": bool},
    total=False,
)


class ClientCreateDeploymentCanarySettingsTypeDef(_ClientCreateDeploymentCanarySettingsTypeDef):
    """
    The input configuration for the canary deployment when the deployment is a canary release
    deployment.
    - **percentTraffic** *(float) --*

      The percentage (0.0-100.0) of traffic routed to the canary deployment.
    """


_ClientCreateDeploymentResponseapiSummaryTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class ClientCreateDeploymentResponseapiSummaryTypeDef(
    _ClientCreateDeploymentResponseapiSummaryTypeDef
):
    pass


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, ClientCreateDeploymentResponseapiSummaryTypeDef]],
    },
    total=False,
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    - *(dict) --*

      An immutable representation of a  RestApi resource that can be called by users using  Stages .
      A deployment must be associated with a  Stage for it to be callable over the Internet.

        To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view,
        update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified
        deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,
        Deployments ,  Stage , `AWS CLI
        <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS
        SDKs <https://aws.amazon.com/tools/>`__
    """


_RequiredClientCreateDocumentationPartLocationTypeDef = TypedDict(
    "_RequiredClientCreateDocumentationPartLocationTypeDef",
    {
        "type": Literal[
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
        ]
    },
)
_OptionalClientCreateDocumentationPartLocationTypeDef = TypedDict(
    "_OptionalClientCreateDocumentationPartLocationTypeDef",
    {"path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class ClientCreateDocumentationPartLocationTypeDef(
    _RequiredClientCreateDocumentationPartLocationTypeDef,
    _OptionalClientCreateDocumentationPartLocationTypeDef,
):
    """
    [Required] The location of the targeted API entity of the to-be-created documentation part.
    - **type** *(string) --***[REQUIRED]**

      [Required] The type of API entity to which the documentation content applies. Valid values are
      ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` ,
      ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` ,
      ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Content inheritance does not apply to any entity
      of the ``API`` , ``AUTHORIZER`` , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or ``RESOURCE``
      type.
    """


_ClientCreateDocumentationPartResponselocationTypeDef = TypedDict(
    "_ClientCreateDocumentationPartResponselocationTypeDef",
    {
        "type": Literal[
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
        ],
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)


class ClientCreateDocumentationPartResponselocationTypeDef(
    _ClientCreateDocumentationPartResponselocationTypeDef
):
    pass


_ClientCreateDocumentationPartResponseTypeDef = TypedDict(
    "_ClientCreateDocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": ClientCreateDocumentationPartResponselocationTypeDef,
        "properties": str,
    },
    total=False,
)


class ClientCreateDocumentationPartResponseTypeDef(_ClientCreateDocumentationPartResponseTypeDef):
    """
    - *(dict) --*

      A documentation part for a targeted API entity.
      A documentation part consists of a content map (``properties`` ) and a target (``location`` ).
      The target specifies an API entity to which the documentation content applies. The supported
      API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend
      on the API entity type. All valid fields are not required.
      The content map is a JSON string of API-specific key-value pairs. Although an API can use any
      shape for the content map, only the OpenAPI-compliant documentation fields will be injected
      into the associated API entity definition in the exported OpenAPI definition file.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationParts
    """


_ClientCreateDocumentationVersionResponseTypeDef = TypedDict(
    "_ClientCreateDocumentationVersionResponseTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class ClientCreateDocumentationVersionResponseTypeDef(
    _ClientCreateDocumentationVersionResponseTypeDef
):
    """
    - *(dict) --*

      A snapshot of the documentation of an API.
      Publishing API documentation involves creating a documentation version associated with an API
      stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationPart ,  DocumentationVersions
    """


_ClientCreateDomainNameEndpointConfigurationTypeDef = TypedDict(
    "_ClientCreateDomainNameEndpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientCreateDomainNameEndpointConfigurationTypeDef(
    _ClientCreateDomainNameEndpointConfigurationTypeDef
):
    """
    The endpoint configuration of this  DomainName showing the endpoint types of the domain name.
    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For
      an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a
      regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a private
      API, the endpoint type is ``PRIVATE`` .
      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most suitable
        for mobile applications; ``REGIONAL`` for regional API endpoint setup, most suitable for
        calling from AWS Region; and ``PRIVATE`` for private APIs.
    """


_ClientCreateDomainNameResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientCreateDomainNameResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientCreateDomainNameResponseendpointConfigurationTypeDef(
    _ClientCreateDomainNameResponseendpointConfigurationTypeDef
):
    pass


_ClientCreateDomainNameResponseTypeDef = TypedDict(
    "_ClientCreateDomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientCreateDomainNameResponseendpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateDomainNameResponseTypeDef(_ClientCreateDomainNameResponseTypeDef):
    """
    - *(dict) --*

      Represents a custom domain name as a user-friendly host name of an API ( RestApi ).
      When you deploy an API, API Gateway creates a default host name for the API. This default API
      host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the
      default host name, you can access the API's root resource with the URL of
      ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a
      custom domain name of ``apis.example.com`` for this API, you can then access the same resource
      using the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path
      mapping ( BasePathMapping ) of your API under the custom domain name.

        `Set a Custom Host Name for an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_ClientCreateModelResponseTypeDef = TypedDict(
    "_ClientCreateModelResponseTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class ClientCreateModelResponseTypeDef(_ClientCreateModelResponseTypeDef):
    """
    - *(dict) --*

      Represents the data structure of a method's request or response payload.
      A request model defines the data structure of the client-supplied request payload. A response
      model defines the data structure of the response payload returned by the back end. Although
      not required, models are useful for mapping payloads between the front end and back end.
      A model is used for generating an API's SDK, validating the input request body, and creating a
      skeletal mapping template.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__
    """


_ClientCreateRequestValidatorResponseTypeDef = TypedDict(
    "_ClientCreateRequestValidatorResponseTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)


class ClientCreateRequestValidatorResponseTypeDef(_ClientCreateRequestValidatorResponseTypeDef):
    """
    - *(dict) --*

      A set of validation rules for incoming  Method requests.
      In OpenAPI, a  RequestValidator of an API is defined by the
      `x-amazon-apigateway-request-validators.requestValidator
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.requestValidator.html>`__
      object. It the referenced using the `x-amazon-apigateway-request-validator
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validator>`__
      property.

        `Enable Basic Request Validation in API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__
    """


_ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "_ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef(
    _ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef
):
    pass


_ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef = TypedDict(
    "_ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str,
            ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef,
        ],
    },
    total=False,
)


class ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef(
    _ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef
):
    pass


_ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef = TypedDict(
    "_ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef(
    _ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef
):
    pass


_ClientCreateResourceResponseresourceMethodsTypeDef = TypedDict(
    "_ClientCreateResourceResponseresourceMethodsTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[
            str, ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef
        ],
        "methodIntegration": ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)


class ClientCreateResourceResponseresourceMethodsTypeDef(
    _ClientCreateResourceResponseresourceMethodsTypeDef
):
    pass


_ClientCreateResourceResponseTypeDef = TypedDict(
    "_ClientCreateResourceResponseTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, ClientCreateResourceResponseresourceMethodsTypeDef],
    },
    total=False,
)


class ClientCreateResourceResponseTypeDef(_ClientCreateResourceResponseTypeDef):
    """
    - *(dict) --*

      Represents an API resource.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientCreateRestApiEndpointConfigurationTypeDef = TypedDict(
    "_ClientCreateRestApiEndpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientCreateRestApiEndpointConfigurationTypeDef(
    _ClientCreateRestApiEndpointConfigurationTypeDef
):
    """
    The endpoint configuration of this  RestApi showing the endpoint types of the API.
    - **types** *(list) --*

      A list of endpoint types of an API ( RestApi ) or its custom domain name ( DomainName ). For
      an edge-optimized API and its custom domain name, the endpoint type is ``"EDGE"`` . For a
      regional API and its custom domain name, the endpoint type is ``REGIONAL`` . For a private
      API, the endpoint type is ``PRIVATE`` .
      - *(string) --*

        The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup, most suitable
        for mobile applications; ``REGIONAL`` for regional API endpoint setup, most suitable for
        calling from AWS Region; and ``PRIVATE`` for private APIs.
    """


_ClientCreateRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientCreateRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientCreateRestApiResponseendpointConfigurationTypeDef(
    _ClientCreateRestApiResponseendpointConfigurationTypeDef
):
    pass


_ClientCreateRestApiResponseTypeDef = TypedDict(
    "_ClientCreateRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientCreateRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateRestApiResponseTypeDef(_ClientCreateRestApiResponseTypeDef):
    """
    - *(dict) --*

      Represents a REST API.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientCreateStageCanarySettingsTypeDef = TypedDict(
    "_ClientCreateStageCanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientCreateStageCanarySettingsTypeDef(_ClientCreateStageCanarySettingsTypeDef):
    """
    The canary deployment settings of this stage.
    - **percentTraffic** *(float) --*

      The percent (0-100) of traffic diverted to a canary deployment.
    """


_ClientCreateStageResponseaccessLogSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponseaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)


class ClientCreateStageResponseaccessLogSettingsTypeDef(
    _ClientCreateStageResponseaccessLogSettingsTypeDef
):
    pass


_ClientCreateStageResponsecanarySettingsTypeDef = TypedDict(
    "_ClientCreateStageResponsecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientCreateStageResponsecanarySettingsTypeDef(
    _ClientCreateStageResponsecanarySettingsTypeDef
):
    pass


_ClientCreateStageResponsemethodSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponsemethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": Literal[
            "FAIL_WITH_403", "SUCCEED_WITH_RESPONSE_HEADER", "SUCCEED_WITHOUT_RESPONSE_HEADER"
        ],
    },
    total=False,
)


class ClientCreateStageResponsemethodSettingsTypeDef(
    _ClientCreateStageResponsemethodSettingsTypeDef
):
    pass


_ClientCreateStageResponseTypeDef = TypedDict(
    "_ClientCreateStageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"],
        "cacheClusterStatus": Literal[
            "CREATE_IN_PROGRESS",
            "AVAILABLE",
            "DELETE_IN_PROGRESS",
            "NOT_AVAILABLE",
            "FLUSH_IN_PROGRESS",
        ],
        "methodSettings": Dict[str, ClientCreateStageResponsemethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientCreateStageResponseaccessLogSettingsTypeDef,
        "canarySettings": ClientCreateStageResponsecanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)


class ClientCreateStageResponseTypeDef(_ClientCreateStageResponseTypeDef):
    """
    - *(dict) --*

      Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

        `Deploy an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__
    """


_ClientCreateUsagePlanApiStagesthrottleTypeDef = TypedDict(
    "_ClientCreateUsagePlanApiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientCreateUsagePlanApiStagesthrottleTypeDef(_ClientCreateUsagePlanApiStagesthrottleTypeDef):
    pass


_ClientCreateUsagePlanApiStagesTypeDef = TypedDict(
    "_ClientCreateUsagePlanApiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientCreateUsagePlanApiStagesthrottleTypeDef],
    },
    total=False,
)


class ClientCreateUsagePlanApiStagesTypeDef(_ClientCreateUsagePlanApiStagesTypeDef):
    """
    - *(dict) --*

      API stage name of the associated API stage in a usage plan.
      - **apiId** *(string) --*

        API Id of the associated API stage in a usage plan.
    """


_ClientCreateUsagePlanKeyResponseTypeDef = TypedDict(
    "_ClientCreateUsagePlanKeyResponseTypeDef",
    {"id": str, "type": str, "value": str, "name": str},
    total=False,
)


class ClientCreateUsagePlanKeyResponseTypeDef(_ClientCreateUsagePlanKeyResponseTypeDef):
    """
    - *(dict) --*

      Represents a usage plan key to identify a plan customer.
      To associate an API stage with a selected API key in a usage plan, you must create a
      UsagePlanKey resource to represent the selected  ApiKey .

        "  `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
    """


_ClientCreateUsagePlanQuotaTypeDef = TypedDict(
    "_ClientCreateUsagePlanQuotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)


class ClientCreateUsagePlanQuotaTypeDef(_ClientCreateUsagePlanQuotaTypeDef):
    """
    The quota of the usage plan.
    - **limit** *(integer) --*

      The maximum number of requests that can be made in a given time period.
    """


_ClientCreateUsagePlanResponseapiStagesthrottleTypeDef = TypedDict(
    "_ClientCreateUsagePlanResponseapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientCreateUsagePlanResponseapiStagesthrottleTypeDef(
    _ClientCreateUsagePlanResponseapiStagesthrottleTypeDef
):
    pass


_ClientCreateUsagePlanResponseapiStagesTypeDef = TypedDict(
    "_ClientCreateUsagePlanResponseapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientCreateUsagePlanResponseapiStagesthrottleTypeDef],
    },
    total=False,
)


class ClientCreateUsagePlanResponseapiStagesTypeDef(_ClientCreateUsagePlanResponseapiStagesTypeDef):
    pass


_ClientCreateUsagePlanResponsequotaTypeDef = TypedDict(
    "_ClientCreateUsagePlanResponsequotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)


class ClientCreateUsagePlanResponsequotaTypeDef(_ClientCreateUsagePlanResponsequotaTypeDef):
    pass


_ClientCreateUsagePlanResponsethrottleTypeDef = TypedDict(
    "_ClientCreateUsagePlanResponsethrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientCreateUsagePlanResponsethrottleTypeDef(_ClientCreateUsagePlanResponsethrottleTypeDef):
    pass


_ClientCreateUsagePlanResponseTypeDef = TypedDict(
    "_ClientCreateUsagePlanResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ClientCreateUsagePlanResponseapiStagesTypeDef],
        "throttle": ClientCreateUsagePlanResponsethrottleTypeDef,
        "quota": ClientCreateUsagePlanResponsequotaTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateUsagePlanResponseTypeDef(_ClientCreateUsagePlanResponseTypeDef):
    """
    - *(dict) --*

      Represents a usage plan than can specify who can assess associated API stages with specified
      request limits and quotas.
      In a usage plan, you associate an API by specifying the API's Id and a stage name of the
      specified API. You add plan customers by adding API keys to the plan.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
    """


_ClientCreateUsagePlanThrottleTypeDef = TypedDict(
    "_ClientCreateUsagePlanThrottleTypeDef", {"burstLimit": int, "rateLimit": float}, total=False
)


class ClientCreateUsagePlanThrottleTypeDef(_ClientCreateUsagePlanThrottleTypeDef):
    """
    The throttling limits of the usage plan.
    - **burstLimit** *(integer) --*

      The API request burst limit, the maximum rate limit over a time ranging from one to a few
      seconds, depending upon whether the underlying token bucket is at its full capacity.
    """


_ClientCreateVpcLinkResponseTypeDef = TypedDict(
    "_ClientCreateVpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateVpcLinkResponseTypeDef(_ClientCreateVpcLinkResponseTypeDef):
    """
    - *(dict) --*

      A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud
      (VPC).
      To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway,
      you, as an API developer, create a  VpcLink resource targeted for one or more network load
      balancers of the VPC and then integrate an API method with a private integration that uses the
      VpcLink . The private integration has an integration type of ``HTTP`` or ``HTTP_PROXY`` and
      has a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to
      identify the  VpcLink used.
      - **id** *(string) --*

        The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .
    """


_ClientGenerateClientCertificateResponseTypeDef = TypedDict(
    "_ClientGenerateClientCertificateResponseTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGenerateClientCertificateResponseTypeDef(
    _ClientGenerateClientCertificateResponseTypeDef
):
    """
    - *(dict) --*

      Represents a client certificate used to configure client-side SSL authentication while sending
      requests to the integration endpoint.

        Client certificates are used to authenticate an API by the backend server. To authenticate
        an API client (or user), use IAM roles and policies, a custom  Authorizer or an Amazon
        Cognito user pool.  `Use Client-Side Certificate
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__
    """


_ClientGetAccountResponsethrottleSettingsTypeDef = TypedDict(
    "_ClientGetAccountResponsethrottleSettingsTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientGetAccountResponsethrottleSettingsTypeDef(
    _ClientGetAccountResponsethrottleSettingsTypeDef
):
    pass


_ClientGetAccountResponseTypeDef = TypedDict(
    "_ClientGetAccountResponseTypeDef",
    {
        "cloudwatchRoleArn": str,
        "throttleSettings": ClientGetAccountResponsethrottleSettingsTypeDef,
        "features": List[str],
        "apiKeyVersion": str,
    },
    total=False,
)


class ClientGetAccountResponseTypeDef(_ClientGetAccountResponseTypeDef):
    """
    - *(dict) --*

      Represents an AWS account that is associated with API Gateway.
      To view the account info, call ``GET`` on this resource.

        Error Codes
    """


_ClientGetApiKeyResponseTypeDef = TypedDict(
    "_ClientGetApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetApiKeyResponseTypeDef(_ClientGetApiKeyResponseTypeDef):
    """
    - *(dict) --*

      A resource that can be distributed to callers for executing  Method resources that require an
      API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
      callers with the API key can make requests to that stage.

        `Use API Keys
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__
    """


_ClientGetApiKeysResponseitemsTypeDef = TypedDict(
    "_ClientGetApiKeysResponseitemsTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetApiKeysResponseitemsTypeDef(_ClientGetApiKeysResponseitemsTypeDef):
    pass


_ClientGetApiKeysResponseTypeDef = TypedDict(
    "_ClientGetApiKeysResponseTypeDef",
    {"warnings": List[str], "position": str, "items": List[ClientGetApiKeysResponseitemsTypeDef]},
    total=False,
)


class ClientGetApiKeysResponseTypeDef(_ClientGetApiKeysResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of API keys as represented by an  ApiKeys resource.

        `Use API Keys
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__
    """


_ClientGetAuthorizerResponseTypeDef = TypedDict(
    "_ClientGetAuthorizerResponseTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)


class ClientGetAuthorizerResponseTypeDef(_ClientGetAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      Represents an authorization layer for methods. If enabled on a method, API Gateway will
      activate the authorizer when a client calls the method.

        `Use Lambda Function as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html>`__
        `Use Cognito User Pool as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html>`__
    """


_ClientGetAuthorizersResponseitemsTypeDef = TypedDict(
    "_ClientGetAuthorizersResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)


class ClientGetAuthorizersResponseitemsTypeDef(_ClientGetAuthorizersResponseitemsTypeDef):
    pass


_ClientGetAuthorizersResponseTypeDef = TypedDict(
    "_ClientGetAuthorizersResponseTypeDef",
    {"position": str, "items": List[ClientGetAuthorizersResponseitemsTypeDef]},
    total=False,
)


class ClientGetAuthorizersResponseTypeDef(_ClientGetAuthorizersResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  Authorizer resources.

        `Use Lambda Function as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html>`__
        `Use Cognito User Pool as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html>`__
    """


_ClientGetBasePathMappingResponseTypeDef = TypedDict(
    "_ClientGetBasePathMappingResponseTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)


class ClientGetBasePathMappingResponseTypeDef(_ClientGetBasePathMappingResponseTypeDef):
    """
    - *(dict) --*

      Represents the base path that callers of the API must provide as part of the URL after the
      domain name.

        A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi
        in a given stage of the owner  Account .  `Use Custom Domain Names
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_ClientGetBasePathMappingsResponseitemsTypeDef = TypedDict(
    "_ClientGetBasePathMappingsResponseitemsTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)


class ClientGetBasePathMappingsResponseitemsTypeDef(_ClientGetBasePathMappingsResponseitemsTypeDef):
    pass


_ClientGetBasePathMappingsResponseTypeDef = TypedDict(
    "_ClientGetBasePathMappingsResponseTypeDef",
    {"position": str, "items": List[ClientGetBasePathMappingsResponseitemsTypeDef]},
    total=False,
)


class ClientGetBasePathMappingsResponseTypeDef(_ClientGetBasePathMappingsResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  BasePathMapping resources.

        `Use Custom Domain Names
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_ClientGetClientCertificateResponseTypeDef = TypedDict(
    "_ClientGetClientCertificateResponseTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetClientCertificateResponseTypeDef(_ClientGetClientCertificateResponseTypeDef):
    """
    - *(dict) --*

      Represents a client certificate used to configure client-side SSL authentication while sending
      requests to the integration endpoint.

        Client certificates are used to authenticate an API by the backend server. To authenticate
        an API client (or user), use IAM roles and policies, a custom  Authorizer or an Amazon
        Cognito user pool.  `Use Client-Side Certificate
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__
    """


_ClientGetClientCertificatesResponseitemsTypeDef = TypedDict(
    "_ClientGetClientCertificatesResponseitemsTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetClientCertificatesResponseitemsTypeDef(
    _ClientGetClientCertificatesResponseitemsTypeDef
):
    pass


_ClientGetClientCertificatesResponseTypeDef = TypedDict(
    "_ClientGetClientCertificatesResponseTypeDef",
    {"position": str, "items": List[ClientGetClientCertificatesResponseitemsTypeDef]},
    total=False,
)


class ClientGetClientCertificatesResponseTypeDef(_ClientGetClientCertificatesResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  ClientCertificate resources.

        `Use Client-Side Certificate
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__
    """


_ClientGetDeploymentResponseapiSummaryTypeDef = TypedDict(
    "_ClientGetDeploymentResponseapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class ClientGetDeploymentResponseapiSummaryTypeDef(_ClientGetDeploymentResponseapiSummaryTypeDef):
    pass


_ClientGetDeploymentResponseTypeDef = TypedDict(
    "_ClientGetDeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, ClientGetDeploymentResponseapiSummaryTypeDef]],
    },
    total=False,
)


class ClientGetDeploymentResponseTypeDef(_ClientGetDeploymentResponseTypeDef):
    """
    - *(dict) --*

      An immutable representation of a  RestApi resource that can be called by users using  Stages .
      A deployment must be associated with a  Stage for it to be callable over the Internet.

        To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view,
        update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified
        deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,
        Deployments ,  Stage , `AWS CLI
        <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS
        SDKs <https://aws.amazon.com/tools/>`__
    """


_ClientGetDeploymentsResponseitemsapiSummaryTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseitemsapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class ClientGetDeploymentsResponseitemsapiSummaryTypeDef(
    _ClientGetDeploymentsResponseitemsapiSummaryTypeDef
):
    pass


_ClientGetDeploymentsResponseitemsTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseitemsTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, ClientGetDeploymentsResponseitemsapiSummaryTypeDef]],
    },
    total=False,
)


class ClientGetDeploymentsResponseitemsTypeDef(_ClientGetDeploymentsResponseitemsTypeDef):
    pass


_ClientGetDeploymentsResponseTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseTypeDef",
    {"position": str, "items": List[ClientGetDeploymentsResponseitemsTypeDef]},
    total=False,
)


class ClientGetDeploymentsResponseTypeDef(_ClientGetDeploymentsResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection resource that contains zero or more references to your existing
      deployments, and links that guide you on how to interact with your collection. The collection
      offers a paginated view of the contained deployments.

        To create a new deployment of a  RestApi , make a ``POST`` request against this resource. To
        view, update, or delete an existing deployment, make a ``GET`` , ``PATCH`` , or ``DELETE``
        request, respectively, on a specified  Deployment resource.  `Deploying an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__ ,
        `AWS CLI
        <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS
        SDKs <https://aws.amazon.com/tools/>`__
    """


_ClientGetDocumentationPartResponselocationTypeDef = TypedDict(
    "_ClientGetDocumentationPartResponselocationTypeDef",
    {
        "type": Literal[
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
        ],
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)


class ClientGetDocumentationPartResponselocationTypeDef(
    _ClientGetDocumentationPartResponselocationTypeDef
):
    pass


_ClientGetDocumentationPartResponseTypeDef = TypedDict(
    "_ClientGetDocumentationPartResponseTypeDef",
    {"id": str, "location": ClientGetDocumentationPartResponselocationTypeDef, "properties": str},
    total=False,
)


class ClientGetDocumentationPartResponseTypeDef(_ClientGetDocumentationPartResponseTypeDef):
    """
    - *(dict) --*

      A documentation part for a targeted API entity.
      A documentation part consists of a content map (``properties`` ) and a target (``location`` ).
      The target specifies an API entity to which the documentation content applies. The supported
      API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend
      on the API entity type. All valid fields are not required.
      The content map is a JSON string of API-specific key-value pairs. Although an API can use any
      shape for the content map, only the OpenAPI-compliant documentation fields will be injected
      into the associated API entity definition in the exported OpenAPI definition file.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationParts
    """


_ClientGetDocumentationPartsResponseitemslocationTypeDef = TypedDict(
    "_ClientGetDocumentationPartsResponseitemslocationTypeDef",
    {
        "type": Literal[
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
        ],
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)


class ClientGetDocumentationPartsResponseitemslocationTypeDef(
    _ClientGetDocumentationPartsResponseitemslocationTypeDef
):
    pass


_ClientGetDocumentationPartsResponseitemsTypeDef = TypedDict(
    "_ClientGetDocumentationPartsResponseitemsTypeDef",
    {
        "id": str,
        "location": ClientGetDocumentationPartsResponseitemslocationTypeDef,
        "properties": str,
    },
    total=False,
)


class ClientGetDocumentationPartsResponseitemsTypeDef(
    _ClientGetDocumentationPartsResponseitemsTypeDef
):
    pass


_ClientGetDocumentationPartsResponseTypeDef = TypedDict(
    "_ClientGetDocumentationPartsResponseTypeDef",
    {"position": str, "items": List[ClientGetDocumentationPartsResponseitemsTypeDef]},
    total=False,
)


class ClientGetDocumentationPartsResponseTypeDef(_ClientGetDocumentationPartsResponseTypeDef):
    """
    - *(dict) --*

      The collection of documentation parts of an API.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationPart
    """


_ClientGetDocumentationVersionResponseTypeDef = TypedDict(
    "_ClientGetDocumentationVersionResponseTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class ClientGetDocumentationVersionResponseTypeDef(_ClientGetDocumentationVersionResponseTypeDef):
    """
    - *(dict) --*

      A snapshot of the documentation of an API.
      Publishing API documentation involves creating a documentation version associated with an API
      stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationPart ,  DocumentationVersions
    """


_ClientGetDocumentationVersionsResponseitemsTypeDef = TypedDict(
    "_ClientGetDocumentationVersionsResponseitemsTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class ClientGetDocumentationVersionsResponseitemsTypeDef(
    _ClientGetDocumentationVersionsResponseitemsTypeDef
):
    pass


_ClientGetDocumentationVersionsResponseTypeDef = TypedDict(
    "_ClientGetDocumentationVersionsResponseTypeDef",
    {"position": str, "items": List[ClientGetDocumentationVersionsResponseitemsTypeDef]},
    total=False,
)


class ClientGetDocumentationVersionsResponseTypeDef(_ClientGetDocumentationVersionsResponseTypeDef):
    """
    - *(dict) --*

      The collection of documentation snapshots of an API.
      Use the  DocumentationVersions to manage documentation snapshots associated with various API
      stages.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationPart ,  DocumentationVersion
    """


_ClientGetDomainNameResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientGetDomainNameResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientGetDomainNameResponseendpointConfigurationTypeDef(
    _ClientGetDomainNameResponseendpointConfigurationTypeDef
):
    pass


_ClientGetDomainNameResponseTypeDef = TypedDict(
    "_ClientGetDomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientGetDomainNameResponseendpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDomainNameResponseTypeDef(_ClientGetDomainNameResponseTypeDef):
    """
    - *(dict) --*

      Represents a custom domain name as a user-friendly host name of an API ( RestApi ).
      When you deploy an API, API Gateway creates a default host name for the API. This default API
      host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the
      default host name, you can access the API's root resource with the URL of
      ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a
      custom domain name of ``apis.example.com`` for this API, you can then access the same resource
      using the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path
      mapping ( BasePathMapping ) of your API under the custom domain name.

        `Set a Custom Host Name for an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef = TypedDict(
    "_ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef(
    _ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef
):
    pass


_ClientGetDomainNamesResponseitemsTypeDef = TypedDict(
    "_ClientGetDomainNamesResponseitemsTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDomainNamesResponseitemsTypeDef(_ClientGetDomainNamesResponseitemsTypeDef):
    pass


_ClientGetDomainNamesResponseTypeDef = TypedDict(
    "_ClientGetDomainNamesResponseTypeDef",
    {"position": str, "items": List[ClientGetDomainNamesResponseitemsTypeDef]},
    total=False,
)


class ClientGetDomainNamesResponseTypeDef(_ClientGetDomainNamesResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  DomainName resources.

        `Use Client-Side Certificate
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_ClientGetExportResponseTypeDef = TypedDict(
    "_ClientGetExportResponseTypeDef",
    {"contentType": str, "contentDisposition": str, "body": StreamingBody},
    total=False,
)


class ClientGetExportResponseTypeDef(_ClientGetExportResponseTypeDef):
    """
    - *(dict) --*

      The binary blob response to  GetExport , which contains the generated SDK.
      - **contentType** *(string) --*

        The content-type header value in the HTTP response. This will correspond to a valid 'accept'
        type in the request.
    """


_ClientGetGatewayResponseResponseTypeDef = TypedDict(
    "_ClientGetGatewayResponseResponseTypeDef",
    {
        "responseType": Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)


class ClientGetGatewayResponseResponseTypeDef(_ClientGetGatewayResponseResponseTypeDef):
    """
    - *(dict) --*

      A gateway response of a given response type and status code, with optional response parameters
      and mapping templates.

        For more information about valid gateway response types, see `Gateway Response Types
        Supported by API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__
        Example: Get a Gateway Response of a given response type Request
    """


_ClientGetGatewayResponsesResponseitemsTypeDef = TypedDict(
    "_ClientGetGatewayResponsesResponseitemsTypeDef",
    {
        "responseType": Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)


class ClientGetGatewayResponsesResponseitemsTypeDef(_ClientGetGatewayResponsesResponseitemsTypeDef):
    pass


_ClientGetGatewayResponsesResponseTypeDef = TypedDict(
    "_ClientGetGatewayResponsesResponseTypeDef",
    {"position": str, "items": List[ClientGetGatewayResponsesResponseitemsTypeDef]},
    total=False,
)


class ClientGetGatewayResponsesResponseTypeDef(_ClientGetGatewayResponsesResponseTypeDef):
    """
    - *(dict) --*

      The collection of the  GatewayResponse instances of a  RestApi as a ``responseType`` -to-
      GatewayResponse object map of key-value pairs. As such, pagination is not supported for
      querying this collection.

        For more information about valid gateway response types, see `Gateway Response Types
        Supported by API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__
        Example: Get the collection of gateway responses of an API Request
    """


_ClientGetIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientGetIntegrationResponseResponseTypeDef(_ClientGetIntegrationResponseResponseTypeDef):
    """
    - *(dict) --*

      Represents an integration response. The status code must map to an existing  MethodResponse ,
      and parameters and templates can be used to transform the back-end response.

        `Creating an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientGetIntegrationResponseintegrationResponsesTypeDef = TypedDict(
    "_ClientGetIntegrationResponseintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientGetIntegrationResponseintegrationResponsesTypeDef(
    _ClientGetIntegrationResponseintegrationResponsesTypeDef
):
    pass


_ClientGetIntegrationResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponseTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, ClientGetIntegrationResponseintegrationResponsesTypeDef],
    },
    total=False,
)


class ClientGetIntegrationResponseTypeDef(_ClientGetIntegrationResponseTypeDef):
    """
    - *(dict) --*

      Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

        In the API Gateway console, the built-in Lambda integration is an AWS integration.
        `Creating an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientGetMethodResponseResponseTypeDef = TypedDict(
    "_ClientGetMethodResponseResponseTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientGetMethodResponseResponseTypeDef(_ClientGetMethodResponseResponseTypeDef):
    """
    - *(dict) --*

      Represents a method response of a given HTTP status code returned to the client. The method
      response is passed from the back end through the associated integration response that can be
      transformed using a mapping template.

        Example: A **MethodResponse** instance of an API Request
    """


_ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "_ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef(
    _ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef
):
    pass


_ClientGetMethodResponsemethodIntegrationTypeDef = TypedDict(
    "_ClientGetMethodResponsemethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef
        ],
    },
    total=False,
)


class ClientGetMethodResponsemethodIntegrationTypeDef(
    _ClientGetMethodResponsemethodIntegrationTypeDef
):
    pass


_ClientGetMethodResponsemethodResponsesTypeDef = TypedDict(
    "_ClientGetMethodResponsemethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientGetMethodResponsemethodResponsesTypeDef(_ClientGetMethodResponsemethodResponsesTypeDef):
    pass


_ClientGetMethodResponseTypeDef = TypedDict(
    "_ClientGetMethodResponseTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, ClientGetMethodResponsemethodResponsesTypeDef],
        "methodIntegration": ClientGetMethodResponsemethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)


class ClientGetMethodResponseTypeDef(_ClientGetMethodResponseTypeDef):
    """
    - *(dict) --*

      Represents a client-facing interface by which the client calls the API to access back-end
      resources. A **Method** resource is integrated with an  Integration resource. Both consist of
      a request and one or more responses. The method request takes the client input that is passed
      to the back end through the integration request. A method response returns the output from the
      back end to the client through an integration response. A method request is embodied in a
      **Method** resource, whereas an integration request is embodied in an  Integration resource.
      On the other hand, a method response is represented by a  MethodResponse resource, whereas an
      integration response is represented by an  IntegrationResponse resource.

        Example: Retrive the GET method on a specified resource Request
    """


_ClientGetModelResponseTypeDef = TypedDict(
    "_ClientGetModelResponseTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class ClientGetModelResponseTypeDef(_ClientGetModelResponseTypeDef):
    """
    - *(dict) --*

      Represents the data structure of a method's request or response payload.
      A request model defines the data structure of the client-supplied request payload. A response
      model defines the data structure of the response payload returned by the back end. Although
      not required, models are useful for mapping payloads between the front end and back end.
      A model is used for generating an API's SDK, validating the input request body, and creating a
      skeletal mapping template.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__
    """


_ClientGetModelTemplateResponseTypeDef = TypedDict(
    "_ClientGetModelTemplateResponseTypeDef", {"value": str}, total=False
)


class ClientGetModelTemplateResponseTypeDef(_ClientGetModelTemplateResponseTypeDef):
    """
    - *(dict) --*

      Represents a mapping template used to transform a payload.

        `Mapping Templates
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html#models-mappings-mappings>`__
    """


_ClientGetModelsResponseitemsTypeDef = TypedDict(
    "_ClientGetModelsResponseitemsTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class ClientGetModelsResponseitemsTypeDef(_ClientGetModelsResponseitemsTypeDef):
    pass


_ClientGetModelsResponseTypeDef = TypedDict(
    "_ClientGetModelsResponseTypeDef",
    {"position": str, "items": List[ClientGetModelsResponseitemsTypeDef]},
    total=False,
)


class ClientGetModelsResponseTypeDef(_ClientGetModelsResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  Model resources.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__
    """


_ClientGetRequestValidatorResponseTypeDef = TypedDict(
    "_ClientGetRequestValidatorResponseTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)


class ClientGetRequestValidatorResponseTypeDef(_ClientGetRequestValidatorResponseTypeDef):
    """
    - *(dict) --*

      A set of validation rules for incoming  Method requests.
      In OpenAPI, a  RequestValidator of an API is defined by the
      `x-amazon-apigateway-request-validators.requestValidator
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.requestValidator.html>`__
      object. It the referenced using the `x-amazon-apigateway-request-validator
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validator>`__
      property.

        `Enable Basic Request Validation in API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__
    """


_ClientGetRequestValidatorsResponseitemsTypeDef = TypedDict(
    "_ClientGetRequestValidatorsResponseitemsTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)


class ClientGetRequestValidatorsResponseitemsTypeDef(
    _ClientGetRequestValidatorsResponseitemsTypeDef
):
    pass


_ClientGetRequestValidatorsResponseTypeDef = TypedDict(
    "_ClientGetRequestValidatorsResponseTypeDef",
    {"position": str, "items": List[ClientGetRequestValidatorsResponseitemsTypeDef]},
    total=False,
)


class ClientGetRequestValidatorsResponseTypeDef(_ClientGetRequestValidatorsResponseTypeDef):
    """
    - *(dict) --*

      A collection of  RequestValidator resources of a given  RestApi .
      In OpenAPI, the  RequestValidators of an API is defined by the
      `x-amazon-apigateway-request-validators
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.html>`__
      extension.

        `Enable Basic Request Validation in API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__
    """


_ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "_ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef(
    _ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef
):
    pass


_ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef = TypedDict(
    "_ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str,
            ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef,
        ],
    },
    total=False,
)


class ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef(
    _ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef
):
    pass


_ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef = TypedDict(
    "_ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef(
    _ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef
):
    pass


_ClientGetResourceResponseresourceMethodsTypeDef = TypedDict(
    "_ClientGetResourceResponseresourceMethodsTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[
            str, ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef
        ],
        "methodIntegration": ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)


class ClientGetResourceResponseresourceMethodsTypeDef(
    _ClientGetResourceResponseresourceMethodsTypeDef
):
    pass


_ClientGetResourceResponseTypeDef = TypedDict(
    "_ClientGetResourceResponseTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, ClientGetResourceResponseresourceMethodsTypeDef],
    },
    total=False,
)


class ClientGetResourceResponseTypeDef(_ClientGetResourceResponseTypeDef):
    """
    - *(dict) --*

      Represents an API resource.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "_ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef(
    _ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef
):
    pass


_ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef = TypedDict(
    "_ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str,
            ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef,
        ],
    },
    total=False,
)


class ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef(
    _ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef
):
    pass


_ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef = TypedDict(
    "_ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef(
    _ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef
):
    pass


_ClientGetResourcesResponseitemsresourceMethodsTypeDef = TypedDict(
    "_ClientGetResourcesResponseitemsresourceMethodsTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[
            str, ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef
        ],
        "methodIntegration": ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)


class ClientGetResourcesResponseitemsresourceMethodsTypeDef(
    _ClientGetResourcesResponseitemsresourceMethodsTypeDef
):
    pass


_ClientGetResourcesResponseitemsTypeDef = TypedDict(
    "_ClientGetResourcesResponseitemsTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, ClientGetResourcesResponseitemsresourceMethodsTypeDef],
    },
    total=False,
)


class ClientGetResourcesResponseitemsTypeDef(_ClientGetResourcesResponseitemsTypeDef):
    pass


_ClientGetResourcesResponseTypeDef = TypedDict(
    "_ClientGetResourcesResponseTypeDef",
    {"position": str, "items": List[ClientGetResourcesResponseitemsTypeDef]},
    total=False,
)


class ClientGetResourcesResponseTypeDef(_ClientGetResourcesResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  Resource resources.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientGetRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientGetRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientGetRestApiResponseendpointConfigurationTypeDef(
    _ClientGetRestApiResponseendpointConfigurationTypeDef
):
    pass


_ClientGetRestApiResponseTypeDef = TypedDict(
    "_ClientGetRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientGetRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetRestApiResponseTypeDef(_ClientGetRestApiResponseTypeDef):
    """
    - *(dict) --*

      Represents a REST API.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientGetRestApisResponseitemsendpointConfigurationTypeDef = TypedDict(
    "_ClientGetRestApisResponseitemsendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientGetRestApisResponseitemsendpointConfigurationTypeDef(
    _ClientGetRestApisResponseitemsendpointConfigurationTypeDef
):
    pass


_ClientGetRestApisResponseitemsTypeDef = TypedDict(
    "_ClientGetRestApisResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientGetRestApisResponseitemsendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetRestApisResponseitemsTypeDef(_ClientGetRestApisResponseitemsTypeDef):
    pass


_ClientGetRestApisResponseTypeDef = TypedDict(
    "_ClientGetRestApisResponseTypeDef",
    {"position": str, "items": List[ClientGetRestApisResponseitemsTypeDef]},
    total=False,
)


class ClientGetRestApisResponseTypeDef(_ClientGetRestApisResponseTypeDef):
    """
    - *(dict) --*

      Contains references to your APIs and links that guide you in how to interact with your
      collection. A collection offers a paginated view of your APIs.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientGetSdkResponseTypeDef = TypedDict(
    "_ClientGetSdkResponseTypeDef",
    {"contentType": str, "contentDisposition": str, "body": StreamingBody},
    total=False,
)


class ClientGetSdkResponseTypeDef(_ClientGetSdkResponseTypeDef):
    """
    - *(dict) --*

      The binary blob response to  GetSdk , which contains the generated SDK.
      - **contentType** *(string) --*

        The content-type header value in the HTTP response.
    """


_ClientGetSdkTypeResponseconfigurationPropertiesTypeDef = TypedDict(
    "_ClientGetSdkTypeResponseconfigurationPropertiesTypeDef",
    {"name": str, "friendlyName": str, "description": str, "required": bool, "defaultValue": str},
    total=False,
)


class ClientGetSdkTypeResponseconfigurationPropertiesTypeDef(
    _ClientGetSdkTypeResponseconfigurationPropertiesTypeDef
):
    pass


_ClientGetSdkTypeResponseTypeDef = TypedDict(
    "_ClientGetSdkTypeResponseTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[ClientGetSdkTypeResponseconfigurationPropertiesTypeDef],
    },
    total=False,
)


class ClientGetSdkTypeResponseTypeDef(_ClientGetSdkTypeResponseTypeDef):
    """
    - *(dict) --*

      A type of SDK that API Gateway can generate.
      - **id** *(string) --*

        The identifier of an  SdkType instance.
    """


_ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef = TypedDict(
    "_ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef",
    {"name": str, "friendlyName": str, "description": str, "required": bool, "defaultValue": str},
    total=False,
)


class ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef(
    _ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef
):
    pass


_ClientGetSdkTypesResponseitemsTypeDef = TypedDict(
    "_ClientGetSdkTypesResponseitemsTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[
            ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef
        ],
    },
    total=False,
)


class ClientGetSdkTypesResponseitemsTypeDef(_ClientGetSdkTypesResponseitemsTypeDef):
    """
    - *(dict) --*

      A type of SDK that API Gateway can generate.
      - **id** *(string) --*

        The identifier of an  SdkType instance.
    """


_ClientGetSdkTypesResponseTypeDef = TypedDict(
    "_ClientGetSdkTypesResponseTypeDef",
    {"position": str, "items": List[ClientGetSdkTypesResponseitemsTypeDef]},
    total=False,
)


class ClientGetSdkTypesResponseTypeDef(_ClientGetSdkTypesResponseTypeDef):
    """
    - *(dict) --*

      The collection of  SdkType instances.
      - **position** *(string) --*
      - **items** *(list) --*

        The current page of elements from this collection.
        - *(dict) --*

          A type of SDK that API Gateway can generate.
          - **id** *(string) --*

            The identifier of an  SdkType instance.
    """


_ClientGetStageResponseaccessLogSettingsTypeDef = TypedDict(
    "_ClientGetStageResponseaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)


class ClientGetStageResponseaccessLogSettingsTypeDef(
    _ClientGetStageResponseaccessLogSettingsTypeDef
):
    pass


_ClientGetStageResponsecanarySettingsTypeDef = TypedDict(
    "_ClientGetStageResponsecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientGetStageResponsecanarySettingsTypeDef(_ClientGetStageResponsecanarySettingsTypeDef):
    pass


_ClientGetStageResponsemethodSettingsTypeDef = TypedDict(
    "_ClientGetStageResponsemethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": Literal[
            "FAIL_WITH_403", "SUCCEED_WITH_RESPONSE_HEADER", "SUCCEED_WITHOUT_RESPONSE_HEADER"
        ],
    },
    total=False,
)


class ClientGetStageResponsemethodSettingsTypeDef(_ClientGetStageResponsemethodSettingsTypeDef):
    pass


_ClientGetStageResponseTypeDef = TypedDict(
    "_ClientGetStageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"],
        "cacheClusterStatus": Literal[
            "CREATE_IN_PROGRESS",
            "AVAILABLE",
            "DELETE_IN_PROGRESS",
            "NOT_AVAILABLE",
            "FLUSH_IN_PROGRESS",
        ],
        "methodSettings": Dict[str, ClientGetStageResponsemethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientGetStageResponseaccessLogSettingsTypeDef,
        "canarySettings": ClientGetStageResponsecanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)


class ClientGetStageResponseTypeDef(_ClientGetStageResponseTypeDef):
    """
    - *(dict) --*

      Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

        `Deploy an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__
    """


_ClientGetStagesResponseitemaccessLogSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseitemaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)


class ClientGetStagesResponseitemaccessLogSettingsTypeDef(
    _ClientGetStagesResponseitemaccessLogSettingsTypeDef
):
    pass


_ClientGetStagesResponseitemcanarySettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseitemcanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientGetStagesResponseitemcanarySettingsTypeDef(
    _ClientGetStagesResponseitemcanarySettingsTypeDef
):
    pass


_ClientGetStagesResponseitemmethodSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseitemmethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": Literal[
            "FAIL_WITH_403", "SUCCEED_WITH_RESPONSE_HEADER", "SUCCEED_WITHOUT_RESPONSE_HEADER"
        ],
    },
    total=False,
)


class ClientGetStagesResponseitemmethodSettingsTypeDef(
    _ClientGetStagesResponseitemmethodSettingsTypeDef
):
    pass


_ClientGetStagesResponseitemTypeDef = TypedDict(
    "_ClientGetStagesResponseitemTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"],
        "cacheClusterStatus": Literal[
            "CREATE_IN_PROGRESS",
            "AVAILABLE",
            "DELETE_IN_PROGRESS",
            "NOT_AVAILABLE",
            "FLUSH_IN_PROGRESS",
        ],
        "methodSettings": Dict[str, ClientGetStagesResponseitemmethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientGetStagesResponseitemaccessLogSettingsTypeDef,
        "canarySettings": ClientGetStagesResponseitemcanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)


class ClientGetStagesResponseitemTypeDef(_ClientGetStagesResponseitemTypeDef):
    pass


_ClientGetStagesResponseTypeDef = TypedDict(
    "_ClientGetStagesResponseTypeDef",
    {"item": List[ClientGetStagesResponseitemTypeDef]},
    total=False,
)


class ClientGetStagesResponseTypeDef(_ClientGetStagesResponseTypeDef):
    """
    - *(dict) --*

      A list of  Stage resources that are associated with the  ApiKey resource.

        `Deploying API in Stages
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/stages.html>`__
    """


_ClientGetTagsResponseTypeDef = TypedDict(
    "_ClientGetTagsResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientGetTagsResponseTypeDef(_ClientGetTagsResponseTypeDef):
    """
    - *(dict) --*

      The collection of tags. Each tag element is associated with a given resource.
      - **tags** *(dict) --*

        The collection of tags. Each tag element is associated with a given resource.
        - *(string) --*

          - *(string) --*
    """


_ClientGetUsagePlanKeyResponseTypeDef = TypedDict(
    "_ClientGetUsagePlanKeyResponseTypeDef",
    {"id": str, "type": str, "value": str, "name": str},
    total=False,
)


class ClientGetUsagePlanKeyResponseTypeDef(_ClientGetUsagePlanKeyResponseTypeDef):
    """
    - *(dict) --*

      Represents a usage plan key to identify a plan customer.
      To associate an API stage with a selected API key in a usage plan, you must create a
      UsagePlanKey resource to represent the selected  ApiKey .

        "  `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
    """


_ClientGetUsagePlanKeysResponseitemsTypeDef = TypedDict(
    "_ClientGetUsagePlanKeysResponseitemsTypeDef",
    {"id": str, "type": str, "value": str, "name": str},
    total=False,
)


class ClientGetUsagePlanKeysResponseitemsTypeDef(_ClientGetUsagePlanKeysResponseitemsTypeDef):
    pass


_ClientGetUsagePlanKeysResponseTypeDef = TypedDict(
    "_ClientGetUsagePlanKeysResponseTypeDef",
    {"position": str, "items": List[ClientGetUsagePlanKeysResponseitemsTypeDef]},
    total=False,
)


class ClientGetUsagePlanKeysResponseTypeDef(_ClientGetUsagePlanKeysResponseTypeDef):
    """
    - *(dict) --*

      Represents the collection of usage plan keys added to usage plans for the associated API keys
      and, possibly, other types of keys.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
    """


_ClientGetUsagePlanResponseapiStagesthrottleTypeDef = TypedDict(
    "_ClientGetUsagePlanResponseapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientGetUsagePlanResponseapiStagesthrottleTypeDef(
    _ClientGetUsagePlanResponseapiStagesthrottleTypeDef
):
    pass


_ClientGetUsagePlanResponseapiStagesTypeDef = TypedDict(
    "_ClientGetUsagePlanResponseapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientGetUsagePlanResponseapiStagesthrottleTypeDef],
    },
    total=False,
)


class ClientGetUsagePlanResponseapiStagesTypeDef(_ClientGetUsagePlanResponseapiStagesTypeDef):
    pass


_ClientGetUsagePlanResponsequotaTypeDef = TypedDict(
    "_ClientGetUsagePlanResponsequotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)


class ClientGetUsagePlanResponsequotaTypeDef(_ClientGetUsagePlanResponsequotaTypeDef):
    pass


_ClientGetUsagePlanResponsethrottleTypeDef = TypedDict(
    "_ClientGetUsagePlanResponsethrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientGetUsagePlanResponsethrottleTypeDef(_ClientGetUsagePlanResponsethrottleTypeDef):
    pass


_ClientGetUsagePlanResponseTypeDef = TypedDict(
    "_ClientGetUsagePlanResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ClientGetUsagePlanResponseapiStagesTypeDef],
        "throttle": ClientGetUsagePlanResponsethrottleTypeDef,
        "quota": ClientGetUsagePlanResponsequotaTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetUsagePlanResponseTypeDef(_ClientGetUsagePlanResponseTypeDef):
    """
    - *(dict) --*

      Represents a usage plan than can specify who can assess associated API stages with specified
      request limits and quotas.
      In a usage plan, you associate an API by specifying the API's Id and a stage name of the
      specified API. You add plan customers by adding API keys to the plan.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
    """


_ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef = TypedDict(
    "_ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef(
    _ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef
):
    pass


_ClientGetUsagePlansResponseitemsapiStagesTypeDef = TypedDict(
    "_ClientGetUsagePlansResponseitemsapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef],
    },
    total=False,
)


class ClientGetUsagePlansResponseitemsapiStagesTypeDef(
    _ClientGetUsagePlansResponseitemsapiStagesTypeDef
):
    pass


_ClientGetUsagePlansResponseitemsquotaTypeDef = TypedDict(
    "_ClientGetUsagePlansResponseitemsquotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)


class ClientGetUsagePlansResponseitemsquotaTypeDef(_ClientGetUsagePlansResponseitemsquotaTypeDef):
    pass


_ClientGetUsagePlansResponseitemsthrottleTypeDef = TypedDict(
    "_ClientGetUsagePlansResponseitemsthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientGetUsagePlansResponseitemsthrottleTypeDef(
    _ClientGetUsagePlansResponseitemsthrottleTypeDef
):
    pass


_ClientGetUsagePlansResponseitemsTypeDef = TypedDict(
    "_ClientGetUsagePlansResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ClientGetUsagePlansResponseitemsapiStagesTypeDef],
        "throttle": ClientGetUsagePlansResponseitemsthrottleTypeDef,
        "quota": ClientGetUsagePlansResponseitemsquotaTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetUsagePlansResponseitemsTypeDef(_ClientGetUsagePlansResponseitemsTypeDef):
    pass


_ClientGetUsagePlansResponseTypeDef = TypedDict(
    "_ClientGetUsagePlansResponseTypeDef",
    {"position": str, "items": List[ClientGetUsagePlansResponseitemsTypeDef]},
    total=False,
)


class ClientGetUsagePlansResponseTypeDef(_ClientGetUsagePlansResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of usage plans for an AWS account.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
    """


_ClientGetUsageResponseTypeDef = TypedDict(
    "_ClientGetUsageResponseTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "position": str,
        "items": Dict[str, List[List[int]]],
    },
    total=False,
)


class ClientGetUsageResponseTypeDef(_ClientGetUsageResponseTypeDef):
    """
    - *(dict) --*

      Represents the usage data of a usage plan.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
        , `Manage Usage in a Usage Plan
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans-with-console.html#api-gateway-usage-plan-manage-usage>`__
    """


_ClientGetVpcLinkResponseTypeDef = TypedDict(
    "_ClientGetVpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetVpcLinkResponseTypeDef(_ClientGetVpcLinkResponseTypeDef):
    """
    - *(dict) --*

      A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud
      (VPC).
      To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway,
      you, as an API developer, create a  VpcLink resource targeted for one or more network load
      balancers of the VPC and then integrate an API method with a private integration that uses the
      VpcLink . The private integration has an integration type of ``HTTP`` or ``HTTP_PROXY`` and
      has a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to
      identify the  VpcLink used.
      - **id** *(string) --*

        The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .
    """


_ClientGetVpcLinksResponseitemsTypeDef = TypedDict(
    "_ClientGetVpcLinksResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetVpcLinksResponseitemsTypeDef(_ClientGetVpcLinksResponseitemsTypeDef):
    pass


_ClientGetVpcLinksResponseTypeDef = TypedDict(
    "_ClientGetVpcLinksResponseTypeDef",
    {"position": str, "items": List[ClientGetVpcLinksResponseitemsTypeDef]},
    total=False,
)


class ClientGetVpcLinksResponseTypeDef(_ClientGetVpcLinksResponseTypeDef):
    """
    - *(dict) --*

      The collection of VPC links under the caller's account in a region.

        `Getting Started with Private Integrations
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-private-integration.html>`__
        , `Set up Private Integrations
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html>`__
    """


_ClientImportApiKeysResponseTypeDef = TypedDict(
    "_ClientImportApiKeysResponseTypeDef", {"ids": List[str], "warnings": List[str]}, total=False
)


class ClientImportApiKeysResponseTypeDef(_ClientImportApiKeysResponseTypeDef):
    """
    - *(dict) --*

      The identifier of an  ApiKey used in a  UsagePlan .
      - **ids** *(list) --*

        A list of all the  ApiKey identifiers.
        - *(string) --*
    """


_ClientImportDocumentationPartsResponseTypeDef = TypedDict(
    "_ClientImportDocumentationPartsResponseTypeDef",
    {"ids": List[str], "warnings": List[str]},
    total=False,
)


class ClientImportDocumentationPartsResponseTypeDef(_ClientImportDocumentationPartsResponseTypeDef):
    """
    - *(dict) --*

      A collection of the imported  DocumentationPart identifiers.

        This is used to return the result when documentation parts in an external (e.g., OpenAPI)
        file are imported into API Gateway  `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        , `documentationpart\\:import
        <https://docs.aws.amazon.com/apigateway/api-reference/link-relation/documentationpart-import/>`__
        ,  DocumentationPart
    """


_ClientImportRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientImportRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientImportRestApiResponseendpointConfigurationTypeDef(
    _ClientImportRestApiResponseendpointConfigurationTypeDef
):
    pass


_ClientImportRestApiResponseTypeDef = TypedDict(
    "_ClientImportRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientImportRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientImportRestApiResponseTypeDef(_ClientImportRestApiResponseTypeDef):
    """
    - *(dict) --*

      Represents a REST API.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientPutGatewayResponseResponseTypeDef = TypedDict(
    "_ClientPutGatewayResponseResponseTypeDef",
    {
        "responseType": Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)


class ClientPutGatewayResponseResponseTypeDef(_ClientPutGatewayResponseResponseTypeDef):
    """
    - *(dict) --*

      A gateway response of a given response type and status code, with optional response parameters
      and mapping templates.

        For more information about valid gateway response types, see `Gateway Response Types
        Supported by API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__
        Example: Get a Gateway Response of a given response type Request
    """


_ClientPutIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientPutIntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientPutIntegrationResponseResponseTypeDef(_ClientPutIntegrationResponseResponseTypeDef):
    """
    - *(dict) --*

      Represents an integration response. The status code must map to an existing  MethodResponse ,
      and parameters and templates can be used to transform the back-end response.

        `Creating an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientPutIntegrationResponseintegrationResponsesTypeDef = TypedDict(
    "_ClientPutIntegrationResponseintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientPutIntegrationResponseintegrationResponsesTypeDef(
    _ClientPutIntegrationResponseintegrationResponsesTypeDef
):
    pass


_ClientPutIntegrationResponseTypeDef = TypedDict(
    "_ClientPutIntegrationResponseTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, ClientPutIntegrationResponseintegrationResponsesTypeDef],
    },
    total=False,
)


class ClientPutIntegrationResponseTypeDef(_ClientPutIntegrationResponseTypeDef):
    """
    - *(dict) --*

      Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

        In the API Gateway console, the built-in Lambda integration is an AWS integration.
        `Creating an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientPutMethodResponseResponseTypeDef = TypedDict(
    "_ClientPutMethodResponseResponseTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientPutMethodResponseResponseTypeDef(_ClientPutMethodResponseResponseTypeDef):
    """
    - *(dict) --*

      Represents a method response of a given HTTP status code returned to the client. The method
      response is passed from the back end through the associated integration response that can be
      transformed using a mapping template.

        Example: A **MethodResponse** instance of an API Request
    """


_ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "_ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef(
    _ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef
):
    pass


_ClientPutMethodResponsemethodIntegrationTypeDef = TypedDict(
    "_ClientPutMethodResponsemethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef
        ],
    },
    total=False,
)


class ClientPutMethodResponsemethodIntegrationTypeDef(
    _ClientPutMethodResponsemethodIntegrationTypeDef
):
    pass


_ClientPutMethodResponsemethodResponsesTypeDef = TypedDict(
    "_ClientPutMethodResponsemethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientPutMethodResponsemethodResponsesTypeDef(_ClientPutMethodResponsemethodResponsesTypeDef):
    pass


_ClientPutMethodResponseTypeDef = TypedDict(
    "_ClientPutMethodResponseTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, ClientPutMethodResponsemethodResponsesTypeDef],
        "methodIntegration": ClientPutMethodResponsemethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)


class ClientPutMethodResponseTypeDef(_ClientPutMethodResponseTypeDef):
    """
    - *(dict) --*

      Represents a client-facing interface by which the client calls the API to access back-end
      resources. A **Method** resource is integrated with an  Integration resource. Both consist of
      a request and one or more responses. The method request takes the client input that is passed
      to the back end through the integration request. A method response returns the output from the
      back end to the client through an integration response. A method request is embodied in a
      **Method** resource, whereas an integration request is embodied in an  Integration resource.
      On the other hand, a method response is represented by a  MethodResponse resource, whereas an
      integration response is represented by an  IntegrationResponse resource.

        Example: Retrive the GET method on a specified resource Request
    """


_ClientPutRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientPutRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientPutRestApiResponseendpointConfigurationTypeDef(
    _ClientPutRestApiResponseendpointConfigurationTypeDef
):
    pass


_ClientPutRestApiResponseTypeDef = TypedDict(
    "_ClientPutRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientPutRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientPutRestApiResponseTypeDef(_ClientPutRestApiResponseTypeDef):
    """
    - *(dict) --*

      Represents a REST API.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientTestInvokeAuthorizerResponseTypeDef = TypedDict(
    "_ClientTestInvokeAuthorizerResponseTypeDef",
    {
        "clientStatus": int,
        "log": str,
        "latency": int,
        "principalId": str,
        "policy": str,
        "authorization": Dict[str, List[str]],
        "claims": Dict[str, str],
    },
    total=False,
)


class ClientTestInvokeAuthorizerResponseTypeDef(_ClientTestInvokeAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      Represents the response of the test invoke request for a custom  Authorizer
      - **clientStatus** *(integer) --*

        The HTTP status code that the client would have received. Value is 0 if the authorizer
        succeeded.
    """


_ClientTestInvokeMethodResponseTypeDef = TypedDict(
    "_ClientTestInvokeMethodResponseTypeDef",
    {
        "status": int,
        "body": str,
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "log": str,
        "latency": int,
    },
    total=False,
)


class ClientTestInvokeMethodResponseTypeDef(_ClientTestInvokeMethodResponseTypeDef):
    """
    - *(dict) --*

      Represents the response of the test invoke request in the HTTP method.

        `Test API using the API Gateway console
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-test-method.html#how-to-test-method-console>`__
    """


_ClientUpdateAccountPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateAccountPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateAccountPatchOperationsTypeDef(_ClientUpdateAccountPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateAccountResponsethrottleSettingsTypeDef = TypedDict(
    "_ClientUpdateAccountResponsethrottleSettingsTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientUpdateAccountResponsethrottleSettingsTypeDef(
    _ClientUpdateAccountResponsethrottleSettingsTypeDef
):
    pass


_ClientUpdateAccountResponseTypeDef = TypedDict(
    "_ClientUpdateAccountResponseTypeDef",
    {
        "cloudwatchRoleArn": str,
        "throttleSettings": ClientUpdateAccountResponsethrottleSettingsTypeDef,
        "features": List[str],
        "apiKeyVersion": str,
    },
    total=False,
)


class ClientUpdateAccountResponseTypeDef(_ClientUpdateAccountResponseTypeDef):
    """
    - *(dict) --*

      Represents an AWS account that is associated with API Gateway.
      To view the account info, call ``GET`` on this resource.

        Error Codes
    """


_ClientUpdateApiKeyPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateApiKeyPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateApiKeyPatchOperationsTypeDef(_ClientUpdateApiKeyPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateApiKeyResponseTypeDef = TypedDict(
    "_ClientUpdateApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateApiKeyResponseTypeDef(_ClientUpdateApiKeyResponseTypeDef):
    """
    - *(dict) --*

      A resource that can be distributed to callers for executing  Method resources that require an
      API key. API keys can be mapped to any  Stage on any  RestApi , which indicates that the
      callers with the API key can make requests to that stage.

        `Use API Keys
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__
    """


_ClientUpdateAuthorizerPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateAuthorizerPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateAuthorizerPatchOperationsTypeDef(_ClientUpdateAuthorizerPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateAuthorizerResponseTypeDef = TypedDict(
    "_ClientUpdateAuthorizerResponseTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)


class ClientUpdateAuthorizerResponseTypeDef(_ClientUpdateAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      Represents an authorization layer for methods. If enabled on a method, API Gateway will
      activate the authorizer when a client calls the method.

        `Use Lambda Function as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html>`__
        `Use Cognito User Pool as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html>`__
    """


_ClientUpdateBasePathMappingPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateBasePathMappingPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateBasePathMappingPatchOperationsTypeDef(
    _ClientUpdateBasePathMappingPatchOperationsTypeDef
):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateBasePathMappingResponseTypeDef = TypedDict(
    "_ClientUpdateBasePathMappingResponseTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)


class ClientUpdateBasePathMappingResponseTypeDef(_ClientUpdateBasePathMappingResponseTypeDef):
    """
    - *(dict) --*

      Represents the base path that callers of the API must provide as part of the URL after the
      domain name.

        A custom domain name plus a ``BasePathMapping`` specification identifies a deployed  RestApi
        in a given stage of the owner  Account .  `Use Custom Domain Names
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_ClientUpdateClientCertificatePatchOperationsTypeDef = TypedDict(
    "_ClientUpdateClientCertificatePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateClientCertificatePatchOperationsTypeDef(
    _ClientUpdateClientCertificatePatchOperationsTypeDef
):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateClientCertificateResponseTypeDef = TypedDict(
    "_ClientUpdateClientCertificateResponseTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateClientCertificateResponseTypeDef(_ClientUpdateClientCertificateResponseTypeDef):
    """
    - *(dict) --*

      Represents a client certificate used to configure client-side SSL authentication while sending
      requests to the integration endpoint.

        Client certificates are used to authenticate an API by the backend server. To authenticate
        an API client (or user), use IAM roles and policies, a custom  Authorizer or an Amazon
        Cognito user pool.  `Use Client-Side Certificate
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__
    """


_ClientUpdateDeploymentPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateDeploymentPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateDeploymentPatchOperationsTypeDef(_ClientUpdateDeploymentPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateDeploymentResponseapiSummaryTypeDef = TypedDict(
    "_ClientUpdateDeploymentResponseapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class ClientUpdateDeploymentResponseapiSummaryTypeDef(
    _ClientUpdateDeploymentResponseapiSummaryTypeDef
):
    pass


_ClientUpdateDeploymentResponseTypeDef = TypedDict(
    "_ClientUpdateDeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, ClientUpdateDeploymentResponseapiSummaryTypeDef]],
    },
    total=False,
)


class ClientUpdateDeploymentResponseTypeDef(_ClientUpdateDeploymentResponseTypeDef):
    """
    - *(dict) --*

      An immutable representation of a  RestApi resource that can be called by users using  Stages .
      A deployment must be associated with a  Stage for it to be callable over the Internet.

        To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi . To view,
        update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE`` on the specified
        deployment resource (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,
        Deployments ,  Stage , `AWS CLI
        <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS
        SDKs <https://aws.amazon.com/tools/>`__
    """


_ClientUpdateDocumentationPartPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateDocumentationPartPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateDocumentationPartPatchOperationsTypeDef(
    _ClientUpdateDocumentationPartPatchOperationsTypeDef
):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateDocumentationPartResponselocationTypeDef = TypedDict(
    "_ClientUpdateDocumentationPartResponselocationTypeDef",
    {
        "type": Literal[
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
        ],
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)


class ClientUpdateDocumentationPartResponselocationTypeDef(
    _ClientUpdateDocumentationPartResponselocationTypeDef
):
    pass


_ClientUpdateDocumentationPartResponseTypeDef = TypedDict(
    "_ClientUpdateDocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": ClientUpdateDocumentationPartResponselocationTypeDef,
        "properties": str,
    },
    total=False,
)


class ClientUpdateDocumentationPartResponseTypeDef(_ClientUpdateDocumentationPartResponseTypeDef):
    """
    - *(dict) --*

      A documentation part for a targeted API entity.
      A documentation part consists of a content map (``properties`` ) and a target (``location`` ).
      The target specifies an API entity to which the documentation content applies. The supported
      API entity types are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` , ``METHOD`` ,
      ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` ,
      ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . Valid ``location`` fields depend
      on the API entity type. All valid fields are not required.
      The content map is a JSON string of API-specific key-value pairs. Although an API can use any
      shape for the content map, only the OpenAPI-compliant documentation fields will be injected
      into the associated API entity definition in the exported OpenAPI definition file.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationParts
    """


_ClientUpdateDocumentationVersionPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateDocumentationVersionPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateDocumentationVersionPatchOperationsTypeDef(
    _ClientUpdateDocumentationVersionPatchOperationsTypeDef
):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateDocumentationVersionResponseTypeDef = TypedDict(
    "_ClientUpdateDocumentationVersionResponseTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class ClientUpdateDocumentationVersionResponseTypeDef(
    _ClientUpdateDocumentationVersionResponseTypeDef
):
    """
    - *(dict) --*

      A snapshot of the documentation of an API.
      Publishing API documentation involves creating a documentation version associated with an API
      stage and exporting the versioned documentation to an external (e.g., OpenAPI) file.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationPart ,  DocumentationVersions
    """


_ClientUpdateDomainNamePatchOperationsTypeDef = TypedDict(
    "_ClientUpdateDomainNamePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateDomainNamePatchOperationsTypeDef(_ClientUpdateDomainNamePatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateDomainNameResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientUpdateDomainNameResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientUpdateDomainNameResponseendpointConfigurationTypeDef(
    _ClientUpdateDomainNameResponseendpointConfigurationTypeDef
):
    pass


_ClientUpdateDomainNameResponseTypeDef = TypedDict(
    "_ClientUpdateDomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientUpdateDomainNameResponseendpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateDomainNameResponseTypeDef(_ClientUpdateDomainNameResponseTypeDef):
    """
    - *(dict) --*

      Represents a custom domain name as a user-friendly host name of an API ( RestApi ).
      When you deploy an API, API Gateway creates a default host name for the API. This default API
      host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com`` format. With the
      default host name, you can access the API's root resource with the URL of
      ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When you set up a
      custom domain name of ``apis.example.com`` for this API, you can then access the same resource
      using the URL of the ``https://apis.examples.com/myApi`` , where ``myApi`` is the base path
      mapping ( BasePathMapping ) of your API under the custom domain name.

        `Set a Custom Host Name for an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_ClientUpdateGatewayResponsePatchOperationsTypeDef = TypedDict(
    "_ClientUpdateGatewayResponsePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateGatewayResponsePatchOperationsTypeDef(
    _ClientUpdateGatewayResponsePatchOperationsTypeDef
):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateGatewayResponseResponseTypeDef = TypedDict(
    "_ClientUpdateGatewayResponseResponseTypeDef",
    {
        "responseType": Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)


class ClientUpdateGatewayResponseResponseTypeDef(_ClientUpdateGatewayResponseResponseTypeDef):
    """
    - *(dict) --*

      A gateway response of a given response type and status code, with optional response parameters
      and mapping templates.

        For more information about valid gateway response types, see `Gateway Response Types
        Supported by API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__
        Example: Get a Gateway Response of a given response type Request
    """


_ClientUpdateIntegrationPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateIntegrationPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateIntegrationPatchOperationsTypeDef(_ClientUpdateIntegrationPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateIntegrationResponsePatchOperationsTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponsePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateIntegrationResponsePatchOperationsTypeDef(
    _ClientUpdateIntegrationResponsePatchOperationsTypeDef
):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientUpdateIntegrationResponseResponseTypeDef(
    _ClientUpdateIntegrationResponseResponseTypeDef
):
    """
    - *(dict) --*

      Represents an integration response. The status code must map to an existing  MethodResponse ,
      and parameters and templates can be used to transform the back-end response.

        `Creating an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientUpdateIntegrationResponseintegrationResponsesTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientUpdateIntegrationResponseintegrationResponsesTypeDef(
    _ClientUpdateIntegrationResponseintegrationResponsesTypeDef
):
    pass


_ClientUpdateIntegrationResponseTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientUpdateIntegrationResponseintegrationResponsesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateIntegrationResponseTypeDef(_ClientUpdateIntegrationResponseTypeDef):
    """
    - *(dict) --*

      Represents an HTTP, HTTP_PROXY, AWS, AWS_PROXY, or Mock integration.

        In the API Gateway console, the built-in Lambda integration is an AWS integration.
        `Creating an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientUpdateMethodPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateMethodPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateMethodPatchOperationsTypeDef(_ClientUpdateMethodPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateMethodResponsePatchOperationsTypeDef = TypedDict(
    "_ClientUpdateMethodResponsePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateMethodResponsePatchOperationsTypeDef(
    _ClientUpdateMethodResponsePatchOperationsTypeDef
):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateMethodResponseResponseTypeDef = TypedDict(
    "_ClientUpdateMethodResponseResponseTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientUpdateMethodResponseResponseTypeDef(_ClientUpdateMethodResponseResponseTypeDef):
    """
    - *(dict) --*

      Represents a method response of a given HTTP status code returned to the client. The method
      response is passed from the back end through the associated integration response that can be
      transformed using a mapping template.

        Example: A **MethodResponse** instance of an API Request
    """


_ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "_ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef(
    _ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef
):
    pass


_ClientUpdateMethodResponsemethodIntegrationTypeDef = TypedDict(
    "_ClientUpdateMethodResponsemethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateMethodResponsemethodIntegrationTypeDef(
    _ClientUpdateMethodResponsemethodIntegrationTypeDef
):
    pass


_ClientUpdateMethodResponsemethodResponsesTypeDef = TypedDict(
    "_ClientUpdateMethodResponsemethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientUpdateMethodResponsemethodResponsesTypeDef(
    _ClientUpdateMethodResponsemethodResponsesTypeDef
):
    pass


_ClientUpdateMethodResponseTypeDef = TypedDict(
    "_ClientUpdateMethodResponseTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, ClientUpdateMethodResponsemethodResponsesTypeDef],
        "methodIntegration": ClientUpdateMethodResponsemethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)


class ClientUpdateMethodResponseTypeDef(_ClientUpdateMethodResponseTypeDef):
    """
    - *(dict) --*

      Represents a client-facing interface by which the client calls the API to access back-end
      resources. A **Method** resource is integrated with an  Integration resource. Both consist of
      a request and one or more responses. The method request takes the client input that is passed
      to the back end through the integration request. A method response returns the output from the
      back end to the client through an integration response. A method request is embodied in a
      **Method** resource, whereas an integration request is embodied in an  Integration resource.
      On the other hand, a method response is represented by a  MethodResponse resource, whereas an
      integration response is represented by an  IntegrationResponse resource.

        Example: Retrive the GET method on a specified resource Request
    """


_ClientUpdateModelPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateModelPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateModelPatchOperationsTypeDef(_ClientUpdateModelPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateModelResponseTypeDef = TypedDict(
    "_ClientUpdateModelResponseTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class ClientUpdateModelResponseTypeDef(_ClientUpdateModelResponseTypeDef):
    """
    - *(dict) --*

      Represents the data structure of a method's request or response payload.
      A request model defines the data structure of the client-supplied request payload. A response
      model defines the data structure of the response payload returned by the back end. Although
      not required, models are useful for mapping payloads between the front end and back end.
      A model is used for generating an API's SDK, validating the input request body, and creating a
      skeletal mapping template.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__
    """


_ClientUpdateRequestValidatorPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateRequestValidatorPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateRequestValidatorPatchOperationsTypeDef(
    _ClientUpdateRequestValidatorPatchOperationsTypeDef
):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateRequestValidatorResponseTypeDef = TypedDict(
    "_ClientUpdateRequestValidatorResponseTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)


class ClientUpdateRequestValidatorResponseTypeDef(_ClientUpdateRequestValidatorResponseTypeDef):
    """
    - *(dict) --*

      A set of validation rules for incoming  Method requests.
      In OpenAPI, a  RequestValidator of an API is defined by the
      `x-amazon-apigateway-request-validators.requestValidator
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.requestValidator.html>`__
      object. It the referenced using the `x-amazon-apigateway-request-validator
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validator>`__
      property.

        `Enable Basic Request Validation in API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__
    """


_ClientUpdateResourcePatchOperationsTypeDef = TypedDict(
    "_ClientUpdateResourcePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateResourcePatchOperationsTypeDef(_ClientUpdateResourcePatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "_ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef(
    _ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef
):
    pass


_ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef = TypedDict(
    "_ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str,
            ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef,
        ],
    },
    total=False,
)


class ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef(
    _ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef
):
    pass


_ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef = TypedDict(
    "_ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef(
    _ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef
):
    pass


_ClientUpdateResourceResponseresourceMethodsTypeDef = TypedDict(
    "_ClientUpdateResourceResponseresourceMethodsTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[
            str, ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef
        ],
        "methodIntegration": ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)


class ClientUpdateResourceResponseresourceMethodsTypeDef(
    _ClientUpdateResourceResponseresourceMethodsTypeDef
):
    pass


_ClientUpdateResourceResponseTypeDef = TypedDict(
    "_ClientUpdateResourceResponseTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, ClientUpdateResourceResponseresourceMethodsTypeDef],
    },
    total=False,
)


class ClientUpdateResourceResponseTypeDef(_ClientUpdateResourceResponseTypeDef):
    """
    - *(dict) --*

      Represents an API resource.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientUpdateRestApiPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateRestApiPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateRestApiPatchOperationsTypeDef(_ClientUpdateRestApiPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "_ClientUpdateRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class ClientUpdateRestApiResponseendpointConfigurationTypeDef(
    _ClientUpdateRestApiResponseendpointConfigurationTypeDef
):
    pass


_ClientUpdateRestApiResponseTypeDef = TypedDict(
    "_ClientUpdateRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientUpdateRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateRestApiResponseTypeDef(_ClientUpdateRestApiResponseTypeDef):
    """
    - *(dict) --*

      Represents a REST API.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_ClientUpdateStagePatchOperationsTypeDef = TypedDict(
    "_ClientUpdateStagePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateStagePatchOperationsTypeDef(_ClientUpdateStagePatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateStageResponseaccessLogSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponseaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)


class ClientUpdateStageResponseaccessLogSettingsTypeDef(
    _ClientUpdateStageResponseaccessLogSettingsTypeDef
):
    pass


_ClientUpdateStageResponsecanarySettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponsecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)


class ClientUpdateStageResponsecanarySettingsTypeDef(
    _ClientUpdateStageResponsecanarySettingsTypeDef
):
    pass


_ClientUpdateStageResponsemethodSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponsemethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": Literal[
            "FAIL_WITH_403", "SUCCEED_WITH_RESPONSE_HEADER", "SUCCEED_WITHOUT_RESPONSE_HEADER"
        ],
    },
    total=False,
)


class ClientUpdateStageResponsemethodSettingsTypeDef(
    _ClientUpdateStageResponsemethodSettingsTypeDef
):
    pass


_ClientUpdateStageResponseTypeDef = TypedDict(
    "_ClientUpdateStageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"],
        "cacheClusterStatus": Literal[
            "CREATE_IN_PROGRESS",
            "AVAILABLE",
            "DELETE_IN_PROGRESS",
            "NOT_AVAILABLE",
            "FLUSH_IN_PROGRESS",
        ],
        "methodSettings": Dict[str, ClientUpdateStageResponsemethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientUpdateStageResponseaccessLogSettingsTypeDef,
        "canarySettings": ClientUpdateStageResponsecanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)


class ClientUpdateStageResponseTypeDef(_ClientUpdateStageResponseTypeDef):
    """
    - *(dict) --*

      Represents a unique identifier for a version of a deployed  RestApi that is callable by users.

        `Deploy an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__
    """


_ClientUpdateUsagePatchOperationsTypeDef = TypedDict(
    "_ClientUpdateUsagePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateUsagePatchOperationsTypeDef(_ClientUpdateUsagePatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateUsagePlanPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateUsagePlanPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateUsagePlanPatchOperationsTypeDef(_ClientUpdateUsagePlanPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef = TypedDict(
    "_ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef(
    _ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef
):
    pass


_ClientUpdateUsagePlanResponseapiStagesTypeDef = TypedDict(
    "_ClientUpdateUsagePlanResponseapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef],
    },
    total=False,
)


class ClientUpdateUsagePlanResponseapiStagesTypeDef(_ClientUpdateUsagePlanResponseapiStagesTypeDef):
    pass


_ClientUpdateUsagePlanResponsequotaTypeDef = TypedDict(
    "_ClientUpdateUsagePlanResponsequotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)


class ClientUpdateUsagePlanResponsequotaTypeDef(_ClientUpdateUsagePlanResponsequotaTypeDef):
    pass


_ClientUpdateUsagePlanResponsethrottleTypeDef = TypedDict(
    "_ClientUpdateUsagePlanResponsethrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class ClientUpdateUsagePlanResponsethrottleTypeDef(_ClientUpdateUsagePlanResponsethrottleTypeDef):
    pass


_ClientUpdateUsagePlanResponseTypeDef = TypedDict(
    "_ClientUpdateUsagePlanResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ClientUpdateUsagePlanResponseapiStagesTypeDef],
        "throttle": ClientUpdateUsagePlanResponsethrottleTypeDef,
        "quota": ClientUpdateUsagePlanResponsequotaTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateUsagePlanResponseTypeDef(_ClientUpdateUsagePlanResponseTypeDef):
    """
    - *(dict) --*

      Represents a usage plan than can specify who can assess associated API stages with specified
      request limits and quotas.
      In a usage plan, you associate an API by specifying the API's Id and a stage name of the
      specified API. You add plan customers by adding API keys to the plan.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
    """


_ClientUpdateUsageResponseTypeDef = TypedDict(
    "_ClientUpdateUsageResponseTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "position": str,
        "items": Dict[str, List[List[int]]],
    },
    total=False,
)


class ClientUpdateUsageResponseTypeDef(_ClientUpdateUsageResponseTypeDef):
    """
    - *(dict) --*

      Represents the usage data of a usage plan.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
        , `Manage Usage in a Usage Plan
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans-with-console.html#api-gateway-usage-plan-manage-usage>`__
    """


_ClientUpdateVpcLinkPatchOperationsTypeDef = TypedDict(
    "_ClientUpdateVpcLinkPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)


class ClientUpdateVpcLinkPatchOperationsTypeDef(_ClientUpdateVpcLinkPatchOperationsTypeDef):
    """
    - *(dict) --*A single patch operation to apply to the specified resource. Please refer to
    http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.

      - **op** *(string) --*

        An update operation to be performed with this PATCH request. The valid value can be ``add``
        , ``remove`` , ``replace`` or ``copy`` . Not all valid operations are supported for a given
        resource. Support of the operations depends on specific operational contexts. Attempts to
        apply an unsupported operation on a resource will return an error message.
    """


_ClientUpdateVpcLinkResponseTypeDef = TypedDict(
    "_ClientUpdateVpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateVpcLinkResponseTypeDef(_ClientUpdateVpcLinkResponseTypeDef):
    """
    - *(dict) --*

      A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual Private Cloud
      (VPC).
      To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API Gateway,
      you, as an API developer, create a  VpcLink resource targeted for one or more network load
      balancers of the VPC and then integrate an API method with a private integration that uses the
      VpcLink . The private integration has an integration type of ``HTTP`` or ``HTTP_PROXY`` and
      has a connection type of ``VPC_LINK`` . The integration uses the ``connectionId`` property to
      identify the  VpcLink used.
      - **id** *(string) --*

        The identifier of the  VpcLink . It is used in an  Integration to reference this  VpcLink .
    """


_GetApiKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_GetApiKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetApiKeysPaginatePaginationConfigTypeDef(_GetApiKeysPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetApiKeysPaginateResponseitemsTypeDef = TypedDict(
    "_GetApiKeysPaginateResponseitemsTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class GetApiKeysPaginateResponseitemsTypeDef(_GetApiKeysPaginateResponseitemsTypeDef):
    pass


_GetApiKeysPaginateResponseTypeDef = TypedDict(
    "_GetApiKeysPaginateResponseTypeDef",
    {
        "warnings": List[str],
        "items": List[GetApiKeysPaginateResponseitemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetApiKeysPaginateResponseTypeDef(_GetApiKeysPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of API keys as represented by an  ApiKeys resource.

        `Use API Keys
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__
    """


_GetAuthorizersPaginatePaginationConfigTypeDef = TypedDict(
    "_GetAuthorizersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetAuthorizersPaginatePaginationConfigTypeDef(_GetAuthorizersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetAuthorizersPaginateResponseitemsTypeDef = TypedDict(
    "_GetAuthorizersPaginateResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)


class GetAuthorizersPaginateResponseitemsTypeDef(_GetAuthorizersPaginateResponseitemsTypeDef):
    pass


_GetAuthorizersPaginateResponseTypeDef = TypedDict(
    "_GetAuthorizersPaginateResponseTypeDef",
    {"items": List[GetAuthorizersPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetAuthorizersPaginateResponseTypeDef(_GetAuthorizersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  Authorizer resources.

        `Use Lambda Function as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html>`__
        `Use Cognito User Pool as Authorizer
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html>`__
    """


_GetBasePathMappingsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetBasePathMappingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetBasePathMappingsPaginatePaginationConfigTypeDef(
    _GetBasePathMappingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetBasePathMappingsPaginateResponseitemsTypeDef = TypedDict(
    "_GetBasePathMappingsPaginateResponseitemsTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)


class GetBasePathMappingsPaginateResponseitemsTypeDef(
    _GetBasePathMappingsPaginateResponseitemsTypeDef
):
    pass


_GetBasePathMappingsPaginateResponseTypeDef = TypedDict(
    "_GetBasePathMappingsPaginateResponseTypeDef",
    {"items": List[GetBasePathMappingsPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetBasePathMappingsPaginateResponseTypeDef(_GetBasePathMappingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  BasePathMapping resources.

        `Use Custom Domain Names
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_GetClientCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetClientCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetClientCertificatesPaginatePaginationConfigTypeDef(
    _GetClientCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetClientCertificatesPaginateResponseitemsTypeDef = TypedDict(
    "_GetClientCertificatesPaginateResponseitemsTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetClientCertificatesPaginateResponseitemsTypeDef(
    _GetClientCertificatesPaginateResponseitemsTypeDef
):
    pass


_GetClientCertificatesPaginateResponseTypeDef = TypedDict(
    "_GetClientCertificatesPaginateResponseTypeDef",
    {"items": List[GetClientCertificatesPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetClientCertificatesPaginateResponseTypeDef(_GetClientCertificatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  ClientCertificate resources.

        `Use Client-Side Certificate
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__
    """


_GetDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDeploymentsPaginatePaginationConfigTypeDef(_GetDeploymentsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDeploymentsPaginateResponseitemsapiSummaryTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseitemsapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)


class GetDeploymentsPaginateResponseitemsapiSummaryTypeDef(
    _GetDeploymentsPaginateResponseitemsapiSummaryTypeDef
):
    pass


_GetDeploymentsPaginateResponseitemsTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseitemsTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, GetDeploymentsPaginateResponseitemsapiSummaryTypeDef]],
    },
    total=False,
)


class GetDeploymentsPaginateResponseitemsTypeDef(_GetDeploymentsPaginateResponseitemsTypeDef):
    pass


_GetDeploymentsPaginateResponseTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseTypeDef",
    {"items": List[GetDeploymentsPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetDeploymentsPaginateResponseTypeDef(_GetDeploymentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection resource that contains zero or more references to your existing
      deployments, and links that guide you on how to interact with your collection. The collection
      offers a paginated view of the contained deployments.

        To create a new deployment of a  RestApi , make a ``POST`` request against this resource. To
        view, update, or delete an existing deployment, make a ``GET`` , ``PATCH`` , or ``DELETE``
        request, respectively, on a specified  Deployment resource.  `Deploying an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__ ,
        `AWS CLI
        <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ , `AWS
        SDKs <https://aws.amazon.com/tools/>`__
    """


_GetDocumentationPartsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDocumentationPartsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDocumentationPartsPaginatePaginationConfigTypeDef(
    _GetDocumentationPartsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDocumentationPartsPaginateResponseitemslocationTypeDef = TypedDict(
    "_GetDocumentationPartsPaginateResponseitemslocationTypeDef",
    {
        "type": Literal[
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
        ],
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)


class GetDocumentationPartsPaginateResponseitemslocationTypeDef(
    _GetDocumentationPartsPaginateResponseitemslocationTypeDef
):
    pass


_GetDocumentationPartsPaginateResponseitemsTypeDef = TypedDict(
    "_GetDocumentationPartsPaginateResponseitemsTypeDef",
    {
        "id": str,
        "location": GetDocumentationPartsPaginateResponseitemslocationTypeDef,
        "properties": str,
    },
    total=False,
)


class GetDocumentationPartsPaginateResponseitemsTypeDef(
    _GetDocumentationPartsPaginateResponseitemsTypeDef
):
    pass


_GetDocumentationPartsPaginateResponseTypeDef = TypedDict(
    "_GetDocumentationPartsPaginateResponseTypeDef",
    {"items": List[GetDocumentationPartsPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetDocumentationPartsPaginateResponseTypeDef(_GetDocumentationPartsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The collection of documentation parts of an API.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationPart
    """


_GetDocumentationVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDocumentationVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDocumentationVersionsPaginatePaginationConfigTypeDef(
    _GetDocumentationVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDocumentationVersionsPaginateResponseitemsTypeDef = TypedDict(
    "_GetDocumentationVersionsPaginateResponseitemsTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)


class GetDocumentationVersionsPaginateResponseitemsTypeDef(
    _GetDocumentationVersionsPaginateResponseitemsTypeDef
):
    pass


_GetDocumentationVersionsPaginateResponseTypeDef = TypedDict(
    "_GetDocumentationVersionsPaginateResponseTypeDef",
    {"items": List[GetDocumentationVersionsPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetDocumentationVersionsPaginateResponseTypeDef(
    _GetDocumentationVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      The collection of documentation snapshots of an API.
      Use the  DocumentationVersions to manage documentation snapshots associated with various API
      stages.

        `Documenting an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
        ,  DocumentationPart ,  DocumentationVersion
    """


_GetDomainNamesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDomainNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDomainNamesPaginatePaginationConfigTypeDef(_GetDomainNamesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDomainNamesPaginateResponseitemsendpointConfigurationTypeDef = TypedDict(
    "_GetDomainNamesPaginateResponseitemsendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class GetDomainNamesPaginateResponseitemsendpointConfigurationTypeDef(
    _GetDomainNamesPaginateResponseitemsendpointConfigurationTypeDef
):
    pass


_GetDomainNamesPaginateResponseitemsTypeDef = TypedDict(
    "_GetDomainNamesPaginateResponseitemsTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": GetDomainNamesPaginateResponseitemsendpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)


class GetDomainNamesPaginateResponseitemsTypeDef(_GetDomainNamesPaginateResponseitemsTypeDef):
    pass


_GetDomainNamesPaginateResponseTypeDef = TypedDict(
    "_GetDomainNamesPaginateResponseTypeDef",
    {"items": List[GetDomainNamesPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetDomainNamesPaginateResponseTypeDef(_GetDomainNamesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  DomainName resources.

        `Use Client-Side Certificate
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__
    """


_GetGatewayResponsesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetGatewayResponsesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetGatewayResponsesPaginatePaginationConfigTypeDef(
    _GetGatewayResponsesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetGatewayResponsesPaginateResponseitemsTypeDef = TypedDict(
    "_GetGatewayResponsesPaginateResponseitemsTypeDef",
    {
        "responseType": Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)


class GetGatewayResponsesPaginateResponseitemsTypeDef(
    _GetGatewayResponsesPaginateResponseitemsTypeDef
):
    pass


_GetGatewayResponsesPaginateResponseTypeDef = TypedDict(
    "_GetGatewayResponsesPaginateResponseTypeDef",
    {"items": List[GetGatewayResponsesPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetGatewayResponsesPaginateResponseTypeDef(_GetGatewayResponsesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The collection of the  GatewayResponse instances of a  RestApi as a ``responseType`` -to-
      GatewayResponse object map of key-value pairs. As such, pagination is not supported for
      querying this collection.

        For more information about valid gateway response types, see `Gateway Response Types
        Supported by API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__
        Example: Get the collection of gateway responses of an API Request
    """


_GetModelsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetModelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetModelsPaginatePaginationConfigTypeDef(_GetModelsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetModelsPaginateResponseitemsTypeDef = TypedDict(
    "_GetModelsPaginateResponseitemsTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class GetModelsPaginateResponseitemsTypeDef(_GetModelsPaginateResponseitemsTypeDef):
    pass


_GetModelsPaginateResponseTypeDef = TypedDict(
    "_GetModelsPaginateResponseTypeDef",
    {"items": List[GetModelsPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetModelsPaginateResponseTypeDef(_GetModelsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  Model resources.

        Method ,  MethodResponse , `Models and Mappings
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__
    """


_GetRequestValidatorsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRequestValidatorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetRequestValidatorsPaginatePaginationConfigTypeDef(
    _GetRequestValidatorsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRequestValidatorsPaginateResponseitemsTypeDef = TypedDict(
    "_GetRequestValidatorsPaginateResponseitemsTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)


class GetRequestValidatorsPaginateResponseitemsTypeDef(
    _GetRequestValidatorsPaginateResponseitemsTypeDef
):
    pass


_GetRequestValidatorsPaginateResponseTypeDef = TypedDict(
    "_GetRequestValidatorsPaginateResponseTypeDef",
    {"items": List[GetRequestValidatorsPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetRequestValidatorsPaginateResponseTypeDef(_GetRequestValidatorsPaginateResponseTypeDef):
    """
    - *(dict) --*

      A collection of  RequestValidator resources of a given  RestApi .
      In OpenAPI, the  RequestValidators of an API is defined by the
      `x-amazon-apigateway-request-validators
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.html>`__
      extension.

        `Enable Basic Request Validation in API Gateway
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__
    """


_GetResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourcesPaginatePaginationConfigTypeDef(_GetResourcesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "_GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)


class GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef(
    _GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef
):
    pass


_GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationTypeDef = TypedDict(
    "_GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str,
            GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef,
        ],
    },
    total=False,
)


class GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationTypeDef(
    _GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationTypeDef
):
    pass


_GetResourcesPaginateResponseitemsresourceMethodsmethodResponsesTypeDef = TypedDict(
    "_GetResourcesPaginateResponseitemsresourceMethodsmethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)


class GetResourcesPaginateResponseitemsresourceMethodsmethodResponsesTypeDef(
    _GetResourcesPaginateResponseitemsresourceMethodsmethodResponsesTypeDef
):
    pass


_GetResourcesPaginateResponseitemsresourceMethodsTypeDef = TypedDict(
    "_GetResourcesPaginateResponseitemsresourceMethodsTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[
            str, GetResourcesPaginateResponseitemsresourceMethodsmethodResponsesTypeDef
        ],
        "methodIntegration": GetResourcesPaginateResponseitemsresourceMethodsmethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)


class GetResourcesPaginateResponseitemsresourceMethodsTypeDef(
    _GetResourcesPaginateResponseitemsresourceMethodsTypeDef
):
    pass


_GetResourcesPaginateResponseitemsTypeDef = TypedDict(
    "_GetResourcesPaginateResponseitemsTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, GetResourcesPaginateResponseitemsresourceMethodsTypeDef],
    },
    total=False,
)


class GetResourcesPaginateResponseitemsTypeDef(_GetResourcesPaginateResponseitemsTypeDef):
    pass


_GetResourcesPaginateResponseTypeDef = TypedDict(
    "_GetResourcesPaginateResponseTypeDef",
    {"items": List[GetResourcesPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetResourcesPaginateResponseTypeDef(_GetResourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of  Resource resources.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_GetRestApisPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRestApisPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetRestApisPaginatePaginationConfigTypeDef(_GetRestApisPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRestApisPaginateResponseitemsendpointConfigurationTypeDef = TypedDict(
    "_GetRestApisPaginateResponseitemsendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)


class GetRestApisPaginateResponseitemsendpointConfigurationTypeDef(
    _GetRestApisPaginateResponseitemsendpointConfigurationTypeDef
):
    pass


_GetRestApisPaginateResponseitemsTypeDef = TypedDict(
    "_GetRestApisPaginateResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": GetRestApisPaginateResponseitemsendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetRestApisPaginateResponseitemsTypeDef(_GetRestApisPaginateResponseitemsTypeDef):
    pass


_GetRestApisPaginateResponseTypeDef = TypedDict(
    "_GetRestApisPaginateResponseTypeDef",
    {"items": List[GetRestApisPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetRestApisPaginateResponseTypeDef(_GetRestApisPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains references to your APIs and links that guide you in how to interact with your
      collection. A collection offers a paginated view of your APIs.

        `Create an API
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__
    """


_GetSdkTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSdkTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetSdkTypesPaginatePaginationConfigTypeDef(_GetSdkTypesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef = TypedDict(
    "_GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef",
    {"name": str, "friendlyName": str, "description": str, "required": bool, "defaultValue": str},
    total=False,
)


class GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef(
    _GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef
):
    pass


_GetSdkTypesPaginateResponseitemsTypeDef = TypedDict(
    "_GetSdkTypesPaginateResponseitemsTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[
            GetSdkTypesPaginateResponseitemsconfigurationPropertiesTypeDef
        ],
    },
    total=False,
)


class GetSdkTypesPaginateResponseitemsTypeDef(_GetSdkTypesPaginateResponseitemsTypeDef):
    """
    - *(dict) --*

      A type of SDK that API Gateway can generate.
      - **id** *(string) --*

        The identifier of an  SdkType instance.
    """


_GetSdkTypesPaginateResponseTypeDef = TypedDict(
    "_GetSdkTypesPaginateResponseTypeDef",
    {"items": List[GetSdkTypesPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetSdkTypesPaginateResponseTypeDef(_GetSdkTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The collection of  SdkType instances.
      - **items** *(list) --*

        The current page of elements from this collection.
        - *(dict) --*

          A type of SDK that API Gateway can generate.
          - **id** *(string) --*

            The identifier of an  SdkType instance.
    """


_GetUsagePaginatePaginationConfigTypeDef = TypedDict(
    "_GetUsagePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetUsagePaginatePaginationConfigTypeDef(_GetUsagePaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetUsagePaginateResponseTypeDef = TypedDict(
    "_GetUsagePaginateResponseTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "items": Dict[str, List[List[int]]],
        "NextToken": str,
    },
    total=False,
)


class GetUsagePaginateResponseTypeDef(_GetUsagePaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the usage data of a usage plan.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
        , `Manage Usage in a Usage Plan
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans-with-console.html#api-gateway-usage-plan-manage-usage>`__
    """


_GetUsagePlanKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_GetUsagePlanKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetUsagePlanKeysPaginatePaginationConfigTypeDef(
    _GetUsagePlanKeysPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetUsagePlanKeysPaginateResponseitemsTypeDef = TypedDict(
    "_GetUsagePlanKeysPaginateResponseitemsTypeDef",
    {"id": str, "type": str, "value": str, "name": str},
    total=False,
)


class GetUsagePlanKeysPaginateResponseitemsTypeDef(_GetUsagePlanKeysPaginateResponseitemsTypeDef):
    pass


_GetUsagePlanKeysPaginateResponseTypeDef = TypedDict(
    "_GetUsagePlanKeysPaginateResponseTypeDef",
    {"items": List[GetUsagePlanKeysPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetUsagePlanKeysPaginateResponseTypeDef(_GetUsagePlanKeysPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the collection of usage plan keys added to usage plans for the associated API keys
      and, possibly, other types of keys.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
    """


_GetUsagePlansPaginatePaginationConfigTypeDef = TypedDict(
    "_GetUsagePlansPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetUsagePlansPaginatePaginationConfigTypeDef(_GetUsagePlansPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetUsagePlansPaginateResponseitemsapiStagesthrottleTypeDef = TypedDict(
    "_GetUsagePlansPaginateResponseitemsapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class GetUsagePlansPaginateResponseitemsapiStagesthrottleTypeDef(
    _GetUsagePlansPaginateResponseitemsapiStagesthrottleTypeDef
):
    pass


_GetUsagePlansPaginateResponseitemsapiStagesTypeDef = TypedDict(
    "_GetUsagePlansPaginateResponseitemsapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, GetUsagePlansPaginateResponseitemsapiStagesthrottleTypeDef],
    },
    total=False,
)


class GetUsagePlansPaginateResponseitemsapiStagesTypeDef(
    _GetUsagePlansPaginateResponseitemsapiStagesTypeDef
):
    pass


_GetUsagePlansPaginateResponseitemsquotaTypeDef = TypedDict(
    "_GetUsagePlansPaginateResponseitemsquotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)


class GetUsagePlansPaginateResponseitemsquotaTypeDef(
    _GetUsagePlansPaginateResponseitemsquotaTypeDef
):
    pass


_GetUsagePlansPaginateResponseitemsthrottleTypeDef = TypedDict(
    "_GetUsagePlansPaginateResponseitemsthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)


class GetUsagePlansPaginateResponseitemsthrottleTypeDef(
    _GetUsagePlansPaginateResponseitemsthrottleTypeDef
):
    pass


_GetUsagePlansPaginateResponseitemsTypeDef = TypedDict(
    "_GetUsagePlansPaginateResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[GetUsagePlansPaginateResponseitemsapiStagesTypeDef],
        "throttle": GetUsagePlansPaginateResponseitemsthrottleTypeDef,
        "quota": GetUsagePlansPaginateResponseitemsquotaTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetUsagePlansPaginateResponseitemsTypeDef(_GetUsagePlansPaginateResponseitemsTypeDef):
    pass


_GetUsagePlansPaginateResponseTypeDef = TypedDict(
    "_GetUsagePlansPaginateResponseTypeDef",
    {"items": List[GetUsagePlansPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetUsagePlansPaginateResponseTypeDef(_GetUsagePlansPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents a collection of usage plans for an AWS account.

        `Create and Use Usage Plans
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
    """


_GetVpcLinksPaginatePaginationConfigTypeDef = TypedDict(
    "_GetVpcLinksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetVpcLinksPaginatePaginationConfigTypeDef(_GetVpcLinksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetVpcLinksPaginateResponseitemsTypeDef = TypedDict(
    "_GetVpcLinksPaginateResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetVpcLinksPaginateResponseitemsTypeDef(_GetVpcLinksPaginateResponseitemsTypeDef):
    pass


_GetVpcLinksPaginateResponseTypeDef = TypedDict(
    "_GetVpcLinksPaginateResponseTypeDef",
    {"items": List[GetVpcLinksPaginateResponseitemsTypeDef], "NextToken": str},
    total=False,
)


class GetVpcLinksPaginateResponseTypeDef(_GetVpcLinksPaginateResponseTypeDef):
    """
    - *(dict) --*

      The collection of VPC links under the caller's account in a region.

        `Getting Started with Private Integrations
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-private-integration.html>`__
        , `Set up Private Integrations
        <https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html>`__
    """
