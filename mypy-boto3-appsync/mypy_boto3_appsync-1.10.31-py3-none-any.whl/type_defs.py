"Main interface for appsync service type defs"
from __future__ import annotations

from typing import Dict, List
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateApiCacheResponseapiCacheTypeDef",
    "ClientCreateApiCacheResponseTypeDef",
    "ClientCreateApiKeyResponseapiKeyTypeDef",
    "ClientCreateApiKeyResponseTypeDef",
    "ClientCreateDataSourceDynamodbConfigdeltaSyncConfigTypeDef",
    "ClientCreateDataSourceDynamodbConfigTypeDef",
    "ClientCreateDataSourceElasticsearchConfigTypeDef",
    "ClientCreateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef",
    "ClientCreateDataSourceHttpConfigauthorizationConfigTypeDef",
    "ClientCreateDataSourceHttpConfigTypeDef",
    "ClientCreateDataSourceLambdaConfigTypeDef",
    "ClientCreateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    "ClientCreateDataSourceRelationalDatabaseConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourcedynamodbConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourceelasticsearchConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourcehttpConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourcelambdaConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef",
    "ClientCreateDataSourceResponsedataSourceTypeDef",
    "ClientCreateDataSourceResponseTypeDef",
    "ClientCreateFunctionResponsefunctionConfigurationTypeDef",
    "ClientCreateFunctionResponseTypeDef",
    "ClientCreateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    "ClientCreateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef",
    "ClientCreateGraphqlApiAdditionalAuthenticationProvidersTypeDef",
    "ClientCreateGraphqlApiLogConfigTypeDef",
    "ClientCreateGraphqlApiOpenIDConnectConfigTypeDef",
    "ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    "ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    "ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef",
    "ClientCreateGraphqlApiResponsegraphqlApilogConfigTypeDef",
    "ClientCreateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef",
    "ClientCreateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef",
    "ClientCreateGraphqlApiResponsegraphqlApiTypeDef",
    "ClientCreateGraphqlApiResponseTypeDef",
    "ClientCreateGraphqlApiUserPoolConfigTypeDef",
    "ClientCreateResolverCachingConfigTypeDef",
    "ClientCreateResolverPipelineConfigTypeDef",
    "ClientCreateResolverResponseresolvercachingConfigTypeDef",
    "ClientCreateResolverResponseresolverpipelineConfigTypeDef",
    "ClientCreateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef",
    "ClientCreateResolverResponseresolversyncConfigTypeDef",
    "ClientCreateResolverResponseresolverTypeDef",
    "ClientCreateResolverResponseTypeDef",
    "ClientCreateResolverSyncConfiglambdaConflictHandlerConfigTypeDef",
    "ClientCreateResolverSyncConfigTypeDef",
    "ClientCreateTypeResponsetypeTypeDef",
    "ClientCreateTypeResponseTypeDef",
    "ClientGetApiCacheResponseapiCacheTypeDef",
    "ClientGetApiCacheResponseTypeDef",
    "ClientGetDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef",
    "ClientGetDataSourceResponsedataSourcedynamodbConfigTypeDef",
    "ClientGetDataSourceResponsedataSourceelasticsearchConfigTypeDef",
    "ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef",
    "ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef",
    "ClientGetDataSourceResponsedataSourcehttpConfigTypeDef",
    "ClientGetDataSourceResponsedataSourcelambdaConfigTypeDef",
    "ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    "ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef",
    "ClientGetDataSourceResponsedataSourceTypeDef",
    "ClientGetDataSourceResponseTypeDef",
    "ClientGetFunctionResponsefunctionConfigurationTypeDef",
    "ClientGetFunctionResponseTypeDef",
    "ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    "ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    "ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef",
    "ClientGetGraphqlApiResponsegraphqlApilogConfigTypeDef",
    "ClientGetGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef",
    "ClientGetGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef",
    "ClientGetGraphqlApiResponsegraphqlApiTypeDef",
    "ClientGetGraphqlApiResponseTypeDef",
    "ClientGetIntrospectionSchemaResponseTypeDef",
    "ClientGetResolverResponseresolvercachingConfigTypeDef",
    "ClientGetResolverResponseresolverpipelineConfigTypeDef",
    "ClientGetResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef",
    "ClientGetResolverResponseresolversyncConfigTypeDef",
    "ClientGetResolverResponseresolverTypeDef",
    "ClientGetResolverResponseTypeDef",
    "ClientGetSchemaCreationStatusResponseTypeDef",
    "ClientGetTypeResponsetypeTypeDef",
    "ClientGetTypeResponseTypeDef",
    "ClientListApiKeysResponseapiKeysTypeDef",
    "ClientListApiKeysResponseTypeDef",
    "ClientListDataSourcesResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef",
    "ClientListDataSourcesResponsedataSourcesdynamodbConfigTypeDef",
    "ClientListDataSourcesResponsedataSourceselasticsearchConfigTypeDef",
    "ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef",
    "ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigTypeDef",
    "ClientListDataSourcesResponsedataSourceshttpConfigTypeDef",
    "ClientListDataSourcesResponsedataSourceslambdaConfigTypeDef",
    "ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    "ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigTypeDef",
    "ClientListDataSourcesResponsedataSourcesTypeDef",
    "ClientListDataSourcesResponseTypeDef",
    "ClientListFunctionsResponsefunctionsTypeDef",
    "ClientListFunctionsResponseTypeDef",
    "ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    "ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    "ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersTypeDef",
    "ClientListGraphqlApisResponsegraphqlApislogConfigTypeDef",
    "ClientListGraphqlApisResponsegraphqlApisopenIDConnectConfigTypeDef",
    "ClientListGraphqlApisResponsegraphqlApisuserPoolConfigTypeDef",
    "ClientListGraphqlApisResponsegraphqlApisTypeDef",
    "ClientListGraphqlApisResponseTypeDef",
    "ClientListResolversByFunctionResponseresolverscachingConfigTypeDef",
    "ClientListResolversByFunctionResponseresolverspipelineConfigTypeDef",
    "ClientListResolversByFunctionResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    "ClientListResolversByFunctionResponseresolverssyncConfigTypeDef",
    "ClientListResolversByFunctionResponseresolversTypeDef",
    "ClientListResolversByFunctionResponseTypeDef",
    "ClientListResolversResponseresolverscachingConfigTypeDef",
    "ClientListResolversResponseresolverspipelineConfigTypeDef",
    "ClientListResolversResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    "ClientListResolversResponseresolverssyncConfigTypeDef",
    "ClientListResolversResponseresolversTypeDef",
    "ClientListResolversResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTypesResponsetypesTypeDef",
    "ClientListTypesResponseTypeDef",
    "ClientStartSchemaCreationResponseTypeDef",
    "ClientUpdateApiCacheResponseapiCacheTypeDef",
    "ClientUpdateApiCacheResponseTypeDef",
    "ClientUpdateApiKeyResponseapiKeyTypeDef",
    "ClientUpdateApiKeyResponseTypeDef",
    "ClientUpdateDataSourceDynamodbConfigdeltaSyncConfigTypeDef",
    "ClientUpdateDataSourceDynamodbConfigTypeDef",
    "ClientUpdateDataSourceElasticsearchConfigTypeDef",
    "ClientUpdateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef",
    "ClientUpdateDataSourceHttpConfigauthorizationConfigTypeDef",
    "ClientUpdateDataSourceHttpConfigTypeDef",
    "ClientUpdateDataSourceLambdaConfigTypeDef",
    "ClientUpdateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    "ClientUpdateDataSourceRelationalDatabaseConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourcedynamodbConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourceelasticsearchConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourcehttpConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourcelambdaConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef",
    "ClientUpdateDataSourceResponsedataSourceTypeDef",
    "ClientUpdateDataSourceResponseTypeDef",
    "ClientUpdateFunctionResponsefunctionConfigurationTypeDef",
    "ClientUpdateFunctionResponseTypeDef",
    "ClientUpdateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    "ClientUpdateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef",
    "ClientUpdateGraphqlApiAdditionalAuthenticationProvidersTypeDef",
    "ClientUpdateGraphqlApiLogConfigTypeDef",
    "ClientUpdateGraphqlApiOpenIDConnectConfigTypeDef",
    "ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    "ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    "ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef",
    "ClientUpdateGraphqlApiResponsegraphqlApilogConfigTypeDef",
    "ClientUpdateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef",
    "ClientUpdateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef",
    "ClientUpdateGraphqlApiResponsegraphqlApiTypeDef",
    "ClientUpdateGraphqlApiResponseTypeDef",
    "ClientUpdateGraphqlApiUserPoolConfigTypeDef",
    "ClientUpdateResolverCachingConfigTypeDef",
    "ClientUpdateResolverPipelineConfigTypeDef",
    "ClientUpdateResolverResponseresolvercachingConfigTypeDef",
    "ClientUpdateResolverResponseresolverpipelineConfigTypeDef",
    "ClientUpdateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef",
    "ClientUpdateResolverResponseresolversyncConfigTypeDef",
    "ClientUpdateResolverResponseresolverTypeDef",
    "ClientUpdateResolverResponseTypeDef",
    "ClientUpdateResolverSyncConfiglambdaConflictHandlerConfigTypeDef",
    "ClientUpdateResolverSyncConfigTypeDef",
    "ClientUpdateTypeResponsetypeTypeDef",
    "ClientUpdateTypeResponseTypeDef",
    "ListApiKeysPaginatePaginationConfigTypeDef",
    "ListApiKeysPaginateResponseapiKeysTypeDef",
    "ListApiKeysPaginateResponseTypeDef",
    "ListDataSourcesPaginatePaginationConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourcesdynamodbConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourceselasticsearchConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourceshttpConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourceslambdaConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigTypeDef",
    "ListDataSourcesPaginateResponsedataSourcesTypeDef",
    "ListDataSourcesPaginateResponseTypeDef",
    "ListFunctionsPaginatePaginationConfigTypeDef",
    "ListFunctionsPaginateResponsefunctionsTypeDef",
    "ListFunctionsPaginateResponseTypeDef",
    "ListGraphqlApisPaginatePaginationConfigTypeDef",
    "ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    "ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    "ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersTypeDef",
    "ListGraphqlApisPaginateResponsegraphqlApislogConfigTypeDef",
    "ListGraphqlApisPaginateResponsegraphqlApisopenIDConnectConfigTypeDef",
    "ListGraphqlApisPaginateResponsegraphqlApisuserPoolConfigTypeDef",
    "ListGraphqlApisPaginateResponsegraphqlApisTypeDef",
    "ListGraphqlApisPaginateResponseTypeDef",
    "ListResolversByFunctionPaginatePaginationConfigTypeDef",
    "ListResolversByFunctionPaginateResponseresolverscachingConfigTypeDef",
    "ListResolversByFunctionPaginateResponseresolverspipelineConfigTypeDef",
    "ListResolversByFunctionPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    "ListResolversByFunctionPaginateResponseresolverssyncConfigTypeDef",
    "ListResolversByFunctionPaginateResponseresolversTypeDef",
    "ListResolversByFunctionPaginateResponseTypeDef",
    "ListResolversPaginatePaginationConfigTypeDef",
    "ListResolversPaginateResponseresolverscachingConfigTypeDef",
    "ListResolversPaginateResponseresolverspipelineConfigTypeDef",
    "ListResolversPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    "ListResolversPaginateResponseresolverssyncConfigTypeDef",
    "ListResolversPaginateResponseresolversTypeDef",
    "ListResolversPaginateResponseTypeDef",
    "ListTypesPaginatePaginationConfigTypeDef",
    "ListTypesPaginateResponsetypesTypeDef",
    "ListTypesPaginateResponseTypeDef",
)


