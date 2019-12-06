"Main interface for personalize-events service type defs"
from __future__ import annotations

from datetime import datetime
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientPutEventsEventListTypeDef = TypedDict(
    "ClientPutEventsEventListTypeDef",
    {"eventId": str, "eventType": str, "properties": str, "sentAt": datetime},
    total=False,
)
