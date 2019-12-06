"Main interface for alexaforbusiness service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_alexaforbusiness.type_defs import (
    ListBusinessReportSchedulesPaginatePaginationConfigTypeDef,
    ListBusinessReportSchedulesPaginateResponseTypeDef,
    ListConferenceProvidersPaginatePaginationConfigTypeDef,
    ListConferenceProvidersPaginateResponseTypeDef,
    ListDeviceEventsPaginatePaginationConfigTypeDef,
    ListDeviceEventsPaginateResponseTypeDef,
    ListSkillsPaginatePaginationConfigTypeDef,
    ListSkillsPaginateResponseTypeDef,
    ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef,
    ListSkillsStoreCategoriesPaginateResponseTypeDef,
    ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef,
    ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef,
    ListSmartHomeAppliancesPaginatePaginationConfigTypeDef,
    ListSmartHomeAppliancesPaginateResponseTypeDef,
    ListTagsPaginatePaginationConfigTypeDef,
    ListTagsPaginateResponseTypeDef,
    SearchDevicesPaginateFiltersTypeDef,
    SearchDevicesPaginatePaginationConfigTypeDef,
    SearchDevicesPaginateResponseTypeDef,
    SearchDevicesPaginateSortCriteriaTypeDef,
    SearchProfilesPaginateFiltersTypeDef,
    SearchProfilesPaginatePaginationConfigTypeDef,
    SearchProfilesPaginateResponseTypeDef,
    SearchProfilesPaginateSortCriteriaTypeDef,
    SearchRoomsPaginateFiltersTypeDef,
    SearchRoomsPaginatePaginationConfigTypeDef,
    SearchRoomsPaginateResponseTypeDef,
    SearchRoomsPaginateSortCriteriaTypeDef,
    SearchSkillGroupsPaginateFiltersTypeDef,
    SearchSkillGroupsPaginatePaginationConfigTypeDef,
    SearchSkillGroupsPaginateResponseTypeDef,
    SearchSkillGroupsPaginateSortCriteriaTypeDef,
    SearchUsersPaginateFiltersTypeDef,
    SearchUsersPaginatePaginationConfigTypeDef,
    SearchUsersPaginateResponseTypeDef,
    SearchUsersPaginateSortCriteriaTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListBusinessReportSchedulesPaginator",
    "ListConferenceProvidersPaginator",
    "ListDeviceEventsPaginator",
    "ListSkillsPaginator",
    "ListSkillsStoreCategoriesPaginator",
    "ListSkillsStoreSkillsByCategoryPaginator",
    "ListSmartHomeAppliancesPaginator",
    "ListTagsPaginator",
    "SearchDevicesPaginator",
    "SearchProfilesPaginator",
    "SearchRoomsPaginator",
    "SearchSkillGroupsPaginator",
    "SearchUsersPaginator",
)


class ListBusinessReportSchedulesPaginator(Boto3Paginator):
    """
    Paginator for `list_business_report_schedules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListBusinessReportSchedulesPaginatePaginationConfigTypeDef = None
    ) -> ListBusinessReportSchedulesPaginateResponseTypeDef:
        """
        [ListBusinessReportSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListBusinessReportSchedules.paginate)
        """


class ListConferenceProvidersPaginator(Boto3Paginator):
    """
    Paginator for `list_conference_providers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListConferenceProvidersPaginatePaginationConfigTypeDef = None
    ) -> ListConferenceProvidersPaginateResponseTypeDef:
        """
        [ListConferenceProviders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListConferenceProviders.paginate)
        """


class ListDeviceEventsPaginator(Boto3Paginator):
    """
    Paginator for `list_device_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DeviceArn: str,
        EventType: Literal["CONNECTION_STATUS", "DEVICE_STATUS"] = None,
        PaginationConfig: ListDeviceEventsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeviceEventsPaginateResponseTypeDef:
        """
        [ListDeviceEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListDeviceEvents.paginate)
        """


class ListSkillsPaginator(Boto3Paginator):
    """
    Paginator for `list_skills`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SkillGroupArn: str = None,
        EnablementType: Literal["ENABLED", "PENDING"] = None,
        SkillType: Literal["PUBLIC", "PRIVATE", "ALL"] = None,
        PaginationConfig: ListSkillsPaginatePaginationConfigTypeDef = None,
    ) -> ListSkillsPaginateResponseTypeDef:
        """
        [ListSkills.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkills.paginate)
        """


class ListSkillsStoreCategoriesPaginator(Boto3Paginator):
    """
    Paginator for `list_skills_store_categories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef = None
    ) -> ListSkillsStoreCategoriesPaginateResponseTypeDef:
        """
        [ListSkillsStoreCategories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreCategories.paginate)
        """


class ListSkillsStoreSkillsByCategoryPaginator(Boto3Paginator):
    """
    Paginator for `list_skills_store_skills_by_category`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CategoryId: int,
        PaginationConfig: ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef = None,
    ) -> ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef:
        """
        [ListSkillsStoreSkillsByCategory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreSkillsByCategory.paginate)
        """


class ListSmartHomeAppliancesPaginator(Boto3Paginator):
    """
    Paginator for `list_smart_home_appliances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RoomArn: str,
        PaginationConfig: ListSmartHomeAppliancesPaginatePaginationConfigTypeDef = None,
    ) -> ListSmartHomeAppliancesPaginateResponseTypeDef:
        """
        [ListSmartHomeAppliances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSmartHomeAppliances.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    Paginator for `list_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Arn: str, PaginationConfig: ListTagsPaginatePaginationConfigTypeDef = None
    ) -> ListTagsPaginateResponseTypeDef:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListTags.paginate)
        """


class SearchDevicesPaginator(Boto3Paginator):
    """
    Paginator for `search_devices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchDevicesPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchDevicesPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchDevicesPaginatePaginationConfigTypeDef = None,
    ) -> SearchDevicesPaginateResponseTypeDef:
        """
        [SearchDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchDevices.paginate)
        """


class SearchProfilesPaginator(Boto3Paginator):
    """
    Paginator for `search_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchProfilesPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchProfilesPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchProfilesPaginatePaginationConfigTypeDef = None,
    ) -> SearchProfilesPaginateResponseTypeDef:
        """
        [SearchProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchProfiles.paginate)
        """


class SearchRoomsPaginator(Boto3Paginator):
    """
    Paginator for `search_rooms`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchRoomsPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchRoomsPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchRoomsPaginatePaginationConfigTypeDef = None,
    ) -> SearchRoomsPaginateResponseTypeDef:
        """
        [SearchRooms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchRooms.paginate)
        """


class SearchSkillGroupsPaginator(Boto3Paginator):
    """
    Paginator for `search_skill_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchSkillGroupsPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchSkillGroupsPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchSkillGroupsPaginatePaginationConfigTypeDef = None,
    ) -> SearchSkillGroupsPaginateResponseTypeDef:
        """
        [SearchSkillGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchSkillGroups.paginate)
        """


class SearchUsersPaginator(Boto3Paginator):
    """
    Paginator for `search_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchUsersPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchUsersPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchUsersPaginatePaginationConfigTypeDef = None,
    ) -> SearchUsersPaginateResponseTypeDef:
        """
        [SearchUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchUsers.paginate)
        """
