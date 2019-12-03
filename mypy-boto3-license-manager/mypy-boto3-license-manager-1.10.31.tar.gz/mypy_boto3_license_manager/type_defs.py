"Main interface for license-manager service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    "ClientCreateLicenseConfigurationProductInformationListTypeDef",
    "ClientCreateLicenseConfigurationResponseTypeDef",
    "ClientCreateLicenseConfigurationTagsTypeDef",
    "ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef",
    "ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef",
    "ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef",
    "ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef",
    "ClientGetLicenseConfigurationResponseProductInformationListTypeDef",
    "ClientGetLicenseConfigurationResponseTagsTypeDef",
    "ClientGetLicenseConfigurationResponseTypeDef",
    "ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef",
    "ClientGetServiceSettingsResponseTypeDef",
    "ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef",
    "ClientListAssociationsForLicenseConfigurationResponseTypeDef",
    "ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef",
    "ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef",
    "ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "ClientListLicenseConfigurationsFiltersTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef",
    "ClientListLicenseConfigurationsResponseTypeDef",
    "ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef",
    "ClientListLicenseSpecificationsForResourceResponseTypeDef",
    "ClientListResourceInventoryFiltersTypeDef",
    "ClientListResourceInventoryResponseResourceInventoryListTypeDef",
    "ClientListResourceInventoryResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUsageForLicenseConfigurationFiltersTypeDef",
    "ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef",
    "ClientListUsageForLicenseConfigurationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    "ClientUpdateLicenseConfigurationProductInformationListTypeDef",
    "ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef",
    "ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef",
    "ClientUpdateServiceSettingsOrganizationConfigurationTypeDef",
    "ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef",
    "ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef",
    "ListAssociationsForLicenseConfigurationPaginateResponseTypeDef",
    "ListLicenseConfigurationsPaginateFiltersTypeDef",
    "ListLicenseConfigurationsPaginatePaginationConfigTypeDef",
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef",
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef",
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListTypeDef",
    "ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef",
    "ListLicenseConfigurationsPaginateResponseTypeDef",
    "ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef",
    "ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef",
    "ListLicenseSpecificationsForResourcePaginateResponseTypeDef",
    "ListResourceInventoryPaginateFiltersTypeDef",
    "ListResourceInventoryPaginatePaginationConfigTypeDef",
    "ListResourceInventoryPaginateResponseResourceInventoryListTypeDef",
    "ListResourceInventoryPaginateResponseTypeDef",
    "ListUsageForLicenseConfigurationPaginateFiltersTypeDef",
    "ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef",
    "ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef",
    "ListUsageForLicenseConfigurationPaginateResponseTypeDef",
)


_ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "_ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)


class ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef(
    _ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef
):
    pass


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
    """
    - *(dict) --*

      Describes product information for a license configuration.
      - **ResourceType** *(string) --***[REQUIRED]**

        Resource type. The value is ``SSM_MANAGED`` .
    """


_ClientCreateLicenseConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateLicenseConfigurationResponseTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)


class ClientCreateLicenseConfigurationResponseTypeDef(
    _ClientCreateLicenseConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseConfigurationArn** *(string) --*

        Amazon Resource Name (ARN) of the license configuration.
    """


_ClientCreateLicenseConfigurationTagsTypeDef = TypedDict(
    "_ClientCreateLicenseConfigurationTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateLicenseConfigurationTagsTypeDef(_ClientCreateLicenseConfigurationTagsTypeDef):
    """
    - *(dict) --*

      Details about a tag for a license configuration.
      - **Key** *(string) --*

        Tag key.
    """


_ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef",
    {"LastRunTime": datetime},
    total=False,
)


class ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef(
    _ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef
):
    pass


_ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)


class ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef(
    _ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef
):
    pass


_ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)


class ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef(
    _ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef
):
    pass


_ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)


class ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef(
    _ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef
):
    pass


_ClientGetLicenseConfigurationResponseProductInformationListTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseProductInformationListTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[
            ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef
        ],
    },
    total=False,
)


class ClientGetLicenseConfigurationResponseProductInformationListTypeDef(
    _ClientGetLicenseConfigurationResponseProductInformationListTypeDef
):
    pass


_ClientGetLicenseConfigurationResponseTagsTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetLicenseConfigurationResponseTagsTypeDef(
    _ClientGetLicenseConfigurationResponseTagsTypeDef
):
    pass


_ClientGetLicenseConfigurationResponseTypeDef = TypedDict(
    "_ClientGetLicenseConfigurationResponseTypeDef",
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


class ClientGetLicenseConfigurationResponseTypeDef(_ClientGetLicenseConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **LicenseConfigurationId** *(string) --*

        Unique ID for the license configuration.
    """


_ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef = TypedDict(
    "_ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef",
    {"EnableIntegration": bool},
    total=False,
)


class ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef(
    _ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef
):
    pass


_ClientGetServiceSettingsResponseTypeDef = TypedDict(
    "_ClientGetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef,
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
    },
    total=False,
)


