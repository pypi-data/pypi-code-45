"Main interface for mediatailor service type defs"
from __future__ import annotations

import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)

ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)

ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)

ClientGetPlaybackConfigurationResponseTypeDef = TypedDict(
    "ClientGetPlaybackConfigurationResponseTypeDef",
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

ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseItemsCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseItemsDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)

ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseItemsHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)

ClientListPlaybackConfigurationsResponseItemsTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseItemsTypeDef",
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

ClientListPlaybackConfigurationsResponseTypeDef = TypedDict(
    "ClientListPlaybackConfigurationsResponseTypeDef",
    {"Items": List[ClientListPlaybackConfigurationsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientPutPlaybackConfigurationCdnConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

ClientPutPlaybackConfigurationDashConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationDashConfigurationTypeDef",
    {"MpdLocation": str, "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"]},
    total=False,
)

ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)

ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)

ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)

ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseLivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)

ClientPutPlaybackConfigurationResponseTypeDef = TypedDict(
    "ClientPutPlaybackConfigurationResponseTypeDef",
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

ListPlaybackConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPlaybackConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPlaybackConfigurationsPaginateResponseItemsCdnConfigurationTypeDef = TypedDict(
    "ListPlaybackConfigurationsPaginateResponseItemsCdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

ListPlaybackConfigurationsPaginateResponseItemsDashConfigurationTypeDef = TypedDict(
    "ListPlaybackConfigurationsPaginateResponseItemsDashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)

ListPlaybackConfigurationsPaginateResponseItemsHlsConfigurationTypeDef = TypedDict(
    "ListPlaybackConfigurationsPaginateResponseItemsHlsConfigurationTypeDef",
    {"ManifestEndpointPrefix": str},
    total=False,
)

ListPlaybackConfigurationsPaginateResponseItemsTypeDef = TypedDict(
    "ListPlaybackConfigurationsPaginateResponseItemsTypeDef",
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

ListPlaybackConfigurationsPaginateResponseTypeDef = TypedDict(
    "ListPlaybackConfigurationsPaginateResponseTypeDef",
    {"Items": List[ListPlaybackConfigurationsPaginateResponseItemsTypeDef]},
    total=False,
)
