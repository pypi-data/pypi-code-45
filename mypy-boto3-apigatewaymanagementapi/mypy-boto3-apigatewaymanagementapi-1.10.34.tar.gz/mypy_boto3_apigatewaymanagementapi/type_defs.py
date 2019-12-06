"Main interface for apigatewaymanagementapi service type defs"
from __future__ import annotations

from datetime import datetime
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientGetConnectionResponseIdentityTypeDef = TypedDict(
    "ClientGetConnectionResponseIdentityTypeDef", {"SourceIp": str, "UserAgent": str}, total=False
)

ClientGetConnectionResponseTypeDef = TypedDict(
    "ClientGetConnectionResponseTypeDef",
    {
        "ConnectedAt": datetime,
        "Identity": ClientGetConnectionResponseIdentityTypeDef,
        "LastActiveAt": datetime,
    },
    total=False,
)
