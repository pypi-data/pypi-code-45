"Main interface for fms service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientGetAdminAccountResponseTypeDef",
    "ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef",
    "ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef",
    "ClientGetComplianceDetailResponseTypeDef",
    "ClientGetNotificationChannelResponseTypeDef",
    "ClientGetPolicyResponsePolicyResourceTagsTypeDef",
    "ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef",
    "ClientGetPolicyResponsePolicyTypeDef",
    "ClientGetPolicyResponseTypeDef",
    "ClientGetProtectionStatusResponseTypeDef",
    "ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    "ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef",
    "ClientListComplianceStatusResponseTypeDef",
    "ClientListMemberAccountsResponseTypeDef",
    "ClientListPoliciesResponsePolicyListTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientPutPolicyPolicyResourceTagsTypeDef",
    "ClientPutPolicyPolicySecurityServicePolicyDataTypeDef",
    "ClientPutPolicyPolicyTypeDef",
    "ClientPutPolicyResponsePolicyResourceTagsTypeDef",
    "ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef",
    "ClientPutPolicyResponsePolicyTypeDef",
    "ClientPutPolicyResponseTypeDef",
    "ListComplianceStatusPaginatePaginationConfigTypeDef",
    "ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    "ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef",
    "ListComplianceStatusPaginateResponseTypeDef",
    "ListMemberAccountsPaginatePaginationConfigTypeDef",
    "ListMemberAccountsPaginateResponseTypeDef",
    "ListPoliciesPaginatePaginationConfigTypeDef",
    "ListPoliciesPaginateResponsePolicyListTypeDef",
    "ListPoliciesPaginateResponseTypeDef",
)


_ClientGetAdminAccountResponseTypeDef = TypedDict(
    "_ClientGetAdminAccountResponseTypeDef",
    {
        "AdminAccount": str,
        "RoleStatus": Literal["READY", "CREATING", "PENDING_DELETION", "DELETING", "DELETED"],
    },
    total=False,
)


class ClientGetAdminAccountResponseTypeDef(_ClientGetAdminAccountResponseTypeDef):
    """
    - *(dict) --*

      - **AdminAccount** *(string) --*

        The AWS account that is set as the AWS Firewall Manager administrator.
    """


_ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef = TypedDict(
    "_ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef",
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


class ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef(
    _ClientGetComplianceDetailResponsePolicyComplianceDetailViolatorsTypeDef
):
    pass


_ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef = TypedDict(
    "_ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef",
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


class ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef(
    _ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef
):
    """
    - **PolicyComplianceDetail** *(dict) --*

      Information about the resources and the policy that you specified in the
      ``GetComplianceDetail`` request.
      - **PolicyOwner** *(string) --*

        The AWS account that created the AWS Firewall Manager policy.
    """


_ClientGetComplianceDetailResponseTypeDef = TypedDict(
    "_ClientGetComplianceDetailResponseTypeDef",
    {"PolicyComplianceDetail": ClientGetComplianceDetailResponsePolicyComplianceDetailTypeDef},
    total=False,
)


class ClientGetComplianceDetailResponseTypeDef(_ClientGetComplianceDetailResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyComplianceDetail** *(dict) --*

        Information about the resources and the policy that you specified in the
        ``GetComplianceDetail`` request.
        - **PolicyOwner** *(string) --*

          The AWS account that created the AWS Firewall Manager policy.
    """


_ClientGetNotificationChannelResponseTypeDef = TypedDict(
    "_ClientGetNotificationChannelResponseTypeDef",
    {"SnsTopicArn": str, "SnsRoleName": str},
    total=False,
)


class ClientGetNotificationChannelResponseTypeDef(_ClientGetNotificationChannelResponseTypeDef):
    """
    - *(dict) --*

      - **SnsTopicArn** *(string) --*

        The SNS topic that records AWS Firewall Manager activity.
    """


_ClientGetPolicyResponsePolicyResourceTagsTypeDef = TypedDict(
    "_ClientGetPolicyResponsePolicyResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetPolicyResponsePolicyResourceTagsTypeDef(
    _ClientGetPolicyResponsePolicyResourceTagsTypeDef
):
    pass


_ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef = TypedDict(
    "_ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef",
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


class ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef(
    _ClientGetPolicyResponsePolicySecurityServicePolicyDataTypeDef
):
    pass


_ClientGetPolicyResponsePolicyTypeDef = TypedDict(
    "_ClientGetPolicyResponsePolicyTypeDef",
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


class ClientGetPolicyResponsePolicyTypeDef(_ClientGetPolicyResponsePolicyTypeDef):
    """
    - **Policy** *(dict) --*

      Information about the specified AWS Firewall Manager policy.
      - **PolicyId** *(string) --*

        The ID of the AWS Firewall Manager policy.
    """


_ClientGetPolicyResponseTypeDef = TypedDict(
    "_ClientGetPolicyResponseTypeDef",
    {"Policy": ClientGetPolicyResponsePolicyTypeDef, "PolicyArn": str},
    total=False,
)


class ClientGetPolicyResponseTypeDef(_ClientGetPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(dict) --*

        Information about the specified AWS Firewall Manager policy.
        - **PolicyId** *(string) --*

          The ID of the AWS Firewall Manager policy.
    """


_ClientGetProtectionStatusResponseTypeDef = TypedDict(
    "_ClientGetProtectionStatusResponseTypeDef",
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


class ClientGetProtectionStatusResponseTypeDef(_ClientGetProtectionStatusResponseTypeDef):
    """
    - *(dict) --*

      - **AdminAccountId** *(string) --*

        The ID of the AWS Firewall administrator account for this policy.
    """


_ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef = TypedDict(
    "_ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    {
        "ComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)


class ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef(
    _ClientListComplianceStatusResponsePolicyComplianceStatusListEvaluationResultsTypeDef
):
    pass


_ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef = TypedDict(
    "_ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef",
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


class ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef(
    _ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef
):
    """
    - *(dict) --*

      Indicates whether the account is compliant with the specified policy. An account is considered
      noncompliant if it includes resources that are not protected by the policy, for AWS WAF and
      Shield Advanced policies, or that are noncompliant with the policy, for security group
      policies.
      - **PolicyOwner** *(string) --*

        The AWS account that created the AWS Firewall Manager policy.
    """


_ClientListComplianceStatusResponseTypeDef = TypedDict(
    "_ClientListComplianceStatusResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[
            ClientListComplianceStatusResponsePolicyComplianceStatusListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListComplianceStatusResponseTypeDef(_ClientListComplianceStatusResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyComplianceStatusList** *(list) --*

        An array of ``PolicyComplianceStatus`` objects.
        - *(dict) --*

          Indicates whether the account is compliant with the specified policy. An account is
          considered noncompliant if it includes resources that are not protected by the policy, for
          AWS WAF and Shield Advanced policies, or that are noncompliant with the policy, for
          security group policies.
          - **PolicyOwner** *(string) --*

            The AWS account that created the AWS Firewall Manager policy.
    """


_ClientListMemberAccountsResponseTypeDef = TypedDict(
    "_ClientListMemberAccountsResponseTypeDef",
    {"MemberAccounts": List[str], "NextToken": str},
    total=False,
)


class ClientListMemberAccountsResponseTypeDef(_ClientListMemberAccountsResponseTypeDef):
    """
    - *(dict) --*

      - **MemberAccounts** *(list) --*

        An array of account IDs.
        - *(string) --*
    """


_ClientListPoliciesResponsePolicyListTypeDef = TypedDict(
    "_ClientListPoliciesResponsePolicyListTypeDef",
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


class ClientListPoliciesResponsePolicyListTypeDef(_ClientListPoliciesResponsePolicyListTypeDef):
    """
    - *(dict) --*

      Details of the AWS Firewall Manager policy.
      - **PolicyArn** *(string) --*

        The Amazon Resource Name (ARN) of the specified policy.
    """


_ClientListPoliciesResponseTypeDef = TypedDict(
    "_ClientListPoliciesResponseTypeDef",
    {"PolicyList": List[ClientListPoliciesResponsePolicyListTypeDef], "NextToken": str},
    total=False,
)


class ClientListPoliciesResponseTypeDef(_ClientListPoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyList** *(list) --*

        An array of ``PolicySummary`` objects.
        - *(dict) --*

          Details of the AWS Firewall Manager policy.
          - **PolicyArn** *(string) --*

            The Amazon Resource Name (ARN) of the specified policy.
    """


_ClientPutPolicyPolicyResourceTagsTypeDef = TypedDict(
    "_ClientPutPolicyPolicyResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutPolicyPolicyResourceTagsTypeDef(_ClientPutPolicyPolicyResourceTagsTypeDef):
    pass


_ClientPutPolicyPolicySecurityServicePolicyDataTypeDef = TypedDict(
    "_ClientPutPolicyPolicySecurityServicePolicyDataTypeDef",
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


class ClientPutPolicyPolicySecurityServicePolicyDataTypeDef(
    _ClientPutPolicyPolicySecurityServicePolicyDataTypeDef
):
    pass


_ClientPutPolicyPolicyTypeDef = TypedDict(
    "_ClientPutPolicyPolicyTypeDef",
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


class ClientPutPolicyPolicyTypeDef(_ClientPutPolicyPolicyTypeDef):
    """
    The details of the AWS Firewall Manager policy to be created.
    - **PolicyId** *(string) --*

      The ID of the AWS Firewall Manager policy.
    """


_ClientPutPolicyResponsePolicyResourceTagsTypeDef = TypedDict(
    "_ClientPutPolicyResponsePolicyResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientPutPolicyResponsePolicyResourceTagsTypeDef(
    _ClientPutPolicyResponsePolicyResourceTagsTypeDef
):
    pass


_ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef = TypedDict(
    "_ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef",
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


class ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef(
    _ClientPutPolicyResponsePolicySecurityServicePolicyDataTypeDef
):
    pass


_ClientPutPolicyResponsePolicyTypeDef = TypedDict(
    "_ClientPutPolicyResponsePolicyTypeDef",
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


class ClientPutPolicyResponsePolicyTypeDef(_ClientPutPolicyResponsePolicyTypeDef):
    """
    - **Policy** *(dict) --*

      The details of the AWS Firewall Manager policy that was created.
      - **PolicyId** *(string) --*

        The ID of the AWS Firewall Manager policy.
    """


_ClientPutPolicyResponseTypeDef = TypedDict(
    "_ClientPutPolicyResponseTypeDef",
    {"Policy": ClientPutPolicyResponsePolicyTypeDef, "PolicyArn": str},
    total=False,
)


class ClientPutPolicyResponseTypeDef(_ClientPutPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(dict) --*

        The details of the AWS Firewall Manager policy that was created.
        - **PolicyId** *(string) --*

          The ID of the AWS Firewall Manager policy.
    """


_ListComplianceStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_ListComplianceStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListComplianceStatusPaginatePaginationConfigTypeDef(
    _ListComplianceStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef = TypedDict(
    "_ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef",
    {
        "ComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ViolatorCount": int,
        "EvaluationLimitExceeded": bool,
    },
    total=False,
)


class ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef(
    _ListComplianceStatusPaginateResponsePolicyComplianceStatusListEvaluationResultsTypeDef
):
    pass


_ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef = TypedDict(
    "_ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef",
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


class ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef(
    _ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef
):
    """
    - *(dict) --*

      Indicates whether the account is compliant with the specified policy. An account is considered
      noncompliant if it includes resources that are not protected by the policy, for AWS WAF and
      Shield Advanced policies, or that are noncompliant with the policy, for security group
      policies.
      - **PolicyOwner** *(string) --*

        The AWS account that created the AWS Firewall Manager policy.
    """


_ListComplianceStatusPaginateResponseTypeDef = TypedDict(
    "_ListComplianceStatusPaginateResponseTypeDef",
    {
        "PolicyComplianceStatusList": List[
            ListComplianceStatusPaginateResponsePolicyComplianceStatusListTypeDef
        ]
    },
    total=False,
)


class ListComplianceStatusPaginateResponseTypeDef(_ListComplianceStatusPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyComplianceStatusList** *(list) --*

        An array of ``PolicyComplianceStatus`` objects.
        - *(dict) --*

          Indicates whether the account is compliant with the specified policy. An account is
          considered noncompliant if it includes resources that are not protected by the policy, for
          AWS WAF and Shield Advanced policies, or that are noncompliant with the policy, for
          security group policies.
          - **PolicyOwner** *(string) --*

            The AWS account that created the AWS Firewall Manager policy.
    """


_ListMemberAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMemberAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMemberAccountsPaginatePaginationConfigTypeDef(
    _ListMemberAccountsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMemberAccountsPaginateResponseTypeDef = TypedDict(
    "_ListMemberAccountsPaginateResponseTypeDef", {"MemberAccounts": List[str]}, total=False
)


class ListMemberAccountsPaginateResponseTypeDef(_ListMemberAccountsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **MemberAccounts** *(list) --*

        An array of account IDs.
        - *(string) --*
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


_ListPoliciesPaginateResponsePolicyListTypeDef = TypedDict(
    "_ListPoliciesPaginateResponsePolicyListTypeDef",
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


class ListPoliciesPaginateResponsePolicyListTypeDef(_ListPoliciesPaginateResponsePolicyListTypeDef):
    """
    - *(dict) --*

      Details of the AWS Firewall Manager policy.
      - **PolicyArn** *(string) --*

        The Amazon Resource Name (ARN) of the specified policy.
    """


_ListPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesPaginateResponseTypeDef",
    {"PolicyList": List[ListPoliciesPaginateResponsePolicyListTypeDef]},
    total=False,
)


class ListPoliciesPaginateResponseTypeDef(_ListPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyList** *(list) --*

        An array of ``PolicySummary`` objects.
        - *(dict) --*

          Details of the AWS Firewall Manager policy.
          - **PolicyArn** *(string) --*

            The Amazon Resource Name (ARN) of the specified policy.
    """
