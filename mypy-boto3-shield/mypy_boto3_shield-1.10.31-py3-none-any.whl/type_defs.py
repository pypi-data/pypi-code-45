"Main interface for shield service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateProtectionResponseTypeDef",
    "ClientDescribeAttackResponseAttackAttackCountersTypeDef",
    "ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef",
    "ClientDescribeAttackResponseAttackAttackPropertiesTypeDef",
    "ClientDescribeAttackResponseAttackMitigationsTypeDef",
    "ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef",
    "ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef",
    "ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef",
    "ClientDescribeAttackResponseAttackSubResourcesTypeDef",
    "ClientDescribeAttackResponseAttackTypeDef",
    "ClientDescribeAttackResponseTypeDef",
    "ClientDescribeDrtAccessResponseTypeDef",
    "ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef",
    "ClientDescribeEmergencyContactSettingsResponseTypeDef",
    "ClientDescribeProtectionResponseProtectionTypeDef",
    "ClientDescribeProtectionResponseTypeDef",
    "ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef",
    "ClientDescribeSubscriptionResponseSubscriptionTypeDef",
    "ClientDescribeSubscriptionResponseTypeDef",
    "ClientGetSubscriptionStateResponseTypeDef",
    "ClientListAttacksEndTimeTypeDef",
    "ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef",
    "ClientListAttacksResponseAttackSummariesTypeDef",
    "ClientListAttacksResponseTypeDef",
    "ClientListAttacksStartTimeTypeDef",
    "ClientListProtectionsResponseProtectionsTypeDef",
    "ClientListProtectionsResponseTypeDef",
    "ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef",
    "ListAttacksPaginateEndTimeTypeDef",
    "ListAttacksPaginatePaginationConfigTypeDef",
    "ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef",
    "ListAttacksPaginateResponseAttackSummariesTypeDef",
    "ListAttacksPaginateResponseTypeDef",
    "ListAttacksPaginateStartTimeTypeDef",
    "ListProtectionsPaginatePaginationConfigTypeDef",
    "ListProtectionsPaginateResponseProtectionsTypeDef",
    "ListProtectionsPaginateResponseTypeDef",
)


_ClientCreateProtectionResponseTypeDef = TypedDict(
    "_ClientCreateProtectionResponseTypeDef", {"ProtectionId": str}, total=False
)


class ClientCreateProtectionResponseTypeDef(_ClientCreateProtectionResponseTypeDef):
    """
    - *(dict) --*

      - **ProtectionId** *(string) --*

        The unique identifier (ID) for the  Protection object that is created.
    """


_ClientDescribeAttackResponseAttackAttackCountersTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackAttackCountersTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)


class ClientDescribeAttackResponseAttackAttackCountersTypeDef(
    _ClientDescribeAttackResponseAttackAttackCountersTypeDef
):
    pass


_ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)


class ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef(
    _ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef
):
    pass


_ClientDescribeAttackResponseAttackAttackPropertiesTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackAttackPropertiesTypeDef",
    {
        "AttackLayer": Literal["NETWORK", "APPLICATION"],
        "AttackPropertyIdentifier": Literal[
            "DESTINATION_URL",
            "REFERRER",
            "SOURCE_ASN",
            "SOURCE_COUNTRY",
            "SOURCE_IP_ADDRESS",
            "SOURCE_USER_AGENT",
            "WORDPRESS_PINGBACK_REFLECTOR",
            "WORDPRESS_PINGBACK_SOURCE",
        ],
        "TopContributors": List[
            ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef
        ],
        "Unit": Literal["BITS", "BYTES", "PACKETS", "REQUESTS"],
        "Total": int,
    },
    total=False,
)


class ClientDescribeAttackResponseAttackAttackPropertiesTypeDef(
    _ClientDescribeAttackResponseAttackAttackPropertiesTypeDef
):
    pass


_ClientDescribeAttackResponseAttackMitigationsTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackMitigationsTypeDef", {"MitigationName": str}, total=False
)


class ClientDescribeAttackResponseAttackMitigationsTypeDef(
    _ClientDescribeAttackResponseAttackMitigationsTypeDef
):
    pass


_ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)


class ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef(
    _ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef
):
    pass


_ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef",
    {
        "VectorType": str,
        "VectorCounters": List[
            ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef(
    _ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef
):
    pass


_ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)


class ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef(
    _ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef
):
    pass


_ClientDescribeAttackResponseAttackSubResourcesTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackSubResourcesTypeDef",
    {
        "Type": Literal["IP", "URL"],
        "Id": str,
        "AttackVectors": List[ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef],
        "Counters": List[ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef],
    },
    total=False,
)


class ClientDescribeAttackResponseAttackSubResourcesTypeDef(
    _ClientDescribeAttackResponseAttackSubResourcesTypeDef
):
    pass


_ClientDescribeAttackResponseAttackTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "SubResources": List[ClientDescribeAttackResponseAttackSubResourcesTypeDef],
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackCounters": List[ClientDescribeAttackResponseAttackAttackCountersTypeDef],
        "AttackProperties": List[ClientDescribeAttackResponseAttackAttackPropertiesTypeDef],
        "Mitigations": List[ClientDescribeAttackResponseAttackMitigationsTypeDef],
    },
    total=False,
)


class ClientDescribeAttackResponseAttackTypeDef(_ClientDescribeAttackResponseAttackTypeDef):
    """
    - **Attack** *(dict) --*

      The attack that is described.
      - **AttackId** *(string) --*

        The unique identifier (ID) of the attack.
    """


_ClientDescribeAttackResponseTypeDef = TypedDict(
    "_ClientDescribeAttackResponseTypeDef",
    {"Attack": ClientDescribeAttackResponseAttackTypeDef},
    total=False,
)


class ClientDescribeAttackResponseTypeDef(_ClientDescribeAttackResponseTypeDef):
    """
    - *(dict) --*

      - **Attack** *(dict) --*

        The attack that is described.
        - **AttackId** *(string) --*

          The unique identifier (ID) of the attack.
    """


_ClientDescribeDrtAccessResponseTypeDef = TypedDict(
    "_ClientDescribeDrtAccessResponseTypeDef",
    {"RoleArn": str, "LogBucketList": List[str]},
    total=False,
)


class ClientDescribeDrtAccessResponseTypeDef(_ClientDescribeDrtAccessResponseTypeDef):
    """
    - *(dict) --*

      - **RoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the role the DRT used to access your AWS account.
    """


_ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef = TypedDict(
    "_ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef",
    {"EmailAddress": str},
    total=False,
)


class ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef(
    _ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef
):
    """
    - *(dict) --*

      Contact information that the DRT can use to contact you during a suspected attack.
      - **EmailAddress** *(string) --*

        An email address that the DRT can use to contact you during a suspected attack.
    """


