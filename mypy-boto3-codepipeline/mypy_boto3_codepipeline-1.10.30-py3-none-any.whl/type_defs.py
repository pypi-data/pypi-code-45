"Main interface for codepipeline service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAcknowledgeJobResponseTypeDef",
    "ClientAcknowledgeThirdPartyJobResponseTypeDef",
    "ClientCreateCustomActionTypeConfigurationPropertiesTypeDef",
    "ClientCreateCustomActionTypeInputArtifactDetailsTypeDef",
    "ClientCreateCustomActionTypeOutputArtifactDetailsTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeidTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef",
    "ClientCreateCustomActionTypeResponseactionTypeTypeDef",
    "ClientCreateCustomActionTypeResponsetagsTypeDef",
    "ClientCreateCustomActionTypeResponseTypeDef",
    "ClientCreateCustomActionTypeSettingsTypeDef",
    "ClientCreateCustomActionTypeTagsTypeDef",
    "ClientCreatePipelinePipelineartifactStoreencryptionKeyTypeDef",
    "ClientCreatePipelinePipelineartifactStoreTypeDef",
    "ClientCreatePipelinePipelineartifactStoresencryptionKeyTypeDef",
    "ClientCreatePipelinePipelineartifactStoresTypeDef",
    "ClientCreatePipelinePipelinestagesactionsactionTypeIdTypeDef",
    "ClientCreatePipelinePipelinestagesactionsinputArtifactsTypeDef",
    "ClientCreatePipelinePipelinestagesactionsoutputArtifactsTypeDef",
    "ClientCreatePipelinePipelinestagesactionsTypeDef",
    "ClientCreatePipelinePipelinestagesblockersTypeDef",
    "ClientCreatePipelinePipelinestagesTypeDef",
    "ClientCreatePipelinePipelineTypeDef",
    "ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    "ClientCreatePipelineResponsepipelineartifactStoreTypeDef",
    "ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    "ClientCreatePipelineResponsepipelineartifactStoresTypeDef",
    "ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    "ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    "ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    "ClientCreatePipelineResponsepipelinestagesactionsTypeDef",
    "ClientCreatePipelineResponsepipelinestagesblockersTypeDef",
    "ClientCreatePipelineResponsepipelinestagesTypeDef",
    "ClientCreatePipelineResponsepipelineTypeDef",
    "ClientCreatePipelineResponsetagsTypeDef",
    "ClientCreatePipelineResponseTypeDef",
    "ClientCreatePipelineTagsTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    "ClientGetJobDetailsResponsejobDetailsdataTypeDef",
    "ClientGetJobDetailsResponsejobDetailsTypeDef",
    "ClientGetJobDetailsResponseTypeDef",
    "ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef",
    "ClientGetPipelineExecutionResponsepipelineExecutionTypeDef",
    "ClientGetPipelineExecutionResponseTypeDef",
    "ClientGetPipelineResponsemetadataTypeDef",
    "ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    "ClientGetPipelineResponsepipelineartifactStoreTypeDef",
    "ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    "ClientGetPipelineResponsepipelineartifactStoresTypeDef",
    "ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    "ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    "ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    "ClientGetPipelineResponsepipelinestagesactionsTypeDef",
    "ClientGetPipelineResponsepipelinestagesblockersTypeDef",
    "ClientGetPipelineResponsepipelinestagesTypeDef",
    "ClientGetPipelineResponsepipelineTypeDef",
    "ClientGetPipelineResponseTypeDef",
    "ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef",
    "ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef",
    "ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef",
    "ClientGetPipelineStateResponsestageStatesactionStatesTypeDef",
    "ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef",
    "ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef",
    "ClientGetPipelineStateResponsestageStatesTypeDef",
    "ClientGetPipelineStateResponseTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef",
    "ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef",
    "ClientGetThirdPartyJobDetailsResponseTypeDef",
    "ClientListActionExecutionsFilterTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef",
    "ClientListActionExecutionsResponseactionExecutionDetailsTypeDef",
    "ClientListActionExecutionsResponseTypeDef",
    "ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef",
    "ClientListActionTypesResponseactionTypesidTypeDef",
    "ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef",
    "ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef",
    "ClientListActionTypesResponseactionTypessettingsTypeDef",
    "ClientListActionTypesResponseactionTypesTypeDef",
    "ClientListActionTypesResponseTypeDef",
    "ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    "ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef",
    "ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef",
    "ClientListPipelineExecutionsResponseTypeDef",
    "ClientListPipelinesResponsepipelinesTypeDef",
    "ClientListPipelinesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    "ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef",
    "ClientListWebhooksResponsewebhooksdefinitionTypeDef",
    "ClientListWebhooksResponsewebhookstagsTypeDef",
    "ClientListWebhooksResponsewebhooksTypeDef",
    "ClientListWebhooksResponseTypeDef",
    "ClientPollForJobsActionTypeIdTypeDef",
    "ClientPollForJobsResponsejobsdataactionConfigurationTypeDef",
    "ClientPollForJobsResponsejobsdataactionTypeIdTypeDef",
    "ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef",
    "ClientPollForJobsResponsejobsdataencryptionKeyTypeDef",
    "ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef",
    "ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef",
    "ClientPollForJobsResponsejobsdatainputArtifactsTypeDef",
    "ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef",
    "ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef",
    "ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef",
    "ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef",
    "ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef",
    "ClientPollForJobsResponsejobsdatapipelineContextTypeDef",
    "ClientPollForJobsResponsejobsdataTypeDef",
    "ClientPollForJobsResponsejobsTypeDef",
    "ClientPollForJobsResponseTypeDef",
    "ClientPollForThirdPartyJobsActionTypeIdTypeDef",
    "ClientPollForThirdPartyJobsResponsejobsTypeDef",
    "ClientPollForThirdPartyJobsResponseTypeDef",
    "ClientPutActionRevisionActionRevisionTypeDef",
    "ClientPutActionRevisionResponseTypeDef",
    "ClientPutApprovalResultResponseTypeDef",
    "ClientPutApprovalResultResultTypeDef",
    "ClientPutJobFailureResultFailureDetailsTypeDef",
    "ClientPutJobSuccessResultCurrentRevisionTypeDef",
    "ClientPutJobSuccessResultExecutionDetailsTypeDef",
    "ClientPutThirdPartyJobFailureResultFailureDetailsTypeDef",
    "ClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef",
    "ClientPutThirdPartyJobSuccessResultExecutionDetailsTypeDef",
    "ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef",
    "ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef",
    "ClientPutWebhookResponsewebhookdefinitionTypeDef",
    "ClientPutWebhookResponsewebhooktagsTypeDef",
    "ClientPutWebhookResponsewebhookTypeDef",
    "ClientPutWebhookResponseTypeDef",
    "ClientPutWebhookTagsTypeDef",
    "ClientPutWebhookWebhookauthenticationConfigurationTypeDef",
    "ClientPutWebhookWebhookfiltersTypeDef",
    "ClientPutWebhookWebhookTypeDef",
    "ClientRetryStageExecutionResponseTypeDef",
    "ClientStartPipelineExecutionResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdatePipelinePipelineartifactStoreencryptionKeyTypeDef",
    "ClientUpdatePipelinePipelineartifactStoreTypeDef",
    "ClientUpdatePipelinePipelineartifactStoresencryptionKeyTypeDef",
    "ClientUpdatePipelinePipelineartifactStoresTypeDef",
    "ClientUpdatePipelinePipelinestagesactionsactionTypeIdTypeDef",
    "ClientUpdatePipelinePipelinestagesactionsinputArtifactsTypeDef",
    "ClientUpdatePipelinePipelinestagesactionsoutputArtifactsTypeDef",
    "ClientUpdatePipelinePipelinestagesactionsTypeDef",
    "ClientUpdatePipelinePipelinestagesblockersTypeDef",
    "ClientUpdatePipelinePipelinestagesTypeDef",
    "ClientUpdatePipelinePipelineTypeDef",
    "ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    "ClientUpdatePipelineResponsepipelineartifactStoreTypeDef",
    "ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    "ClientUpdatePipelineResponsepipelineartifactStoresTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesactionsTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesblockersTypeDef",
    "ClientUpdatePipelineResponsepipelinestagesTypeDef",
    "ClientUpdatePipelineResponsepipelineTypeDef",
    "ClientUpdatePipelineResponseTypeDef",
    "ListActionExecutionsPaginateFilterTypeDef",
    "ListActionExecutionsPaginatePaginationConfigTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef",
    "ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef",
    "ListActionExecutionsPaginateResponseTypeDef",
    "ListActionTypesPaginatePaginationConfigTypeDef",
    "ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef",
    "ListActionTypesPaginateResponseactionTypesidTypeDef",
    "ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef",
    "ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef",
    "ListActionTypesPaginateResponseactionTypessettingsTypeDef",
    "ListActionTypesPaginateResponseactionTypesTypeDef",
    "ListActionTypesPaginateResponseTypeDef",
    "ListPipelineExecutionsPaginatePaginationConfigTypeDef",
    "ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    "ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef",
    "ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef",
    "ListPipelineExecutionsPaginateResponseTypeDef",
    "ListPipelinesPaginatePaginationConfigTypeDef",
    "ListPipelinesPaginateResponsepipelinesTypeDef",
    "ListPipelinesPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponsetagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListWebhooksPaginatePaginationConfigTypeDef",
    "ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    "ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef",
    "ListWebhooksPaginateResponsewebhooksdefinitionTypeDef",
    "ListWebhooksPaginateResponsewebhookstagsTypeDef",
    "ListWebhooksPaginateResponsewebhooksTypeDef",
    "ListWebhooksPaginateResponseTypeDef",
)


