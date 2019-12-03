"Main interface for organizations service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAcceptHandshakeResponseHandshakePartiesTypeDef",
    "ClientAcceptHandshakeResponseHandshakeResourcesTypeDef",
    "ClientAcceptHandshakeResponseHandshakeTypeDef",
    "ClientAcceptHandshakeResponseTypeDef",
    "ClientCancelHandshakeResponseHandshakePartiesTypeDef",
    "ClientCancelHandshakeResponseHandshakeResourcesTypeDef",
    "ClientCancelHandshakeResponseHandshakeTypeDef",
    "ClientCancelHandshakeResponseTypeDef",
    "ClientCreateAccountResponseCreateAccountStatusTypeDef",
    "ClientCreateAccountResponseTypeDef",
    "ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef",
    "ClientCreateGovCloudAccountResponseTypeDef",
    "ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    "ClientCreateOrganizationResponseOrganizationTypeDef",
    "ClientCreateOrganizationResponseTypeDef",
    "ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    "ClientCreateOrganizationalUnitResponseTypeDef",
    "ClientCreatePolicyResponsePolicyPolicySummaryTypeDef",
    "ClientCreatePolicyResponsePolicyTypeDef",
    "ClientCreatePolicyResponseTypeDef",
    "ClientDeclineHandshakeResponseHandshakePartiesTypeDef",
    "ClientDeclineHandshakeResponseHandshakeResourcesTypeDef",
    "ClientDeclineHandshakeResponseHandshakeTypeDef",
    "ClientDeclineHandshakeResponseTypeDef",
    "ClientDescribeAccountResponseAccountTypeDef",
    "ClientDescribeAccountResponseTypeDef",
    "ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef",
    "ClientDescribeCreateAccountStatusResponseTypeDef",
    "ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef",
    "ClientDescribeEffectivePolicyResponseTypeDef",
    "ClientDescribeHandshakeResponseHandshakePartiesTypeDef",
    "ClientDescribeHandshakeResponseHandshakeResourcesTypeDef",
    "ClientDescribeHandshakeResponseHandshakeTypeDef",
    "ClientDescribeHandshakeResponseTypeDef",
    "ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    "ClientDescribeOrganizationResponseOrganizationTypeDef",
    "ClientDescribeOrganizationResponseTypeDef",
    "ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef",
    "ClientDescribeOrganizationalUnitResponseTypeDef",
    "ClientDescribePolicyResponsePolicyPolicySummaryTypeDef",
    "ClientDescribePolicyResponsePolicyTypeDef",
    "ClientDescribePolicyResponseTypeDef",
    "ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef",
    "ClientDisablePolicyTypeResponseRootTypeDef",
    "ClientDisablePolicyTypeResponseTypeDef",
    "ClientEnableAllFeaturesResponseHandshakePartiesTypeDef",
    "ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef",
    "ClientEnableAllFeaturesResponseHandshakeTypeDef",
    "ClientEnableAllFeaturesResponseTypeDef",
    "ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef",
    "ClientEnablePolicyTypeResponseRootTypeDef",
    "ClientEnablePolicyTypeResponseTypeDef",
    "ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef",
    "ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef",
    "ClientInviteAccountToOrganizationResponseHandshakeTypeDef",
    "ClientInviteAccountToOrganizationResponseTypeDef",
    "ClientInviteAccountToOrganizationTargetTypeDef",
    "ClientListAccountsForParentResponseAccountsTypeDef",
    "ClientListAccountsForParentResponseTypeDef",
    "ClientListAccountsResponseAccountsTypeDef",
    "ClientListAccountsResponseTypeDef",
    "ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef",
    "ClientListAwsServiceAccessForOrganizationResponseTypeDef",
    "ClientListChildrenResponseChildrenTypeDef",
    "ClientListChildrenResponseTypeDef",
    "ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef",
    "ClientListCreateAccountStatusResponseTypeDef",
    "ClientListHandshakesForAccountFilterTypeDef",
    "ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef",
    "ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef",
    "ClientListHandshakesForAccountResponseHandshakesTypeDef",
    "ClientListHandshakesForAccountResponseTypeDef",
    "ClientListHandshakesForOrganizationFilterTypeDef",
    "ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef",
    "ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef",
    "ClientListHandshakesForOrganizationResponseHandshakesTypeDef",
    "ClientListHandshakesForOrganizationResponseTypeDef",
    "ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef",
    "ClientListOrganizationalUnitsForParentResponseTypeDef",
    "ClientListParentsResponseParentsTypeDef",
    "ClientListParentsResponseTypeDef",
    "ClientListPoliciesForTargetResponsePoliciesTypeDef",
    "ClientListPoliciesForTargetResponseTypeDef",
    "ClientListPoliciesResponsePoliciesTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientListRootsResponseRootsPolicyTypesTypeDef",
    "ClientListRootsResponseRootsTypeDef",
    "ClientListRootsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTargetsForPolicyResponseTargetsTypeDef",
    "ClientListTargetsForPolicyResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    "ClientUpdateOrganizationalUnitResponseTypeDef",
    "ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef",
    "ClientUpdatePolicyResponsePolicyTypeDef",
    "ClientUpdatePolicyResponseTypeDef",
    "ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef",
    "ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef",
    "ListAWSServiceAccessForOrganizationPaginateResponseTypeDef",
    "ListAccountsForParentPaginatePaginationConfigTypeDef",
    "ListAccountsForParentPaginateResponseAccountsTypeDef",
    "ListAccountsForParentPaginateResponseTypeDef",
    "ListAccountsPaginatePaginationConfigTypeDef",
    "ListAccountsPaginateResponseAccountsTypeDef",
    "ListAccountsPaginateResponseTypeDef",
    "ListChildrenPaginatePaginationConfigTypeDef",
    "ListChildrenPaginateResponseChildrenTypeDef",
    "ListChildrenPaginateResponseTypeDef",
    "ListCreateAccountStatusPaginatePaginationConfigTypeDef",
    "ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef",
    "ListCreateAccountStatusPaginateResponseTypeDef",
    "ListHandshakesForAccountPaginateFilterTypeDef",
    "ListHandshakesForAccountPaginatePaginationConfigTypeDef",
    "ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef",
    "ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef",
    "ListHandshakesForAccountPaginateResponseHandshakesTypeDef",
    "ListHandshakesForAccountPaginateResponseTypeDef",
    "ListHandshakesForOrganizationPaginateFilterTypeDef",
    "ListHandshakesForOrganizationPaginatePaginationConfigTypeDef",
    "ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef",
    "ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef",
    "ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef",
    "ListHandshakesForOrganizationPaginateResponseTypeDef",
    "ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef",
    "ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef",
    "ListOrganizationalUnitsForParentPaginateResponseTypeDef",
    "ListParentsPaginatePaginationConfigTypeDef",
    "ListParentsPaginateResponseParentsTypeDef",
    "ListParentsPaginateResponseTypeDef",
    "ListPoliciesForTargetPaginatePaginationConfigTypeDef",
    "ListPoliciesForTargetPaginateResponsePoliciesTypeDef",
    "ListPoliciesForTargetPaginateResponseTypeDef",
    "ListPoliciesPaginatePaginationConfigTypeDef",
    "ListPoliciesPaginateResponsePoliciesTypeDef",
    "ListPoliciesPaginateResponseTypeDef",
    "ListRootsPaginatePaginationConfigTypeDef",
    "ListRootsPaginateResponseRootsPolicyTypesTypeDef",
    "ListRootsPaginateResponseRootsTypeDef",
    "ListRootsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListTargetsForPolicyPaginatePaginationConfigTypeDef",
    "ListTargetsForPolicyPaginateResponseTargetsTypeDef",
    "ListTargetsForPolicyPaginateResponseTypeDef",
)


_ClientAcceptHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientAcceptHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ClientAcceptHandshakeResponseHandshakePartiesTypeDef(
    _ClientAcceptHandshakeResponseHandshakePartiesTypeDef
):
    pass


_ClientAcceptHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientAcceptHandshakeResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ClientAcceptHandshakeResponseHandshakeResourcesTypeDef(
    _ClientAcceptHandshakeResponseHandshakeResourcesTypeDef
):
    pass


