"Main interface for shield service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateProtectionResponseTypeDef = TypedDict(
    "ClientCreateProtectionResponseTypeDef", {"ProtectionId": str}, total=False
)

ClientDescribeAttackResponseAttackAttackCountersTypeDef = TypedDict(
    "ClientDescribeAttackResponseAttackAttackCountersTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)

ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef = TypedDict(
    "ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)

ClientDescribeAttackResponseAttackAttackPropertiesTypeDef = TypedDict(
    "ClientDescribeAttackResponseAttackAttackPropertiesTypeDef",
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

ClientDescribeAttackResponseAttackMitigationsTypeDef = TypedDict(
    "ClientDescribeAttackResponseAttackMitigationsTypeDef", {"MitigationName": str}, total=False
)

ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef = TypedDict(
    "ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)

ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef = TypedDict(
    "ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef",
    {
        "VectorType": str,
        "VectorCounters": List[
            ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef
        ],
    },
    total=False,
)

ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef = TypedDict(
    "ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)

ClientDescribeAttackResponseAttackSubResourcesTypeDef = TypedDict(
    "ClientDescribeAttackResponseAttackSubResourcesTypeDef",
    {
        "Type": Literal["IP", "URL"],
        "Id": str,
        "AttackVectors": List[ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef],
        "Counters": List[ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef],
    },
    total=False,
)

ClientDescribeAttackResponseAttackTypeDef = TypedDict(
    "ClientDescribeAttackResponseAttackTypeDef",
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

ClientDescribeAttackResponseTypeDef = TypedDict(
    "ClientDescribeAttackResponseTypeDef",
    {"Attack": ClientDescribeAttackResponseAttackTypeDef},
    total=False,
)

ClientDescribeDrtAccessResponseTypeDef = TypedDict(
    "ClientDescribeDrtAccessResponseTypeDef",
    {"RoleArn": str, "LogBucketList": List[str]},
    total=False,
)

ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef = TypedDict(
    "ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef",
    {"EmailAddress": str},
    total=False,
)

ClientDescribeEmergencyContactSettingsResponseTypeDef = TypedDict(
    "ClientDescribeEmergencyContactSettingsResponseTypeDef",
    {
        "EmergencyContactList": List[
            ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef
        ]
    },
    total=False,
)

ClientDescribeProtectionResponseProtectionTypeDef = TypedDict(
    "ClientDescribeProtectionResponseProtectionTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str},
    total=False,
)

ClientDescribeProtectionResponseTypeDef = TypedDict(
    "ClientDescribeProtectionResponseTypeDef",
    {"Protection": ClientDescribeProtectionResponseProtectionTypeDef},
    total=False,
)

ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef = TypedDict(
    "ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef",
    {"Type": str, "Max": int},
    total=False,
)

ClientDescribeSubscriptionResponseSubscriptionTypeDef = TypedDict(
    "ClientDescribeSubscriptionResponseSubscriptionTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "TimeCommitmentInSeconds": int,
        "AutoRenew": Literal["ENABLED", "DISABLED"],
        "Limits": List[ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef],
    },
    total=False,
)

ClientDescribeSubscriptionResponseTypeDef = TypedDict(
    "ClientDescribeSubscriptionResponseTypeDef",
    {"Subscription": ClientDescribeSubscriptionResponseSubscriptionTypeDef},
    total=False,
)

ClientGetSubscriptionStateResponseTypeDef = TypedDict(
    "ClientGetSubscriptionStateResponseTypeDef",
    {"SubscriptionState": Literal["ACTIVE", "INACTIVE"]},
    total=False,
)

ClientListAttacksEndTimeTypeDef = TypedDict(
    "ClientListAttacksEndTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)

ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef = TypedDict(
    "ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef", {"VectorType": str}, total=False
)

ClientListAttacksResponseAttackSummariesTypeDef = TypedDict(
    "ClientListAttacksResponseAttackSummariesTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackVectors": List[ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef],
    },
    total=False,
)

ClientListAttacksResponseTypeDef = TypedDict(
    "ClientListAttacksResponseTypeDef",
    {"AttackSummaries": List[ClientListAttacksResponseAttackSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListAttacksStartTimeTypeDef = TypedDict(
    "ClientListAttacksStartTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)

ClientListProtectionsResponseProtectionsTypeDef = TypedDict(
    "ClientListProtectionsResponseProtectionsTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str},
    total=False,
)

ClientListProtectionsResponseTypeDef = TypedDict(
    "ClientListProtectionsResponseTypeDef",
    {"Protections": List[ClientListProtectionsResponseProtectionsTypeDef], "NextToken": str},
    total=False,
)

ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef = TypedDict(
    "ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef", {"EmailAddress": str}
)

ListAttacksPaginateEndTimeTypeDef = TypedDict(
    "ListAttacksPaginateEndTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)

ListAttacksPaginatePaginationConfigTypeDef = TypedDict(
    "ListAttacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef = TypedDict(
    "ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef",
    {"VectorType": str},
    total=False,
)

ListAttacksPaginateResponseAttackSummariesTypeDef = TypedDict(
    "ListAttacksPaginateResponseAttackSummariesTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackVectors": List[ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef],
    },
    total=False,
)

ListAttacksPaginateResponseTypeDef = TypedDict(
    "ListAttacksPaginateResponseTypeDef",
    {"AttackSummaries": List[ListAttacksPaginateResponseAttackSummariesTypeDef]},
    total=False,
)

ListAttacksPaginateStartTimeTypeDef = TypedDict(
    "ListAttacksPaginateStartTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)

ListProtectionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListProtectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListProtectionsPaginateResponseProtectionsTypeDef = TypedDict(
    "ListProtectionsPaginateResponseProtectionsTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str},
    total=False,
)

ListProtectionsPaginateResponseTypeDef = TypedDict(
    "ListProtectionsPaginateResponseTypeDef",
    {"Protections": List[ListProtectionsPaginateResponseProtectionsTypeDef]},
    total=False,
)
