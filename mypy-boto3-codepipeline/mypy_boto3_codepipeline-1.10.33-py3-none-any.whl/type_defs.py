"Main interface for codepipeline service type defs"
from __future__ import annotations

from datetime import datetime
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


ClientAcknowledgeJobResponseTypeDef = TypedDict(
    "ClientAcknowledgeJobResponseTypeDef",
    {
        "status": Literal[
            "Created", "Queued", "Dispatched", "InProgress", "TimedOut", "Succeeded", "Failed"
        ]
    },
    total=False,
)

ClientAcknowledgeThirdPartyJobResponseTypeDef = TypedDict(
    "ClientAcknowledgeThirdPartyJobResponseTypeDef",
    {
        "status": Literal[
            "Created", "Queued", "Dispatched", "InProgress", "TimedOut", "Succeeded", "Failed"
        ]
    },
    total=False,
)

ClientCreateCustomActionTypeConfigurationPropertiesTypeDef = TypedDict(
    "ClientCreateCustomActionTypeConfigurationPropertiesTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": bool,
        "description": str,
        "type": Literal["String", "Number", "Boolean"],
    },
    total=False,
)

_RequiredClientCreateCustomActionTypeInputArtifactDetailsTypeDef = TypedDict(
    "_RequiredClientCreateCustomActionTypeInputArtifactDetailsTypeDef", {"minimumCount": int}
)
_OptionalClientCreateCustomActionTypeInputArtifactDetailsTypeDef = TypedDict(
    "_OptionalClientCreateCustomActionTypeInputArtifactDetailsTypeDef",
    {"maximumCount": int},
    total=False,
)


class ClientCreateCustomActionTypeInputArtifactDetailsTypeDef(
    _RequiredClientCreateCustomActionTypeInputArtifactDetailsTypeDef,
    _OptionalClientCreateCustomActionTypeInputArtifactDetailsTypeDef,
):
    pass


_RequiredClientCreateCustomActionTypeOutputArtifactDetailsTypeDef = TypedDict(
    "_RequiredClientCreateCustomActionTypeOutputArtifactDetailsTypeDef", {"minimumCount": int}
)
_OptionalClientCreateCustomActionTypeOutputArtifactDetailsTypeDef = TypedDict(
    "_OptionalClientCreateCustomActionTypeOutputArtifactDetailsTypeDef",
    {"maximumCount": int},
    total=False,
)


class ClientCreateCustomActionTypeOutputArtifactDetailsTypeDef(
    _RequiredClientCreateCustomActionTypeOutputArtifactDetailsTypeDef,
    _OptionalClientCreateCustomActionTypeOutputArtifactDetailsTypeDef,
):
    pass


ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef = TypedDict(
    "ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": bool,
        "description": str,
        "type": Literal["String", "Number", "Boolean"],
    },
    total=False,
)

ClientCreateCustomActionTypeResponseactionTypeidTypeDef = TypedDict(
    "ClientCreateCustomActionTypeResponseactionTypeidTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef = TypedDict(
    "ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)

ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef = TypedDict(
    "ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)

ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef = TypedDict(
    "ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

ClientCreateCustomActionTypeResponseactionTypeTypeDef = TypedDict(
    "ClientCreateCustomActionTypeResponseactionTypeTypeDef",
    {
        "id": ClientCreateCustomActionTypeResponseactionTypeidTypeDef,
        "settings": ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef,
        "actionConfigurationProperties": List[
            ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef
        ],
        "inputArtifactDetails": ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef,
        "outputArtifactDetails": ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef,
    },
    total=False,
)

ClientCreateCustomActionTypeResponsetagsTypeDef = TypedDict(
    "ClientCreateCustomActionTypeResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateCustomActionTypeResponseTypeDef = TypedDict(
    "ClientCreateCustomActionTypeResponseTypeDef",
    {
        "actionType": ClientCreateCustomActionTypeResponseactionTypeTypeDef,
        "tags": List[ClientCreateCustomActionTypeResponsetagsTypeDef],
    },
    total=False,
)

ClientCreateCustomActionTypeSettingsTypeDef = TypedDict(
    "ClientCreateCustomActionTypeSettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

_RequiredClientCreateCustomActionTypeTagsTypeDef = TypedDict(
    "_RequiredClientCreateCustomActionTypeTagsTypeDef", {"key": str}
)
_OptionalClientCreateCustomActionTypeTagsTypeDef = TypedDict(
    "_OptionalClientCreateCustomActionTypeTagsTypeDef", {"value": str}, total=False
)


class ClientCreateCustomActionTypeTagsTypeDef(
    _RequiredClientCreateCustomActionTypeTagsTypeDef,
    _OptionalClientCreateCustomActionTypeTagsTypeDef,
):
    pass


ClientCreatePipelinePipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "ClientCreatePipelinePipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientCreatePipelinePipelineartifactStoreTypeDef = TypedDict(
    "ClientCreatePipelinePipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelinePipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)

ClientCreatePipelinePipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "ClientCreatePipelinePipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientCreatePipelinePipelineartifactStoresTypeDef = TypedDict(
    "ClientCreatePipelinePipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelinePipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)

ClientCreatePipelinePipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "ClientCreatePipelinePipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientCreatePipelinePipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "ClientCreatePipelinePipelinestagesactionsinputArtifactsTypeDef", {"name": str}, total=False
)

ClientCreatePipelinePipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "ClientCreatePipelinePipelinestagesactionsoutputArtifactsTypeDef", {"name": str}, total=False
)

ClientCreatePipelinePipelinestagesactionsTypeDef = TypedDict(
    "ClientCreatePipelinePipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientCreatePipelinePipelinestagesactionsactionTypeIdTypeDef,
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[ClientCreatePipelinePipelinestagesactionsoutputArtifactsTypeDef],
        "inputArtifacts": List[ClientCreatePipelinePipelinestagesactionsinputArtifactsTypeDef],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)

ClientCreatePipelinePipelinestagesblockersTypeDef = TypedDict(
    "ClientCreatePipelinePipelinestagesblockersTypeDef", {"name": str, "type": str}, total=False
)

ClientCreatePipelinePipelinestagesTypeDef = TypedDict(
    "ClientCreatePipelinePipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientCreatePipelinePipelinestagesblockersTypeDef],
        "actions": List[ClientCreatePipelinePipelinestagesactionsTypeDef],
    },
    total=False,
)

_RequiredClientCreatePipelinePipelineTypeDef = TypedDict(
    "_RequiredClientCreatePipelinePipelineTypeDef", {"name": str}
)
_OptionalClientCreatePipelinePipelineTypeDef = TypedDict(
    "_OptionalClientCreatePipelinePipelineTypeDef",
    {
        "roleArn": str,
        "artifactStore": ClientCreatePipelinePipelineartifactStoreTypeDef,
        "artifactStores": Dict[str, ClientCreatePipelinePipelineartifactStoresTypeDef],
        "stages": List[ClientCreatePipelinePipelinestagesTypeDef],
        "version": int,
    },
    total=False,
)


class ClientCreatePipelinePipelineTypeDef(
    _RequiredClientCreatePipelinePipelineTypeDef, _OptionalClientCreatePipelinePipelineTypeDef
):
    pass


ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientCreatePipelineResponsepipelineartifactStoreTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)

ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientCreatePipelineResponsepipelineartifactStoresTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)

ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    {"name": str},
    total=False,
)

ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    {"name": str},
    total=False,
)

