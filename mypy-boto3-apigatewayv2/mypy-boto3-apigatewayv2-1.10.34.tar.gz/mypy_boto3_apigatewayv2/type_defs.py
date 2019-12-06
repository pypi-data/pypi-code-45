"Main interface for apigatewayv2 service type defs"
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


ClientCreateApiCorsConfigurationTypeDef = TypedDict(
    "ClientCreateApiCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientCreateApiMappingResponseTypeDef = TypedDict(
    "ClientCreateApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)

ClientCreateApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientCreateApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientCreateApiResponseTypeDef = TypedDict(
    "ClientCreateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientCreateApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientCreateAuthorizerJwtConfigurationTypeDef = TypedDict(
    "ClientCreateAuthorizerJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientCreateAuthorizerResponseJwtConfigurationTypeDef = TypedDict(
    "ClientCreateAuthorizerResponseJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientCreateAuthorizerResponseTypeDef = TypedDict(
    "ClientCreateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": ClientCreateAuthorizerResponseJwtConfigurationTypeDef,
        "Name": str,
    },
    total=False,
)

ClientCreateDeploymentResponseTypeDef = TypedDict(
    "ClientCreateDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

ClientCreateDomainNameDomainNameConfigurationsTypeDef = TypedDict(
    "ClientCreateDomainNameDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientCreateDomainNameResponseTypeDef = TypedDict(
    "ClientCreateDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientCreateIntegrationResponseResponseTypeDef = TypedDict(
    "ClientCreateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

ClientCreateIntegrationResponseTypeDef = TypedDict(
    "ClientCreateIntegrationResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

ClientCreateModelResponseTypeDef = TypedDict(
    "ClientCreateModelResponseTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)

ClientCreateRouteRequestParametersTypeDef = TypedDict(
    "ClientCreateRouteRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientCreateRouteResponseResponseParametersTypeDef = TypedDict(
    "ClientCreateRouteResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientCreateRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "ClientCreateRouteResponseResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientCreateRouteResponseResponseTypeDef = TypedDict(
    "ClientCreateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ClientCreateRouteResponseResponseResponseParametersTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)

ClientCreateRouteResponseRequestParametersTypeDef = TypedDict(
    "ClientCreateRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientCreateRouteResponseTypeDef = TypedDict(
    "ClientCreateRouteResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ClientCreateRouteResponseRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

ClientCreateStageAccessLogSettingsTypeDef = TypedDict(
    "ClientCreateStageAccessLogSettingsTypeDef", {"DestinationArn": str, "Format": str}, total=False
)

ClientCreateStageDefaultRouteSettingsTypeDef = TypedDict(
    "ClientCreateStageDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientCreateStageResponseAccessLogSettingsTypeDef = TypedDict(
    "ClientCreateStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)

ClientCreateStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "ClientCreateStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientCreateStageResponseRouteSettingsTypeDef = TypedDict(
    "ClientCreateStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientCreateStageResponseTypeDef = TypedDict(
    "ClientCreateStageResponseTypeDef",
    {
        "AccessLogSettings": ClientCreateStageResponseAccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientCreateStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientCreateStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientCreateStageRouteSettingsTypeDef = TypedDict(
    "ClientCreateStageRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetApiMappingResponseTypeDef = TypedDict(
    "ClientGetApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)

ClientGetApiMappingsResponseItemsTypeDef = TypedDict(
    "ClientGetApiMappingsResponseItemsTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)

ClientGetApiMappingsResponseTypeDef = TypedDict(
    "ClientGetApiMappingsResponseTypeDef",
    {"Items": List[ClientGetApiMappingsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientGetApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientGetApiResponseTypeDef = TypedDict(
    "ClientGetApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientGetApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientGetApisResponseItemsCorsConfigurationTypeDef = TypedDict(
    "ClientGetApisResponseItemsCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientGetApisResponseItemsTypeDef = TypedDict(
    "ClientGetApisResponseItemsTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientGetApisResponseItemsCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientGetApisResponseTypeDef = TypedDict(
    "ClientGetApisResponseTypeDef",
    {"Items": List[ClientGetApisResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetAuthorizerResponseJwtConfigurationTypeDef = TypedDict(
    "ClientGetAuthorizerResponseJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientGetAuthorizerResponseTypeDef = TypedDict(
    "ClientGetAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": ClientGetAuthorizerResponseJwtConfigurationTypeDef,
        "Name": str,
    },
    total=False,
)

ClientGetAuthorizersResponseItemsJwtConfigurationTypeDef = TypedDict(
    "ClientGetAuthorizersResponseItemsJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientGetAuthorizersResponseItemsTypeDef = TypedDict(
    "ClientGetAuthorizersResponseItemsTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": ClientGetAuthorizersResponseItemsJwtConfigurationTypeDef,
        "Name": str,
    },
    total=False,
)

ClientGetAuthorizersResponseTypeDef = TypedDict(
    "ClientGetAuthorizersResponseTypeDef",
    {"Items": List[ClientGetAuthorizersResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetDeploymentResponseTypeDef = TypedDict(
    "ClientGetDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

ClientGetDeploymentsResponseItemsTypeDef = TypedDict(
    "ClientGetDeploymentsResponseItemsTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

ClientGetDeploymentsResponseTypeDef = TypedDict(
    "ClientGetDeploymentsResponseTypeDef",
    {"Items": List[ClientGetDeploymentsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "ClientGetDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientGetDomainNameResponseTypeDef = TypedDict(
    "ClientGetDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientGetDomainNameResponseDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef = TypedDict(
    "ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientGetDomainNamesResponseItemsTypeDef = TypedDict(
    "ClientGetDomainNamesResponseItemsTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetDomainNamesResponseTypeDef = TypedDict(
    "ClientGetDomainNamesResponseTypeDef",
    {"Items": List[ClientGetDomainNamesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetIntegrationResponseResponseTypeDef = TypedDict(
    "ClientGetIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

ClientGetIntegrationResponseTypeDef = TypedDict(
    "ClientGetIntegrationResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

ClientGetIntegrationResponsesResponseItemsTypeDef = TypedDict(
    "ClientGetIntegrationResponsesResponseItemsTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

ClientGetIntegrationResponsesResponseTypeDef = TypedDict(
    "ClientGetIntegrationResponsesResponseTypeDef",
    {"Items": List[ClientGetIntegrationResponsesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetIntegrationsResponseItemsTypeDef = TypedDict(
    "ClientGetIntegrationsResponseItemsTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

ClientGetIntegrationsResponseTypeDef = TypedDict(
    "ClientGetIntegrationsResponseTypeDef",
    {"Items": List[ClientGetIntegrationsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetModelResponseTypeDef = TypedDict(
    "ClientGetModelResponseTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)

ClientGetModelTemplateResponseTypeDef = TypedDict(
    "ClientGetModelTemplateResponseTypeDef", {"Value": str}, total=False
)

ClientGetModelsResponseItemsTypeDef = TypedDict(
    "ClientGetModelsResponseItemsTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)

ClientGetModelsResponseTypeDef = TypedDict(
    "ClientGetModelsResponseTypeDef",
    {"Items": List[ClientGetModelsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "ClientGetRouteResponseResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientGetRouteResponseResponseTypeDef = TypedDict(
    "ClientGetRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ClientGetRouteResponseResponseResponseParametersTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)

ClientGetRouteResponseRequestParametersTypeDef = TypedDict(
    "ClientGetRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientGetRouteResponseTypeDef = TypedDict(
    "ClientGetRouteResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ClientGetRouteResponseRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

ClientGetRouteResponsesResponseItemsResponseParametersTypeDef = TypedDict(
    "ClientGetRouteResponsesResponseItemsResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientGetRouteResponsesResponseItemsTypeDef = TypedDict(
    "ClientGetRouteResponsesResponseItemsTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[
            str, ClientGetRouteResponsesResponseItemsResponseParametersTypeDef
        ],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)

ClientGetRouteResponsesResponseTypeDef = TypedDict(
    "ClientGetRouteResponsesResponseTypeDef",
    {"Items": List[ClientGetRouteResponsesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetRoutesResponseItemsRequestParametersTypeDef = TypedDict(
    "ClientGetRoutesResponseItemsRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientGetRoutesResponseItemsTypeDef = TypedDict(
    "ClientGetRoutesResponseItemsTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ClientGetRoutesResponseItemsRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

ClientGetRoutesResponseTypeDef = TypedDict(
    "ClientGetRoutesResponseTypeDef",
    {"Items": List[ClientGetRoutesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetStageResponseAccessLogSettingsTypeDef = TypedDict(
    "ClientGetStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)

ClientGetStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "ClientGetStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetStageResponseRouteSettingsTypeDef = TypedDict(
    "ClientGetStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetStageResponseTypeDef = TypedDict(
    "ClientGetStageResponseTypeDef",
    {
        "AccessLogSettings": ClientGetStageResponseAccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientGetStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientGetStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetStagesResponseItemsAccessLogSettingsTypeDef = TypedDict(
    "ClientGetStagesResponseItemsAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)

ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef = TypedDict(
    "ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetStagesResponseItemsRouteSettingsTypeDef = TypedDict(
    "ClientGetStagesResponseItemsRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetStagesResponseItemsTypeDef = TypedDict(
    "ClientGetStagesResponseItemsTypeDef",
    {
        "AccessLogSettings": ClientGetStagesResponseItemsAccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientGetStagesResponseItemsRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetStagesResponseTypeDef = TypedDict(
    "ClientGetStagesResponseTypeDef",
    {"Items": List[ClientGetStagesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetTagsResponseTypeDef = TypedDict(
    "ClientGetTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientImportApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientImportApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientImportApiResponseTypeDef = TypedDict(
    "ClientImportApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientImportApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientReimportApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientReimportApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientReimportApiResponseTypeDef = TypedDict(
    "ClientReimportApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientReimportApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientUpdateApiCorsConfigurationTypeDef = TypedDict(
    "ClientUpdateApiCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientUpdateApiMappingResponseTypeDef = TypedDict(
    "ClientUpdateApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)

ClientUpdateApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientUpdateApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientUpdateApiResponseTypeDef = TypedDict(
    "ClientUpdateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientUpdateApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientUpdateAuthorizerJwtConfigurationTypeDef = TypedDict(
    "ClientUpdateAuthorizerJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientUpdateAuthorizerResponseJwtConfigurationTypeDef = TypedDict(
    "ClientUpdateAuthorizerResponseJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientUpdateAuthorizerResponseTypeDef = TypedDict(
    "ClientUpdateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": ClientUpdateAuthorizerResponseJwtConfigurationTypeDef,
        "Name": str,
    },
    total=False,
)

ClientUpdateDeploymentResponseTypeDef = TypedDict(
    "ClientUpdateDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

ClientUpdateDomainNameDomainNameConfigurationsTypeDef = TypedDict(
    "ClientUpdateDomainNameDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientUpdateDomainNameResponseTypeDef = TypedDict(
    "ClientUpdateDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateIntegrationResponseResponseTypeDef = TypedDict(
    "ClientUpdateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

ClientUpdateIntegrationResponseTypeDef = TypedDict(
    "ClientUpdateIntegrationResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

ClientUpdateModelResponseTypeDef = TypedDict(
    "ClientUpdateModelResponseTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)

ClientUpdateRouteRequestParametersTypeDef = TypedDict(
    "ClientUpdateRouteRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientUpdateRouteResponseResponseParametersTypeDef = TypedDict(
    "ClientUpdateRouteResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientUpdateRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "ClientUpdateRouteResponseResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientUpdateRouteResponseResponseTypeDef = TypedDict(
    "ClientUpdateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ClientUpdateRouteResponseResponseResponseParametersTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)

ClientUpdateRouteResponseRequestParametersTypeDef = TypedDict(
    "ClientUpdateRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientUpdateRouteResponseTypeDef = TypedDict(
    "ClientUpdateRouteResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ClientUpdateRouteResponseRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

ClientUpdateStageAccessLogSettingsTypeDef = TypedDict(
    "ClientUpdateStageAccessLogSettingsTypeDef", {"DestinationArn": str, "Format": str}, total=False
)

ClientUpdateStageDefaultRouteSettingsTypeDef = TypedDict(
    "ClientUpdateStageDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientUpdateStageResponseAccessLogSettingsTypeDef = TypedDict(
    "ClientUpdateStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)

ClientUpdateStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "ClientUpdateStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientUpdateStageResponseRouteSettingsTypeDef = TypedDict(
    "ClientUpdateStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientUpdateStageResponseTypeDef = TypedDict(
    "ClientUpdateStageResponseTypeDef",
    {
        "AccessLogSettings": ClientUpdateStageResponseAccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientUpdateStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientUpdateStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateStageRouteSettingsTypeDef = TypedDict(
    "ClientUpdateStageRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

GetApisPaginatePaginationConfigTypeDef = TypedDict(
    "GetApisPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetApisPaginateResponseItemsCorsConfigurationTypeDef = TypedDict(
    "GetApisPaginateResponseItemsCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

GetApisPaginateResponseItemsTypeDef = TypedDict(
    "GetApisPaginateResponseItemsTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": GetApisPaginateResponseItemsCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

GetApisPaginateResponseTypeDef = TypedDict(
    "GetApisPaginateResponseTypeDef",
    {"Items": List[GetApisPaginateResponseItemsTypeDef]},
    total=False,
)

GetAuthorizersPaginatePaginationConfigTypeDef = TypedDict(
    "GetAuthorizersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetAuthorizersPaginateResponseItemsJwtConfigurationTypeDef = TypedDict(
    "GetAuthorizersPaginateResponseItemsJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

GetAuthorizersPaginateResponseItemsTypeDef = TypedDict(
    "GetAuthorizersPaginateResponseItemsTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": GetAuthorizersPaginateResponseItemsJwtConfigurationTypeDef,
        "Name": str,
    },
    total=False,
)

GetAuthorizersPaginateResponseTypeDef = TypedDict(
    "GetAuthorizersPaginateResponseTypeDef",
    {"Items": List[GetAuthorizersPaginateResponseItemsTypeDef]},
    total=False,
)

GetDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "GetDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetDeploymentsPaginateResponseItemsTypeDef = TypedDict(
    "GetDeploymentsPaginateResponseItemsTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

GetDeploymentsPaginateResponseTypeDef = TypedDict(
    "GetDeploymentsPaginateResponseTypeDef",
    {"Items": List[GetDeploymentsPaginateResponseItemsTypeDef]},
    total=False,
)

GetDomainNamesPaginatePaginationConfigTypeDef = TypedDict(
    "GetDomainNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef = TypedDict(
    "GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

GetDomainNamesPaginateResponseItemsTypeDef = TypedDict(
    "GetDomainNamesPaginateResponseItemsTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

GetDomainNamesPaginateResponseTypeDef = TypedDict(
    "GetDomainNamesPaginateResponseTypeDef",
    {"Items": List[GetDomainNamesPaginateResponseItemsTypeDef]},
    total=False,
)

GetIntegrationResponsesPaginatePaginationConfigTypeDef = TypedDict(
    "GetIntegrationResponsesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetIntegrationResponsesPaginateResponseItemsTypeDef = TypedDict(
    "GetIntegrationResponsesPaginateResponseItemsTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

GetIntegrationResponsesPaginateResponseTypeDef = TypedDict(
    "GetIntegrationResponsesPaginateResponseTypeDef",
    {"Items": List[GetIntegrationResponsesPaginateResponseItemsTypeDef]},
    total=False,
)

GetIntegrationsPaginatePaginationConfigTypeDef = TypedDict(
    "GetIntegrationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetIntegrationsPaginateResponseItemsTypeDef = TypedDict(
    "GetIntegrationsPaginateResponseItemsTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

GetIntegrationsPaginateResponseTypeDef = TypedDict(
    "GetIntegrationsPaginateResponseTypeDef",
    {"Items": List[GetIntegrationsPaginateResponseItemsTypeDef]},
    total=False,
)

GetModelsPaginatePaginationConfigTypeDef = TypedDict(
    "GetModelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetModelsPaginateResponseItemsTypeDef = TypedDict(
    "GetModelsPaginateResponseItemsTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)

GetModelsPaginateResponseTypeDef = TypedDict(
    "GetModelsPaginateResponseTypeDef",
    {"Items": List[GetModelsPaginateResponseItemsTypeDef]},
    total=False,
)

GetRouteResponsesPaginatePaginationConfigTypeDef = TypedDict(
    "GetRouteResponsesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef = TypedDict(
    "GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)

GetRouteResponsesPaginateResponseItemsTypeDef = TypedDict(
    "GetRouteResponsesPaginateResponseItemsTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[
            str, GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef
        ],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)

GetRouteResponsesPaginateResponseTypeDef = TypedDict(
    "GetRouteResponsesPaginateResponseTypeDef",
    {"Items": List[GetRouteResponsesPaginateResponseItemsTypeDef]},
    total=False,
)

GetRoutesPaginatePaginationConfigTypeDef = TypedDict(
    "GetRoutesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetRoutesPaginateResponseItemsRequestParametersTypeDef = TypedDict(
    "GetRoutesPaginateResponseItemsRequestParametersTypeDef", {"Required": bool}, total=False
)

GetRoutesPaginateResponseItemsTypeDef = TypedDict(
    "GetRoutesPaginateResponseItemsTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, GetRoutesPaginateResponseItemsRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

GetRoutesPaginateResponseTypeDef = TypedDict(
    "GetRoutesPaginateResponseTypeDef",
    {"Items": List[GetRoutesPaginateResponseItemsTypeDef]},
    total=False,
)

GetStagesPaginatePaginationConfigTypeDef = TypedDict(
    "GetStagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetStagesPaginateResponseItemsAccessLogSettingsTypeDef = TypedDict(
    "GetStagesPaginateResponseItemsAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)

GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef = TypedDict(
    "GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

GetStagesPaginateResponseItemsRouteSettingsTypeDef = TypedDict(
    "GetStagesPaginateResponseItemsRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

GetStagesPaginateResponseItemsTypeDef = TypedDict(
    "GetStagesPaginateResponseItemsTypeDef",
    {
        "AccessLogSettings": GetStagesPaginateResponseItemsAccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, GetStagesPaginateResponseItemsRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

GetStagesPaginateResponseTypeDef = TypedDict(
    "GetStagesPaginateResponseTypeDef",
    {"Items": List[GetStagesPaginateResponseItemsTypeDef]},
    total=False,
)
