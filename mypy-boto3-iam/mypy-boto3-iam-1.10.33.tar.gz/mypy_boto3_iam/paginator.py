"Main interface for iam service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iam.type_defs import (
    GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef,
    GetAccountAuthorizationDetailsPaginateResponseTypeDef,
    GetGroupPaginatePaginationConfigTypeDef,
    GetGroupPaginateResponseTypeDef,
    ListAccessKeysPaginatePaginationConfigTypeDef,
    ListAccessKeysPaginateResponseTypeDef,
    ListAccountAliasesPaginatePaginationConfigTypeDef,
    ListAccountAliasesPaginateResponseTypeDef,
    ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef,
    ListAttachedGroupPoliciesPaginateResponseTypeDef,
    ListAttachedRolePoliciesPaginatePaginationConfigTypeDef,
    ListAttachedRolePoliciesPaginateResponseTypeDef,
    ListAttachedUserPoliciesPaginatePaginationConfigTypeDef,
    ListAttachedUserPoliciesPaginateResponseTypeDef,
    ListEntitiesForPolicyPaginatePaginationConfigTypeDef,
    ListEntitiesForPolicyPaginateResponseTypeDef,
    ListGroupPoliciesPaginatePaginationConfigTypeDef,
    ListGroupPoliciesPaginateResponseTypeDef,
    ListGroupsForUserPaginatePaginationConfigTypeDef,
    ListGroupsForUserPaginateResponseTypeDef,
    ListGroupsPaginatePaginationConfigTypeDef,
    ListGroupsPaginateResponseTypeDef,
    ListInstanceProfilesForRolePaginatePaginationConfigTypeDef,
    ListInstanceProfilesForRolePaginateResponseTypeDef,
    ListInstanceProfilesPaginatePaginationConfigTypeDef,
    ListInstanceProfilesPaginateResponseTypeDef,
    ListMFADevicesPaginatePaginationConfigTypeDef,
    ListMFADevicesPaginateResponseTypeDef,
    ListPoliciesPaginatePaginationConfigTypeDef,
    ListPoliciesPaginateResponseTypeDef,
    ListPolicyVersionsPaginatePaginationConfigTypeDef,
    ListPolicyVersionsPaginateResponseTypeDef,
    ListRolePoliciesPaginatePaginationConfigTypeDef,
    ListRolePoliciesPaginateResponseTypeDef,
    ListRolesPaginatePaginationConfigTypeDef,
    ListRolesPaginateResponseTypeDef,
    ListSSHPublicKeysPaginatePaginationConfigTypeDef,
    ListSSHPublicKeysPaginateResponseTypeDef,
    ListServerCertificatesPaginatePaginationConfigTypeDef,
    ListServerCertificatesPaginateResponseTypeDef,
    ListSigningCertificatesPaginatePaginationConfigTypeDef,
    ListSigningCertificatesPaginateResponseTypeDef,
    ListUserPoliciesPaginatePaginationConfigTypeDef,
    ListUserPoliciesPaginateResponseTypeDef,
    ListUsersPaginatePaginationConfigTypeDef,
    ListUsersPaginateResponseTypeDef,
    ListVirtualMFADevicesPaginatePaginationConfigTypeDef,
    ListVirtualMFADevicesPaginateResponseTypeDef,
    SimulateCustomPolicyPaginateContextEntriesTypeDef,
    SimulateCustomPolicyPaginatePaginationConfigTypeDef,
    SimulateCustomPolicyPaginateResponseTypeDef,
    SimulatePrincipalPolicyPaginateContextEntriesTypeDef,
    SimulatePrincipalPolicyPaginatePaginationConfigTypeDef,
    SimulatePrincipalPolicyPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetAccountAuthorizationDetailsPaginator",
    "GetGroupPaginator",
    "ListAccessKeysPaginator",
    "ListAccountAliasesPaginator",
    "ListAttachedGroupPoliciesPaginator",
    "ListAttachedRolePoliciesPaginator",
    "ListAttachedUserPoliciesPaginator",
    "ListEntitiesForPolicyPaginator",
    "ListGroupPoliciesPaginator",
    "ListGroupsPaginator",
    "ListGroupsForUserPaginator",
    "ListInstanceProfilesPaginator",
    "ListInstanceProfilesForRolePaginator",
    "ListMFADevicesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyVersionsPaginator",
    "ListRolePoliciesPaginator",
    "ListRolesPaginator",
    "ListSSHPublicKeysPaginator",
    "ListServerCertificatesPaginator",
    "ListSigningCertificatesPaginator",
    "ListUserPoliciesPaginator",
    "ListUsersPaginator",
    "ListVirtualMFADevicesPaginator",
    "SimulateCustomPolicyPaginator",
    "SimulatePrincipalPolicyPaginator",
)


