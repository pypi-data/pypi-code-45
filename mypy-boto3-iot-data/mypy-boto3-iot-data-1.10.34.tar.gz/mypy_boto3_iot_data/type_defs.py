"Main interface for iot-data service type defs"
from __future__ import annotations

import sys
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientDeleteThingShadowResponseTypeDef = TypedDict(
    "ClientDeleteThingShadowResponseTypeDef", {"payload": StreamingBody}, total=False
)

ClientGetThingShadowResponseTypeDef = TypedDict(
    "ClientGetThingShadowResponseTypeDef", {"payload": StreamingBody}, total=False
)

ClientUpdateThingShadowResponseTypeDef = TypedDict(
    "ClientUpdateThingShadowResponseTypeDef", {"payload": StreamingBody}, total=False
)
