"Main interface for secretsmanager service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientCancelRotateSecretResponseTypeDef",
    "ClientCreateSecretResponseTypeDef",
    "ClientCreateSecretTagsTypeDef",
    "ClientDeleteResourcePolicyResponseTypeDef",
    "ClientDeleteSecretResponseTypeDef",
    "ClientDescribeSecretResponseRotationRulesTypeDef",
    "ClientDescribeSecretResponseTagsTypeDef",
    "ClientDescribeSecretResponseTypeDef",
    "ClientGetRandomPasswordResponseTypeDef",
    "ClientGetResourcePolicyResponseTypeDef",
    "ClientGetSecretValueResponseTypeDef",
    "ClientListSecretVersionIdsResponseVersionsTypeDef",
    "ClientListSecretVersionIdsResponseTypeDef",
    "ClientListSecretsResponseSecretListRotationRulesTypeDef",
    "ClientListSecretsResponseSecretListTagsTypeDef",
    "ClientListSecretsResponseSecretListTypeDef",
    "ClientListSecretsResponseTypeDef",
    "ClientPutResourcePolicyResponseTypeDef",
    "ClientPutSecretValueResponseTypeDef",
    "ClientRestoreSecretResponseTypeDef",
    "ClientRotateSecretResponseTypeDef",
    "ClientRotateSecretRotationRulesTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateSecretResponseTypeDef",
    "ClientUpdateSecretVersionStageResponseTypeDef",
    "ListSecretsPaginatePaginationConfigTypeDef",
    "ListSecretsPaginateResponseSecretListRotationRulesTypeDef",
    "ListSecretsPaginateResponseSecretListTagsTypeDef",
    "ListSecretsPaginateResponseSecretListTypeDef",
    "ListSecretsPaginateResponseTypeDef",
)


_ClientCancelRotateSecretResponseTypeDef = TypedDict(
    "_ClientCancelRotateSecretResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str},
    total=False,
)


