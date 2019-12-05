"Main interface for appsync service type defs"
from __future__ import annotations

import sys
from typing import Dict, List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateApiCacheResponseapiCacheTypeDef = TypedDict(
    "ClientCreateApiCacheResponseapiCacheTypeDef",
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

ClientCreateApiCacheResponseTypeDef = TypedDict(
    "ClientCreateApiCacheResponseTypeDef",
    {"apiCache": ClientCreateApiCacheResponseapiCacheTypeDef},
    total=False,
)

ClientCreateApiKeyResponseapiKeyTypeDef = TypedDict(
    "ClientCreateApiKeyResponseapiKeyTypeDef",
    {"id": str, "description": str, "expires": int},
    total=False,
)

ClientCreateApiKeyResponseTypeDef = TypedDict(
    "ClientCreateApiKeyResponseTypeDef",
    {"apiKey": ClientCreateApiKeyResponseapiKeyTypeDef},
    total=False,
)

ClientCreateDataSourceDynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "ClientCreateDataSourceDynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)

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
    pass


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
    pass


ClientCreateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "ClientCreateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)

ClientCreateDataSourceHttpConfigauthorizationConfigTypeDef = TypedDict(
    "ClientCreateDataSourceHttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientCreateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)

ClientCreateDataSourceHttpConfigTypeDef = TypedDict(
    "ClientCreateDataSourceHttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientCreateDataSourceHttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)

ClientCreateDataSourceLambdaConfigTypeDef = TypedDict(
    "ClientCreateDataSourceLambdaConfigTypeDef", {"lambdaFunctionArn": str}
)

ClientCreateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "ClientCreateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

ClientCreateDataSourceRelationalDatabaseConfigTypeDef = TypedDict(
    "ClientCreateDataSourceRelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientCreateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)

ClientCreateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)

ClientCreateDataSourceResponsedataSourcedynamodbConfigTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourcedynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientCreateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)

ClientCreateDataSourceResponsedataSourceelasticsearchConfigTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourceelasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)

ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)

ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)

ClientCreateDataSourceResponsedataSourcehttpConfigTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourcehttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientCreateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)

ClientCreateDataSourceResponsedataSourcelambdaConfigTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourcelambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)

ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientCreateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)

