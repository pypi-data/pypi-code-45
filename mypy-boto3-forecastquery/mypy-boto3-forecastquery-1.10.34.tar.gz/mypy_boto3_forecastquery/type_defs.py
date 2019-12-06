"Main interface for forecastquery service type defs"
from __future__ import annotations

import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientQueryForecastResponseForecastPredictionsTypeDef = TypedDict(
    "ClientQueryForecastResponseForecastPredictionsTypeDef",
    {"Timestamp": str, "Value": float},
    total=False,
)

ClientQueryForecastResponseForecastTypeDef = TypedDict(
    "ClientQueryForecastResponseForecastTypeDef",
    {"Predictions": Dict[str, List[ClientQueryForecastResponseForecastPredictionsTypeDef]]},
    total=False,
)

ClientQueryForecastResponseTypeDef = TypedDict(
    "ClientQueryForecastResponseTypeDef",
    {"Forecast": ClientQueryForecastResponseForecastTypeDef},
    total=False,
)