ClientCreatePipelineResponsepipelinestagesactionsTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef,
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[
            ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
        ],
        "inputArtifacts": List[
            ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef
        ],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)

ClientCreatePipelineResponsepipelinestagesblockersTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelinestagesblockersTypeDef",
    {"name": str, "type": str},
    total=False,
)

ClientCreatePipelineResponsepipelinestagesTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientCreatePipelineResponsepipelinestagesblockersTypeDef],
        "actions": List[ClientCreatePipelineResponsepipelinestagesactionsTypeDef],
    },
    total=False,
)

ClientCreatePipelineResponsepipelineTypeDef = TypedDict(
    "ClientCreatePipelineResponsepipelineTypeDef",
    {
        "name": str,
        "roleArn": str,
        "artifactStore": ClientCreatePipelineResponsepipelineartifactStoreTypeDef,
        "artifactStores": Dict[str, ClientCreatePipelineResponsepipelineartifactStoresTypeDef],
        "stages": List[ClientCreatePipelineResponsepipelinestagesTypeDef],
        "version": int,
    },
    total=False,
)

ClientCreatePipelineResponsetagsTypeDef = TypedDict(
    "ClientCreatePipelineResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreatePipelineResponseTypeDef = TypedDict(
    "ClientCreatePipelineResponseTypeDef",
    {
        "pipeline": ClientCreatePipelineResponsepipelineTypeDef,
        "tags": List[ClientCreatePipelineResponsetagsTypeDef],
    },
    total=False,
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


ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    {"configuration": Dict[str, str]},
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef,
    },
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef,
    },
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef,
    },
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef,
    },
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    {"name": str, "actionExecutionId": str},
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    {"name": str},
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef,
        "action": ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)

ClientGetJobDetailsResponsejobDetailsdataTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsdataTypeDef",
    {
        "actionTypeId": ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef,
        "actionConfiguration": ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef,
        "pipelineContext": ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef,
        "inputArtifacts": List[ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef],
        "outputArtifacts": List[ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef],
        "artifactCredentials": ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef,
        "continuationToken": str,
        "encryptionKey": ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef,
    },
    total=False,
)

ClientGetJobDetailsResponsejobDetailsTypeDef = TypedDict(
    "ClientGetJobDetailsResponsejobDetailsTypeDef",
    {"id": str, "data": ClientGetJobDetailsResponsejobDetailsdataTypeDef, "accountId": str},
    total=False,
)

ClientGetJobDetailsResponseTypeDef = TypedDict(
    "ClientGetJobDetailsResponseTypeDef",
    {"jobDetails": ClientGetJobDetailsResponsejobDetailsTypeDef},
    total=False,
)

ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef = TypedDict(
    "ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef",
    {
        "name": str,
        "revisionId": str,
        "revisionChangeIdentifier": str,
        "revisionSummary": str,
        "created": datetime,
        "revisionUrl": str,
    },
    total=False,
)

ClientGetPipelineExecutionResponsepipelineExecutionTypeDef = TypedDict(
    "ClientGetPipelineExecutionResponsepipelineExecutionTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "pipelineExecutionId": str,
        "status": Literal["InProgress", "Succeeded", "Superseded", "Failed"],
        "artifactRevisions": List[
            ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef
        ],
    },
    total=False,
)

ClientGetPipelineExecutionResponseTypeDef = TypedDict(
    "ClientGetPipelineExecutionResponseTypeDef",
    {"pipelineExecution": ClientGetPipelineExecutionResponsepipelineExecutionTypeDef},
    total=False,
)

