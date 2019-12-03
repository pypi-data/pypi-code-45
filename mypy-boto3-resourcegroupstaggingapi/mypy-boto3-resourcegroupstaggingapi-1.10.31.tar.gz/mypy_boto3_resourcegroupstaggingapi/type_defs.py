"Main interface for resourcegroupstaggingapi service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeReportCreationResponseTypeDef",
    "ClientGetComplianceSummaryResponseSummaryListTypeDef",
    "ClientGetComplianceSummaryResponseTypeDef",
    "ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef",
    "ClientGetResourcesResponseResourceTagMappingListTagsTypeDef",
    "ClientGetResourcesResponseResourceTagMappingListTypeDef",
    "ClientGetResourcesResponseTypeDef",
    "ClientGetResourcesTagFiltersTypeDef",
    "ClientGetTagKeysResponseTypeDef",
    "ClientGetTagValuesResponseTypeDef",
    "ClientTagResourcesResponseFailedResourcesMapTypeDef",
    "ClientTagResourcesResponseTypeDef",
    "ClientUntagResourcesResponseFailedResourcesMapTypeDef",
    "ClientUntagResourcesResponseTypeDef",
    "GetComplianceSummaryPaginatePaginationConfigTypeDef",
    "GetComplianceSummaryPaginateResponseSummaryListTypeDef",
    "GetComplianceSummaryPaginateResponseTypeDef",
    "GetResourcesPaginatePaginationConfigTypeDef",
    "GetResourcesPaginateResponseResourceTagMappingListComplianceDetailsTypeDef",
    "GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef",
    "GetResourcesPaginateResponseResourceTagMappingListTypeDef",
    "GetResourcesPaginateResponseTypeDef",
    "GetResourcesPaginateTagFiltersTypeDef",
    "GetTagKeysPaginatePaginationConfigTypeDef",
    "GetTagKeysPaginateResponseTypeDef",
    "GetTagValuesPaginatePaginationConfigTypeDef",
    "GetTagValuesPaginateResponseTypeDef",
)


_ClientDescribeReportCreationResponseTypeDef = TypedDict(
    "_ClientDescribeReportCreationResponseTypeDef",
    {"Status": str, "S3Location": str, "ErrorMessage": str},
    total=False,
)


