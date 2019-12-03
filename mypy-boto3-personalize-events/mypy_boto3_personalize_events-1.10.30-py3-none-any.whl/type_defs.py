"Main interface for personalize-events service type defs"
from __future__ import annotations

from datetime import datetime
from mypy_boto3.type_defs import TypedDict


__all__ = ("ClientPutEventsEventListTypeDef",)


_ClientPutEventsEventListTypeDef = TypedDict(
    "_ClientPutEventsEventListTypeDef",
    {"eventId": str, "eventType": str, "properties": str, "sentAt": datetime},
    total=False,
)


class ClientPutEventsEventListTypeDef(_ClientPutEventsEventListTypeDef):
    """
    - *(dict) --*

      Represents user interaction event information sent using the ``PutEvents`` API.
      - **eventId** *(string) --*

        An ID associated with the event. If an event ID is not provided, Amazon Personalize
        generates a unique ID for the event. An event ID is not used as an input to the model.
        Amazon Personalize uses the event ID to distinquish unique events. Any subsequent events
        after the first with the same event ID are not used in model training.
    """