class GetAccountAuthorizationDetailsPaginator(Boto3Paginator):
    """
    Paginator for `get_account_authorization_details`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: List[
            Literal["User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"]
        ] = None,
        PaginationConfig: GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef = None,
    ) -> GetAccountAuthorizationDetailsPaginateResponseTypeDef:
        """
        [GetAccountAuthorizationDetails.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails.paginate)
        """


class GetGroupPaginator(Boto3Paginator):
    """
    Paginator for `get_group`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GroupName: str, PaginationConfig: GetGroupPaginatePaginationConfigTypeDef = None
    ) -> GetGroupPaginateResponseTypeDef:
        """
        [GetGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.GetGroup.paginate)
        """


class ListAccessKeysPaginator(Boto3Paginator):
    """
    Paginator for `list_access_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserName: str = None,
        PaginationConfig: ListAccessKeysPaginatePaginationConfigTypeDef = None,
    ) -> ListAccessKeysPaginateResponseTypeDef:
        """
        [ListAccessKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListAccessKeys.paginate)
        """


class ListAccountAliasesPaginator(Boto3Paginator):
    """
    Paginator for `list_account_aliases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListAccountAliasesPaginatePaginationConfigTypeDef = None
    ) -> ListAccountAliasesPaginateResponseTypeDef:
        """
        [ListAccountAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListAccountAliases.paginate)
        """


class ListAttachedGroupPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_attached_group_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GroupName: str,
        PathPrefix: str = None,
        PaginationConfig: ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListAttachedGroupPoliciesPaginateResponseTypeDef:
        """
        [ListAttachedGroupPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies.paginate)
        """


class ListAttachedRolePoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_attached_role_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RoleName: str,
        PathPrefix: str = None,
        PaginationConfig: ListAttachedRolePoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListAttachedRolePoliciesPaginateResponseTypeDef:
        """
        [ListAttachedRolePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies.paginate)
        """


class ListAttachedUserPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_attached_user_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserName: str,
        PathPrefix: str = None,
        PaginationConfig: ListAttachedUserPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListAttachedUserPoliciesPaginateResponseTypeDef:
        """
        [ListAttachedUserPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies.paginate)
        """


class ListEntitiesForPolicyPaginator(Boto3Paginator):
    """
    Paginator for `list_entities_for_policy`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicyArn: str,
        EntityFilter: Literal[
            "User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"
        ] = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        PaginationConfig: ListEntitiesForPolicyPaginatePaginationConfigTypeDef = None,
    ) -> ListEntitiesForPolicyPaginateResponseTypeDef:
        """
        [ListEntitiesForPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy.paginate)
        """


class ListGroupPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_group_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GroupName: str,
        PaginationConfig: ListGroupPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListGroupPoliciesPaginateResponseTypeDef:
        """
        [ListGroupPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListGroupPolicies.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: ListGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListGroupsPaginateResponseTypeDef:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListGroups.paginate)
        """


class ListGroupsForUserPaginator(Boto3Paginator):
    """
    Paginator for `list_groups_for_user`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserName: str,
        PaginationConfig: ListGroupsForUserPaginatePaginationConfigTypeDef = None,
    ) -> ListGroupsForUserPaginateResponseTypeDef:
        """
        [ListGroupsForUser.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListGroupsForUser.paginate)
        """


class ListInstanceProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_instance_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: ListInstanceProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListInstanceProfilesPaginateResponseTypeDef:
        """
        [ListInstanceProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles.paginate)
        """


class ListInstanceProfilesForRolePaginator(Boto3Paginator):
    """
    Paginator for `list_instance_profiles_for_role`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RoleName: str,
        PaginationConfig: ListInstanceProfilesForRolePaginatePaginationConfigTypeDef = None,
    ) -> ListInstanceProfilesForRolePaginateResponseTypeDef:
        """
        [ListInstanceProfilesForRole.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole.paginate)
        """


class ListMFADevicesPaginator(Boto3Paginator):
    """
    Paginator for `list_mfa_devices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserName: str = None,
        PaginationConfig: ListMFADevicesPaginatePaginationConfigTypeDef = None,
    ) -> ListMFADevicesPaginateResponseTypeDef:
        """
        [ListMFADevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListMFADevices.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Scope: Literal["All", "AWS", "Local"] = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        PaginationConfig: ListPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListPoliciesPaginateResponseTypeDef:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListPolicies.paginate)
        """


class ListPolicyVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_policy_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicyArn: str,
        PaginationConfig: ListPolicyVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListPolicyVersionsPaginateResponseTypeDef:
        """
        [ListPolicyVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListPolicyVersions.paginate)
        """


class ListRolePoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_role_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RoleName: str,
        PaginationConfig: ListRolePoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListRolePoliciesPaginateResponseTypeDef:
        """
        [ListRolePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListRolePolicies.paginate)
        """


class ListRolesPaginator(Boto3Paginator):
    """
    Paginator for `list_roles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: ListRolesPaginatePaginationConfigTypeDef = None,
    ) -> ListRolesPaginateResponseTypeDef:
        """
        [ListRoles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListRoles.paginate)
        """


class ListSSHPublicKeysPaginator(Boto3Paginator):
    """
    Paginator for `list_ssh_public_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserName: str = None,
        PaginationConfig: ListSSHPublicKeysPaginatePaginationConfigTypeDef = None,
    ) -> ListSSHPublicKeysPaginateResponseTypeDef:
        """
        [ListSSHPublicKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys.paginate)
        """


class ListServerCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `list_server_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: ListServerCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> ListServerCertificatesPaginateResponseTypeDef:
        """
        [ListServerCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListServerCertificates.paginate)
        """


class ListSigningCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `list_signing_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserName: str = None,
        PaginationConfig: ListSigningCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> ListSigningCertificatesPaginateResponseTypeDef:
        """
        [ListSigningCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListSigningCertificates.paginate)
        """


class ListUserPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_user_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserName: str,
        PaginationConfig: ListUserPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListUserPoliciesPaginateResponseTypeDef:
        """
        [ListUserPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListUserPolicies.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    Paginator for `list_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PathPrefix: str = None,
        PaginationConfig: ListUsersPaginatePaginationConfigTypeDef = None,
    ) -> ListUsersPaginateResponseTypeDef:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListUsers.paginate)
        """


class ListVirtualMFADevicesPaginator(Boto3Paginator):
    """
    Paginator for `list_virtual_mfa_devices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssignmentStatus: Literal["Assigned", "Unassigned", "Any"] = None,
        PaginationConfig: ListVirtualMFADevicesPaginatePaginationConfigTypeDef = None,
    ) -> ListVirtualMFADevicesPaginateResponseTypeDef:
        """
        [ListVirtualMFADevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices.paginate)
        """


class SimulateCustomPolicyPaginator(Boto3Paginator):
    """
    Paginator for `simulate_custom_policy`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicyInputList: List[str],
        ActionNames: List[str],
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[SimulateCustomPolicyPaginateContextEntriesTypeDef] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: SimulateCustomPolicyPaginatePaginationConfigTypeDef = None,
    ) -> SimulateCustomPolicyPaginateResponseTypeDef:
        """
        [SimulateCustomPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy.paginate)
        """


class SimulatePrincipalPolicyPaginator(Boto3Paginator):
    """
    Paginator for `simulate_principal_policy`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicySourceArn: str,
        ActionNames: List[str],
        PolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[SimulatePrincipalPolicyPaginateContextEntriesTypeDef] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: SimulatePrincipalPolicyPaginatePaginationConfigTypeDef = None,
    ) -> SimulatePrincipalPolicyPaginateResponseTypeDef:
        """
        [SimulatePrincipalPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy.paginate)
        """