_ClientDescribeEmergencyContactSettingsResponseTypeDef = TypedDict(
    "_ClientDescribeEmergencyContactSettingsResponseTypeDef",
    {
        "EmergencyContactList": List[
            ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeEmergencyContactSettingsResponseTypeDef(
    _ClientDescribeEmergencyContactSettingsResponseTypeDef
):
    """
    - *(dict) --*

      - **EmergencyContactList** *(list) --*

        A list of email addresses that the DRT can use to contact you during a suspected attack.
        - *(dict) --*

          Contact information that the DRT can use to contact you during a suspected attack.
          - **EmailAddress** *(string) --*

            An email address that the DRT can use to contact you during a suspected attack.
    """


_ClientDescribeProtectionResponseProtectionTypeDef = TypedDict(
    "_ClientDescribeProtectionResponseProtectionTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str},
    total=False,
)


class ClientDescribeProtectionResponseProtectionTypeDef(
    _ClientDescribeProtectionResponseProtectionTypeDef
):
    """
    - **Protection** *(dict) --*

      The  Protection object that is described.
      - **Id** *(string) --*

        The unique identifier (ID) of the protection.
    """


_ClientDescribeProtectionResponseTypeDef = TypedDict(
    "_ClientDescribeProtectionResponseTypeDef",
    {"Protection": ClientDescribeProtectionResponseProtectionTypeDef},
    total=False,
)


class ClientDescribeProtectionResponseTypeDef(_ClientDescribeProtectionResponseTypeDef):
    """
    - *(dict) --*

      - **Protection** *(dict) --*

        The  Protection object that is described.
        - **Id** *(string) --*

          The unique identifier (ID) of the protection.
    """


_ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef = TypedDict(
    "_ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef",
    {"Type": str, "Max": int},
    total=False,
)


class ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef(
    _ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef
):
    pass


_ClientDescribeSubscriptionResponseSubscriptionTypeDef = TypedDict(
    "_ClientDescribeSubscriptionResponseSubscriptionTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "TimeCommitmentInSeconds": int,
        "AutoRenew": Literal["ENABLED", "DISABLED"],
        "Limits": List[ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef],
    },
    total=False,
)


class ClientDescribeSubscriptionResponseSubscriptionTypeDef(
    _ClientDescribeSubscriptionResponseSubscriptionTypeDef
):
    """
    - **Subscription** *(dict) --*

      The AWS Shield Advanced subscription details for an account.
      - **StartTime** *(datetime) --*

        The start time of the subscription, in Unix time in seconds. For more information see
        `timestamp
        <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
    """


_ClientDescribeSubscriptionResponseTypeDef = TypedDict(
    "_ClientDescribeSubscriptionResponseTypeDef",
    {"Subscription": ClientDescribeSubscriptionResponseSubscriptionTypeDef},
    total=False,
)


class ClientDescribeSubscriptionResponseTypeDef(_ClientDescribeSubscriptionResponseTypeDef):
    """
    - *(dict) --*

      - **Subscription** *(dict) --*

        The AWS Shield Advanced subscription details for an account.
        - **StartTime** *(datetime) --*

          The start time of the subscription, in Unix time in seconds. For more information see
          `timestamp
          <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__
          .
    """


_ClientGetSubscriptionStateResponseTypeDef = TypedDict(
    "_ClientGetSubscriptionStateResponseTypeDef",
    {"SubscriptionState": Literal["ACTIVE", "INACTIVE"]},
    total=False,
)


class ClientGetSubscriptionStateResponseTypeDef(_ClientGetSubscriptionStateResponseTypeDef):
    """
    - *(dict) --*

      - **SubscriptionState** *(string) --*

        The status of the subscription.
    """


_ClientListAttacksEndTimeTypeDef = TypedDict(
    "_ClientListAttacksEndTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)


class ClientListAttacksEndTimeTypeDef(_ClientListAttacksEndTimeTypeDef):
    """
    The end of the time period for the attacks. This is a ``timestamp`` type. The sample request
    above indicates a ``number`` type because the default used by WAF is Unix time in seconds.
    However any valid `timestamp format
    <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is
    allowed.
    - **FromInclusive** *(datetime) --*

      The start time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
    """


_ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef = TypedDict(
    "_ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef",
    {"VectorType": str},
    total=False,
)


class ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef(
    _ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef
):
    pass


_ClientListAttacksResponseAttackSummariesTypeDef = TypedDict(
    "_ClientListAttacksResponseAttackSummariesTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackVectors": List[ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef],
    },
    total=False,
)


class ClientListAttacksResponseAttackSummariesTypeDef(
    _ClientListAttacksResponseAttackSummariesTypeDef
):
    """
    - *(dict) --*

      Summarizes all DDoS attacks for a specified time period.
      - **AttackId** *(string) --*

        The unique identifier (ID) of the attack.
    """


_ClientListAttacksResponseTypeDef = TypedDict(
    "_ClientListAttacksResponseTypeDef",
    {"AttackSummaries": List[ClientListAttacksResponseAttackSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListAttacksResponseTypeDef(_ClientListAttacksResponseTypeDef):
    """
    - *(dict) --*

      - **AttackSummaries** *(list) --*

        The attack information for the specified time range.
        - *(dict) --*

          Summarizes all DDoS attacks for a specified time period.
          - **AttackId** *(string) --*

            The unique identifier (ID) of the attack.
    """


_ClientListAttacksStartTimeTypeDef = TypedDict(
    "_ClientListAttacksStartTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)


class ClientListAttacksStartTimeTypeDef(_ClientListAttacksStartTimeTypeDef):
    """
    The start of the time period for the attacks. This is a ``timestamp`` type. The sample request
    above indicates a ``number`` type because the default used by WAF is Unix time in seconds.
    However any valid `timestamp format
    <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is
    allowed.
    - **FromInclusive** *(datetime) --*

      The start time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
    """


_ClientListProtectionsResponseProtectionsTypeDef = TypedDict(
    "_ClientListProtectionsResponseProtectionsTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str},
    total=False,
)


class ClientListProtectionsResponseProtectionsTypeDef(
    _ClientListProtectionsResponseProtectionsTypeDef
):
    """
    - *(dict) --*

      An object that represents a resource that is under DDoS protection.
      - **Id** *(string) --*

        The unique identifier (ID) of the protection.
    """


_ClientListProtectionsResponseTypeDef = TypedDict(
    "_ClientListProtectionsResponseTypeDef",
    {"Protections": List[ClientListProtectionsResponseProtectionsTypeDef], "NextToken": str},
    total=False,
)


class ClientListProtectionsResponseTypeDef(_ClientListProtectionsResponseTypeDef):
    """
    - *(dict) --*

      - **Protections** *(list) --*

        The array of enabled  Protection objects.
        - *(dict) --*

          An object that represents a resource that is under DDoS protection.
          - **Id** *(string) --*

            The unique identifier (ID) of the protection.
    """


_ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef = TypedDict(
    "_ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef", {"EmailAddress": str}
)


class ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef(
    _ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef
):
    """
    - *(dict) --*

      Contact information that the DRT can use to contact you during a suspected attack.
      - **EmailAddress** *(string) --***[REQUIRED]**

        An email address that the DRT can use to contact you during a suspected attack.
    """


_ListAttacksPaginateEndTimeTypeDef = TypedDict(
    "_ListAttacksPaginateEndTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)


class ListAttacksPaginateEndTimeTypeDef(_ListAttacksPaginateEndTimeTypeDef):
    """
    The end of the time period for the attacks. This is a ``timestamp`` type. The sample request
    above indicates a ``number`` type because the default used by WAF is Unix time in seconds.
    However any valid `timestamp format
    <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is
    allowed.
    - **FromInclusive** *(datetime) --*

      The start time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
    """


_ListAttacksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttacksPaginatePaginationConfigTypeDef(_ListAttacksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef = TypedDict(
    "_ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef",
    {"VectorType": str},
    total=False,
)


class ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef(
    _ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef
):
    pass


_ListAttacksPaginateResponseAttackSummariesTypeDef = TypedDict(
    "_ListAttacksPaginateResponseAttackSummariesTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackVectors": List[ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef],
    },
    total=False,
)


class ListAttacksPaginateResponseAttackSummariesTypeDef(
    _ListAttacksPaginateResponseAttackSummariesTypeDef
):
    """
    - *(dict) --*

      Summarizes all DDoS attacks for a specified time period.
      - **AttackId** *(string) --*

        The unique identifier (ID) of the attack.
    """


_ListAttacksPaginateResponseTypeDef = TypedDict(
    "_ListAttacksPaginateResponseTypeDef",
    {"AttackSummaries": List[ListAttacksPaginateResponseAttackSummariesTypeDef]},
    total=False,
)


class ListAttacksPaginateResponseTypeDef(_ListAttacksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **AttackSummaries** *(list) --*

        The attack information for the specified time range.
        - *(dict) --*

          Summarizes all DDoS attacks for a specified time period.
          - **AttackId** *(string) --*

            The unique identifier (ID) of the attack.
    """


_ListAttacksPaginateStartTimeTypeDef = TypedDict(
    "_ListAttacksPaginateStartTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)


class ListAttacksPaginateStartTimeTypeDef(_ListAttacksPaginateStartTimeTypeDef):
    """
    The start of the time period for the attacks. This is a ``timestamp`` type. The sample request
    above indicates a ``number`` type because the default used by WAF is Unix time in seconds.
    However any valid `timestamp format
    <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is
    allowed.
    - **FromInclusive** *(datetime) --*

      The start time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
    """


_ListProtectionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProtectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProtectionsPaginatePaginationConfigTypeDef(
    _ListProtectionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListProtectionsPaginateResponseProtectionsTypeDef = TypedDict(
    "_ListProtectionsPaginateResponseProtectionsTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str},
    total=False,
)


class ListProtectionsPaginateResponseProtectionsTypeDef(
    _ListProtectionsPaginateResponseProtectionsTypeDef
):
    """
    - *(dict) --*

      An object that represents a resource that is under DDoS protection.
      - **Id** *(string) --*

        The unique identifier (ID) of the protection.
    """


_ListProtectionsPaginateResponseTypeDef = TypedDict(
    "_ListProtectionsPaginateResponseTypeDef",
    {"Protections": List[ListProtectionsPaginateResponseProtectionsTypeDef]},
    total=False,
)


class ListProtectionsPaginateResponseTypeDef(_ListProtectionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Protections** *(list) --*

        The array of enabled  Protection objects.
        - *(dict) --*

          An object that represents a resource that is under DDoS protection.
          - **Id** *(string) --*

            The unique identifier (ID) of the protection.
    """
