"Main interface for apigatewayv2 service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateApiMappingResponseTypeDef",
    "ClientCreateApiResponseTypeDef",
    "ClientCreateAuthorizerResponseTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDomainNameDomainNameConfigurationsTypeDef",
    "ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef",
    "ClientCreateDomainNameResponseTypeDef",
    "ClientCreateIntegrationResponseResponseTypeDef",
    "ClientCreateIntegrationResponseTypeDef",
    "ClientCreateModelResponseTypeDef",
    "ClientCreateRouteRequestParametersTypeDef",
    "ClientCreateRouteResponseResponseParametersTypeDef",
    "ClientCreateRouteResponseResponseResponseParametersTypeDef",
    "ClientCreateRouteResponseResponseTypeDef",
    "ClientCreateRouteResponseRequestParametersTypeDef",
    "ClientCreateRouteResponseTypeDef",
    "ClientCreateStageAccessLogSettingsTypeDef",
    "ClientCreateStageDefaultRouteSettingsTypeDef",
    "ClientCreateStageResponseAccessLogSettingsTypeDef",
    "ClientCreateStageResponseDefaultRouteSettingsTypeDef",
    "ClientCreateStageResponseRouteSettingsTypeDef",
    "ClientCreateStageResponseTypeDef",
    "ClientCreateStageRouteSettingsTypeDef",
    "ClientGetApiMappingResponseTypeDef",
    "ClientGetApiMappingsResponseItemsTypeDef",
    "ClientGetApiMappingsResponseTypeDef",
    "ClientGetApiResponseTypeDef",
    "ClientGetApisResponseItemsTypeDef",
    "ClientGetApisResponseTypeDef",
    "ClientGetAuthorizerResponseTypeDef",
    "ClientGetAuthorizersResponseItemsTypeDef",
    "ClientGetAuthorizersResponseTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentsResponseItemsTypeDef",
    "ClientGetDeploymentsResponseTypeDef",
    "ClientGetDomainNameResponseDomainNameConfigurationsTypeDef",
    "ClientGetDomainNameResponseTypeDef",
    "ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef",
    "ClientGetDomainNamesResponseItemsTypeDef",
    "ClientGetDomainNamesResponseTypeDef",
    "ClientGetIntegrationResponseResponseTypeDef",
    "ClientGetIntegrationResponseTypeDef",
    "ClientGetIntegrationResponsesResponseItemsTypeDef",
    "ClientGetIntegrationResponsesResponseTypeDef",
    "ClientGetIntegrationsResponseItemsTypeDef",
    "ClientGetIntegrationsResponseTypeDef",
    "ClientGetModelResponseTypeDef",
    "ClientGetModelTemplateResponseTypeDef",
    "ClientGetModelsResponseItemsTypeDef",
    "ClientGetModelsResponseTypeDef",
    "ClientGetRouteResponseResponseResponseParametersTypeDef",
    "ClientGetRouteResponseResponseTypeDef",
    "ClientGetRouteResponseRequestParametersTypeDef",
    "ClientGetRouteResponseTypeDef",
    "ClientGetRouteResponsesResponseItemsResponseParametersTypeDef",
    "ClientGetRouteResponsesResponseItemsTypeDef",
    "ClientGetRouteResponsesResponseTypeDef",
    "ClientGetRoutesResponseItemsRequestParametersTypeDef",
    "ClientGetRoutesResponseItemsTypeDef",
    "ClientGetRoutesResponseTypeDef",
    "ClientGetStageResponseAccessLogSettingsTypeDef",
    "ClientGetStageResponseDefaultRouteSettingsTypeDef",
    "ClientGetStageResponseRouteSettingsTypeDef",
    "ClientGetStageResponseTypeDef",
    "ClientGetStagesResponseItemsAccessLogSettingsTypeDef",
    "ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef",
    "ClientGetStagesResponseItemsRouteSettingsTypeDef",
    "ClientGetStagesResponseItemsTypeDef",
    "ClientGetStagesResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientUpdateApiMappingResponseTypeDef",
    "ClientUpdateApiResponseTypeDef",
    "ClientUpdateAuthorizerResponseTypeDef",
    "ClientUpdateDeploymentResponseTypeDef",
    "ClientUpdateDomainNameDomainNameConfigurationsTypeDef",
    "ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef",
    "ClientUpdateDomainNameResponseTypeDef",
    "ClientUpdateIntegrationResponseResponseTypeDef",
    "ClientUpdateIntegrationResponseTypeDef",
    "ClientUpdateModelResponseTypeDef",
    "ClientUpdateRouteRequestParametersTypeDef",
    "ClientUpdateRouteResponseResponseParametersTypeDef",
    "ClientUpdateRouteResponseResponseResponseParametersTypeDef",
    "ClientUpdateRouteResponseResponseTypeDef",
    "ClientUpdateRouteResponseRequestParametersTypeDef",
    "ClientUpdateRouteResponseTypeDef",
    "ClientUpdateStageAccessLogSettingsTypeDef",
    "ClientUpdateStageDefaultRouteSettingsTypeDef",
    "ClientUpdateStageResponseAccessLogSettingsTypeDef",
    "ClientUpdateStageResponseDefaultRouteSettingsTypeDef",
    "ClientUpdateStageResponseRouteSettingsTypeDef",
    "ClientUpdateStageResponseTypeDef",
    "ClientUpdateStageRouteSettingsTypeDef",
    "GetApisPaginatePaginationConfigTypeDef",
    "GetApisPaginateResponseItemsTypeDef",
    "GetApisPaginateResponseTypeDef",
    "GetAuthorizersPaginatePaginationConfigTypeDef",
    "GetAuthorizersPaginateResponseItemsTypeDef",
    "GetAuthorizersPaginateResponseTypeDef",
    "GetDeploymentsPaginatePaginationConfigTypeDef",
    "GetDeploymentsPaginateResponseItemsTypeDef",
    "GetDeploymentsPaginateResponseTypeDef",
    "GetDomainNamesPaginatePaginationConfigTypeDef",
    "GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef",
    "GetDomainNamesPaginateResponseItemsTypeDef",
    "GetDomainNamesPaginateResponseTypeDef",
    "GetIntegrationResponsesPaginatePaginationConfigTypeDef",
    "GetIntegrationResponsesPaginateResponseItemsTypeDef",
    "GetIntegrationResponsesPaginateResponseTypeDef",
    "GetIntegrationsPaginatePaginationConfigTypeDef",
    "GetIntegrationsPaginateResponseItemsTypeDef",
    "GetIntegrationsPaginateResponseTypeDef",
    "GetModelsPaginatePaginationConfigTypeDef",
    "GetModelsPaginateResponseItemsTypeDef",
    "GetModelsPaginateResponseTypeDef",
    "GetRouteResponsesPaginatePaginationConfigTypeDef",
    "GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef",
    "GetRouteResponsesPaginateResponseItemsTypeDef",
    "GetRouteResponsesPaginateResponseTypeDef",
    "GetRoutesPaginatePaginationConfigTypeDef",
    "GetRoutesPaginateResponseItemsRequestParametersTypeDef",
    "GetRoutesPaginateResponseItemsTypeDef",
    "GetRoutesPaginateResponseTypeDef",
    "GetStagesPaginatePaginationConfigTypeDef",
    "GetStagesPaginateResponseItemsAccessLogSettingsTypeDef",
    "GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef",
    "GetStagesPaginateResponseItemsRouteSettingsTypeDef",
    "GetStagesPaginateResponseItemsTypeDef",
    "GetStagesPaginateResponseTypeDef",
)