ClientCreateDataSourceResponsedataSourceTypeDef = TypedDict(
    "ClientCreateDataSourceResponsedataSourceTypeDef",
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

ClientCreateDataSourceResponseTypeDef = TypedDict(
    "ClientCreateDataSourceResponseTypeDef",
    {"dataSource": ClientCreateDataSourceResponsedataSourceTypeDef},
    total=False,
)

ClientCreateFunctionResponsefunctionConfigurationTypeDef = TypedDict(
    "ClientCreateFunctionResponsefunctionConfigurationTypeDef",
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

ClientCreateFunctionResponseTypeDef = TypedDict(
    "ClientCreateFunctionResponseTypeDef",
    {"functionConfiguration": ClientCreateFunctionResponsefunctionConfigurationTypeDef},
    total=False,
)

ClientCreateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "ClientCreateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientCreateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "ClientCreateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)

ClientCreateGraphqlApiAdditionalAuthenticationProvidersTypeDef = TypedDict(
    "ClientCreateGraphqlApiAdditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientCreateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientCreateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)

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
    pass


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
    pass


ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)

ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef = TypedDict(
    "ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientCreateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)

ClientCreateGraphqlApiResponsegraphqlApilogConfigTypeDef = TypedDict(
    "ClientCreateGraphqlApiResponsegraphqlApilogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)

ClientCreateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef = TypedDict(
    "ClientCreateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientCreateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef = TypedDict(
    "ClientCreateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)

ClientCreateGraphqlApiResponsegraphqlApiTypeDef = TypedDict(
    "ClientCreateGraphqlApiResponsegraphqlApiTypeDef",
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

ClientCreateGraphqlApiResponseTypeDef = TypedDict(
    "ClientCreateGraphqlApiResponseTypeDef",
    {"graphqlApi": ClientCreateGraphqlApiResponsegraphqlApiTypeDef},
    total=False,
)

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
    pass


ClientCreateResolverCachingConfigTypeDef = TypedDict(
    "ClientCreateResolverCachingConfigTypeDef", {"ttl": int, "cachingKeys": List[str]}, total=False
)

ClientCreateResolverPipelineConfigTypeDef = TypedDict(
    "ClientCreateResolverPipelineConfigTypeDef", {"functions": List[str]}, total=False
)

ClientCreateResolverResponseresolvercachingConfigTypeDef = TypedDict(
    "ClientCreateResolverResponseresolvercachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)

ClientCreateResolverResponseresolverpipelineConfigTypeDef = TypedDict(
    "ClientCreateResolverResponseresolverpipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)

ClientCreateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "ClientCreateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)

ClientCreateResolverResponseresolversyncConfigTypeDef = TypedDict(
    "ClientCreateResolverResponseresolversyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientCreateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ClientCreateResolverResponseresolverTypeDef = TypedDict(
    "ClientCreateResolverResponseresolverTypeDef",
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

ClientCreateResolverResponseTypeDef = TypedDict(
    "ClientCreateResolverResponseTypeDef",
    {"resolver": ClientCreateResolverResponseresolverTypeDef},
    total=False,
)

ClientCreateResolverSyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "ClientCreateResolverSyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)

ClientCreateResolverSyncConfigTypeDef = TypedDict(
    "ClientCreateResolverSyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientCreateResolverSyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ClientCreateTypeResponsetypeTypeDef = TypedDict(
    "ClientCreateTypeResponsetypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)

ClientCreateTypeResponseTypeDef = TypedDict(
    "ClientCreateTypeResponseTypeDef", {"type": ClientCreateTypeResponsetypeTypeDef}, total=False
)

ClientGetApiCacheResponseapiCacheTypeDef = TypedDict(
    "ClientGetApiCacheResponseapiCacheTypeDef",
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

ClientGetApiCacheResponseTypeDef = TypedDict(
    "ClientGetApiCacheResponseTypeDef",
    {"apiCache": ClientGetApiCacheResponseapiCacheTypeDef},
    total=False,
)

ClientGetDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)

ClientGetDataSourceResponsedataSourcedynamodbConfigTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourcedynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientGetDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)

ClientGetDataSourceResponsedataSourceelasticsearchConfigTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourceelasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)

ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)

ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)

ClientGetDataSourceResponsedataSourcehttpConfigTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourcehttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientGetDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)

ClientGetDataSourceResponsedataSourcelambdaConfigTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourcelambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)

ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientGetDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)

ClientGetDataSourceResponsedataSourceTypeDef = TypedDict(
    "ClientGetDataSourceResponsedataSourceTypeDef",
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

ClientGetDataSourceResponseTypeDef = TypedDict(
    "ClientGetDataSourceResponseTypeDef",
    {"dataSource": ClientGetDataSourceResponsedataSourceTypeDef},
    total=False,
)

ClientGetFunctionResponsefunctionConfigurationTypeDef = TypedDict(
    "ClientGetFunctionResponsefunctionConfigurationTypeDef",
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

ClientGetFunctionResponseTypeDef = TypedDict(
    "ClientGetFunctionResponseTypeDef",
    {"functionConfiguration": ClientGetFunctionResponsefunctionConfigurationTypeDef},
    total=False,
)

ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)

ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef = TypedDict(
    "ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientGetGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)

ClientGetGraphqlApiResponsegraphqlApilogConfigTypeDef = TypedDict(
    "ClientGetGraphqlApiResponsegraphqlApilogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)

ClientGetGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef = TypedDict(
    "ClientGetGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientGetGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef = TypedDict(
    "ClientGetGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)

ClientGetGraphqlApiResponsegraphqlApiTypeDef = TypedDict(
    "ClientGetGraphqlApiResponsegraphqlApiTypeDef",
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

ClientGetGraphqlApiResponseTypeDef = TypedDict(
    "ClientGetGraphqlApiResponseTypeDef",
    {"graphqlApi": ClientGetGraphqlApiResponsegraphqlApiTypeDef},
    total=False,
)

ClientGetIntrospectionSchemaResponseTypeDef = TypedDict(
    "ClientGetIntrospectionSchemaResponseTypeDef", {"schema": StreamingBody}, total=False
)

ClientGetResolverResponseresolvercachingConfigTypeDef = TypedDict(
    "ClientGetResolverResponseresolvercachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)

ClientGetResolverResponseresolverpipelineConfigTypeDef = TypedDict(
    "ClientGetResolverResponseresolverpipelineConfigTypeDef", {"functions": List[str]}, total=False
)

ClientGetResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "ClientGetResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)

ClientGetResolverResponseresolversyncConfigTypeDef = TypedDict(
    "ClientGetResolverResponseresolversyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientGetResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ClientGetResolverResponseresolverTypeDef = TypedDict(
    "ClientGetResolverResponseresolverTypeDef",
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

ClientGetResolverResponseTypeDef = TypedDict(
    "ClientGetResolverResponseTypeDef",
    {"resolver": ClientGetResolverResponseresolverTypeDef},
    total=False,
)

ClientGetSchemaCreationStatusResponseTypeDef = TypedDict(
    "ClientGetSchemaCreationStatusResponseTypeDef",
    {
        "status": Literal[
            "PROCESSING", "ACTIVE", "DELETING", "FAILED", "SUCCESS", "NOT_APPLICABLE"
        ],
        "details": str,
    },
    total=False,
)

ClientGetTypeResponsetypeTypeDef = TypedDict(
    "ClientGetTypeResponsetypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)

ClientGetTypeResponseTypeDef = TypedDict(
    "ClientGetTypeResponseTypeDef", {"type": ClientGetTypeResponsetypeTypeDef}, total=False
)

ClientListApiKeysResponseapiKeysTypeDef = TypedDict(
    "ClientListApiKeysResponseapiKeysTypeDef",
    {"id": str, "description": str, "expires": int},
    total=False,
)

ClientListApiKeysResponseTypeDef = TypedDict(
    "ClientListApiKeysResponseTypeDef",
    {"apiKeys": List[ClientListApiKeysResponseapiKeysTypeDef], "nextToken": str},
    total=False,
)

ClientListDataSourcesResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)

ClientListDataSourcesResponsedataSourcesdynamodbConfigTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourcesdynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientListDataSourcesResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)

ClientListDataSourcesResponsedataSourceselasticsearchConfigTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourceselasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)

ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)

ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)

ClientListDataSourcesResponsedataSourceshttpConfigTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourceshttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientListDataSourcesResponsedataSourceshttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)

ClientListDataSourcesResponsedataSourceslambdaConfigTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourceslambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)

ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientListDataSourcesResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)

ClientListDataSourcesResponsedataSourcesTypeDef = TypedDict(
    "ClientListDataSourcesResponsedataSourcesTypeDef",
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

ClientListDataSourcesResponseTypeDef = TypedDict(
    "ClientListDataSourcesResponseTypeDef",
    {"dataSources": List[ClientListDataSourcesResponsedataSourcesTypeDef], "nextToken": str},
    total=False,
)

ClientListFunctionsResponsefunctionsTypeDef = TypedDict(
    "ClientListFunctionsResponsefunctionsTypeDef",
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

ClientListFunctionsResponseTypeDef = TypedDict(
    "ClientListFunctionsResponseTypeDef",
    {"functions": List[ClientListFunctionsResponsefunctionsTypeDef], "nextToken": str},
    total=False,
)

ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)

ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersTypeDef = TypedDict(
    "ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientListGraphqlApisResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)

ClientListGraphqlApisResponsegraphqlApislogConfigTypeDef = TypedDict(
    "ClientListGraphqlApisResponsegraphqlApislogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)

ClientListGraphqlApisResponsegraphqlApisopenIDConnectConfigTypeDef = TypedDict(
    "ClientListGraphqlApisResponsegraphqlApisopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientListGraphqlApisResponsegraphqlApisuserPoolConfigTypeDef = TypedDict(
    "ClientListGraphqlApisResponsegraphqlApisuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)

ClientListGraphqlApisResponsegraphqlApisTypeDef = TypedDict(
    "ClientListGraphqlApisResponsegraphqlApisTypeDef",
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

ClientListGraphqlApisResponseTypeDef = TypedDict(
    "ClientListGraphqlApisResponseTypeDef",
    {"graphqlApis": List[ClientListGraphqlApisResponsegraphqlApisTypeDef], "nextToken": str},
    total=False,
)

ClientListResolversByFunctionResponseresolverscachingConfigTypeDef = TypedDict(
    "ClientListResolversByFunctionResponseresolverscachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)

ClientListResolversByFunctionResponseresolverspipelineConfigTypeDef = TypedDict(
    "ClientListResolversByFunctionResponseresolverspipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)

ClientListResolversByFunctionResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "ClientListResolversByFunctionResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)

ClientListResolversByFunctionResponseresolverssyncConfigTypeDef = TypedDict(
    "ClientListResolversByFunctionResponseresolverssyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientListResolversByFunctionResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ClientListResolversByFunctionResponseresolversTypeDef = TypedDict(
    "ClientListResolversByFunctionResponseresolversTypeDef",
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

ClientListResolversByFunctionResponseTypeDef = TypedDict(
    "ClientListResolversByFunctionResponseTypeDef",
    {"resolvers": List[ClientListResolversByFunctionResponseresolversTypeDef], "nextToken": str},
    total=False,
)

ClientListResolversResponseresolverscachingConfigTypeDef = TypedDict(
    "ClientListResolversResponseresolverscachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)

ClientListResolversResponseresolverspipelineConfigTypeDef = TypedDict(
    "ClientListResolversResponseresolverspipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)

ClientListResolversResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "ClientListResolversResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)

ClientListResolversResponseresolverssyncConfigTypeDef = TypedDict(
    "ClientListResolversResponseresolverssyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientListResolversResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ClientListResolversResponseresolversTypeDef = TypedDict(
    "ClientListResolversResponseresolversTypeDef",
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

ClientListResolversResponseTypeDef = TypedDict(
    "ClientListResolversResponseTypeDef",
    {"resolvers": List[ClientListResolversResponseresolversTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientListTypesResponsetypesTypeDef = TypedDict(
    "ClientListTypesResponsetypesTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)

ClientListTypesResponseTypeDef = TypedDict(
    "ClientListTypesResponseTypeDef",
    {"types": List[ClientListTypesResponsetypesTypeDef], "nextToken": str},
    total=False,
)

ClientStartSchemaCreationResponseTypeDef = TypedDict(
    "ClientStartSchemaCreationResponseTypeDef",
    {"status": Literal["PROCESSING", "ACTIVE", "DELETING", "FAILED", "SUCCESS", "NOT_APPLICABLE"]},
    total=False,
)

ClientUpdateApiCacheResponseapiCacheTypeDef = TypedDict(
    "ClientUpdateApiCacheResponseapiCacheTypeDef",
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

ClientUpdateApiCacheResponseTypeDef = TypedDict(
    "ClientUpdateApiCacheResponseTypeDef",
    {"apiCache": ClientUpdateApiCacheResponseapiCacheTypeDef},
    total=False,
)

ClientUpdateApiKeyResponseapiKeyTypeDef = TypedDict(
    "ClientUpdateApiKeyResponseapiKeyTypeDef",
    {"id": str, "description": str, "expires": int},
    total=False,
)

ClientUpdateApiKeyResponseTypeDef = TypedDict(
    "ClientUpdateApiKeyResponseTypeDef",
    {"apiKey": ClientUpdateApiKeyResponseapiKeyTypeDef},
    total=False,
)

ClientUpdateDataSourceDynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceDynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)

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
    pass


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
    pass


ClientUpdateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)

ClientUpdateDataSourceHttpConfigauthorizationConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceHttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientUpdateDataSourceHttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)

ClientUpdateDataSourceHttpConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceHttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientUpdateDataSourceHttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)

ClientUpdateDataSourceLambdaConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceLambdaConfigTypeDef", {"lambdaFunctionArn": str}
)

ClientUpdateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

ClientUpdateDataSourceRelationalDatabaseConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceRelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientUpdateDataSourceRelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)

ClientUpdateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)

ClientUpdateDataSourceResponsedataSourcedynamodbConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourcedynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ClientUpdateDataSourceResponsedataSourcedynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)

ClientUpdateDataSourceResponsedataSourceelasticsearchConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourceelasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)

ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)

ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)

ClientUpdateDataSourceResponsedataSourcehttpConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourcehttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ClientUpdateDataSourceResponsedataSourcehttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)

ClientUpdateDataSourceResponsedataSourcelambdaConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourcelambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)

ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ClientUpdateDataSourceResponsedataSourcerelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)

ClientUpdateDataSourceResponsedataSourceTypeDef = TypedDict(
    "ClientUpdateDataSourceResponsedataSourceTypeDef",
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

ClientUpdateDataSourceResponseTypeDef = TypedDict(
    "ClientUpdateDataSourceResponseTypeDef",
    {"dataSource": ClientUpdateDataSourceResponsedataSourceTypeDef},
    total=False,
)

ClientUpdateFunctionResponsefunctionConfigurationTypeDef = TypedDict(
    "ClientUpdateFunctionResponsefunctionConfigurationTypeDef",
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

ClientUpdateFunctionResponseTypeDef = TypedDict(
    "ClientUpdateFunctionResponseTypeDef",
    {"functionConfiguration": ClientUpdateFunctionResponsefunctionConfigurationTypeDef},
    total=False,
)

ClientUpdateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "ClientUpdateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientUpdateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "ClientUpdateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)

ClientUpdateGraphqlApiAdditionalAuthenticationProvidersTypeDef = TypedDict(
    "ClientUpdateGraphqlApiAdditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientUpdateGraphqlApiAdditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientUpdateGraphqlApiAdditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)

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
    pass


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
    pass


ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)

ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef = TypedDict(
    "ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ClientUpdateGraphqlApiResponsegraphqlApiadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)

ClientUpdateGraphqlApiResponsegraphqlApilogConfigTypeDef = TypedDict(
    "ClientUpdateGraphqlApiResponsegraphqlApilogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)

ClientUpdateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef = TypedDict(
    "ClientUpdateGraphqlApiResponsegraphqlApiopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ClientUpdateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef = TypedDict(
    "ClientUpdateGraphqlApiResponsegraphqlApiuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)

ClientUpdateGraphqlApiResponsegraphqlApiTypeDef = TypedDict(
    "ClientUpdateGraphqlApiResponsegraphqlApiTypeDef",
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

ClientUpdateGraphqlApiResponseTypeDef = TypedDict(
    "ClientUpdateGraphqlApiResponseTypeDef",
    {"graphqlApi": ClientUpdateGraphqlApiResponsegraphqlApiTypeDef},
    total=False,
)

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
    pass


ClientUpdateResolverCachingConfigTypeDef = TypedDict(
    "ClientUpdateResolverCachingConfigTypeDef", {"ttl": int, "cachingKeys": List[str]}, total=False
)

ClientUpdateResolverPipelineConfigTypeDef = TypedDict(
    "ClientUpdateResolverPipelineConfigTypeDef", {"functions": List[str]}, total=False
)

ClientUpdateResolverResponseresolvercachingConfigTypeDef = TypedDict(
    "ClientUpdateResolverResponseresolvercachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)

ClientUpdateResolverResponseresolverpipelineConfigTypeDef = TypedDict(
    "ClientUpdateResolverResponseresolverpipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)

ClientUpdateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "ClientUpdateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)

ClientUpdateResolverResponseresolversyncConfigTypeDef = TypedDict(
    "ClientUpdateResolverResponseresolversyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientUpdateResolverResponseresolversyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ClientUpdateResolverResponseresolverTypeDef = TypedDict(
    "ClientUpdateResolverResponseresolverTypeDef",
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

ClientUpdateResolverResponseTypeDef = TypedDict(
    "ClientUpdateResolverResponseTypeDef",
    {"resolver": ClientUpdateResolverResponseresolverTypeDef},
    total=False,
)

ClientUpdateResolverSyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "ClientUpdateResolverSyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)

ClientUpdateResolverSyncConfigTypeDef = TypedDict(
    "ClientUpdateResolverSyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ClientUpdateResolverSyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ClientUpdateTypeResponsetypeTypeDef = TypedDict(
    "ClientUpdateTypeResponsetypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)

ClientUpdateTypeResponseTypeDef = TypedDict(
    "ClientUpdateTypeResponseTypeDef", {"type": ClientUpdateTypeResponsetypeTypeDef}, total=False
)

ListApiKeysPaginatePaginationConfigTypeDef = TypedDict(
    "ListApiKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListApiKeysPaginateResponseapiKeysTypeDef = TypedDict(
    "ListApiKeysPaginateResponseapiKeysTypeDef",
    {"id": str, "description": str, "expires": int},
    total=False,
)

ListApiKeysPaginateResponseTypeDef = TypedDict(
    "ListApiKeysPaginateResponseTypeDef",
    {"apiKeys": List[ListApiKeysPaginateResponseapiKeysTypeDef], "NextToken": str},
    total=False,
)

ListDataSourcesPaginatePaginationConfigTypeDef = TypedDict(
    "ListDataSourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDataSourcesPaginateResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)

ListDataSourcesPaginateResponsedataSourcesdynamodbConfigTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourcesdynamodbConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": bool,
        "deltaSyncConfig": ListDataSourcesPaginateResponsedataSourcesdynamodbConfigdeltaSyncConfigTypeDef,
        "versioned": bool,
    },
    total=False,
)

ListDataSourcesPaginateResponsedataSourceselasticsearchConfigTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourceselasticsearchConfigTypeDef",
    {"endpoint": str, "awsRegion": str},
    total=False,
)

ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef",
    {"signingRegion": str, "signingServiceName": str},
    total=False,
)

ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigTypeDef",
    {
        "authorizationType": str,
        "awsIamConfig": ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigawsIamConfigTypeDef,
    },
    total=False,
)

ListDataSourcesPaginateResponsedataSourceshttpConfigTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourceshttpConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": ListDataSourcesPaginateResponsedataSourceshttpConfigauthorizationConfigTypeDef,
    },
    total=False,
)

ListDataSourcesPaginateResponsedataSourceslambdaConfigTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourceslambdaConfigTypeDef",
    {"lambdaFunctionArn": str},
    total=False,
)

ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigTypeDef",
    {
        "relationalDatabaseSourceType": str,
        "rdsHttpEndpointConfig": ListDataSourcesPaginateResponsedataSourcesrelationalDatabaseConfigrdsHttpEndpointConfigTypeDef,
    },
    total=False,
)

ListDataSourcesPaginateResponsedataSourcesTypeDef = TypedDict(
    "ListDataSourcesPaginateResponsedataSourcesTypeDef",
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

ListDataSourcesPaginateResponseTypeDef = TypedDict(
    "ListDataSourcesPaginateResponseTypeDef",
    {"dataSources": List[ListDataSourcesPaginateResponsedataSourcesTypeDef], "NextToken": str},
    total=False,
)

ListFunctionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListFunctionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListFunctionsPaginateResponsefunctionsTypeDef = TypedDict(
    "ListFunctionsPaginateResponsefunctionsTypeDef",
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

ListFunctionsPaginateResponseTypeDef = TypedDict(
    "ListFunctionsPaginateResponseTypeDef",
    {"functions": List[ListFunctionsPaginateResponsefunctionsTypeDef], "NextToken": str},
    total=False,
)

ListGraphqlApisPaginatePaginationConfigTypeDef = TypedDict(
    "ListGraphqlApisPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef = TypedDict(
    "ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef = TypedDict(
    "ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "appIdClientRegex": str},
    total=False,
)

ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersTypeDef = TypedDict(
    "ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersTypeDef",
    {
        "authenticationType": Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        "openIDConnectConfig": ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersopenIDConnectConfigTypeDef,
        "userPoolConfig": ListGraphqlApisPaginateResponsegraphqlApisadditionalAuthenticationProvidersuserPoolConfigTypeDef,
    },
    total=False,
)

ListGraphqlApisPaginateResponsegraphqlApislogConfigTypeDef = TypedDict(
    "ListGraphqlApisPaginateResponsegraphqlApislogConfigTypeDef",
    {
        "fieldLogLevel": Literal["NONE", "ERROR", "ALL"],
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": bool,
    },
    total=False,
)

ListGraphqlApisPaginateResponsegraphqlApisopenIDConnectConfigTypeDef = TypedDict(
    "ListGraphqlApisPaginateResponsegraphqlApisopenIDConnectConfigTypeDef",
    {"issuer": str, "clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)

ListGraphqlApisPaginateResponsegraphqlApisuserPoolConfigTypeDef = TypedDict(
    "ListGraphqlApisPaginateResponsegraphqlApisuserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": Literal["ALLOW", "DENY"],
        "appIdClientRegex": str,
    },
    total=False,
)

ListGraphqlApisPaginateResponsegraphqlApisTypeDef = TypedDict(
    "ListGraphqlApisPaginateResponsegraphqlApisTypeDef",
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

ListGraphqlApisPaginateResponseTypeDef = TypedDict(
    "ListGraphqlApisPaginateResponseTypeDef",
    {"graphqlApis": List[ListGraphqlApisPaginateResponsegraphqlApisTypeDef], "NextToken": str},
    total=False,
)

ListResolversByFunctionPaginatePaginationConfigTypeDef = TypedDict(
    "ListResolversByFunctionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResolversByFunctionPaginateResponseresolverscachingConfigTypeDef = TypedDict(
    "ListResolversByFunctionPaginateResponseresolverscachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)

ListResolversByFunctionPaginateResponseresolverspipelineConfigTypeDef = TypedDict(
    "ListResolversByFunctionPaginateResponseresolverspipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)

ListResolversByFunctionPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "ListResolversByFunctionPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)

ListResolversByFunctionPaginateResponseresolverssyncConfigTypeDef = TypedDict(
    "ListResolversByFunctionPaginateResponseresolverssyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ListResolversByFunctionPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ListResolversByFunctionPaginateResponseresolversTypeDef = TypedDict(
    "ListResolversByFunctionPaginateResponseresolversTypeDef",
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

ListResolversByFunctionPaginateResponseTypeDef = TypedDict(
    "ListResolversByFunctionPaginateResponseTypeDef",
    {"resolvers": List[ListResolversByFunctionPaginateResponseresolversTypeDef], "NextToken": str},
    total=False,
)

ListResolversPaginatePaginationConfigTypeDef = TypedDict(
    "ListResolversPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResolversPaginateResponseresolverscachingConfigTypeDef = TypedDict(
    "ListResolversPaginateResponseresolverscachingConfigTypeDef",
    {"ttl": int, "cachingKeys": List[str]},
    total=False,
)

ListResolversPaginateResponseresolverspipelineConfigTypeDef = TypedDict(
    "ListResolversPaginateResponseresolverspipelineConfigTypeDef",
    {"functions": List[str]},
    total=False,
)

ListResolversPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef = TypedDict(
    "ListResolversPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef",
    {"lambdaConflictHandlerArn": str},
    total=False,
)

ListResolversPaginateResponseresolverssyncConfigTypeDef = TypedDict(
    "ListResolversPaginateResponseresolverssyncConfigTypeDef",
    {
        "conflictHandler": Literal["OPTIMISTIC_CONCURRENCY", "LAMBDA", "AUTOMERGE", "NONE"],
        "conflictDetection": Literal["VERSION", "NONE"],
        "lambdaConflictHandlerConfig": ListResolversPaginateResponseresolverssyncConfiglambdaConflictHandlerConfigTypeDef,
    },
    total=False,
)

ListResolversPaginateResponseresolversTypeDef = TypedDict(
    "ListResolversPaginateResponseresolversTypeDef",
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

ListResolversPaginateResponseTypeDef = TypedDict(
    "ListResolversPaginateResponseTypeDef",
    {"resolvers": List[ListResolversPaginateResponseresolversTypeDef], "NextToken": str},
    total=False,
)

ListTypesPaginatePaginationConfigTypeDef = TypedDict(
    "ListTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTypesPaginateResponsetypesTypeDef = TypedDict(
    "ListTypesPaginateResponsetypesTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": Literal["SDL", "JSON"],
    },
    total=False,
)

ListTypesPaginateResponseTypeDef = TypedDict(
    "ListTypesPaginateResponseTypeDef",
    {"types": List[ListTypesPaginateResponsetypesTypeDef], "NextToken": str},
    total=False,
)
