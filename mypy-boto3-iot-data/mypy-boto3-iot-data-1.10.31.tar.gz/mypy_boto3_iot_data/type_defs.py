"Main interface for iot-data service type defs"
from __future__ import annotations

from botocore.response import StreamingBody
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientDeleteThingShadowResponseTypeDef",
    "ClientGetThingShadowResponseTypeDef",
    "ClientUpdateThingShadowResponseTypeDef",
)


_ClientDeleteThingShadowResponseTypeDef = TypedDict(
    "_ClientDeleteThingShadowResponseTypeDef", {"payload": StreamingBody}, total=False
)


class ClientDeleteThingShadowResponseTypeDef(_ClientDeleteThingShadowResponseTypeDef):
    """
    - *(dict) --*

      The output from the DeleteThingShadow operation.
      - **payload** (:class:`.StreamingBody`) --

        The state information, in JSON format.
    """


_ClientGetThingShadowResponseTypeDef = TypedDict(
    "_ClientGetThingShadowResponseTypeDef", {"payload": StreamingBody}, total=False
)


class ClientGetThingShadowResponseTypeDef(_ClientGetThingShadowResponseTypeDef):
    """
    - *(dict) --*

      The output from the GetThingShadow operation.
      - **payload** (:class:`.StreamingBody`) --

        The state information, in JSON format.
    """


_ClientUpdateThingShadowResponseTypeDef = TypedDict(
    "_ClientUpdateThingShadowResponseTypeDef", {"payload": StreamingBody}, total=False
)


class ClientUpdateThingShadowResponseTypeDef(_ClientUpdateThingShadowResponseTypeDef):
    """
    - *(dict) --*

      The output from the UpdateThingShadow operation.
      - **payload** (:class:`.StreamingBody`) --

        The state information, in JSON format.
    """
