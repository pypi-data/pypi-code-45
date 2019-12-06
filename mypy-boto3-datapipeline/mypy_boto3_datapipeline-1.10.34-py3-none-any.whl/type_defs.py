"Main interface for datapipeline service type defs"
from __future__ import annotations

import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


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
    pass


_RequiredClientAddTagsTagsTypeDef = TypedDict("_RequiredClientAddTagsTagsTypeDef", {"key": str})
_OptionalClientAddTagsTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsTypeDef", {"value": str}, total=False
)


class ClientAddTagsTagsTypeDef(
    _RequiredClientAddTagsTagsTypeDef, _OptionalClientAddTagsTagsTypeDef
):
    pass


ClientCreatePipelineResponseTypeDef = TypedDict(
    "ClientCreatePipelineResponseTypeDef", {"pipelineId": str}, total=False
)

_RequiredClientCreatePipelineTagsTypeDef = TypedDict(
    "_RequiredClientCreatePipelineTagsTypeDef", {"key": str}
)
_OptionalClientCreatePipelineTagsTypeDef = TypedDict(
    "_OptionalClientCreatePipelineTagsTypeDef", {"value": str}, total=False
)


class ClientCreatePipelineTagsTypeDef(
    _RequiredClientCreatePipelineTagsTypeDef, _OptionalClientCreatePipelineTagsTypeDef
):
    pass


ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef = TypedDict(
    "ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)

ClientDescribeObjectsResponsepipelineObjectsTypeDef = TypedDict(
    "ClientDescribeObjectsResponsepipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientDescribeObjectsResponsepipelineObjectsfieldsTypeDef],
    },
    total=False,
)

