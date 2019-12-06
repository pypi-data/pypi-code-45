"Main interface for personalize-runtime service type defs"
from __future__ import annotations

import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef = TypedDict(
    "ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef", {"itemId": str}, total=False
)

ClientGetPersonalizedRankingResponseTypeDef = TypedDict(
    "ClientGetPersonalizedRankingResponseTypeDef",
    {"personalizedRanking": List[ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef]},
    total=False,
)

ClientGetRecommendationsResponseitemListTypeDef = TypedDict(
    "ClientGetRecommendationsResponseitemListTypeDef", {"itemId": str}, total=False
)

ClientGetRecommendationsResponseTypeDef = TypedDict(
    "ClientGetRecommendationsResponseTypeDef",
    {"itemList": List[ClientGetRecommendationsResponseitemListTypeDef]},
    total=False,
)
