"Main interface for kinesis-video-archived-media service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)

ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef = TypedDict(
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef,
    },
    total=False,
)

ClientGetDashStreamingSessionUrlResponseTypeDef = TypedDict(
    "ClientGetDashStreamingSessionUrlResponseTypeDef", {"DASHStreamingSessionURL": str}, total=False
)

ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)

ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef = TypedDict(
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef,
    },
    total=False,
)

ClientGetHlsStreamingSessionUrlResponseTypeDef = TypedDict(
    "ClientGetHlsStreamingSessionUrlResponseTypeDef", {"HLSStreamingSessionURL": str}, total=False
)

ClientGetMediaForFragmentListResponseTypeDef = TypedDict(
    "ClientGetMediaForFragmentListResponseTypeDef",
    {"ContentType": str, "Payload": StreamingBody},
    total=False,
)

ClientListFragmentsFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "ClientListFragmentsFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)

_RequiredClientListFragmentsFragmentSelectorTypeDef = TypedDict(
    "_RequiredClientListFragmentsFragmentSelectorTypeDef",
    {"FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]},
)
_OptionalClientListFragmentsFragmentSelectorTypeDef = TypedDict(
    "_OptionalClientListFragmentsFragmentSelectorTypeDef",
    {"TimestampRange": ClientListFragmentsFragmentSelectorTimestampRangeTypeDef},
    total=False,
)


class ClientListFragmentsFragmentSelectorTypeDef(
    _RequiredClientListFragmentsFragmentSelectorTypeDef,
    _OptionalClientListFragmentsFragmentSelectorTypeDef,
):
    pass


ClientListFragmentsResponseFragmentsTypeDef = TypedDict(
    "ClientListFragmentsResponseFragmentsTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)

ClientListFragmentsResponseTypeDef = TypedDict(
    "ClientListFragmentsResponseTypeDef",
    {"Fragments": List[ClientListFragmentsResponseFragmentsTypeDef], "NextToken": str},
    total=False,
)

ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)

_RequiredListFragmentsPaginateFragmentSelectorTypeDef = TypedDict(
    "_RequiredListFragmentsPaginateFragmentSelectorTypeDef",
    {"FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]},
)
_OptionalListFragmentsPaginateFragmentSelectorTypeDef = TypedDict(
    "_OptionalListFragmentsPaginateFragmentSelectorTypeDef",
    {"TimestampRange": ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef},
    total=False,
)


class ListFragmentsPaginateFragmentSelectorTypeDef(
    _RequiredListFragmentsPaginateFragmentSelectorTypeDef,
    _OptionalListFragmentsPaginateFragmentSelectorTypeDef,
):
    pass


ListFragmentsPaginatePaginationConfigTypeDef = TypedDict(
    "ListFragmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListFragmentsPaginateResponseFragmentsTypeDef = TypedDict(
    "ListFragmentsPaginateResponseFragmentsTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)

ListFragmentsPaginateResponseTypeDef = TypedDict(
    "ListFragmentsPaginateResponseTypeDef",
    {"Fragments": List[ListFragmentsPaginateResponseFragmentsTypeDef]},
    total=False,
)
