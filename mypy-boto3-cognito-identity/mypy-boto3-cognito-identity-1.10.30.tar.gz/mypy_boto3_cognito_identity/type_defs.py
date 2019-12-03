"Main interface for cognito-identity service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef",
    "ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    "ClientCreateIdentityPoolResponseTypeDef",
    "ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef",
    "ClientDeleteIdentitiesResponseTypeDef",
    "ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    "ClientDescribeIdentityPoolResponseTypeDef",
    "ClientDescribeIdentityResponseTypeDef",
    "ClientGetCredentialsForIdentityResponseCredentialsTypeDef",
    "ClientGetCredentialsForIdentityResponseTypeDef",
    "ClientGetIdResponseTypeDef",
    "ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef",
    "ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef",
    "ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef",
    "ClientGetIdentityPoolRolesResponseTypeDef",
    "ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    "ClientGetOpenIdTokenResponseTypeDef",
    "ClientListIdentitiesResponseIdentitiesTypeDef",
    "ClientListIdentitiesResponseTypeDef",
    "ClientListIdentityPoolsResponseIdentityPoolsTypeDef",
    "ClientListIdentityPoolsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientLookupDeveloperIdentityResponseTypeDef",
    "ClientMergeDeveloperIdentitiesResponseTypeDef",
    "ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef",
    "ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef",
    "ClientSetIdentityPoolRolesRoleMappingsTypeDef",
    "ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef",
    "ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    "ClientUpdateIdentityPoolResponseTypeDef",
    "ListIdentityPoolsPaginatePaginationConfigTypeDef",
    "ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef",
    "ListIdentityPoolsPaginateResponseTypeDef",
)


_ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef(
    _ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef
):
    """
    - *(dict) --*

      A provider representing an Amazon Cognito user pool and its client ID.
      - **ProviderName** *(string) --*

        The provider name for an Amazon Cognito user pool. For example,
        ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .
    """


_ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef(
    _ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef
):
    pass


_ClientCreateIdentityPoolResponseTypeDef = TypedDict(
    "_ClientCreateIdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[
            ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef
        ],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)


class ClientCreateIdentityPoolResponseTypeDef(_ClientCreateIdentityPoolResponseTypeDef):
    """
    - *(dict) --*

      An object representing an Amazon Cognito identity pool.
      - **IdentityPoolId** *(string) --*

        An identity pool ID in the format REGION:GUID.
    """


_ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef = TypedDict(
    "_ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef",
    {"IdentityId": str, "ErrorCode": Literal["AccessDenied", "InternalServerError"]},
    total=False,
)


class ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef(
    _ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef
):
    """
    - *(dict) --*

      An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.
      - **IdentityId** *(string) --*

        A unique identifier in the format REGION:GUID.
    """


_ClientDeleteIdentitiesResponseTypeDef = TypedDict(
    "_ClientDeleteIdentitiesResponseTypeDef",
    {"UnprocessedIdentityIds": List[ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef]},
    total=False,
)


class ClientDeleteIdentitiesResponseTypeDef(_ClientDeleteIdentitiesResponseTypeDef):
    """
    - *(dict) --*

      Returned in response to a successful ``DeleteIdentities`` operation.
      - **UnprocessedIdentityIds** *(list) --*

        An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and
        IdentityId.
        - *(dict) --*

          An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and
          IdentityId.
          - **IdentityId** *(string) --*

            A unique identifier in the format REGION:GUID.
    """


_ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef(
    _ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef
):
    pass


_ClientDescribeIdentityPoolResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[
            ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef
        ],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeIdentityPoolResponseTypeDef(_ClientDescribeIdentityPoolResponseTypeDef):
    """
    - *(dict) --*

      An object representing an Amazon Cognito identity pool.
      - **IdentityPoolId** *(string) --*

        An identity pool ID in the format REGION:GUID.
    """


_ClientDescribeIdentityResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeIdentityResponseTypeDef(_ClientDescribeIdentityResponseTypeDef):
    """
    - *(dict) --*

      A description of the identity.
      - **IdentityId** *(string) --*

        A unique identifier in the format REGION:GUID.
    """


