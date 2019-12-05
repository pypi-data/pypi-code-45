"Main interface for datapipeline service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_datapipeline.client as client_scope

# pylint: disable=import-self
import mypy_boto3_datapipeline.paginator as paginator_scope
from mypy_boto3_datapipeline.type_defs import (
    ClientActivatePipelineParameterValuesTypeDef,
    ClientAddTagsTagsTypeDef,
    ClientCreatePipelineResponseTypeDef,
    ClientCreatePipelineTagsTypeDef,
    ClientDescribePipelinesResponseTypeDef,
    ClientEvaluateExpressionResponseTypeDef,
    ClientPutPipelineDefinitionParameterObjectsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
from typing import overload
from mypy_boto3_datapipeline.type_defs import (
    ClientDescribeObjectsResponseTypeDef,
    ClientGetPipelineDefinitionResponseTypeDef,
    ClientListPipelinesResponseTypeDef,
    ClientPollForTaskInstanceIdentityTypeDef,
    ClientPollForTaskResponseTypeDef,
    ClientPutPipelineDefinitionParameterValuesTypeDef,
    ClientPutPipelineDefinitionPipelineObjectsTypeDef,
    ClientPutPipelineDefinitionResponseTypeDef,
    ClientQueryObjectsQueryTypeDef,
    ClientQueryObjectsResponseTypeDef,
    ClientReportTaskProgressFieldsTypeDef,
    ClientReportTaskProgressResponseTypeDef,
    ClientReportTaskRunnerHeartbeatResponseTypeDef,
    ClientValidatePipelineDefinitionParameterObjectsTypeDef,
    ClientValidatePipelineDefinitionParameterValuesTypeDef,
    ClientValidatePipelineDefinitionPipelineObjectsTypeDef,
    ClientValidatePipelineDefinitionResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    """
    [DataPipeline.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate_pipeline(
        self,
        pipelineId: str,
        parameterValues: List[ClientActivatePipelineParameterValuesTypeDef] = None,
        startTimestamp: datetime = None,
    ) -> Dict[str, Any]:
        """
        [Client.activate_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.activate_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags(self, pipelineId: str, tags: List[ClientAddTagsTagsTypeDef]) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.add_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_pipeline(
        self,
        name: str,
        uniqueId: str,
        description: str = None,
        tags: List[ClientCreatePipelineTagsTypeDef] = None,
    ) -> ClientCreatePipelineResponseTypeDef:
        """
        [Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.create_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate_pipeline(self, pipelineId: str, cancelActive: bool = None) -> Dict[str, Any]:
        """
        [Client.deactivate_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.deactivate_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_pipeline(self, pipelineId: str) -> None:
        """
        [Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.delete_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_objects(
        self,
        pipelineId: str,
        objectIds: List[str],
        evaluateExpressions: bool = None,
        marker: str = None,
    ) -> ClientDescribeObjectsResponseTypeDef:
        """
        [Client.describe_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.describe_objects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_pipelines(self, pipelineIds: List[str]) -> ClientDescribePipelinesResponseTypeDef:
        """
        [Client.describe_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.describe_pipelines)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def evaluate_expression(
        self, pipelineId: str, objectId: str, expression: str
    ) -> ClientEvaluateExpressionResponseTypeDef:
        """
        [Client.evaluate_expression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.evaluate_expression)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_pipeline_definition(
        self, pipelineId: str, version: str = None
    ) -> ClientGetPipelineDefinitionResponseTypeDef:
        """
        [Client.get_pipeline_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.get_pipeline_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_pipelines(self, marker: str = None) -> ClientListPipelinesResponseTypeDef:
        """
        [Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.list_pipelines)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def poll_for_task(
        self,
        workerGroup: str,
        hostname: str = None,
        instanceIdentity: ClientPollForTaskInstanceIdentityTypeDef = None,
    ) -> ClientPollForTaskResponseTypeDef:
        """
        [Client.poll_for_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.poll_for_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_pipeline_definition(
        self,
        pipelineId: str,
        pipelineObjects: List[ClientPutPipelineDefinitionPipelineObjectsTypeDef],
        parameterObjects: List[ClientPutPipelineDefinitionParameterObjectsTypeDef] = None,
        parameterValues: List[ClientPutPipelineDefinitionParameterValuesTypeDef] = None,
    ) -> ClientPutPipelineDefinitionResponseTypeDef:
        """
        [Client.put_pipeline_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.put_pipeline_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def query_objects(
        self,
        pipelineId: str,
        sphere: str,
        query: ClientQueryObjectsQueryTypeDef = None,
        marker: str = None,
        limit: int = None,
    ) -> ClientQueryObjectsResponseTypeDef:
        """
        [Client.query_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.query_objects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags(self, pipelineId: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.remove_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def report_task_progress(
        self, taskId: str, fields: List[ClientReportTaskProgressFieldsTypeDef] = None
    ) -> ClientReportTaskProgressResponseTypeDef:
        """
        [Client.report_task_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.report_task_progress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def report_task_runner_heartbeat(
        self, taskrunnerId: str, workerGroup: str = None, hostname: str = None
    ) -> ClientReportTaskRunnerHeartbeatResponseTypeDef:
        """
        [Client.report_task_runner_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.report_task_runner_heartbeat)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_status(self, pipelineId: str, objectIds: List[str], status: str) -> None:
        """
        [Client.set_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.set_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_task_status(
        self,
        taskId: str,
        taskStatus: Literal["FINISHED", "FAILED", "FALSE"],
        errorId: str = None,
        errorMessage: str = None,
        errorStackTrace: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.set_task_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.set_task_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def validate_pipeline_definition(
        self,
        pipelineId: str,
        pipelineObjects: List[ClientValidatePipelineDefinitionPipelineObjectsTypeDef],
        parameterObjects: List[ClientValidatePipelineDefinitionParameterObjectsTypeDef] = None,
        parameterValues: List[ClientValidatePipelineDefinitionParameterValuesTypeDef] = None,
    ) -> ClientValidatePipelineDefinitionResponseTypeDef:
        """
        [Client.validate_pipeline_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Client.validate_pipeline_definition)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_objects"]
    ) -> paginator_scope.DescribeObjectsPaginator:
        """
        [Paginator.DescribeObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Paginator.DescribeObjects)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_pipelines"]
    ) -> paginator_scope.ListPipelinesPaginator:
        """
        [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Paginator.ListPipelines)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["query_objects"]
    ) -> paginator_scope.QueryObjectsPaginator:
        """
        [Paginator.QueryObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/datapipeline.html#DataPipeline.Paginator.QueryObjects)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceError: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    PipelineDeletedException: Boto3ClientError
    PipelineNotFoundException: Boto3ClientError
    TaskNotFoundException: Boto3ClientError
