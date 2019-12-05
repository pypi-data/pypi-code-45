"Main interface for fms service type defs"
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


ClientGetAdminAccountResponseTypeDef = TypedDict(
    "ClientGetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": Literal["READY", "CREATING", "PENDING_DELETION", "DELETING", "DELETED"],
    },
    total=False,
)

ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef = TypedDict(
    "ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef",
    {
        "ResourceId": str,
        "ViolationReason": Literal[
            "WEB_ACL_MISSING_RULE_GROUP",
            "RESOURCE_MISSING_WEB_ACL",
            "RESOURCE_INCORRECT_WEB_ACL",
            "RESOURCE_MISSING_SHIELD_PROTECTION",
            "RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION",
            "RESOURCE_MISSING_SECURITY_GROUP",
            "RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP",
            "SECURITY_GROUP_UNUSED",
            "SECURITY_GROUP_REDUNDANT",
        ],
        "ResourceType": str,
    },
    total=False,
)

ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef = TypedDict(
    "ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "MemberAccount": str,
        "Violators": List[ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef],
        "EvaluationLimitExceeded": bool,
        "ExpiredAt": datetime,
        "IssueInfoMap": Dict[str, str],
    },
    total=False,
)

ClientGetComplianceDetailResponseTypeDef = TypedDict(
    "ClientGetComplianceDetailResponseTypeDef",
    {"PolicyComplianceDetail": ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef},
    total=False,
)

ClientGetNotificationChannelResponseTypeDef = TypedDict(
    "ClientGetNotificationChannelResponseTypeDef",
    {"SnsTopicArn": str, "SnsRoleName": str},
    total=False,
)

ClientGetPolicyResponsePolicyResourceTagsTypeDef = TypedDict(
    "ClientGetPolicyResponsePolicyResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef = TypedDict(
    "ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef",
    {
        "Type": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "ManagedServiceData": str,
    },
    total=False,
)

ClientGetPolicyResponsePolicyTypeDef = TypedDict(
    "ClientGetPolicyResponsePolicyTypeDef",
    {
        "PolicyId": str,
        "PolicyName": str,
        "PolicyUpdateToken": str,
        "SecurityServicePolicyData": ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef,
        "ResourceType": str,
        "ResourceTypeList": List[str],
        "ResourceTags": List[ClientGetPolicyResponsePolicyResourceTagsTypeDef],
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "IncludeMap": Dict[str, List[str]],
        "ExcludeMap": Dict[str, List[str]],
    },
    total=False,
)

ClientGetPolicyResponseTypeDef = TypedDict(
    "ClientGetPolicyResponseTypeDef",
    {"Policy": ClientGetPolicyResponsePolicyTypeDef, "PolicyArn": str},
    total=False,
)

ClientGetProtectionStatusResponseTypeDef = TypedDict(
    "ClientGetProtectionStatusResponseTypeDef",
    {
        "AdminAccountId": str,
        "ServiceType": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "Data": str,
        "NextToken": str,
    },
    total=False,
)

ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef = TypedDict(
    "ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    {
        "ComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)

ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef = TypedDict(
    "ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "PolicyName": str,
        "MemberAccount": str,
        "EvaluationResults": List[
            ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef
        ],
        "LastUpdated": datetime,
        "IssueInfoMap": Dict[str, str],
    },
    total=False,
)

