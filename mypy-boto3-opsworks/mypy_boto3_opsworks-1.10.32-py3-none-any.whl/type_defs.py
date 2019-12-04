"Main interface for opsworks service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "AppExistsWaitWaiterConfigTypeDef",
    "ClientCloneStackChefConfigurationTypeDef",
    "ClientCloneStackConfigurationManagerTypeDef",
    "ClientCloneStackCustomCookbooksSourceTypeDef",
    "ClientCloneStackResponseTypeDef",
    "ClientCreateAppAppSourceTypeDef",
    "ClientCreateAppDataSourcesTypeDef",
    "ClientCreateAppEnvironmentTypeDef",
    "ClientCreateAppResponseTypeDef",
    "ClientCreateAppSslConfigurationTypeDef",
    "ClientCreateDeploymentCommandTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateInstanceBlockDeviceMappingsEbsTypeDef",
    "ClientCreateInstanceBlockDeviceMappingsTypeDef",
    "ClientCreateInstanceResponseTypeDef",
    "ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    "ClientCreateLayerCloudWatchLogsConfigurationTypeDef",
    "ClientCreateLayerCustomRecipesTypeDef",
    "ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    "ClientCreateLayerLifecycleEventConfigurationTypeDef",
    "ClientCreateLayerResponseTypeDef",
    "ClientCreateLayerVolumeConfigurationsTypeDef",
    "ClientCreateStackChefConfigurationTypeDef",
    "ClientCreateStackConfigurationManagerTypeDef",
    "ClientCreateStackCustomCookbooksSourceTypeDef",
    "ClientCreateStackResponseTypeDef",
    "ClientCreateUserProfileResponseTypeDef",
    "ClientDescribeAgentVersionsConfigurationManagerTypeDef",
    "ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef",
    "ClientDescribeAgentVersionsResponseAgentVersionsTypeDef",
    "ClientDescribeAgentVersionsResponseTypeDef",
    "ClientDescribeAppsResponseAppsAppSourceTypeDef",
    "ClientDescribeAppsResponseAppsDataSourcesTypeDef",
    "ClientDescribeAppsResponseAppsEnvironmentTypeDef",
    "ClientDescribeAppsResponseAppsSslConfigurationTypeDef",
    "ClientDescribeAppsResponseAppsTypeDef",
    "ClientDescribeAppsResponseTypeDef",
    "ClientDescribeCommandsResponseCommandsTypeDef",
    "ClientDescribeCommandsResponseTypeDef",
    "ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef",
    "ClientDescribeDeploymentsResponseDeploymentsTypeDef",
    "ClientDescribeDeploymentsResponseTypeDef",
    "ClientDescribeEcsClustersResponseEcsClustersTypeDef",
    "ClientDescribeEcsClustersResponseTypeDef",
    "ClientDescribeElasticIpsResponseElasticIpsTypeDef",
    "ClientDescribeElasticIpsResponseTypeDef",
    "ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef",
    "ClientDescribeElasticLoadBalancersResponseTypeDef",
    "ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef",
    "ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef",
    "ClientDescribeInstancesResponseInstancesReportedOsTypeDef",
    "ClientDescribeInstancesResponseInstancesTypeDef",
    "ClientDescribeInstancesResponseTypeDef",
    "ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef",
    "ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef",
    "ClientDescribeLayersResponseLayersCustomRecipesTypeDef",
    "ClientDescribeLayersResponseLayersDefaultRecipesTypeDef",
    "ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef",
    "ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef",
    "ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef",
    "ClientDescribeLayersResponseLayersTypeDef",
    "ClientDescribeLayersResponseTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseTypeDef",
    "ClientDescribeMyUserProfileResponseUserProfileTypeDef",
    "ClientDescribeMyUserProfileResponseTypeDef",
    "ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef",
    "ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef",
    "ClientDescribeOperatingSystemsResponseTypeDef",
    "ClientDescribePermissionsResponsePermissionsTypeDef",
    "ClientDescribePermissionsResponseTypeDef",
    "ClientDescribeRaidArraysResponseRaidArraysTypeDef",
    "ClientDescribeRaidArraysResponseTypeDef",
    "ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef",
    "ClientDescribeRdsDbInstancesResponseTypeDef",
    "ClientDescribeServiceErrorsResponseServiceErrorsTypeDef",
    "ClientDescribeServiceErrorsResponseTypeDef",
    "ClientDescribeStackProvisioningParametersResponseTypeDef",
    "ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef",
    "ClientDescribeStackSummaryResponseStackSummaryTypeDef",
    "ClientDescribeStackSummaryResponseTypeDef",
    "ClientDescribeStacksResponseStacksChefConfigurationTypeDef",
    "ClientDescribeStacksResponseStacksConfigurationManagerTypeDef",
    "ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef",
    "ClientDescribeStacksResponseStacksTypeDef",
    "ClientDescribeStacksResponseTypeDef",
    "ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef",
    "ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef",
    "ClientDescribeTimeBasedAutoScalingResponseTypeDef",
    "ClientDescribeUserProfilesResponseUserProfilesTypeDef",
    "ClientDescribeUserProfilesResponseTypeDef",
    "ClientDescribeVolumesResponseVolumesTypeDef",
    "ClientDescribeVolumesResponseTypeDef",
    "ClientGetHostnameSuggestionResponseTypeDef",
    "ClientGrantAccessResponseTemporaryCredentialTypeDef",
    "ClientGrantAccessResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientRegisterEcsClusterResponseTypeDef",
    "ClientRegisterElasticIpResponseTypeDef",
    "ClientRegisterInstanceInstanceIdentityTypeDef",
    "ClientRegisterInstanceResponseTypeDef",
    "ClientRegisterVolumeResponseTypeDef",
    "ClientSetLoadBasedAutoScalingDownScalingTypeDef",
    "ClientSetLoadBasedAutoScalingUpScalingTypeDef",
    "ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef",
    "ClientUpdateAppAppSourceTypeDef",
    "ClientUpdateAppDataSourcesTypeDef",
    "ClientUpdateAppEnvironmentTypeDef",
    "ClientUpdateAppSslConfigurationTypeDef",
    "ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    "ClientUpdateLayerCloudWatchLogsConfigurationTypeDef",
    "ClientUpdateLayerCustomRecipesTypeDef",
    "ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef",
    "ClientUpdateLayerLifecycleEventConfigurationTypeDef",
    "ClientUpdateLayerVolumeConfigurationsTypeDef",
    "ClientUpdateStackChefConfigurationTypeDef",
    "ClientUpdateStackConfigurationManagerTypeDef",
    "ClientUpdateStackCustomCookbooksSourceTypeDef",
    "DeploymentSuccessfulWaitWaiterConfigTypeDef",
    "DescribeEcsClustersPaginatePaginationConfigTypeDef",
    "DescribeEcsClustersPaginateResponseEcsClustersTypeDef",
    "DescribeEcsClustersPaginateResponseTypeDef",
    "InstanceOnlineWaitWaiterConfigTypeDef",
    "InstanceRegisteredWaitWaiterConfigTypeDef",
    "InstanceStoppedWaitWaiterConfigTypeDef",
    "InstanceTerminatedWaitWaiterConfigTypeDef",
    "ServiceResourceCreateStackChefConfigurationTypeDef",
    "ServiceResourceCreateStackConfigurationManagerTypeDef",
    "ServiceResourceCreateStackCustomCookbooksSourceTypeDef",
    "StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    "StackCreateLayerCloudWatchLogsConfigurationTypeDef",
    "StackCreateLayerCustomRecipesTypeDef",
    "StackCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    "StackCreateLayerLifecycleEventConfigurationTypeDef",
    "StackCreateLayerVolumeConfigurationsTypeDef",
)


