"Main interface for qldb-session service type defs"
from __future__ import annotations

from typing import Any, Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientSendCommandCommitTransactionTypeDef",
    "ClientSendCommandExecuteStatementParametersTypeDef",
    "ClientSendCommandExecuteStatementTypeDef",
    "ClientSendCommandFetchPageTypeDef",
    "ClientSendCommandResponseCommitTransactionTypeDef",
    "ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef",
    "ClientSendCommandResponseExecuteStatementFirstPageTypeDef",
    "ClientSendCommandResponseExecuteStatementTypeDef",
    "ClientSendCommandResponseFetchPagePageValuesTypeDef",
    "ClientSendCommandResponseFetchPagePageTypeDef",
    "ClientSendCommandResponseFetchPageTypeDef",
    "ClientSendCommandResponseStartSessionTypeDef",
    "ClientSendCommandResponseStartTransactionTypeDef",
    "ClientSendCommandResponseTypeDef",
    "ClientSendCommandStartSessionTypeDef",
)


_RequiredClientSendCommandCommitTransactionTypeDef = TypedDict(
    "_RequiredClientSendCommandCommitTransactionTypeDef", {"TransactionId": str}
)
_OptionalClientSendCommandCommitTransactionTypeDef = TypedDict(
    "_OptionalClientSendCommandCommitTransactionTypeDef", {"CommitDigest": bytes}, total=False
)


class ClientSendCommandCommitTransactionTypeDef(
    _RequiredClientSendCommandCommitTransactionTypeDef,
    _OptionalClientSendCommandCommitTransactionTypeDef,
):
    """
    Command to commit the specified transaction.
    - **TransactionId** *(string) --***[REQUIRED]**

      Specifies the transaction id of the transaction to commit.
    """


_ClientSendCommandExecuteStatementParametersTypeDef = TypedDict(
    "_ClientSendCommandExecuteStatementParametersTypeDef",
    {"IonBinary": bytes, "IonText": str},
    total=False,
)


class ClientSendCommandExecuteStatementParametersTypeDef(
    _ClientSendCommandExecuteStatementParametersTypeDef
):
    pass


_RequiredClientSendCommandExecuteStatementTypeDef = TypedDict(
    "_RequiredClientSendCommandExecuteStatementTypeDef", {"TransactionId": str}
)
_OptionalClientSendCommandExecuteStatementTypeDef = TypedDict(
    "_OptionalClientSendCommandExecuteStatementTypeDef",
    {"Statement": str, "Parameters": List[ClientSendCommandExecuteStatementParametersTypeDef]},
    total=False,
)


class ClientSendCommandExecuteStatementTypeDef(
    _RequiredClientSendCommandExecuteStatementTypeDef,
    _OptionalClientSendCommandExecuteStatementTypeDef,
):
    """
    Command to execute a statement in the specified transaction.
    - **TransactionId** *(string) --***[REQUIRED]**

      Specifies the transaction id of the request.
    """


_RequiredClientSendCommandFetchPageTypeDef = TypedDict(
    "_RequiredClientSendCommandFetchPageTypeDef", {"TransactionId": str}
)
_OptionalClientSendCommandFetchPageTypeDef = TypedDict(
    "_OptionalClientSendCommandFetchPageTypeDef", {"NextPageToken": str}, total=False
)


class ClientSendCommandFetchPageTypeDef(
    _RequiredClientSendCommandFetchPageTypeDef, _OptionalClientSendCommandFetchPageTypeDef
):
    """
    Command to fetch a page.
    - **TransactionId** *(string) --***[REQUIRED]**

      Specifies the transaction id of the page to be fetched.
    """


_ClientSendCommandResponseCommitTransactionTypeDef = TypedDict(
    "_ClientSendCommandResponseCommitTransactionTypeDef",
    {"TransactionId": str, "CommitDigest": bytes},
    total=False,
)


class ClientSendCommandResponseCommitTransactionTypeDef(
    _ClientSendCommandResponseCommitTransactionTypeDef
):
    pass


_ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef = TypedDict(
    "_ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef",
    {"IonBinary": bytes, "IonText": str},
    total=False,
)


class ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef(
    _ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef
):
    pass


