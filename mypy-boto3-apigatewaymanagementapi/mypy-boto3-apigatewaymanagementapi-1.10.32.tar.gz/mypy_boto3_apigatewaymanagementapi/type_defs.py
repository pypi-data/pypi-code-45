"Main interface for apigatewaymanagementapi service type defs"
from __future__ import annotations

from datetime import datetime
from mypy_boto3.type_defs import TypedDict


__all__ = ("ClientGetConnectionResponseIdentityTypeDef", "ClientGetConnectionResponseTypeDef")


_ClientGetConnectionResponseIdentityTypeDef = TypedDict(
    "_ClientGetConnectionResponseIdentityTypeDef", {"SourceIp": str, "UserAgent": str}, total=False
)


class ClientGetConnectionResponseIdentityTypeDef(_ClientGetConnectionResponseIdentityTypeDef):
    pass


_ClientGetConnectionResponseTypeDef = TypedDict(
    "_ClientGetConnectionResponseTypeDef",
    {
        "ConnectedAt": datetime,
        "Identity": ClientGetConnectionResponseIdentityTypeDef,
        "LastActiveAt": datetime,
    },
    total=False,
)


class ClientGetConnectionResponseTypeDef(_ClientGetConnectionResponseTypeDef):
    """
    - *(dict) --*

      - **ConnectedAt** *(datetime) --*

        The time in ISO 8601 format for when the connection was established.
    """