class ClientGetServiceSettingsResponseTypeDef(_ClientGetServiceSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **S3BucketArn** *(string) --*

        Regional S3 bucket path for storing reports, license trail event data, discovery data, and
        so on.
    """


_ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef = TypedDict(
    "_ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef",
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


class ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef(
    _ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes an association with a license configuration.
      - **ResourceArn** *(string) --*

        Amazon Resource Name (ARN) of the resource.
    """


_ClientListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "_ClientListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[
            ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListAssociationsForLicenseConfigurationResponseTypeDef(
    _ClientListAssociationsForLicenseConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseConfigurationAssociations** *(list) --*

        Information about the associations for the license configuration.
        - *(dict) --*

          Describes an association with a license configuration.
          - **ResourceArn** *(string) --*

            Amazon Resource Name (ARN) of the resource.
    """


_ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef = TypedDict(
    "_ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef(
    _ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef
):
    pass


_ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef = TypedDict(
    "_ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef",
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


class ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef(
    _ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef
):
    """
    - *(dict) --*

      Describes the failure of a license operation.
      - **ResourceArn** *(string) --*

        Amazon Resource Name (ARN) of the resource.
    """


_ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "_ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {
        "LicenseOperationFailureList": List[
            ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef(
    _ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseOperationFailureList** *(list) --*

        License configuration operations that failed.
        - *(dict) --*

          Describes the failure of a license operation.
          - **ResourceArn** *(string) --*

            Amazon Resource Name (ARN) of the resource.
    """


_ClientListLicenseConfigurationsFiltersTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientListLicenseConfigurationsFiltersTypeDef(_ClientListLicenseConfigurationsFiltersTypeDef):
    """
    - *(dict) --*

      A filter name and value pair that is used to return more specific results from a describe
      operation. Filters can be used to match a set of resources by specific criteria, such as tags,
      attributes, or IDs.
      - **Name** *(string) --*

        Name of the filter. Filter names are case-sensitive.
    """


_ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef",
    {"LastRunTime": datetime},
    total=False,
)


class ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef(
    _ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef
):
    pass


_ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)


class ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef(
    _ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef
):
    pass


_ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)


class ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef(
    _ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef
):
    pass


_ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)


class ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef(
    _ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef
):
    pass


_ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef
        ],
    },
    total=False,
)


class ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef(
    _ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef
):
    pass


_ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef",
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


class ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef(
    _ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef
):
    """
    - *(dict) --*

      A license configuration is an abstraction of a customer license agreement that can be consumed
      and enforced by License Manager. Components include specifications for the license type
      (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated
      Instance, Dedicated Host, or all of these), host affinity (how long a VM must be associated
      with a host), and the number of licenses purchased and used.
      - **LicenseConfigurationId** *(string) --*

        Unique ID of the license configuration.
    """


