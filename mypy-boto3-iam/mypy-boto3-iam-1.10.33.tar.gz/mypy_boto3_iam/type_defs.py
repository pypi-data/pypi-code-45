"Main interface for iam service type defs"
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


ClientCreateAccessKeyResponseAccessKeyTypeDef = TypedDict(
    "ClientCreateAccessKeyResponseAccessKeyTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "SecretAccessKey": str,
        "CreateDate": datetime,
    },
    total=False,
)

ClientCreateAccessKeyResponseTypeDef = TypedDict(
    "ClientCreateAccessKeyResponseTypeDef",
    {"AccessKey": ClientCreateAccessKeyResponseAccessKeyTypeDef},
    total=False,
)

ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "ClientCreateGroupResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)

ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef",
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

ClientCreateInstanceProfileResponseInstanceProfileTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileTypeDef",
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

ClientCreateInstanceProfileResponseTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseTypeDef",
    {"InstanceProfile": ClientCreateInstanceProfileResponseInstanceProfileTypeDef},
    total=False,
)

ClientCreateLoginProfileResponseLoginProfileTypeDef = TypedDict(
    "ClientCreateLoginProfileResponseLoginProfileTypeDef",
    {"UserName": str, "CreateDate": datetime, "PasswordResetRequired": bool},
    total=False,
)

ClientCreateLoginProfileResponseTypeDef = TypedDict(
    "ClientCreateLoginProfileResponseTypeDef",
    {"LoginProfile": ClientCreateLoginProfileResponseLoginProfileTypeDef},
    total=False,
)

ClientCreateOpenIdConnectProviderResponseTypeDef = TypedDict(
    "ClientCreateOpenIdConnectProviderResponseTypeDef",
    {"OpenIDConnectProviderArn": str},
    total=False,
)

ClientCreatePolicyResponsePolicyTypeDef = TypedDict(
    "ClientCreatePolicyResponsePolicyTypeDef",
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

ClientCreatePolicyResponseTypeDef = TypedDict(
    "ClientCreatePolicyResponseTypeDef",
    {"Policy": ClientCreatePolicyResponsePolicyTypeDef},
    total=False,
)

ClientCreatePolicyVersionResponsePolicyVersionTypeDef = TypedDict(
    "ClientCreatePolicyVersionResponsePolicyVersionTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

ClientCreatePolicyVersionResponseTypeDef = TypedDict(
    "ClientCreatePolicyVersionResponseTypeDef",
    {"PolicyVersion": ClientCreatePolicyVersionResponsePolicyVersionTypeDef},
    total=False,
)

ClientCreateRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "ClientCreateRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientCreateRoleResponseRoleTagsTypeDef = TypedDict(
    "ClientCreateRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateRoleResponseRoleTypeDef = TypedDict(
    "ClientCreateRoleResponseRoleTypeDef",
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

ClientCreateRoleResponseTypeDef = TypedDict(
    "ClientCreateRoleResponseTypeDef", {"Role": ClientCreateRoleResponseRoleTypeDef}, total=False
)

ClientCreateRoleTagsTypeDef = TypedDict(
    "ClientCreateRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSamlProviderResponseTypeDef = TypedDict(
    "ClientCreateSamlProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)

ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateServiceLinkedRoleResponseRoleTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseRoleTypeDef",
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

ClientCreateServiceLinkedRoleResponseTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseTypeDef",
    {"Role": ClientCreateServiceLinkedRoleResponseRoleTypeDef},
    total=False,
)

ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef = TypedDict(
    "ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
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

ClientCreateServiceSpecificCredentialResponseTypeDef = TypedDict(
    "ClientCreateServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
    },
    total=False,
)

ClientCreateUserResponseUserPermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateUserResponseUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateUserResponseUserTagsTypeDef = TypedDict(
    "ClientCreateUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateUserResponseUserTypeDef = TypedDict(
    "ClientCreateUserResponseUserTypeDef",
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

ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"User": ClientCreateUserResponseUserTypeDef}, total=False
)

ClientCreateUserTagsTypeDef = TypedDict(
    "ClientCreateUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef",
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

ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)

ClientCreateVirtualMfaDeviceResponseTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseTypeDef",
    {"VirtualMFADevice": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef},
    total=False,
)

ClientDeleteServiceLinkedRoleResponseTypeDef = TypedDict(
    "ClientDeleteServiceLinkedRoleResponseTypeDef", {"DeletionTaskId": str}, total=False
)

