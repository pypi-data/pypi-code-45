"Main interface for datapipeline service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientActivatePipelineParameterValuesTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCreatePipelineResponseTypeDef",
    "ClientCreatePipelineTagsTypeDef",
    "ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef",
    "ClientDescribeObjectsResponsepipelineObjectsTypeDef",
    "ClientDescribeObjectsResponseTypeDef",
    "ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef",
    "ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef",
    "ClientDescribePipelinesResponsepipelineDescriptionListTypeDef",
    "ClientDescribePipelinesResponseTypeDef",
    "ClientEvaluateExpressionResponseTypeDef",
    "ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef",
    "ClientGetPipelineDefinitionResponseparameterObjectsTypeDef",
    "ClientGetPipelineDefinitionResponseparameterValuesTypeDef",
    "ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef",
    "ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef",
    "ClientGetPipelineDefinitionResponseTypeDef",
    "ClientListPipelinesResponsepipelineIdListTypeDef",
    "ClientListPipelinesResponseTypeDef",
    "ClientPollForTaskInstanceIdentityTypeDef",
    "ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef",
    "ClientPollForTaskResponsetaskObjectobjectsTypeDef",
    "ClientPollForTaskResponsetaskObjectTypeDef",
    "ClientPollForTaskResponseTypeDef",
    "ClientPutPipelineDefinitionParameterObjectsattributesTypeDef",
    "ClientPutPipelineDefinitionParameterObjectsTypeDef",
    "ClientPutPipelineDefinitionParameterValuesTypeDef",
    "ClientPutPipelineDefinitionPipelineObjectsfieldsTypeDef",
    "ClientPutPipelineDefinitionPipelineObjectsTypeDef",
    "ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef",
    "ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef",
    "ClientPutPipelineDefinitionResponseTypeDef",
    "ClientQueryObjectsQueryselectorsoperatorTypeDef",
    "ClientQueryObjectsQueryselectorsTypeDef",
    "ClientQueryObjectsQueryTypeDef",
    "ClientQueryObjectsResponseTypeDef",
    "ClientReportTaskProgressFieldsTypeDef",
    "ClientReportTaskProgressResponseTypeDef",
    "ClientReportTaskRunnerHeartbeatResponseTypeDef",
    "ClientValidatePipelineDefinitionParameterObjectsattributesTypeDef",
    "ClientValidatePipelineDefinitionParameterObjectsTypeDef",
    "ClientValidatePipelineDefinitionParameterValuesTypeDef",
    "ClientValidatePipelineDefinitionPipelineObjectsfieldsTypeDef",
    "ClientValidatePipelineDefinitionPipelineObjectsTypeDef",
    "ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef",
    "ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef",
    "ClientValidatePipelineDefinitionResponseTypeDef",
    "DescribeObjectsPaginatePaginationConfigTypeDef",
    "DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef",
    "DescribeObjectsPaginateResponsepipelineObjectsTypeDef",
    "DescribeObjectsPaginateResponseTypeDef",
    "ListPipelinesPaginatePaginationConfigTypeDef",
    "ListPipelinesPaginateResponsepipelineIdListTypeDef",
    "ListPipelinesPaginateResponseTypeDef",
    "QueryObjectsPaginatePaginationConfigTypeDef",
    "QueryObjectsPaginateQueryselectorsoperatorTypeDef",
    "QueryObjectsPaginateQueryselectorsTypeDef",
    "QueryObjectsPaginateQueryTypeDef",
    "QueryObjectsPaginateResponseTypeDef",
)


_RequiredClientActivatePipelineParameterValuesTypeDef = TypedDict(
    "_RequiredClientActivatePipelineParameterValuesTypeDef", {"id": str}
)
_OptionalClientActivatePipelineParameterValuesTypeDef = TypedDict(
    "_OptionalClientActivatePipelineParameterValuesTypeDef", {"stringValue": str}, total=False
)


class ClientActivatePipelineParameterValuesTypeDef(
    _RequiredClientActivatePipelineParameterValuesTypeDef,
    _OptionalClientActivatePipelineParameterValuesTypeDef,
):
    """
    - *(dict) --*

      A value or list of parameter values.
      - **id** *(string) --***[REQUIRED]**

        The ID of the parameter value.
    """


_RequiredClientAddTagsTagsTypeDef = TypedDict("_RequiredClientAddTagsTagsTypeDef", {"key": str})
_OptionalClientAddTagsTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsTypeDef", {"value": str}, total=False
)


