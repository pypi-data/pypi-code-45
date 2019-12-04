"Main interface for forecastquery service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientQueryForecastResponseForecastPredictionsTypeDef",
    "ClientQueryForecastResponseForecastTypeDef",
    "ClientQueryForecastResponseTypeDef",
)


_ClientQueryForecastResponseForecastPredictionsTypeDef = TypedDict(
    "_ClientQueryForecastResponseForecastPredictionsTypeDef",
    {"Timestamp": str, "Value": float},
    total=False,
)


class ClientQueryForecastResponseForecastPredictionsTypeDef(
    _ClientQueryForecastResponseForecastPredictionsTypeDef
):
    pass


_ClientQueryForecastResponseForecastTypeDef = TypedDict(
    "_ClientQueryForecastResponseForecastTypeDef",
    {"Predictions": Dict[str, List[ClientQueryForecastResponseForecastPredictionsTypeDef]]},
    total=False,
)


class ClientQueryForecastResponseForecastTypeDef(_ClientQueryForecastResponseForecastTypeDef):
    """
    - **Forecast** *(dict) --*

      The forecast.
      - **Predictions** *(dict) --*

        The forecast.
        The *string* of the string to array map is one of the following values:
        * mean
        * p10
        * p50
        * p90
        - *(string) --*

          - *(list) --*

            - *(dict) --*

              The forecast value for a specific date. Part of the  Forecast object.
              - **Timestamp** *(string) --*

                The timestamp of the specific forecast.
    """


_ClientQueryForecastResponseTypeDef = TypedDict(
    "_ClientQueryForecastResponseTypeDef",
    {"Forecast": ClientQueryForecastResponseForecastTypeDef},
    total=False,
)


class ClientQueryForecastResponseTypeDef(_ClientQueryForecastResponseTypeDef):
    """
    - *(dict) --*

      - **Forecast** *(dict) --*

        The forecast.
        - **Predictions** *(dict) --*

          The forecast.
          The *string* of the string to array map is one of the following values:
          * mean
          * p10
          * p50
          * p90
          - *(string) --*

            - *(list) --*

              - *(dict) --*

                The forecast value for a specific date. Part of the  Forecast object.
                - **Timestamp** *(string) --*

                  The timestamp of the specific forecast.
    """