ClientGetPipelineResponsemetadataTypeDef = TypedDict(
    "ClientGetPipelineResponsemetadataTypeDef",
    {"pipelineArn": str, "created": datetime, "updated": datetime},
    total=False,
)

ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientGetPipelineResponsepipelineartifactStoreTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)

ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientGetPipelineResponsepipelineartifactStoresTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)

ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    {"name": str},
    total=False,
)

ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    {"name": str},
    total=False,
)

ClientGetPipelineResponsepipelinestagesactionsTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef,
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[
            ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
        ],
        "inputArtifacts": List[ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)

ClientGetPipelineResponsepipelinestagesblockersTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelinestagesblockersTypeDef",
    {"name": str, "type": str},
    total=False,
)

ClientGetPipelineResponsepipelinestagesTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientGetPipelineResponsepipelinestagesblockersTypeDef],
        "actions": List[ClientGetPipelineResponsepipelinestagesactionsTypeDef],
    },
    total=False,
)

ClientGetPipelineResponsepipelineTypeDef = TypedDict(
    "ClientGetPipelineResponsepipelineTypeDef",
    {
        "name": str,
        "roleArn": str,
        "artifactStore": ClientGetPipelineResponsepipelineartifactStoreTypeDef,
        "artifactStores": Dict[str, ClientGetPipelineResponsepipelineartifactStoresTypeDef],
        "stages": List[ClientGetPipelineResponsepipelinestagesTypeDef],
        "version": int,
    },
    total=False,
)

ClientGetPipelineResponseTypeDef = TypedDict(
    "ClientGetPipelineResponseTypeDef",
    {
        "pipeline": ClientGetPipelineResponsepipelineTypeDef,
        "metadata": ClientGetPipelineResponsemetadataTypeDef,
    },
    total=False,
)

ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef = TypedDict(
    "ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef",
    {"revisionId": str, "revisionChangeId": str, "created": datetime},
    total=False,
)

ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef = TypedDict(
    "ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef",
    {"code": str, "message": str},
    total=False,
)

ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef = TypedDict(
    "ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef",
    {
        "status": Literal["InProgress", "Succeeded", "Failed"],
        "summary": str,
        "lastStatusChange": datetime,
        "token": str,
        "lastUpdatedBy": str,
        "externalExecutionId": str,
        "externalExecutionUrl": str,
        "percentComplete": int,
        "errorDetails": ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef,
    },
    total=False,
)

ClientGetPipelineStateResponsestageStatesactionStatesTypeDef = TypedDict(
    "ClientGetPipelineStateResponsestageStatesactionStatesTypeDef",
    {
        "actionName": str,
        "currentRevision": ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef,
        "latestExecution": ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef,
        "entityUrl": str,
        "revisionUrl": str,
    },
    total=False,
)

ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef = TypedDict(
    "ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef",
    {"enabled": bool, "lastChangedBy": str, "lastChangedAt": datetime, "disabledReason": str},
    total=False,
)

ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef = TypedDict(
    "ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef",
    {"pipelineExecutionId": str, "status": Literal["InProgress", "Failed", "Succeeded"]},
    total=False,
)

ClientGetPipelineStateResponsestageStatesTypeDef = TypedDict(
    "ClientGetPipelineStateResponsestageStatesTypeDef",
    {
        "stageName": str,
        "inboundTransitionState": ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef,
        "actionStates": List[ClientGetPipelineStateResponsestageStatesactionStatesTypeDef],
        "latestExecution": ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef,
    },
    total=False,
)

ClientGetPipelineStateResponseTypeDef = TypedDict(
    "ClientGetPipelineStateResponseTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "stageStates": List[ClientGetPipelineStateResponsestageStatesTypeDef],
        "created": datetime,
        "updated": datetime,
    },
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    {"configuration": Dict[str, str]},
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef,
    },
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef,
    },
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef,
    },
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef,
    },
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    {"name": str, "actionExecutionId": str},
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    {"name": str},
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef,
        "action": ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef",
    {
        "actionTypeId": ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef,
        "actionConfiguration": ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef,
        "pipelineContext": ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef,
        "inputArtifacts": List[
            ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef
        ],
        "outputArtifacts": List[
            ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef
        ],
        "artifactCredentials": ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef,
        "continuationToken": str,
        "encryptionKey": ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef,
    },
    total=False,
)

ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef",
    {"id": str, "data": ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef, "nonce": str},
    total=False,
)

ClientGetThirdPartyJobDetailsResponseTypeDef = TypedDict(
    "ClientGetThirdPartyJobDetailsResponseTypeDef",
    {"jobDetails": ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef},
    total=False,
)

ClientListActionExecutionsFilterTypeDef = TypedDict(
    "ClientListActionExecutionsFilterTypeDef", {"pipelineExecutionId": str}, total=False
)

ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef = TypedDict(
    "ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef = TypedDict(
    "ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)

ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef = TypedDict(
    "ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef,
    },
    total=False,
)

ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef = TypedDict(
    "ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef",
    {
        "actionTypeId": ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef,
        "configuration": Dict[str, str],
        "resolvedConfiguration": Dict[str, str],
        "roleArn": str,
        "region": str,
        "inputArtifacts": List[
            ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef
        ],
        "namespace": str,
    },
    total=False,
)

ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef = TypedDict(
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    {"externalExecutionId": str, "externalExecutionSummary": str, "externalExecutionUrl": str},
    total=False,
)

ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef = TypedDict(
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)

ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef = TypedDict(
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef,
    },
    total=False,
)

ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef = TypedDict(
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef",
    {
        "outputArtifacts": List[
            ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
        ],
        "executionResult": ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef,
        "outputVariables": Dict[str, str],
    },
    total=False,
)