_ClientAcknowledgeJobResponseTypeDef = TypedDict(
    "_ClientAcknowledgeJobResponseTypeDef",
    {
        "status": Literal[
            "Created", "Queued", "Dispatched", "InProgress", "TimedOut", "Succeeded", "Failed"
        ]
    },
    total=False,
)


class ClientAcknowledgeJobResponseTypeDef(_ClientAcknowledgeJobResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an AcknowledgeJob action.
      - **status** *(string) --*

        Whether the job worker has received the specified job.
    """


_ClientAcknowledgeThirdPartyJobResponseTypeDef = TypedDict(
    "_ClientAcknowledgeThirdPartyJobResponseTypeDef",
    {
        "status": Literal[
            "Created", "Queued", "Dispatched", "InProgress", "TimedOut", "Succeeded", "Failed"
        ]
    },
    total=False,
)


class ClientAcknowledgeThirdPartyJobResponseTypeDef(_ClientAcknowledgeThirdPartyJobResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an AcknowledgeThirdPartyJob action.
      - **status** *(string) --*

        The status information for the third party job, if any.
    """


_ClientCreateCustomActionTypeConfigurationPropertiesTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeConfigurationPropertiesTypeDef",
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


class ClientCreateCustomActionTypeConfigurationPropertiesTypeDef(
    _ClientCreateCustomActionTypeConfigurationPropertiesTypeDef
):
    pass


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
    """
    The details of the input artifact for the action, such as its commit ID.
    - **minimumCount** *(integer) --***[REQUIRED]**

      The minimum number of artifacts allowed for the action type.
    """


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
    """
    The details of the output artifact of the action, such as its commit ID.
    - **minimumCount** *(integer) --***[REQUIRED]**

      The minimum number of artifacts allowed for the action type.
    """


_ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef",
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


class ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeactionConfigurationPropertiesTypeDef
):
    pass


_ClientCreateCustomActionTypeResponseactionTypeidTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeidTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypeidTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeidTypeDef
):
    """
    - **id** *(dict) --*

      Represents information about an action type.
      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following values.
    """


_ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeinputArtifactDetailsTypeDef
):
    pass


_ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeoutputArtifactDetailsTypeDef
):
    pass


_ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)


class ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypesettingsTypeDef
):
    pass


_ClientCreateCustomActionTypeResponseactionTypeTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseactionTypeTypeDef",
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


class ClientCreateCustomActionTypeResponseactionTypeTypeDef(
    _ClientCreateCustomActionTypeResponseactionTypeTypeDef
):
    """
    - **actionType** *(dict) --*

      Returns information about the details of an action type.
      - **id** *(dict) --*

        Represents information about an action type.
        - **category** *(string) --*

          A category defines what kind of action can be taken in the stage, and constrains the
          provider type for the action. Valid categories are limited to one of the following values.
    """


_ClientCreateCustomActionTypeResponsetagsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateCustomActionTypeResponsetagsTypeDef(
    _ClientCreateCustomActionTypeResponsetagsTypeDef
):
    pass


_ClientCreateCustomActionTypeResponseTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeResponseTypeDef",
    {
        "actionType": ClientCreateCustomActionTypeResponseactionTypeTypeDef,
        "tags": List[ClientCreateCustomActionTypeResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreateCustomActionTypeResponseTypeDef(_ClientCreateCustomActionTypeResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``CreateCustomActionType`` operation.
      - **actionType** *(dict) --*

        Returns information about the details of an action type.
        - **id** *(dict) --*

          Represents information about an action type.
          - **category** *(string) --*

            A category defines what kind of action can be taken in the stage, and constrains the
            provider type for the action. Valid categories are limited to one of the following
            values.
    """


_ClientCreateCustomActionTypeSettingsTypeDef = TypedDict(
    "_ClientCreateCustomActionTypeSettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)


class ClientCreateCustomActionTypeSettingsTypeDef(_ClientCreateCustomActionTypeSettingsTypeDef):
    """
    URLs that provide users information about this custom action.
    - **thirdPartyConfigurationUrl** *(string) --*

      The URL of a sign-up page where users can sign up for an external service and perform initial
      configuration of the action provided by that service.
    """


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
    """
    - *(dict) --*

      A tag is a key-value pair that is used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientCreatePipelinePipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientCreatePipelinePipelineartifactStoreencryptionKeyTypeDef(
    _ClientCreatePipelinePipelineartifactStoreencryptionKeyTypeDef
):
    pass


_ClientCreatePipelinePipelineartifactStoreTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelinePipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)


class ClientCreatePipelinePipelineartifactStoreTypeDef(
    _ClientCreatePipelinePipelineartifactStoreTypeDef
):
    pass


_ClientCreatePipelinePipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientCreatePipelinePipelineartifactStoresencryptionKeyTypeDef(
    _ClientCreatePipelinePipelineartifactStoresencryptionKeyTypeDef
):
    pass


_ClientCreatePipelinePipelineartifactStoresTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelinePipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)


class ClientCreatePipelinePipelineartifactStoresTypeDef(
    _ClientCreatePipelinePipelineartifactStoresTypeDef
):
    pass


_ClientCreatePipelinePipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientCreatePipelinePipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientCreatePipelinePipelinestagesactionsactionTypeIdTypeDef(
    _ClientCreatePipelinePipelinestagesactionsactionTypeIdTypeDef
):
    pass


_ClientCreatePipelinePipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientCreatePipelinePipelinestagesactionsinputArtifactsTypeDef", {"name": str}, total=False
)


class ClientCreatePipelinePipelinestagesactionsinputArtifactsTypeDef(
    _ClientCreatePipelinePipelinestagesactionsinputArtifactsTypeDef
):
    pass


_ClientCreatePipelinePipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientCreatePipelinePipelinestagesactionsoutputArtifactsTypeDef", {"name": str}, total=False
)


class ClientCreatePipelinePipelinestagesactionsoutputArtifactsTypeDef(
    _ClientCreatePipelinePipelinestagesactionsoutputArtifactsTypeDef
):
    pass


_ClientCreatePipelinePipelinestagesactionsTypeDef = TypedDict(
    "_ClientCreatePipelinePipelinestagesactionsTypeDef",
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


class ClientCreatePipelinePipelinestagesactionsTypeDef(
    _ClientCreatePipelinePipelinestagesactionsTypeDef
):
    pass


_ClientCreatePipelinePipelinestagesblockersTypeDef = TypedDict(
    "_ClientCreatePipelinePipelinestagesblockersTypeDef", {"name": str, "type": str}, total=False
)


class ClientCreatePipelinePipelinestagesblockersTypeDef(
    _ClientCreatePipelinePipelinestagesblockersTypeDef
):
    pass


_ClientCreatePipelinePipelinestagesTypeDef = TypedDict(
    "_ClientCreatePipelinePipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientCreatePipelinePipelinestagesblockersTypeDef],
        "actions": List[ClientCreatePipelinePipelinestagesactionsTypeDef],
    },
    total=False,
)


class ClientCreatePipelinePipelinestagesTypeDef(_ClientCreatePipelinePipelinestagesTypeDef):
    pass


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
    """
    Represents the structure of actions and stages to be performed in the pipeline.
    - **name** *(string) --***[REQUIRED]**

      The name of the action to be performed.
    """


_ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef(
    _ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef
):
    pass


_ClientCreatePipelineResponsepipelineartifactStoreTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)


