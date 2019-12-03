"Main interface for sdb service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientBatchDeleteAttributesItemsAttributesTypeDef",
    "ClientBatchDeleteAttributesItemsTypeDef",
    "ClientBatchPutAttributesItemsAttributesTypeDef",
    "ClientBatchPutAttributesItemsTypeDef",
    "ClientDeleteAttributesAttributesTypeDef",
    "ClientDeleteAttributesExpectedTypeDef",
    "ClientDomainMetadataResponseTypeDef",
    "ClientGetAttributesResponseAttributesTypeDef",
    "ClientGetAttributesResponseTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientPutAttributesAttributesTypeDef",
    "ClientPutAttributesExpectedTypeDef",
    "ClientSelectResponseItemsAttributesTypeDef",
    "ClientSelectResponseItemsTypeDef",
    "ClientSelectResponseTypeDef",
    "ListDomainsPaginatePaginationConfigTypeDef",
    "ListDomainsPaginateResponseTypeDef",
    "SelectPaginatePaginationConfigTypeDef",
    "SelectPaginateResponseItemsAttributesTypeDef",
    "SelectPaginateResponseItemsTypeDef",
    "SelectPaginateResponseTypeDef",
)


_RequiredClientBatchDeleteAttributesItemsAttributesTypeDef = TypedDict(
    "_RequiredClientBatchDeleteAttributesItemsAttributesTypeDef", {"Name": str, "Value": str}
)
_OptionalClientBatchDeleteAttributesItemsAttributesTypeDef = TypedDict(
    "_OptionalClientBatchDeleteAttributesItemsAttributesTypeDef",
    {"AlternateNameEncoding": str, "AlternateValueEncoding": str},
    total=False,
)


class ClientBatchDeleteAttributesItemsAttributesTypeDef(
    _RequiredClientBatchDeleteAttributesItemsAttributesTypeDef,
    _OptionalClientBatchDeleteAttributesItemsAttributesTypeDef,
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]** The name of the attribute.
      - **AlternateNameEncoding** *(string) --*
      - **Value** *(string) --***[REQUIRED]** The value of the attribute.
      - **AlternateValueEncoding** *(string) --*
    """


_RequiredClientBatchDeleteAttributesItemsTypeDef = TypedDict(
    "_RequiredClientBatchDeleteAttributesItemsTypeDef", {"Name": str}
)
_OptionalClientBatchDeleteAttributesItemsTypeDef = TypedDict(
    "_OptionalClientBatchDeleteAttributesItemsTypeDef",
    {"Attributes": List[ClientBatchDeleteAttributesItemsAttributesTypeDef]},
    total=False,
)


class ClientBatchDeleteAttributesItemsTypeDef(
    _RequiredClientBatchDeleteAttributesItemsTypeDef,
    _OptionalClientBatchDeleteAttributesItemsTypeDef,
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]**
      - **Attributes** *(list) --*

        - *(dict) --*

          - **Name** *(string) --***[REQUIRED]** The name of the attribute.
          - **AlternateNameEncoding** *(string) --*
          - **Value** *(string) --***[REQUIRED]** The value of the attribute.
          - **AlternateValueEncoding** *(string) --*
    """


_RequiredClientBatchPutAttributesItemsAttributesTypeDef = TypedDict(
    "_RequiredClientBatchPutAttributesItemsAttributesTypeDef", {"Name": str, "Value": str}
)
_OptionalClientBatchPutAttributesItemsAttributesTypeDef = TypedDict(
    "_OptionalClientBatchPutAttributesItemsAttributesTypeDef", {"Replace": bool}, total=False
)


class ClientBatchPutAttributesItemsAttributesTypeDef(
    _RequiredClientBatchPutAttributesItemsAttributesTypeDef,
    _OptionalClientBatchPutAttributesItemsAttributesTypeDef,
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]** The name of the replaceable attribute.
      - **Value** *(string) --***[REQUIRED]** The value of the replaceable attribute.
      - **Replace** *(boolean) --*A flag specifying whether or not to replace the attribute/value
      pair or to add a new attribute/value pair. The default setting is ``false`` .
    """


_ClientBatchPutAttributesItemsTypeDef = TypedDict(
    "_ClientBatchPutAttributesItemsTypeDef",
    {"Name": str, "Attributes": List[ClientBatchPutAttributesItemsAttributesTypeDef]},
)


class ClientBatchPutAttributesItemsTypeDef(_ClientBatchPutAttributesItemsTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]** The name of the replaceable item.
      - **Attributes** *(list) --***[REQUIRED]** The list of attributes for a replaceable item.

        - *(dict) --*

          - **Name** *(string) --***[REQUIRED]** The name of the replaceable attribute.
          - **Value** *(string) --***[REQUIRED]** The value of the replaceable attribute.
          - **Replace** *(boolean) --*A flag specifying whether or not to replace the
          attribute/value pair or to add a new attribute/value pair. The default setting is
          ``false`` .
    """


_RequiredClientDeleteAttributesAttributesTypeDef = TypedDict(
    "_RequiredClientDeleteAttributesAttributesTypeDef", {"Name": str, "Value": str}
)
_OptionalClientDeleteAttributesAttributesTypeDef = TypedDict(
    "_OptionalClientDeleteAttributesAttributesTypeDef",
    {"AlternateNameEncoding": str, "AlternateValueEncoding": str},
    total=False,
)


class ClientDeleteAttributesAttributesTypeDef(
    _RequiredClientDeleteAttributesAttributesTypeDef,
    _OptionalClientDeleteAttributesAttributesTypeDef,
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]** The name of the attribute.
      - **AlternateNameEncoding** *(string) --*
      - **Value** *(string) --***[REQUIRED]** The value of the attribute.
      - **AlternateValueEncoding** *(string) --*
    """


_ClientDeleteAttributesExpectedTypeDef = TypedDict(
    "_ClientDeleteAttributesExpectedTypeDef",
    {"Name": str, "Value": str, "Exists": bool},
    total=False,
)


class ClientDeleteAttributesExpectedTypeDef(_ClientDeleteAttributesExpectedTypeDef):
    """
    - **Name** *(string) --*

      The name of the attribute involved in the condition.
    """


_ClientDomainMetadataResponseTypeDef = TypedDict(
    "_ClientDomainMetadataResponseTypeDef",
    {
        "ItemCount": int,
        "ItemNamesSizeBytes": int,
        "AttributeNameCount": int,
        "AttributeNamesSizeBytes": int,
        "AttributeValueCount": int,
        "AttributeValuesSizeBytes": int,
        "Timestamp": int,
    },
    total=False,
)


class ClientDomainMetadataResponseTypeDef(_ClientDomainMetadataResponseTypeDef):
    """
    - *(dict) --*

      - **ItemCount** *(integer) --*The number of all items in the domain.
      - **ItemNamesSizeBytes** *(integer) --*The total size of all item names in the domain, in
      bytes.
      - **AttributeNameCount** *(integer) --*The number of unique attribute names in the domain.
      - **AttributeNamesSizeBytes** *(integer) --*The total size of all unique attribute names in
      the domain, in bytes.
      - **AttributeValueCount** *(integer) --*The number of all attribute name/value pairs in the
      domain.
      - **AttributeValuesSizeBytes** *(integer) --*The total size of all attribute values in the
      domain, in bytes.
      - **Timestamp** *(integer) --*The data and time when metadata was calculated, in Epoch (UNIX)
      seconds.
    """


_ClientGetAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientGetAttributesResponseAttributesTypeDef",
    {"Name": str, "AlternateNameEncoding": str, "Value": str, "AlternateValueEncoding": str},
    total=False,
)


class ClientGetAttributesResponseAttributesTypeDef(_ClientGetAttributesResponseAttributesTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*The name of the attribute.
      - **AlternateNameEncoding** *(string) --*
      - **Value** *(string) --*The value of the attribute.
      - **AlternateValueEncoding** *(string) --*
    """