class ClientAddTagsTagsTypeDef(
    _RequiredClientAddTagsTagsTypeDef, _OptionalClientAddTagsTagsTypeDef
):
    """
    - *(dict) --*

      Tags are key/value pairs defined by a user and associated with a pipeline to control access.
      AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see
      `Controlling User Access to Pipelines
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
      the *AWS Data Pipeline Developer Guide* .
      - **key** *(string) --***[REQUIRED]**

        The key name of a tag defined by a user. For more information, see `Controlling User Access
        to Pipelines
        <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
        the *AWS Data Pipeline Developer Guide* .
    """


_ClientCreatePipelineResponseTypeDef = TypedDict(
    "_ClientCreatePipelineResponseTypeDef", {"pipelineId": str}, total=False
)


class ClientCreatePipelineResponseTypeDef(_ClientCreatePipelineResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of CreatePipeline.
      - **pipelineId** *(string) --*

        The ID that AWS Data Pipeline assigns the newly created pipeline. For example,
        ``df-06372391ZG65EXAMPLE`` .
    """


_RequiredClientCreatePipelineTagsTypeDef = TypedDict(
    "_RequiredClientCreatePipelineTagsTypeDef", {"key": str}
)
_OptionalClientCreatePipelineTagsTypeDef = TypedDict(
    "_OptionalClientCreatePipelineTagsTypeDef", {"value": str}, total=False
)


class ClientCreatePipelineTagsTypeDef(
    _RequiredClientCreatePipelineTagsTypeDef, _OptionalClientCreatePipelineTagsTypeDef
):
    """
    - *(dict) --*

      Tags are key/value pairs defined by a user and associated with a pipeline to control access.
      AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see
      `Controlling User Access to Pipelines
      <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
      the *AWS Data Pipeline Developer Guide* .
      - **key** *(string) --***[REQUIRED]**

        The key name of a tag defined by a user. For more information, see `Controlling User Access
        to Pipelines
        <http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html>`__ in
        the *AWS Data Pipeline Developer Guide* .
    """


_ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef = TypedDict(
    "_ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef(
    _ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef
):
    pass


_ClientDescribeObjectsResponsepipelineObjectsTypeDef = TypedDict(
    "_ClientDescribeObjectsResponsepipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef],
    },
    total=False,
)


class ClientDescribeObjectsResponsepipelineObjectsTypeDef(
    _ClientDescribeObjectsResponsepipelineObjectsTypeDef
):
    """
    - *(dict) --*

      Contains information about a pipeline object. This can be a logical, physical, or physical
      attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
      - **id** *(string) --*

        The ID of the object.
    """


_ClientDescribeObjectsResponseTypeDef = TypedDict(
    "_ClientDescribeObjectsResponseTypeDef",
    {
        "pipelineObjects": List[ClientDescribeObjectsResponsepipelineObjectsTypeDef],
        "marker": str,
        "hasMoreResults": bool,
    },
    total=False,
)


class ClientDescribeObjectsResponseTypeDef(_ClientDescribeObjectsResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of DescribeObjects.
      - **pipelineObjects** *(list) --*

        An array of object definitions.
        - *(dict) --*

          Contains information about a pipeline object. This can be a logical, physical, or physical
          attempt pipeline object. The complete set of components of a pipeline defines the
          pipeline.
          - **id** *(string) --*

            The ID of the object.
    """


_ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef = TypedDict(
    "_ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef(
    _ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef
):
    pass


_ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef = TypedDict(
    "_ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef(
    _ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef
):
    pass


_ClientDescribePipelinesResponsepipelineDescriptionListTypeDef = TypedDict(
    "_ClientDescribePipelinesResponsepipelineDescriptionListTypeDef",
    {
        "pipelineId": str,
        "name": str,
        "fields": List[ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef],
        "description": str,
        "tags": List[ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef],
    },
    total=False,
)


class ClientDescribePipelinesResponsepipelineDescriptionListTypeDef(
    _ClientDescribePipelinesResponsepipelineDescriptionListTypeDef
):
    """
    - *(dict) --*

      Contains pipeline metadata.
      - **pipelineId** *(string) --*

        The pipeline identifier that was assigned by AWS Data Pipeline. This is a string of the form
        ``df-297EG78HU43EEXAMPLE`` .
    """


_ClientDescribePipelinesResponseTypeDef = TypedDict(
    "_ClientDescribePipelinesResponseTypeDef",
    {
        "pipelineDescriptionList": List[
            ClientDescribePipelinesResponsepipelineDescriptionListTypeDef
        ]
    },
    total=False,
)


class ClientDescribePipelinesResponseTypeDef(_ClientDescribePipelinesResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of DescribePipelines.
      - **pipelineDescriptionList** *(list) --*

        An array of descriptions for the specified pipelines.
        - *(dict) --*

          Contains pipeline metadata.
          - **pipelineId** *(string) --*

            The pipeline identifier that was assigned by AWS Data Pipeline. This is a string of the
            form ``df-297EG78HU43EEXAMPLE`` .
    """


_ClientEvaluateExpressionResponseTypeDef = TypedDict(
    "_ClientEvaluateExpressionResponseTypeDef", {"evaluatedExpression": str}, total=False
)


class ClientEvaluateExpressionResponseTypeDef(_ClientEvaluateExpressionResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of EvaluateExpression.
      - **evaluatedExpression** *(string) --*

        The evaluated expression.
    """


_ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef",
    {"key": str, "stringValue": str},
    total=False,
)


class ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef(
    _ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef
):
    pass


_ClientGetPipelineDefinitionResponseparameterObjectsTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponseparameterObjectsTypeDef",
    {
        "id": str,
        "attributes": List[ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef],
    },
    total=False,
)


class ClientGetPipelineDefinitionResponseparameterObjectsTypeDef(
    _ClientGetPipelineDefinitionResponseparameterObjectsTypeDef
):
    pass


_ClientGetPipelineDefinitionResponseparameterValuesTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponseparameterValuesTypeDef",
    {"id": str, "stringValue": str},
    total=False,
)


class ClientGetPipelineDefinitionResponseparameterValuesTypeDef(
    _ClientGetPipelineDefinitionResponseparameterValuesTypeDef
):
    pass


_ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef(
    _ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef
):
    pass


_ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef],
    },
    total=False,
)


class ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef(
    _ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef
):
    """
    - *(dict) --*

      Contains information about a pipeline object. This can be a logical, physical, or physical
      attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
      - **id** *(string) --*

        The ID of the object.
    """


_ClientGetPipelineDefinitionResponseTypeDef = TypedDict(
    "_ClientGetPipelineDefinitionResponseTypeDef",
    {
        "pipelineObjects": List[ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef],
        "parameterObjects": List[ClientGetPipelineDefinitionResponseparameterObjectsTypeDef],
        "parameterValues": List[ClientGetPipelineDefinitionResponseparameterValuesTypeDef],
    },
    total=False,
)


class ClientGetPipelineDefinitionResponseTypeDef(_ClientGetPipelineDefinitionResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of GetPipelineDefinition.
      - **pipelineObjects** *(list) --*

        The objects defined in the pipeline.
        - *(dict) --*

          Contains information about a pipeline object. This can be a logical, physical, or physical
          attempt pipeline object. The complete set of components of a pipeline defines the
          pipeline.
          - **id** *(string) --*

            The ID of the object.
    """


_ClientListPipelinesResponsepipelineIdListTypeDef = TypedDict(
    "_ClientListPipelinesResponsepipelineIdListTypeDef", {"id": str, "name": str}, total=False
)


class ClientListPipelinesResponsepipelineIdListTypeDef(
    _ClientListPipelinesResponsepipelineIdListTypeDef
):
    """
    - *(dict) --*

      Contains the name and identifier of a pipeline.
      - **id** *(string) --*

        The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the form
        ``df-297EG78HU43EEXAMPLE`` .
    """


_ClientListPipelinesResponseTypeDef = TypedDict(
    "_ClientListPipelinesResponseTypeDef",
    {
        "pipelineIdList": List[ClientListPipelinesResponsepipelineIdListTypeDef],
        "marker": str,
        "hasMoreResults": bool,
    },
    total=False,
)


class ClientListPipelinesResponseTypeDef(_ClientListPipelinesResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of ListPipelines.
      - **pipelineIdList** *(list) --*

        The pipeline identifiers. If you require additional information about the pipelines, you can
        use these identifiers to call  DescribePipelines and  GetPipelineDefinition .
        - *(dict) --*

          Contains the name and identifier of a pipeline.
          - **id** *(string) --*

            The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the
            form ``df-297EG78HU43EEXAMPLE`` .
    """


_ClientPollForTaskInstanceIdentityTypeDef = TypedDict(
    "_ClientPollForTaskInstanceIdentityTypeDef", {"document": str, "signature": str}, total=False
)


class ClientPollForTaskInstanceIdentityTypeDef(_ClientPollForTaskInstanceIdentityTypeDef):
    """
    Identity information for the EC2 instance that is hosting the task runner. You can get this
    value from the instance using ``http://169.254.169.254/latest/meta-data/instance-id`` . For more
    information, see `Instance Metadata
    <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html>`__ in the
    *Amazon Elastic Compute Cloud User Guide.* Passing in this value proves that your task runner is
    running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied
    to your pipeline.
    - **document** *(string) --*

      A description of an EC2 instance that is generated when the instance is launched and exposed
      to the instance via the instance metadata service in the form of a JSON representation of an
      object.
    """


_ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef = TypedDict(
    "_ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef(
    _ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef
):
    pass


_ClientPollForTaskResponsetaskObjectobjectsTypeDef = TypedDict(
    "_ClientPollForTaskResponsetaskObjectobjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef],
    },
    total=False,
)


class ClientPollForTaskResponsetaskObjectobjectsTypeDef(
    _ClientPollForTaskResponsetaskObjectobjectsTypeDef
):
    pass


_ClientPollForTaskResponsetaskObjectTypeDef = TypedDict(
    "_ClientPollForTaskResponsetaskObjectTypeDef",
    {
        "taskId": str,
        "pipelineId": str,
        "attemptId": str,
        "objects": Dict[str, ClientPollForTaskResponsetaskObjectobjectsTypeDef],
    },
    total=False,
)


class ClientPollForTaskResponsetaskObjectTypeDef(_ClientPollForTaskResponsetaskObjectTypeDef):
    """
    - **taskObject** *(dict) --*

      The information needed to complete the task that is being assigned to the task runner. One of
      the fields returned in this object is ``taskId`` , which contains an identifier for the task
      being assigned. The calling task runner uses ``taskId`` in subsequent calls to
      ReportTaskProgress and  SetTaskStatus .
      - **taskId** *(string) --*

        An internal identifier for the task. This ID is passed to the  SetTaskStatus and
        ReportTaskProgress actions.
    """


_ClientPollForTaskResponseTypeDef = TypedDict(
    "_ClientPollForTaskResponseTypeDef",
    {"taskObject": ClientPollForTaskResponsetaskObjectTypeDef},
    total=False,
)


class ClientPollForTaskResponseTypeDef(_ClientPollForTaskResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of PollForTask.
      - **taskObject** *(dict) --*

        The information needed to complete the task that is being assigned to the task runner. One
        of the fields returned in this object is ``taskId`` , which contains an identifier for the
        task being assigned. The calling task runner uses ``taskId`` in subsequent calls to
        ReportTaskProgress and  SetTaskStatus .
        - **taskId** *(string) --*

          An internal identifier for the task. This ID is passed to the  SetTaskStatus and
          ReportTaskProgress actions.
    """


_ClientPutPipelineDefinitionParameterObjectsattributesTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionParameterObjectsattributesTypeDef",
    {"key": str, "stringValue": str},
    total=False,
)


class ClientPutPipelineDefinitionParameterObjectsattributesTypeDef(
    _ClientPutPipelineDefinitionParameterObjectsattributesTypeDef
):
    pass


_RequiredClientPutPipelineDefinitionParameterObjectsTypeDef = TypedDict(
    "_RequiredClientPutPipelineDefinitionParameterObjectsTypeDef", {"id": str}
)
_OptionalClientPutPipelineDefinitionParameterObjectsTypeDef = TypedDict(
    "_OptionalClientPutPipelineDefinitionParameterObjectsTypeDef",
    {"attributes": List[ClientPutPipelineDefinitionParameterObjectsattributesTypeDef]},
    total=False,
)


class ClientPutPipelineDefinitionParameterObjectsTypeDef(
    _RequiredClientPutPipelineDefinitionParameterObjectsTypeDef,
    _OptionalClientPutPipelineDefinitionParameterObjectsTypeDef,
):
    """
    - *(dict) --*

      Contains information about a parameter object.
      - **id** *(string) --***[REQUIRED]**

        The ID of the parameter object.
    """


_RequiredClientPutPipelineDefinitionParameterValuesTypeDef = TypedDict(
    "_RequiredClientPutPipelineDefinitionParameterValuesTypeDef", {"id": str}
)
_OptionalClientPutPipelineDefinitionParameterValuesTypeDef = TypedDict(
    "_OptionalClientPutPipelineDefinitionParameterValuesTypeDef", {"stringValue": str}, total=False
)


class ClientPutPipelineDefinitionParameterValuesTypeDef(
    _RequiredClientPutPipelineDefinitionParameterValuesTypeDef,
    _OptionalClientPutPipelineDefinitionParameterValuesTypeDef,
):
    """
    - *(dict) --*

      A value or list of parameter values.
      - **id** *(string) --***[REQUIRED]**

        The ID of the parameter value.
    """


_ClientPutPipelineDefinitionPipelineObjectsfieldsTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionPipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientPutPipelineDefinitionPipelineObjectsfieldsTypeDef(
    _ClientPutPipelineDefinitionPipelineObjectsfieldsTypeDef
):
    pass


_RequiredClientPutPipelineDefinitionPipelineObjectsTypeDef = TypedDict(
    "_RequiredClientPutPipelineDefinitionPipelineObjectsTypeDef", {"id": str}
)
_OptionalClientPutPipelineDefinitionPipelineObjectsTypeDef = TypedDict(
    "_OptionalClientPutPipelineDefinitionPipelineObjectsTypeDef",
    {"name": str, "fields": List[ClientPutPipelineDefinitionPipelineObjectsfieldsTypeDef]},
    total=False,
)


class ClientPutPipelineDefinitionPipelineObjectsTypeDef(
    _RequiredClientPutPipelineDefinitionPipelineObjectsTypeDef,
    _OptionalClientPutPipelineDefinitionPipelineObjectsTypeDef,
):
    """
    - *(dict) --*

      Contains information about a pipeline object. This can be a logical, physical, or physical
      attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
      - **id** *(string) --***[REQUIRED]**

        The ID of the object.
    """


_ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef",
    {"id": str, "errors": List[str]},
    total=False,
)


class ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef(
    _ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef
):
    """
    - *(dict) --*

      Defines a validation error. Validation errors prevent pipeline activation. The set of
      validation errors that can be returned are defined by AWS Data Pipeline.
      - **id** *(string) --*

        The identifier of the object that contains the validation error.
    """


_ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef",
    {"id": str, "warnings": List[str]},
    total=False,
)


class ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef(
    _ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef
):
    pass


_ClientPutPipelineDefinitionResponseTypeDef = TypedDict(
    "_ClientPutPipelineDefinitionResponseTypeDef",
    {
        "validationErrors": List[ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef],
        "validationWarnings": List[ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef],
        "errored": bool,
    },
    total=False,
)


class ClientPutPipelineDefinitionResponseTypeDef(_ClientPutPipelineDefinitionResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of PutPipelineDefinition.
      - **validationErrors** *(list) --*

        The validation errors that are associated with the objects defined in ``pipelineObjects`` .
        - *(dict) --*

          Defines a validation error. Validation errors prevent pipeline activation. The set of
          validation errors that can be returned are defined by AWS Data Pipeline.
          - **id** *(string) --*

            The identifier of the object that contains the validation error.
    """


_ClientQueryObjectsQueryselectorsoperatorTypeDef = TypedDict(
    "_ClientQueryObjectsQueryselectorsoperatorTypeDef",
    {"type": Literal["EQ", "REF_EQ", "LE", "GE", "BETWEEN"], "values": List[str]},
    total=False,
)


class ClientQueryObjectsQueryselectorsoperatorTypeDef(
    _ClientQueryObjectsQueryselectorsoperatorTypeDef
):
    pass


_ClientQueryObjectsQueryselectorsTypeDef = TypedDict(
    "_ClientQueryObjectsQueryselectorsTypeDef",
    {"fieldName": str, "operator": ClientQueryObjectsQueryselectorsoperatorTypeDef},
    total=False,
)


class ClientQueryObjectsQueryselectorsTypeDef(_ClientQueryObjectsQueryselectorsTypeDef):
    """
    - *(dict) --*

      A comparision that is used to determine whether a query should return this object.
      - **fieldName** *(string) --*

        The name of the field that the operator will be applied to. The field name is the "key"
        portion of the field definition in the pipeline definition syntax that is used by the AWS
        Data Pipeline API. If the field is not set on the object, the condition fails.
    """


_ClientQueryObjectsQueryTypeDef = TypedDict(
    "_ClientQueryObjectsQueryTypeDef",
    {"selectors": List[ClientQueryObjectsQueryselectorsTypeDef]},
    total=False,
)


class ClientQueryObjectsQueryTypeDef(_ClientQueryObjectsQueryTypeDef):
    """
    The query that defines the objects to be returned. The ``Query`` object can contain a maximum of
    ten selectors. The conditions in the query are limited to top-level String fields in the object.
    These filters can be applied to components, instances, and attempts.
    - **selectors** *(list) --*

      List of selectors that define the query. An object must satisfy all of the selectors to match
      the query.
      - *(dict) --*

        A comparision that is used to determine whether a query should return this object.
        - **fieldName** *(string) --*

          The name of the field that the operator will be applied to. The field name is the "key"
          portion of the field definition in the pipeline definition syntax that is used by the AWS
          Data Pipeline API. If the field is not set on the object, the condition fails.
    """


_ClientQueryObjectsResponseTypeDef = TypedDict(
    "_ClientQueryObjectsResponseTypeDef",
    {"ids": List[str], "marker": str, "hasMoreResults": bool},
    total=False,
)


class ClientQueryObjectsResponseTypeDef(_ClientQueryObjectsResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of QueryObjects.
      - **ids** *(list) --*

        The identifiers that match the query selectors.
        - *(string) --*
    """


_RequiredClientReportTaskProgressFieldsTypeDef = TypedDict(
    "_RequiredClientReportTaskProgressFieldsTypeDef", {"key": str}
)
_OptionalClientReportTaskProgressFieldsTypeDef = TypedDict(
    "_OptionalClientReportTaskProgressFieldsTypeDef",
    {"stringValue": str, "refValue": str},
    total=False,
)


class ClientReportTaskProgressFieldsTypeDef(
    _RequiredClientReportTaskProgressFieldsTypeDef, _OptionalClientReportTaskProgressFieldsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that describes a property of a pipeline object. The value is specified as
      either a string value (``StringValue`` ) or a reference to another object (``RefValue`` ) but
      not as both.
      - **key** *(string) --***[REQUIRED]**

        The field identifier.
    """


_ClientReportTaskProgressResponseTypeDef = TypedDict(
    "_ClientReportTaskProgressResponseTypeDef", {"canceled": bool}, total=False
)


class ClientReportTaskProgressResponseTypeDef(_ClientReportTaskProgressResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of ReportTaskProgress.
      - **canceled** *(boolean) --*

        If true, the calling task runner should cancel processing of the task. The task runner does
        not need to call  SetTaskStatus for canceled tasks.
    """


_ClientReportTaskRunnerHeartbeatResponseTypeDef = TypedDict(
    "_ClientReportTaskRunnerHeartbeatResponseTypeDef", {"terminate": bool}, total=False
)


class ClientReportTaskRunnerHeartbeatResponseTypeDef(
    _ClientReportTaskRunnerHeartbeatResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of ReportTaskRunnerHeartbeat.
      - **terminate** *(boolean) --*

        Indicates whether the calling task runner should terminate.
    """


_ClientValidatePipelineDefinitionParameterObjectsattributesTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionParameterObjectsattributesTypeDef",
    {"key": str, "stringValue": str},
    total=False,
)


class ClientValidatePipelineDefinitionParameterObjectsattributesTypeDef(
    _ClientValidatePipelineDefinitionParameterObjectsattributesTypeDef
):
    pass


_RequiredClientValidatePipelineDefinitionParameterObjectsTypeDef = TypedDict(
    "_RequiredClientValidatePipelineDefinitionParameterObjectsTypeDef", {"id": str}
)
_OptionalClientValidatePipelineDefinitionParameterObjectsTypeDef = TypedDict(
    "_OptionalClientValidatePipelineDefinitionParameterObjectsTypeDef",
    {"attributes": List[ClientValidatePipelineDefinitionParameterObjectsattributesTypeDef]},
    total=False,
)


class ClientValidatePipelineDefinitionParameterObjectsTypeDef(
    _RequiredClientValidatePipelineDefinitionParameterObjectsTypeDef,
    _OptionalClientValidatePipelineDefinitionParameterObjectsTypeDef,
):
    """
    - *(dict) --*

      Contains information about a parameter object.
      - **id** *(string) --***[REQUIRED]**

        The ID of the parameter object.
    """


_RequiredClientValidatePipelineDefinitionParameterValuesTypeDef = TypedDict(
    "_RequiredClientValidatePipelineDefinitionParameterValuesTypeDef", {"id": str}
)
_OptionalClientValidatePipelineDefinitionParameterValuesTypeDef = TypedDict(
    "_OptionalClientValidatePipelineDefinitionParameterValuesTypeDef",
    {"stringValue": str},
    total=False,
)


class ClientValidatePipelineDefinitionParameterValuesTypeDef(
    _RequiredClientValidatePipelineDefinitionParameterValuesTypeDef,
    _OptionalClientValidatePipelineDefinitionParameterValuesTypeDef,
):
    """
    - *(dict) --*

      A value or list of parameter values.
      - **id** *(string) --***[REQUIRED]**

        The ID of the parameter value.
    """


_ClientValidatePipelineDefinitionPipelineObjectsfieldsTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionPipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class ClientValidatePipelineDefinitionPipelineObjectsfieldsTypeDef(
    _ClientValidatePipelineDefinitionPipelineObjectsfieldsTypeDef
):
    pass


_RequiredClientValidatePipelineDefinitionPipelineObjectsTypeDef = TypedDict(
    "_RequiredClientValidatePipelineDefinitionPipelineObjectsTypeDef", {"id": str}
)
_OptionalClientValidatePipelineDefinitionPipelineObjectsTypeDef = TypedDict(
    "_OptionalClientValidatePipelineDefinitionPipelineObjectsTypeDef",
    {"name": str, "fields": List[ClientValidatePipelineDefinitionPipelineObjectsfieldsTypeDef]},
    total=False,
)


class ClientValidatePipelineDefinitionPipelineObjectsTypeDef(
    _RequiredClientValidatePipelineDefinitionPipelineObjectsTypeDef,
    _OptionalClientValidatePipelineDefinitionPipelineObjectsTypeDef,
):
    """
    - *(dict) --*

      Contains information about a pipeline object. This can be a logical, physical, or physical
      attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
      - **id** *(string) --***[REQUIRED]**

        The ID of the object.
    """


_ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef",
    {"id": str, "errors": List[str]},
    total=False,
)


class ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef(
    _ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef
):
    """
    - *(dict) --*

      Defines a validation error. Validation errors prevent pipeline activation. The set of
      validation errors that can be returned are defined by AWS Data Pipeline.
      - **id** *(string) --*

        The identifier of the object that contains the validation error.
    """


_ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef",
    {"id": str, "warnings": List[str]},
    total=False,
)


class ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef(
    _ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef
):
    pass


_ClientValidatePipelineDefinitionResponseTypeDef = TypedDict(
    "_ClientValidatePipelineDefinitionResponseTypeDef",
    {
        "validationErrors": List[ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef],
        "validationWarnings": List[
            ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef
        ],
        "errored": bool,
    },
    total=False,
)


class ClientValidatePipelineDefinitionResponseTypeDef(
    _ClientValidatePipelineDefinitionResponseTypeDef
):
    """
    - *(dict) --*

      Contains the output of ValidatePipelineDefinition.
      - **validationErrors** *(list) --*

        Any validation errors that were found.
        - *(dict) --*

          Defines a validation error. Validation errors prevent pipeline activation. The set of
          validation errors that can be returned are defined by AWS Data Pipeline.
          - **id** *(string) --*

            The identifier of the object that contains the validation error.
    """


_DescribeObjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeObjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeObjectsPaginatePaginationConfigTypeDef(
    _DescribeObjectsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef = TypedDict(
    "_DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)


class DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef(
    _DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef
):
    pass


_DescribeObjectsPaginateResponsepipelineObjectsTypeDef = TypedDict(
    "_DescribeObjectsPaginateResponsepipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef],
    },
    total=False,
)


class DescribeObjectsPaginateResponsepipelineObjectsTypeDef(
    _DescribeObjectsPaginateResponsepipelineObjectsTypeDef
):
    """
    - *(dict) --*

      Contains information about a pipeline object. This can be a logical, physical, or physical
      attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
      - **id** *(string) --*

        The ID of the object.
    """


_DescribeObjectsPaginateResponseTypeDef = TypedDict(
    "_DescribeObjectsPaginateResponseTypeDef",
    {
        "pipelineObjects": List[DescribeObjectsPaginateResponsepipelineObjectsTypeDef],
        "hasMoreResults": bool,
        "NextToken": str,
    },
    total=False,
)


class DescribeObjectsPaginateResponseTypeDef(_DescribeObjectsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of DescribeObjects.
      - **pipelineObjects** *(list) --*

        An array of object definitions.
        - *(dict) --*

          Contains information about a pipeline object. This can be a logical, physical, or physical
          attempt pipeline object. The complete set of components of a pipeline defines the
          pipeline.
          - **id** *(string) --*

            The ID of the object.
    """


_ListPipelinesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPipelinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPipelinesPaginatePaginationConfigTypeDef(_ListPipelinesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPipelinesPaginateResponsepipelineIdListTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsepipelineIdListTypeDef", {"id": str, "name": str}, total=False
)


class ListPipelinesPaginateResponsepipelineIdListTypeDef(
    _ListPipelinesPaginateResponsepipelineIdListTypeDef
):
    """
    - *(dict) --*

      Contains the name and identifier of a pipeline.
      - **id** *(string) --*

        The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the form
        ``df-297EG78HU43EEXAMPLE`` .
    """


_ListPipelinesPaginateResponseTypeDef = TypedDict(
    "_ListPipelinesPaginateResponseTypeDef",
    {
        "pipelineIdList": List[ListPipelinesPaginateResponsepipelineIdListTypeDef],
        "hasMoreResults": bool,
        "NextToken": str,
    },
    total=False,
)


class ListPipelinesPaginateResponseTypeDef(_ListPipelinesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of ListPipelines.
      - **pipelineIdList** *(list) --*

        The pipeline identifiers. If you require additional information about the pipelines, you can
        use these identifiers to call  DescribePipelines and  GetPipelineDefinition .
        - *(dict) --*

          Contains the name and identifier of a pipeline.
          - **id** *(string) --*

            The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the
            form ``df-297EG78HU43EEXAMPLE`` .
    """


_QueryObjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_QueryObjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class QueryObjectsPaginatePaginationConfigTypeDef(_QueryObjectsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_QueryObjectsPaginateQueryselectorsoperatorTypeDef = TypedDict(
    "_QueryObjectsPaginateQueryselectorsoperatorTypeDef",
    {"type": Literal["EQ", "REF_EQ", "LE", "GE", "BETWEEN"], "values": List[str]},
    total=False,
)


class QueryObjectsPaginateQueryselectorsoperatorTypeDef(
    _QueryObjectsPaginateQueryselectorsoperatorTypeDef
):
    pass


_QueryObjectsPaginateQueryselectorsTypeDef = TypedDict(
    "_QueryObjectsPaginateQueryselectorsTypeDef",
    {"fieldName": str, "operator": QueryObjectsPaginateQueryselectorsoperatorTypeDef},
    total=False,
)


class QueryObjectsPaginateQueryselectorsTypeDef(_QueryObjectsPaginateQueryselectorsTypeDef):
    """
    - *(dict) --*

      A comparision that is used to determine whether a query should return this object.
      - **fieldName** *(string) --*

        The name of the field that the operator will be applied to. The field name is the "key"
        portion of the field definition in the pipeline definition syntax that is used by the AWS
        Data Pipeline API. If the field is not set on the object, the condition fails.
    """


_QueryObjectsPaginateQueryTypeDef = TypedDict(
    "_QueryObjectsPaginateQueryTypeDef",
    {"selectors": List[QueryObjectsPaginateQueryselectorsTypeDef]},
    total=False,
)


class QueryObjectsPaginateQueryTypeDef(_QueryObjectsPaginateQueryTypeDef):
    """
    The query that defines the objects to be returned. The ``Query`` object can contain a maximum of
    ten selectors. The conditions in the query are limited to top-level String fields in the object.
    These filters can be applied to components, instances, and attempts.
    - **selectors** *(list) --*

      List of selectors that define the query. An object must satisfy all of the selectors to match
      the query.
      - *(dict) --*

        A comparision that is used to determine whether a query should return this object.
        - **fieldName** *(string) --*

          The name of the field that the operator will be applied to. The field name is the "key"
          portion of the field definition in the pipeline definition syntax that is used by the AWS
          Data Pipeline API. If the field is not set on the object, the condition fails.
    """


_QueryObjectsPaginateResponseTypeDef = TypedDict(
    "_QueryObjectsPaginateResponseTypeDef",
    {"ids": List[str], "hasMoreResults": bool, "NextToken": str},
    total=False,
)


class QueryObjectsPaginateResponseTypeDef(_QueryObjectsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of QueryObjects.
      - **ids** *(list) --*

        The identifiers that match the query selectors.
        - *(string) --*
    """