class ClientCreatePipelineResponsepipelineartifactStoreTypeDef(
    _ClientCreatePipelineResponsepipelineartifactStoreTypeDef
):
    pass


_ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef(
    _ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef
):
    pass


_ClientCreatePipelineResponsepipelineartifactStoresTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientCreatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)


class ClientCreatePipelineResponsepipelineartifactStoresTypeDef(
    _ClientCreatePipelineResponsepipelineartifactStoresTypeDef
):
    pass


_ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef(
    _ClientCreatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef
):
    pass


_ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef(
    _ClientCreatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef
):
    pass


_ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef(
    _ClientCreatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
):
    pass


_ClientCreatePipelineResponsepipelinestagesactionsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesactionsTypeDef",
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


class ClientCreatePipelineResponsepipelinestagesactionsTypeDef(
    _ClientCreatePipelineResponsepipelinestagesactionsTypeDef
):
    pass


_ClientCreatePipelineResponsepipelinestagesblockersTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesblockersTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesblockersTypeDef(
    _ClientCreatePipelineResponsepipelinestagesblockersTypeDef
):
    pass


_ClientCreatePipelineResponsepipelinestagesTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientCreatePipelineResponsepipelinestagesblockersTypeDef],
        "actions": List[ClientCreatePipelineResponsepipelinestagesactionsTypeDef],
    },
    total=False,
)


class ClientCreatePipelineResponsepipelinestagesTypeDef(
    _ClientCreatePipelineResponsepipelinestagesTypeDef
):
    pass