class ClientCancelRotateSecretResponseTypeDef(_ClientCancelRotateSecretResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret for which rotation was canceled.
    """


_ClientCreateSecretResponseTypeDef = TypedDict(
    "_ClientCreateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)


class ClientCreateSecretResponseTypeDef(_ClientCreateSecretResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The Amazon Resource Name (ARN) of the secret that you just created.
        .. note::

          Secrets Manager automatically adds several random characters to the name at the end of the
          ARN when you initially create a secret. This affects only the ARN and not the actual
          friendly name. This ensures that if you create a new secret with the same name as an old
          secret that you previously deleted, then users with access to the old secret *don't*
          automatically get access to the new secret because the ARNs are different.
    """


_ClientCreateSecretTagsTypeDef = TypedDict(
    "_ClientCreateSecretTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateSecretTagsTypeDef(_ClientCreateSecretTagsTypeDef):
    pass


_ClientDeleteResourcePolicyResponseTypeDef = TypedDict(
    "_ClientDeleteResourcePolicyResponseTypeDef", {"ARN": str, "Name": str}, total=False
)


class ClientDeleteResourcePolicyResponseTypeDef(_ClientDeleteResourcePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret that the resource-based policy was deleted for.
    """


_ClientDeleteSecretResponseTypeDef = TypedDict(
    "_ClientDeleteSecretResponseTypeDef",
    {"ARN": str, "Name": str, "DeletionDate": datetime},
    total=False,
)


class ClientDeleteSecretResponseTypeDef(_ClientDeleteSecretResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret that is now scheduled for deletion.
    """


_ClientDescribeSecretResponseRotationRulesTypeDef = TypedDict(
    "_ClientDescribeSecretResponseRotationRulesTypeDef",
    {"AutomaticallyAfterDays": int},
    total=False,
)


class ClientDescribeSecretResponseRotationRulesTypeDef(
    _ClientDescribeSecretResponseRotationRulesTypeDef
):
    pass


_ClientDescribeSecretResponseTagsTypeDef = TypedDict(
    "_ClientDescribeSecretResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeSecretResponseTagsTypeDef(_ClientDescribeSecretResponseTagsTypeDef):
    pass


_ClientDescribeSecretResponseTypeDef = TypedDict(
    "_ClientDescribeSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": ClientDescribeSecretResponseRotationRulesTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[ClientDescribeSecretResponseTagsTypeDef],
        "VersionIdsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)


class ClientDescribeSecretResponseTypeDef(_ClientDescribeSecretResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret.
    """


_ClientGetRandomPasswordResponseTypeDef = TypedDict(
    "_ClientGetRandomPasswordResponseTypeDef", {"RandomPassword": str}, total=False
)


class ClientGetRandomPasswordResponseTypeDef(_ClientGetRandomPasswordResponseTypeDef):
    """
    - *(dict) --*

      - **RandomPassword** *(string) --*

        A string with the generated password.
    """


_ClientGetResourcePolicyResponseTypeDef = TypedDict(
    "_ClientGetResourcePolicyResponseTypeDef",
    {"ARN": str, "Name": str, "ResourcePolicy": str},
    total=False,
)


class ClientGetResourcePolicyResponseTypeDef(_ClientGetResourcePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret that the resource-based policy was retrieved for.
    """


_ClientGetSecretValueResponseTypeDef = TypedDict(
    "_ClientGetSecretValueResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "SecretBinary": bytes,
        "SecretString": str,
        "VersionStages": List[str],
        "CreatedDate": datetime,
    },
    total=False,
)


class ClientGetSecretValueResponseTypeDef(_ClientGetSecretValueResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret.
    """


_ClientListSecretVersionIdsResponseVersionsTypeDef = TypedDict(
    "_ClientListSecretVersionIdsResponseVersionsTypeDef",
    {
        "VersionId": str,
        "VersionStages": List[str],
        "LastAccessedDate": datetime,
        "CreatedDate": datetime,
    },
    total=False,
)


class ClientListSecretVersionIdsResponseVersionsTypeDef(
    _ClientListSecretVersionIdsResponseVersionsTypeDef
):
    """
    - *(dict) --*

      A structure that contains information about one version of a secret.
      - **VersionId** *(string) --*

        The unique version identifier of this version of the secret.
    """


_ClientListSecretVersionIdsResponseTypeDef = TypedDict(
    "_ClientListSecretVersionIdsResponseTypeDef",
    {
        "Versions": List[ClientListSecretVersionIdsResponseVersionsTypeDef],
        "NextToken": str,
        "ARN": str,
        "Name": str,
    },
    total=False,
)


class ClientListSecretVersionIdsResponseTypeDef(_ClientListSecretVersionIdsResponseTypeDef):
    """
    - *(dict) --*

      - **Versions** *(list) --*

        The list of the currently available versions of the specified secret.
        - *(dict) --*

          A structure that contains information about one version of a secret.
          - **VersionId** *(string) --*

            The unique version identifier of this version of the secret.
    """


_ClientListSecretsResponseSecretListRotationRulesTypeDef = TypedDict(
    "_ClientListSecretsResponseSecretListRotationRulesTypeDef",
    {"AutomaticallyAfterDays": int},
    total=False,
)


class ClientListSecretsResponseSecretListRotationRulesTypeDef(
    _ClientListSecretsResponseSecretListRotationRulesTypeDef
):
    pass


_ClientListSecretsResponseSecretListTagsTypeDef = TypedDict(
    "_ClientListSecretsResponseSecretListTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListSecretsResponseSecretListTagsTypeDef(
    _ClientListSecretsResponseSecretListTagsTypeDef
):
    pass


_ClientListSecretsResponseSecretListTypeDef = TypedDict(
    "_ClientListSecretsResponseSecretListTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": ClientListSecretsResponseSecretListRotationRulesTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[ClientListSecretsResponseSecretListTagsTypeDef],
        "SecretVersionsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)


class ClientListSecretsResponseSecretListTypeDef(_ClientListSecretsResponseSecretListTypeDef):
    """
    - *(dict) --*

      A structure that contains the details about a secret. It does not include the encrypted
      ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue
      operation.
      - **ARN** *(string) --*

        The Amazon Resource Name (ARN) of the secret.
        For more information about ARNs in Secrets Manager, see `Policy Resources
        <https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__
        in the *AWS Secrets Manager User Guide* .
    """


_ClientListSecretsResponseTypeDef = TypedDict(
    "_ClientListSecretsResponseTypeDef",
    {"SecretList": List[ClientListSecretsResponseSecretListTypeDef], "NextToken": str},
    total=False,
)


class ClientListSecretsResponseTypeDef(_ClientListSecretsResponseTypeDef):
    """
    - *(dict) --*

      - **SecretList** *(list) --*

        A list of the secrets in the account.
        - *(dict) --*

          A structure that contains the details about a secret. It does not include the encrypted
          ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue
          operation.
          - **ARN** *(string) --*

            The Amazon Resource Name (ARN) of the secret.
            For more information about ARNs in Secrets Manager, see `Policy Resources
            <https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__
            in the *AWS Secrets Manager User Guide* .
    """


_ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "_ClientPutResourcePolicyResponseTypeDef", {"ARN": str, "Name": str}, total=False
)


class ClientPutResourcePolicyResponseTypeDef(_ClientPutResourcePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret that the resource-based policy was retrieved for.
    """


_ClientPutSecretValueResponseTypeDef = TypedDict(
    "_ClientPutSecretValueResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str, "VersionStages": List[str]},
    total=False,
)


class ClientPutSecretValueResponseTypeDef(_ClientPutSecretValueResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The Amazon Resource Name (ARN) for the secret for which you just created a version.
    """


_ClientRestoreSecretResponseTypeDef = TypedDict(
    "_ClientRestoreSecretResponseTypeDef", {"ARN": str, "Name": str}, total=False
)


class ClientRestoreSecretResponseTypeDef(_ClientRestoreSecretResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret that was restored.
    """


_ClientRotateSecretResponseTypeDef = TypedDict(
    "_ClientRotateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)


class ClientRotateSecretResponseTypeDef(_ClientRotateSecretResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret.
    """


_ClientRotateSecretRotationRulesTypeDef = TypedDict(
    "_ClientRotateSecretRotationRulesTypeDef", {"AutomaticallyAfterDays": int}, total=False
)


class ClientRotateSecretRotationRulesTypeDef(_ClientRotateSecretRotationRulesTypeDef):
    """
    A structure that defines the rotation configuration for this secret.
    - **AutomaticallyAfterDays** *(integer) --*

      Specifies the number of days between automatic scheduled rotations of the secret.
      Secrets Manager schedules the next rotation when the previous one is complete. Secrets Manager
      schedules the date by adding the rotation interval (number of days) to the actual date of the
      last rotation. The service chooses the hour within that 24-hour date window randomly. The
      minute is also chosen somewhat randomly, but weighted towards the top of the hour and
      influenced by a variety of factors that help distribute load.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      A structure that contains information about a tag.
      - **Key** *(string) --*

        The key identifier, or name, of the tag.
    """


_ClientUpdateSecretResponseTypeDef = TypedDict(
    "_ClientUpdateSecretResponseTypeDef", {"ARN": str, "Name": str, "VersionId": str}, total=False
)


class ClientUpdateSecretResponseTypeDef(_ClientUpdateSecretResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret that was updated.
        .. note::

          Secrets Manager automatically adds several random characters to the name at the end of the
          ARN when you initially create a secret. This affects only the ARN and not the actual
          friendly name. This ensures that if you create a new secret with the same name as an old
          secret that you previously deleted, then users with access to the old secret *don't*
          automatically get access to the new secret because the ARNs are different.
    """


_ClientUpdateSecretVersionStageResponseTypeDef = TypedDict(
    "_ClientUpdateSecretVersionStageResponseTypeDef", {"ARN": str, "Name": str}, total=False
)


class ClientUpdateSecretVersionStageResponseTypeDef(_ClientUpdateSecretVersionStageResponseTypeDef):
    """
    - *(dict) --*

      - **ARN** *(string) --*

        The ARN of the secret with the staging label that was modified.
    """


_ListSecretsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSecretsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSecretsPaginatePaginationConfigTypeDef(_ListSecretsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSecretsPaginateResponseSecretListRotationRulesTypeDef = TypedDict(
    "_ListSecretsPaginateResponseSecretListRotationRulesTypeDef",
    {"AutomaticallyAfterDays": int},
    total=False,
)


class ListSecretsPaginateResponseSecretListRotationRulesTypeDef(
    _ListSecretsPaginateResponseSecretListRotationRulesTypeDef
):
    pass


_ListSecretsPaginateResponseSecretListTagsTypeDef = TypedDict(
    "_ListSecretsPaginateResponseSecretListTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListSecretsPaginateResponseSecretListTagsTypeDef(
    _ListSecretsPaginateResponseSecretListTagsTypeDef
):
    pass


_ListSecretsPaginateResponseSecretListTypeDef = TypedDict(
    "_ListSecretsPaginateResponseSecretListTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": ListSecretsPaginateResponseSecretListRotationRulesTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[ListSecretsPaginateResponseSecretListTagsTypeDef],
        "SecretVersionsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)


class ListSecretsPaginateResponseSecretListTypeDef(_ListSecretsPaginateResponseSecretListTypeDef):
    """
    - *(dict) --*

      A structure that contains the details about a secret. It does not include the encrypted
      ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue
      operation.
      - **ARN** *(string) --*

        The Amazon Resource Name (ARN) of the secret.
        For more information about ARNs in Secrets Manager, see `Policy Resources
        <https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__
        in the *AWS Secrets Manager User Guide* .
    """


_ListSecretsPaginateResponseTypeDef = TypedDict(
    "_ListSecretsPaginateResponseTypeDef",
    {"SecretList": List[ListSecretsPaginateResponseSecretListTypeDef]},
    total=False,
)


class ListSecretsPaginateResponseTypeDef(_ListSecretsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SecretList** *(list) --*

        A list of the secrets in the account.
        - *(dict) --*

          A structure that contains the details about a secret. It does not include the encrypted
          ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue
          operation.
          - **ARN** *(string) --*

            The Amazon Resource Name (ARN) of the secret.
            For more information about ARNs in Secrets Manager, see `Policy Resources
            <https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__
            in the *AWS Secrets Manager User Guide* .
    """
