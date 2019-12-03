"Main interface for iam service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateAccessKeyResponseAccessKeyTypeDef",
    "ClientCreateAccessKeyResponseTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileTypeDef",
    "ClientCreateInstanceProfileResponseTypeDef",
    "ClientCreateLoginProfileResponseLoginProfileTypeDef",
    "ClientCreateLoginProfileResponseTypeDef",
    "ClientCreateOpenIdConnectProviderResponseTypeDef",
    "ClientCreatePolicyResponsePolicyTypeDef",
    "ClientCreatePolicyResponseTypeDef",
    "ClientCreatePolicyVersionResponsePolicyVersionTypeDef",
    "ClientCreatePolicyVersionResponseTypeDef",
    "ClientCreateRoleResponseRolePermissionsBoundaryTypeDef",
    "ClientCreateRoleResponseRoleRoleLastUsedTypeDef",
    "ClientCreateRoleResponseRoleTagsTypeDef",
    "ClientCreateRoleResponseRoleTypeDef",
    "ClientCreateRoleResponseTypeDef",
    "ClientCreateRoleTagsTypeDef",
    "ClientCreateSamlProviderResponseTypeDef",
    "ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef",
    "ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef",
    "ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef",
    "ClientCreateServiceLinkedRoleResponseRoleTypeDef",
    "ClientCreateServiceLinkedRoleResponseTypeDef",
    "ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    "ClientCreateServiceSpecificCredentialResponseTypeDef",
    "ClientCreateUserResponseUserPermissionsBoundaryTypeDef",
    "ClientCreateUserResponseUserTagsTypeDef",
    "ClientCreateUserResponseUserTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserTagsTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef",
    "ClientCreateVirtualMfaDeviceResponseTypeDef",
    "ClientDeleteServiceLinkedRoleResponseTypeDef",
    "ClientGenerateCredentialReportResponseTypeDef",
    "ClientGenerateOrganizationsAccessReportResponseTypeDef",
    "ClientGenerateServiceLastAccessedDetailsResponseTypeDef",
    "ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef",
    "ClientGetAccessKeyLastUsedResponseTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseTypeDef",
    "ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef",
    "ClientGetAccountPasswordPolicyResponseTypeDef",
    "ClientGetAccountSummaryResponseTypeDef",
    "ClientGetContextKeysForCustomPolicyResponseTypeDef",
    "ClientGetContextKeysForPrincipalPolicyResponseTypeDef",
    "ClientGetCredentialReportResponseTypeDef",
    "ClientGetGroupPolicyResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseUsersPermissionsBoundaryTypeDef",
    "ClientGetGroupResponseUsersTagsTypeDef",
    "ClientGetGroupResponseUsersTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileTypeDef",
    "ClientGetInstanceProfileResponseTypeDef",
    "ClientGetLoginProfileResponseLoginProfileTypeDef",
    "ClientGetLoginProfileResponseTypeDef",
    "ClientGetOpenIdConnectProviderResponseTypeDef",
    "ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef",
    "ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef",
    "ClientGetOrganizationsAccessReportResponseTypeDef",
    "ClientGetPolicyResponsePolicyTypeDef",
    "ClientGetPolicyResponseTypeDef",
    "ClientGetPolicyVersionResponsePolicyVersionTypeDef",
    "ClientGetPolicyVersionResponseTypeDef",
    "ClientGetRolePolicyResponseTypeDef",
    "ClientGetRoleResponseRolePermissionsBoundaryTypeDef",
    "ClientGetRoleResponseRoleRoleLastUsedTypeDef",
    "ClientGetRoleResponseRoleTagsTypeDef",
    "ClientGetRoleResponseRoleTypeDef",
    "ClientGetRoleResponseTypeDef",
    "ClientGetSamlProviderResponseTypeDef",
    "ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef",
    "ClientGetServerCertificateResponseServerCertificateTypeDef",
    "ClientGetServerCertificateResponseTypeDef",
    "ClientGetServiceLastAccessedDetailsResponseErrorTypeDef",
    "ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef",
    "ClientGetServiceLastAccessedDetailsResponseTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef",
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef",
    "ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef",
    "ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef",
    "ClientGetSshPublicKeyResponseTypeDef",
    "ClientGetUserPolicyResponseTypeDef",
    "ClientGetUserResponseUserPermissionsBoundaryTypeDef",
    "ClientGetUserResponseUserTagsTypeDef",
    "ClientGetUserResponseUserTypeDef",
    "ClientGetUserResponseTypeDef",
    "ClientListAccessKeysResponseAccessKeyMetadataTypeDef",
    "ClientListAccessKeysResponseTypeDef",
    "ClientListAccountAliasesResponseTypeDef",
    "ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef",
    "ClientListAttachedGroupPoliciesResponseTypeDef",
    "ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef",
    "ClientListAttachedRolePoliciesResponseTypeDef",
    "ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef",
    "ClientListAttachedUserPoliciesResponseTypeDef",
    "ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef",
    "ClientListEntitiesForPolicyResponsePolicyRolesTypeDef",
    "ClientListEntitiesForPolicyResponsePolicyUsersTypeDef",
    "ClientListEntitiesForPolicyResponseTypeDef",
    "ClientListGroupPoliciesResponseTypeDef",
    "ClientListGroupsForUserResponseGroupsTypeDef",
    "ClientListGroupsForUserResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef",
    "ClientListInstanceProfilesForRoleResponseTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesTypeDef",
    "ClientListInstanceProfilesResponseTypeDef",
    "ClientListMfaDevicesResponseMFADevicesTypeDef",
    "ClientListMfaDevicesResponseTypeDef",
    "ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef",
    "ClientListOpenIdConnectProvidersResponseTypeDef",
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef",
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef",
    "ClientListPoliciesGrantingServiceAccessResponseTypeDef",
    "ClientListPoliciesResponsePoliciesTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientListPolicyVersionsResponseVersionsTypeDef",
    "ClientListPolicyVersionsResponseTypeDef",
    "ClientListRolePoliciesResponseTypeDef",
    "ClientListRoleTagsResponseTagsTypeDef",
    "ClientListRoleTagsResponseTypeDef",
    "ClientListRolesResponseRolesPermissionsBoundaryTypeDef",
    "ClientListRolesResponseRolesRoleLastUsedTypeDef",
    "ClientListRolesResponseRolesTagsTypeDef",
    "ClientListRolesResponseRolesTypeDef",
    "ClientListRolesResponseTypeDef",
    "ClientListSamlProvidersResponseSAMLProviderListTypeDef",
    "ClientListSamlProvidersResponseTypeDef",
    "ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef",
    "ClientListServerCertificatesResponseTypeDef",
    "ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef",
    "ClientListServiceSpecificCredentialsResponseTypeDef",
    "ClientListSigningCertificatesResponseCertificatesTypeDef",
    "ClientListSigningCertificatesResponseTypeDef",
    "ClientListSshPublicKeysResponseSSHPublicKeysTypeDef",
    "ClientListSshPublicKeysResponseTypeDef",
    "ClientListUserPoliciesResponseTypeDef",
    "ClientListUserTagsResponseTagsTypeDef",
    "ClientListUserTagsResponseTypeDef",
    "ClientListUsersResponseUsersPermissionsBoundaryTypeDef",
    "ClientListUsersResponseUsersTagsTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef",
    "ClientListVirtualMfaDevicesResponseTypeDef",
    "ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    "ClientResetServiceSpecificCredentialResponseTypeDef",
    "ClientSimulateCustomPolicyContextEntriesTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef",
    "ClientSimulateCustomPolicyResponseTypeDef",
    "ClientSimulatePrincipalPolicyContextEntriesTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef",
    "ClientSimulatePrincipalPolicyResponseTypeDef",
    "ClientTagRoleTagsTypeDef",
    "ClientTagUserTagsTypeDef",
    "ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef",
    "ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef",
    "ClientUpdateRoleDescriptionResponseRoleTagsTypeDef",
    "ClientUpdateRoleDescriptionResponseRoleTypeDef",
    "ClientUpdateRoleDescriptionResponseTypeDef",
    "ClientUpdateSamlProviderResponseTypeDef",
    "ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef",
    "ClientUploadServerCertificateResponseTypeDef",
    "ClientUploadSigningCertificateResponseCertificateTypeDef",
    "ClientUploadSigningCertificateResponseTypeDef",
    "ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef",
    "ClientUploadSshPublicKeyResponseTypeDef",
    "GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseTypeDef",
    "GetGroupPaginatePaginationConfigTypeDef",
    "GetGroupPaginateResponseGroupTypeDef",
    "GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef",
    "GetGroupPaginateResponseUsersTagsTypeDef",
    "GetGroupPaginateResponseUsersTypeDef",
    "GetGroupPaginateResponseTypeDef",
    "InstanceProfileExistsWaitWaiterConfigTypeDef",
    "ListAccessKeysPaginatePaginationConfigTypeDef",
    "ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef",
    "ListAccessKeysPaginateResponseTypeDef",
    "ListAccountAliasesPaginatePaginationConfigTypeDef",
    "ListAccountAliasesPaginateResponseTypeDef",
    "ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef",
    "ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef",
    "ListAttachedGroupPoliciesPaginateResponseTypeDef",
    "ListAttachedRolePoliciesPaginatePaginationConfigTypeDef",
    "ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef",
    "ListAttachedRolePoliciesPaginateResponseTypeDef",
    "ListAttachedUserPoliciesPaginatePaginationConfigTypeDef",
    "ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef",
    "ListAttachedUserPoliciesPaginateResponseTypeDef",
    "ListEntitiesForPolicyPaginatePaginationConfigTypeDef",
    "ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef",
    "ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef",
    "ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef",
    "ListEntitiesForPolicyPaginateResponseTypeDef",
    "ListGroupPoliciesPaginatePaginationConfigTypeDef",
    "ListGroupPoliciesPaginateResponseTypeDef",
    "ListGroupsForUserPaginatePaginationConfigTypeDef",
    "ListGroupsForUserPaginateResponseGroupsTypeDef",
    "ListGroupsForUserPaginateResponseTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "ListInstanceProfilesForRolePaginatePaginationConfigTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef",
    "ListInstanceProfilesForRolePaginateResponseTypeDef",
    "ListInstanceProfilesPaginatePaginationConfigTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef",
    "ListInstanceProfilesPaginateResponseTypeDef",
    "ListMFADevicesPaginatePaginationConfigTypeDef",
    "ListMFADevicesPaginateResponseMFADevicesTypeDef",
    "ListMFADevicesPaginateResponseTypeDef",
    "ListPoliciesPaginatePaginationConfigTypeDef",
    "ListPoliciesPaginateResponsePoliciesTypeDef",
    "ListPoliciesPaginateResponseTypeDef",
    "ListPolicyVersionsPaginatePaginationConfigTypeDef",
    "ListPolicyVersionsPaginateResponseVersionsTypeDef",
    "ListPolicyVersionsPaginateResponseTypeDef",
    "ListRolePoliciesPaginatePaginationConfigTypeDef",
    "ListRolePoliciesPaginateResponseTypeDef",
    "ListRolesPaginatePaginationConfigTypeDef",
    "ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef",
    "ListRolesPaginateResponseRolesRoleLastUsedTypeDef",
    "ListRolesPaginateResponseRolesTagsTypeDef",
    "ListRolesPaginateResponseRolesTypeDef",
    "ListRolesPaginateResponseTypeDef",
    "ListSSHPublicKeysPaginatePaginationConfigTypeDef",
    "ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef",
    "ListSSHPublicKeysPaginateResponseTypeDef",
    "ListServerCertificatesPaginatePaginationConfigTypeDef",
    "ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef",
    "ListServerCertificatesPaginateResponseTypeDef",
    "ListSigningCertificatesPaginatePaginationConfigTypeDef",
    "ListSigningCertificatesPaginateResponseCertificatesTypeDef",
    "ListSigningCertificatesPaginateResponseTypeDef",
    "ListUserPoliciesPaginatePaginationConfigTypeDef",
    "ListUserPoliciesPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef",
    "ListUsersPaginateResponseUsersTagsTypeDef",
    "ListUsersPaginateResponseUsersTypeDef",
    "ListUsersPaginateResponseTypeDef",
    "ListVirtualMFADevicesPaginatePaginationConfigTypeDef",
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef",
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef",
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef",
    "ListVirtualMFADevicesPaginateResponseTypeDef",
    "PolicyExistsWaitWaiterConfigTypeDef",
    "RoleExistsWaitWaiterConfigTypeDef",
    "SamlProviderUpdateResponseTypeDef",
    "ServiceResourceCreateRoleTagsTypeDef",
    "ServiceResourceCreateUserTagsTypeDef",
    "SimulateCustomPolicyPaginateContextEntriesTypeDef",
    "SimulateCustomPolicyPaginatePaginationConfigTypeDef",
    "SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    "SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    "SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef",
    "SimulateCustomPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    "SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    "SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    "SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    "SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef",
    "SimulateCustomPolicyPaginateResponseEvaluationResultsTypeDef",
    "SimulateCustomPolicyPaginateResponseTypeDef",
    "SimulatePrincipalPolicyPaginateContextEntriesTypeDef",
    "SimulatePrincipalPolicyPaginatePaginationConfigTypeDef",
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef",
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef",
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsTypeDef",
    "SimulatePrincipalPolicyPaginateResponseTypeDef",
    "UserCreateTagsTypeDef",
    "UserExistsWaitWaiterConfigTypeDef",
)


_ClientCreateAccessKeyResponseAccessKeyTypeDef = TypedDict(
    "_ClientCreateAccessKeyResponseAccessKeyTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "SecretAccessKey": str,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientCreateAccessKeyResponseAccessKeyTypeDef(_ClientCreateAccessKeyResponseAccessKeyTypeDef):
    """
    - **AccessKey** *(dict) --*

      A structure with details about the access key.
      - **UserName** *(string) --*

        The name of the IAM user that the access key is associated with.
    """


_ClientCreateAccessKeyResponseTypeDef = TypedDict(
    "_ClientCreateAccessKeyResponseTypeDef",
    {"AccessKey": ClientCreateAccessKeyResponseAccessKeyTypeDef},
    total=False,
)


class ClientCreateAccessKeyResponseTypeDef(_ClientCreateAccessKeyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreateAccessKey request.
      - **AccessKey** *(dict) --*

        A structure with details about the access key.
        - **UserName** *(string) --*

          The name of the IAM user that the access key is associated with.
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      A structure containing details about the new group.
      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreateGroup request.
      - **Group** *(dict) --*

        A structure containing details about the new group.
        - **Path** *(string) --*

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef
):
    pass


_ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef
):
    pass


_ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef
):
    pass


_ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef],
        "RoleLastUsed": ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef
):
    pass