_ClientCreateApiCacheResponseapiCacheTypeDef = TypedDict(
    "_ClientCreateApiCacheResponseapiCacheTypeDef",
    {
        "ttl": int,
        "apiCachingBehavior": Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"],
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
        "type": Literal[
            "T2_SMALL",
            "T2_MEDIUM",
            "R4_LARGE",
            "R4_XLARGE",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
        ],
        "status": Literal["AVAILABLE", "CREATING", "DELETING", "MODIFYING", "FAILED"],
    },
    total=False,
)


class ClientCreateApiCacheResponseapiCacheTypeDef(_ClientCreateApiCacheResponseapiCacheTypeDef):
    """
    - **apiCache** *(dict) --*

      The ``ApiCache`` object.
      - **ttl** *(integer) --*

        TTL in seconds for cache entries.
        Valid values are between 1 and 3600 seconds.
    """


_ClientCreateApiCacheResponseTypeDef = TypedDict(
    "_ClientCreateApiCacheResponseTypeDef",
    {"apiCache": ClientCreateApiCacheResponseapiCacheTypeDef},
    total=False,
)


class ClientCreateApiCacheResponseTypeDef(_ClientCreateApiCacheResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``CreateApiCache`` operation.
      - **apiCache** *(dict) --*

        The ``ApiCache`` object.
        - **ttl** *(integer) --*

          TTL in seconds for cache entries.
          Valid values are between 1 and 3600 seconds.
    """


_ClientCreateApiKeyResponseapiKeyTypeDef = TypedDict(
    "_ClientCreateApiKeyResponseapiKeyTypeDef",
    {"id": str, "description": str, "expires": int},
    total=False,
)


class ClientCreateApiKeyResponseapiKeyTypeDef(_ClientCreateApiKeyResponseapiKeyTypeDef):
    """
    - **apiKey** *(dict) --*

      The API key.
      - **id** *(string) --*

        The API key ID.
    """


_ClientCreateApiKeyResponseTypeDef = TypedDict(
    "_ClientCreateApiKeyResponseTypeDef",
    {"apiKey": ClientCreateApiKeyResponseapiKeyTypeDef},
    total=False,
)


class ClientCreateApiKeyResponseTypeDef(_ClientCreateApiKeyResponseTypeDef):
    """
    - *(dict) --*

      - **apiKey** *(dict) --*

        The API key.
        - **id** *(string) --*

          The API key ID.
    """


_ClientCreateDataSourceDynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceDynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)


class ClientCreateDataSourceDynamodbConfigdeltaSyncConfigTypeDef(
    _ClientCreateDataSourceDynamodbConfigdeltaSyncConfigTypeDef
):
    pass


_RequiredClientCreateDataSourceDynamodbConfigTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceDynamodbConfigTypeDef", {"tableName": str}
)
_OptionalClientCreateDataSourceDynamodbConfigTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceDynamodbConfigTypeDef",
    {
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientCreateDataSourceDynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)


class ClientCreateDataSourceDynamodbConfigTypeDef(
    _RequiredClientCreateDataSourceDynamodbConfigTypeDef,
    _OptionalClientCreateDataSourceDynamodbConfigTypeDef,
):
    """
    Amazon DynamoDB settings.
    - **tableName** *(string) --***[REQUIRED]**

      The table name.
    """


_RequiredClientCreateDataSourceElasticsearchConfigTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceElasticsearchConfigTypeDef", {"endpoint": str}
)
_OptionalClientCreateDataSourceElasticsearchConfigTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceElasticsearchConfigTypeDef", {"awsRegion": str}, total=False
)


class ClientCreateDataSourceElasticsearchConfigTypeDef(
    _RequiredClientCreateDataSourceElasticsearchConfigTypeDef,
    _OptionalClientCreateDataSourceElasticsearchConfigTypeDef,
):
    """
    Amazon Elasticsearch Service settings.
    - **endpoint** *(string) --***[REQUIRED]**

      The endpoint.
    """


_ClientCreateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)


class ClientCreateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef(
    _ClientCreateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef
):
    pass


_ClientCreateDataSourceHttpConfigauthorizationConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceHttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientCreateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)


class ClientCreateDataSourceHttpConfigauthorizationConfigTypeDef(
    _ClientCreateDataSourceHttpConfigauthorizationConfigTypeDef
):
    pass


_ClientCreateDataSourceHttpConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceHttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientCreateDataSourceHttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)


class ClientCreateDataSourceHttpConfigTypeDef(_ClientCreateDataSourceHttpConfigTypeDef):
    """
    HTTP endpoint settings.
    - **endpoint** *(string) --*

      The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and
      the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the
      default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
    """


_ClientCreateDataSourceLambdaConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceLambdaConfigTypeDef", {"lambdaFunctionArn": str}
)


class ClientCreateDataSourceLambdaConfigTypeDef(_ClientCreateDataSourceLambdaConfigTypeDef):
    """
    AWS Lambda settings.
    - **lambdaFunctionArn** *(string) --***[REQUIRED]**

      The ARN for the Lambda function.
    """


_ClientCreateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)


class ClientCreateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef(
    _ClientCreateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef
):
    pass


_ClientCreateDataSourceRelationalDatabaseConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceRelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientCreateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)


class ClientCreateDataSourceRelationalDatabaseConfigTypeDef(
    _ClientCreateDataSourceRelationalDatabaseConfigTypeDef
):
    """
    Relational database settings.
    - **relationalDatabaseSourceType** *(string) --*

      Source type for the relational database.
      * **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon RDS HTTP endpoint.
    """


_ClientCreateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)


class ClientCreateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef(
    _ClientCreateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef
):
    pass


_ClientCreateDataSourceResponsedataSourcedynamodbConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourcedynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientCreateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)


class ClientCreateDataSourceResponsedataSourcedynamodbConfigTypeDef(
    _ClientCreateDataSourceResponsedataSourcedynamodbConfigTypeDef
):
    pass


_ClientCreateDataSourceResponsedataSourceelasticsearchConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourceelasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)


class ClientCreateDataSourceResponsedataSourceelasticsearchConfigTypeDef(
    _ClientCreateDataSourceResponsedataSourceelasticsearchConfigTypeDef
):
    pass


_ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)


class ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef(
    _ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef
):
    pass


_ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)


class ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef(
    _ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef
):
    pass


_ClientCreateDataSourceResponsedataSourcehttpConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourcehttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)


class ClientCreateDataSourceResponsedataSourcehttpConfigTypeDef(
    _ClientCreateDataSourceResponsedataSourcehttpConfigTypeDef
):
    pass


_ClientCreateDataSourceResponsedataSourcelambdaConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourcelambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)


class ClientCreateDataSourceResponsedataSourcelambdaConfigTypeDef(
    _ClientCreateDataSourceResponsedataSourcelambdaConfigTypeDef
):
    pass


_ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)


class ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef(
    _ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef
):
    pass


_ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)


class ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef(
    _ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef
):
    pass


_ClientCreateDataSourceResponsedataSourceTypeDef = TypedDict(
    "_ClientCreateDataSourceResponsedataSourceTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        "serviceRoleArn": str,
        "dynamodbConfig": ClientCreateDataSourceResponsedataSourcedynamodbConfigTypeDef,
        "lambdaConfig": ClientCreateDataSourceResponsedataSourcelambdaConfigTypeDef,
        "elasticsearchConfig": ClientCreateDataSourceResponsedataSourceelasticsearchConfigTypeDef,
        "httpConfig": ClientCreateDataSourceResponsedataSourcehttpConfigTypeDef,
        "relationalDatabaseConfig": ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef,
    },
    total=False,
)


class ClientCreateDataSourceResponsedataSourceTypeDef(
    _ClientCreateDataSourceResponsedataSourceTypeDef
):
    """
    - **dataSource** *(dict) --*

      The ``DataSource`` object.
      - **dataSourceArn** *(string) --*

        The data source ARN.
    """


_ClientCreateDataSourceResponseTypeDef = TypedDict(
    "_ClientCreateDataSourceResponseTypeDef",
    {"dataSource": ClientCreateDataSourceResponsedataSourceTypeDef},
    total=False,
)


class ClientCreateDataSourceResponseTypeDef(_ClientCreateDataSourceResponseTypeDef):
    """
    - *(dict) --*

      - **dataSource** *(dict) --*

        The ``DataSource`` object.
        - **dataSourceArn** *(string) --*

          The data source ARN.
    """


_ClientCreateFunctionResponsefunctionConfigurationTypeDef = TypedDict(
    "_ClientCreateFunctionResponsefunctionConfigurationTypeDef",
    {
        "functionId": str,
        "functionArn": str,
        "name": str,
        "description": str,
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
    },
    total=False,
)


class ClientCreateFunctionResponsefunctionConfigurationTypeDef(
    _ClientCreateFunctionResponsefunctionConfigurationTypeDef
):
    """
    - **functionConfiguration** *(dict) --*

      The ``Function`` object.
      - **functionId** *(string) --*

        A unique ID representing the ``Function`` object.
    """


_ClientCreateFunctionResponseTypeDef = TypedDict(
    "_ClientCreateFunctionResponseTypeDef",
    {"functionConfiguration": ClientCreateFunctionResponsefunctionConfigurationTypeDef},
    total=False,
)


class ClientCreateFunctionResponseTypeDef(_ClientCreateFunctionResponseTypeDef):
    """
    - *(dict) --*

      - **functionConfiguration** *(dict) --*

        The ``Function`` object.
        - **functionId** *(string) --*

          A unique ID representing the ``Function`` object.
    """


_ClientCreateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "_ClientCreateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientCreateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef(
    _ClientCreateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef
):
    pass


_ClientCreateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "_ClientCreateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)


class ClientCreateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef(
    _ClientCreateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef
):
    pass


_ClientCreateGraphqlApiAdditionalAuthenticationProvidersTypeDef = TypedDict(
    "_ClientCreateGraphqlApiAdditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientCreateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientCreateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)


class ClientCreateGraphqlApiAdditionalAuthenticationProvidersTypeDef(
    _ClientCreateGraphqlApiAdditionalAuthenticationProvidersTypeDef
):
    """
    - *(dict) --*

      Describes an additional authentication provider.
      - **authenticationType** *(string) --*

        The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.
    """


_RequiredClientCreateGraphqlApiLogConfigTypeDef = TypedDict(
    "_RequiredClientCreateGraphqlApiLogConfigTypeDef",
    {"fieldLogLevel": Literal["NONE", "ERROR", "ALL"]},
)
_OptionalClientCreateGraphqlApiLogConfigTypeDef = TypedDict(
    "_OptionalClientCreateGraphqlApiLogConfigTypeDef",
    {"cloudWatchLogsRoleArn": str, "excludeVerboseContent": bool},
    total=False,
)


class ClientCreateGraphqlApiLogConfigTypeDef(
    _RequiredClientCreateGraphqlApiLogConfigTypeDef, _OptionalClientCreateGraphqlApiLogConfigTypeDef
):
    """
    The Amazon CloudWatch Logs configuration.
    - **fieldLogLevel** *(string) --***[REQUIRED]**

      The field logging level. Values can be NONE, ERROR, or ALL.
      * **NONE** : No field-level logs are captured.
      * **ERROR** : Logs the following information only for the fields that are in error:

        * The error section in the server response.
        * Field-level errors.
        * The generated request/response functions that got resolved for error fields.
    """


_RequiredClientCreateGraphqlApiOpenIDConnectConfigTypeDef = TypedDict(
    "_RequiredClientCreateGraphqlApiOpenIDConnectConfigTypeDef", {"issuer": str}
)
_OptionalClientCreateGraphqlApiOpenIDConnectConfigTypeDef = TypedDict(
    "_OptionalClientCreateGraphqlApiOpenIDConnectConfigTypeDef",
    {"clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientCreateGraphqlApiOpenIDConnectConfigTypeDef(
    _RequiredClientCreateGraphqlApiOpenIDConnectConfigTypeDef,
    _OptionalClientCreateGraphqlApiOpenIDConnectConfigTypeDef,
):
    """
    The OpenID Connect configuration.
    - **issuer** *(string) --***[REQUIRED]**

      The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly
      match the value of ``iss`` in the ID token.
    """


_ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "_ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef(
    _ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef
):
    pass


_ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "_ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)


class ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef(
    _ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef
):
    pass


_ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef = TypedDict(
    "_ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)


class ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef(
    _ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef
):
    pass


_ClientCreateGraphqlApiResponsegraphqlApilogConfigTypeDef = TypedDict(
    "_ClientCreateGraphqlApiResponsegraphqlApilogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)


class ClientCreateGraphqlApiResponsegraphqlApilogConfigTypeDef(
    _ClientCreateGraphqlApiResponsegraphqlApilogConfigTypeDef
):
    pass


_ClientCreateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef = TypedDict(
    "_ClientCreateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientCreateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef(
    _ClientCreateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef
):
    pass


_ClientCreateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef = TypedDict(
    "_ClientCreateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)


class ClientCreateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef(
    _ClientCreateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef
):
    pass


_ClientCreateGraphqlApiResponsegraphqlApiTypeDef = TypedDict(
    "_ClientCreateGraphqlApiResponsegraphqlApiTypeDef",
    {
        "name": str,
        "apiId": str,
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "logConfig": ClientCreateGraphqlApiResponsegraphqlApilogConfigTypeDef,
        "userPoolConfig": ClientCreateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef,
        "openIDConnectConfig": ClientCreateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef,
        "arn": str,
        "uris": Dict[str, str],
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List[
            ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef
        ],
    },
    total=False,
)


class ClientCreateGraphqlApiResponsegraphqlApiTypeDef(
    _ClientCreateGraphqlApiResponsegraphqlApiTypeDef
):
    """
    - **graphqlApi** *(dict) --*

      The ``GraphqlApi`` .
      - **name** *(string) --*

        The API name.
    """


_ClientCreateGraphqlApiResponseTypeDef = TypedDict(
    "_ClientCreateGraphqlApiResponseTypeDef",
    {"graphqlApi": ClientCreateGraphqlApiResponsegraphqlApiTypeDef},
    total=False,
)


class ClientCreateGraphqlApiResponseTypeDef(_ClientCreateGraphqlApiResponseTypeDef):
    """
    - *(dict) --*

      - **graphqlApi** *(dict) --*

        The ``GraphqlApi`` .
        - **name** *(string) --*

          The API name.
    """


_RequiredClientCreateGraphqlApiUserPoolConfigTypeDef = TypedDict(
    "_RequiredClientCreateGraphqlApiUserPoolConfigTypeDef", {"userPoolId": str}
)
_OptionalClientCreateGraphqlApiUserPoolConfigTypeDef = TypedDict(
    "_OptionalClientCreateGraphqlApiUserPoolConfigTypeDef",
    {"awsRegion": str, "defaultAction": Literal["ALLOW", "DENY"], "appIdClientRegex": str},
    total=False,
)


class ClientCreateGraphqlApiUserPoolConfigTypeDef(
    _RequiredClientCreateGraphqlApiUserPoolConfigTypeDef,
    _OptionalClientCreateGraphqlApiUserPoolConfigTypeDef,
):
    """
    The Amazon Cognito user pool configuration.
    - **userPoolId** *(string) --***[REQUIRED]**

      The user pool ID.
    """


_ClientCreateResolverCachingConfigTypeDef = TypedDict(
    "_ClientCreateResolverCachingConfigTypeDef", {"ttl": int, "cachingKeys": List[str]}, total=False
)


class ClientCreateResolverCachingConfigTypeDef(_ClientCreateResolverCachingConfigTypeDef):
    """
    The caching configuration for the resolver.
    - **ttl** *(integer) --*

      The TTL in seconds for a resolver that has caching enabled.
      Valid values are between 1 and 3600 seconds.
    """


_ClientCreateResolverPipelineConfigTypeDef = TypedDict(
    "_ClientCreateResolverPipelineConfigTypeDef", {"functions": List[str]}, total=False
)


class ClientCreateResolverPipelineConfigTypeDef(_ClientCreateResolverPipelineConfigTypeDef):
    """
    The ``PipelineConfig`` .
    - **functions** *(list) --*

      A list of ``Function`` objects.
      - *(string) --*
    """


_ClientCreateResolverResponseresolvercachingConfigTypeDef = TypedDict(
    "_ClientCreateResolverResponseresolvercachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)


class ClientCreateResolverResponseresolvercachingConfigTypeDef(
    _ClientCreateResolverResponseresolvercachingConfigTypeDef
):
    pass


_ClientCreateResolverResponseresolverpipelineConfigTypeDef = TypedDict(
    "_ClientCreateResolverResponseresolverpipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)


class ClientCreateResolverResponseresolverpipelineConfigTypeDef(
    _ClientCreateResolverResponseresolverpipelineConfigTypeDef
):
    pass


_ClientCreateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "_ClientCreateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)


class ClientCreateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef(
    _ClientCreateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef
):
    pass


_ClientCreateResolverResponseresolversyncConfigTypeDef = TypedDict(
    "_ClientCreateResolverResponseresolversyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientCreateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)


class ClientCreateResolverResponseresolversyncConfigTypeDef(
    _ClientCreateResolverResponseresolversyncConfigTypeDef
):
    pass


_ClientCreateResolverResponseresolverTypeDef = TypedDict(
    "_ClientCreateResolverResponseresolverTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": Literal["UNIT", "PIPELINE"],
        "pipelineConfig": ClientCreateResolverResponseresolverpipelineConfigTypeDef,
        "syncConfig": ClientCreateResolverResponseresolversyncConfigTypeDef,
        "cachingConfig": ClientCreateResolverResponseresolvercachingConfigTypeDef,
    },
    total=False,
)


class ClientCreateResolverResponseresolverTypeDef(_ClientCreateResolverResponseresolverTypeDef):
    """
    - **resolver** *(dict) --*

      The ``Resolver`` object.
      - **typeName** *(string) --*

        The resolver type name.
    """


_ClientCreateResolverResponseTypeDef = TypedDict(
    "_ClientCreateResolverResponseTypeDef",
    {"resolver": ClientCreateResolverResponseresolverTypeDef},
    total=False,
)


class ClientCreateResolverResponseTypeDef(_ClientCreateResolverResponseTypeDef):
    """
    - *(dict) --*

      - **resolver** *(dict) --*

        The ``Resolver`` object.
        - **typeName** *(string) --*

          The resolver type name.
    """


_ClientCreateResolverSyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "_ClientCreateResolverSyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)


class ClientCreateResolverSyncConfiglambdaConflictHandlerConfigTypeDef(
    _ClientCreateResolverSyncConfiglambdaConflictHandlerConfigTypeDef
):
    pass


_ClientCreateResolverSyncConfigTypeDef = TypedDict(
    "_ClientCreateResolverSyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientCreateResolverSyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)


class ClientCreateResolverSyncConfigTypeDef(_ClientCreateResolverSyncConfigTypeDef):
    """
    The ``SyncConfig`` for a resolver attached to a versioned datasource.
    - **conflictHandler** *(string) --*

      The Conflict Resolution strategy to perform in the event of a conflict.
      * **OPTIMISTIC_CONCURRENCY** : Resolve conflicts by rejecting mutations when versions do not
      match the latest version at the server.
      * **AUTOMERGE** : Resolve conflicts with the Automerge conflict resolution strategy.
      * **LAMBDA** : Resolve conflicts with a Lambda function supplied in the
      LambdaConflictHandlerConfig.
    """


_ClientCreateTypeResponsetypeTypeDef = TypedDict(
    "_ClientCreateTypeResponsetypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)


class ClientCreateTypeResponsetypeTypeDef(_ClientCreateTypeResponsetypeTypeDef):
    """
    - **type** *(dict) --*

      The ``Type`` object.
      - **name** *(string) --*

        The type name.
    """


_ClientCreateTypeResponseTypeDef = TypedDict(
    "_ClientCreateTypeResponseTypeDef", {"type": ClientCreateTypeResponsetypeTypeDef}, total=False
)


class ClientCreateTypeResponseTypeDef(_ClientCreateTypeResponseTypeDef):
    """
    - *(dict) --*

      - **type** *(dict) --*

        The ``Type`` object.
        - **name** *(string) --*

          The type name.
    """


_ClientGetApiCacheResponseapiCacheTypeDef = TypedDict(
    "_ClientGetApiCacheResponseapiCacheTypeDef",
    {
        "ttl": int,
        "apiCachingBehavior": Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"],
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
        "type": Literal[
            "T2_SMALL",
            "T2_MEDIUM",
            "R4_LARGE",
            "R4_XLARGE",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
        ],
        "status": Literal["AVAILABLE", "CREATING", "DELETING", "MODIFYING", "FAILED"],
    },
    total=False,
)


class ClientGetApiCacheResponseapiCacheTypeDef(_ClientGetApiCacheResponseapiCacheTypeDef):
    """
    - **apiCache** *(dict) --*

      - **ttl** *(integer) --*

        TTL in seconds for cache entries.
        Valid values are between 1 and 3600 seconds.
    """


_ClientGetApiCacheResponseTypeDef = TypedDict(
    "_ClientGetApiCacheResponseTypeDef",
    {"apiCache": ClientGetApiCacheResponseapiCacheTypeDef},
    total=False,
)


class ClientGetApiCacheResponseTypeDef(_ClientGetApiCacheResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetApiCache`` operation.
      - **apiCache** *(dict) --*

        - **ttl** *(integer) --*

          TTL in seconds for cache entries.
          Valid values are between 1 and 3600 seconds.
    """


_ClientGetDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)


class ClientGetDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef(
    _ClientGetDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef
):
    pass


_ClientGetDataSourceResponsedataSourcedynamodbConfigTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourcedynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientGetDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)


class ClientGetDataSourceResponsedataSourcedynamodbConfigTypeDef(
    _ClientGetDataSourceResponsedataSourcedynamodbConfigTypeDef
):
    pass


_ClientGetDataSourceResponsedataSourceelasticsearchConfigTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourceelasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)


class ClientGetDataSourceResponsedataSourceelasticsearchConfigTypeDef(
    _ClientGetDataSourceResponsedataSourceelasticsearchConfigTypeDef
):
    pass


_ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)


class ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef(
    _ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef
):
    pass


_ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)


class ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef(
    _ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef
):
    pass


_ClientGetDataSourceResponsedataSourcehttpConfigTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourcehttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)


class ClientGetDataSourceResponsedataSourcehttpConfigTypeDef(
    _ClientGetDataSourceResponsedataSourcehttpConfigTypeDef
):
    pass


_ClientGetDataSourceResponsedataSourcelambdaConfigTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourcelambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)


class ClientGetDataSourceResponsedataSourcelambdaConfigTypeDef(
    _ClientGetDataSourceResponsedataSourcelambdaConfigTypeDef
):
    pass


_ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)


class ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef(
    _ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef
):
    pass


_ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)


class ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef(
    _ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef
):
    pass


_ClientGetDataSourceResponsedataSourceTypeDef = TypedDict(
    "_ClientGetDataSourceResponsedataSourceTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        "serviceRoleArn": str,
        "dynamodbConfig": ClientGetDataSourceResponsedataSourcedynamodbConfigTypeDef,
        "lambdaConfig": ClientGetDataSourceResponsedataSourcelambdaConfigTypeDef,
        "elasticsearchConfig": ClientGetDataSourceResponsedataSourceelasticsearchConfigTypeDef,
        "httpConfig": ClientGetDataSourceResponsedataSourcehttpConfigTypeDef,
        "relationalDatabaseConfig": ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef,
    },
    total=False,
)


