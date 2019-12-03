"Main interface for pi service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientDescribeDimensionKeysGroupByTypeDef",
    "ClientDescribeDimensionKeysPartitionByTypeDef",
    "ClientDescribeDimensionKeysResponseKeysTypeDef",
    "ClientDescribeDimensionKeysResponsePartitionKeysTypeDef",
    "ClientDescribeDimensionKeysResponseTypeDef",
    "ClientGetResourceMetricsMetricQueriesGroupByTypeDef",
    "ClientGetResourceMetricsMetricQueriesTypeDef",
    "ClientGetResourceMetricsResponseMetricListDataPointsTypeDef",
    "ClientGetResourceMetricsResponseMetricListKeyTypeDef",
    "ClientGetResourceMetricsResponseMetricListTypeDef",
    "ClientGetResourceMetricsResponseTypeDef",
)


_RequiredClientDescribeDimensionKeysGroupByTypeDef = TypedDict(
    "_RequiredClientDescribeDimensionKeysGroupByTypeDef", {"Group": str}
)
_OptionalClientDescribeDimensionKeysGroupByTypeDef = TypedDict(
    "_OptionalClientDescribeDimensionKeysGroupByTypeDef",
    {"Dimensions": List[str], "Limit": int},
    total=False,
)


class ClientDescribeDimensionKeysGroupByTypeDef(
    _RequiredClientDescribeDimensionKeysGroupByTypeDef,
    _OptionalClientDescribeDimensionKeysGroupByTypeDef,
):
    """
    A specification for how to aggregate the data points from a query result. You must specify a
    valid dimension group. Performance Insights will return all of the dimensions within that group,
    unless you provide the names of specific dimensions within that group. You can also request that
    Performance Insights return a limited number of values for a dimension.
    - **Group** *(string) --***[REQUIRED]**

      The name of the dimension group. Valid values are:
      * ``db.user``
      * ``db.host``
      * ``db.sql``
      * ``db.sql_tokenized``
      * ``db.wait_event``
      * ``db.wait_event_type``
    """


_RequiredClientDescribeDimensionKeysPartitionByTypeDef = TypedDict(
    "_RequiredClientDescribeDimensionKeysPartitionByTypeDef", {"Group": str}
)
_OptionalClientDescribeDimensionKeysPartitionByTypeDef = TypedDict(
    "_OptionalClientDescribeDimensionKeysPartitionByTypeDef",
    {"Dimensions": List[str], "Limit": int},
    total=False,
)


class ClientDescribeDimensionKeysPartitionByTypeDef(
    _RequiredClientDescribeDimensionKeysPartitionByTypeDef,
    _OptionalClientDescribeDimensionKeysPartitionByTypeDef,
):
    """
    For each dimension specified in ``GroupBy`` , specify a secondary dimension to further subdivide
    the partition keys in the response.
    - **Group** *(string) --***[REQUIRED]**

      The name of the dimension group. Valid values are:
      * ``db.user``
      * ``db.host``
      * ``db.sql``
      * ``db.sql_tokenized``
      * ``db.wait_event``
      * ``db.wait_event_type``
    """


_ClientDescribeDimensionKeysResponseKeysTypeDef = TypedDict(
    "_ClientDescribeDimensionKeysResponseKeysTypeDef",
    {"Dimensions": Dict[str, str], "Total": float, "Partitions": List[float]},
    total=False,
)


class ClientDescribeDimensionKeysResponseKeysTypeDef(
    _ClientDescribeDimensionKeysResponseKeysTypeDef
):
    pass


_ClientDescribeDimensionKeysResponsePartitionKeysTypeDef = TypedDict(
    "_ClientDescribeDimensionKeysResponsePartitionKeysTypeDef",
    {"Dimensions": Dict[str, str]},
    total=False,
)


class ClientDescribeDimensionKeysResponsePartitionKeysTypeDef(
    _ClientDescribeDimensionKeysResponsePartitionKeysTypeDef
):
    pass