_AppExistsWaitWaiterConfigTypeDef = TypedDict(
    "_AppExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class AppExistsWaitWaiterConfigTypeDef(_AppExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1
    """


_ClientCloneStackChefConfigurationTypeDef = TypedDict(
    "_ClientCloneStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ClientCloneStackChefConfigurationTypeDef(_ClientCloneStackChefConfigurationTypeDef):
    """
    A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf
    version on Chef 11.10 stacks. For more information, see `Create a New Stack
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .
    - **ManageBerkshelf** *(boolean) --*

      Whether to enable Berkshelf.
    """


_ClientCloneStackConfigurationManagerTypeDef = TypedDict(
    "_ClientCloneStackConfigurationManagerTypeDef", {"Name": str, "Version": str}, total=False
)


class ClientCloneStackConfigurationManagerTypeDef(_ClientCloneStackConfigurationManagerTypeDef):
    """
    The configuration manager. When you clone a stack we recommend that you use the configuration
    manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows
    stacks. The default value for Linux stacks is currently 12.
    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".
    """


_ClientCloneStackCustomCookbooksSourceTypeDef = TypedDict(
    "_ClientCloneStackCustomCookbooksSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientCloneStackCustomCookbooksSourceTypeDef(_ClientCloneStackCustomCookbooksSourceTypeDef):
    """
    Contains the information required to retrieve an app or cookbook from a repository. For more
    information, see `Adding Apps
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
    `Cookbooks and Recipes
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .
    - **Type** *(string) --*

      The repository type.
    """


_ClientCloneStackResponseTypeDef = TypedDict(
    "_ClientCloneStackResponseTypeDef", {"StackId": str}, total=False
)


class ClientCloneStackResponseTypeDef(_ClientCloneStackResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``CloneStack`` request.
      - **StackId** *(string) --*

        The cloned stack ID.
    """


_ClientCreateAppAppSourceTypeDef = TypedDict(
    "_ClientCreateAppAppSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientCreateAppAppSourceTypeDef(_ClientCreateAppAppSourceTypeDef):
    """
    A ``Source`` object that specifies the app repository.
    - **Type** *(string) --*

      The repository type.
    """


_ClientCreateAppDataSourcesTypeDef = TypedDict(
    "_ClientCreateAppDataSourcesTypeDef",
    {"Type": str, "Arn": str, "DatabaseName": str},
    total=False,
)


class ClientCreateAppDataSourcesTypeDef(_ClientCreateAppDataSourcesTypeDef):
    """
    - *(dict) --*

      Describes an app's data source.
      - **Type** *(string) --*

        The data source's type, ``AutoSelectOpsworksMysqlInstance`` , ``OpsworksMysqlInstance`` ,
        ``RdsDbInstance`` , or ``None`` .
    """


_ClientCreateAppEnvironmentTypeDef = TypedDict(
    "_ClientCreateAppEnvironmentTypeDef", {"Key": str, "Value": str, "Secure": bool}, total=False
)


class ClientCreateAppEnvironmentTypeDef(_ClientCreateAppEnvironmentTypeDef):
    pass


_ClientCreateAppResponseTypeDef = TypedDict(
    "_ClientCreateAppResponseTypeDef", {"AppId": str}, total=False
)


class ClientCreateAppResponseTypeDef(_ClientCreateAppResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``CreateApp`` request.
      - **AppId** *(string) --*

        The app ID.
    """


_RequiredClientCreateAppSslConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateAppSslConfigurationTypeDef", {"Certificate": str}
)
_OptionalClientCreateAppSslConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateAppSslConfigurationTypeDef",
    {"PrivateKey": str, "Chain": str},
    total=False,
)


class ClientCreateAppSslConfigurationTypeDef(
    _RequiredClientCreateAppSslConfigurationTypeDef, _OptionalClientCreateAppSslConfigurationTypeDef
):
    """
    An ``SslConfiguration`` object with the SSL configuration.
    - **Certificate** *(string) --***[REQUIRED]**

      The contents of the certificate's domain.crt file.
    """


_RequiredClientCreateDeploymentCommandTypeDef = TypedDict(
    "_RequiredClientCreateDeploymentCommandTypeDef",
    {
        "Name": Literal[
            "install_dependencies",
            "update_dependencies",
            "update_custom_cookbooks",
            "execute_recipes",
            "configure",
            "setup",
            "deploy",
            "rollback",
            "start",
            "stop",
            "restart",
            "undeploy",
        ]
    },
)
_OptionalClientCreateDeploymentCommandTypeDef = TypedDict(
    "_OptionalClientCreateDeploymentCommandTypeDef", {"Args": Dict[str, List[str]]}, total=False
)


class ClientCreateDeploymentCommandTypeDef(
    _RequiredClientCreateDeploymentCommandTypeDef, _OptionalClientCreateDeploymentCommandTypeDef
):
    """
    A ``DeploymentCommand`` object that specifies the deployment command and any associated
    arguments.
    - **Name** *(string) --***[REQUIRED]**

      Specifies the operation. You can specify only one command.
      For stacks, the following commands are available:
      * ``execute_recipes`` : Execute one or more recipes. To specify the recipes, set an ``Args``
      parameter named ``recipes`` to the list of recipes to be executed. For example, to execute
      ``phpapp::appsetup`` , set ``Args`` to ``{"recipes":["phpapp::appsetup"]}`` .
      * ``install_dependencies`` : Install the stack's dependencies.
      * ``update_custom_cookbooks`` : Update the stack's custom cookbooks.
      * ``update_dependencies`` : Update the stack's dependencies.
      .. note::

        The update_dependencies and install_dependencies commands are supported only for Linux
        instances. You can run the commands successfully on Windows instances, but they do nothing.
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef", {"DeploymentId": str}, total=False
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``CreateDeployment`` request.
      - **DeploymentId** *(string) --*

        The deployment ID, which can be used with other requests to identify the deployment.
    """


_ClientCreateInstanceBlockDeviceMappingsEbsTypeDef = TypedDict(
    "_ClientCreateInstanceBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "Iops": int,
        "VolumeSize": int,
        "VolumeType": Literal["gp2", "io1", "standard"],
        "DeleteOnTermination": bool,
    },
    total=False,
)


class ClientCreateInstanceBlockDeviceMappingsEbsTypeDef(
    _ClientCreateInstanceBlockDeviceMappingsEbsTypeDef
):
    pass


_ClientCreateInstanceBlockDeviceMappingsTypeDef = TypedDict(
    "_ClientCreateInstanceBlockDeviceMappingsTypeDef",
    {
        "DeviceName": str,
        "NoDevice": str,
        "VirtualName": str,
        "Ebs": ClientCreateInstanceBlockDeviceMappingsEbsTypeDef,
    },
    total=False,
)


class ClientCreateInstanceBlockDeviceMappingsTypeDef(
    _ClientCreateInstanceBlockDeviceMappingsTypeDef
):
    """
    - *(dict) --*

      Describes a block device mapping. This data type maps directly to the Amazon EC2
      `BlockDeviceMapping
      <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`__ data
      type.
      - **DeviceName** *(string) --*

        The device name that is exposed to the instance, such as ``/dev/sdh`` . For the root device,
        you can use the explicit device name or you can set this parameter to ``ROOT_DEVICE`` and
        AWS OpsWorks Stacks will provide the correct device name.
    """


_ClientCreateInstanceResponseTypeDef = TypedDict(
    "_ClientCreateInstanceResponseTypeDef", {"InstanceId": str}, total=False
)


class ClientCreateInstanceResponseTypeDef(_ClientCreateInstanceResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``CreateInstance`` request.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "_ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": Literal["LOCAL", "UTC"],
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": Literal["start_of_file", "end_of_file"],
        "Encoding": Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "johab",
            "koi8_r",
            "koi8_u",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ],
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)


class ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef(
    _ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef
):
    pass


_ClientCreateLayerCloudWatchLogsConfigurationTypeDef = TypedDict(
    "_ClientCreateLayerCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef],
    },
    total=False,
)


class ClientCreateLayerCloudWatchLogsConfigurationTypeDef(
    _ClientCreateLayerCloudWatchLogsConfigurationTypeDef
):
    """
    Specifies CloudWatch Logs configuration options for the layer. For more information, see
    CloudWatchLogsLogStream .
    - **Enabled** *(boolean) --*

      Whether CloudWatch Logs is enabled for a layer.
    """


_ClientCreateLayerCustomRecipesTypeDef = TypedDict(
    "_ClientCreateLayerCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)


class ClientCreateLayerCustomRecipesTypeDef(_ClientCreateLayerCustomRecipesTypeDef):
    """
    A ``LayerCustomRecipes`` object that specifies the layer custom recipes.
    - **Setup** *(list) --*

      An array of custom recipe names to be run following a ``setup`` event.
      - *(string) --*
    """


_ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "_ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)


class ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef(
    _ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef
):
    """
    - **Shutdown** *(dict) --*

      A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.
      - **ExecutionTimeout** *(integer) --*

        The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
        before shutting down an instance.
    """


_ClientCreateLayerLifecycleEventConfigurationTypeDef = TypedDict(
    "_ClientCreateLayerLifecycleEventConfigurationTypeDef",
    {"Shutdown": ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)


class ClientCreateLayerLifecycleEventConfigurationTypeDef(
    _ClientCreateLayerLifecycleEventConfigurationTypeDef
):
    """
    A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to
    specify an execution timeout and enable or disable Elastic Load Balancer connection draining.
    - **Shutdown** *(dict) --*

      A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.
      - **ExecutionTimeout** *(integer) --*

        The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
        before shutting down an instance.
    """


_ClientCreateLayerResponseTypeDef = TypedDict(
    "_ClientCreateLayerResponseTypeDef", {"LayerId": str}, total=False
)


class ClientCreateLayerResponseTypeDef(_ClientCreateLayerResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``CreateLayer`` request.
      - **LayerId** *(string) --*

        The layer ID.
    """


_RequiredClientCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_RequiredClientCreateLayerVolumeConfigurationsTypeDef", {"MountPoint": str}
)
_OptionalClientCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_OptionalClientCreateLayerVolumeConfigurationsTypeDef",
    {
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class ClientCreateLayerVolumeConfigurationsTypeDef(
    _RequiredClientCreateLayerVolumeConfigurationsTypeDef,
    _OptionalClientCreateLayerVolumeConfigurationsTypeDef,
):
    """
    - *(dict) --*

      Describes an Amazon EBS volume configuration.
      - **MountPoint** *(string) --***[REQUIRED]**

        The volume mount point. For example "/dev/sdh".
    """


_ClientCreateStackChefConfigurationTypeDef = TypedDict(
    "_ClientCreateStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ClientCreateStackChefConfigurationTypeDef(_ClientCreateStackChefConfigurationTypeDef):
    """
    A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf
    version on Chef 11.10 stacks. For more information, see `Create a New Stack
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .
    - **ManageBerkshelf** *(boolean) --*

      Whether to enable Berkshelf.
    """


_ClientCreateStackConfigurationManagerTypeDef = TypedDict(
    "_ClientCreateStackConfigurationManagerTypeDef", {"Name": str, "Version": str}, total=False
)


class ClientCreateStackConfigurationManagerTypeDef(_ClientCreateStackConfigurationManagerTypeDef):
    """
    The configuration manager. When you create a stack we recommend that you use the configuration
    manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows
    stacks. The default value for Linux stacks is currently 12.
    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".
    """


_ClientCreateStackCustomCookbooksSourceTypeDef = TypedDict(
    "_ClientCreateStackCustomCookbooksSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientCreateStackCustomCookbooksSourceTypeDef(_ClientCreateStackCustomCookbooksSourceTypeDef):
    """
    Contains the information required to retrieve an app or cookbook from a repository. For more
    information, see `Adding Apps
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
    `Cookbooks and Recipes
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .
    - **Type** *(string) --*

      The repository type.
    """


_ClientCreateStackResponseTypeDef = TypedDict(
    "_ClientCreateStackResponseTypeDef", {"StackId": str}, total=False
)


class ClientCreateStackResponseTypeDef(_ClientCreateStackResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``CreateStack`` request.
      - **StackId** *(string) --*

        The stack ID, which is an opaque string that you use to identify the stack when performing
        actions such as ``DescribeStacks`` .
    """


_ClientCreateUserProfileResponseTypeDef = TypedDict(
    "_ClientCreateUserProfileResponseTypeDef", {"IamUserArn": str}, total=False
)


class ClientCreateUserProfileResponseTypeDef(_ClientCreateUserProfileResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``CreateUserProfile`` request.
      - **IamUserArn** *(string) --*

        The user's IAM ARN.
    """


_ClientDescribeAgentVersionsConfigurationManagerTypeDef = TypedDict(
    "_ClientDescribeAgentVersionsConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribeAgentVersionsConfigurationManagerTypeDef(
    _ClientDescribeAgentVersionsConfigurationManagerTypeDef
):
    """
    The configuration manager.
    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".
    """


_ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef = TypedDict(
    "_ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef(
    _ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef
):
    pass


_ClientDescribeAgentVersionsResponseAgentVersionsTypeDef = TypedDict(
    "_ClientDescribeAgentVersionsResponseAgentVersionsTypeDef",
    {
        "Version": str,
        "ConfigurationManager": ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef,
    },
    total=False,
)


class ClientDescribeAgentVersionsResponseAgentVersionsTypeDef(
    _ClientDescribeAgentVersionsResponseAgentVersionsTypeDef
):
    """
    - *(dict) --*

      Describes an agent version.
      - **Version** *(string) --*

        The agent version.
    """


_ClientDescribeAgentVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeAgentVersionsResponseTypeDef",
    {"AgentVersions": List[ClientDescribeAgentVersionsResponseAgentVersionsTypeDef]},
    total=False,
)


class ClientDescribeAgentVersionsResponseTypeDef(_ClientDescribeAgentVersionsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeAgentVersions`` request.
      - **AgentVersions** *(list) --*

        The agent versions for the specified stack or configuration manager. Note that this value is
        the complete version number, not the abbreviated number used by the console.
        - *(dict) --*

          Describes an agent version.
          - **Version** *(string) --*

            The agent version.
    """


_ClientDescribeAppsResponseAppsAppSourceTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsAppSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientDescribeAppsResponseAppsAppSourceTypeDef(
    _ClientDescribeAppsResponseAppsAppSourceTypeDef
):
    pass


_ClientDescribeAppsResponseAppsDataSourcesTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsDataSourcesTypeDef",
    {"Type": str, "Arn": str, "DatabaseName": str},
    total=False,
)


class ClientDescribeAppsResponseAppsDataSourcesTypeDef(
    _ClientDescribeAppsResponseAppsDataSourcesTypeDef
):
    pass


_ClientDescribeAppsResponseAppsEnvironmentTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsEnvironmentTypeDef",
    {"Key": str, "Value": str, "Secure": bool},
    total=False,
)


