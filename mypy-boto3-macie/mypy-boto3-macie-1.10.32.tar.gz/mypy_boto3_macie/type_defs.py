"Main interface for macie service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    "ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    "ClientAssociateS3ResourcesResponseTypeDef",
    "ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef",
    "ClientAssociateS3ResourcesS3ResourcesTypeDef",
    "ClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef",
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    "ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    "ClientDisassociateS3ResourcesResponseTypeDef",
    "ClientListMemberAccountsResponsememberAccountsTypeDef",
    "ClientListMemberAccountsResponseTypeDef",
    "ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef",
    "ClientListS3ResourcesResponses3ResourcesTypeDef",
    "ClientListS3ResourcesResponseTypeDef",
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    "ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef",
    "ClientUpdateS3ResourcesResponseTypeDef",
    "ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef",
    "ClientUpdateS3ResourcesS3ResourcesUpdateTypeDef",
    "ListMemberAccountsPaginatePaginationConfigTypeDef",
    "ListMemberAccountsPaginateResponsememberAccountsTypeDef",
    "ListMemberAccountsPaginateResponseTypeDef",
    "ListS3ResourcesPaginatePaginationConfigTypeDef",
    "ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef",
    "ListS3ResourcesPaginateResponses3ResourcesTypeDef",
    "ListS3ResourcesPaginateResponseTypeDef",
)


_ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "_ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)


class ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef(
    _ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef
):
    """
    - **failedItem** *(dict) --*

      The failed S3 resources.
      - **bucketName** *(string) --*

        The name of the S3 bucket.
    """


_ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "_ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientAssociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)


class ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef(
    _ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef
):
    """
    - *(dict) --*

      Includes details about the failed S3 resources.
      - **failedItem** *(dict) --*

        The failed S3 resources.
        - **bucketName** *(string) --*

          The name of the S3 bucket.
    """


_ClientAssociateS3ResourcesResponseTypeDef = TypedDict(
    "_ClientAssociateS3ResourcesResponseTypeDef",
    {"failedS3Resources": List[ClientAssociateS3ResourcesResponsefailedS3ResourcesTypeDef]},
    total=False,
)


