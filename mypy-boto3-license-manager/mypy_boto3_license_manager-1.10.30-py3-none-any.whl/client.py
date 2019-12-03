"Main interface for license-manager service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_license_manager.client as client_scope

# pylint: disable=import-self
import mypy_boto3_license_manager.paginator as paginator_scope
from mypy_boto3_license_manager.type_defs import (
    ClientCreateLicenseConfigurationProductInformationListTypeDef,
    ClientCreateLicenseConfigurationResponseTypeDef,
    ClientCreateLicenseConfigurationTagsTypeDef,
    ClientGetLicenseConfigurationResponseTypeDef,
    ClientGetServiceSettingsResponseTypeDef,
    ClientListAssociationsForLicenseConfigurationResponseTypeDef,
    ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef,
    ClientListLicenseConfigurationsFiltersTypeDef,
    ClientListLicenseConfigurationsResponseTypeDef,
    ClientListLicenseSpecificationsForResourceResponseTypeDef,
    ClientListResourceInventoryFiltersTypeDef,
    ClientListResourceInventoryResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListUsageForLicenseConfigurationFiltersTypeDef,
    ClientListUsageForLicenseConfigurationResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateLicenseConfigurationProductInformationListTypeDef,
    ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef,
    ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef,
    ClientUpdateServiceSettingsOrganizationConfigurationTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_license_configuration(
        self,
        Name: str,
        LicenseCountingType: Literal["vCPU", "Instance", "Core", "Socket"],
        Description: str = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        LicenseRules: List[str] = None,
        Tags: List[ClientCreateLicenseConfigurationTagsTypeDef] = None,
        ProductInformationList: List[
            ClientCreateLicenseConfigurationProductInformationListTypeDef
        ] = None,
    ) -> ClientCreateLicenseConfigurationResponseTypeDef:
        """
        Creates a license configuration.

        A license configuration is an abstraction of a customer license agreement that can be
        consumed and enforced by License Manager. Components include specifications for the license
        type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy,
        Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a VM must be
        associated with a host), and the number of licenses purchased and used.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/CreateLicenseConfiguration>`_

        **Request Syntax**
        ::

          response = client.create_license_configuration(
              Name='string',
              Description='string',
              LicenseCountingType='vCPU'|'Instance'|'Core'|'Socket',
              LicenseCount=123,
              LicenseCountHardLimit=True|False,
              LicenseRules=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              ProductInformationList=[
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
              ]
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the license configuration.

        :type Description: string
        :param Description:

          Description of the license configuration.

        :type LicenseCountingType: string
        :param LicenseCountingType: **[REQUIRED]**

          Dimension used to track the license inventory.

        :type LicenseCount: integer
        :param LicenseCount:

          Number of licenses managed by the license configuration.

        :type LicenseCountHardLimit: boolean
        :param LicenseCountHardLimit:

          Indicates whether hard or soft license enforcement is used. Exceeding a hard limit blocks
          the launch of new instances.

        :type LicenseRules: list
        :param LicenseRules:

          License rules. The syntax is #name=value (for example, #allowedTenancy=
              EC2-DedicatedHost).
          Available rules vary by dimension.

          * ``Cores`` dimension: ``allowedTenancy`` | ``maximumCores`` | ``minimumCores``

          * ``Instances`` dimension: ``allowedTenancy`` | ``maximumCores`` | ``minimumCores`` |
          ``maximumSockets`` | ``minimumSockets`` | ``maximumVcpus`` | ``minimumVcpus``

          * ``Sockets`` dimension: ``allowedTenancy`` | ``maximumSockets`` | ``minimumSockets``

          * ``vCPUs`` dimension: ``allowedTenancy`` | ``honorVcpuOptimization``
          | ``maximumVcpus`` |
          ``minimumVcpus``

          - *(string) --*

        :type Tags: list
        :param Tags:

          Tags to add to the license configuration.

          - *(dict) --*

            Details about a tag for a license configuration.

            - **Key** *(string) --*

              Tag key.

            - **Value** *(string) --*

              Tag value.

        :type ProductInformationList: list
        :param ProductInformationList:

          Product information.

          - *(dict) --*

            Describes product information for a license configuration.

            - **ResourceType** *(string) --* **[REQUIRED]**

              Resource type. The value is ``SSM_MANAGED`` .

            - **ProductInformationFilterList** *(list) --* **[REQUIRED]**

              Product information filters. The following filters and logical operators are
              supported:

              * ``Application Name`` - The name of the application. Logical operator is ``EQUALS`` .

              * ``Application Publisher`` - The publisher of the application. Logical operator is
              ``EQUALS`` .

              * ``Application Version`` - The version of the application. Logical operator is
              ``EQUALS`` .

              * ``Platform Name`` - The name of the platform. Logical operator is ``EQUALS`` .

              * ``Platform Type`` - The platform type. Logical operator is ``EQUALS`` .

              * ``License Included`` - The type of license included. Logical operators are
              ``EQUALS`` and ``NOT_EQUALS`` . Possible values are ``sql-server-enterprise`` |
              ``sql-server-standard`` | ``sql-server-web`` | ``windows-server-datacenter`` .

              - *(dict) --*

                Describes product information filters.

                - **ProductInformationFilterName** *(string) --* **[REQUIRED]**

                  Filter name.

                - **ProductInformationFilterValue** *(list) --* **[REQUIRED]**

                  Filter value.

                  - *(string) --*

                - **ProductInformationFilterComparator** *(string) --* **[REQUIRED]**

                  Logical operator.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LicenseConfigurationArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **LicenseConfigurationArn** *(string) --*

              Amazon Resource Name (ARN) of the license configuration.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_license_configuration(self, LicenseConfigurationArn: str) -> Dict[str, Any]:
        """
        Deletes the specified license configuration.

        You cannot delete a license configuration that is in use.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/DeleteLicenseConfiguration>`_

        **Request Syntax**
        ::

          response = client.delete_license_configuration(
              LicenseConfigurationArn='string'
          )
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**

          ID of the license configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_license_configuration(
        self, LicenseConfigurationArn: str
    ) -> ClientGetLicenseConfigurationResponseTypeDef:
        """
        Gets detailed information about the specified license configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/GetLicenseConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_license_configuration(
              LicenseConfigurationArn='string'
          )
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of the license configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

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
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
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
            }
          **Response Structure**

          - *(dict) --*

            - **LicenseConfigurationId** *(string) --*

              Unique ID for the license configuration.

            - **LicenseConfigurationArn** *(string) --*

              Amazon Resource Name (ARN) of the license configuration.

            - **Name** *(string) --*

              Name of the license configuration.

            - **Description** *(string) --*

              Description of the license configuration.

            - **LicenseCountingType** *(string) --*

              Dimension on which the licenses are counted.

            - **LicenseRules** *(list) --*

              License rules.

              - *(string) --*

            - **LicenseCount** *(integer) --*

              Number of available licenses.

            - **LicenseCountHardLimit** *(boolean) --*

              Sets the number of available licenses as a hard limit.

            - **ConsumedLicenses** *(integer) --*

              Number of licenses assigned to resources.

            - **Status** *(string) --*

              License configuration status.

            - **OwnerAccountId** *(string) --*

              Account ID of the owner of the license configuration.

            - **ConsumedLicenseSummaryList** *(list) --*

              Summaries of the licenses consumed by resources.

              - *(dict) --*

                Details about license consumption.

                - **ResourceType** *(string) --*

                  Resource type of the resource consuming a license.

                - **ConsumedLicenses** *(integer) --*

                  Number of licenses consumed by the resource.

            - **ManagedResourceSummaryList** *(list) --*

              Summaries of the managed resources.

              - *(dict) --*

                Summary information about a managed resource.

                - **ResourceType** *(string) --*

                  Type of resource associated with a license.

                - **AssociationCount** *(integer) --*

                  Number of resources associated with licenses.

            - **Tags** *(list) --*

              Tags for the license configuration.

              - *(dict) --*

                Details about a tag for a license configuration.

                - **Key** *(string) --*

                  Tag key.

                - **Value** *(string) --*

                  Tag value.

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

                  * ``Application Publisher`` - The publisher of the application. Logical operator
                  is ``EQUALS`` .

                  * ``Application Version`` - The version of the application. Logical operator is
                  ``EQUALS`` .

                  * ``Platform Name`` - The name of the platform. Logical operator is ``EQUALS`` .

                  * ``Platform Type`` - The platform type. Logical operator is ``EQUALS`` .

                  * ``License Included`` - The type of license included. Logical operators are
                  ``EQUALS`` and ``NOT_EQUALS`` . Possible values are ``sql-server-enterprise``
                  |
                  ``sql-server-standard`` | ``sql-server-web``
                  | ``windows-server-datacenter`` .

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_settings(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetServiceSettingsResponseTypeDef:
        """
        Gets the License Manager settings for the current Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/GetServiceSettings>`_

        **Request Syntax**
        ::

          response = client.get_service_settings()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'S3BucketArn': 'string',
                'SnsTopicArn': 'string',
                'OrganizationConfiguration': {
                    'EnableIntegration': True|False
                },
                'EnableCrossAccountsDiscovery': True|False,
                'LicenseManagerResourceShareArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **S3BucketArn** *(string) --*

              Regional S3 bucket path for storing reports, license trail event data, discovery data,
              and so on.

            - **SnsTopicArn** *(string) --*

              SNS topic configured to receive notifications from License Manager.

            - **OrganizationConfiguration** *(dict) --*

              Indicates whether AWS Organizations has been integrated with License Manager for
              cross-account discovery.

              - **EnableIntegration** *(boolean) --*

                Enables AWS Organization integration.

            - **EnableCrossAccountsDiscovery** *(boolean) --*

              Indicates whether cross-account discovery has been enabled.

            - **LicenseManagerResourceShareArn** *(string) --*

              Amazon Resource Name (ARN) of the AWS resource share. The License Manager master
              account will provide member accounts with access to this share.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_associations_for_license_configuration(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListAssociationsForLicenseConfigurationResponseTypeDef:
        """
        Lists the resource associations for the specified license configuration.

        Resource associations need not consume licenses from a license configuration. For example,
        an AMI or a stopped instance might not consume a license (depending on the license rules).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListAssociationsForLicenseConfiguration>`_

        **Request Syntax**
        ::

          response = client.list_associations_for_license_configuration(
              LicenseConfigurationArn='string',
              MaxResults=123,
              NextToken='string'
          )
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of a license configuration.

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          Token for the next set of results.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              Token for the next set of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_failures_for_license_configuration_operations(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef:
        """
        Lists the license configuration operations that failed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListFailuresForLicenseConfigurationOperations>`_

        **Request Syntax**
        ::

          response = client.list_failures_for_license_configuration_operations(
              LicenseConfigurationArn='string',
              MaxResults=123,
              NextToken='string'
          )
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**

          Amazon Resource Name of the license configuration.

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          Token for the next set of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LicenseOperationFailureList': [
                    {
                        'ResourceArn': 'string',
                        'ResourceType':
                        'EC2_INSTANCE'|'EC2_HOST'|'EC2_AMI'|'RDS'
                        |'SYSTEMS_MANAGER_MANAGED_INSTANCE',
                        'ErrorMessage': 'string',
                        'FailureTime': datetime(2015, 1, 1),
                        'OperationName': 'string',
                        'ResourceOwnerId': 'string',
                        'OperationRequestedBy': 'string',
                        'MetadataList': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **LicenseOperationFailureList** *(list) --*

              License configuration operations that failed.

              - *(dict) --*

                Describes the failure of a license operation.

                - **ResourceArn** *(string) --*

                  Amazon Resource Name (ARN) of the resource.

                - **ResourceType** *(string) --*

                  Resource type.

                - **ErrorMessage** *(string) --*

                  Error message.

                - **FailureTime** *(datetime) --*

                  Failure time.

                - **OperationName** *(string) --*

                  Name of the operation.

                - **ResourceOwnerId** *(string) --*

                  ID of the AWS account that owns the resource.

                - **OperationRequestedBy** *(string) --*

                  The requester is "License Manager Automated Discovery".

                - **MetadataList** *(list) --*

                  Reserved.

                  - *(dict) --*

                    Reserved.

                    - **Name** *(string) --*

                      Reserved.

                    - **Value** *(string) --*

                      Reserved.

            - **NextToken** *(string) --*

              Token for the next set of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_license_configurations(
        self,
        LicenseConfigurationArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListLicenseConfigurationsFiltersTypeDef] = None,
    ) -> ClientListLicenseConfigurationsResponseTypeDef:
        """
        Lists the license configurations for your account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseConfigurations>`_

        **Request Syntax**
        ::

          response = client.list_license_configurations(
              LicenseConfigurationArns=[
                  'string',
              ],
              MaxResults=123,
              NextToken='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        :type LicenseConfigurationArns: list
        :param LicenseConfigurationArns:

          Amazon Resource Names (ARN) of the license configurations.

          - *(string) --*

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          Token for the next set of results.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              Token for the next set of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_license_specifications_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListLicenseSpecificationsForResourceResponseTypeDef:
        """
        Describes the license configurations for the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseSpecificationsForResource>`_

        **Request Syntax**
        ::

          response = client.list_license_specifications_for_resource(
              ResourceArn='string',
              MaxResults=123,
              NextToken='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of a resource that has an associated license configuration.

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          Token for the next set of results.

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
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **LicenseSpecifications** *(list) --*

              License configurations associated with a resource.

              - *(dict) --*

                Details for associating a license configuration with a resource.

                - **LicenseConfigurationArn** *(string) --*

                  Amazon Resource Name (ARN) of the license configuration.

            - **NextToken** *(string) --*

              Token for the next set of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_inventory(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListResourceInventoryFiltersTypeDef] = None,
    ) -> ClientListResourceInventoryResponseTypeDef:
        """
        Lists resources managed using Systems Manager inventory.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListResourceInventory>`_

        **Request Syntax**
        ::

          response = client.list_resource_inventory(
              MaxResults=123,
              NextToken='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Condition': 'EQUALS'|'NOT_EQUALS'|'BEGINS_WITH'|'CONTAINS',
                      'Value': 'string'
                  },
              ]
          )
        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          Token for the next set of results.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              Token for the next set of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified license configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of the license configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              Information about the tags.

              - *(dict) --*

                Details about a tag for a license configuration.

                - **Key** *(string) --*

                  Tag key.

                - **Value** *(string) --*

                  Tag value.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_usage_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListUsageForLicenseConfigurationFiltersTypeDef] = None,
    ) -> ClientListUsageForLicenseConfigurationResponseTypeDef:
        """
        Lists all license usage records for a license configuration, displaying license consumption
        details by resource at a selected point in time. Use this action to audit the current
        license consumption for any license inventory and configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListUsageForLicenseConfiguration>`_

        **Request Syntax**
        ::

          response = client.list_usage_for_license_configuration(
              LicenseConfigurationArn='string',
              MaxResults=123,
              NextToken='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of the license configuration.

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return in a single call.

        :type NextToken: string
        :param NextToken:

          Token for the next set of results.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              Token for the next set of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified license configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of the license configuration.

        :type Tags: list
        :param Tags: **[REQUIRED]**

          One or more tags.

          - *(dict) --*

            Details about a tag for a license configuration.

            - **Key** *(string) --*

              Tag key.

            - **Value** *(string) --*

              Tag value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified license configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of the license configuration.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          Keys identifying the tags to remove.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_license_configuration(
        self,
        LicenseConfigurationArn: str,
        LicenseConfigurationStatus: Literal["AVAILABLE", "DISABLED"] = None,
        LicenseRules: List[str] = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        Name: str = None,
        Description: str = None,
        ProductInformationList: List[
            ClientUpdateLicenseConfigurationProductInformationListTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        Modifies the attributes of an existing license configuration.

        A license configuration is an abstraction of a customer license agreement that can be
        consumed and enforced by License Manager. Components include specifications for the license
        type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy,
        Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a VM must be
        associated with a host), and the number of licenses purchased and used.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/UpdateLicenseConfiguration>`_

        **Request Syntax**
        ::

          response = client.update_license_configuration(
              LicenseConfigurationArn='string',
              LicenseConfigurationStatus='AVAILABLE'|'DISABLED',
              LicenseRules=[
                  'string',
              ],
              LicenseCount=123,
              LicenseCountHardLimit=True|False,
              Name='string',
              Description='string',
              ProductInformationList=[
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
              ]
          )
        :type LicenseConfigurationArn: string
        :param LicenseConfigurationArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of the license configuration.

        :type LicenseConfigurationStatus: string
        :param LicenseConfigurationStatus:

          New status of the license configuration.

        :type LicenseRules: list
        :param LicenseRules:

          New license rules.

          - *(string) --*

        :type LicenseCount: integer
        :param LicenseCount:

          New number of licenses managed by the license configuration.

        :type LicenseCountHardLimit: boolean
        :param LicenseCountHardLimit:

          New hard limit of the number of available licenses.

        :type Name: string
        :param Name:

          New name of the license configuration.

        :type Description: string
        :param Description:

          New description of the license configuration.

        :type ProductInformationList: list
        :param ProductInformationList:

          New product information.

          - *(dict) --*

            Describes product information for a license configuration.

            - **ResourceType** *(string) --* **[REQUIRED]**

              Resource type. The value is ``SSM_MANAGED`` .

            - **ProductInformationFilterList** *(list) --* **[REQUIRED]**

              Product information filters. The following filters and logical operators are
              supported:

              * ``Application Name`` - The name of the application. Logical operator is ``EQUALS`` .

              * ``Application Publisher`` - The publisher of the application. Logical operator is
              ``EQUALS`` .

              * ``Application Version`` - The version of the application. Logical operator is
              ``EQUALS`` .

              * ``Platform Name`` - The name of the platform. Logical operator is ``EQUALS`` .

              * ``Platform Type`` - The platform type. Logical operator is ``EQUALS`` .

              * ``License Included`` - The type of license included. Logical operators are
              ``EQUALS`` and ``NOT_EQUALS`` . Possible values are ``sql-server-enterprise`` |
              ``sql-server-standard`` | ``sql-server-web`` | ``windows-server-datacenter`` .

              - *(dict) --*

                Describes product information filters.

                - **ProductInformationFilterName** *(string) --* **[REQUIRED]**

                  Filter name.

                - **ProductInformationFilterValue** *(list) --* **[REQUIRED]**

                  Filter value.

                  - *(string) --*

                - **ProductInformationFilterComparator** *(string) --* **[REQUIRED]**

                  Logical operator.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_license_specifications_for_resource(
        self,
        ResourceArn: str,
        AddLicenseSpecifications: List[
            ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef
        ] = None,
        RemoveLicenseSpecifications: List[
            ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        Adds or removes the specified license configurations for the specified AWS resource.

        You can update the license specifications of AMIs, instances, and hosts. You cannot update
        the license specifications for launch templates and AWS CloudFormation templates, as they
        send license configurations to the operation that creates the resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/UpdateLicenseSpecificationsForResource>`_

        **Request Syntax**
        ::

          response = client.update_license_specifications_for_resource(
              ResourceArn='string',
              AddLicenseSpecifications=[
                  {
                      'LicenseConfigurationArn': 'string'
                  },
              ],
              RemoveLicenseSpecifications=[
                  {
                      'LicenseConfigurationArn': 'string'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          Amazon Resource Name (ARN) of the AWS resource.

        :type AddLicenseSpecifications: list
        :param AddLicenseSpecifications:

          ARNs of the license configurations to add.

          - *(dict) --*

            Details for associating a license configuration with a resource.

            - **LicenseConfigurationArn** *(string) --* **[REQUIRED]**

              Amazon Resource Name (ARN) of the license configuration.

        :type RemoveLicenseSpecifications: list
        :param RemoveLicenseSpecifications:

          ARNs of the license configurations to remove.

          - *(dict) --*

            Details for associating a license configuration with a resource.

            - **LicenseConfigurationArn** *(string) --* **[REQUIRED]**

              Amazon Resource Name (ARN) of the license configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_service_settings(
        self,
        S3BucketArn: str = None,
        SnsTopicArn: str = None,
        OrganizationConfiguration: ClientUpdateServiceSettingsOrganizationConfigurationTypeDef = None,
        EnableCrossAccountsDiscovery: bool = None,
    ) -> Dict[str, Any]:
        """
        Updates License Manager settings for the current Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/UpdateServiceSettings>`_

        **Request Syntax**
        ::

          response = client.update_service_settings(
              S3BucketArn='string',
              SnsTopicArn='string',
              OrganizationConfiguration={
                  'EnableIntegration': True|False
              },
              EnableCrossAccountsDiscovery=True|False
          )
        :type S3BucketArn: string
        :param S3BucketArn:

          Amazon Resource Name (ARN) of the Amazon S3 bucket where the License Manager information
          is stored.

        :type SnsTopicArn: string
        :param SnsTopicArn:

          Amazon Resource Name (ARN) of the Amazon SNS topic used for License Manager alerts.

        :type OrganizationConfiguration: dict
        :param OrganizationConfiguration:

          Enables integration with AWS Organizations for cross-account discovery.

          - **EnableIntegration** *(boolean) --* **[REQUIRED]**

            Enables AWS Organization integration.

        :type EnableCrossAccountsDiscovery: boolean
        :param EnableCrossAccountsDiscovery:

          Activates cross-account discovery.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_associations_for_license_configuration"]
    ) -> paginator_scope.ListAssociationsForLicenseConfigurationPaginator:
        """
        Get Paginator for `list_associations_for_license_configuration` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_license_configurations"]
    ) -> paginator_scope.ListLicenseConfigurationsPaginator:
        """
        Get Paginator for `list_license_configurations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_license_specifications_for_resource"]
    ) -> paginator_scope.ListLicenseSpecificationsForResourcePaginator:
        """
        Get Paginator for `list_license_specifications_for_resource` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_inventory"]
    ) -> paginator_scope.ListResourceInventoryPaginator:
        """
        Get Paginator for `list_resource_inventory` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_usage_for_license_configuration"]
    ) -> paginator_scope.ListUsageForLicenseConfigurationPaginator:
        """
        Get Paginator for `list_usage_for_license_configuration` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AuthorizationException: Boto3ClientError
    ClientError: Boto3ClientError
    FailedDependencyException: Boto3ClientError
    FilterLimitExceededException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidResourceStateException: Boto3ClientError
    LicenseUsageException: Boto3ClientError
    RateLimitExceededException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ServerInternalException: Boto3ClientError