class ClientDescribeReportCreationResponseTypeDef(_ClientDescribeReportCreationResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        Reports the status of the operation.
        The operation status can be one of the following:
        * ``RUNNING`` - Report creation is in progress.
        * ``SUCCEEDED`` - Report creation is complete. You can open the report from the Amazon S3
        bucket that you specified when you ran ``StartReportCreation`` .
        * ``FAILED`` - Report creation timed out or the Amazon S3 bucket is not accessible.
        * ``NO REPORT`` - No report was generated in the last 90 days.
    """


_ClientGetComplianceSummaryResponseSummaryListTypeDef = TypedDict(
    "_ClientGetComplianceSummaryResponseSummaryListTypeDef",
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


class ClientGetComplianceSummaryResponseSummaryListTypeDef(
    _ClientGetComplianceSummaryResponseSummaryListTypeDef
):
    """
    - *(dict) --*

      A count of noncompliant resources.
      - **LastUpdated** *(string) --*

        The timestamp that shows when this summary was generated in this Region.
    """


_ClientGetComplianceSummaryResponseTypeDef = TypedDict(
    "_ClientGetComplianceSummaryResponseTypeDef",
    {
        "SummaryList": List[ClientGetComplianceSummaryResponseSummaryListTypeDef],
        "PaginationToken": str,
    },
    total=False,
)


class ClientGetComplianceSummaryResponseTypeDef(_ClientGetComplianceSummaryResponseTypeDef):
    """
    - *(dict) --*

      - **SummaryList** *(list) --*

        A table that shows counts of noncompliant resources.
        - *(dict) --*

          A count of noncompliant resources.
          - **LastUpdated** *(string) --*

            The timestamp that shows when this summary was generated in this Region.
    """


_ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef = TypedDict(
    "_ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef",
    {
        "NoncompliantKeys": List[str],
        "KeysWithNoncompliantValues": List[str],
        "ComplianceStatus": bool,
    },
    total=False,
)


class ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef(
    _ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef
):
    pass


_ClientGetResourcesResponseResourceTagMappingListTagsTypeDef = TypedDict(
    "_ClientGetResourcesResponseResourceTagMappingListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetResourcesResponseResourceTagMappingListTagsTypeDef(
    _ClientGetResourcesResponseResourceTagMappingListTagsTypeDef
):
    pass


_ClientGetResourcesResponseResourceTagMappingListTypeDef = TypedDict(
    "_ClientGetResourcesResponseResourceTagMappingListTypeDef",
    {
        "ResourceARN": str,
        "Tags": List[ClientGetResourcesResponseResourceTagMappingListTagsTypeDef],
        "ComplianceDetails": ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef,
    },
    total=False,
)


class ClientGetResourcesResponseResourceTagMappingListTypeDef(
    _ClientGetResourcesResponseResourceTagMappingListTypeDef
):
    pass


_ClientGetResourcesResponseTypeDef = TypedDict(
    "_ClientGetResourcesResponseTypeDef",
    {
        "PaginationToken": str,
        "ResourceTagMappingList": List[ClientGetResourcesResponseResourceTagMappingListTypeDef],
    },
    total=False,
)


class ClientGetResourcesResponseTypeDef(_ClientGetResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **PaginationToken** *(string) --*

        A string that indicates that the response contains more data than can be returned in a
        single response. To receive additional data, specify this string for the ``PaginationToken``
        value in a subsequent request.
    """


_ClientGetResourcesTagFiltersTypeDef = TypedDict(
    "_ClientGetResourcesTagFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientGetResourcesTagFiltersTypeDef(_ClientGetResourcesTagFiltersTypeDef):
    pass


_ClientGetTagKeysResponseTypeDef = TypedDict(
    "_ClientGetTagKeysResponseTypeDef", {"PaginationToken": str, "TagKeys": List[str]}, total=False
)


class ClientGetTagKeysResponseTypeDef(_ClientGetTagKeysResponseTypeDef):
    """
    - *(dict) --*

      - **PaginationToken** *(string) --*

        A string that indicates that the response contains more data than can be returned in a
        single response. To receive additional data, specify this string for the ``PaginationToken``
        value in a subsequent request.
    """


_ClientGetTagValuesResponseTypeDef = TypedDict(
    "_ClientGetTagValuesResponseTypeDef",
    {"PaginationToken": str, "TagValues": List[str]},
    total=False,
)


class ClientGetTagValuesResponseTypeDef(_ClientGetTagValuesResponseTypeDef):
    """
    - *(dict) --*

      - **PaginationToken** *(string) --*

        A string that indicates that the response contains more data than can be returned in a
        single response. To receive additional data, specify this string for the ``PaginationToken``
        value in a subsequent request.
    """


_ClientTagResourcesResponseFailedResourcesMapTypeDef = TypedDict(
    "_ClientTagResourcesResponseFailedResourcesMapTypeDef",
    {
        "StatusCode": int,
        "ErrorCode": Literal["InternalServiceException", "InvalidParameterException"],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientTagResourcesResponseFailedResourcesMapTypeDef(
    _ClientTagResourcesResponseFailedResourcesMapTypeDef
):
    pass


_ClientTagResourcesResponseTypeDef = TypedDict(
    "_ClientTagResourcesResponseTypeDef",
    {"FailedResourcesMap": Dict[str, ClientTagResourcesResponseFailedResourcesMapTypeDef]},
    total=False,
)


class ClientTagResourcesResponseTypeDef(_ClientTagResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **FailedResourcesMap** *(dict) --*

        Details of resources that could not be tagged. An error code, status code, and error message
        are returned for each failed item.
        - *(string) --*

          - *(dict) --*

            Details of the common errors that all actions return.
            - **StatusCode** *(integer) --*

              The HTTP status code of the common error.
    """


_ClientUntagResourcesResponseFailedResourcesMapTypeDef = TypedDict(
    "_ClientUntagResourcesResponseFailedResourcesMapTypeDef",
    {
        "StatusCode": int,
        "ErrorCode": Literal["InternalServiceException", "InvalidParameterException"],
        "ErrorMessage": str,
    },
    total=False,
)


class ClientUntagResourcesResponseFailedResourcesMapTypeDef(
    _ClientUntagResourcesResponseFailedResourcesMapTypeDef
):
    pass


_ClientUntagResourcesResponseTypeDef = TypedDict(
    "_ClientUntagResourcesResponseTypeDef",
    {"FailedResourcesMap": Dict[str, ClientUntagResourcesResponseFailedResourcesMapTypeDef]},
    total=False,
)


class ClientUntagResourcesResponseTypeDef(_ClientUntagResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **FailedResourcesMap** *(dict) --*

        Details of resources that could not be untagged. An error code, status code, and error
        message are returned for each failed item.
        - *(string) --*

          - *(dict) --*

            Details of the common errors that all actions return.
            - **StatusCode** *(integer) --*

              The HTTP status code of the common error.
    """


_GetComplianceSummaryPaginatePaginationConfigTypeDef = TypedDict(
    "_GetComplianceSummaryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetComplianceSummaryPaginatePaginationConfigTypeDef(
    _GetComplianceSummaryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetComplianceSummaryPaginateResponseSummaryListTypeDef = TypedDict(
    "_GetComplianceSummaryPaginateResponseSummaryListTypeDef",
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


class GetComplianceSummaryPaginateResponseSummaryListTypeDef(
    _GetComplianceSummaryPaginateResponseSummaryListTypeDef
):
    """
    - *(dict) --*

      A count of noncompliant resources.
      - **LastUpdated** *(string) --*

        The timestamp that shows when this summary was generated in this Region.
    """


_GetComplianceSummaryPaginateResponseTypeDef = TypedDict(
    "_GetComplianceSummaryPaginateResponseTypeDef",
    {"SummaryList": List[GetComplianceSummaryPaginateResponseSummaryListTypeDef], "NextToken": str},
    total=False,
)


class GetComplianceSummaryPaginateResponseTypeDef(_GetComplianceSummaryPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SummaryList** *(list) --*

        A table that shows counts of noncompliant resources.
        - *(dict) --*

          A count of noncompliant resources.
          - **LastUpdated** *(string) --*

            The timestamp that shows when this summary was generated in this Region.
    """


_GetResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourcesPaginatePaginationConfigTypeDef(_GetResourcesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetResourcesPaginateResponseResourceTagMappingListComplianceDetailsTypeDef = TypedDict(
    "_GetResourcesPaginateResponseResourceTagMappingListComplianceDetailsTypeDef",
    {
        "NoncompliantKeys": List[str],
        "KeysWithNoncompliantValues": List[str],
        "ComplianceStatus": bool,
    },
    total=False,
)


class GetResourcesPaginateResponseResourceTagMappingListComplianceDetailsTypeDef(
    _GetResourcesPaginateResponseResourceTagMappingListComplianceDetailsTypeDef
):
    pass


_GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef = TypedDict(
    "_GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef(
    _GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef
):
    pass


_GetResourcesPaginateResponseResourceTagMappingListTypeDef = TypedDict(
    "_GetResourcesPaginateResponseResourceTagMappingListTypeDef",
    {
        "ResourceARN": str,
        "Tags": List[GetResourcesPaginateResponseResourceTagMappingListTagsTypeDef],
        "ComplianceDetails": GetResourcesPaginateResponseResourceTagMappingListComplianceDetailsTypeDef,
    },
    total=False,
)


class GetResourcesPaginateResponseResourceTagMappingListTypeDef(
    _GetResourcesPaginateResponseResourceTagMappingListTypeDef
):
    """
    - *(dict) --*

      A list of resource ARNs and the tags (keys and values) that are associated with each.
      - **ResourceARN** *(string) --*

        The ARN of the resource.
    """


_GetResourcesPaginateResponseTypeDef = TypedDict(
    "_GetResourcesPaginateResponseTypeDef",
    {
        "ResourceTagMappingList": List[GetResourcesPaginateResponseResourceTagMappingListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetResourcesPaginateResponseTypeDef(_GetResourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceTagMappingList** *(list) --*

        A list of resource ARNs and the tags (keys and values) associated with each.
        - *(dict) --*

          A list of resource ARNs and the tags (keys and values) that are associated with each.
          - **ResourceARN** *(string) --*

            The ARN of the resource.
    """


_GetResourcesPaginateTagFiltersTypeDef = TypedDict(
    "_GetResourcesPaginateTagFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class GetResourcesPaginateTagFiltersTypeDef(_GetResourcesPaginateTagFiltersTypeDef):
    pass


_GetTagKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTagKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTagKeysPaginatePaginationConfigTypeDef(_GetTagKeysPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetTagKeysPaginateResponseTypeDef = TypedDict(
    "_GetTagKeysPaginateResponseTypeDef", {"TagKeys": List[str], "NextToken": str}, total=False
)


class GetTagKeysPaginateResponseTypeDef(_GetTagKeysPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TagKeys** *(list) --*

        A list of all tag keys in the AWS account.
        - *(string) --*
    """


_GetTagValuesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTagValuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTagValuesPaginatePaginationConfigTypeDef(_GetTagValuesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetTagValuesPaginateResponseTypeDef = TypedDict(
    "_GetTagValuesPaginateResponseTypeDef", {"TagValues": List[str], "NextToken": str}, total=False
)


class GetTagValuesPaginateResponseTypeDef(_GetTagValuesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TagValues** *(list) --*

        A list of all tag values for the specified key in the AWS account.
        - *(string) --*
    """