ClientGenerateCredentialReportResponseTypeDef = TypedDict(
    "ClientGenerateCredentialReportResponseTypeDef",
    {"State": Literal["STARTED", "INPROGRESS", "COMPLETE"], "Description": str},
    total=False,
)

ClientGenerateOrganizationsAccessReportResponseTypeDef = TypedDict(
    "ClientGenerateOrganizationsAccessReportResponseTypeDef", {"JobId": str}, total=False
)

ClientGenerateServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "ClientGenerateServiceLastAccessedDetailsResponseTypeDef", {"JobId": str}, total=False
)

ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef = TypedDict(
    "ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef",
    {"LastUsedDate": datetime, "ServiceName": str, "Region": str},
    total=False,
)

ClientGetAccessKeyLastUsedResponseTypeDef = TypedDict(
    "ClientGetAccessKeyLastUsedResponseTypeDef",
    {
        "UserName": str,
        "AccessKeyLastUsed": ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef,
    },
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef",
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

ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef",
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

ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef",
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

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef",
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

ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef",
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

ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef",
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

ClientGetAccountAuthorizationDetailsResponseTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseTypeDef",
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

ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef = TypedDict(
    "ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef",
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

ClientGetAccountPasswordPolicyResponseTypeDef = TypedDict(
    "ClientGetAccountPasswordPolicyResponseTypeDef",
    {"PasswordPolicy": ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef},
    total=False,
)

ClientGetAccountSummaryResponseTypeDef = TypedDict(
    "ClientGetAccountSummaryResponseTypeDef", {"SummaryMap": Dict[str, int]}, total=False
)

ClientGetContextKeysForCustomPolicyResponseTypeDef = TypedDict(
    "ClientGetContextKeysForCustomPolicyResponseTypeDef",
    {"ContextKeyNames": List[str]},
    total=False,
)

ClientGetContextKeysForPrincipalPolicyResponseTypeDef = TypedDict(
    "ClientGetContextKeysForPrincipalPolicyResponseTypeDef",
    {"ContextKeyNames": List[str]},
    total=False,
)

ClientGetCredentialReportResponseTypeDef = TypedDict(
    "ClientGetCredentialReportResponseTypeDef",
    {"Content": bytes, "ReportFormat": str, "GeneratedTime": datetime},
    total=False,
)

ClientGetGroupPolicyResponseTypeDef = TypedDict(
    "ClientGetGroupPolicyResponseTypeDef",
    {"GroupName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetGroupResponseGroupTypeDef = TypedDict(
    "ClientGetGroupResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ClientGetGroupResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetGroupResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetGroupResponseUsersTagsTypeDef = TypedDict(
    "ClientGetGroupResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetGroupResponseUsersTypeDef = TypedDict(
    "ClientGetGroupResponseUsersTypeDef",
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

ClientGetGroupResponseTypeDef = TypedDict(
    "ClientGetGroupResponseTypeDef",
    {
        "Group": ClientGetGroupResponseGroupTypeDef,
        "Users": List[ClientGetGroupResponseUsersTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef",
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

ClientGetInstanceProfileResponseInstanceProfileTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileTypeDef",
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

ClientGetInstanceProfileResponseTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseTypeDef",
    {"InstanceProfile": ClientGetInstanceProfileResponseInstanceProfileTypeDef},
    total=False,
)

ClientGetLoginProfileResponseLoginProfileTypeDef = TypedDict(
    "ClientGetLoginProfileResponseLoginProfileTypeDef",
    {"UserName": str, "CreateDate": datetime, "PasswordResetRequired": bool},
    total=False,
)

ClientGetLoginProfileResponseTypeDef = TypedDict(
    "ClientGetLoginProfileResponseTypeDef",
    {"LoginProfile": ClientGetLoginProfileResponseLoginProfileTypeDef},
    total=False,
)

ClientGetOpenIdConnectProviderResponseTypeDef = TypedDict(
    "ClientGetOpenIdConnectProviderResponseTypeDef",
    {"Url": str, "ClientIDList": List[str], "ThumbprintList": List[str], "CreateDate": datetime},
    total=False,
)

ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef = TypedDict(
    "ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef",
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

ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef = TypedDict(
    "ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef",
    {"Message": str, "Code": str},
    total=False,
)

ClientGetOrganizationsAccessReportResponseTypeDef = TypedDict(
    "ClientGetOrganizationsAccessReportResponseTypeDef",
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

ClientGetPolicyResponsePolicyTypeDef = TypedDict(
    "ClientGetPolicyResponsePolicyTypeDef",
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

ClientGetPolicyResponseTypeDef = TypedDict(
    "ClientGetPolicyResponseTypeDef", {"Policy": ClientGetPolicyResponsePolicyTypeDef}, total=False
)

ClientGetPolicyVersionResponsePolicyVersionTypeDef = TypedDict(
    "ClientGetPolicyVersionResponsePolicyVersionTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

ClientGetPolicyVersionResponseTypeDef = TypedDict(
    "ClientGetPolicyVersionResponseTypeDef",
    {"PolicyVersion": ClientGetPolicyVersionResponsePolicyVersionTypeDef},
    total=False,
)

ClientGetRolePolicyResponseTypeDef = TypedDict(
    "ClientGetRolePolicyResponseTypeDef",
    {"RoleName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "ClientGetRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "ClientGetRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientGetRoleResponseRoleTagsTypeDef = TypedDict(
    "ClientGetRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetRoleResponseRoleTypeDef = TypedDict(
    "ClientGetRoleResponseRoleTypeDef",
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

ClientGetRoleResponseTypeDef = TypedDict(
    "ClientGetRoleResponseTypeDef", {"Role": ClientGetRoleResponseRoleTypeDef}, total=False
)

ClientGetSamlProviderResponseTypeDef = TypedDict(
    "ClientGetSamlProviderResponseTypeDef",
    {"SAMLMetadataDocument": str, "CreateDate": datetime, "ValidUntil": datetime},
    total=False,
)

ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef = TypedDict(
    "ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef",
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

ClientGetServerCertificateResponseServerCertificateTypeDef = TypedDict(
    "ClientGetServerCertificateResponseServerCertificateTypeDef",
    {
        "ServerCertificateMetadata": ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef,
        "CertificateBody": str,
        "CertificateChain": str,
    },
    total=False,
)

ClientGetServerCertificateResponseTypeDef = TypedDict(
    "ClientGetServerCertificateResponseTypeDef",
    {"ServerCertificate": ClientGetServerCertificateResponseServerCertificateTypeDef},
    total=False,
)

ClientGetServiceLastAccessedDetailsResponseErrorTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsResponseErrorTypeDef",
    {"Message": str, "Code": str},
    total=False,
)

ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef",
    {
        "ServiceName": str,
        "LastAuthenticated": datetime,
        "ServiceNamespace": str,
        "LastAuthenticatedEntity": str,
        "TotalAuthenticatedEntities": int,
    },
    total=False,
)

ClientGetServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsResponseTypeDef",
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

ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef",
    {"Arn": str, "Name": str, "Type": Literal["USER", "ROLE", "GROUP"], "Id": str, "Path": str},
    total=False,
)

ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef",
    {
        "EntityInfo": ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef,
        "LastAuthenticated": datetime,
    },
    total=False,
)

ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef",
    {"Message": str, "Code": str},
    total=False,
)

ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
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

ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef = TypedDict(
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef",
    {"Region": str, "Resources": List[str]},
    total=False,
)

ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef = TypedDict(
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef",
    {
        "Reason": str,
        "RoleUsageList": List[
            ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef
        ],
    },
    total=False,
)

ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef = TypedDict(
    "ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef",
    {
        "Status": Literal["SUCCEEDED", "IN_PROGRESS", "FAILED", "NOT_STARTED"],
        "Reason": ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef,
    },
    total=False,
)

ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef = TypedDict(
    "ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef",
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

ClientGetSshPublicKeyResponseTypeDef = TypedDict(
    "ClientGetSshPublicKeyResponseTypeDef",
    {"SSHPublicKey": ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef},
    total=False,
)

ClientGetUserPolicyResponseTypeDef = TypedDict(
    "ClientGetUserPolicyResponseTypeDef",
    {"UserName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetUserResponseUserPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetUserResponseUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetUserResponseUserTagsTypeDef = TypedDict(
    "ClientGetUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetUserResponseUserTypeDef = TypedDict(
    "ClientGetUserResponseUserTypeDef",
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

ClientGetUserResponseTypeDef = TypedDict(
    "ClientGetUserResponseTypeDef", {"User": ClientGetUserResponseUserTypeDef}, total=False
)

ClientListAccessKeysResponseAccessKeyMetadataTypeDef = TypedDict(
    "ClientListAccessKeysResponseAccessKeyMetadataTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "CreateDate": datetime,
    },
    total=False,
)

ClientListAccessKeysResponseTypeDef = TypedDict(
    "ClientListAccessKeysResponseTypeDef",
    {
        "AccessKeyMetadata": List[ClientListAccessKeysResponseAccessKeyMetadataTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListAccountAliasesResponseTypeDef = TypedDict(
    "ClientListAccountAliasesResponseTypeDef",
    {"AccountAliases": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientListAttachedGroupPoliciesResponseTypeDef = TypedDict(
    "ClientListAttachedGroupPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientListAttachedRolePoliciesResponseTypeDef = TypedDict(
    "ClientListAttachedRolePoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientListAttachedUserPoliciesResponseTypeDef = TypedDict(
    "ClientListAttachedUserPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef = TypedDict(
    "ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef",
    {"GroupName": str, "GroupId": str},
    total=False,
)

ClientListEntitiesForPolicyResponsePolicyRolesTypeDef = TypedDict(
    "ClientListEntitiesForPolicyResponsePolicyRolesTypeDef",
    {"RoleName": str, "RoleId": str},
    total=False,
)

ClientListEntitiesForPolicyResponsePolicyUsersTypeDef = TypedDict(
    "ClientListEntitiesForPolicyResponsePolicyUsersTypeDef",
    {"UserName": str, "UserId": str},
    total=False,
)

ClientListEntitiesForPolicyResponseTypeDef = TypedDict(
    "ClientListEntitiesForPolicyResponseTypeDef",
    {
        "PolicyGroups": List[ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef],
        "PolicyUsers": List[ClientListEntitiesForPolicyResponsePolicyUsersTypeDef],
        "PolicyRoles": List[ClientListEntitiesForPolicyResponsePolicyRolesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListGroupPoliciesResponseTypeDef = TypedDict(
    "ClientListGroupPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListGroupsForUserResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsForUserResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ClientListGroupsForUserResponseTypeDef = TypedDict(
    "ClientListGroupsForUserResponseTypeDef",
    {
        "Groups": List[ClientListGroupsForUserResponseGroupsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ClientListGroupsResponseTypeDef = TypedDict(
    "ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef",
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

ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef",
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

ClientListInstanceProfilesForRoleResponseTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseTypeDef",
    {
        "InstanceProfiles": List[ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef",
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

ClientListInstanceProfilesResponseInstanceProfilesTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesTypeDef",
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

ClientListInstanceProfilesResponseTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseTypeDef",
    {
        "InstanceProfiles": List[ClientListInstanceProfilesResponseInstanceProfilesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListMfaDevicesResponseMFADevicesTypeDef = TypedDict(
    "ClientListMfaDevicesResponseMFADevicesTypeDef",
    {"UserName": str, "SerialNumber": str, "EnableDate": datetime},
    total=False,
)

ClientListMfaDevicesResponseTypeDef = TypedDict(
    "ClientListMfaDevicesResponseTypeDef",
    {
        "MFADevices": List[ClientListMfaDevicesResponseMFADevicesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef = TypedDict(
    "ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef",
    {"Arn": str},
    total=False,
)

ClientListOpenIdConnectProvidersResponseTypeDef = TypedDict(
    "ClientListOpenIdConnectProvidersResponseTypeDef",
    {
        "OpenIDConnectProviderList": List[
            ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef
        ]
    },
    total=False,
)

ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef = TypedDict(
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": Literal["INLINE", "MANAGED"],
        "PolicyArn": str,
        "EntityType": Literal["USER", "ROLE", "GROUP"],
        "EntityName": str,
    },
    total=False,
)

ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef = TypedDict(
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef",
    {
        "ServiceNamespace": str,
        "Policies": List[
            ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef
        ],
    },
    total=False,
)

ClientListPoliciesGrantingServiceAccessResponseTypeDef = TypedDict(
    "ClientListPoliciesGrantingServiceAccessResponseTypeDef",
    {
        "PoliciesGrantingServiceAccess": List[
            ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListPoliciesResponsePoliciesTypeDef = TypedDict(
    "ClientListPoliciesResponsePoliciesTypeDef",
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

ClientListPoliciesResponseTypeDef = TypedDict(
    "ClientListPoliciesResponseTypeDef",
    {
        "Policies": List[ClientListPoliciesResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListPolicyVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListPolicyVersionsResponseVersionsTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

ClientListPolicyVersionsResponseTypeDef = TypedDict(
    "ClientListPolicyVersionsResponseTypeDef",
    {
        "Versions": List[ClientListPolicyVersionsResponseVersionsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListRolePoliciesResponseTypeDef = TypedDict(
    "ClientListRolePoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListRoleTagsResponseTagsTypeDef = TypedDict(
    "ClientListRoleTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListRoleTagsResponseTypeDef = TypedDict(
    "ClientListRoleTagsResponseTypeDef",
    {"Tags": List[ClientListRoleTagsResponseTagsTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListRolesResponseRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientListRolesResponseRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListRolesResponseRolesRoleLastUsedTypeDef = TypedDict(
    "ClientListRolesResponseRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientListRolesResponseRolesTagsTypeDef = TypedDict(
    "ClientListRolesResponseRolesTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListRolesResponseRolesTypeDef = TypedDict(
    "ClientListRolesResponseRolesTypeDef",
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

ClientListRolesResponseTypeDef = TypedDict(
    "ClientListRolesResponseTypeDef",
    {"Roles": List[ClientListRolesResponseRolesTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListSamlProvidersResponseSAMLProviderListTypeDef = TypedDict(
    "ClientListSamlProvidersResponseSAMLProviderListTypeDef",
    {"Arn": str, "ValidUntil": datetime, "CreateDate": datetime},
    total=False,
)

ClientListSamlProvidersResponseTypeDef = TypedDict(
    "ClientListSamlProvidersResponseTypeDef",
    {"SAMLProviderList": List[ClientListSamlProvidersResponseSAMLProviderListTypeDef]},
    total=False,
)

ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef = TypedDict(
    "ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef",
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

ClientListServerCertificatesResponseTypeDef = TypedDict(
    "ClientListServerCertificatesResponseTypeDef",
    {
        "ServerCertificateMetadataList": List[
            ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef = TypedDict(
    "ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef",
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

ClientListServiceSpecificCredentialsResponseTypeDef = TypedDict(
    "ClientListServiceSpecificCredentialsResponseTypeDef",
    {
        "ServiceSpecificCredentials": List[
            ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef
        ]
    },
    total=False,
)

ClientListSigningCertificatesResponseCertificatesTypeDef = TypedDict(
    "ClientListSigningCertificatesResponseCertificatesTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ClientListSigningCertificatesResponseTypeDef = TypedDict(
    "ClientListSigningCertificatesResponseTypeDef",
    {
        "Certificates": List[ClientListSigningCertificatesResponseCertificatesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListSshPublicKeysResponseSSHPublicKeysTypeDef = TypedDict(
    "ClientListSshPublicKeysResponseSSHPublicKeysTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ClientListSshPublicKeysResponseTypeDef = TypedDict(
    "ClientListSshPublicKeysResponseTypeDef",
    {
        "SSHPublicKeys": List[ClientListSshPublicKeysResponseSSHPublicKeysTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListUserPoliciesResponseTypeDef = TypedDict(
    "ClientListUserPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListUserTagsResponseTagsTypeDef = TypedDict(
    "ClientListUserTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListUserTagsResponseTypeDef = TypedDict(
    "ClientListUserTagsResponseTypeDef",
    {"Tags": List[ClientListUserTagsResponseTagsTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListUsersResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "ClientListUsersResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListUsersResponseUsersTagsTypeDef = TypedDict(
    "ClientListUsersResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListUsersResponseUsersTypeDef = TypedDict(
    "ClientListUsersResponseUsersTypeDef",
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

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef",
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

ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)

ClientListVirtualMfaDevicesResponseTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseTypeDef",
    {
        "VirtualMFADevices": List[ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef = TypedDict(
    "ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
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

ClientResetServiceSpecificCredentialResponseTypeDef = TypedDict(
    "ClientResetServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
    },
    total=False,
)

ClientSimulateCustomPolicyContextEntriesTypeDef = TypedDict(
    "ClientSimulateCustomPolicyContextEntriesTypeDef",
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

ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
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

ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
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

ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
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

ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef",
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

ClientSimulateCustomPolicyResponseTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseTypeDef",
    {
        "EvaluationResults": List[ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientSimulatePrincipalPolicyContextEntriesTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyContextEntriesTypeDef",
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

ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
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

ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
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

ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
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

ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef",
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

ClientSimulatePrincipalPolicyResponseTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseTypeDef",
    {
        "EvaluationResults": List[ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

_RequiredClientTagRoleTagsTypeDef = TypedDict("_RequiredClientTagRoleTagsTypeDef", {"Key": str})
_OptionalClientTagRoleTagsTypeDef = TypedDict(
    "_OptionalClientTagRoleTagsTypeDef", {"Value": str}, total=False
)


class ClientTagRoleTagsTypeDef(
    _RequiredClientTagRoleTagsTypeDef, _OptionalClientTagRoleTagsTypeDef
):
    pass


_RequiredClientTagUserTagsTypeDef = TypedDict("_RequiredClientTagUserTagsTypeDef", {"Key": str})
_OptionalClientTagUserTagsTypeDef = TypedDict(
    "_OptionalClientTagUserTagsTypeDef", {"Value": str}, total=False
)


class ClientTagUserTagsTypeDef(
    _RequiredClientTagUserTagsTypeDef, _OptionalClientTagUserTagsTypeDef
):
    pass


ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientUpdateRoleDescriptionResponseRoleTagsTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateRoleDescriptionResponseRoleTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseRoleTypeDef",
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

ClientUpdateRoleDescriptionResponseTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseTypeDef",
    {"Role": ClientUpdateRoleDescriptionResponseRoleTypeDef},
    total=False,
)

ClientUpdateSamlProviderResponseTypeDef = TypedDict(
    "ClientUpdateSamlProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)

ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef = TypedDict(
    "ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef",
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

ClientUploadServerCertificateResponseTypeDef = TypedDict(
    "ClientUploadServerCertificateResponseTypeDef",
    {
        "ServerCertificateMetadata": ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef
    },
    total=False,
)

ClientUploadSigningCertificateResponseCertificateTypeDef = TypedDict(
    "ClientUploadSigningCertificateResponseCertificateTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ClientUploadSigningCertificateResponseTypeDef = TypedDict(
    "ClientUploadSigningCertificateResponseTypeDef",
    {"Certificate": ClientUploadSigningCertificateResponseCertificateTypeDef},
    total=False,
)

ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef = TypedDict(
    "ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef",
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

ClientUploadSshPublicKeyResponseTypeDef = TypedDict(
    "ClientUploadSshPublicKeyResponseTypeDef",
    {"SSHPublicKey": ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef},
    total=False,
)

GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef",
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

GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef",
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

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef",
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

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef",
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

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef",
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

GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)

GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef",
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

GetAccountAuthorizationDetailsPaginateResponseTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsPaginateResponseTypeDef",
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

GetGroupPaginatePaginationConfigTypeDef = TypedDict(
    "GetGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetGroupPaginateResponseGroupTypeDef = TypedDict(
    "GetGroupPaginateResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

GetGroupPaginateResponseUsersTagsTypeDef = TypedDict(
    "GetGroupPaginateResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)

GetGroupPaginateResponseUsersTypeDef = TypedDict(
    "GetGroupPaginateResponseUsersTypeDef",
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

GetGroupPaginateResponseTypeDef = TypedDict(
    "GetGroupPaginateResponseTypeDef",
    {
        "Group": GetGroupPaginateResponseGroupTypeDef,
        "Users": List[GetGroupPaginateResponseUsersTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

InstanceProfileExistsWaitWaiterConfigTypeDef = TypedDict(
    "InstanceProfileExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

ListAccessKeysPaginatePaginationConfigTypeDef = TypedDict(
    "ListAccessKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef = TypedDict(
    "ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "CreateDate": datetime,
    },
    total=False,
)

ListAccessKeysPaginateResponseTypeDef = TypedDict(
    "ListAccessKeysPaginateResponseTypeDef",
    {
        "AccessKeyMetadata": List[ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListAccountAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAccountAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAccountAliasesPaginateResponseTypeDef = TypedDict(
    "ListAccountAliasesPaginateResponseTypeDef",
    {"AccountAliases": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)

ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef = TypedDict(
    "ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ListAttachedGroupPoliciesPaginateResponseTypeDef = TypedDict(
    "ListAttachedGroupPoliciesPaginateResponseTypeDef",
    {
        "AttachedPolicies": List[ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListAttachedRolePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAttachedRolePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef = TypedDict(
    "ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ListAttachedRolePoliciesPaginateResponseTypeDef = TypedDict(
    "ListAttachedRolePoliciesPaginateResponseTypeDef",
    {
        "AttachedPolicies": List[ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListAttachedUserPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAttachedUserPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef = TypedDict(
    "ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ListAttachedUserPoliciesPaginateResponseTypeDef = TypedDict(
    "ListAttachedUserPoliciesPaginateResponseTypeDef",
    {
        "AttachedPolicies": List[ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListEntitiesForPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "ListEntitiesForPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef = TypedDict(
    "ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef",
    {"GroupName": str, "GroupId": str},
    total=False,
)

ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef = TypedDict(
    "ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef",
    {"RoleName": str, "RoleId": str},
    total=False,
)

ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef = TypedDict(
    "ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef",
    {"UserName": str, "UserId": str},
    total=False,
)

ListEntitiesForPolicyPaginateResponseTypeDef = TypedDict(
    "ListEntitiesForPolicyPaginateResponseTypeDef",
    {
        "PolicyGroups": List[ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef],
        "PolicyUsers": List[ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef],
        "PolicyRoles": List[ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListGroupPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListGroupPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListGroupPoliciesPaginateResponseTypeDef = TypedDict(
    "ListGroupPoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)

ListGroupsForUserPaginatePaginationConfigTypeDef = TypedDict(
    "ListGroupsForUserPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListGroupsForUserPaginateResponseGroupsTypeDef = TypedDict(
    "ListGroupsForUserPaginateResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ListGroupsForUserPaginateResponseTypeDef = TypedDict(
    "ListGroupsForUserPaginateResponseTypeDef",
    {
        "Groups": List[ListGroupsForUserPaginateResponseGroupsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "ListGroupsPaginateResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ListGroupsPaginateResponseTypeDef = TypedDict(
    "ListGroupsPaginateResponseTypeDef",
    {
        "Groups": List[ListGroupsPaginateResponseGroupsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListInstanceProfilesForRolePaginatePaginationConfigTypeDef = TypedDict(
    "ListInstanceProfilesForRolePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef = TypedDict(
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef",
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

ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef = TypedDict(
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef",
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

ListInstanceProfilesForRolePaginateResponseTypeDef = TypedDict(
    "ListInstanceProfilesForRolePaginateResponseTypeDef",
    {
        "InstanceProfiles": List[
            ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListInstanceProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "ListInstanceProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef = TypedDict(
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef",
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

ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef = TypedDict(
    "ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef",
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

ListInstanceProfilesPaginateResponseTypeDef = TypedDict(
    "ListInstanceProfilesPaginateResponseTypeDef",
    {
        "InstanceProfiles": List[ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListMFADevicesPaginatePaginationConfigTypeDef = TypedDict(
    "ListMFADevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListMFADevicesPaginateResponseMFADevicesTypeDef = TypedDict(
    "ListMFADevicesPaginateResponseMFADevicesTypeDef",
    {"UserName": str, "SerialNumber": str, "EnableDate": datetime},
    total=False,
)

ListMFADevicesPaginateResponseTypeDef = TypedDict(
    "ListMFADevicesPaginateResponseTypeDef",
    {
        "MFADevices": List[ListMFADevicesPaginateResponseMFADevicesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPoliciesPaginateResponsePoliciesTypeDef = TypedDict(
    "ListPoliciesPaginateResponsePoliciesTypeDef",
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

ListPoliciesPaginateResponseTypeDef = TypedDict(
    "ListPoliciesPaginateResponseTypeDef",
    {
        "Policies": List[ListPoliciesPaginateResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListPolicyVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPolicyVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPolicyVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListPolicyVersionsPaginateResponseVersionsTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

ListPolicyVersionsPaginateResponseTypeDef = TypedDict(
    "ListPolicyVersionsPaginateResponseTypeDef",
    {
        "Versions": List[ListPolicyVersionsPaginateResponseVersionsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListRolePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListRolePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRolePoliciesPaginateResponseTypeDef = TypedDict(
    "ListRolePoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)

ListRolesPaginatePaginationConfigTypeDef = TypedDict(
    "ListRolesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef = TypedDict(
    "ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ListRolesPaginateResponseRolesRoleLastUsedTypeDef = TypedDict(
    "ListRolesPaginateResponseRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ListRolesPaginateResponseRolesTagsTypeDef = TypedDict(
    "ListRolesPaginateResponseRolesTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ListRolesPaginateResponseRolesTypeDef = TypedDict(
    "ListRolesPaginateResponseRolesTypeDef",
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

ListRolesPaginateResponseTypeDef = TypedDict(
    "ListRolesPaginateResponseTypeDef",
    {"Roles": List[ListRolesPaginateResponseRolesTypeDef], "IsTruncated": bool, "NextToken": str},
    total=False,
)

ListSSHPublicKeysPaginatePaginationConfigTypeDef = TypedDict(
    "ListSSHPublicKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef = TypedDict(
    "ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ListSSHPublicKeysPaginateResponseTypeDef = TypedDict(
    "ListSSHPublicKeysPaginateResponseTypeDef",
    {
        "SSHPublicKeys": List[ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListServerCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "ListServerCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef = TypedDict(
    "ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef",
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

ListServerCertificatesPaginateResponseTypeDef = TypedDict(
    "ListServerCertificatesPaginateResponseTypeDef",
    {
        "ServerCertificateMetadataList": List[
            ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListSigningCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "ListSigningCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSigningCertificatesPaginateResponseCertificatesTypeDef = TypedDict(
    "ListSigningCertificatesPaginateResponseCertificatesTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ListSigningCertificatesPaginateResponseTypeDef = TypedDict(
    "ListSigningCertificatesPaginateResponseTypeDef",
    {
        "Certificates": List[ListSigningCertificatesPaginateResponseCertificatesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

ListUserPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListUserPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListUserPoliciesPaginateResponseTypeDef = TypedDict(
    "ListUserPoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)

ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ListUsersPaginateResponseUsersTagsTypeDef = TypedDict(
    "ListUsersPaginateResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "ListUsersPaginateResponseUsersTypeDef",
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

ListUsersPaginateResponseTypeDef = TypedDict(
    "ListUsersPaginateResponseTypeDef",
    {"Users": List[ListUsersPaginateResponseUsersTypeDef], "IsTruncated": bool, "NextToken": str},
    total=False,
)

ListVirtualMFADevicesPaginatePaginationConfigTypeDef = TypedDict(
    "ListVirtualMFADevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef = TypedDict(
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef = TypedDict(
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef = TypedDict(
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef",
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

ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef = TypedDict(
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)

ListVirtualMFADevicesPaginateResponseTypeDef = TypedDict(
    "ListVirtualMFADevicesPaginateResponseTypeDef",
    {
        "VirtualMFADevices": List[ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

PolicyExistsWaitWaiterConfigTypeDef = TypedDict(
    "PolicyExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

RoleExistsWaitWaiterConfigTypeDef = TypedDict(
    "RoleExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

SamlProviderUpdateResponseTypeDef = TypedDict(
    "SamlProviderUpdateResponseTypeDef", {"SAMLProviderArn": str}, total=False
)

ServiceResourceCreateRoleTagsTypeDef = TypedDict(
    "ServiceResourceCreateRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ServiceResourceCreateUserTagsTypeDef = TypedDict(
    "ServiceResourceCreateUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)

SimulateCustomPolicyPaginateContextEntriesTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateContextEntriesTypeDef",
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

SimulateCustomPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "SimulateCustomPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef",
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

SimulateCustomPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)

SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
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

SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef",
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

SimulateCustomPolicyPaginateResponseEvaluationResultsTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseEvaluationResultsTypeDef",
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

SimulateCustomPolicyPaginateResponseTypeDef = TypedDict(
    "SimulateCustomPolicyPaginateResponseTypeDef",
    {
        "EvaluationResults": List[SimulateCustomPolicyPaginateResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

SimulatePrincipalPolicyPaginateContextEntriesTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateContextEntriesTypeDef",
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

SimulatePrincipalPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsMatchedStatementsTypeDef",
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

SimulatePrincipalPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)

SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
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

SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsResourceSpecificResultsTypeDef",
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

SimulatePrincipalPolicyPaginateResponseEvaluationResultsTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseEvaluationResultsTypeDef",
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

SimulatePrincipalPolicyPaginateResponseTypeDef = TypedDict(
    "SimulatePrincipalPolicyPaginateResponseTypeDef",
    {
        "EvaluationResults": List[SimulatePrincipalPolicyPaginateResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)

UserCreateTagsTypeDef = TypedDict("UserCreateTagsTypeDef", {"Key": str, "Value": str}, total=False)

UserExistsWaitWaiterConfigTypeDef = TypedDict(
    "UserExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
