"Main interface for iam service ServiceResource"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_iam.service_resource as service_resource_scope
from mypy_boto3_iam.type_defs import (
    SamlProviderUpdateResponseTypeDef,
    ServiceResourceCreateRoleTagsTypeDef,
    ServiceResourceCreateUserTagsTypeDef,
    UserCreateTagsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ServiceResource",
    "AccessKey",
    "AccessKeyPair",
    "AccountPasswordPolicy",
    "AccountSummary",
    "AssumeRolePolicy",
    "CurrentUser",
    "Group",
    "GroupPolicy",
    "InstanceProfile",
    "LoginProfile",
    "MfaDevice",
    "Policy",
    "PolicyVersion",
    "Role",
    "RolePolicy",
    "SamlProvider",
    "ServerCertificate",
    "SigningCertificate",
    "User",
    "UserPolicy",
    "VirtualMfaDevice",
    "ServiceResourceGroupsCollection",
    "ServiceResourceInstanceProfilesCollection",
    "ServiceResourcePoliciesCollection",
    "ServiceResourceRolesCollection",
    "ServiceResourceSamlProvidersCollection",
    "ServiceResourceServerCertificatesCollection",
    "ServiceResourceUsersCollection",
    "ServiceResourceVirtualMfaDevicesCollection",
    "CurrentUserAccessKeysCollection",
    "CurrentUserMfaDevicesCollection",
    "CurrentUserSigningCertificatesCollection",
    "GroupAttachedPoliciesCollection",
    "GroupPoliciesCollection",
    "GroupUsersCollection",
    "PolicyAttachedGroupsCollection",
    "PolicyAttachedRolesCollection",
    "PolicyAttachedUsersCollection",
    "PolicyVersionsCollection",
    "RoleAttachedPoliciesCollection",
    "RoleInstanceProfilesCollection",
    "RolePoliciesCollection",
    "UserAccessKeysCollection",
    "UserAttachedPoliciesCollection",
    "UserGroupsCollection",
    "UserMfaDevicesCollection",
    "UserPoliciesCollection",
    "UserSigningCertificatesCollection",
)


