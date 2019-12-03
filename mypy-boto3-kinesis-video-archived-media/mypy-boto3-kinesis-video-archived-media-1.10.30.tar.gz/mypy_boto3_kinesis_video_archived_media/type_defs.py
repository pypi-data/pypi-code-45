"Main interface for kinesis-video-archived-media service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef",
    "ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef",
    "ClientGetDashStreamingSessionUrlResponseTypeDef",
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef",
    "ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef",
    "ClientGetHlsStreamingSessionUrlResponseTypeDef",
    "ClientGetMediaForFragmentListResponseTypeDef",
    "ClientListFragmentsFragmentSelectorTimestampRangeTypeDef",
    "ClientListFragmentsFragmentSelectorTypeDef",
    "ClientListFragmentsResponseFragmentsTypeDef",
    "ClientListFragmentsResponseTypeDef",
    "ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef",
    "ListFragmentsPaginateFragmentSelectorTypeDef",
    "ListFragmentsPaginatePaginationConfigTypeDef",
    "ListFragmentsPaginateResponseFragmentsTypeDef",
    "ListFragmentsPaginateResponseTypeDef",
)


_ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "_ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)


class ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef(
    _ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef
):
    pass


_ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef = TypedDict(
    "_ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": ClientGetDashStreamingSessionUrlDASHFragmentSelectorTimestampRangeTypeDef,
    },
    total=False,
)


class ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef(
    _ClientGetDashStreamingSessionUrlDASHFragmentSelectorTypeDef
):
    """
    The time range of the requested fragment and the source of the timestamps.
    This parameter is required if ``PlaybackMode`` is ``ON_DEMAND`` or ``LIVE_REPLAY`` . This
    parameter is optional if PlaybackMode is ``LIVE`` . If ``PlaybackMode`` is ``LIVE`` , the
    ``FragmentSelectorType`` can be set, but the ``TimestampRange`` should not be set. If
    ``PlaybackMode`` is ``ON_DEMAND`` or ``LIVE_REPLAY`` , both ``FragmentSelectorType`` and
    ``TimestampRange`` must be set.
    - **FragmentSelectorType** *(string) --*

      The source of the timestamps for the requested media.
      When ``FragmentSelectorType`` is set to ``PRODUCER_TIMESTAMP`` and
      GetDASHStreamingSessionURLInput$PlaybackMode is ``ON_DEMAND`` or ``LIVE_REPLAY`` , the first
      fragment ingested with a producer timestamp within the specified
      FragmentSelector$TimestampRange is included in the media playlist. In addition, the fragments
      with producer timestamps within the ``TimestampRange`` ingested immediately following the
      first fragment (up to the  GetDASHStreamingSessionURLInput$MaxManifestFragmentResults value)
      are included.
      Fragments that have duplicate producer timestamps are deduplicated. This means that if
      producers are producing a stream of fragments with producer timestamps that are approximately
      equal to the true clock time, the MPEG-DASH manifest will contain all of the fragments within
      the requested timestamp range. If some fragments are ingested within the same time range and
      very different points in time, only the oldest ingested collection of fragments are returned.
      When ``FragmentSelectorType`` is set to ``PRODUCER_TIMESTAMP`` and
      GetDASHStreamingSessionURLInput$PlaybackMode is ``LIVE`` , the producer timestamps are used in
      the MP4 fragments and for deduplication. But the most recently ingested fragments based on
      server timestamps are included in the MPEG-DASH manifest. This means that even if fragments
      ingested in the past have producer timestamps with values now, they are not included in the
      HLS media playlist.
      The default is ``SERVER_TIMESTAMP`` .
    """


_ClientGetDashStreamingSessionUrlResponseTypeDef = TypedDict(
    "_ClientGetDashStreamingSessionUrlResponseTypeDef",
    {"DASHStreamingSessionURL": str},
    total=False,
)


class ClientGetDashStreamingSessionUrlResponseTypeDef(
    _ClientGetDashStreamingSessionUrlResponseTypeDef
):
    """
    - *(dict) --*

      - **DASHStreamingSessionURL** *(string) --*

        The URL (containing the session token) that a media player can use to retrieve the MPEG-DASH
        manifest.
    """


_ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "_ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)


class ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef(
    _ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef
):
    pass


_ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef = TypedDict(
    "_ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTimestampRangeTypeDef,
    },
    total=False,
)


class ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef(
    _ClientGetHlsStreamingSessionUrlHLSFragmentSelectorTypeDef
):
    """
    The time range of the requested fragment and the source of the timestamps.
    This parameter is required if ``PlaybackMode`` is ``ON_DEMAND`` or ``LIVE_REPLAY`` . This
    parameter is optional if PlaybackMode is ``LIVE`` . If ``PlaybackMode`` is ``LIVE`` , the
    ``FragmentSelectorType`` can be set, but the ``TimestampRange`` should not be set. If
    ``PlaybackMode`` is ``ON_DEMAND`` or ``LIVE_REPLAY`` , both ``FragmentSelectorType`` and
    ``TimestampRange`` must be set.
    - **FragmentSelectorType** *(string) --*

      The source of the timestamps for the requested media.
      When ``FragmentSelectorType`` is set to ``PRODUCER_TIMESTAMP`` and
      GetHLSStreamingSessionURLInput$PlaybackMode is ``ON_DEMAND`` or ``LIVE_REPLAY`` , the first
      fragment ingested with a producer timestamp within the specified
      FragmentSelector$TimestampRange is included in the media playlist. In addition, the fragments
      with producer timestamps within the ``TimestampRange`` ingested immediately following the
      first fragment (up to the  GetHLSStreamingSessionURLInput$MaxMediaPlaylistFragmentResults
      value) are included.
      Fragments that have duplicate producer timestamps are deduplicated. This means that if
      producers are producing a stream of fragments with producer timestamps that are approximately
      equal to the true clock time, the HLS media playlists will contain all of the fragments within
      the requested timestamp range. If some fragments are ingested within the same time range and
      very different points in time, only the oldest ingested collection of fragments are returned.
      When ``FragmentSelectorType`` is set to ``PRODUCER_TIMESTAMP`` and
      GetHLSStreamingSessionURLInput$PlaybackMode is ``LIVE`` , the producer timestamps are used in
      the MP4 fragments and for deduplication. But the most recently ingested fragments based on
      server timestamps are included in the HLS media playlist. This means that even if fragments
      ingested in the past have producer timestamps with values now, they are not included in the
      HLS media playlist.
      The default is ``SERVER_TIMESTAMP`` .
    """