class ClientDescribeAppsResponseAppsEnvironmentTypeDef(
    _ClientDescribeAppsResponseAppsEnvironmentTypeDef
):
    pass


_ClientDescribeAppsResponseAppsSslConfigurationTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsSslConfigurationTypeDef",
    {"Certificate": str, "PrivateKey": str, "Chain": str},
    total=False,
)


class ClientDescribeAppsResponseAppsSslConfigurationTypeDef(
    _ClientDescribeAppsResponseAppsSslConfigurationTypeDef
):
    pass


_ClientDescribeAppsResponseAppsTypeDef = TypedDict(
    "_ClientDescribeAppsResponseAppsTypeDef",
    {
        "AppId": str,
        "StackId": str,
        "Shortname": str,
        "Name": str,
        "Description": str,
        "DataSources": List[ClientDescribeAppsResponseAppsDataSourcesTypeDef],
        "Type": Literal["aws-flow-ruby", "java", "rails", "php", "nodejs", "static", "other"],
        "AppSource": ClientDescribeAppsResponseAppsAppSourceTypeDef,
        "Domains": List[str],
        "EnableSsl": bool,
        "SslConfiguration": ClientDescribeAppsResponseAppsSslConfigurationTypeDef,
        "Attributes": Dict[str, str],
        "CreatedAt": str,
        "Environment": List[ClientDescribeAppsResponseAppsEnvironmentTypeDef],
    },
    total=False,
)


class ClientDescribeAppsResponseAppsTypeDef(_ClientDescribeAppsResponseAppsTypeDef):
    """
    - *(dict) --*

      A description of the app.
      - **AppId** *(string) --*

        The app ID.
    """


_ClientDescribeAppsResponseTypeDef = TypedDict(
    "_ClientDescribeAppsResponseTypeDef",
    {"Apps": List[ClientDescribeAppsResponseAppsTypeDef]},
    total=False,
)