_ClientListLicenseConfigurationsResponseTypeDef = TypedDict(
    "_ClientListLicenseConfigurationsResponseTypeDef",
    {
        "LicenseConfigurations": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListLicenseConfigurationsResponseTypeDef(
    _ClientListLicenseConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseConfigurations** *(list) --*

        Information about the license configurations.
        - *(dict) --*

          A license configuration is an abstraction of a customer license agreement that can be
          consumed and enforced by License Manager. Components include specifications for the
          license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared
          tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a
          VM must be associated with a host), and the number of licenses purchased and used.
          - **LicenseConfigurationId** *(string) --*

            Unique ID of the license configuration.
    """


_ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef = TypedDict(
    "_ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)


class ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef(
    _ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef
):
    """
    - *(dict) --*

      Details for associating a license configuration with a resource.
      - **LicenseConfigurationArn** *(string) --*

        Amazon Resource Name (ARN) of the license configuration.
    """


_ClientListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "_ClientListLicenseSpecificationsForResourceResponseTypeDef",
    {
        "LicenseSpecifications": List[
            ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListLicenseSpecificationsForResourceResponseTypeDef(
    _ClientListLicenseSpecificationsForResourceResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseSpecifications** *(list) --*

        License configurations associated with a resource.
        - *(dict) --*

          Details for associating a license configuration with a resource.
          - **LicenseConfigurationArn** *(string) --*

            Amazon Resource Name (ARN) of the license configuration.
    """


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
    """
    - *(dict) --*

      An inventory filter.
      - **Name** *(string) --***[REQUIRED]**

        Name of the filter.
    """


_ClientListResourceInventoryResponseResourceInventoryListTypeDef = TypedDict(
    "_ClientListResourceInventoryResponseResourceInventoryListTypeDef",
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


class ClientListResourceInventoryResponseResourceInventoryListTypeDef(
    _ClientListResourceInventoryResponseResourceInventoryListTypeDef
):
    """
    - *(dict) --*

      Details about a resource.
      - **ResourceId** *(string) --*

        ID of the resource.
    """


_ClientListResourceInventoryResponseTypeDef = TypedDict(
    "_ClientListResourceInventoryResponseTypeDef",
    {
        "ResourceInventoryList": List[
            ClientListResourceInventoryResponseResourceInventoryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourceInventoryResponseTypeDef(_ClientListResourceInventoryResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceInventoryList** *(list) --*

        Information about the resources.
        - *(dict) --*

          Details about a resource.
          - **ResourceId** *(string) --*

            ID of the resource.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      Details about a tag for a license configuration.
      - **Key** *(string) --*

        Tag key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        Information about the tags.
        - *(dict) --*

          Details about a tag for a license configuration.
          - **Key** *(string) --*

            Tag key.
    """


_ClientListUsageForLicenseConfigurationFiltersTypeDef = TypedDict(
    "_ClientListUsageForLicenseConfigurationFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientListUsageForLicenseConfigurationFiltersTypeDef(
    _ClientListUsageForLicenseConfigurationFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return more specific results from a describe
      operation. Filters can be used to match a set of resources by specific criteria, such as tags,
      attributes, or IDs.
      - **Name** *(string) --*

        Name of the filter. Filter names are case-sensitive.
    """


_ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef = TypedDict(
    "_ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef",
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


class ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef(
    _ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef
):
    """
    - *(dict) --*

      Details about the usage of a resource associated with a license configuration.
      - **ResourceArn** *(string) --*

        Amazon Resource Name (ARN) of the resource.
    """


_ClientListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "_ClientListUsageForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List[
            ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListUsageForLicenseConfigurationResponseTypeDef(
    _ClientListUsageForLicenseConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseConfigurationUsageList** *(list) --*

        Information about the license configurations.
        - *(dict) --*

          Details about the usage of a resource associated with a license configuration.
          - **ResourceArn** *(string) --*

            Amazon Resource Name (ARN) of the resource.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      Details about a tag for a license configuration.
      - **Key** *(string) --*

        Tag key.
    """


_ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "_ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)


class ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef(
    _ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef
):
    pass


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
    """
    - *(dict) --*

      Describes product information for a license configuration.
      - **ResourceType** *(string) --***[REQUIRED]**

        Resource type. The value is ``SSM_MANAGED`` .
    """


_ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef = TypedDict(
    "_ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
)


class ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef(
    _ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef
):
    """
    - *(dict) --*

      Details for associating a license configuration with a resource.
      - **LicenseConfigurationArn** *(string) --***[REQUIRED]**

        Amazon Resource Name (ARN) of the license configuration.
    """


_ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef = TypedDict(
    "_ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
)


class ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef(
    _ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef
):
    """
    - *(dict) --*

      Details for associating a license configuration with a resource.
      - **LicenseConfigurationArn** *(string) --***[REQUIRED]**

        Amazon Resource Name (ARN) of the license configuration.
    """


_ClientUpdateServiceSettingsOrganizationConfigurationTypeDef = TypedDict(
    "_ClientUpdateServiceSettingsOrganizationConfigurationTypeDef", {"EnableIntegration": bool}
)


class ClientUpdateServiceSettingsOrganizationConfigurationTypeDef(
    _ClientUpdateServiceSettingsOrganizationConfigurationTypeDef
):
    """
    Enables integration with AWS Organizations for cross-account discovery.
    - **EnableIntegration** *(boolean) --***[REQUIRED]**

      Enables AWS Organization integration.
    """


_ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef(
    _ListAssociationsForLicenseConfigurationPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef = TypedDict(
    "_ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef",
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


class ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef(
    _ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes an association with a license configuration.
      - **ResourceArn** *(string) --*

        Amazon Resource Name (ARN) of the resource.
    """


_ListAssociationsForLicenseConfigurationPaginateResponseTypeDef = TypedDict(
    "_ListAssociationsForLicenseConfigurationPaginateResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[
            ListAssociationsForLicenseConfigurationPaginateResponseLicenseConfigurationAssociationsTypeDef
        ]
    },
    total=False,
)


class ListAssociationsForLicenseConfigurationPaginateResponseTypeDef(
    _ListAssociationsForLicenseConfigurationPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseConfigurationAssociations** *(list) --*

        Information about the associations for the license configuration.
        - *(dict) --*

          Describes an association with a license configuration.
          - **ResourceArn** *(string) --*

            Amazon Resource Name (ARN) of the resource.
    """


_ListLicenseConfigurationsPaginateFiltersTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ListLicenseConfigurationsPaginateFiltersTypeDef(
    _ListLicenseConfigurationsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return more specific results from a describe
      operation. Filters can be used to match a set of resources by specific criteria, such as tags,
      attributes, or IDs.
      - **Name** *(string) --*

        Name of the filter. Filter names are case-sensitive.
    """


_ListLicenseConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLicenseConfigurationsPaginatePaginationConfigTypeDef(
    _ListLicenseConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef",
    {"LastRunTime": datetime},
    total=False,
)


class ListLicenseConfigurationsPaginateResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef(
    _ListLicenseConfigurationsPaginateResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef
):
    pass


_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)


class ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef(
    _ListLicenseConfigurationsPaginateResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef
):
    pass


_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)


class ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef(
    _ListLicenseConfigurationsPaginateResponseLicenseConfigurationsManagedResourceSummaryListTypeDef
):
    pass


_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)


class ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef(
    _ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef
):
    pass


_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef
        ],
    },
    total=False,
)


class ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListTypeDef(
    _ListLicenseConfigurationsPaginateResponseLicenseConfigurationsProductInformationListTypeDef
):
    pass


_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef",
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


class ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef(
    _ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef
):
    """
    - *(dict) --*

      A license configuration is an abstraction of a customer license agreement that can be consumed
      and enforced by License Manager. Components include specifications for the license type
      (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated
      Instance, Dedicated Host, or all of these), host affinity (how long a VM must be associated
      with a host), and the number of licenses purchased and used.
      - **LicenseConfigurationId** *(string) --*

        Unique ID of the license configuration.
    """


_ListLicenseConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListLicenseConfigurationsPaginateResponseTypeDef",
    {
        "LicenseConfigurations": List[
            ListLicenseConfigurationsPaginateResponseLicenseConfigurationsTypeDef
        ]
    },
    total=False,
)


class ListLicenseConfigurationsPaginateResponseTypeDef(
    _ListLicenseConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseConfigurations** *(list) --*

        Information about the license configurations.
        - *(dict) --*

          A license configuration is an abstraction of a customer license agreement that can be
          consumed and enforced by License Manager. Components include specifications for the
          license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared
          tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a
          VM must be associated with a host), and the number of licenses purchased and used.
          - **LicenseConfigurationId** *(string) --*

            Unique ID of the license configuration.
    """


_ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef(
    _ListLicenseSpecificationsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef = TypedDict(
    "_ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)


class ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef(
    _ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef
):
    """
    - *(dict) --*

      Details for associating a license configuration with a resource.
      - **LicenseConfigurationArn** *(string) --*

        Amazon Resource Name (ARN) of the license configuration.
    """


_ListLicenseSpecificationsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListLicenseSpecificationsForResourcePaginateResponseTypeDef",
    {
        "LicenseSpecifications": List[
            ListLicenseSpecificationsForResourcePaginateResponseLicenseSpecificationsTypeDef
        ]
    },
    total=False,
)


class ListLicenseSpecificationsForResourcePaginateResponseTypeDef(
    _ListLicenseSpecificationsForResourcePaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseSpecifications** *(list) --*

        License configurations associated with a resource.
        - *(dict) --*

          Details for associating a license configuration with a resource.
          - **LicenseConfigurationArn** *(string) --*

            Amazon Resource Name (ARN) of the license configuration.
    """


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
    """
    - *(dict) --*

      An inventory filter.
      - **Name** *(string) --***[REQUIRED]**

        Name of the filter.
    """


_ListResourceInventoryPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceInventoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceInventoryPaginatePaginationConfigTypeDef(
    _ListResourceInventoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourceInventoryPaginateResponseResourceInventoryListTypeDef = TypedDict(
    "_ListResourceInventoryPaginateResponseResourceInventoryListTypeDef",
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


class ListResourceInventoryPaginateResponseResourceInventoryListTypeDef(
    _ListResourceInventoryPaginateResponseResourceInventoryListTypeDef
):
    """
    - *(dict) --*

      Details about a resource.
      - **ResourceId** *(string) --*

        ID of the resource.
    """


_ListResourceInventoryPaginateResponseTypeDef = TypedDict(
    "_ListResourceInventoryPaginateResponseTypeDef",
    {
        "ResourceInventoryList": List[
            ListResourceInventoryPaginateResponseResourceInventoryListTypeDef
        ]
    },
    total=False,
)


class ListResourceInventoryPaginateResponseTypeDef(_ListResourceInventoryPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceInventoryList** *(list) --*

        Information about the resources.
        - *(dict) --*

          Details about a resource.
          - **ResourceId** *(string) --*

            ID of the resource.
    """


_ListUsageForLicenseConfigurationPaginateFiltersTypeDef = TypedDict(
    "_ListUsageForLicenseConfigurationPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ListUsageForLicenseConfigurationPaginateFiltersTypeDef(
    _ListUsageForLicenseConfigurationPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to return more specific results from a describe
      operation. Filters can be used to match a set of resources by specific criteria, such as tags,
      attributes, or IDs.
      - **Name** *(string) --*

        Name of the filter. Filter names are case-sensitive.
    """


_ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef(
    _ListUsageForLicenseConfigurationPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef = TypedDict(
    "_ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef",
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


class ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef(
    _ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef
):
    """
    - *(dict) --*

      Details about the usage of a resource associated with a license configuration.
      - **ResourceArn** *(string) --*

        Amazon Resource Name (ARN) of the resource.
    """


_ListUsageForLicenseConfigurationPaginateResponseTypeDef = TypedDict(
    "_ListUsageForLicenseConfigurationPaginateResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List[
            ListUsageForLicenseConfigurationPaginateResponseLicenseConfigurationUsageListTypeDef
        ]
    },
    total=False,
)


class ListUsageForLicenseConfigurationPaginateResponseTypeDef(
    _ListUsageForLicenseConfigurationPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **LicenseConfigurationUsageList** *(list) --*

        Information about the license configurations.
        - *(dict) --*

          Details about the usage of a resource associated with a license configuration.
          - **ResourceArn** *(string) --*

            Amazon Resource Name (ARN) of the resource.
    """