_ClientCreatePipelineResponsepipelineTypeDef = TypedDict(
    "_ClientCreatePipelineResponsepipelineTypeDef",
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


class ClientCreatePipelineResponsepipelineTypeDef(_ClientCreatePipelineResponsepipelineTypeDef):
    """
    - **pipeline** *(dict) --*

      Represents the structure of actions and stages to be performed in the pipeline.
      - **name** *(string) --*

        The name of the action to be performed.
    """


_ClientCreatePipelineResponsetagsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreatePipelineResponsetagsTypeDef(_ClientCreatePipelineResponsetagsTypeDef):
    pass


_ClientCreatePipelineResponseTypeDef = TypedDict(
    "_ClientCreatePipelineResponseTypeDef",
    {
        "pipeline": ClientCreatePipelineResponsepipelineTypeDef,
        "tags": List[ClientCreatePipelineResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreatePipelineResponseTypeDef(_ClientCreatePipelineResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``CreatePipeline`` action.
      - **pipeline** *(dict) --*

        Represents the structure of actions and stages to be performed in the pipeline.
        - **name** *(string) --*

          The name of the action to be performed.
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

      A tag is a key-value pair that is used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    {"configuration": Dict[str, str]},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataactionConfigurationTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataactionTypeIdTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataencryptionKeyTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatainputArtifactsTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    {"name": str, "actionExecutionId": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    {"name": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": ClientGetJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef,
        "action": ClientGetJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdatapipelineContextTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsdataTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsdataTypeDef",
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


class ClientGetJobDetailsResponsejobDetailsdataTypeDef(
    _ClientGetJobDetailsResponsejobDetailsdataTypeDef
):
    pass


_ClientGetJobDetailsResponsejobDetailsTypeDef = TypedDict(
    "_ClientGetJobDetailsResponsejobDetailsTypeDef",
    {"id": str, "data": ClientGetJobDetailsResponsejobDetailsdataTypeDef, "accountId": str},
    total=False,
)


class ClientGetJobDetailsResponsejobDetailsTypeDef(_ClientGetJobDetailsResponsejobDetailsTypeDef):
    """
    - **jobDetails** *(dict) --*

      The details of the job.
      .. note::

        If AWSSessionCredentials is used, a long-running job can call ``GetJobDetails`` again to
        obtain new credentials.
    """


_ClientGetJobDetailsResponseTypeDef = TypedDict(
    "_ClientGetJobDetailsResponseTypeDef",
    {"jobDetails": ClientGetJobDetailsResponsejobDetailsTypeDef},
    total=False,
)


class ClientGetJobDetailsResponseTypeDef(_ClientGetJobDetailsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetJobDetails`` action.
      - **jobDetails** *(dict) --*

        The details of the job.
        .. note::

          If AWSSessionCredentials is used, a long-running job can call ``GetJobDetails`` again to
          obtain new credentials.
    """


_ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef = TypedDict(
    "_ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef",
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


class ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef(
    _ClientGetPipelineExecutionResponsepipelineExecutionartifactRevisionsTypeDef
):
    pass


_ClientGetPipelineExecutionResponsepipelineExecutionTypeDef = TypedDict(
    "_ClientGetPipelineExecutionResponsepipelineExecutionTypeDef",
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


class ClientGetPipelineExecutionResponsepipelineExecutionTypeDef(
    _ClientGetPipelineExecutionResponsepipelineExecutionTypeDef
):
    """
    - **pipelineExecution** *(dict) --*

      Represents information about the execution of a pipeline.
      - **pipelineName** *(string) --*

        The name of the pipeline that was executed.
    """


_ClientGetPipelineExecutionResponseTypeDef = TypedDict(
    "_ClientGetPipelineExecutionResponseTypeDef",
    {"pipelineExecution": ClientGetPipelineExecutionResponsepipelineExecutionTypeDef},
    total=False,
)


class ClientGetPipelineExecutionResponseTypeDef(_ClientGetPipelineExecutionResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetPipelineExecution`` action.
      - **pipelineExecution** *(dict) --*

        Represents information about the execution of a pipeline.
        - **pipelineName** *(string) --*

          The name of the pipeline that was executed.
    """


_ClientGetPipelineResponsemetadataTypeDef = TypedDict(
    "_ClientGetPipelineResponsemetadataTypeDef",
    {"pipelineArn": str, "created": datetime, "updated": datetime},
    total=False,
)


class ClientGetPipelineResponsemetadataTypeDef(_ClientGetPipelineResponsemetadataTypeDef):
    pass


_ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef(
    _ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef
):
    pass


_ClientGetPipelineResponsepipelineartifactStoreTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientGetPipelineResponsepipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)


class ClientGetPipelineResponsepipelineartifactStoreTypeDef(
    _ClientGetPipelineResponsepipelineartifactStoreTypeDef
):
    pass


_ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef(
    _ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef
):
    pass


_ClientGetPipelineResponsepipelineartifactStoresTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientGetPipelineResponsepipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)


class ClientGetPipelineResponsepipelineartifactStoresTypeDef(
    _ClientGetPipelineResponsepipelineartifactStoresTypeDef
):
    pass


_ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef(
    _ClientGetPipelineResponsepipelinestagesactionsactionTypeIdTypeDef
):
    pass


_ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef(
    _ClientGetPipelineResponsepipelinestagesactionsinputArtifactsTypeDef
):
    pass


_ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef(
    _ClientGetPipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
):
    pass


_ClientGetPipelineResponsepipelinestagesactionsTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesactionsTypeDef",
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


class ClientGetPipelineResponsepipelinestagesactionsTypeDef(
    _ClientGetPipelineResponsepipelinestagesactionsTypeDef
):
    pass


_ClientGetPipelineResponsepipelinestagesblockersTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesblockersTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientGetPipelineResponsepipelinestagesblockersTypeDef(
    _ClientGetPipelineResponsepipelinestagesblockersTypeDef
):
    pass


_ClientGetPipelineResponsepipelinestagesTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientGetPipelineResponsepipelinestagesblockersTypeDef],
        "actions": List[ClientGetPipelineResponsepipelinestagesactionsTypeDef],
    },
    total=False,
)


class ClientGetPipelineResponsepipelinestagesTypeDef(
    _ClientGetPipelineResponsepipelinestagesTypeDef
):
    pass


_ClientGetPipelineResponsepipelineTypeDef = TypedDict(
    "_ClientGetPipelineResponsepipelineTypeDef",
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


class ClientGetPipelineResponsepipelineTypeDef(_ClientGetPipelineResponsepipelineTypeDef):
    """
    - **pipeline** *(dict) --*

      Represents the structure of actions and stages to be performed in the pipeline.
      - **name** *(string) --*

        The name of the action to be performed.
    """


_ClientGetPipelineResponseTypeDef = TypedDict(
    "_ClientGetPipelineResponseTypeDef",
    {
        "pipeline": ClientGetPipelineResponsepipelineTypeDef,
        "metadata": ClientGetPipelineResponsemetadataTypeDef,
    },
    total=False,
)


class ClientGetPipelineResponseTypeDef(_ClientGetPipelineResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetPipeline`` action.
      - **pipeline** *(dict) --*

        Represents the structure of actions and stages to be performed in the pipeline.
        - **name** *(string) --*

          The name of the action to be performed.
    """


_ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef",
    {"revisionId": str, "revisionChangeId": str, "created": datetime},
    total=False,
)


class ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef(
    _ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef
):
    pass


_ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef",
    {"code": str, "message": str},
    total=False,
)


class ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef(
    _ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionerrorDetailsTypeDef
):
    pass


_ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef",
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


class ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef(
    _ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef
):
    pass


_ClientGetPipelineStateResponsestageStatesactionStatesTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesactionStatesTypeDef",
    {
        "actionName": str,
        "currentRevision": ClientGetPipelineStateResponsestageStatesactionStatescurrentRevisionTypeDef,
        "latestExecution": ClientGetPipelineStateResponsestageStatesactionStateslatestExecutionTypeDef,
        "entityUrl": str,
        "revisionUrl": str,
    },
    total=False,
)


class ClientGetPipelineStateResponsestageStatesactionStatesTypeDef(
    _ClientGetPipelineStateResponsestageStatesactionStatesTypeDef
):
    pass


_ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef",
    {"enabled": bool, "lastChangedBy": str, "lastChangedAt": datetime, "disabledReason": str},
    total=False,
)


class ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef(
    _ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef
):
    pass


_ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef",
    {"pipelineExecutionId": str, "status": Literal["InProgress", "Failed", "Succeeded"]},
    total=False,
)


class ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef(
    _ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef
):
    pass


_ClientGetPipelineStateResponsestageStatesTypeDef = TypedDict(
    "_ClientGetPipelineStateResponsestageStatesTypeDef",
    {
        "stageName": str,
        "inboundTransitionState": ClientGetPipelineStateResponsestageStatesinboundTransitionStateTypeDef,
        "actionStates": List[ClientGetPipelineStateResponsestageStatesactionStatesTypeDef],
        "latestExecution": ClientGetPipelineStateResponsestageStateslatestExecutionTypeDef,
    },
    total=False,
)


class ClientGetPipelineStateResponsestageStatesTypeDef(
    _ClientGetPipelineStateResponsestageStatesTypeDef
):
    pass


_ClientGetPipelineStateResponseTypeDef = TypedDict(
    "_ClientGetPipelineStateResponseTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "stageStates": List[ClientGetPipelineStateResponsestageStatesTypeDef],
        "created": datetime,
        "updated": datetime,
    },
    total=False,
)


class ClientGetPipelineStateResponseTypeDef(_ClientGetPipelineStateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetPipelineState`` action.
      - **pipelineName** *(string) --*

        The name of the pipeline for which you want to get the state.
    """


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef",
    {"configuration": Dict[str, str]},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionConfigurationTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataactionTypeIdTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataartifactCredentialsTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataencryptionKeyTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatainputArtifactsTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataoutputArtifactsTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef",
    {"name": str, "actionExecutionId": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef",
    {"name": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextstageTypeDef,
        "action": ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextactionTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdatapipelineContextTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef",
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


class ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef
):
    pass


_ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef",
    {"id": str, "data": ClientGetThirdPartyJobDetailsResponsejobDetailsdataTypeDef, "nonce": str},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef(
    _ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef
):
    """
    - **jobDetails** *(dict) --*

      The details of the job, including any protected values defined for the job.
      - **id** *(string) --*

        The identifier used to identify the job details in AWS CodePipeline.
    """


_ClientGetThirdPartyJobDetailsResponseTypeDef = TypedDict(
    "_ClientGetThirdPartyJobDetailsResponseTypeDef",
    {"jobDetails": ClientGetThirdPartyJobDetailsResponsejobDetailsTypeDef},
    total=False,
)


class ClientGetThirdPartyJobDetailsResponseTypeDef(_ClientGetThirdPartyJobDetailsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``GetThirdPartyJobDetails`` action.
      - **jobDetails** *(dict) --*

        The details of the job, including any protected values defined for the job.
        - **id** *(string) --*

          The identifier used to identify the job details in AWS CodePipeline.
    """


_ClientListActionExecutionsFilterTypeDef = TypedDict(
    "_ClientListActionExecutionsFilterTypeDef", {"pipelineExecutionId": str}, total=False
)


class ClientListActionExecutionsFilterTypeDef(_ClientListActionExecutionsFilterTypeDef):
    """
    Input information used to filter action execution history.
    - **pipelineExecutionId** *(string) --*

      The pipeline execution ID used to filter action execution history.
    """


_ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsinputactionTypeIdTypeDef
):
    pass


_ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef
):
    pass


_ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef,
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsinputinputArtifactsTypeDef
):
    pass


_ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef",
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


class ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsinputTypeDef
):
    pass


_ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    {"externalExecutionId": str, "externalExecutionSummary": str, "externalExecutionUrl": str},
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef
):
    pass


_ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef
):
    pass


_ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef,
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
):
    pass


_ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef",
    {
        "outputArtifacts": List[
            ClientListActionExecutionsResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
        ],
        "executionResult": ClientListActionExecutionsResponseactionExecutionDetailsoutputexecutionResultTypeDef,
        "outputVariables": Dict[str, str],
    },
    total=False,
)


class ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsoutputTypeDef
):
    pass


_ClientListActionExecutionsResponseactionExecutionDetailsTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseactionExecutionDetailsTypeDef",
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


class ClientListActionExecutionsResponseactionExecutionDetailsTypeDef(
    _ClientListActionExecutionsResponseactionExecutionDetailsTypeDef
):
    """
    - *(dict) --*

      Returns information about an execution of an action, including the action execution ID, and
      the name, version, and timing of the action.
      - **pipelineExecutionId** *(string) --*

        The pipeline execution ID for the action execution.
    """


_ClientListActionExecutionsResponseTypeDef = TypedDict(
    "_ClientListActionExecutionsResponseTypeDef",
    {
        "actionExecutionDetails": List[
            ClientListActionExecutionsResponseactionExecutionDetailsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListActionExecutionsResponseTypeDef(_ClientListActionExecutionsResponseTypeDef):
    """
    - *(dict) --*

      - **actionExecutionDetails** *(list) --*

        The details for a list of recent executions, such as action execution ID.
        - *(dict) --*

          Returns information about an execution of an action, including the action execution ID,
          and the name, version, and timing of the action.
          - **pipelineExecutionId** *(string) --*

            The pipeline execution ID for the action execution.
    """


_ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef",
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


class ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef(
    _ClientListActionTypesResponseactionTypesactionConfigurationPropertiesTypeDef
):
    pass


_ClientListActionTypesResponseactionTypesidTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesidTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientListActionTypesResponseactionTypesidTypeDef(
    _ClientListActionTypesResponseactionTypesidTypeDef
):
    """
    - **id** *(dict) --*

      Represents information about an action type.
      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following values.
    """


_ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef(
    _ClientListActionTypesResponseactionTypesinputArtifactDetailsTypeDef
):
    pass


_ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef(
    _ClientListActionTypesResponseactionTypesoutputArtifactDetailsTypeDef
):
    pass


_ClientListActionTypesResponseactionTypessettingsTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypessettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)


class ClientListActionTypesResponseactionTypessettingsTypeDef(
    _ClientListActionTypesResponseactionTypessettingsTypeDef
):
    pass


_ClientListActionTypesResponseactionTypesTypeDef = TypedDict(
    "_ClientListActionTypesResponseactionTypesTypeDef",
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


class ClientListActionTypesResponseactionTypesTypeDef(
    _ClientListActionTypesResponseactionTypesTypeDef
):
    """
    - *(dict) --*

      Returns information about the details of an action type.
      - **id** *(dict) --*

        Represents information about an action type.
        - **category** *(string) --*

          A category defines what kind of action can be taken in the stage, and constrains the
          provider type for the action. Valid categories are limited to one of the following values.
    """


_ClientListActionTypesResponseTypeDef = TypedDict(
    "_ClientListActionTypesResponseTypeDef",
    {"actionTypes": List[ClientListActionTypesResponseactionTypesTypeDef], "nextToken": str},
    total=False,
)


class ClientListActionTypesResponseTypeDef(_ClientListActionTypesResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``ListActionTypes`` action.
      - **actionTypes** *(list) --*

        Provides details of the action types.
        - *(dict) --*

          Returns information about the details of an action type.
          - **id** *(dict) --*

            Represents information about an action type.
            - **category** *(string) --*

              A category defines what kind of action can be taken in the stage, and constrains the
              provider type for the action. Valid categories are limited to one of the following
              values.
    """


_ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef = TypedDict(
    "_ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    {"actionName": str, "revisionId": str, "revisionSummary": str, "revisionUrl": str},
    total=False,
)


class ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef(
    _ClientListPipelineExecutionsResponsepipelineExecutionSummariessourceRevisionsTypeDef
):
    pass


_ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef = TypedDict(
    "_ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef",
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


class ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef(
    _ClientListPipelineExecutionsResponsepipelineExecutionSummariestriggerTypeDef
):
    pass


_ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef = TypedDict(
    "_ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef",
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


class ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef(
    _ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information about a pipeline execution.
      - **pipelineExecutionId** *(string) --*

        The ID of the pipeline execution.
    """


_ClientListPipelineExecutionsResponseTypeDef = TypedDict(
    "_ClientListPipelineExecutionsResponseTypeDef",
    {
        "pipelineExecutionSummaries": List[
            ClientListPipelineExecutionsResponsepipelineExecutionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListPipelineExecutionsResponseTypeDef(_ClientListPipelineExecutionsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``ListPipelineExecutions`` action.
      - **pipelineExecutionSummaries** *(list) --*

        A list of executions in the history of a pipeline.
        - *(dict) --*

          Summary information about a pipeline execution.
          - **pipelineExecutionId** *(string) --*

            The ID of the pipeline execution.
    """


_ClientListPipelinesResponsepipelinesTypeDef = TypedDict(
    "_ClientListPipelinesResponsepipelinesTypeDef",
    {"name": str, "version": int, "created": datetime, "updated": datetime},
    total=False,
)


class ClientListPipelinesResponsepipelinesTypeDef(_ClientListPipelinesResponsepipelinesTypeDef):
    """
    - *(dict) --*

      Returns a summary of a pipeline.
      - **name** *(string) --*

        The name of the pipeline.
    """


_ClientListPipelinesResponseTypeDef = TypedDict(
    "_ClientListPipelinesResponseTypeDef",
    {"pipelines": List[ClientListPipelinesResponsepipelinesTypeDef], "nextToken": str},
    total=False,
)


class ClientListPipelinesResponseTypeDef(_ClientListPipelinesResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``ListPipelines`` action.
      - **pipelines** *(list) --*

        The list of pipelines.
        - *(dict) --*

          Returns a summary of a pipeline.
          - **name** *(string) --*

            The name of the pipeline.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    """
    - *(dict) --*

      A tag is a key-value pair that is used to manage the resource.
      - **key** *(string) --*

        The tag's key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef], "nextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        The tags for the resource.
        - *(dict) --*

          A tag is a key-value pair that is used to manage the resource.
          - **key** *(string) --*

            The tag's key.
    """


_ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)


class ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef(
    _ClientListWebhooksResponsewebhooksdefinitionauthenticationConfigurationTypeDef
):
    pass


_ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef",
    {"jsonPath": str, "matchEquals": str},
    total=False,
)


class ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef(
    _ClientListWebhooksResponsewebhooksdefinitionfiltersTypeDef
):
    pass


_ClientListWebhooksResponsewebhooksdefinitionTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksdefinitionTypeDef",
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


class ClientListWebhooksResponsewebhooksdefinitionTypeDef(
    _ClientListWebhooksResponsewebhooksdefinitionTypeDef
):
    """
    - **definition** *(dict) --*

      The detail returned for each webhook, such as the webhook authentication type and filter
      rules.
      - **name** *(string) --*

        The name of the webhook.
    """


_ClientListWebhooksResponsewebhookstagsTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhookstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientListWebhooksResponsewebhookstagsTypeDef(_ClientListWebhooksResponsewebhookstagsTypeDef):
    pass


_ClientListWebhooksResponsewebhooksTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksTypeDef",
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


class ClientListWebhooksResponsewebhooksTypeDef(_ClientListWebhooksResponsewebhooksTypeDef):
    """
    - *(dict) --*

      The detail returned for each webhook after listing webhooks, such as the webhook URL, the
      webhook name, and the webhook ARN.
      - **definition** *(dict) --*

        The detail returned for each webhook, such as the webhook authentication type and filter
        rules.
        - **name** *(string) --*

          The name of the webhook.
    """


_ClientListWebhooksResponseTypeDef = TypedDict(
    "_ClientListWebhooksResponseTypeDef",
    {"webhooks": List[ClientListWebhooksResponsewebhooksTypeDef], "NextToken": str},
    total=False,
)


class ClientListWebhooksResponseTypeDef(_ClientListWebhooksResponseTypeDef):
    """
    - *(dict) --*

      - **webhooks** *(list) --*

        The JSON detail returned for each webhook in the list output for the ListWebhooks call.
        - *(dict) --*

          The detail returned for each webhook after listing webhooks, such as the webhook URL, the
          webhook name, and the webhook ARN.
          - **definition** *(dict) --*

            The detail returned for each webhook, such as the webhook authentication type and filter
            rules.
            - **name** *(string) --*

              The name of the webhook.
    """


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
    """
    Represents information about an action type.
    - **category** *(string) --***[REQUIRED]**

      A category defines what kind of action can be taken in the stage, and constrains the provider
      type for the action. Valid categories are limited to one of the following values.
    """


_ClientPollForJobsResponsejobsdataactionConfigurationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataactionConfigurationTypeDef",
    {"configuration": Dict[str, str]},
    total=False,
)


class ClientPollForJobsResponsejobsdataactionConfigurationTypeDef(
    _ClientPollForJobsResponsejobsdataactionConfigurationTypeDef
):
    pass


_ClientPollForJobsResponsejobsdataactionTypeIdTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdataactionTypeIdTypeDef(
    _ClientPollForJobsResponsejobsdataactionTypeIdTypeDef
):
    pass


_ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
    total=False,
)


class ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef(
    _ClientPollForJobsResponsejobsdataartifactCredentialsTypeDef
):
    pass


_ClientPollForJobsResponsejobsdataencryptionKeyTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataencryptionKeyTypeDef", {"id": str, "type": str}, total=False
)


class ClientPollForJobsResponsejobsdataencryptionKeyTypeDef(
    _ClientPollForJobsResponsejobsdataencryptionKeyTypeDef
):
    pass


_ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef(
    _ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef
):
    pass


_ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientPollForJobsResponsejobsdatainputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef(
    _ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef
):
    pass


_ClientPollForJobsResponsejobsdatainputArtifactsTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatainputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientPollForJobsResponsejobsdatainputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdatainputArtifactsTypeDef(
    _ClientPollForJobsResponsejobsdatainputArtifactsTypeDef
):
    pass


_ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef",
    {"bucketName": str, "objectKey": str},
    total=False,
)


class ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef(
    _ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef
):
    pass


_ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef",
    {
        "type": str,
        "s3Location": ClientPollForJobsResponsejobsdataoutputArtifactslocations3LocationTypeDef,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef(
    _ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef
):
    pass


_ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef",
    {
        "name": str,
        "revision": str,
        "location": ClientPollForJobsResponsejobsdataoutputArtifactslocationTypeDef,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef(
    _ClientPollForJobsResponsejobsdataoutputArtifactsTypeDef
):
    pass


_ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef",
    {"name": str, "actionExecutionId": str},
    total=False,
)


class ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef(
    _ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef
):
    pass


_ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef", {"name": str}, total=False
)


class ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef(
    _ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef
):
    pass


_ClientPollForJobsResponsejobsdatapipelineContextTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdatapipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": ClientPollForJobsResponsejobsdatapipelineContextstageTypeDef,
        "action": ClientPollForJobsResponsejobsdatapipelineContextactionTypeDef,
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)


class ClientPollForJobsResponsejobsdatapipelineContextTypeDef(
    _ClientPollForJobsResponsejobsdatapipelineContextTypeDef
):
    pass


_ClientPollForJobsResponsejobsdataTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsdataTypeDef",
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


class ClientPollForJobsResponsejobsdataTypeDef(_ClientPollForJobsResponsejobsdataTypeDef):
    pass


_ClientPollForJobsResponsejobsTypeDef = TypedDict(
    "_ClientPollForJobsResponsejobsTypeDef",
    {"id": str, "data": ClientPollForJobsResponsejobsdataTypeDef, "nonce": str, "accountId": str},
    total=False,
)


class ClientPollForJobsResponsejobsTypeDef(_ClientPollForJobsResponsejobsTypeDef):
    """
    - *(dict) --*

      Represents information about a job.
      - **id** *(string) --*

        The unique system-generated ID of the job.
    """


_ClientPollForJobsResponseTypeDef = TypedDict(
    "_ClientPollForJobsResponseTypeDef",
    {"jobs": List[ClientPollForJobsResponsejobsTypeDef]},
    total=False,
)


class ClientPollForJobsResponseTypeDef(_ClientPollForJobsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``PollForJobs`` action.
      - **jobs** *(list) --*

        Information about the jobs to take action on.
        - *(dict) --*

          Represents information about a job.
          - **id** *(string) --*

            The unique system-generated ID of the job.
    """


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
    """
    Represents information about an action type.
    - **category** *(string) --***[REQUIRED]**

      A category defines what kind of action can be taken in the stage, and constrains the provider
      type for the action. Valid categories are limited to one of the following values.
    """


_ClientPollForThirdPartyJobsResponsejobsTypeDef = TypedDict(
    "_ClientPollForThirdPartyJobsResponsejobsTypeDef", {"clientId": str, "jobId": str}, total=False
)


class ClientPollForThirdPartyJobsResponsejobsTypeDef(
    _ClientPollForThirdPartyJobsResponsejobsTypeDef
):
    """
    - *(dict) --*

      A response to a ``PollForThirdPartyJobs`` request returned by AWS CodePipeline when there is a
      job to be worked on by a partner action.
      - **clientId** *(string) --*

        The ``clientToken`` portion of the ``clientId`` and ``clientToken`` pair used to verify that
        the calling entity is allowed access to the job and its details.
    """


_ClientPollForThirdPartyJobsResponseTypeDef = TypedDict(
    "_ClientPollForThirdPartyJobsResponseTypeDef",
    {"jobs": List[ClientPollForThirdPartyJobsResponsejobsTypeDef]},
    total=False,
)


class ClientPollForThirdPartyJobsResponseTypeDef(_ClientPollForThirdPartyJobsResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``PollForThirdPartyJobs`` action.
      - **jobs** *(list) --*

        Information about the jobs to take action on.
        - *(dict) --*

          A response to a ``PollForThirdPartyJobs`` request returned by AWS CodePipeline when there
          is a job to be worked on by a partner action.
          - **clientId** *(string) --*

            The ``clientToken`` portion of the ``clientId`` and ``clientToken`` pair used to verify
            that the calling entity is allowed access to the job and its details.
    """


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
    """
    Represents information about the version (or revision) of an action.
    - **revisionId** *(string) --***[REQUIRED]**

      The system-generated unique ID that identifies the revision number of the action.
    """


_ClientPutActionRevisionResponseTypeDef = TypedDict(
    "_ClientPutActionRevisionResponseTypeDef",
    {"newRevision": bool, "pipelineExecutionId": str},
    total=False,
)


class ClientPutActionRevisionResponseTypeDef(_ClientPutActionRevisionResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``PutActionRevision`` action.
      - **newRevision** *(boolean) --*

        Indicates whether the artifact revision was previously used in an execution of the specified
        pipeline.
    """


_ClientPutApprovalResultResponseTypeDef = TypedDict(
    "_ClientPutApprovalResultResponseTypeDef", {"approvedAt": datetime}, total=False
)


class ClientPutApprovalResultResponseTypeDef(_ClientPutApprovalResultResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``PutApprovalResult`` action.
      - **approvedAt** *(datetime) --*

        The timestamp showing when the approval or rejection was submitted.
    """


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
    """
    Represents information about the result of the approval request.
    - **summary** *(string) --***[REQUIRED]**

      The summary of the current status of the approval request.
    """


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
    """
    The details about the failure of a job.
    - **type** *(string) --***[REQUIRED]**

      The type of the failure.
    """


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
    """
    The ID of the current revision of the artifact successfully worked on by the job.
    - **revision** *(string) --***[REQUIRED]**

      The revision ID of the current version of an artifact.
    """


_ClientPutJobSuccessResultExecutionDetailsTypeDef = TypedDict(
    "_ClientPutJobSuccessResultExecutionDetailsTypeDef",
    {"summary": str, "externalExecutionId": str, "percentComplete": int},
    total=False,
)


class ClientPutJobSuccessResultExecutionDetailsTypeDef(
    _ClientPutJobSuccessResultExecutionDetailsTypeDef
):
    """
    The execution details of the successful job, such as the actions taken by the job worker.
    - **summary** *(string) --*

      The summary of the current status of the actions.
    """


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
    """
    Represents information about failure details.
    - **type** *(string) --***[REQUIRED]**

      The type of the failure.
    """


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
    """
    Represents information about a current revision.
    - **revision** *(string) --***[REQUIRED]**

      The revision ID of the current version of an artifact.
    """


_ClientPutThirdPartyJobSuccessResultExecutionDetailsTypeDef = TypedDict(
    "_ClientPutThirdPartyJobSuccessResultExecutionDetailsTypeDef",
    {"summary": str, "externalExecutionId": str, "percentComplete": int},
    total=False,
)


class ClientPutThirdPartyJobSuccessResultExecutionDetailsTypeDef(
    _ClientPutThirdPartyJobSuccessResultExecutionDetailsTypeDef
):
    """
    The details of the actions taken and results produced on an artifact as it passes through stages
    in the pipeline.
    - **summary** *(string) --*

      The summary of the current status of the actions.
    """


_ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)


class ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef(
    _ClientPutWebhookResponsewebhookdefinitionauthenticationConfigurationTypeDef
):
    pass


_ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef",
    {"jsonPath": str, "matchEquals": str},
    total=False,
)


class ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef(
    _ClientPutWebhookResponsewebhookdefinitionfiltersTypeDef
):
    pass


_ClientPutWebhookResponsewebhookdefinitionTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhookdefinitionTypeDef",
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


class ClientPutWebhookResponsewebhookdefinitionTypeDef(
    _ClientPutWebhookResponsewebhookdefinitionTypeDef
):
    """
    - **definition** *(dict) --*

      The detail returned for each webhook, such as the webhook authentication type and filter
      rules.
      - **name** *(string) --*

        The name of the webhook.
    """


_ClientPutWebhookResponsewebhooktagsTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhooktagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientPutWebhookResponsewebhooktagsTypeDef(_ClientPutWebhookResponsewebhooktagsTypeDef):
    pass


_ClientPutWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientPutWebhookResponsewebhookTypeDef",
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


class ClientPutWebhookResponsewebhookTypeDef(_ClientPutWebhookResponsewebhookTypeDef):
    """
    - **webhook** *(dict) --*

      The detail returned from creating the webhook, such as the webhook name, webhook URL, and
      webhook ARN.
      - **definition** *(dict) --*

        The detail returned for each webhook, such as the webhook authentication type and filter
        rules.
        - **name** *(string) --*

          The name of the webhook.
    """


_ClientPutWebhookResponseTypeDef = TypedDict(
    "_ClientPutWebhookResponseTypeDef",
    {"webhook": ClientPutWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientPutWebhookResponseTypeDef(_ClientPutWebhookResponseTypeDef):
    """
    - *(dict) --*

      - **webhook** *(dict) --*

        The detail returned from creating the webhook, such as the webhook name, webhook URL, and
        webhook ARN.
        - **definition** *(dict) --*

          The detail returned for each webhook, such as the webhook authentication type and filter
          rules.
          - **name** *(string) --*

            The name of the webhook.
    """


_RequiredClientPutWebhookTagsTypeDef = TypedDict(
    "_RequiredClientPutWebhookTagsTypeDef", {"key": str}
)
_OptionalClientPutWebhookTagsTypeDef = TypedDict(
    "_OptionalClientPutWebhookTagsTypeDef", {"value": str}, total=False
)


class ClientPutWebhookTagsTypeDef(
    _RequiredClientPutWebhookTagsTypeDef, _OptionalClientPutWebhookTagsTypeDef
):
    """
    - *(dict) --*

      A tag is a key-value pair that is used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientPutWebhookWebhookauthenticationConfigurationTypeDef = TypedDict(
    "_ClientPutWebhookWebhookauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)


class ClientPutWebhookWebhookauthenticationConfigurationTypeDef(
    _ClientPutWebhookWebhookauthenticationConfigurationTypeDef
):
    pass


_ClientPutWebhookWebhookfiltersTypeDef = TypedDict(
    "_ClientPutWebhookWebhookfiltersTypeDef", {"jsonPath": str, "matchEquals": str}, total=False
)


class ClientPutWebhookWebhookfiltersTypeDef(_ClientPutWebhookWebhookfiltersTypeDef):
    pass


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
    """
    The detail provided in an input file to create the webhook, such as the webhook name, the
    pipeline name, and the action name. Give the webhook a unique name that helps you identify it.
    You might name the webhook after the pipeline and action it targets so that you can easily
    recognize what it's used for later.
    - **name** *(string) --***[REQUIRED]**

      The name of the webhook.
    """


_ClientRetryStageExecutionResponseTypeDef = TypedDict(
    "_ClientRetryStageExecutionResponseTypeDef", {"pipelineExecutionId": str}, total=False
)


class ClientRetryStageExecutionResponseTypeDef(_ClientRetryStageExecutionResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``RetryStageExecution`` action.
      - **pipelineExecutionId** *(string) --*

        The ID of the current workflow execution in the failed stage.
    """


_ClientStartPipelineExecutionResponseTypeDef = TypedDict(
    "_ClientStartPipelineExecutionResponseTypeDef", {"pipelineExecutionId": str}, total=False
)


class ClientStartPipelineExecutionResponseTypeDef(_ClientStartPipelineExecutionResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``StartPipelineExecution`` action.
      - **pipelineExecutionId** *(string) --*

        The unique system-generated ID of the pipeline execution that was started.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      A tag is a key-value pair that is used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientUpdatePipelinePipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientUpdatePipelinePipelineartifactStoreencryptionKeyTypeDef(
    _ClientUpdatePipelinePipelineartifactStoreencryptionKeyTypeDef
):
    pass


_ClientUpdatePipelinePipelineartifactStoreTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelinePipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)


class ClientUpdatePipelinePipelineartifactStoreTypeDef(
    _ClientUpdatePipelinePipelineartifactStoreTypeDef
):
    pass


_ClientUpdatePipelinePipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientUpdatePipelinePipelineartifactStoresencryptionKeyTypeDef(
    _ClientUpdatePipelinePipelineartifactStoresencryptionKeyTypeDef
):
    pass


_ClientUpdatePipelinePipelineartifactStoresTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelinePipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)


class ClientUpdatePipelinePipelineartifactStoresTypeDef(
    _ClientUpdatePipelinePipelineartifactStoresTypeDef
):
    pass


_ClientUpdatePipelinePipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientUpdatePipelinePipelinestagesactionsactionTypeIdTypeDef(
    _ClientUpdatePipelinePipelinestagesactionsactionTypeIdTypeDef
):
    pass


_ClientUpdatePipelinePipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelinestagesactionsinputArtifactsTypeDef", {"name": str}, total=False
)


class ClientUpdatePipelinePipelinestagesactionsinputArtifactsTypeDef(
    _ClientUpdatePipelinePipelinestagesactionsinputArtifactsTypeDef
):
    pass


_ClientUpdatePipelinePipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelinestagesactionsoutputArtifactsTypeDef", {"name": str}, total=False
)


class ClientUpdatePipelinePipelinestagesactionsoutputArtifactsTypeDef(
    _ClientUpdatePipelinePipelinestagesactionsoutputArtifactsTypeDef
):
    pass


_ClientUpdatePipelinePipelinestagesactionsTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelinestagesactionsTypeDef",
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


class ClientUpdatePipelinePipelinestagesactionsTypeDef(
    _ClientUpdatePipelinePipelinestagesactionsTypeDef
):
    pass


_ClientUpdatePipelinePipelinestagesblockersTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelinestagesblockersTypeDef", {"name": str, "type": str}, total=False
)


class ClientUpdatePipelinePipelinestagesblockersTypeDef(
    _ClientUpdatePipelinePipelinestagesblockersTypeDef
):
    pass


_ClientUpdatePipelinePipelinestagesTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientUpdatePipelinePipelinestagesblockersTypeDef],
        "actions": List[ClientUpdatePipelinePipelinestagesactionsTypeDef],
    },
    total=False,
)


