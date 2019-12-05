"Main interface for license-manager service type defs"
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


ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)

_RequiredClientCreateLicenseConfigurationProductInformationListTypeDef = TypedDict(
    "_RequiredClientCreateLicenseConfigurationProductInformationListTypeDef", {"ResourceType": str}
)
_OptionalClientCreateLicenseConfigurationProductInformationListTypeDef = TypedDict(
    "_OptionalClientCreateLicenseConfigurationProductInformationListTypeDef",
    {
        "ProductInformationFilterList": List[
            ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef
        ]
    },
    total=False,
)


class ClientCreateLicenseConfigurationProductInformationListTypeDef(
    _RequiredClientCreateLicenseConfigurationProductInformationListTypeDef,
    _OptionalClientCreateLicenseConfigurationProductInformationListTypeDef,
):
    pass


ClientCreateLicenseConfigurationResponseTypeDef = TypedDict(
    "ClientCreateLicenseConfigurationResponseTypeDef", {"LicenseConfigurationArn": str}, total=False
)

ClientCreateLicenseConfigurationTagsTypeDef = TypedDict(
    "ClientCreateLicenseConfigurationTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef",
    {"LastRunTime": datetime},
    total=False,
)

ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)

ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)

ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)

ClientGetLicenseConfigurationResponseProductInformationListTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseProductInformationListTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[
            ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef
        ],
    },
    total=False,
)

ClientGetLicenseConfigurationResponseTagsTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetLicenseConfigurationResponseTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": Literal["vCPU", "Instance", "Core", "Socket"],
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[
            ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef
        ],
        "ManagedResourceSummaryList": List[
            ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef
        ],
        "Tags": List[ClientGetLicenseConfigurationResponseTagsTypeDef],
        "ProductInformationList": List[
            ClientGetLicenseConfigurationResponseProductInformationListTypeDef
        ],
        "AutomatedDiscoveryInformation": ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef,
    },
    total=False,
)

ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef = TypedDict(
    "ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef",
    {"EnableIntegration": bool},
    total=False,
)

ClientGetServiceSettingsResponseTypeDef = TypedDict(
    "ClientGetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef,
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
    },
    total=False,
)

ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef = TypedDict(
    "ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
    },
    total=False,
)

ClientListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ClientListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[
            ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef = TypedDict(
    "ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef = TypedDict(
    "ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ErrorMessage": str,
        "FailureTime": datetime,
        "OperationName": str,
        "ResourceOwnerId": str,
        "OperationRequestedBy": str,
        "MetadataList": List[
            ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef
        ],
    },
    total=False,
)

ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {
        "LicenseOperationFailureList": List[
            ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListLicenseConfigurationsFiltersTypeDef = TypedDict(
    "ClientListLicenseConfigurationsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef",
    {"LastRunTime": datetime},
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef
        ],
    },
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": Literal["vCPU", "Instance", "Core", "Socket"],
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef
        ],
        "ManagedResourceSummaryList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef
        ],
        "ProductInformationList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef
        ],
        "AutomatedDiscoveryInformation": ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef,
    },
    total=False,
)

ClientListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseTypeDef",
    {
        "LicenseConfigurations": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef = TypedDict(
    "ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)

ClientListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ClientListLicenseSpecificationsForResourceResponseTypeDef",
    {
        "LicenseSpecifications": List[
            ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListResourceInventoryFiltersTypeDef = TypedDict(
    "_RequiredClientListResourceInventoryFiltersTypeDef", {"Name": str}
)
_OptionalClientListResourceInventoryFiltersTypeDef = TypedDict(
    "_OptionalClientListResourceInventoryFiltersTypeDef",
    {"Condition": Literal["EQUALS", "NOT_EQUALS", "BEGINS_WITH", "CONTAINS"], "Value": str},
    total=False,
)


class ClientListResourceInventoryFiltersTypeDef(
    _RequiredClientListResourceInventoryFiltersTypeDef,
    _OptionalClientListResourceInventoryFiltersTypeDef,
):
    pass


ClientListResourceInventoryResponseResourceInventoryListTypeDef = TypedDict(
    "ClientListResourceInventoryResponseResourceInventoryListTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
    },
    total=False,
)

ClientListResourceInventoryResponseTypeDef = TypedDict(
    "ClientListResourceInventoryResponseTypeDef",
    {
        "ResourceInventoryList": List[
            ClientListResourceInventoryResponseResourceInventoryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientListUsageForLicenseConfigurationFiltersTypeDef = TypedDict(
    "ClientListUsageForLicenseConfigurationFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef = TypedDict(
    "ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)

ClientListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ClientListUsageForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List[
            ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)

_RequiredClientUpdateLicenseConfigurationProductInformationListTypeDef = TypedDict(
    "_RequiredClientUpdateLicenseConfigurationProductInformationListTypeDef", {"ResourceType": str}
)
_OptionalClientUpdateLicenseConfigurationProductInformationListTypeDef = TypedDict(
    "_OptionalClientUpdateLicenseConfigurationProductInformationListTypeDef",
    {
        "ProductInformationFilterList": List[
            ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef
        ]
    },
    total=False,
)


class ClientUpdateLicenseConfigurationProductInformationListTypeDef(
    _RequiredClientUpdateLicenseConfigurationProductInformationListTypeDef,
    _OptionalClientUpdateLicenseConfigurationProductInformationListTypeDef,
):
    pass


ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef = TypedDict(
    "ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
)

ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef = TypedDict(
    "ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
)

ClientUpdateServiceSettingsOrganizationConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceSettingsOrganizationConfigurationTypeDef", {"EnableIntegration": bool}
)

ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
    },
    total=False,
)

ListAssociationsForLicenseConfigurationPaginateResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationPaginateResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[
            ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef
        ]
    },
    total=False,
)

ListLicenseConfigurationsPaginateFiltersTypeDef = TypedDict(
    "ListLicenseConfigurationsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ListLicenseConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListLicenseConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListLicenseConfigurationsPaginateResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef = TypedDict(
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef",
    {"LastRunTime": datetime},
    total=False,
)

ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef = TypedDict(
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)

ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef = TypedDict(
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)

ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)

ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListTypeDef = TypedDict(
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef
        ],
    },
    total=False,
)

ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef = TypedDict(
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": Literal["vCPU", "Instance", "Core", "Socket"],
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef
        ],
        "ManagedResourceSummaryList": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef
        ],
        "ProductInformationList": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListTypeDef
        ],
        "AutomatedDiscoveryInformation": ListLicenseConfigurationsPaginateResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef,
    },
    total=False,
)

ListLicenseConfigurationsPaginateResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsPaginateResponseTypeDef",
    {
        "LicenseConfigurations": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef
        ]
    },
    total=False,
)

ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)

ListLicenseSpecificationsForResourcePaginateResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourcePaginateResponseTypeDef",
    {
        "LicenseSpecifications": List[
            ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef
        ]
    },
    total=False,
)

_RequiredListResourceInventoryPaginateFiltersTypeDef = TypedDict(
    "_RequiredListResourceInventoryPaginateFiltersTypeDef", {"Name": str}
)
_OptionalListResourceInventoryPaginateFiltersTypeDef = TypedDict(
    "_OptionalListResourceInventoryPaginateFiltersTypeDef",
    {"Condition": Literal["EQUALS", "NOT_EQUALS", "BEGINS_WITH", "CONTAINS"], "Value": str},
    total=False,
)


class ListResourceInventoryPaginateFiltersTypeDef(
    _RequiredListResourceInventoryPaginateFiltersTypeDef,
    _OptionalListResourceInventoryPaginateFiltersTypeDef,
):
    pass


ListResourceInventoryPaginatePaginationConfigTypeDef = TypedDict(
    "ListResourceInventoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResourceInventoryPaginateResponseResourceInventoryListTypeDef = TypedDict(
    "ListResourceInventoryPaginateResponseResourceInventoryListTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
    },
    total=False,
)

ListResourceInventoryPaginateResponseTypeDef = TypedDict(
    "ListResourceInventoryPaginateResponseTypeDef",
    {
        "ResourceInventoryList": List[
            ListResourceInventoryPaginateResponseResourceInventoryListTypeDef
        ]
    },
    total=False,
)

ListUsageForLicenseConfigurationPaginateFiltersTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)

ListUsageForLicenseConfigurationPaginateResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationPaginateResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List[
            ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef
        ]
    },
    total=False,
)