_ClientCreateInstanceProfileResponseInstanceProfileTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef],
    },
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileTypeDef
):
    """
    - **InstanceProfile** *(dict) --*

      A structure containing details about the new instance profile.
      - **Path** *(string) --*

        The path to the instance profile. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientCreateInstanceProfileResponseTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseTypeDef",
    {"InstanceProfile": ClientCreateInstanceProfileResponseInstanceProfileTypeDef},
    total=False,
)


class ClientCreateInstanceProfileResponseTypeDef(_ClientCreateInstanceProfileResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreateInstanceProfile request.
      - **InstanceProfile** *(dict) --*

        A structure containing details about the new instance profile.
        - **Path** *(string) --*

          The path to the instance profile. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientCreateLoginProfileResponseLoginProfileTypeDef = TypedDict(
    "_ClientCreateLoginProfileResponseLoginProfileTypeDef",
    {"UserName": str, "CreateDate": datetime, "PasswordResetRequired": bool},
    total=False,
)


class ClientCreateLoginProfileResponseLoginProfileTypeDef(
    _ClientCreateLoginProfileResponseLoginProfileTypeDef
):
    """
    - **LoginProfile** *(dict) --*

      A structure containing the user name and password create date.
      - **UserName** *(string) --*

        The name of the user, which can be used for signing in to the AWS Management Console.
    """


_ClientCreateLoginProfileResponseTypeDef = TypedDict(
    "_ClientCreateLoginProfileResponseTypeDef",
    {"LoginProfile": ClientCreateLoginProfileResponseLoginProfileTypeDef},
    total=False,
)


class ClientCreateLoginProfileResponseTypeDef(_ClientCreateLoginProfileResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreateLoginProfile request.
      - **LoginProfile** *(dict) --*

        A structure containing the user name and password create date.
        - **UserName** *(string) --*

          The name of the user, which can be used for signing in to the AWS Management Console.
    """


_ClientCreateOpenIdConnectProviderResponseTypeDef = TypedDict(
    "_ClientCreateOpenIdConnectProviderResponseTypeDef",
    {"OpenIDConnectProviderArn": str},
    total=False,
)


class ClientCreateOpenIdConnectProviderResponseTypeDef(
    _ClientCreateOpenIdConnectProviderResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  CreateOpenIDConnectProvider request.
      - **OpenIDConnectProviderArn** *(string) --*

        The Amazon Resource Name (ARN) of the new IAM OpenID Connect provider that is created. For
        more information, see  OpenIDConnectProviderListEntry .
    """


_ClientCreatePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientCreatePolicyResponsePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)


class ClientCreatePolicyResponsePolicyTypeDef(_ClientCreatePolicyResponsePolicyTypeDef):
    """
    - **Policy** *(dict) --*

      A structure containing details about the new policy.
      - **PolicyName** *(string) --*

        The friendly name (not ARN) identifying the policy.
    """


_ClientCreatePolicyResponseTypeDef = TypedDict(
    "_ClientCreatePolicyResponseTypeDef",
    {"Policy": ClientCreatePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientCreatePolicyResponseTypeDef(_ClientCreatePolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreatePolicy request.
      - **Policy** *(dict) --*

        A structure containing details about the new policy.
        - **PolicyName** *(string) --*

          The friendly name (not ARN) identifying the policy.
    """


_ClientCreatePolicyVersionResponsePolicyVersionTypeDef = TypedDict(
    "_ClientCreatePolicyVersionResponsePolicyVersionTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)


class ClientCreatePolicyVersionResponsePolicyVersionTypeDef(
    _ClientCreatePolicyVersionResponsePolicyVersionTypeDef
):
    """
    - **PolicyVersion** *(dict) --*

      A structure containing details about the new policy version.
      - **Document** *(string) --*

        The policy document.
        The policy document is returned in the response to the  GetPolicyVersion and
        GetAccountAuthorizationDetails operations. It is not returned in the response to the
        CreatePolicyVersion or  ListPolicyVersions operations.
        The policy document returned in this structure is URL-encoded compliant with `RFC 3986
        <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the
        policy back to plain JSON text. For example, if you use Java, you can use the ``decode``
        method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and
        SDKs provide similar functionality.
    """


_ClientCreatePolicyVersionResponseTypeDef = TypedDict(
    "_ClientCreatePolicyVersionResponseTypeDef",
    {"PolicyVersion": ClientCreatePolicyVersionResponsePolicyVersionTypeDef},
    total=False,
)


class ClientCreatePolicyVersionResponseTypeDef(_ClientCreatePolicyVersionResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreatePolicyVersion request.
      - **PolicyVersion** *(dict) --*

        A structure containing details about the new policy version.
        - **Document** *(string) --*

          The policy document.
          The policy document is returned in the response to the  GetPolicyVersion and
          GetAccountAuthorizationDetails operations. It is not returned in the response to the
          CreatePolicyVersion or  ListPolicyVersions operations.
          The policy document returned in this structure is URL-encoded compliant with `RFC 3986
          <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert
          the policy back to plain JSON text. For example, if you use Java, you can use the
          ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other
          languages and SDKs provide similar functionality.
    """


_ClientCreateRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateRoleResponseRolePermissionsBoundaryTypeDef(
    _ClientCreateRoleResponseRolePermissionsBoundaryTypeDef
):
    pass


_ClientCreateRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "_ClientCreateRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientCreateRoleResponseRoleRoleLastUsedTypeDef(
    _ClientCreateRoleResponseRoleRoleLastUsedTypeDef
):
    pass


_ClientCreateRoleResponseRoleTagsTypeDef = TypedDict(
    "_ClientCreateRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRoleResponseRoleTagsTypeDef(_ClientCreateRoleResponseRoleTagsTypeDef):
    pass


_ClientCreateRoleResponseRoleTypeDef = TypedDict(
    "_ClientCreateRoleResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientCreateRoleResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateRoleResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientCreateRoleResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientCreateRoleResponseRoleTypeDef(_ClientCreateRoleResponseRoleTypeDef):
    """
    - **Role** *(dict) --*

      A structure containing details about the new role.
      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientCreateRoleResponseTypeDef = TypedDict(
    "_ClientCreateRoleResponseTypeDef", {"Role": ClientCreateRoleResponseRoleTypeDef}, total=False
)


class ClientCreateRoleResponseTypeDef(_ClientCreateRoleResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreateRole request.
      - **Role** *(dict) --*

        A structure containing details about the new role.
        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientCreateRoleTagsTypeDef = TypedDict(
    "_ClientCreateRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRoleTagsTypeDef(_ClientCreateRoleTagsTypeDef):
    pass


_ClientCreateSamlProviderResponseTypeDef = TypedDict(
    "_ClientCreateSamlProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)


class ClientCreateSamlProviderResponseTypeDef(_ClientCreateSamlProviderResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreateSAMLProvider request.
      - **SAMLProviderArn** *(string) --*

        The Amazon Resource Name (ARN) of the new SAML provider resource in IAM.
    """


_ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef(
    _ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef
):
    pass


_ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef(
    _ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef
):
    pass


_ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef(
    _ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef
):
    pass


_ClientCreateServiceLinkedRoleResponseRoleTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientCreateServiceLinkedRoleResponseRoleTypeDef(
    _ClientCreateServiceLinkedRoleResponseRoleTypeDef
):
    """
    - **Role** *(dict) --*

      A  Role object that contains details about the newly created role.
      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientCreateServiceLinkedRoleResponseTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseTypeDef",
    {"Role": ClientCreateServiceLinkedRoleResponseRoleTypeDef},
    total=False,
)


class ClientCreateServiceLinkedRoleResponseTypeDef(_ClientCreateServiceLinkedRoleResponseTypeDef):
    """
    - *(dict) --*

      - **Role** *(dict) --*

        A  Role object that contains details about the newly created role.
        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef = TypedDict(
    "_ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
    },
    total=False,
)


class ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef(
    _ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
):
    """
    - **ServiceSpecificCredential** *(dict) --*

      A structure that contains information about the newly created service-specific credential.
      .. warning::

        This is the only time that the password for this credential set is available. It cannot be
        recovered later. Instead, you must reset the password with  ResetServiceSpecificCredential .
    """


_ClientCreateServiceSpecificCredentialResponseTypeDef = TypedDict(
    "_ClientCreateServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
    },
    total=False,
)


class ClientCreateServiceSpecificCredentialResponseTypeDef(
    _ClientCreateServiceSpecificCredentialResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceSpecificCredential** *(dict) --*

        A structure that contains information about the newly created service-specific credential.
        .. warning::

          This is the only time that the password for this credential set is available. It cannot be
          recovered later. Instead, you must reset the password with  ResetServiceSpecificCredential
          .
    """


_ClientCreateUserResponseUserPermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateUserResponseUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateUserResponseUserPermissionsBoundaryTypeDef(
    _ClientCreateUserResponseUserPermissionsBoundaryTypeDef
):
    pass


_ClientCreateUserResponseUserTagsTypeDef = TypedDict(
    "_ClientCreateUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateUserResponseUserTagsTypeDef(_ClientCreateUserResponseUserTagsTypeDef):
    pass


_ClientCreateUserResponseUserTypeDef = TypedDict(
    "_ClientCreateUserResponseUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientCreateUserResponseUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateUserResponseUserTagsTypeDef],
    },
    total=False,
)


class ClientCreateUserResponseUserTypeDef(_ClientCreateUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      A structure with details about the new IAM user.
      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"User": ClientCreateUserResponseUserTypeDef}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreateUser request.
      - **User** *(dict) --*

        A structure with details about the new IAM user.
        - **Path** *(string) --*

          The path to the user. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientCreateUserTagsTypeDef = TypedDict(
    "_ClientCreateUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateUserTagsTypeDef(_ClientCreateUserTagsTypeDef):
    pass


_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef(
    _ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef
):
    pass


_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef(
    _ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef
):
    pass


_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef],
    },
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef(
    _ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef
):
    pass


_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef(
    _ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef
):
    """
    - **VirtualMFADevice** *(dict) --*

      A structure containing details about the new virtual MFA device.
      - **SerialNumber** *(string) --*

        The serial number associated with ``VirtualMFADevice`` .
    """


_ClientCreateVirtualMfaDeviceResponseTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseTypeDef",
    {"VirtualMFADevice": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef},
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseTypeDef(_ClientCreateVirtualMfaDeviceResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  CreateVirtualMFADevice request.
      - **VirtualMFADevice** *(dict) --*

        A structure containing details about the new virtual MFA device.
        - **SerialNumber** *(string) --*

          The serial number associated with ``VirtualMFADevice`` .
    """


_ClientDeleteServiceLinkedRoleResponseTypeDef = TypedDict(
    "_ClientDeleteServiceLinkedRoleResponseTypeDef", {"DeletionTaskId": str}, total=False
)


class ClientDeleteServiceLinkedRoleResponseTypeDef(_ClientDeleteServiceLinkedRoleResponseTypeDef):
    """
    - *(dict) --*

      - **DeletionTaskId** *(string) --*

        The deletion task identifier that you can use to check the status of the deletion. This
        identifier is returned in the format
        ``task/aws-service-role/<service-principal-name>/<role-name>/<task-uuid>`` .
    """


_ClientGenerateCredentialReportResponseTypeDef = TypedDict(
    "_ClientGenerateCredentialReportResponseTypeDef",
    {"State": Literal["STARTED", "INPROGRESS", "COMPLETE"], "Description": str},
    total=False,
)


class ClientGenerateCredentialReportResponseTypeDef(_ClientGenerateCredentialReportResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GenerateCredentialReport request.
      - **State** *(string) --*

        Information about the state of the credential report.
    """


_ClientGenerateOrganizationsAccessReportResponseTypeDef = TypedDict(
    "_ClientGenerateOrganizationsAccessReportResponseTypeDef", {"JobId": str}, total=False
)


class ClientGenerateOrganizationsAccessReportResponseTypeDef(
    _ClientGenerateOrganizationsAccessReportResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The job identifier that you can use in the  GetOrganizationsAccessReport operation.
    """


_ClientGenerateServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "_ClientGenerateServiceLastAccessedDetailsResponseTypeDef", {"JobId": str}, total=False
)


class ClientGenerateServiceLastAccessedDetailsResponseTypeDef(
    _ClientGenerateServiceLastAccessedDetailsResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The job ID that you can use in the  GetServiceLastAccessedDetails or
        GetServiceLastAccessedDetailsWithEntities operations.
    """


_ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef = TypedDict(
    "_ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef",
    {"LastUsedDate": datetime, "ServiceName": str, "Region": str},
    total=False,
)


class ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef(
    _ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef
):
    pass


_ClientGetAccessKeyLastUsedResponseTypeDef = TypedDict(
    "_ClientGetAccessKeyLastUsedResponseTypeDef",
    {
        "UserName": str,
        "AccessKeyLastUsed": ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef,
    },
    total=False,
)


class ClientGetAccessKeyLastUsedResponseTypeDef(_ClientGetAccessKeyLastUsedResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetAccessKeyLastUsed request. It is also returned as a
      member of the  AccessKeyMetaData structure returned by the  ListAccessKeys action.
      - **UserName** *(string) --*

        The name of the AWS IAM user that owns this access key.
    """


_ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
        "GroupPolicyList": List[
            ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef
        ],
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "PolicyVersionList": List[
            ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef
        ],
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef
        ],
        "RoleLastUsed": ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef
        ],
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "InstanceProfileList": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef
        ],
        "RolePolicyList": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef],
        "RoleLastUsed": ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef
):
    pass


_ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "UserPolicyList": List[
            ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef
        ],
        "GroupList": List[str],
        "AttachedManagedPolicies": List[
            ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef],
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef
):
    """
    - *(dict) --*

      Contains information about an IAM user, including all the user's policies and all the IAM
      groups the user is in.
      This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientGetAccountAuthorizationDetailsResponseTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseTypeDef",
    {
        "UserDetailList": List[ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef],
        "GroupDetailList": List[ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef],
        "RoleDetailList": List[ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef],
        "Policies": List[ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  GetAccountAuthorizationDetails request.
      - **UserDetailList** *(list) --*

        A list containing information about IAM users.
        - *(dict) --*

          Contains information about an IAM user, including all the user's policies and all the IAM
          groups the user is in.
          This data type is used as a response element in the  GetAccountAuthorizationDetails
          operation.
          - **Path** *(string) --*

            The path to the user. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef = TypedDict(
    "_ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "ExpirePasswords": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)


class ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef(
    _ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef
):
    """
    - **PasswordPolicy** *(dict) --*

      A structure that contains details about the account's password policy.
      - **MinimumPasswordLength** *(integer) --*

        Minimum length to require for IAM user passwords.
    """


_ClientGetAccountPasswordPolicyResponseTypeDef = TypedDict(
    "_ClientGetAccountPasswordPolicyResponseTypeDef",
    {"PasswordPolicy": ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef},
    total=False,
)


class ClientGetAccountPasswordPolicyResponseTypeDef(_ClientGetAccountPasswordPolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetAccountPasswordPolicy request.
      - **PasswordPolicy** *(dict) --*

        A structure that contains details about the account's password policy.
        - **MinimumPasswordLength** *(integer) --*

          Minimum length to require for IAM user passwords.
    """


_ClientGetAccountSummaryResponseTypeDef = TypedDict(
    "_ClientGetAccountSummaryResponseTypeDef", {"SummaryMap": Dict[str, int]}, total=False
)


class ClientGetAccountSummaryResponseTypeDef(_ClientGetAccountSummaryResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetAccountSummary request.
      - **SummaryMap** *(dict) --*

        A set of key–value pairs containing information about IAM entity usage and IAM quotas.
        - *(string) --*

          - *(integer) --*
    """


_ClientGetContextKeysForCustomPolicyResponseTypeDef = TypedDict(
    "_ClientGetContextKeysForCustomPolicyResponseTypeDef",
    {"ContextKeyNames": List[str]},
    total=False,
)


class ClientGetContextKeysForCustomPolicyResponseTypeDef(
    _ClientGetContextKeysForCustomPolicyResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  GetContextKeysForPrincipalPolicy or
      GetContextKeysForCustomPolicy request.
      - **ContextKeyNames** *(list) --*

        The list of context keys that are referenced in the input policies.
        - *(string) --*
    """


_ClientGetContextKeysForPrincipalPolicyResponseTypeDef = TypedDict(
    "_ClientGetContextKeysForPrincipalPolicyResponseTypeDef",
    {"ContextKeyNames": List[str]},
    total=False,
)


class ClientGetContextKeysForPrincipalPolicyResponseTypeDef(
    _ClientGetContextKeysForPrincipalPolicyResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  GetContextKeysForPrincipalPolicy or
      GetContextKeysForCustomPolicy request.
      - **ContextKeyNames** *(list) --*

        The list of context keys that are referenced in the input policies.
        - *(string) --*
    """


_ClientGetCredentialReportResponseTypeDef = TypedDict(
    "_ClientGetCredentialReportResponseTypeDef",
    {"Content": bytes, "ReportFormat": str, "GeneratedTime": datetime},
    total=False,
)


class ClientGetCredentialReportResponseTypeDef(_ClientGetCredentialReportResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetCredentialReport request.
      - **Content** *(bytes) --*

        Contains the credential report. The report is Base64-encoded.
    """


_ClientGetGroupPolicyResponseTypeDef = TypedDict(
    "_ClientGetGroupPolicyResponseTypeDef",
    {"GroupName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetGroupPolicyResponseTypeDef(_ClientGetGroupPolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetGroupPolicy request.
      - **GroupName** *(string) --*

        The group the policy is associated with.
    """


_ClientGetGroupResponseGroupTypeDef = TypedDict(
    "_ClientGetGroupResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ClientGetGroupResponseGroupTypeDef(_ClientGetGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      A structure that contains details about the group.
      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientGetGroupResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetGroupResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetGroupResponseUsersPermissionsBoundaryTypeDef(
    _ClientGetGroupResponseUsersPermissionsBoundaryTypeDef
):
    pass


_ClientGetGroupResponseUsersTagsTypeDef = TypedDict(
    "_ClientGetGroupResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetGroupResponseUsersTagsTypeDef(_ClientGetGroupResponseUsersTagsTypeDef):
    pass


_ClientGetGroupResponseUsersTypeDef = TypedDict(
    "_ClientGetGroupResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientGetGroupResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetGroupResponseUsersTagsTypeDef],
    },
    total=False,
)


class ClientGetGroupResponseUsersTypeDef(_ClientGetGroupResponseUsersTypeDef):
    pass


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef",
    {
        "Group": ClientGetGroupResponseGroupTypeDef,
        "Users": List[ClientGetGroupResponseUsersTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetGroup request.
      - **Group** *(dict) --*

        A structure that contains details about the group.
        - **Path** *(string) --*

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef
):
    pass


_ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef
):
    pass


_ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef
):
    pass


_ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef],
        "RoleLastUsed": ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef
):
    pass


_ClientGetInstanceProfileResponseInstanceProfileTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef],
    },
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileTypeDef
):
    """
    - **InstanceProfile** *(dict) --*

      A structure containing details about the instance profile.
      - **Path** *(string) --*

        The path to the instance profile. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientGetInstanceProfileResponseTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseTypeDef",
    {"InstanceProfile": ClientGetInstanceProfileResponseInstanceProfileTypeDef},
    total=False,
)


class ClientGetInstanceProfileResponseTypeDef(_ClientGetInstanceProfileResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetInstanceProfile request.
      - **InstanceProfile** *(dict) --*

        A structure containing details about the instance profile.
        - **Path** *(string) --*

          The path to the instance profile. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientGetLoginProfileResponseLoginProfileTypeDef = TypedDict(
    "_ClientGetLoginProfileResponseLoginProfileTypeDef",
    {"UserName": str, "CreateDate": datetime, "PasswordResetRequired": bool},
    total=False,
)


class ClientGetLoginProfileResponseLoginProfileTypeDef(
    _ClientGetLoginProfileResponseLoginProfileTypeDef
):
    """
    - **LoginProfile** *(dict) --*

      A structure containing the user name and password create date for the user.
      - **UserName** *(string) --*

        The name of the user, which can be used for signing in to the AWS Management Console.
    """


_ClientGetLoginProfileResponseTypeDef = TypedDict(
    "_ClientGetLoginProfileResponseTypeDef",
    {"LoginProfile": ClientGetLoginProfileResponseLoginProfileTypeDef},
    total=False,
)


class ClientGetLoginProfileResponseTypeDef(_ClientGetLoginProfileResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetLoginProfile request.
      - **LoginProfile** *(dict) --*

        A structure containing the user name and password create date for the user.
        - **UserName** *(string) --*

          The name of the user, which can be used for signing in to the AWS Management Console.
    """


_ClientGetOpenIdConnectProviderResponseTypeDef = TypedDict(
    "_ClientGetOpenIdConnectProviderResponseTypeDef",
    {"Url": str, "ClientIDList": List[str], "ThumbprintList": List[str], "CreateDate": datetime},
    total=False,
)


class ClientGetOpenIdConnectProviderResponseTypeDef(_ClientGetOpenIdConnectProviderResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetOpenIDConnectProvider request.
      - **Url** *(string) --*

        The URL that the IAM OIDC provider resource object is associated with. For more information,
        see  CreateOpenIDConnectProvider .
    """


_ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef = TypedDict(
    "_ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
        "Region": str,
        "EntityPath": str,
        "LastAuthenticatedTime": datetime,
        "TotalAuthenticatedEntities": int,
    },
    total=False,
)


class ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef(
    _ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef
):
    pass


_ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef = TypedDict(
    "_ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef",
    {"Message": str, "Code": str},
    total=False,
)


class ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef(
    _ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef
):
    pass


_ClientGetOrganizationsAccessReportResponseTypeDef = TypedDict(
    "_ClientGetOrganizationsAccessReportResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED"],
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "NumberOfServicesAccessible": int,
        "NumberOfServicesNotAccessed": int,
        "AccessDetails": List[ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ErrorDetails": ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef,
    },
    total=False,
)


class ClientGetOrganizationsAccessReportResponseTypeDef(
    _ClientGetOrganizationsAccessReportResponseTypeDef
):
    """
    - *(dict) --*

      - **JobStatus** *(string) --*

        The status of the job.
    """


_ClientGetPolicyResponsePolicyTypeDef = TypedDict(
    "_ClientGetPolicyResponsePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)


class ClientGetPolicyResponsePolicyTypeDef(_ClientGetPolicyResponsePolicyTypeDef):
    """
    - **Policy** *(dict) --*

      A structure containing details about the policy.
      - **PolicyName** *(string) --*

        The friendly name (not ARN) identifying the policy.
    """


_ClientGetPolicyResponseTypeDef = TypedDict(
    "_ClientGetPolicyResponseTypeDef", {"Policy": ClientGetPolicyResponsePolicyTypeDef}, total=False
)


class ClientGetPolicyResponseTypeDef(_ClientGetPolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetPolicy request.
      - **Policy** *(dict) --*

        A structure containing details about the policy.
        - **PolicyName** *(string) --*

          The friendly name (not ARN) identifying the policy.
    """


_ClientGetPolicyVersionResponsePolicyVersionTypeDef = TypedDict(
    "_ClientGetPolicyVersionResponsePolicyVersionTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)


class ClientGetPolicyVersionResponsePolicyVersionTypeDef(
    _ClientGetPolicyVersionResponsePolicyVersionTypeDef
):
    """
    - **PolicyVersion** *(dict) --*

      A structure containing details about the policy version.
      - **Document** *(string) --*

        The policy document.
        The policy document is returned in the response to the  GetPolicyVersion and
        GetAccountAuthorizationDetails operations. It is not returned in the response to the
        CreatePolicyVersion or  ListPolicyVersions operations.
        The policy document returned in this structure is URL-encoded compliant with `RFC 3986
        <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the
        policy back to plain JSON text. For example, if you use Java, you can use the ``decode``
        method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and
        SDKs provide similar functionality.
    """


_ClientGetPolicyVersionResponseTypeDef = TypedDict(
    "_ClientGetPolicyVersionResponseTypeDef",
    {"PolicyVersion": ClientGetPolicyVersionResponsePolicyVersionTypeDef},
    total=False,
)


class ClientGetPolicyVersionResponseTypeDef(_ClientGetPolicyVersionResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetPolicyVersion request.
      - **PolicyVersion** *(dict) --*

        A structure containing details about the policy version.
        - **Document** *(string) --*

          The policy document.
          The policy document is returned in the response to the  GetPolicyVersion and
          GetAccountAuthorizationDetails operations. It is not returned in the response to the
          CreatePolicyVersion or  ListPolicyVersions operations.
          The policy document returned in this structure is URL-encoded compliant with `RFC 3986
          <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert
          the policy back to plain JSON text. For example, if you use Java, you can use the
          ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other
          languages and SDKs provide similar functionality.
    """


_ClientGetRolePolicyResponseTypeDef = TypedDict(
    "_ClientGetRolePolicyResponseTypeDef",
    {"RoleName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetRolePolicyResponseTypeDef(_ClientGetRolePolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetRolePolicy request.
      - **RoleName** *(string) --*

        The role the policy is associated with.
    """


_ClientGetRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetRoleResponseRolePermissionsBoundaryTypeDef(
    _ClientGetRoleResponseRolePermissionsBoundaryTypeDef
):
    pass


_ClientGetRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "_ClientGetRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientGetRoleResponseRoleRoleLastUsedTypeDef(_ClientGetRoleResponseRoleRoleLastUsedTypeDef):
    pass


_ClientGetRoleResponseRoleTagsTypeDef = TypedDict(
    "_ClientGetRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetRoleResponseRoleTagsTypeDef(_ClientGetRoleResponseRoleTagsTypeDef):
    pass


_ClientGetRoleResponseRoleTypeDef = TypedDict(
    "_ClientGetRoleResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientGetRoleResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientGetRoleResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientGetRoleResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientGetRoleResponseRoleTypeDef(_ClientGetRoleResponseRoleTypeDef):
    """
    - **Role** *(dict) --*

      A structure containing details about the IAM role.
      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientGetRoleResponseTypeDef = TypedDict(
    "_ClientGetRoleResponseTypeDef", {"Role": ClientGetRoleResponseRoleTypeDef}, total=False
)


class ClientGetRoleResponseTypeDef(_ClientGetRoleResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetRole request.
      - **Role** *(dict) --*

        A structure containing details about the IAM role.
        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientGetSamlProviderResponseTypeDef = TypedDict(
    "_ClientGetSamlProviderResponseTypeDef",
    {"SAMLMetadataDocument": str, "CreateDate": datetime, "ValidUntil": datetime},
    total=False,
)


class ClientGetSamlProviderResponseTypeDef(_ClientGetSamlProviderResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetSAMLProvider request.
      - **SAMLMetadataDocument** *(string) --*

        The XML metadata document that includes information about an identity provider.
    """


_ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef = TypedDict(
    "_ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)


class ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef(
    _ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef
):
    """
    - **ServerCertificateMetadata** *(dict) --*

      The meta information of the server certificate, such as its name, path, ID, and ARN.
      - **Path** *(string) --*

        The path to the server certificate. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientGetServerCertificateResponseServerCertificateTypeDef = TypedDict(
    "_ClientGetServerCertificateResponseServerCertificateTypeDef",
    {
        "ServerCertificateMetadata": ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef,
        "CertificateBody": str,
        "CertificateChain": str,
    },
    total=False,
)


class ClientGetServerCertificateResponseServerCertificateTypeDef(
    _ClientGetServerCertificateResponseServerCertificateTypeDef
):
    """
    - **ServerCertificate** *(dict) --*

      A structure containing details about the server certificate.
      - **ServerCertificateMetadata** *(dict) --*

        The meta information of the server certificate, such as its name, path, ID, and ARN.
        - **Path** *(string) --*

          The path to the server certificate. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientGetServerCertificateResponseTypeDef = TypedDict(
    "_ClientGetServerCertificateResponseTypeDef",
    {"ServerCertificate": ClientGetServerCertificateResponseServerCertificateTypeDef},
    total=False,
)


class ClientGetServerCertificateResponseTypeDef(_ClientGetServerCertificateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetServerCertificate request.
      - **ServerCertificate** *(dict) --*

        A structure containing details about the server certificate.
        - **ServerCertificateMetadata** *(dict) --*

          The meta information of the server certificate, such as its name, path, ID, and ARN.
          - **Path** *(string) --*

            The path to the server certificate. For more information about paths, see `IAM
            Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
            in the *IAM User Guide* .
    """


_ClientGetServiceLastAccessedDetailsResponseErrorTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsResponseErrorTypeDef",
    {"Message": str, "Code": str},
    total=False,
)


class ClientGetServiceLastAccessedDetailsResponseErrorTypeDef(
    _ClientGetServiceLastAccessedDetailsResponseErrorTypeDef
):
    pass


_ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef",
    {
        "ServiceName": str,
        "LastAuthenticated": datetime,
        "ServiceNamespace": str,
        "LastAuthenticatedEntity": str,
        "TotalAuthenticatedEntities": int,
    },
    total=False,
)


class ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef(
    _ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef
):
    pass


_ClientGetServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED"],
        "JobCreationDate": datetime,
        "ServicesLastAccessed": List[
            ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef
        ],
        "JobCompletionDate": datetime,
        "IsTruncated": bool,
        "Marker": str,
        "Error": ClientGetServiceLastAccessedDetailsResponseErrorTypeDef,
    },
    total=False,
)


class ClientGetServiceLastAccessedDetailsResponseTypeDef(
    _ClientGetServiceLastAccessedDetailsResponseTypeDef
):
    """
    - *(dict) --*

      - **JobStatus** *(string) --*

        The status of the job.
    """


_ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef",
    {"Arn": str, "Name": str, "Type": Literal["USER", "ROLE", "GROUP"], "Id": str, "Path": str},
    total=False,
)


class ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef(
    _ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef
):
    pass


_ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef",
    {
        "EntityInfo": ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef,
        "LastAuthenticated": datetime,
    },
    total=False,
)


class ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef(
    _ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef
):
    pass


_ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef",
    {"Message": str, "Code": str},
    total=False,
)


class ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef(
    _ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef
):
    pass


_ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED"],
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "EntityDetailsList": List[
            ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
        "Error": ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef,
    },
    total=False,
)


class ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef(
    _ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef
):
    """
    - *(dict) --*

      - **JobStatus** *(string) --*

        The status of the job.
    """


_ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef = TypedDict(
    "_ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef",
    {"Region": str, "Resources": List[str]},
    total=False,
)


class ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef(
    _ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef
):
    pass


_ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef = TypedDict(
    "_ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef",
    {
        "Reason": str,
        "RoleUsageList": List[
            ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef
        ],
    },
    total=False,
)


class ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef(
    _ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef
):
    pass


_ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef = TypedDict(
    "_ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef",
    {
        "Status": Literal["SUCCEEDED", "IN_PROGRESS", "FAILED", "NOT_STARTED"],
        "Reason": ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef,
    },
    total=False,
)


class ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef(
    _ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The status of the deletion.
    """


_ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef = TypedDict(
    "_ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)


class ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef(
    _ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef
):
    """
    - **SSHPublicKey** *(dict) --*

      A structure containing details about the SSH public key.
      - **UserName** *(string) --*

        The name of the IAM user associated with the SSH public key.
    """


_ClientGetSshPublicKeyResponseTypeDef = TypedDict(
    "_ClientGetSshPublicKeyResponseTypeDef",
    {"SSHPublicKey": ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef},
    total=False,
)


class ClientGetSshPublicKeyResponseTypeDef(_ClientGetSshPublicKeyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetSSHPublicKey request.
      - **SSHPublicKey** *(dict) --*

        A structure containing details about the SSH public key.
        - **UserName** *(string) --*

          The name of the IAM user associated with the SSH public key.
    """


_ClientGetUserPolicyResponseTypeDef = TypedDict(
    "_ClientGetUserPolicyResponseTypeDef",
    {"UserName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetUserPolicyResponseTypeDef(_ClientGetUserPolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetUserPolicy request.
      - **UserName** *(string) --*

        The user the policy is associated with.
    """


_ClientGetUserResponseUserPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetUserResponseUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetUserResponseUserPermissionsBoundaryTypeDef(
    _ClientGetUserResponseUserPermissionsBoundaryTypeDef
):
    pass


_ClientGetUserResponseUserTagsTypeDef = TypedDict(
    "_ClientGetUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetUserResponseUserTagsTypeDef(_ClientGetUserResponseUserTagsTypeDef):
    pass


_ClientGetUserResponseUserTypeDef = TypedDict(
    "_ClientGetUserResponseUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientGetUserResponseUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetUserResponseUserTagsTypeDef],
    },
    total=False,
)


class ClientGetUserResponseUserTypeDef(_ClientGetUserResponseUserTypeDef):
    """
    - **User** *(dict) --*

      A structure containing details about the IAM user.
      .. warning::

        Due to a service issue, password last used data does not include password use from May 3,
        2018 22:50 PDT to May 23, 2018 14:08 PDT. This affects `last sign-in
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html>`__
        dates shown in the IAM console and password last used dates in the `IAM credential report
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html>`__ ,
        and returned by this GetUser API. If users signed in during the affected time, the password
        last used date that is returned is the date the user last signed in before May 3, 2018. For
        users that signed in after May 23, 2018 14:08 PDT, the returned password last used date is
        accurate.
        You can use password last used information to identify unused credentials for deletion. For
        example, you might delete users who did not sign in to AWS in the last 90 days. In cases
        like this, we recommend that you adjust your evaluation window to include dates after May
        23, 2018. Alternatively, if your users use access keys to access AWS programmatically you
        can refer to access key last used information because it is accurate for all dates.
    """


_ClientGetUserResponseTypeDef = TypedDict(
    "_ClientGetUserResponseTypeDef", {"User": ClientGetUserResponseUserTypeDef}, total=False
)


class ClientGetUserResponseTypeDef(_ClientGetUserResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetUser request.
      - **User** *(dict) --*

        A structure containing details about the IAM user.
        .. warning::

          Due to a service issue, password last used data does not include password use from May 3,
          2018 22:50 PDT to May 23, 2018 14:08 PDT. This affects `last sign-in
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html>`__
          dates shown in the IAM console and password last used dates in the `IAM credential report
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html>`__ ,
          and returned by this GetUser API. If users signed in during the affected time, the
          password last used date that is returned is the date the user last signed in before May 3,
          2018. For users that signed in after May 23, 2018 14:08 PDT, the returned password last
          used date is accurate.
          You can use password last used information to identify unused credentials for deletion.
          For example, you might delete users who did not sign in to AWS in the last 90 days. In
          cases like this, we recommend that you adjust your evaluation window to include dates
          after May 23, 2018. Alternatively, if your users use access keys to access AWS
          programmatically you can refer to access key last used information because it is accurate
          for all dates.
    """


_ClientListAccessKeysResponseAccessKeyMetadataTypeDef = TypedDict(
    "_ClientListAccessKeysResponseAccessKeyMetadataTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "CreateDate": datetime,
    },
    total=False,
)


class ClientListAccessKeysResponseAccessKeyMetadataTypeDef(
    _ClientListAccessKeysResponseAccessKeyMetadataTypeDef
):
    """
    - *(dict) --*

      Contains information about an AWS access key, without its secret key.
      This data type is used as a response element in the  ListAccessKeys operation.
      - **UserName** *(string) --*

        The name of the IAM user that the key is associated with.
    """


_ClientListAccessKeysResponseTypeDef = TypedDict(
    "_ClientListAccessKeysResponseTypeDef",
    {
        "AccessKeyMetadata": List[ClientListAccessKeysResponseAccessKeyMetadataTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListAccessKeysResponseTypeDef(_ClientListAccessKeysResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListAccessKeys request.
      - **AccessKeyMetadata** *(list) --*

        A list of objects containing metadata about the access keys.
        - *(dict) --*

          Contains information about an AWS access key, without its secret key.
          This data type is used as a response element in the  ListAccessKeys operation.
          - **UserName** *(string) --*

            The name of the IAM user that the key is associated with.
    """


_ClientListAccountAliasesResponseTypeDef = TypedDict(
    "_ClientListAccountAliasesResponseTypeDef",
    {"AccountAliases": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListAccountAliasesResponseTypeDef(_ClientListAccountAliasesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListAccountAliases request.
      - **AccountAliases** *(list) --*

        A list of aliases associated with the account. AWS supports only one alias per account.
        - *(string) --*
    """


_ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "_ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef(
    _ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef
):
    """
    - *(dict) --*

      Contains information about an attached policy.
      An attached policy is a managed policy that has been attached to a user, group, or role. This
      data type is used as a response element in the  ListAttachedGroupPolicies ,
      ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
      operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **PolicyName** *(string) --*

        The friendly name of the attached policy.
    """


_ClientListAttachedGroupPoliciesResponseTypeDef = TypedDict(
    "_ClientListAttachedGroupPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListAttachedGroupPoliciesResponseTypeDef(
    _ClientListAttachedGroupPoliciesResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  ListAttachedGroupPolicies request.
      - **AttachedPolicies** *(list) --*

        A list of the attached policies.
        - *(dict) --*

          Contains information about an attached policy.
          An attached policy is a managed policy that has been attached to a user, group, or role.
          This data type is used as a response element in the  ListAttachedGroupPolicies ,
          ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
          operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **PolicyName** *(string) --*

            The friendly name of the attached policy.
    """


_ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "_ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef(
    _ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef
):
    """
    - *(dict) --*

      Contains information about an attached policy.
      An attached policy is a managed policy that has been attached to a user, group, or role. This
      data type is used as a response element in the  ListAttachedGroupPolicies ,
      ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
      operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **PolicyName** *(string) --*

        The friendly name of the attached policy.
    """


_ClientListAttachedRolePoliciesResponseTypeDef = TypedDict(
    "_ClientListAttachedRolePoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListAttachedRolePoliciesResponseTypeDef(_ClientListAttachedRolePoliciesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListAttachedRolePolicies request.
      - **AttachedPolicies** *(list) --*

        A list of the attached policies.
        - *(dict) --*

          Contains information about an attached policy.
          An attached policy is a managed policy that has been attached to a user, group, or role.
          This data type is used as a response element in the  ListAttachedGroupPolicies ,
          ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
          operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **PolicyName** *(string) --*

            The friendly name of the attached policy.
    """


_ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "_ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef(
    _ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef
):
    """
    - *(dict) --*

      Contains information about an attached policy.
      An attached policy is a managed policy that has been attached to a user, group, or role. This
      data type is used as a response element in the  ListAttachedGroupPolicies ,
      ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
      operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **PolicyName** *(string) --*

        The friendly name of the attached policy.
    """


_ClientListAttachedUserPoliciesResponseTypeDef = TypedDict(
    "_ClientListAttachedUserPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListAttachedUserPoliciesResponseTypeDef(_ClientListAttachedUserPoliciesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListAttachedUserPolicies request.
      - **AttachedPolicies** *(list) --*

        A list of the attached policies.
        - *(dict) --*

          Contains information about an attached policy.
          An attached policy is a managed policy that has been attached to a user, group, or role.
          This data type is used as a response element in the  ListAttachedGroupPolicies ,
          ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
          operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **PolicyName** *(string) --*

            The friendly name of the attached policy.
    """


_ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef = TypedDict(
    "_ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef",
    {"GroupName": str, "GroupId": str},
    total=False,
)


class ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef(
    _ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef
):
    """
    - *(dict) --*

      Contains information about a group that a managed policy is attached to.
      This data type is used as a response element in the  ListEntitiesForPolicy operation.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **GroupName** *(string) --*

        The name (friendly name, not ARN) identifying the group.
    """


_ClientListEntitiesForPolicyResponsePolicyRolesTypeDef = TypedDict(
    "_ClientListEntitiesForPolicyResponsePolicyRolesTypeDef",
    {"RoleName": str, "RoleId": str},
    total=False,
)


class ClientListEntitiesForPolicyResponsePolicyRolesTypeDef(
    _ClientListEntitiesForPolicyResponsePolicyRolesTypeDef
):
    pass


_ClientListEntitiesForPolicyResponsePolicyUsersTypeDef = TypedDict(
    "_ClientListEntitiesForPolicyResponsePolicyUsersTypeDef",
    {"UserName": str, "UserId": str},
    total=False,
)


class ClientListEntitiesForPolicyResponsePolicyUsersTypeDef(
    _ClientListEntitiesForPolicyResponsePolicyUsersTypeDef
):
    pass


_ClientListEntitiesForPolicyResponseTypeDef = TypedDict(
    "_ClientListEntitiesForPolicyResponseTypeDef",
    {
        "PolicyGroups": List[ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef],
        "PolicyUsers": List[ClientListEntitiesForPolicyResponsePolicyUsersTypeDef],
        "PolicyRoles": List[ClientListEntitiesForPolicyResponsePolicyRolesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListEntitiesForPolicyResponseTypeDef(_ClientListEntitiesForPolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListEntitiesForPolicy request.
      - **PolicyGroups** *(list) --*

        A list of IAM groups that the policy is attached to.
        - *(dict) --*

          Contains information about a group that a managed policy is attached to.
          This data type is used as a response element in the  ListEntitiesForPolicy operation.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **GroupName** *(string) --*

            The name (friendly name, not ARN) identifying the group.
    """


_ClientListGroupPoliciesResponseTypeDef = TypedDict(
    "_ClientListGroupPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListGroupPoliciesResponseTypeDef(_ClientListGroupPoliciesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListGroupPolicies request.
      - **PolicyNames** *(list) --*

        A list of policy names.
        This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
        string of characters consisting of upper and lowercase alphanumeric characters with no
        spaces. You can also include any of the following characters: _+=,.@-
        - *(string) --*
    """


_ClientListGroupsForUserResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsForUserResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ClientListGroupsForUserResponseGroupsTypeDef(_ClientListGroupsForUserResponseGroupsTypeDef):
    """
    - *(dict) --*

      Contains information about an IAM group entity.
      This data type is used as a response element in the following operations:
      *  CreateGroup
      *  GetGroup
      *  ListGroups
      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientListGroupsForUserResponseTypeDef = TypedDict(
    "_ClientListGroupsForUserResponseTypeDef",
    {
        "Groups": List[ClientListGroupsForUserResponseGroupsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListGroupsForUserResponseTypeDef(_ClientListGroupsForUserResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListGroupsForUser request.
      - **Groups** *(list) --*

        A list of groups.
        - *(dict) --*

          Contains information about an IAM group entity.
          This data type is used as a response element in the following operations:
          *  CreateGroup
          *  GetGroup
          *  ListGroups
          - **Path** *(string) --*

            The path to the group. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    """
    - *(dict) --*

      Contains information about an IAM group entity.
      This data type is used as a response element in the following operations:
      *  CreateGroup
      *  GetGroup
      *  ListGroups
      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListGroups request.
      - **Groups** *(list) --*

        A list of groups.
        - *(dict) --*

          Contains information about an IAM group entity.
          This data type is used as a response element in the following operations:
          *  CreateGroup
          *  GetGroup
          *  ListGroups
          - **Path** *(string) --*

            The path to the group. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef
):
    pass


_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef
):
    pass


_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef
):
    pass


_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef],
        "RoleLastUsed": ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef
):
    pass


_ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef],
    },
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef
):
    """
    - *(dict) --*

      Contains information about an instance profile.
      This data type is used as a response element in the following operations:
      *  CreateInstanceProfile
      *  GetInstanceProfile
      *  ListInstanceProfiles
      *  ListInstanceProfilesForRole
      - **Path** *(string) --*

        The path to the instance profile. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientListInstanceProfilesForRoleResponseTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseTypeDef",
    {
        "InstanceProfiles": List[ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListInstanceProfilesForRoleResponseTypeDef(
    _ClientListInstanceProfilesForRoleResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  ListInstanceProfilesForRole request.
      - **InstanceProfiles** *(list) --*

        A list of instance profiles.
        - *(dict) --*

          Contains information about an instance profile.
          This data type is used as a response element in the following operations:
          *  CreateInstanceProfile
          *  GetInstanceProfile
          *  ListInstanceProfiles
          *  ListInstanceProfilesForRole
          - **Path** *(string) --*

            The path to the instance profile. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef
):
    pass


_ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef
):
    pass


_ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef
):
    pass


_ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef],
        "RoleLastUsed": ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef
):
    pass


_ClientListInstanceProfilesResponseInstanceProfilesTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef],
    },
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesTypeDef
):
    """
    - *(dict) --*

      Contains information about an instance profile.
      This data type is used as a response element in the following operations:
      *  CreateInstanceProfile
      *  GetInstanceProfile
      *  ListInstanceProfiles
      *  ListInstanceProfilesForRole
      - **Path** *(string) --*

        The path to the instance profile. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientListInstanceProfilesResponseTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseTypeDef",
    {
        "InstanceProfiles": List[ClientListInstanceProfilesResponseInstanceProfilesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListInstanceProfilesResponseTypeDef(_ClientListInstanceProfilesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListInstanceProfiles request.
      - **InstanceProfiles** *(list) --*

        A list of instance profiles.
        - *(dict) --*

          Contains information about an instance profile.
          This data type is used as a response element in the following operations:
          *  CreateInstanceProfile
          *  GetInstanceProfile
          *  ListInstanceProfiles
          *  ListInstanceProfilesForRole
          - **Path** *(string) --*

            The path to the instance profile. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ClientListMfaDevicesResponseMFADevicesTypeDef = TypedDict(
    "_ClientListMfaDevicesResponseMFADevicesTypeDef",
    {"UserName": str, "SerialNumber": str, "EnableDate": datetime},
    total=False,
)


class ClientListMfaDevicesResponseMFADevicesTypeDef(_ClientListMfaDevicesResponseMFADevicesTypeDef):
    """
    - *(dict) --*

      Contains information about an MFA device.
      This data type is used as a response element in the  ListMFADevices operation.
      - **UserName** *(string) --*

        The user with whom the MFA device is associated.
    """


_ClientListMfaDevicesResponseTypeDef = TypedDict(
    "_ClientListMfaDevicesResponseTypeDef",
    {
        "MFADevices": List[ClientListMfaDevicesResponseMFADevicesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListMfaDevicesResponseTypeDef(_ClientListMfaDevicesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListMFADevices request.
      - **MFADevices** *(list) --*

        A list of MFA devices.
        - *(dict) --*

          Contains information about an MFA device.
          This data type is used as a response element in the  ListMFADevices operation.
          - **UserName** *(string) --*

            The user with whom the MFA device is associated.
    """


_ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef = TypedDict(
    "_ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef",
    {"Arn": str},
    total=False,
)


class ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef(
    _ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef
):
    """
    - *(dict) --*

      Contains the Amazon Resource Name (ARN) for an IAM OpenID Connect provider.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
        For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
        Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
        in the *AWS General Reference* .
    """


_ClientListOpenIdConnectProvidersResponseTypeDef = TypedDict(
    "_ClientListOpenIdConnectProvidersResponseTypeDef",
    {
        "OpenIDConnectProviderList": List[
            ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef
        ]
    },
    total=False,
)


class ClientListOpenIdConnectProvidersResponseTypeDef(
    _ClientListOpenIdConnectProvidersResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  ListOpenIDConnectProviders request.
      - **OpenIDConnectProviderList** *(list) --*

        The list of IAM OIDC provider resource objects defined in the AWS account.
        - *(dict) --*

          Contains the Amazon Resource Name (ARN) for an IAM OpenID Connect provider.
          - **Arn** *(string) --*

            The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
            For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
            Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
            *AWS General Reference* .
    """


_ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef = TypedDict(
    "_ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": Literal["INLINE", "MANAGED"],
        "PolicyArn": str,
        "EntityType": Literal["USER", "ROLE", "GROUP"],
        "EntityName": str,
    },
    total=False,
)


class ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef(
    _ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef
):
    pass


_ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef = TypedDict(
    "_ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef",
    {
        "ServiceNamespace": str,
        "Policies": List[
            ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef
        ],
    },
    total=False,
)


class ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef(
    _ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef
):
    """
    - *(dict) --*

      Contains details about the permissions policies that are attached to the specified identity
      (user, group, or role).
      This data type is used as a response element in the  ListPoliciesGrantingServiceAccess
      operation.
      - **ServiceNamespace** *(string) --*

        The namespace of the service that was accessed.
        To learn the service namespace of a service, go to `Actions, Resources, and Condition Keys
        for AWS Services
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html>`__
        in the *IAM User Guide* . Choose the name of the service to view details for that service.
        In the first paragraph, find the service prefix. For example, ``(service prefix: a4b)`` .
        For more information about service namespaces, see `AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
        in the *AWS General Reference* .
    """


_ClientListPoliciesGrantingServiceAccessResponseTypeDef = TypedDict(
    "_ClientListPoliciesGrantingServiceAccessResponseTypeDef",
    {
        "PoliciesGrantingServiceAccess": List[
            ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListPoliciesGrantingServiceAccessResponseTypeDef(
    _ClientListPoliciesGrantingServiceAccessResponseTypeDef
):
    """
    - *(dict) --*

      - **PoliciesGrantingServiceAccess** *(list) --*

        A ``ListPoliciesGrantingServiceAccess`` object that contains details about the permissions
        policies attached to the specified identity (user, group, or role).
        - *(dict) --*

          Contains details about the permissions policies that are attached to the specified
          identity (user, group, or role).
          This data type is used as a response element in the  ListPoliciesGrantingServiceAccess
          operation.
          - **ServiceNamespace** *(string) --*

            The namespace of the service that was accessed.
            To learn the service namespace of a service, go to `Actions, Resources, and Condition
            Keys for AWS Services
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html>`__
            in the *IAM User Guide* . Choose the name of the service to view details for that
            service. In the first paragraph, find the service prefix. For example, ``(service
            prefix: a4b)`` . For more information about service namespaces, see `AWS Service
            Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
            in the *AWS General Reference* .
    """


_ClientListPoliciesResponsePoliciesTypeDef = TypedDict(
    "_ClientListPoliciesResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)


class ClientListPoliciesResponsePoliciesTypeDef(_ClientListPoliciesResponsePoliciesTypeDef):
    """
    - *(dict) --*

      Contains information about a managed policy.
      This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and
      ListPolicies operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **PolicyName** *(string) --*

        The friendly name (not ARN) identifying the policy.
    """


_ClientListPoliciesResponseTypeDef = TypedDict(
    "_ClientListPoliciesResponseTypeDef",
    {
        "Policies": List[ClientListPoliciesResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListPoliciesResponseTypeDef(_ClientListPoliciesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListPolicies request.
      - **Policies** *(list) --*

        A list of policies.
        - *(dict) --*

          Contains information about a managed policy.
          This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and
          ListPolicies operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **PolicyName** *(string) --*

            The friendly name (not ARN) identifying the policy.
    """


_ClientListPolicyVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListPolicyVersionsResponseVersionsTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)


class ClientListPolicyVersionsResponseVersionsTypeDef(
    _ClientListPolicyVersionsResponseVersionsTypeDef
):
    """
    - *(dict) --*

      Contains information about a version of a managed policy.
      This data type is used as a response element in the  CreatePolicyVersion ,  GetPolicyVersion ,
      ListPolicyVersions , and  GetAccountAuthorizationDetails operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **Document** *(string) --*

        The policy document.
        The policy document is returned in the response to the  GetPolicyVersion and
        GetAccountAuthorizationDetails operations. It is not returned in the response to the
        CreatePolicyVersion or  ListPolicyVersions operations.
        The policy document returned in this structure is URL-encoded compliant with `RFC 3986
        <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the
        policy back to plain JSON text. For example, if you use Java, you can use the ``decode``
        method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and
        SDKs provide similar functionality.
    """


_ClientListPolicyVersionsResponseTypeDef = TypedDict(
    "_ClientListPolicyVersionsResponseTypeDef",
    {
        "Versions": List[ClientListPolicyVersionsResponseVersionsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListPolicyVersionsResponseTypeDef(_ClientListPolicyVersionsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListPolicyVersions request.
      - **Versions** *(list) --*

        A list of policy versions.
        For more information about managed policy versions, see `Versioning for Managed Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in the
        *IAM User Guide* .
        - *(dict) --*

          Contains information about a version of a managed policy.
          This data type is used as a response element in the  CreatePolicyVersion ,
          GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **Document** *(string) --*

            The policy document.
            The policy document is returned in the response to the  GetPolicyVersion and
            GetAccountAuthorizationDetails operations. It is not returned in the response to the
            CreatePolicyVersion or  ListPolicyVersions operations.
            The policy document returned in this structure is URL-encoded compliant with `RFC 3986
            <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert
            the policy back to plain JSON text. For example, if you use Java, you can use the
            ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other
            languages and SDKs provide similar functionality.
    """


_ClientListRolePoliciesResponseTypeDef = TypedDict(
    "_ClientListRolePoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListRolePoliciesResponseTypeDef(_ClientListRolePoliciesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListRolePolicies request.
      - **PolicyNames** *(list) --*

        A list of policy names.
        - *(string) --*
    """


_ClientListRoleTagsResponseTagsTypeDef = TypedDict(
    "_ClientListRoleTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListRoleTagsResponseTagsTypeDef(_ClientListRoleTagsResponseTagsTypeDef):
    """
    - *(dict) --*

      A structure that represents user-provided metadata that can be associated with a resource such
      as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .
      - **Key** *(string) --*

        The key name that can be used to look up or retrieve the associated value. For example,
        ``Department`` or ``Cost Center`` are common choices.
    """


_ClientListRoleTagsResponseTypeDef = TypedDict(
    "_ClientListRoleTagsResponseTypeDef",
    {"Tags": List[ClientListRoleTagsResponseTagsTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListRoleTagsResponseTypeDef(_ClientListRoleTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The list of tags currently that is attached to the role. Each tag consists of a key name and
        an associated value. If no tags are attached to the specified role, the response contains an
        empty list.
        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a resource
          such as an IAM user or role. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .
          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For example,
            ``Department`` or ``Cost Center`` are common choices.
    """


_ClientListRolesResponseRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListRolesResponseRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListRolesResponseRolesPermissionsBoundaryTypeDef(
    _ClientListRolesResponseRolesPermissionsBoundaryTypeDef
):
    pass


_ClientListRolesResponseRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientListRolesResponseRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientListRolesResponseRolesRoleLastUsedTypeDef(
    _ClientListRolesResponseRolesRoleLastUsedTypeDef
):
    pass


_ClientListRolesResponseRolesTagsTypeDef = TypedDict(
    "_ClientListRolesResponseRolesTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListRolesResponseRolesTagsTypeDef(_ClientListRolesResponseRolesTagsTypeDef):
    pass


_ClientListRolesResponseRolesTypeDef = TypedDict(
    "_ClientListRolesResponseRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientListRolesResponseRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientListRolesResponseRolesTagsTypeDef],
        "RoleLastUsed": ClientListRolesResponseRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientListRolesResponseRolesTypeDef(_ClientListRolesResponseRolesTypeDef):
    """
    - *(dict) --*

      Contains information about an IAM role. This structure is returned as a response element in
      several API operations that interact with roles.
      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientListRolesResponseTypeDef = TypedDict(
    "_ClientListRolesResponseTypeDef",
    {"Roles": List[ClientListRolesResponseRolesTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListRolesResponseTypeDef(_ClientListRolesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListRoles request.
      - **Roles** *(list) --*

        A list of roles.
        - *(dict) --*

          Contains information about an IAM role. This structure is returned as a response element
          in several API operations that interact with roles.
          - **Path** *(string) --*

            The path to the role. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ClientListSamlProvidersResponseSAMLProviderListTypeDef = TypedDict(
    "_ClientListSamlProvidersResponseSAMLProviderListTypeDef",
    {"Arn": str, "ValidUntil": datetime, "CreateDate": datetime},
    total=False,
)


class ClientListSamlProvidersResponseSAMLProviderListTypeDef(
    _ClientListSamlProvidersResponseSAMLProviderListTypeDef
):
    """
    - *(dict) --*

      Contains the list of SAML providers for this account.
      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the SAML provider.
    """


_ClientListSamlProvidersResponseTypeDef = TypedDict(
    "_ClientListSamlProvidersResponseTypeDef",
    {"SAMLProviderList": List[ClientListSamlProvidersResponseSAMLProviderListTypeDef]},
    total=False,
)


class ClientListSamlProvidersResponseTypeDef(_ClientListSamlProvidersResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListSAMLProviders request.
      - **SAMLProviderList** *(list) --*

        The list of SAML provider resource objects defined in IAM for this AWS account.
        - *(dict) --*

          Contains the list of SAML providers for this account.
          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the SAML provider.
    """


_ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef = TypedDict(
    "_ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)


class ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef(
    _ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef
):
    """
    - *(dict) --*

      Contains information about a server certificate without its certificate body, certificate
      chain, and private key.
      This data type is used as a response element in the  UploadServerCertificate and
      ListServerCertificates operations.
      - **Path** *(string) --*

        The path to the server certificate. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientListServerCertificatesResponseTypeDef = TypedDict(
    "_ClientListServerCertificatesResponseTypeDef",
    {
        "ServerCertificateMetadataList": List[
            ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListServerCertificatesResponseTypeDef(_ClientListServerCertificatesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListServerCertificates request.
      - **ServerCertificateMetadataList** *(list) --*

        A list of server certificates.
        - *(dict) --*

          Contains information about a server certificate without its certificate body, certificate
          chain, and private key.
          This data type is used as a response element in the  UploadServerCertificate and
          ListServerCertificates operations.
          - **Path** *(string) --*

            The path to the server certificate. For more information about paths, see `IAM
            Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
            in the *IAM User Guide* .
    """


_ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef = TypedDict(
    "_ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef",
    {
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
        "ServiceUserName": str,
        "CreateDate": datetime,
        "ServiceSpecificCredentialId": str,
        "ServiceName": str,
    },
    total=False,
)


class ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef(
    _ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef
):
    """
    - *(dict) --*

      Contains additional details about a service-specific credential.
      - **UserName** *(string) --*

        The name of the IAM user associated with the service-specific credential.
    """


_ClientListServiceSpecificCredentialsResponseTypeDef = TypedDict(
    "_ClientListServiceSpecificCredentialsResponseTypeDef",
    {
        "ServiceSpecificCredentials": List[
            ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef
        ]
    },
    total=False,
)


class ClientListServiceSpecificCredentialsResponseTypeDef(
    _ClientListServiceSpecificCredentialsResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceSpecificCredentials** *(list) --*

        A list of structures that each contain details about a service-specific credential.
        - *(dict) --*

          Contains additional details about a service-specific credential.
          - **UserName** *(string) --*

            The name of the IAM user associated with the service-specific credential.
    """


_ClientListSigningCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientListSigningCertificatesResponseCertificatesTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)


class ClientListSigningCertificatesResponseCertificatesTypeDef(
    _ClientListSigningCertificatesResponseCertificatesTypeDef
):
    """
    - *(dict) --*

      Contains information about an X.509 signing certificate.
      This data type is used as a response element in the  UploadSigningCertificate and
      ListSigningCertificates operations.
      - **UserName** *(string) --*

        The name of the user the signing certificate is associated with.
    """


_ClientListSigningCertificatesResponseTypeDef = TypedDict(
    "_ClientListSigningCertificatesResponseTypeDef",
    {
        "Certificates": List[ClientListSigningCertificatesResponseCertificatesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListSigningCertificatesResponseTypeDef(_ClientListSigningCertificatesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListSigningCertificates request.
      - **Certificates** *(list) --*

        A list of the user's signing certificate information.
        - *(dict) --*

          Contains information about an X.509 signing certificate.
          This data type is used as a response element in the  UploadSigningCertificate and
          ListSigningCertificates operations.
          - **UserName** *(string) --*

            The name of the user the signing certificate is associated with.
    """


_ClientListSshPublicKeysResponseSSHPublicKeysTypeDef = TypedDict(
    "_ClientListSshPublicKeysResponseSSHPublicKeysTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)


class ClientListSshPublicKeysResponseSSHPublicKeysTypeDef(
    _ClientListSshPublicKeysResponseSSHPublicKeysTypeDef
):
    """
    - *(dict) --*

      Contains information about an SSH public key, without the key's body or fingerprint.
      This data type is used as a response element in the  ListSSHPublicKeys operation.
      - **UserName** *(string) --*

        The name of the IAM user associated with the SSH public key.
    """


_ClientListSshPublicKeysResponseTypeDef = TypedDict(
    "_ClientListSshPublicKeysResponseTypeDef",
    {
        "SSHPublicKeys": List[ClientListSshPublicKeysResponseSSHPublicKeysTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListSshPublicKeysResponseTypeDef(_ClientListSshPublicKeysResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListSSHPublicKeys request.
      - **SSHPublicKeys** *(list) --*

        A list of the SSH public keys assigned to IAM user.
        - *(dict) --*

          Contains information about an SSH public key, without the key's body or fingerprint.
          This data type is used as a response element in the  ListSSHPublicKeys operation.
          - **UserName** *(string) --*

            The name of the IAM user associated with the SSH public key.
    """


_ClientListUserPoliciesResponseTypeDef = TypedDict(
    "_ClientListUserPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListUserPoliciesResponseTypeDef(_ClientListUserPoliciesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListUserPolicies request.
      - **PolicyNames** *(list) --*

        A list of policy names.
        - *(string) --*
    """


_ClientListUserTagsResponseTagsTypeDef = TypedDict(
    "_ClientListUserTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListUserTagsResponseTagsTypeDef(_ClientListUserTagsResponseTagsTypeDef):
    """
    - *(dict) --*

      A structure that represents user-provided metadata that can be associated with a resource such
      as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .
      - **Key** *(string) --*

        The key name that can be used to look up or retrieve the associated value. For example,
        ``Department`` or ``Cost Center`` are common choices.
    """


_ClientListUserTagsResponseTypeDef = TypedDict(
    "_ClientListUserTagsResponseTypeDef",
    {"Tags": List[ClientListUserTagsResponseTagsTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListUserTagsResponseTypeDef(_ClientListUserTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The list of tags that are currently attached to the user. Each tag consists of a key name
        and an associated value. If no tags are attached to the specified user, the response
        contains an empty list.
        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a resource
          such as an IAM user or role. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .
          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For example,
            ``Department`` or ``Cost Center`` are common choices.
    """


_ClientListUsersResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListUsersResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListUsersResponseUsersPermissionsBoundaryTypeDef(
    _ClientListUsersResponseUsersPermissionsBoundaryTypeDef
):
    pass


_ClientListUsersResponseUsersTagsTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListUsersResponseUsersTagsTypeDef(_ClientListUsersResponseUsersTagsTypeDef):
    pass


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientListUsersResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[ClientListUsersResponseUsersTagsTypeDef],
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    - *(dict) --*

      Contains information about an IAM user entity.
      This data type is used as a response element in the following operations:
      *  CreateUser
      *  GetUser
      *  ListUsers
      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListUsers request.
      - **Users** *(list) --*

        A list of users.
        - *(dict) --*

          Contains information about an IAM user entity.
          This data type is used as a response element in the following operations:
          *  CreateUser
          *  GetUser
          *  ListUsers
          - **Path** *(string) --*

            The path to the user. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef(
    _ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef
):
    pass


_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef(
    _ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef
):
    pass


_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef],
    },
    total=False,
)


class ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef(
    _ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef
):
    pass


_ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)


class ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef(
    _ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef
):
    """
    - *(dict) --*

      Contains information about a virtual MFA device.
      - **SerialNumber** *(string) --*

        The serial number associated with ``VirtualMFADevice`` .
    """


_ClientListVirtualMfaDevicesResponseTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseTypeDef",
    {
        "VirtualMFADevices": List[ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListVirtualMfaDevicesResponseTypeDef(_ClientListVirtualMfaDevicesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListVirtualMFADevices request.
      - **VirtualMFADevices** *(list) --*

        The list of virtual MFA devices in the current account that match the ``AssignmentStatus``
        value that was passed in the request.
        - *(dict) --*

          Contains information about a virtual MFA device.
          - **SerialNumber** *(string) --*

            The serial number associated with ``VirtualMFADevice`` .
    """


_ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef = TypedDict(
    "_ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
    },
    total=False,
)


class ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef(
    _ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
):
    """
    - **ServiceSpecificCredential** *(dict) --*

      A structure with details about the updated service-specific credential, including the new
      password.
      .. warning::

        This is the **only** time that you can access the password. You cannot recover the password
        later, but you can reset it again.
    """


_ClientResetServiceSpecificCredentialResponseTypeDef = TypedDict(
    "_ClientResetServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
    },
    total=False,
)


class ClientResetServiceSpecificCredentialResponseTypeDef(
    _ClientResetServiceSpecificCredentialResponseTypeDef
):
    """
    - *(dict) --*

      - **ServiceSpecificCredential** *(dict) --*

        A structure with details about the updated service-specific credential, including the new
        password.
        .. warning::

          This is the **only** time that you can access the password. You cannot recover the
          password later, but you can reset it again.
    """


_ClientSimulateCustomPolicyContextEntriesTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyContextEntriesTypeDef",
    {
        "ContextKeyName": str,
        "ContextKeyValues": List[str],
        "ContextKeyType": Literal[
            "string",
            "stringList",
            "numeric",
            "numericList",
            "boolean",
            "booleanList",
            "ip",
            "ipList",
            "binary",
            "binaryList",
            "date",
            "dateList",
        ],
    },
    total=False,
)


class ClientSimulateCustomPolicyContextEntriesTypeDef(
    _ClientSimulateCustomPolicyContextEntriesTypeDef
):
    """
    - *(dict) --*

      Contains information about a condition context key. It includes the name of the key and
      specifies the value (or values, if the context key supports multiple values) to use in the
      simulation. This information is used when evaluating the ``Condition`` elements of the input
      policies.
      This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``
      SimulatePrincipalPolicy `` .
      - **ContextKeyName** *(string) --*

        The full name of a condition context key, including the service prefix. For example,
        ``aws:SourceIp`` or ``s3:VersionId`` .
    """


_ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef(
    _ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef
):
    pass


_ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef(
    _ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef
):
    pass


_ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)


class ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef(
    _ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef
):
    pass


_ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)


class ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef(
    _ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef
):
    pass


_ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef(
    _ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef
):
    pass


_ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef(
    _ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef
):
    pass


_ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)


class ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef(
    _ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
):
    pass


_ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
    },
    total=False,
)


class ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef(
    _ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef
):
    pass


_ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef",
    {
        "EvalActionName": str,
        "EvalResourceName": str,
        "EvalDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "OrganizationsDecisionDetail": ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef,
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "ResourceSpecificResults": List[
            ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef
        ],
    },
    total=False,
)


class ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef(
    _ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      Contains the results of a simulation.
      This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``
      SimulatePrincipalPolicy `` .
      - **EvalActionName** *(string) --*

        The name of the API operation tested on the indicated resource.
    """


_ClientSimulateCustomPolicyResponseTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyResponseTypeDef",
    {
        "EvaluationResults": List[ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientSimulateCustomPolicyResponseTypeDef(_ClientSimulateCustomPolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  SimulatePrincipalPolicy or  SimulateCustomPolicy
      request.
      - **EvaluationResults** *(list) --*

        The results of the simulation.
        - *(dict) --*

          Contains the results of a simulation.
          This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``
          SimulatePrincipalPolicy `` .
          - **EvalActionName** *(string) --*

            The name of the API operation tested on the indicated resource.
    """


_ClientSimulatePrincipalPolicyContextEntriesTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyContextEntriesTypeDef",
    {
        "ContextKeyName": str,
        "ContextKeyValues": List[str],
        "ContextKeyType": Literal[
            "string",
            "stringList",
            "numeric",
            "numericList",
            "boolean",
            "booleanList",
            "ip",
            "ipList",
            "binary",
            "binaryList",
            "date",
            "dateList",
        ],
    },
    total=False,
)


class ClientSimulatePrincipalPolicyContextEntriesTypeDef(
    _ClientSimulatePrincipalPolicyContextEntriesTypeDef
):
    """
    - *(dict) --*

      Contains information about a condition context key. It includes the name of the key and
      specifies the value (or values, if the context key supports multiple values) to use in the
      simulation. This information is used when evaluating the ``Condition`` elements of the input
      policies.
      This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``
      SimulatePrincipalPolicy `` .
      - **ContextKeyName** *(string) --*

        The full name of a condition context key, including the service prefix. For example,
        ``aws:SourceIp`` or ``s3:VersionId`` .
    """


_ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef(
    _ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef
):
    pass


_ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef(
    _ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef
):
    pass


_ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)


class ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef(
    _ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef
):
    pass


_ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)


class ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef(
    _ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef
):
    pass


_ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef(
    _ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef
):
    pass


_ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef(
    _ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef
):
    pass


_ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)


class ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef(
    _ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
):
    pass


_ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
    },
    total=False,
)


class ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef(
    _ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef
):
    pass


_ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef",
    {
        "EvalActionName": str,
        "EvalResourceName": str,
        "EvalDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "OrganizationsDecisionDetail": ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef,
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "ResourceSpecificResults": List[
            ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef
        ],
    },
    total=False,
)


class ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef(
    _ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      Contains the results of a simulation.
      This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``
      SimulatePrincipalPolicy `` .
      - **EvalActionName** *(string) --*

        The name of the API operation tested on the indicated resource.
    """


_ClientSimulatePrincipalPolicyResponseTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyResponseTypeDef",
    {
        "EvaluationResults": List[ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientSimulatePrincipalPolicyResponseTypeDef(_ClientSimulatePrincipalPolicyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  SimulatePrincipalPolicy or  SimulateCustomPolicy
      request.
      - **EvaluationResults** *(list) --*

        The results of the simulation.
        - *(dict) --*

          Contains the results of a simulation.
          This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``
          SimulatePrincipalPolicy `` .
          - **EvalActionName** *(string) --*

            The name of the API operation tested on the indicated resource.
    """


_RequiredClientTagRoleTagsTypeDef = TypedDict("_RequiredClientTagRoleTagsTypeDef", {"Key": str})
_OptionalClientTagRoleTagsTypeDef = TypedDict(
    "_OptionalClientTagRoleTagsTypeDef", {"Value": str}, total=False
)


class ClientTagRoleTagsTypeDef(
    _RequiredClientTagRoleTagsTypeDef, _OptionalClientTagRoleTagsTypeDef
):
    """
    - *(dict) --*

      A structure that represents user-provided metadata that can be associated with a resource such
      as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .
      - **Key** *(string) --***[REQUIRED]**

        The key name that can be used to look up or retrieve the associated value. For example,
        ``Department`` or ``Cost Center`` are common choices.
    """


_RequiredClientTagUserTagsTypeDef = TypedDict("_RequiredClientTagUserTagsTypeDef", {"Key": str})
_OptionalClientTagUserTagsTypeDef = TypedDict(
    "_OptionalClientTagUserTagsTypeDef", {"Value": str}, total=False
)


class ClientTagUserTagsTypeDef(
    _RequiredClientTagUserTagsTypeDef, _OptionalClientTagUserTagsTypeDef
):
    """
    - *(dict) --*

      A structure that represents user-provided metadata that can be associated with a resource such
      as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .
      - **Key** *(string) --***[REQUIRED]**

        The key name that can be used to look up or retrieve the associated value. For example,
        ``Department`` or ``Cost Center`` are common choices.
    """


_ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef(
    _ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef
):
    pass


_ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef(
    _ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef
):
    pass


_ClientUpdateRoleDescriptionResponseRoleTagsTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdateRoleDescriptionResponseRoleTagsTypeDef(
    _ClientUpdateRoleDescriptionResponseRoleTagsTypeDef
):
    pass


_ClientUpdateRoleDescriptionResponseRoleTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientUpdateRoleDescriptionResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientUpdateRoleDescriptionResponseRoleTypeDef(
    _ClientUpdateRoleDescriptionResponseRoleTypeDef
):
    """
    - **Role** *(dict) --*

      A structure that contains details about the modified role.
      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientUpdateRoleDescriptionResponseTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseTypeDef",
    {"Role": ClientUpdateRoleDescriptionResponseRoleTypeDef},
    total=False,
)


class ClientUpdateRoleDescriptionResponseTypeDef(_ClientUpdateRoleDescriptionResponseTypeDef):
    """
    - *(dict) --*

      - **Role** *(dict) --*

        A structure that contains details about the modified role.
        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientUpdateSamlProviderResponseTypeDef = TypedDict(
    "_ClientUpdateSamlProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)


class ClientUpdateSamlProviderResponseTypeDef(_ClientUpdateSamlProviderResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  UpdateSAMLProvider request.
      - **SAMLProviderArn** *(string) --*

        The Amazon Resource Name (ARN) of the SAML provider that was updated.
    """


_ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef = TypedDict(
    "_ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)


class ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef(
    _ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef
):
    """
    - **ServerCertificateMetadata** *(dict) --*

      The meta information of the uploaded server certificate without its certificate body,
      certificate chain, and private key.
      - **Path** *(string) --*

        The path to the server certificate. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ClientUploadServerCertificateResponseTypeDef = TypedDict(
    "_ClientUploadServerCertificateResponseTypeDef",
    {
        "ServerCertificateMetadata": ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef
    },
    total=False,
)


class ClientUploadServerCertificateResponseTypeDef(_ClientUploadServerCertificateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  UploadServerCertificate request.
      - **ServerCertificateMetadata** *(dict) --*

        The meta information of the uploaded server certificate without its certificate body,
        certificate chain, and private key.
        - **Path** *(string) --*

          The path to the server certificate. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_ClientUploadSigningCertificateResponseCertificateTypeDef = TypedDict(
    "_ClientUploadSigningCertificateResponseCertificateTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)


class ClientUploadSigningCertificateResponseCertificateTypeDef(
    _ClientUploadSigningCertificateResponseCertificateTypeDef
):
    """
    - **Certificate** *(dict) --*

      Information about the certificate.
      - **UserName** *(string) --*

        The name of the user the signing certificate is associated with.
    """


_ClientUploadSigningCertificateResponseTypeDef = TypedDict(
    "_ClientUploadSigningCertificateResponseTypeDef",
    {"Certificate": ClientUploadSigningCertificateResponseCertificateTypeDef},
    total=False,
)


class ClientUploadSigningCertificateResponseTypeDef(_ClientUploadSigningCertificateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  UploadSigningCertificate request.
      - **Certificate** *(dict) --*

        Information about the certificate.
        - **UserName** *(string) --*

          The name of the user the signing certificate is associated with.
    """


_ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef = TypedDict(
    "_ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)


class ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef(
    _ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef
):
    """
    - **SSHPublicKey** *(dict) --*

      Contains information about the SSH public key.
      - **UserName** *(string) --*

        The name of the IAM user associated with the SSH public key.
    """


_ClientUploadSshPublicKeyResponseTypeDef = TypedDict(
    "_ClientUploadSshPublicKeyResponseTypeDef",
    {"SSHPublicKey": ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef},
    total=False,
)


class ClientUploadSshPublicKeyResponseTypeDef(_ClientUploadSshPublicKeyResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  UploadSSHPublicKey request.
      - **SSHPublicKey** *(dict) --*

        Contains information about the SSH public key.
        - **UserName** *(string) --*

          The name of the IAM user associated with the SSH public key.
    """


_GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef(
    _GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
        "GroupPolicyList": List[
            GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef
        ],
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "PolicyVersionList": List[
            GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef
        ],
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef
        ],
        "RoleLastUsed": GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef
        ],
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "InstanceProfileList": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef
        ],
        "RolePolicyList": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef,
        "Tags": List[GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef],
        "RoleLastUsed": GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef,
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef
):
    pass


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "UserPolicyList": List[
            GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef
        ],
        "GroupList": List[str],
        "AttachedManagedPolicies": List[
            GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef,
        "Tags": List[GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef],
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef
):
    """
    - *(dict) --*

      Contains information about an IAM user, including all the user's policies and all the IAM
      groups the user is in.
      This data type is used as a response element in the  GetAccountAuthorizationDetails operation.
      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_GetAccountAuthorizationDetailsPaginateResponseTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseTypeDef",
    {
        "UserDetailList": List[GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef],
        "GroupDetailList": List[
            GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef
        ],
        "RoleDetailList": List[GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef],
        "Policies": List[GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  GetAccountAuthorizationDetails request.
      - **UserDetailList** *(list) --*

        A list containing information about IAM users.
        - *(dict) --*

          Contains information about an IAM user, including all the user's policies and all the IAM
          groups the user is in.
          This data type is used as a response element in the  GetAccountAuthorizationDetails
          operation.
          - **Path** *(string) --*

            The path to the user. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_GetGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_GetGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetGroupPaginatePaginationConfigTypeDef(_GetGroupPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetGroupPaginateResponseGroupTypeDef = TypedDict(
    "_GetGroupPaginateResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class GetGroupPaginateResponseGroupTypeDef(_GetGroupPaginateResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      A structure that contains details about the group.
      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "_GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef(
    _GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef
):
    pass


_GetGroupPaginateResponseUsersTagsTypeDef = TypedDict(
    "_GetGroupPaginateResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class GetGroupPaginateResponseUsersTagsTypeDef(_GetGroupPaginateResponseUsersTagsTypeDef):
    pass


_GetGroupPaginateResponseUsersTypeDef = TypedDict(
    "_GetGroupPaginateResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[GetGroupPaginateResponseUsersTagsTypeDef],
    },
    total=False,
)


class GetGroupPaginateResponseUsersTypeDef(_GetGroupPaginateResponseUsersTypeDef):
    pass


_GetGroupPaginateResponseTypeDef = TypedDict(
    "_GetGroupPaginateResponseTypeDef",
    {
        "Group": GetGroupPaginateResponseGroupTypeDef,
        "Users": List[GetGroupPaginateResponseUsersTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class GetGroupPaginateResponseTypeDef(_GetGroupPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetGroup request.
      - **Group** *(dict) --*

        A structure that contains details about the group.
        - **Path** *(string) --*

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .
    """


_InstanceProfileExistsWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceProfileExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class InstanceProfileExistsWaitWaiterConfigTypeDef(_InstanceProfileExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1
    """


_ListAccessKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccessKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccessKeysPaginatePaginationConfigTypeDef(_ListAccessKeysPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef = TypedDict(
    "_ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "CreateDate": datetime,
    },
    total=False,
)


class ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef(
    _ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef
):
    """
    - *(dict) --*

      Contains information about an AWS access key, without its secret key.
      This data type is used as a response element in the  ListAccessKeys operation.
      - **UserName** *(string) --*

        The name of the IAM user that the key is associated with.
    """


_ListAccessKeysPaginateResponseTypeDef = TypedDict(
    "_ListAccessKeysPaginateResponseTypeDef",
    {
        "AccessKeyMetadata": List[ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAccessKeysPaginateResponseTypeDef(_ListAccessKeysPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListAccessKeys request.
      - **AccessKeyMetadata** *(list) --*

        A list of objects containing metadata about the access keys.
        - *(dict) --*

          Contains information about an AWS access key, without its secret key.
          This data type is used as a response element in the  ListAccessKeys operation.
          - **UserName** *(string) --*

            The name of the IAM user that the key is associated with.
    """


_ListAccountAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccountAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccountAliasesPaginatePaginationConfigTypeDef(
    _ListAccountAliasesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAccountAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAccountAliasesPaginateResponseTypeDef",
    {"AccountAliases": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListAccountAliasesPaginateResponseTypeDef(_ListAccountAliasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListAccountAliases request.
      - **AccountAliases** *(list) --*

        A list of aliases associated with the account. AWS supports only one alias per account.
        - *(string) --*
    """


_ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef(
    _ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef = TypedDict(
    "_ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef(
    _ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef
):
    """
    - *(dict) --*

      Contains information about an attached policy.
      An attached policy is a managed policy that has been attached to a user, group, or role. This
      data type is used as a response element in the  ListAttachedGroupPolicies ,
      ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
      operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **PolicyName** *(string) --*

        The friendly name of the attached policy.
    """


_ListAttachedGroupPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedGroupPoliciesPaginateResponseTypeDef",
    {
        "AttachedPolicies": List[ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAttachedGroupPoliciesPaginateResponseTypeDef(
    _ListAttachedGroupPoliciesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  ListAttachedGroupPolicies request.
      - **AttachedPolicies** *(list) --*

        A list of the attached policies.
        - *(dict) --*

          Contains information about an attached policy.
          An attached policy is a managed policy that has been attached to a user, group, or role.
          This data type is used as a response element in the  ListAttachedGroupPolicies ,
          ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
          operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **PolicyName** *(string) --*

            The friendly name of the attached policy.
    """


_ListAttachedRolePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedRolePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedRolePoliciesPaginatePaginationConfigTypeDef(
    _ListAttachedRolePoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef = TypedDict(
    "_ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef(
    _ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef
):
    """
    - *(dict) --*

      Contains information about an attached policy.
      An attached policy is a managed policy that has been attached to a user, group, or role. This
      data type is used as a response element in the  ListAttachedGroupPolicies ,
      ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
      operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **PolicyName** *(string) --*

        The friendly name of the attached policy.
    """


_ListAttachedRolePoliciesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedRolePoliciesPaginateResponseTypeDef",
    {
        "AttachedPolicies": List[ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAttachedRolePoliciesPaginateResponseTypeDef(
    _ListAttachedRolePoliciesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  ListAttachedRolePolicies request.
      - **AttachedPolicies** *(list) --*

        A list of the attached policies.
        - *(dict) --*

          Contains information about an attached policy.
          An attached policy is a managed policy that has been attached to a user, group, or role.
          This data type is used as a response element in the  ListAttachedGroupPolicies ,
          ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
          operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **PolicyName** *(string) --*

            The friendly name of the attached policy.
    """


_ListAttachedUserPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedUserPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedUserPoliciesPaginatePaginationConfigTypeDef(
    _ListAttachedUserPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef = TypedDict(
    "_ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef(
    _ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef
):
    """
    - *(dict) --*

      Contains information about an attached policy.
      An attached policy is a managed policy that has been attached to a user, group, or role. This
      data type is used as a response element in the  ListAttachedGroupPolicies ,
      ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
      operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **PolicyName** *(string) --*

        The friendly name of the attached policy.
    """


_ListAttachedUserPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedUserPoliciesPaginateResponseTypeDef",
    {
        "AttachedPolicies": List[ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAttachedUserPoliciesPaginateResponseTypeDef(
    _ListAttachedUserPoliciesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  ListAttachedUserPolicies request.
      - **AttachedPolicies** *(list) --*

        A list of the attached policies.
        - *(dict) --*

          Contains information about an attached policy.
          An attached policy is a managed policy that has been attached to a user, group, or role.
          This data type is used as a response element in the  ListAttachedGroupPolicies ,
          ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
          operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **PolicyName** *(string) --*

            The friendly name of the attached policy.
    """


_ListEntitiesForPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEntitiesForPolicyPaginatePaginationConfigTypeDef(
    _ListEntitiesForPolicyPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef",
    {"GroupName": str, "GroupId": str},
    total=False,
)


class ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef(
    _ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef
):
    """
    - *(dict) --*

      Contains information about a group that a managed policy is attached to.
      This data type is used as a response element in the  ListEntitiesForPolicy operation.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **GroupName** *(string) --*

        The name (friendly name, not ARN) identifying the group.
    """


_ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef",
    {"RoleName": str, "RoleId": str},
    total=False,
)


class ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef(
    _ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef
):
    pass


_ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef",
    {"UserName": str, "UserId": str},
    total=False,
)


class ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef(
    _ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef
):
    pass


_ListEntitiesForPolicyPaginateResponseTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginateResponseTypeDef",
    {
        "PolicyGroups": List[ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef],
        "PolicyUsers": List[ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef],
        "PolicyRoles": List[ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListEntitiesForPolicyPaginateResponseTypeDef(_ListEntitiesForPolicyPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListEntitiesForPolicy request.
      - **PolicyGroups** *(list) --*

        A list of IAM groups that the policy is attached to.
        - *(dict) --*

          Contains information about a group that a managed policy is attached to.
          This data type is used as a response element in the  ListEntitiesForPolicy operation.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **GroupName** *(string) --*

            The name (friendly name, not ARN) identifying the group.
    """


_ListGroupPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupPoliciesPaginatePaginationConfigTypeDef(
    _ListGroupPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListGroupPoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListGroupPoliciesPaginateResponseTypeDef(_ListGroupPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListGroupPolicies request.
      - **PolicyNames** *(list) --*

        A list of policy names.
        This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
        string of characters consisting of upper and lowercase alphanumeric characters with no
        spaces. You can also include any of the following characters: _+=,.@-
        - *(string) --*
    """


_ListGroupsForUserPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsForUserPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsForUserPaginatePaginationConfigTypeDef(
    _ListGroupsForUserPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupsForUserPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsForUserPaginateResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ListGroupsForUserPaginateResponseGroupsTypeDef(
    _ListGroupsForUserPaginateResponseGroupsTypeDef
):
    """
    - *(dict) --*

      Contains information about an IAM group entity.
      This data type is used as a response element in the following operations:
      *  CreateGroup
      *  GetGroup
      *  ListGroups
      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ListGroupsForUserPaginateResponseTypeDef = TypedDict(
    "_ListGroupsForUserPaginateResponseTypeDef",
    {
        "Groups": List[ListGroupsForUserPaginateResponseGroupsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListGroupsForUserPaginateResponseTypeDef(_ListGroupsForUserPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListGroupsForUser request.
      - **Groups** *(list) --*

        A list of groups.
        - *(dict) --*

          Contains information about an IAM group entity.
          This data type is used as a response element in the following operations:
          *  CreateGroup
          *  GetGroup
          *  ListGroups
          - **Path** *(string) --*

            The path to the group. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsPaginatePaginationConfigTypeDef(_ListGroupsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    """
    - *(dict) --*

      Contains information about an IAM group entity.
      This data type is used as a response element in the following operations:
      *  CreateGroup
      *  GetGroup
      *  ListGroups
      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {
        "Groups": List[ListGroupsPaginateResponseGroupsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListGroups request.
      - **Groups** *(list) --*

        A list of groups.
        - *(dict) --*

          Contains information about an IAM group entity.
          This data type is used as a response element in the following operations:
          *  CreateGroup
          *  GetGroup
          *  ListGroups
          - **Path** *(string) --*

            The path to the group. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ListInstanceProfilesForRolePaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInstanceProfilesForRolePaginatePaginationConfigTypeDef(
    _ListInstanceProfilesForRolePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef
):
    pass


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef
):
    pass


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef
):
    pass


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef],
        "RoleLastUsed": ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef
):
    pass


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef],
    },
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef
):
    """
    - *(dict) --*

      Contains information about an instance profile.
      This data type is used as a response element in the following operations:
      *  CreateInstanceProfile
      *  GetInstanceProfile
      *  ListInstanceProfiles
      *  ListInstanceProfilesForRole
      - **Path** *(string) --*

        The path to the instance profile. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ListInstanceProfilesForRolePaginateResponseTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseTypeDef",
    {
        "InstanceProfiles": List[
            ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseTypeDef(
    _ListInstanceProfilesForRolePaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  ListInstanceProfilesForRole request.
      - **InstanceProfiles** *(list) --*

        A list of instance profiles.
        - *(dict) --*

          Contains information about an instance profile.
          This data type is used as a response element in the following operations:
          *  CreateInstanceProfile
          *  GetInstanceProfile
          *  ListInstanceProfiles
          *  ListInstanceProfilesForRole
          - **Path** *(string) --*

            The path to the instance profile. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ListInstanceProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstanceProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInstanceProfilesPaginatePaginationConfigTypeDef(
    _ListInstanceProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef
):
    pass


_ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef
):
    pass


_ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef
):
    pass


_ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef],
        "RoleLastUsed": ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef
):
    pass


_ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef],
    },
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef
):
    """
    - *(dict) --*

      Contains information about an instance profile.
      This data type is used as a response element in the following operations:
      *  CreateInstanceProfile
      *  GetInstanceProfile
      *  ListInstanceProfiles
      *  ListInstanceProfilesForRole
      - **Path** *(string) --*

        The path to the instance profile. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ListInstanceProfilesPaginateResponseTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseTypeDef",
    {
        "InstanceProfiles": List[ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListInstanceProfilesPaginateResponseTypeDef(_ListInstanceProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListInstanceProfiles request.
      - **InstanceProfiles** *(list) --*

        A list of instance profiles.
        - *(dict) --*

          Contains information about an instance profile.
          This data type is used as a response element in the following operations:
          *  CreateInstanceProfile
          *  GetInstanceProfile
          *  ListInstanceProfiles
          *  ListInstanceProfilesForRole
          - **Path** *(string) --*

            The path to the instance profile. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ListMFADevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMFADevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMFADevicesPaginatePaginationConfigTypeDef(_ListMFADevicesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMFADevicesPaginateResponseMFADevicesTypeDef = TypedDict(
    "_ListMFADevicesPaginateResponseMFADevicesTypeDef",
    {"UserName": str, "SerialNumber": str, "EnableDate": datetime},
    total=False,
)


class ListMFADevicesPaginateResponseMFADevicesTypeDef(
    _ListMFADevicesPaginateResponseMFADevicesTypeDef
):
    """
    - *(dict) --*

      Contains information about an MFA device.
      This data type is used as a response element in the  ListMFADevices operation.
      - **UserName** *(string) --*

        The user with whom the MFA device is associated.
    """


_ListMFADevicesPaginateResponseTypeDef = TypedDict(
    "_ListMFADevicesPaginateResponseTypeDef",
    {
        "MFADevices": List[ListMFADevicesPaginateResponseMFADevicesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListMFADevicesPaginateResponseTypeDef(_ListMFADevicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListMFADevices request.
      - **MFADevices** *(list) --*

        A list of MFA devices.
        - *(dict) --*

          Contains information about an MFA device.
          This data type is used as a response element in the  ListMFADevices operation.
          - **UserName** *(string) --*

            The user with whom the MFA device is associated.
    """


_ListPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPoliciesPaginatePaginationConfigTypeDef(_ListPoliciesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPoliciesPaginateResponsePoliciesTypeDef = TypedDict(
    "_ListPoliciesPaginateResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)


class ListPoliciesPaginateResponsePoliciesTypeDef(_ListPoliciesPaginateResponsePoliciesTypeDef):
    """
    - *(dict) --*

      Contains information about a managed policy.
      This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and
      ListPolicies operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **PolicyName** *(string) --*

        The friendly name (not ARN) identifying the policy.
    """


_ListPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesPaginateResponseTypeDef",
    {
        "Policies": List[ListPoliciesPaginateResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListPoliciesPaginateResponseTypeDef(_ListPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListPolicies request.
      - **Policies** *(list) --*

        A list of policies.
        - *(dict) --*

          Contains information about a managed policy.
          This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and
          ListPolicies operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **PolicyName** *(string) --*

            The friendly name (not ARN) identifying the policy.
    """


_ListPolicyVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPolicyVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPolicyVersionsPaginatePaginationConfigTypeDef(
    _ListPolicyVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPolicyVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListPolicyVersionsPaginateResponseVersionsTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)


class ListPolicyVersionsPaginateResponseVersionsTypeDef(
    _ListPolicyVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*

      Contains information about a version of a managed policy.
      This data type is used as a response element in the  CreatePolicyVersion ,  GetPolicyVersion ,
      ListPolicyVersions , and  GetAccountAuthorizationDetails operations.
      For more information about managed policies, refer to `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
      *IAM User Guide* .
      - **Document** *(string) --*

        The policy document.
        The policy document is returned in the response to the  GetPolicyVersion and
        GetAccountAuthorizationDetails operations. It is not returned in the response to the
        CreatePolicyVersion or  ListPolicyVersions operations.
        The policy document returned in this structure is URL-encoded compliant with `RFC 3986
        <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the
        policy back to plain JSON text. For example, if you use Java, you can use the ``decode``
        method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and
        SDKs provide similar functionality.
    """


_ListPolicyVersionsPaginateResponseTypeDef = TypedDict(
    "_ListPolicyVersionsPaginateResponseTypeDef",
    {
        "Versions": List[ListPolicyVersionsPaginateResponseVersionsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListPolicyVersionsPaginateResponseTypeDef(_ListPolicyVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListPolicyVersions request.
      - **Versions** *(list) --*

        A list of policy versions.
        For more information about managed policy versions, see `Versioning for Managed Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in the
        *IAM User Guide* .
        - *(dict) --*

          Contains information about a version of a managed policy.
          This data type is used as a response element in the  CreatePolicyVersion ,
          GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.
          For more information about managed policies, refer to `Managed Policies and Inline
          Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
          the *IAM User Guide* .
          - **Document** *(string) --*

            The policy document.
            The policy document is returned in the response to the  GetPolicyVersion and
            GetAccountAuthorizationDetails operations. It is not returned in the response to the
            CreatePolicyVersion or  ListPolicyVersions operations.
            The policy document returned in this structure is URL-encoded compliant with `RFC 3986
            <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert
            the policy back to plain JSON text. For example, if you use Java, you can use the
            ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other
            languages and SDKs provide similar functionality.
    """


_ListRolePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRolePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRolePoliciesPaginatePaginationConfigTypeDef(
    _ListRolePoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRolePoliciesPaginateResponseTypeDef = TypedDict(
    "_ListRolePoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListRolePoliciesPaginateResponseTypeDef(_ListRolePoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListRolePolicies request.
      - **PolicyNames** *(list) --*

        A list of policy names.
        - *(string) --*
    """


_ListRolesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRolesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRolesPaginatePaginationConfigTypeDef(_ListRolesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef(
    _ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef
):
    pass


_ListRolesPaginateResponseRolesRoleLastUsedTypeDef = TypedDict(
    "_ListRolesPaginateResponseRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ListRolesPaginateResponseRolesRoleLastUsedTypeDef(
    _ListRolesPaginateResponseRolesRoleLastUsedTypeDef
):
    pass


_ListRolesPaginateResponseRolesTagsTypeDef = TypedDict(
    "_ListRolesPaginateResponseRolesTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListRolesPaginateResponseRolesTagsTypeDef(_ListRolesPaginateResponseRolesTagsTypeDef):
    pass


_ListRolesPaginateResponseRolesTypeDef = TypedDict(
    "_ListRolesPaginateResponseRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef,
        "Tags": List[ListRolesPaginateResponseRolesTagsTypeDef],
        "RoleLastUsed": ListRolesPaginateResponseRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ListRolesPaginateResponseRolesTypeDef(_ListRolesPaginateResponseRolesTypeDef):
    """
    - *(dict) --*

      Contains information about an IAM role. This structure is returned as a response element in
      several API operations that interact with roles.
      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ListRolesPaginateResponseTypeDef = TypedDict(
    "_ListRolesPaginateResponseTypeDef",
    {"Roles": List[ListRolesPaginateResponseRolesTypeDef], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListRolesPaginateResponseTypeDef(_ListRolesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListRoles request.
      - **Roles** *(list) --*

        A list of roles.
        - *(dict) --*

          Contains information about an IAM role. This structure is returned as a response element
          in several API operations that interact with roles.
          - **Path** *(string) --*

            The path to the role. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ListSSHPublicKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSSHPublicKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSSHPublicKeysPaginatePaginationConfigTypeDef(
    _ListSSHPublicKeysPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef = TypedDict(
    "_ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)


class ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef(
    _ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef
):
    """
    - *(dict) --*

      Contains information about an SSH public key, without the key's body or fingerprint.
      This data type is used as a response element in the  ListSSHPublicKeys operation.
      - **UserName** *(string) --*

        The name of the IAM user associated with the SSH public key.
    """


_ListSSHPublicKeysPaginateResponseTypeDef = TypedDict(
    "_ListSSHPublicKeysPaginateResponseTypeDef",
    {
        "SSHPublicKeys": List[ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListSSHPublicKeysPaginateResponseTypeDef(_ListSSHPublicKeysPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListSSHPublicKeys request.
      - **SSHPublicKeys** *(list) --*

        A list of the SSH public keys assigned to IAM user.
        - *(dict) --*

          Contains information about an SSH public key, without the key's body or fingerprint.
          This data type is used as a response element in the  ListSSHPublicKeys operation.
          - **UserName** *(string) --*

            The name of the IAM user associated with the SSH public key.
    """


_ListServerCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServerCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServerCertificatesPaginatePaginationConfigTypeDef(
    _ListServerCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef = TypedDict(
    "_ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)


class ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef(
    _ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef
):
    """
    - *(dict) --*

      Contains information about a server certificate without its certificate body, certificate
      chain, and private key.
      This data type is used as a response element in the  UploadServerCertificate and
      ListServerCertificates operations.
      - **Path** *(string) --*

        The path to the server certificate. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ListServerCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListServerCertificatesPaginateResponseTypeDef",
    {
        "ServerCertificateMetadataList": List[
            ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListServerCertificatesPaginateResponseTypeDef(_ListServerCertificatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListServerCertificates request.
      - **ServerCertificateMetadataList** *(list) --*

        A list of server certificates.
        - *(dict) --*

          Contains information about a server certificate without its certificate body, certificate
          chain, and private key.
          This data type is used as a response element in the  UploadServerCertificate and
          ListServerCertificates operations.
          - **Path** *(string) --*

            The path to the server certificate. For more information about paths, see `IAM
            Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
            in the *IAM User Guide* .
    """


_ListSigningCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSigningCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSigningCertificatesPaginatePaginationConfigTypeDef(
    _ListSigningCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSigningCertificatesPaginateResponseCertificatesTypeDef = TypedDict(
    "_ListSigningCertificatesPaginateResponseCertificatesTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)


class ListSigningCertificatesPaginateResponseCertificatesTypeDef(
    _ListSigningCertificatesPaginateResponseCertificatesTypeDef
):
    """
    - *(dict) --*

      Contains information about an X.509 signing certificate.
      This data type is used as a response element in the  UploadSigningCertificate and
      ListSigningCertificates operations.
      - **UserName** *(string) --*

        The name of the user the signing certificate is associated with.
    """


_ListSigningCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListSigningCertificatesPaginateResponseTypeDef",
    {
        "Certificates": List[ListSigningCertificatesPaginateResponseCertificatesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListSigningCertificatesPaginateResponseTypeDef(
    _ListSigningCertificatesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  ListSigningCertificates request.
      - **Certificates** *(list) --*

        A list of the user's signing certificate information.
        - *(dict) --*

          Contains information about an X.509 signing certificate.
          This data type is used as a response element in the  UploadSigningCertificate and
          ListSigningCertificates operations.
          - **UserName** *(string) --*

            The name of the user the signing certificate is associated with.
    """


_ListUserPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserPoliciesPaginatePaginationConfigTypeDef(
    _ListUserPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUserPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListUserPoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListUserPoliciesPaginateResponseTypeDef(_ListUserPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListUserPolicies request.
      - **PolicyNames** *(list) --*

        A list of policy names.
        - *(string) --*
    """


_ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsersPaginatePaginationConfigTypeDef(_ListUsersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef(
    _ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef
):
    pass


_ListUsersPaginateResponseUsersTagsTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListUsersPaginateResponseUsersTagsTypeDef(_ListUsersPaginateResponseUsersTagsTypeDef):
    pass


_ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[ListUsersPaginateResponseUsersTagsTypeDef],
    },
    total=False,
)


class ListUsersPaginateResponseUsersTypeDef(_ListUsersPaginateResponseUsersTypeDef):
    """
    - *(dict) --*

      Contains information about an IAM user entity.
      This data type is used as a response element in the following operations:
      *  CreateUser
      *  GetUser
      *  ListUsers
      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {"Users": List[ListUsersPaginateResponseUsersTypeDef], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListUsers request.
      - **Users** *(list) --*

        A list of users.
        - *(dict) --*

          Contains information about an IAM user entity.
          This data type is used as a response element in the following operations:
          *  CreateUser
          *  GetUser
          *  ListUsers
          - **Path** *(string) --*

            The path to the user. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
            User Guide* .
    """


_ListVirtualMFADevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVirtualMFADevicesPaginatePaginationConfigTypeDef(
    _ListVirtualMFADevicesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef(
    _ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef
):
    pass


_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef(
    _ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef
):
    pass


_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef,
        "Tags": List[ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef],
    },
    total=False,
)


class ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef(
    _ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef
):
    pass


_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)


class ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef(
    _ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef
):
    """
    - *(dict) --*

      Contains information about a virtual MFA device.
      - **SerialNumber** *(string) --*

        The serial number associated with ``VirtualMFADevice`` .
    """


_ListVirtualMFADevicesPaginateResponseTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseTypeDef",
    {
        "VirtualMFADevices": List[ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListVirtualMFADevicesPaginateResponseTypeDef(_ListVirtualMFADevicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  ListVirtualMFADevices request.
      - **VirtualMFADevices** *(list) --*

        The list of virtual MFA devices in the current account that match the ``AssignmentStatus``
        value that was passed in the request.
        - *(dict) --*

          Contains information about a virtual MFA device.
          - **SerialNumber** *(string) --*

            The serial number associated with ``VirtualMFADevice`` .
    """


_PolicyExistsWaitWaiterConfigTypeDef = TypedDict(
    "_PolicyExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class PolicyExistsWaitWaiterConfigTypeDef(_PolicyExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1
    """


_RoleExistsWaitWaiterConfigTypeDef = TypedDict(
    "_RoleExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class RoleExistsWaitWaiterConfigTypeDef(_RoleExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1
    """


_SamlProviderUpdateResponseTypeDef = TypedDict(
    "_SamlProviderUpdateResponseTypeDef", {"SAMLProviderArn": str}, total=False
)


class SamlProviderUpdateResponseTypeDef(_SamlProviderUpdateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  UpdateSAMLProvider request.
      - **SAMLProviderArn** *(string) --*

        The Amazon Resource Name (ARN) of the SAML provider that was updated.
    """


_ServiceResourceCreateRoleTagsTypeDef = TypedDict(
    "_ServiceResourceCreateRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ServiceResourceCreateRoleTagsTypeDef(_ServiceResourceCreateRoleTagsTypeDef):
    pass


_ServiceResourceCreateUserTagsTypeDef = TypedDict(
    "_ServiceResourceCreateUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ServiceResourceCreateUserTagsTypeDef(_ServiceResourceCreateUserTagsTypeDef):
    pass


_SimulateCustomPolicyPaginateContextEntriesTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateContextEntriesTypeDef",
    {
        "ContextKeyName": str,
        "ContextKeyValues": List[str],
        "ContextKeyType": Literal[
            "string",
            "stringList",
            "numeric",
            "numericList",
            "boolean",
            "booleanList",
            "ip",
            "ipList",
            "binary",
            "binaryList",
            "date",
            "dateList",
        ],
    },
    total=False,
)


class SimulateCustomPolicyPaginateContextEntriesTypeDef(
    _SimulateCustomPolicyPaginateContextEntriesTypeDef
):
    """
    - *(dict) --*

      Contains information about a condition context key. It includes the name of the key and
      specifies the value (or values, if the context key supports multiple values) to use in the
      simulation. This information is used when evaluating the ``Condition`` elements of the input
      policies.
      This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``
      SimulatePrincipalPolicy `` .
      - **ContextKeyName** *(string) --*

        The full name of a condition context key, including the service prefix. For example,
        ``aws:SourceIp`` or ``s3:VersionId`` .
    """


_SimulateCustomPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SimulateCustomPolicyPaginatePaginationConfigTypeDef(
    _SimulateCustomPolicyPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef(
    _SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef
):
    pass


_SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef(
    _SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef
):
    pass


_SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)


class SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef(
    _SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef
):
    pass


_SimulateCustomPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)


class SimulateCustomPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef(
    _SimulateCustomPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef
):
    pass


_SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef(
    _SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef
):
    pass


_SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef(
    _SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef
):
    pass


_SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)


class SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef(
    _SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
):
    pass


_SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
    },
    total=False,
)


class SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef(
    _SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef
):
    pass


_SimulateCustomPolicyPaginateResponseEvaluationResultsTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseEvaluationResultsTypeDef",
    {
        "EvalActionName": str,
        "EvalResourceName": str,
        "EvalDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "OrganizationsDecisionDetail": SimulateCustomPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef,
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "ResourceSpecificResults": List[
            SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef
        ],
    },
    total=False,
)


class SimulateCustomPolicyPaginateResponseEvaluationResultsTypeDef(
    _SimulateCustomPolicyPaginateResponseEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      Contains the results of a simulation.
      This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``
      SimulatePrincipalPolicy `` .
      - **EvalActionName** *(string) --*

        The name of the API operation tested on the indicated resource.
    """


_SimulateCustomPolicyPaginateResponseTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateResponseTypeDef",
    {
        "EvaluationResults": List[SimulateCustomPolicyPaginateResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class SimulateCustomPolicyPaginateResponseTypeDef(_SimulateCustomPolicyPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  SimulatePrincipalPolicy or  SimulateCustomPolicy
      request.
      - **EvaluationResults** *(list) --*

        The results of the simulation.
        - *(dict) --*

          Contains the results of a simulation.
          This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``
          SimulatePrincipalPolicy `` .
          - **EvalActionName** *(string) --*

            The name of the API operation tested on the indicated resource.
    """


_SimulatePrincipalPolicyPaginateContextEntriesTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateContextEntriesTypeDef",
    {
        "ContextKeyName": str,
        "ContextKeyValues": List[str],
        "ContextKeyType": Literal[
            "string",
            "stringList",
            "numeric",
            "numericList",
            "boolean",
            "booleanList",
            "ip",
            "ipList",
            "binary",
            "binaryList",
            "date",
            "dateList",
        ],
    },
    total=False,
)


class SimulatePrincipalPolicyPaginateContextEntriesTypeDef(
    _SimulatePrincipalPolicyPaginateContextEntriesTypeDef
):
    """
    - *(dict) --*

      Contains information about a condition context key. It includes the name of the key and
      specifies the value (or values, if the context key supports multiple values) to use in the
      simulation. This information is used when evaluating the ``Condition`` elements of the input
      policies.
      This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``
      SimulatePrincipalPolicy `` .
      - **ContextKeyName** *(string) --*

        The full name of a condition context key, including the service prefix. For example,
        ``aws:SourceIp`` or ``s3:VersionId`` .
    """


_SimulatePrincipalPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SimulatePrincipalPolicyPaginatePaginationConfigTypeDef(
    _SimulatePrincipalPolicyPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef(
    _SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef
):
    pass


_SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef(
    _SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef
):
    pass


_SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef(
    _SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef
):
    pass


_SimulatePrincipalPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef(
    _SimulatePrincipalPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef
):
    pass


_SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef(
    _SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef
):
    pass


_SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef(
    _SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef
):
    pass


_SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef(
    _SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
):
    pass


_SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
    },
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef(
    _SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef
):
    pass


_SimulatePrincipalPolicyPaginateResponseEvaluationResultsTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseEvaluationResultsTypeDef",
    {
        "EvalActionName": str,
        "EvalResourceName": str,
        "EvalDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "OrganizationsDecisionDetail": SimulatePrincipalPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef,
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "ResourceSpecificResults": List[
            SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef
        ],
    },
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseEvaluationResultsTypeDef(
    _SimulatePrincipalPolicyPaginateResponseEvaluationResultsTypeDef
):
    """
    - *(dict) --*

      Contains the results of a simulation.
      This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``
      SimulatePrincipalPolicy `` .
      - **EvalActionName** *(string) --*

        The name of the API operation tested on the indicated resource.
    """


_SimulatePrincipalPolicyPaginateResponseTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateResponseTypeDef",
    {
        "EvaluationResults": List[SimulatePrincipalPolicyPaginateResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class SimulatePrincipalPolicyPaginateResponseTypeDef(
    _SimulatePrincipalPolicyPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  SimulatePrincipalPolicy or  SimulateCustomPolicy
      request.
      - **EvaluationResults** *(list) --*

        The results of the simulation.
        - *(dict) --*

          Contains the results of a simulation.
          This data type is used by the return parameter of ``  SimulateCustomPolicy `` and ``
          SimulatePrincipalPolicy `` .
          - **EvalActionName** *(string) --*

            The name of the API operation tested on the indicated resource.
    """


_UserCreateTagsTypeDef = TypedDict(
    "_UserCreateTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class UserCreateTagsTypeDef(_UserCreateTagsTypeDef):
    pass


_UserExistsWaitWaiterConfigTypeDef = TypedDict(
    "_UserExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class UserExistsWaitWaiterConfigTypeDef(_UserExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1
    """