class ClientUpdatePipelinePipelinestagesTypeDef(_ClientUpdatePipelinePipelinestagesTypeDef):
    pass


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
    """
    The name of the pipeline to be updated.
    - **name** *(string) --***[REQUIRED]**

      The name of the action to be performed.
    """


_ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef(
    _ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelineartifactStoreTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineartifactStoreTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelineResponsepipelineartifactStoreencryptionKeyTypeDef,
    },
    total=False,
)


class ClientUpdatePipelineResponsepipelineartifactStoreTypeDef(
    _ClientUpdatePipelineResponsepipelineartifactStoreTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef",
    {"id": str, "type": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef(
    _ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelineartifactStoresTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineartifactStoresTypeDef",
    {
        "type": str,
        "location": str,
        "encryptionKey": ClientUpdatePipelineResponsepipelineartifactStoresencryptionKeyTypeDef,
    },
    total=False,
)


class ClientUpdatePipelineResponsepipelineartifactStoresTypeDef(
    _ClientUpdatePipelineResponsepipelineartifactStoresTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesactionsactionTypeIdTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesactionsinputArtifactsTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef",
    {"name": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesactionsoutputArtifactsTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelinestagesactionsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesactionsTypeDef",
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


class ClientUpdatePipelineResponsepipelinestagesactionsTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesactionsTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelinestagesblockersTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesblockersTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesblockersTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesblockersTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelinestagesTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelinestagesTypeDef",
    {
        "name": str,
        "blockers": List[ClientUpdatePipelineResponsepipelinestagesblockersTypeDef],
        "actions": List[ClientUpdatePipelineResponsepipelinestagesactionsTypeDef],
    },
    total=False,
)


class ClientUpdatePipelineResponsepipelinestagesTypeDef(
    _ClientUpdatePipelineResponsepipelinestagesTypeDef
):
    pass


_ClientUpdatePipelineResponsepipelineTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsepipelineTypeDef",
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


class ClientUpdatePipelineResponsepipelineTypeDef(_ClientUpdatePipelineResponsepipelineTypeDef):
    """
    - **pipeline** *(dict) --*

      The structure of the updated pipeline.
      - **name** *(string) --*

        The name of the action to be performed.
    """


_ClientUpdatePipelineResponseTypeDef = TypedDict(
    "_ClientUpdatePipelineResponseTypeDef",
    {"pipeline": ClientUpdatePipelineResponsepipelineTypeDef},
    total=False,
)


class ClientUpdatePipelineResponseTypeDef(_ClientUpdatePipelineResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of an ``UpdatePipeline`` action.
      - **pipeline** *(dict) --*

        The structure of the updated pipeline.
        - **name** *(string) --*

          The name of the action to be performed.
    """


_ListActionExecutionsPaginateFilterTypeDef = TypedDict(
    "_ListActionExecutionsPaginateFilterTypeDef", {"pipelineExecutionId": str}, total=False
)


class ListActionExecutionsPaginateFilterTypeDef(_ListActionExecutionsPaginateFilterTypeDef):
    """
    Input information used to filter action execution history.
    - **pipelineExecutionId** *(string) --*

      The pipeline execution ID used to filter action execution history.
    """


_ListActionExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListActionExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListActionExecutionsPaginatePaginationConfigTypeDef(
    _ListActionExecutionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsinputactionTypeIdTypeDef
):
    pass


_ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef
):
    pass


_ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactss3locationTypeDef,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsinputinputArtifactsTypeDef
):
    pass


_ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef",
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


class ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsinputTypeDef
):
    pass


_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef",
    {"externalExecutionId": str, "externalExecutionSummary": str, "externalExecutionUrl": str},
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef
):
    pass


_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef
):
    pass


_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef",
    {
        "name": str,
        "s3location": ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactss3locationTypeDef,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
):
    pass


_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef",
    {
        "outputArtifacts": List[
            ListActionExecutionsPaginateResponseactionExecutionDetailsoutputoutputArtifactsTypeDef
        ],
        "executionResult": ListActionExecutionsPaginateResponseactionExecutionDetailsoutputexecutionResultTypeDef,
        "outputVariables": Dict[str, str],
    },
    total=False,
)


class ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsoutputTypeDef
):
    pass


_ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef",
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


class ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef(
    _ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef
):
    """
    - *(dict) --*

      Returns information about an execution of an action, including the action execution ID, and
      the name, version, and timing of the action.
      - **pipelineExecutionId** *(string) --*

        The pipeline execution ID for the action execution.
    """


_ListActionExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListActionExecutionsPaginateResponseTypeDef",
    {
        "actionExecutionDetails": List[
            ListActionExecutionsPaginateResponseactionExecutionDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListActionExecutionsPaginateResponseTypeDef(_ListActionExecutionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **actionExecutionDetails** *(list) --*

        The details for a list of recent executions, such as action execution ID.
        - *(dict) --*

          Returns information about an execution of an action, including the action execution ID,
          and the name, version, and timing of the action.
          - **pipelineExecutionId** *(string) --*

            The pipeline execution ID for the action execution.
    """


_ListActionTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListActionTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListActionTypesPaginatePaginationConfigTypeDef(
    _ListActionTypesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef",
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


class ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef(
    _ListActionTypesPaginateResponseactionTypesactionConfigurationPropertiesTypeDef
):
    pass


_ListActionTypesPaginateResponseactionTypesidTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesidTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
    total=False,
)


class ListActionTypesPaginateResponseactionTypesidTypeDef(
    _ListActionTypesPaginateResponseactionTypesidTypeDef
):
    """
    - **id** *(dict) --*

      Represents information about an action type.
      - **category** *(string) --*

        A category defines what kind of action can be taken in the stage, and constrains the
        provider type for the action. Valid categories are limited to one of the following values.
    """


_ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef(
    _ListActionTypesPaginateResponseactionTypesinputArtifactDetailsTypeDef
):
    pass


_ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef",
    {"minimumCount": int, "maximumCount": int},
    total=False,
)


class ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef(
    _ListActionTypesPaginateResponseactionTypesoutputArtifactDetailsTypeDef
):
    pass


_ListActionTypesPaginateResponseactionTypessettingsTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypessettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)


class ListActionTypesPaginateResponseactionTypessettingsTypeDef(
    _ListActionTypesPaginateResponseactionTypessettingsTypeDef
):
    pass


_ListActionTypesPaginateResponseactionTypesTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseactionTypesTypeDef",
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


class ListActionTypesPaginateResponseactionTypesTypeDef(
    _ListActionTypesPaginateResponseactionTypesTypeDef
):
    """
    - *(dict) --*

      Returns information about the details of an action type.
      - **id** *(dict) --*

        Represents information about an action type.
        - **category** *(string) --*

          A category defines what kind of action can be taken in the stage, and constrains the
          provider type for the action. Valid categories are limited to one of the following values.
    """


_ListActionTypesPaginateResponseTypeDef = TypedDict(
    "_ListActionTypesPaginateResponseTypeDef",
    {"actionTypes": List[ListActionTypesPaginateResponseactionTypesTypeDef], "NextToken": str},
    total=False,
)


class ListActionTypesPaginateResponseTypeDef(_ListActionTypesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``ListActionTypes`` action.
      - **actionTypes** *(list) --*

        Provides details of the action types.
        - *(dict) --*

          Returns information about the details of an action type.
          - **id** *(dict) --*

            Represents information about an action type.
            - **category** *(string) --*

              A category defines what kind of action can be taken in the stage, and constrains the
              provider type for the action. Valid categories are limited to one of the following
              values.
    """


_ListPipelineExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPipelineExecutionsPaginatePaginationConfigTypeDef(
    _ListPipelineExecutionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef",
    {"actionName": str, "revisionId": str, "revisionSummary": str, "revisionUrl": str},
    total=False,
)


class ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef(
    _ListPipelineExecutionsPaginateResponsepipelineExecutionSummariessourceRevisionsTypeDef
):
    pass


_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef",
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


class ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef(
    _ListPipelineExecutionsPaginateResponsepipelineExecutionSummariestriggerTypeDef
):
    pass


_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef",
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


class ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef(
    _ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information about a pipeline execution.
      - **pipelineExecutionId** *(string) --*

        The ID of the pipeline execution.
    """


_ListPipelineExecutionsPaginateResponseTypeDef = TypedDict(
    "_ListPipelineExecutionsPaginateResponseTypeDef",
    {
        "pipelineExecutionSummaries": List[
            ListPipelineExecutionsPaginateResponsepipelineExecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListPipelineExecutionsPaginateResponseTypeDef(_ListPipelineExecutionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``ListPipelineExecutions`` action.
      - **pipelineExecutionSummaries** *(list) --*

        A list of executions in the history of a pipeline.
        - *(dict) --*

          Summary information about a pipeline execution.
          - **pipelineExecutionId** *(string) --*

            The ID of the pipeline execution.
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


_ListPipelinesPaginateResponsepipelinesTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsepipelinesTypeDef",
    {"name": str, "version": int, "created": datetime, "updated": datetime},
    total=False,
)


class ListPipelinesPaginateResponsepipelinesTypeDef(_ListPipelinesPaginateResponsepipelinesTypeDef):
    """
    - *(dict) --*

      Returns a summary of a pipeline.
      - **name** *(string) --*

        The name of the pipeline.
    """


_ListPipelinesPaginateResponseTypeDef = TypedDict(
    "_ListPipelinesPaginateResponseTypeDef",
    {"pipelines": List[ListPipelinesPaginateResponsepipelinesTypeDef], "NextToken": str},
    total=False,
)


class ListPipelinesPaginateResponseTypeDef(_ListPipelinesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``ListPipelines`` action.
      - **pipelines** *(list) --*

        The list of pipelines.
        - *(dict) --*

          Returns a summary of a pipeline.
          - **name** *(string) --*

            The name of the pipeline.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ListTagsForResourcePaginateResponsetagsTypeDef(
    _ListTagsForResourcePaginateResponsetagsTypeDef
):
    """
    - *(dict) --*

      A tag is a key-value pair that is used to manage the resource.
      - **key** *(string) --*

        The tag's key.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        The tags for the resource.
        - *(dict) --*

          A tag is a key-value pair that is used to manage the resource.
          - **key** *(string) --*

            The tag's key.
    """


_ListWebhooksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListWebhooksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListWebhooksPaginatePaginationConfigTypeDef(_ListWebhooksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef",
    {"AllowedIPRange": str, "SecretToken": str},
    total=False,
)


class ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef(
    _ListWebhooksPaginateResponsewebhooksdefinitionauthenticationConfigurationTypeDef
):
    pass


_ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef",
    {"jsonPath": str, "matchEquals": str},
    total=False,
)


class ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef(
    _ListWebhooksPaginateResponsewebhooksdefinitionfiltersTypeDef
):
    pass


_ListWebhooksPaginateResponsewebhooksdefinitionTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhooksdefinitionTypeDef",
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


class ListWebhooksPaginateResponsewebhooksdefinitionTypeDef(
    _ListWebhooksPaginateResponsewebhooksdefinitionTypeDef
):
    """
    - **definition** *(dict) --*

      The detail returned for each webhook, such as the webhook authentication type and filter
      rules.
      - **name** *(string) --*

        The name of the webhook.
    """


_ListWebhooksPaginateResponsewebhookstagsTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhookstagsTypeDef", {"key": str, "value": str}, total=False
)


class ListWebhooksPaginateResponsewebhookstagsTypeDef(
    _ListWebhooksPaginateResponsewebhookstagsTypeDef
):
    pass


_ListWebhooksPaginateResponsewebhooksTypeDef = TypedDict(
    "_ListWebhooksPaginateResponsewebhooksTypeDef",
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


class ListWebhooksPaginateResponsewebhooksTypeDef(_ListWebhooksPaginateResponsewebhooksTypeDef):
    """
    - *(dict) --*

      The detail returned for each webhook after listing webhooks, such as the webhook URL, the
      webhook name, and the webhook ARN.
      - **definition** *(dict) --*

        The detail returned for each webhook, such as the webhook authentication type and filter
        rules.
        - **name** *(string) --*

          The name of the webhook.
    """


_ListWebhooksPaginateResponseTypeDef = TypedDict(
    "_ListWebhooksPaginateResponseTypeDef",
    {"webhooks": List[ListWebhooksPaginateResponsewebhooksTypeDef]},
    total=False,
)


class ListWebhooksPaginateResponseTypeDef(_ListWebhooksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **webhooks** *(list) --*

        The JSON detail returned for each webhook in the list output for the ListWebhooks call.
        - *(dict) --*

          The detail returned for each webhook after listing webhooks, such as the webhook URL, the
          webhook name, and the webhook ARN.
          - **definition** *(dict) --*

            The detail returned for each webhook, such as the webhook authentication type and filter
            rules.
            - **name** *(string) --*

              The name of the webhook.
    """