_ClientAcceptHandshakeResponseHandshakeTypeDef = TypedDict(
    "_ClientAcceptHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientAcceptHandshakeResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientAcceptHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientAcceptHandshakeResponseHandshakeTypeDef(_ClientAcceptHandshakeResponseHandshakeTypeDef):
    """
    - **Handshake** *(dict) --*

      A structure that contains details about the accepted handshake.
      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientAcceptHandshakeResponseTypeDef = TypedDict(
    "_ClientAcceptHandshakeResponseTypeDef",
    {"Handshake": ClientAcceptHandshakeResponseHandshakeTypeDef},
    total=False,
)


class ClientAcceptHandshakeResponseTypeDef(_ClientAcceptHandshakeResponseTypeDef):
    """
    - *(dict) --*

      - **Handshake** *(dict) --*

        A structure that contains details about the accepted handshake.
        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientCancelHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientCancelHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ClientCancelHandshakeResponseHandshakePartiesTypeDef(
    _ClientCancelHandshakeResponseHandshakePartiesTypeDef
):
    pass


_ClientCancelHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientCancelHandshakeResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ClientCancelHandshakeResponseHandshakeResourcesTypeDef(
    _ClientCancelHandshakeResponseHandshakeResourcesTypeDef
):
    pass


_ClientCancelHandshakeResponseHandshakeTypeDef = TypedDict(
    "_ClientCancelHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientCancelHandshakeResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientCancelHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientCancelHandshakeResponseHandshakeTypeDef(_ClientCancelHandshakeResponseHandshakeTypeDef):
    """
    - **Handshake** *(dict) --*

      A structure that contains details about the handshake that you canceled.
      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientCancelHandshakeResponseTypeDef = TypedDict(
    "_ClientCancelHandshakeResponseTypeDef",
    {"Handshake": ClientCancelHandshakeResponseHandshakeTypeDef},
    total=False,
)


class ClientCancelHandshakeResponseTypeDef(_ClientCancelHandshakeResponseTypeDef):
    """
    - *(dict) --*

      - **Handshake** *(dict) --*

        A structure that contains details about the handshake that you canceled.
        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientCreateAccountResponseCreateAccountStatusTypeDef = TypedDict(
    "_ClientCreateAccountResponseCreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)


class ClientCreateAccountResponseCreateAccountStatusTypeDef(
    _ClientCreateAccountResponseCreateAccountStatusTypeDef
):
    """
    - **CreateAccountStatus** *(dict) --*

      A structure that contains details about the request to create an account. This response
      structure might not be fully populated when you first receive it because account creation is
      an asynchronous process. You can pass the returned ``CreateAccountStatus`` ID as a parameter
      to  DescribeCreateAccountStatus to get status about the progress of the request at later
      times. You can also check the AWS CloudTrail log for the ``CreateAccountResult`` event. For
      more information, see `Monitoring the Activity in Your Organization
      <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_monitoring.html>`__ in the
      *AWS Organizations User Guide* .
      - **Id** *(string) --*

        The unique identifier (ID) that references this request. You get this value from the
        response of the initial  CreateAccount request to create the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
        string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientCreateAccountResponseTypeDef = TypedDict(
    "_ClientCreateAccountResponseTypeDef",
    {"CreateAccountStatus": ClientCreateAccountResponseCreateAccountStatusTypeDef},
    total=False,
)


class ClientCreateAccountResponseTypeDef(_ClientCreateAccountResponseTypeDef):
    """
    - *(dict) --*

      - **CreateAccountStatus** *(dict) --*

        A structure that contains details about the request to create an account. This response
        structure might not be fully populated when you first receive it because account creation is
        an asynchronous process. You can pass the returned ``CreateAccountStatus`` ID as a parameter
        to  DescribeCreateAccountStatus to get status about the progress of the request at later
        times. You can also check the AWS CloudTrail log for the ``CreateAccountResult`` event. For
        more information, see `Monitoring the Activity in Your Organization
        <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_monitoring.html>`__ in the
        *AWS Organizations User Guide* .
        - **Id** *(string) --*

          The unique identifier (ID) that references this request. You get this value from the
          response of the initial  CreateAccount request to create the account.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
          string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef = TypedDict(
    "_ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)


class ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef(
    _ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef
):
    """
    - **CreateAccountStatus** *(dict) --*

      Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an AWS
      account or an AWS GovCloud (US) account in an organization.
      - **Id** *(string) --*

        The unique identifier (ID) that references this request. You get this value from the
        response of the initial  CreateAccount request to create the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
        string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientCreateGovCloudAccountResponseTypeDef = TypedDict(
    "_ClientCreateGovCloudAccountResponseTypeDef",
    {"CreateAccountStatus": ClientCreateGovCloudAccountResponseCreateAccountStatusTypeDef},
    total=False,
)


class ClientCreateGovCloudAccountResponseTypeDef(_ClientCreateGovCloudAccountResponseTypeDef):
    """
    - *(dict) --*

      - **CreateAccountStatus** *(dict) --*

        Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an
        AWS account or an AWS GovCloud (US) account in an organization.
        - **Id** *(string) --*

          The unique identifier (ID) that references this request. You get this value from the
          response of the initial  CreateAccount request to create the account.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
          string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef = TypedDict(
    "_ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)


class ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef(
    _ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
):
    pass


_ClientCreateOrganizationResponseOrganizationTypeDef = TypedDict(
    "_ClientCreateOrganizationResponseOrganizationTypeDef",
    {
        "Id": str,
        "Arn": str,
        "FeatureSet": Literal["ALL", "CONSOLIDATED_BILLING"],
        "MasterAccountArn": str,
        "MasterAccountId": str,
        "MasterAccountEmail": str,
        "AvailablePolicyTypes": List[
            ClientCreateOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
        ],
    },
    total=False,
)


class ClientCreateOrganizationResponseOrganizationTypeDef(
    _ClientCreateOrganizationResponseOrganizationTypeDef
):
    """
    - **Organization** *(dict) --*

      A structure that contains details about the newly created organization.
      - **Id** *(string) --*

        The unique identifier (ID) of an organization.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string
        requires "o-" followed by from 10 to 32 lower-case letters or digits.
    """


_ClientCreateOrganizationResponseTypeDef = TypedDict(
    "_ClientCreateOrganizationResponseTypeDef",
    {"Organization": ClientCreateOrganizationResponseOrganizationTypeDef},
    total=False,
)


class ClientCreateOrganizationResponseTypeDef(_ClientCreateOrganizationResponseTypeDef):
    """
    - *(dict) --*

      - **Organization** *(dict) --*

        A structure that contains details about the newly created organization.
        - **Id** *(string) --*

          The unique identifier (ID) of an organization.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string
          requires "o-" followed by from 10 to 32 lower-case letters or digits.
    """


_ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef = TypedDict(
    "_ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef(
    _ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef
):
    """
    - **OrganizationalUnit** *(dict) --*

      A structure that contains details about the newly created OU.
      - **Id** *(string) --*

        The unique identifier (ID) associated with this OU.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string
        requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root
        that contains the OU). This string is followed by a second "-" dash and from 8 to 32
        additional lower-case letters or digits.
    """


_ClientCreateOrganizationalUnitResponseTypeDef = TypedDict(
    "_ClientCreateOrganizationalUnitResponseTypeDef",
    {"OrganizationalUnit": ClientCreateOrganizationalUnitResponseOrganizationalUnitTypeDef},
    total=False,
)


class ClientCreateOrganizationalUnitResponseTypeDef(_ClientCreateOrganizationalUnitResponseTypeDef):
    """
    - *(dict) --*

      - **OrganizationalUnit** *(dict) --*

        A structure that contains details about the newly created OU.
        - **Id** *(string) --*

          The unique identifier (ID) associated with this OU.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
          string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the
          root that contains the OU). This string is followed by a second "-" dash and from 8 to 32
          additional lower-case letters or digits.
    """


_ClientCreatePolicyResponsePolicyPolicySummaryTypeDef = TypedDict(
    "_ClientCreatePolicyResponsePolicyPolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)


class ClientCreatePolicyResponsePolicyPolicySummaryTypeDef(
    _ClientCreatePolicyResponsePolicyPolicySummaryTypeDef
):
    """
    - **PolicySummary** *(dict) --*

      A structure that contains additional details about the policy.
      - **Id** *(string) --*

        The unique identifier (ID) of the policy.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-"
        followed by from 8 to 128 lower-case letters or digits.
    """


_ClientCreatePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientCreatePolicyResponsePolicyTypeDef",
    {"PolicySummary": ClientCreatePolicyResponsePolicyPolicySummaryTypeDef, "Content": str},
    total=False,
)


class ClientCreatePolicyResponsePolicyTypeDef(_ClientCreatePolicyResponsePolicyTypeDef):
    """
    - **Policy** *(dict) --*

      A structure that contains details about the newly created policy.
      - **PolicySummary** *(dict) --*

        A structure that contains additional details about the policy.
        - **Id** *(string) --*

          The unique identifier (ID) of the policy.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.
    """


_ClientCreatePolicyResponseTypeDef = TypedDict(
    "_ClientCreatePolicyResponseTypeDef",
    {"Policy": ClientCreatePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientCreatePolicyResponseTypeDef(_ClientCreatePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(dict) --*

        A structure that contains details about the newly created policy.
        - **PolicySummary** *(dict) --*

          A structure that contains additional details about the policy.
          - **Id** *(string) --*

            The unique identifier (ID) of the policy.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
            "p-" followed by from 8 to 128 lower-case letters or digits.
    """


_ClientDeclineHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientDeclineHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ClientDeclineHandshakeResponseHandshakePartiesTypeDef(
    _ClientDeclineHandshakeResponseHandshakePartiesTypeDef
):
    pass


_ClientDeclineHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientDeclineHandshakeResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ClientDeclineHandshakeResponseHandshakeResourcesTypeDef(
    _ClientDeclineHandshakeResponseHandshakeResourcesTypeDef
):
    pass


_ClientDeclineHandshakeResponseHandshakeTypeDef = TypedDict(
    "_ClientDeclineHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientDeclineHandshakeResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientDeclineHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientDeclineHandshakeResponseHandshakeTypeDef(
    _ClientDeclineHandshakeResponseHandshakeTypeDef
):
    """
    - **Handshake** *(dict) --*

      A structure that contains details about the declined handshake. The state is updated to show
      the value ``DECLINED`` .
      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientDeclineHandshakeResponseTypeDef = TypedDict(
    "_ClientDeclineHandshakeResponseTypeDef",
    {"Handshake": ClientDeclineHandshakeResponseHandshakeTypeDef},
    total=False,
)


class ClientDeclineHandshakeResponseTypeDef(_ClientDeclineHandshakeResponseTypeDef):
    """
    - *(dict) --*

      - **Handshake** *(dict) --*

        A structure that contains details about the declined handshake. The state is updated to show
        the value ``DECLINED`` .
        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientDescribeAccountResponseAccountTypeDef = TypedDict(
    "_ClientDescribeAccountResponseAccountTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": Literal["ACTIVE", "SUSPENDED"],
        "JoinedMethod": Literal["INVITED", "CREATED"],
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeAccountResponseAccountTypeDef(_ClientDescribeAccountResponseAccountTypeDef):
    """
    - **Account** *(dict) --*

      A structure that contains information about the requested account.
      - **Id** *(string) --*

        The unique identifier (ID) of the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.
    """


_ClientDescribeAccountResponseTypeDef = TypedDict(
    "_ClientDescribeAccountResponseTypeDef",
    {"Account": ClientDescribeAccountResponseAccountTypeDef},
    total=False,
)


class ClientDescribeAccountResponseTypeDef(_ClientDescribeAccountResponseTypeDef):
    """
    - *(dict) --*

      - **Account** *(dict) --*

        A structure that contains information about the requested account.
        - **Id** *(string) --*

          The unique identifier (ID) of the account.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
          exactly 12 digits.
    """


_ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef = TypedDict(
    "_ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)


class ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef(
    _ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef
):
    """
    - **CreateAccountStatus** *(dict) --*

      A structure that contains the current status of an account creation request.
      - **Id** *(string) --*

        The unique identifier (ID) that references this request. You get this value from the
        response of the initial  CreateAccount request to create the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
        string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientDescribeCreateAccountStatusResponseTypeDef = TypedDict(
    "_ClientDescribeCreateAccountStatusResponseTypeDef",
    {"CreateAccountStatus": ClientDescribeCreateAccountStatusResponseCreateAccountStatusTypeDef},
    total=False,
)


class ClientDescribeCreateAccountStatusResponseTypeDef(
    _ClientDescribeCreateAccountStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **CreateAccountStatus** *(dict) --*

        A structure that contains the current status of an account creation request.
        - **Id** *(string) --*

          The unique identifier (ID) that references this request. You get this value from the
          response of the initial  CreateAccount request to create the account.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
          string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef = TypedDict(
    "_ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef",
    {"PolicyContent": str, "LastUpdatedTimestamp": datetime, "TargetId": str, "PolicyType": str},
    total=False,
)


class ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef(
    _ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef
):
    """
    - **EffectivePolicy** *(dict) --*

      The contents of the effective policy.
      - **PolicyContent** *(string) --*

        The text content of the policy.
    """


_ClientDescribeEffectivePolicyResponseTypeDef = TypedDict(
    "_ClientDescribeEffectivePolicyResponseTypeDef",
    {"EffectivePolicy": ClientDescribeEffectivePolicyResponseEffectivePolicyTypeDef},
    total=False,
)


class ClientDescribeEffectivePolicyResponseTypeDef(_ClientDescribeEffectivePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **EffectivePolicy** *(dict) --*

        The contents of the effective policy.
        - **PolicyContent** *(string) --*

          The text content of the policy.
    """


_ClientDescribeHandshakeResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientDescribeHandshakeResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ClientDescribeHandshakeResponseHandshakePartiesTypeDef(
    _ClientDescribeHandshakeResponseHandshakePartiesTypeDef
):
    pass


_ClientDescribeHandshakeResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientDescribeHandshakeResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ClientDescribeHandshakeResponseHandshakeResourcesTypeDef(
    _ClientDescribeHandshakeResponseHandshakeResourcesTypeDef
):
    pass


_ClientDescribeHandshakeResponseHandshakeTypeDef = TypedDict(
    "_ClientDescribeHandshakeResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientDescribeHandshakeResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientDescribeHandshakeResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientDescribeHandshakeResponseHandshakeTypeDef(
    _ClientDescribeHandshakeResponseHandshakeTypeDef
):
    """
    - **Handshake** *(dict) --*

      A structure that contains information about the specified handshake.
      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientDescribeHandshakeResponseTypeDef = TypedDict(
    "_ClientDescribeHandshakeResponseTypeDef",
    {"Handshake": ClientDescribeHandshakeResponseHandshakeTypeDef},
    total=False,
)


class ClientDescribeHandshakeResponseTypeDef(_ClientDescribeHandshakeResponseTypeDef):
    """
    - *(dict) --*

      - **Handshake** *(dict) --*

        A structure that contains information about the specified handshake.
        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef = TypedDict(
    "_ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)


class ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef(
    _ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
):
    pass


_ClientDescribeOrganizationResponseOrganizationTypeDef = TypedDict(
    "_ClientDescribeOrganizationResponseOrganizationTypeDef",
    {
        "Id": str,
        "Arn": str,
        "FeatureSet": Literal["ALL", "CONSOLIDATED_BILLING"],
        "MasterAccountArn": str,
        "MasterAccountId": str,
        "MasterAccountEmail": str,
        "AvailablePolicyTypes": List[
            ClientDescribeOrganizationResponseOrganizationAvailablePolicyTypesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeOrganizationResponseOrganizationTypeDef(
    _ClientDescribeOrganizationResponseOrganizationTypeDef
):
    """
    - **Organization** *(dict) --*

      A structure that contains information about the organization.
      - **Id** *(string) --*

        The unique identifier (ID) of an organization.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string
        requires "o-" followed by from 10 to 32 lower-case letters or digits.
    """


_ClientDescribeOrganizationResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationResponseTypeDef",
    {"Organization": ClientDescribeOrganizationResponseOrganizationTypeDef},
    total=False,
)


class ClientDescribeOrganizationResponseTypeDef(_ClientDescribeOrganizationResponseTypeDef):
    """
    - *(dict) --*

      - **Organization** *(dict) --*

        A structure that contains information about the organization.
        - **Id** *(string) --*

          The unique identifier (ID) of an organization.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string
          requires "o-" followed by from 10 to 32 lower-case letters or digits.
    """


_ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef = TypedDict(
    "_ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef(
    _ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef
):
    """
    - **OrganizationalUnit** *(dict) --*

      A structure that contains details about the specified OU.
      - **Id** *(string) --*

        The unique identifier (ID) associated with this OU.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string
        requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root
        that contains the OU). This string is followed by a second "-" dash and from 8 to 32
        additional lower-case letters or digits.
    """


_ClientDescribeOrganizationalUnitResponseTypeDef = TypedDict(
    "_ClientDescribeOrganizationalUnitResponseTypeDef",
    {"OrganizationalUnit": ClientDescribeOrganizationalUnitResponseOrganizationalUnitTypeDef},
    total=False,
)


class ClientDescribeOrganizationalUnitResponseTypeDef(
    _ClientDescribeOrganizationalUnitResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationalUnit** *(dict) --*

        A structure that contains details about the specified OU.
        - **Id** *(string) --*

          The unique identifier (ID) associated with this OU.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
          string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the
          root that contains the OU). This string is followed by a second "-" dash and from 8 to 32
          additional lower-case letters or digits.
    """


_ClientDescribePolicyResponsePolicyPolicySummaryTypeDef = TypedDict(
    "_ClientDescribePolicyResponsePolicyPolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)


class ClientDescribePolicyResponsePolicyPolicySummaryTypeDef(
    _ClientDescribePolicyResponsePolicyPolicySummaryTypeDef
):
    """
    - **PolicySummary** *(dict) --*

      A structure that contains additional details about the policy.
      - **Id** *(string) --*

        The unique identifier (ID) of the policy.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-"
        followed by from 8 to 128 lower-case letters or digits.
    """


_ClientDescribePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientDescribePolicyResponsePolicyTypeDef",
    {"PolicySummary": ClientDescribePolicyResponsePolicyPolicySummaryTypeDef, "Content": str},
    total=False,
)


class ClientDescribePolicyResponsePolicyTypeDef(_ClientDescribePolicyResponsePolicyTypeDef):
    """
    - **Policy** *(dict) --*

      A structure that contains details about the specified policy.
      - **PolicySummary** *(dict) --*

        A structure that contains additional details about the policy.
        - **Id** *(string) --*

          The unique identifier (ID) of the policy.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.
    """


_ClientDescribePolicyResponseTypeDef = TypedDict(
    "_ClientDescribePolicyResponseTypeDef",
    {"Policy": ClientDescribePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientDescribePolicyResponseTypeDef(_ClientDescribePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(dict) --*

        A structure that contains details about the specified policy.
        - **PolicySummary** *(dict) --*

          A structure that contains additional details about the policy.
          - **Id** *(string) --*

            The unique identifier (ID) of the policy.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
            "p-" followed by from 8 to 128 lower-case letters or digits.
    """


_ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef = TypedDict(
    "_ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)


class ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef(
    _ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef
):
    pass


_ClientDisablePolicyTypeResponseRootTypeDef = TypedDict(
    "_ClientDisablePolicyTypeResponseRootTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ClientDisablePolicyTypeResponseRootPolicyTypesTypeDef],
    },
    total=False,
)


class ClientDisablePolicyTypeResponseRootTypeDef(_ClientDisablePolicyTypeResponseRootTypeDef):
    """
    - **Root** *(dict) --*

      A structure that shows the root with the updated list of enabled policy types.
      - **Id** *(string) --*

        The unique identifier (ID) for the root.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
        followed by from 4 to 32 lower-case letters or digits.
    """


_ClientDisablePolicyTypeResponseTypeDef = TypedDict(
    "_ClientDisablePolicyTypeResponseTypeDef",
    {"Root": ClientDisablePolicyTypeResponseRootTypeDef},
    total=False,
)


class ClientDisablePolicyTypeResponseTypeDef(_ClientDisablePolicyTypeResponseTypeDef):
    """
    - *(dict) --*

      - **Root** *(dict) --*

        A structure that shows the root with the updated list of enabled policy types.
        - **Id** *(string) --*

          The unique identifier (ID) for the root.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
          followed by from 4 to 32 lower-case letters or digits.
    """


_ClientEnableAllFeaturesResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientEnableAllFeaturesResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ClientEnableAllFeaturesResponseHandshakePartiesTypeDef(
    _ClientEnableAllFeaturesResponseHandshakePartiesTypeDef
):
    pass


_ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef(
    _ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef
):
    pass


_ClientEnableAllFeaturesResponseHandshakeTypeDef = TypedDict(
    "_ClientEnableAllFeaturesResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientEnableAllFeaturesResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientEnableAllFeaturesResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientEnableAllFeaturesResponseHandshakeTypeDef(
    _ClientEnableAllFeaturesResponseHandshakeTypeDef
):
    """
    - **Handshake** *(dict) --*

      A structure that contains details about the handshake created to support this request to
      enable all features in the organization.
      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientEnableAllFeaturesResponseTypeDef = TypedDict(
    "_ClientEnableAllFeaturesResponseTypeDef",
    {"Handshake": ClientEnableAllFeaturesResponseHandshakeTypeDef},
    total=False,
)


class ClientEnableAllFeaturesResponseTypeDef(_ClientEnableAllFeaturesResponseTypeDef):
    """
    - *(dict) --*

      - **Handshake** *(dict) --*

        A structure that contains details about the handshake created to support this request to
        enable all features in the organization.
        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef = TypedDict(
    "_ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)


class ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef(
    _ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef
):
    pass


_ClientEnablePolicyTypeResponseRootTypeDef = TypedDict(
    "_ClientEnablePolicyTypeResponseRootTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ClientEnablePolicyTypeResponseRootPolicyTypesTypeDef],
    },
    total=False,
)


class ClientEnablePolicyTypeResponseRootTypeDef(_ClientEnablePolicyTypeResponseRootTypeDef):
    """
    - **Root** *(dict) --*

      A structure that shows the root with the updated list of enabled policy types.
      - **Id** *(string) --*

        The unique identifier (ID) for the root.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
        followed by from 4 to 32 lower-case letters or digits.
    """


_ClientEnablePolicyTypeResponseTypeDef = TypedDict(
    "_ClientEnablePolicyTypeResponseTypeDef",
    {"Root": ClientEnablePolicyTypeResponseRootTypeDef},
    total=False,
)


class ClientEnablePolicyTypeResponseTypeDef(_ClientEnablePolicyTypeResponseTypeDef):
    """
    - *(dict) --*

      - **Root** *(dict) --*

        A structure that shows the root with the updated list of enabled policy types.
        - **Id** *(string) --*

          The unique identifier (ID) for the root.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
          followed by from 4 to 32 lower-case letters or digits.
    """


_ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef(
    _ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef
):
    pass


_ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef(
    _ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef
):
    pass


_ClientInviteAccountToOrganizationResponseHandshakeTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationResponseHandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientInviteAccountToOrganizationResponseHandshakePartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientInviteAccountToOrganizationResponseHandshakeResourcesTypeDef],
    },
    total=False,
)


class ClientInviteAccountToOrganizationResponseHandshakeTypeDef(
    _ClientInviteAccountToOrganizationResponseHandshakeTypeDef
):
    """
    - **Handshake** *(dict) --*

      A structure that contains details about the handshake that is created to support this
      invitation request.
      - **Id** *(string) --*

        The unique identifier (ID) of a handshake. The originating account creates the ID when it
        initiates the handshake.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
        "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientInviteAccountToOrganizationResponseTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationResponseTypeDef",
    {"Handshake": ClientInviteAccountToOrganizationResponseHandshakeTypeDef},
    total=False,
)


class ClientInviteAccountToOrganizationResponseTypeDef(
    _ClientInviteAccountToOrganizationResponseTypeDef
):
    """
    - *(dict) --*

      - **Handshake** *(dict) --*

        A structure that contains details about the handshake that is created to support this
        invitation request.
        - **Id** *(string) --*

          The unique identifier (ID) of a handshake. The originating account creates the ID when it
          initiates the handshake.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires
          "h-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientInviteAccountToOrganizationTargetTypeDef = TypedDict(
    "_ClientInviteAccountToOrganizationTargetTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ClientInviteAccountToOrganizationTargetTypeDef(
    _ClientInviteAccountToOrganizationTargetTypeDef
):
    """
    The identifier (ID) of the AWS account that you want to invite to join your organization. This
    is a JSON object that contains the following elements:

      ``{ "Type": "ACCOUNT", "Id": "<* **account id number** * >" }``
    """


_ClientListAccountsForParentResponseAccountsTypeDef = TypedDict(
    "_ClientListAccountsForParentResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": Literal["ACTIVE", "SUSPENDED"],
        "JoinedMethod": Literal["INVITED", "CREATED"],
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ClientListAccountsForParentResponseAccountsTypeDef(
    _ClientListAccountsForParentResponseAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about an AWS account that is a member of an organization.
      - **Id** *(string) --*

        The unique identifier (ID) of the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.
    """


_ClientListAccountsForParentResponseTypeDef = TypedDict(
    "_ClientListAccountsForParentResponseTypeDef",
    {"Accounts": List[ClientListAccountsForParentResponseAccountsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAccountsForParentResponseTypeDef(_ClientListAccountsForParentResponseTypeDef):
    """
    - *(dict) --*

      - **Accounts** *(list) --*

        A list of the accounts in the specified root or OU.
        - *(dict) --*

          Contains information about an AWS account that is a member of an organization.
          - **Id** *(string) --*

            The unique identifier (ID) of the account.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string
            requires exactly 12 digits.
    """


_ClientListAccountsResponseAccountsTypeDef = TypedDict(
    "_ClientListAccountsResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": Literal["ACTIVE", "SUSPENDED"],
        "JoinedMethod": Literal["INVITED", "CREATED"],
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ClientListAccountsResponseAccountsTypeDef(_ClientListAccountsResponseAccountsTypeDef):
    """
    - *(dict) --*

      Contains information about an AWS account that is a member of an organization.
      - **Id** *(string) --*

        The unique identifier (ID) of the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.
    """


_ClientListAccountsResponseTypeDef = TypedDict(
    "_ClientListAccountsResponseTypeDef",
    {"Accounts": List[ClientListAccountsResponseAccountsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAccountsResponseTypeDef(_ClientListAccountsResponseTypeDef):
    """
    - *(dict) --*

      - **Accounts** *(list) --*

        A list of objects in the organization.
        - *(dict) --*

          Contains information about an AWS account that is a member of an organization.
          - **Id** *(string) --*

            The unique identifier (ID) of the account.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string
            requires exactly 12 digits.
    """


_ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef = TypedDict(
    "_ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef",
    {"ServicePrincipal": str, "DateEnabled": datetime},
    total=False,
)


class ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef(
    _ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef
):
    """
    - *(dict) --*

      A structure that contains details of a service principal that is enabled to integrate with AWS
      Organizations.
      - **ServicePrincipal** *(string) --*

        The name of the service principal. This is typically in the form of a URL, such as: ``
        *servicename* .amazonaws.com`` .
    """


_ClientListAwsServiceAccessForOrganizationResponseTypeDef = TypedDict(
    "_ClientListAwsServiceAccessForOrganizationResponseTypeDef",
    {
        "EnabledServicePrincipals": List[
            ClientListAwsServiceAccessForOrganizationResponseEnabledServicePrincipalsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListAwsServiceAccessForOrganizationResponseTypeDef(
    _ClientListAwsServiceAccessForOrganizationResponseTypeDef
):
    """
    - *(dict) --*

      - **EnabledServicePrincipals** *(list) --*

        A list of the service principals for the services that are enabled to integrate with your
        organization. Each principal is a structure that includes the name and the date that it was
        enabled for integration with AWS Organizations.
        - *(dict) --*

          A structure that contains details of a service principal that is enabled to integrate with
          AWS Organizations.
          - **ServicePrincipal** *(string) --*

            The name of the service principal. This is typically in the form of a URL, such as: ``
            *servicename* .amazonaws.com`` .
    """


_ClientListChildrenResponseChildrenTypeDef = TypedDict(
    "_ClientListChildrenResponseChildrenTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"]},
    total=False,
)


class ClientListChildrenResponseChildrenTypeDef(_ClientListChildrenResponseChildrenTypeDef):
    """
    - *(dict) --*

      Contains a list of child entities, either OUs or accounts.
      - **Id** *(string) --*

        The unique identifier (ID) of this child entity.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires one
        of the following:
        * Account: A string that consists of exactly 12 digits.
        * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
        lower-case letters or digits (the ID of the root that contains the OU). This string is
        followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ClientListChildrenResponseTypeDef = TypedDict(
    "_ClientListChildrenResponseTypeDef",
    {"Children": List[ClientListChildrenResponseChildrenTypeDef], "NextToken": str},
    total=False,
)


class ClientListChildrenResponseTypeDef(_ClientListChildrenResponseTypeDef):
    """
    - *(dict) --*

      - **Children** *(list) --*

        The list of children of the specified parent container.
        - *(dict) --*

          Contains a list of child entities, either OUs or accounts.
          - **Id** *(string) --*

            The unique identifier (ID) of this child entity.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires
            one of the following:
            * Account: A string that consists of exactly 12 digits.
            * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
            lower-case letters or digits (the ID of the root that contains the OU). This string is
            followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef = TypedDict(
    "_ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)


class ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef(
    _ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef
):
    """
    - *(dict) --*

      Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an AWS
      account or an AWS GovCloud (US) account in an organization.
      - **Id** *(string) --*

        The unique identifier (ID) that references this request. You get this value from the
        response of the initial  CreateAccount request to create the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
        string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientListCreateAccountStatusResponseTypeDef = TypedDict(
    "_ClientListCreateAccountStatusResponseTypeDef",
    {
        "CreateAccountStatuses": List[
            ClientListCreateAccountStatusResponseCreateAccountStatusesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCreateAccountStatusResponseTypeDef(_ClientListCreateAccountStatusResponseTypeDef):
    """
    - *(dict) --*

      - **CreateAccountStatuses** *(list) --*

        A list of objects with details about the requests. Certain elements, such as the accountId
        number, are present in the output only after the account has been successfully created.
        - *(dict) --*

          Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an
          AWS account or an AWS GovCloud (US) account in an organization.
          - **Id** *(string) --*

            The unique identifier (ID) that references this request. You get this value from the
            response of the initial  CreateAccount request to create the account.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
            string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ClientListHandshakesForAccountFilterTypeDef = TypedDict(
    "_ClientListHandshakesForAccountFilterTypeDef",
    {
        "ActionType": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "ParentHandshakeId": str,
    },
    total=False,
)


class ClientListHandshakesForAccountFilterTypeDef(_ClientListHandshakesForAccountFilterTypeDef):
    """
    Filters the handshakes that you want included in the response. The default is all types. Use the
    ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` ,
    ``ENABLE_ALL_FEATURES`` , or ``APPROVE_ALL_FEATURES`` . Alternatively, you can specify the
    ``ENABLE_ALL_FEATURES`` handshake, which generates a separate child handshake for each member
    account. When you do specify ``ParentHandshakeId`` to see only the handshakes that were
    generated by that parent request.
    - **ActionType** *(string) --*

      Specifies the type of handshake action.
      If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .
    """


_ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef = TypedDict(
    "_ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef(
    _ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef
):
    pass


_ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef = TypedDict(
    "_ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef(
    _ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef
):
    pass


_ClientListHandshakesForAccountResponseHandshakesTypeDef = TypedDict(
    "_ClientListHandshakesForAccountResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientListHandshakesForAccountResponseHandshakesPartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientListHandshakesForAccountResponseHandshakesResourcesTypeDef],
    },
    total=False,
)


class ClientListHandshakesForAccountResponseHandshakesTypeDef(
    _ClientListHandshakesForAccountResponseHandshakesTypeDef
):
    """
    - *(dict) --*

      Contains information that must be exchanged to securely establish a relationship between two
      accounts (an *originator* and a *recipient* ). For example, assume that a master account (the
      originator) invites another account (the recipient) to join its organization. In that case,
      the two accounts exchange information as a series of handshake requests and responses.

        **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
        days after entering that state. After that, they are deleted.
    """


_ClientListHandshakesForAccountResponseTypeDef = TypedDict(
    "_ClientListHandshakesForAccountResponseTypeDef",
    {"Handshakes": List[ClientListHandshakesForAccountResponseHandshakesTypeDef], "NextToken": str},
    total=False,
)


class ClientListHandshakesForAccountResponseTypeDef(_ClientListHandshakesForAccountResponseTypeDef):
    """
    - *(dict) --*

      - **Handshakes** *(list) --*

        A list of  Handshake objects with details about each of the handshakes that is associated
        with the specified account.
        - *(dict) --*

          Contains information that must be exchanged to securely establish a relationship between
          two accounts (an *originator* and a *recipient* ). For example, assume that a master
          account (the originator) invites another account (the recipient) to join its organization.
          In that case, the two accounts exchange information as a series of handshake requests and
          responses.

            **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only
            30 days after entering that state. After that, they are deleted.
    """


_ClientListHandshakesForOrganizationFilterTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationFilterTypeDef",
    {
        "ActionType": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "ParentHandshakeId": str,
    },
    total=False,
)


class ClientListHandshakesForOrganizationFilterTypeDef(
    _ClientListHandshakesForOrganizationFilterTypeDef
):
    """
    A filter of the handshakes that you want included in the response. The default is all types. Use
    the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` ,
    ``ENABLE-ALL-FEATURES`` , or ``APPROVE-ALL-FEATURES`` . Alternatively, you can specify the
    ``ENABLE-ALL-FEATURES`` handshake, which generates a separate child handshake for each member
    account. When you do, specify the ``ParentHandshakeId`` to see only the handshakes that were
    generated by that parent request.
    - **ActionType** *(string) --*

      Specifies the type of handshake action.
      If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .
    """


_ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef(
    _ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef
):
    pass


_ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef(
    _ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef
):
    pass


_ClientListHandshakesForOrganizationResponseHandshakesTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ClientListHandshakesForOrganizationResponseHandshakesPartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ClientListHandshakesForOrganizationResponseHandshakesResourcesTypeDef],
    },
    total=False,
)


class ClientListHandshakesForOrganizationResponseHandshakesTypeDef(
    _ClientListHandshakesForOrganizationResponseHandshakesTypeDef
):
    """
    - *(dict) --*

      Contains information that must be exchanged to securely establish a relationship between two
      accounts (an *originator* and a *recipient* ). For example, assume that a master account (the
      originator) invites another account (the recipient) to join its organization. In that case,
      the two accounts exchange information as a series of handshake requests and responses.

        **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
        days after entering that state. After that, they are deleted.
    """


_ClientListHandshakesForOrganizationResponseTypeDef = TypedDict(
    "_ClientListHandshakesForOrganizationResponseTypeDef",
    {
        "Handshakes": List[ClientListHandshakesForOrganizationResponseHandshakesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListHandshakesForOrganizationResponseTypeDef(
    _ClientListHandshakesForOrganizationResponseTypeDef
):
    """
    - *(dict) --*

      - **Handshakes** *(list) --*

        A list of  Handshake objects with details about each of the handshakes that are associated
        with an organization.
        - *(dict) --*

          Contains information that must be exchanged to securely establish a relationship between
          two accounts (an *originator* and a *recipient* ). For example, assume that a master
          account (the originator) invites another account (the recipient) to join its organization.
          In that case, the two accounts exchange information as a series of handshake requests and
          responses.

            **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only
            30 days after entering that state. After that, they are deleted.
    """


_ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef = TypedDict(
    "_ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef(
    _ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef
):
    """
    - *(dict) --*

      Contains details about an organizational unit (OU). An OU is a container of AWS accounts
      within a root of an organization. Policies that are attached to an OU apply to all accounts
      contained in that OU and in any child OUs.
      - **Id** *(string) --*

        The unique identifier (ID) associated with this OU.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string
        requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root
        that contains the OU). This string is followed by a second "-" dash and from 8 to 32
        additional lower-case letters or digits.
    """


_ClientListOrganizationalUnitsForParentResponseTypeDef = TypedDict(
    "_ClientListOrganizationalUnitsForParentResponseTypeDef",
    {
        "OrganizationalUnits": List[
            ClientListOrganizationalUnitsForParentResponseOrganizationalUnitsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListOrganizationalUnitsForParentResponseTypeDef(
    _ClientListOrganizationalUnitsForParentResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationalUnits** *(list) --*

        A list of the OUs in the specified root or parent OU.
        - *(dict) --*

          Contains details about an organizational unit (OU). An OU is a container of AWS accounts
          within a root of an organization. Policies that are attached to an OU apply to all
          accounts contained in that OU and in any child OUs.
          - **Id** *(string) --*

            The unique identifier (ID) associated with this OU.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
            string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of
            the root that contains the OU). This string is followed by a second "-" dash and from 8
            to 32 additional lower-case letters or digits.
    """


_ClientListParentsResponseParentsTypeDef = TypedDict(
    "_ClientListParentsResponseParentsTypeDef",
    {"Id": str, "Type": Literal["ROOT", "ORGANIZATIONAL_UNIT"]},
    total=False,
)


class ClientListParentsResponseParentsTypeDef(_ClientListParentsResponseParentsTypeDef):
    """
    - *(dict) --*

      Contains information about either a root or an organizational unit (OU) that can contain OUs
      or accounts in an organization.
      - **Id** *(string) --*

        The unique identifier (ID) of the parent entity.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one
        of the following:
        * Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or
        digits.
        * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
        lower-case letters or digits (the ID of the root that the OU is in). This string is followed
        by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ClientListParentsResponseTypeDef = TypedDict(
    "_ClientListParentsResponseTypeDef",
    {"Parents": List[ClientListParentsResponseParentsTypeDef], "NextToken": str},
    total=False,
)


class ClientListParentsResponseTypeDef(_ClientListParentsResponseTypeDef):
    """
    - *(dict) --*

      - **Parents** *(list) --*

        A list of parents for the specified child account or OU.
        - *(dict) --*

          Contains information about either a root or an organizational unit (OU) that can contain
          OUs or accounts in an organization.
          - **Id** *(string) --*

            The unique identifier (ID) of the parent entity.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires
            one of the following:
            * Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or
            digits.
            * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
            lower-case letters or digits (the ID of the root that the OU is in). This string is
            followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ClientListPoliciesForTargetResponsePoliciesTypeDef = TypedDict(
    "_ClientListPoliciesForTargetResponsePoliciesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)


class ClientListPoliciesForTargetResponsePoliciesTypeDef(
    _ClientListPoliciesForTargetResponsePoliciesTypeDef
):
    """
    - *(dict) --*

      Contains information about a policy, but does not include the content. To see the content of a
      policy, see  DescribePolicy .
      - **Id** *(string) --*

        The unique identifier (ID) of the policy.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-"
        followed by from 8 to 128 lower-case letters or digits.
    """


_ClientListPoliciesForTargetResponseTypeDef = TypedDict(
    "_ClientListPoliciesForTargetResponseTypeDef",
    {"Policies": List[ClientListPoliciesForTargetResponsePoliciesTypeDef], "NextToken": str},
    total=False,
)


class ClientListPoliciesForTargetResponseTypeDef(_ClientListPoliciesForTargetResponseTypeDef):
    """
    - *(dict) --*

      - **Policies** *(list) --*

        The list of policies that match the criteria in the request.
        - *(dict) --*

          Contains information about a policy, but does not include the content. To see the content
          of a policy, see  DescribePolicy .
          - **Id** *(string) --*

            The unique identifier (ID) of the policy.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
            "p-" followed by from 8 to 128 lower-case letters or digits.
    """


_ClientListPoliciesResponsePoliciesTypeDef = TypedDict(
    "_ClientListPoliciesResponsePoliciesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)


class ClientListPoliciesResponsePoliciesTypeDef(_ClientListPoliciesResponsePoliciesTypeDef):
    """
    - *(dict) --*

      Contains information about a policy, but does not include the content. To see the content of a
      policy, see  DescribePolicy .
      - **Id** *(string) --*

        The unique identifier (ID) of the policy.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-"
        followed by from 8 to 128 lower-case letters or digits.
    """


_ClientListPoliciesResponseTypeDef = TypedDict(
    "_ClientListPoliciesResponseTypeDef",
    {"Policies": List[ClientListPoliciesResponsePoliciesTypeDef], "NextToken": str},
    total=False,
)


class ClientListPoliciesResponseTypeDef(_ClientListPoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **Policies** *(list) --*

        A list of policies that match the filter criteria in the request. The output list doesn't
        include the policy contents. To see the content for a policy, see  DescribePolicy .
        - *(dict) --*

          Contains information about a policy, but does not include the content. To see the content
          of a policy, see  DescribePolicy .
          - **Id** *(string) --*

            The unique identifier (ID) of the policy.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
            "p-" followed by from 8 to 128 lower-case letters or digits.
    """


_ClientListRootsResponseRootsPolicyTypesTypeDef = TypedDict(
    "_ClientListRootsResponseRootsPolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)


class ClientListRootsResponseRootsPolicyTypesTypeDef(
    _ClientListRootsResponseRootsPolicyTypesTypeDef
):
    pass


_ClientListRootsResponseRootsTypeDef = TypedDict(
    "_ClientListRootsResponseRootsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ClientListRootsResponseRootsPolicyTypesTypeDef],
    },
    total=False,
)


class ClientListRootsResponseRootsTypeDef(_ClientListRootsResponseRootsTypeDef):
    """
    - *(dict) --*

      Contains details about a root. A root is a top-level parent node in the hierarchy of an
      organization that can contain organizational units (OUs) and accounts. Every root contains
      every AWS account in the organization. Each root enables the accounts to be organized in a
      different way and to have different policy types enabled for use in that root.
      - **Id** *(string) --*

        The unique identifier (ID) for the root.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
        followed by from 4 to 32 lower-case letters or digits.
    """


_ClientListRootsResponseTypeDef = TypedDict(
    "_ClientListRootsResponseTypeDef",
    {"Roots": List[ClientListRootsResponseRootsTypeDef], "NextToken": str},
    total=False,
)


class ClientListRootsResponseTypeDef(_ClientListRootsResponseTypeDef):
    """
    - *(dict) --*

      - **Roots** *(list) --*

        A list of roots that are defined in an organization.
        - *(dict) --*

          Contains details about a root. A root is a top-level parent node in the hierarchy of an
          organization that can contain organizational units (OUs) and accounts. Every root contains
          every AWS account in the organization. Each root enables the accounts to be organized in a
          different way and to have different policy types enabled for use in that root.
          - **Id** *(string) --*

            The unique identifier (ID) for the root.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires
            "r-" followed by from 4 to 32 lower-case letters or digits.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      A custom key-value pair associated with a resource such as an account within your
      organization.
      - **Key** *(string) --*

        The key identifier, or name, of the tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tags that are assigned to the resource.
        - *(dict) --*

          A custom key-value pair associated with a resource such as an account within your
          organization.
          - **Key** *(string) --*

            The key identifier, or name, of the tag.
    """


_ClientListTargetsForPolicyResponseTargetsTypeDef = TypedDict(
    "_ClientListTargetsForPolicyResponseTargetsTypeDef",
    {
        "TargetId": str,
        "Arn": str,
        "Name": str,
        "Type": Literal["ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT"],
    },
    total=False,
)


class ClientListTargetsForPolicyResponseTargetsTypeDef(
    _ClientListTargetsForPolicyResponseTargetsTypeDef
):
    """
    - *(dict) --*

      Contains information about a root, OU, or account that a policy is attached to.
      - **TargetId** *(string) --*

        The unique identifier (ID) of the policy target.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one
        of the following:
        * Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or
        digits.
        * Account: A string that consists of exactly 12 digits.
        * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
        lower-case letters or digits (the ID of the root that the OU is in). This string is followed
        by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ClientListTargetsForPolicyResponseTypeDef = TypedDict(
    "_ClientListTargetsForPolicyResponseTypeDef",
    {"Targets": List[ClientListTargetsForPolicyResponseTargetsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTargetsForPolicyResponseTypeDef(_ClientListTargetsForPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        A list of structures, each of which contains details about one of the entities to which the
        specified policy is attached.
        - *(dict) --*

          Contains information about a root, OU, or account that a policy is attached to.
          - **TargetId** *(string) --*

            The unique identifier (ID) of the policy target.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires
            one of the following:
            * Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or
            digits.
            * Account: A string that consists of exactly 12 digits.
            * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
            lower-case letters or digits (the ID of the root that the OU is in). This string is
            followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      A custom key-value pair associated with a resource such as an account within your
      organization.
      - **Key** *(string) --***[REQUIRED]**

        The key identifier, or name, of the tag.
    """


_ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef = TypedDict(
    "_ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef(
    _ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef
):
    """
    - **OrganizationalUnit** *(dict) --*

      A structure that contains the details about the specified OU, including its new name.
      - **Id** *(string) --*

        The unique identifier (ID) associated with this OU.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string
        requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root
        that contains the OU). This string is followed by a second "-" dash and from 8 to 32
        additional lower-case letters or digits.
    """


_ClientUpdateOrganizationalUnitResponseTypeDef = TypedDict(
    "_ClientUpdateOrganizationalUnitResponseTypeDef",
    {"OrganizationalUnit": ClientUpdateOrganizationalUnitResponseOrganizationalUnitTypeDef},
    total=False,
)


class ClientUpdateOrganizationalUnitResponseTypeDef(_ClientUpdateOrganizationalUnitResponseTypeDef):
    """
    - *(dict) --*

      - **OrganizationalUnit** *(dict) --*

        A structure that contains the details about the specified OU, including its new name.
        - **Id** *(string) --*

          The unique identifier (ID) associated with this OU.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
          string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the
          root that contains the OU). This string is followed by a second "-" dash and from 8 to 32
          additional lower-case letters or digits.
    """


_ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef = TypedDict(
    "_ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)


class ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef(
    _ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef
):
    """
    - **PolicySummary** *(dict) --*

      A structure that contains additional details about the policy.
      - **Id** *(string) --*

        The unique identifier (ID) of the policy.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-"
        followed by from 8 to 128 lower-case letters or digits.
    """


_ClientUpdatePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientUpdatePolicyResponsePolicyTypeDef",
    {"PolicySummary": ClientUpdatePolicyResponsePolicyPolicySummaryTypeDef, "Content": str},
    total=False,
)


class ClientUpdatePolicyResponsePolicyTypeDef(_ClientUpdatePolicyResponsePolicyTypeDef):
    """
    - **Policy** *(dict) --*

      A structure that contains details about the updated policy, showing the requested changes.
      - **PolicySummary** *(dict) --*

        A structure that contains additional details about the policy.
        - **Id** *(string) --*

          The unique identifier (ID) of the policy.
          The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
          "p-" followed by from 8 to 128 lower-case letters or digits.
    """


_ClientUpdatePolicyResponseTypeDef = TypedDict(
    "_ClientUpdatePolicyResponseTypeDef",
    {"Policy": ClientUpdatePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientUpdatePolicyResponseTypeDef(_ClientUpdatePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(dict) --*

        A structure that contains details about the updated policy, showing the requested changes.
        - **PolicySummary** *(dict) --*

          A structure that contains additional details about the policy.
          - **Id** *(string) --*

            The unique identifier (ID) of the policy.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
            "p-" followed by from 8 to 128 lower-case letters or digits.
    """


_ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef(
    _ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef = TypedDict(
    "_ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef",
    {"ServicePrincipal": str, "DateEnabled": datetime},
    total=False,
)


class ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef(
    _ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef
):
    """
    - *(dict) --*

      A structure that contains details of a service principal that is enabled to integrate with AWS
      Organizations.
      - **ServicePrincipal** *(string) --*

        The name of the service principal. This is typically in the form of a URL, such as: ``
        *servicename* .amazonaws.com`` .
    """


_ListAWSServiceAccessForOrganizationPaginateResponseTypeDef = TypedDict(
    "_ListAWSServiceAccessForOrganizationPaginateResponseTypeDef",
    {
        "EnabledServicePrincipals": List[
            ListAWSServiceAccessForOrganizationPaginateResponseEnabledServicePrincipalsTypeDef
        ]
    },
    total=False,
)


class ListAWSServiceAccessForOrganizationPaginateResponseTypeDef(
    _ListAWSServiceAccessForOrganizationPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EnabledServicePrincipals** *(list) --*

        A list of the service principals for the services that are enabled to integrate with your
        organization. Each principal is a structure that includes the name and the date that it was
        enabled for integration with AWS Organizations.
        - *(dict) --*

          A structure that contains details of a service principal that is enabled to integrate with
          AWS Organizations.
          - **ServicePrincipal** *(string) --*

            The name of the service principal. This is typically in the form of a URL, such as: ``
            *servicename* .amazonaws.com`` .
    """


_ListAccountsForParentPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccountsForParentPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccountsForParentPaginatePaginationConfigTypeDef(
    _ListAccountsForParentPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAccountsForParentPaginateResponseAccountsTypeDef = TypedDict(
    "_ListAccountsForParentPaginateResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": Literal["ACTIVE", "SUSPENDED"],
        "JoinedMethod": Literal["INVITED", "CREATED"],
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ListAccountsForParentPaginateResponseAccountsTypeDef(
    _ListAccountsForParentPaginateResponseAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about an AWS account that is a member of an organization.
      - **Id** *(string) --*

        The unique identifier (ID) of the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.
    """


_ListAccountsForParentPaginateResponseTypeDef = TypedDict(
    "_ListAccountsForParentPaginateResponseTypeDef",
    {"Accounts": List[ListAccountsForParentPaginateResponseAccountsTypeDef]},
    total=False,
)


class ListAccountsForParentPaginateResponseTypeDef(_ListAccountsForParentPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Accounts** *(list) --*

        A list of the accounts in the specified root or OU.
        - *(dict) --*

          Contains information about an AWS account that is a member of an organization.
          - **Id** *(string) --*

            The unique identifier (ID) of the account.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string
            requires exactly 12 digits.
    """


_ListAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccountsPaginatePaginationConfigTypeDef(_ListAccountsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAccountsPaginateResponseAccountsTypeDef = TypedDict(
    "_ListAccountsPaginateResponseAccountsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": Literal["ACTIVE", "SUSPENDED"],
        "JoinedMethod": Literal["INVITED", "CREATED"],
        "JoinedTimestamp": datetime,
    },
    total=False,
)


class ListAccountsPaginateResponseAccountsTypeDef(_ListAccountsPaginateResponseAccountsTypeDef):
    """
    - *(dict) --*

      Contains information about an AWS account that is a member of an organization.
      - **Id** *(string) --*

        The unique identifier (ID) of the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires
        exactly 12 digits.
    """


_ListAccountsPaginateResponseTypeDef = TypedDict(
    "_ListAccountsPaginateResponseTypeDef",
    {"Accounts": List[ListAccountsPaginateResponseAccountsTypeDef]},
    total=False,
)


class ListAccountsPaginateResponseTypeDef(_ListAccountsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Accounts** *(list) --*

        A list of objects in the organization.
        - *(dict) --*

          Contains information about an AWS account that is a member of an organization.
          - **Id** *(string) --*

            The unique identifier (ID) of the account.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string
            requires exactly 12 digits.
    """


_ListChildrenPaginatePaginationConfigTypeDef = TypedDict(
    "_ListChildrenPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListChildrenPaginatePaginationConfigTypeDef(_ListChildrenPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListChildrenPaginateResponseChildrenTypeDef = TypedDict(
    "_ListChildrenPaginateResponseChildrenTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"]},
    total=False,
)


class ListChildrenPaginateResponseChildrenTypeDef(_ListChildrenPaginateResponseChildrenTypeDef):
    """
    - *(dict) --*

      Contains a list of child entities, either OUs or accounts.
      - **Id** *(string) --*

        The unique identifier (ID) of this child entity.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires one
        of the following:
        * Account: A string that consists of exactly 12 digits.
        * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
        lower-case letters or digits (the ID of the root that contains the OU). This string is
        followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ListChildrenPaginateResponseTypeDef = TypedDict(
    "_ListChildrenPaginateResponseTypeDef",
    {"Children": List[ListChildrenPaginateResponseChildrenTypeDef]},
    total=False,
)


class ListChildrenPaginateResponseTypeDef(_ListChildrenPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Children** *(list) --*

        The list of children of the specified parent container.
        - *(dict) --*

          Contains a list of child entities, either OUs or accounts.
          - **Id** *(string) --*

            The unique identifier (ID) of this child entity.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires
            one of the following:
            * Account: A string that consists of exactly 12 digits.
            * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
            lower-case letters or digits (the ID of the root that contains the OU). This string is
            followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ListCreateAccountStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCreateAccountStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCreateAccountStatusPaginatePaginationConfigTypeDef(
    _ListCreateAccountStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef = TypedDict(
    "_ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "EMAIL_ALREADY_EXISTS",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "INTERNAL_FAILURE",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        ],
    },
    total=False,
)


class ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef(
    _ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef
):
    """
    - *(dict) --*

      Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an AWS
      account or an AWS GovCloud (US) account in an organization.
      - **Id** *(string) --*

        The unique identifier (ID) that references this request. You get this value from the
        response of the initial  CreateAccount request to create the account.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
        string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ListCreateAccountStatusPaginateResponseTypeDef = TypedDict(
    "_ListCreateAccountStatusPaginateResponseTypeDef",
    {
        "CreateAccountStatuses": List[
            ListCreateAccountStatusPaginateResponseCreateAccountStatusesTypeDef
        ]
    },
    total=False,
)


class ListCreateAccountStatusPaginateResponseTypeDef(
    _ListCreateAccountStatusPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **CreateAccountStatuses** *(list) --*

        A list of objects with details about the requests. Certain elements, such as the accountId
        number, are present in the output only after the account has been successfully created.
        - *(dict) --*

          Contains the status about a  CreateAccount or  CreateGovCloudAccount request to create an
          AWS account or an AWS GovCloud (US) account in an organization.
          - **Id** *(string) --*

            The unique identifier (ID) that references this request. You get this value from the
            response of the initial  CreateAccount request to create the account.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a create account request ID
            string requires "car-" followed by from 8 to 32 lower-case letters or digits.
    """


_ListHandshakesForAccountPaginateFilterTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateFilterTypeDef",
    {
        "ActionType": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "ParentHandshakeId": str,
    },
    total=False,
)


class ListHandshakesForAccountPaginateFilterTypeDef(_ListHandshakesForAccountPaginateFilterTypeDef):
    """
    Filters the handshakes that you want included in the response. The default is all types. Use the
    ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` ,
    ``ENABLE_ALL_FEATURES`` , or ``APPROVE_ALL_FEATURES`` . Alternatively, you can specify the
    ``ENABLE_ALL_FEATURES`` handshake, which generates a separate child handshake for each member
    account. When you do specify ``ParentHandshakeId`` to see only the handshakes that were
    generated by that parent request.
    - **ActionType** *(string) --*

      Specifies the type of handshake action.
      If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .
    """


_ListHandshakesForAccountPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHandshakesForAccountPaginatePaginationConfigTypeDef(
    _ListHandshakesForAccountPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef(
    _ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef
):
    pass


_ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef(
    _ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef
):
    pass


_ListHandshakesForAccountPaginateResponseHandshakesTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ListHandshakesForAccountPaginateResponseHandshakesPartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ListHandshakesForAccountPaginateResponseHandshakesResourcesTypeDef],
    },
    total=False,
)


class ListHandshakesForAccountPaginateResponseHandshakesTypeDef(
    _ListHandshakesForAccountPaginateResponseHandshakesTypeDef
):
    """
    - *(dict) --*

      Contains information that must be exchanged to securely establish a relationship between two
      accounts (an *originator* and a *recipient* ). For example, assume that a master account (the
      originator) invites another account (the recipient) to join its organization. In that case,
      the two accounts exchange information as a series of handshake requests and responses.

        **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
        days after entering that state. After that, they are deleted.
    """


_ListHandshakesForAccountPaginateResponseTypeDef = TypedDict(
    "_ListHandshakesForAccountPaginateResponseTypeDef",
    {"Handshakes": List[ListHandshakesForAccountPaginateResponseHandshakesTypeDef]},
    total=False,
)


class ListHandshakesForAccountPaginateResponseTypeDef(
    _ListHandshakesForAccountPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Handshakes** *(list) --*

        A list of  Handshake objects with details about each of the handshakes that is associated
        with the specified account.
        - *(dict) --*

          Contains information that must be exchanged to securely establish a relationship between
          two accounts (an *originator* and a *recipient* ). For example, assume that a master
          account (the originator) invites another account (the recipient) to join its organization.
          In that case, the two accounts exchange information as a series of handshake requests and
          responses.

            **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only
            30 days after entering that state. After that, they are deleted.
    """


_ListHandshakesForOrganizationPaginateFilterTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateFilterTypeDef",
    {
        "ActionType": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "ParentHandshakeId": str,
    },
    total=False,
)


class ListHandshakesForOrganizationPaginateFilterTypeDef(
    _ListHandshakesForOrganizationPaginateFilterTypeDef
):
    """
    A filter of the handshakes that you want included in the response. The default is all types. Use
    the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` ,
    ``ENABLE-ALL-FEATURES`` , or ``APPROVE-ALL-FEATURES`` . Alternatively, you can specify the
    ``ENABLE-ALL-FEATURES`` handshake, which generates a separate child handshake for each member
    account. When you do, specify the ``ParentHandshakeId`` to see only the handshakes that were
    generated by that parent request.
    - **ActionType** *(string) --*

      Specifies the type of handshake action.
      If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .
    """


_ListHandshakesForOrganizationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHandshakesForOrganizationPaginatePaginationConfigTypeDef(
    _ListHandshakesForOrganizationPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef",
    {"Id": str, "Type": Literal["ACCOUNT", "ORGANIZATION", "EMAIL"]},
    total=False,
)


class ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef(
    _ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef
):
    pass


_ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef",
    {
        "Value": str,
        "Type": Literal[
            "ACCOUNT",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "PARENT_HANDSHAKE",
        ],
        "Resources": Any,
    },
    total=False,
)


class ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef(
    _ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef
):
    pass


_ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List[ListHandshakesForOrganizationPaginateResponseHandshakesPartiesTypeDef],
        "State": Literal["REQUESTED", "OPEN", "CANCELED", "ACCEPTED", "DECLINED", "EXPIRED"],
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": Literal[
            "INVITE",
            "ENABLE_ALL_FEATURES",
            "APPROVE_ALL_FEATURES",
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
        ],
        "Resources": List[ListHandshakesForOrganizationPaginateResponseHandshakesResourcesTypeDef],
    },
    total=False,
)


class ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef(
    _ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef
):
    """
    - *(dict) --*

      Contains information that must be exchanged to securely establish a relationship between two
      accounts (an *originator* and a *recipient* ). For example, assume that a master account (the
      originator) invites another account (the recipient) to join its organization. In that case,
      the two accounts exchange information as a series of handshake requests and responses.

        **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30
        days after entering that state. After that, they are deleted.
    """


_ListHandshakesForOrganizationPaginateResponseTypeDef = TypedDict(
    "_ListHandshakesForOrganizationPaginateResponseTypeDef",
    {"Handshakes": List[ListHandshakesForOrganizationPaginateResponseHandshakesTypeDef]},
    total=False,
)


class ListHandshakesForOrganizationPaginateResponseTypeDef(
    _ListHandshakesForOrganizationPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Handshakes** *(list) --*

        A list of  Handshake objects with details about each of the handshakes that are associated
        with an organization.
        - *(dict) --*

          Contains information that must be exchanged to securely establish a relationship between
          two accounts (an *originator* and a *recipient* ). For example, assume that a master
          account (the originator) invites another account (the recipient) to join its organization.
          In that case, the two accounts exchange information as a series of handshake requests and
          responses.

            **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only
            30 days after entering that state. After that, they are deleted.
    """


_ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef(
    _ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef = TypedDict(
    "_ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef(
    _ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef
):
    """
    - *(dict) --*

      Contains details about an organizational unit (OU). An OU is a container of AWS accounts
      within a root of an organization. Policies that are attached to an OU apply to all accounts
      contained in that OU and in any child OUs.
      - **Id** *(string) --*

        The unique identifier (ID) associated with this OU.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string
        requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root
        that contains the OU). This string is followed by a second "-" dash and from 8 to 32
        additional lower-case letters or digits.
    """


_ListOrganizationalUnitsForParentPaginateResponseTypeDef = TypedDict(
    "_ListOrganizationalUnitsForParentPaginateResponseTypeDef",
    {
        "OrganizationalUnits": List[
            ListOrganizationalUnitsForParentPaginateResponseOrganizationalUnitsTypeDef
        ]
    },
    total=False,
)


class ListOrganizationalUnitsForParentPaginateResponseTypeDef(
    _ListOrganizationalUnitsForParentPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **OrganizationalUnits** *(list) --*

        A list of the OUs in the specified root or parent OU.
        - *(dict) --*

          Contains details about an organizational unit (OU). An OU is a container of AWS accounts
          within a root of an organization. Policies that are attached to an OU apply to all
          accounts contained in that OU and in any child OUs.
          - **Id** *(string) --*

            The unique identifier (ID) associated with this OU.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID
            string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of
            the root that contains the OU). This string is followed by a second "-" dash and from 8
            to 32 additional lower-case letters or digits.
    """


_ListParentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListParentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListParentsPaginatePaginationConfigTypeDef(_ListParentsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListParentsPaginateResponseParentsTypeDef = TypedDict(
    "_ListParentsPaginateResponseParentsTypeDef",
    {"Id": str, "Type": Literal["ROOT", "ORGANIZATIONAL_UNIT"]},
    total=False,
)


class ListParentsPaginateResponseParentsTypeDef(_ListParentsPaginateResponseParentsTypeDef):
    """
    - *(dict) --*

      Contains information about either a root or an organizational unit (OU) that can contain OUs
      or accounts in an organization.
      - **Id** *(string) --*

        The unique identifier (ID) of the parent entity.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one
        of the following:
        * Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or
        digits.
        * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
        lower-case letters or digits (the ID of the root that the OU is in). This string is followed
        by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ListParentsPaginateResponseTypeDef = TypedDict(
    "_ListParentsPaginateResponseTypeDef",
    {"Parents": List[ListParentsPaginateResponseParentsTypeDef]},
    total=False,
)


class ListParentsPaginateResponseTypeDef(_ListParentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Parents** *(list) --*

        A list of parents for the specified child account or OU.
        - *(dict) --*

          Contains information about either a root or an organizational unit (OU) that can contain
          OUs or accounts in an organization.
          - **Id** *(string) --*

            The unique identifier (ID) of the parent entity.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires
            one of the following:
            * Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or
            digits.
            * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
            lower-case letters or digits (the ID of the root that the OU is in). This string is
            followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ListPoliciesForTargetPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPoliciesForTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPoliciesForTargetPaginatePaginationConfigTypeDef(
    _ListPoliciesForTargetPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPoliciesForTargetPaginateResponsePoliciesTypeDef = TypedDict(
    "_ListPoliciesForTargetPaginateResponsePoliciesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)


class ListPoliciesForTargetPaginateResponsePoliciesTypeDef(
    _ListPoliciesForTargetPaginateResponsePoliciesTypeDef
):
    """
    - *(dict) --*

      Contains information about a policy, but does not include the content. To see the content of a
      policy, see  DescribePolicy .
      - **Id** *(string) --*

        The unique identifier (ID) of the policy.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-"
        followed by from 8 to 128 lower-case letters or digits.
    """


_ListPoliciesForTargetPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesForTargetPaginateResponseTypeDef",
    {"Policies": List[ListPoliciesForTargetPaginateResponsePoliciesTypeDef]},
    total=False,
)


class ListPoliciesForTargetPaginateResponseTypeDef(_ListPoliciesForTargetPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Policies** *(list) --*

        The list of policies that match the criteria in the request.
        - *(dict) --*

          Contains information about a policy, but does not include the content. To see the content
          of a policy, see  DescribePolicy .
          - **Id** *(string) --*

            The unique identifier (ID) of the policy.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
            "p-" followed by from 8 to 128 lower-case letters or digits.
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
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "AwsManaged": bool,
    },
    total=False,
)


class ListPoliciesPaginateResponsePoliciesTypeDef(_ListPoliciesPaginateResponsePoliciesTypeDef):
    """
    - *(dict) --*

      Contains information about a policy, but does not include the content. To see the content of a
      policy, see  DescribePolicy .
      - **Id** *(string) --*

        The unique identifier (ID) of the policy.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-"
        followed by from 8 to 128 lower-case letters or digits.
    """


_ListPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesPaginateResponseTypeDef",
    {"Policies": List[ListPoliciesPaginateResponsePoliciesTypeDef]},
    total=False,
)


class ListPoliciesPaginateResponseTypeDef(_ListPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Policies** *(list) --*

        A list of policies that match the filter criteria in the request. The output list doesn't
        include the policy contents. To see the content for a policy, see  DescribePolicy .
        - *(dict) --*

          Contains information about a policy, but does not include the content. To see the content
          of a policy, see  DescribePolicy .
          - **Id** *(string) --*

            The unique identifier (ID) of the policy.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires
            "p-" followed by from 8 to 128 lower-case letters or digits.
    """


_ListRootsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRootsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRootsPaginatePaginationConfigTypeDef(_ListRootsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRootsPaginateResponseRootsPolicyTypesTypeDef = TypedDict(
    "_ListRootsPaginateResponseRootsPolicyTypesTypeDef",
    {
        "Type": Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        "Status": Literal["ENABLED", "PENDING_ENABLE", "PENDING_DISABLE"],
    },
    total=False,
)


class ListRootsPaginateResponseRootsPolicyTypesTypeDef(
    _ListRootsPaginateResponseRootsPolicyTypesTypeDef
):
    pass


_ListRootsPaginateResponseRootsTypeDef = TypedDict(
    "_ListRootsPaginateResponseRootsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "PolicyTypes": List[ListRootsPaginateResponseRootsPolicyTypesTypeDef],
    },
    total=False,
)


class ListRootsPaginateResponseRootsTypeDef(_ListRootsPaginateResponseRootsTypeDef):
    """
    - *(dict) --*

      Contains details about a root. A root is a top-level parent node in the hierarchy of an
      organization that can contain organizational units (OUs) and accounts. Every root contains
      every AWS account in the organization. Each root enables the accounts to be organized in a
      different way and to have different policy types enabled for use in that root.
      - **Id** *(string) --*

        The unique identifier (ID) for the root.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-"
        followed by from 4 to 32 lower-case letters or digits.
    """


_ListRootsPaginateResponseTypeDef = TypedDict(
    "_ListRootsPaginateResponseTypeDef",
    {"Roots": List[ListRootsPaginateResponseRootsTypeDef]},
    total=False,
)


class ListRootsPaginateResponseTypeDef(_ListRootsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Roots** *(list) --*

        A list of roots that are defined in an organization.
        - *(dict) --*

          Contains details about a root. A root is a top-level parent node in the hierarchy of an
          organization that can contain organizational units (OUs) and accounts. Every root contains
          every AWS account in the organization. Each root enables the accounts to be organized in a
          different way and to have different policy types enabled for use in that root.
          - **Id** *(string) --*

            The unique identifier (ID) for the root.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires
            "r-" followed by from 4 to 32 lower-case letters or digits.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    - *(dict) --*

      A custom key-value pair associated with a resource such as an account within your
      organization.
      - **Key** *(string) --*

        The key identifier, or name, of the tag.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tags that are assigned to the resource.
        - *(dict) --*

          A custom key-value pair associated with a resource such as an account within your
          organization.
          - **Key** *(string) --*

            The key identifier, or name, of the tag.
    """


_ListTargetsForPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsForPolicyPaginatePaginationConfigTypeDef(
    _ListTargetsForPolicyPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTargetsForPolicyPaginateResponseTargetsTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginateResponseTargetsTypeDef",
    {
        "TargetId": str,
        "Arn": str,
        "Name": str,
        "Type": Literal["ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT"],
    },
    total=False,
)


class ListTargetsForPolicyPaginateResponseTargetsTypeDef(
    _ListTargetsForPolicyPaginateResponseTargetsTypeDef
):
    """
    - *(dict) --*

      Contains information about a root, OU, or account that a policy is attached to.
      - **TargetId** *(string) --*

        The unique identifier (ID) of the policy target.
        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one
        of the following:
        * Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or
        digits.
        * Account: A string that consists of exactly 12 digits.
        * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
        lower-case letters or digits (the ID of the root that the OU is in). This string is followed
        by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """


_ListTargetsForPolicyPaginateResponseTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginateResponseTypeDef",
    {"Targets": List[ListTargetsForPolicyPaginateResponseTargetsTypeDef]},
    total=False,
)


class ListTargetsForPolicyPaginateResponseTypeDef(_ListTargetsForPolicyPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Targets** *(list) --*

        A list of structures, each of which contains details about one of the entities to which the
        specified policy is attached.
        - *(dict) --*

          Contains information about a root, OU, or account that a policy is attached to.
          - **TargetId** *(string) --*

            The unique identifier (ID) of the policy target.
            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires
            one of the following:
            * Root: A string that begins with "r-" followed by from 4 to 32 lower-case letters or
            digits.
            * Account: A string that consists of exactly 12 digits.
            * Organizational unit (OU): A string that begins with "ou-" followed by from 4 to 32
            lower-case letters or digits (the ID of the root that the OU is in). This string is
            followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.
    """
