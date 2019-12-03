"Main interface for personalize-runtime service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef",
    "ClientGetPersonalizedRankingResponseTypeDef",
    "ClientGetRecommendationsResponseitemListTypeDef",
    "ClientGetRecommendationsResponseTypeDef",
)


_ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef = TypedDict(
    "_ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef", {"itemId": str}, total=False
)


class ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef(
    _ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef
):
    """
    - *(dict) --*

      An object that identifies an item.
      The and APIs return a list of ``PredictedItem`` s.
      - **itemId** *(string) --*

        The recommended item ID.
    """


_ClientGetPersonalizedRankingResponseTypeDef = TypedDict(
    "_ClientGetPersonalizedRankingResponseTypeDef",
    {"personalizedRanking": List[ClientGetPersonalizedRankingResponsepersonalizedRankingTypeDef]},
    total=False,
)


class ClientGetPersonalizedRankingResponseTypeDef(_ClientGetPersonalizedRankingResponseTypeDef):
    """
    - *(dict) --*

      - **personalizedRanking** *(list) --*

        A list of items in order of most likely interest to the user.
        - *(dict) --*

          An object that identifies an item.
          The and APIs return a list of ``PredictedItem`` s.
          - **itemId** *(string) --*

            The recommended item ID.
    """


_ClientGetRecommendationsResponseitemListTypeDef = TypedDict(
    "_ClientGetRecommendationsResponseitemListTypeDef", {"itemId": str}, total=False
)


class ClientGetRecommendationsResponseitemListTypeDef(
    _ClientGetRecommendationsResponseitemListTypeDef
):
    """
    - *(dict) --*

      An object that identifies an item.
      The and APIs return a list of ``PredictedItem`` s.
      - **itemId** *(string) --*

        The recommended item ID.
    """


_ClientGetRecommendationsResponseTypeDef = TypedDict(
    "_ClientGetRecommendationsResponseTypeDef",
    {"itemList": List[ClientGetRecommendationsResponseitemListTypeDef]},
    total=False,
)


class ClientGetRecommendationsResponseTypeDef(_ClientGetRecommendationsResponseTypeDef):
    """
    - *(dict) --*

      - **itemList** *(list) --*

        A list of recommendations.
        - *(dict) --*

          An object that identifies an item.
          The and APIs return a list of ``PredictedItem`` s.
          - **itemId** *(string) --*

            The recommended item ID.
    """
