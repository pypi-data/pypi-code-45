"Main interface for connect service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_connect.type_defs import (
    GetMetricDataPaginateFiltersTypeDef,
    GetMetricDataPaginateHistoricalMetricsTypeDef,
    GetMetricDataPaginatePaginationConfigTypeDef,
    GetMetricDataPaginateResponseTypeDef,
    ListContactFlowsPaginatePaginationConfigTypeDef,
    ListContactFlowsPaginateResponseTypeDef,
    ListHoursOfOperationsPaginatePaginationConfigTypeDef,
    ListHoursOfOperationsPaginateResponseTypeDef,
    ListPhoneNumbersPaginatePaginationConfigTypeDef,
    ListPhoneNumbersPaginateResponseTypeDef,
    ListQueuesPaginatePaginationConfigTypeDef,
    ListQueuesPaginateResponseTypeDef,
    ListRoutingProfilesPaginatePaginationConfigTypeDef,
    ListRoutingProfilesPaginateResponseTypeDef,
    ListSecurityProfilesPaginatePaginationConfigTypeDef,
    ListSecurityProfilesPaginateResponseTypeDef,
    ListUserHierarchyGroupsPaginatePaginationConfigTypeDef,
    ListUserHierarchyGroupsPaginateResponseTypeDef,
    ListUsersPaginatePaginationConfigTypeDef,
    ListUsersPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetMetricDataPaginator",
    "ListContactFlowsPaginator",
    "ListHoursOfOperationsPaginator",
    "ListPhoneNumbersPaginator",
    "ListQueuesPaginator",
    "ListRoutingProfilesPaginator",
    "ListSecurityProfilesPaginator",
    "ListUserHierarchyGroupsPaginator",
    "ListUsersPaginator",
)


class GetMetricDataPaginator(Boto3Paginator):
    """
    Paginator for `get_metric_data`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: GetMetricDataPaginateFiltersTypeDef,
        HistoricalMetrics: List[GetMetricDataPaginateHistoricalMetricsTypeDef],
        Groupings: List[Literal["QUEUE", "CHANNEL"]] = None,
        PaginationConfig: GetMetricDataPaginatePaginationConfigTypeDef = None,
    ) -> GetMetricDataPaginateResponseTypeDef:
        """
        [GetMetricData.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/connect.html#Connect.Paginator.GetMetricData.paginate)
        """


class ListContactFlowsPaginator(Boto3Paginator):
    """
    Paginator for `list_contact_flows`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        ContactFlowTypes: List[
            Literal[
                "CONTACT_FLOW",
                "CUSTOMER_QUEUE",
                "CUSTOMER_HOLD",
                "CUSTOMER_WHISPER",
                "AGENT_HOLD",
                "AGENT_WHISPER",
                "OUTBOUND_WHISPER",
                "AGENT_TRANSFER",
                "QUEUE_TRANSFER",
            ]
        ] = None,
        PaginationConfig: ListContactFlowsPaginatePaginationConfigTypeDef = None,
    ) -> ListContactFlowsPaginateResponseTypeDef:
        """
        [ListContactFlows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/connect.html#Connect.Paginator.ListContactFlows.paginate)
        """