_ClientCreateApiMappingResponseTypeDef = TypedDict(
    "_ClientCreateApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)


class ClientCreateApiMappingResponseTypeDef(_ClientCreateApiMappingResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **ApiId** *(string) --*

        The API identifier.
    """


_ClientCreateApiResponseTypeDef = TypedDict(
    "_ClientCreateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateApiResponseTypeDef(_ClientCreateApiResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **ApiEndpoint** *(string) --*

        The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name
        is typically appended to this URI to form a complete path to a deployed API stage.
    """


_ClientCreateAuthorizerResponseTypeDef = TypedDict(
    "_ClientCreateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class ClientCreateAuthorizerResponseTypeDef(_ClientCreateAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **AuthorizerCredentialsArn** *(string) --*

        Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.
        To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN).
        To use resource-based permissions on the Lambda function, specify null.
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **CreatedDate** *(datetime) --*

        The date and time when the Deployment resource was created.
    """


_ClientCreateDomainNameDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientCreateDomainNameDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientCreateDomainNameDomainNameConfigurationsTypeDef(
    _ClientCreateDomainNameDomainNameConfigurationsTypeDef
):
    """
    - *(dict) --*

      The domain name configuration.
      - **ApiGatewayDomainName** *(string) --*

        A domain name for the WebSocket API.
    """


_ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef(
    _ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef
):
    pass


_ClientCreateDomainNameResponseTypeDef = TypedDict(
    "_ClientCreateDomainNameResponseTypeDef",
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


class ClientCreateDomainNameResponseTypeDef(_ClientCreateDomainNameResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **ApiMappingSelectionExpression** *(string) --*

        The API mapping selection expression.
    """


_ClientCreateIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientCreateIntegrationResponseResponseTypeDef",
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


class ClientCreateIntegrationResponseResponseTypeDef(
    _ClientCreateIntegrationResponseResponseTypeDef
):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **ContentHandlingStrategy** *(string) --*

        Specifies how to handle response payload content type conversions. Supported values are
        CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
        CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
        corresponding binary blob.
        CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
        If this property is not defined, the response payload will be passed through from the
        integration response to the route response or method response without modification.
    """


_ClientCreateIntegrationResponseTypeDef = TypedDict(
    "_ClientCreateIntegrationResponseTypeDef",
    {
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
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class ClientCreateIntegrationResponseTypeDef(_ClientCreateIntegrationResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **ConnectionId** *(string) --*

        The connection ID.
    """


_ClientCreateModelResponseTypeDef = TypedDict(
    "_ClientCreateModelResponseTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)


class ClientCreateModelResponseTypeDef(_ClientCreateModelResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **ContentType** *(string) --*

        The content-type for the model, for example, "application/json".
    """


_ClientCreateRouteRequestParametersTypeDef = TypedDict(
    "_ClientCreateRouteRequestParametersTypeDef", {"Required": bool}, total=False
)


class ClientCreateRouteRequestParametersTypeDef(_ClientCreateRouteRequestParametersTypeDef):
    pass


_ClientCreateRouteResponseResponseParametersTypeDef = TypedDict(
    "_ClientCreateRouteResponseResponseParametersTypeDef", {"Required": bool}, total=False
)


class ClientCreateRouteResponseResponseParametersTypeDef(
    _ClientCreateRouteResponseResponseParametersTypeDef
):
    pass


_ClientCreateRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "_ClientCreateRouteResponseResponseResponseParametersTypeDef", {"Required": bool}, total=False
)


class ClientCreateRouteResponseResponseResponseParametersTypeDef(
    _ClientCreateRouteResponseResponseResponseParametersTypeDef
):
    pass


_ClientCreateRouteResponseResponseTypeDef = TypedDict(
    "_ClientCreateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ClientCreateRouteResponseResponseResponseParametersTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)


class ClientCreateRouteResponseResponseTypeDef(_ClientCreateRouteResponseResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **ModelSelectionExpression** *(string) --*

        Represents the model selection expression of a route response.
    """


_ClientCreateRouteResponseRequestParametersTypeDef = TypedDict(
    "_ClientCreateRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)


class ClientCreateRouteResponseRequestParametersTypeDef(
    _ClientCreateRouteResponseRequestParametersTypeDef
):
    pass


_ClientCreateRouteResponseTypeDef = TypedDict(
    "_ClientCreateRouteResponseTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM"],
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


class ClientCreateRouteResponseTypeDef(_ClientCreateRouteResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **ApiKeyRequired** *(boolean) --*

        Specifies whether an API key is required for this route.
    """


_ClientCreateStageAccessLogSettingsTypeDef = TypedDict(
    "_ClientCreateStageAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientCreateStageAccessLogSettingsTypeDef(_ClientCreateStageAccessLogSettingsTypeDef):
    """
    Settings for logging access in this stage.
    - **DestinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientCreateStageDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientCreateStageDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientCreateStageDefaultRouteSettingsTypeDef(_ClientCreateStageDefaultRouteSettingsTypeDef):
    """
    The default route settings for the stage.
    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route. This
      property affects the log entries pushed to Amazon CloudWatch Logs.
    """


_ClientCreateStageResponseAccessLogSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientCreateStageResponseAccessLogSettingsTypeDef(
    _ClientCreateStageResponseAccessLogSettingsTypeDef
):
    """
    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.
      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientCreateStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientCreateStageResponseDefaultRouteSettingsTypeDef(
    _ClientCreateStageResponseDefaultRouteSettingsTypeDef
):
    pass


_ClientCreateStageResponseRouteSettingsTypeDef = TypedDict(
    "_ClientCreateStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientCreateStageResponseRouteSettingsTypeDef(_ClientCreateStageResponseRouteSettingsTypeDef):
    pass


_ClientCreateStageResponseTypeDef = TypedDict(
    "_ClientCreateStageResponseTypeDef",
    {
        "AccessLogSettings": ClientCreateStageResponseAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientCreateStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientCreateStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateStageResponseTypeDef(_ClientCreateStageResponseTypeDef):
    """
    - *(dict) --*

      The request has succeeded and has resulted in the creation of a resource.
      - **AccessLogSettings** *(dict) --*

        Settings for logging access in this stage.
        - **DestinationArn** *(string) --*

          The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientCreateStageRouteSettingsTypeDef = TypedDict(
    "_ClientCreateStageRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientCreateStageRouteSettingsTypeDef(_ClientCreateStageRouteSettingsTypeDef):
    pass


_ClientGetApiMappingResponseTypeDef = TypedDict(
    "_ClientGetApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)


class ClientGetApiMappingResponseTypeDef(_ClientGetApiMappingResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApiId** *(string) --*

        The API identifier.
    """


_ClientGetApiMappingsResponseItemsTypeDef = TypedDict(
    "_ClientGetApiMappingsResponseItemsTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)


class ClientGetApiMappingsResponseItemsTypeDef(_ClientGetApiMappingsResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents an API mapping.
      - **ApiId** *(string) --*

        The API identifier.
    """


_ClientGetApiMappingsResponseTypeDef = TypedDict(
    "_ClientGetApiMappingsResponseTypeDef",
    {"Items": List[ClientGetApiMappingsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetApiMappingsResponseTypeDef(_ClientGetApiMappingsResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an API mapping.
          - **ApiId** *(string) --*

            The API identifier.
    """


_ClientGetApiResponseTypeDef = TypedDict(
    "_ClientGetApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetApiResponseTypeDef(_ClientGetApiResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApiEndpoint** *(string) --*

        The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name
        is typically appended to this URI to form a complete path to a deployed API stage.
    """


_ClientGetApisResponseItemsTypeDef = TypedDict(
    "_ClientGetApisResponseItemsTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetApisResponseItemsTypeDef(_ClientGetApisResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents an API.
      - **ApiEndpoint** *(string) --*

        The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name
        is typically appended to this URI to form a complete path to a deployed API stage.
    """


_ClientGetApisResponseTypeDef = TypedDict(
    "_ClientGetApisResponseTypeDef",
    {"Items": List[ClientGetApisResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetApisResponseTypeDef(_ClientGetApisResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an API.
          - **ApiEndpoint** *(string) --*

            The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage
            name is typically appended to this URI to form a complete path to a deployed API stage.
    """


_ClientGetAuthorizerResponseTypeDef = TypedDict(
    "_ClientGetAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class ClientGetAuthorizerResponseTypeDef(_ClientGetAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **AuthorizerCredentialsArn** *(string) --*

        Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.
        To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN).
        To use resource-based permissions on the Lambda function, specify null.
    """


_ClientGetAuthorizersResponseItemsTypeDef = TypedDict(
    "_ClientGetAuthorizersResponseItemsTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class ClientGetAuthorizersResponseItemsTypeDef(_ClientGetAuthorizersResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents an authorizer.
      - **AuthorizerCredentialsArn** *(string) --*

        Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.
        To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN).
        To use resource-based permissions on the Lambda function, specify null.
    """


_ClientGetAuthorizersResponseTypeDef = TypedDict(
    "_ClientGetAuthorizersResponseTypeDef",
    {"Items": List[ClientGetAuthorizersResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetAuthorizersResponseTypeDef(_ClientGetAuthorizersResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an authorizer.
          - **AuthorizerCredentialsArn** *(string) --*

            Specifies the required credentials as an IAM role for API Gateway to invoke the
            authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon
            Resource Name (ARN). To use resource-based permissions on the Lambda function, specify
            null.
    """


_ClientGetDeploymentResponseTypeDef = TypedDict(
    "_ClientGetDeploymentResponseTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class ClientGetDeploymentResponseTypeDef(_ClientGetDeploymentResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **CreatedDate** *(datetime) --*

        The date and time when the Deployment resource was created.
    """


_ClientGetDeploymentsResponseItemsTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseItemsTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class ClientGetDeploymentsResponseItemsTypeDef(_ClientGetDeploymentsResponseItemsTypeDef):
    """
    - *(dict) --*

      An immutable representation of an API that can be called by users. A Deployment must be
      associated with a Stage for it to be callable over the internet.
      - **CreatedDate** *(datetime) --*

        The date and time when the Deployment resource was created.
    """


_ClientGetDeploymentsResponseTypeDef = TypedDict(
    "_ClientGetDeploymentsResponseTypeDef",
    {"Items": List[ClientGetDeploymentsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetDeploymentsResponseTypeDef(_ClientGetDeploymentsResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          An immutable representation of an API that can be called by users. A Deployment must be
          associated with a Stage for it to be callable over the internet.
          - **CreatedDate** *(datetime) --*

            The date and time when the Deployment resource was created.
    """


_ClientGetDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientGetDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientGetDomainNameResponseDomainNameConfigurationsTypeDef(
    _ClientGetDomainNameResponseDomainNameConfigurationsTypeDef
):
    pass


_ClientGetDomainNameResponseTypeDef = TypedDict(
    "_ClientGetDomainNameResponseTypeDef",
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


class ClientGetDomainNameResponseTypeDef(_ClientGetDomainNameResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApiMappingSelectionExpression** *(string) --*

        The API mapping selection expression.
    """


_ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef(
    _ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef
):
    pass


_ClientGetDomainNamesResponseItemsTypeDef = TypedDict(
    "_ClientGetDomainNamesResponseItemsTypeDef",
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


class ClientGetDomainNamesResponseItemsTypeDef(_ClientGetDomainNamesResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents a domain name.
      - **ApiMappingSelectionExpression** *(string) --*

        The API mapping selection expression.
    """


_ClientGetDomainNamesResponseTypeDef = TypedDict(
    "_ClientGetDomainNamesResponseTypeDef",
    {"Items": List[ClientGetDomainNamesResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetDomainNamesResponseTypeDef(_ClientGetDomainNamesResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents a domain name.
          - **ApiMappingSelectionExpression** *(string) --*

            The API mapping selection expression.
    """


_ClientGetIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponseResponseTypeDef",
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


class ClientGetIntegrationResponseResponseTypeDef(_ClientGetIntegrationResponseResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ContentHandlingStrategy** *(string) --*

        Specifies how to handle response payload content type conversions. Supported values are
        CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
        CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
        corresponding binary blob.
        CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
        If this property is not defined, the response payload will be passed through from the
        integration response to the route response or method response without modification.
    """


_ClientGetIntegrationResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponseTypeDef",
    {
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
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class ClientGetIntegrationResponseTypeDef(_ClientGetIntegrationResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ConnectionId** *(string) --*

        The connection ID.
    """


_ClientGetIntegrationResponsesResponseItemsTypeDef = TypedDict(
    "_ClientGetIntegrationResponsesResponseItemsTypeDef",
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


class ClientGetIntegrationResponsesResponseItemsTypeDef(
    _ClientGetIntegrationResponsesResponseItemsTypeDef
):
    """
    - *(dict) --*

      Represents an integration response.
      - **ContentHandlingStrategy** *(string) --*

        Specifies how to handle response payload content type conversions. Supported values are
        CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
        CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
        corresponding binary blob.
        CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
        If this property is not defined, the response payload will be passed through from the
        integration response to the route response or method response without modification.
    """


_ClientGetIntegrationResponsesResponseTypeDef = TypedDict(
    "_ClientGetIntegrationResponsesResponseTypeDef",
    {"Items": List[ClientGetIntegrationResponsesResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetIntegrationResponsesResponseTypeDef(_ClientGetIntegrationResponsesResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an integration response.
          - **ContentHandlingStrategy** *(string) --*

            Specifies how to handle response payload content type conversions. Supported values are
            CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
            CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
            corresponding binary blob.
            CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
            string.
            If this property is not defined, the response payload will be passed through from the
            integration response to the route response or method response without modification.
    """


_ClientGetIntegrationsResponseItemsTypeDef = TypedDict(
    "_ClientGetIntegrationsResponseItemsTypeDef",
    {
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
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class ClientGetIntegrationsResponseItemsTypeDef(_ClientGetIntegrationsResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents an integration.
      - **ConnectionId** *(string) --*

        The connection ID.
    """


_ClientGetIntegrationsResponseTypeDef = TypedDict(
    "_ClientGetIntegrationsResponseTypeDef",
    {"Items": List[ClientGetIntegrationsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetIntegrationsResponseTypeDef(_ClientGetIntegrationsResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an integration.
          - **ConnectionId** *(string) --*

            The connection ID.
    """


_ClientGetModelResponseTypeDef = TypedDict(
    "_ClientGetModelResponseTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)


class ClientGetModelResponseTypeDef(_ClientGetModelResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ContentType** *(string) --*

        The content-type for the model, for example, "application/json".
    """


_ClientGetModelTemplateResponseTypeDef = TypedDict(
    "_ClientGetModelTemplateResponseTypeDef", {"Value": str}, total=False
)


class ClientGetModelTemplateResponseTypeDef(_ClientGetModelTemplateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Value** *(string) --*

        The template value.
    """


_ClientGetModelsResponseItemsTypeDef = TypedDict(
    "_ClientGetModelsResponseItemsTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)


class ClientGetModelsResponseItemsTypeDef(_ClientGetModelsResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents a data model for an API. See `Create Models and Mapping Templates for Request and
      Response Mappings
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__ .
      - **ContentType** *(string) --*

        The content-type for the model, for example, "application/json".
    """


_ClientGetModelsResponseTypeDef = TypedDict(
    "_ClientGetModelsResponseTypeDef",
    {"Items": List[ClientGetModelsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetModelsResponseTypeDef(_ClientGetModelsResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents a data model for an API. See `Create Models and Mapping Templates for Request
          and Response Mappings
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__ .
          - **ContentType** *(string) --*

            The content-type for the model, for example, "application/json".
    """


_ClientGetRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "_ClientGetRouteResponseResponseResponseParametersTypeDef", {"Required": bool}, total=False
)


class ClientGetRouteResponseResponseResponseParametersTypeDef(
    _ClientGetRouteResponseResponseResponseParametersTypeDef
):
    pass


_ClientGetRouteResponseResponseTypeDef = TypedDict(
    "_ClientGetRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ClientGetRouteResponseResponseResponseParametersTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)


class ClientGetRouteResponseResponseTypeDef(_ClientGetRouteResponseResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ModelSelectionExpression** *(string) --*

        Represents the model selection expression of a route response.
    """


_ClientGetRouteResponseRequestParametersTypeDef = TypedDict(
    "_ClientGetRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)


class ClientGetRouteResponseRequestParametersTypeDef(
    _ClientGetRouteResponseRequestParametersTypeDef
):
    pass


_ClientGetRouteResponseTypeDef = TypedDict(
    "_ClientGetRouteResponseTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM"],
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


class ClientGetRouteResponseTypeDef(_ClientGetRouteResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApiKeyRequired** *(boolean) --*

        Specifies whether an API key is required for this route.
    """


_ClientGetRouteResponsesResponseItemsResponseParametersTypeDef = TypedDict(
    "_ClientGetRouteResponsesResponseItemsResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)


class ClientGetRouteResponsesResponseItemsResponseParametersTypeDef(
    _ClientGetRouteResponsesResponseItemsResponseParametersTypeDef
):
    pass


_ClientGetRouteResponsesResponseItemsTypeDef = TypedDict(
    "_ClientGetRouteResponsesResponseItemsTypeDef",
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


class ClientGetRouteResponsesResponseItemsTypeDef(_ClientGetRouteResponsesResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents a route response.
      - **ModelSelectionExpression** *(string) --*

        Represents the model selection expression of a route response.
    """


_ClientGetRouteResponsesResponseTypeDef = TypedDict(
    "_ClientGetRouteResponsesResponseTypeDef",
    {"Items": List[ClientGetRouteResponsesResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetRouteResponsesResponseTypeDef(_ClientGetRouteResponsesResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents a route response.
          - **ModelSelectionExpression** *(string) --*

            Represents the model selection expression of a route response.
    """


_ClientGetRoutesResponseItemsRequestParametersTypeDef = TypedDict(
    "_ClientGetRoutesResponseItemsRequestParametersTypeDef", {"Required": bool}, total=False
)


class ClientGetRoutesResponseItemsRequestParametersTypeDef(
    _ClientGetRoutesResponseItemsRequestParametersTypeDef
):
    pass


_ClientGetRoutesResponseItemsTypeDef = TypedDict(
    "_ClientGetRoutesResponseItemsTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM"],
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


class ClientGetRoutesResponseItemsTypeDef(_ClientGetRoutesResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents a route.
      - **ApiKeyRequired** *(boolean) --*

        Specifies whether an API key is required for this route.
    """


_ClientGetRoutesResponseTypeDef = TypedDict(
    "_ClientGetRoutesResponseTypeDef",
    {"Items": List[ClientGetRoutesResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetRoutesResponseTypeDef(_ClientGetRoutesResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents a route.
          - **ApiKeyRequired** *(boolean) --*

            Specifies whether an API key is required for this route.
    """


_ClientGetStageResponseAccessLogSettingsTypeDef = TypedDict(
    "_ClientGetStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientGetStageResponseAccessLogSettingsTypeDef(
    _ClientGetStageResponseAccessLogSettingsTypeDef
):
    """
    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.
      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientGetStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientGetStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientGetStageResponseDefaultRouteSettingsTypeDef(
    _ClientGetStageResponseDefaultRouteSettingsTypeDef
):
    pass


_ClientGetStageResponseRouteSettingsTypeDef = TypedDict(
    "_ClientGetStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientGetStageResponseRouteSettingsTypeDef(_ClientGetStageResponseRouteSettingsTypeDef):
    pass


_ClientGetStageResponseTypeDef = TypedDict(
    "_ClientGetStageResponseTypeDef",
    {
        "AccessLogSettings": ClientGetStageResponseAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientGetStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientGetStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetStageResponseTypeDef(_ClientGetStageResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **AccessLogSettings** *(dict) --*

        Settings for logging access in this stage.
        - **DestinationArn** *(string) --*

          The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientGetStagesResponseItemsAccessLogSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseItemsAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientGetStagesResponseItemsAccessLogSettingsTypeDef(
    _ClientGetStagesResponseItemsAccessLogSettingsTypeDef
):
    """
    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.
      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef(
    _ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef
):
    pass


_ClientGetStagesResponseItemsRouteSettingsTypeDef = TypedDict(
    "_ClientGetStagesResponseItemsRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientGetStagesResponseItemsRouteSettingsTypeDef(
    _ClientGetStagesResponseItemsRouteSettingsTypeDef
):
    pass


_ClientGetStagesResponseItemsTypeDef = TypedDict(
    "_ClientGetStagesResponseItemsTypeDef",
    {
        "AccessLogSettings": ClientGetStagesResponseItemsAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientGetStagesResponseItemsRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetStagesResponseItemsTypeDef(_ClientGetStagesResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents an API stage.
      - **AccessLogSettings** *(dict) --*

        Settings for logging access in this stage.
        - **DestinationArn** *(string) --*

          The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientGetStagesResponseTypeDef = TypedDict(
    "_ClientGetStagesResponseTypeDef",
    {"Items": List[ClientGetStagesResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetStagesResponseTypeDef(_ClientGetStagesResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an API stage.
          - **AccessLogSettings** *(dict) --*

            Settings for logging access in this stage.
            - **DestinationArn** *(string) --*

              The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientGetTagsResponseTypeDef = TypedDict(
    "_ClientGetTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientGetTagsResponseTypeDef(_ClientGetTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        - *(string) --*

          - *(string) --*
    """


_ClientUpdateApiMappingResponseTypeDef = TypedDict(
    "_ClientUpdateApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)


class ClientUpdateApiMappingResponseTypeDef(_ClientUpdateApiMappingResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApiId** *(string) --*

        The API identifier.
    """


_ClientUpdateApiResponseTypeDef = TypedDict(
    "_ClientUpdateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateApiResponseTypeDef(_ClientUpdateApiResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApiEndpoint** *(string) --*

        The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name
        is typically appended to this URI to form a complete path to a deployed API stage.
    """


_ClientUpdateAuthorizerResponseTypeDef = TypedDict(
    "_ClientUpdateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class ClientUpdateAuthorizerResponseTypeDef(_ClientUpdateAuthorizerResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **AuthorizerCredentialsArn** *(string) --*

        Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.
        To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN).
        To use resource-based permissions on the Lambda function, specify null.
    """


_ClientUpdateDeploymentResponseTypeDef = TypedDict(
    "_ClientUpdateDeploymentResponseTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class ClientUpdateDeploymentResponseTypeDef(_ClientUpdateDeploymentResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **CreatedDate** *(datetime) --*

        The date and time when the Deployment resource was created.
    """


_ClientUpdateDomainNameDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientUpdateDomainNameDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientUpdateDomainNameDomainNameConfigurationsTypeDef(
    _ClientUpdateDomainNameDomainNameConfigurationsTypeDef
):
    """
    - *(dict) --*

      The domain name configuration.
      - **ApiGatewayDomainName** *(string) --*

        A domain name for the WebSocket API.
    """


_ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "_ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef(
    _ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef
):
    pass


_ClientUpdateDomainNameResponseTypeDef = TypedDict(
    "_ClientUpdateDomainNameResponseTypeDef",
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


class ClientUpdateDomainNameResponseTypeDef(_ClientUpdateDomainNameResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApiMappingSelectionExpression** *(string) --*

        The API mapping selection expression.
    """


_ClientUpdateIntegrationResponseResponseTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseResponseTypeDef",
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


class ClientUpdateIntegrationResponseResponseTypeDef(
    _ClientUpdateIntegrationResponseResponseTypeDef
):
    """
    - *(dict) --*

      Success
      - **ContentHandlingStrategy** *(string) --*

        Specifies how to handle response payload content type conversions. Supported values are
        CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
        CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
        corresponding binary blob.
        CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
        If this property is not defined, the response payload will be passed through from the
        integration response to the route response or method response without modification.
    """


_ClientUpdateIntegrationResponseTypeDef = TypedDict(
    "_ClientUpdateIntegrationResponseTypeDef",
    {
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
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class ClientUpdateIntegrationResponseTypeDef(_ClientUpdateIntegrationResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ConnectionId** *(string) --*

        The connection ID.
    """


_ClientUpdateModelResponseTypeDef = TypedDict(
    "_ClientUpdateModelResponseTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)


class ClientUpdateModelResponseTypeDef(_ClientUpdateModelResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ContentType** *(string) --*

        The content-type for the model, for example, "application/json".
    """


_ClientUpdateRouteRequestParametersTypeDef = TypedDict(
    "_ClientUpdateRouteRequestParametersTypeDef", {"Required": bool}, total=False
)


class ClientUpdateRouteRequestParametersTypeDef(_ClientUpdateRouteRequestParametersTypeDef):
    pass


_ClientUpdateRouteResponseResponseParametersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseResponseParametersTypeDef", {"Required": bool}, total=False
)


class ClientUpdateRouteResponseResponseParametersTypeDef(
    _ClientUpdateRouteResponseResponseParametersTypeDef
):
    pass


_ClientUpdateRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseResponseResponseParametersTypeDef", {"Required": bool}, total=False
)


class ClientUpdateRouteResponseResponseResponseParametersTypeDef(
    _ClientUpdateRouteResponseResponseResponseParametersTypeDef
):
    pass


_ClientUpdateRouteResponseResponseTypeDef = TypedDict(
    "_ClientUpdateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ClientUpdateRouteResponseResponseResponseParametersTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)


class ClientUpdateRouteResponseResponseTypeDef(_ClientUpdateRouteResponseResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ModelSelectionExpression** *(string) --*

        Represents the model selection expression of a route response.
    """


_ClientUpdateRouteResponseRequestParametersTypeDef = TypedDict(
    "_ClientUpdateRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)


class ClientUpdateRouteResponseRequestParametersTypeDef(
    _ClientUpdateRouteResponseRequestParametersTypeDef
):
    pass


_ClientUpdateRouteResponseTypeDef = TypedDict(
    "_ClientUpdateRouteResponseTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM"],
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


class ClientUpdateRouteResponseTypeDef(_ClientUpdateRouteResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **ApiKeyRequired** *(boolean) --*

        Specifies whether an API key is required for this route.
    """


_ClientUpdateStageAccessLogSettingsTypeDef = TypedDict(
    "_ClientUpdateStageAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientUpdateStageAccessLogSettingsTypeDef(_ClientUpdateStageAccessLogSettingsTypeDef):
    """
    Settings for logging access in this stage.
    - **DestinationArn** *(string) --*

      The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientUpdateStageDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientUpdateStageDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientUpdateStageDefaultRouteSettingsTypeDef(_ClientUpdateStageDefaultRouteSettingsTypeDef):
    """
    The default route settings for the stage.
    - **DataTraceEnabled** *(boolean) --*

      Specifies whether (true) or not (false) data trace logging is enabled for this route. This
      property affects the log entries pushed to Amazon CloudWatch Logs.
    """


_ClientUpdateStageResponseAccessLogSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class ClientUpdateStageResponseAccessLogSettingsTypeDef(
    _ClientUpdateStageResponseAccessLogSettingsTypeDef
):
    """
    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.
      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientUpdateStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientUpdateStageResponseDefaultRouteSettingsTypeDef(
    _ClientUpdateStageResponseDefaultRouteSettingsTypeDef
):
    pass


_ClientUpdateStageResponseRouteSettingsTypeDef = TypedDict(
    "_ClientUpdateStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientUpdateStageResponseRouteSettingsTypeDef(_ClientUpdateStageResponseRouteSettingsTypeDef):
    pass


_ClientUpdateStageResponseTypeDef = TypedDict(
    "_ClientUpdateStageResponseTypeDef",
    {
        "AccessLogSettings": ClientUpdateStageResponseAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientUpdateStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientUpdateStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateStageResponseTypeDef(_ClientUpdateStageResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **AccessLogSettings** *(dict) --*

        Settings for logging access in this stage.
        - **DestinationArn** *(string) --*

          The ARN of the CloudWatch Logs log group to receive access logs.
    """


_ClientUpdateStageRouteSettingsTypeDef = TypedDict(
    "_ClientUpdateStageRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class ClientUpdateStageRouteSettingsTypeDef(_ClientUpdateStageRouteSettingsTypeDef):
    pass


_GetApisPaginatePaginationConfigTypeDef = TypedDict(
    "_GetApisPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetApisPaginatePaginationConfigTypeDef(_GetApisPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetApisPaginateResponseItemsTypeDef = TypedDict(
    "_GetApisPaginateResponseItemsTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "Version": str,
        "Warnings": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetApisPaginateResponseItemsTypeDef(_GetApisPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents an API.
      - **ApiEndpoint** *(string) --*

        The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name
        is typically appended to this URI to form a complete path to a deployed API stage.
    """


_GetApisPaginateResponseTypeDef = TypedDict(
    "_GetApisPaginateResponseTypeDef",
    {"Items": List[GetApisPaginateResponseItemsTypeDef]},
    total=False,
)


class GetApisPaginateResponseTypeDef(_GetApisPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an API.
          - **ApiEndpoint** *(string) --*

            The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage
            name is typically appended to this URI to form a complete path to a deployed API stage.
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


_GetAuthorizersPaginateResponseItemsTypeDef = TypedDict(
    "_GetAuthorizersPaginateResponseItemsTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": str,
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "Name": str,
        "ProviderArns": List[str],
    },
    total=False,
)


class GetAuthorizersPaginateResponseItemsTypeDef(_GetAuthorizersPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents an authorizer.
      - **AuthorizerCredentialsArn** *(string) --*

        Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.
        To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN).
        To use resource-based permissions on the Lambda function, specify null.
    """


_GetAuthorizersPaginateResponseTypeDef = TypedDict(
    "_GetAuthorizersPaginateResponseTypeDef",
    {"Items": List[GetAuthorizersPaginateResponseItemsTypeDef]},
    total=False,
)


class GetAuthorizersPaginateResponseTypeDef(_GetAuthorizersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an authorizer.
          - **AuthorizerCredentialsArn** *(string) --*

            Specifies the required credentials as an IAM role for API Gateway to invoke the
            authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon
            Resource Name (ARN). To use resource-based permissions on the Lambda function, specify
            null.
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


_GetDeploymentsPaginateResponseItemsTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseItemsTypeDef",
    {
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)


class GetDeploymentsPaginateResponseItemsTypeDef(_GetDeploymentsPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      An immutable representation of an API that can be called by users. A Deployment must be
      associated with a Stage for it to be callable over the internet.
      - **CreatedDate** *(datetime) --*

        The date and time when the Deployment resource was created.
    """


_GetDeploymentsPaginateResponseTypeDef = TypedDict(
    "_GetDeploymentsPaginateResponseTypeDef",
    {"Items": List[GetDeploymentsPaginateResponseItemsTypeDef]},
    total=False,
)


class GetDeploymentsPaginateResponseTypeDef(_GetDeploymentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          An immutable representation of an API that can be called by users. A Deployment must be
          associated with a Stage for it to be callable over the internet.
          - **CreatedDate** *(datetime) --*

            The date and time when the Deployment resource was created.
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


_GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef = TypedDict(
    "_GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
    },
    total=False,
)


class GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef(
    _GetDomainNamesPaginateResponseItemsDomainNameConfigurationsTypeDef
):
    pass


_GetDomainNamesPaginateResponseItemsTypeDef = TypedDict(
    "_GetDomainNamesPaginateResponseItemsTypeDef",
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


class GetDomainNamesPaginateResponseItemsTypeDef(_GetDomainNamesPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents a domain name.
      - **ApiMappingSelectionExpression** *(string) --*

        The API mapping selection expression.
    """


_GetDomainNamesPaginateResponseTypeDef = TypedDict(
    "_GetDomainNamesPaginateResponseTypeDef",
    {"Items": List[GetDomainNamesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetDomainNamesPaginateResponseTypeDef(_GetDomainNamesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents a domain name.
          - **ApiMappingSelectionExpression** *(string) --*

            The API mapping selection expression.
    """


_GetIntegrationResponsesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetIntegrationResponsesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetIntegrationResponsesPaginatePaginationConfigTypeDef(
    _GetIntegrationResponsesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetIntegrationResponsesPaginateResponseItemsTypeDef = TypedDict(
    "_GetIntegrationResponsesPaginateResponseItemsTypeDef",
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


class GetIntegrationResponsesPaginateResponseItemsTypeDef(
    _GetIntegrationResponsesPaginateResponseItemsTypeDef
):
    """
    - *(dict) --*

      Represents an integration response.
      - **ContentHandlingStrategy** *(string) --*

        Specifies how to handle response payload content type conversions. Supported values are
        CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
        CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
        corresponding binary blob.
        CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.
        If this property is not defined, the response payload will be passed through from the
        integration response to the route response or method response without modification.
    """


_GetIntegrationResponsesPaginateResponseTypeDef = TypedDict(
    "_GetIntegrationResponsesPaginateResponseTypeDef",
    {"Items": List[GetIntegrationResponsesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetIntegrationResponsesPaginateResponseTypeDef(
    _GetIntegrationResponsesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an integration response.
          - **ContentHandlingStrategy** *(string) --*

            Specifies how to handle response payload content type conversions. Supported values are
            CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:
            CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
            corresponding binary blob.
            CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded
            string.
            If this property is not defined, the response payload will be passed through from the
            integration response to the route response or method response without modification.
    """


_GetIntegrationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetIntegrationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetIntegrationsPaginatePaginationConfigTypeDef(
    _GetIntegrationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetIntegrationsPaginateResponseItemsTypeDef = TypedDict(
    "_GetIntegrationsPaginateResponseItemsTypeDef",
    {
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
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)


class GetIntegrationsPaginateResponseItemsTypeDef(_GetIntegrationsPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents an integration.
      - **ConnectionId** *(string) --*

        The connection ID.
    """


_GetIntegrationsPaginateResponseTypeDef = TypedDict(
    "_GetIntegrationsPaginateResponseTypeDef",
    {"Items": List[GetIntegrationsPaginateResponseItemsTypeDef]},
    total=False,
)


class GetIntegrationsPaginateResponseTypeDef(_GetIntegrationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an integration.
          - **ConnectionId** *(string) --*

            The connection ID.
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


_GetModelsPaginateResponseItemsTypeDef = TypedDict(
    "_GetModelsPaginateResponseItemsTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)


class GetModelsPaginateResponseItemsTypeDef(_GetModelsPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents a data model for an API. See `Create Models and Mapping Templates for Request and
      Response Mappings
      <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__ .
      - **ContentType** *(string) --*

        The content-type for the model, for example, "application/json".
    """


_GetModelsPaginateResponseTypeDef = TypedDict(
    "_GetModelsPaginateResponseTypeDef",
    {"Items": List[GetModelsPaginateResponseItemsTypeDef]},
    total=False,
)


class GetModelsPaginateResponseTypeDef(_GetModelsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents a data model for an API. See `Create Models and Mapping Templates for Request
          and Response Mappings
          <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__ .
          - **ContentType** *(string) --*

            The content-type for the model, for example, "application/json".
    """


_GetRouteResponsesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRouteResponsesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetRouteResponsesPaginatePaginationConfigTypeDef(
    _GetRouteResponsesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef = TypedDict(
    "_GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef",
    {"Required": bool},
    total=False,
)


class GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef(
    _GetRouteResponsesPaginateResponseItemsResponseParametersTypeDef
):
    pass


_GetRouteResponsesPaginateResponseItemsTypeDef = TypedDict(
    "_GetRouteResponsesPaginateResponseItemsTypeDef",
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


class GetRouteResponsesPaginateResponseItemsTypeDef(_GetRouteResponsesPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents a route response.
      - **ModelSelectionExpression** *(string) --*

        Represents the model selection expression of a route response.
    """


_GetRouteResponsesPaginateResponseTypeDef = TypedDict(
    "_GetRouteResponsesPaginateResponseTypeDef",
    {"Items": List[GetRouteResponsesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetRouteResponsesPaginateResponseTypeDef(_GetRouteResponsesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents a route response.
          - **ModelSelectionExpression** *(string) --*

            Represents the model selection expression of a route response.
    """


_GetRoutesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetRoutesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetRoutesPaginatePaginationConfigTypeDef(_GetRoutesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetRoutesPaginateResponseItemsRequestParametersTypeDef = TypedDict(
    "_GetRoutesPaginateResponseItemsRequestParametersTypeDef", {"Required": bool}, total=False
)


class GetRoutesPaginateResponseItemsRequestParametersTypeDef(
    _GetRoutesPaginateResponseItemsRequestParametersTypeDef
):
    pass


_GetRoutesPaginateResponseItemsTypeDef = TypedDict(
    "_GetRoutesPaginateResponseItemsTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM"],
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


class GetRoutesPaginateResponseItemsTypeDef(_GetRoutesPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents a route.
      - **ApiKeyRequired** *(boolean) --*

        Specifies whether an API key is required for this route.
    """


_GetRoutesPaginateResponseTypeDef = TypedDict(
    "_GetRoutesPaginateResponseTypeDef",
    {"Items": List[GetRoutesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetRoutesPaginateResponseTypeDef(_GetRoutesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents a route.
          - **ApiKeyRequired** *(boolean) --*

            Specifies whether an API key is required for this route.
    """


_GetStagesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetStagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetStagesPaginatePaginationConfigTypeDef(_GetStagesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetStagesPaginateResponseItemsAccessLogSettingsTypeDef = TypedDict(
    "_GetStagesPaginateResponseItemsAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)


class GetStagesPaginateResponseItemsAccessLogSettingsTypeDef(
    _GetStagesPaginateResponseItemsAccessLogSettingsTypeDef
):
    """
    - **AccessLogSettings** *(dict) --*

      Settings for logging access in this stage.
      - **DestinationArn** *(string) --*

        The ARN of the CloudWatch Logs log group to receive access logs.
    """


_GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef = TypedDict(
    "_GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef(
    _GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef
):
    pass


_GetStagesPaginateResponseItemsRouteSettingsTypeDef = TypedDict(
    "_GetStagesPaginateResponseItemsRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)


class GetStagesPaginateResponseItemsRouteSettingsTypeDef(
    _GetStagesPaginateResponseItemsRouteSettingsTypeDef
):
    pass


_GetStagesPaginateResponseItemsTypeDef = TypedDict(
    "_GetStagesPaginateResponseItemsTypeDef",
    {
        "AccessLogSettings": GetStagesPaginateResponseItemsAccessLogSettingsTypeDef,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": GetStagesPaginateResponseItemsDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, GetStagesPaginateResponseItemsRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetStagesPaginateResponseItemsTypeDef(_GetStagesPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      Represents an API stage.
      - **AccessLogSettings** *(dict) --*

        Settings for logging access in this stage.
        - **DestinationArn** *(string) --*

          The ARN of the CloudWatch Logs log group to receive access logs.
    """


_GetStagesPaginateResponseTypeDef = TypedDict(
    "_GetStagesPaginateResponseTypeDef",
    {"Items": List[GetStagesPaginateResponseItemsTypeDef]},
    total=False,
)


class GetStagesPaginateResponseTypeDef(_GetStagesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Success
      - **Items** *(list) --*

        The elements from this collection.
        - *(dict) --*

          Represents an API stage.
          - **AccessLogSettings** *(dict) --*

            Settings for logging access in this stage.
            - **DestinationArn** *(string) --*

              The ARN of the CloudWatch Logs log group to receive access logs.
    """
