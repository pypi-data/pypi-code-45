"Main interface for mediatailor service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef",
    "ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef",
    "ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef",
    "ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    "ClientGetPlaybackConfigurationResponseTypeDef",
    "ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef",
    "ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef",
    "ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef",
    "ClientListPlaybackConfigurationsResponseItemsTypeDef",
    "ClientListPlaybackConfigurationsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutPlaybackConfigurationCdnConfigurationTypeDef",
    "ClientPutPlaybackConfigurationDashConfigurationTypeDef",
    "ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    "ClientPutPlaybackConfigurationResponseTypeDef",
    "ListPlaybackConfigurationsPaginatePaginationConfigTypeDef",
    "ListPlaybackConfigurationsPaginateResponseItemsCdnConfigurationTypeDef",
    "ListPlaybackConfigurationsPaginateResponseItemsDashConfigurationTypeDef",
    "ListPlaybackConfigurationsPaginateResponseItemsHlsConfigurationTypeDef",
    "ListPlaybackConfigurationsPaginateResponseItemsTypeDef",
    "ListPlaybackConfigurationsPaginateResponseTypeDef",
)


_ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef = TypedDict(
    "_ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)


class ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef(
    _ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef
):
    pass


_ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef = TypedDict(
    "_ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)


class ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef(
    _ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef
):
    pass


_ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef = TypedDict(
    "_ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)


class ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef(
    _ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef
):
    pass


_ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef = TypedDict(
    "_ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)


class ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef(
    _ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef
):
    pass


_ClientGetPlaybackConfigurationResponseTypeDef = TypedDict(
    "_ClientGetPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "CdnConfiguration": ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef,
        "DashConfiguration": ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef,
        "HlsConfiguration": ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef,
        "LivePreRollConfiguration": ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef,
        "Name": str,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)


class ClientGetPlaybackConfigurationResponseTypeDef(_ClientGetPlaybackConfigurationResponseTypeDef):
    """
    - *(dict) --*

      Success.
      - **AdDecisionServerUrl** *(string) --*

        The URL for the ad decision server (ADS). This includes the specification of static
        parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes
        player-specific and session-specific parameters as needed when calling the ADS. Alternately,
        for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
    """


_ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef = TypedDict(
    "_ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)


class ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef(
    _ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef
):
    pass


_ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef = TypedDict(
    "_ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)


class ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef(
    _ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef
):
    pass


_ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef = TypedDict(
    "_ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)


class ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef(
    _ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef
):
    pass


_ClientListPlaybackConfigurationsResponseItemsTypeDef = TypedDict(
    "_ClientListPlaybackConfigurationsResponseItemsTypeDef",
    {
        "AdDecisionServerUrl": str,
        "CdnConfiguration": ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef,
        "DashConfiguration": ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef,
        "HlsConfiguration": ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef,
        "Name": str,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)


class ClientListPlaybackConfigurationsResponseItemsTypeDef(
    _ClientListPlaybackConfigurationsResponseItemsTypeDef
):
    """
    - *(dict) --*

      The AWSMediaTailor configuration.
      - **AdDecisionServerUrl** *(string) --*

        The URL for the ad decision server (ADS). This includes the specification of static
        parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes
        player-specific and session-specific parameters as needed when calling the ADS. Alternately,
        for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
    """


_ClientListPlaybackConfigurationsResponseTypeDef = TypedDict(
    "_ClientListPlaybackConfigurationsResponseTypeDef",
    {"Items": List[ClientListPlaybackConfigurationsResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientListPlaybackConfigurationsResponseTypeDef(
    _ClientListPlaybackConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      Success.
      - **Items** *(list) --*

        Array of playback configurations. This might be all the available configurations or a
        subset, depending on the settings that you provide and the total number of configurations
        stored.
        - *(dict) --*

          The AWSMediaTailor configuration.
          - **AdDecisionServerUrl** *(string) --*

            The URL for the ad decision server (ADS). This includes the specification of static
            parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor
            substitutes player-specific and session-specific parameters as needed when calling the
            ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is
            25,000 characters.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      Success.
      - **Tags** *(dict) --*

        A comma-separated list of tag key:value pairs. For example: { "Key1": "Value1", "Key2":
        "Value2" }
        - *(string) --*

          - *(string) --*
    """


_ClientPutPlaybackConfigurationCdnConfigurationTypeDef = TypedDict(
    "_ClientPutPlaybackConfigurationCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)


class ClientPutPlaybackConfigurationCdnConfigurationTypeDef(
    _ClientPutPlaybackConfigurationCdnConfigurationTypeDef
):
    """
    The configuration for using a content delivery network (CDN), like Amazon CloudFront, for
    content and ad segment management.
    - **AdSegmentUrlPrefix** *(string) --*

      A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental
      MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To
      set up an alternate CDN, create a rule in your CDN for the following origin:
      ads.mediatailor.<region>.amazonaws.com. Then specify the rule's name in this
      AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as
      the source for ad segments.
    """


_ClientPutPlaybackConfigurationDashConfigurationTypeDef = TypedDict(
    "_ClientPutPlaybackConfigurationDashConfigurationTypeDef",
    {"MpdLocation": str, "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"]},
    total=False,
)


class ClientPutPlaybackConfigurationDashConfigurationTypeDef(
    _ClientPutPlaybackConfigurationDashConfigurationTypeDef
):
    """
    The configuration for DASH content.
    - **MpdLocation** *(string) --*

      The setting that controls whether MediaTailor includes the Location tag in DASH manifests.
      MediaTailor populates the Location tag with the URL for manifest update requests, to be used
      by players that don't support sticky redirects. Disable this if you have CDN routing rules set
      up for accessing MediaTailor manifests, and you are either using client-side reporting or your
      players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The
      EMT_DEFAULT setting enables the inclusion of the tag and is the default value.
    """


_ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef = TypedDict(
    "_ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)


class ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef(
    _ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef
):
    """
    The configuration for pre-roll ad insertion.
    - **AdDecisionServerUrl** *(string) --*

      The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of
      static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor
      substitutes player-specific and session-specific parameters as needed when calling the ADS.
      Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000
      characters.
    """


_ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef = TypedDict(
    "_ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)


class ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef(
    _ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef
):
    pass


_ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef = TypedDict(
    "_ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)


class ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef(
    _ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef
):
    pass


_ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef = TypedDict(
    "_ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)


class ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef(
    _ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef
):
    pass


_ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef = TypedDict(
    "_ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)


class ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef(
    _ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef
):
    pass


_ClientPutPlaybackConfigurationResponseTypeDef = TypedDict(
    "_ClientPutPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "CdnConfiguration": ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef,
        "DashConfiguration": ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef,
        "HlsConfiguration": ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef,
        "LivePreRollConfiguration": ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef,
        "Name": str,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)


class ClientPutPlaybackConfigurationResponseTypeDef(_ClientPutPlaybackConfigurationResponseTypeDef):
    """
    - *(dict) --*

      Success.
      - **AdDecisionServerUrl** *(string) --*

        The URL for the ad decision server (ADS). This includes the specification of static
        parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes
        player-specific and session-specific parameters as needed when calling the ADS. Alternately,
        for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
    """


_ListPlaybackConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPlaybackConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPlaybackConfigurationsPaginatePaginationConfigTypeDef(
    _ListPlaybackConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPlaybackConfigurationsPaginateResponseItemsCdnConfigurationTypeDef = TypedDict(
    "_ListPlaybackConfigurationsPaginateResponseItemsCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)


class ListPlaybackConfigurationsPaginateResponseItemsCdnConfigurationTypeDef(
    _ListPlaybackConfigurationsPaginateResponseItemsCdnConfigurationTypeDef
):
    pass


_ListPlaybackConfigurationsPaginateResponseItemsDashConfigurationTypeDef = TypedDict(
    "_ListPlaybackConfigurationsPaginateResponseItemsDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)


class ListPlaybackConfigurationsPaginateResponseItemsDashConfigurationTypeDef(
    _ListPlaybackConfigurationsPaginateResponseItemsDashConfigurationTypeDef
):
    pass


_ListPlaybackConfigurationsPaginateResponseItemsHlsConfigurationTypeDef = TypedDict(
    "_ListPlaybackConfigurationsPaginateResponseItemsHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)


class ListPlaybackConfigurationsPaginateResponseItemsHlsConfigurationTypeDef(
    _ListPlaybackConfigurationsPaginateResponseItemsHlsConfigurationTypeDef
):
    pass


_ListPlaybackConfigurationsPaginateResponseItemsTypeDef = TypedDict(
    "_ListPlaybackConfigurationsPaginateResponseItemsTypeDef",
    {
        "AdDecisionServerUrl": str,
        "CdnConfiguration": ListPlaybackConfigurationsPaginateResponseItemsCdnConfigurationTypeDef,
        "DashConfiguration": ListPlaybackConfigurationsPaginateResponseItemsDashConfigurationTypeDef,
        "HlsConfiguration": ListPlaybackConfigurationsPaginateResponseItemsHlsConfigurationTypeDef,
        "Name": str,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)


class ListPlaybackConfigurationsPaginateResponseItemsTypeDef(
    _ListPlaybackConfigurationsPaginateResponseItemsTypeDef
):
    """
    - *(dict) --*

      The AWSMediaTailor configuration.
      - **AdDecisionServerUrl** *(string) --*

        The URL for the ad decision server (ADS). This includes the specification of static
        parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes
        player-specific and session-specific parameters as needed when calling the ADS. Alternately,
        for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
    """


_ListPlaybackConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListPlaybackConfigurationsPaginateResponseTypeDef",
    {"Items": List[ListPlaybackConfigurationsPaginateResponseItemsTypeDef]},
    total=False,
)


class ListPlaybackConfigurationsPaginateResponseTypeDef(
    _ListPlaybackConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Success.
      - **Items** *(list) --*

        Array of playback configurations. This might be all the available configurations or a
        subset, depending on the settings that you provide and the total number of configurations
        stored.
        - *(dict) --*

          The AWSMediaTailor configuration.
          - **AdDecisionServerUrl** *(string) --*

            The URL for the ad decision server (ADS). This includes the specification of static
            parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor
            substitutes player-specific and session-specific parameters as needed when calling the
            ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is
            25,000 characters.
    """
