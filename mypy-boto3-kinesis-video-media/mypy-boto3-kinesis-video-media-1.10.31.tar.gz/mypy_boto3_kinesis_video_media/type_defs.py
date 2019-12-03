"Main interface for kinesis-video-media service type defs"
from __future__ import annotations

from datetime import datetime
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = ("ClientGetMediaResponseTypeDef", "ClientGetMediaStartSelectorTypeDef")


_ClientGetMediaResponseTypeDef = TypedDict(
    "_ClientGetMediaResponseTypeDef", {"ContentType": str, "Payload": StreamingBody}, total=False
)


class ClientGetMediaResponseTypeDef(_ClientGetMediaResponseTypeDef):
    """
    - *(dict) --*

      - **ContentType** *(string) --*

        The content type of the requested media.
    """


_RequiredClientGetMediaStartSelectorTypeDef = TypedDict(
    "_RequiredClientGetMediaStartSelectorTypeDef",
    {
        "StartSelectorType": Literal[
            "FRAGMENT_NUMBER",
            "SERVER_TIMESTAMP",
            "PRODUCER_TIMESTAMP",
            "NOW",
            "EARLIEST",
            "CONTINUATION_TOKEN",
        ]
    },
)
_OptionalClientGetMediaStartSelectorTypeDef = TypedDict(
    "_OptionalClientGetMediaStartSelectorTypeDef",
    {"AfterFragmentNumber": str, "StartTimestamp": datetime, "ContinuationToken": str},
    total=False,
)


class ClientGetMediaStartSelectorTypeDef(
    _RequiredClientGetMediaStartSelectorTypeDef, _OptionalClientGetMediaStartSelectorTypeDef
):
    """
    Identifies the starting chunk to get from the specified stream.
    - **StartSelectorType** *(string) --***[REQUIRED]**

      Identifies the fragment on the Kinesis video stream where you want to start getting the data
      from.
      * NOW - Start with the latest chunk on the stream.
      * EARLIEST - Start with earliest available chunk on the stream.
      * FRAGMENT_NUMBER - Start with the chunk after a specific fragment. You must also specify the
      ``AfterFragmentNumber`` parameter.
      * PRODUCER_TIMESTAMP or SERVER_TIMESTAMP - Start with the chunk containing a fragment with the
      specified producer or server timestamp. You specify the timestamp by adding ``StartTimestamp``
      .
      * CONTINUATION_TOKEN - Read using the specified continuation token.
      .. note::

        If you choose the NOW, EARLIEST, or CONTINUATION_TOKEN as the ``startSelectorType`` , you
        don't provide any additional information in the ``startSelector`` .
    """
