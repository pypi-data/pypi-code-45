"Main interface for emr service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_emr.client as client_scope

# pylint: disable=import-self
import mypy_boto3_emr.paginator as paginator_scope
from mypy_boto3_emr.type_defs import (
    ClientAddInstanceFleetInstanceFleetTypeDef,
    ClientAddInstanceFleetResponseTypeDef,
    ClientAddInstanceGroupsInstanceGroupsTypeDef,
    ClientAddInstanceGroupsResponseTypeDef,
    ClientAddJobFlowStepsResponseTypeDef,
    ClientAddJobFlowStepsStepsTypeDef,
    ClientAddTagsTagsTypeDef,
    ClientCancelStepsResponseTypeDef,
    ClientCreateSecurityConfigurationResponseTypeDef,
    ClientDescribeClusterResponseTypeDef,
    ClientDescribeJobFlowsResponseTypeDef,
    ClientDescribeSecurityConfigurationResponseTypeDef,
    ClientDescribeStepResponseTypeDef,
    ClientGetBlockPublicAccessConfigurationResponseTypeDef,
    ClientListBootstrapActionsResponseTypeDef,
    ClientListClustersResponseTypeDef,
    ClientListInstanceFleetsResponseTypeDef,
    ClientListInstanceGroupsResponseTypeDef,
    ClientListInstancesResponseTypeDef,
    ClientListSecurityConfigurationsResponseTypeDef,
    ClientListStepsResponseTypeDef,
    ClientModifyClusterResponseTypeDef,
    ClientModifyInstanceFleetInstanceFleetTypeDef,
    ClientModifyInstanceGroupsInstanceGroupsTypeDef,
    ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef,
    ClientPutAutoScalingPolicyResponseTypeDef,
    ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef,
    ClientRunJobFlowApplicationsTypeDef,
    ClientRunJobFlowBootstrapActionsTypeDef,
    ClientRunJobFlowConfigurationsTypeDef,
    ClientRunJobFlowInstancesTypeDef,
    ClientRunJobFlowKerberosAttributesTypeDef,
    ClientRunJobFlowNewSupportedProductsTypeDef,
    ClientRunJobFlowResponseTypeDef,
    ClientRunJobFlowStepsTypeDef,
    ClientRunJobFlowTagsTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_emr.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [EMR.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_instance_fleet(
        self, ClusterId: str, InstanceFleet: ClientAddInstanceFleetInstanceFleetTypeDef
    ) -> ClientAddInstanceFleetResponseTypeDef:
        """
        [Client.add_instance_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.add_instance_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_instance_groups(
        self, InstanceGroups: List[ClientAddInstanceGroupsInstanceGroupsTypeDef], JobFlowId: str
    ) -> ClientAddInstanceGroupsResponseTypeDef:
        """
        [Client.add_instance_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.add_instance_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_job_flow_steps(
        self, JobFlowId: str, Steps: List[ClientAddJobFlowStepsStepsTypeDef]
    ) -> ClientAddJobFlowStepsResponseTypeDef:
        """
        [Client.add_job_flow_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.add_job_flow_steps)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags(self, ResourceId: str, Tags: List[ClientAddTagsTagsTypeDef]) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.add_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_steps(
        self,
        ClusterId: str,
        StepIds: List[str],
        StepCancellationOption: Literal["SEND_INTERRUPT", "TERMINATE_PROCESS"] = None,
    ) -> ClientCancelStepsResponseTypeDef:
        """
        [Client.cancel_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.cancel_steps)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_security_configuration(
        self, Name: str, SecurityConfiguration: str
    ) -> ClientCreateSecurityConfigurationResponseTypeDef:
        """
        [Client.create_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.create_security_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_security_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.delete_security_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster(self, ClusterId: str) -> ClientDescribeClusterResponseTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.describe_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_job_flows(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        JobFlowIds: List[str] = None,
        JobFlowStates: List[
            Literal[
                "STARTING",
                "BOOTSTRAPPING",
                "RUNNING",
                "WAITING",
                "SHUTTING_DOWN",
                "TERMINATED",
                "COMPLETED",
                "FAILED",
            ]
        ] = None,
    ) -> ClientDescribeJobFlowsResponseTypeDef:
        """
        [Client.describe_job_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.describe_job_flows)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_security_configuration(
        self, Name: str
    ) -> ClientDescribeSecurityConfigurationResponseTypeDef:
        """
        [Client.describe_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.describe_security_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_step(self, ClusterId: str, StepId: str) -> ClientDescribeStepResponseTypeDef:
        """
        [Client.describe_step documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.describe_step)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_block_public_access_configuration(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetBlockPublicAccessConfigurationResponseTypeDef:
        """
        [Client.get_block_public_access_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.get_block_public_access_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bootstrap_actions(
        self, ClusterId: str, Marker: str = None
    ) -> ClientListBootstrapActionsResponseTypeDef:
        """
        [Client.list_bootstrap_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.list_bootstrap_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_clusters(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[
            Literal[
                "STARTING",
                "BOOTSTRAPPING",
                "RUNNING",
                "WAITING",
                "TERMINATING",
                "TERMINATED",
                "TERMINATED_WITH_ERRORS",
            ]
        ] = None,
        Marker: str = None,
    ) -> ClientListClustersResponseTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.list_clusters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_instance_fleets(
        self, ClusterId: str, Marker: str = None
    ) -> ClientListInstanceFleetsResponseTypeDef:
        """
        [Client.list_instance_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.list_instance_fleets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_instance_groups(
        self, ClusterId: str, Marker: str = None
    ) -> ClientListInstanceGroupsResponseTypeDef:
        """
        [Client.list_instance_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.list_instance_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_instances(
        self,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[Literal["MASTER", "CORE", "TASK"]] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: Literal["MASTER", "CORE", "TASK"] = None,
        InstanceStates: List[
            Literal[
                "AWAITING_FULFILLMENT", "PROVISIONING", "BOOTSTRAPPING", "RUNNING", "TERMINATED"
            ]
        ] = None,
        Marker: str = None,
    ) -> ClientListInstancesResponseTypeDef:
        """
        [Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.list_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_security_configurations(
        self, Marker: str = None
    ) -> ClientListSecurityConfigurationsResponseTypeDef:
        """
        [Client.list_security_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.list_security_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_steps(
        self,
        ClusterId: str,
        StepStates: List[
            Literal[
                "PENDING",
                "CANCEL_PENDING",
                "RUNNING",
                "COMPLETED",
                "CANCELLED",
                "FAILED",
                "INTERRUPTED",
            ]
        ] = None,
        StepIds: List[str] = None,
        Marker: str = None,
    ) -> ClientListStepsResponseTypeDef:
        """
        [Client.list_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.list_steps)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cluster(
        self, ClusterId: str, StepConcurrencyLevel: int = None
    ) -> ClientModifyClusterResponseTypeDef:
        """
        [Client.modify_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.modify_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_instance_fleet(
        self, ClusterId: str, InstanceFleet: ClientModifyInstanceFleetInstanceFleetTypeDef
    ) -> None:
        """
        [Client.modify_instance_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.modify_instance_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_instance_groups(
        self,
        ClusterId: str = None,
        InstanceGroups: List[ClientModifyInstanceGroupsInstanceGroupsTypeDef] = None,
    ) -> None:
        """
        [Client.modify_instance_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.modify_instance_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_auto_scaling_policy(
        self,
        ClusterId: str,
        InstanceGroupId: str,
        AutoScalingPolicy: ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef,
    ) -> ClientPutAutoScalingPolicyResponseTypeDef:
        """
        [Client.put_auto_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.put_auto_scaling_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_block_public_access_configuration(
        self,
        BlockPublicAccessConfiguration: ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.put_block_public_access_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.put_block_public_access_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_auto_scaling_policy(self, ClusterId: str, InstanceGroupId: str) -> Dict[str, Any]:
        """
        [Client.remove_auto_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.remove_auto_scaling_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.remove_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def run_job_flow(
        self,
        Name: str,
        Instances: ClientRunJobFlowInstancesTypeDef,
        LogUri: str = None,
        AdditionalInfo: str = None,
        AmiVersion: str = None,
        ReleaseLabel: str = None,
        Steps: List[ClientRunJobFlowStepsTypeDef] = None,
        BootstrapActions: List[ClientRunJobFlowBootstrapActionsTypeDef] = None,
        SupportedProducts: List[str] = None,
        NewSupportedProducts: List[ClientRunJobFlowNewSupportedProductsTypeDef] = None,
        Applications: List[ClientRunJobFlowApplicationsTypeDef] = None,
        Configurations: List[ClientRunJobFlowConfigurationsTypeDef] = None,
        VisibleToAllUsers: bool = None,
        JobFlowRole: str = None,
        ServiceRole: str = None,
        Tags: List[ClientRunJobFlowTagsTypeDef] = None,
        SecurityConfiguration: str = None,
        AutoScalingRole: str = None,
        ScaleDownBehavior: Literal[
            "TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"
        ] = None,
        CustomAmiId: str = None,
        EbsRootVolumeSize: int = None,
        RepoUpgradeOnBoot: Literal["SECURITY", "NONE"] = None,
        KerberosAttributes: ClientRunJobFlowKerberosAttributesTypeDef = None,
        StepConcurrencyLevel: int = None,
    ) -> ClientRunJobFlowResponseTypeDef:
        """
        [Client.run_job_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.run_job_flow)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_termination_protection(self, JobFlowIds: List[str], TerminationProtected: bool) -> None:
        """
        [Client.set_termination_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.set_termination_protection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_visible_to_all_users(self, JobFlowIds: List[str], VisibleToAllUsers: bool) -> None:
        """
        [Client.set_visible_to_all_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.set_visible_to_all_users)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate_job_flows(self, JobFlowIds: List[str]) -> None:
        """
        [Client.terminate_job_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Client.terminate_job_flows)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bootstrap_actions"]
    ) -> paginator_scope.ListBootstrapActionsPaginator:
        """
        [Paginator.ListBootstrapActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Paginator.ListBootstrapActions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_clusters"]
    ) -> paginator_scope.ListClustersPaginator:
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Paginator.ListClusters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_instance_fleets"]
    ) -> paginator_scope.ListInstanceFleetsPaginator:
        """
        [Paginator.ListInstanceFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Paginator.ListInstanceFleets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_instance_groups"]
    ) -> paginator_scope.ListInstanceGroupsPaginator:
        """
        [Paginator.ListInstanceGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Paginator.ListInstanceGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_instances"]
    ) -> paginator_scope.ListInstancesPaginator:
        """
        [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Paginator.ListInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_security_configurations"]
    ) -> paginator_scope.ListSecurityConfigurationsPaginator:
        """
        [Paginator.ListSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_steps"]
    ) -> paginator_scope.ListStepsPaginator:
        """
        [Paginator.ListSteps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Paginator.ListSteps)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cluster_running"]
    ) -> waiter_scope.ClusterRunningWaiter:
        """
        [Waiter.ClusterRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Waiter.ClusterRunning)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cluster_terminated"]
    ) -> waiter_scope.ClusterTerminatedWaiter:
        """
        [Waiter.ClusterTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Waiter.ClusterTerminated)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["step_complete"]) -> waiter_scope.StepCompleteWaiter:
        """
        [Waiter.StepComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/emr.html#EMR.Waiter.StepComplete)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerError: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