ClientListActionExecutionsResponseactionExecutionDetailsTypeDef = TypedDict(
    "ClientListActionExecutionsResponseactionExecutionDetailsTypeDef",
    {
        "pipelineExecutionId": str,
        "actionExecutionId": str,
        "pipelineVersion": int,
        "stageName": str,
        "actionName": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["InProgress", "Succeeded", "Failed"],
        "input": ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef,
        "output": ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef,
    },
    total=False,
)

ClientListActionExecutionsResponseTypeDef = TypedDict(
    "ClientListActionExecutionsResponseTypeDef",
    {
        "actionExecutionDetails": List[
            ClientListActionExecutionsResponseactionExecutionDetailsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef = TypedDict(
    "ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": bool,
        "description": str,
        "type": Literal["String", "Number", "Boolean"],
    },
    total=False,
)

ClientListActionTypesResponseactionTypesidTypeDef = TypedDict(
    "ClientListActionTypesResponseactionTypesidTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef = TypedDict(
    "ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)

ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef = TypedDict(
    "ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)

ClientListActionTypesResponseactionTypessettingsTypeDef = TypedDict(
    "ClientListActionTypesResponseactionTypessettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

ClientListActionTypesResponseactionTypesTypeDef = TypedDict(
    "ClientListActionTypesResponseactionTypesTypeDef",
    {
        "id": ClientListActionTypesResponseactionTypesidTypeDef,
        "settings": ClientListActionTypesResponseactionTypessettingsTypeDef,
        "actionConfigurationProperties": List[
            ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef
        ],
        "inputArtifactDetails": ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef,
        "outputArtifactDetails": ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef,
    },
    total=False,
)

ClientListActionTypesResponseTypeDef = TypedDict(
    "ClientListActionTypesResponseTypeDef",
    {"actionTypes": List[ClientListActionTypesResponseactionTypesTypeDef], "nextToken": str},
    total=False,
)

ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef = TypedDict(
    "ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    {"actionName": str, "revisionId": str, "revisionSummary": str, "revisionUrl": str},
    total=False,
)

ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef = TypedDict(
    "ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef",
    {
        "triggerType": Literal[
            "CreatePipeline",
            "StartPipelineExecution",
            "PollForSourceChanges",
            "Webhook",
            "CloudWatchEvent",
            "PutActionRevision",
        ],
        "triggerDetail": str,
    },
    total=False,
)

ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef = TypedDict(
    "ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef",
    {
        "pipelineExecutionId": str,
        "status": Literal["InProgress", "Succeeded", "Superseded", "Failed"],
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "sourceRevisions": List[
            ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef
        ],
        "trigger": ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef,
    },
    total=False,
)

ClientListPipelineExecutionsResponseTypeDef = TypedDict(
    "ClientListPipelineExecutionsResponseTypeDef",
    {
        "pipelineExecutionSummaries": List[
            ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListPipelinesResponsepipelinesTypeDef = TypedDict(
    "ClientListPipelinesResponsepipelinesTypeDef",
    {"name": str, "version": int, "created": datetime, "updated": datetime},
    total=False,
)

ClientListPipelinesResponseTypeDef = TypedDict(
    "ClientListPipelinesResponseTypeDef",
    {"pipelines": List[ClientListPipelinesResponsepipelinesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef], "nextToken": str},
    total=False,
)

ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef = TypedDict(
    "ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)

ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef = TypedDict(
    "ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef",
    {"jsonPath": str, "matchEquals": str},
    total=False,
)

ClientListWebhooksResponsewebhooksdefinitionTypeDef = TypedDict(
    "ClientListWebhooksResponsewebhooksdefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef],
        "authentication": Literal["GITHUB_HMAC", "IP", "UNAUTHENTICATED"],
        "authenticationConfiguration": ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef,
    },
    total=False,
)

ClientListWebhooksResponsewebhookstagsTypeDef = TypedDict(
    "ClientListWebhooksResponsewebhookstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListWebhooksResponsewebhooksTypeDef = TypedDict(
    "ClientListWebhooksResponsewebhooksTypeDef",
    {
        "definition": ClientListWebhooksResponsewebhooksdefinitionTypeDef,
        "url": str,
        "errorMessage": str,
        "errorCode": str,
        "lastTriggered": datetime,
        "arn": str,
        "tags": List[ClientListWebhooksResponsewebhookstagsTypeDef],
    },
    total=False,
)

ClientListWebhooksResponseTypeDef = TypedDict(
    "ClientListWebhooksResponseTypeDef",
    {"webhooks": List[ClientListWebhooksResponsewebhooksTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientPollForJobsActionTypeIdTypeDef = TypedDict(
    "_RequiredClientPollForJobsActionTypeIdTypeDef",
    {"category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"]},
)
_OptionalClientPollForJobsActionTypeIdTypeDef = TypedDict(
    "_OptionalClientPollForJobsActionTypeIdTypeDef",
    {"owner": Literal["AWS", "ThirdParty", "Custom"], "provider": str, "version": str},
    total=False,
)


class ClientPollForJobsActionTypeIdTypeDef(
    _RequiredClientPollForJobsActionTypeIdTypeDef, _OptionalClientPollForJobsActionTypeIdTypeDef
):
    pass


ClientPollForJobsResponsejobsdataactionConfigurationTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdataactionConfigurationTypeDef",
    {"configuration": Dict[str, str]},
    total=False,
)

ClientPollForJobsResponsejobsdataactionTypeIdTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdataactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
    total=False,
)

ClientPollForJobsResponsejobsdataencryptionKeyTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdataencryptionKeyTypeDef", {"id": str, "type": str}, total=False
)

ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)

ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef,
    },
    total=False,
)

ClientPollForJobsResponsejobsdatainputArtifactsTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdatainputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef,
    },
    total=False,
)

ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)

ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef,
    },
    total=False,
)

ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef,
    },
    total=False,
)

ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef",
    {"name": str, "actionExecutionId": str},
    total=False,
)

ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef", {"name": str}, total=False
)

