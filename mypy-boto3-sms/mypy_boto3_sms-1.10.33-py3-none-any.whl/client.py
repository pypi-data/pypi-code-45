"Main interface for sms service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sms.client as client_scope

# pylint: disable=import-self
import mypy_boto3_sms.paginator as paginator_scope
from mypy_boto3_sms.type_defs import (
    ClientCreateAppResponseTypeDef,
    ClientCreateAppServerGroupsTypeDef,
    ClientCreateAppTagsTypeDef,
    ClientCreateReplicationJobResponseTypeDef,
    ClientGenerateChangeSetResponseTypeDef,
    ClientGenerateTemplateResponseTypeDef,
    ClientGetAppLaunchConfigurationResponseTypeDef,
    ClientGetAppReplicationConfigurationResponseTypeDef,
    ClientGetAppResponseTypeDef,
    ClientGetConnectorsResponseTypeDef,
    ClientGetReplicationJobsResponseTypeDef,
    ClientGetReplicationRunsResponseTypeDef,
    ClientGetServersResponseTypeDef,
    ClientGetServersVmServerAddressListTypeDef,
    ClientListAppsResponseTypeDef,
    ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef,
    ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef,
    ClientStartOnDemandReplicationRunResponseTypeDef,
    ClientUpdateAppResponseTypeDef,
    ClientUpdateAppServerGroupsTypeDef,
    ClientUpdateAppTagsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [SMS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_app(
        self,
        name: str = None,
        description: str = None,
        roleName: str = None,
        clientToken: str = None,
        serverGroups: List[ClientCreateAppServerGroupsTypeDef] = None,
        tags: List[ClientCreateAppTagsTypeDef] = None,
    ) -> ClientCreateAppResponseTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.create_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_replication_job(
        self,
        serverId: str,
        seedReplicationTime: datetime,
        frequency: int = None,
        runOnce: bool = None,
        licenseType: Literal["AWS", "BYOL"] = None,
        roleName: str = None,
        description: str = None,
        numberOfRecentAmisToKeep: int = None,
        encrypted: bool = None,
        kmsKeyId: str = None,
    ) -> ClientCreateReplicationJobResponseTypeDef:
        """
        [Client.create_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.create_replication_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_app(
        self,
        appId: str = None,
        forceStopAppReplication: bool = None,
        forceTerminateApp: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.delete_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_app_launch_configuration(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.delete_app_launch_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_app_replication_configuration(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.delete_app_replication_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_replication_job(self, replicationJobId: str) -> Dict[str, Any]:
        """
        [Client.delete_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.delete_replication_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_server_catalog(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.delete_server_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.delete_server_catalog)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_connector(self, connectorId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.disassociate_connector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_change_set(
        self, appId: str = None, changesetFormat: Literal["JSON", "YAML"] = None
    ) -> ClientGenerateChangeSetResponseTypeDef:
        """
        [Client.generate_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.generate_change_set)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_template(
        self, appId: str = None, templateFormat: Literal["JSON", "YAML"] = None
    ) -> ClientGenerateTemplateResponseTypeDef:
        """
        [Client.generate_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.generate_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_app(self, appId: str = None) -> ClientGetAppResponseTypeDef:
        """
        [Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.get_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_app_launch_configuration(
        self, appId: str = None
    ) -> ClientGetAppLaunchConfigurationResponseTypeDef:
        """
        [Client.get_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.get_app_launch_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_app_replication_configuration(
        self, appId: str = None
    ) -> ClientGetAppReplicationConfigurationResponseTypeDef:
        """
        [Client.get_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.get_app_replication_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connectors(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientGetConnectorsResponseTypeDef:
        """
        [Client.get_connectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.get_connectors)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_replication_jobs(
        self, replicationJobId: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientGetReplicationJobsResponseTypeDef:
        """
        [Client.get_replication_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.get_replication_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_replication_runs(
        self, replicationJobId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientGetReplicationRunsResponseTypeDef:
        """
        [Client.get_replication_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.get_replication_runs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_servers(
        self,
        nextToken: str = None,
        maxResults: int = None,
        vmServerAddressList: List[ClientGetServersVmServerAddressListTypeDef] = None,
    ) -> ClientGetServersResponseTypeDef:
        """
        [Client.get_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.get_servers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_server_catalog(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.import_server_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.import_server_catalog)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def launch_app(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.launch_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.launch_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_apps(
        self, appIds: List[str] = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListAppsResponseTypeDef:
        """
        [Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.list_apps)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_app_launch_configuration(
        self,
        appId: str = None,
        roleName: str = None,
        serverGroupLaunchConfigurations: List[
            ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.put_app_launch_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_app_replication_configuration(
        self,
        appId: str = None,
        serverGroupReplicationConfigurations: List[
            ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.put_app_replication_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_app_replication(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.start_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.start_app_replication)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_on_demand_replication_run(
        self, replicationJobId: str, description: str = None
    ) -> ClientStartOnDemandReplicationRunResponseTypeDef:
        """
        [Client.start_on_demand_replication_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.start_on_demand_replication_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_app_replication(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.stop_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.stop_app_replication)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate_app(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.terminate_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.terminate_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_app(
        self,
        appId: str = None,
        name: str = None,
        description: str = None,
        roleName: str = None,
        serverGroups: List[ClientUpdateAppServerGroupsTypeDef] = None,
        tags: List[ClientUpdateAppTagsTypeDef] = None,
    ) -> ClientUpdateAppResponseTypeDef:
        """
        [Client.update_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.update_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_replication_job(
        self,
        replicationJobId: str,
        frequency: int = None,
        nextReplicationRunStartTime: datetime = None,
        licenseType: Literal["AWS", "BYOL"] = None,
        roleName: str = None,
        description: str = None,
        numberOfRecentAmisToKeep: int = None,
        encrypted: bool = None,
        kmsKeyId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Client.update_replication_job)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_connectors"]
    ) -> paginator_scope.GetConnectorsPaginator:
        """
        [Paginator.GetConnectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.GetConnectors)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_replication_jobs"]
    ) -> paginator_scope.GetReplicationJobsPaginator:
        """
        [Paginator.GetReplicationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.GetReplicationJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_replication_runs"]
    ) -> paginator_scope.GetReplicationRunsPaginator:
        """
        [Paginator.GetReplicationRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.GetReplicationRuns)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_servers"]
    ) -> paginator_scope.GetServersPaginator:
        """
        [Paginator.GetServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.GetServers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_apps"]
    ) -> paginator_scope.ListAppsPaginator:
        """
        [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sms.html#SMS.Paginator.ListApps)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalError: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    MissingRequiredParameterException: Boto3ClientError
    NoConnectorsAvailableException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    ReplicationJobAlreadyExistsException: Boto3ClientError
    ReplicationJobNotFoundException: Boto3ClientError
    ReplicationRunLimitExceededException: Boto3ClientError
    ServerCannotBeReplicatedException: Boto3ClientError
    TemporarilyUnavailableException: Boto3ClientError
    UnauthorizedOperationException: Boto3ClientError
