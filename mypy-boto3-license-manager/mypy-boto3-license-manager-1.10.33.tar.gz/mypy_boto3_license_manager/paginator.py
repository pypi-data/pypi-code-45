"Main interface for license-manager service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_license_manager.type_defs import (
    ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef,
    ListAssociationsForLicenseConfigurationPaginateResponseTypeDef,
    ListLicenseConfigurationsPaginateFiltersTypeDef,
    ListLicenseConfigurationsPaginatePaginationConfigTypeDef,
    ListLicenseConfigurationsPaginateResponseTypeDef,
    ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef,
    ListLicenseSpecificationsForResourcePaginateResponseTypeDef,
    ListResourceInventoryPaginateFiltersTypeDef,
    ListResourceInventoryPaginatePaginationConfigTypeDef,
    ListResourceInventoryPaginateResponseTypeDef,
    ListUsageForLicenseConfigurationPaginateFiltersTypeDef,
    ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef,
    ListUsageForLicenseConfigurationPaginateResponseTypeDef,
)


__all__ = (
    "ListAssociationsForLicenseConfigurationPaginator",
    "ListLicenseConfigurationsPaginator",
    "ListLicenseSpecificationsForResourcePaginator",
    "ListResourceInventoryPaginator",
    "ListUsageForLicenseConfigurationPaginator",
)


class ListAssociationsForLicenseConfigurationPaginator(Boto3Paginator):
    """
    Paginator for `list_associations_for_license_configuration`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LicenseConfigurationArn: str,
        PaginationConfig: ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef = None,
    ) -> ListAssociationsForLicenseConfigurationPaginateResponseTypeDef:
        """
        [ListAssociationsForLicenseConfiguration.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration.paginate)
        """


class ListLicenseConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_license_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LicenseConfigurationArns: List[str] = None,
        Filters: List[ListLicenseConfigurationsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListLicenseConfigurationsPaginatePaginationConfigTypeDef = None,
    ) -> ListLicenseConfigurationsPaginateResponseTypeDef:
        """
        [ListLicenseConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations.paginate)
        """


class ListLicenseSpecificationsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_license_specifications_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListLicenseSpecificationsForResourcePaginateResponseTypeDef:
        """
        [ListLicenseSpecificationsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource.paginate)
        """


class ListResourceInventoryPaginator(Boto3Paginator):
    """
    Paginator for `list_resource_inventory`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListResourceInventoryPaginateFiltersTypeDef] = None,
        PaginationConfig: ListResourceInventoryPaginatePaginationConfigTypeDef = None,
    ) -> ListResourceInventoryPaginateResponseTypeDef:
        """
        [ListResourceInventory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory.paginate)
        """


class ListUsageForLicenseConfigurationPaginator(Boto3Paginator):
    """
    Paginator for `list_usage_for_license_configuration`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LicenseConfigurationArn: str,
        Filters: List[ListUsageForLicenseConfigurationPaginateFiltersTypeDef] = None,
        PaginationConfig: ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef = None,
    ) -> ListUsageForLicenseConfigurationPaginateResponseTypeDef:
        """
        [ListUsageForLicenseConfiguration.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration.paginate)
        """
