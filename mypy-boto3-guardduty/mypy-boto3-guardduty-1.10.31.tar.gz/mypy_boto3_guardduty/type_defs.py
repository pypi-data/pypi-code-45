"Main interface for guardduty service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateDetectorResponseTypeDef",
    "ClientCreateFilterFindingCriteriaCriterionTypeDef",
    "ClientCreateFilterFindingCriteriaTypeDef",
    "ClientCreateFilterResponseTypeDef",
    "ClientCreateIpSetResponseTypeDef",
    "ClientCreateMembersAccountDetailsTypeDef",
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    "ClientCreateMembersResponseTypeDef",
    "ClientCreatePublishingDestinationDestinationPropertiesTypeDef",
    "ClientCreatePublishingDestinationResponseTypeDef",
    "ClientCreateThreatIntelSetResponseTypeDef",
    "ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeclineInvitationsResponseTypeDef",
    "ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    "ClientDeleteInvitationsResponseTypeDef",
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    "ClientDeleteMembersResponseTypeDef",
    "ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef",
    "ClientDescribePublishingDestinationResponseTypeDef",
    "ClientDisassociateMembersResponseUnprocessedAccountsTypeDef",
    "ClientDisassociateMembersResponseTypeDef",
    "ClientGetDetectorResponseTypeDef",
    "ClientGetFilterResponseFindingCriteriaCriterionTypeDef",
    "ClientGetFilterResponseFindingCriteriaTypeDef",
    "ClientGetFilterResponseTypeDef",
    "ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef",
    "ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef",
    "ClientGetFindingsResponseFindingsResourceTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceActionTypeDef",
    "ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef",
    "ClientGetFindingsResponseFindingsServiceEvidenceTypeDef",
    "ClientGetFindingsResponseFindingsServiceTypeDef",
    "ClientGetFindingsResponseFindingsTypeDef",
    "ClientGetFindingsResponseTypeDef",
    "ClientGetFindingsSortCriteriaTypeDef",
    "ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef",
    "ClientGetFindingsStatisticsFindingCriteriaTypeDef",
    "ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef",
    "ClientGetFindingsStatisticsResponseTypeDef",
    "ClientGetInvitationsCountResponseTypeDef",
    "ClientGetIpSetResponseTypeDef",
    "ClientGetMasterAccountResponseMasterTypeDef",
    "ClientGetMasterAccountResponseTypeDef",
    "ClientGetMembersResponseMembersTypeDef",
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    "ClientGetMembersResponseTypeDef",
    "ClientGetThreatIntelSetResponseTypeDef",
    "ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    "ClientInviteMembersResponseTypeDef",
    "ClientListDetectorsResponseTypeDef",
    "ClientListFiltersResponseTypeDef",
    "ClientListFindingsFindingCriteriaCriterionTypeDef",
    "ClientListFindingsFindingCriteriaTypeDef",
    "ClientListFindingsResponseTypeDef",
    "ClientListFindingsSortCriteriaTypeDef",
    "ClientListInvitationsResponseInvitationsTypeDef",
    "ClientListInvitationsResponseTypeDef",
    "ClientListIpSetsResponseTypeDef",
    "ClientListMembersResponseMembersTypeDef",
    "ClientListMembersResponseTypeDef",
    "ClientListPublishingDestinationsResponseDestinationsTypeDef",
    "ClientListPublishingDestinationsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListThreatIntelSetsResponseTypeDef",
    "ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef",
    "ClientStartMonitoringMembersResponseTypeDef",
    "ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef",
    "ClientStopMonitoringMembersResponseTypeDef",
    "ClientUpdateFilterFindingCriteriaCriterionTypeDef",
    "ClientUpdateFilterFindingCriteriaTypeDef",
    "ClientUpdateFilterResponseTypeDef",
    "ClientUpdatePublishingDestinationDestinationPropertiesTypeDef",
    "ListDetectorsPaginatePaginationConfigTypeDef",
    "ListDetectorsPaginateResponseTypeDef",
    "ListFiltersPaginatePaginationConfigTypeDef",
    "ListFiltersPaginateResponseTypeDef",
    "ListFindingsPaginateFindingCriteriaCriterionTypeDef",
    "ListFindingsPaginateFindingCriteriaTypeDef",
    "ListFindingsPaginatePaginationConfigTypeDef",
    "ListFindingsPaginateResponseTypeDef",
    "ListFindingsPaginateSortCriteriaTypeDef",
    "ListIPSetsPaginatePaginationConfigTypeDef",
    "ListIPSetsPaginateResponseTypeDef",
    "ListInvitationsPaginatePaginationConfigTypeDef",
    "ListInvitationsPaginateResponseInvitationsTypeDef",
    "ListInvitationsPaginateResponseTypeDef",
    "ListMembersPaginatePaginationConfigTypeDef",
    "ListMembersPaginateResponseMembersTypeDef",
    "ListMembersPaginateResponseTypeDef",
    "ListThreatIntelSetsPaginatePaginationConfigTypeDef",
    "ListThreatIntelSetsPaginateResponseTypeDef",
)


_ClientCreateDetectorResponseTypeDef = TypedDict(
    "_ClientCreateDetectorResponseTypeDef", {"DetectorId": str}, total=False
)


class ClientCreateDetectorResponseTypeDef(_ClientCreateDetectorResponseTypeDef):
    """
    - *(dict) --*

      - **DetectorId** *(string) --*

        The unique ID of the created detector.
    """


_ClientCreateFilterFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientCreateFilterFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientCreateFilterFindingCriteriaCriterionTypeDef(
    _ClientCreateFilterFindingCriteriaCriterionTypeDef
):
    pass


