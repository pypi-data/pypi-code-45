"Main interface for securityhub service type defs"
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


ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef = TypedDict(
    "ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)

ClientBatchDisableStandardsResponseTypeDef = TypedDict(
    "ClientBatchDisableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            ClientBatchDisableStandardsResponseStandardsSubscriptionsTypeDef
        ]
    },
    total=False,
)

ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef = TypedDict(
    "ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)

ClientBatchEnableStandardsResponseTypeDef = TypedDict(
    "ClientBatchEnableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            ClientBatchEnableStandardsResponseStandardsSubscriptionsTypeDef
        ]
    },
    total=False,
)

ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef = TypedDict(
    "ClientBatchEnableStandardsStandardsSubscriptionRequestsTypeDef",
    {"StandardsArn": str, "StandardsInput": Dict[str, str]},
    total=False,
)

ClientBatchImportFindingsFindingsComplianceTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsComplianceTypeDef",
    {"Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"]},
    total=False,
)

ClientBatchImportFindingsFindingsMalwareTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsMalwareTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)

ClientBatchImportFindingsFindingsNetworkTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsNetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsNoteTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsNoteTypeDef",
    {"Text": str, "UpdatedBy": str, "UpdatedAt": str},
    total=False,
)

ClientBatchImportFindingsFindingsProcessTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsProcessTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsRelatedFindingsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsRelatedFindingsTypeDef",
    {"ProductArn": str, "Id": str},
    total=False,
)

ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef",
    {"Text": str, "Url": str},
    total=False,
)

ClientBatchImportFindingsFindingsRemediationTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsRemediationTypeDef",
    {"Recommendation": ClientBatchImportFindingsFindingsRemediationRecommendationTypeDef},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    {"UserName": str, "Status": Literal["Active", "Inactive"], "CreatedAt": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef",
    {"OwnerId": str, "OwnerName": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)

ClientBatchImportFindingsFindingsResourcesDetailsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesDetailsTypeDef",
    {
        "AwsEc2Instance": ClientBatchImportFindingsFindingsResourcesDetailsAwsEc2InstanceTypeDef,
        "AwsS3Bucket": ClientBatchImportFindingsFindingsResourcesDetailsAwsS3BucketTypeDef,
        "AwsIamAccessKey": ClientBatchImportFindingsFindingsResourcesDetailsAwsIamAccessKeyTypeDef,
        "Container": ClientBatchImportFindingsFindingsResourcesDetailsContainerTypeDef,
        "Other": Dict[str, str],
    },
    total=False,
)

ClientBatchImportFindingsFindingsResourcesTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsResourcesTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "Tags": Dict[str, str],
        "Details": ClientBatchImportFindingsFindingsResourcesDetailsTypeDef,
    },
    total=False,
)

ClientBatchImportFindingsFindingsSeverityTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsSeverityTypeDef",
    {"Product": float, "Normalized": int},
    total=False,
)

ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)

ClientBatchImportFindingsFindingsTypeDef = TypedDict(
    "ClientBatchImportFindingsFindingsTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": ClientBatchImportFindingsFindingsSeverityTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Title": str,
        "Description": str,
        "Remediation": ClientBatchImportFindingsFindingsRemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[ClientBatchImportFindingsFindingsMalwareTypeDef],
        "Network": ClientBatchImportFindingsFindingsNetworkTypeDef,
        "Process": ClientBatchImportFindingsFindingsProcessTypeDef,
        "ThreatIntelIndicators": List[
            ClientBatchImportFindingsFindingsThreatIntelIndicatorsTypeDef
        ],
        "Resources": List[ClientBatchImportFindingsFindingsResourcesTypeDef],
        "Compliance": ClientBatchImportFindingsFindingsComplianceTypeDef,
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List[ClientBatchImportFindingsFindingsRelatedFindingsTypeDef],
        "Note": ClientBatchImportFindingsFindingsNoteTypeDef,
    },
    total=False,
)