ClientDescribeObjectsResponseTypeDef = TypedDict(
    "ClientDescribeObjectsResponseTypeDef",
    {
        "pipelineObjects": List[ClientDescribeObjectsResponsepipelineObjectsTypeDef],
        "marker": str,
        "hasMoreResults": bool,
    },
    total=False,
)

ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef = TypedDict(
    "ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)

ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef = TypedDict(
    "ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribePipelinesResponsepipelineDescriptionListTypeDef = TypedDict(
    "ClientDescribePipelinesResponsepipelineDescriptionListTypeDef",
    {
        "pipelineId": str,
        "name": str,
        "fields": List[ClientDescribePipelinesResponsepipelineDescriptionListfieldsTypeDef],
        "description": str,
        "tags": List[ClientDescribePipelinesResponsepipelineDescriptionListtagsTypeDef],
    },
    total=False,
)

ClientDescribePipelinesResponseTypeDef = TypedDict(
    "ClientDescribePipelinesResponseTypeDef",
    {
        "pipelineDescriptionList": List[
            ClientDescribePipelinesResponsepipelineDescriptionListTypeDef
        ]
    },
    total=False,
)

ClientEvaluateExpressionResponseTypeDef = TypedDict(
    "ClientEvaluateExpressionResponseTypeDef", {"evaluatedExpression": str}, total=False
)

ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef = TypedDict(
    "ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef",
    {"key": str, "stringValue": str},
    total=False,
)

ClientGetPipelineDefinitionResponseparameterObjectsTypeDef = TypedDict(
    "ClientGetPipelineDefinitionResponseparameterObjectsTypeDef",
    {
        "id": str,
        "attributes": List[ClientGetPipelineDefinitionResponseparameterObjectsattributesTypeDef],
    },
    total=False,
)

ClientGetPipelineDefinitionResponseparameterValuesTypeDef = TypedDict(
    "ClientGetPipelineDefinitionResponseparameterValuesTypeDef",
    {"id": str, "stringValue": str},
    total=False,
)

ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef = TypedDict(
    "ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)

ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef = TypedDict(
    "ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientGetPipelineDefinitionResponsepipelineObjectsfieldsTypeDef],
    },
    total=False,
)

ClientGetPipelineDefinitionResponseTypeDef = TypedDict(
    "ClientGetPipelineDefinitionResponseTypeDef",
    {
        "pipelineObjects": List[ClientGetPipelineDefinitionResponsepipelineObjectsTypeDef],
        "parameterObjects": List[ClientGetPipelineDefinitionResponseparameterObjectsTypeDef],
        "parameterValues": List[ClientGetPipelineDefinitionResponseparameterValuesTypeDef],
    },
    total=False,
)

ClientListPipelinesResponsepipelineIdListTypeDef = TypedDict(
    "ClientListPipelinesResponsepipelineIdListTypeDef", {"id": str, "name": str}, total=False
)

ClientListPipelinesResponseTypeDef = TypedDict(
    "ClientListPipelinesResponseTypeDef",
    {
        "pipelineIdList": List[ClientListPipelinesResponsepipelineIdListTypeDef],
        "marker": str,
        "hasMoreResults": bool,
    },
    total=False,
)

ClientPollForTaskInstanceIdentityTypeDef = TypedDict(
    "ClientPollForTaskInstanceIdentityTypeDef", {"document": str, "signature": str}, total=False
)

ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef = TypedDict(
    "ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)

ClientPollForTaskResponsetaskObjectobjectsTypeDef = TypedDict(
    "ClientPollForTaskResponsetaskObjectobjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[ClientPollForTaskResponsetaskObjectobjectsfieldsTypeDef],
    },
    total=False,
)

ClientPollForTaskResponsetaskObjectTypeDef = TypedDict(
    "ClientPollForTaskResponsetaskObjectTypeDef",
    {
        "taskId": str,
        "pipelineId": str,
        "attemptId": str,
        "objects": Dict[str, ClientPollForTaskResponsetaskObjectobjectsTypeDef],
    },
    total=False,
)

ClientPollForTaskResponseTypeDef = TypedDict(
    "ClientPollForTaskResponseTypeDef",
    {"taskObject": ClientPollForTaskResponsetaskObjectTypeDef},
    total=False,
)

ClientPutPipelineDefinitionParameterObjectsattributesTypeDef = TypedDict(
    "ClientPutPipelineDefinitionParameterObjectsattributesTypeDef",
    {"key": str, "stringValue": str},
    total=False,
)

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
    pass


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
    pass


ClientPutPipelineDefinitionPipelineObjectsfieldsTypeDef = TypedDict(
    "ClientPutPipelineDefinitionPipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)

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
    pass


ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef = TypedDict(
    "ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef",
    {"id": str, "errors": List[str]},
    total=False,
)

ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef = TypedDict(
    "ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef",
    {"id": str, "warnings": List[str]},
    total=False,
)

ClientPutPipelineDefinitionResponseTypeDef = TypedDict(
    "ClientPutPipelineDefinitionResponseTypeDef",
    {
        "validationErrors": List[ClientPutPipelineDefinitionResponsevalidationErrorsTypeDef],
        "validationWarnings": List[ClientPutPipelineDefinitionResponsevalidationWarningsTypeDef],
        "errored": bool,
    },
    total=False,
)

ClientQueryObjectsQueryselectorsoperatorTypeDef = TypedDict(
    "ClientQueryObjectsQueryselectorsoperatorTypeDef",
    {"type": Literal["EQ", "REF_EQ", "LE", "GE", "BETWEEN"], "values": List[str]},
    total=False,
)

ClientQueryObjectsQueryselectorsTypeDef = TypedDict(
    "ClientQueryObjectsQueryselectorsTypeDef",
    {"fieldName": str, "operator": ClientQueryObjectsQueryselectorsoperatorTypeDef},
    total=False,
)

ClientQueryObjectsQueryTypeDef = TypedDict(
    "ClientQueryObjectsQueryTypeDef",
    {"selectors": List[ClientQueryObjectsQueryselectorsTypeDef]},
    total=False,
)

ClientQueryObjectsResponseTypeDef = TypedDict(
    "ClientQueryObjectsResponseTypeDef",
    {"ids": List[str], "marker": str, "hasMoreResults": bool},
    total=False,
)

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
    pass


ClientReportTaskProgressResponseTypeDef = TypedDict(
    "ClientReportTaskProgressResponseTypeDef", {"canceled": bool}, total=False
)

ClientReportTaskRunnerHeartbeatResponseTypeDef = TypedDict(
    "ClientReportTaskRunnerHeartbeatResponseTypeDef", {"terminate": bool}, total=False
)

ClientValidatePipelineDefinitionParameterObjectsattributesTypeDef = TypedDict(
    "ClientValidatePipelineDefinitionParameterObjectsattributesTypeDef",
    {"key": str, "stringValue": str},
    total=False,
)

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
    pass


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
    pass


ClientValidatePipelineDefinitionPipelineObjectsfieldsTypeDef = TypedDict(
    "ClientValidatePipelineDefinitionPipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)

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
    pass


ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef = TypedDict(
    "ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef",
    {"id": str, "errors": List[str]},
    total=False,
)

ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef = TypedDict(
    "ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef",
    {"id": str, "warnings": List[str]},
    total=False,
)

ClientValidatePipelineDefinitionResponseTypeDef = TypedDict(
    "ClientValidatePipelineDefinitionResponseTypeDef",
    {
        "validationErrors": List[ClientValidatePipelineDefinitionResponsevalidationErrorsTypeDef],
        "validationWarnings": List[
            ClientValidatePipelineDefinitionResponsevalidationWarningsTypeDef
        ],
        "errored": bool,
    },
    total=False,
)

DescribeObjectsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeObjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef = TypedDict(
    "DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef",
    {"key": str, "stringValue": str, "refValue": str},
    total=False,
)

DescribeObjectsPaginateResponsepipelineObjectsTypeDef = TypedDict(
    "DescribeObjectsPaginateResponsepipelineObjectsTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List[DescribeObjectsPaginateResponsepipelineObjectsfieldsTypeDef],
    },
    total=False,
)

DescribeObjectsPaginateResponseTypeDef = TypedDict(
    "DescribeObjectsPaginateResponseTypeDef",
    {
        "pipelineObjects": List[DescribeObjectsPaginateResponsepipelineObjectsTypeDef],
        "hasMoreResults": bool,
        "NextToken": str,
    },
    total=False,
)

ListPipelinesPaginatePaginationConfigTypeDef = TypedDict(
    "ListPipelinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListPipelinesPaginateResponsepipelineIdListTypeDef = TypedDict(
    "ListPipelinesPaginateResponsepipelineIdListTypeDef", {"id": str, "name": str}, total=False
)

ListPipelinesPaginateResponseTypeDef = TypedDict(
    "ListPipelinesPaginateResponseTypeDef",
    {
        "pipelineIdList": List[ListPipelinesPaginateResponsepipelineIdListTypeDef],
        "hasMoreResults": bool,
        "NextToken": str,
    },
    total=False,
)

QueryObjectsPaginatePaginationConfigTypeDef = TypedDict(
    "QueryObjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

QueryObjectsPaginateQueryselectorsoperatorTypeDef = TypedDict(
    "QueryObjectsPaginateQueryselectorsoperatorTypeDef",
    {"type": Literal["EQ", "REF_EQ", "LE", "GE", "BETWEEN"], "values": List[str]},
    total=False,
)

QueryObjectsPaginateQueryselectorsTypeDef = TypedDict(
    "QueryObjectsPaginateQueryselectorsTypeDef",
    {"fieldName": str, "operator": QueryObjectsPaginateQueryselectorsoperatorTypeDef},
    total=False,
)

QueryObjectsPaginateQueryTypeDef = TypedDict(
    "QueryObjectsPaginateQueryTypeDef",
    {"selectors": List[QueryObjectsPaginateQueryselectorsTypeDef]},
    total=False,
)

QueryObjectsPaginateResponseTypeDef = TypedDict(
    "QueryObjectsPaginateResponseTypeDef",
    {"ids": List[str], "hasMoreResults": bool, "NextToken": str},
    total=False,
)