_ClientGetCredentialsForIdentityResponseCredentialsTypeDef = TypedDict(
    "_ClientGetCredentialsForIdentityResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)


class ClientGetCredentialsForIdentityResponseCredentialsTypeDef(
    _ClientGetCredentialsForIdentityResponseCredentialsTypeDef
):
    pass


_ClientGetCredentialsForIdentityResponseTypeDef = TypedDict(
    "_ClientGetCredentialsForIdentityResponseTypeDef",
    {"IdentityId": str, "Credentials": ClientGetCredentialsForIdentityResponseCredentialsTypeDef},
    total=False,
)


class ClientGetCredentialsForIdentityResponseTypeDef(
    _ClientGetCredentialsForIdentityResponseTypeDef
):
    """
    - *(dict) --*

      Returned in response to a successful ``GetCredentialsForIdentity`` operation.
      - **IdentityId** *(string) --*

        A unique identifier in the format REGION:GUID.
    """


_ClientGetIdResponseTypeDef = TypedDict(
    "_ClientGetIdResponseTypeDef", {"IdentityId": str}, total=False
)


class ClientGetIdResponseTypeDef(_ClientGetIdResponseTypeDef):
    """
    - *(dict) --*

      Returned in response to a GetId request.
      - **IdentityId** *(string) --*

        A unique identifier in the format REGION:GUID.
    """


_ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef = TypedDict(
    "_ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef",
    {
        "Claim": str,
        "MatchType": Literal["Equals", "Contains", "StartsWith", "NotEqual"],
        "Value": str,
        "RoleARN": str,
    },
    total=False,
)


class ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef(
    _ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef
):
    pass


_ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef = TypedDict(
    "_ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef",
    {"Rules": List[ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef]},
    total=False,
)


class ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef(
    _ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef
):
    pass


_ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef = TypedDict(
    "_ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef",
    {
        "Type": Literal["Token", "Rules"],
        "AmbiguousRoleResolution": Literal["AuthenticatedRole", "Deny"],
        "RulesConfiguration": ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef,
    },
    total=False,
)


class ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef(
    _ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef
):
    pass


_ClientGetIdentityPoolRolesResponseTypeDef = TypedDict(
    "_ClientGetIdentityPoolRolesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
        "RoleMappings": Dict[str, ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef],
    },
    total=False,
)


class ClientGetIdentityPoolRolesResponseTypeDef(_ClientGetIdentityPoolRolesResponseTypeDef):
    """
    - *(dict) --*

      Returned in response to a successful ``GetIdentityPoolRoles`` operation.
      - **IdentityPoolId** *(string) --*

        An identity pool ID in the format REGION:GUID.
    """


_ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef = TypedDict(
    "_ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    {"IdentityId": str, "Token": str},
    total=False,
)


class ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef(
    _ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef
):
    """
    - *(dict) --*

      Returned in response to a successful ``GetOpenIdTokenForDeveloperIdentity`` request.
      - **IdentityId** *(string) --*

        A unique identifier in the format REGION:GUID.
    """


_ClientGetOpenIdTokenResponseTypeDef = TypedDict(
    "_ClientGetOpenIdTokenResponseTypeDef", {"IdentityId": str, "Token": str}, total=False
)


class ClientGetOpenIdTokenResponseTypeDef(_ClientGetOpenIdTokenResponseTypeDef):
    """
    - *(dict) --*

      Returned in response to a successful GetOpenIdToken request.
      - **IdentityId** *(string) --*

        A unique identifier in the format REGION:GUID. Note that the IdentityId returned may not
        match the one passed on input.
    """


