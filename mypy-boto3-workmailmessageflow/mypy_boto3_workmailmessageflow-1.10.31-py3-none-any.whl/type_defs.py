"Main interface for workmailmessageflow service type defs"
from __future__ import annotations

from botocore.response import StreamingBody
from mypy_boto3.type_defs import TypedDict


__all__ = ("ClientGetRawMessageContentResponseTypeDef",)


_ClientGetRawMessageContentResponseTypeDef = TypedDict(
    "_ClientGetRawMessageContentResponseTypeDef", {"messageContent": StreamingBody}, total=False
)


class ClientGetRawMessageContentResponseTypeDef(_ClientGetRawMessageContentResponseTypeDef):
    """
    - *(dict) --*

      - **messageContent** (:class:`.StreamingBody`) --

        The raw content of the email message, in MIME format.
    """