class ServiceResource(Boto3ServiceResource):
    """
    [IAM.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource)
    """

    groups: service_resource_scope.ServiceResourceGroupsCollection
    instance_profiles: service_resource_scope.ServiceResourceInstanceProfilesCollection
    policies: service_resource_scope.ServiceResourcePoliciesCollection
    roles: service_resource_scope.ServiceResourceRolesCollection
    saml_providers: service_resource_scope.ServiceResourceSamlProvidersCollection
    server_certificates: service_resource_scope.ServiceResourceServerCertificatesCollection
    users: service_resource_scope.ServiceResourceUsersCollection
    virtual_mfa_devices: service_resource_scope.ServiceResourceVirtualMfaDevicesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccessKey(self, user_name: str, id: str) -> service_resource_scope.AccessKey:
        """
        [ServiceResource.AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AccessKey)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccessKeyPair(
        self, user_name: str, id: str, secret: str
    ) -> service_resource_scope.AccessKeyPair:
        """
        [ServiceResource.AccessKeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccountPasswordPolicy(
        self, *args: Any, **kwargs: Any
    ) -> service_resource_scope.AccountPasswordPolicy:
        """
        [ServiceResource.AccountPasswordPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccountSummary(self, *args: Any, **kwargs: Any) -> service_resource_scope.AccountSummary:
        """
        [ServiceResource.AccountSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AssumeRolePolicy(self, role_name: str) -> service_resource_scope.AssumeRolePolicy:
        """
        [ServiceResource.AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def CurrentUser(self, *args: Any, **kwargs: Any) -> service_resource_scope.CurrentUser:
        """
        [ServiceResource.CurrentUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Group(self, name: str) -> service_resource_scope.Group:
        """
        [ServiceResource.Group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.Group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def GroupPolicy(self, group_name: str, name: str) -> service_resource_scope.GroupPolicy:
        """
        [ServiceResource.GroupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def InstanceProfile(self, name: str) -> service_resource_scope.InstanceProfile:
        """
        [ServiceResource.InstanceProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def LoginProfile(self, user_name: str) -> service_resource_scope.LoginProfile:
        """
        [ServiceResource.LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def MfaDevice(self, user_name: str, serial_number: str) -> service_resource_scope.MfaDevice:
        """
        [ServiceResource.MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Policy(self, policy_arn: str) -> service_resource_scope.Policy:
        """
        [ServiceResource.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.Policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def PolicyVersion(self, arn: str, version_id: str) -> service_resource_scope.PolicyVersion:
        """
        [ServiceResource.PolicyVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Role(self, name: str) -> service_resource_scope.Role:
        """
        [ServiceResource.Role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.Role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def RolePolicy(self, role_name: str, name: str) -> service_resource_scope.RolePolicy:
        """
        [ServiceResource.RolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def SamlProvider(self, arn: str) -> service_resource_scope.SamlProvider:
        """
        [ServiceResource.SamlProvider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def ServerCertificate(self, name: str) -> service_resource_scope.ServerCertificate:
        """
        [ServiceResource.ServerCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def SigningCertificate(
        self, user_name: str, id: str
    ) -> service_resource_scope.SigningCertificate:
        """
        [ServiceResource.SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def User(self, name: str) -> service_resource_scope.User:
        """
        [ServiceResource.User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.User)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def UserPolicy(self, user_name: str, name: str) -> service_resource_scope.UserPolicy:
        """
        [ServiceResource.UserPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def VirtualMfaDevice(self, serial_number: str) -> service_resource_scope.VirtualMfaDevice:
        """
        [ServiceResource.VirtualMfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_password(self, OldPassword: str, NewPassword: str) -> None:
        """
        [ServiceResource.change_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.change_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_account_alias(self, AccountAlias: str) -> None:
        """
        [ServiceResource.create_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_account_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_account_password_policy(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> service_resource_scope.AccountPasswordPolicy:
        """
        [ServiceResource.create_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_account_password_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(self, GroupName: str, Path: str = None) -> List[service_resource_scope.Group]:
        """
        [ServiceResource.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instance_profile(
        self, InstanceProfileName: str, Path: str = None
    ) -> service_resource_scope.InstanceProfile:
        """
        [ServiceResource.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_instance_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self, PolicyName: str, PolicyDocument: str, Path: str = None, Description: str = None
    ) -> service_resource_scope.Policy:
        """
        [ServiceResource.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_role(
        self,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = None,
        Description: str = None,
        MaxSessionDuration: int = None,
        PermissionsBoundary: str = None,
        Tags: List[ServiceResourceCreateRoleTagsTypeDef] = None,
    ) -> service_resource_scope.Role:
        """
        [ServiceResource.create_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_saml_provider(
        self, SAMLMetadataDocument: str, Name: str
    ) -> service_resource_scope.SamlProvider:
        """
        [ServiceResource.create_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_saml_provider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_server_certificate(
        self,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = None,
        CertificateChain: str = None,
    ) -> service_resource_scope.ServerCertificate:
        """
        [ServiceResource.create_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_server_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_signing_certificate(
        self, CertificateBody: str, UserName: str = None
    ) -> service_resource_scope.SigningCertificate:
        """
        [ServiceResource.create_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_signing_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self,
        UserName: str,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List[ServiceResourceCreateUserTagsTypeDef] = None,
    ) -> service_resource_scope.User:
        """
        [ServiceResource.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_virtual_mfa_device(
        self, VirtualMFADeviceName: str, Path: str = None
    ) -> service_resource_scope.VirtualMfaDevice:
        """
        [ServiceResource.create_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.create_virtual_mfa_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.get_available_subresources)
        """


class AccessKey(Boto3ServiceResource):
    """
    [AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AccessKey)
    """

    access_key_id: str
    status: str
    create_date: datetime
    user_name: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class AccessKeyPair(Boto3ServiceResource):
    """
    [AccessKeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
    """

    access_key_id: str
    status: str
    secret_access_key: str
    create_date: datetime
    user_name: str
    id: str
    secret: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class AccountPasswordPolicy(Boto3ServiceResource):
    """
    [AccountPasswordPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
    """

    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> None:
        pass


class AccountSummary(Boto3ServiceResource):
    """
    [AccountSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
    """

    summary_map: Dict[str, Any]

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class AssumeRolePolicy(Boto3ServiceResource):
    """
    [AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
    """

    role_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, PolicyDocument: str) -> None:
        pass


class CurrentUser(Boto3ServiceResource):
    """
    [CurrentUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    access_keys: service_resource_scope.CurrentUserAccessKeysCollection
    mfa_devices: service_resource_scope.CurrentUserMfaDevicesCollection
    signing_certificates: service_resource_scope.CurrentUserSigningCertificatesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class Group(Boto3ServiceResource):
    """
    [Group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.Group)
    """

    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    name: str
    attached_policies: service_resource_scope.GroupAttachedPoliciesCollection
    policies: service_resource_scope.GroupPoliciesCollection
    users: service_resource_scope.GroupUsersCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_user(self, UserName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyArn: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(self, Path: str = None) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self, PolicyName: str, PolicyDocument: str
    ) -> service_resource_scope.GroupPolicy:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyArn: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_user(self, UserName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self, NewPath: str = None, NewGroupName: str = None
    ) -> List[service_resource_scope.Group]:
        pass


class GroupPolicy(Boto3ServiceResource):
    """
    [GroupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
    """

    policy_name: str
    policy_document: str
    group_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, PolicyDocument: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class InstanceProfile(Boto3ServiceResource):
    """
    [InstanceProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
    """

    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List[Any]
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_role(self, RoleName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_role(self, RoleName: str) -> None:
        pass


class LoginProfile(Boto3ServiceResource):
    """
    [LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
    """

    create_date: datetime
    password_reset_required: bool
    user_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(
        self, Password: str, PasswordResetRequired: bool = None
    ) -> service_resource_scope.LoginProfile:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, Password: str = None, PasswordResetRequired: bool = None) -> None:
        pass


class MfaDevice(Boto3ServiceResource):
    """
    [MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
    """

    enable_date: datetime
    user_name: str
    serial_number: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resync(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        pass


class Policy(Boto3ServiceResource):
    """
    [Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.Policy)
    """

    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    arn: str
    attached_groups: service_resource_scope.PolicyAttachedGroupsCollection
    attached_roles: service_resource_scope.PolicyAttachedRolesCollection
    attached_users: service_resource_scope.PolicyAttachedUsersCollection
    versions: service_resource_scope.PolicyVersionsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_group(self, GroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_role(self, RoleName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_user(self, UserName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_version(
        self, PolicyDocument: str, SetAsDefault: bool = None
    ) -> service_resource_scope.PolicyVersion:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_group(self, GroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_role(self, RoleName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_user(self, UserName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class PolicyVersion(Boto3ServiceResource):
    """
    [PolicyVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
    """

    document: str
    is_default_version: bool
    create_date: datetime
    arn: str
    version_id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_as_default(self, *args: Any, **kwargs: Any) -> None:
        pass


class Role(Boto3ServiceResource):
    """
    [Role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.Role)
    """

    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: str
    description: str
    max_session_duration: int
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    role_last_used: Dict[str, Any]
    name: str
    attached_policies: service_resource_scope.RoleAttachedPoliciesCollection
    instance_profiles: service_resource_scope.RoleInstanceProfilesCollection
    policies: service_resource_scope.RolePoliciesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyArn: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyArn: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class RolePolicy(Boto3ServiceResource):
    """
    [RolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
    """

    policy_name: str
    policy_document: str
    role_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, PolicyDocument: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class SamlProvider(Boto3ServiceResource):
    """
    [SamlProvider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
    """

    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    arn: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, SAMLMetadataDocument: str) -> SamlProviderUpdateResponseTypeDef:
        pass


class ServerCertificate(Boto3ServiceResource):
    """
    [ServerCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
    """

    server_certificate_metadata: Dict[str, Any]
    certificate_body: str
    certificate_chain: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self, NewPath: str = None, NewServerCertificateName: str = None
    ) -> service_resource_scope.ServerCertificate:
        pass


class SigningCertificate(Boto3ServiceResource):
    """
    [SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
    """

    certificate_id: str
    certificate_body: str
    status: str
    upload_date: datetime
    user_name: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class User(Boto3ServiceResource):
    """
    [User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.User)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    name: str
    access_keys: service_resource_scope.UserAccessKeysCollection
    attached_policies: service_resource_scope.UserAttachedPoliciesCollection
    groups: service_resource_scope.UserGroupsCollection
    mfa_devices: service_resource_scope.UserMfaDevicesCollection
    policies: service_resource_scope.UserPoliciesCollection
    signing_certificates: service_resource_scope.UserSigningCertificatesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_group(self, GroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyArn: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(
        self,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List[UserCreateTagsTypeDef] = None,
    ) -> service_resource_scope.User:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_access_key_pair(
        self, *args: Any, **kwargs: Any
    ) -> service_resource_scope.AccessKeyPair:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_login_profile(
        self, Password: str, PasswordResetRequired: bool = None
    ) -> service_resource_scope.LoginProfile:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self, PolicyName: str, PolicyDocument: str
    ) -> service_resource_scope.UserPolicy:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyArn: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_mfa(
        self, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> service_resource_scope.MfaDevice:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_group(self, GroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, NewPath: str = None, NewUserName: str = None) -> service_resource_scope.User:
        pass


class UserPolicy(Boto3ServiceResource):
    """
    [UserPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
    """

    policy_name: str
    policy_document: str
    user_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, PolicyDocument: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class VirtualMfaDevice(Boto3ServiceResource):
    """
    [VirtualMfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
    """

    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: Dict[str, Any]
    enable_date: datetime
    serial_number: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class ServiceResourceGroupsCollection(ResourceCollection):
    """
    [ServiceResource.groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.groups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceInstanceProfilesCollection(ResourceCollection):
    """
    [ServiceResource.instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.InstanceProfile]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.InstanceProfile]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.InstanceProfile]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.InstanceProfile]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourcePoliciesCollection(ResourceCollection):
    """
    [ServiceResource.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.policies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Scope: Literal["All", "AWS", "Local"] = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceRolesCollection(ResourceCollection):
    """
    [ServiceResource.roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.roles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Role]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Role]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Role]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Role]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceSamlProvidersCollection(ResourceCollection):
    """
    [ServiceResource.saml_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.saml_providers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.SamlProvider]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, **kwargs: Any) -> List[service_resource_scope.SamlProvider]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.SamlProvider]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.SamlProvider]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceServerCertificatesCollection(ResourceCollection):
    """
    [ServiceResource.server_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.server_certificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.ServerCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.ServerCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.ServerCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.ServerCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceUsersCollection(ResourceCollection):
    """
    [ServiceResource.users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.users)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceVirtualMfaDevicesCollection(ResourceCollection):
    """
    [ServiceResource.virtual_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.VirtualMfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        AssignmentStatus: Literal["Assigned", "Unassigned", "Any"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.VirtualMfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.VirtualMfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.VirtualMfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class CurrentUserAccessKeysCollection(ResourceCollection):
    """
    [CurrentUser.access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.CurrentUser.access_keys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.AccessKey]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.AccessKey]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.AccessKey]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.AccessKey]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class CurrentUserMfaDevicesCollection(ResourceCollection):
    """
    [CurrentUser.mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.CurrentUser.mfa_devices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.MfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.MfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.MfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.MfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class CurrentUserSigningCertificatesCollection(ResourceCollection):
    """
    [CurrentUser.signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.CurrentUser.signing_certificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.SigningCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.SigningCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.SigningCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.SigningCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class GroupAttachedPoliciesCollection(ResourceCollection):
    """
    [Group.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Group.attached_policies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class GroupPoliciesCollection(ResourceCollection):
    """
    [Group.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Group.policies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.GroupPolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.GroupPolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.GroupPolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.GroupPolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class GroupUsersCollection(ResourceCollection):
    """
    [Group.users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Group.users)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, Marker: str = None, MaxItems: int = None) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class PolicyAttachedGroupsCollection(ResourceCollection):
    """
    [Policy.attached_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Policy.attached_groups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class PolicyAttachedRolesCollection(ResourceCollection):
    """
    [Policy.attached_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Policy.attached_roles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Role]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.Role]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Role]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Role]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class PolicyAttachedUsersCollection(ResourceCollection):
    """
    [Policy.attached_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Policy.attached_users)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.User]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class PolicyVersionsCollection(ResourceCollection):
    """
    [Policy.versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Policy.versions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.PolicyVersion]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.PolicyVersion]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.PolicyVersion]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.PolicyVersion]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class RoleAttachedPoliciesCollection(ResourceCollection):
    """
    [Role.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Role.attached_policies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class RoleInstanceProfilesCollection(ResourceCollection):
    """
    [Role.instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Role.instance_profiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.InstanceProfile]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.InstanceProfile]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.InstanceProfile]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.InstanceProfile]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class RolePoliciesCollection(ResourceCollection):
    """
    [Role.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.Role.policies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.RolePolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.RolePolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.RolePolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.RolePolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class UserAccessKeysCollection(ResourceCollection):
    """
    [User.access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.User.access_keys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.AccessKey]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.AccessKey]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.AccessKey]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.AccessKey]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class UserAttachedPoliciesCollection(ResourceCollection):
    """
    [User.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.User.attached_policies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Policy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class UserGroupsCollection(ResourceCollection):
    """
    [User.groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.User.groups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Group]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class UserMfaDevicesCollection(ResourceCollection):
    """
    [User.mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.User.mfa_devices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.MfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.MfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.MfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.MfaDevice]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class UserPoliciesCollection(ResourceCollection):
    """
    [User.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.User.policies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.UserPolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.UserPolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.UserPolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.UserPolicy]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class UserSigningCertificatesCollection(ResourceCollection):
    """
    [User.signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/iam.html#IAM.User.signing_certificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.SigningCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.SigningCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.SigningCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.SigningCertificate]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass
