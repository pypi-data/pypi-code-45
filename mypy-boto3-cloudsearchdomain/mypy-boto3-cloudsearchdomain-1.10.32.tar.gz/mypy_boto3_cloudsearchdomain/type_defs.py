"Main interface for cloudsearchdomain service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientSearchResponsefacetsbucketsTypeDef",
    "ClientSearchResponsefacetsTypeDef",
    "ClientSearchResponsehitshitTypeDef",
    "ClientSearchResponsehitsTypeDef",
    "ClientSearchResponsestatsTypeDef",
    "ClientSearchResponsestatusTypeDef",
    "ClientSearchResponseTypeDef",
    "ClientSuggestResponsestatusTypeDef",
    "ClientSuggestResponsesuggestsuggestionsTypeDef",
    "ClientSuggestResponsesuggestTypeDef",
    "ClientSuggestResponseTypeDef",
    "ClientUploadDocumentsResponsewarningsTypeDef",
    "ClientUploadDocumentsResponseTypeDef",
)


_ClientSearchResponsefacetsbucketsTypeDef = TypedDict(
    "_ClientSearchResponsefacetsbucketsTypeDef", {"value": str, "count": int}, total=False
)


class ClientSearchResponsefacetsbucketsTypeDef(_ClientSearchResponsefacetsbucketsTypeDef):
    pass


_ClientSearchResponsefacetsTypeDef = TypedDict(
    "_ClientSearchResponsefacetsTypeDef",
    {"buckets": List[ClientSearchResponsefacetsbucketsTypeDef]},
    total=False,
)


class ClientSearchResponsefacetsTypeDef(_ClientSearchResponsefacetsTypeDef):
    pass


_ClientSearchResponsehitshitTypeDef = TypedDict(
    "_ClientSearchResponsehitshitTypeDef",
    {
        "id": str,
        "fields": Dict[str, List[str]],
        "exprs": Dict[str, str],
        "highlights": Dict[str, str],
    },
    total=False,
)


class ClientSearchResponsehitshitTypeDef(_ClientSearchResponsehitshitTypeDef):
    pass


_ClientSearchResponsehitsTypeDef = TypedDict(
    "_ClientSearchResponsehitsTypeDef",
    {"found": int, "start": int, "cursor": str, "hit": List[ClientSearchResponsehitshitTypeDef]},
    total=False,
)


class ClientSearchResponsehitsTypeDef(_ClientSearchResponsehitsTypeDef):
    pass


_ClientSearchResponsestatsTypeDef = TypedDict(
    "_ClientSearchResponsestatsTypeDef",
    {
        "min": str,
        "max": str,
        "count": int,
        "missing": int,
        "sum": float,
        "sumOfSquares": float,
        "mean": str,
        "stddev": float,
    },
    total=False,
)


class ClientSearchResponsestatsTypeDef(_ClientSearchResponsestatsTypeDef):
    pass


_ClientSearchResponsestatusTypeDef = TypedDict(
    "_ClientSearchResponsestatusTypeDef", {"timems": int, "rid": str}, total=False
)


class ClientSearchResponsestatusTypeDef(_ClientSearchResponsestatusTypeDef):
    """
    - **status** *(dict) --*

      The status information returned for the search request.
      - **timems** *(integer) --*

        How long it took to process the request, in milliseconds.
    """


_ClientSearchResponseTypeDef = TypedDict(
    "_ClientSearchResponseTypeDef",
    {
        "status": ClientSearchResponsestatusTypeDef,
        "hits": ClientSearchResponsehitsTypeDef,
        "facets": Dict[str, ClientSearchResponsefacetsTypeDef],
        "stats": Dict[str, ClientSearchResponsestatsTypeDef],
    },
    total=False,
)


class ClientSearchResponseTypeDef(_ClientSearchResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``Search`` request. Contains the documents that match the specified search
      criteria and any requested fields, highlights, and facet information.
      - **status** *(dict) --*

        The status information returned for the search request.
        - **timems** *(integer) --*

          How long it took to process the request, in milliseconds.
    """


_ClientSuggestResponsestatusTypeDef = TypedDict(
    "_ClientSuggestResponsestatusTypeDef", {"timems": int, "rid": str}, total=False
)


class ClientSuggestResponsestatusTypeDef(_ClientSuggestResponsestatusTypeDef):
    """
    - **status** *(dict) --*

      The status of a ``SuggestRequest`` . Contains the resource ID (``rid`` ) and how long it took
      to process the request (``timems`` ).
      - **timems** *(integer) --*

        How long it took to process the request, in milliseconds.
    """


_ClientSuggestResponsesuggestsuggestionsTypeDef = TypedDict(
    "_ClientSuggestResponsesuggestsuggestionsTypeDef",
    {"suggestion": str, "score": int, "id": str},
    total=False,
)


class ClientSuggestResponsesuggestsuggestionsTypeDef(
    _ClientSuggestResponsesuggestsuggestionsTypeDef
):
    pass


_ClientSuggestResponsesuggestTypeDef = TypedDict(
    "_ClientSuggestResponsesuggestTypeDef",
    {
        "query": str,
        "found": int,
        "suggestions": List[ClientSuggestResponsesuggestsuggestionsTypeDef],
    },
    total=False,
)


class ClientSuggestResponsesuggestTypeDef(_ClientSuggestResponsesuggestTypeDef):
    pass


_ClientSuggestResponseTypeDef = TypedDict(
    "_ClientSuggestResponseTypeDef",
    {"status": ClientSuggestResponsestatusTypeDef, "suggest": ClientSuggestResponsesuggestTypeDef},
    total=False,
)


class ClientSuggestResponseTypeDef(_ClientSuggestResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a ``Suggest`` request.
      - **status** *(dict) --*

        The status of a ``SuggestRequest`` . Contains the resource ID (``rid`` ) and how long it
        took to process the request (``timems`` ).
        - **timems** *(integer) --*

          How long it took to process the request, in milliseconds.
    """


_ClientUploadDocumentsResponsewarningsTypeDef = TypedDict(
    "_ClientUploadDocumentsResponsewarningsTypeDef", {"message": str}, total=False
)


class ClientUploadDocumentsResponsewarningsTypeDef(_ClientUploadDocumentsResponsewarningsTypeDef):
    pass


_ClientUploadDocumentsResponseTypeDef = TypedDict(
    "_ClientUploadDocumentsResponseTypeDef",
    {
        "status": str,
        "adds": int,
        "deletes": int,
        "warnings": List[ClientUploadDocumentsResponsewarningsTypeDef],
    },
    total=False,
)


class ClientUploadDocumentsResponseTypeDef(_ClientUploadDocumentsResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to an ``UploadDocuments`` request.
      - **status** *(string) --*

        The status of an ``UploadDocumentsRequest`` .
    """