class ClientGetDataSourceResponsedataSourceTypeDef(_ClientGetDataSourceResponsedataSourceTypeDef):
    """
    - **dataSource** *(dict) --*

      The ``DataSource`` object.
      - **dataSourceArn** *(string) --*

        The data source ARN.
    """


_ClientGetDataSourceResponseTypeDef = TypedDict(
    "_ClientGetDataSourceResponseTypeDef",
    {"dataSource": ClientGetDataSourceResponsedataSourceTypeDef},
    total=False,
)


class ClientGetDataSourceResponseTypeDef(_ClientGetDataSourceResponseTypeDef):
    """
    - *(dict) --*

      - **dataSource** *(dict) --*

        The ``DataSource`` object.
        - **dataSourceArn** *(string) --*

          The data source ARN.
    """


_ClientGetFunctionResponsefunctionConfigurationTypeDef = TypedDict(
    "_ClientGetFunctionResponsefunctionConfigurationTypeDef",
    {
        "functionId": str,
        "functionArn": str,
        "name": str,
        "description": str,
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
    },
    total=False,
)


class ClientGetFunctionResponsefunctionConfigurationTypeDef(
    _ClientGetFunctionResponsefunctionConfigurationTypeDef
):
    """
    - **functionConfiguration** *(dict) --*

      The ``Function`` object.
      - **functionId** *(string) --*

        A unique ID representing the ``Function`` object.
    """


_ClientGetFunctionResponseTypeDef = TypedDict(
    "_ClientGetFunctionResponseTypeDef",
    {"functionConfiguration": ClientGetFunctionResponsefunctionConfigurationTypeDef},
    total=False,
)


class ClientGetFunctionResponseTypeDef(_ClientGetFunctionResponseTypeDef):
    """
    - *(dict) --*

      - **functionConfiguration** *(dict) --*

        The ``Function`` object.
        - **functionId** *(string) --*

          A unique ID representing the ``Function`` object.
    """


_ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "_ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef(
    _ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef
):
    pass


_ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "_ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)


class ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef(
    _ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef
):
    pass


_ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef = TypedDict(
    "_ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)


class ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef(
    _ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef
):
    pass


_ClientGetGraphqlApiResponsegraphqlApilogConfigTypeDef = TypedDict(
    "_ClientGetGraphqlApiResponsegraphqlApilogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)


class ClientGetGraphqlApiResponsegraphqlApilogConfigTypeDef(
    _ClientGetGraphqlApiResponsegraphqlApilogConfigTypeDef
):
    pass


_ClientGetGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef = TypedDict(
    "_ClientGetGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientGetGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef(
    _ClientGetGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef
):
    pass


_ClientGetGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef = TypedDict(
    "_ClientGetGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)


class ClientGetGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef(
    _ClientGetGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef
):
    pass


_ClientGetGraphqlApiResponsegraphqlApiTypeDef = TypedDict(
    "_ClientGetGraphqlApiResponsegraphqlApiTypeDef",
    {
        "name": str,
        "apiId": str,
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "logConfig": ClientGetGraphqlApiResponsegraphqlApilogConfigTypeDef,
        "userPoolConfig": ClientGetGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef,
        "openIDConnectConfig": ClientGetGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef,
        "arn": str,
        "uris": Dict[str, str],
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List[
            ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef
        ],
    },
    total=False,
)


class ClientGetGraphqlApiResponsegraphqlApiTypeDef(_ClientGetGraphqlApiResponsegraphqlApiTypeDef):
    """
    - **graphqlApi** *(dict) --*

      The ``GraphqlApi`` object.
      - **name** *(string) --*

        The API name.
    """


_ClientGetGraphqlApiResponseTypeDef = TypedDict(
    "_ClientGetGraphqlApiResponseTypeDef",
    {"graphqlApi": ClientGetGraphqlApiResponsegraphqlApiTypeDef},
    total=False,
)


class ClientGetGraphqlApiResponseTypeDef(_ClientGetGraphqlApiResponseTypeDef):
    """
    - *(dict) --*

      - **graphqlApi** *(dict) --*

        The ``GraphqlApi`` object.
        - **name** *(string) --*

          The API name.
    """


_ClientGetIntrospectionSchemaResponseTypeDef = TypedDict(
    "_ClientGetIntrospectionSchemaResponseTypeDef", {"schema": StreamingBody}, total=False
)


class ClientGetIntrospectionSchemaResponseTypeDef(_ClientGetIntrospectionSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **schema** (:class:`.StreamingBody`) --

        The schema, in GraphQL Schema Definition Language (SDL) format.
        For more information, see the `GraphQL SDL documentation
        <http://graphql.org/learn/schema/>`__ .
    """


_ClientGetResolverResponseresolvercachingConfigTypeDef = TypedDict(
    "_ClientGetResolverResponseresolvercachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)


class ClientGetResolverResponseresolvercachingConfigTypeDef(
    _ClientGetResolverResponseresolvercachingConfigTypeDef
):
    pass


_ClientGetResolverResponseresolverpipelineConfigTypeDef = TypedDict(
    "_ClientGetResolverResponseresolverpipelineConfigTypeDef", {"functions": List[str]}, total=False
)


class ClientGetResolverResponseresolverpipelineConfigTypeDef(
    _ClientGetResolverResponseresolverpipelineConfigTypeDef
):
    pass


_ClientGetResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "_ClientGetResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)


class ClientGetResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef(
    _ClientGetResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef
):
    pass


_ClientGetResolverResponseresolversyncConfigTypeDef = TypedDict(
    "_ClientGetResolverResponseresolversyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientGetResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)


class ClientGetResolverResponseresolversyncConfigTypeDef(
    _ClientGetResolverResponseresolversyncConfigTypeDef
):
    pass


_ClientGetResolverResponseresolverTypeDef = TypedDict(
    "_ClientGetResolverResponseresolverTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": Literal["UNIT", "PIPELINE"],
        "pipelineConfig": ClientGetResolverResponseresolverpipelineConfigTypeDef,
        "syncConfig": ClientGetResolverResponseresolversyncConfigTypeDef,
        "cachingConfig": ClientGetResolverResponseresolvercachingConfigTypeDef,
    },
    total=False,
)


class ClientGetResolverResponseresolverTypeDef(_ClientGetResolverResponseresolverTypeDef):
    """
    - **resolver** *(dict) --*

      The ``Resolver`` object.
      - **typeName** *(string) --*

        The resolver type name.
    """


_ClientGetResolverResponseTypeDef = TypedDict(
    "_ClientGetResolverResponseTypeDef",
    {"resolver": ClientGetResolverResponseresolverTypeDef},
    total=False,
)


class ClientGetResolverResponseTypeDef(_ClientGetResolverResponseTypeDef):
    """
    - *(dict) --*

      - **resolver** *(dict) --*

        The ``Resolver`` object.
        - **typeName** *(string) --*

          The resolver type name.
    """


_ClientGetSchemaCreationStatusResponseTypeDef = TypedDict(
    "_ClientGetSchemaCreationStatusResponseTypeDef",
    {
        "status": Literal[
            "PROCESSING", "ACTIVE", "DELETING", "FAILED", "SUCCESS", "NOT_APPLICABLE"
        ],
        "details": str,
    },
    total=False,
)


class ClientGetSchemaCreationStatusResponseTypeDef(_ClientGetSchemaCreationStatusResponseTypeDef):
    """
    - *(dict) --*

      - **status** *(string) --*

        The current state of the schema (PROCESSING, FAILED, SUCCESS, or NOT_APPLICABLE). When the
        schema is in the ACTIVE state, you can add data.
    """


_ClientGetTypeResponsetypeTypeDef = TypedDict(
    "_ClientGetTypeResponsetypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)


class ClientGetTypeResponsetypeTypeDef(_ClientGetTypeResponsetypeTypeDef):
    """
    - **type** *(dict) --*

      The ``Type`` object.
      - **name** *(string) --*

        The type name.
    """


_ClientGetTypeResponseTypeDef = TypedDict(
    "_ClientGetTypeResponseTypeDef", {"type": ClientGetTypeResponsetypeTypeDef}, total=False
)


class ClientGetTypeResponseTypeDef(_ClientGetTypeResponseTypeDef):
    """
    - *(dict) --*

      - **type** *(dict) --*

        The ``Type`` object.
        - **name** *(string) --*

          The type name.
    """


_ClientListApiKeysResponseapiKeysTypeDef = TypedDict(
    "_ClientListApiKeysResponseapiKeysTypeDef",
    {"id": str, "description": str, "expires": int},
    total=False,
)


class ClientListApiKeysResponseapiKeysTypeDef(_ClientListApiKeysResponseapiKeysTypeDef):
    """
    - *(dict) --*

      Describes an API key.
      Customers invoke AWS AppSync GraphQL API operations with API keys as an identity mechanism.
      There are two key versions:

        **da1** : This version was introduced at launch in November 2017. These keys always expire
        after 7 days. Key expiration is managed by Amazon DynamoDB TTL. The keys ceased to be valid
        after February 21, 2018 and should not be used after that date.
    """


_ClientListApiKeysResponseTypeDef = TypedDict(
    "_ClientListApiKeysResponseTypeDef",
    {"apiKeys": List[ClientListApiKeysResponseapiKeysTypeDef], "nextToken": str},
    total=False,
)


class ClientListApiKeysResponseTypeDef(_ClientListApiKeysResponseTypeDef):
    """
    - *(dict) --*

      - **apiKeys** *(list) --*

        The ``ApiKey`` objects.
        - *(dict) --*

          Describes an API key.
          Customers invoke AWS AppSync GraphQL API operations with API keys as an identity
          mechanism. There are two key versions:

            **da1** : This version was introduced at launch in November 2017. These keys always
            expire after 7 days. Key expiration is managed by Amazon DynamoDB TTL. The keys ceased
            to be valid after February 21, 2018 and should not be used after that date.
    """


_ClientListDataSourcesResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)


class ClientListDataSourcesResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef(
    _ClientListDataSourcesResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef
):
    pass


_ClientListDataSourcesResponsedataSourcesdynamodbConfigTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourcesdynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientListDataSourcesResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)


class ClientListDataSourcesResponsedataSourcesdynamodbConfigTypeDef(
    _ClientListDataSourcesResponsedataSourcesdynamodbConfigTypeDef
):
    pass


_ClientListDataSourcesResponsedataSourceselasticsearchConfigTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourceselasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)


class ClientListDataSourcesResponsedataSourceselasticsearchConfigTypeDef(
    _ClientListDataSourcesResponsedataSourceselasticsearchConfigTypeDef
):
    pass


_ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)


class ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef(
    _ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef
):
    pass


_ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)


class ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigTypeDef(
    _ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigTypeDef
):
    pass


_ClientListDataSourcesResponsedataSourceshttpConfigTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourceshttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)


class ClientListDataSourcesResponsedataSourceshttpConfigTypeDef(
    _ClientListDataSourcesResponsedataSourceshttpConfigTypeDef
):
    pass


_ClientListDataSourcesResponsedataSourceslambdaConfigTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourceslambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)


class ClientListDataSourcesResponsedataSourceslambdaConfigTypeDef(
    _ClientListDataSourcesResponsedataSourceslambdaConfigTypeDef
):
    pass


_ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)


class ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef(
    _ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef
):
    pass


_ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)


class ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigTypeDef(
    _ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigTypeDef
):
    pass


_ClientListDataSourcesResponsedataSourcesTypeDef = TypedDict(
    "_ClientListDataSourcesResponsedataSourcesTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        "serviceRoleArn": str,
        "dynamodbConfig": ClientListDataSourcesResponsedataSourcesdynamodbConfigTypeDef,
        "lambdaConfig": ClientListDataSourcesResponsedataSourceslambdaConfigTypeDef,
        "elasticsearchConfig": ClientListDataSourcesResponsedataSourceselasticsearchConfigTypeDef,
        "httpConfig": ClientListDataSourcesResponsedataSourceshttpConfigTypeDef,
        "relationalDatabaseConfig": ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigTypeDef,
    },
    total=False,
)


class ClientListDataSourcesResponsedataSourcesTypeDef(
    _ClientListDataSourcesResponsedataSourcesTypeDef
):
    """
    - *(dict) --*

      Describes a data source.
      - **dataSourceArn** *(string) --*

        The data source ARN.
    """


_ClientListDataSourcesResponseTypeDef = TypedDict(
    "_ClientListDataSourcesResponseTypeDef",
    {"dataSources": List[ClientListDataSourcesResponsedataSourcesTypeDef], "nextToken": str},
    total=False,
)


class ClientListDataSourcesResponseTypeDef(_ClientListDataSourcesResponseTypeDef):
    """
    - *(dict) --*

      - **dataSources** *(list) --*

        The ``DataSource`` objects.
        - *(dict) --*

          Describes a data source.
          - **dataSourceArn** *(string) --*

            The data source ARN.
    """


_ClientListFunctionsResponsefunctionsTypeDef = TypedDict(
    "_ClientListFunctionsResponsefunctionsTypeDef",
    {
        "functionId": str,
        "functionArn": str,
        "name": str,
        "description": str,
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
    },
    total=False,
)


class ClientListFunctionsResponsefunctionsTypeDef(_ClientListFunctionsResponsefunctionsTypeDef):
    """
    - *(dict) --*

      A function is a reusable entity. Multiple functions can be used to compose the resolver logic.
      - **functionId** *(string) --*

        A unique ID representing the ``Function`` object.
    """


_ClientListFunctionsResponseTypeDef = TypedDict(
    "_ClientListFunctionsResponseTypeDef",
    {"functions": List[ClientListFunctionsResponsefunctionsTypeDef], "nextToken": str},
    total=False,
)


class ClientListFunctionsResponseTypeDef(_ClientListFunctionsResponseTypeDef):
    """
    - *(dict) --*

      - **functions** *(list) --*

        A list of ``Function`` objects.
        - *(dict) --*

          A function is a reusable entity. Multiple functions can be used to compose the resolver
          logic.
          - **functionId** *(string) --*

            A unique ID representing the ``Function`` object.
    """


_ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "_ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef(
    _ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef
):
    pass


_ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "_ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)


class ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef(
    _ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef
):
    pass


_ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersTypeDef = TypedDict(
    "_ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)


class ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersTypeDef(
    _ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersTypeDef
):
    pass


_ClientListGraphqlApisResponsegraphqlApislogConfigTypeDef = TypedDict(
    "_ClientListGraphqlApisResponsegraphqlApislogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)


class ClientListGraphqlApisResponsegraphqlApislogConfigTypeDef(
    _ClientListGraphqlApisResponsegraphqlApislogConfigTypeDef
):
    pass


_ClientListGraphqlApisResponsegraphqlApisopenIDConnectConfigTypeDef = TypedDict(
    "_ClientListGraphqlApisResponsegraphqlApisopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientListGraphqlApisResponsegraphqlApisopenIDConnectConfigTypeDef(
    _ClientListGraphqlApisResponsegraphqlApisopenIDConnectConfigTypeDef
):
    pass


_ClientListGraphqlApisResponsegraphqlApisuserPoolConfigTypeDef = TypedDict(
    "_ClientListGraphqlApisResponsegraphqlApisuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)


class ClientListGraphqlApisResponsegraphqlApisuserPoolConfigTypeDef(
    _ClientListGraphqlApisResponsegraphqlApisuserPoolConfigTypeDef
):
    pass


_ClientListGraphqlApisResponsegraphqlApisTypeDef = TypedDict(
    "_ClientListGraphqlApisResponsegraphqlApisTypeDef",
    {
        "name": str,
        "apiId": str,
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "logConfig": ClientListGraphqlApisResponsegraphqlApislogConfigTypeDef,
        "userPoolConfig": ClientListGraphqlApisResponsegraphqlApisuserPoolConfigTypeDef,
        "openIDConnectConfig": ClientListGraphqlApisResponsegraphqlApisopenIDConnectConfigTypeDef,
        "arn": str,
        "uris": Dict[str, str],
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List[
            ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersTypeDef
        ],
    },
    total=False,
)


class ClientListGraphqlApisResponsegraphqlApisTypeDef(
    _ClientListGraphqlApisResponsegraphqlApisTypeDef
):
    """
    - *(dict) --*

      Describes a GraphQL API.
      - **name** *(string) --*

        The API name.
    """


_ClientListGraphqlApisResponseTypeDef = TypedDict(
    "_ClientListGraphqlApisResponseTypeDef",
    {"graphqlApis": List[ClientListGraphqlApisResponsegraphqlApisTypeDef], "nextToken": str},
    total=False,
)


class ClientListGraphqlApisResponseTypeDef(_ClientListGraphqlApisResponseTypeDef):
    """
    - *(dict) --*

      - **graphqlApis** *(list) --*

        The ``GraphqlApi`` objects.
        - *(dict) --*

          Describes a GraphQL API.
          - **name** *(string) --*

            The API name.
    """


_ClientListResolversByFunctionResponseresolverscachingConfigTypeDef = TypedDict(
    "_ClientListResolversByFunctionResponseresolverscachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)


class ClientListResolversByFunctionResponseresolverscachingConfigTypeDef(
    _ClientListResolversByFunctionResponseresolverscachingConfigTypeDef
):
    pass


_ClientListResolversByFunctionResponseresolverspipelineConfigTypeDef = TypedDict(
    "_ClientListResolversByFunctionResponseresolverspipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)


class ClientListResolversByFunctionResponseresolverspipelineConfigTypeDef(
    _ClientListResolversByFunctionResponseresolverspipelineConfigTypeDef
):
    pass


_ClientListResolversByFunctionResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "_ClientListResolversByFunctionResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)


class ClientListResolversByFunctionResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef(
    _ClientListResolversByFunctionResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef
):
    pass


_ClientListResolversByFunctionResponseresolverssyncConfigTypeDef = TypedDict(
    "_ClientListResolversByFunctionResponseresolverssyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientListResolversByFunctionResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)


class ClientListResolversByFunctionResponseresolverssyncConfigTypeDef(
    _ClientListResolversByFunctionResponseresolverssyncConfigTypeDef
):
    pass


_ClientListResolversByFunctionResponseresolversTypeDef = TypedDict(
    "_ClientListResolversByFunctionResponseresolversTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": Literal["UNIT", "PIPELINE"],
        "pipelineConfig": ClientListResolversByFunctionResponseresolverspipelineConfigTypeDef,
        "syncConfig": ClientListResolversByFunctionResponseresolverssyncConfigTypeDef,
        "cachingConfig": ClientListResolversByFunctionResponseresolverscachingConfigTypeDef,
    },
    total=False,
)


class ClientListResolversByFunctionResponseresolversTypeDef(
    _ClientListResolversByFunctionResponseresolversTypeDef
):
    """
    - *(dict) --*

      Describes a resolver.
      - **typeName** *(string) --*

        The resolver type name.
    """


_ClientListResolversByFunctionResponseTypeDef = TypedDict(
    "_ClientListResolversByFunctionResponseTypeDef",
    {"resolvers": List[ClientListResolversByFunctionResponseresolversTypeDef], "nextToken": str},
    total=False,
)


class ClientListResolversByFunctionResponseTypeDef(_ClientListResolversByFunctionResponseTypeDef):
    """
    - *(dict) --*

      - **resolvers** *(list) --*

        The list of resolvers.
        - *(dict) --*

          Describes a resolver.
          - **typeName** *(string) --*

            The resolver type name.
    """


_ClientListResolversResponseresolverscachingConfigTypeDef = TypedDict(
    "_ClientListResolversResponseresolverscachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)


class ClientListResolversResponseresolverscachingConfigTypeDef(
    _ClientListResolversResponseresolverscachingConfigTypeDef
):
    pass


_ClientListResolversResponseresolverspipelineConfigTypeDef = TypedDict(
    "_ClientListResolversResponseresolverspipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)


class ClientListResolversResponseresolverspipelineConfigTypeDef(
    _ClientListResolversResponseresolverspipelineConfigTypeDef
):
    pass


_ClientListResolversResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "_ClientListResolversResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)


class ClientListResolversResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef(
    _ClientListResolversResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef
):
    pass


_ClientListResolversResponseresolverssyncConfigTypeDef = TypedDict(
    "_ClientListResolversResponseresolverssyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientListResolversResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)


class ClientListResolversResponseresolverssyncConfigTypeDef(
    _ClientListResolversResponseresolverssyncConfigTypeDef
):
    pass


_ClientListResolversResponseresolversTypeDef = TypedDict(
    "_ClientListResolversResponseresolversTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": Literal["UNIT", "PIPELINE"],
        "pipelineConfig": ClientListResolversResponseresolverspipelineConfigTypeDef,
        "syncConfig": ClientListResolversResponseresolverssyncConfigTypeDef,
        "cachingConfig": ClientListResolversResponseresolverscachingConfigTypeDef,
    },
    total=False,
)


class ClientListResolversResponseresolversTypeDef(_ClientListResolversResponseresolversTypeDef):
    """
    - *(dict) --*

      Describes a resolver.
      - **typeName** *(string) --*

        The resolver type name.
    """


_ClientListResolversResponseTypeDef = TypedDict(
    "_ClientListResolversResponseTypeDef",
    {"resolvers": List[ClientListResolversResponseresolversTypeDef], "nextToken": str},
    total=False,
)


class ClientListResolversResponseTypeDef(_ClientListResolversResponseTypeDef):
    """
    - *(dict) --*

      - **resolvers** *(list) --*

        The ``Resolver`` objects.
        - *(dict) --*

          Describes a resolver.
          - **typeName** *(string) --*

            The resolver type name.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        A ``TagMap`` object.
        - *(string) --*

          The key for the tag.
          - *(string) --*

            The value for the tag.
    """


_ClientListTypesResponsetypesTypeDef = TypedDict(
    "_ClientListTypesResponsetypesTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)


class ClientListTypesResponsetypesTypeDef(_ClientListTypesResponsetypesTypeDef):
    """
    - *(dict) --*

      Describes a type.
      - **name** *(string) --*

        The type name.
    """


_ClientListTypesResponseTypeDef = TypedDict(
    "_ClientListTypesResponseTypeDef",
    {"types": List[ClientListTypesResponsetypesTypeDef], "nextToken": str},
    total=False,
)


class ClientListTypesResponseTypeDef(_ClientListTypesResponseTypeDef):
    """
    - *(dict) --*

      - **types** *(list) --*

        The ``Type`` objects.
        - *(dict) --*

          Describes a type.
          - **name** *(string) --*

            The type name.
    """


_ClientStartSchemaCreationResponseTypeDef = TypedDict(
    "_ClientStartSchemaCreationResponseTypeDef",
    {"status": Literal["PROCESSING", "ACTIVE", "DELETING", "FAILED", "SUCCESS", "NOT_APPLICABLE"]},
    total=False,
)


class ClientStartSchemaCreationResponseTypeDef(_ClientStartSchemaCreationResponseTypeDef):
    """
    - *(dict) --*

      - **status** *(string) --*

        The current state of the schema (PROCESSING, FAILED, SUCCESS, or NOT_APPLICABLE). When the
        schema is in the ACTIVE state, you can add data.
    """


_ClientUpdateApiCacheResponseapiCacheTypeDef = TypedDict(
    "_ClientUpdateApiCacheResponseapiCacheTypeDef",
    {
        "ttl": int,
        "apiCachingBehavior": Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"],
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
        "type": Literal[
            "T2_SMALL",
            "T2_MEDIUM",
            "R4_LARGE",
            "R4_XLARGE",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
        ],
        "status": Literal["AVAILABLE", "CREATING", "DELETING", "MODIFYING", "FAILED"],
    },
    total=False,
)


class ClientUpdateApiCacheResponseapiCacheTypeDef(_ClientUpdateApiCacheResponseapiCacheTypeDef):
    """
    - **apiCache** *(dict) --*

      The ``ApiCache`` object.
      - **ttl** *(integer) --*

        TTL in seconds for cache entries.
        Valid values are between 1 and 3600 seconds.
    """


_ClientUpdateApiCacheResponseTypeDef = TypedDict(
    "_ClientUpdateApiCacheResponseTypeDef",
    {"apiCache": ClientUpdateApiCacheResponseapiCacheTypeDef},
    total=False,
)


class ClientUpdateApiCacheResponseTypeDef(_ClientUpdateApiCacheResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``UpdateApiCache`` operation.
      - **apiCache** *(dict) --*

        The ``ApiCache`` object.
        - **ttl** *(integer) --*

          TTL in seconds for cache entries.
          Valid values are between 1 and 3600 seconds.
    """


_ClientUpdateApiKeyResponseapiKeyTypeDef = TypedDict(
    "_ClientUpdateApiKeyResponseapiKeyTypeDef",
    {"id": str, "description": str, "expires": int},
    total=False,
)


class ClientUpdateApiKeyResponseapiKeyTypeDef(_ClientUpdateApiKeyResponseapiKeyTypeDef):
    """
    - **apiKey** *(dict) --*

      The API key.
      - **id** *(string) --*

        The API key ID.
    """


_ClientUpdateApiKeyResponseTypeDef = TypedDict(
    "_ClientUpdateApiKeyResponseTypeDef",
    {"apiKey": ClientUpdateApiKeyResponseapiKeyTypeDef},
    total=False,
)


class ClientUpdateApiKeyResponseTypeDef(_ClientUpdateApiKeyResponseTypeDef):
    """
    - *(dict) --*

      - **apiKey** *(dict) --*

        The API key.
        - **id** *(string) --*

          The API key ID.
    """


_ClientUpdateDataSourceDynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceDynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)


class ClientUpdateDataSourceDynamodbConfigdeltaSyncConfigTypeDef(
    _ClientUpdateDataSourceDynamodbConfigdeltaSyncConfigTypeDef
):
    pass


_RequiredClientUpdateDataSourceDynamodbConfigTypeDef = TypedDict(
    "_RequiredClientUpdateDataSourceDynamodbConfigTypeDef", {"tableName": str}
)
_OptionalClientUpdateDataSourceDynamodbConfigTypeDef = TypedDict(
    "_OptionalClientUpdateDataSourceDynamodbConfigTypeDef",
    {
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientUpdateDataSourceDynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)


class ClientUpdateDataSourceDynamodbConfigTypeDef(
    _RequiredClientUpdateDataSourceDynamodbConfigTypeDef,
    _OptionalClientUpdateDataSourceDynamodbConfigTypeDef,
):
    """
    The new Amazon DynamoDB configuration.
    - **tableName** *(string) --***[REQUIRED]**

      The table name.
    """


_RequiredClientUpdateDataSourceElasticsearchConfigTypeDef = TypedDict(
    "_RequiredClientUpdateDataSourceElasticsearchConfigTypeDef", {"endpoint": str}
)
_OptionalClientUpdateDataSourceElasticsearchConfigTypeDef = TypedDict(
    "_OptionalClientUpdateDataSourceElasticsearchConfigTypeDef", {"awsRegion": str}, total=False
)


class ClientUpdateDataSourceElasticsearchConfigTypeDef(
    _RequiredClientUpdateDataSourceElasticsearchConfigTypeDef,
    _OptionalClientUpdateDataSourceElasticsearchConfigTypeDef,
):
    """
    The new Elasticsearch Service configuration.
    - **endpoint** *(string) --***[REQUIRED]**

      The endpoint.
    """


_ClientUpdateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)


class ClientUpdateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef(
    _ClientUpdateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef
):
    pass


_ClientUpdateDataSourceHttpConfigauthorizationConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceHttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientUpdateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDataSourceHttpConfigauthorizationConfigTypeDef(
    _ClientUpdateDataSourceHttpConfigauthorizationConfigTypeDef
):
    pass


_ClientUpdateDataSourceHttpConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceHttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientUpdateDataSourceHttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDataSourceHttpConfigTypeDef(_ClientUpdateDataSourceHttpConfigTypeDef):
    """
    The new HTTP endpoint configuration.
    - **endpoint** *(string) --*

      The HTTP URL endpoint. You can either specify the domain name or IP, and port combination, and
      the URL scheme must be HTTP or HTTPS. If the port is not specified, AWS AppSync uses the
      default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.
    """


_ClientUpdateDataSourceLambdaConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceLambdaConfigTypeDef", {"lambdaFunctionArn": str}
)


class ClientUpdateDataSourceLambdaConfigTypeDef(_ClientUpdateDataSourceLambdaConfigTypeDef):
    """
    The new AWS Lambda configuration.
    - **lambdaFunctionArn** *(string) --***[REQUIRED]**

      The ARN for the Lambda function.
    """


_ClientUpdateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)


class ClientUpdateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef(
    _ClientUpdateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef
):
    pass


_ClientUpdateDataSourceRelationalDatabaseConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceRelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientUpdateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDataSourceRelationalDatabaseConfigTypeDef(
    _ClientUpdateDataSourceRelationalDatabaseConfigTypeDef
):
    """
    The new relational database configuration.
    - **relationalDatabaseSourceType** *(string) --*

      Source type for the relational database.
      * **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon RDS HTTP endpoint.
    """


_ClientUpdateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)


class ClientUpdateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef(
    _ClientUpdateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef
):
    pass


_ClientUpdateDataSourceResponsedataSourcedynamodbConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourcedynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientUpdateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)


class ClientUpdateDataSourceResponsedataSourcedynamodbConfigTypeDef(
    _ClientUpdateDataSourceResponsedataSourcedynamodbConfigTypeDef
):
    pass


_ClientUpdateDataSourceResponsedataSourceelasticsearchConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourceelasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)


class ClientUpdateDataSourceResponsedataSourceelasticsearchConfigTypeDef(
    _ClientUpdateDataSourceResponsedataSourceelasticsearchConfigTypeDef
):
    pass


_ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)


class ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef(
    _ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef
):
    pass


_ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef(
    _ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef
):
    pass


_ClientUpdateDataSourceResponsedataSourcehttpConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourcehttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDataSourceResponsedataSourcehttpConfigTypeDef(
    _ClientUpdateDataSourceResponsedataSourcehttpConfigTypeDef
):
    pass


_ClientUpdateDataSourceResponsedataSourcelambdaConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourcelambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)


class ClientUpdateDataSourceResponsedataSourcelambdaConfigTypeDef(
    _ClientUpdateDataSourceResponsedataSourcelambdaConfigTypeDef
):
    pass


_ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)


class ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef(
    _ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef
):
    pass


_ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef(
    _ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef
):
    pass


_ClientUpdateDataSourceResponsedataSourceTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponsedataSourceTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        "serviceRoleArn": str,
        "dynamodbConfig": ClientUpdateDataSourceResponsedataSourcedynamodbConfigTypeDef,
        "lambdaConfig": ClientUpdateDataSourceResponsedataSourcelambdaConfigTypeDef,
        "elasticsearchConfig": ClientUpdateDataSourceResponsedataSourceelasticsearchConfigTypeDef,
        "httpConfig": ClientUpdateDataSourceResponsedataSourcehttpConfigTypeDef,
        "relationalDatabaseConfig": ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDataSourceResponsedataSourceTypeDef(
    _ClientUpdateDataSourceResponsedataSourceTypeDef
):
    """
    - **dataSource** *(dict) --*

      The updated ``DataSource`` object.
      - **dataSourceArn** *(string) --*

        The data source ARN.
    """


_ClientUpdateDataSourceResponseTypeDef = TypedDict(
    "_ClientUpdateDataSourceResponseTypeDef",
    {"dataSource": ClientUpdateDataSourceResponsedataSourceTypeDef},
    total=False,
)


class ClientUpdateDataSourceResponseTypeDef(_ClientUpdateDataSourceResponseTypeDef):
    """
    - *(dict) --*

      - **dataSource** *(dict) --*

        The updated ``DataSource`` object.
        - **dataSourceArn** *(string) --*

          The data source ARN.
    """


_ClientUpdateFunctionResponsefunctionConfigurationTypeDef = TypedDict(
    "_ClientUpdateFunctionResponsefunctionConfigurationTypeDef",
    {
        "functionId": str,
        "functionArn": str,
        "name": str,
        "description": str,
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
    },
    total=False,
)


class ClientUpdateFunctionResponsefunctionConfigurationTypeDef(
    _ClientUpdateFunctionResponsefunctionConfigurationTypeDef
):
    """
    - **functionConfiguration** *(dict) --*

      The ``Function`` object.
      - **functionId** *(string) --*

        A unique ID representing the ``Function`` object.
    """


_ClientUpdateFunctionResponseTypeDef = TypedDict(
    "_ClientUpdateFunctionResponseTypeDef",
    {"functionConfiguration": ClientUpdateFunctionResponsefunctionConfigurationTypeDef},
    total=False,
)


class ClientUpdateFunctionResponseTypeDef(_ClientUpdateFunctionResponseTypeDef):
    """
    - *(dict) --*

      - **functionConfiguration** *(dict) --*

        The ``Function`` object.
        - **functionId** *(string) --*

          A unique ID representing the ``Function`` object.
    """


_ClientUpdateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientUpdateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef(
    _ClientUpdateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef
):
    pass


_ClientUpdateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)


class ClientUpdateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef(
    _ClientUpdateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef
):
    pass


_ClientUpdateGraphqlApiAdditionalAuthenticationProvidersTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiAdditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientUpdateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientUpdateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)


class ClientUpdateGraphqlApiAdditionalAuthenticationProvidersTypeDef(
    _ClientUpdateGraphqlApiAdditionalAuthenticationProvidersTypeDef
):
    """
    - *(dict) --*

      Describes an additional authentication provider.
      - **authenticationType** *(string) --*

        The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.
    """


_RequiredClientUpdateGraphqlApiLogConfigTypeDef = TypedDict(
    "_RequiredClientUpdateGraphqlApiLogConfigTypeDef",
    {"fieldLogLevel": Literal["NONE", "ERROR", "ALL"]},
)
_OptionalClientUpdateGraphqlApiLogConfigTypeDef = TypedDict(
    "_OptionalClientUpdateGraphqlApiLogConfigTypeDef",
    {"cloudWatchLogsRoleArn": str, "excludeVerboseContent": bool},
    total=False,
)


class ClientUpdateGraphqlApiLogConfigTypeDef(
    _RequiredClientUpdateGraphqlApiLogConfigTypeDef, _OptionalClientUpdateGraphqlApiLogConfigTypeDef
):
    """
    The Amazon CloudWatch Logs configuration for the ``GraphqlApi`` object.
    - **fieldLogLevel** *(string) --***[REQUIRED]**

      The field logging level. Values can be NONE, ERROR, or ALL.
      * **NONE** : No field-level logs are captured.
      * **ERROR** : Logs the following information only for the fields that are in error:

        * The error section in the server response.
        * Field-level errors.
        * The generated request/response functions that got resolved for error fields.
    """