class ClientAssociateS3ResourcesResponseTypeDef(_ClientAssociateS3ResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **failedS3Resources** *(list) --*

        S3 resources that couldn't be associated with Amazon Macie. An error code and an error
        message are provided for each failed item.
        - *(dict) --*

          Includes details about the failed S3 resources.
          - **failedItem** *(dict) --*

            The failed S3 resources.
            - **bucketName** *(string) --*

              The name of the S3 bucket.
    """


_ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef = TypedDict(
    "_ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)


class ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef(
    _ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef
):
    pass


_RequiredClientAssociateS3ResourcesS3ResourcesTypeDef = TypedDict(
    "_RequiredClientAssociateS3ResourcesS3ResourcesTypeDef", {"bucketName": str}
)
_OptionalClientAssociateS3ResourcesS3ResourcesTypeDef = TypedDict(
    "_OptionalClientAssociateS3ResourcesS3ResourcesTypeDef",
    {
        "prefix": str,
        "classificationType": ClientAssociateS3ResourcesS3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)


class ClientAssociateS3ResourcesS3ResourcesTypeDef(
    _RequiredClientAssociateS3ResourcesS3ResourcesTypeDef,
    _OptionalClientAssociateS3ResourcesS3ResourcesTypeDef,
):
    """
    - *(dict) --*

      The S3 resources that you want to associate with Amazon Macie for monitoring and data
      classification. This data type is used as a request parameter in the AssociateS3Resources
      action and a response parameter in the ListS3Resources action.
      - **bucketName** *(string) --***[REQUIRED]**

        The name of the S3 bucket that you want to associate with Amazon Macie.
    """


_RequiredClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef = TypedDict(
    "_RequiredClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef", {"bucketName": str}
)
_OptionalClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef = TypedDict(
    "_OptionalClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef",
    {"prefix": str},
    total=False,
)


class ClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef(
    _RequiredClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef,
    _OptionalClientDisassociateS3ResourcesAssociatedS3ResourcesTypeDef,
):
    """
    - *(dict) --*

      Contains information about the S3 resource. This data type is used as a request parameter in
      the DisassociateS3Resources action and can be used as a response parameter in the
      AssociateS3Resources and UpdateS3Resources actions.
      - **bucketName** *(string) --***[REQUIRED]**

        The name of the S3 bucket.
    """


_ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "_ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)


class ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef(
    _ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef
):
    """
    - **failedItem** *(dict) --*

      The failed S3 resources.
      - **bucketName** *(string) --*

        The name of the S3 bucket.
    """


_ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "_ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientDisassociateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)


class ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef(
    _ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef
):
    """
    - *(dict) --*

      Includes details about the failed S3 resources.
      - **failedItem** *(dict) --*

        The failed S3 resources.
        - **bucketName** *(string) --*

          The name of the S3 bucket.
    """


_ClientDisassociateS3ResourcesResponseTypeDef = TypedDict(
    "_ClientDisassociateS3ResourcesResponseTypeDef",
    {"failedS3Resources": List[ClientDisassociateS3ResourcesResponsefailedS3ResourcesTypeDef]},
    total=False,
)


class ClientDisassociateS3ResourcesResponseTypeDef(_ClientDisassociateS3ResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **failedS3Resources** *(list) --*

        S3 resources that couldn't be removed from being monitored and classified by Amazon Macie.
        An error code and an error message are provided for each failed item.
        - *(dict) --*

          Includes details about the failed S3 resources.
          - **failedItem** *(dict) --*

            The failed S3 resources.
            - **bucketName** *(string) --*

              The name of the S3 bucket.
    """


_ClientListMemberAccountsResponsememberAccountsTypeDef = TypedDict(
    "_ClientListMemberAccountsResponsememberAccountsTypeDef", {"accountId": str}, total=False
)


class ClientListMemberAccountsResponsememberAccountsTypeDef(
    _ClientListMemberAccountsResponsememberAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the Amazon Macie member account.
      - **accountId** *(string) --*

        The AWS account ID of the Amazon Macie member account.
    """


_ClientListMemberAccountsResponseTypeDef = TypedDict(
    "_ClientListMemberAccountsResponseTypeDef",
    {
        "memberAccounts": List[ClientListMemberAccountsResponsememberAccountsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListMemberAccountsResponseTypeDef(_ClientListMemberAccountsResponseTypeDef):
    """
    - *(dict) --*

      - **memberAccounts** *(list) --*

        A list of the Amazon Macie member accounts returned by the action. The current master
        account is also included in this list.
        - *(dict) --*

          Contains information about the Amazon Macie member account.
          - **accountId** *(string) --*

            The AWS account ID of the Amazon Macie member account.
    """


_ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef = TypedDict(
    "_ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)


class ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef(
    _ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef
):
    pass


_ClientListS3ResourcesResponses3ResourcesTypeDef = TypedDict(
    "_ClientListS3ResourcesResponses3ResourcesTypeDef",
    {
        "bucketName": str,
        "prefix": str,
        "classificationType": ClientListS3ResourcesResponses3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)


class ClientListS3ResourcesResponses3ResourcesTypeDef(
    _ClientListS3ResourcesResponses3ResourcesTypeDef
):
    """
    - *(dict) --*

      The S3 resources that you want to associate with Amazon Macie for monitoring and data
      classification. This data type is used as a request parameter in the AssociateS3Resources
      action and a response parameter in the ListS3Resources action.
      - **bucketName** *(string) --*

        The name of the S3 bucket that you want to associate with Amazon Macie.
    """


_ClientListS3ResourcesResponseTypeDef = TypedDict(
    "_ClientListS3ResourcesResponseTypeDef",
    {"s3Resources": List[ClientListS3ResourcesResponses3ResourcesTypeDef], "nextToken": str},
    total=False,
)


class ClientListS3ResourcesResponseTypeDef(_ClientListS3ResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **s3Resources** *(list) --*

        A list of the associated S3 resources returned by the action.
        - *(dict) --*

          The S3 resources that you want to associate with Amazon Macie for monitoring and data
          classification. This data type is used as a request parameter in the AssociateS3Resources
          action and a response parameter in the ListS3Resources action.
          - **bucketName** *(string) --*

            The name of the S3 bucket that you want to associate with Amazon Macie.
    """


_ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef = TypedDict(
    "_ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)


class ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef(
    _ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef
):
    """
    - **failedItem** *(dict) --*

      The failed S3 resources.
      - **bucketName** *(string) --*

        The name of the S3 bucket.
    """


_ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef = TypedDict(
    "_ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef",
    {
        "failedItem": ClientUpdateS3ResourcesResponsefailedS3ResourcesfailedItemTypeDef,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)


class ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef(
    _ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef
):
    """
    - *(dict) --*

      Includes details about the failed S3 resources.
      - **failedItem** *(dict) --*

        The failed S3 resources.
        - **bucketName** *(string) --*

          The name of the S3 bucket.
    """


_ClientUpdateS3ResourcesResponseTypeDef = TypedDict(
    "_ClientUpdateS3ResourcesResponseTypeDef",
    {"failedS3Resources": List[ClientUpdateS3ResourcesResponsefailedS3ResourcesTypeDef]},
    total=False,
)


class ClientUpdateS3ResourcesResponseTypeDef(_ClientUpdateS3ResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **failedS3Resources** *(list) --*

        The S3 resources whose classification types can't be updated. An error code and an error
        message are provided for each failed item.
        - *(dict) --*

          Includes details about the failed S3 resources.
          - **failedItem** *(dict) --*

            The failed S3 resources.
            - **bucketName** *(string) --*

              The name of the S3 bucket.
    """


_ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef = TypedDict(
    "_ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)


class ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef(
    _ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef
):
    pass


_RequiredClientUpdateS3ResourcesS3ResourcesUpdateTypeDef = TypedDict(
    "_RequiredClientUpdateS3ResourcesS3ResourcesUpdateTypeDef", {"bucketName": str}
)
_OptionalClientUpdateS3ResourcesS3ResourcesUpdateTypeDef = TypedDict(
    "_OptionalClientUpdateS3ResourcesS3ResourcesUpdateTypeDef",
    {
        "prefix": str,
        "classificationTypeUpdate": ClientUpdateS3ResourcesS3ResourcesUpdateclassificationTypeUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateS3ResourcesS3ResourcesUpdateTypeDef(
    _RequiredClientUpdateS3ResourcesS3ResourcesUpdateTypeDef,
    _OptionalClientUpdateS3ResourcesS3ResourcesUpdateTypeDef,
):
    """
    - *(dict) --*

      The S3 resources whose classification types you want to update. This data type is used as a
      request parameter in the UpdateS3Resources action.
      - **bucketName** *(string) --***[REQUIRED]**

        The name of the S3 bucket whose classification types you want to update.
    """


_ListMemberAccountsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMemberAccountsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMemberAccountsPaginatePaginationConfigTypeDef(
    _ListMemberAccountsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMemberAccountsPaginateResponsememberAccountsTypeDef = TypedDict(
    "_ListMemberAccountsPaginateResponsememberAccountsTypeDef", {"accountId": str}, total=False
)


class ListMemberAccountsPaginateResponsememberAccountsTypeDef(
    _ListMemberAccountsPaginateResponsememberAccountsTypeDef
):
    """
    - *(dict) --*

      Contains information about the Amazon Macie member account.
      - **accountId** *(string) --*

        The AWS account ID of the Amazon Macie member account.
    """


_ListMemberAccountsPaginateResponseTypeDef = TypedDict(
    "_ListMemberAccountsPaginateResponseTypeDef",
    {
        "memberAccounts": List[ListMemberAccountsPaginateResponsememberAccountsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListMemberAccountsPaginateResponseTypeDef(_ListMemberAccountsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **memberAccounts** *(list) --*

        A list of the Amazon Macie member accounts returned by the action. The current master
        account is also included in this list.
        - *(dict) --*

          Contains information about the Amazon Macie member account.
          - **accountId** *(string) --*

            The AWS account ID of the Amazon Macie member account.
    """


_ListS3ResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListS3ResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListS3ResourcesPaginatePaginationConfigTypeDef(
    _ListS3ResourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef = TypedDict(
    "_ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef",
    {"oneTime": Literal["FULL", "NONE"], "continuous": str},
    total=False,
)


class ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef(
    _ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef
):
    pass


_ListS3ResourcesPaginateResponses3ResourcesTypeDef = TypedDict(
    "_ListS3ResourcesPaginateResponses3ResourcesTypeDef",
    {
        "bucketName": str,
        "prefix": str,
        "classificationType": ListS3ResourcesPaginateResponses3ResourcesclassificationTypeTypeDef,
    },
    total=False,
)


class ListS3ResourcesPaginateResponses3ResourcesTypeDef(
    _ListS3ResourcesPaginateResponses3ResourcesTypeDef
):
    """
    - *(dict) --*

      The S3 resources that you want to associate with Amazon Macie for monitoring and data
      classification. This data type is used as a request parameter in the AssociateS3Resources
      action and a response parameter in the ListS3Resources action.
      - **bucketName** *(string) --*

        The name of the S3 bucket that you want to associate with Amazon Macie.
    """


_ListS3ResourcesPaginateResponseTypeDef = TypedDict(
    "_ListS3ResourcesPaginateResponseTypeDef",
    {"s3Resources": List[ListS3ResourcesPaginateResponses3ResourcesTypeDef], "NextToken": str},
    total=False,
)


class ListS3ResourcesPaginateResponseTypeDef(_ListS3ResourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **s3Resources** *(list) --*

        A list of the associated S3 resources returned by the action.
        - *(dict) --*

          The S3 resources that you want to associate with Amazon Macie for monitoring and data
          classification. This data type is used as a request parameter in the AssociateS3Resources
          action and a response parameter in the ListS3Resources action.
          - **bucketName** *(string) --*

            The name of the S3 bucket that you want to associate with Amazon Macie.
    """
