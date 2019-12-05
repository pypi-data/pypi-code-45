"Main interface for kinesis-video-signaling service type defs"
from __future__ import annotations

import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientGetIceServerConfigResponseIceServerListTypeDef = TypedDict(
    "ClientGetIceServerConfigResponseIceServerListTypeDef",
    {"Uris": List[str], "Username": str, "Password": str, "Ttl": int},
    total=False,
)

ClientGetIceServerConfigResponseTypeDef = TypedDict(
    "ClientGetIceServerConfigResponseTypeDef",
    {"IceServerList": List[ClientGetIceServerConfigResponseIceServerListTypeDef]},
    total=False,
)

ClientSendAlexaOfferToMasterResponseTypeDef = TypedDict(
    "ClientSendAlexaOfferToMasterResponseTypeDef", {"Answer": str}, total=False
)
