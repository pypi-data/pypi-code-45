"Main interface for workmailmessageflow service type defs"
from __future__ import annotations

import sys
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientGetRawMessageContentResponseTypeDef = TypedDict(
    "ClientGetRawMessageContentResponseTypeDef", {"messageContent": StreamingBody}, total=False
)
