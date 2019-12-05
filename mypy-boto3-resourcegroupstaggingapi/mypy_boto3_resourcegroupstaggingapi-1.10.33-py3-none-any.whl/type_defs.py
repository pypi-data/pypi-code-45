"Main interface for resourcegroupstaggingapi service type defs"
from __future__ import annotations

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


ClientDescribeReportCreationResponseTypeDef = TypedDict(
    "ClientDescribeReportCreationResponseTypeDef",
    {"Status": str, "S3Location": str, "ErrorMessage": str},
    total=False,
)

ClientGetComplianceSummaryResponseSummaryListTypeDef = TypedDict(
    "ClientGetComplianceSummaryResponseSummaryListTypeDef",
    {
        "LastUpdated": str,
        "TargetId": str,
        "TargetIdType": Literal["ACCOUNT", "OU", "ROOT"],
        "Region": str,
        "ResourceType": str,
        "NonCompliantResources": int,
    },
    total=False,
)

ClientGetComplianceSummaryResponseTypeDef = TypedDict(
    "ClientGetComplianceSummaryResponseTypeDef",
    {
        "SummaryList": List[ClientGetComplianceSummaryResponseSummaryListTypeDef],
        "PaginationToken": str,
    },
    total=False,
)

ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef = TypedDict(
    "ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef",
    {
        "NoncompliantKeys": List[str],
        "KeysWithNoncompliantValues": List[str],
        "ComplianceStatus": bool,
    },
    total=False,
)

ClientGetResourcesResponseResourceTagMappingListTagsTypeDef = TypedDict(
    "ClientGetResourcesResponseResourceTagMappingListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetResourcesResponseResourceTagMappingListTypeDef = TypedDict(
    "ClientGetResourcesResponseResourceTagMappingListTypeDef",
    {
        "ResourceARN": str,
        "Tags": List[ClientGetResourcesResponseResourceTagMappingListTagsTypeDef],
        "ComplianceDetails": ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef,
    },
    total=False,
)

ClientGetResourcesResponseTypeDef = TypedDict(
    "ClientGetResourcesResponseTypeDef",
    {
        "PaginationToken": str,
        "ResourceTagMappingList": List[ClientGetResourcesResponseResourceTagMappingListTypeDef],
    },
    total=False,
)

ClientGetResourcesTagFiltersTypeDef = TypedDict(
    "ClientGetResourcesTagFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientGetTagKeysResponseTypeDef = TypedDict(
    "ClientGetTagKeysResponseTypeDef", {"PaginationToken": str, "TagKeys": List[str]}, total=False
)

ClientGetTagValuesResponseTypeDef = TypedDict(
    "ClientGetTagValuesResponseTypeDef",
    {"PaginationToken": str, "TagValues": List[str]},
    total=False,
)

ClientTagResourcesResponseFailedResourcesMapTypeDef = TypedDict(
    "ClientTagResourcesResponseFailedResourcesMapTypeDef",
    {
        "StatusCode": int,
        "ErrorCode": Literal["InternalServiceException", "InvalidParameterException"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientTagResourcesResponseTypeDef = TypedDict(
    "ClientTagResourcesResponseTypeDef",
    {"FailedResourcesMap": Dict[str, ClientTagResourcesResponseFailedResourcesMapTypeDef]},
    total=False,
)

ClientUntagResourcesResponseFailedResourcesMapTypeDef = TypedDict(
    "ClientUntagResourcesResponseFailedResourcesMapTypeDef",
    {
        "StatusCode": int,
        "ErrorCode": Literal["InternalServiceException", "InvalidParameterException"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientUntagResourcesResponseTypeDef = TypedDict(
    "ClientUntagResourcesResponseTypeDef",
    {"FailedResourcesMap": Dict[str, ClientUntagResourcesResponseFailedResourcesMapTypeDef]},
    total=False,
)

GetComplianceSummaryPaginatePaginationConfigTypeDef = TypedDict(
    "GetComplianceSummaryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetComplianceSummaryPaginateResponseSummaryListTypeDef = TypedDict(
    "GetComplianceSummaryPaginateResponseSummaryListTypeDef",
    {
        "LastUpdated": str,
        "TargetId": str,
        "TargetIdType": Literal["ACCOUNT", "OU", "ROOT"],
        "Region": str,
        "ResourceType": str,
        "NonCompliantResources": int,
    },
    total=False,
)

GetComplianceSummaryPaginateResponseTypeDef = TypedDict(
    "GetComplianceSummaryPaginateResponseTypeDef",
    {"SummaryList": List[GetComplianceSummaryPaginateResponseSummaryListTypeDef], "NextToken": str},
    total=False,
)

GetResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "GetResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetResourcesPaginateResponseResourceTagMappingListComplianceDetailsTypeDef = TypedDict(
    "GetResourcesPaginateResponseResourceTagMappingListComplianceDetailsTypeDef",
    {
        "NoncompliantKeys": List[str],
        "KeysWithNoncompliantValues": List[str],
        "ComplianceStatus": bool,
    },
    total=False,
)

GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef = TypedDict(
    "GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

GetResourcesPaginateResponseResourceTagMappingListTypeDef = TypedDict(
    "GetResourcesPaginateResponseResourceTagMappingListTypeDef",
    {
        "ResourceARN": str,
        "Tags": List[GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef],
        "ComplianceDetails": GetResourcesPaginateResponseResourceTagMappingListComplianceDetailsTypeDef,
    },
    total=False,
)

GetResourcesPaginateResponseTypeDef = TypedDict(
    "GetResourcesPaginateResponseTypeDef",
    {
        "ResourceTagMappingList": List[GetResourcesPaginateResponseResourceTagMappingListTypeDef],
        "NextToken": str,
    },
    total=False,
)

GetResourcesPaginateTagFiltersTypeDef = TypedDict(
    "GetResourcesPaginateTagFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

GetTagKeysPaginatePaginationConfigTypeDef = TypedDict(
    "GetTagKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetTagKeysPaginateResponseTypeDef = TypedDict(
    "GetTagKeysPaginateResponseTypeDef", {"TagKeys": List[str], "NextToken": str}, total=False
)

GetTagValuesPaginatePaginationConfigTypeDef = TypedDict(
    "GetTagValuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetTagValuesPaginateResponseTypeDef = TypedDict(
    "GetTagValuesPaginateResponseTypeDef", {"TagValues": List[str], "NextToken": str}, total=False
)