class ListHoursOfOperationsPaginator(Boto3Paginator):
    """
    Paginator for `list_hours_of_operations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: ListHoursOfOperationsPaginatePaginationConfigTypeDef = None,
    ) -> ListHoursOfOperationsPaginateResponseTypeDef:
        """
        [ListHoursOfOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations.paginate)
        """


class ListPhoneNumbersPaginator(Boto3Paginator):
    """
    Paginator for `list_phone_numbers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PhoneNumberTypes: List[Literal["TOLL_FREE", "DID"]] = None,
        PhoneNumberCountryCodes: List[
            Literal[
                "AF",
                "AL",
                "DZ",
                "AS",
                "AD",
                "AO",
                "AI",
                "AQ",
                "AG",
                "AR",
                "AM",
                "AW",
                "AU",
                "AT",
                "AZ",
                "BS",
                "BH",
                "BD",
                "BB",
                "BY",
                "BE",
                "BZ",
                "BJ",
                "BM",
                "BT",
                "BO",
                "BA",
                "BW",
                "BR",
                "IO",
                "VG",
                "BN",
                "BG",
                "BF",
                "BI",
                "KH",
                "CM",
                "CA",
                "CV",
                "KY",
                "CF",
                "TD",
                "CL",
                "CN",
                "CX",
                "CC",
                "CO",
                "KM",
                "CK",
                "CR",
                "HR",
                "CU",
                "CW",
                "CY",
                "CZ",
                "CD",
                "DK",
                "DJ",
                "DM",
                "DO",
                "TL",
                "EC",
                "EG",
                "SV",
                "GQ",
                "ER",
                "EE",
                "ET",
                "FK",
                "FO",
                "FJ",
                "FI",
                "FR",
                "PF",
                "GA",
                "GM",
                "GE",
                "DE",
                "GH",
                "GI",
                "GR",
                "GL",
                "GD",
                "GU",
                "GT",
                "GG",
                "GN",
                "GW",
                "GY",
                "HT",
                "HN",
                "HK",
                "HU",
                "IS",
                "IN",
                "ID",
                "IR",
                "IQ",
                "IE",
                "IM",
                "IL",
                "IT",
                "CI",
                "JM",
                "JP",
                "JE",
                "JO",
                "KZ",
                "KE",
                "KI",
                "KW",
                "KG",
                "LA",
                "LV",
                "LB",
                "LS",
                "LR",
                "LY",
                "LI",
                "LT",
                "LU",
                "MO",
                "MK",
                "MG",
                "MW",
                "MY",
                "MV",
                "ML",
                "MT",
                "MH",
                "MR",
                "MU",
                "YT",
                "MX",
                "FM",
                "MD",
                "MC",
                "MN",
                "ME",
                "MS",
                "MA",
                "MZ",
                "MM",
                "NA",
                "NR",
                "NP",
                "NL",
                "AN",
                "NC",
                "NZ",
                "NI",
                "NE",
                "NG",
                "NU",
                "KP",
                "MP",
                "NO",
                "OM",
                "PK",
                "PW",
                "PA",
                "PG",
                "PY",
                "PE",
                "PH",
                "PN",
                "PL",
                "PT",
                "PR",
                "QA",
                "CG",
                "RE",
                "RO",
                "RU",
                "RW",
                "BL",
                "SH",
                "KN",
                "LC",
                "MF",
                "PM",
                "VC",
                "WS",
                "SM",
                "ST",
                "SA",
                "SN",
                "RS",
                "SC",
                "SL",
                "SG",
                "SX",
                "SK",
                "SI",
                "SB",
                "SO",
                "ZA",
                "KR",
                "ES",
                "LK",
                "SD",
                "SR",
                "SJ",
                "SZ",
                "SE",
                "CH",
                "SY",
                "TW",
                "TJ",
                "TZ",
                "TH",
                "TG",
                "TK",
                "TO",
                "TT",
                "TN",
                "TR",
                "TM",
                "TC",
                "TV",
                "VI",
                "UG",
                "UA",
                "AE",
                "GB",
                "US",
                "UY",
                "UZ",
                "VU",
                "VA",
                "VE",
                "VN",
                "WF",
                "EH",
                "YE",
                "ZM",
                "ZW",
            ]
        ] = None,
        PaginationConfig: ListPhoneNumbersPaginatePaginationConfigTypeDef = None,
    ) -> ListPhoneNumbersPaginateResponseTypeDef:
        """
        [ListPhoneNumbers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers.paginate)
        """


class ListQueuesPaginator(Boto3Paginator):
    """
    Paginator for `list_queues`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        QueueTypes: List[Literal["STANDARD", "AGENT"]] = None,
        PaginationConfig: ListQueuesPaginatePaginationConfigTypeDef = None,
    ) -> ListQueuesPaginateResponseTypeDef:
        """
        [ListQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/connect.html#Connect.Paginator.ListQueues.paginate)
        """


class ListRoutingProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_routing_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: ListRoutingProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListRoutingProfilesPaginateResponseTypeDef:
        """
        [ListRoutingProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles.paginate)
        """


class ListSecurityProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_security_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: ListSecurityProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListSecurityProfilesPaginateResponseTypeDef:
        """
        [ListSecurityProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles.paginate)
        """


class ListUserHierarchyGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_user_hierarchy_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: ListUserHierarchyGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListUserHierarchyGroupsPaginateResponseTypeDef:
        """
        [ListUserHierarchyGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    Paginator for `list_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, InstanceId: str, PaginationConfig: ListUsersPaginatePaginationConfigTypeDef = None
    ) -> ListUsersPaginateResponseTypeDef:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/connect.html#Connect.Paginator.ListUsers.paginate)
        """
