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
        Creates an iterator that will paginate through responses from
        :py:meth:`LicenseManager.Client.list_associations_for_license_configuration`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListAssociationsForLicenseConfiguration>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              LicenseConfigurationArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of a license configuration.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LicenseConfigurationAssociations': [
                    {
                        'ResourceArn': 'string',
                        'ResourceType':
                        'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'
                        |'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                        'ResourceOwnerId': 'string',
                        'AssociationTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **LicenseConfigurationAssociations** *(list) --*

              Information about the associations for the license configuration.

              - *(dict) --*

                Describes an association with a license configuration.

                - **ResourceArn** *(string) --*

                  Amazon Resource Name (ARN) of the resource.

                - **ResourceType** *(string) --*

                  Type of server resource.

                - **ResourceOwnerId** *(string) --*

                  ID of the AWS account that owns the resource consuming licenses.

                - **AssociationTime** *(datetime) --*

                  Time when the license configuration was associated with the resource.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`LicenseManager.Client.list_license_configurations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseConfigurations>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              LicenseConfigurationArns=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type LicenseConfigurationArns: list
        :param LicenseConfigurationArns:

          Amazon Resource Names (ARN) of the license configurations.

          - *(string) --*

        :type Filters: list
        :param Filters:

          Filters to scope the results. The following filters and logical operators are supported:

          * ``licenseCountingType`` - The dimension on which licenses are counted (vCPU). Logical
          operators are ``EQUALS`` | ``NOT_EQUALS`` .

          * ``enforceLicenseCount`` - A Boolean value that indicates whether hard license
          enforcement is used. Logical operators are ``EQUALS`` | ``NOT_EQUALS`` .

          * ``usagelimitExceeded`` - A Boolean value that indicates whether the available licenses
          have been exceeded. Logical operators are ``EQUALS`` | ``NOT_EQUALS`` .

          - *(dict) --*

            A filter name and value pair that is used to return more specific results from a
            describe operation. Filters can be used to match a set of resources by specific
            criteria, such as tags, attributes, or IDs.

            - **Name** *(string) --*

              Name of the filter. Filter names are case-sensitive.

            - **Values** *(list) --*

              Filter values. Filter values are case-sensitive.

              - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LicenseConfigurations': [
                    {
                        'LicenseConfigurationId': 'string',
                        'LicenseConfigurationArn': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'LicenseCountingType': 'vCPU'|'Instance'|'Core'|'Socket',
                        'LicenseRules': [
                            'string',
                        ],
                        'LicenseCount': 123,
                        'LicenseCountHardLimit': True|False,
                        'ConsumedLicenses': 123,
                        'Status': 'string',
                        'OwnerAccountId': 'string',
                        'ConsumedLicenseSummaryList': [
                            {
                                'ResourceType':
                                'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'
                                |'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                                'ConsumedLicenses': 123
                            },
                        ],
                        'ManagedResourceSummaryList': [
                            {
                                'ResourceType':
                                'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'
                                |'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                                'AssociationCount': 123
                            },
                        ],
                        'ProductInformationList': [
                            {
                                'ResourceType': 'string',
                                'ProductInformationFilterList': [
                                    {
                                        'ProductInformationFilterName': 'string',
                                        'ProductInformationFilterValue': [
                                            'string',
                                        ],
                                        'ProductInformationFilterComparator': 'string'
                                    },
                                ]
                            },
                        ],
                        'AutomatedDiscoveryInformation': {
                            'LastRunTime': datetime(2015, 1, 1)
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **LicenseConfigurations** *(list) --*

              Information about the license configurations.

              - *(dict) --*

                A license configuration is an abstraction of a customer license agreement that can
                be consumed and enforced by License Manager. Components include specifications for
                the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy
                (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity
                (how long a VM must be associated with a host), and the number of licenses purchased
                and used.

                - **LicenseConfigurationId** *(string) --*

                  Unique ID of the license configuration.

                - **LicenseConfigurationArn** *(string) --*

                  Amazon Resource Name (ARN) of the license configuration.

                - **Name** *(string) --*

                  Name of the license configuration.

                - **Description** *(string) --*

                  Description of the license configuration.

                - **LicenseCountingType** *(string) --*

                  Dimension to use to track the license inventory.

                - **LicenseRules** *(list) --*

                  License rules.

                  - *(string) --*

                - **LicenseCount** *(integer) --*

                  Number of licenses managed by the license configuration.

                - **LicenseCountHardLimit** *(boolean) --*

                  Number of available licenses as a hard limit.

                - **ConsumedLicenses** *(integer) --*

                  Number of licenses consumed.

                - **Status** *(string) --*

                  Status of the license configuration.

                - **OwnerAccountId** *(string) --*

                  Account ID of the license configuration's owner.

                - **ConsumedLicenseSummaryList** *(list) --*

                  Summaries for licenses consumed by various resources.

                  - *(dict) --*

                    Details about license consumption.

                    - **ResourceType** *(string) --*

                      Resource type of the resource consuming a license.

                    - **ConsumedLicenses** *(integer) --*

                      Number of licenses consumed by the resource.

                - **ManagedResourceSummaryList** *(list) --*

                  Summaries for managed resources.

                  - *(dict) --*

                    Summary information about a managed resource.

                    - **ResourceType** *(string) --*

                      Type of resource associated with a license.

                    - **AssociationCount** *(integer) --*

                      Number of resources associated with licenses.

                - **ProductInformationList** *(list) --*

                  Product information.

                  - *(dict) --*

                    Describes product information for a license configuration.

                    - **ResourceType** *(string) --*

                      Resource type. The value is ``SSM_MANAGED`` .

                    - **ProductInformationFilterList** *(list) --*

                      Product information filters. The following filters and logical operators are
                      supported:

                      * ``Application Name`` - The name of the application. Logical operator is
                      ``EQUALS`` .

                      * ``Application Publisher`` - The publisher of the application. Logical
                      operator is ``EQUALS`` .

                      * ``Application Version`` - The version of the application. Logical operator
                      is ``EQUALS`` .

                      * ``Platform Name`` - The name of the platform. Logical operator is ``EQUALS``
                      .

                      * ``Platform Type`` - The platform type. Logical operator is ``EQUALS`` .

                      * ``License Included`` - The type of license included. Logical operators are
                      ``EQUALS`` and ``NOT_EQUALS`` . Possible values are ``sql-server-enterprise``
                      | ``sql-server-standard`` | ``sql-server-web``
                      | ``windows-server-datacenter``
                      .

                      - *(dict) --*

                        Describes product information filters.

                        - **ProductInformationFilterName** *(string) --*

                          Filter name.

                        - **ProductInformationFilterValue** *(list) --*

                          Filter value.

                          - *(string) --*

                        - **ProductInformationFilterComparator** *(string) --*

                          Logical operator.

                - **AutomatedDiscoveryInformation** *(dict) --*

                  Automated discovery information.

                  - **LastRunTime** *(datetime) --*

                    Time that automated discovery last ran.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`LicenseManager.Client.list_license_specifications_for_resource`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseSpecificationsForResource>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ResourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of a resource that has an associated license configuration.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LicenseSpecifications': [
                    {
                        'LicenseConfigurationArn': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **LicenseSpecifications** *(list) --*

              License configurations associated with a resource.

              - *(dict) --*

                Details for associating a license configuration with a resource.

                - **LicenseConfigurationArn** *(string) --*

                  Amazon Resource Name (ARN) of the license configuration.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`LicenseManager.Client.list_resource_inventory`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListResourceInventory>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Condition': 'EQUALS'|'NOT_EQUALS'|'BEGINS_WITH'|'CONTAINS',
                      'Value': 'string'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          Filters to scope the results. The following filters and logical operators are supported:

          * ``account_id`` - The ID of the AWS account that owns the resource. Logical operators are
          ``EQUALS`` | ``NOT_EQUALS`` .

          * ``application_name`` - The name of the application. Logical operators are ``EQUALS`` |
          ``BEGINS_WITH`` .

          * ``license_included`` - The type of license included. Logical operators are ``EQUALS``
          |
          ``NOT_EQUALS`` . Possible values are ``sql-server-enterprise``
          | ``sql-server-standard`` |
          ``sql-server-web`` | ``windows-server-datacenter`` .

          * ``platform`` - The platform of the resource. Logical operators are ``EQUALS`` |
          ``BEGINS_WITH`` .

          * ``resource_id`` - The ID of the resource. Logical operators are ``EQUALS`` |
          ``NOT_EQUALS`` .

          - *(dict) --*

            An inventory filter.

            - **Name** *(string) --* **[REQUIRED]**

              Name of the filter.

            - **Condition** *(string) --* **[REQUIRED]**

              Condition of the filter.

            - **Value** *(string) --*

              Value of the filter.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceInventoryList': [
                    {
                        'ResourceId': 'string',
                        'ResourceType':
                        'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'
                        |'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                        'ResourceArn': 'string',
                        'Platform': 'string',
                        'PlatformVersion': 'string',
                        'ResourceOwningAccountId': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ResourceInventoryList** *(list) --*

              Information about the resources.

              - *(dict) --*

                Details about a resource.

                - **ResourceId** *(string) --*

                  ID of the resource.

                - **ResourceType** *(string) --*

                  Type of resource.

                - **ResourceArn** *(string) --*

                  Amazon Resource Name (ARN) of the resource.

                - **Platform** *(string) --*

                  Platform of the resource.

                - **PlatformVersion** *(string) --*

                  Platform version of the resource in the inventory.

                - **ResourceOwningAccountId** *(string) --*

                  ID of the account that owns the resource.
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
        Creates an iterator that will paginate through responses from
        :py:meth:`LicenseManager.Client.list_usage_for_license_configuration`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListUsageForLicenseConfiguration>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              LicenseConfigurationArn='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of the license configuration.

        :type Filters: list
        :param Filters:

          Filters to scope the results. The following filters and logical operators are supported:

          * ``resourceArn`` - The ARN of the license configuration resource. Logical operators are
          ``EQUALS`` | ``NOT_EQUALS`` .

          * ``resourceType`` - The resource type (EC2_INSTANCE | EC2_HOST | EC2_AMI |
          SYSTEMS_MANAGER_MANAGED_INSTANCE). Logical operators are ``EQUALS`` | ``NOT_EQUALS`` .

          * ``resourceAccount`` - The ID of the account that owns the resource. Logical operators
          are ``EQUALS`` | ``NOT_EQUALS`` .

          - *(dict) --*

            A filter name and value pair that is used to return more specific results from a
            describe operation. Filters can be used to match a set of resources by specific
            criteria, such as tags, attributes, or IDs.

            - **Name** *(string) --*

              Name of the filter. Filter names are case-sensitive.

            - **Values** *(list) --*

              Filter values. Filter values are case-sensitive.

              - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LicenseConfigurationUsageList': [
                    {
                        'ResourceArn': 'string',
                        'ResourceType':
                        'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'
                        |'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                        'ResourceStatus': 'string',
                        'ResourceOwnerId': 'string',
                        'AssociationTime': datetime(2015, 1, 1),
                        'ConsumedLicenses': 123
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **LicenseConfigurationUsageList** *(list) --*

              Information about the license configurations.

              - *(dict) --*

                Details about the usage of a resource associated with a license configuration.

                - **ResourceArn** *(string) --*

                  Amazon Resource Name (ARN) of the resource.

                - **ResourceType** *(string) --*

                  Type of resource.

                - **ResourceStatus** *(string) --*

                  Status of the resource.

                - **ResourceOwnerId** *(string) --*

                  ID of the account that owns the resource.

                - **AssociationTime** *(datetime) --*

                  Time when the license configuration was initially associated with the resource.

                - **ConsumedLicenses** *(integer) --*

                  Number of licenses consumed by the resource.
        """
