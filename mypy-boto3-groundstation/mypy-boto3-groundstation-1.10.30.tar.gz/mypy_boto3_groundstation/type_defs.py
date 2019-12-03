"Main interface for groundstation service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCancelContactResponseTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    "ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    "ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef",
    "ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef",
    "ClientCreateConfigConfigDataantennaUplinkConfigTypeDef",
    "ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef",
    "ClientCreateConfigConfigDatatrackingConfigTypeDef",
    "ClientCreateConfigConfigDatauplinkEchoConfigTypeDef",
    "ClientCreateConfigConfigDataTypeDef",
    "ClientCreateConfigResponseTypeDef",
    "ClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef",
    "ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef",
    "ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef",
    "ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef",
    "ClientCreateDataflowEndpointGroupResponseTypeDef",
    "ClientCreateMissionProfileResponseTypeDef",
    "ClientDeleteConfigResponseTypeDef",
    "ClientDeleteDataflowEndpointGroupResponseTypeDef",
    "ClientDeleteMissionProfileResponseTypeDef",
    "ClientDescribeContactResponsemaximumElevationTypeDef",
    "ClientDescribeContactResponseTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef",
    "ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef",
    "ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef",
    "ClientGetConfigResponseconfigDatatrackingConfigTypeDef",
    "ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef",
    "ClientGetConfigResponseconfigDataTypeDef",
    "ClientGetConfigResponseTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef",
    "ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef",
    "ClientGetDataflowEndpointGroupResponseTypeDef",
    "ClientGetMinuteUsageResponseTypeDef",
    "ClientGetMissionProfileResponseTypeDef",
    "ClientGetSatelliteResponseTypeDef",
    "ClientListConfigsResponseconfigListTypeDef",
    "ClientListConfigsResponseTypeDef",
    "ClientListContactsResponsecontactListmaximumElevationTypeDef",
    "ClientListContactsResponsecontactListTypeDef",
    "ClientListContactsResponseTypeDef",
    "ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef",
    "ClientListDataflowEndpointGroupsResponseTypeDef",
    "ClientListGroundStationsResponsegroundStationListTypeDef",
    "ClientListGroundStationsResponseTypeDef",
    "ClientListMissionProfilesResponsemissionProfileListTypeDef",
    "ClientListMissionProfilesResponseTypeDef",
    "ClientListSatellitesResponsesatellitesTypeDef",
    "ClientListSatellitesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientReserveContactResponseTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    "ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef",
    "ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef",
    "ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef",
    "ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef",
    "ClientUpdateConfigConfigDatatrackingConfigTypeDef",
    "ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef",
    "ClientUpdateConfigConfigDataTypeDef",
    "ClientUpdateConfigResponseTypeDef",
    "ClientUpdateMissionProfileResponseTypeDef",
    "ListConfigsPaginatePaginationConfigTypeDef",
    "ListConfigsPaginateResponseconfigListTypeDef",
    "ListConfigsPaginateResponseTypeDef",
    "ListContactsPaginatePaginationConfigTypeDef",
    "ListContactsPaginateResponsecontactListmaximumElevationTypeDef",
    "ListContactsPaginateResponsecontactListTypeDef",
    "ListContactsPaginateResponseTypeDef",
    "ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef",
    "ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef",
    "ListDataflowEndpointGroupsPaginateResponseTypeDef",
    "ListGroundStationsPaginatePaginationConfigTypeDef",
    "ListGroundStationsPaginateResponsegroundStationListTypeDef",
    "ListGroundStationsPaginateResponseTypeDef",
    "ListMissionProfilesPaginatePaginationConfigTypeDef",
    "ListMissionProfilesPaginateResponsemissionProfileListTypeDef",
    "ListMissionProfilesPaginateResponseTypeDef",
    "ListSatellitesPaginatePaginationConfigTypeDef",
    "ListSatellitesPaginateResponsesatellitesTypeDef",
    "ListSatellitesPaginateResponseTypeDef",
)


_ClientCancelContactResponseTypeDef = TypedDict(
    "_ClientCancelContactResponseTypeDef", {"contactId": str}, total=False
)


class ClientCancelContactResponseTypeDef(_ClientCancelContactResponseTypeDef):
    """
    - *(dict) --*

      - **contactId** *(string) --*

        UUID of a contact.
    """


_RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"]},
)
_OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"value": float},
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef(
    _RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
    _OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
):
    """
    - **bandwidth** *(dict) --***[REQUIRED]**

      Bandwidth of a spectral ``Config`` .
      - **units** *(string) --***[REQUIRED]**

        Frequency bandwidth units.
    """


_ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef
):
    pass


_RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {"bandwidth": ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef},
)
_OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef(
    _RequiredClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef,
    _OptionalClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef,
):
    """
    - **spectrumConfig** *(dict) --***[REQUIRED]**

      Object that describes a spectral ``Config`` .
      - **bandwidth** *(dict) --***[REQUIRED]**

        Bandwidth of a spectral ``Config`` .
        - **units** *(string) --***[REQUIRED]**

          Frequency bandwidth units.
    """


_ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef",
    {"spectrumConfig": ClientCreateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef},
)


class ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef(
    _ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef
):
    """
    - **antennaDownlinkConfig** *(dict) --*

      Information about how AWS Ground Station should configure an antenna for downlink during a
      contact.
      - **spectrumConfig** *(dict) --***[REQUIRED]**

        Object that describes a spectral ``Config`` .
        - **bandwidth** *(dict) --***[REQUIRED]**

          Bandwidth of a spectral ``Config`` .
          - **units** *(string) --***[REQUIRED]**

            Frequency bandwidth units.
    """


_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef(
    _ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef
):
    pass


_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef(
    _ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef
):
    pass


_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef(
    _ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef
):
    pass


_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef
):
    pass


_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef(
    _ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef
):
    pass


_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef,
        "demodulationConfig": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef,
        "spectrumConfig": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    },
    total=False,
)


class ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef(
    _ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef
):
    pass


_ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef
):
    pass


_ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef(
    _ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef
):
    pass


_ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef",
    {"units": str, "value": float},
    total=False,
)


class ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef(
    _ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef
):
    pass


_ClientCreateConfigConfigDataantennaUplinkConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataantennaUplinkConfigTypeDef",
    {
        "spectrumConfig": ClientCreateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef,
        "targetEirp": ClientCreateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef,
    },
    total=False,
)


class ClientCreateConfigConfigDataantennaUplinkConfigTypeDef(
    _ClientCreateConfigConfigDataantennaUplinkConfigTypeDef
):
    pass


_ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef",
    {"dataflowEndpointName": str},
    total=False,
)


class ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef(
    _ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef
):
    pass


_ClientCreateConfigConfigDatatrackingConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDatatrackingConfigTypeDef",
    {"autotrack": Literal["PREFERRED", "REMOVED", "REQUIRED"]},
    total=False,
)


class ClientCreateConfigConfigDatatrackingConfigTypeDef(
    _ClientCreateConfigConfigDatatrackingConfigTypeDef
):
    pass


_ClientCreateConfigConfigDatauplinkEchoConfigTypeDef = TypedDict(
    "_ClientCreateConfigConfigDatauplinkEchoConfigTypeDef",
    {"antennaUplinkConfigArn": str, "enabled": bool},
    total=False,
)


class ClientCreateConfigConfigDatauplinkEchoConfigTypeDef(
    _ClientCreateConfigConfigDatauplinkEchoConfigTypeDef
):
    pass


_ClientCreateConfigConfigDataTypeDef = TypedDict(
    "_ClientCreateConfigConfigDataTypeDef",
    {
        "antennaDownlinkConfig": ClientCreateConfigConfigDataantennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": ClientCreateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": ClientCreateConfigConfigDataantennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": ClientCreateConfigConfigDatadataflowEndpointConfigTypeDef,
        "trackingConfig": ClientCreateConfigConfigDatatrackingConfigTypeDef,
        "uplinkEchoConfig": ClientCreateConfigConfigDatauplinkEchoConfigTypeDef,
    },
    total=False,
)


class ClientCreateConfigConfigDataTypeDef(_ClientCreateConfigConfigDataTypeDef):
    """
    Parameters of a ``Config`` .
    - **antennaDownlinkConfig** *(dict) --*

      Information about how AWS Ground Station should configure an antenna for downlink during a
      contact.
      - **spectrumConfig** *(dict) --***[REQUIRED]**

        Object that describes a spectral ``Config`` .
        - **bandwidth** *(dict) --***[REQUIRED]**

          Bandwidth of a spectral ``Config`` .
          - **units** *(string) --***[REQUIRED]**

            Frequency bandwidth units.
    """


_ClientCreateConfigResponseTypeDef = TypedDict(
    "_ClientCreateConfigResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    },
    total=False,
)


class ClientCreateConfigResponseTypeDef(_ClientCreateConfigResponseTypeDef):
    """
    - *(dict) --*

      - **configArn** *(string) --*

        ARN of a ``Config`` .
    """


_RequiredClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef = TypedDict(
    "_RequiredClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef", {"name": str}
)
_OptionalClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef = TypedDict(
    "_OptionalClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef",
    {"port": int},
    total=False,
)


class ClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef(
    _RequiredClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef,
    _OptionalClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef,
):
    """
    - **address** *(dict) --*

      Socket address of a dataflow endpoint.
      - **name** *(string) --***[REQUIRED]**

        Name of a socket address.
    """


_ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef = TypedDict(
    "_ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef",
    {
        "address": ClientCreateDataflowEndpointGroupEndpointDetailsendpointaddressTypeDef,
        "name": str,
        "status": Literal["created", "creating", "deleted", "deleting", "failed"],
    },
    total=False,
)


class ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef(
    _ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef
):
    """
    - **endpoint** *(dict) --*

      A dataflow endpoint.
      - **address** *(dict) --*

        Socket address of a dataflow endpoint.
        - **name** *(string) --***[REQUIRED]**

          Name of a socket address.
    """


_ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef = TypedDict(
    "_ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef",
    {"roleArn": str, "securityGroupIds": List[str], "subnetIds": List[str]},
    total=False,
)


class ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef(
    _ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef
):
    pass


_ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef = TypedDict(
    "_ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef",
    {
        "endpoint": ClientCreateDataflowEndpointGroupEndpointDetailsendpointTypeDef,
        "securityDetails": ClientCreateDataflowEndpointGroupEndpointDetailssecurityDetailsTypeDef,
    },
    total=False,
)


class ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef(
    _ClientCreateDataflowEndpointGroupEndpointDetailsTypeDef
):
    """
    - *(dict) --*

      Information about the endpoint details.
      - **endpoint** *(dict) --*

        A dataflow endpoint.
        - **address** *(dict) --*

          Socket address of a dataflow endpoint.
          - **name** *(string) --***[REQUIRED]**

            Name of a socket address.
    """


_ClientCreateDataflowEndpointGroupResponseTypeDef = TypedDict(
    "_ClientCreateDataflowEndpointGroupResponseTypeDef",
    {"dataflowEndpointGroupId": str},
    total=False,
)


class ClientCreateDataflowEndpointGroupResponseTypeDef(
    _ClientCreateDataflowEndpointGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **dataflowEndpointGroupId** *(string) --*

        ID of a dataflow endpoint group.
    """


_ClientCreateMissionProfileResponseTypeDef = TypedDict(
    "_ClientCreateMissionProfileResponseTypeDef", {"missionProfileId": str}, total=False
)


class ClientCreateMissionProfileResponseTypeDef(_ClientCreateMissionProfileResponseTypeDef):
    """
    - *(dict) --*

      - **missionProfileId** *(string) --*

        ID of a mission profile.
    """


_ClientDeleteConfigResponseTypeDef = TypedDict(
    "_ClientDeleteConfigResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    },
    total=False,
)


class ClientDeleteConfigResponseTypeDef(_ClientDeleteConfigResponseTypeDef):
    """
    - *(dict) --*

      - **configArn** *(string) --*

        ARN of a ``Config`` .
    """


_ClientDeleteDataflowEndpointGroupResponseTypeDef = TypedDict(
    "_ClientDeleteDataflowEndpointGroupResponseTypeDef",
    {"dataflowEndpointGroupId": str},
    total=False,
)


class ClientDeleteDataflowEndpointGroupResponseTypeDef(
    _ClientDeleteDataflowEndpointGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **dataflowEndpointGroupId** *(string) --*

        ID of a dataflow endpoint group.
    """


_ClientDeleteMissionProfileResponseTypeDef = TypedDict(
    "_ClientDeleteMissionProfileResponseTypeDef", {"missionProfileId": str}, total=False
)


class ClientDeleteMissionProfileResponseTypeDef(_ClientDeleteMissionProfileResponseTypeDef):
    """
    - *(dict) --*

      - **missionProfileId** *(string) --*

        ID of a mission profile.
    """


_ClientDescribeContactResponsemaximumElevationTypeDef = TypedDict(
    "_ClientDescribeContactResponsemaximumElevationTypeDef",
    {"unit": Literal["DEGREE_ANGLE", "RADIAN"], "value": float},
    total=False,
)


class ClientDescribeContactResponsemaximumElevationTypeDef(
    _ClientDescribeContactResponsemaximumElevationTypeDef
):
    pass


_ClientDescribeContactResponseTypeDef = TypedDict(
    "_ClientDescribeContactResponseTypeDef",
    {
        "contactId": str,
        "contactStatus": Literal[
            "AVAILABLE",
            "AWS_CANCELLED",
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "FAILED_TO_SCHEDULE",
            "PASS",
            "POSTPASS",
            "PREPASS",
            "SCHEDULED",
            "SCHEDULING",
        ],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ClientDescribeContactResponsemaximumElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeContactResponseTypeDef(_ClientDescribeContactResponseTypeDef):
    """
    - *(dict) --*

      - **contactId** *(string) --*

        UUID of a contact.
    """


_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef",
    {"spectrumConfig": ClientGetConfigResponseconfigDataantennaDownlinkConfigspectrumConfigTypeDef},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef,
        "demodulationConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef,
        "spectrumConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef",
    {"units": str, "value": float},
    total=False,
)


class ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef(
    _ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef
):
    pass


_ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef",
    {
        "spectrumConfig": ClientGetConfigResponseconfigDataantennaUplinkConfigspectrumConfigTypeDef,
        "targetEirp": ClientGetConfigResponseconfigDataantennaUplinkConfigtargetEirpTypeDef,
    },
    total=False,
)


class ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef(
    _ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef",
    {"dataflowEndpointName": str},
    total=False,
)


class ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef(
    _ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDatatrackingConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDatatrackingConfigTypeDef",
    {"autotrack": Literal["PREFERRED", "REMOVED", "REQUIRED"]},
    total=False,
)


class ClientGetConfigResponseconfigDatatrackingConfigTypeDef(
    _ClientGetConfigResponseconfigDatatrackingConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef",
    {"antennaUplinkConfigArn": str, "enabled": bool},
    total=False,
)


class ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef(
    _ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef
):
    pass


_ClientGetConfigResponseconfigDataTypeDef = TypedDict(
    "_ClientGetConfigResponseconfigDataTypeDef",
    {
        "antennaDownlinkConfig": ClientGetConfigResponseconfigDataantennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": ClientGetConfigResponseconfigDataantennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": ClientGetConfigResponseconfigDataantennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": ClientGetConfigResponseconfigDatadataflowEndpointConfigTypeDef,
        "trackingConfig": ClientGetConfigResponseconfigDatatrackingConfigTypeDef,
        "uplinkEchoConfig": ClientGetConfigResponseconfigDatauplinkEchoConfigTypeDef,
    },
    total=False,
)


class ClientGetConfigResponseconfigDataTypeDef(_ClientGetConfigResponseconfigDataTypeDef):
    pass


_ClientGetConfigResponseTypeDef = TypedDict(
    "_ClientGetConfigResponseTypeDef",
    {
        "configArn": str,
        "configData": ClientGetConfigResponseconfigDataTypeDef,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetConfigResponseTypeDef(_ClientGetConfigResponseTypeDef):
    """
    - *(dict) --*

      - **configArn** *(string) --*

        ARN of a ``Config``
    """


_ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef",
    {"name": str, "port": int},
    total=False,
)


class ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef(
    _ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef
):
    pass


_ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef",
    {
        "address": ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointaddressTypeDef,
        "name": str,
        "status": Literal["created", "creating", "deleted", "deleting", "failed"],
    },
    total=False,
)


class ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef(
    _ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef
):
    pass


_ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef",
    {"roleArn": str, "securityGroupIds": List[str], "subnetIds": List[str]},
    total=False,
)


class ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef(
    _ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef
):
    pass


_ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef",
    {
        "endpoint": ClientGetDataflowEndpointGroupResponseendpointsDetailsendpointTypeDef,
        "securityDetails": ClientGetDataflowEndpointGroupResponseendpointsDetailssecurityDetailsTypeDef,
    },
    total=False,
)


class ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef(
    _ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef
):
    pass


_ClientGetDataflowEndpointGroupResponseTypeDef = TypedDict(
    "_ClientGetDataflowEndpointGroupResponseTypeDef",
    {
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
        "endpointsDetails": List[ClientGetDataflowEndpointGroupResponseendpointsDetailsTypeDef],
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDataflowEndpointGroupResponseTypeDef(_ClientGetDataflowEndpointGroupResponseTypeDef):
    """
    - *(dict) --*

      - **dataflowEndpointGroupArn** *(string) --*

        ARN of a dataflow endpoint group.
    """


_ClientGetMinuteUsageResponseTypeDef = TypedDict(
    "_ClientGetMinuteUsageResponseTypeDef",
    {
        "estimatedMinutesRemaining": int,
        "isReservedMinutesCustomer": bool,
        "totalReservedMinuteAllocation": int,
        "totalScheduledMinutes": int,
        "upcomingMinutesScheduled": int,
    },
    total=False,
)


class ClientGetMinuteUsageResponseTypeDef(_ClientGetMinuteUsageResponseTypeDef):
    """
    - *(dict) --*

      - **estimatedMinutesRemaining** *(integer) --*

        Estimated number of minutes remaining for an account, specific to the month being requested.
    """


_ClientGetMissionProfileResponseTypeDef = TypedDict(
    "_ClientGetMissionProfileResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
        "tags": Dict[str, str],
        "trackingConfigArn": str,
    },
    total=False,
)


class ClientGetMissionProfileResponseTypeDef(_ClientGetMissionProfileResponseTypeDef):
    """
    - *(dict) --*

      - **contactPostPassDurationSeconds** *(integer) --*

        Amount of time after a contact ends that you’d like to receive a CloudWatch event indicating
        the pass has finished.
    """


_ClientGetSatelliteResponseTypeDef = TypedDict(
    "_ClientGetSatelliteResponseTypeDef",
    {
        "dateCreated": datetime,
        "lastUpdated": datetime,
        "noradSatelliteID": int,
        "satelliteArn": str,
        "satelliteId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetSatelliteResponseTypeDef(_ClientGetSatelliteResponseTypeDef):
    """
    - *(dict) --*

      - **dateCreated** *(datetime) --*

        When a satellite was created.
    """


_ClientListConfigsResponseconfigListTypeDef = TypedDict(
    "_ClientListConfigsResponseconfigListTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
        "name": str,
    },
    total=False,
)


class ClientListConfigsResponseconfigListTypeDef(_ClientListConfigsResponseconfigListTypeDef):
    """
    - *(dict) --*

      An item in a list of ``Config`` objects.
      - **configArn** *(string) --*

        ARN of a ``Config`` .
    """


_ClientListConfigsResponseTypeDef = TypedDict(
    "_ClientListConfigsResponseTypeDef",
    {"configList": List[ClientListConfigsResponseconfigListTypeDef], "nextToken": str},
    total=False,
)


class ClientListConfigsResponseTypeDef(_ClientListConfigsResponseTypeDef):
    """
    - *(dict) --*

      - **configList** *(list) --*

        List of ``Config`` items.
        - *(dict) --*

          An item in a list of ``Config`` objects.
          - **configArn** *(string) --*

            ARN of a ``Config`` .
    """


_ClientListContactsResponsecontactListmaximumElevationTypeDef = TypedDict(
    "_ClientListContactsResponsecontactListmaximumElevationTypeDef",
    {"unit": Literal["DEGREE_ANGLE", "RADIAN"], "value": float},
    total=False,
)


class ClientListContactsResponsecontactListmaximumElevationTypeDef(
    _ClientListContactsResponsecontactListmaximumElevationTypeDef
):
    pass


_ClientListContactsResponsecontactListTypeDef = TypedDict(
    "_ClientListContactsResponsecontactListTypeDef",
    {
        "contactId": str,
        "contactStatus": Literal[
            "AVAILABLE",
            "AWS_CANCELLED",
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "FAILED_TO_SCHEDULE",
            "PASS",
            "POSTPASS",
            "PREPASS",
            "SCHEDULED",
            "SCHEDULING",
        ],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ClientListContactsResponsecontactListmaximumElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientListContactsResponsecontactListTypeDef(_ClientListContactsResponsecontactListTypeDef):
    """
    - *(dict) --*

      Data describing a contact.
      - **contactId** *(string) --*

        UUID of a contact.
    """


_ClientListContactsResponseTypeDef = TypedDict(
    "_ClientListContactsResponseTypeDef",
    {"contactList": List[ClientListContactsResponsecontactListTypeDef], "nextToken": str},
    total=False,
)


class ClientListContactsResponseTypeDef(_ClientListContactsResponseTypeDef):
    """
    - *(dict) --*

      - **contactList** *(list) --*

        List of contacts.
        - *(dict) --*

          Data describing a contact.
          - **contactId** *(string) --*

            UUID of a contact.
    """


_ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef = TypedDict(
    "_ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef",
    {"dataflowEndpointGroupArn": str, "dataflowEndpointGroupId": str},
    total=False,
)


class ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef(
    _ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef
):
    """
    - *(dict) --*

      Item in a list of ``DataflowEndpoint`` groups.
      - **dataflowEndpointGroupArn** *(string) --*

        ARN of a dataflow endpoint group.
    """


_ClientListDataflowEndpointGroupsResponseTypeDef = TypedDict(
    "_ClientListDataflowEndpointGroupsResponseTypeDef",
    {
        "dataflowEndpointGroupList": List[
            ClientListDataflowEndpointGroupsResponsedataflowEndpointGroupListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDataflowEndpointGroupsResponseTypeDef(
    _ClientListDataflowEndpointGroupsResponseTypeDef
):
    """
    - *(dict) --*

      - **dataflowEndpointGroupList** *(list) --*

        A list of dataflow endpoint groups.
        - *(dict) --*

          Item in a list of ``DataflowEndpoint`` groups.
          - **dataflowEndpointGroupArn** *(string) --*

            ARN of a dataflow endpoint group.
    """


_ClientListGroundStationsResponsegroundStationListTypeDef = TypedDict(
    "_ClientListGroundStationsResponsegroundStationListTypeDef",
    {"groundStationId": str, "groundStationName": str, "region": str},
    total=False,
)


class ClientListGroundStationsResponsegroundStationListTypeDef(
    _ClientListGroundStationsResponsegroundStationListTypeDef
):
    """
    - *(dict) --*

      Information about the ground station data.
      - **groundStationId** *(string) --*

        ID of a ground station.
    """


_ClientListGroundStationsResponseTypeDef = TypedDict(
    "_ClientListGroundStationsResponseTypeDef",
    {
        "groundStationList": List[ClientListGroundStationsResponsegroundStationListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListGroundStationsResponseTypeDef(_ClientListGroundStationsResponseTypeDef):
    """
    - *(dict) --*

      - **groundStationList** *(list) --*

        List of ground stations.
        - *(dict) --*

          Information about the ground station data.
          - **groundStationId** *(string) --*

            ID of a ground station.
    """


_ClientListMissionProfilesResponsemissionProfileListTypeDef = TypedDict(
    "_ClientListMissionProfilesResponsemissionProfileListTypeDef",
    {"missionProfileArn": str, "missionProfileId": str, "name": str, "region": str},
    total=False,
)


class ClientListMissionProfilesResponsemissionProfileListTypeDef(
    _ClientListMissionProfilesResponsemissionProfileListTypeDef
):
    """
    - *(dict) --*

      Item in a list of mission profiles.
      - **missionProfileArn** *(string) --*

        ARN of a mission profile.
    """


_ClientListMissionProfilesResponseTypeDef = TypedDict(
    "_ClientListMissionProfilesResponseTypeDef",
    {
        "missionProfileList": List[ClientListMissionProfilesResponsemissionProfileListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListMissionProfilesResponseTypeDef(_ClientListMissionProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **missionProfileList** *(list) --*

        List of mission profiles
        - *(dict) --*

          Item in a list of mission profiles.
          - **missionProfileArn** *(string) --*

            ARN of a mission profile.
    """


_ClientListSatellitesResponsesatellitesTypeDef = TypedDict(
    "_ClientListSatellitesResponsesatellitesTypeDef",
    {"noradSatelliteID": int, "satelliteArn": str, "satelliteId": str},
    total=False,
)


class ClientListSatellitesResponsesatellitesTypeDef(_ClientListSatellitesResponsesatellitesTypeDef):
    pass


_ClientListSatellitesResponseTypeDef = TypedDict(
    "_ClientListSatellitesResponseTypeDef",
    {"nextToken": str, "satellites": List[ClientListSatellitesResponsesatellitesTypeDef]},
    total=False,
)


class ClientListSatellitesResponseTypeDef(_ClientListSatellitesResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        Next token that can be supplied in the next call to get the next page of satellites.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        Tags assigned to a resource.
        - *(string) --*

          - *(string) --*
    """


_ClientReserveContactResponseTypeDef = TypedDict(
    "_ClientReserveContactResponseTypeDef", {"contactId": str}, total=False
)


class ClientReserveContactResponseTypeDef(_ClientReserveContactResponseTypeDef):
    """
    - *(dict) --*

      - **contactId** *(string) --*

        UUID of a contact.
    """


_RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"]},
)
_OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef",
    {"value": float},
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef(
    _RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
    _OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef,
):
    """
    - **bandwidth** *(dict) --***[REQUIRED]**

      Bandwidth of a spectral ``Config`` .
      - **units** *(string) --***[REQUIRED]**

        Frequency bandwidth units.
    """


_ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef
):
    pass


_RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {"bandwidth": ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigbandwidthTypeDef},
)
_OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef = TypedDict(
    "_OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef(
    _RequiredClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef,
    _OptionalClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef,
):
    """
    - **spectrumConfig** *(dict) --***[REQUIRED]**

      Object that describes a spectral ``Config`` .
      - **bandwidth** *(dict) --***[REQUIRED]**

        Bandwidth of a spectral ``Config`` .
        - **units** *(string) --***[REQUIRED]**

          Frequency bandwidth units.
    """


_ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef",
    {"spectrumConfig": ClientUpdateConfigConfigDataantennaDownlinkConfigspectrumConfigTypeDef},
)


class ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef(
    _ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef
):
    """
    - **antennaDownlinkConfig** *(dict) --*

      Information about how AWS Ground Station should configure an antenna for downlink during a
      contact.
      - **spectrumConfig** *(dict) --***[REQUIRED]**

        Object that describes a spectral ``Config`` .
        - **bandwidth** *(dict) --***[REQUIRED]**

          Bandwidth of a spectral ``Config`` .
          - **units** *(string) --***[REQUIRED]**

            Frequency bandwidth units.
    """


_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef(
    _ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef
):
    pass


_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef",
    {"unvalidatedJSON": str},
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef(
    _ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef
):
    pass


_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef(
    _ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef
):
    pass


_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef
):
    pass


_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef",
    {
        "bandwidth": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigbandwidthTypeDef,
        "centerFrequency": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef(
    _ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef
):
    pass


_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdecodeConfigTypeDef,
        "demodulationConfig": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigdemodulationConfigTypeDef,
        "spectrumConfig": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigspectrumConfigTypeDef,
    },
    total=False,
)


class ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef(
    _ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef
):
    pass


_ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef",
    {"units": Literal["GHz", "MHz", "kHz"], "value": float},
    total=False,
)


class ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef(
    _ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef
):
    pass


_ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef",
    {
        "centerFrequency": ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigcenterFrequencyTypeDef,
        "polarization": Literal["LEFT_HAND", "NONE", "RIGHT_HAND"],
    },
    total=False,
)


class ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef(
    _ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef
):
    pass


_ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef",
    {"units": str, "value": float},
    total=False,
)


class ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef(
    _ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef
):
    pass


_ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef",
    {
        "spectrumConfig": ClientUpdateConfigConfigDataantennaUplinkConfigspectrumConfigTypeDef,
        "targetEirp": ClientUpdateConfigConfigDataantennaUplinkConfigtargetEirpTypeDef,
    },
    total=False,
)


class ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef(
    _ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef
):
    pass


_ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef",
    {"dataflowEndpointName": str},
    total=False,
)


class ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef(
    _ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef
):
    pass


_ClientUpdateConfigConfigDatatrackingConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDatatrackingConfigTypeDef",
    {"autotrack": Literal["PREFERRED", "REMOVED", "REQUIRED"]},
    total=False,
)


class ClientUpdateConfigConfigDatatrackingConfigTypeDef(
    _ClientUpdateConfigConfigDatatrackingConfigTypeDef
):
    pass


_ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef",
    {"antennaUplinkConfigArn": str, "enabled": bool},
    total=False,
)


class ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef(
    _ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef
):
    pass


_ClientUpdateConfigConfigDataTypeDef = TypedDict(
    "_ClientUpdateConfigConfigDataTypeDef",
    {
        "antennaDownlinkConfig": ClientUpdateConfigConfigDataantennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": ClientUpdateConfigConfigDataantennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": ClientUpdateConfigConfigDataantennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": ClientUpdateConfigConfigDatadataflowEndpointConfigTypeDef,
        "trackingConfig": ClientUpdateConfigConfigDatatrackingConfigTypeDef,
        "uplinkEchoConfig": ClientUpdateConfigConfigDatauplinkEchoConfigTypeDef,
    },
    total=False,
)


class ClientUpdateConfigConfigDataTypeDef(_ClientUpdateConfigConfigDataTypeDef):
    """
    Parameters for a ``Config`` .
    - **antennaDownlinkConfig** *(dict) --*

      Information about how AWS Ground Station should configure an antenna for downlink during a
      contact.
      - **spectrumConfig** *(dict) --***[REQUIRED]**

        Object that describes a spectral ``Config`` .
        - **bandwidth** *(dict) --***[REQUIRED]**

          Bandwidth of a spectral ``Config`` .
          - **units** *(string) --***[REQUIRED]**

            Frequency bandwidth units.
    """


_ClientUpdateConfigResponseTypeDef = TypedDict(
    "_ClientUpdateConfigResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    },
    total=False,
)


class ClientUpdateConfigResponseTypeDef(_ClientUpdateConfigResponseTypeDef):
    """
    - *(dict) --*

      - **configArn** *(string) --*

        ARN of a ``Config`` .
    """


_ClientUpdateMissionProfileResponseTypeDef = TypedDict(
    "_ClientUpdateMissionProfileResponseTypeDef", {"missionProfileId": str}, total=False
)


class ClientUpdateMissionProfileResponseTypeDef(_ClientUpdateMissionProfileResponseTypeDef):
    """
    - *(dict) --*

      - **missionProfileId** *(string) --*

        ID of a mission profile.
    """


_ListConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigsPaginatePaginationConfigTypeDef(_ListConfigsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListConfigsPaginateResponseconfigListTypeDef = TypedDict(
    "_ListConfigsPaginateResponseconfigListTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
        "name": str,
    },
    total=False,
)


class ListConfigsPaginateResponseconfigListTypeDef(_ListConfigsPaginateResponseconfigListTypeDef):
    """
    - *(dict) --*

      An item in a list of ``Config`` objects.
      - **configArn** *(string) --*

        ARN of a ``Config`` .
    """


_ListConfigsPaginateResponseTypeDef = TypedDict(
    "_ListConfigsPaginateResponseTypeDef",
    {"configList": List[ListConfigsPaginateResponseconfigListTypeDef], "NextToken": str},
    total=False,
)


class ListConfigsPaginateResponseTypeDef(_ListConfigsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **configList** *(list) --*

        List of ``Config`` items.
        - *(dict) --*

          An item in a list of ``Config`` objects.
          - **configArn** *(string) --*

            ARN of a ``Config`` .
    """


_ListContactsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListContactsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListContactsPaginatePaginationConfigTypeDef(_ListContactsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListContactsPaginateResponsecontactListmaximumElevationTypeDef = TypedDict(
    "_ListContactsPaginateResponsecontactListmaximumElevationTypeDef",
    {"unit": Literal["DEGREE_ANGLE", "RADIAN"], "value": float},
    total=False,
)


class ListContactsPaginateResponsecontactListmaximumElevationTypeDef(
    _ListContactsPaginateResponsecontactListmaximumElevationTypeDef
):
    pass


_ListContactsPaginateResponsecontactListTypeDef = TypedDict(
    "_ListContactsPaginateResponsecontactListTypeDef",
    {
        "contactId": str,
        "contactStatus": Literal[
            "AVAILABLE",
            "AWS_CANCELLED",
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "FAILED_TO_SCHEDULE",
            "PASS",
            "POSTPASS",
            "PREPASS",
            "SCHEDULED",
            "SCHEDULING",
        ],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ListContactsPaginateResponsecontactListmaximumElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ListContactsPaginateResponsecontactListTypeDef(
    _ListContactsPaginateResponsecontactListTypeDef
):
    """
    - *(dict) --*

      Data describing a contact.
      - **contactId** *(string) --*

        UUID of a contact.
    """


_ListContactsPaginateResponseTypeDef = TypedDict(
    "_ListContactsPaginateResponseTypeDef",
    {"contactList": List[ListContactsPaginateResponsecontactListTypeDef], "NextToken": str},
    total=False,
)


class ListContactsPaginateResponseTypeDef(_ListContactsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **contactList** *(list) --*

        List of contacts.
        - *(dict) --*

          Data describing a contact.
          - **contactId** *(string) --*

            UUID of a contact.
    """


_ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef(
    _ListDataflowEndpointGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef = TypedDict(
    "_ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef",
    {"dataflowEndpointGroupArn": str, "dataflowEndpointGroupId": str},
    total=False,
)


class ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef(
    _ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef
):
    """
    - *(dict) --*

      Item in a list of ``DataflowEndpoint`` groups.
      - **dataflowEndpointGroupArn** *(string) --*

        ARN of a dataflow endpoint group.
    """


_ListDataflowEndpointGroupsPaginateResponseTypeDef = TypedDict(
    "_ListDataflowEndpointGroupsPaginateResponseTypeDef",
    {
        "dataflowEndpointGroupList": List[
            ListDataflowEndpointGroupsPaginateResponsedataflowEndpointGroupListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListDataflowEndpointGroupsPaginateResponseTypeDef(
    _ListDataflowEndpointGroupsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **dataflowEndpointGroupList** *(list) --*

        A list of dataflow endpoint groups.
        - *(dict) --*

          Item in a list of ``DataflowEndpoint`` groups.
          - **dataflowEndpointGroupArn** *(string) --*

            ARN of a dataflow endpoint group.
    """


_ListGroundStationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroundStationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroundStationsPaginatePaginationConfigTypeDef(
    _ListGroundStationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroundStationsPaginateResponsegroundStationListTypeDef = TypedDict(
    "_ListGroundStationsPaginateResponsegroundStationListTypeDef",
    {"groundStationId": str, "groundStationName": str, "region": str},
    total=False,
)


class ListGroundStationsPaginateResponsegroundStationListTypeDef(
    _ListGroundStationsPaginateResponsegroundStationListTypeDef
):
    """
    - *(dict) --*

      Information about the ground station data.
      - **groundStationId** *(string) --*

        ID of a ground station.
    """


_ListGroundStationsPaginateResponseTypeDef = TypedDict(
    "_ListGroundStationsPaginateResponseTypeDef",
    {
        "groundStationList": List[ListGroundStationsPaginateResponsegroundStationListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListGroundStationsPaginateResponseTypeDef(_ListGroundStationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **groundStationList** *(list) --*

        List of ground stations.
        - *(dict) --*

          Information about the ground station data.
          - **groundStationId** *(string) --*

            ID of a ground station.
    """


_ListMissionProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMissionProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMissionProfilesPaginatePaginationConfigTypeDef(
    _ListMissionProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMissionProfilesPaginateResponsemissionProfileListTypeDef = TypedDict(
    "_ListMissionProfilesPaginateResponsemissionProfileListTypeDef",
    {"missionProfileArn": str, "missionProfileId": str, "name": str, "region": str},
    total=False,
)


class ListMissionProfilesPaginateResponsemissionProfileListTypeDef(
    _ListMissionProfilesPaginateResponsemissionProfileListTypeDef
):
    """
    - *(dict) --*

      Item in a list of mission profiles.
      - **missionProfileArn** *(string) --*

        ARN of a mission profile.
    """


_ListMissionProfilesPaginateResponseTypeDef = TypedDict(
    "_ListMissionProfilesPaginateResponseTypeDef",
    {
        "missionProfileList": List[ListMissionProfilesPaginateResponsemissionProfileListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListMissionProfilesPaginateResponseTypeDef(_ListMissionProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **missionProfileList** *(list) --*

        List of mission profiles
        - *(dict) --*

          Item in a list of mission profiles.
          - **missionProfileArn** *(string) --*

            ARN of a mission profile.
    """


_ListSatellitesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSatellitesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSatellitesPaginatePaginationConfigTypeDef(_ListSatellitesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSatellitesPaginateResponsesatellitesTypeDef = TypedDict(
    "_ListSatellitesPaginateResponsesatellitesTypeDef",
    {"noradSatelliteID": int, "satelliteArn": str, "satelliteId": str},
    total=False,
)


class ListSatellitesPaginateResponsesatellitesTypeDef(
    _ListSatellitesPaginateResponsesatellitesTypeDef
):
    """
    - *(dict) --*

      Item in a list of satellites.
      - **noradSatelliteID** *(integer) --*

        NORAD satellite ID number.
    """


_ListSatellitesPaginateResponseTypeDef = TypedDict(
    "_ListSatellitesPaginateResponseTypeDef",
    {"satellites": List[ListSatellitesPaginateResponsesatellitesTypeDef], "NextToken": str},
    total=False,
)


class ListSatellitesPaginateResponseTypeDef(_ListSatellitesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **satellites** *(list) --*

        List of satellites.
        - *(dict) --*

          Item in a list of satellites.
          - **noradSatelliteID** *(integer) --*

            NORAD satellite ID number.
    """
