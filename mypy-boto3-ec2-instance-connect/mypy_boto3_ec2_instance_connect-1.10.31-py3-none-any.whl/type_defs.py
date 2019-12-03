"Main interface for ec2-instance-connect service type defs"
from __future__ import annotations

from mypy_boto3.type_defs import TypedDict


__all__ = ("ClientSendSshPublicKeyResponseTypeDef",)


_ClientSendSshPublicKeyResponseTypeDef = TypedDict(
    "_ClientSendSshPublicKeyResponseTypeDef", {"RequestId": str, "Success": bool}, total=False
)


class ClientSendSshPublicKeyResponseTypeDef(_ClientSendSshPublicKeyResponseTypeDef):
    """
    - *(dict) --*

      - **RequestId** *(string) --*

        The request ID as logged by EC2 Connect. Please provide this when contacting AWS Support.
    """