_RequiredClientUpdateGraphqlApiOpenIDConnectConfigTypeDef = TypedDict(
    "_RequiredClientUpdateGraphqlApiOpenIDConnectConfigTypeDef", {"issuer": str}
)
_OptionalClientUpdateGraphqlApiOpenIDConnectConfigTypeDef = TypedDict(
    "_OptionalClientUpdateGraphqlApiOpenIDConnectConfigTypeDef",
    {"clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientUpdateGraphqlApiOpenIDConnectConfigTypeDef(
    _RequiredClientUpdateGraphqlApiOpenIDConnectConfigTypeDef,
    _OptionalClientUpdateGraphqlApiOpenIDConnectConfigTypeDef,
):
    """
    The OpenID Connect configuration for the ``GraphqlApi`` object.
    - **issuer** *(string) --***[REQUIRED]**

      The issuer for the OpenID Connect configuration. The issuer returned by discovery must exactly
      match the value of ``iss`` in the ID token.
    """


_ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef(
    _ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef
):
    pass


_ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)


class ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef(
    _ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef
):
    pass


_ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)


class ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef(
    _ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef
):
    pass


_ClientUpdateGraphqlApiResponsegraphqlApilogConfigTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiResponsegraphqlApilogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)


class ClientUpdateGraphqlApiResponsegraphqlApilogConfigTypeDef(
    _ClientUpdateGraphqlApiResponsegraphqlApilogConfigTypeDef
):
    pass


_ClientUpdateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ClientUpdateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef(
    _ClientUpdateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef
):
    pass


_ClientUpdateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)


class ClientUpdateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef(
    _ClientUpdateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef
):
    pass


_ClientUpdateGraphqlApiResponsegraphqlApiTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiResponsegraphqlApiTypeDef",
    {
        "name": str,
        "apiId": str,
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "logConfig": ClientUpdateGraphqlApiResponsegraphqlApilogConfigTypeDef,
        "userPoolConfig": ClientUpdateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef,
        "openIDConnectConfig": ClientUpdateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef,
        "arn": str,
        "uris": Dict[str, str],
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List[
            ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef
        ],
    },
    total=False,
)


class ClientUpdateGraphqlApiResponsegraphqlApiTypeDef(
    _ClientUpdateGraphqlApiResponsegraphqlApiTypeDef
):
    """
    - **graphqlApi** *(dict) --*

      The updated ``GraphqlApi`` object.
      - **name** *(string) --*

        The API name.
    """


_ClientUpdateGraphqlApiResponseTypeDef = TypedDict(
    "_ClientUpdateGraphqlApiResponseTypeDef",
    {"graphqlApi": ClientUpdateGraphqlApiResponsegraphqlApiTypeDef},
    total=False,
)


class ClientUpdateGraphqlApiResponseTypeDef(_ClientUpdateGraphqlApiResponseTypeDef):
    """
    - *(dict) --*

      - **graphqlApi** *(dict) --*

        The updated ``GraphqlApi`` object.
        - **name** *(string) --*

          The API name.
    """


_RequiredClientUpdateGraphqlApiUserPoolConfigTypeDef = TypedDict(
    "_RequiredClientUpdateGraphqlApiUserPoolConfigTypeDef", {"userPoolId": str}
)
_OptionalClientUpdateGraphqlApiUserPoolConfigTypeDef = TypedDict(
    "_OptionalClientUpdateGraphqlApiUserPoolConfigTypeDef",
    {"awsRegion": str, "defaultAction": Literal["ALLOW", "DENY"], "appIdClientRegex": str},
    total=False,
)


class ClientUpdateGraphqlApiUserPoolConfigTypeDef(
    _RequiredClientUpdateGraphqlApiUserPoolConfigTypeDef,
    _OptionalClientUpdateGraphqlApiUserPoolConfigTypeDef,
):
    """
    The new Amazon Cognito user pool configuration for the ``GraphqlApi`` object.
    - **userPoolId** *(string) --***[REQUIRED]**

      The user pool ID.
    """


_ClientUpdateResolverCachingConfigTypeDef = TypedDict(
    "_ClientUpdateResolverCachingConfigTypeDef", {"ttl": int, "cachingKeys": List[str]}, total=False
)


class ClientUpdateResolverCachingConfigTypeDef(_ClientUpdateResolverCachingConfigTypeDef):
    """
    The caching configuration for the resolver.
    - **ttl** *(integer) --*

      The TTL in seconds for a resolver that has caching enabled.
      Valid values are between 1 and 3600 seconds.
    """


_ClientUpdateResolverPipelineConfigTypeDef = TypedDict(
    "_ClientUpdateResolverPipelineConfigTypeDef", {"functions": List[str]}, total=False
)


class ClientUpdateResolverPipelineConfigTypeDef(_ClientUpdateResolverPipelineConfigTypeDef):
    """
    The ``PipelineConfig`` .
    - **functions** *(list) --*

      A list of ``Function`` objects.
      - *(string) --*
    """