_ClientSendCommandResponseExecuteStatementFirstPageTypeDef = TypedDict(
    "_ClientSendCommandResponseExecuteStatementFirstPageTypeDef",
    {
        "Values": List[ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientSendCommandResponseExecuteStatementFirstPageTypeDef(
    _ClientSendCommandResponseExecuteStatementFirstPageTypeDef
):
    pass


_ClientSendCommandResponseExecuteStatementTypeDef = TypedDict(
    "_ClientSendCommandResponseExecuteStatementTypeDef",
    {"FirstPage": ClientSendCommandResponseExecuteStatementFirstPageTypeDef},
    total=False,
)


class ClientSendCommandResponseExecuteStatementTypeDef(
    _ClientSendCommandResponseExecuteStatementTypeDef
):
    pass


_ClientSendCommandResponseFetchPagePageValuesTypeDef = TypedDict(
    "_ClientSendCommandResponseFetchPagePageValuesTypeDef",
    {"IonBinary": bytes, "IonText": str},
    total=False,
)


class ClientSendCommandResponseFetchPagePageValuesTypeDef(
    _ClientSendCommandResponseFetchPagePageValuesTypeDef
):
    pass


_ClientSendCommandResponseFetchPagePageTypeDef = TypedDict(
    "_ClientSendCommandResponseFetchPagePageTypeDef",
    {"Values": List[ClientSendCommandResponseFetchPagePageValuesTypeDef], "NextPageToken": str},
    total=False,
)


class ClientSendCommandResponseFetchPagePageTypeDef(_ClientSendCommandResponseFetchPagePageTypeDef):
    pass


_ClientSendCommandResponseFetchPageTypeDef = TypedDict(
    "_ClientSendCommandResponseFetchPageTypeDef",
    {"Page": ClientSendCommandResponseFetchPagePageTypeDef},
    total=False,
)


class ClientSendCommandResponseFetchPageTypeDef(_ClientSendCommandResponseFetchPageTypeDef):
    pass


_ClientSendCommandResponseStartSessionTypeDef = TypedDict(
    "_ClientSendCommandResponseStartSessionTypeDef", {"SessionToken": str}, total=False
)


class ClientSendCommandResponseStartSessionTypeDef(_ClientSendCommandResponseStartSessionTypeDef):
    """
    - **StartSession** *(dict) --*

      Contains the details of the started session that includes a session token. This
      ``SessionToken`` is required for every subsequent command that is issued during the current
      session.
      - **SessionToken** *(string) --*

        Session token of the started session. This ``SessionToken`` is required for every subsequent
        command that is issued during the current session.
    """


_ClientSendCommandResponseStartTransactionTypeDef = TypedDict(
    "_ClientSendCommandResponseStartTransactionTypeDef", {"TransactionId": str}, total=False
)


class ClientSendCommandResponseStartTransactionTypeDef(
    _ClientSendCommandResponseStartTransactionTypeDef
):
    pass


_ClientSendCommandResponseTypeDef = TypedDict(
    "_ClientSendCommandResponseTypeDef",
    {
        "StartSession": ClientSendCommandResponseStartSessionTypeDef,
        "StartTransaction": ClientSendCommandResponseStartTransactionTypeDef,
        "EndSession": Dict[str, Any],
        "CommitTransaction": ClientSendCommandResponseCommitTransactionTypeDef,
        "AbortTransaction": Dict[str, Any],
        "ExecuteStatement": ClientSendCommandResponseExecuteStatementTypeDef,
        "FetchPage": ClientSendCommandResponseFetchPageTypeDef,
    },
    total=False,
)


class ClientSendCommandResponseTypeDef(_ClientSendCommandResponseTypeDef):
    """
    - *(dict) --*

      - **StartSession** *(dict) --*

        Contains the details of the started session that includes a session token. This
        ``SessionToken`` is required for every subsequent command that is issued during the current
        session.
        - **SessionToken** *(string) --*

          Session token of the started session. This ``SessionToken`` is required for every
          subsequent command that is issued during the current session.
    """


_ClientSendCommandStartSessionTypeDef = TypedDict(
    "_ClientSendCommandStartSessionTypeDef", {"LedgerName": str}
)


class ClientSendCommandStartSessionTypeDef(_ClientSendCommandStartSessionTypeDef):
    """
    Command to start a new session. A session token is obtained as part of the response.
    - **LedgerName** *(string) --***[REQUIRED]**

      The name of the ledger to start a new session against.
    """