ClientPollForJobsResponsejobsdatapipelineContextTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdatapipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef,
        "action": ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)

ClientPollForJobsResponsejobsdataTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsdataTypeDef",
    {
        "actionTypeId": ClientPollForJobsResponsejobsdataactionTypeIdTypeDef,
        "actionConfiguration": ClientPollForJobsResponsejobsdataactionConfigurationTypeDef,
        "pipelineContext": ClientPollForJobsResponsejobsdatapipelineContextTypeDef,
        "inputArtifacts": List[ClientPollForJobsResponsejobsdatainputArtifactsTypeDef],
        "outputArtifacts": List[ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef],
        "artifactCredentials": ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef,
        "continuationToken": str,
        "encryptionKey": ClientPollForJobsResponsejobsdataencryptionKeyTypeDef,
    },
    total=False,
)

ClientPollForJobsResponsejobsTypeDef = TypedDict(
    "ClientPollForJobsResponsejobsTypeDef",
    {"id": str, "data": ClientPollForJobsResponsejobsdataTypeDef, "nonce": str, "accountId": str},
    total=False,
)

ClientPollForJobsResponseTypeDef = TypedDict(
    "ClientPollForJobsResponseTypeDef",
    {"jobs": List[ClientPollForJobsResponsejobsTypeDef]},
    total=False,
)

_RequiredClientPollForThirdPartyJobsActionTypeIdTypeDef = TypedDict(
    "_RequiredClientPollForThirdPartyJobsActionTypeIdTypeDef",
    {"category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"]},
)
_OptionalClientPollForThirdPartyJobsActionTypeIdTypeDef = TypedDict(
    "_OptionalClientPollForThirdPartyJobsActionTypeIdTypeDef",
    {"owner": Literal["AWS", "ThirdParty", "Custom"], "provider": str, "version": str},
    total=False,
)


class ClientPollForThirdPartyJobsActionTypeIdTypeDef(
    _RequiredClientPollForThirdPartyJobsActionTypeIdTypeDef,
    _OptionalClientPollForThirdPartyJobsActionTypeIdTypeDef,
):
    pass


ClientPollForThirdPartyJobsResponsejobsTypeDef = TypedDict(
    "ClientPollForThirdPartyJobsResponsejobsTypeDef", {"clientId": str, "jobId": str}, total=False
)

ClientPollForThirdPartyJobsResponseTypeDef = TypedDict(
    "ClientPollForThirdPartyJobsResponseTypeDef",
    {"jobs": List[ClientPollForThirdPartyJobsResponsejobsTypeDef]},
    total=False,
)

_RequiredClientPutActionRevisionActionRevisionTypeDef = TypedDict(
    "_RequiredClientPutActionRevisionActionRevisionTypeDef", {"revisionId": str}
)
_OptionalClientPutActionRevisionActionRevisionTypeDef = TypedDict(
    "_OptionalClientPutActionRevisionActionRevisionTypeDef",
    {"revisionChangeId": str, "created": datetime},
    total=False,
)


class ClientPutActionRevisionActionRevisionTypeDef(
    _RequiredClientPutActionRevisionActionRevisionTypeDef,
    _OptionalClientPutActionRevisionActionRevisionTypeDef,
):
    pass


ClientPutActionRevisionResponseTypeDef = TypedDict(
    "ClientPutActionRevisionResponseTypeDef",
    {"newRevision": bool, "pipelineExecutionId": str},
    total=False,
)

ClientPutApprovalResultResponseTypeDef = TypedDict(
    "ClientPutApprovalResultResponseTypeDef", {"approvedAt": datetime}, total=False
)

_RequiredClientPutApprovalResultResultTypeDef = TypedDict(
    "_RequiredClientPutApprovalResultResultTypeDef", {"summary": str}
)
_OptionalClientPutApprovalResultResultTypeDef = TypedDict(
    "_OptionalClientPutApprovalResultResultTypeDef",
    {"status": Literal["Approved", "Rejected"]},
    total=False,
)


class ClientPutApprovalResultResultTypeDef(
    _RequiredClientPutApprovalResultResultTypeDef, _OptionalClientPutApprovalResultResultTypeDef
):
    pass


_RequiredClientPutJobFailureResultFailureDetailsTypeDef = TypedDict(
    "_RequiredClientPutJobFailureResultFailureDetailsTypeDef",
    {
        "type": Literal[
            "JobFailed",
            "ConfigurationError",
            "PermissionError",
            "RevisionOutOfSync",
            "RevisionUnavailable",
            "SystemUnavailable",
        ]
    },
)
_OptionalClientPutJobFailureResultFailureDetailsTypeDef = TypedDict(
    "_OptionalClientPutJobFailureResultFailureDetailsTypeDef",
    {"message": str, "externalExecutionId": str},
    total=False,
)


