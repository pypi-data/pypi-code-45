"Main interface for datasync service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_datasync.client as client_scope

# pylint: disable=import-self
import mypy_boto3_datasync.paginator as paginator_scope
from mypy_boto3_datasync.type_defs import (
    ClientCreateAgentResponseTypeDef,
    ClientCreateAgentTagsTypeDef,
    ClientCreateLocationEfsEc2ConfigTypeDef,
    ClientCreateLocationEfsResponseTypeDef,
    ClientCreateLocationNfsMountOptionsTypeDef,
    ClientCreateLocationNfsTagsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
from typing import overload
from mypy_boto3_datasync.type_defs import (
    ClientCreateLocationEfsTagsTypeDef,
    ClientCreateLocationNfsOnPremConfigTypeDef,
    ClientCreateLocationNfsResponseTypeDef,
    ClientCreateLocationS3ResponseTypeDef,
    ClientCreateLocationS3S3ConfigTypeDef,
    ClientCreateLocationS3TagsTypeDef,
    ClientCreateLocationSmbMountOptionsTypeDef,
    ClientCreateLocationSmbResponseTypeDef,
    ClientCreateLocationSmbTagsTypeDef,
    ClientCreateTaskExcludesTypeDef,
    ClientCreateTaskOptionsTypeDef,
    ClientCreateTaskResponseTypeDef,
    ClientCreateTaskScheduleTypeDef,
    ClientCreateTaskTagsTypeDef,
    ClientDescribeAgentResponseTypeDef,
    ClientDescribeLocationEfsResponseTypeDef,
    ClientDescribeLocationNfsResponseTypeDef,
    ClientDescribeLocationS3ResponseTypeDef,
    ClientDescribeLocationSmbResponseTypeDef,
    ClientDescribeTaskExecutionResponseTypeDef,
    ClientDescribeTaskResponseTypeDef,
    ClientListAgentsResponseTypeDef,
    ClientListLocationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTaskExecutionsResponseTypeDef,
    ClientListTasksResponseTypeDef,
    ClientStartTaskExecutionIncludesTypeDef,
    ClientStartTaskExecutionOverrideOptionsTypeDef,
    ClientStartTaskExecutionResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateTaskExcludesTypeDef,
    ClientUpdateTaskOptionsTypeDef,
    ClientUpdateTaskScheduleTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    """
    [DataSync.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_task_execution(self, TaskExecutionArn: str) -> Dict[str, Any]:
        """
        [Client.cancel_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.cancel_task_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_agent(
        self,
        ActivationKey: str,
        AgentName: str = None,
        Tags: List[ClientCreateAgentTagsTypeDef] = None,
        VpcEndpointId: str = None,
        SubnetArns: List[str] = None,
        SecurityGroupArns: List[str] = None,
    ) -> ClientCreateAgentResponseTypeDef:
        """
        [Client.create_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.create_agent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_location_efs(
        self,
        EfsFilesystemArn: str,
        Ec2Config: ClientCreateLocationEfsEc2ConfigTypeDef,
        Subdirectory: str = None,
        Tags: List[ClientCreateLocationEfsTagsTypeDef] = None,
    ) -> ClientCreateLocationEfsResponseTypeDef:
        """
        [Client.create_location_efs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.create_location_efs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_location_nfs(
        self,
        Subdirectory: str,
        ServerHostname: str,
        OnPremConfig: ClientCreateLocationNfsOnPremConfigTypeDef,
        MountOptions: ClientCreateLocationNfsMountOptionsTypeDef = None,
        Tags: List[ClientCreateLocationNfsTagsTypeDef] = None,
    ) -> ClientCreateLocationNfsResponseTypeDef:
        """
        [Client.create_location_nfs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.create_location_nfs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_location_s3(
        self,
        S3BucketArn: str,
        S3Config: ClientCreateLocationS3S3ConfigTypeDef,
        Subdirectory: str = None,
        S3StorageClass: Literal[
            "STANDARD",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        Tags: List[ClientCreateLocationS3TagsTypeDef] = None,
    ) -> ClientCreateLocationS3ResponseTypeDef:
        """
        [Client.create_location_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.create_location_s3)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_location_smb(
        self,
        Subdirectory: str,
        ServerHostname: str,
        User: str,
        Password: str,
        AgentArns: List[str],
        Domain: str = None,
        MountOptions: ClientCreateLocationSmbMountOptionsTypeDef = None,
        Tags: List[ClientCreateLocationSmbTagsTypeDef] = None,
    ) -> ClientCreateLocationSmbResponseTypeDef:
        """
        [Client.create_location_smb documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.create_location_smb)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_task(
        self,
        SourceLocationArn: str,
        DestinationLocationArn: str,
        CloudWatchLogGroupArn: str = None,
        Name: str = None,
        Options: ClientCreateTaskOptionsTypeDef = None,
        Excludes: List[ClientCreateTaskExcludesTypeDef] = None,
        Schedule: ClientCreateTaskScheduleTypeDef = None,
        Tags: List[ClientCreateTaskTagsTypeDef] = None,
    ) -> ClientCreateTaskResponseTypeDef:
        """
        [Client.create_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.create_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_agent(self, AgentArn: str) -> Dict[str, Any]:
        """
        [Client.delete_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.delete_agent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_location(self, LocationArn: str) -> Dict[str, Any]:
        """
        [Client.delete_location documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.delete_location)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_task(self, TaskArn: str) -> Dict[str, Any]:
        """
        [Client.delete_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.delete_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_agent(self, AgentArn: str) -> ClientDescribeAgentResponseTypeDef:
        """
        [Client.describe_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.describe_agent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_location_efs(self, LocationArn: str) -> ClientDescribeLocationEfsResponseTypeDef:
        """
        [Client.describe_location_efs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.describe_location_efs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_location_nfs(self, LocationArn: str) -> ClientDescribeLocationNfsResponseTypeDef:
        """
        [Client.describe_location_nfs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.describe_location_nfs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_location_s3(self, LocationArn: str) -> ClientDescribeLocationS3ResponseTypeDef:
        """
        [Client.describe_location_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.describe_location_s3)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_location_smb(self, LocationArn: str) -> ClientDescribeLocationSmbResponseTypeDef:
        """
        [Client.describe_location_smb documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.describe_location_smb)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_task(self, TaskArn: str) -> ClientDescribeTaskResponseTypeDef:
        """
        [Client.describe_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.describe_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_task_execution(
        self, TaskExecutionArn: str
    ) -> ClientDescribeTaskExecutionResponseTypeDef:
        """
        [Client.describe_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.describe_task_execution)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_agents(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListAgentsResponseTypeDef:
        """
        [Client.list_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.list_agents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_locations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListLocationsResponseTypeDef:
        """
        [Client.list_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.list_locations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_task_executions(
        self, TaskArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTaskExecutionsResponseTypeDef:
        """
        [Client.list_task_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.list_task_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tasks(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTasksResponseTypeDef:
        """
        [Client.list_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.list_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_task_execution(
        self,
        TaskArn: str,
        OverrideOptions: ClientStartTaskExecutionOverrideOptionsTypeDef = None,
        Includes: List[ClientStartTaskExecutionIncludesTypeDef] = None,
    ) -> ClientStartTaskExecutionResponseTypeDef:
        """
        [Client.start_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.start_task_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, Keys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_agent(self, AgentArn: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.update_agent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_task(
        self,
        TaskArn: str,
        Options: ClientUpdateTaskOptionsTypeDef = None,
        Excludes: List[ClientUpdateTaskExcludesTypeDef] = None,
        Schedule: ClientUpdateTaskScheduleTypeDef = None,
        Name: str = None,
        CloudWatchLogGroupArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Client.update_task)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_agents"]
    ) -> paginator_scope.ListAgentsPaginator:
        """
        [Paginator.ListAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Paginator.ListAgents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_locations"]
    ) -> paginator_scope.ListLocationsPaginator:
        """
        [Paginator.ListLocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Paginator.ListLocations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_task_executions"]
    ) -> paginator_scope.ListTaskExecutionsPaginator:
        """
        [Paginator.ListTaskExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tasks"]
    ) -> paginator_scope.ListTasksPaginator:
        """
        [Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datasync.html#DataSync.Paginator.ListTasks)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