_ClientDescribeDimensionKeysResponseTypeDef = TypedDict(
    "_ClientDescribeDimensionKeysResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "PartitionKeys": List[ClientDescribeDimensionKeysResponsePartitionKeysTypeDef],
        "Keys": List[ClientDescribeDimensionKeysResponseKeysTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeDimensionKeysResponseTypeDef(_ClientDescribeDimensionKeysResponseTypeDef):
    """
    - *(dict) --*

      - **AlignedStartTime** *(datetime) --*

        The start time for the returned dimension keys, after alignment to a granular boundary (as
        specified by ``PeriodInSeconds`` ). ``AlignedStartTime`` will be less than or equal to the
        value of the user-specified ``StartTime`` .
    """


_ClientGetResourceMetricsMetricQueriesGroupByTypeDef = TypedDict(
    "_ClientGetResourceMetricsMetricQueriesGroupByTypeDef",
    {"Group": str, "Dimensions": List[str], "Limit": int},
    total=False,
)


class ClientGetResourceMetricsMetricQueriesGroupByTypeDef(
    _ClientGetResourceMetricsMetricQueriesGroupByTypeDef
):
    pass


_RequiredClientGetResourceMetricsMetricQueriesTypeDef = TypedDict(
    "_RequiredClientGetResourceMetricsMetricQueriesTypeDef", {"Metric": str}
)
_OptionalClientGetResourceMetricsMetricQueriesTypeDef = TypedDict(
    "_OptionalClientGetResourceMetricsMetricQueriesTypeDef",
    {"GroupBy": ClientGetResourceMetricsMetricQueriesGroupByTypeDef, "Filter": Dict[str, str]},
    total=False,
)


class ClientGetResourceMetricsMetricQueriesTypeDef(
    _RequiredClientGetResourceMetricsMetricQueriesTypeDef,
    _OptionalClientGetResourceMetricsMetricQueriesTypeDef,
):
    """
    - *(dict) --*

      A single query to be processed. You must provide the metric to query. If no other parameters
      are specified, Performance Insights returns all of the data points for that metric. You can
      optionally request that the data points be aggregated by dimension group ( ``GroupBy`` ), and
      return only those data points that match your criteria (``Filter`` ).
      - **Metric** *(string) --***[REQUIRED]**

        The name of a Performance Insights metric to be measured.
        Valid values for ``Metric`` are:
        * ``db.load.avg`` - a scaled representation of the number of active sessions for the
        database engine.
        * ``db.sampledload.avg`` - the raw number of active sessions for the database engine.
    """


_ClientGetResourceMetricsResponseMetricListDataPointsTypeDef = TypedDict(
    "_ClientGetResourceMetricsResponseMetricListDataPointsTypeDef",
    {"Timestamp": datetime, "Value": float},
    total=False,
)


class ClientGetResourceMetricsResponseMetricListDataPointsTypeDef(
    _ClientGetResourceMetricsResponseMetricListDataPointsTypeDef
):
    pass


_ClientGetResourceMetricsResponseMetricListKeyTypeDef = TypedDict(
    "_ClientGetResourceMetricsResponseMetricListKeyTypeDef",
    {"Metric": str, "Dimensions": Dict[str, str]},
    total=False,
)


class ClientGetResourceMetricsResponseMetricListKeyTypeDef(
    _ClientGetResourceMetricsResponseMetricListKeyTypeDef
):
    pass


_ClientGetResourceMetricsResponseMetricListTypeDef = TypedDict(
    "_ClientGetResourceMetricsResponseMetricListTypeDef",
    {
        "Key": ClientGetResourceMetricsResponseMetricListKeyTypeDef,
        "DataPoints": List[ClientGetResourceMetricsResponseMetricListDataPointsTypeDef],
    },
    total=False,
)


class ClientGetResourceMetricsResponseMetricListTypeDef(
    _ClientGetResourceMetricsResponseMetricListTypeDef
):
    pass


_ClientGetResourceMetricsResponseTypeDef = TypedDict(
    "_ClientGetResourceMetricsResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "Identifier": str,
        "MetricList": List[ClientGetResourceMetricsResponseMetricListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetResourceMetricsResponseTypeDef(_ClientGetResourceMetricsResponseTypeDef):
    """
    - *(dict) --*

      - **AlignedStartTime** *(datetime) --*

        The start time for the returned metrics, after alignment to a granular boundary (as
        specified by ``PeriodInSeconds`` ). ``AlignedStartTime`` will be less than or equal to the
        value of the user-specified ``StartTime`` .
    """