class ClientPutJobFailureResultFailureDetailsTypeDef(
    _RequiredClientPutJobFailureResultFailureDetailsTypeDef,
    _OptionalClientPutJobFailureResultFailureDetailsTypeDef,
):
    pass


_RequiredClientPutJobSuccessResultCurrentRevisionTypeDef = TypedDict(
    "_RequiredClientPutJobSuccessResultCurrentRevisionTypeDef", {"revision": str}
)
_OptionalClientPutJobSuccessResultCurrentRevisionTypeDef = TypedDict(
    "_OptionalClientPutJobSuccessResultCurrentRevisionTypeDef",
    {"changeIdentifier": str, "created": datetime, "revisionSummary": str},
    total=False,
)


class ClientPutJobSuccessResultCurrentRevisionTypeDef(
    _RequiredClientPutJobSuccessResultCurrentRevisionTypeDef,
    _OptionalClientPutJobSuccessResultCurrentRevisionTypeDef,
):
    pass


ClientPutJobSuccessResultExecutionDetailsTypeDef = TypedDict(
    "ClientPutJobSuccessResultExecutionDetailsTypeDef",
    {"summary": str, "externalExecutionId": str, "percentComplete": int},
    total=False,
)

_RequiredClientPutThirdPartyJobFailureResultFailureDetailsTypeDef = TypedDict(
    "_RequiredClientPutThirdPartyJobFailureResultFailureDetailsTypeDef",
    {
        "type": Literal[
            "JobFailed",
            "ConfigurationError",
            "PermissionError",
            "RevisionOutOfSync",
            "RevisionUnavailable",
            "SystemUnavailable",
        ]
    },
)
_OptionalClientPutThirdPartyJobFailureResultFailureDetailsTypeDef = TypedDict(
    "_OptionalClientPutThirdPartyJobFailureResultFailureDetailsTypeDef",
    {"message": str, "externalExecutionId": str},
    total=False,
)


class ClientPutThirdPartyJobFailureResultFailureDetailsTypeDef(
    _RequiredClientPutThirdPartyJobFailureResultFailureDetailsTypeDef,
    _OptionalClientPutThirdPartyJobFailureResultFailureDetailsTypeDef,
):
    pass


_RequiredClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef = TypedDict(
    "_RequiredClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef", {"revision": str}
)
_OptionalClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef = TypedDict(
    "_OptionalClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef",
    {"changeIdentifier": str, "created": datetime, "revisionSummary": str},
    total=False,
)


class ClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef(
    _RequiredClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef,
    _OptionalClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef,
):
    pass


ClientPutThirdPartyJobSuccessResultExecutionDetailsTypeDef = TypedDict(
    "ClientPutThirdPartyJobSuccessResultExecutionDetailsTypeDef",
    {"summary": str, "externalExecutionId": str, "percentComplete": int},
    total=False,
)

ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef = TypedDict(
    "ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)

ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef = TypedDict(
    "ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef",
    {"jsonPath": str, "matchEquals": str},
    total=False,
)

ClientPutWebhookResponsewebhookdefinitionTypeDef = TypedDict(
    "ClientPutWebhookResponsewebhookdefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef],
        "authentication": Literal["GITHUB_HMAC", "IP", "UNAUTHENTICATED"],
        "authenticationConfiguration": ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef,
    },
    total=False,
)

ClientPutWebhookResponsewebhooktagsTypeDef = TypedDict(
    "ClientPutWebhookResponsewebhooktagsTypeDef", {"key": str, "value": str}, total=False
)

ClientPutWebhookResponsewebhookTypeDef = TypedDict(
    "ClientPutWebhookResponsewebhookTypeDef",
    {
        "definition": ClientPutWebhookResponsewebhookdefinitionTypeDef,
        "url": str,
        "errorMessage": str,
        "errorCode": str,
        "lastTriggered": datetime,
        "arn": str,
        "tags": List[ClientPutWebhookResponsewebhooktagsTypeDef],
    },
    total=False,
)

ClientPutWebhookResponseTypeDef = TypedDict(
    "ClientPutWebhookResponseTypeDef",
    {"webhook": ClientPutWebhookResponsewebhookTypeDef},
    total=False,
)

_RequiredClientPutWebhookTagsTypeDef = TypedDict(
    "_RequiredClientPutWebhookTagsTypeDef", {"key": str}
)
_OptionalClientPutWebhookTagsTypeDef = TypedDict(
    "_OptionalClientPutWebhookTagsTypeDef", {"value": str}, total=False
)


class ClientPutWebhookTagsTypeDef(
    _RequiredClientPutWebhookTagsTypeDef, _OptionalClientPutWebhookTagsTypeDef
):
    pass


