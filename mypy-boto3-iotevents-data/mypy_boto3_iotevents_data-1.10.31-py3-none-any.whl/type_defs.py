"Main interface for iotevents-data service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchPutMessageMessagesTypeDef",
    "ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef",
    "ClientBatchPutMessageResponseTypeDef",
    "ClientBatchUpdateDetectorDetectorsstatetimersTypeDef",
    "ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef",
    "ClientBatchUpdateDetectorDetectorsstateTypeDef",
    "ClientBatchUpdateDetectorDetectorsTypeDef",
    "ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef",
    "ClientBatchUpdateDetectorResponseTypeDef",
    "ClientDescribeDetectorResponsedetectorstatetimersTypeDef",
    "ClientDescribeDetectorResponsedetectorstatevariablesTypeDef",
    "ClientDescribeDetectorResponsedetectorstateTypeDef",
    "ClientDescribeDetectorResponsedetectorTypeDef",
    "ClientDescribeDetectorResponseTypeDef",
    "ClientListDetectorsResponsedetectorSummariesstateTypeDef",
    "ClientListDetectorsResponsedetectorSummariesTypeDef",
    "ClientListDetectorsResponseTypeDef",
)


_RequiredClientBatchPutMessageMessagesTypeDef = TypedDict(
    "_RequiredClientBatchPutMessageMessagesTypeDef", {"messageId": str}
)
_OptionalClientBatchPutMessageMessagesTypeDef = TypedDict(
    "_OptionalClientBatchPutMessageMessagesTypeDef",
    {"inputName": str, "payload": bytes},
    total=False,
)


class ClientBatchPutMessageMessagesTypeDef(
    _RequiredClientBatchPutMessageMessagesTypeDef, _OptionalClientBatchPutMessageMessagesTypeDef
):
    """
    - *(dict) --*

      Information about a message.
      - **messageId** *(string) --***[REQUIRED]**

        The ID to assign to the message. Within each batch sent, each ``"messageId"`` must be
        unique.
    """


_ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef = TypedDict(
    "_ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef",
    {
        "messageId": str,
        "errorCode": Literal[
            "ResourceNotFoundException",
            "InvalidRequestException",
            "InternalFailureException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ],
        "errorMessage": str,
    },
    total=False,
)


class ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef(
    _ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef
):
    """
    - *(dict) --*

      Contains information about the errors encountered.
      - **messageId** *(string) --*

        The ID of the message that caused the error. (See the value corresponding to the
        ``"messageId"`` key in the ``"message"`` object.)
    """


_ClientBatchPutMessageResponseTypeDef = TypedDict(
    "_ClientBatchPutMessageResponseTypeDef",
    {
        "BatchPutMessageErrorEntries": List[
            ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef
        ]
    },
    total=False,
)


class ClientBatchPutMessageResponseTypeDef(_ClientBatchPutMessageResponseTypeDef):
    """
    - *(dict) --*

      - **BatchPutMessageErrorEntries** *(list) --*

        A list of any errors encountered when sending the messages.
        - *(dict) --*

          Contains information about the errors encountered.
          - **messageId** *(string) --*

            The ID of the message that caused the error. (See the value corresponding to the
            ``"messageId"`` key in the ``"message"`` object.)
    """


_ClientBatchUpdateDetectorDetectorsstatetimersTypeDef = TypedDict(
    "_ClientBatchUpdateDetectorDetectorsstatetimersTypeDef",
    {"name": str, "seconds": int},
    total=False,
)


class ClientBatchUpdateDetectorDetectorsstatetimersTypeDef(
    _ClientBatchUpdateDetectorDetectorsstatetimersTypeDef
):
    pass


_ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef = TypedDict(
    "_ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef(
    _ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef
):
    pass


_ClientBatchUpdateDetectorDetectorsstateTypeDef = TypedDict(
    "_ClientBatchUpdateDetectorDetectorsstateTypeDef",
    {
        "stateName": str,
        "variables": List[ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef],
        "timers": List[ClientBatchUpdateDetectorDetectorsstatetimersTypeDef],
    },
    total=False,
)


class ClientBatchUpdateDetectorDetectorsstateTypeDef(
    _ClientBatchUpdateDetectorDetectorsstateTypeDef
):
    pass


_RequiredClientBatchUpdateDetectorDetectorsTypeDef = TypedDict(
    "_RequiredClientBatchUpdateDetectorDetectorsTypeDef", {"messageId": str}
)
_OptionalClientBatchUpdateDetectorDetectorsTypeDef = TypedDict(
    "_OptionalClientBatchUpdateDetectorDetectorsTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "state": ClientBatchUpdateDetectorDetectorsstateTypeDef,
    },
    total=False,
)


class ClientBatchUpdateDetectorDetectorsTypeDef(
    _RequiredClientBatchUpdateDetectorDetectorsTypeDef,
    _OptionalClientBatchUpdateDetectorDetectorsTypeDef,
):
    """
    - *(dict) --*

      Information used to update the detector (instance).
      - **messageId** *(string) --***[REQUIRED]**

        The ID to assign to the detector update ``"message"`` . Each ``"messageId"`` must be unique
        within each batch sent.
    """


_ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef = TypedDict(
    "_ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef",
    {
        "messageId": str,
        "errorCode": Literal[
            "ResourceNotFoundException",
            "InvalidRequestException",
            "InternalFailureException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ],
        "errorMessage": str,
    },
    total=False,
)


class ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef(
    _ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef
):
    """
    - *(dict) --*

      Information about the error that occured when attempting to update a detector.
      - **messageId** *(string) --*

        The ``"messageId"`` of the update request that caused the error. (The value of the
        ``"messageId"`` in the update request ``"Detector"`` object.)
    """


_ClientBatchUpdateDetectorResponseTypeDef = TypedDict(
    "_ClientBatchUpdateDetectorResponseTypeDef",
    {
        "batchUpdateDetectorErrorEntries": List[
            ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef
        ]
    },
    total=False,
)


class ClientBatchUpdateDetectorResponseTypeDef(_ClientBatchUpdateDetectorResponseTypeDef):
    """
    - *(dict) --*

      - **batchUpdateDetectorErrorEntries** *(list) --*

        A list of those detector updates that resulted in errors. (If an error is listed here, the
        specific update did not occur.)
        - *(dict) --*

          Information about the error that occured when attempting to update a detector.
          - **messageId** *(string) --*

            The ``"messageId"`` of the update request that caused the error. (The value of the
            ``"messageId"`` in the update request ``"Detector"`` object.)
    """


_ClientDescribeDetectorResponsedetectorstatetimersTypeDef = TypedDict(
    "_ClientDescribeDetectorResponsedetectorstatetimersTypeDef",
    {"name": str, "timestamp": datetime},
    total=False,
)


class ClientDescribeDetectorResponsedetectorstatetimersTypeDef(
    _ClientDescribeDetectorResponsedetectorstatetimersTypeDef
):
    pass


_ClientDescribeDetectorResponsedetectorstatevariablesTypeDef = TypedDict(
    "_ClientDescribeDetectorResponsedetectorstatevariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeDetectorResponsedetectorstatevariablesTypeDef(
    _ClientDescribeDetectorResponsedetectorstatevariablesTypeDef
):
    pass


_ClientDescribeDetectorResponsedetectorstateTypeDef = TypedDict(
    "_ClientDescribeDetectorResponsedetectorstateTypeDef",
    {
        "stateName": str,
        "variables": List[ClientDescribeDetectorResponsedetectorstatevariablesTypeDef],
        "timers": List[ClientDescribeDetectorResponsedetectorstatetimersTypeDef],
    },
    total=False,
)


class ClientDescribeDetectorResponsedetectorstateTypeDef(
    _ClientDescribeDetectorResponsedetectorstateTypeDef
):
    pass


_ClientDescribeDetectorResponsedetectorTypeDef = TypedDict(
    "_ClientDescribeDetectorResponsedetectorTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": ClientDescribeDetectorResponsedetectorstateTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeDetectorResponsedetectorTypeDef(_ClientDescribeDetectorResponsedetectorTypeDef):
    """
    - **detector** *(dict) --*

      Information about the detector (instance).
      - **detectorModelName** *(string) --*

        The name of the detector model that created this detector (instance).
    """


_ClientDescribeDetectorResponseTypeDef = TypedDict(
    "_ClientDescribeDetectorResponseTypeDef",
    {"detector": ClientDescribeDetectorResponsedetectorTypeDef},
    total=False,
)


class ClientDescribeDetectorResponseTypeDef(_ClientDescribeDetectorResponseTypeDef):
    """
    - *(dict) --*

      - **detector** *(dict) --*

        Information about the detector (instance).
        - **detectorModelName** *(string) --*

          The name of the detector model that created this detector (instance).
    """


_ClientListDetectorsResponsedetectorSummariesstateTypeDef = TypedDict(
    "_ClientListDetectorsResponsedetectorSummariesstateTypeDef", {"stateName": str}, total=False
)


class ClientListDetectorsResponsedetectorSummariesstateTypeDef(
    _ClientListDetectorsResponsedetectorSummariesstateTypeDef
):
    pass


_ClientListDetectorsResponsedetectorSummariesTypeDef = TypedDict(
    "_ClientListDetectorsResponsedetectorSummariesTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": ClientListDetectorsResponsedetectorSummariesstateTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientListDetectorsResponsedetectorSummariesTypeDef(
    _ClientListDetectorsResponsedetectorSummariesTypeDef
):
    """
    - *(dict) --*

      Information about the detector (instance).
      - **detectorModelName** *(string) --*

        The name of the detector model that created this detector (instance).
    """


_ClientListDetectorsResponseTypeDef = TypedDict(
    "_ClientListDetectorsResponseTypeDef",
    {
        "detectorSummaries": List[ClientListDetectorsResponsedetectorSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDetectorsResponseTypeDef(_ClientListDetectorsResponseTypeDef):
    """
    - *(dict) --*

      - **detectorSummaries** *(list) --*

        A list of summary information about the detectors (instances).
        - *(dict) --*

          Information about the detector (instance).
          - **detectorModelName** *(string) --*

            The name of the detector model that created this detector (instance).
    """