_ClientCreateFilterFindingCriteriaTypeDef = TypedDict(
    "_ClientCreateFilterFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientCreateFilterFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ClientCreateFilterFindingCriteriaTypeDef(_ClientCreateFilterFindingCriteriaTypeDef):
    """
    Represents the criteria to be used in the filter for querying findings.
    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when
      querying findings.
      - *(string) --*

        - *(dict) --*

          Contains information about the condition.
          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for
            findings.
            - *(string) --*
    """


_ClientCreateFilterResponseTypeDef = TypedDict(
    "_ClientCreateFilterResponseTypeDef", {"Name": str}, total=False
)


class ClientCreateFilterResponseTypeDef(_ClientCreateFilterResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the successfully created filter.
    """


_ClientCreateIpSetResponseTypeDef = TypedDict(
    "_ClientCreateIpSetResponseTypeDef", {"IpSetId": str}, total=False
)


class ClientCreateIpSetResponseTypeDef(_ClientCreateIpSetResponseTypeDef):
    """
    - *(dict) --*

      - **IpSetId** *(string) --*

        The ID of the IPSet resource.
    """


_RequiredClientCreateMembersAccountDetailsTypeDef = TypedDict(
    "_RequiredClientCreateMembersAccountDetailsTypeDef", {"AccountId": str}
)
_OptionalClientCreateMembersAccountDetailsTypeDef = TypedDict(
    "_OptionalClientCreateMembersAccountDetailsTypeDef", {"Email": str}, total=False
)


class ClientCreateMembersAccountDetailsTypeDef(
    _RequiredClientCreateMembersAccountDetailsTypeDef,
    _OptionalClientCreateMembersAccountDetailsTypeDef,
):
    """
    - *(dict) --*

      Contains information about the account.
      - **AccountId** *(string) --***[REQUIRED]**

        Member account ID.
    """


_ClientCreateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientCreateMembersResponseUnprocessedAccountsTypeDef(
    _ClientCreateMembersResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the accounts that were not processed.
      - **AccountId** *(string) --*

        AWS Account ID.
    """


_ClientCreateMembersResponseTypeDef = TypedDict(
    "_ClientCreateMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientCreateMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientCreateMembersResponseTypeDef(_ClientCreateMembersResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of objects containing the unprocessed account and a result string explaining why it
        was unprocessed.
        - *(dict) --*

          Contains information about the accounts that were not processed.
          - **AccountId** *(string) --*

            AWS Account ID.
    """


_ClientCreatePublishingDestinationDestinationPropertiesTypeDef = TypedDict(
    "_ClientCreatePublishingDestinationDestinationPropertiesTypeDef",
    {"DestinationArn": str, "KmsKeyArn": str},
    total=False,
)


class ClientCreatePublishingDestinationDestinationPropertiesTypeDef(
    _ClientCreatePublishingDestinationDestinationPropertiesTypeDef
):
    """
    Properties of the publishing destination, including the ARNs for the destination and the KMS key
    used for encryption.
    - **DestinationArn** *(string) --*

      The ARN of the resource to publish to.
    """


_ClientCreatePublishingDestinationResponseTypeDef = TypedDict(
    "_ClientCreatePublishingDestinationResponseTypeDef", {"DestinationId": str}, total=False
)


class ClientCreatePublishingDestinationResponseTypeDef(
    _ClientCreatePublishingDestinationResponseTypeDef
):
    """
    - *(dict) --*

      - **DestinationId** *(string) --*

        The ID of the publishing destination created.
    """


_ClientCreateThreatIntelSetResponseTypeDef = TypedDict(
    "_ClientCreateThreatIntelSetResponseTypeDef", {"ThreatIntelSetId": str}, total=False
)


class ClientCreateThreatIntelSetResponseTypeDef(_ClientCreateThreatIntelSetResponseTypeDef):
    """
    - *(dict) --*

      - **ThreatIntelSetId** *(string) --*

        The ID of the ThreatIntelSet resource.
    """


_ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef(
    _ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the accounts that were not processed.
      - **AccountId** *(string) --*

        AWS Account ID.
    """


_ClientDeclineInvitationsResponseTypeDef = TypedDict(
    "_ClientDeclineInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientDeclineInvitationsResponseTypeDef(_ClientDeclineInvitationsResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of objects containing the unprocessed account and a result string explaining why it
        was unprocessed.
        - *(dict) --*

          Contains information about the accounts that were not processed.
          - **AccountId** *(string) --*

            AWS Account ID.
    """


_ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef(
    _ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the accounts that were not processed.
      - **AccountId** *(string) --*

        AWS Account ID.
    """


_ClientDeleteInvitationsResponseTypeDef = TypedDict(
    "_ClientDeleteInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientDeleteInvitationsResponseTypeDef(_ClientDeleteInvitationsResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of objects containing the unprocessed account and a result string explaining why it
        was unprocessed.
        - *(dict) --*

          Contains information about the accounts that were not processed.
          - **AccountId** *(string) --*

            AWS Account ID.
    """


_ClientDeleteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientDeleteMembersResponseUnprocessedAccountsTypeDef(
    _ClientDeleteMembersResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the accounts that were not processed.
      - **AccountId** *(string) --*

        AWS Account ID.
    """


_ClientDeleteMembersResponseTypeDef = TypedDict(
    "_ClientDeleteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientDeleteMembersResponseTypeDef(_ClientDeleteMembersResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        The accounts that could not be processed.
        - *(dict) --*

          Contains information about the accounts that were not processed.
          - **AccountId** *(string) --*

            AWS Account ID.
    """


_ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef = TypedDict(
    "_ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef",
    {"DestinationArn": str, "KmsKeyArn": str},
    total=False,
)


class ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef(
    _ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef
):
    pass


_ClientDescribePublishingDestinationResponseTypeDef = TypedDict(
    "_ClientDescribePublishingDestinationResponseTypeDef",
    {
        "DestinationId": str,
        "DestinationType": str,
        "Status": Literal[
            "PENDING_VERIFICATION",
            "PUBLISHING",
            "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY",
            "STOPPED",
        ],
        "PublishingFailureStartTimestamp": int,
        "DestinationProperties": ClientDescribePublishingDestinationResponseDestinationPropertiesTypeDef,
    },
    total=False,
)


class ClientDescribePublishingDestinationResponseTypeDef(
    _ClientDescribePublishingDestinationResponseTypeDef
):
    """
    - *(dict) --*

      - **DestinationId** *(string) --*

        The ID of the publishing destination.
    """


_ClientDisassociateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientDisassociateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientDisassociateMembersResponseUnprocessedAccountsTypeDef(
    _ClientDisassociateMembersResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the accounts that were not processed.
      - **AccountId** *(string) --*

        AWS Account ID.
    """


_ClientDisassociateMembersResponseTypeDef = TypedDict(
    "_ClientDisassociateMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDisassociateMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientDisassociateMembersResponseTypeDef(_ClientDisassociateMembersResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of objects containing the unprocessed account and a result string explaining why it
        was unprocessed.
        - *(dict) --*

          Contains information about the accounts that were not processed.
          - **AccountId** *(string) --*

            AWS Account ID.
    """


_ClientGetDetectorResponseTypeDef = TypedDict(
    "_ClientGetDetectorResponseTypeDef",
    {
        "CreatedAt": str,
        "FindingPublishingFrequency": Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"],
        "ServiceRole": str,
        "Status": Literal["ENABLED", "DISABLED"],
        "UpdatedAt": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDetectorResponseTypeDef(_ClientGetDetectorResponseTypeDef):
    """
    - *(dict) --*

      - **CreatedAt** *(string) --*

        Detector creation timestamp.
    """


_ClientGetFilterResponseFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientGetFilterResponseFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientGetFilterResponseFindingCriteriaCriterionTypeDef(
    _ClientGetFilterResponseFindingCriteriaCriterionTypeDef
):
    pass


_ClientGetFilterResponseFindingCriteriaTypeDef = TypedDict(
    "_ClientGetFilterResponseFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientGetFilterResponseFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ClientGetFilterResponseFindingCriteriaTypeDef(_ClientGetFilterResponseFindingCriteriaTypeDef):
    pass


_ClientGetFilterResponseTypeDef = TypedDict(
    "_ClientGetFilterResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": Literal["NOOP", "ARCHIVE"],
        "Rank": int,
        "FindingCriteria": ClientGetFilterResponseFindingCriteriaTypeDef,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetFilterResponseTypeDef(_ClientGetFilterResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the filter.
    """


_ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef",
    {"AccessKeyId": str, "PrincipalId": str, "UserName": str, "UserType": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef(
    _ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef",
    {"Arn": str, "Id": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef",
    {"PrivateDnsName": str, "PrivateIpAddress": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef",
    {"GroupId": str, "GroupName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef",
    {
        "Ipv6Addresses": List[str],
        "NetworkInterfaceId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesPrivateIpAddressesTypeDef
        ],
        "PublicDnsName": str,
        "PublicIp": str,
        "SecurityGroups": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesSecurityGroupsTypeDef
        ],
        "SubnetId": str,
        "VpcId": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef",
    {"Code": str, "ProductType": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef",
    {
        "AvailabilityZone": str,
        "IamInstanceProfile": ClientGetFindingsResponseFindingsResourceInstanceDetailsIamInstanceProfileTypeDef,
        "ImageDescription": str,
        "ImageId": str,
        "InstanceId": str,
        "InstanceState": str,
        "InstanceType": str,
        "LaunchTime": str,
        "NetworkInterfaces": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsNetworkInterfacesTypeDef
        ],
        "Platform": str,
        "ProductCodes": List[
            ClientGetFindingsResponseFindingsResourceInstanceDetailsProductCodesTypeDef
        ],
        "Tags": List[ClientGetFindingsResponseFindingsResourceInstanceDetailsTagsTypeDef],
    },
    total=False,
)


class ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef(
    _ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsResourceTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsResourceTypeDef",
    {
        "AccessKeyDetails": ClientGetFindingsResponseFindingsResourceAccessKeyDetailsTypeDef,
        "InstanceDetails": ClientGetFindingsResponseFindingsResourceInstanceDetailsTypeDef,
        "ResourceType": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsResourceTypeDef(
    _ClientGetFindingsResponseFindingsResourceTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef",
    {"Domain": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef",
    {"CityName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef",
    {"CountryCode": str, "CountryName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef",
    {"Lat": float, "Lon": float},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef",
    {"Asn": str, "AsnOrg": str, "Isp": str, "Org": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef",
    {
        "City": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCityTypeDef,
        "Country": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsCountryTypeDef,
        "GeoLocation": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsGeoLocationTypeDef,
        "IpAddressV4": str,
        "Organization": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsOrganizationTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef",
    {
        "Api": str,
        "CallerType": str,
        "DomainDetails": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionDomainDetailsTypeDef,
        "RemoteIpDetails": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionRemoteIpDetailsTypeDef,
        "ServiceName": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef",
    {"Domain": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef",
    {"Port": int, "PortName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef",
    {"CityName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef",
    {"CountryCode": str, "CountryName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef",
    {"Lat": float, "Lon": float},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef",
    {"Asn": str, "AsnOrg": str, "Isp": str, "Org": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef",
    {
        "City": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCityTypeDef,
        "Country": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsCountryTypeDef,
        "GeoLocation": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsGeoLocationTypeDef,
        "IpAddressV4": str,
        "Organization": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsOrganizationTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef",
    {"Port": int, "PortName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef",
    {
        "Blocked": bool,
        "ConnectionDirection": str,
        "LocalPortDetails": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionLocalPortDetailsTypeDef,
        "Protocol": str,
        "RemoteIpDetails": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemoteIpDetailsTypeDef,
        "RemotePortDetails": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionRemotePortDetailsTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef",
    {"Port": int, "PortName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef",
    {"CityName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef",
    {"CountryCode": str, "CountryName": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef",
    {"Lat": float, "Lon": float},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef",
    {"Asn": str, "AsnOrg": str, "Isp": str, "Org": str},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef",
    {
        "City": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCityTypeDef,
        "Country": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsCountryTypeDef,
        "GeoLocation": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsGeoLocationTypeDef,
        "IpAddressV4": str,
        "Organization": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsOrganizationTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef",
    {
        "LocalPortDetails": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsLocalPortDetailsTypeDef,
        "RemoteIpDetails": ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsRemoteIpDetailsTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef",
    {
        "Blocked": bool,
        "PortProbeDetails": List[
            ClientGetFindingsResponseFindingsServiceActionPortProbeActionPortProbeDetailsTypeDef
        ],
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceActionTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceActionTypeDef",
    {
        "ActionType": str,
        "AwsApiCallAction": ClientGetFindingsResponseFindingsServiceActionAwsApiCallActionTypeDef,
        "DnsRequestAction": ClientGetFindingsResponseFindingsServiceActionDnsRequestActionTypeDef,
        "NetworkConnectionAction": ClientGetFindingsResponseFindingsServiceActionNetworkConnectionActionTypeDef,
        "PortProbeAction": ClientGetFindingsResponseFindingsServiceActionPortProbeActionTypeDef,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceActionTypeDef(
    _ClientGetFindingsResponseFindingsServiceActionTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef",
    {"ThreatListName": str, "ThreatNames": List[str]},
    total=False,
)


class ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef(
    _ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceEvidenceTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceEvidenceTypeDef",
    {
        "ThreatIntelligenceDetails": List[
            ClientGetFindingsResponseFindingsServiceEvidenceThreatIntelligenceDetailsTypeDef
        ]
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceEvidenceTypeDef(
    _ClientGetFindingsResponseFindingsServiceEvidenceTypeDef
):
    pass


_ClientGetFindingsResponseFindingsServiceTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsServiceTypeDef",
    {
        "Action": ClientGetFindingsResponseFindingsServiceActionTypeDef,
        "Evidence": ClientGetFindingsResponseFindingsServiceEvidenceTypeDef,
        "Archived": bool,
        "Count": int,
        "DetectorId": str,
        "EventFirstSeen": str,
        "EventLastSeen": str,
        "ResourceRole": str,
        "ServiceName": str,
        "UserFeedback": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsServiceTypeDef(
    _ClientGetFindingsResponseFindingsServiceTypeDef
):
    pass


_ClientGetFindingsResponseFindingsTypeDef = TypedDict(
    "_ClientGetFindingsResponseFindingsTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "Confidence": float,
        "CreatedAt": str,
        "Description": str,
        "Id": str,
        "Partition": str,
        "Region": str,
        "Resource": ClientGetFindingsResponseFindingsResourceTypeDef,
        "SchemaVersion": str,
        "Service": ClientGetFindingsResponseFindingsServiceTypeDef,
        "Severity": float,
        "Title": str,
        "Type": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ClientGetFindingsResponseFindingsTypeDef(_ClientGetFindingsResponseFindingsTypeDef):
    """
    - *(dict) --*

      Contains information about the finding, which is generated when abnormal or suspicious
      activity is detected.
      - **AccountId** *(string) --*

        The ID of the account in which the finding was generated.
    """


_ClientGetFindingsResponseTypeDef = TypedDict(
    "_ClientGetFindingsResponseTypeDef",
    {"Findings": List[ClientGetFindingsResponseFindingsTypeDef]},
    total=False,
)


class ClientGetFindingsResponseTypeDef(_ClientGetFindingsResponseTypeDef):
    """
    - *(dict) --*

      - **Findings** *(list) --*

        A list of findings.
        - *(dict) --*

          Contains information about the finding, which is generated when abnormal or suspicious
          activity is detected.
          - **AccountId** *(string) --*

            The ID of the account in which the finding was generated.
    """


_ClientGetFindingsSortCriteriaTypeDef = TypedDict(
    "_ClientGetFindingsSortCriteriaTypeDef",
    {"AttributeName": str, "OrderBy": Literal["ASC", "DESC"]},
    total=False,
)


class ClientGetFindingsSortCriteriaTypeDef(_ClientGetFindingsSortCriteriaTypeDef):
    """
    Represents the criteria used for sorting findings.
    - **AttributeName** *(string) --*

      Represents the finding attribute (for example, accountId) by which to sort findings.
    """


_ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef(
    _ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef
):
    pass


_ClientGetFindingsStatisticsFindingCriteriaTypeDef = TypedDict(
    "_ClientGetFindingsStatisticsFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientGetFindingsStatisticsFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ClientGetFindingsStatisticsFindingCriteriaTypeDef(
    _ClientGetFindingsStatisticsFindingCriteriaTypeDef
):
    """
    Represents the criteria used for querying findings.
    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when
      querying findings.
      - *(string) --*

        - *(dict) --*

          Contains information about the condition.
          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for
            findings.
            - *(string) --*
    """


_ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef = TypedDict(
    "_ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef",
    {"CountBySeverity": Dict[str, int]},
    total=False,
)


class ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef(
    _ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef
):
    """
    - **FindingStatistics** *(dict) --*

      Finding statistics object.
      - **CountBySeverity** *(dict) --*

        Represents a map of severity to count statistic for a set of findings
        - *(string) --*

          - *(integer) --*
    """


_ClientGetFindingsStatisticsResponseTypeDef = TypedDict(
    "_ClientGetFindingsStatisticsResponseTypeDef",
    {"FindingStatistics": ClientGetFindingsStatisticsResponseFindingStatisticsTypeDef},
    total=False,
)


class ClientGetFindingsStatisticsResponseTypeDef(_ClientGetFindingsStatisticsResponseTypeDef):
    """
    - *(dict) --*

      - **FindingStatistics** *(dict) --*

        Finding statistics object.
        - **CountBySeverity** *(dict) --*

          Represents a map of severity to count statistic for a set of findings
          - *(string) --*

            - *(integer) --*
    """


_ClientGetInvitationsCountResponseTypeDef = TypedDict(
    "_ClientGetInvitationsCountResponseTypeDef", {"InvitationsCount": int}, total=False
)


class ClientGetInvitationsCountResponseTypeDef(_ClientGetInvitationsCountResponseTypeDef):
    """
    - *(dict) --*

      - **InvitationsCount** *(integer) --*

        The number of received invitations.
    """


_ClientGetIpSetResponseTypeDef = TypedDict(
    "_ClientGetIpSetResponseTypeDef",
    {
        "Name": str,
        "Format": Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        "Location": str,
        "Status": Literal[
            "INACTIVE", "ACTIVATING", "ACTIVE", "DEACTIVATING", "ERROR", "DELETE_PENDING", "DELETED"
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetIpSetResponseTypeDef(_ClientGetIpSetResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The user friendly name for the IPSet.
    """


_ClientGetMasterAccountResponseMasterTypeDef = TypedDict(
    "_ClientGetMasterAccountResponseMasterTypeDef",
    {"AccountId": str, "InvitationId": str, "RelationshipStatus": str, "InvitedAt": str},
    total=False,
)


class ClientGetMasterAccountResponseMasterTypeDef(_ClientGetMasterAccountResponseMasterTypeDef):
    """
    - **Master** *(dict) --*

      Master account details.
      - **AccountId** *(string) --*

        The ID of the account used as the Master account.
    """


_ClientGetMasterAccountResponseTypeDef = TypedDict(
    "_ClientGetMasterAccountResponseTypeDef",
    {"Master": ClientGetMasterAccountResponseMasterTypeDef},
    total=False,
)


class ClientGetMasterAccountResponseTypeDef(_ClientGetMasterAccountResponseTypeDef):
    """
    - *(dict) --*

      - **Master** *(dict) --*

        Master account details.
        - **AccountId** *(string) --*

          The ID of the account used as the Master account.
    """


_ClientGetMembersResponseMembersTypeDef = TypedDict(
    "_ClientGetMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "DetectorId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ClientGetMembersResponseMembersTypeDef(_ClientGetMembersResponseMembersTypeDef):
    """
    - *(dict) --*

      Continas information about the member account
      - **AccountId** *(string) --*

        Member account ID.
    """


_ClientGetMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientGetMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientGetMembersResponseUnprocessedAccountsTypeDef(
    _ClientGetMembersResponseUnprocessedAccountsTypeDef
):
    pass


_ClientGetMembersResponseTypeDef = TypedDict(
    "_ClientGetMembersResponseTypeDef",
    {
        "Members": List[ClientGetMembersResponseMembersTypeDef],
        "UnprocessedAccounts": List[ClientGetMembersResponseUnprocessedAccountsTypeDef],
    },
    total=False,
)


class ClientGetMembersResponseTypeDef(_ClientGetMembersResponseTypeDef):
    """
    - *(dict) --*

      - **Members** *(list) --*

        A list of members.
        - *(dict) --*

          Continas information about the member account
          - **AccountId** *(string) --*

            Member account ID.
    """


_ClientGetThreatIntelSetResponseTypeDef = TypedDict(
    "_ClientGetThreatIntelSetResponseTypeDef",
    {
        "Name": str,
        "Format": Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        "Location": str,
        "Status": Literal[
            "INACTIVE", "ACTIVATING", "ACTIVE", "DEACTIVATING", "ERROR", "DELETE_PENDING", "DELETED"
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetThreatIntelSetResponseTypeDef(_ClientGetThreatIntelSetResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        A user-friendly ThreatIntelSet name that is displayed in all finding generated by activity
        that involves IP addresses included in this ThreatIntelSet.
    """


_ClientInviteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientInviteMembersResponseUnprocessedAccountsTypeDef(
    _ClientInviteMembersResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the accounts that were not processed.
      - **AccountId** *(string) --*

        AWS Account ID.
    """


_ClientInviteMembersResponseTypeDef = TypedDict(
    "_ClientInviteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientInviteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientInviteMembersResponseTypeDef(_ClientInviteMembersResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of objects containing the unprocessed account and a result string explaining why it
        was unprocessed.
        - *(dict) --*

          Contains information about the accounts that were not processed.
          - **AccountId** *(string) --*

            AWS Account ID.
    """


_ClientListDetectorsResponseTypeDef = TypedDict(
    "_ClientListDetectorsResponseTypeDef", {"DetectorIds": List[str], "NextToken": str}, total=False
)


class ClientListDetectorsResponseTypeDef(_ClientListDetectorsResponseTypeDef):
    """
    - *(dict) --*

      - **DetectorIds** *(list) --*

        A list of detector Ids.
        - *(string) --*
    """


_ClientListFiltersResponseTypeDef = TypedDict(
    "_ClientListFiltersResponseTypeDef", {"FilterNames": List[str], "NextToken": str}, total=False
)


class ClientListFiltersResponseTypeDef(_ClientListFiltersResponseTypeDef):
    """
    - *(dict) --*

      - **FilterNames** *(list) --*

        A list of filter names
        - *(string) --*
    """


_ClientListFindingsFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientListFindingsFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientListFindingsFindingCriteriaCriterionTypeDef(
    _ClientListFindingsFindingCriteriaCriterionTypeDef
):
    pass


_ClientListFindingsFindingCriteriaTypeDef = TypedDict(
    "_ClientListFindingsFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientListFindingsFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ClientListFindingsFindingCriteriaTypeDef(_ClientListFindingsFindingCriteriaTypeDef):
    """
    Represents the criteria used for querying findings. Valid values include:
    * JSON field name
    * accountId
    * region
    * confidence
    * id
    * resource.accessKeyDetails.accessKeyId
    * resource.accessKeyDetails.principalId
    * resource.accessKeyDetails.userName
    * resource.accessKeyDetails.userType
    * resource.instanceDetails.iamInstanceProfile.id
    * resource.instanceDetails.imageId
    * resource.instanceDetails.instanceId
    * resource.instanceDetails.networkInterfaces.ipv6Addresses
    * resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress
    * resource.instanceDetails.networkInterfaces.publicDnsName
    * resource.instanceDetails.networkInterfaces.publicIp
    * resource.instanceDetails.networkInterfaces.securityGroups.groupId
    * resource.instanceDetails.networkInterfaces.securityGroups.groupName
    * resource.instanceDetails.networkInterfaces.subnetId
    * resource.instanceDetails.networkInterfaces.vpcId
    * resource.instanceDetails.tags.key
    * resource.instanceDetails.tags.value
    * resource.resourceType
    * service.action.actionType
    * service.action.awsApiCallAction.api
    * service.action.awsApiCallAction.callerType
    * service.action.awsApiCallAction.remoteIpDetails.city.cityName
    * service.action.awsApiCallAction.remoteIpDetails.country.countryName
    * service.action.awsApiCallAction.remoteIpDetails.ipAddressV4
    * service.action.awsApiCallAction.remoteIpDetails.organization.asn
    * service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg
    * service.action.awsApiCallAction.serviceName
    * service.action.dnsRequestAction.domain
    * service.action.networkConnectionAction.blocked
    * service.action.networkConnectionAction.connectionDirection
    * service.action.networkConnectionAction.localPortDetails.port
    * service.action.networkConnectionAction.protocol
    * service.action.networkConnectionAction.remoteIpDetails.city.cityName
    * service.action.networkConnectionAction.remoteIpDetails.country.countryName
    * service.action.networkConnectionAction.remoteIpDetails.ipAddressV4
    * service.action.networkConnectionAction.remoteIpDetails.organization.asn
    * service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg
    * service.action.networkConnectionAction.remotePortDetails.port
    * service.additionalInfo.threatListName
    * service.archived When this attribute is set to 'true', only archived findings are listed. When
    it's set to 'false', only unarchived findings are listed. When this attribute is not set, all
    existing findings are listed.
    * service.resourceRole
    * severity
    * type
    * updatedAt Type: Timestamp in Unix Epoch millisecond format: 1486685375000
    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when
      querying findings.
      - *(string) --*

        - *(dict) --*

          Contains information about the condition.
          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for
            findings.
            - *(string) --*
    """


_ClientListFindingsResponseTypeDef = TypedDict(
    "_ClientListFindingsResponseTypeDef", {"FindingIds": List[str], "NextToken": str}, total=False
)


class ClientListFindingsResponseTypeDef(_ClientListFindingsResponseTypeDef):
    """
    - *(dict) --*

      - **FindingIds** *(list) --*

        The IDs of the findings you are listing.
        - *(string) --*
    """


_ClientListFindingsSortCriteriaTypeDef = TypedDict(
    "_ClientListFindingsSortCriteriaTypeDef",
    {"AttributeName": str, "OrderBy": Literal["ASC", "DESC"]},
    total=False,
)


class ClientListFindingsSortCriteriaTypeDef(_ClientListFindingsSortCriteriaTypeDef):
    """
    Represents the criteria used for sorting findings.
    - **AttributeName** *(string) --*

      Represents the finding attribute (for example, accountId) by which to sort findings.
    """


_ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "_ClientListInvitationsResponseInvitationsTypeDef",
    {"AccountId": str, "InvitationId": str, "RelationshipStatus": str, "InvitedAt": str},
    total=False,
)


class ClientListInvitationsResponseInvitationsTypeDef(
    _ClientListInvitationsResponseInvitationsTypeDef
):
    """
    - *(dict) --*

      Contains information about the invitation to become a member account.
      - **AccountId** *(string) --*

        The ID of the account from which the invitations was sent.
    """


_ClientListInvitationsResponseTypeDef = TypedDict(
    "_ClientListInvitationsResponseTypeDef",
    {"Invitations": List[ClientListInvitationsResponseInvitationsTypeDef], "NextToken": str},
    total=False,
)


class ClientListInvitationsResponseTypeDef(_ClientListInvitationsResponseTypeDef):
    """
    - *(dict) --*

      - **Invitations** *(list) --*

        A list of invitation descriptions.
        - *(dict) --*

          Contains information about the invitation to become a member account.
          - **AccountId** *(string) --*

            The ID of the account from which the invitations was sent.
    """


_ClientListIpSetsResponseTypeDef = TypedDict(
    "_ClientListIpSetsResponseTypeDef", {"IpSetIds": List[str], "NextToken": str}, total=False
)


class ClientListIpSetsResponseTypeDef(_ClientListIpSetsResponseTypeDef):
    """
    - *(dict) --*

      - **IpSetIds** *(list) --*

        The IDs of the IPSet resources.
        - *(string) --*
    """


_ClientListMembersResponseMembersTypeDef = TypedDict(
    "_ClientListMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "DetectorId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ClientListMembersResponseMembersTypeDef(_ClientListMembersResponseMembersTypeDef):
    """
    - *(dict) --*

      Continas information about the member account
      - **AccountId** *(string) --*

        Member account ID.
    """


_ClientListMembersResponseTypeDef = TypedDict(
    "_ClientListMembersResponseTypeDef",
    {"Members": List[ClientListMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)


class ClientListMembersResponseTypeDef(_ClientListMembersResponseTypeDef):
    """
    - *(dict) --*

      - **Members** *(list) --*

        A list of members.
        - *(dict) --*

          Continas information about the member account
          - **AccountId** *(string) --*

            Member account ID.
    """


_ClientListPublishingDestinationsResponseDestinationsTypeDef = TypedDict(
    "_ClientListPublishingDestinationsResponseDestinationsTypeDef",
    {
        "DestinationId": str,
        "DestinationType": str,
        "Status": Literal[
            "PENDING_VERIFICATION",
            "PUBLISHING",
            "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY",
            "STOPPED",
        ],
    },
    total=False,
)


class ClientListPublishingDestinationsResponseDestinationsTypeDef(
    _ClientListPublishingDestinationsResponseDestinationsTypeDef
):
    """
    - *(dict) --*

      Contains information about a publishing destination, including the ID, type, and status.
      - **DestinationId** *(string) --*

        The unique ID of the publishing destination.
    """


_ClientListPublishingDestinationsResponseTypeDef = TypedDict(
    "_ClientListPublishingDestinationsResponseTypeDef",
    {
        "Destinations": List[ClientListPublishingDestinationsResponseDestinationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListPublishingDestinationsResponseTypeDef(
    _ClientListPublishingDestinationsResponseTypeDef
):
    """
    - *(dict) --*

      - **Destinations** *(list) --*

        A ``Destinations`` obect that includes information about each publishing destination
        returned.
        - *(dict) --*

          Contains information about a publishing destination, including the ID, type, and status.
          - **DestinationId** *(string) --*

            The unique ID of the publishing destination.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The tags associated with the resource.
        - *(string) --*

          - *(string) --*
    """


_ClientListThreatIntelSetsResponseTypeDef = TypedDict(
    "_ClientListThreatIntelSetsResponseTypeDef",
    {"ThreatIntelSetIds": List[str], "NextToken": str},
    total=False,
)


class ClientListThreatIntelSetsResponseTypeDef(_ClientListThreatIntelSetsResponseTypeDef):
    """
    - *(dict) --*

      - **ThreatIntelSetIds** *(list) --*

        The IDs of the ThreatIntelSet resources.
        - *(string) --*
    """


_ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef(
    _ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the accounts that were not processed.
      - **AccountId** *(string) --*

        AWS Account ID.
    """


_ClientStartMonitoringMembersResponseTypeDef = TypedDict(
    "_ClientStartMonitoringMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientStartMonitoringMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientStartMonitoringMembersResponseTypeDef(_ClientStartMonitoringMembersResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of objects containing the unprocessed account and a result string explaining why it
        was unprocessed.
        - *(dict) --*

          Contains information about the accounts that were not processed.
          - **AccountId** *(string) --*

            AWS Account ID.
    """


_ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "_ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "Result": str},
    total=False,
)


class ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef(
    _ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the accounts that were not processed.
      - **AccountId** *(string) --*

        AWS Account ID.
    """


_ClientStopMonitoringMembersResponseTypeDef = TypedDict(
    "_ClientStopMonitoringMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientStopMonitoringMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)


class ClientStopMonitoringMembersResponseTypeDef(_ClientStopMonitoringMembersResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedAccounts** *(list) --*

        A list of objects containing the unprocessed account and a result string explaining why it
        was unprocessed.
        - *(dict) --*

          Contains information about the accounts that were not processed.
          - **AccountId** *(string) --*

            AWS Account ID.
    """


_ClientUpdateFilterFindingCriteriaCriterionTypeDef = TypedDict(
    "_ClientUpdateFilterFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ClientUpdateFilterFindingCriteriaCriterionTypeDef(
    _ClientUpdateFilterFindingCriteriaCriterionTypeDef
):
    pass


_ClientUpdateFilterFindingCriteriaTypeDef = TypedDict(
    "_ClientUpdateFilterFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ClientUpdateFilterFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ClientUpdateFilterFindingCriteriaTypeDef(_ClientUpdateFilterFindingCriteriaTypeDef):
    """
    Represents the criteria to be used in the filter for querying findings.
    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when
      querying findings.
      - *(string) --*

        - *(dict) --*

          Contains information about the condition.
          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for
            findings.
            - *(string) --*
    """


_ClientUpdateFilterResponseTypeDef = TypedDict(
    "_ClientUpdateFilterResponseTypeDef", {"Name": str}, total=False
)


class ClientUpdateFilterResponseTypeDef(_ClientUpdateFilterResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the filter.
    """


_ClientUpdatePublishingDestinationDestinationPropertiesTypeDef = TypedDict(
    "_ClientUpdatePublishingDestinationDestinationPropertiesTypeDef",
    {"DestinationArn": str, "KmsKeyArn": str},
    total=False,
)


class ClientUpdatePublishingDestinationDestinationPropertiesTypeDef(
    _ClientUpdatePublishingDestinationDestinationPropertiesTypeDef
):
    """
    A ``DestinationProperties`` object that includes the ``DestinationArn`` and ``KmsKeyArn`` of the
    publishing destination.
    - **DestinationArn** *(string) --*

      The ARN of the resource to publish to.
    """


_ListDetectorsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDetectorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDetectorsPaginatePaginationConfigTypeDef(_ListDetectorsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDetectorsPaginateResponseTypeDef = TypedDict(
    "_ListDetectorsPaginateResponseTypeDef", {"DetectorIds": List[str]}, total=False
)


class ListDetectorsPaginateResponseTypeDef(_ListDetectorsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DetectorIds** *(list) --*

        A list of detector Ids.
        - *(string) --*
    """


_ListFiltersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFiltersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFiltersPaginatePaginationConfigTypeDef(_ListFiltersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFiltersPaginateResponseTypeDef = TypedDict(
    "_ListFiltersPaginateResponseTypeDef", {"FilterNames": List[str]}, total=False
)


class ListFiltersPaginateResponseTypeDef(_ListFiltersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **FilterNames** *(list) --*

        A list of filter names
        - *(string) --*
    """


_ListFindingsPaginateFindingCriteriaCriterionTypeDef = TypedDict(
    "_ListFindingsPaginateFindingCriteriaCriterionTypeDef",
    {
        "Eq": List[str],
        "Neq": List[str],
        "Gt": int,
        "Gte": int,
        "Lt": int,
        "Lte": int,
        "Equals": List[str],
        "NotEquals": List[str],
        "GreaterThan": int,
        "GreaterThanOrEqual": int,
        "LessThan": int,
        "LessThanOrEqual": int,
    },
    total=False,
)


class ListFindingsPaginateFindingCriteriaCriterionTypeDef(
    _ListFindingsPaginateFindingCriteriaCriterionTypeDef
):
    pass


_ListFindingsPaginateFindingCriteriaTypeDef = TypedDict(
    "_ListFindingsPaginateFindingCriteriaTypeDef",
    {"Criterion": Dict[str, ListFindingsPaginateFindingCriteriaCriterionTypeDef]},
    total=False,
)


class ListFindingsPaginateFindingCriteriaTypeDef(_ListFindingsPaginateFindingCriteriaTypeDef):
    """
    Represents the criteria used for querying findings. Valid values include:
    * JSON field name
    * accountId
    * region
    * confidence
    * id
    * resource.accessKeyDetails.accessKeyId
    * resource.accessKeyDetails.principalId
    * resource.accessKeyDetails.userName
    * resource.accessKeyDetails.userType
    * resource.instanceDetails.iamInstanceProfile.id
    * resource.instanceDetails.imageId
    * resource.instanceDetails.instanceId
    * resource.instanceDetails.networkInterfaces.ipv6Addresses
    * resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress
    * resource.instanceDetails.networkInterfaces.publicDnsName
    * resource.instanceDetails.networkInterfaces.publicIp
    * resource.instanceDetails.networkInterfaces.securityGroups.groupId
    * resource.instanceDetails.networkInterfaces.securityGroups.groupName
    * resource.instanceDetails.networkInterfaces.subnetId
    * resource.instanceDetails.networkInterfaces.vpcId
    * resource.instanceDetails.tags.key
    * resource.instanceDetails.tags.value
    * resource.resourceType
    * service.action.actionType
    * service.action.awsApiCallAction.api
    * service.action.awsApiCallAction.callerType
    * service.action.awsApiCallAction.remoteIpDetails.city.cityName
    * service.action.awsApiCallAction.remoteIpDetails.country.countryName
    * service.action.awsApiCallAction.remoteIpDetails.ipAddressV4
    * service.action.awsApiCallAction.remoteIpDetails.organization.asn
    * service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg
    * service.action.awsApiCallAction.serviceName
    * service.action.dnsRequestAction.domain
    * service.action.networkConnectionAction.blocked
    * service.action.networkConnectionAction.connectionDirection
    * service.action.networkConnectionAction.localPortDetails.port
    * service.action.networkConnectionAction.protocol
    * service.action.networkConnectionAction.remoteIpDetails.city.cityName
    * service.action.networkConnectionAction.remoteIpDetails.country.countryName
    * service.action.networkConnectionAction.remoteIpDetails.ipAddressV4
    * service.action.networkConnectionAction.remoteIpDetails.organization.asn
    * service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg
    * service.action.networkConnectionAction.remotePortDetails.port
    * service.additionalInfo.threatListName
    * service.archived When this attribute is set to 'true', only archived findings are listed. When
    it's set to 'false', only unarchived findings are listed. When this attribute is not set, all
    existing findings are listed.
    * service.resourceRole
    * severity
    * type
    * updatedAt Type: Timestamp in Unix Epoch millisecond format: 1486685375000
    - **Criterion** *(dict) --*

      Represents a map of finding properties that match specified conditions and values when
      querying findings.
      - *(string) --*

        - *(dict) --*

          Contains information about the condition.
          - **Eq** *(list) --*

            Represents the equal condition to be applied to a single field when querying for
            findings.
            - *(string) --*
    """


_ListFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFindingsPaginatePaginationConfigTypeDef(_ListFindingsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFindingsPaginateResponseTypeDef = TypedDict(
    "_ListFindingsPaginateResponseTypeDef", {"FindingIds": List[str]}, total=False
)


class ListFindingsPaginateResponseTypeDef(_ListFindingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **FindingIds** *(list) --*

        The IDs of the findings you are listing.
        - *(string) --*
    """


_ListFindingsPaginateSortCriteriaTypeDef = TypedDict(
    "_ListFindingsPaginateSortCriteriaTypeDef",
    {"AttributeName": str, "OrderBy": Literal["ASC", "DESC"]},
    total=False,
)


class ListFindingsPaginateSortCriteriaTypeDef(_ListFindingsPaginateSortCriteriaTypeDef):
    """
    Represents the criteria used for sorting findings.
    - **AttributeName** *(string) --*

      Represents the finding attribute (for example, accountId) by which to sort findings.
    """


_ListIPSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIPSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIPSetsPaginatePaginationConfigTypeDef(_ListIPSetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListIPSetsPaginateResponseTypeDef = TypedDict(
    "_ListIPSetsPaginateResponseTypeDef", {"IpSetIds": List[str]}, total=False
)


class ListIPSetsPaginateResponseTypeDef(_ListIPSetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **IpSetIds** *(list) --*

        The IDs of the IPSet resources.
        - *(string) --*
    """


_ListInvitationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInvitationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInvitationsPaginatePaginationConfigTypeDef(
    _ListInvitationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListInvitationsPaginateResponseInvitationsTypeDef = TypedDict(
    "_ListInvitationsPaginateResponseInvitationsTypeDef",
    {"AccountId": str, "InvitationId": str, "RelationshipStatus": str, "InvitedAt": str},
    total=False,
)


class ListInvitationsPaginateResponseInvitationsTypeDef(
    _ListInvitationsPaginateResponseInvitationsTypeDef
):
    """
    - *(dict) --*

      Contains information about the invitation to become a member account.
      - **AccountId** *(string) --*

        The ID of the account from which the invitations was sent.
    """


_ListInvitationsPaginateResponseTypeDef = TypedDict(
    "_ListInvitationsPaginateResponseTypeDef",
    {"Invitations": List[ListInvitationsPaginateResponseInvitationsTypeDef]},
    total=False,
)


class ListInvitationsPaginateResponseTypeDef(_ListInvitationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Invitations** *(list) --*

        A list of invitation descriptions.
        - *(dict) --*

          Contains information about the invitation to become a member account.
          - **AccountId** *(string) --*

            The ID of the account from which the invitations was sent.
    """


_ListMembersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMembersPaginatePaginationConfigTypeDef(_ListMembersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMembersPaginateResponseMembersTypeDef = TypedDict(
    "_ListMembersPaginateResponseMembersTypeDef",
    {
        "AccountId": str,
        "DetectorId": str,
        "MasterId": str,
        "Email": str,
        "RelationshipStatus": str,
        "InvitedAt": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ListMembersPaginateResponseMembersTypeDef(_ListMembersPaginateResponseMembersTypeDef):
    """
    - *(dict) --*

      Continas information about the member account
      - **AccountId** *(string) --*

        Member account ID.
    """


_ListMembersPaginateResponseTypeDef = TypedDict(
    "_ListMembersPaginateResponseTypeDef",
    {"Members": List[ListMembersPaginateResponseMembersTypeDef]},
    total=False,
)


class ListMembersPaginateResponseTypeDef(_ListMembersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Members** *(list) --*

        A list of members.
        - *(dict) --*

          Continas information about the member account
          - **AccountId** *(string) --*

            Member account ID.
    """


_ListThreatIntelSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThreatIntelSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThreatIntelSetsPaginatePaginationConfigTypeDef(
    _ListThreatIntelSetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListThreatIntelSetsPaginateResponseTypeDef = TypedDict(
    "_ListThreatIntelSetsPaginateResponseTypeDef", {"ThreatIntelSetIds": List[str]}, total=False
)


class ListThreatIntelSetsPaginateResponseTypeDef(_ListThreatIntelSetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ThreatIntelSetIds** *(list) --*

        The IDs of the ThreatIntelSet resources.
        - *(string) --*
    """