ClientPutWebhookWebhookauthenticationConfigurationTypeDef = TypedDict(
    "ClientPutWebhookWebhookauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)

ClientPutWebhookWebhookfiltersTypeDef = TypedDict(
    "ClientPutWebhookWebhookfiltersTypeDef", {"jsonPath": str, "matchEquals": str}, total=False
)

_RequiredClientPutWebhookWebhookTypeDef = TypedDict(
    "_RequiredClientPutWebhookWebhookTypeDef", {"name": str}
)
_OptionalClientPutWebhookWebhookTypeDef = TypedDict(
    "_OptionalClientPutWebhookWebhookTypeDef",
    {
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[ClientPutWebhookWebhookfiltersTypeDef],
        "authentication": Literal["GITHUB_HMAC", "IP", "UNAUTHENTICATED"],
        "authenticationConfiguration": ClientPutWebhookWebhookauthenticationConfigurationTypeDef,
    },
    total=False,
)


class ClientPutWebhookWebhookTypeDef(
    _RequiredClientPutWebhookWebhookTypeDef, _OptionalClientPutWebhookWebhookTypeDef
):
    pass


ClientRetryStageExecutionResponseTypeDef = TypedDict(
    "ClientRetryStageExecutionResponseTypeDef", {"pipelineExecutionId": str}, total=False
)

ClientStartPipelineExecutionResponseTypeDef = TypedDict(
    "ClientStartPipelineExecutionResponseTypeDef", {"pipelineExecutionId": str}, total=False
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdatePipelinePipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientUpdatePipelinePipelineartifactStoreTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelinePipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)

ClientUpdatePipelinePipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientUpdatePipelinePipelineartifactStoresTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelinePipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)

ClientUpdatePipelinePipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "ClientUpdatePipelinePipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientUpdatePipelinePipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "ClientUpdatePipelinePipelinestagesactionsinputArtifactsTypeDef", {"name": str}, total=False
)

ClientUpdatePipelinePipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "ClientUpdatePipelinePipelinestagesactionsoutputArtifactsTypeDef", {"name": str}, total=False
)

ClientUpdatePipelinePipelinestagesactionsTypeDef = TypedDict(
    "ClientUpdatePipelinePipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientUpdatePipelinePipelinestagesactionsactionTypeIdTypeDef,
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[ClientUpdatePipelinePipelinestagesactionsoutputArtifactsTypeDef],
        "inputArtifacts": List[ClientUpdatePipelinePipelinestagesactionsinputArtifactsTypeDef],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)

ClientUpdatePipelinePipelinestagesblockersTypeDef = TypedDict(
    "ClientUpdatePipelinePipelinestagesblockersTypeDef", {"name": str, "type": str}, total=False
)

ClientUpdatePipelinePipelinestagesTypeDef = TypedDict(
    "ClientUpdatePipelinePipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientUpdatePipelinePipelinestagesblockersTypeDef],
        "actions": List[ClientUpdatePipelinePipelinestagesactionsTypeDef],
    },
    total=False,
)

_RequiredClientUpdatePipelinePipelineTypeDef = TypedDict(
    "_RequiredClientUpdatePipelinePipelineTypeDef", {"name": str}
)
_OptionalClientUpdatePipelinePipelineTypeDef = TypedDict(
    "_OptionalClientUpdatePipelinePipelineTypeDef",
    {
        "roleArn": str,
        "artifactStore": ClientUpdatePipelinePipelineartifactStoreTypeDef,
        "artifactStores": Dict[str, ClientUpdatePipelinePipelineartifactStoresTypeDef],
        "stages": List[ClientUpdatePipelinePipelinestagesTypeDef],
        "version": int,
    },
    total=False,
)


class ClientUpdatePipelinePipelineTypeDef(
    _RequiredClientUpdatePipelinePipelineTypeDef, _OptionalClientUpdatePipelinePipelineTypeDef
):
    pass


ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientUpdatePipelineResponsepipelineartifactStoreTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)

ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)

ClientUpdatePipelineResponsepipelineartifactStoresTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)

ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    {"name": str},
    total=False,
)

ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    {"name": str},
    total=False,
)

ClientUpdatePipelineResponsepipelinestagesactionsTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelinestagesactionsTypeDef",
    {
        "name": str,
        "actionTypeId": ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef,
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List[
            ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
        ],
        "inputArtifacts": List[
            ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef
        ],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)

ClientUpdatePipelineResponsepipelinestagesblockersTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelinestagesblockersTypeDef",
    {"name": str, "type": str},
    total=False,
)

ClientUpdatePipelineResponsepipelinestagesTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientUpdatePipelineResponsepipelinestagesblockersTypeDef],
        "actions": List[ClientUpdatePipelineResponsepipelinestagesactionsTypeDef],
    },
    total=False,
)

ClientUpdatePipelineResponsepipelineTypeDef = TypedDict(
    "ClientUpdatePipelineResponsepipelineTypeDef",
    {
        "name": str,
        "roleArn": str,
        "artifactStore": ClientUpdatePipelineResponsepipelineartifactStoreTypeDef,
        "artifactStores": Dict[str, ClientUpdatePipelineResponsepipelineartifactStoresTypeDef],
        "stages": List[ClientUpdatePipelineResponsepipelinestagesTypeDef],
        "version": int,
    },
    total=False,
)

ClientUpdatePipelineResponseTypeDef = TypedDict(
    "ClientUpdatePipelineResponseTypeDef",
    {"pipeline": ClientUpdatePipelineResponsepipelineTypeDef},
    total=False,
)

ListActionExecutionsPaginateFilterTypeDef = TypedDict(
    "ListActionExecutionsPaginateFilterTypeDef", {"pipelineExecutionId": str}, total=False
)

ListActionExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListActionExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)

ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef,
    },
    total=False,
)

ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef",
    {
        "actionTypeId": ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef,
        "configuration": Dict[str, str],
        "resolvedConfiguration": Dict[str, str],
        "roleArn": str,
        "region": str,
        "inputArtifacts": List[
            ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef
        ],
        "namespace": str,
    },
    total=False,
)

ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    {"externalExecutionId": str, "externalExecutionSummary": str, "externalExecutionUrl": str},
    total=False,
)

ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)

ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef,
    },
    total=False,
)

ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef",
    {
        "outputArtifacts": List[
            ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
        ],
        "executionResult": ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef,
        "outputVariables": Dict[str, str],
    },
    total=False,
)

ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef",
    {
        "pipelineExecutionId": str,
        "actionExecutionId": str,
        "pipelineVersion": int,
        "stageName": str,
        "actionName": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["InProgress", "Succeeded", "Failed"],
        "input": ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef,
        "output": ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef,
    },
    total=False,
)

ListActionExecutionsPaginateResponseTypeDef = TypedDict(
    "ListActionExecutionsPaginateResponseTypeDef",
    {
        "actionExecutionDetails": List[
            ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListActionTypesPaginatePaginationConfigTypeDef = TypedDict(
    "ListActionTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef = TypedDict(
    "ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": bool,
        "description": str,
        "type": Literal["String", "Number", "Boolean"],
    },
    total=False,
)

ListActionTypesPaginateResponseactionTypesidTypeDef = TypedDict(
    "ListActionTypesPaginateResponseactionTypesidTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)

ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef = TypedDict(
    "ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)

ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef = TypedDict(
    "ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)

ListActionTypesPaginateResponseactionTypessettingsTypeDef = TypedDict(
    "ListActionTypesPaginateResponseactionTypessettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

ListActionTypesPaginateResponseactionTypesTypeDef = TypedDict(
    "ListActionTypesPaginateResponseactionTypesTypeDef",
    {
        "id": ListActionTypesPaginateResponseactionTypesidTypeDef,
        "settings": ListActionTypesPaginateResponseactionTypessettingsTypeDef,
        "actionConfigurationProperties": List[
            ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef
        ],
        "inputArtifactDetails": ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef,
        "outputArtifactDetails": ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef,
    },
    total=False,
)

ListActionTypesPaginateResponseTypeDef = TypedDict(
    "ListActionTypesPaginateResponseTypeDef",
    {"actionTypes": List[ListActionTypesPaginateResponseactionTypesTypeDef], "NextToken": str},
    total=False,
)

ListPipelineExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPipelineExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef = TypedDict(
    "ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    {"actionName": str, "revisionId": str, "revisionSummary": str, "revisionUrl": str},
    total=False,
)

ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef = TypedDict(
    "ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef",
    {
        "triggerType": Literal[
            "CreatePipeline",
            "StartPipelineExecution",
            "PollForSourceChanges",
            "Webhook",
            "CloudWatchEvent",
            "PutActionRevision",
        ],
        "triggerDetail": str,
    },
    total=False,
)

ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef = TypedDict(
    "ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef",
    {
        "pipelineExecutionId": str,
        "status": Literal["InProgress", "Succeeded", "Superseded", "Failed"],
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "sourceRevisions": List[
            ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef
        ],
        "trigger": ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef,
    },
    total=False,
)

ListPipelineExecutionsPaginateResponseTypeDef = TypedDict(
    "ListPipelineExecutionsPaginateResponseTypeDef",
    {
        "pipelineExecutionSummaries": List[
            ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListPipelinesPaginatePaginationConfigTypeDef = TypedDict(
    "ListPipelinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListPipelinesPaginateResponsepipelinesTypeDef = TypedDict(
    "ListPipelinesPaginateResponsepipelinesTypeDef",
    {"name": str, "version": int, "created": datetime, "updated": datetime},
    total=False,
)

ListPipelinesPaginateResponseTypeDef = TypedDict(
    "ListPipelinesPaginateResponseTypeDef",
    {"pipelines": List[ListPipelinesPaginateResponsepipelinesTypeDef], "NextToken": str},
    total=False,
)

ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "ListTagsForResourcePaginateResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)

ListWebhooksPaginatePaginationConfigTypeDef = TypedDict(
    "ListWebhooksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef = TypedDict(
    "ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)

ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef = TypedDict(
    "ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef",
    {"jsonPath": str, "matchEquals": str},
    total=False,
)

ListWebhooksPaginateResponsewebhooksdefinitionTypeDef = TypedDict(
    "ListWebhooksPaginateResponsewebhooksdefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef],
        "authentication": Literal["GITHUB_HMAC", "IP", "UNAUTHENTICATED"],
        "authenticationConfiguration": ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef,
    },
    total=False,
)

ListWebhooksPaginateResponsewebhookstagsTypeDef = TypedDict(
    "ListWebhooksPaginateResponsewebhookstagsTypeDef", {"key": str, "value": str}, total=False
)

ListWebhooksPaginateResponsewebhooksTypeDef = TypedDict(
    "ListWebhooksPaginateResponsewebhooksTypeDef",
    {
        "definition": ListWebhooksPaginateResponsewebhooksdefinitionTypeDef,
        "url": str,
        "errorMessage": str,
        "errorCode": str,
        "lastTriggered": datetime,
        "arn": str,
        "tags": List[ListWebhooksPaginateResponsewebhookstagsTypeDef],
    },
    total=False,
)

ListWebhooksPaginateResponseTypeDef = TypedDict(
    "ListWebhooksPaginateResponseTypeDef",
    {"webhooks": List[ListWebhooksPaginateResponsewebhooksTypeDef]},
    total=False,
)