class ClientDescribeAppsResponseTypeDef(_ClientDescribeAppsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeApps`` request.
      - **Apps** *(list) --*

        An array of ``App`` objects that describe the specified apps.
        - *(dict) --*

          A description of the app.
          - **AppId** *(string) --*

            The app ID.
    """


_ClientDescribeCommandsResponseCommandsTypeDef = TypedDict(
    "_ClientDescribeCommandsResponseCommandsTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "DeploymentId": str,
        "CreatedAt": str,
        "AcknowledgedAt": str,
        "CompletedAt": str,
        "Status": str,
        "ExitCode": int,
        "LogUrl": str,
        "Type": str,
    },
    total=False,
)


class ClientDescribeCommandsResponseCommandsTypeDef(_ClientDescribeCommandsResponseCommandsTypeDef):
    """
    - *(dict) --*

      Describes a command.
      - **CommandId** *(string) --*

        The command ID.
    """


_ClientDescribeCommandsResponseTypeDef = TypedDict(
    "_ClientDescribeCommandsResponseTypeDef",
    {"Commands": List[ClientDescribeCommandsResponseCommandsTypeDef]},
    total=False,
)


class ClientDescribeCommandsResponseTypeDef(_ClientDescribeCommandsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeCommands`` request.
      - **Commands** *(list) --*

        An array of ``Command`` objects that describe each of the specified commands.
        - *(dict) --*

          Describes a command.
          - **CommandId** *(string) --*

            The command ID.
    """


_ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef = TypedDict(
    "_ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef",
    {
        "Name": Literal[
            "install_dependencies",
            "update_dependencies",
            "update_custom_cookbooks",
            "execute_recipes",
            "configure",
            "setup",
            "deploy",
            "rollback",
            "start",
            "stop",
            "restart",
            "undeploy",
        ],
        "Args": Dict[str, List[str]],
    },
    total=False,
)


class ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef(
    _ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef
):
    pass


_ClientDescribeDeploymentsResponseDeploymentsTypeDef = TypedDict(
    "_ClientDescribeDeploymentsResponseDeploymentsTypeDef",
    {
        "DeploymentId": str,
        "StackId": str,
        "AppId": str,
        "CreatedAt": str,
        "CompletedAt": str,
        "Duration": int,
        "IamUserArn": str,
        "Comment": str,
        "Command": ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef,
        "Status": str,
        "CustomJson": str,
        "InstanceIds": List[str],
    },
    total=False,
)


class ClientDescribeDeploymentsResponseDeploymentsTypeDef(
    _ClientDescribeDeploymentsResponseDeploymentsTypeDef
):
    """
    - *(dict) --*

      Describes a deployment of a stack or app.
      - **DeploymentId** *(string) --*

        The deployment ID.
    """


_ClientDescribeDeploymentsResponseTypeDef = TypedDict(
    "_ClientDescribeDeploymentsResponseTypeDef",
    {"Deployments": List[ClientDescribeDeploymentsResponseDeploymentsTypeDef]},
    total=False,
)


class ClientDescribeDeploymentsResponseTypeDef(_ClientDescribeDeploymentsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeDeployments`` request.
      - **Deployments** *(list) --*

        An array of ``Deployment`` objects that describe the deployments.
        - *(dict) --*

          Describes a deployment of a stack or app.
          - **DeploymentId** *(string) --*

            The deployment ID.
    """


_ClientDescribeEcsClustersResponseEcsClustersTypeDef = TypedDict(
    "_ClientDescribeEcsClustersResponseEcsClustersTypeDef",
    {"EcsClusterArn": str, "EcsClusterName": str, "StackId": str, "RegisteredAt": str},
    total=False,
)


class ClientDescribeEcsClustersResponseEcsClustersTypeDef(
    _ClientDescribeEcsClustersResponseEcsClustersTypeDef
):
    """
    - *(dict) --*

      Describes a registered Amazon ECS cluster.
      - **EcsClusterArn** *(string) --*

        The cluster's ARN.
    """


_ClientDescribeEcsClustersResponseTypeDef = TypedDict(
    "_ClientDescribeEcsClustersResponseTypeDef",
    {"EcsClusters": List[ClientDescribeEcsClustersResponseEcsClustersTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeEcsClustersResponseTypeDef(_ClientDescribeEcsClustersResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeEcsClusters`` request.
      - **EcsClusters** *(list) --*

        A list of ``EcsCluster`` objects containing the cluster descriptions.
        - *(dict) --*

          Describes a registered Amazon ECS cluster.
          - **EcsClusterArn** *(string) --*

            The cluster's ARN.
    """


_ClientDescribeElasticIpsResponseElasticIpsTypeDef = TypedDict(
    "_ClientDescribeElasticIpsResponseElasticIpsTypeDef",
    {"Ip": str, "Name": str, "Domain": str, "Region": str, "InstanceId": str},
    total=False,
)


class ClientDescribeElasticIpsResponseElasticIpsTypeDef(
    _ClientDescribeElasticIpsResponseElasticIpsTypeDef
):
    """
    - *(dict) --*

      Describes an Elastic IP address.
      - **Ip** *(string) --*

        The IP address.
    """


_ClientDescribeElasticIpsResponseTypeDef = TypedDict(
    "_ClientDescribeElasticIpsResponseTypeDef",
    {"ElasticIps": List[ClientDescribeElasticIpsResponseElasticIpsTypeDef]},
    total=False,
)


class ClientDescribeElasticIpsResponseTypeDef(_ClientDescribeElasticIpsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeElasticIps`` request.
      - **ElasticIps** *(list) --*

        An ``ElasticIps`` object that describes the specified Elastic IP addresses.
        - *(dict) --*

          Describes an Elastic IP address.
          - **Ip** *(string) --*

            The IP address.
    """


_ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef = TypedDict(
    "_ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "Region": str,
        "DnsName": str,
        "StackId": str,
        "LayerId": str,
        "VpcId": str,
        "AvailabilityZones": List[str],
        "SubnetIds": List[str],
        "Ec2InstanceIds": List[str],
    },
    total=False,
)


class ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef(
    _ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef
):
    """
    - *(dict) --*

      Describes an Elastic Load Balancing instance.
      - **ElasticLoadBalancerName** *(string) --*

        The Elastic Load Balancing instance's name.
    """


_ClientDescribeElasticLoadBalancersResponseTypeDef = TypedDict(
    "_ClientDescribeElasticLoadBalancersResponseTypeDef",
    {
        "ElasticLoadBalancers": List[
            ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef
        ]
    },
    total=False,
)


class ClientDescribeElasticLoadBalancersResponseTypeDef(
    _ClientDescribeElasticLoadBalancersResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a ``DescribeElasticLoadBalancers`` request.
      - **ElasticLoadBalancers** *(list) --*

        A list of ``ElasticLoadBalancer`` objects that describe the specified Elastic Load Balancing
        instances.
        - *(dict) --*

          Describes an Elastic Load Balancing instance.
          - **ElasticLoadBalancerName** *(string) --*

            The Elastic Load Balancing instance's name.
    """


_ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef = TypedDict(
    "_ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "Iops": int,
        "VolumeSize": int,
        "VolumeType": Literal["gp2", "io1", "standard"],
        "DeleteOnTermination": bool,
    },
    total=False,
)


class ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef(
    _ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef
):
    pass


_ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef = TypedDict(
    "_ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef",
    {
        "DeviceName": str,
        "NoDevice": str,
        "VirtualName": str,
        "Ebs": ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef,
    },
    total=False,
)


class ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef(
    _ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef
):
    pass


_ClientDescribeInstancesResponseInstancesReportedOsTypeDef = TypedDict(
    "_ClientDescribeInstancesResponseInstancesReportedOsTypeDef",
    {"Family": str, "Name": str, "Version": str},
    total=False,
)


class ClientDescribeInstancesResponseInstancesReportedOsTypeDef(
    _ClientDescribeInstancesResponseInstancesReportedOsTypeDef
):
    pass


_ClientDescribeInstancesResponseInstancesTypeDef = TypedDict(
    "_ClientDescribeInstancesResponseInstancesTypeDef",
    {
        "AgentVersion": str,
        "AmiId": str,
        "Architecture": Literal["x86_64", "i386"],
        "Arn": str,
        "AutoScalingType": Literal["load", "timer"],
        "AvailabilityZone": str,
        "BlockDeviceMappings": List[
            ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef
        ],
        "CreatedAt": str,
        "EbsOptimized": bool,
        "Ec2InstanceId": str,
        "EcsClusterArn": str,
        "EcsContainerInstanceArn": str,
        "ElasticIp": str,
        "Hostname": str,
        "InfrastructureClass": str,
        "InstallUpdatesOnBoot": bool,
        "InstanceId": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "LastServiceErrorId": str,
        "LayerIds": List[str],
        "Os": str,
        "Platform": str,
        "PrivateDns": str,
        "PrivateIp": str,
        "PublicDns": str,
        "PublicIp": str,
        "RegisteredBy": str,
        "ReportedAgentVersion": str,
        "ReportedOs": ClientDescribeInstancesResponseInstancesReportedOsTypeDef,
        "RootDeviceType": Literal["ebs", "instance-store"],
        "RootDeviceVolumeId": str,
        "SecurityGroupIds": List[str],
        "SshHostDsaKeyFingerprint": str,
        "SshHostRsaKeyFingerprint": str,
        "SshKeyName": str,
        "StackId": str,
        "Status": str,
        "SubnetId": str,
        "Tenancy": str,
        "VirtualizationType": Literal["paravirtual", "hvm"],
    },
    total=False,
)


class ClientDescribeInstancesResponseInstancesTypeDef(
    _ClientDescribeInstancesResponseInstancesTypeDef
):
    """
    - *(dict) --*

      Describes an instance.
      - **AgentVersion** *(string) --*

        The agent version. This parameter is set to ``INHERIT`` if the instance inherits the default
        stack setting or to a a version number for a fixed agent version.
    """


_ClientDescribeInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeInstancesResponseTypeDef",
    {"Instances": List[ClientDescribeInstancesResponseInstancesTypeDef]},
    total=False,
)


class ClientDescribeInstancesResponseTypeDef(_ClientDescribeInstancesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeInstances`` request.
      - **Instances** *(list) --*

        An array of ``Instance`` objects that describe the instances.
        - *(dict) --*

          Describes an instance.
          - **AgentVersion** *(string) --*

            The agent version. This parameter is set to ``INHERIT`` if the instance inherits the
            default stack setting or to a a version number for a fixed agent version.
    """


_ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "_ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": Literal["LOCAL", "UTC"],
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": Literal["start_of_file", "end_of_file"],
        "Encoding": Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "johab",
            "koi8_r",
            "koi8_u",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ],
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)


class ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef(
    _ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef
):
    pass


_ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef = TypedDict(
    "_ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[
            ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef(
    _ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef
):
    pass


_ClientDescribeLayersResponseLayersCustomRecipesTypeDef = TypedDict(
    "_ClientDescribeLayersResponseLayersCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)


class ClientDescribeLayersResponseLayersCustomRecipesTypeDef(
    _ClientDescribeLayersResponseLayersCustomRecipesTypeDef
):
    pass


_ClientDescribeLayersResponseLayersDefaultRecipesTypeDef = TypedDict(
    "_ClientDescribeLayersResponseLayersDefaultRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)


class ClientDescribeLayersResponseLayersDefaultRecipesTypeDef(
    _ClientDescribeLayersResponseLayersDefaultRecipesTypeDef
):
    pass


_ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "_ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)


class ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef(
    _ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef
):
    pass


_ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef = TypedDict(
    "_ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef",
    {"Shutdown": ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)


class ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef(
    _ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef
):
    pass


_ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef = TypedDict(
    "_ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef",
    {
        "MountPoint": str,
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef(
    _ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef
):
    pass


_ClientDescribeLayersResponseLayersTypeDef = TypedDict(
    "_ClientDescribeLayersResponseLayersTypeDef",
    {
        "Arn": str,
        "StackId": str,
        "LayerId": str,
        "Type": Literal[
            "aws-flow-ruby",
            "ecs-cluster",
            "java-app",
            "lb",
            "web",
            "php-app",
            "rails-app",
            "nodejs-app",
            "memcached",
            "db-master",
            "monitoring-master",
            "custom",
        ],
        "Name": str,
        "Shortname": str,
        "Attributes": Dict[str, str],
        "CloudWatchLogsConfiguration": ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef,
        "CustomInstanceProfileArn": str,
        "CustomJson": str,
        "CustomSecurityGroupIds": List[str],
        "DefaultSecurityGroupNames": List[str],
        "Packages": List[str],
        "VolumeConfigurations": List[ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef],
        "EnableAutoHealing": bool,
        "AutoAssignElasticIps": bool,
        "AutoAssignPublicIps": bool,
        "DefaultRecipes": ClientDescribeLayersResponseLayersDefaultRecipesTypeDef,
        "CustomRecipes": ClientDescribeLayersResponseLayersCustomRecipesTypeDef,
        "CreatedAt": str,
        "InstallUpdatesOnBoot": bool,
        "UseEbsOptimizedInstances": bool,
        "LifecycleEventConfiguration": ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeLayersResponseLayersTypeDef(_ClientDescribeLayersResponseLayersTypeDef):
    """
    - *(dict) --*

      Describes a layer.
      - **Arn** *(string) --*

        The Amazon Resource Number (ARN) of a layer.
    """


_ClientDescribeLayersResponseTypeDef = TypedDict(
    "_ClientDescribeLayersResponseTypeDef",
    {"Layers": List[ClientDescribeLayersResponseLayersTypeDef]},
    total=False,
)


class ClientDescribeLayersResponseTypeDef(_ClientDescribeLayersResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeLayers`` request.
      - **Layers** *(list) --*

        An array of ``Layer`` objects that describe the layers.
        - *(dict) --*

          Describes a layer.
          - **Arn** *(string) --*

            The Amazon Resource Number (ARN) of a layer.
    """


_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef = TypedDict(
    "_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)


class ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef(
    _ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef
):
    pass


_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef = TypedDict(
    "_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)


class ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef(
    _ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef
):
    pass


_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef = TypedDict(
    "_ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef",
    {
        "LayerId": str,
        "Enable": bool,
        "UpScaling": ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef,
        "DownScaling": ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef,
    },
    total=False,
)


class ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef(
    _ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef
):
    """
    - *(dict) --*

      Describes a layer's load-based auto scaling configuration.
      - **LayerId** *(string) --*

        The layer ID.
    """


_ClientDescribeLoadBasedAutoScalingResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBasedAutoScalingResponseTypeDef",
    {
        "LoadBasedAutoScalingConfigurations": List[
            ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeLoadBasedAutoScalingResponseTypeDef(
    _ClientDescribeLoadBasedAutoScalingResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a ``DescribeLoadBasedAutoScaling`` request.
      - **LoadBasedAutoScalingConfigurations** *(list) --*

        An array of ``LoadBasedAutoScalingConfiguration`` objects that describe each layer's
        configuration.
        - *(dict) --*

          Describes a layer's load-based auto scaling configuration.
          - **LayerId** *(string) --*

            The layer ID.
    """


_ClientDescribeMyUserProfileResponseUserProfileTypeDef = TypedDict(
    "_ClientDescribeMyUserProfileResponseUserProfileTypeDef",
    {"IamUserArn": str, "Name": str, "SshUsername": str, "SshPublicKey": str},
    total=False,
)


class ClientDescribeMyUserProfileResponseUserProfileTypeDef(
    _ClientDescribeMyUserProfileResponseUserProfileTypeDef
):
    """
    - **UserProfile** *(dict) --*

      A ``UserProfile`` object that describes the user's SSH information.
      - **IamUserArn** *(string) --*

        The user's IAM ARN.
    """


_ClientDescribeMyUserProfileResponseTypeDef = TypedDict(
    "_ClientDescribeMyUserProfileResponseTypeDef",
    {"UserProfile": ClientDescribeMyUserProfileResponseUserProfileTypeDef},
    total=False,
)


class ClientDescribeMyUserProfileResponseTypeDef(_ClientDescribeMyUserProfileResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeMyUserProfile`` request.
      - **UserProfile** *(dict) --*

        A ``UserProfile`` object that describes the user's SSH information.
        - **IamUserArn** *(string) --*

          The user's IAM ARN.
    """


_ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef = TypedDict(
    "_ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef(
    _ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef
):
    pass


_ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef = TypedDict(
    "_ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": str,
        "ConfigurationManagers": List[
            ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef
        ],
        "ReportedName": str,
        "ReportedVersion": str,
        "Supported": bool,
    },
    total=False,
)


class ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef(
    _ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef
):
    """
    - *(dict) --*

      Describes supported operating systems in AWS OpsWorks Stacks.
      - **Name** *(string) --*

        The name of the operating system, such as ``Amazon Linux 2018.03`` .
    """


_ClientDescribeOperatingSystemsResponseTypeDef = TypedDict(
    "_ClientDescribeOperatingSystemsResponseTypeDef",
    {"OperatingSystems": List[ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef]},
    total=False,
)


class ClientDescribeOperatingSystemsResponseTypeDef(_ClientDescribeOperatingSystemsResponseTypeDef):
    """
    - *(dict) --*

      The response to a ``DescribeOperatingSystems`` request.
      - **OperatingSystems** *(list) --*

        Contains information in response to a ``DescribeOperatingSystems`` request.
        - *(dict) --*

          Describes supported operating systems in AWS OpsWorks Stacks.
          - **Name** *(string) --*

            The name of the operating system, such as ``Amazon Linux 2018.03`` .
    """


_ClientDescribePermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientDescribePermissionsResponsePermissionsTypeDef",
    {"StackId": str, "IamUserArn": str, "AllowSsh": bool, "AllowSudo": bool, "Level": str},
    total=False,
)


class ClientDescribePermissionsResponsePermissionsTypeDef(
    _ClientDescribePermissionsResponsePermissionsTypeDef
):
    """
    - *(dict) --*

      Describes stack or user permissions.
      - **StackId** *(string) --*

        A stack ID.
    """


_ClientDescribePermissionsResponseTypeDef = TypedDict(
    "_ClientDescribePermissionsResponseTypeDef",
    {"Permissions": List[ClientDescribePermissionsResponsePermissionsTypeDef]},
    total=False,
)


class ClientDescribePermissionsResponseTypeDef(_ClientDescribePermissionsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribePermissions`` request.
      - **Permissions** *(list) --*

        An array of ``Permission`` objects that describe the stack permissions.
        * If the request object contains only a stack ID, the array contains a ``Permission`` object
        with permissions for each of the stack IAM ARNs.
        * If the request object contains only an IAM ARN, the array contains a ``Permission`` object
        with permissions for each of the user's stack IDs.
        * If the request contains a stack ID and an IAM ARN, the array contains a single
        ``Permission`` object with permissions for the specified stack and IAM ARN.
        - *(dict) --*

          Describes stack or user permissions.
          - **StackId** *(string) --*

            A stack ID.
    """


_ClientDescribeRaidArraysResponseRaidArraysTypeDef = TypedDict(
    "_ClientDescribeRaidArraysResponseRaidArraysTypeDef",
    {
        "RaidArrayId": str,
        "InstanceId": str,
        "Name": str,
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "AvailabilityZone": str,
        "CreatedAt": str,
        "StackId": str,
        "VolumeType": str,
        "Iops": int,
    },
    total=False,
)


class ClientDescribeRaidArraysResponseRaidArraysTypeDef(
    _ClientDescribeRaidArraysResponseRaidArraysTypeDef
):
    """
    - *(dict) --*

      Describes an instance's RAID array.
      - **RaidArrayId** *(string) --*

        The array ID.
    """


_ClientDescribeRaidArraysResponseTypeDef = TypedDict(
    "_ClientDescribeRaidArraysResponseTypeDef",
    {"RaidArrays": List[ClientDescribeRaidArraysResponseRaidArraysTypeDef]},
    total=False,
)


class ClientDescribeRaidArraysResponseTypeDef(_ClientDescribeRaidArraysResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeRaidArrays`` request.
      - **RaidArrays** *(list) --*

        A ``RaidArrays`` object that describes the specified RAID arrays.
        - *(dict) --*

          Describes an instance's RAID array.
          - **RaidArrayId** *(string) --*

            The array ID.
    """


_ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef = TypedDict(
    "_ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef",
    {
        "RdsDbInstanceArn": str,
        "DbInstanceIdentifier": str,
        "DbUser": str,
        "DbPassword": str,
        "Region": str,
        "Address": str,
        "Engine": str,
        "StackId": str,
        "MissingOnRds": bool,
    },
    total=False,
)


class ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef(
    _ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef
):
    """
    - *(dict) --*

      Describes an Amazon RDS instance.
      - **RdsDbInstanceArn** *(string) --*

        The instance's ARN.
    """


_ClientDescribeRdsDbInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeRdsDbInstancesResponseTypeDef",
    {"RdsDbInstances": List[ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef]},
    total=False,
)


class ClientDescribeRdsDbInstancesResponseTypeDef(_ClientDescribeRdsDbInstancesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeRdsDbInstances`` request.
      - **RdsDbInstances** *(list) --*

        An a array of ``RdsDbInstance`` objects that describe the instances.
        - *(dict) --*

          Describes an Amazon RDS instance.
          - **RdsDbInstanceArn** *(string) --*

            The instance's ARN.
    """


_ClientDescribeServiceErrorsResponseServiceErrorsTypeDef = TypedDict(
    "_ClientDescribeServiceErrorsResponseServiceErrorsTypeDef",
    {
        "ServiceErrorId": str,
        "StackId": str,
        "InstanceId": str,
        "Type": str,
        "Message": str,
        "CreatedAt": str,
    },
    total=False,
)


class ClientDescribeServiceErrorsResponseServiceErrorsTypeDef(
    _ClientDescribeServiceErrorsResponseServiceErrorsTypeDef
):
    """
    - *(dict) --*

      Describes an AWS OpsWorks Stacks service error.
      - **ServiceErrorId** *(string) --*

        The error ID.
    """


_ClientDescribeServiceErrorsResponseTypeDef = TypedDict(
    "_ClientDescribeServiceErrorsResponseTypeDef",
    {"ServiceErrors": List[ClientDescribeServiceErrorsResponseServiceErrorsTypeDef]},
    total=False,
)


class ClientDescribeServiceErrorsResponseTypeDef(_ClientDescribeServiceErrorsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeServiceErrors`` request.
      - **ServiceErrors** *(list) --*

        An array of ``ServiceError`` objects that describe the specified service errors.
        - *(dict) --*

          Describes an AWS OpsWorks Stacks service error.
          - **ServiceErrorId** *(string) --*

            The error ID.
    """


_ClientDescribeStackProvisioningParametersResponseTypeDef = TypedDict(
    "_ClientDescribeStackProvisioningParametersResponseTypeDef",
    {"AgentInstallerUrl": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientDescribeStackProvisioningParametersResponseTypeDef(
    _ClientDescribeStackProvisioningParametersResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a ``DescribeStackProvisioningParameters`` request.
      - **AgentInstallerUrl** *(string) --*

        The AWS OpsWorks Stacks agent installer's URL.
    """


_ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef = TypedDict(
    "_ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef",
    {
        "Assigning": int,
        "Booting": int,
        "ConnectionLost": int,
        "Deregistering": int,
        "Online": int,
        "Pending": int,
        "Rebooting": int,
        "Registered": int,
        "Registering": int,
        "Requested": int,
        "RunningSetup": int,
        "SetupFailed": int,
        "ShuttingDown": int,
        "StartFailed": int,
        "StopFailed": int,
        "Stopped": int,
        "Stopping": int,
        "Terminated": int,
        "Terminating": int,
        "Unassigning": int,
    },
    total=False,
)


class ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef(
    _ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef
):
    pass


_ClientDescribeStackSummaryResponseStackSummaryTypeDef = TypedDict(
    "_ClientDescribeStackSummaryResponseStackSummaryTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "LayersCount": int,
        "AppsCount": int,
        "InstancesCount": ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef,
    },
    total=False,
)


class ClientDescribeStackSummaryResponseStackSummaryTypeDef(
    _ClientDescribeStackSummaryResponseStackSummaryTypeDef
):
    """
    - **StackSummary** *(dict) --*

      A ``StackSummary`` object that contains the results.
      - **StackId** *(string) --*

        The stack ID.
    """


_ClientDescribeStackSummaryResponseTypeDef = TypedDict(
    "_ClientDescribeStackSummaryResponseTypeDef",
    {"StackSummary": ClientDescribeStackSummaryResponseStackSummaryTypeDef},
    total=False,
)


class ClientDescribeStackSummaryResponseTypeDef(_ClientDescribeStackSummaryResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeStackSummary`` request.
      - **StackSummary** *(dict) --*

        A ``StackSummary`` object that contains the results.
        - **StackId** *(string) --*

          The stack ID.
    """


_ClientDescribeStacksResponseStacksChefConfigurationTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ClientDescribeStacksResponseStacksChefConfigurationTypeDef(
    _ClientDescribeStacksResponseStacksChefConfigurationTypeDef
):
    pass


_ClientDescribeStacksResponseStacksConfigurationManagerTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribeStacksResponseStacksConfigurationManagerTypeDef(
    _ClientDescribeStacksResponseStacksConfigurationManagerTypeDef
):
    pass


_ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef(
    _ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef
):
    pass


_ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "Region": str,
        "VpcId": str,
        "Attributes": Dict[str, str],
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "DefaultOs": str,
        "HostnameTheme": str,
        "DefaultAvailabilityZone": str,
        "DefaultSubnetId": str,
        "CustomJson": str,
        "ConfigurationManager": ClientDescribeStacksResponseStacksConfigurationManagerTypeDef,
        "ChefConfiguration": ClientDescribeStacksResponseStacksChefConfigurationTypeDef,
        "UseCustomCookbooks": bool,
        "UseOpsworksSecurityGroups": bool,
        "CustomCookbooksSource": ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef,
        "DefaultSshKeyName": str,
        "CreatedAt": str,
        "DefaultRootDeviceType": Literal["ebs", "instance-store"],
        "AgentVersion": str,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksTypeDef(_ClientDescribeStacksResponseStacksTypeDef):
    """
    - *(dict) --*

      Describes a stack.
      - **StackId** *(string) --*

        The stack ID.
    """


_ClientDescribeStacksResponseTypeDef = TypedDict(
    "_ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef]},
    total=False,
)


class ClientDescribeStacksResponseTypeDef(_ClientDescribeStacksResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeStacks`` request.
      - **Stacks** *(list) --*

        An array of ``Stack`` objects that describe the stacks.
        - *(dict) --*

          Describes a stack.
          - **StackId** *(string) --*

            The stack ID.
    """


_ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef = TypedDict(
    "_ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef",
    {
        "Monday": Dict[str, str],
        "Tuesday": Dict[str, str],
        "Wednesday": Dict[str, str],
        "Thursday": Dict[str, str],
        "Friday": Dict[str, str],
        "Saturday": Dict[str, str],
        "Sunday": Dict[str, str],
    },
    total=False,
)


class ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef(
    _ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef
):
    pass


_ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef = TypedDict(
    "_ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef",
    {
        "InstanceId": str,
        "AutoScalingSchedule": ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef,
    },
    total=False,
)


class ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef(
    _ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef
):
    """
    - *(dict) --*

      Describes an instance's time-based auto scaling configuration.
      - **InstanceId** *(string) --*

        The instance ID.
    """


_ClientDescribeTimeBasedAutoScalingResponseTypeDef = TypedDict(
    "_ClientDescribeTimeBasedAutoScalingResponseTypeDef",
    {
        "TimeBasedAutoScalingConfigurations": List[
            ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeTimeBasedAutoScalingResponseTypeDef(
    _ClientDescribeTimeBasedAutoScalingResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a ``DescribeTimeBasedAutoScaling`` request.
      - **TimeBasedAutoScalingConfigurations** *(list) --*

        An array of ``TimeBasedAutoScalingConfiguration`` objects that describe the configuration
        for the specified instances.
        - *(dict) --*

          Describes an instance's time-based auto scaling configuration.
          - **InstanceId** *(string) --*

            The instance ID.
    """


_ClientDescribeUserProfilesResponseUserProfilesTypeDef = TypedDict(
    "_ClientDescribeUserProfilesResponseUserProfilesTypeDef",
    {
        "IamUserArn": str,
        "Name": str,
        "SshUsername": str,
        "SshPublicKey": str,
        "AllowSelfManagement": bool,
    },
    total=False,
)


class ClientDescribeUserProfilesResponseUserProfilesTypeDef(
    _ClientDescribeUserProfilesResponseUserProfilesTypeDef
):
    """
    - *(dict) --*

      Describes a user's SSH information.
      - **IamUserArn** *(string) --*

        The user's IAM ARN.
    """


_ClientDescribeUserProfilesResponseTypeDef = TypedDict(
    "_ClientDescribeUserProfilesResponseTypeDef",
    {"UserProfiles": List[ClientDescribeUserProfilesResponseUserProfilesTypeDef]},
    total=False,
)


class ClientDescribeUserProfilesResponseTypeDef(_ClientDescribeUserProfilesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeUserProfiles`` request.
      - **UserProfiles** *(list) --*

        A ``Users`` object that describes the specified users.
        - *(dict) --*

          Describes a user's SSH information.
          - **IamUserArn** *(string) --*

            The user's IAM ARN.
    """


_ClientDescribeVolumesResponseVolumesTypeDef = TypedDict(
    "_ClientDescribeVolumesResponseVolumesTypeDef",
    {
        "VolumeId": str,
        "Ec2VolumeId": str,
        "Name": str,
        "RaidArrayId": str,
        "InstanceId": str,
        "Status": str,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "Region": str,
        "AvailabilityZone": str,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class ClientDescribeVolumesResponseVolumesTypeDef(_ClientDescribeVolumesResponseVolumesTypeDef):
    """
    - *(dict) --*

      Describes an instance's Amazon EBS volume.
      - **VolumeId** *(string) --*

        The volume ID.
    """


_ClientDescribeVolumesResponseTypeDef = TypedDict(
    "_ClientDescribeVolumesResponseTypeDef",
    {"Volumes": List[ClientDescribeVolumesResponseVolumesTypeDef]},
    total=False,
)


class ClientDescribeVolumesResponseTypeDef(_ClientDescribeVolumesResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeVolumes`` request.
      - **Volumes** *(list) --*

        An array of volume IDs.
        - *(dict) --*

          Describes an instance's Amazon EBS volume.
          - **VolumeId** *(string) --*

            The volume ID.
    """


_ClientGetHostnameSuggestionResponseTypeDef = TypedDict(
    "_ClientGetHostnameSuggestionResponseTypeDef", {"LayerId": str, "Hostname": str}, total=False
)


class ClientGetHostnameSuggestionResponseTypeDef(_ClientGetHostnameSuggestionResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``GetHostnameSuggestion`` request.
      - **LayerId** *(string) --*

        The layer ID.
    """


_ClientGrantAccessResponseTemporaryCredentialTypeDef = TypedDict(
    "_ClientGrantAccessResponseTemporaryCredentialTypeDef",
    {"Username": str, "Password": str, "ValidForInMinutes": int, "InstanceId": str},
    total=False,
)


class ClientGrantAccessResponseTemporaryCredentialTypeDef(
    _ClientGrantAccessResponseTemporaryCredentialTypeDef
):
    """
    - **TemporaryCredential** *(dict) --*

      A ``TemporaryCredential`` object that contains the data needed to log in to the instance by
      RDP clients, such as the Microsoft Remote Desktop Connection.
      - **Username** *(string) --*

        The user name.
    """


_ClientGrantAccessResponseTypeDef = TypedDict(
    "_ClientGrantAccessResponseTypeDef",
    {"TemporaryCredential": ClientGrantAccessResponseTemporaryCredentialTypeDef},
    total=False,
)


class ClientGrantAccessResponseTypeDef(_ClientGrantAccessResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``GrantAccess`` request.
      - **TemporaryCredential** *(dict) --*

        A ``TemporaryCredential`` object that contains the data needed to log in to the instance by
        RDP clients, such as the Microsoft Remote Desktop Connection.
        - **Username** *(string) --*

          The user name.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef", {"Tags": Dict[str, str], "NextToken": str}, total=False
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``ListTags`` request.
      - **Tags** *(dict) --*

        A set of key-value pairs that contain tag keys and tag values that are attached to a stack
        or layer.
        - *(string) --*

          - *(string) --*
    """


_ClientRegisterEcsClusterResponseTypeDef = TypedDict(
    "_ClientRegisterEcsClusterResponseTypeDef", {"EcsClusterArn": str}, total=False
)


class ClientRegisterEcsClusterResponseTypeDef(_ClientRegisterEcsClusterResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``RegisterEcsCluster`` request.
      - **EcsClusterArn** *(string) --*

        The cluster's ARN.
    """


_ClientRegisterElasticIpResponseTypeDef = TypedDict(
    "_ClientRegisterElasticIpResponseTypeDef", {"ElasticIp": str}, total=False
)


class ClientRegisterElasticIpResponseTypeDef(_ClientRegisterElasticIpResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``RegisterElasticIp`` request.
      - **ElasticIp** *(string) --*

        The Elastic IP address.
    """


_ClientRegisterInstanceInstanceIdentityTypeDef = TypedDict(
    "_ClientRegisterInstanceInstanceIdentityTypeDef",
    {"Document": str, "Signature": str},
    total=False,
)


class ClientRegisterInstanceInstanceIdentityTypeDef(_ClientRegisterInstanceInstanceIdentityTypeDef):
    """
    An InstanceIdentity object that contains the instance's identity.
    - **Document** *(string) --*

      A JSON document that contains the metadata.
    """


_ClientRegisterInstanceResponseTypeDef = TypedDict(
    "_ClientRegisterInstanceResponseTypeDef", {"InstanceId": str}, total=False
)


class ClientRegisterInstanceResponseTypeDef(_ClientRegisterInstanceResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``RegisterInstanceResult`` request.
      - **InstanceId** *(string) --*

        The registered instance's AWS OpsWorks Stacks ID.
    """


_ClientRegisterVolumeResponseTypeDef = TypedDict(
    "_ClientRegisterVolumeResponseTypeDef", {"VolumeId": str}, total=False
)


class ClientRegisterVolumeResponseTypeDef(_ClientRegisterVolumeResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``RegisterVolume`` request.
      - **VolumeId** *(string) --*

        The volume ID.
    """


_ClientSetLoadBasedAutoScalingDownScalingTypeDef = TypedDict(
    "_ClientSetLoadBasedAutoScalingDownScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)


class ClientSetLoadBasedAutoScalingDownScalingTypeDef(
    _ClientSetLoadBasedAutoScalingDownScalingTypeDef
):
    """
    An ``AutoScalingThresholds`` object with the downscaling threshold configuration. If the load
    falls below these thresholds for a specified amount of time, AWS OpsWorks Stacks stops a
    specified number of instances.
    - **InstanceCount** *(integer) --*

      The number of instances to add or remove when the load exceeds a threshold.
    """


_ClientSetLoadBasedAutoScalingUpScalingTypeDef = TypedDict(
    "_ClientSetLoadBasedAutoScalingUpScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)


class ClientSetLoadBasedAutoScalingUpScalingTypeDef(_ClientSetLoadBasedAutoScalingUpScalingTypeDef):
    """
    An ``AutoScalingThresholds`` object with the upscaling threshold configuration. If the load
    exceeds these thresholds for a specified amount of time, AWS OpsWorks Stacks starts a specified
    number of instances.
    - **InstanceCount** *(integer) --*

      The number of instances to add or remove when the load exceeds a threshold.
    """


_ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef = TypedDict(
    "_ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef",
    {
        "Monday": Dict[str, str],
        "Tuesday": Dict[str, str],
        "Wednesday": Dict[str, str],
        "Thursday": Dict[str, str],
        "Friday": Dict[str, str],
        "Saturday": Dict[str, str],
        "Sunday": Dict[str, str],
    },
    total=False,
)


class ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef(
    _ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef
):
    """
    An ``AutoScalingSchedule`` with the instance schedule.
    - **Monday** *(dict) --*

      The schedule for Monday.
      - *(string) --*

        - *(string) --*
    """


_ClientUpdateAppAppSourceTypeDef = TypedDict(
    "_ClientUpdateAppAppSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientUpdateAppAppSourceTypeDef(_ClientUpdateAppAppSourceTypeDef):
    """
    A ``Source`` object that specifies the app repository.
    - **Type** *(string) --*

      The repository type.
    """


_ClientUpdateAppDataSourcesTypeDef = TypedDict(
    "_ClientUpdateAppDataSourcesTypeDef",
    {"Type": str, "Arn": str, "DatabaseName": str},
    total=False,
)


class ClientUpdateAppDataSourcesTypeDef(_ClientUpdateAppDataSourcesTypeDef):
    """
    - *(dict) --*

      Describes an app's data source.
      - **Type** *(string) --*

        The data source's type, ``AutoSelectOpsworksMysqlInstance`` , ``OpsworksMysqlInstance`` ,
        ``RdsDbInstance`` , or ``None`` .
    """


_ClientUpdateAppEnvironmentTypeDef = TypedDict(
    "_ClientUpdateAppEnvironmentTypeDef", {"Key": str, "Value": str, "Secure": bool}, total=False
)


class ClientUpdateAppEnvironmentTypeDef(_ClientUpdateAppEnvironmentTypeDef):
    pass


_RequiredClientUpdateAppSslConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateAppSslConfigurationTypeDef", {"Certificate": str}
)
_OptionalClientUpdateAppSslConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateAppSslConfigurationTypeDef",
    {"PrivateKey": str, "Chain": str},
    total=False,
)


class ClientUpdateAppSslConfigurationTypeDef(
    _RequiredClientUpdateAppSslConfigurationTypeDef, _OptionalClientUpdateAppSslConfigurationTypeDef
):
    """
    An ``SslConfiguration`` object with the SSL configuration.
    - **Certificate** *(string) --***[REQUIRED]**

      The contents of the certificate's domain.crt file.
    """


_ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "_ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": Literal["LOCAL", "UTC"],
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": Literal["start_of_file", "end_of_file"],
        "Encoding": Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "johab",
            "koi8_r",
            "koi8_u",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ],
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)


class ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef(
    _ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef
):
    pass


_ClientUpdateLayerCloudWatchLogsConfigurationTypeDef = TypedDict(
    "_ClientUpdateLayerCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef],
    },
    total=False,
)


class ClientUpdateLayerCloudWatchLogsConfigurationTypeDef(
    _ClientUpdateLayerCloudWatchLogsConfigurationTypeDef
):
    """
    Specifies CloudWatch Logs configuration options for the layer. For more information, see
    CloudWatchLogsLogStream .
    - **Enabled** *(boolean) --*

      Whether CloudWatch Logs is enabled for a layer.
    """


_ClientUpdateLayerCustomRecipesTypeDef = TypedDict(
    "_ClientUpdateLayerCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)


class ClientUpdateLayerCustomRecipesTypeDef(_ClientUpdateLayerCustomRecipesTypeDef):
    """
    A ``LayerCustomRecipes`` object that specifies the layer's custom recipes.
    - **Setup** *(list) --*

      An array of custom recipe names to be run following a ``setup`` event.
      - *(string) --*
    """


_ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "_ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)


class ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef(
    _ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef
):
    """
    - **Shutdown** *(dict) --*

      A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.
      - **ExecutionTimeout** *(integer) --*

        The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
        before shutting down an instance.
    """


_ClientUpdateLayerLifecycleEventConfigurationTypeDef = TypedDict(
    "_ClientUpdateLayerLifecycleEventConfigurationTypeDef",
    {"Shutdown": ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)


class ClientUpdateLayerLifecycleEventConfigurationTypeDef(
    _ClientUpdateLayerLifecycleEventConfigurationTypeDef
):
    """
    - **Shutdown** *(dict) --*

      A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.
      - **ExecutionTimeout** *(integer) --*

        The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
        before shutting down an instance.
    """


_RequiredClientUpdateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_RequiredClientUpdateLayerVolumeConfigurationsTypeDef", {"MountPoint": str}
)
_OptionalClientUpdateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_OptionalClientUpdateLayerVolumeConfigurationsTypeDef",
    {
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class ClientUpdateLayerVolumeConfigurationsTypeDef(
    _RequiredClientUpdateLayerVolumeConfigurationsTypeDef,
    _OptionalClientUpdateLayerVolumeConfigurationsTypeDef,
):
    """
    - *(dict) --*

      Describes an Amazon EBS volume configuration.
      - **MountPoint** *(string) --***[REQUIRED]**

        The volume mount point. For example "/dev/sdh".
    """


_ClientUpdateStackChefConfigurationTypeDef = TypedDict(
    "_ClientUpdateStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ClientUpdateStackChefConfigurationTypeDef(_ClientUpdateStackChefConfigurationTypeDef):
    """
    A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf
    version on Chef 11.10 stacks. For more information, see `Create a New Stack
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .
    - **ManageBerkshelf** *(boolean) --*

      Whether to enable Berkshelf.
    """


_ClientUpdateStackConfigurationManagerTypeDef = TypedDict(
    "_ClientUpdateStackConfigurationManagerTypeDef", {"Name": str, "Version": str}, total=False
)


class ClientUpdateStackConfigurationManagerTypeDef(_ClientUpdateStackConfigurationManagerTypeDef):
    """
    The configuration manager. When you update a stack, we recommend that you use the configuration
    manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows
    stacks. The default value for Linux stacks is currently 12.
    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".
    """


_ClientUpdateStackCustomCookbooksSourceTypeDef = TypedDict(
    "_ClientUpdateStackCustomCookbooksSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ClientUpdateStackCustomCookbooksSourceTypeDef(_ClientUpdateStackCustomCookbooksSourceTypeDef):
    """
    Contains the information required to retrieve an app or cookbook from a repository. For more
    information, see `Adding Apps
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
    `Cookbooks and Recipes
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .
    - **Type** *(string) --*

      The repository type.
    """


_DeploymentSuccessfulWaitWaiterConfigTypeDef = TypedDict(
    "_DeploymentSuccessfulWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class DeploymentSuccessfulWaitWaiterConfigTypeDef(_DeploymentSuccessfulWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_DescribeEcsClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEcsClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEcsClustersPaginatePaginationConfigTypeDef(
    _DescribeEcsClustersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEcsClustersPaginateResponseEcsClustersTypeDef = TypedDict(
    "_DescribeEcsClustersPaginateResponseEcsClustersTypeDef",
    {"EcsClusterArn": str, "EcsClusterName": str, "StackId": str, "RegisteredAt": str},
    total=False,
)


class DescribeEcsClustersPaginateResponseEcsClustersTypeDef(
    _DescribeEcsClustersPaginateResponseEcsClustersTypeDef
):
    """
    - *(dict) --*

      Describes a registered Amazon ECS cluster.
      - **EcsClusterArn** *(string) --*

        The cluster's ARN.
    """


_DescribeEcsClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeEcsClustersPaginateResponseTypeDef",
    {"EcsClusters": List[DescribeEcsClustersPaginateResponseEcsClustersTypeDef]},
    total=False,
)


class DescribeEcsClustersPaginateResponseTypeDef(_DescribeEcsClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``DescribeEcsClusters`` request.
      - **EcsClusters** *(list) --*

        A list of ``EcsCluster`` objects containing the cluster descriptions.
        - *(dict) --*

          Describes a registered Amazon ECS cluster.
          - **EcsClusterArn** *(string) --*

            The cluster's ARN.
    """


_InstanceOnlineWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceOnlineWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class InstanceOnlineWaitWaiterConfigTypeDef(_InstanceOnlineWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_InstanceRegisteredWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceRegisteredWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class InstanceRegisteredWaitWaiterConfigTypeDef(_InstanceRegisteredWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_InstanceStoppedWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceStoppedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class InstanceStoppedWaitWaiterConfigTypeDef(_InstanceStoppedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_InstanceTerminatedWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceTerminatedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class InstanceTerminatedWaitWaiterConfigTypeDef(_InstanceTerminatedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15
    """


_ServiceResourceCreateStackChefConfigurationTypeDef = TypedDict(
    "_ServiceResourceCreateStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)


class ServiceResourceCreateStackChefConfigurationTypeDef(
    _ServiceResourceCreateStackChefConfigurationTypeDef
):
    """
    A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf
    version on Chef 11.10 stacks. For more information, see `Create a New Stack
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .
    - **ManageBerkshelf** *(boolean) --*

      Whether to enable Berkshelf.
    """


_ServiceResourceCreateStackConfigurationManagerTypeDef = TypedDict(
    "_ServiceResourceCreateStackConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ServiceResourceCreateStackConfigurationManagerTypeDef(
    _ServiceResourceCreateStackConfigurationManagerTypeDef
):
    """
    The configuration manager. When you create a stack we recommend that you use the configuration
    manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows
    stacks. The default value for Linux stacks is currently 12.
    - **Name** *(string) --*

      The name. This parameter must be set to "Chef".
    """


_ServiceResourceCreateStackCustomCookbooksSourceTypeDef = TypedDict(
    "_ServiceResourceCreateStackCustomCookbooksSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class ServiceResourceCreateStackCustomCookbooksSourceTypeDef(
    _ServiceResourceCreateStackCustomCookbooksSourceTypeDef
):
    """
    Contains the information required to retrieve an app or cookbook from a repository. For more
    information, see `Adding Apps
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or
    `Cookbooks and Recipes
    <https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .
    - **Type** *(string) --*

      The repository type.
    """


_StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "_StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": Literal["LOCAL", "UTC"],
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": Literal["start_of_file", "end_of_file"],
        "Encoding": Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "johab",
            "koi8_r",
            "koi8_u",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ],
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)


class StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef(
    _StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef
):
    pass


_StackCreateLayerCloudWatchLogsConfigurationTypeDef = TypedDict(
    "_StackCreateLayerCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[StackCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef],
    },
    total=False,
)


class StackCreateLayerCloudWatchLogsConfigurationTypeDef(
    _StackCreateLayerCloudWatchLogsConfigurationTypeDef
):
    """
    Specifies CloudWatch Logs configuration options for the layer. For more information, see
    CloudWatchLogsLogStream .
    - **Enabled** *(boolean) --*

      Whether CloudWatch Logs is enabled for a layer.
    """


_StackCreateLayerCustomRecipesTypeDef = TypedDict(
    "_StackCreateLayerCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)


class StackCreateLayerCustomRecipesTypeDef(_StackCreateLayerCustomRecipesTypeDef):
    """
    A ``LayerCustomRecipes`` object that specifies the layer custom recipes.
    - **Setup** *(list) --*

      An array of custom recipe names to be run following a ``setup`` event.
      - *(string) --*
    """


_StackCreateLayerLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "_StackCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)


class StackCreateLayerLifecycleEventConfigurationShutdownTypeDef(
    _StackCreateLayerLifecycleEventConfigurationShutdownTypeDef
):
    """
    - **Shutdown** *(dict) --*

      A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.
      - **ExecutionTimeout** *(integer) --*

        The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
        before shutting down an instance.
    """


_StackCreateLayerLifecycleEventConfigurationTypeDef = TypedDict(
    "_StackCreateLayerLifecycleEventConfigurationTypeDef",
    {"Shutdown": StackCreateLayerLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)


class StackCreateLayerLifecycleEventConfigurationTypeDef(
    _StackCreateLayerLifecycleEventConfigurationTypeDef
):
    """
    A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to
    specify an execution timeout and enable or disable Elastic Load Balancer connection draining.
    - **Shutdown** *(dict) --*

      A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.
      - **ExecutionTimeout** *(integer) --*

        The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event
        before shutting down an instance.
    """


_RequiredStackCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_RequiredStackCreateLayerVolumeConfigurationsTypeDef", {"MountPoint": str}
)
_OptionalStackCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_OptionalStackCreateLayerVolumeConfigurationsTypeDef",
    {
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class StackCreateLayerVolumeConfigurationsTypeDef(
    _RequiredStackCreateLayerVolumeConfigurationsTypeDef,
    _OptionalStackCreateLayerVolumeConfigurationsTypeDef,
):
    """
    - *(dict) --*

      Describes an Amazon EBS volume configuration.
      - **MountPoint** *(string) --***[REQUIRED]**

        The volume mount point. For example "/dev/sdh".
    """