ClientBatchImportFindingsResponseFailedFindingsTypeDef = TypedDict(
    "ClientBatchImportFindingsResponseFailedFindingsTypeDef",
    {"Id": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchImportFindingsResponseTypeDef = TypedDict(
    "ClientBatchImportFindingsResponseTypeDef",
    {
        "FailedCount": int,
        "SuccessCount": int,
        "FailedFindings": List[ClientBatchImportFindingsResponseFailedFindingsTypeDef],
    },
    total=False,
)

ClientCreateActionTargetResponseTypeDef = TypedDict(
    "ClientCreateActionTargetResponseTypeDef", {"ActionTargetArn": str}, total=False
)

ClientCreateInsightFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersCompanyNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersComplianceStatusTypeDef = TypedDict(
    "ClientCreateInsightFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersConfidenceTypeDef = TypedDict(
    "ClientCreateInsightFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientCreateInsightFiltersCreatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientCreateInsightFiltersCreatedAtDateRangeTypeDef},
    total=False,
)

ClientCreateInsightFiltersCriticalityTypeDef = TypedDict(
    "ClientCreateInsightFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersDescriptionTypeDef = TypedDict(
    "ClientCreateInsightFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersGeneratorIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersKeywordTypeDef = TypedDict(
    "ClientCreateInsightFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersLastObservedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersMalwareNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersMalwarePathTypeDef = TypedDict(
    "ClientCreateInsightFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersMalwareStateTypeDef = TypedDict(
    "ClientCreateInsightFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersMalwareTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)

ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)

ClientCreateInsightFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientCreateInsightFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientCreateInsightFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientCreateInsightFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersNoteTextTypeDef = TypedDict(
    "ClientCreateInsightFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientCreateInsightFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersProcessNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersProcessParentPidTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersProcessPathTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersProcessPidTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersProductArnTypeDef = TypedDict(
    "ClientCreateInsightFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersProductFieldsTypeDef = TypedDict(
    "ClientCreateInsightFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientCreateInsightFiltersProductNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersRecommendationTextTypeDef = TypedDict(
    "ClientCreateInsightFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersRecordStateTypeDef = TypedDict(
    "ClientCreateInsightFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientCreateInsightFiltersResourceIdTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourcePartitionTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceRegionTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersResourceTagsTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientCreateInsightFiltersResourceTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersSeverityLabelTypeDef = TypedDict(
    "ClientCreateInsightFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientCreateInsightFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersSeverityProductTypeDef = TypedDict(
    "ClientCreateInsightFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientCreateInsightFiltersSourceUrlTypeDef = TypedDict(
    "ClientCreateInsightFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersTitleTypeDef = TypedDict(
    "ClientCreateInsightFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersTypeTypeDef = TypedDict(
    "ClientCreateInsightFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientCreateInsightFiltersUpdatedAtTypeDef = TypedDict(
    "ClientCreateInsightFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientCreateInsightFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientCreateInsightFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientCreateInsightFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientCreateInsightFiltersVerificationStateTypeDef = TypedDict(
    "ClientCreateInsightFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersWorkflowStateTypeDef = TypedDict(
    "ClientCreateInsightFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientCreateInsightFiltersTypeDef = TypedDict(
    "ClientCreateInsightFiltersTypeDef",
    {
        "ProductArn": List[ClientCreateInsightFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientCreateInsightFiltersAwsAccountIdTypeDef],
        "Id": List[ClientCreateInsightFiltersIdTypeDef],
        "GeneratorId": List[ClientCreateInsightFiltersGeneratorIdTypeDef],
        "Type": List[ClientCreateInsightFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientCreateInsightFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientCreateInsightFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientCreateInsightFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientCreateInsightFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientCreateInsightFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientCreateInsightFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientCreateInsightFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientCreateInsightFiltersConfidenceTypeDef],
        "Criticality": List[ClientCreateInsightFiltersCriticalityTypeDef],
        "Title": List[ClientCreateInsightFiltersTitleTypeDef],
        "Description": List[ClientCreateInsightFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientCreateInsightFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientCreateInsightFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientCreateInsightFiltersProductFieldsTypeDef],
        "ProductName": List[ClientCreateInsightFiltersProductNameTypeDef],
        "CompanyName": List[ClientCreateInsightFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientCreateInsightFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientCreateInsightFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientCreateInsightFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientCreateInsightFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientCreateInsightFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientCreateInsightFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientCreateInsightFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientCreateInsightFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientCreateInsightFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientCreateInsightFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientCreateInsightFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientCreateInsightFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientCreateInsightFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientCreateInsightFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientCreateInsightFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[ClientCreateInsightFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[ClientCreateInsightFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientCreateInsightFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientCreateInsightFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientCreateInsightFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientCreateInsightFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientCreateInsightFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[ClientCreateInsightFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[
            ClientCreateInsightFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientCreateInsightFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientCreateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientCreateInsightFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientCreateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientCreateInsightFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientCreateInsightFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientCreateInsightFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientCreateInsightFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientCreateInsightFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientCreateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientCreateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientCreateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientCreateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientCreateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientCreateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientCreateInsightFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[ClientCreateInsightFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            ClientCreateInsightFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientCreateInsightFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientCreateInsightFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientCreateInsightFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientCreateInsightFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientCreateInsightFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientCreateInsightFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientCreateInsightFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientCreateInsightFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientCreateInsightFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientCreateInsightFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientCreateInsightFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientCreateInsightFiltersKeywordTypeDef],
    },
    total=False,
)

ClientCreateInsightResponseTypeDef = TypedDict(
    "ClientCreateInsightResponseTypeDef", {"InsightArn": str}, total=False
)

ClientCreateMembersAccountDetailsTypeDef = TypedDict(
    "ClientCreateMembersAccountDetailsTypeDef", {"AccountId": str, "Email": str}, total=False
)

ClientCreateMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientCreateMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientCreateMembersResponseTypeDef = TypedDict(
    "ClientCreateMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientCreateMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientDeclineInvitationsResponseTypeDef = TypedDict(
    "ClientDeclineInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeclineInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDeleteActionTargetResponseTypeDef = TypedDict(
    "ClientDeleteActionTargetResponseTypeDef", {"ActionTargetArn": str}, total=False
)

ClientDeleteInsightResponseTypeDef = TypedDict(
    "ClientDeleteInsightResponseTypeDef", {"InsightArn": str}, total=False
)

ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientDeleteInvitationsResponseTypeDef = TypedDict(
    "ClientDeleteInvitationsResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteInvitationsResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDeleteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientDeleteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientDeleteMembersResponseTypeDef = TypedDict(
    "ClientDeleteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientDeleteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientDescribeActionTargetsResponseActionTargetsTypeDef = TypedDict(
    "ClientDescribeActionTargetsResponseActionTargetsTypeDef",
    {"ActionTargetArn": str, "Name": str, "Description": str},
    total=False,
)

ClientDescribeActionTargetsResponseTypeDef = TypedDict(
    "ClientDescribeActionTargetsResponseTypeDef",
    {
        "ActionTargets": List[ClientDescribeActionTargetsResponseActionTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeHubResponseTypeDef = TypedDict(
    "ClientDescribeHubResponseTypeDef", {"HubArn": str, "SubscribedAt": str}, total=False
)

ClientDescribeProductsResponseProductsTypeDef = TypedDict(
    "ClientDescribeProductsResponseProductsTypeDef",
    {
        "ProductArn": str,
        "ProductName": str,
        "CompanyName": str,
        "Description": str,
        "Categories": List[str],
        "MarketplaceUrl": str,
        "ActivationUrl": str,
        "ProductSubscriptionResourcePolicy": str,
    },
    total=False,
)

ClientDescribeProductsResponseTypeDef = TypedDict(
    "ClientDescribeProductsResponseTypeDef",
    {"Products": List[ClientDescribeProductsResponseProductsTypeDef], "NextToken": str},
    total=False,
)

ClientEnableImportFindingsForProductResponseTypeDef = TypedDict(
    "ClientEnableImportFindingsForProductResponseTypeDef",
    {"ProductSubscriptionArn": str},
    total=False,
)

ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef = TypedDict(
    "ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)

ClientGetEnabledStandardsResponseTypeDef = TypedDict(
    "ClientGetEnabledStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            ClientGetEnabledStandardsResponseStandardsSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetFindingsFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersCompanyNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersComplianceStatusTypeDef = TypedDict(
    "ClientGetFindingsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersConfidenceTypeDef = TypedDict(
    "ClientGetFindingsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientGetFindingsFiltersCreatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersCreatedAtDateRangeTypeDef},
    total=False,
)

ClientGetFindingsFiltersCriticalityTypeDef = TypedDict(
    "ClientGetFindingsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersDescriptionTypeDef = TypedDict(
    "ClientGetFindingsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersGeneratorIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersKeywordTypeDef = TypedDict(
    "ClientGetFindingsFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersLastObservedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersLastObservedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersLastObservedAtDateRangeTypeDef},
    total=False,
)

ClientGetFindingsFiltersMalwareNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersMalwarePathTypeDef = TypedDict(
    "ClientGetFindingsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersMalwareStateTypeDef = TypedDict(
    "ClientGetFindingsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersMalwareTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientGetFindingsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersNoteTextTypeDef = TypedDict(
    "ClientGetFindingsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersNoteUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersNoteUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientGetFindingsFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientGetFindingsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersProcessNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersProcessParentPidTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersProcessPathTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersProcessPidTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersProductArnTypeDef = TypedDict(
    "ClientGetFindingsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersProductFieldsTypeDef = TypedDict(
    "ClientGetFindingsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetFindingsFiltersProductNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersRecommendationTextTypeDef = TypedDict(
    "ClientGetFindingsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersRecordStateTypeDef = TypedDict(
    "ClientGetFindingsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef", {"Cidr": str}, total=False
)

ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetFindingsFiltersResourceIdTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourcePartitionTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceRegionTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersResourceTagsTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetFindingsFiltersResourceTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersSeverityLabelTypeDef = TypedDict(
    "ClientGetFindingsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientGetFindingsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersSeverityProductTypeDef = TypedDict(
    "ClientGetFindingsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetFindingsFiltersSourceUrlTypeDef = TypedDict(
    "ClientGetFindingsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersTitleTypeDef = TypedDict(
    "ClientGetFindingsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersTypeTypeDef = TypedDict(
    "ClientGetFindingsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientGetFindingsFiltersUpdatedAtTypeDef = TypedDict(
    "ClientGetFindingsFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientGetFindingsFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientGetFindingsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientGetFindingsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetFindingsFiltersVerificationStateTypeDef = TypedDict(
    "ClientGetFindingsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersWorkflowStateTypeDef = TypedDict(
    "ClientGetFindingsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetFindingsFiltersTypeDef = TypedDict(
    "ClientGetFindingsFiltersTypeDef",
    {
        "ProductArn": List[ClientGetFindingsFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientGetFindingsFiltersAwsAccountIdTypeDef],
        "Id": List[ClientGetFindingsFiltersIdTypeDef],
        "GeneratorId": List[ClientGetFindingsFiltersGeneratorIdTypeDef],
        "Type": List[ClientGetFindingsFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientGetFindingsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientGetFindingsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientGetFindingsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientGetFindingsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientGetFindingsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientGetFindingsFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientGetFindingsFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientGetFindingsFiltersConfidenceTypeDef],
        "Criticality": List[ClientGetFindingsFiltersCriticalityTypeDef],
        "Title": List[ClientGetFindingsFiltersTitleTypeDef],
        "Description": List[ClientGetFindingsFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientGetFindingsFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientGetFindingsFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientGetFindingsFiltersProductFieldsTypeDef],
        "ProductName": List[ClientGetFindingsFiltersProductNameTypeDef],
        "CompanyName": List[ClientGetFindingsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientGetFindingsFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientGetFindingsFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientGetFindingsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientGetFindingsFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientGetFindingsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientGetFindingsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientGetFindingsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientGetFindingsFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientGetFindingsFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientGetFindingsFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientGetFindingsFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientGetFindingsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientGetFindingsFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientGetFindingsFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientGetFindingsFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[ClientGetFindingsFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[ClientGetFindingsFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientGetFindingsFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientGetFindingsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientGetFindingsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientGetFindingsFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientGetFindingsFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[ClientGetFindingsFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[ClientGetFindingsFiltersThreatIntelIndicatorValueTypeDef],
        "ThreatIntelIndicatorCategory": List[
            ClientGetFindingsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientGetFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientGetFindingsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientGetFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientGetFindingsFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientGetFindingsFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientGetFindingsFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientGetFindingsFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientGetFindingsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientGetFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientGetFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientGetFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientGetFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientGetFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientGetFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientGetFindingsFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[ClientGetFindingsFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            ClientGetFindingsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientGetFindingsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientGetFindingsFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientGetFindingsFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientGetFindingsFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientGetFindingsFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientGetFindingsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[ClientGetFindingsFiltersRelatedFindingsProductArnTypeDef],
        "RelatedFindingsId": List[ClientGetFindingsFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientGetFindingsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientGetFindingsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientGetFindingsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientGetFindingsFiltersKeywordTypeDef],
    },
    total=False,
)

ClientGetFindingsResponseFindingsComplianceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsComplianceTypeDef",
    {"Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"]},
    total=False,
)

ClientGetFindingsResponseFindingsMalwareTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsMalwareTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)

ClientGetFindingsResponseFindingsNetworkTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsNetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsNoteTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsNoteTypeDef",
    {"Text": str, "UpdatedBy": str, "UpdatedAt": str},
    total=False,
)

ClientGetFindingsResponseFindingsProcessTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsProcessTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsRelatedFindingsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsRelatedFindingsTypeDef",
    {"ProductArn": str, "Id": str},
    total=False,
)

ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef",
    {"Text": str, "Url": str},
    total=False,
)

ClientGetFindingsResponseFindingsRemediationTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsRemediationTypeDef",
    {"Recommendation": ClientGetFindingsResponseFindingsRemediationRecommendationTypeDef},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    {"UserName": str, "Status": Literal["Active", "Inactive"], "CreatedAt": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef",
    {"OwnerId": str, "OwnerName": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)

ClientGetFindingsResponseFindingsResourcesDetailsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesDetailsTypeDef",
    {
        "AwsEc2Instance": ClientGetFindingsResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef,
        "AwsS3Bucket": ClientGetFindingsResponseFindingsResourcesDetailsAwsS3BucketTypeDef,
        "AwsIamAccessKey": ClientGetFindingsResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef,
        "Container": ClientGetFindingsResponseFindingsResourcesDetailsContainerTypeDef,
        "Other": Dict[str, str],
    },
    total=False,
)

ClientGetFindingsResponseFindingsResourcesTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsResourcesTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "Tags": Dict[str, str],
        "Details": ClientGetFindingsResponseFindingsResourcesDetailsTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseFindingsSeverityTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsSeverityTypeDef",
    {"Product": float, "Normalized": int},
    total=False,
)

ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)

ClientGetFindingsResponseFindingsTypeDef = TypedDict(
    "ClientGetFindingsResponseFindingsTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": ClientGetFindingsResponseFindingsSeverityTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Title": str,
        "Description": str,
        "Remediation": ClientGetFindingsResponseFindingsRemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[ClientGetFindingsResponseFindingsMalwareTypeDef],
        "Network": ClientGetFindingsResponseFindingsNetworkTypeDef,
        "Process": ClientGetFindingsResponseFindingsProcessTypeDef,
        "ThreatIntelIndicators": List[
            ClientGetFindingsResponseFindingsThreatIntelIndicatorsTypeDef
        ],
        "Resources": List[ClientGetFindingsResponseFindingsResourcesTypeDef],
        "Compliance": ClientGetFindingsResponseFindingsComplianceTypeDef,
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List[ClientGetFindingsResponseFindingsRelatedFindingsTypeDef],
        "Note": ClientGetFindingsResponseFindingsNoteTypeDef,
    },
    total=False,
)

ClientGetFindingsResponseTypeDef = TypedDict(
    "ClientGetFindingsResponseTypeDef",
    {"Findings": List[ClientGetFindingsResponseFindingsTypeDef], "NextToken": str},
    total=False,
)

ClientGetFindingsSortCriteriaTypeDef = TypedDict(
    "ClientGetFindingsSortCriteriaTypeDef",
    {"Field": str, "SortOrder": Literal["asc", "desc"]},
    total=False,
)

ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef = TypedDict(
    "ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef",
    {"GroupByAttributeValue": str, "Count": int},
    total=False,
)

ClientGetInsightResultsResponseInsightResultsTypeDef = TypedDict(
    "ClientGetInsightResultsResponseInsightResultsTypeDef",
    {
        "InsightArn": str,
        "GroupByAttribute": str,
        "ResultValues": List[ClientGetInsightResultsResponseInsightResultsResultValuesTypeDef],
    },
    total=False,
)

ClientGetInsightResultsResponseTypeDef = TypedDict(
    "ClientGetInsightResultsResponseTypeDef",
    {"InsightResults": ClientGetInsightResultsResponseInsightResultsTypeDef},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersKeywordTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef",
    {"Cidr": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef",
    {"Cidr": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProductArnTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersProductNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersTitleTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersTypeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientGetInsightsResponseInsightsFiltersUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientGetInsightsResponseInsightsFiltersTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsFiltersTypeDef",
    {
        "ProductArn": List[ClientGetInsightsResponseInsightsFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientGetInsightsResponseInsightsFiltersAwsAccountIdTypeDef],
        "Id": List[ClientGetInsightsResponseInsightsFiltersIdTypeDef],
        "GeneratorId": List[ClientGetInsightsResponseInsightsFiltersGeneratorIdTypeDef],
        "Type": List[ClientGetInsightsResponseInsightsFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientGetInsightsResponseInsightsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientGetInsightsResponseInsightsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientGetInsightsResponseInsightsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientGetInsightsResponseInsightsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientGetInsightsResponseInsightsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[
            ClientGetInsightsResponseInsightsFiltersSeverityNormalizedTypeDef
        ],
        "SeverityLabel": List[ClientGetInsightsResponseInsightsFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientGetInsightsResponseInsightsFiltersConfidenceTypeDef],
        "Criticality": List[ClientGetInsightsResponseInsightsFiltersCriticalityTypeDef],
        "Title": List[ClientGetInsightsResponseInsightsFiltersTitleTypeDef],
        "Description": List[ClientGetInsightsResponseInsightsFiltersDescriptionTypeDef],
        "RecommendationText": List[
            ClientGetInsightsResponseInsightsFiltersRecommendationTextTypeDef
        ],
        "SourceUrl": List[ClientGetInsightsResponseInsightsFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientGetInsightsResponseInsightsFiltersProductFieldsTypeDef],
        "ProductName": List[ClientGetInsightsResponseInsightsFiltersProductNameTypeDef],
        "CompanyName": List[ClientGetInsightsResponseInsightsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientGetInsightsResponseInsightsFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientGetInsightsResponseInsightsFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientGetInsightsResponseInsightsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientGetInsightsResponseInsightsFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientGetInsightsResponseInsightsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientGetInsightsResponseInsightsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientGetInsightsResponseInsightsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientGetInsightsResponseInsightsFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientGetInsightsResponseInsightsFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[
            ClientGetInsightsResponseInsightsFiltersNetworkSourceDomainTypeDef
        ],
        "NetworkSourceMac": List[ClientGetInsightsResponseInsightsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV4TypeDef
        ],
        "NetworkDestinationIpV6": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationIpV6TypeDef
        ],
        "NetworkDestinationPort": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationPortTypeDef
        ],
        "NetworkDestinationDomain": List[
            ClientGetInsightsResponseInsightsFiltersNetworkDestinationDomainTypeDef
        ],
        "ProcessName": List[ClientGetInsightsResponseInsightsFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientGetInsightsResponseInsightsFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientGetInsightsResponseInsightsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientGetInsightsResponseInsightsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientGetInsightsResponseInsightsFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[
            ClientGetInsightsResponseInsightsFiltersProcessTerminatedAtTypeDef
        ],
        "ThreatIntelIndicatorType": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef
        ],
        "ThreatIntelIndicatorValue": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientGetInsightsResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientGetInsightsResponseInsightsFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientGetInsightsResponseInsightsFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientGetInsightsResponseInsightsFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientGetInsightsResponseInsightsFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientGetInsightsResponseInsightsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientGetInsightsResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerNameTypeDef
        ],
        "ResourceContainerImageId": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerImageIdTypeDef
        ],
        "ResourceContainerImageName": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientGetInsightsResponseInsightsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[
            ClientGetInsightsResponseInsightsFiltersResourceDetailsOtherTypeDef
        ],
        "ComplianceStatus": List[ClientGetInsightsResponseInsightsFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientGetInsightsResponseInsightsFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientGetInsightsResponseInsightsFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientGetInsightsResponseInsightsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientGetInsightsResponseInsightsFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientGetInsightsResponseInsightsFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientGetInsightsResponseInsightsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientGetInsightsResponseInsightsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientGetInsightsResponseInsightsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientGetInsightsResponseInsightsFiltersKeywordTypeDef],
    },
    total=False,
)

ClientGetInsightsResponseInsightsTypeDef = TypedDict(
    "ClientGetInsightsResponseInsightsTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": ClientGetInsightsResponseInsightsFiltersTypeDef,
        "GroupByAttribute": str,
    },
    total=False,
)

ClientGetInsightsResponseTypeDef = TypedDict(
    "ClientGetInsightsResponseTypeDef",
    {"Insights": List[ClientGetInsightsResponseInsightsTypeDef], "NextToken": str},
    total=False,
)

ClientGetInvitationsCountResponseTypeDef = TypedDict(
    "ClientGetInvitationsCountResponseTypeDef", {"InvitationsCount": int}, total=False
)

ClientGetMasterAccountResponseMasterTypeDef = TypedDict(
    "ClientGetMasterAccountResponseMasterTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)

ClientGetMasterAccountResponseTypeDef = TypedDict(
    "ClientGetMasterAccountResponseTypeDef",
    {"Master": ClientGetMasterAccountResponseMasterTypeDef},
    total=False,
)

ClientGetMembersResponseMembersTypeDef = TypedDict(
    "ClientGetMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientGetMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientGetMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientGetMembersResponseTypeDef = TypedDict(
    "ClientGetMembersResponseTypeDef",
    {
        "Members": List[ClientGetMembersResponseMembersTypeDef],
        "UnprocessedAccounts": List[ClientGetMembersResponseUnprocessedAccountsTypeDef],
    },
    total=False,
)

ClientInviteMembersResponseUnprocessedAccountsTypeDef = TypedDict(
    "ClientInviteMembersResponseUnprocessedAccountsTypeDef",
    {"AccountId": str, "ProcessingResult": str},
    total=False,
)

ClientInviteMembersResponseTypeDef = TypedDict(
    "ClientInviteMembersResponseTypeDef",
    {"UnprocessedAccounts": List[ClientInviteMembersResponseUnprocessedAccountsTypeDef]},
    total=False,
)

ClientListEnabledProductsForImportResponseTypeDef = TypedDict(
    "ClientListEnabledProductsForImportResponseTypeDef",
    {"ProductSubscriptions": List[str], "NextToken": str},
    total=False,
)

ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "ClientListInvitationsResponseInvitationsTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)

ClientListInvitationsResponseTypeDef = TypedDict(
    "ClientListInvitationsResponseTypeDef",
    {"Invitations": List[ClientListInvitationsResponseInvitationsTypeDef], "NextToken": str},
    total=False,
)

ClientListMembersResponseMembersTypeDef = TypedDict(
    "ClientListMembersResponseMembersTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientListMembersResponseTypeDef = TypedDict(
    "ClientListMembersResponseTypeDef",
    {"Members": List[ClientListMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUpdateFindingsFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersCompanyNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersComplianceStatusTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersConfidenceTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientUpdateFindingsFiltersCreatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateFindingsFiltersCreatedAtDateRangeTypeDef},
    total=False,
)

ClientUpdateFindingsFiltersCriticalityTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersDescriptionTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersGeneratorIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersKeywordTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersLastObservedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersMalwareNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersMalwarePathTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersMalwareStateTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersMalwareTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)

ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)

ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientUpdateFindingsFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersNoteTextTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersProcessNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersProcessParentPidTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersProcessPathTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersProcessPidTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersProductArnTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersProductFieldsTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateFindingsFiltersProductNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersRecommendationTextTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersRecordStateTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceIdTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourcePartitionTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceRegionTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersResourceTagsTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateFindingsFiltersResourceTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersSeverityLabelTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersSeverityProductTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateFindingsFiltersSourceUrlTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersTitleTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersTypeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientUpdateFindingsFiltersUpdatedAtTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateFindingsFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateFindingsFiltersVerificationStateTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersWorkflowStateTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateFindingsFiltersTypeDef = TypedDict(
    "ClientUpdateFindingsFiltersTypeDef",
    {
        "ProductArn": List[ClientUpdateFindingsFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientUpdateFindingsFiltersAwsAccountIdTypeDef],
        "Id": List[ClientUpdateFindingsFiltersIdTypeDef],
        "GeneratorId": List[ClientUpdateFindingsFiltersGeneratorIdTypeDef],
        "Type": List[ClientUpdateFindingsFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientUpdateFindingsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientUpdateFindingsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientUpdateFindingsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientUpdateFindingsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientUpdateFindingsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientUpdateFindingsFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientUpdateFindingsFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientUpdateFindingsFiltersConfidenceTypeDef],
        "Criticality": List[ClientUpdateFindingsFiltersCriticalityTypeDef],
        "Title": List[ClientUpdateFindingsFiltersTitleTypeDef],
        "Description": List[ClientUpdateFindingsFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientUpdateFindingsFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientUpdateFindingsFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientUpdateFindingsFiltersProductFieldsTypeDef],
        "ProductName": List[ClientUpdateFindingsFiltersProductNameTypeDef],
        "CompanyName": List[ClientUpdateFindingsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientUpdateFindingsFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientUpdateFindingsFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientUpdateFindingsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientUpdateFindingsFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientUpdateFindingsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientUpdateFindingsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientUpdateFindingsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientUpdateFindingsFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientUpdateFindingsFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientUpdateFindingsFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientUpdateFindingsFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientUpdateFindingsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientUpdateFindingsFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientUpdateFindingsFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientUpdateFindingsFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[
            ClientUpdateFindingsFiltersNetworkDestinationDomainTypeDef
        ],
        "ProcessName": List[ClientUpdateFindingsFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientUpdateFindingsFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientUpdateFindingsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientUpdateFindingsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientUpdateFindingsFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientUpdateFindingsFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorTypeTypeDef
        ],
        "ThreatIntelIndicatorValue": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientUpdateFindingsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientUpdateFindingsFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientUpdateFindingsFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientUpdateFindingsFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientUpdateFindingsFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientUpdateFindingsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientUpdateFindingsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientUpdateFindingsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientUpdateFindingsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientUpdateFindingsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientUpdateFindingsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientUpdateFindingsFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[
            ClientUpdateFindingsFiltersResourceContainerImageIdTypeDef
        ],
        "ResourceContainerImageName": List[
            ClientUpdateFindingsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientUpdateFindingsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientUpdateFindingsFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientUpdateFindingsFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientUpdateFindingsFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientUpdateFindingsFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientUpdateFindingsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientUpdateFindingsFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientUpdateFindingsFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientUpdateFindingsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientUpdateFindingsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientUpdateFindingsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientUpdateFindingsFiltersKeywordTypeDef],
    },
    total=False,
)

_RequiredClientUpdateFindingsNoteTypeDef = TypedDict(
    "_RequiredClientUpdateFindingsNoteTypeDef", {"Text": str}
)
_OptionalClientUpdateFindingsNoteTypeDef = TypedDict(
    "_OptionalClientUpdateFindingsNoteTypeDef", {"UpdatedBy": str}, total=False
)


class ClientUpdateFindingsNoteTypeDef(
    _RequiredClientUpdateFindingsNoteTypeDef, _OptionalClientUpdateFindingsNoteTypeDef
):
    pass


ClientUpdateInsightFiltersAwsAccountIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersCompanyNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersComplianceStatusTypeDef = TypedDict(
    "ClientUpdateInsightFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersConfidenceTypeDef = TypedDict(
    "ClientUpdateInsightFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientUpdateInsightFiltersCreatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateInsightFiltersCreatedAtDateRangeTypeDef},
    total=False,
)

ClientUpdateInsightFiltersCriticalityTypeDef = TypedDict(
    "ClientUpdateInsightFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersDescriptionTypeDef = TypedDict(
    "ClientUpdateInsightFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersFirstObservedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersGeneratorIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersKeywordTypeDef = TypedDict(
    "ClientUpdateInsightFiltersKeywordTypeDef", {"Value": str}, total=False
)

ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersLastObservedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersMalwareNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersMalwarePathTypeDef = TypedDict(
    "ClientUpdateInsightFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersMalwareStateTypeDef = TypedDict(
    "ClientUpdateInsightFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersMalwareTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)

ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)

ClientUpdateInsightFiltersNetworkDestinationPortTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersNetworkDirectionTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkProtocolTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkSourceDomainTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

ClientUpdateInsightFiltersNetworkSourceMacTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNetworkSourcePortTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersNoteTextTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersNoteUpdatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersNoteUpdatedByTypeDef = TypedDict(
    "ClientUpdateInsightFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersProcessLaunchedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersProcessNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersProcessParentPidTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersProcessPathTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersProcessPidTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersProcessTerminatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersProductArnTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersProductFieldsTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateInsightFiltersProductNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersRecommendationTextTypeDef = TypedDict(
    "ClientUpdateInsightFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersRecordStateTypeDef = TypedDict(
    "ClientUpdateInsightFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersRelatedFindingsIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceContainerImageIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceContainerImageNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersResourceContainerNameTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceDetailsOtherTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateInsightFiltersResourceIdTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourcePartitionTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceRegionTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersResourceTagsTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateInsightFiltersResourceTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersSeverityLabelTypeDef = TypedDict(
    "ClientUpdateInsightFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersSeverityNormalizedTypeDef = TypedDict(
    "ClientUpdateInsightFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersSeverityProductTypeDef = TypedDict(
    "ClientUpdateInsightFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

ClientUpdateInsightFiltersSourceUrlTypeDef = TypedDict(
    "ClientUpdateInsightFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersTitleTypeDef = TypedDict(
    "ClientUpdateInsightFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersTypeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

ClientUpdateInsightFiltersUpdatedAtTypeDef = TypedDict(
    "ClientUpdateInsightFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": ClientUpdateInsightFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)

ClientUpdateInsightFiltersUserDefinedFieldsTypeDef = TypedDict(
    "ClientUpdateInsightFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

ClientUpdateInsightFiltersVerificationStateTypeDef = TypedDict(
    "ClientUpdateInsightFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersWorkflowStateTypeDef = TypedDict(
    "ClientUpdateInsightFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

ClientUpdateInsightFiltersTypeDef = TypedDict(
    "ClientUpdateInsightFiltersTypeDef",
    {
        "ProductArn": List[ClientUpdateInsightFiltersProductArnTypeDef],
        "AwsAccountId": List[ClientUpdateInsightFiltersAwsAccountIdTypeDef],
        "Id": List[ClientUpdateInsightFiltersIdTypeDef],
        "GeneratorId": List[ClientUpdateInsightFiltersGeneratorIdTypeDef],
        "Type": List[ClientUpdateInsightFiltersTypeTypeDef],
        "FirstObservedAt": List[ClientUpdateInsightFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[ClientUpdateInsightFiltersLastObservedAtTypeDef],
        "CreatedAt": List[ClientUpdateInsightFiltersCreatedAtTypeDef],
        "UpdatedAt": List[ClientUpdateInsightFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[ClientUpdateInsightFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[ClientUpdateInsightFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[ClientUpdateInsightFiltersSeverityLabelTypeDef],
        "Confidence": List[ClientUpdateInsightFiltersConfidenceTypeDef],
        "Criticality": List[ClientUpdateInsightFiltersCriticalityTypeDef],
        "Title": List[ClientUpdateInsightFiltersTitleTypeDef],
        "Description": List[ClientUpdateInsightFiltersDescriptionTypeDef],
        "RecommendationText": List[ClientUpdateInsightFiltersRecommendationTextTypeDef],
        "SourceUrl": List[ClientUpdateInsightFiltersSourceUrlTypeDef],
        "ProductFields": List[ClientUpdateInsightFiltersProductFieldsTypeDef],
        "ProductName": List[ClientUpdateInsightFiltersProductNameTypeDef],
        "CompanyName": List[ClientUpdateInsightFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[ClientUpdateInsightFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[ClientUpdateInsightFiltersMalwareNameTypeDef],
        "MalwareType": List[ClientUpdateInsightFiltersMalwareTypeTypeDef],
        "MalwarePath": List[ClientUpdateInsightFiltersMalwarePathTypeDef],
        "MalwareState": List[ClientUpdateInsightFiltersMalwareStateTypeDef],
        "NetworkDirection": List[ClientUpdateInsightFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[ClientUpdateInsightFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[ClientUpdateInsightFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[ClientUpdateInsightFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[ClientUpdateInsightFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[ClientUpdateInsightFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[ClientUpdateInsightFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[ClientUpdateInsightFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[ClientUpdateInsightFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[ClientUpdateInsightFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[ClientUpdateInsightFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[ClientUpdateInsightFiltersProcessNameTypeDef],
        "ProcessPath": List[ClientUpdateInsightFiltersProcessPathTypeDef],
        "ProcessPid": List[ClientUpdateInsightFiltersProcessPidTypeDef],
        "ProcessParentPid": List[ClientUpdateInsightFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[ClientUpdateInsightFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[ClientUpdateInsightFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[ClientUpdateInsightFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            ClientUpdateInsightFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[ClientUpdateInsightFiltersResourceTypeTypeDef],
        "ResourceId": List[ClientUpdateInsightFiltersResourceIdTypeDef],
        "ResourcePartition": List[ClientUpdateInsightFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[ClientUpdateInsightFiltersResourceRegionTypeDef],
        "ResourceTags": List[ClientUpdateInsightFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            ClientUpdateInsightFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            ClientUpdateInsightFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            ClientUpdateInsightFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            ClientUpdateInsightFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            ClientUpdateInsightFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            ClientUpdateInsightFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[ClientUpdateInsightFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[ClientUpdateInsightFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            ClientUpdateInsightFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            ClientUpdateInsightFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[ClientUpdateInsightFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[ClientUpdateInsightFiltersComplianceStatusTypeDef],
        "VerificationState": List[ClientUpdateInsightFiltersVerificationStateTypeDef],
        "WorkflowState": List[ClientUpdateInsightFiltersWorkflowStateTypeDef],
        "RecordState": List[ClientUpdateInsightFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            ClientUpdateInsightFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[ClientUpdateInsightFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[ClientUpdateInsightFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[ClientUpdateInsightFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[ClientUpdateInsightFiltersNoteUpdatedByTypeDef],
        "Keyword": List[ClientUpdateInsightFiltersKeywordTypeDef],
    },
    total=False,
)

GetEnabledStandardsPaginatePaginationConfigTypeDef = TypedDict(
    "GetEnabledStandardsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetEnabledStandardsPaginateResponseStandardsSubscriptionsTypeDef = TypedDict(
    "GetEnabledStandardsPaginateResponseStandardsSubscriptionsTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
    total=False,
)

GetEnabledStandardsPaginateResponseTypeDef = TypedDict(
    "GetEnabledStandardsPaginateResponseTypeDef",
    {
        "StandardsSubscriptions": List[
            GetEnabledStandardsPaginateResponseStandardsSubscriptionsTypeDef
        ]
    },
    total=False,
)

GetFindingsPaginateFiltersAwsAccountIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersCompanyNameTypeDef = TypedDict(
    "GetFindingsPaginateFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersComplianceStatusTypeDef = TypedDict(
    "GetFindingsPaginateFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersConfidenceTypeDef = TypedDict(
    "GetFindingsPaginateFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetFindingsPaginateFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersCreatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

GetFindingsPaginateFiltersCreatedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersCreatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": GetFindingsPaginateFiltersCreatedAtDateRangeTypeDef},
    total=False,
)

GetFindingsPaginateFiltersCriticalityTypeDef = TypedDict(
    "GetFindingsPaginateFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetFindingsPaginateFiltersDescriptionTypeDef = TypedDict(
    "GetFindingsPaginateFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetFindingsPaginateFiltersFirstObservedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

GetFindingsPaginateFiltersGeneratorIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersKeywordTypeDef = TypedDict(
    "GetFindingsPaginateFiltersKeywordTypeDef", {"Value": str}, total=False
)

GetFindingsPaginateFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetFindingsPaginateFiltersLastObservedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

GetFindingsPaginateFiltersMalwareNameTypeDef = TypedDict(
    "GetFindingsPaginateFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersMalwarePathTypeDef = TypedDict(
    "GetFindingsPaginateFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersMalwareStateTypeDef = TypedDict(
    "GetFindingsPaginateFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersMalwareTypeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkDestinationIpV4TypeDef", {"Cidr": str}, total=False
)

GetFindingsPaginateFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkDestinationIpV6TypeDef", {"Cidr": str}, total=False
)

GetFindingsPaginateFiltersNetworkDestinationPortTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetFindingsPaginateFiltersNetworkDirectionTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersNetworkProtocolTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersNetworkSourceDomainTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

GetFindingsPaginateFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

GetFindingsPaginateFiltersNetworkSourceMacTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersNetworkSourcePortTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetFindingsPaginateFiltersNoteTextTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetFindingsPaginateFiltersNoteUpdatedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

GetFindingsPaginateFiltersNoteUpdatedByTypeDef = TypedDict(
    "GetFindingsPaginateFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetFindingsPaginateFiltersProcessLaunchedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

GetFindingsPaginateFiltersProcessNameTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersProcessParentPidTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetFindingsPaginateFiltersProcessPathTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersProcessPidTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetFindingsPaginateFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetFindingsPaginateFiltersProcessTerminatedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

GetFindingsPaginateFiltersProductArnTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersProductFieldsTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

GetFindingsPaginateFiltersProductNameTypeDef = TypedDict(
    "GetFindingsPaginateFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersRecommendationTextTypeDef = TypedDict(
    "GetFindingsPaginateFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersRecordStateTypeDef = TypedDict(
    "GetFindingsPaginateFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersRelatedFindingsIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "GetFindingsPaginateFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

GetFindingsPaginateFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceContainerImageIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceContainerImageNameTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetFindingsPaginateFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

GetFindingsPaginateFiltersResourceContainerNameTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceDetailsOtherTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

GetFindingsPaginateFiltersResourceIdTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourcePartitionTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceRegionTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersResourceTagsTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

GetFindingsPaginateFiltersResourceTypeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersSeverityLabelTypeDef = TypedDict(
    "GetFindingsPaginateFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersSeverityNormalizedTypeDef = TypedDict(
    "GetFindingsPaginateFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetFindingsPaginateFiltersSeverityProductTypeDef = TypedDict(
    "GetFindingsPaginateFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetFindingsPaginateFiltersSourceUrlTypeDef = TypedDict(
    "GetFindingsPaginateFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "GetFindingsPaginateFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

GetFindingsPaginateFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "GetFindingsPaginateFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "GetFindingsPaginateFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "GetFindingsPaginateFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersTitleTypeDef = TypedDict(
    "GetFindingsPaginateFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersTypeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "GetFindingsPaginateFiltersUpdatedAtDateRangeTypeDef", {"Value": int, "Unit": str}, total=False
)

GetFindingsPaginateFiltersUpdatedAtTypeDef = TypedDict(
    "GetFindingsPaginateFiltersUpdatedAtTypeDef",
    {"Start": str, "End": str, "DateRange": GetFindingsPaginateFiltersUpdatedAtDateRangeTypeDef},
    total=False,
)

GetFindingsPaginateFiltersUserDefinedFieldsTypeDef = TypedDict(
    "GetFindingsPaginateFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

GetFindingsPaginateFiltersVerificationStateTypeDef = TypedDict(
    "GetFindingsPaginateFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersWorkflowStateTypeDef = TypedDict(
    "GetFindingsPaginateFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetFindingsPaginateFiltersTypeDef = TypedDict(
    "GetFindingsPaginateFiltersTypeDef",
    {
        "ProductArn": List[GetFindingsPaginateFiltersProductArnTypeDef],
        "AwsAccountId": List[GetFindingsPaginateFiltersAwsAccountIdTypeDef],
        "Id": List[GetFindingsPaginateFiltersIdTypeDef],
        "GeneratorId": List[GetFindingsPaginateFiltersGeneratorIdTypeDef],
        "Type": List[GetFindingsPaginateFiltersTypeTypeDef],
        "FirstObservedAt": List[GetFindingsPaginateFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[GetFindingsPaginateFiltersLastObservedAtTypeDef],
        "CreatedAt": List[GetFindingsPaginateFiltersCreatedAtTypeDef],
        "UpdatedAt": List[GetFindingsPaginateFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[GetFindingsPaginateFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[GetFindingsPaginateFiltersSeverityNormalizedTypeDef],
        "SeverityLabel": List[GetFindingsPaginateFiltersSeverityLabelTypeDef],
        "Confidence": List[GetFindingsPaginateFiltersConfidenceTypeDef],
        "Criticality": List[GetFindingsPaginateFiltersCriticalityTypeDef],
        "Title": List[GetFindingsPaginateFiltersTitleTypeDef],
        "Description": List[GetFindingsPaginateFiltersDescriptionTypeDef],
        "RecommendationText": List[GetFindingsPaginateFiltersRecommendationTextTypeDef],
        "SourceUrl": List[GetFindingsPaginateFiltersSourceUrlTypeDef],
        "ProductFields": List[GetFindingsPaginateFiltersProductFieldsTypeDef],
        "ProductName": List[GetFindingsPaginateFiltersProductNameTypeDef],
        "CompanyName": List[GetFindingsPaginateFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[GetFindingsPaginateFiltersUserDefinedFieldsTypeDef],
        "MalwareName": List[GetFindingsPaginateFiltersMalwareNameTypeDef],
        "MalwareType": List[GetFindingsPaginateFiltersMalwareTypeTypeDef],
        "MalwarePath": List[GetFindingsPaginateFiltersMalwarePathTypeDef],
        "MalwareState": List[GetFindingsPaginateFiltersMalwareStateTypeDef],
        "NetworkDirection": List[GetFindingsPaginateFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[GetFindingsPaginateFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[GetFindingsPaginateFiltersNetworkSourceIpV4TypeDef],
        "NetworkSourceIpV6": List[GetFindingsPaginateFiltersNetworkSourceIpV6TypeDef],
        "NetworkSourcePort": List[GetFindingsPaginateFiltersNetworkSourcePortTypeDef],
        "NetworkSourceDomain": List[GetFindingsPaginateFiltersNetworkSourceDomainTypeDef],
        "NetworkSourceMac": List[GetFindingsPaginateFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[GetFindingsPaginateFiltersNetworkDestinationIpV4TypeDef],
        "NetworkDestinationIpV6": List[GetFindingsPaginateFiltersNetworkDestinationIpV6TypeDef],
        "NetworkDestinationPort": List[GetFindingsPaginateFiltersNetworkDestinationPortTypeDef],
        "NetworkDestinationDomain": List[GetFindingsPaginateFiltersNetworkDestinationDomainTypeDef],
        "ProcessName": List[GetFindingsPaginateFiltersProcessNameTypeDef],
        "ProcessPath": List[GetFindingsPaginateFiltersProcessPathTypeDef],
        "ProcessPid": List[GetFindingsPaginateFiltersProcessPidTypeDef],
        "ProcessParentPid": List[GetFindingsPaginateFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[GetFindingsPaginateFiltersProcessLaunchedAtTypeDef],
        "ProcessTerminatedAt": List[GetFindingsPaginateFiltersProcessTerminatedAtTypeDef],
        "ThreatIntelIndicatorType": List[GetFindingsPaginateFiltersThreatIntelIndicatorTypeTypeDef],
        "ThreatIntelIndicatorValue": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            GetFindingsPaginateFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[GetFindingsPaginateFiltersResourceTypeTypeDef],
        "ResourceId": List[GetFindingsPaginateFiltersResourceIdTypeDef],
        "ResourcePartition": List[GetFindingsPaginateFiltersResourcePartitionTypeDef],
        "ResourceRegion": List[GetFindingsPaginateFiltersResourceRegionTypeDef],
        "ResourceTags": List[GetFindingsPaginateFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            GetFindingsPaginateFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            GetFindingsPaginateFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            GetFindingsPaginateFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            GetFindingsPaginateFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            GetFindingsPaginateFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            GetFindingsPaginateFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[GetFindingsPaginateFiltersResourceContainerNameTypeDef],
        "ResourceContainerImageId": List[GetFindingsPaginateFiltersResourceContainerImageIdTypeDef],
        "ResourceContainerImageName": List[
            GetFindingsPaginateFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            GetFindingsPaginateFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[GetFindingsPaginateFiltersResourceDetailsOtherTypeDef],
        "ComplianceStatus": List[GetFindingsPaginateFiltersComplianceStatusTypeDef],
        "VerificationState": List[GetFindingsPaginateFiltersVerificationStateTypeDef],
        "WorkflowState": List[GetFindingsPaginateFiltersWorkflowStateTypeDef],
        "RecordState": List[GetFindingsPaginateFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            GetFindingsPaginateFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[GetFindingsPaginateFiltersRelatedFindingsIdTypeDef],
        "NoteText": List[GetFindingsPaginateFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[GetFindingsPaginateFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[GetFindingsPaginateFiltersNoteUpdatedByTypeDef],
        "Keyword": List[GetFindingsPaginateFiltersKeywordTypeDef],
    },
    total=False,
)

GetFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "GetFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetFindingsPaginateResponseFindingsComplianceTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsComplianceTypeDef",
    {"Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"]},
    total=False,
)

GetFindingsPaginateResponseFindingsMalwareTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsMalwareTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)

GetFindingsPaginateResponseFindingsNetworkTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsNetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)

GetFindingsPaginateResponseFindingsNoteTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsNoteTypeDef",
    {"Text": str, "UpdatedBy": str, "UpdatedAt": str},
    total=False,
)

GetFindingsPaginateResponseFindingsProcessTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsProcessTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)

GetFindingsPaginateResponseFindingsRelatedFindingsTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsRelatedFindingsTypeDef",
    {"ProductArn": str, "Id": str},
    total=False,
)

GetFindingsPaginateResponseFindingsRemediationRecommendationTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsRemediationRecommendationTypeDef",
    {"Text": str, "Url": str},
    total=False,
)

GetFindingsPaginateResponseFindingsRemediationTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsRemediationTypeDef",
    {"Recommendation": GetFindingsPaginateResponseFindingsRemediationRecommendationTypeDef},
    total=False,
)

GetFindingsPaginateResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)

GetFindingsPaginateResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef",
    {"UserName": str, "Status": Literal["Active", "Inactive"], "CreatedAt": str},
    total=False,
)

GetFindingsPaginateResponseFindingsResourcesDetailsAwsS3BucketTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsResourcesDetailsAwsS3BucketTypeDef",
    {"OwnerId": str, "OwnerName": str},
    total=False,
)

GetFindingsPaginateResponseFindingsResourcesDetailsContainerTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsResourcesDetailsContainerTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)

GetFindingsPaginateResponseFindingsResourcesDetailsTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsResourcesDetailsTypeDef",
    {
        "AwsEc2Instance": GetFindingsPaginateResponseFindingsResourcesDetailsAwsEc2InstanceTypeDef,
        "AwsS3Bucket": GetFindingsPaginateResponseFindingsResourcesDetailsAwsS3BucketTypeDef,
        "AwsIamAccessKey": GetFindingsPaginateResponseFindingsResourcesDetailsAwsIamAccessKeyTypeDef,
        "Container": GetFindingsPaginateResponseFindingsResourcesDetailsContainerTypeDef,
        "Other": Dict[str, str],
    },
    total=False,
)

GetFindingsPaginateResponseFindingsResourcesTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsResourcesTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "Tags": Dict[str, str],
        "Details": GetFindingsPaginateResponseFindingsResourcesDetailsTypeDef,
    },
    total=False,
)

GetFindingsPaginateResponseFindingsSeverityTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsSeverityTypeDef",
    {"Product": float, "Normalized": int},
    total=False,
)

GetFindingsPaginateResponseFindingsThreatIntelIndicatorsTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsThreatIntelIndicatorsTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)

GetFindingsPaginateResponseFindingsTypeDef = TypedDict(
    "GetFindingsPaginateResponseFindingsTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": GetFindingsPaginateResponseFindingsSeverityTypeDef,
        "Confidence": int,
        "Criticality": int,
        "Title": str,
        "Description": str,
        "Remediation": GetFindingsPaginateResponseFindingsRemediationTypeDef,
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List[GetFindingsPaginateResponseFindingsMalwareTypeDef],
        "Network": GetFindingsPaginateResponseFindingsNetworkTypeDef,
        "Process": GetFindingsPaginateResponseFindingsProcessTypeDef,
        "ThreatIntelIndicators": List[
            GetFindingsPaginateResponseFindingsThreatIntelIndicatorsTypeDef
        ],
        "Resources": List[GetFindingsPaginateResponseFindingsResourcesTypeDef],
        "Compliance": GetFindingsPaginateResponseFindingsComplianceTypeDef,
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List[GetFindingsPaginateResponseFindingsRelatedFindingsTypeDef],
        "Note": GetFindingsPaginateResponseFindingsNoteTypeDef,
    },
    total=False,
)

GetFindingsPaginateResponseTypeDef = TypedDict(
    "GetFindingsPaginateResponseTypeDef",
    {"Findings": List[GetFindingsPaginateResponseFindingsTypeDef]},
    total=False,
)

GetFindingsPaginateSortCriteriaTypeDef = TypedDict(
    "GetFindingsPaginateSortCriteriaTypeDef",
    {"Field": str, "SortOrder": Literal["asc", "desc"]},
    total=False,
)

GetInsightsPaginatePaginationConfigTypeDef = TypedDict(
    "GetInsightsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersAwsAccountIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersAwsAccountIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersCompanyNameTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersCompanyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersComplianceStatusTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersComplianceStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersConfidenceTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersConfidenceTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersCreatedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersCreatedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersCreatedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersCriticalityTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersCriticalityTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersDescriptionTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersDescriptionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersFirstObservedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersFirstObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersFirstObservedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersFirstObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersFirstObservedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersGeneratorIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersGeneratorIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersKeywordTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersKeywordTypeDef", {"Value": str}, total=False
)

GetInsightsPaginateResponseInsightsFiltersLastObservedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersLastObservedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersMalwareNameTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersMalwareNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersMalwarePathTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersMalwarePathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersMalwareStateTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersMalwareStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersMalwareTypeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersMalwareTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNetworkDestinationDomainTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkDestinationDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV4TypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV4TypeDef",
    {"Cidr": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV6TypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV6TypeDef",
    {"Cidr": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNetworkDestinationPortTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkDestinationPortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNetworkDirectionTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkDirectionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNetworkProtocolTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkProtocolTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNetworkSourceDomainTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourceDomainTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV4TypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV4TypeDef", {"Cidr": str}, total=False
)

GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV6TypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV6TypeDef", {"Cidr": str}, total=False
)

GetInsightsPaginateResponseInsightsFiltersNetworkSourceMacTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourceMacTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNetworkSourcePortTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNetworkSourcePortTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNoteTextTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNoteTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersNoteUpdatedByTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersNoteUpdatedByTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProcessNameTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProcessNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProcessParentPidTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProcessParentPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProcessPathTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProcessPathTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProcessPidTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProcessPidTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProductArnTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProductFieldsTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProductFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersProductNameTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersProductNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersRecommendationTextTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersRecommendationTextTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersRecordStateTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersRecordStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersRelatedFindingsIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersRelatedFindingsIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersRelatedFindingsProductArnTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersRelatedFindingsProductArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef",
    {"Cidr": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceContainerImageIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerImageIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceContainerImageNameTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerImageNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceContainerNameTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceContainerNameTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceDetailsOtherTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceDetailsOtherTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceIdTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceIdTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourcePartitionTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourcePartitionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceRegionTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceRegionTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceTagsTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceTagsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersResourceTypeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersResourceTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersSeverityLabelTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersSeverityLabelTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersSeverityNormalizedTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersSeverityNormalizedTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersSeverityProductTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersSeverityProductTypeDef",
    {"Gte": float, "Lte": float, "Eq": float},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersSourceUrlTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorValueTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorValueTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersTitleTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersTitleTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersTypeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersTypeTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersUpdatedAtDateRangeTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersUpdatedAtDateRangeTypeDef",
    {"Value": int, "Unit": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersUpdatedAtTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersUpdatedAtTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": GetInsightsPaginateResponseInsightsFiltersUpdatedAtDateRangeTypeDef,
    },
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersUserDefinedFieldsTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersUserDefinedFieldsTypeDef",
    {"Key": str, "Value": str, "Comparison": str},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersVerificationStateTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersVerificationStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersWorkflowStateTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersWorkflowStateTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX"]},
    total=False,
)

GetInsightsPaginateResponseInsightsFiltersTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsFiltersTypeDef",
    {
        "ProductArn": List[GetInsightsPaginateResponseInsightsFiltersProductArnTypeDef],
        "AwsAccountId": List[GetInsightsPaginateResponseInsightsFiltersAwsAccountIdTypeDef],
        "Id": List[GetInsightsPaginateResponseInsightsFiltersIdTypeDef],
        "GeneratorId": List[GetInsightsPaginateResponseInsightsFiltersGeneratorIdTypeDef],
        "Type": List[GetInsightsPaginateResponseInsightsFiltersTypeTypeDef],
        "FirstObservedAt": List[GetInsightsPaginateResponseInsightsFiltersFirstObservedAtTypeDef],
        "LastObservedAt": List[GetInsightsPaginateResponseInsightsFiltersLastObservedAtTypeDef],
        "CreatedAt": List[GetInsightsPaginateResponseInsightsFiltersCreatedAtTypeDef],
        "UpdatedAt": List[GetInsightsPaginateResponseInsightsFiltersUpdatedAtTypeDef],
        "SeverityProduct": List[GetInsightsPaginateResponseInsightsFiltersSeverityProductTypeDef],
        "SeverityNormalized": List[
            GetInsightsPaginateResponseInsightsFiltersSeverityNormalizedTypeDef
        ],
        "SeverityLabel": List[GetInsightsPaginateResponseInsightsFiltersSeverityLabelTypeDef],
        "Confidence": List[GetInsightsPaginateResponseInsightsFiltersConfidenceTypeDef],
        "Criticality": List[GetInsightsPaginateResponseInsightsFiltersCriticalityTypeDef],
        "Title": List[GetInsightsPaginateResponseInsightsFiltersTitleTypeDef],
        "Description": List[GetInsightsPaginateResponseInsightsFiltersDescriptionTypeDef],
        "RecommendationText": List[
            GetInsightsPaginateResponseInsightsFiltersRecommendationTextTypeDef
        ],
        "SourceUrl": List[GetInsightsPaginateResponseInsightsFiltersSourceUrlTypeDef],
        "ProductFields": List[GetInsightsPaginateResponseInsightsFiltersProductFieldsTypeDef],
        "ProductName": List[GetInsightsPaginateResponseInsightsFiltersProductNameTypeDef],
        "CompanyName": List[GetInsightsPaginateResponseInsightsFiltersCompanyNameTypeDef],
        "UserDefinedFields": List[
            GetInsightsPaginateResponseInsightsFiltersUserDefinedFieldsTypeDef
        ],
        "MalwareName": List[GetInsightsPaginateResponseInsightsFiltersMalwareNameTypeDef],
        "MalwareType": List[GetInsightsPaginateResponseInsightsFiltersMalwareTypeTypeDef],
        "MalwarePath": List[GetInsightsPaginateResponseInsightsFiltersMalwarePathTypeDef],
        "MalwareState": List[GetInsightsPaginateResponseInsightsFiltersMalwareStateTypeDef],
        "NetworkDirection": List[GetInsightsPaginateResponseInsightsFiltersNetworkDirectionTypeDef],
        "NetworkProtocol": List[GetInsightsPaginateResponseInsightsFiltersNetworkProtocolTypeDef],
        "NetworkSourceIpV4": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV4TypeDef
        ],
        "NetworkSourceIpV6": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkSourceIpV6TypeDef
        ],
        "NetworkSourcePort": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkSourcePortTypeDef
        ],
        "NetworkSourceDomain": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkSourceDomainTypeDef
        ],
        "NetworkSourceMac": List[GetInsightsPaginateResponseInsightsFiltersNetworkSourceMacTypeDef],
        "NetworkDestinationIpV4": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV4TypeDef
        ],
        "NetworkDestinationIpV6": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkDestinationIpV6TypeDef
        ],
        "NetworkDestinationPort": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkDestinationPortTypeDef
        ],
        "NetworkDestinationDomain": List[
            GetInsightsPaginateResponseInsightsFiltersNetworkDestinationDomainTypeDef
        ],
        "ProcessName": List[GetInsightsPaginateResponseInsightsFiltersProcessNameTypeDef],
        "ProcessPath": List[GetInsightsPaginateResponseInsightsFiltersProcessPathTypeDef],
        "ProcessPid": List[GetInsightsPaginateResponseInsightsFiltersProcessPidTypeDef],
        "ProcessParentPid": List[GetInsightsPaginateResponseInsightsFiltersProcessParentPidTypeDef],
        "ProcessLaunchedAt": List[
            GetInsightsPaginateResponseInsightsFiltersProcessLaunchedAtTypeDef
        ],
        "ProcessTerminatedAt": List[
            GetInsightsPaginateResponseInsightsFiltersProcessTerminatedAtTypeDef
        ],
        "ThreatIntelIndicatorType": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorTypeTypeDef
        ],
        "ThreatIntelIndicatorValue": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorValueTypeDef
        ],
        "ThreatIntelIndicatorCategory": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorCategoryTypeDef
        ],
        "ThreatIntelIndicatorLastObservedAt": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorLastObservedAtTypeDef
        ],
        "ThreatIntelIndicatorSource": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceTypeDef
        ],
        "ThreatIntelIndicatorSourceUrl": List[
            GetInsightsPaginateResponseInsightsFiltersThreatIntelIndicatorSourceUrlTypeDef
        ],
        "ResourceType": List[GetInsightsPaginateResponseInsightsFiltersResourceTypeTypeDef],
        "ResourceId": List[GetInsightsPaginateResponseInsightsFiltersResourceIdTypeDef],
        "ResourcePartition": List[
            GetInsightsPaginateResponseInsightsFiltersResourcePartitionTypeDef
        ],
        "ResourceRegion": List[GetInsightsPaginateResponseInsightsFiltersResourceRegionTypeDef],
        "ResourceTags": List[GetInsightsPaginateResponseInsightsFiltersResourceTagsTypeDef],
        "ResourceAwsEc2InstanceType": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceTypeTypeDef
        ],
        "ResourceAwsEc2InstanceImageId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceImageIdTypeDef
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV4AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIpV6AddressesTypeDef
        ],
        "ResourceAwsEc2InstanceKeyName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceKeyNameTypeDef
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceIamInstanceProfileArnTypeDef
        ],
        "ResourceAwsEc2InstanceVpcId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceVpcIdTypeDef
        ],
        "ResourceAwsEc2InstanceSubnetId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceSubnetIdTypeDef
        ],
        "ResourceAwsEc2InstanceLaunchedAt": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsEc2InstanceLaunchedAtTypeDef
        ],
        "ResourceAwsS3BucketOwnerId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerIdTypeDef
        ],
        "ResourceAwsS3BucketOwnerName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsS3BucketOwnerNameTypeDef
        ],
        "ResourceAwsIamAccessKeyUserName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyUserNameTypeDef
        ],
        "ResourceAwsIamAccessKeyStatus": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyStatusTypeDef
        ],
        "ResourceAwsIamAccessKeyCreatedAt": List[
            GetInsightsPaginateResponseInsightsFiltersResourceAwsIamAccessKeyCreatedAtTypeDef
        ],
        "ResourceContainerName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceContainerNameTypeDef
        ],
        "ResourceContainerImageId": List[
            GetInsightsPaginateResponseInsightsFiltersResourceContainerImageIdTypeDef
        ],
        "ResourceContainerImageName": List[
            GetInsightsPaginateResponseInsightsFiltersResourceContainerImageNameTypeDef
        ],
        "ResourceContainerLaunchedAt": List[
            GetInsightsPaginateResponseInsightsFiltersResourceContainerLaunchedAtTypeDef
        ],
        "ResourceDetailsOther": List[
            GetInsightsPaginateResponseInsightsFiltersResourceDetailsOtherTypeDef
        ],
        "ComplianceStatus": List[GetInsightsPaginateResponseInsightsFiltersComplianceStatusTypeDef],
        "VerificationState": List[
            GetInsightsPaginateResponseInsightsFiltersVerificationStateTypeDef
        ],
        "WorkflowState": List[GetInsightsPaginateResponseInsightsFiltersWorkflowStateTypeDef],
        "RecordState": List[GetInsightsPaginateResponseInsightsFiltersRecordStateTypeDef],
        "RelatedFindingsProductArn": List[
            GetInsightsPaginateResponseInsightsFiltersRelatedFindingsProductArnTypeDef
        ],
        "RelatedFindingsId": List[
            GetInsightsPaginateResponseInsightsFiltersRelatedFindingsIdTypeDef
        ],
        "NoteText": List[GetInsightsPaginateResponseInsightsFiltersNoteTextTypeDef],
        "NoteUpdatedAt": List[GetInsightsPaginateResponseInsightsFiltersNoteUpdatedAtTypeDef],
        "NoteUpdatedBy": List[GetInsightsPaginateResponseInsightsFiltersNoteUpdatedByTypeDef],
        "Keyword": List[GetInsightsPaginateResponseInsightsFiltersKeywordTypeDef],
    },
    total=False,
)

GetInsightsPaginateResponseInsightsTypeDef = TypedDict(
    "GetInsightsPaginateResponseInsightsTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": GetInsightsPaginateResponseInsightsFiltersTypeDef,
        "GroupByAttribute": str,
    },
    total=False,
)

GetInsightsPaginateResponseTypeDef = TypedDict(
    "GetInsightsPaginateResponseTypeDef",
    {"Insights": List[GetInsightsPaginateResponseInsightsTypeDef]},
    total=False,
)

ListEnabledProductsForImportPaginatePaginationConfigTypeDef = TypedDict(
    "ListEnabledProductsForImportPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListEnabledProductsForImportPaginateResponseTypeDef = TypedDict(
    "ListEnabledProductsForImportPaginateResponseTypeDef",
    {"ProductSubscriptions": List[str]},
    total=False,
)

ListInvitationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListInvitationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListInvitationsPaginateResponseInvitationsTypeDef = TypedDict(
    "ListInvitationsPaginateResponseInvitationsTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)

ListInvitationsPaginateResponseTypeDef = TypedDict(
    "ListInvitationsPaginateResponseTypeDef",
    {"Invitations": List[ListInvitationsPaginateResponseInvitationsTypeDef]},
    total=False,
)

ListMembersPaginatePaginationConfigTypeDef = TypedDict(
    "ListMembersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListMembersPaginateResponseMembersTypeDef = TypedDict(
    "ListMembersPaginateResponseMembersTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ListMembersPaginateResponseTypeDef = TypedDict(
    "ListMembersPaginateResponseTypeDef",
    {"Members": List[ListMembersPaginateResponseMembersTypeDef]},
    total=False,
)