_ClientGetAttributesResponseTypeDef = TypedDict(
    "_ClientGetAttributesResponseTypeDef",
    {"Attributes": List[ClientGetAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientGetAttributesResponseTypeDef(_ClientGetAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **Attributes** *(list) --*The list of attributes returned by the operation.

        - *(dict) --*

          - **Name** *(string) --*The name of the attribute.
          - **AlternateNameEncoding** *(string) --*
          - **Value** *(string) --*The value of the attribute.
          - **AlternateValueEncoding** *(string) --*
    """


_ClientListDomainsResponseTypeDef = TypedDict(
    "_ClientListDomainsResponseTypeDef", {"DomainNames": List[str], "NextToken": str}, total=False
)


class ClientListDomainsResponseTypeDef(_ClientListDomainsResponseTypeDef):
    """
    - *(dict) --*

      - **DomainNames** *(list) --*A list of domain names that match the expression.

        - *(string) --*
    """


_RequiredClientPutAttributesAttributesTypeDef = TypedDict(
    "_RequiredClientPutAttributesAttributesTypeDef", {"Name": str, "Value": str}
)
_OptionalClientPutAttributesAttributesTypeDef = TypedDict(
    "_OptionalClientPutAttributesAttributesTypeDef", {"Replace": bool}, total=False
)


class ClientPutAttributesAttributesTypeDef(
    _RequiredClientPutAttributesAttributesTypeDef, _OptionalClientPutAttributesAttributesTypeDef
):
    """
    - *(dict) --*

      - **Name** *(string) --***[REQUIRED]** The name of the replaceable attribute.
      - **Value** *(string) --***[REQUIRED]** The value of the replaceable attribute.
      - **Replace** *(boolean) --*A flag specifying whether or not to replace the attribute/value
      pair or to add a new attribute/value pair. The default setting is ``false`` .
    """


_ClientPutAttributesExpectedTypeDef = TypedDict(
    "_ClientPutAttributesExpectedTypeDef", {"Name": str, "Value": str, "Exists": bool}, total=False
)


class ClientPutAttributesExpectedTypeDef(_ClientPutAttributesExpectedTypeDef):
    """
    - **Name** *(string) --*

      The name of the attribute involved in the condition.
    """


_ClientSelectResponseItemsAttributesTypeDef = TypedDict(
    "_ClientSelectResponseItemsAttributesTypeDef",
    {"Name": str, "AlternateNameEncoding": str, "Value": str, "AlternateValueEncoding": str},
    total=False,
)


class ClientSelectResponseItemsAttributesTypeDef(_ClientSelectResponseItemsAttributesTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*The name of the attribute.
      - **AlternateNameEncoding** *(string) --*
      - **Value** *(string) --*The value of the attribute.
      - **AlternateValueEncoding** *(string) --*
    """


_ClientSelectResponseItemsTypeDef = TypedDict(
    "_ClientSelectResponseItemsTypeDef",
    {
        "Name": str,
        "AlternateNameEncoding": str,
        "Attributes": List[ClientSelectResponseItemsAttributesTypeDef],
    },
    total=False,
)


class ClientSelectResponseItemsTypeDef(_ClientSelectResponseItemsTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*The name of the item.
      - **AlternateNameEncoding** *(string) --*
      - **Attributes** *(list) --*A list of attributes.

        - *(dict) --*

          - **Name** *(string) --*The name of the attribute.
          - **AlternateNameEncoding** *(string) --*
          - **Value** *(string) --*The value of the attribute.
          - **AlternateValueEncoding** *(string) --*
    """


_ClientSelectResponseTypeDef = TypedDict(
    "_ClientSelectResponseTypeDef",
    {"Items": List[ClientSelectResponseItemsTypeDef], "NextToken": str},
    total=False,
)


class ClientSelectResponseTypeDef(_ClientSelectResponseTypeDef):
    """
    - *(dict) --*

      - **Items** *(list) --*A list of items that match the select expression.

        - *(dict) --*

          - **Name** *(string) --*The name of the item.
          - **AlternateNameEncoding** *(string) --*
          - **Attributes** *(list) --*A list of attributes.

            - *(dict) --*

              - **Name** *(string) --*The name of the attribute.
              - **AlternateNameEncoding** *(string) --*
              - **Value** *(string) --*The value of the attribute.
              - **AlternateValueEncoding** *(string) --*
    """


_ListDomainsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDomainsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDomainsPaginatePaginationConfigTypeDef(_ListDomainsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDomainsPaginateResponseTypeDef = TypedDict(
    "_ListDomainsPaginateResponseTypeDef", {"DomainNames": List[str]}, total=False
)


class ListDomainsPaginateResponseTypeDef(_ListDomainsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **DomainNames** *(list) --*A list of domain names that match the expression.

        - *(string) --*
    """


_SelectPaginatePaginationConfigTypeDef = TypedDict(
    "_SelectPaginatePaginationConfigTypeDef", {"MaxItems": int, "StartingToken": str}, total=False
)


class SelectPaginatePaginationConfigTypeDef(_SelectPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SelectPaginateResponseItemsAttributesTypeDef = TypedDict(
    "_SelectPaginateResponseItemsAttributesTypeDef",
    {"Name": str, "AlternateNameEncoding": str, "Value": str, "AlternateValueEncoding": str},
    total=False,
)


class SelectPaginateResponseItemsAttributesTypeDef(_SelectPaginateResponseItemsAttributesTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*The name of the attribute.
      - **AlternateNameEncoding** *(string) --*
      - **Value** *(string) --*The value of the attribute.
      - **AlternateValueEncoding** *(string) --*
    """


_SelectPaginateResponseItemsTypeDef = TypedDict(
    "_SelectPaginateResponseItemsTypeDef",
    {
        "Name": str,
        "AlternateNameEncoding": str,
        "Attributes": List[SelectPaginateResponseItemsAttributesTypeDef],
    },
    total=False,
)


class SelectPaginateResponseItemsTypeDef(_SelectPaginateResponseItemsTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*The name of the item.
      - **AlternateNameEncoding** *(string) --*
      - **Attributes** *(list) --*A list of attributes.

        - *(dict) --*

          - **Name** *(string) --*The name of the attribute.
          - **AlternateNameEncoding** *(string) --*
          - **Value** *(string) --*The value of the attribute.
          - **AlternateValueEncoding** *(string) --*
    """


_SelectPaginateResponseTypeDef = TypedDict(
    "_SelectPaginateResponseTypeDef",
    {"Items": List[SelectPaginateResponseItemsTypeDef]},
    total=False,
)


class SelectPaginateResponseTypeDef(_SelectPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Items** *(list) --*A list of items that match the select expression.

        - *(dict) --*

          - **Name** *(string) --*The name of the item.
          - **AlternateNameEncoding** *(string) --*
          - **Attributes** *(list) --*A list of attributes.

            - *(dict) --*

              - **Name** *(string) --*The name of the attribute.
              - **AlternateNameEncoding** *(string) --*
              - **Value** *(string) --*The value of the attribute.
              - **AlternateValueEncoding** *(string) --*
    """
