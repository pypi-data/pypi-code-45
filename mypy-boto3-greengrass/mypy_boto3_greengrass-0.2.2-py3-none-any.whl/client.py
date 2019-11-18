"Main interface for greengrass Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_greengrass.client as client_scope

# pylint: disable=import-self
import mypy_boto3_greengrass.paginator as paginator_scope
from mypy_boto3_greengrass.type_defs import (
    ClientAssociateRoleToGroupResponseTypeDef,
    ClientAssociateServiceRoleToAccountResponseTypeDef,
    ClientCreateConnectorDefinitionInitialVersionTypeDef,
    ClientCreateConnectorDefinitionResponseTypeDef,
    ClientCreateConnectorDefinitionVersionResponseTypeDef,
    ClientCreateCoreDefinitionInitialVersionTypeDef,
    ClientCreateCoreDefinitionResponseTypeDef,
    ClientCreateCoreDefinitionVersionCoresTypeDef,
    ClientCreateCoreDefinitionVersionResponseTypeDef,
    ClientCreateDeploymentResponseTypeDef,
    ClientCreateDeviceDefinitionInitialVersionTypeDef,
    ClientCreateDeviceDefinitionResponseTypeDef,
    ClientCreateDeviceDefinitionVersionDevicesTypeDef,
    ClientCreateDeviceDefinitionVersionResponseTypeDef,
    ClientCreateFunctionDefinitionInitialVersionTypeDef,
    ClientCreateFunctionDefinitionResponseTypeDef,
    ClientCreateFunctionDefinitionVersionFunctionsTypeDef,
    ClientCreateFunctionDefinitionVersionResponseTypeDef,
    ClientCreateGroupCertificateAuthorityResponseTypeDef,
    ClientCreateGroupInitialVersionTypeDef,
    ClientCreateGroupResponseTypeDef,
    ClientCreateGroupVersionResponseTypeDef,
    ClientCreateLoggerDefinitionInitialVersionTypeDef,
    ClientCreateLoggerDefinitionResponseTypeDef,
    ClientCreateLoggerDefinitionVersionLoggersTypeDef,
    ClientCreateLoggerDefinitionVersionResponseTypeDef,
    ClientCreateResourceDefinitionInitialVersionTypeDef,
    ClientCreateResourceDefinitionResponseTypeDef,
    ClientCreateResourceDefinitionVersionResourcesTypeDef,
    ClientCreateResourceDefinitionVersionResponseTypeDef,
    ClientCreateSoftwareUpdateJobResponseTypeDef,
    ClientCreateSubscriptionDefinitionInitialVersionTypeDef,
    ClientCreateSubscriptionDefinitionResponseTypeDef,
    ClientCreateSubscriptionDefinitionVersionResponseTypeDef,
    ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef,
    ClientDisassociateRoleFromGroupResponseTypeDef,
    ClientDisassociateServiceRoleFromAccountResponseTypeDef,
    ClientGetAssociatedRoleResponseTypeDef,
    ClientGetBulkDeploymentStatusResponseTypeDef,
    ClientGetConnectivityInfoResponseTypeDef,
    ClientGetConnectorDefinitionResponseTypeDef,
    ClientGetConnectorDefinitionVersionResponseTypeDef,
    ClientGetCoreDefinitionResponseTypeDef,
    ClientGetCoreDefinitionVersionResponseTypeDef,
    ClientGetDeploymentStatusResponseTypeDef,
    ClientGetDeviceDefinitionResponseTypeDef,
    ClientGetDeviceDefinitionVersionResponseTypeDef,
    ClientGetFunctionDefinitionResponseTypeDef,
    ClientGetFunctionDefinitionVersionResponseTypeDef,
    ClientGetGroupCertificateAuthorityResponseTypeDef,
    ClientGetGroupCertificateConfigurationResponseTypeDef,
    ClientGetGroupResponseTypeDef,
    ClientGetGroupVersionResponseTypeDef,
    ClientGetLoggerDefinitionResponseTypeDef,
    ClientGetLoggerDefinitionVersionResponseTypeDef,
    ClientGetResourceDefinitionResponseTypeDef,
    ClientGetResourceDefinitionVersionResponseTypeDef,
    ClientGetServiceRoleForAccountResponseTypeDef,
    ClientGetSubscriptionDefinitionResponseTypeDef,
    ClientGetSubscriptionDefinitionVersionResponseTypeDef,
    ClientListBulkDeploymentDetailedReportsResponseTypeDef,
    ClientListBulkDeploymentsResponseTypeDef,
    ClientListConnectorDefinitionVersionsResponseTypeDef,
    ClientListConnectorDefinitionsResponseTypeDef,
    ClientListCoreDefinitionVersionsResponseTypeDef,
    ClientListCoreDefinitionsResponseTypeDef,
    ClientListDeploymentsResponseTypeDef,
    ClientListDeviceDefinitionVersionsResponseTypeDef,
    ClientListDeviceDefinitionsResponseTypeDef,
    ClientListFunctionDefinitionVersionsResponseTypeDef,
    ClientListGroupCertificateAuthoritiesResponseTypeDef,
    ClientListGroupsResponseTypeDef,
    ClientListLoggerDefinitionVersionsResponseTypeDef,
    ClientListLoggerDefinitionsResponseTypeDef,
    ClientListResourceDefinitionVersionsResponseTypeDef,
    ClientListResourceDefinitionsResponseTypeDef,
    ClientListSubscriptionDefinitionVersionsResponseTypeDef,
    ClientListSubscriptionDefinitionsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientResetDeploymentsResponseTypeDef,
    ClientStartBulkDeploymentResponseTypeDef,
    ClientUpdateConnectivityInfoConnectivityInfoTypeDef,
    ClientUpdateConnectivityInfoResponseTypeDef,
    ClientUpdateGroupCertificateConfigurationResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_role_to_group(
        self, GroupId: str, RoleArn: str
    ) -> ClientAssociateRoleToGroupResponseTypeDef:
        """
        Associates a role with a group. Your Greengrass core will use the role to access AWS cloud
        services. The role's permissions should allow Greengrass core Lambda functions to perform actions
        against the cloud.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/AssociateRoleToGroup>`_

        **Request Syntax**
        ::

          response = client.associate_role_to_group(
              GroupId='string',
              RoleArn='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :type RoleArn: string
        :param RoleArn: **[REQUIRED]** The ARN of the role you wish to associate with this group. The
        existence of the role is not validated.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AssociatedAt': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **AssociatedAt** *(string) --* The time, in milliseconds since the epoch, when the role ARN
            was associated with the group.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_service_role_to_account(
        self, RoleArn: str
    ) -> ClientAssociateServiceRoleToAccountResponseTypeDef:
        """
        Associates a role with your account. AWS IoT Greengrass will use the role to access your Lambda
        functions and AWS IoT resources. This is necessary for deployments to succeed. The role must have
        at least minimum permissions in the policy ''AWSGreengrassResourceAccessRolePolicy''.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/AssociateServiceRoleToAccount>`_

        **Request Syntax**
        ::

          response = client.associate_service_role_to_account(
              RoleArn='string'
          )
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]** The ARN of the service role you wish to associate with your account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AssociatedAt': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **AssociatedAt** *(string) --* The time when the service role was associated with the account.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
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
    def create_connector_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateConnectorDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateConnectorDefinitionResponseTypeDef:
        """
        Creates a connector definition. You may provide the initial version of the connector definition now
        or use ''CreateConnectorDefinitionVersion'' at a later time.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateConnectorDefinition>`_

        **Request Syntax**
        ::

          response = client.create_connector_definition(
              AmznClientToken='string',
              InitialVersion={
                  'Connectors': [
                      {
                          'ConnectorArn': 'string',
                          'Id': 'string',
                          'Parameters': {
                              'string': 'string'
                          }
                      },
                  ]
              },
              Name='string',
              tags={
                  'string': 'string'
              }
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the connector definition.

          - **Connectors** *(list) --* A list of references to connectors in this version, with their
          corresponding configuration settings.

            - *(dict) --* Information about a connector. Connectors run on the Greengrass core and contain
            built-in integration with local infrastructure, device protocols, AWS, and other cloud services.

              - **ConnectorArn** *(string) --* **[REQUIRED]** The ARN of the connector.

              - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the connector. This
              value must be unique within the connector definition version. Max length is 128 characters
              with pattern [a-zA-Z0-9:_-]+.

              - **Parameters** *(dict) --* The parameters or configuration that the connector uses.

                - *(string) --*

                  - *(string) --*

        :type Name: string
        :param Name: The name of the connector definition.

        :type tags: dict
        :param tags: Tag(s) to add to the new resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_connector_definition_version(
        self,
        ConnectorDefinitionId: str,
        AmznClientToken: str = None,
        Connectors: List[Any] = None,
    ) -> ClientCreateConnectorDefinitionVersionResponseTypeDef:
        """
        Creates a version of a connector definition which has already been defined.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateConnectorDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.create_connector_definition_version(
              AmznClientToken='string',
              ConnectorDefinitionId='string',
              Connectors=[
                  {
                      'ConnectorArn': 'string',
                      'Id': 'string',
                      'Parameters': {
                          'string': 'string'
                      }
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type ConnectorDefinitionId: string
        :param ConnectorDefinitionId: **[REQUIRED]** The ID of the connector definition.

        :type Connectors: list
        :param Connectors: A list of references to connectors in this version, with their corresponding
        configuration settings.

          - *(dict) --* Information about a connector. Connectors run on the Greengrass core and contain
          built-in integration with local infrastructure, device protocols, AWS, and other cloud services.

            - **ConnectorArn** *(string) --* **[REQUIRED]** The ARN of the connector.

            - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the connector. This
            value must be unique within the connector definition version. Max length is 128 characters with
            pattern [a-zA-Z0-9:_-]+.

            - **Parameters** *(dict) --* The parameters or configuration that the connector uses.

              - *(string) --*

                - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            version was created.

            - **Id** *(string) --* The ID of the version.

            - **Version** *(string) --* The unique ID of the version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_core_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateCoreDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateCoreDefinitionResponseTypeDef:
        """
        Creates a core definition. You may provide the initial version of the core definition now or use
        ''CreateCoreDefinitionVersion'' at a later time. Greengrass groups must each contain exactly one
        Greengrass core.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateCoreDefinition>`_

        **Request Syntax**
        ::

          response = client.create_core_definition(
              AmznClientToken='string',
              InitialVersion={
                  'Cores': [
                      {
                          'CertificateArn': 'string',
                          'Id': 'string',
                          'SyncShadow': True|False,
                          'ThingArn': 'string'
                      },
                  ]
              },
              Name='string',
              tags={
                  'string': 'string'
              }
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the core definition.

          - **Cores** *(list) --* A list of cores in the core definition version.

            - *(dict) --* Information about a core.

              - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
              the core.

              - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the core. This value
              must be unique within the core definition version. Max length is 128 characters with pattern
              ''[a-zA-Z0-9:_-]+''.

              - **SyncShadow** *(boolean) --* If true, the core's local shadow is automatically synced with
              the cloud.

              - **ThingArn** *(string) --* **[REQUIRED]** The ARN of the thing which is the core.

        :type Name: string
        :param Name: The name of the core definition.

        :type tags: dict
        :param tags: Tag(s) to add to the new resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_core_definition_version(
        self,
        CoreDefinitionId: str,
        AmznClientToken: str = None,
        Cores: List[ClientCreateCoreDefinitionVersionCoresTypeDef] = None,
    ) -> ClientCreateCoreDefinitionVersionResponseTypeDef:
        """
        Creates a version of a core definition that has already been defined. Greengrass groups must each
        contain exactly one Greengrass core.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateCoreDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.create_core_definition_version(
              AmznClientToken='string',
              CoreDefinitionId='string',
              Cores=[
                  {
                      'CertificateArn': 'string',
                      'Id': 'string',
                      'SyncShadow': True|False,
                      'ThingArn': 'string'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.

        :type Cores: list
        :param Cores: A list of cores in the core definition version.

          - *(dict) --* Information about a core.

            - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
            the core.

            - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the core. This value
            must be unique within the core definition version. Max length is 128 characters with pattern
            ''[a-zA-Z0-9:_-]+''.

            - **SyncShadow** *(boolean) --* If true, the core's local shadow is automatically synced with
            the cloud.

            - **ThingArn** *(string) --* **[REQUIRED]** The ARN of the thing which is the core.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            version was created.

            - **Id** *(string) --* The ID of the version.

            - **Version** *(string) --* The unique ID of the version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment(
        self,
        DeploymentType: str,
        GroupId: str,
        AmznClientToken: str = None,
        DeploymentId: str = None,
        GroupVersionId: str = None,
    ) -> ClientCreateDeploymentResponseTypeDef:
        """
        Creates a deployment. ''CreateDeployment'' requests are idempotent with respect to the
        ''X-Amzn-Client-Token'' token and the request parameters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateDeployment>`_

        **Request Syntax**
        ::

          response = client.create_deployment(
              AmznClientToken='string',
              DeploymentId='string',
              DeploymentType='NewDeployment'|'Redeployment'|'ResetDeployment'|'ForceResetDeployment',
              GroupId='string',
              GroupVersionId='string'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type DeploymentId: string
        :param DeploymentId: The ID of the deployment if you wish to redeploy a previous deployment.

        :type DeploymentType: string
        :param DeploymentType: **[REQUIRED]** The type of deployment. When used for ''CreateDeployment'',
        only ''NewDeployment'' and ''Redeployment'' are valid.

        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :type GroupVersionId: string
        :param GroupVersionId: The ID of the group version to be deployed.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DeploymentArn': 'string',
                'DeploymentId': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The group was deployed.

            - **DeploymentArn** *(string) --* The ARN of the deployment.

            - **DeploymentId** *(string) --* The ID of the deployment.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_device_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateDeviceDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateDeviceDefinitionResponseTypeDef:
        """
        Creates a device definition. You may provide the initial version of the device definition now or
        use ''CreateDeviceDefinitionVersion'' at a later time.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateDeviceDefinition>`_

        **Request Syntax**
        ::

          response = client.create_device_definition(
              AmznClientToken='string',
              InitialVersion={
                  'Devices': [
                      {
                          'CertificateArn': 'string',
                          'Id': 'string',
                          'SyncShadow': True|False,
                          'ThingArn': 'string'
                      },
                  ]
              },
              Name='string',
              tags={
                  'string': 'string'
              }
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the device definition.

          - **Devices** *(list) --* A list of devices in the definition version.

            - *(dict) --* Information about a device.

              - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
              the device.

              - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the device. This
              value must be unique within the device definition version. Max length is 128 characters with
              pattern ''[a-zA-Z0-9:_-]+''.

              - **SyncShadow** *(boolean) --* If true, the device's local shadow will be automatically
              synced with the cloud.

              - **ThingArn** *(string) --* **[REQUIRED]** The thing ARN of the device.

        :type Name: string
        :param Name: The name of the device definition.

        :type tags: dict
        :param tags: Tag(s) to add to the new resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_device_definition_version(
        self,
        DeviceDefinitionId: str,
        AmznClientToken: str = None,
        Devices: List[ClientCreateDeviceDefinitionVersionDevicesTypeDef] = None,
    ) -> ClientCreateDeviceDefinitionVersionResponseTypeDef:
        """
        Creates a version of a device definition that has already been defined.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateDeviceDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.create_device_definition_version(
              AmznClientToken='string',
              DeviceDefinitionId='string',
              Devices=[
                  {
                      'CertificateArn': 'string',
                      'Id': 'string',
                      'SyncShadow': True|False,
                      'ThingArn': 'string'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.

        :type Devices: list
        :param Devices: A list of devices in the definition version.

          - *(dict) --* Information about a device.

            - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
            the device.

            - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the device. This value
            must be unique within the device definition version. Max length is 128 characters with pattern
            ''[a-zA-Z0-9:_-]+''.

            - **SyncShadow** *(boolean) --* If true, the device's local shadow will be automatically synced
            with the cloud.

            - **ThingArn** *(string) --* **[REQUIRED]** The thing ARN of the device.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            version was created.

            - **Id** *(string) --* The ID of the version.

            - **Version** *(string) --* The unique ID of the version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_function_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateFunctionDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateFunctionDefinitionResponseTypeDef:
        """
        Creates a Lambda function definition which contains a list of Lambda functions and their
        configurations to be used in a group. You can create an initial version of the definition by
        providing a list of Lambda functions and their configurations now, or use
        ''CreateFunctionDefinitionVersion'' later.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateFunctionDefinition>`_

        **Request Syntax**
        ::

          response = client.create_function_definition(
              AmznClientToken='string',
              InitialVersion={
                  'DefaultConfig': {
                      'Execution': {
                          'IsolationMode': 'GreengrassContainer'|'NoContainer',
                          'RunAs': {
                              'Gid': 123,
                              'Uid': 123
                          }
                      }
                  },
                  'Functions': [
                      {
                          'FunctionArn': 'string',
                          'FunctionConfiguration': {
                              'EncodingType': 'binary'|'json',
                              'Environment': {
                                  'AccessSysfs': True|False,
                                  'Execution': {
                                      'IsolationMode': 'GreengrassContainer'|'NoContainer',
                                      'RunAs': {
                                          'Gid': 123,
                                          'Uid': 123
                                      }
                                  },
                                  'ResourceAccessPolicies': [
                                      {
                                          'Permission': 'ro'|'rw',
                                          'ResourceId': 'string'
                                      },
                                  ],
                                  'Variables': {
                                      'string': 'string'
                                  }
                              },
                              'ExecArgs': 'string',
                              'Executable': 'string',
                              'MemorySize': 123,
                              'Pinned': True|False,
                              'Timeout': 123
                          },
                          'Id': 'string'
                      },
                  ]
              },
              Name='string',
              tags={
                  'string': 'string'
              }
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the function definition.

          - **DefaultConfig** *(dict) --* The default configuration that applies to all Lambda functions in
          this function definition version. Individual Lambda functions can override these settings.

            - **Execution** *(dict) --* Configuration information that specifies how a Lambda function runs.

              - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a Greengrass
              container (default) or without containerization. Unless your scenario requires that you run
              without containerization, we recommend that you run in a Greengrass container. Omit this
              value to run the Lambda function with the default containerization for the group.

              - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when running
              the Lambda function. You can specify one or both values to override the default values. We
              recommend that you avoid running as root unless absolutely necessary to minimize the risk of
              unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
              ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
              ''allowFunctionsToRunAsRoot'' to ''yes''.

                - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda function.

                - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda function.

          - **Functions** *(list) --* A list of Lambda functions in this function definition version.

            - *(dict) --* Information about a Lambda function.

              - **FunctionArn** *(string) --* The ARN of the Lambda function.

              - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.

                - **EncodingType** *(string) --* The expected encoding type of the input payload for the
                function. The default is ''json''.

                - **Environment** *(dict) --* The environment configuration of the function.

                  - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the
                  host's /sys folder. Use this when the Lambda function needs to read device information
                  from /sys. This setting applies only when you run the Lambda function in a Greengrass
                  container.

                  - **Execution** *(dict) --* Configuration related to executing the Lambda function

                    - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
                    Greengrass container (default) or without containerization. Unless your scenario
                    requires that you run without containerization, we recommend that you run in a
                    Greengrass container. Omit this value to run the Lambda function with the default
                    containerization for the group.

                    - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
                    running the Lambda function. You can specify one or both values to override the default
                    values. We recommend that you avoid running as root unless absolutely necessary to
                    minimize the risk of unintended changes or malicious attacks. To run as root, you must
                    set ''IsolationMode'' to ''NoContainer'' and update config.json in
                    ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

                      - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
                      function.

                      - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
                      function.

                  - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions,
                  to which the Lambda function will be granted access. A Lambda function can have at most
                  10 resources. ResourceAccessPolicies apply only when you run the Lambda function in a
                  Greengrass container.

                    - *(dict) --* A policy used by the function to access a resource.

                      - **Permission** *(string) --* The permissions that the Lambda function has to the
                      resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

                      - **ResourceId** *(string) --* **[REQUIRED]** The ID of the resource. (This ID is
                      assigned to the resource when you create the resource definiton.)

                  - **Variables** *(dict) --* Environment variables for the Lambda function's configuration.

                    - *(string) --*

                      - *(string) --*

                - **ExecArgs** *(string) --* The execution arguments.

                - **Executable** *(string) --* The name of the function executable.

                - **MemorySize** *(integer) --* The memory size, in KB, which the function requires. This
                setting is not applicable and should be cleared when you run the Lambda function without
                containerization.

                - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is
                long-lived and starts when the core starts.

                - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should
                terminate the function. This timeout still applies to pinned Lambda functions for each
                request.

              - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the function. This
              value must be unique within the function definition version. Max length is 128 characters
              with pattern ''[a-zA-Z0-9:_-]+''.

        :type Name: string
        :param Name: The name of the function definition.

        :type tags: dict
        :param tags: Tag(s) to add to the new resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_function_definition_version(
        self,
        FunctionDefinitionId: str,
        AmznClientToken: str = None,
        DefaultConfig: Dict[str, Any] = None,
        Functions: List[ClientCreateFunctionDefinitionVersionFunctionsTypeDef] = None,
    ) -> ClientCreateFunctionDefinitionVersionResponseTypeDef:
        """
        Creates a version of a Lambda function definition that has already been defined.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateFunctionDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.create_function_definition_version(
              AmznClientToken='string',
              DefaultConfig={
                  'Execution': {
                      'IsolationMode': 'GreengrassContainer'|'NoContainer',
                      'RunAs': {
                          'Gid': 123,
                          'Uid': 123
                      }
                  }
              },
              FunctionDefinitionId='string',
              Functions=[
                  {
                      'FunctionArn': 'string',
                      'FunctionConfiguration': {
                          'EncodingType': 'binary'|'json',
                          'Environment': {
                              'AccessSysfs': True|False,
                              'Execution': {
                                  'IsolationMode': 'GreengrassContainer'|'NoContainer',
                                  'RunAs': {
                                      'Gid': 123,
                                      'Uid': 123
                                  }
                              },
                              'ResourceAccessPolicies': [
                                  {
                                      'Permission': 'ro'|'rw',
                                      'ResourceId': 'string'
                                  },
                              ],
                              'Variables': {
                                  'string': 'string'
                              }
                          },
                          'ExecArgs': 'string',
                          'Executable': 'string',
                          'MemorySize': 123,
                          'Pinned': True|False,
                          'Timeout': 123
                      },
                      'Id': 'string'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type DefaultConfig: dict
        :param DefaultConfig: The default configuration that applies to all Lambda functions in this
        function definition version. Individual Lambda functions can override these settings.

          - **Execution** *(dict) --* Configuration information that specifies how a Lambda function runs.

            - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a Greengrass
            container (default) or without containerization. Unless your scenario requires that you run
            without containerization, we recommend that you run in a Greengrass container. Omit this value
            to run the Lambda function with the default containerization for the group.

            - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when running
            the Lambda function. You can specify one or both values to override the default values. We
            recommend that you avoid running as root unless absolutely necessary to minimize the risk of
            unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
            ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
            ''allowFunctionsToRunAsRoot'' to ''yes''.

              - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda function.

              - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda function.

        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.

        :type Functions: list
        :param Functions: A list of Lambda functions in this function definition version.

          - *(dict) --* Information about a Lambda function.

            - **FunctionArn** *(string) --* The ARN of the Lambda function.

            - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.

              - **EncodingType** *(string) --* The expected encoding type of the input payload for the
              function. The default is ''json''.

              - **Environment** *(dict) --* The environment configuration of the function.

                - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the
                host's /sys folder. Use this when the Lambda function needs to read device information from
                /sys. This setting applies only when you run the Lambda function in a Greengrass container.

                - **Execution** *(dict) --* Configuration related to executing the Lambda function

                  - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
                  Greengrass container (default) or without containerization. Unless your scenario requires
                  that you run without containerization, we recommend that you run in a Greengrass
                  container. Omit this value to run the Lambda function with the default containerization
                  for the group.

                  - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
                  running the Lambda function. You can specify one or both values to override the default
                  values. We recommend that you avoid running as root unless absolutely necessary to
                  minimize the risk of unintended changes or malicious attacks. To run as root, you must
                  set ''IsolationMode'' to ''NoContainer'' and update config.json in
                  ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

                    - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
                    function.

                    - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
                    function.

                - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions,
                to which the Lambda function will be granted access. A Lambda function can have at most 10
                resources. ResourceAccessPolicies apply only when you run the Lambda function in a
                Greengrass container.

                  - *(dict) --* A policy used by the function to access a resource.

                    - **Permission** *(string) --* The permissions that the Lambda function has to the
                    resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

                    - **ResourceId** *(string) --* **[REQUIRED]** The ID of the resource. (This ID is
                    assigned to the resource when you create the resource definiton.)

                - **Variables** *(dict) --* Environment variables for the Lambda function's configuration.

                  - *(string) --*

                    - *(string) --*

              - **ExecArgs** *(string) --* The execution arguments.

              - **Executable** *(string) --* The name of the function executable.

              - **MemorySize** *(integer) --* The memory size, in KB, which the function requires. This
              setting is not applicable and should be cleared when you run the Lambda function without
              containerization.

              - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is
              long-lived and starts when the core starts.

              - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should
              terminate the function. This timeout still applies to pinned Lambda functions for each
              request.

            - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the function. This
            value must be unique within the function definition version. Max length is 128 characters with
            pattern ''[a-zA-Z0-9:_-]+''.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            version was created.

            - **Id** *(string) --* The ID of the version.

            - **Version** *(string) --* The unique ID of the version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateGroupInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateGroupResponseTypeDef:
        """
        Creates a group. You may provide the initial version of the group or use ''CreateGroupVersion'' at
        a later time. Tip: You can use the ''gg_group_setup'' package
        (https://github.com/awslabs/aws-greengrass-group-setup) as a library or command-line application to
        create and deploy Greengrass groups.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateGroup>`_

        **Request Syntax**
        ::

          response = client.create_group(
              AmznClientToken='string',
              InitialVersion={
                  'ConnectorDefinitionVersionArn': 'string',
                  'CoreDefinitionVersionArn': 'string',
                  'DeviceDefinitionVersionArn': 'string',
                  'FunctionDefinitionVersionArn': 'string',
                  'LoggerDefinitionVersionArn': 'string',
                  'ResourceDefinitionVersionArn': 'string',
                  'SubscriptionDefinitionVersionArn': 'string'
              },
              Name='string',
              tags={
                  'string': 'string'
              }
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the group.

          - **ConnectorDefinitionVersionArn** *(string) --* The ARN of the connector definition version for
          this group.

          - **CoreDefinitionVersionArn** *(string) --* The ARN of the core definition version for this
          group.

          - **DeviceDefinitionVersionArn** *(string) --* The ARN of the device definition version for this
          group.

          - **FunctionDefinitionVersionArn** *(string) --* The ARN of the function definition version for
          this group.

          - **LoggerDefinitionVersionArn** *(string) --* The ARN of the logger definition version for this
          group.

          - **ResourceDefinitionVersionArn** *(string) --* The ARN of the resource definition version for
          this group.

          - **SubscriptionDefinitionVersionArn** *(string) --* The ARN of the subscription definition
          version for this group.

        :type Name: string
        :param Name: The name of the group.

        :type tags: dict
        :param tags: Tag(s) to add to the new resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The group was created.

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group_certificate_authority(
        self, GroupId: str, AmznClientToken: str = None
    ) -> ClientCreateGroupCertificateAuthorityResponseTypeDef:
        """
        Creates a CA for the group. If a CA already exists, it will rotate the existing CA.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateGroupCertificateAuthority>`_

        **Request Syntax**
        ::

          response = client.create_group_certificate_authority(
              AmznClientToken='string',
              GroupId='string'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GroupCertificateAuthorityArn': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the new active CA ARN.

            - **GroupCertificateAuthorityArn** *(string) --* The ARN of the group certificate authority.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group_version(
        self,
        GroupId: str,
        AmznClientToken: str = None,
        ConnectorDefinitionVersionArn: str = None,
        CoreDefinitionVersionArn: str = None,
        DeviceDefinitionVersionArn: str = None,
        FunctionDefinitionVersionArn: str = None,
        LoggerDefinitionVersionArn: str = None,
        ResourceDefinitionVersionArn: str = None,
        SubscriptionDefinitionVersionArn: str = None,
    ) -> ClientCreateGroupVersionResponseTypeDef:
        """
        Creates a version of a group which has already been defined.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateGroupVersion>`_

        **Request Syntax**
        ::

          response = client.create_group_version(
              AmznClientToken='string',
              ConnectorDefinitionVersionArn='string',
              CoreDefinitionVersionArn='string',
              DeviceDefinitionVersionArn='string',
              FunctionDefinitionVersionArn='string',
              GroupId='string',
              LoggerDefinitionVersionArn='string',
              ResourceDefinitionVersionArn='string',
              SubscriptionDefinitionVersionArn='string'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type ConnectorDefinitionVersionArn: string
        :param ConnectorDefinitionVersionArn: The ARN of the connector definition version for this group.

        :type CoreDefinitionVersionArn: string
        :param CoreDefinitionVersionArn: The ARN of the core definition version for this group.

        :type DeviceDefinitionVersionArn: string
        :param DeviceDefinitionVersionArn: The ARN of the device definition version for this group.

        :type FunctionDefinitionVersionArn: string
        :param FunctionDefinitionVersionArn: The ARN of the function definition version for this group.

        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :type LoggerDefinitionVersionArn: string
        :param LoggerDefinitionVersionArn: The ARN of the logger definition version for this group.

        :type ResourceDefinitionVersionArn: string
        :param ResourceDefinitionVersionArn: The ARN of the resource definition version for this group.

        :type SubscriptionDefinitionVersionArn: string
        :param SubscriptionDefinitionVersionArn: The ARN of the subscription definition version for this
        group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response contains information about the group version.

            - **Arn** *(string) --* The ARN of the version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            version was created.

            - **Id** *(string) --* The ID of the version.

            - **Version** *(string) --* The unique ID of the version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_logger_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateLoggerDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateLoggerDefinitionResponseTypeDef:
        """
        Creates a logger definition. You may provide the initial version of the logger definition now or
        use ''CreateLoggerDefinitionVersion'' at a later time.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateLoggerDefinition>`_

        **Request Syntax**
        ::

          response = client.create_logger_definition(
              AmznClientToken='string',
              InitialVersion={
                  'Loggers': [
                      {
                          'Component': 'GreengrassSystem'|'Lambda',
                          'Id': 'string',
                          'Level': 'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
                          'Space': 123,
                          'Type': 'FileSystem'|'AWSCloudWatch'
                      },
                  ]
              },
              Name='string',
              tags={
                  'string': 'string'
              }
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the logger definition.

          - **Loggers** *(list) --* A list of loggers.

            - *(dict) --* Information about a logger

              - **Component** *(string) --* **[REQUIRED]** The component that will be subject to logging.

              - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the logger. This
              value must be unique within the logger definition version. Max length is 128 characters with
              pattern ''[a-zA-Z0-9:_-]+''.

              - **Level** *(string) --* **[REQUIRED]** The level of the logs.

              - **Space** *(integer) --* The amount of file space, in KB, to use if the local file system
              is used for logging purposes.

              - **Type** *(string) --* **[REQUIRED]** The type of log output which will be used.

        :type Name: string
        :param Name: The name of the logger definition.

        :type tags: dict
        :param tags: Tag(s) to add to the new resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_logger_definition_version(
        self,
        LoggerDefinitionId: str,
        AmznClientToken: str = None,
        Loggers: List[ClientCreateLoggerDefinitionVersionLoggersTypeDef] = None,
    ) -> ClientCreateLoggerDefinitionVersionResponseTypeDef:
        """
        Creates a version of a logger definition that has already been defined.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateLoggerDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.create_logger_definition_version(
              AmznClientToken='string',
              LoggerDefinitionId='string',
              Loggers=[
                  {
                      'Component': 'GreengrassSystem'|'Lambda',
                      'Id': 'string',
                      'Level': 'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
                      'Space': 123,
                      'Type': 'FileSystem'|'AWSCloudWatch'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.

        :type Loggers: list
        :param Loggers: A list of loggers.

          - *(dict) --* Information about a logger

            - **Component** *(string) --* **[REQUIRED]** The component that will be subject to logging.

            - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the logger. This value
            must be unique within the logger definition version. Max length is 128 characters with pattern
            ''[a-zA-Z0-9:_-]+''.

            - **Level** *(string) --* **[REQUIRED]** The level of the logs.

            - **Space** *(integer) --* The amount of file space, in KB, to use if the local file system is
            used for logging purposes.

            - **Type** *(string) --* **[REQUIRED]** The type of log output which will be used.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            version was created.

            - **Id** *(string) --* The ID of the version.

            - **Version** *(string) --* The unique ID of the version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateResourceDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateResourceDefinitionResponseTypeDef:
        """
        Creates a resource definition which contains a list of resources to be used in a group. You can
        create an initial version of the definition by providing a list of resources now, or use
        ''CreateResourceDefinitionVersion'' later.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateResourceDefinition>`_

        **Request Syntax**
        ::

          response = client.create_resource_definition(
              AmznClientToken='string',
              InitialVersion={
                  'Resources': [
                      {
                          'Id': 'string',
                          'Name': 'string',
                          'ResourceDataContainer': {
                              'LocalDeviceResourceData': {
                                  'GroupOwnerSetting': {
                                      'AutoAddGroupOwner': True|False,
                                      'GroupOwner': 'string'
                                  },
                                  'SourcePath': 'string'
                              },
                              'LocalVolumeResourceData': {
                                  'DestinationPath': 'string',
                                  'GroupOwnerSetting': {
                                      'AutoAddGroupOwner': True|False,
                                      'GroupOwner': 'string'
                                  },
                                  'SourcePath': 'string'
                              },
                              'S3MachineLearningModelResourceData': {
                                  'DestinationPath': 'string',
                                  'S3Uri': 'string'
                              },
                              'SageMakerMachineLearningModelResourceData': {
                                  'DestinationPath': 'string',
                                  'SageMakerJobArn': 'string'
                              },
                              'SecretsManagerSecretResourceData': {
                                  'ARN': 'string',
                                  'AdditionalStagingLabelsToDownload': [
                                      'string',
                                  ]
                              }
                          }
                      },
                  ]
              },
              Name='string',
              tags={
                  'string': 'string'
              }
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the resource definition.

          - **Resources** *(list) --* A list of resources.

            - *(dict) --* Information about a resource.

              - **Id** *(string) --* **[REQUIRED]** The resource ID, used to refer to a resource in the
              Lambda function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
              This must be unique within a Greengrass group.

              - **Name** *(string) --* **[REQUIRED]** The descriptive resource name, which is displayed on
              the AWS IoT Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
              This must be unique within a Greengrass group.

              - **ResourceDataContainer** *(dict) --* **[REQUIRED]** A container of data for all resource
              types.

                - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device resource.

                  - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

                    - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds
                    the specified Linux OS group owner of the resource to the Lambda process privileges.
                    Thus the Lambda process will have the file access permissions of the added Linux group.

                    - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
                    added to the Lambda process. This field is optional.

                  - **SourcePath** *(string) --* The local absolute path of the device resource. The source
                  path for a device resource can refer only to a character device or block device under
                  ''/dev''.

                - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume resource.

                  - **DestinationPath** *(string) --* The absolute local path of the resource inside the
                  Lambda environment.

                  - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group privileges
                  for the Lambda process. This field is optional.

                    - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds
                    the specified Linux OS group owner of the resource to the Lambda process privileges.
                    Thus the Lambda process will have the file access permissions of the added Linux group.

                    - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
                    added to the Lambda process. This field is optional.

                  - **SourcePath** *(string) --* The local absolute path of the volume resource on the
                  host. The source path for a volume resource type cannot start with ''/sys''.

                - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon S3
                machine learning resource.

                  - **DestinationPath** *(string) --* The absolute local path of the resource inside the
                  Lambda environment.

                  - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model package
                  must be in tar.gz or .zip format.

                - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an
                Amazon SageMaker machine learning resource.

                  - **DestinationPath** *(string) --* The absolute local path of the resource inside the
                  Lambda environment.

                  - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
                  represents the source model.

                - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret
                resource, which references a secret from AWS Secrets Manager.

                  - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on the
                  core. The value of the secret's latest version (represented by the ''AWSCURRENT'' staging
                  label) is included by default.

                  - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels whose
                  values you want to make available on the core, in addition to ''AWSCURRENT''.

                    - *(string) --*

        :type Name: string
        :param Name: The name of the resource definition.

        :type tags: dict
        :param tags: Tag(s) to add to the new resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource_definition_version(
        self,
        ResourceDefinitionId: str,
        AmznClientToken: str = None,
        Resources: List[ClientCreateResourceDefinitionVersionResourcesTypeDef] = None,
    ) -> ClientCreateResourceDefinitionVersionResponseTypeDef:
        """
        Creates a version of a resource definition that has already been defined.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateResourceDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.create_resource_definition_version(
              AmznClientToken='string',
              ResourceDefinitionId='string',
              Resources=[
                  {
                      'Id': 'string',
                      'Name': 'string',
                      'ResourceDataContainer': {
                          'LocalDeviceResourceData': {
                              'GroupOwnerSetting': {
                                  'AutoAddGroupOwner': True|False,
                                  'GroupOwner': 'string'
                              },
                              'SourcePath': 'string'
                          },
                          'LocalVolumeResourceData': {
                              'DestinationPath': 'string',
                              'GroupOwnerSetting': {
                                  'AutoAddGroupOwner': True|False,
                                  'GroupOwner': 'string'
                              },
                              'SourcePath': 'string'
                          },
                          'S3MachineLearningModelResourceData': {
                              'DestinationPath': 'string',
                              'S3Uri': 'string'
                          },
                          'SageMakerMachineLearningModelResourceData': {
                              'DestinationPath': 'string',
                              'SageMakerJobArn': 'string'
                          },
                          'SecretsManagerSecretResourceData': {
                              'ARN': 'string',
                              'AdditionalStagingLabelsToDownload': [
                                  'string',
                              ]
                          }
                      }
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.

        :type Resources: list
        :param Resources: A list of resources.

          - *(dict) --* Information about a resource.

            - **Id** *(string) --* **[REQUIRED]** The resource ID, used to refer to a resource in the
            Lambda function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
            This must be unique within a Greengrass group.

            - **Name** *(string) --* **[REQUIRED]** The descriptive resource name, which is displayed on
            the AWS IoT Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
            This must be unique within a Greengrass group.

            - **ResourceDataContainer** *(dict) --* **[REQUIRED]** A container of data for all resource
            types.

              - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device resource.

                - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

                  - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds the
                  specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
                  Lambda process will have the file access permissions of the added Linux group.

                  - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
                  added to the Lambda process. This field is optional.

                - **SourcePath** *(string) --* The local absolute path of the device resource. The source
                path for a device resource can refer only to a character device or block device under
                ''/dev''.

              - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume resource.

                - **DestinationPath** *(string) --* The absolute local path of the resource inside the
                Lambda environment.

                - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group privileges for
                the Lambda process. This field is optional.

                  - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds the
                  specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
                  Lambda process will have the file access permissions of the added Linux group.

                  - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
                  added to the Lambda process. This field is optional.

                - **SourcePath** *(string) --* The local absolute path of the volume resource on the host.
                The source path for a volume resource type cannot start with ''/sys''.

              - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon S3
              machine learning resource.

                - **DestinationPath** *(string) --* The absolute local path of the resource inside the
                Lambda environment.

                - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model package
                must be in tar.gz or .zip format.

              - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon
              SageMaker machine learning resource.

                - **DestinationPath** *(string) --* The absolute local path of the resource inside the
                Lambda environment.

                - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
                represents the source model.

              - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret resource,
              which references a secret from AWS Secrets Manager.

                - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on the
                core. The value of the secret's latest version (represented by the ''AWSCURRENT'' staging
                label) is included by default.

                - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels whose
                values you want to make available on the core, in addition to ''AWSCURRENT''.

                  - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            version was created.

            - **Id** *(string) --* The ID of the version.

            - **Version** *(string) --* The unique ID of the version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_software_update_job(
        self,
        S3UrlSignerRole: str,
        SoftwareToUpdate: str,
        UpdateTargets: List[Any],
        UpdateTargetsArchitecture: str,
        UpdateTargetsOperatingSystem: str,
        AmznClientToken: str = None,
        UpdateAgentLogLevel: str = None,
    ) -> ClientCreateSoftwareUpdateJobResponseTypeDef:
        """
        Creates a software update for a core or group of cores (specified as an IoT thing group.) Use this
        to update the OTA Agent as well as the Greengrass core software. It makes use of the IoT Jobs
        feature which provides additional commands to manage a Greengrass core software update job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSoftwareUpdateJob>`_

        **Request Syntax**
        ::

          response = client.create_software_update_job(
              AmznClientToken='string',
              S3UrlSignerRole='string',
              SoftwareToUpdate='core'|'ota_agent',
              UpdateAgentLogLevel='NONE'|'TRACE'|'DEBUG'|'VERBOSE'|'INFO'|'WARN'|'ERROR'|'FATAL',
              UpdateTargets=[
                  'string',
              ],
              UpdateTargetsArchitecture='armv6l'|'armv7l'|'x86_64'|'aarch64'|'openwrt',
              UpdateTargetsOperatingSystem='ubuntu'|'raspbian'|'amazon_linux'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type S3UrlSignerRole: string
        :param S3UrlSignerRole: **[REQUIRED]** The IAM Role that Greengrass will use to create pre-signed
        URLs pointing towards the update artifact.

        :type SoftwareToUpdate: string
        :param SoftwareToUpdate: **[REQUIRED]** The piece of software on the Greengrass core that will be
        updated.

        :type UpdateAgentLogLevel: string
        :param UpdateAgentLogLevel: The minimum level of log statements that should be logged by the OTA
        Agent during an update.

        :type UpdateTargets: list
        :param UpdateTargets: **[REQUIRED]** The ARNs of the targets (IoT things or IoT thing groups) that
        this update will be applied to.

          - *(string) --*

        :type UpdateTargetsArchitecture: string
        :param UpdateTargetsArchitecture: **[REQUIRED]** The architecture of the cores which are the
        targets of an update.

        :type UpdateTargetsOperatingSystem: string
        :param UpdateTargetsOperatingSystem: **[REQUIRED]** The operating system of the cores which are the
        targets of an update.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IotJobArn': 'string',
                'IotJobId': 'string',
                'PlatformSoftwareVersion': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **IotJobArn** *(string) --* The IoT Job ARN corresponding to this update.

            - **IotJobId** *(string) --* The IoT Job Id corresponding to this update.

            - **PlatformSoftwareVersion** *(string) --* The software version installed on the device or
            devices after the update.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subscription_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateSubscriptionDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateSubscriptionDefinitionResponseTypeDef:
        """
        Creates a subscription definition. You may provide the initial version of the subscription
        definition now or use ''CreateSubscriptionDefinitionVersion'' at a later time.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSubscriptionDefinition>`_

        **Request Syntax**
        ::

          response = client.create_subscription_definition(
              AmznClientToken='string',
              InitialVersion={
                  'Subscriptions': [
                      {
                          'Id': 'string',
                          'Source': 'string',
                          'Subject': 'string',
                          'Target': 'string'
                      },
                  ]
              },
              Name='string',
              tags={
                  'string': 'string'
              }
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the subscription definition.

          - **Subscriptions** *(list) --* A list of subscriptions.

            - *(dict) --* Information about a subscription.

              - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the subscription.
              This value must be unique within the subscription definition version. Max length is 128
              characters with pattern ''[a-zA-Z0-9:_-]+''.

              - **Source** *(string) --* **[REQUIRED]** The source of the subscription. Can be a thing ARN,
              a Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
              'GGShadowService'.

              - **Subject** *(string) --* **[REQUIRED]** The MQTT topic used to route the message.

              - **Target** *(string) --* **[REQUIRED]** Where the message is sent to. Can be a thing ARN, a
              Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
              'GGShadowService'.

        :type Name: string
        :param Name: The name of the subscription definition.

        :type tags: dict
        :param tags: Tag(s) to add to the new resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        AmznClientToken: str = None,
        Subscriptions: List[
            ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef
        ] = None,
    ) -> ClientCreateSubscriptionDefinitionVersionResponseTypeDef:
        """
        Creates a version of a subscription definition which has already been defined.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSubscriptionDefinitionVersion>`_
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSubscriptionDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.create_subscription_definition_version(
              AmznClientToken='string',
              SubscriptionDefinitionId='string',
              Subscriptions=[
                  {
                      'Id': 'string',
                      'Source': 'string',
                      'Subject': 'string',
                      'Target': 'string'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.

        :type Subscriptions: list
        :param Subscriptions: A list of subscriptions.

          - *(dict) --* Information about a subscription.

            - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the subscription. This
            value must be unique within the subscription definition version. Max length is 128 characters
            with pattern ''[a-zA-Z0-9:_-]+''.

            - **Source** *(string) --* **[REQUIRED]** The source of the subscription. Can be a thing ARN, a
            Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
            'GGShadowService'.

            - **Subject** *(string) --* **[REQUIRED]** The MQTT topic used to route the message.

            - **Target** *(string) --* **[REQUIRED]** Where the message is sent to. Can be a thing ARN, a
            Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
            'GGShadowService'.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            version was created.

            - **Id** *(string) --* The ID of the version.

            - **Version** *(string) --* The unique ID of the version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_connector_definition(self, ConnectorDefinitionId: str) -> Dict[str, Any]:
        """
        Deletes a connector definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteConnectorDefinition>`_

        **Request Syntax**
        ::

          response = client.delete_connector_definition(
              ConnectorDefinitionId='string'
          )
        :type ConnectorDefinitionId: string
        :param ConnectorDefinitionId: **[REQUIRED]** The ID of the connector definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_core_definition(self, CoreDefinitionId: str) -> Dict[str, Any]:
        """
        Deletes a core definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteCoreDefinition>`_

        **Request Syntax**
        ::

          response = client.delete_core_definition(
              CoreDefinitionId='string'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_device_definition(self, DeviceDefinitionId: str) -> Dict[str, Any]:
        """
        Deletes a device definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteDeviceDefinition>`_

        **Request Syntax**
        ::

          response = client.delete_device_definition(
              DeviceDefinitionId='string'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function_definition(self, FunctionDefinitionId: str) -> Dict[str, Any]:
        """
        Deletes a Lambda function definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteFunctionDefinition>`_

        **Request Syntax**
        ::

          response = client.delete_function_definition(
              FunctionDefinitionId='string'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group(self, GroupId: str) -> Dict[str, Any]:
        """
        Deletes a group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteGroup>`_

        **Request Syntax**
        ::

          response = client.delete_group(
              GroupId='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_logger_definition(self, LoggerDefinitionId: str) -> Dict[str, Any]:
        """
        Deletes a logger definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteLoggerDefinition>`_

        **Request Syntax**
        ::

          response = client.delete_logger_definition(
              LoggerDefinitionId='string'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_definition(self, ResourceDefinitionId: str) -> Dict[str, Any]:
        """
        Deletes a resource definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteResourceDefinition>`_

        **Request Syntax**
        ::

          response = client.delete_resource_definition(
              ResourceDefinitionId='string'
          )
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_subscription_definition(
        self, SubscriptionDefinitionId: str
    ) -> Dict[str, Any]:
        """
        Deletes a subscription definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteSubscriptionDefinition>`_

        **Request Syntax**
        ::

          response = client.delete_subscription_definition(
              SubscriptionDefinitionId='string'
          )
        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_role_from_group(
        self, GroupId: str
    ) -> ClientDisassociateRoleFromGroupResponseTypeDef:
        """
        Disassociates the role from a group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DisassociateRoleFromGroup>`_

        **Request Syntax**
        ::

          response = client.disassociate_role_from_group(
              GroupId='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DisassociatedAt': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **DisassociatedAt** *(string) --* The time, in milliseconds since the epoch, when the role
            was disassociated from the group.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_service_role_from_account(
        self, *args: Any, **kwargs: Any
    ) -> ClientDisassociateServiceRoleFromAccountResponseTypeDef:
        """
        Disassociates the service role from your account. Without a service role, deployments will not work.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DisassociateServiceRoleFromAccount>`_

        **Request Syntax**
        ::

          response = client.disassociate_service_role_from_account()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DisassociatedAt': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **DisassociatedAt** *(string) --* The time when the service role was disassociated from the
            account.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
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
    def get_associated_role(
        self, GroupId: str
    ) -> ClientGetAssociatedRoleResponseTypeDef:
        """
        Retrieves the role associated with a particular group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetAssociatedRole>`_

        **Request Syntax**
        ::

          response = client.get_associated_role(
              GroupId='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AssociatedAt': 'string',
                'RoleArn': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **AssociatedAt** *(string) --* The time when the role was associated with the group.

            - **RoleArn** *(string) --* The ARN of the role that is associated with the group.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bulk_deployment_status(
        self, BulkDeploymentId: str
    ) -> ClientGetBulkDeploymentStatusResponseTypeDef:
        """
        Returns the status of a bulk deployment.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetBulkDeploymentStatus>`_

        **Request Syntax**
        ::

          response = client.get_bulk_deployment_status(
              BulkDeploymentId='string'
          )
        :type BulkDeploymentId: string
        :param BulkDeploymentId: **[REQUIRED]** The ID of the bulk deployment.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'BulkDeploymentMetrics': {
                    'InvalidInputRecords': 123,
                    'RecordsProcessed': 123,
                    'RetryAttempts': 123
                },
                'BulkDeploymentStatus': 'Initializing'|'Running'|'Completed'|'Stopping'|'Stopped'|'Failed',
                'CreatedAt': 'string',
                'ErrorDetails': [
                    {
                        'DetailedErrorCode': 'string',
                        'DetailedErrorMessage': 'string'
                    },
                ],
                'ErrorMessage': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the status of the bulk deployment.

            - **BulkDeploymentMetrics** *(dict) --* Relevant metrics on input records processed during bulk
            deployment.

              - **InvalidInputRecords** *(integer) --* The total number of records that returned a
              non-retryable error. For example, this can occur if a group record from the input file uses
              an invalid format or specifies a nonexistent group version, or if the execution role doesn't
              grant permission to deploy a group or group version.

              - **RecordsProcessed** *(integer) --* The total number of group records from the input file
              that have been processed so far, or attempted.

              - **RetryAttempts** *(integer) --* The total number of deployment attempts that returned a
              retryable error. For example, a retry is triggered if the attempt to deploy a group returns a
              throttling error. ''StartBulkDeployment'' retries a group deployment up to five times.

            - **BulkDeploymentStatus** *(string) --* The status of the bulk deployment.

            - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.

            - **ErrorDetails** *(list) --* Error details

              - *(dict) --* Details about the error.

                - **DetailedErrorCode** *(string) --* A detailed error code.

                - **DetailedErrorMessage** *(string) --* A detailed error message.

            - **ErrorMessage** *(string) --* Error message

            - **tags** *(dict) --* Tag(s) attached to the resource arn.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connectivity_info(
        self, ThingName: str
    ) -> ClientGetConnectivityInfoResponseTypeDef:
        """
        Retrieves the connectivity information for a core.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetConnectivityInfo>`_

        **Request Syntax**
        ::

          response = client.get_connectivity_info(
              ThingName='string'
          )
        :type ThingName: string
        :param ThingName: **[REQUIRED]** The thing name.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ConnectivityInfo': [
                    {
                        'HostAddress': 'string',
                        'Id': 'string',
                        'Metadata': 'string',
                        'PortNumber': 123
                    },
                ],
                'Message': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **ConnectivityInfo** *(list) --* Connectivity info list.

              - *(dict) --* Information about a Greengrass core's connectivity.

                - **HostAddress** *(string) --* The endpoint for the Greengrass core. Can be an IP address
                or DNS.

                - **Id** *(string) --* The ID of the connectivity information.

                - **Metadata** *(string) --* Metadata for this endpoint.

                - **PortNumber** *(integer) --* The port of the Greengrass core. Usually 8883.

            - **Message** *(string) --* A message about the connectivity info request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connector_definition(
        self, ConnectorDefinitionId: str
    ) -> ClientGetConnectorDefinitionResponseTypeDef:
        """
        Retrieves information about a connector definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetConnectorDefinition>`_

        **Request Syntax**
        ::

          response = client.get_connector_definition(
              ConnectorDefinitionId='string'
          )
        :type ConnectorDefinitionId: string
        :param ConnectorDefinitionId: **[REQUIRED]** The ID of the connector definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.

            - **tags** *(dict) --* Tag(s) attached to the resource arn.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connector_definition_version(
        self,
        ConnectorDefinitionId: str,
        ConnectorDefinitionVersionId: str,
        NextToken: str = None,
    ) -> ClientGetConnectorDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a connector definition version, including the connectors that the
        version contains. Connectors are prebuilt modules that interact with local infrastructure, device
        protocols, AWS, and other cloud services.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetConnectorDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.get_connector_definition_version(
              ConnectorDefinitionId='string',
              ConnectorDefinitionVersionId='string',
              NextToken='string'
          )
        :type ConnectorDefinitionId: string
        :param ConnectorDefinitionId: **[REQUIRED]** The ID of the connector definition.

        :type ConnectorDefinitionVersionId: string
        :param ConnectorDefinitionVersionId: **[REQUIRED]** The ID of the connector definition version.
        This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object,
        which is returned by ''ListConnectorDefinitionVersions'' requests. If the version is the last one
        that was associated with a connector definition, the value also maps to the ''LatestVersion''
        property of the corresponding ''DefinitionInformation'' object.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Definition': {
                    'Connectors': [
                        {
                            'ConnectorArn': 'string',
                            'Id': 'string',
                            'Parameters': {
                                'string': 'string'
                            }
                        },
                    ]
                },
                'Id': 'string',
                'NextToken': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the connector definition version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            connector definition version was created.

            - **Definition** *(dict) --* Information about the connector definition version.

              - **Connectors** *(list) --* A list of references to connectors in this version, with their
              corresponding configuration settings.

                - *(dict) --* Information about a connector. Connectors run on the Greengrass core and
                contain built-in integration with local infrastructure, device protocols, AWS, and other
                cloud services.

                  - **ConnectorArn** *(string) --* The ARN of the connector.

                  - **Id** *(string) --* A descriptive or arbitrary ID for the connector. This value must
                  be unique within the connector definition version. Max length is 128 characters with
                  pattern [a-zA-Z0-9:_-]+.

                  - **Parameters** *(dict) --* The parameters or configuration that the connector uses.

                    - *(string) --*

                      - *(string) --*

            - **Id** *(string) --* The ID of the connector definition version.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Version** *(string) --* The version of the connector definition version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_core_definition(
        self, CoreDefinitionId: str
    ) -> ClientGetCoreDefinitionResponseTypeDef:
        """
        Retrieves information about a core definition version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetCoreDefinition>`_

        **Request Syntax**
        ::

          response = client.get_core_definition(
              CoreDefinitionId='string'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.

            - **tags** *(dict) --* Tag(s) attached to the resource arn.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_core_definition_version(
        self, CoreDefinitionId: str, CoreDefinitionVersionId: str
    ) -> ClientGetCoreDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a core definition version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetCoreDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.get_core_definition_version(
              CoreDefinitionId='string',
              CoreDefinitionVersionId='string'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.

        :type CoreDefinitionVersionId: string
        :param CoreDefinitionVersionId: **[REQUIRED]** The ID of the core definition version. This value
        maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is
        returned by ''ListCoreDefinitionVersions'' requests. If the version is the last one that was
        associated with a core definition, the value also maps to the ''LatestVersion'' property of the
        corresponding ''DefinitionInformation'' object.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Definition': {
                    'Cores': [
                        {
                            'CertificateArn': 'string',
                            'Id': 'string',
                            'SyncShadow': True|False,
                            'ThingArn': 'string'
                        },
                    ]
                },
                'Id': 'string',
                'NextToken': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **Arn** *(string) --* The ARN of the core definition version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the core
            definition version was created.

            - **Definition** *(dict) --* Information about the core definition version.

              - **Cores** *(list) --* A list of cores in the core definition version.

                - *(dict) --* Information about a core.

                  - **CertificateArn** *(string) --* The ARN of the certificate associated with the core.

                  - **Id** *(string) --* A descriptive or arbitrary ID for the core. This value must be
                  unique within the core definition version. Max length is 128 characters with pattern
                  ''[a-zA-Z0-9:_-]+''.

                  - **SyncShadow** *(boolean) --* If true, the core's local shadow is automatically synced
                  with the cloud.

                  - **ThingArn** *(string) --* The ARN of the thing which is the core.

            - **Id** *(string) --* The ID of the core definition version.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Version** *(string) --* The version of the core definition version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment_status(
        self, DeploymentId: str, GroupId: str
    ) -> ClientGetDeploymentStatusResponseTypeDef:
        """
        Returns the status of a deployment.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetDeploymentStatus>`_

        **Request Syntax**
        ::

          response = client.get_deployment_status(
              DeploymentId='string',
              GroupId='string'
          )
        :type DeploymentId: string
        :param DeploymentId: **[REQUIRED]** The ID of the deployment.

        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DeploymentStatus': 'string',
                'DeploymentType': 'NewDeployment'|'Redeployment'|'ResetDeployment'|'ForceResetDeployment',
                'ErrorDetails': [
                    {
                        'DetailedErrorCode': 'string',
                        'DetailedErrorMessage': 'string'
                    },
                ],
                'ErrorMessage': 'string',
                'UpdatedAt': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the status of the deployment for the group.

            - **DeploymentStatus** *(string) --* The status of the deployment: ''InProgress'',
            ''Building'', ''Success'', or ''Failure''.

            - **DeploymentType** *(string) --* The type of the deployment.

            - **ErrorDetails** *(list) --* Error details

              - *(dict) --* Details about the error.

                - **DetailedErrorCode** *(string) --* A detailed error code.

                - **DetailedErrorMessage** *(string) --* A detailed error message.

            - **ErrorMessage** *(string) --* Error message

            - **UpdatedAt** *(string) --* The time, in milliseconds since the epoch, when the deployment
            status was updated.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_definition(
        self, DeviceDefinitionId: str
    ) -> ClientGetDeviceDefinitionResponseTypeDef:
        """
        Retrieves information about a device definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetDeviceDefinition>`_

        **Request Syntax**
        ::

          response = client.get_device_definition(
              DeviceDefinitionId='string'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.

            - **tags** *(dict) --* Tag(s) attached to the resource arn.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_definition_version(
        self,
        DeviceDefinitionId: str,
        DeviceDefinitionVersionId: str,
        NextToken: str = None,
    ) -> ClientGetDeviceDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a device definition version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetDeviceDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.get_device_definition_version(
              DeviceDefinitionId='string',
              DeviceDefinitionVersionId='string',
              NextToken='string'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.

        :type DeviceDefinitionVersionId: string
        :param DeviceDefinitionVersionId: **[REQUIRED]** The ID of the device definition version. This
        value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is
        returned by ''ListDeviceDefinitionVersions'' requests. If the version is the last one that was
        associated with a device definition, the value also maps to the ''LatestVersion'' property of the
        corresponding ''DefinitionInformation'' object.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Definition': {
                    'Devices': [
                        {
                            'CertificateArn': 'string',
                            'Id': 'string',
                            'SyncShadow': True|False,
                            'ThingArn': 'string'
                        },
                    ]
                },
                'Id': 'string',
                'NextToken': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the device definition version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            device definition version was created.

            - **Definition** *(dict) --* Information about the device definition version.

              - **Devices** *(list) --* A list of devices in the definition version.

                - *(dict) --* Information about a device.

                  - **CertificateArn** *(string) --* The ARN of the certificate associated with the device.

                  - **Id** *(string) --* A descriptive or arbitrary ID for the device. This value must be
                  unique within the device definition version. Max length is 128 characters with pattern
                  ''[a-zA-Z0-9:_-]+''.

                  - **SyncShadow** *(boolean) --* If true, the device's local shadow will be automatically
                  synced with the cloud.

                  - **ThingArn** *(string) --* The thing ARN of the device.

            - **Id** *(string) --* The ID of the device definition version.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Version** *(string) --* The version of the device definition version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_definition(
        self, FunctionDefinitionId: str
    ) -> ClientGetFunctionDefinitionResponseTypeDef:
        """
        Retrieves information about a Lambda function definition, including its creation time and latest
        version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetFunctionDefinition>`_

        **Request Syntax**
        ::

          response = client.get_function_definition(
              FunctionDefinitionId='string'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --* success

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.

            - **tags** *(dict) --* Tag(s) attached to the resource arn.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_definition_version(
        self,
        FunctionDefinitionId: str,
        FunctionDefinitionVersionId: str,
        NextToken: str = None,
    ) -> ClientGetFunctionDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a Lambda function definition version, including which Lambda functions
        are included in the version and their configurations.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetFunctionDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.get_function_definition_version(
              FunctionDefinitionId='string',
              FunctionDefinitionVersionId='string',
              NextToken='string'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.

        :type FunctionDefinitionVersionId: string
        :param FunctionDefinitionVersionId: **[REQUIRED]** The ID of the function definition version. This
        value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is
        returned by ''ListFunctionDefinitionVersions'' requests. If the version is the last one that was
        associated with a function definition, the value also maps to the ''LatestVersion'' property of the
        corresponding ''DefinitionInformation'' object.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Definition': {
                    'DefaultConfig': {
                        'Execution': {
                            'IsolationMode': 'GreengrassContainer'|'NoContainer',
                            'RunAs': {
                                'Gid': 123,
                                'Uid': 123
                            }
                        }
                    },
                    'Functions': [
                        {
                            'FunctionArn': 'string',
                            'FunctionConfiguration': {
                                'EncodingType': 'binary'|'json',
                                'Environment': {
                                    'AccessSysfs': True|False,
                                    'Execution': {
                                        'IsolationMode': 'GreengrassContainer'|'NoContainer',
                                        'RunAs': {
                                            'Gid': 123,
                                            'Uid': 123
                                        }
                                    },
                                    'ResourceAccessPolicies': [
                                        {
                                            'Permission': 'ro'|'rw',
                                            'ResourceId': 'string'
                                        },
                                    ],
                                    'Variables': {
                                        'string': 'string'
                                    }
                                },
                                'ExecArgs': 'string',
                                'Executable': 'string',
                                'MemorySize': 123,
                                'Pinned': True|False,
                                'Timeout': 123
                            },
                            'Id': 'string'
                        },
                    ]
                },
                'Id': 'string',
                'NextToken': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **Arn** *(string) --* The ARN of the function definition version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            function definition version was created.

            - **Definition** *(dict) --* Information on the definition.

              - **DefaultConfig** *(dict) --* The default configuration that applies to all Lambda
              functions in this function definition version. Individual Lambda functions can override these
              settings.

                - **Execution** *(dict) --* Configuration information that specifies how a Lambda function
                runs.

                  - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
                  Greengrass container (default) or without containerization. Unless your scenario requires
                  that you run without containerization, we recommend that you run in a Greengrass
                  container. Omit this value to run the Lambda function with the default containerization
                  for the group.

                  - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
                  running the Lambda function. You can specify one or both values to override the default
                  values. We recommend that you avoid running as root unless absolutely necessary to
                  minimize the risk of unintended changes or malicious attacks. To run as root, you must
                  set ''IsolationMode'' to ''NoContainer'' and update config.json in
                  ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

                    - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
                    function.

                    - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
                    function.

              - **Functions** *(list) --* A list of Lambda functions in this function definition version.

                - *(dict) --* Information about a Lambda function.

                  - **FunctionArn** *(string) --* The ARN of the Lambda function.

                  - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.

                    - **EncodingType** *(string) --* The expected encoding type of the input payload for
                    the function. The default is ''json''.

                    - **Environment** *(dict) --* The environment configuration of the function.

                      - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access
                      the host's /sys folder. Use this when the Lambda function needs to read device
                      information from /sys. This setting applies only when you run the Lambda function in
                      a Greengrass container.

                      - **Execution** *(dict) --* Configuration related to executing the Lambda function

                        - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
                        Greengrass container (default) or without containerization. Unless your scenario
                        requires that you run without containerization, we recommend that you run in a
                        Greengrass container. Omit this value to run the Lambda function with the default
                        containerization for the group.

                        - **RunAs** *(dict) --* Specifies the user and group whose permissions are used
                        when running the Lambda function. You can specify one or both values to override
                        the default values. We recommend that you avoid running as root unless absolutely
                        necessary to minimize the risk of unintended changes or malicious attacks. To run
                        as root, you must set ''IsolationMode'' to ''NoContainer'' and update config.json
                        in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

                          - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
                          function.

                          - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
                          function.

                      - **ResourceAccessPolicies** *(list) --* A list of the resources, with their
                      permissions, to which the Lambda function will be granted access. A Lambda function
                      can have at most 10 resources. ResourceAccessPolicies apply only when you run the
                      Lambda function in a Greengrass container.

                        - *(dict) --* A policy used by the function to access a resource.

                          - **Permission** *(string) --* The permissions that the Lambda function has to
                          the resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

                          - **ResourceId** *(string) --* The ID of the resource. (This ID is assigned to
                          the resource when you create the resource definiton.)

                      - **Variables** *(dict) --* Environment variables for the Lambda function's
                      configuration.

                        - *(string) --*

                          - *(string) --*

                    - **ExecArgs** *(string) --* The execution arguments.

                    - **Executable** *(string) --* The name of the function executable.

                    - **MemorySize** *(integer) --* The memory size, in KB, which the function requires.
                    This setting is not applicable and should be cleared when you run the Lambda function
                    without containerization.

                    - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function
                    is long-lived and starts when the core starts.

                    - **Timeout** *(integer) --* The allowed function execution time, after which Lambda
                    should terminate the function. This timeout still applies to pinned Lambda functions
                    for each request.

                  - **Id** *(string) --* A descriptive or arbitrary ID for the function. This value must be
                  unique within the function definition version. Max length is 128 characters with pattern
                  ''[a-zA-Z0-9:_-]+''.

            - **Id** *(string) --* The ID of the function definition version.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Version** *(string) --* The version of the function definition version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group(self, GroupId: str) -> ClientGetGroupResponseTypeDef:
        """
        Retrieves information about a group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroup>`_

        **Request Syntax**
        ::

          response = client.get_group(
              GroupId='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --* success

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.

            - **tags** *(dict) --* Tag(s) attached to the resource arn.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_certificate_authority(
        self, CertificateAuthorityId: str, GroupId: str
    ) -> ClientGetGroupCertificateAuthorityResponseTypeDef:
        """
        Retreives the CA associated with a group. Returns the public key of the CA.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroupCertificateAuthority>`_

        **Request Syntax**
        ::

          response = client.get_group_certificate_authority(
              CertificateAuthorityId='string',
              GroupId='string'
          )
        :type CertificateAuthorityId: string
        :param CertificateAuthorityId: **[REQUIRED]** The ID of the certificate authority.

        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GroupCertificateAuthorityArn': 'string',
                'GroupCertificateAuthorityId': 'string',
                'PemEncodedCertificate': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the PKI Configuration.

            - **GroupCertificateAuthorityArn** *(string) --* The ARN of the certificate authority for the
            group.

            - **GroupCertificateAuthorityId** *(string) --* The ID of the certificate authority for the
            group.

            - **PemEncodedCertificate** *(string) --* The PEM encoded certificate for the group.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_certificate_configuration(
        self, GroupId: str
    ) -> ClientGetGroupCertificateConfigurationResponseTypeDef:
        """
        Retrieves the current configuration for the CA used by the group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroupCertificateConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_group_certificate_configuration(
              GroupId='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CertificateAuthorityExpiryInMilliseconds': 'string',
                'CertificateExpiryInMilliseconds': 'string',
                'GroupId': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the PKI Configuration.

            - **CertificateAuthorityExpiryInMilliseconds** *(string) --* The amount of time remaining
            before the certificate authority expires, in milliseconds.

            - **CertificateExpiryInMilliseconds** *(string) --* The amount of time remaining before the
            certificate expires, in milliseconds.

            - **GroupId** *(string) --* The ID of the group certificate configuration.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_version(
        self, GroupId: str, GroupVersionId: str
    ) -> ClientGetGroupVersionResponseTypeDef:
        """
        Retrieves information about a group version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroupVersion>`_

        **Request Syntax**
        ::

          response = client.get_group_version(
              GroupId='string',
              GroupVersionId='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :type GroupVersionId: string
        :param GroupVersionId: **[REQUIRED]** The ID of the group version. This value maps to the
        ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by
        ''ListGroupVersions'' requests. If the version is the last one that was associated with a group,
        the value also maps to the ''LatestVersion'' property of the corresponding ''GroupInformation''
        object.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Definition': {
                    'ConnectorDefinitionVersionArn': 'string',
                    'CoreDefinitionVersionArn': 'string',
                    'DeviceDefinitionVersionArn': 'string',
                    'FunctionDefinitionVersionArn': 'string',
                    'LoggerDefinitionVersionArn': 'string',
                    'ResourceDefinitionVersionArn': 'string',
                    'SubscriptionDefinitionVersionArn': 'string'
                },
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **Arn** *(string) --* The ARN of the group version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the group
            version was created.

            - **Definition** *(dict) --* Information about the group version definition.

              - **ConnectorDefinitionVersionArn** *(string) --* The ARN of the connector definition version
              for this group.

              - **CoreDefinitionVersionArn** *(string) --* The ARN of the core definition version for this
              group.

              - **DeviceDefinitionVersionArn** *(string) --* The ARN of the device definition version for
              this group.

              - **FunctionDefinitionVersionArn** *(string) --* The ARN of the function definition version
              for this group.

              - **LoggerDefinitionVersionArn** *(string) --* The ARN of the logger definition version for
              this group.

              - **ResourceDefinitionVersionArn** *(string) --* The ARN of the resource definition version
              for this group.

              - **SubscriptionDefinitionVersionArn** *(string) --* The ARN of the subscription definition
              version for this group.

            - **Id** *(string) --* The ID of the group that the version is associated with.

            - **Version** *(string) --* The ID of the group version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_logger_definition(
        self, LoggerDefinitionId: str
    ) -> ClientGetLoggerDefinitionResponseTypeDef:
        """
        Retrieves information about a logger definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetLoggerDefinition>`_

        **Request Syntax**
        ::

          response = client.get_logger_definition(
              LoggerDefinitionId='string'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.

            - **tags** *(dict) --* Tag(s) attached to the resource arn.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_logger_definition_version(
        self,
        LoggerDefinitionId: str,
        LoggerDefinitionVersionId: str,
        NextToken: str = None,
    ) -> ClientGetLoggerDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a logger definition version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetLoggerDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.get_logger_definition_version(
              LoggerDefinitionId='string',
              LoggerDefinitionVersionId='string',
              NextToken='string'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.

        :type LoggerDefinitionVersionId: string
        :param LoggerDefinitionVersionId: **[REQUIRED]** The ID of the logger definition version. This
        value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is
        returned by ''ListLoggerDefinitionVersions'' requests. If the version is the last one that was
        associated with a logger definition, the value also maps to the ''LatestVersion'' property of the
        corresponding ''DefinitionInformation'' object.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Definition': {
                    'Loggers': [
                        {
                            'Component': 'GreengrassSystem'|'Lambda',
                            'Id': 'string',
                            'Level': 'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
                            'Space': 123,
                            'Type': 'FileSystem'|'AWSCloudWatch'
                        },
                    ]
                },
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **Arn** *(string) --* The ARN of the logger definition version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            logger definition version was created.

            - **Definition** *(dict) --* Information about the logger definition version.

              - **Loggers** *(list) --* A list of loggers.

                - *(dict) --* Information about a logger

                  - **Component** *(string) --* The component that will be subject to logging.

                  - **Id** *(string) --* A descriptive or arbitrary ID for the logger. This value must be
                  unique within the logger definition version. Max length is 128 characters with pattern
                  ''[a-zA-Z0-9:_-]+''.

                  - **Level** *(string) --* The level of the logs.

                  - **Space** *(integer) --* The amount of file space, in KB, to use if the local file
                  system is used for logging purposes.

                  - **Type** *(string) --* The type of log output which will be used.

            - **Id** *(string) --* The ID of the logger definition version.

            - **Version** *(string) --* The version of the logger definition version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_definition(
        self, ResourceDefinitionId: str
    ) -> ClientGetResourceDefinitionResponseTypeDef:
        """
        Retrieves information about a resource definition, including its creation time and latest version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetResourceDefinition>`_

        **Request Syntax**
        ::

          response = client.get_resource_definition(
              ResourceDefinitionId='string'
          )
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --* success

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.

            - **tags** *(dict) --* Tag(s) attached to the resource arn.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_definition_version(
        self, ResourceDefinitionId: str, ResourceDefinitionVersionId: str
    ) -> ClientGetResourceDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a resource definition version, including which resources are included
        in the version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetResourceDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.get_resource_definition_version(
              ResourceDefinitionId='string',
              ResourceDefinitionVersionId='string'
          )
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.

        :type ResourceDefinitionVersionId: string
        :param ResourceDefinitionVersionId: **[REQUIRED]** The ID of the resource definition version. This
        value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is
        returned by ''ListResourceDefinitionVersions'' requests. If the version is the last one that was
        associated with a resource definition, the value also maps to the ''LatestVersion'' property of the
        corresponding ''DefinitionInformation'' object.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Definition': {
                    'Resources': [
                        {
                            'Id': 'string',
                            'Name': 'string',
                            'ResourceDataContainer': {
                                'LocalDeviceResourceData': {
                                    'GroupOwnerSetting': {
                                        'AutoAddGroupOwner': True|False,
                                        'GroupOwner': 'string'
                                    },
                                    'SourcePath': 'string'
                                },
                                'LocalVolumeResourceData': {
                                    'DestinationPath': 'string',
                                    'GroupOwnerSetting': {
                                        'AutoAddGroupOwner': True|False,
                                        'GroupOwner': 'string'
                                    },
                                    'SourcePath': 'string'
                                },
                                'S3MachineLearningModelResourceData': {
                                    'DestinationPath': 'string',
                                    'S3Uri': 'string'
                                },
                                'SageMakerMachineLearningModelResourceData': {
                                    'DestinationPath': 'string',
                                    'SageMakerJobArn': 'string'
                                },
                                'SecretsManagerSecretResourceData': {
                                    'ARN': 'string',
                                    'AdditionalStagingLabelsToDownload': [
                                        'string',
                                    ]
                                }
                            }
                        },
                    ]
                },
                'Id': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **Arn** *(string) --* Arn of the resource definition version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            resource definition version was created.

            - **Definition** *(dict) --* Information about the definition.

              - **Resources** *(list) --* A list of resources.

                - *(dict) --* Information about a resource.

                  - **Id** *(string) --* The resource ID, used to refer to a resource in the Lambda
                  function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
                  This must be unique within a Greengrass group.

                  - **Name** *(string) --* The descriptive resource name, which is displayed on the AWS IoT
                  Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must
                  be unique within a Greengrass group.

                  - **ResourceDataContainer** *(dict) --* A container of data for all resource types.

                    - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device
                    resource.

                      - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

                        - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
                        adds the specified Linux OS group owner of the resource to the Lambda process
                        privileges. Thus the Lambda process will have the file access permissions of the
                        added Linux group.

                        - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
                        be added to the Lambda process. This field is optional.

                      - **SourcePath** *(string) --* The local absolute path of the device resource. The
                      source path for a device resource can refer only to a character device or block
                      device under ''/dev''.

                    - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume
                    resource.

                      - **DestinationPath** *(string) --* The absolute local path of the resource inside
                      the Lambda environment.

                      - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group
                      privileges for the Lambda process. This field is optional.

                        - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
                        adds the specified Linux OS group owner of the resource to the Lambda process
                        privileges. Thus the Lambda process will have the file access permissions of the
                        added Linux group.

                        - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
                        be added to the Lambda process. This field is optional.

                      - **SourcePath** *(string) --* The local absolute path of the volume resource on the
                      host. The source path for a volume resource type cannot start with ''/sys''.

                    - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon
                    S3 machine learning resource.

                      - **DestinationPath** *(string) --* The absolute local path of the resource inside
                      the Lambda environment.

                      - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model
                      package must be in tar.gz or .zip format.

                    - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an
                    Amazon SageMaker machine learning resource.

                      - **DestinationPath** *(string) --* The absolute local path of the resource inside
                      the Lambda environment.

                      - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
                      represents the source model.

                    - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret
                    resource, which references a secret from AWS Secrets Manager.

                      - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on
                      the core. The value of the secret's latest version (represented by the ''AWSCURRENT''
                      staging label) is included by default.

                      - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels
                      whose values you want to make available on the core, in addition to ''AWSCURRENT''.

                        - *(string) --*

            - **Id** *(string) --* The ID of the resource definition version.

            - **Version** *(string) --* The version of the resource definition version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_role_for_account(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetServiceRoleForAccountResponseTypeDef:
        """
        Retrieves the service role that is attached to your account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetServiceRoleForAccount>`_

        **Request Syntax**
        ::

          response = client.get_service_role_for_account()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AssociatedAt': 'string',
                'RoleArn': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **AssociatedAt** *(string) --* The time when the service role was associated with the account.

            - **RoleArn** *(string) --* The ARN of the role which is associated with the account.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_subscription_definition(
        self, SubscriptionDefinitionId: str
    ) -> ClientGetSubscriptionDefinitionResponseTypeDef:
        """
        Retrieves information about a subscription definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetSubscriptionDefinition>`_

        **Request Syntax**
        ::

          response = client.get_subscription_definition(
              SubscriptionDefinitionId='string'
          )
        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Id': 'string',
                'LastUpdatedTimestamp': 'string',
                'LatestVersion': 'string',
                'LatestVersionArn': 'string',
                'Name': 'string',
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the definition.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was created.

            - **Id** *(string) --* The ID of the definition.

            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            definition was last updated.

            - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

            - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
            definition.

            - **Name** *(string) --* The name of the definition.

            - **tags** *(dict) --* Tag(s) attached to the resource arn.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        SubscriptionDefinitionVersionId: str,
        NextToken: str = None,
    ) -> ClientGetSubscriptionDefinitionVersionResponseTypeDef:
        """
        Retrieves information about a subscription definition version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetSubscriptionDefinitionVersion>`_

        **Request Syntax**
        ::

          response = client.get_subscription_definition_version(
              NextToken='string',
              SubscriptionDefinitionId='string',
              SubscriptionDefinitionVersionId='string'
          )
        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.

        :type SubscriptionDefinitionVersionId: string
        :param SubscriptionDefinitionVersionId: **[REQUIRED]** The ID of the subscription definition
        version. This value maps to the ''Version'' property of the corresponding ''VersionInformation''
        object, which is returned by ''ListSubscriptionDefinitionVersions'' requests. If the version is the
        last one that was associated with a subscription definition, the value also maps to the
        ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Arn': 'string',
                'CreationTimestamp': 'string',
                'Definition': {
                    'Subscriptions': [
                        {
                            'Id': 'string',
                            'Source': 'string',
                            'Subject': 'string',
                            'Target': 'string'
                        },
                    ]
                },
                'Id': 'string',
                'NextToken': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Arn** *(string) --* The ARN of the subscription definition version.

            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
            subscription definition version was created.

            - **Definition** *(dict) --* Information about the subscription definition version.

              - **Subscriptions** *(list) --* A list of subscriptions.

                - *(dict) --* Information about a subscription.

                  - **Id** *(string) --* A descriptive or arbitrary ID for the subscription. This value
                  must be unique within the subscription definition version. Max length is 128 characters
                  with pattern ''[a-zA-Z0-9:_-]+''.

                  - **Source** *(string) --* The source of the subscription. Can be a thing ARN, a Lambda
                  function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
                  'GGShadowService'.

                  - **Subject** *(string) --* The MQTT topic used to route the message.

                  - **Target** *(string) --* Where the message is sent to. Can be a thing ARN, a Lambda
                  function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
                  'GGShadowService'.

            - **Id** *(string) --* The ID of the subscription definition version.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Version** *(string) --* The version of the subscription definition version.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bulk_deployment_detailed_reports(
        self, BulkDeploymentId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListBulkDeploymentDetailedReportsResponseTypeDef:
        """
        Gets a paginated list of the deployments that have been started in a bulk deployment operation, and
        their current deployment status.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListBulkDeploymentDetailedReports>`_

        **Request Syntax**
        ::

          response = client.list_bulk_deployment_detailed_reports(
              BulkDeploymentId='string',
              MaxResults='string',
              NextToken='string'
          )
        :type BulkDeploymentId: string
        :param BulkDeploymentId: **[REQUIRED]** The ID of the bulk deployment.

        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Deployments': [
                    {
                        'CreatedAt': 'string',
                        'DeploymentArn': 'string',
                        'DeploymentId': 'string',
                        'DeploymentStatus': 'string',
                        'DeploymentType':
                        'NewDeployment'|'Redeployment'|'ResetDeployment'|'ForceResetDeployment',
                        'ErrorDetails': [
                            {
                                'DetailedErrorCode': 'string',
                                'DetailedErrorMessage': 'string'
                            },
                        ],
                        'ErrorMessage': 'string',
                        'GroupArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the list of deployments for the given group.

            - **Deployments** *(list) --* A list of the individual group deployments in the bulk deployment
            operation.

              - *(dict) --* Information about an individual group deployment in a bulk deployment operation.

                - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.

                - **DeploymentArn** *(string) --* The ARN of the group deployment.

                - **DeploymentId** *(string) --* The ID of the group deployment.

                - **DeploymentStatus** *(string) --* The current status of the group deployment:
                ''InProgress'', ''Building'', ''Success'', or ''Failure''.

                - **DeploymentType** *(string) --* The type of the deployment.

                - **ErrorDetails** *(list) --* Details about the error.

                  - *(dict) --* Details about the error.

                    - **DetailedErrorCode** *(string) --* A detailed error code.

                    - **DetailedErrorMessage** *(string) --* A detailed error message.

                - **ErrorMessage** *(string) --* The error message for a failed deployment

                - **GroupArn** *(string) --* The ARN of the Greengrass group.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bulk_deployments(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListBulkDeploymentsResponseTypeDef:
        """
        Returns a list of bulk deployments.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListBulkDeployments>`_

        **Request Syntax**
        ::

          response = client.list_bulk_deployments(
              MaxResults='string',
              NextToken='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'BulkDeployments': [
                    {
                        'BulkDeploymentArn': 'string',
                        'BulkDeploymentId': 'string',
                        'CreatedAt': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the list of bulk deployments.

            - **BulkDeployments** *(list) --* A list of bulk deployments.

              - *(dict) --* Information about a bulk deployment. You cannot start a new bulk deployment
              while another one is still running or in a non-terminal state.

                - **BulkDeploymentArn** *(string) --* The ARN of the bulk deployment.

                - **BulkDeploymentId** *(string) --* The ID of the bulk deployment.

                - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_connector_definition_versions(
        self, ConnectorDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListConnectorDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a connector definition, which are containers for connectors. Connectors run
        on the Greengrass core and contain built-in integration with local infrastructure, device
        protocols, AWS, and other cloud services.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListConnectorDefinitionVersions>`_

        **Request Syntax**
        ::

          response = client.list_connector_definition_versions(
              ConnectorDefinitionId='string',
              MaxResults='string',
              NextToken='string'
          )
        :type ConnectorDefinitionId: string
        :param ConnectorDefinitionId: **[REQUIRED]** The ID of the connector definition.

        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Versions** *(list) --* Information about a version.

              - *(dict) --* Information about a version.

                - **Arn** *(string) --* The ARN of the version.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                version was created.

                - **Id** *(string) --* The ID of the parent definition that the version is associated with.

                - **Version** *(string) --* The ID of the version.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_connector_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListConnectorDefinitionsResponseTypeDef:
        """
        Retrieves a list of connector definitions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListConnectorDefinitions>`_

        **Request Syntax**
        ::

          response = client.list_connector_definitions(
              MaxResults='string',
              NextToken='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string',
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Definitions** *(list) --* Information about a definition.

              - *(dict) --* Information about a definition.

                - **Arn** *(string) --* The ARN of the definition.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                definition was created.

                - **Id** *(string) --* The ID of the definition.

                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
                the definition was last updated.

                - **LatestVersion** *(string) --* The ID of the latest version associated with the
                definition.

                - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
                definition.

                - **Name** *(string) --* The name of the definition.

                - **Tags** *(dict) --* Tag(s) attached to the resource arn.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_core_definition_versions(
        self, CoreDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListCoreDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a core definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListCoreDefinitionVersions>`_

        **Request Syntax**
        ::

          response = client.list_core_definition_versions(
              CoreDefinitionId='string',
              MaxResults='string',
              NextToken='string'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.

        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Versions** *(list) --* Information about a version.

              - *(dict) --* Information about a version.

                - **Arn** *(string) --* The ARN of the version.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                version was created.

                - **Id** *(string) --* The ID of the parent definition that the version is associated with.

                - **Version** *(string) --* The ID of the version.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_core_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListCoreDefinitionsResponseTypeDef:
        """
        Retrieves a list of core definitions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListCoreDefinitions>`_

        **Request Syntax**
        ::

          response = client.list_core_definitions(
              MaxResults='string',
              NextToken='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string',
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Definitions** *(list) --* Information about a definition.

              - *(dict) --* Information about a definition.

                - **Arn** *(string) --* The ARN of the definition.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                definition was created.

                - **Id** *(string) --* The ID of the definition.

                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
                the definition was last updated.

                - **LatestVersion** *(string) --* The ID of the latest version associated with the
                definition.

                - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
                definition.

                - **Name** *(string) --* The name of the definition.

                - **Tags** *(dict) --* Tag(s) attached to the resource arn.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployments(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListDeploymentsResponseTypeDef:
        """
        Returns a history of deployments for the group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeployments>`_

        **Request Syntax**
        ::

          response = client.list_deployments(
              GroupId='string',
              MaxResults='string',
              NextToken='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Deployments': [
                    {
                        'CreatedAt': 'string',
                        'DeploymentArn': 'string',
                        'DeploymentId': 'string',
                        'DeploymentType':
                        'NewDeployment'|'Redeployment'|'ResetDeployment'|'ForceResetDeployment',
                        'GroupArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the list of deployments for the given group.

            - **Deployments** *(list) --* A list of deployments for the requested groups.

              - *(dict) --* Information about a deployment.

                - **CreatedAt** *(string) --* The time, in milliseconds since the epoch, when the
                deployment was created.

                - **DeploymentArn** *(string) --* The ARN of the deployment.

                - **DeploymentId** *(string) --* The ID of the deployment.

                - **DeploymentType** *(string) --* The type of the deployment.

                - **GroupArn** *(string) --* The ARN of the group for this deployment.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_device_definition_versions(
        self, DeviceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListDeviceDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a device definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeviceDefinitionVersions>`_

        **Request Syntax**
        ::

          response = client.list_device_definition_versions(
              DeviceDefinitionId='string',
              MaxResults='string',
              NextToken='string'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.

        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Versions** *(list) --* Information about a version.

              - *(dict) --* Information about a version.

                - **Arn** *(string) --* The ARN of the version.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                version was created.

                - **Id** *(string) --* The ID of the parent definition that the version is associated with.

                - **Version** *(string) --* The ID of the version.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_device_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListDeviceDefinitionsResponseTypeDef:
        """
        Retrieves a list of device definitions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeviceDefinitions>`_

        **Request Syntax**
        ::

          response = client.list_device_definitions(
              MaxResults='string',
              NextToken='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string',
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Definitions** *(list) --* Information about a definition.

              - *(dict) --* Information about a definition.

                - **Arn** *(string) --* The ARN of the definition.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                definition was created.

                - **Id** *(string) --* The ID of the definition.

                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
                the definition was last updated.

                - **LatestVersion** *(string) --* The ID of the latest version associated with the
                definition.

                - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
                definition.

                - **Name** *(string) --* The name of the definition.

                - **Tags** *(dict) --* Tag(s) attached to the resource arn.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_function_definition_versions(
        self, FunctionDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListFunctionDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a Lambda function definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListFunctionDefinitionVersions>`_

        **Request Syntax**
        ::

          response = client.list_function_definition_versions(
              FunctionDefinitionId='string',
              MaxResults='string',
              NextToken='string'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.

        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --* success

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Versions** *(list) --* Information about a version.

              - *(dict) --* Information about a version.

                - **Arn** *(string) --* The ARN of the version.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                version was created.

                - **Id** *(string) --* The ID of the parent definition that the version is associated with.

                - **Version** *(string) --* The ID of the version.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_function_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> Dict:
        """
        Retrieves a list of Lambda function definitions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListFunctionDefinitions>`_

        **Request Syntax**
        ::

          response = client.list_function_definitions(
              MaxResults='string',
              NextToken='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string',
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response contains the IDs of all the Greengrass Lambda function
          definitions in this account.

            - **Definitions** *(list) --* Information about a definition.

              - *(dict) --* Information about a definition.

                - **Arn** *(string) --* The ARN of the definition.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                definition was created.

                - **Id** *(string) --* The ID of the definition.

                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
                the definition was last updated.

                - **LatestVersion** *(string) --* The ID of the latest version associated with the
                definition.

                - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
                definition.

                - **Name** *(string) --* The name of the definition.

                - **Tags** *(dict) --* Tag(s) attached to the resource arn.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_certificate_authorities(
        self, GroupId: str
    ) -> ClientListGroupCertificateAuthoritiesResponseTypeDef:
        """
        Retrieves the current CAs for a group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroupCertificateAuthorities>`_

        **Request Syntax**
        ::

          response = client.list_group_certificate_authorities(
              GroupId='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GroupCertificateAuthorities': [
                    {
                        'GroupCertificateAuthorityArn': 'string',
                        'GroupCertificateAuthorityId': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the PKI Configuration.

            - **GroupCertificateAuthorities** *(list) --* A list of certificate authorities associated with
            the group.

              - *(dict) --* Information about a certificate authority for a group.

                - **GroupCertificateAuthorityArn** *(string) --* The ARN of the certificate authority for
                the group.

                - **GroupCertificateAuthorityId** *(string) --* The ID of the certificate authority for the
                group.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_versions(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> Dict:
        """
        Lists the versions of a group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroupVersions>`_

        **Request Syntax**
        ::

          response = client.list_group_versions(
              GroupId='string',
              MaxResults='string',
              NextToken='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --* Success. The response contains the list of versions and metadata for the given
          group.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Versions** *(list) --* Information about a version.

              - *(dict) --* Information about a version.

                - **Arn** *(string) --* The ARN of the version.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                version was created.

                - **Id** *(string) --* The ID of the parent definition that the version is associated with.

                - **Version** *(string) --* The ID of the version.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_groups(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListGroupsResponseTypeDef:
        """
        Retrieves a list of groups.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroups>`_

        **Request Syntax**
        ::

          response = client.list_groups(
              MaxResults='string',
              NextToken='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Groups': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Groups** *(list) --* Information about a group.

              - *(dict) --* Information about a group.

                - **Arn** *(string) --* The ARN of the group.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                group was created.

                - **Id** *(string) --* The ID of the group.

                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
                the group was last updated.

                - **LatestVersion** *(string) --* The ID of the latest version associated with the group.

                - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
                group.

                - **Name** *(string) --* The name of the group.

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_logger_definition_versions(
        self, LoggerDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListLoggerDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a logger definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListLoggerDefinitionVersions>`_

        **Request Syntax**
        ::

          response = client.list_logger_definition_versions(
              LoggerDefinitionId='string',
              MaxResults='string',
              NextToken='string'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.

        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Versions** *(list) --* Information about a version.

              - *(dict) --* Information about a version.

                - **Arn** *(string) --* The ARN of the version.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                version was created.

                - **Id** *(string) --* The ID of the parent definition that the version is associated with.

                - **Version** *(string) --* The ID of the version.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_logger_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListLoggerDefinitionsResponseTypeDef:
        """
        Retrieves a list of logger definitions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListLoggerDefinitions>`_

        **Request Syntax**
        ::

          response = client.list_logger_definitions(
              MaxResults='string',
              NextToken='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string',
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Definitions** *(list) --* Information about a definition.

              - *(dict) --* Information about a definition.

                - **Arn** *(string) --* The ARN of the definition.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                definition was created.

                - **Id** *(string) --* The ID of the definition.

                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
                the definition was last updated.

                - **LatestVersion** *(string) --* The ID of the latest version associated with the
                definition.

                - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
                definition.

                - **Name** *(string) --* The name of the definition.

                - **Tags** *(dict) --* Tag(s) attached to the resource arn.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_definition_versions(
        self, ResourceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListResourceDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a resource definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListResourceDefinitionVersions>`_

        **Request Syntax**
        ::

          response = client.list_resource_definition_versions(
              MaxResults='string',
              NextToken='string',
              ResourceDefinitionId='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --* success

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Versions** *(list) --* Information about a version.

              - *(dict) --* Information about a version.

                - **Arn** *(string) --* The ARN of the version.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                version was created.

                - **Id** *(string) --* The ID of the parent definition that the version is associated with.

                - **Version** *(string) --* The ID of the version.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListResourceDefinitionsResponseTypeDef:
        """
        Retrieves a list of resource definitions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListResourceDefinitions>`_

        **Request Syntax**
        ::

          response = client.list_resource_definitions(
              MaxResults='string',
              NextToken='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string',
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --* The IDs of all the Greengrass resource definitions in this account.

            - **Definitions** *(list) --* Information about a definition.

              - *(dict) --* Information about a definition.

                - **Arn** *(string) --* The ARN of the definition.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                definition was created.

                - **Id** *(string) --* The ID of the definition.

                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
                the definition was last updated.

                - **LatestVersion** *(string) --* The ID of the latest version associated with the
                definition.

                - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
                definition.

                - **Name** *(string) --* The name of the definition.

                - **Tags** *(dict) --* Tag(s) attached to the resource arn.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_subscription_definition_versions(
        self,
        SubscriptionDefinitionId: str,
        MaxResults: str = None,
        NextToken: str = None,
    ) -> ClientListSubscriptionDefinitionVersionsResponseTypeDef:
        """
        Lists the versions of a subscription definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListSubscriptionDefinitionVersions>`_

        **Request Syntax**
        ::

          response = client.list_subscription_definition_versions(
              MaxResults='string',
              NextToken='string',
              SubscriptionDefinitionId='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Versions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'Version': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.

            - **Versions** *(list) --* Information about a version.

              - *(dict) --* Information about a version.

                - **Arn** *(string) --* The ARN of the version.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                version was created.

                - **Id** *(string) --* The ID of the parent definition that the version is associated with.

                - **Version** *(string) --* The ID of the version.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_subscription_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListSubscriptionDefinitionsResponseTypeDef:
        """
        Retrieves a list of subscription definitions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListSubscriptionDefinitions>`_

        **Request Syntax**
        ::

          response = client.list_subscription_definitions(
              MaxResults='string',
              NextToken='string'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.

        :type NextToken: string
        :param NextToken: The token for the next set of results, or ''null'' if there are no additional
        results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Definitions': [
                    {
                        'Arn': 'string',
                        'CreationTimestamp': 'string',
                        'Id': 'string',
                        'LastUpdatedTimestamp': 'string',
                        'LatestVersion': 'string',
                        'LatestVersionArn': 'string',
                        'Name': 'string',
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Definitions** *(list) --* Information about a definition.

              - *(dict) --* Information about a definition.

                - **Arn** *(string) --* The ARN of the definition.

                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
                definition was created.

                - **Id** *(string) --* The ID of the definition.

                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
                the definition was last updated.

                - **LatestVersion** *(string) --* The ID of the latest version associated with the
                definition.

                - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
                definition.

                - **Name** *(string) --* The name of the definition.

                - **Tags** *(dict) --* Tag(s) attached to the resource arn.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
            no additional results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of resource tags for a resource arn.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** The Amazon Resource Name (ARN) of the resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --* HTTP Status Code 200: OK.

            - **tags** *(dict) --* The key-value pair for the resource tag.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_deployments(
        self, GroupId: str, AmznClientToken: str = None, Force: bool = None
    ) -> ClientResetDeploymentsResponseTypeDef:
        """
        Resets a group's deployments.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ResetDeployments>`_

        **Request Syntax**
        ::

          response = client.reset_deployments(
              AmznClientToken='string',
              Force=True|False,
              GroupId='string'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type Force: boolean
        :param Force: If true, performs a best-effort only core reset.

        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DeploymentArn': 'string',
                'DeploymentId': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The group's deployments were reset.

            - **DeploymentArn** *(string) --* The ARN of the deployment.

            - **DeploymentId** *(string) --* The ID of the deployment.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_bulk_deployment(
        self,
        ExecutionRoleArn: str,
        InputFileUri: str,
        AmznClientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientStartBulkDeploymentResponseTypeDef:
        """
        Deploys multiple groups in one operation. This action starts the bulk deployment of a specified set
        of group versions. Each group version deployment will be triggered with an adaptive rate that has a
        fixed upper limit. We recommend that you include an ''X-Amzn-Client-Token'' token in every
        ''StartBulkDeployment'' request. These requests are idempotent with respect to the token and the
        request parameters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/StartBulkDeployment>`_

        **Request Syntax**
        ::

          response = client.start_bulk_deployment(
              AmznClientToken='string',
              ExecutionRoleArn='string',
              InputFileUri='string',
              tags={
                  'string': 'string'
              }
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.

        :type ExecutionRoleArn: string
        :param ExecutionRoleArn: **[REQUIRED]** The ARN of the execution role to associate with the bulk
        deployment operation. This IAM role must allow the ''greengrass:CreateDeployment'' action for all
        group versions that are listed in the input file. This IAM role must have access to the S3 bucket
        containing the input file.

        :type InputFileUri: string
        :param InputFileUri: **[REQUIRED]** The URI of the input file contained in the S3 bucket. The
        execution role must have ''getObject'' permissions on this bucket to access the input file. The
        input file is a JSON-serialized, line delimited file with UTF-8 encoding that provides a list of
        group and version IDs and the deployment type. This file must be less than 100 MB. Currently, AWS
        IoT Greengrass supports only ''NewDeployment'' deployment types.

        :type tags: dict
        :param tags: Tag(s) to add to the new resource.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'BulkDeploymentArn': 'string',
                'BulkDeploymentId': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **BulkDeploymentArn** *(string) --* The ARN of the bulk deployment.

            - **BulkDeploymentId** *(string) --* The ID of the bulk deployment.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_bulk_deployment(self, BulkDeploymentId: str) -> Dict[str, Any]:
        """
        Stops the execution of a bulk deployment. This action returns a status of ''Stopping'' until the
        deployment is stopped. You cannot start a new bulk deployment while a previous deployment is in the
        ''Stopping'' state. This action doesn't rollback completed deployments or cancel pending
        deployments.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/StopBulkDeployment>`_

        **Request Syntax**
        ::

          response = client.stop_bulk_deployment(
              BulkDeploymentId='string'
          )
        :type BulkDeploymentId: string
        :param BulkDeploymentId: **[REQUIRED]** The ID of the bulk deployment.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* Success. The bulk deployment is being stopped.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, tags: Dict[str, str] = None) -> None:
        """
        Adds tags to a Greengrass resource. Valid resources are 'Group', 'ConnectorDefinition',
        'CoreDefinition', 'DeviceDefinition', 'FunctionDefinition', 'LoggerDefinition',
        'SubscriptionDefinition', 'ResourceDefinition', and 'BulkDeployment'.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              tags={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** The Amazon Resource Name (ARN) of the resource.

        :type tags: dict
        :param tags: The key-value pair for the resource tag.

          - *(string) --*

            - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Remove resource tags from a Greengrass Resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** The Amazon Resource Name (ARN) of the resource.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** An array of tag keys to delete

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_connectivity_info(
        self,
        ThingName: str,
        ConnectivityInfo: List[
            ClientUpdateConnectivityInfoConnectivityInfoTypeDef
        ] = None,
    ) -> ClientUpdateConnectivityInfoResponseTypeDef:
        """
        Updates the connectivity information for the core. Any devices that belong to the group which has
        this core will receive this information in order to find the location of the core and connect to it.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateConnectivityInfo>`_

        **Request Syntax**
        ::

          response = client.update_connectivity_info(
              ConnectivityInfo=[
                  {
                      'HostAddress': 'string',
                      'Id': 'string',
                      'Metadata': 'string',
                      'PortNumber': 123
                  },
              ],
              ThingName='string'
          )
        :type ConnectivityInfo: list
        :param ConnectivityInfo: A list of connectivity info.

          - *(dict) --* Information about a Greengrass core's connectivity.

            - **HostAddress** *(string) --* The endpoint for the Greengrass core. Can be an IP address or
            DNS.

            - **Id** *(string) --* The ID of the connectivity information.

            - **Metadata** *(string) --* Metadata for this endpoint.

            - **PortNumber** *(integer) --* The port of the Greengrass core. Usually 8883.

        :type ThingName: string
        :param ThingName: **[REQUIRED]** The thing name.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Message': 'string',
                'Version': 'string'
            }
          **Response Structure**

          - *(dict) --* success

            - **Message** *(string) --* A message about the connectivity info update request.

            - **Version** *(string) --* The new version of the connectivity info.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_connector_definition(
        self, ConnectorDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        Updates a connector definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateConnectorDefinition>`_

        **Request Syntax**
        ::

          response = client.update_connector_definition(
              ConnectorDefinitionId='string',
              Name='string'
          )
        :type ConnectorDefinitionId: string
        :param ConnectorDefinitionId: **[REQUIRED]** The ID of the connector definition.

        :type Name: string
        :param Name: The name of the definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_core_definition(
        self, CoreDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        Updates a core definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateCoreDefinition>`_

        **Request Syntax**
        ::

          response = client.update_core_definition(
              CoreDefinitionId='string',
              Name='string'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.

        :type Name: string
        :param Name: The name of the definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device_definition(
        self, DeviceDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        Updates a device definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateDeviceDefinition>`_

        **Request Syntax**
        ::

          response = client.update_device_definition(
              DeviceDefinitionId='string',
              Name='string'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.

        :type Name: string
        :param Name: The name of the definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function_definition(
        self, FunctionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        Updates a Lambda function definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateFunctionDefinition>`_

        **Request Syntax**
        ::

          response = client.update_function_definition(
              FunctionDefinitionId='string',
              Name='string'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.

        :type Name: string
        :param Name: The name of the definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group(self, GroupId: str, Name: str = None) -> Dict[str, Any]:
        """
        Updates a group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateGroup>`_

        **Request Syntax**
        ::

          response = client.update_group(
              GroupId='string',
              Name='string'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :type Name: string
        :param Name: The name of the definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group_certificate_configuration(
        self, GroupId: str, CertificateExpiryInMilliseconds: str = None
    ) -> ClientUpdateGroupCertificateConfigurationResponseTypeDef:
        """
        Updates the Certificate expiry time for a group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateGroupCertificateConfiguration>`_
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateGroupCertificateConfiguration>`_

        **Request Syntax**
        ::

          response = client.update_group_certificate_configuration(
              CertificateExpiryInMilliseconds='string',
              GroupId='string'
          )
        :type CertificateExpiryInMilliseconds: string
        :param CertificateExpiryInMilliseconds: The amount of time remaining before the certificate
        expires, in milliseconds.

        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the Greengrass group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CertificateAuthorityExpiryInMilliseconds': 'string',
                'CertificateExpiryInMilliseconds': 'string',
                'GroupId': 'string'
            }
          **Response Structure**

          - *(dict) --* Success. The response body contains the PKI Configuration.

            - **CertificateAuthorityExpiryInMilliseconds** *(string) --* The amount of time remaining
            before the certificate authority expires, in milliseconds.

            - **CertificateExpiryInMilliseconds** *(string) --* The amount of time remaining before the
            certificate expires, in milliseconds.

            - **GroupId** *(string) --* The ID of the group certificate configuration.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_logger_definition(
        self, LoggerDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        Updates a logger definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateLoggerDefinition>`_

        **Request Syntax**
        ::

          response = client.update_logger_definition(
              LoggerDefinitionId='string',
              Name='string'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.

        :type Name: string
        :param Name: The name of the definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resource_definition(
        self, ResourceDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        Updates a resource definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateResourceDefinition>`_

        **Request Syntax**
        ::

          response = client.update_resource_definition(
              Name='string',
              ResourceDefinitionId='string'
          )
        :type Name: string
        :param Name: The name of the definition.

        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_subscription_definition(
        self, SubscriptionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        Updates a subscription definition.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateSubscriptionDefinition>`_

        **Request Syntax**
        ::

          response = client.update_subscription_definition(
              Name='string',
              SubscriptionDefinitionId='string'
          )
        :type Name: string
        :param Name: The name of the definition.

        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --* success
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployment_detailed_reports"]
    ) -> paginator_scope.ListBulkDeploymentDetailedReportsPaginator:
        """
        Get Paginator for `list_bulk_deployment_detailed_reports` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployments"]
    ) -> paginator_scope.ListBulkDeploymentsPaginator:
        """
        Get Paginator for `list_bulk_deployments` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_connector_definition_versions"]
    ) -> paginator_scope.ListConnectorDefinitionVersionsPaginator:
        """
        Get Paginator for `list_connector_definition_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_connector_definitions"]
    ) -> paginator_scope.ListConnectorDefinitionsPaginator:
        """
        Get Paginator for `list_connector_definitions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_core_definition_versions"]
    ) -> paginator_scope.ListCoreDefinitionVersionsPaginator:
        """
        Get Paginator for `list_core_definition_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_core_definitions"]
    ) -> paginator_scope.ListCoreDefinitionsPaginator:
        """
        Get Paginator for `list_core_definitions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> paginator_scope.ListDeploymentsPaginator:
        """
        Get Paginator for `list_deployments` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_device_definition_versions"]
    ) -> paginator_scope.ListDeviceDefinitionVersionsPaginator:
        """
        Get Paginator for `list_device_definition_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_device_definitions"]
    ) -> paginator_scope.ListDeviceDefinitionsPaginator:
        """
        Get Paginator for `list_device_definitions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_function_definition_versions"]
    ) -> paginator_scope.ListFunctionDefinitionVersionsPaginator:
        """
        Get Paginator for `list_function_definition_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_function_definitions"]
    ) -> paginator_scope.ListFunctionDefinitionsPaginator:
        """
        Get Paginator for `list_function_definitions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_group_versions"]
    ) -> paginator_scope.ListGroupVersionsPaginator:
        """
        Get Paginator for `list_group_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> paginator_scope.ListGroupsPaginator:
        """
        Get Paginator for `list_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_logger_definition_versions"]
    ) -> paginator_scope.ListLoggerDefinitionVersionsPaginator:
        """
        Get Paginator for `list_logger_definition_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_logger_definitions"]
    ) -> paginator_scope.ListLoggerDefinitionsPaginator:
        """
        Get Paginator for `list_logger_definitions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_definition_versions"]
    ) -> paginator_scope.ListResourceDefinitionVersionsPaginator:
        """
        Get Paginator for `list_resource_definition_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_definitions"]
    ) -> paginator_scope.ListResourceDefinitionsPaginator:
        """
        Get Paginator for `list_resource_definitions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_subscription_definition_versions"]
    ) -> paginator_scope.ListSubscriptionDefinitionVersionsPaginator:
        """
        Get Paginator for `list_subscription_definition_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_subscription_definitions"]
    ) -> paginator_scope.ListSubscriptionDefinitionsPaginator:
        """
        Get Paginator for `list_subscription_definitions` operation.
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
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