_ClientGetHlsStreamingSessionUrlResponseTypeDef = TypedDict(
    "_ClientGetHlsStreamingSessionUrlResponseTypeDef", {"HLSStreamingSessionURL": str}, total=False
)


class ClientGetHlsStreamingSessionUrlResponseTypeDef(
    _ClientGetHlsStreamingSessionUrlResponseTypeDef
):
    """
    - *(dict) --*

      - **HLSStreamingSessionURL** *(string) --*

        The URL (containing the session token) that a media player can use to retrieve the HLS
        master playlist.
    """


_ClientGetMediaForFragmentListResponseTypeDef = TypedDict(
    "_ClientGetMediaForFragmentListResponseTypeDef",
    {"ContentType": str, "Payload": StreamingBody},
    total=False,
)


class ClientGetMediaForFragmentListResponseTypeDef(_ClientGetMediaForFragmentListResponseTypeDef):
    """
    - *(dict) --*

      - **ContentType** *(string) --*

        The content type of the requested media.
    """


_ClientListFragmentsFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "_ClientListFragmentsFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)


class ClientListFragmentsFragmentSelectorTimestampRangeTypeDef(
    _ClientListFragmentsFragmentSelectorTimestampRangeTypeDef
):
    pass


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
    """
    Describes the timestamp range and timestamp origin for the range of fragments to return.
    - **FragmentSelectorType** *(string) --***[REQUIRED]**

      The origin of the timestamps to use (Server or Producer).
    """


_ClientListFragmentsResponseFragmentsTypeDef = TypedDict(
    "_ClientListFragmentsResponseFragmentsTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)


class ClientListFragmentsResponseFragmentsTypeDef(_ClientListFragmentsResponseFragmentsTypeDef):
    """
    - *(dict) --*

      Represents a segment of video or other time-delimited data.
      - **FragmentNumber** *(string) --*

        The unique identifier of the fragment. This value monotonically increases based on the
        ingestion order.
    """


_ClientListFragmentsResponseTypeDef = TypedDict(
    "_ClientListFragmentsResponseTypeDef",
    {"Fragments": List[ClientListFragmentsResponseFragmentsTypeDef], "NextToken": str},
    total=False,
)


class ClientListFragmentsResponseTypeDef(_ClientListFragmentsResponseTypeDef):
    """
    - *(dict) --*

      - **Fragments** *(list) --*

        A list of archived  Fragment objects from the stream that meet the selector criteria.
        Results are in no specific order, even across pages.
        - *(dict) --*

          Represents a segment of video or other time-delimited data.
          - **FragmentNumber** *(string) --*

            The unique identifier of the fragment. This value monotonically increases based on the
            ingestion order.
    """


_ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef = TypedDict(
    "_ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef",
    {"StartTimestamp": datetime, "EndTimestamp": datetime},
    total=False,
)


class ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef(
    _ListFragmentsPaginateFragmentSelectorTimestampRangeTypeDef
):
    pass


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
    """
    Describes the timestamp range and timestamp origin for the range of fragments to return.
    - **FragmentSelectorType** *(string) --***[REQUIRED]**

      The origin of the timestamps to use (Server or Producer).
    """


_ListFragmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFragmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFragmentsPaginatePaginationConfigTypeDef(_ListFragmentsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFragmentsPaginateResponseFragmentsTypeDef = TypedDict(
    "_ListFragmentsPaginateResponseFragmentsTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)


class ListFragmentsPaginateResponseFragmentsTypeDef(_ListFragmentsPaginateResponseFragmentsTypeDef):
    """
    - *(dict) --*

      Represents a segment of video or other time-delimited data.
      - **FragmentNumber** *(string) --*

        The unique identifier of the fragment. This value monotonically increases based on the
        ingestion order.
    """


_ListFragmentsPaginateResponseTypeDef = TypedDict(
    "_ListFragmentsPaginateResponseTypeDef",
    {"Fragments": List[ListFragmentsPaginateResponseFragmentsTypeDef]},
    total=False,
)


class ListFragmentsPaginateResponseTypeDef(_ListFragmentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Fragments** *(list) --*

        A list of archived  Fragment objects from the stream that meet the selector criteria.
        Results are in no specific order, even across pages.
        - *(dict) --*

          Represents a segment of video or other time-delimited data.
          - **FragmentNumber** *(string) --*

            The unique identifier of the fragment. This value monotonically increases based on the
            ingestion order.
    """