ClientListComplianceStatusResponseTypeDef = TypedDict(
    "ClientListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[
            ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListMemberAccountsResponseTypeDef = TypedDict(
    "ClientListMemberAccountsResponseTypeDef",
    {"MemberAccounts": List[str], "NextToken": str},
    total=False,
)

ClientListPoliciesResponsePolicyListTypeDef = TypedDict(
    "ClientListPoliciesResponsePolicyListTypeDef",
    {
        "PolicyArn": str,
        "PolicyId": str,
        "PolicyName": str,
        "ResourceType": str,
        "SecurityServiceType": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "RemediationEnabled": bool,
    },
    total=False,
)

ClientListPoliciesResponseTypeDef = TypedDict(
    "ClientListPoliciesResponseTypeDef",
    {"PolicyList": List[ClientListPoliciesResponsePolicyListTypeDef], "NextToken": str},
    total=False,
)

ClientPutPolicyPolicyResourceTagsTypeDef = TypedDict(
    "ClientPutPolicyPolicyResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientPutPolicyPolicySecurityServicePolicyDataTypeDef = TypedDict(
    "ClientPutPolicyPolicySecurityServicePolicyDataTypeDef",
    {
        "Type": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "ManagedServiceData": str,
    },
    total=False,
)

ClientPutPolicyPolicyTypeDef = TypedDict(
    "ClientPutPolicyPolicyTypeDef",
    {
        "PolicyId": str,
        "PolicyName": str,
        "PolicyUpdateToken": str,
        "SecurityServicePolicyData": ClientPutPolicyPolicySecurityServicePolicyDataTypeDef,
        "ResourceType": str,
        "ResourceTypeList": List[str],
        "ResourceTags": List[ClientPutPolicyPolicyResourceTagsTypeDef],
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "IncludeMap": Dict[str, List[str]],
        "ExcludeMap": Dict[str, List[str]],
    },
    total=False,
)

ClientPutPolicyResponsePolicyResourceTagsTypeDef = TypedDict(
    "ClientPutPolicyResponsePolicyResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef = TypedDict(
    "ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef",
    {
        "Type": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "ManagedServiceData": str,
    },
    total=False,
)

ClientPutPolicyResponsePolicyTypeDef = TypedDict(
    "ClientPutPolicyResponsePolicyTypeDef",
    {
        "PolicyId": str,
        "PolicyName": str,
        "PolicyUpdateToken": str,
        "SecurityServicePolicyData": ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef,
        "ResourceType": str,
        "ResourceTypeList": List[str],
        "ResourceTags": List[ClientPutPolicyResponsePolicyResourceTagsTypeDef],
        "ExcludeResourceTags": bool,
        "RemediationEnabled": bool,
        "IncludeMap": Dict[str, List[str]],
        "ExcludeMap": Dict[str, List[str]],
    },
    total=False,
)

ClientPutPolicyResponseTypeDef = TypedDict(
    "ClientPutPolicyResponseTypeDef",
    {"Policy": ClientPutPolicyResponsePolicyTypeDef, "PolicyArn": str},
    total=False,
)

ListComplianceStatusPaginatePaginationConfigTypeDef = TypedDict(
    "ListComplianceStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef = TypedDict(
    "ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    {
        "ComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)

ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef = TypedDict(
    "ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef",
    {
        "PolicyOwner": str,
        "PolicyId": str,
        "PolicyName": str,
        "MemberAccount": str,
        "EvaluationResults": List[
            ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef
        ],
        "LastUpdated": datetime,
        "IssueInfoMap": Dict[str, str],
    },
    total=False,
)

ListComplianceStatusPaginateResponseTypeDef = TypedDict(
    "ListComplianceStatusPaginateResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[
            ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef
        ]
    },
    total=False,
)

ListMemberAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "ListMemberAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListMemberAccountsPaginateResponseTypeDef = TypedDict(
    "ListMemberAccountsPaginateResponseTypeDef", {"MemberAccounts": List[str]}, total=False
)

ListPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "ListPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPoliciesPaginateResponsePolicyListTypeDef = TypedDict(
    "ListPoliciesPaginateResponsePolicyListTypeDef",
    {
        "PolicyArn": str,
        "PolicyId": str,
        "PolicyName": str,
        "ResourceType": str,
        "SecurityServiceType": Literal[
            "WAF",
            "SHIELD_ADVANCED",
            "SECURITY_GROUPS_COMMON",
            "SECURITY_GROUPS_CONTENT_AUDIT",
            "SECURITY_GROUPS_USAGE_AUDIT",
        ],
        "RemediationEnabled": bool,
    },
    total=False,
)

ListPoliciesPaginateResponseTypeDef = TypedDict(
    "ListPoliciesPaginateResponseTypeDef",
    {"PolicyList": List[ListPoliciesPaginateResponsePolicyListTypeDef]},
    total=False,
)