_ClientUpdateResolverResponseresolvercachingConfigTypeDef = TypedDict(
    "_ClientUpdateResolverResponseresolvercachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)


class ClientUpdateResolverResponseresolvercachingConfigTypeDef(
    _ClientUpdateResolverResponseresolvercachingConfigTypeDef
):
    pass


_ClientUpdateResolverResponseresolverpipelineConfigTypeDef = TypedDict(
    "_ClientUpdateResolverResponseresolverpipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)


class ClientUpdateResolverResponseresolverpipelineConfigTypeDef(
    _ClientUpdateResolverResponseresolverpipelineConfigTypeDef
):
    pass


_ClientUpdateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "_ClientUpdateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)


class ClientUpdateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef(
    _ClientUpdateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef
):
    pass


_ClientUpdateResolverResponseresolversyncConfigTypeDef = TypedDict(
    "_ClientUpdateResolverResponseresolversyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientUpdateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)


class ClientUpdateResolverResponseresolversyncConfigTypeDef(
    _ClientUpdateResolverResponseresolversyncConfigTypeDef
):
    pass


_ClientUpdateResolverResponseresolverTypeDef = TypedDict(
    "_ClientUpdateResolverResponseresolverTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": Literal["UNIT", "PIPELINE"],
        "pipelineConfig": ClientUpdateResolverResponseresolverpipelineConfigTypeDef,
        "syncConfig": ClientUpdateResolverResponseresolversyncConfigTypeDef,
        "cachingConfig": ClientUpdateResolverResponseresolvercachingConfigTypeDef,
    },
    total=False,
)


class ClientUpdateResolverResponseresolverTypeDef(_ClientUpdateResolverResponseresolverTypeDef):
    """
    - **resolver** *(dict) --*

      The updated ``Resolver`` object.
      - **typeName** *(string) --*

        The resolver type name.
    """


_ClientUpdateResolverResponseTypeDef = TypedDict(
    "_ClientUpdateResolverResponseTypeDef",
    {"resolver": ClientUpdateResolverResponseresolverTypeDef},
    total=False,
)


class ClientUpdateResolverResponseTypeDef(_ClientUpdateResolverResponseTypeDef):
    """
    - *(dict) --*

      - **resolver** *(dict) --*

        The updated ``Resolver`` object.
        - **typeName** *(string) --*

          The resolver type name.
    """


_ClientUpdateResolverSyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "_ClientUpdateResolverSyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)


class ClientUpdateResolverSyncConfiglambdaConflictHandlerConfigTypeDef(
    _ClientUpdateResolverSyncConfiglambdaConflictHandlerConfigTypeDef
):
    pass


_ClientUpdateResolverSyncConfigTypeDef = TypedDict(
    "_ClientUpdateResolverSyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientUpdateResolverSyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)


class ClientUpdateResolverSyncConfigTypeDef(_ClientUpdateResolverSyncConfigTypeDef):
    """
    The ``SyncConfig`` for a resolver attached to a versioned datasource.
    - **conflictHandler** *(string) --*

      The Conflict Resolution strategy to perform in the event of a conflict.
      * **OPTIMISTIC_CONCURRENCY** : Resolve conflicts by rejecting mutations when versions do not
      match the latest version at the server.
      * **AUTOMERGE** : Resolve conflicts with the Automerge conflict resolution strategy.
      * **LAMBDA** : Resolve conflicts with a Lambda function supplied in the
      LambdaConflictHandlerConfig.
    """


_ClientUpdateTypeResponsetypeTypeDef = TypedDict(
    "_ClientUpdateTypeResponsetypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)


class ClientUpdateTypeResponsetypeTypeDef(_ClientUpdateTypeResponsetypeTypeDef):
    """
    - **type** *(dict) --*

      The updated ``Type`` object.
      - **name** *(string) --*

        The type name.
    """


_ClientUpdateTypeResponseTypeDef = TypedDict(
    "_ClientUpdateTypeResponseTypeDef", {"type": ClientUpdateTypeResponsetypeTypeDef}, total=False
)


class ClientUpdateTypeResponseTypeDef(_ClientUpdateTypeResponseTypeDef):
    """
    - *(dict) --*

      - **type** *(dict) --*

        The updated ``Type`` object.
        - **name** *(string) --*

          The type name.
    """


_ListApiKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListApiKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListApiKeysPaginatePaginationConfigTypeDef(_ListApiKeysPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListApiKeysPaginateResponseapiKeysTypeDef = TypedDict(
    "_ListApiKeysPaginateResponseapiKeysTypeDef",
    {"id": str, "description": str, "expires": int},
    total=False,
)


class ListApiKeysPaginateResponseapiKeysTypeDef(_ListApiKeysPaginateResponseapiKeysTypeDef):
    """
    - *(dict) --*

      Describes an API key.
      Customers invoke AWS AppSync GraphQL API operations with API keys as an identity mechanism.
      There are two key versions:

        **da1** : This version was introduced at launch in November 2017. These keys always expire
        after 7 days. Key expiration is managed by Amazon DynamoDB TTL. The keys ceased to be valid
        after February 21, 2018 and should not be used after that date.
    """


_ListApiKeysPaginateResponseTypeDef = TypedDict(
    "_ListApiKeysPaginateResponseTypeDef",
    {"apiKeys": List[ListApiKeysPaginateResponseapiKeysTypeDef], "NextToken": str},
    total=False,
)


class ListApiKeysPaginateResponseTypeDef(_ListApiKeysPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **apiKeys** *(list) --*

        The ``ApiKey`` objects.
        - *(dict) --*

          Describes an API key.
          Customers invoke AWS AppSync GraphQL API operations with API keys as an identity
          mechanism. There are two key versions:

            **da1** : This version was introduced at launch in November 2017. These keys always
            expire after 7 days. Key expiration is managed by Amazon DynamoDB TTL. The keys ceased
            to be valid after February 21, 2018 and should not be used after that date.
    """


_ListDataSourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDataSourcesPaginatePaginationConfigTypeDef(
    _ListDataSourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDataSourcesPaginateResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)


class ListDataSourcesPaginateResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef(
    _ListDataSourcesPaginateResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef
):
    pass


_ListDataSourcesPaginateResponsedataSourcesdynamodbConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourcesdynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ListDataSourcesPaginateResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)


class ListDataSourcesPaginateResponsedataSourcesdynamodbConfigTypeDef(
    _ListDataSourcesPaginateResponsedataSourcesdynamodbConfigTypeDef
):
    pass


_ListDataSourcesPaginateResponsedataSourceselasticsearchConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourceselasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)


class ListDataSourcesPaginateResponsedataSourceselasticsearchConfigTypeDef(
    _ListDataSourcesPaginateResponsedataSourceselasticsearchConfigTypeDef
):
    pass


_ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)


class ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef(
    _ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef
):
    pass


_ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)


class ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigTypeDef(
    _ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigTypeDef
):
    pass


_ListDataSourcesPaginateResponsedataSourceshttpConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourceshttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)


class ListDataSourcesPaginateResponsedataSourceshttpConfigTypeDef(
    _ListDataSourcesPaginateResponsedataSourceshttpConfigTypeDef
):
    pass


_ListDataSourcesPaginateResponsedataSourceslambdaConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourceslambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)


class ListDataSourcesPaginateResponsedataSourceslambdaConfigTypeDef(
    _ListDataSourcesPaginateResponsedataSourceslambdaConfigTypeDef
):
    pass


_ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)


class ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef(
    _ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef
):
    pass


_ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)


class ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigTypeDef(
    _ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigTypeDef
):
    pass


_ListDataSourcesPaginateResponsedataSourcesTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponsedataSourcesTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        "serviceRoleArn": str,
        "dynamodbConfig": ListDataSourcesPaginateResponsedataSourcesdynamodbConfigTypeDef,
        "lambdaConfig": ListDataSourcesPaginateResponsedataSourceslambdaConfigTypeDef,
        "elasticsearchConfig": ListDataSourcesPaginateResponsedataSourceselasticsearchConfigTypeDef,
        "httpConfig": ListDataSourcesPaginateResponsedataSourceshttpConfigTypeDef,
        "relationalDatabaseConfig": ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigTypeDef,
    },
    total=False,
)


class ListDataSourcesPaginateResponsedataSourcesTypeDef(
    _ListDataSourcesPaginateResponsedataSourcesTypeDef
):
    """
    - *(dict) --*

      Describes a data source.
      - **dataSourceArn** *(string) --*

        The data source ARN.
    """


_ListDataSourcesPaginateResponseTypeDef = TypedDict(
    "_ListDataSourcesPaginateResponseTypeDef",
    {"dataSources": List[ListDataSourcesPaginateResponsedataSourcesTypeDef], "NextToken": str},
    total=False,
)


class ListDataSourcesPaginateResponseTypeDef(_ListDataSourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **dataSources** *(list) --*

        The ``DataSource`` objects.
        - *(dict) --*

          Describes a data source.
          - **dataSourceArn** *(string) --*

            The data source ARN.
    """


_ListFunctionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFunctionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFunctionsPaginatePaginationConfigTypeDef(_ListFunctionsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFunctionsPaginateResponsefunctionsTypeDef = TypedDict(
    "_ListFunctionsPaginateResponsefunctionsTypeDef",
    {
        "functionId": str,
        "functionArn": str,
        "name": str,
        "description": str,
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
    },
    total=False,
)


class ListFunctionsPaginateResponsefunctionsTypeDef(_ListFunctionsPaginateResponsefunctionsTypeDef):
    """
    - *(dict) --*

      A function is a reusable entity. Multiple functions can be used to compose the resolver logic.
      - **functionId** *(string) --*

        A unique ID representing the ``Function`` object.
    """


_ListFunctionsPaginateResponseTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseTypeDef",
    {"functions": List[ListFunctionsPaginateResponsefunctionsTypeDef], "NextToken": str},
    total=False,
)


class ListFunctionsPaginateResponseTypeDef(_ListFunctionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **functions** *(list) --*

        A list of ``Function`` objects.
        - *(dict) --*

          A function is a reusable entity. Multiple functions can be used to compose the resolver
          logic.
          - **functionId** *(string) --*

            A unique ID representing the ``Function`` object.
    """


_ListGraphqlApisPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGraphqlApisPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGraphqlApisPaginatePaginationConfigTypeDef(
    _ListGraphqlApisPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "_ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef(
    _ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef
):
    pass


_ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "_ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)


class ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef(
    _ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef
):
    pass


_ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersTypeDef = TypedDict(
    "_ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)


class ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersTypeDef(
    _ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersTypeDef
):
    pass


_ListGraphqlApisPaginateResponsegraphqlApislogConfigTypeDef = TypedDict(
    "_ListGraphqlApisPaginateResponsegraphqlApislogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)


class ListGraphqlApisPaginateResponsegraphqlApislogConfigTypeDef(
    _ListGraphqlApisPaginateResponsegraphqlApislogConfigTypeDef
):
    pass


_ListGraphqlApisPaginateResponsegraphqlApisopenIDConnectConfigTypeDef = TypedDict(
    "_ListGraphqlApisPaginateResponsegraphqlApisopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class ListGraphqlApisPaginateResponsegraphqlApisopenIDConnectConfigTypeDef(
    _ListGraphqlApisPaginateResponsegraphqlApisopenIDConnectConfigTypeDef
):
    pass


_ListGraphqlApisPaginateResponsegraphqlApisuserPoolConfigTypeDef = TypedDict(
    "_ListGraphqlApisPaginateResponsegraphqlApisuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)


class ListGraphqlApisPaginateResponsegraphqlApisuserPoolConfigTypeDef(
    _ListGraphqlApisPaginateResponsegraphqlApisuserPoolConfigTypeDef
):
    pass


_ListGraphqlApisPaginateResponsegraphqlApisTypeDef = TypedDict(
    "_ListGraphqlApisPaginateResponsegraphqlApisTypeDef",
    {
        "name": str,
        "apiId": str,
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "logConfig": ListGraphqlApisPaginateResponsegraphqlApislogConfigTypeDef,
        "userPoolConfig": ListGraphqlApisPaginateResponsegraphqlApisuserPoolConfigTypeDef,
        "openIDConnectConfig": ListGraphqlApisPaginateResponsegraphqlApisopenIDConnectConfigTypeDef,
        "arn": str,
        "uris": Dict[str, str],
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List[
            ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersTypeDef
        ],
    },
    total=False,
)


class ListGraphqlApisPaginateResponsegraphqlApisTypeDef(
    _ListGraphqlApisPaginateResponsegraphqlApisTypeDef
):
    """
    - *(dict) --*

      Describes a GraphQL API.
      - **name** *(string) --*

        The API name.
    """


_ListGraphqlApisPaginateResponseTypeDef = TypedDict(
    "_ListGraphqlApisPaginateResponseTypeDef",
    {"graphqlApis": List[ListGraphqlApisPaginateResponsegraphqlApisTypeDef], "NextToken": str},
    total=False,
)


class ListGraphqlApisPaginateResponseTypeDef(_ListGraphqlApisPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **graphqlApis** *(list) --*

        The ``GraphqlApi`` objects.
        - *(dict) --*

          Describes a GraphQL API.
          - **name** *(string) --*

            The API name.
    """


_ListResolversByFunctionPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResolversByFunctionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResolversByFunctionPaginatePaginationConfigTypeDef(
    _ListResolversByFunctionPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResolversByFunctionPaginateResponseresolverscachingConfigTypeDef = TypedDict(
    "_ListResolversByFunctionPaginateResponseresolverscachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)


class ListResolversByFunctionPaginateResponseresolverscachingConfigTypeDef(
    _ListResolversByFunctionPaginateResponseresolverscachingConfigTypeDef
):
    pass


_ListResolversByFunctionPaginateResponseresolverspipelineConfigTypeDef = TypedDict(
    "_ListResolversByFunctionPaginateResponseresolverspipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)


class ListResolversByFunctionPaginateResponseresolverspipelineConfigTypeDef(
    _ListResolversByFunctionPaginateResponseresolverspipelineConfigTypeDef
):
    pass


_ListResolversByFunctionPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "_ListResolversByFunctionPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)


class ListResolversByFunctionPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef(
    _ListResolversByFunctionPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef
):
    pass


_ListResolversByFunctionPaginateResponseresolverssyncConfigTypeDef = TypedDict(
    "_ListResolversByFunctionPaginateResponseresolverssyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ListResolversByFunctionPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)


class ListResolversByFunctionPaginateResponseresolverssyncConfigTypeDef(
    _ListResolversByFunctionPaginateResponseresolverssyncConfigTypeDef
):
    pass


_ListResolversByFunctionPaginateResponseresolversTypeDef = TypedDict(
    "_ListResolversByFunctionPaginateResponseresolversTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": Literal["UNIT", "PIPELINE"],
        "pipelineConfig": ListResolversByFunctionPaginateResponseresolverspipelineConfigTypeDef,
        "syncConfig": ListResolversByFunctionPaginateResponseresolverssyncConfigTypeDef,
        "cachingConfig": ListResolversByFunctionPaginateResponseresolverscachingConfigTypeDef,
    },
    total=False,
)


class ListResolversByFunctionPaginateResponseresolversTypeDef(
    _ListResolversByFunctionPaginateResponseresolversTypeDef
):
    """
    - *(dict) --*

      Describes a resolver.
      - **typeName** *(string) --*

        The resolver type name.
    """


_ListResolversByFunctionPaginateResponseTypeDef = TypedDict(
    "_ListResolversByFunctionPaginateResponseTypeDef",
    {"resolvers": List[ListResolversByFunctionPaginateResponseresolversTypeDef], "NextToken": str},
    total=False,
)


class ListResolversByFunctionPaginateResponseTypeDef(
    _ListResolversByFunctionPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **resolvers** *(list) --*

        The list of resolvers.
        - *(dict) --*

          Describes a resolver.
          - **typeName** *(string) --*

            The resolver type name.
    """


_ListResolversPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResolversPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResolversPaginatePaginationConfigTypeDef(_ListResolversPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResolversPaginateResponseresolverscachingConfigTypeDef = TypedDict(
    "_ListResolversPaginateResponseresolverscachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)


class ListResolversPaginateResponseresolverscachingConfigTypeDef(
    _ListResolversPaginateResponseresolverscachingConfigTypeDef
):
    pass


_ListResolversPaginateResponseresolverspipelineConfigTypeDef = TypedDict(
    "_ListResolversPaginateResponseresolverspipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)


class ListResolversPaginateResponseresolverspipelineConfigTypeDef(
    _ListResolversPaginateResponseresolverspipelineConfigTypeDef
):
    pass


_ListResolversPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "_ListResolversPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)


class ListResolversPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef(
    _ListResolversPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef
):
    pass


_ListResolversPaginateResponseresolverssyncConfigTypeDef = TypedDict(
    "_ListResolversPaginateResponseresolverssyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ListResolversPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)


class ListResolversPaginateResponseresolverssyncConfigTypeDef(
    _ListResolversPaginateResponseresolverssyncConfigTypeDef
):
    pass


_ListResolversPaginateResponseresolversTypeDef = TypedDict(
    "_ListResolversPaginateResponseresolversTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": Literal["UNIT", "PIPELINE"],
        "pipelineConfig": ListResolversPaginateResponseresolverspipelineConfigTypeDef,
        "syncConfig": ListResolversPaginateResponseresolverssyncConfigTypeDef,
        "cachingConfig": ListResolversPaginateResponseresolverscachingConfigTypeDef,
    },
    total=False,
)


class ListResolversPaginateResponseresolversTypeDef(_ListResolversPaginateResponseresolversTypeDef):
    """
    - *(dict) --*

      Describes a resolver.
      - **typeName** *(string) --*

        The resolver type name.
    """


_ListResolversPaginateResponseTypeDef = TypedDict(
    "_ListResolversPaginateResponseTypeDef",
    {"resolvers": List[ListResolversPaginateResponseresolversTypeDef], "NextToken": str},
    total=False,
)


class ListResolversPaginateResponseTypeDef(_ListResolversPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **resolvers** *(list) --*

        The ``Resolver`` objects.
        - *(dict) --*

          Describes a resolver.
          - **typeName** *(string) --*

            The resolver type name.
    """


_ListTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTypesPaginatePaginationConfigTypeDef(_ListTypesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTypesPaginateResponsetypesTypeDef = TypedDict(
    "_ListTypesPaginateResponsetypesTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)


class ListTypesPaginateResponsetypesTypeDef(_ListTypesPaginateResponsetypesTypeDef):
    """
    - *(dict) --*

      Describes a type.
      - **name** *(string) --*

        The type name.
    """


_ListTypesPaginateResponseTypeDef = TypedDict(
    "_ListTypesPaginateResponseTypeDef",
    {"types": List[ListTypesPaginateResponsetypesTypeDef], "NextToken": str},
    total=False,
)


class ListTypesPaginateResponseTypeDef(_ListTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **types** *(list) --*

        The ``Type`` objects.
        - *(dict) --*

          Describes a type.
          - **name** *(string) --*

            The type name.
    """