_ClientListIdentitiesResponseIdentitiesTypeDef = TypedDict(
    "_ClientListIdentitiesResponseIdentitiesTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientListIdentitiesResponseIdentitiesTypeDef(_ClientListIdentitiesResponseIdentitiesTypeDef):
    pass


_ClientListIdentitiesResponseTypeDef = TypedDict(
    "_ClientListIdentitiesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Identities": List[ClientListIdentitiesResponseIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListIdentitiesResponseTypeDef(_ClientListIdentitiesResponseTypeDef):
    """
    - *(dict) --*

      The response to a ListIdentities request.
      - **IdentityPoolId** *(string) --*

        An identity pool ID in the format REGION:GUID.
    """


_ClientListIdentityPoolsResponseIdentityPoolsTypeDef = TypedDict(
    "_ClientListIdentityPoolsResponseIdentityPoolsTypeDef",
    {"IdentityPoolId": str, "IdentityPoolName": str},
    total=False,
)


class ClientListIdentityPoolsResponseIdentityPoolsTypeDef(
    _ClientListIdentityPoolsResponseIdentityPoolsTypeDef
):
    """
    - *(dict) --*

      A description of the identity pool.
      - **IdentityPoolId** *(string) --*

        An identity pool ID in the format REGION:GUID.
    """


_ClientListIdentityPoolsResponseTypeDef = TypedDict(
    "_ClientListIdentityPoolsResponseTypeDef",
    {"IdentityPools": List[ClientListIdentityPoolsResponseIdentityPoolsTypeDef], "NextToken": str},
    total=False,
)


class ClientListIdentityPoolsResponseTypeDef(_ClientListIdentityPoolsResponseTypeDef):
    """
    - *(dict) --*

      The result of a successful ListIdentityPools action.
      - **IdentityPools** *(list) --*

        The identity pools returned by the ListIdentityPools action.
        - *(dict) --*

          A description of the identity pool.
          - **IdentityPoolId** *(string) --*

            An identity pool ID in the format REGION:GUID.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The tags that are assigned to the identity pool.
        - *(string) --*

          - *(string) --*
    """


_ClientLookupDeveloperIdentityResponseTypeDef = TypedDict(
    "_ClientLookupDeveloperIdentityResponseTypeDef",
    {"IdentityId": str, "DeveloperUserIdentifierList": List[str], "NextToken": str},
    total=False,
)


class ClientLookupDeveloperIdentityResponseTypeDef(_ClientLookupDeveloperIdentityResponseTypeDef):
    """
    - *(dict) --*

      Returned in response to a successful ``LookupDeveloperIdentity`` action.
      - **IdentityId** *(string) --*

        A unique identifier in the format REGION:GUID.
    """


_ClientMergeDeveloperIdentitiesResponseTypeDef = TypedDict(
    "_ClientMergeDeveloperIdentitiesResponseTypeDef", {"IdentityId": str}, total=False
)


class ClientMergeDeveloperIdentitiesResponseTypeDef(_ClientMergeDeveloperIdentitiesResponseTypeDef):
    """
    - *(dict) --*

      Returned in response to a successful ``MergeDeveloperIdentities`` action.
      - **IdentityId** *(string) --*

        A unique identifier in the format REGION:GUID.
    """


_ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef = TypedDict(
    "_ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef",
    {
        "Claim": str,
        "MatchType": Literal["Equals", "Contains", "StartsWith", "NotEqual"],
        "Value": str,
        "RoleARN": str,
    },
    total=False,
)


class ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef(
    _ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef
):
    pass


_ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef = TypedDict(
    "_ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef",
    {"Rules": List[ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef]},
    total=False,
)


class ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef(
    _ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef
):
    pass


_ClientSetIdentityPoolRolesRoleMappingsTypeDef = TypedDict(
    "_ClientSetIdentityPoolRolesRoleMappingsTypeDef",
    {
        "Type": Literal["Token", "Rules"],
        "AmbiguousRoleResolution": Literal["AuthenticatedRole", "Deny"],
        "RulesConfiguration": ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef,
    },
    total=False,
)


class ClientSetIdentityPoolRolesRoleMappingsTypeDef(_ClientSetIdentityPoolRolesRoleMappingsTypeDef):
    pass


_ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef(
    _ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef
):
    """
    - *(dict) --*

      A provider representing an Amazon Cognito user pool and its client ID.
      - **ProviderName** *(string) --*

        The provider name for an Amazon Cognito user pool. For example,
        ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .
    """


_ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef(
    _ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef
):
    pass


_ClientUpdateIdentityPoolResponseTypeDef = TypedDict(
    "_ClientUpdateIdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[
            ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef
        ],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateIdentityPoolResponseTypeDef(_ClientUpdateIdentityPoolResponseTypeDef):
    """
    - *(dict) --*

      An object representing an Amazon Cognito identity pool.
      - **IdentityPoolId** *(string) --*

        An identity pool ID in the format REGION:GUID.
    """


_ListIdentityPoolsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIdentityPoolsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIdentityPoolsPaginatePaginationConfigTypeDef(
    _ListIdentityPoolsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef = TypedDict(
    "_ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef",
    {"IdentityPoolId": str, "IdentityPoolName": str},
    total=False,
)


class ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef(
    _ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef
):
    """
    - *(dict) --*

      A description of the identity pool.
      - **IdentityPoolId** *(string) --*

        An identity pool ID in the format REGION:GUID.
    """


_ListIdentityPoolsPaginateResponseTypeDef = TypedDict(
    "_ListIdentityPoolsPaginateResponseTypeDef",
    {"IdentityPools": List[ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef]},
    total=False,
)


class ListIdentityPoolsPaginateResponseTypeDef(_ListIdentityPoolsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The result of a successful ListIdentityPools action.
      - **IdentityPools** *(list) --*

        The identity pools returned by the ListIdentityPools action.
        - *(dict) --*

          A description of the identity pool.
          - **IdentityPoolId** *(string) --*

            An identity pool ID in the format REGION:GUID.
    """
