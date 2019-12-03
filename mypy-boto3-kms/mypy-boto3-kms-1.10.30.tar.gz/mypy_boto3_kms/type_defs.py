"Main interface for kms service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCancelKeyDeletionResponseTypeDef",
    "ClientCreateCustomKeyStoreResponseTypeDef",
    "ClientCreateGrantConstraintsTypeDef",
    "ClientCreateGrantResponseTypeDef",
    "ClientCreateKeyResponseKeyMetadataTypeDef",
    "ClientCreateKeyResponseTypeDef",
    "ClientCreateKeyTagsTypeDef",
    "ClientDecryptResponseTypeDef",
    "ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef",
    "ClientDescribeCustomKeyStoresResponseTypeDef",
    "ClientDescribeKeyResponseKeyMetadataTypeDef",
    "ClientDescribeKeyResponseTypeDef",
    "ClientEncryptResponseTypeDef",
    "ClientGenerateDataKeyPairResponseTypeDef",
    "ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    "ClientGenerateDataKeyResponseTypeDef",
    "ClientGenerateDataKeyWithoutPlaintextResponseTypeDef",
    "ClientGenerateRandomResponseTypeDef",
    "ClientGetKeyPolicyResponseTypeDef",
    "ClientGetKeyRotationStatusResponseTypeDef",
    "ClientGetParametersForImportResponseTypeDef",
    "ClientGetPublicKeyResponseTypeDef",
    "ClientListAliasesResponseAliasesTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListGrantsResponseGrantsConstraintsTypeDef",
    "ClientListGrantsResponseGrantsTypeDef",
    "ClientListGrantsResponseTypeDef",
    "ClientListKeyPoliciesResponseTypeDef",
    "ClientListKeysResponseKeysTypeDef",
    "ClientListKeysResponseTypeDef",
    "ClientListResourceTagsResponseTagsTypeDef",
    "ClientListResourceTagsResponseTypeDef",
    "ClientListRetirableGrantsResponseGrantsConstraintsTypeDef",
    "ClientListRetirableGrantsResponseGrantsTypeDef",
    "ClientListRetirableGrantsResponseTypeDef",
    "ClientReEncryptResponseTypeDef",
    "ClientScheduleKeyDeletionResponseTypeDef",
    "ClientSignResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientVerifyResponseTypeDef",
    "ListAliasesPaginatePaginationConfigTypeDef",
    "ListAliasesPaginateResponseAliasesTypeDef",
    "ListAliasesPaginateResponseTypeDef",
    "ListGrantsPaginatePaginationConfigTypeDef",
    "ListGrantsPaginateResponseGrantsConstraintsTypeDef",
    "ListGrantsPaginateResponseGrantsTypeDef",
    "ListGrantsPaginateResponseTypeDef",
    "ListKeyPoliciesPaginatePaginationConfigTypeDef",
    "ListKeyPoliciesPaginateResponseTypeDef",
    "ListKeysPaginatePaginationConfigTypeDef",
    "ListKeysPaginateResponseKeysTypeDef",
    "ListKeysPaginateResponseTypeDef",
)


_ClientCancelKeyDeletionResponseTypeDef = TypedDict(
    "_ClientCancelKeyDeletionResponseTypeDef", {"KeyId": str}, total=False
)


class ClientCancelKeyDeletionResponseTypeDef(_ClientCancelKeyDeletionResponseTypeDef):
    """
    - *(dict) --*

      - **KeyId** *(string) --*

        The unique identifier of the master key for which deletion is canceled.
    """


_ClientCreateCustomKeyStoreResponseTypeDef = TypedDict(
    "_ClientCreateCustomKeyStoreResponseTypeDef", {"CustomKeyStoreId": str}, total=False
)


class ClientCreateCustomKeyStoreResponseTypeDef(_ClientCreateCustomKeyStoreResponseTypeDef):
    """
    - *(dict) --*

      - **CustomKeyStoreId** *(string) --*

        A unique identifier for the new custom key store.
    """


_ClientCreateGrantConstraintsTypeDef = TypedDict(
    "_ClientCreateGrantConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
    total=False,
)


class ClientCreateGrantConstraintsTypeDef(_ClientCreateGrantConstraintsTypeDef):
    """
    Allows a cryptographic operation only when the encryption context matches or includes the
    encryption context specified in this structure. For more information about encryption context,
    see `Encryption Context
    <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__ in the
    * *AWS Key Management Service Developer Guide* * .
    - **EncryptionContextSubset** *(dict) --*

      A list of key-value pairs that must be included in the encryption context of the cryptographic
      operation request. The grant allows the cryptographic operation only when the encryption
      context in the request includes the key-value pairs specified in this constraint, although it
      can include additional key-value pairs.
      - *(string) --*

        - *(string) --*
    """


_ClientCreateGrantResponseTypeDef = TypedDict(
    "_ClientCreateGrantResponseTypeDef", {"GrantToken": str, "GrantId": str}, total=False
)


class ClientCreateGrantResponseTypeDef(_ClientCreateGrantResponseTypeDef):
    """
    - *(dict) --*

      - **GrantToken** *(string) --*

        The grant token.
        For more information, see `Grant Tokens
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the
        *AWS Key Management Service Developer Guide* .
    """


_ClientCreateKeyResponseKeyMetadataTypeDef = TypedDict(
    "_ClientCreateKeyResponseKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "KeyId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"],
        "KeyState": Literal[
            "Enabled", "Disabled", "PendingDeletion", "PendingImport", "Unavailable"
        ],
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": Literal["AWS_KMS", "EXTERNAL", "AWS_CLOUDHSM"],
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": Literal["KEY_MATERIAL_EXPIRES", "KEY_MATERIAL_DOES_NOT_EXPIRE"],
        "KeyManager": Literal["AWS", "CUSTOMER"],
        "CustomerMasterKeySpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ],
        "EncryptionAlgorithms": List[
            Literal["SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"]
        ],
        "SigningAlgorithms": List[
            Literal[
                "RSASSA_PSS_SHA_256",
                "RSASSA_PSS_SHA_384",
                "RSASSA_PSS_SHA_512",
                "RSASSA_PKCS1_V1_5_SHA_256",
                "RSASSA_PKCS1_V1_5_SHA_384",
                "RSASSA_PKCS1_V1_5_SHA_512",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
            ]
        ],
    },
    total=False,
)


class ClientCreateKeyResponseKeyMetadataTypeDef(_ClientCreateKeyResponseKeyMetadataTypeDef):
    """
    - **KeyMetadata** *(dict) --*

      Metadata associated with the CMK.
      - **AWSAccountId** *(string) --*

        The twelve-digit account ID of the AWS account that owns the CMK.
    """


_ClientCreateKeyResponseTypeDef = TypedDict(
    "_ClientCreateKeyResponseTypeDef",
    {"KeyMetadata": ClientCreateKeyResponseKeyMetadataTypeDef},
    total=False,
)


class ClientCreateKeyResponseTypeDef(_ClientCreateKeyResponseTypeDef):
    """
    - *(dict) --*

      - **KeyMetadata** *(dict) --*

        Metadata associated with the CMK.
        - **AWSAccountId** *(string) --*

          The twelve-digit account ID of the AWS account that owns the CMK.
    """


_RequiredClientCreateKeyTagsTypeDef = TypedDict(
    "_RequiredClientCreateKeyTagsTypeDef", {"TagKey": str}
)
_OptionalClientCreateKeyTagsTypeDef = TypedDict(
    "_OptionalClientCreateKeyTagsTypeDef", {"TagValue": str}, total=False
)


class ClientCreateKeyTagsTypeDef(
    _RequiredClientCreateKeyTagsTypeDef, _OptionalClientCreateKeyTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are
      both required, but tag values can be empty (null) strings.
      For information about the rules that apply to tag keys and tag values, see `User-Defined Tag
      Restrictions
      <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
      in the *AWS Billing and Cost Management User Guide* .
      - **TagKey** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientDecryptResponseTypeDef = TypedDict(
    "_ClientDecryptResponseTypeDef",
    {
        "KeyId": str,
        "Plaintext": bytes,
        "EncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
    },
    total=False,
)


class ClientDecryptResponseTypeDef(_ClientDecryptResponseTypeDef):
    """
    - *(dict) --*

      - **KeyId** *(string) --*

        The ARN of the customer master key that was used to perform the decryption.
    """


_ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef = TypedDict(
    "_ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef",
    {
        "CustomKeyStoreId": str,
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "ConnectionState": Literal[
            "CONNECTED", "CONNECTING", "FAILED", "DISCONNECTED", "DISCONNECTING"
        ],
        "ConnectionErrorCode": Literal[
            "INVALID_CREDENTIALS",
            "CLUSTER_NOT_FOUND",
            "NETWORK_ERRORS",
            "INTERNAL_ERROR",
            "INSUFFICIENT_CLOUDHSM_HSMS",
            "USER_LOCKED_OUT",
        ],
        "CreationDate": datetime,
    },
    total=False,
)


class ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef(
    _ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef
):
    """
    - *(dict) --*

      Contains information about each custom key store in the custom key store list.
      - **CustomKeyStoreId** *(string) --*

        A unique identifier for the custom key store.
    """


_ClientDescribeCustomKeyStoresResponseTypeDef = TypedDict(
    "_ClientDescribeCustomKeyStoresResponseTypeDef",
    {
        "CustomKeyStores": List[ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)


class ClientDescribeCustomKeyStoresResponseTypeDef(_ClientDescribeCustomKeyStoresResponseTypeDef):
    """
    - *(dict) --*

      - **CustomKeyStores** *(list) --*

        Contains metadata about each custom key store.
        - *(dict) --*

          Contains information about each custom key store in the custom key store list.
          - **CustomKeyStoreId** *(string) --*

            A unique identifier for the custom key store.
    """


_ClientDescribeKeyResponseKeyMetadataTypeDef = TypedDict(
    "_ClientDescribeKeyResponseKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "KeyId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"],
        "KeyState": Literal[
            "Enabled", "Disabled", "PendingDeletion", "PendingImport", "Unavailable"
        ],
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": Literal["AWS_KMS", "EXTERNAL", "AWS_CLOUDHSM"],
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": Literal["KEY_MATERIAL_EXPIRES", "KEY_MATERIAL_DOES_NOT_EXPIRE"],
        "KeyManager": Literal["AWS", "CUSTOMER"],
        "CustomerMasterKeySpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ],
        "EncryptionAlgorithms": List[
            Literal["SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"]
        ],
        "SigningAlgorithms": List[
            Literal[
                "RSASSA_PSS_SHA_256",
                "RSASSA_PSS_SHA_384",
                "RSASSA_PSS_SHA_512",
                "RSASSA_PKCS1_V1_5_SHA_256",
                "RSASSA_PKCS1_V1_5_SHA_384",
                "RSASSA_PKCS1_V1_5_SHA_512",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
            ]
        ],
    },
    total=False,
)


class ClientDescribeKeyResponseKeyMetadataTypeDef(_ClientDescribeKeyResponseKeyMetadataTypeDef):
    """
    - **KeyMetadata** *(dict) --*

      Metadata associated with the key.
      - **AWSAccountId** *(string) --*

        The twelve-digit account ID of the AWS account that owns the CMK.
    """


_ClientDescribeKeyResponseTypeDef = TypedDict(
    "_ClientDescribeKeyResponseTypeDef",
    {"KeyMetadata": ClientDescribeKeyResponseKeyMetadataTypeDef},
    total=False,
)


class ClientDescribeKeyResponseTypeDef(_ClientDescribeKeyResponseTypeDef):
    """
    - *(dict) --*

      - **KeyMetadata** *(dict) --*

        Metadata associated with the key.
        - **AWSAccountId** *(string) --*

          The twelve-digit account ID of the AWS account that owns the CMK.
    """


_ClientEncryptResponseTypeDef = TypedDict(
    "_ClientEncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "EncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
    },
    total=False,
)


class ClientEncryptResponseTypeDef(_ClientEncryptResponseTypeDef):
    """
    - *(dict) --*

      - **CiphertextBlob** *(bytes) --*

        The encrypted plaintext. When you use the HTTP API or the AWS CLI, the value is
        Base64-encoded. Otherwise, it is not Base64-encoded.
    """


_ClientGenerateDataKeyPairResponseTypeDef = TypedDict(
    "_ClientGenerateDataKeyPairResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PrivateKeyPlaintext": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
    },
    total=False,
)


class ClientGenerateDataKeyPairResponseTypeDef(_ClientGenerateDataKeyPairResponseTypeDef):
    """
    - *(dict) --*

      - **PrivateKeyCiphertextBlob** *(bytes) --*

        The encrypted copy of the private key. When you use the HTTP API or the AWS CLI, the value
        is Base64-encoded. Otherwise, it is not Base64-encoded.
    """


_ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef = TypedDict(
    "_ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
    },
    total=False,
)


class ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef(
    _ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef
):
    """
    - *(dict) --*

      - **PrivateKeyCiphertextBlob** *(bytes) --*

        The encrypted copy of the private key. When you use the HTTP API or the AWS CLI, the value
        is Base64-encoded. Otherwise, it is not Base64-encoded.
    """


_ClientGenerateDataKeyResponseTypeDef = TypedDict(
    "_ClientGenerateDataKeyResponseTypeDef",
    {"CiphertextBlob": bytes, "Plaintext": bytes, "KeyId": str},
    total=False,
)


class ClientGenerateDataKeyResponseTypeDef(_ClientGenerateDataKeyResponseTypeDef):
    """
    - *(dict) --*

      - **CiphertextBlob** *(bytes) --*

        The encrypted copy of the data key. When you use the HTTP API or the AWS CLI, the value is
        Base64-encoded. Otherwise, it is not Base64-encoded.
    """


_ClientGenerateDataKeyWithoutPlaintextResponseTypeDef = TypedDict(
    "_ClientGenerateDataKeyWithoutPlaintextResponseTypeDef",
    {"CiphertextBlob": bytes, "KeyId": str},
    total=False,
)


class ClientGenerateDataKeyWithoutPlaintextResponseTypeDef(
    _ClientGenerateDataKeyWithoutPlaintextResponseTypeDef
):
    """
    - *(dict) --*

      - **CiphertextBlob** *(bytes) --*

        The encrypted data key. When you use the HTTP API or the AWS CLI, the value is
        Base64-encoded. Otherwise, it is not Base64-encoded.
    """


_ClientGenerateRandomResponseTypeDef = TypedDict(
    "_ClientGenerateRandomResponseTypeDef", {"Plaintext": bytes}, total=False
)


class ClientGenerateRandomResponseTypeDef(_ClientGenerateRandomResponseTypeDef):
    """
    - *(dict) --*

      - **Plaintext** *(bytes) --*

        The random byte string. When you use the HTTP API or the AWS CLI, the value is
        Base64-encoded. Otherwise, it is not Base64-encoded.
    """


_ClientGetKeyPolicyResponseTypeDef = TypedDict(
    "_ClientGetKeyPolicyResponseTypeDef", {"Policy": str}, total=False
)


class ClientGetKeyPolicyResponseTypeDef(_ClientGetKeyPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(string) --*

        A key policy document in JSON format.
    """


_ClientGetKeyRotationStatusResponseTypeDef = TypedDict(
    "_ClientGetKeyRotationStatusResponseTypeDef", {"KeyRotationEnabled": bool}, total=False
)


class ClientGetKeyRotationStatusResponseTypeDef(_ClientGetKeyRotationStatusResponseTypeDef):
    """
    - *(dict) --*

      - **KeyRotationEnabled** *(boolean) --*

        A Boolean value that specifies whether key rotation is enabled.
    """


_ClientGetParametersForImportResponseTypeDef = TypedDict(
    "_ClientGetParametersForImportResponseTypeDef",
    {"KeyId": str, "ImportToken": bytes, "PublicKey": bytes, "ParametersValidTo": datetime},
    total=False,
)


class ClientGetParametersForImportResponseTypeDef(_ClientGetParametersForImportResponseTypeDef):
    """
    - *(dict) --*

      - **KeyId** *(string) --*

        The identifier of the CMK to use in a subsequent  ImportKeyMaterial request. This is the
        same CMK specified in the ``GetParametersForImport`` request.
    """


_ClientGetPublicKeyResponseTypeDef = TypedDict(
    "_ClientGetPublicKeyResponseTypeDef",
    {
        "KeyId": str,
        "PublicKey": bytes,
        "CustomerMasterKeySpec": Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ],
        "KeyUsage": Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"],
        "EncryptionAlgorithms": List[
            Literal["SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"]
        ],
        "SigningAlgorithms": List[
            Literal[
                "RSASSA_PSS_SHA_256",
                "RSASSA_PSS_SHA_384",
                "RSASSA_PSS_SHA_512",
                "RSASSA_PKCS1_V1_5_SHA_256",
                "RSASSA_PKCS1_V1_5_SHA_384",
                "RSASSA_PKCS1_V1_5_SHA_512",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
            ]
        ],
    },
    total=False,
)


class ClientGetPublicKeyResponseTypeDef(_ClientGetPublicKeyResponseTypeDef):
    """
    - *(dict) --*

      - **KeyId** *(string) --*

        The identifier of the asymmetric CMK from which the public key was downloaded.
    """


_ClientListAliasesResponseAliasesTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesTypeDef",
    {"AliasName": str, "AliasArn": str, "TargetKeyId": str},
    total=False,
)


class ClientListAliasesResponseAliasesTypeDef(_ClientListAliasesResponseAliasesTypeDef):
    """
    - *(dict) --*

      Contains information about an alias.
      - **AliasName** *(string) --*

        String that contains the alias. This value begins with ``alias/`` .
    """


_ClientListAliasesResponseTypeDef = TypedDict(
    "_ClientListAliasesResponseTypeDef",
    {
        "Aliases": List[ClientListAliasesResponseAliasesTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)


class ClientListAliasesResponseTypeDef(_ClientListAliasesResponseTypeDef):
    """
    - *(dict) --*

      - **Aliases** *(list) --*

        A list of aliases.
        - *(dict) --*

          Contains information about an alias.
          - **AliasName** *(string) --*

            String that contains the alias. This value begins with ``alias/`` .
    """


_ClientListGrantsResponseGrantsConstraintsTypeDef = TypedDict(
    "_ClientListGrantsResponseGrantsConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
    total=False,
)


class ClientListGrantsResponseGrantsConstraintsTypeDef(
    _ClientListGrantsResponseGrantsConstraintsTypeDef
):
    pass


_ClientListGrantsResponseGrantsTypeDef = TypedDict(
    "_ClientListGrantsResponseGrantsTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[
            Literal[
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "Sign",
                "Verify",
                "GetPublicKey",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey",
                "GenerateDataKeyPair",
                "GenerateDataKeyPairWithoutPlaintext",
            ]
        ],
        "Constraints": ClientListGrantsResponseGrantsConstraintsTypeDef,
    },
    total=False,
)


class ClientListGrantsResponseGrantsTypeDef(_ClientListGrantsResponseGrantsTypeDef):
    """
    - *(dict) --*

      Contains information about an entry in a list of grants.
      - **KeyId** *(string) --*

        The unique identifier for the customer master key (CMK) to which the grant applies.
    """


_ClientListGrantsResponseTypeDef = TypedDict(
    "_ClientListGrantsResponseTypeDef",
    {"Grants": List[ClientListGrantsResponseGrantsTypeDef], "NextMarker": str, "Truncated": bool},
    total=False,
)


class ClientListGrantsResponseTypeDef(_ClientListGrantsResponseTypeDef):
    """
    - *(dict) --*

      - **Grants** *(list) --*

        A list of grants.
        - *(dict) --*

          Contains information about an entry in a list of grants.
          - **KeyId** *(string) --*

            The unique identifier for the customer master key (CMK) to which the grant applies.
    """


_ClientListKeyPoliciesResponseTypeDef = TypedDict(
    "_ClientListKeyPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "NextMarker": str, "Truncated": bool},
    total=False,
)


class ClientListKeyPoliciesResponseTypeDef(_ClientListKeyPoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyNames** *(list) --*

        A list of key policy names. The only valid value is ``default`` .
        - *(string) --*
    """


_ClientListKeysResponseKeysTypeDef = TypedDict(
    "_ClientListKeysResponseKeysTypeDef", {"KeyId": str, "KeyArn": str}, total=False
)


class ClientListKeysResponseKeysTypeDef(_ClientListKeysResponseKeysTypeDef):
    """
    - *(dict) --*

      Contains information about each entry in the key list.
      - **KeyId** *(string) --*

        Unique identifier of the key.
    """


_ClientListKeysResponseTypeDef = TypedDict(
    "_ClientListKeysResponseTypeDef",
    {"Keys": List[ClientListKeysResponseKeysTypeDef], "NextMarker": str, "Truncated": bool},
    total=False,
)


class ClientListKeysResponseTypeDef(_ClientListKeysResponseTypeDef):
    """
    - *(dict) --*

      - **Keys** *(list) --*

        A list of customer master keys (CMKs).
        - *(dict) --*

          Contains information about each entry in the key list.
          - **KeyId** *(string) --*

            Unique identifier of the key.
    """


_ClientListResourceTagsResponseTagsTypeDef = TypedDict(
    "_ClientListResourceTagsResponseTagsTypeDef", {"TagKey": str, "TagValue": str}, total=False
)


class ClientListResourceTagsResponseTagsTypeDef(_ClientListResourceTagsResponseTagsTypeDef):
    """
    - *(dict) --*

      A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are
      both required, but tag values can be empty (null) strings.
      For information about the rules that apply to tag keys and tag values, see `User-Defined Tag
      Restrictions
      <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
      in the *AWS Billing and Cost Management User Guide* .
      - **TagKey** *(string) --*

        The key of the tag.
    """


_ClientListResourceTagsResponseTypeDef = TypedDict(
    "_ClientListResourceTagsResponseTypeDef",
    {"Tags": List[ClientListResourceTagsResponseTagsTypeDef], "NextMarker": str, "Truncated": bool},
    total=False,
)


class ClientListResourceTagsResponseTypeDef(_ClientListResourceTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        A list of tags. Each tag consists of a tag key and a tag value.
        - *(dict) --*

          A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are
          both required, but tag values can be empty (null) strings.
          For information about the rules that apply to tag keys and tag values, see `User-Defined
          Tag Restrictions
          <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
          in the *AWS Billing and Cost Management User Guide* .
          - **TagKey** *(string) --*

            The key of the tag.
    """


_ClientListRetirableGrantsResponseGrantsConstraintsTypeDef = TypedDict(
    "_ClientListRetirableGrantsResponseGrantsConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
    total=False,
)


class ClientListRetirableGrantsResponseGrantsConstraintsTypeDef(
    _ClientListRetirableGrantsResponseGrantsConstraintsTypeDef
):
    pass


_ClientListRetirableGrantsResponseGrantsTypeDef = TypedDict(
    "_ClientListRetirableGrantsResponseGrantsTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[
            Literal[
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "Sign",
                "Verify",
                "GetPublicKey",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey",
                "GenerateDataKeyPair",
                "GenerateDataKeyPairWithoutPlaintext",
            ]
        ],
        "Constraints": ClientListRetirableGrantsResponseGrantsConstraintsTypeDef,
    },
    total=False,
)


class ClientListRetirableGrantsResponseGrantsTypeDef(
    _ClientListRetirableGrantsResponseGrantsTypeDef
):
    """
    - *(dict) --*

      Contains information about an entry in a list of grants.
      - **KeyId** *(string) --*

        The unique identifier for the customer master key (CMK) to which the grant applies.
    """


_ClientListRetirableGrantsResponseTypeDef = TypedDict(
    "_ClientListRetirableGrantsResponseTypeDef",
    {
        "Grants": List[ClientListRetirableGrantsResponseGrantsTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)


class ClientListRetirableGrantsResponseTypeDef(_ClientListRetirableGrantsResponseTypeDef):
    """
    - *(dict) --*

      - **Grants** *(list) --*

        A list of grants.
        - *(dict) --*

          Contains information about an entry in a list of grants.
          - **KeyId** *(string) --*

            The unique identifier for the customer master key (CMK) to which the grant applies.
    """


_ClientReEncryptResponseTypeDef = TypedDict(
    "_ClientReEncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "SourceKeyId": str,
        "KeyId": str,
        "SourceEncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
        "DestinationEncryptionAlgorithm": Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ],
    },
    total=False,
)


class ClientReEncryptResponseTypeDef(_ClientReEncryptResponseTypeDef):
    """
    - *(dict) --*

      - **CiphertextBlob** *(bytes) --*

        The reencrypted data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded.
        Otherwise, it is not Base64-encoded.
    """


_ClientScheduleKeyDeletionResponseTypeDef = TypedDict(
    "_ClientScheduleKeyDeletionResponseTypeDef",
    {"KeyId": str, "DeletionDate": datetime},
    total=False,
)


class ClientScheduleKeyDeletionResponseTypeDef(_ClientScheduleKeyDeletionResponseTypeDef):
    """
    - *(dict) --*

      - **KeyId** *(string) --*

        The unique identifier of the customer master key (CMK) for which deletion is scheduled.
    """


_ClientSignResponseTypeDef = TypedDict(
    "_ClientSignResponseTypeDef",
    {
        "KeyId": str,
        "Signature": bytes,
        "SigningAlgorithm": Literal[
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512",
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "ECDSA_SHA_256",
            "ECDSA_SHA_384",
            "ECDSA_SHA_512",
        ],
    },
    total=False,
)


class ClientSignResponseTypeDef(_ClientSignResponseTypeDef):
    """
    - *(dict) --*

      - **KeyId** *(string) --*

        The Amazon Resource Name (ARN) of the asymmetric CMK that was used to sign the message.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"TagKey": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"TagValue": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are
      both required, but tag values can be empty (null) strings.
      For information about the rules that apply to tag keys and tag values, see `User-Defined Tag
      Restrictions
      <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
      in the *AWS Billing and Cost Management User Guide* .
      - **TagKey** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientVerifyResponseTypeDef = TypedDict(
    "_ClientVerifyResponseTypeDef",
    {
        "KeyId": str,
        "SignatureValid": bool,
        "SigningAlgorithm": Literal[
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512",
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "ECDSA_SHA_256",
            "ECDSA_SHA_384",
            "ECDSA_SHA_512",
        ],
    },
    total=False,
)


class ClientVerifyResponseTypeDef(_ClientVerifyResponseTypeDef):
    """
    - *(dict) --*

      - **KeyId** *(string) --*

        The unique identifier for the asymmetric CMK that was used to verify the signature.
    """


_ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAliasesPaginatePaginationConfigTypeDef(_ListAliasesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAliasesPaginateResponseAliasesTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesTypeDef",
    {"AliasName": str, "AliasArn": str, "TargetKeyId": str},
    total=False,
)


class ListAliasesPaginateResponseAliasesTypeDef(_ListAliasesPaginateResponseAliasesTypeDef):
    """
    - *(dict) --*

      Contains information about an alias.
      - **AliasName** *(string) --*

        String that contains the alias. This value begins with ``alias/`` .
    """


_ListAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAliasesPaginateResponseTypeDef",
    {
        "Aliases": List[ListAliasesPaginateResponseAliasesTypeDef],
        "Truncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAliasesPaginateResponseTypeDef(_ListAliasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Aliases** *(list) --*

        A list of aliases.
        - *(dict) --*

          Contains information about an alias.
          - **AliasName** *(string) --*

            String that contains the alias. This value begins with ``alias/`` .
    """


_ListGrantsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGrantsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGrantsPaginatePaginationConfigTypeDef(_ListGrantsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGrantsPaginateResponseGrantsConstraintsTypeDef = TypedDict(
    "_ListGrantsPaginateResponseGrantsConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
    total=False,
)


class ListGrantsPaginateResponseGrantsConstraintsTypeDef(
    _ListGrantsPaginateResponseGrantsConstraintsTypeDef
):
    pass


_ListGrantsPaginateResponseGrantsTypeDef = TypedDict(
    "_ListGrantsPaginateResponseGrantsTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[
            Literal[
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "Sign",
                "Verify",
                "GetPublicKey",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey",
                "GenerateDataKeyPair",
                "GenerateDataKeyPairWithoutPlaintext",
            ]
        ],
        "Constraints": ListGrantsPaginateResponseGrantsConstraintsTypeDef,
    },
    total=False,
)


class ListGrantsPaginateResponseGrantsTypeDef(_ListGrantsPaginateResponseGrantsTypeDef):
    """
    - *(dict) --*

      Contains information about an entry in a list of grants.
      - **KeyId** *(string) --*

        The unique identifier for the customer master key (CMK) to which the grant applies.
    """


_ListGrantsPaginateResponseTypeDef = TypedDict(
    "_ListGrantsPaginateResponseTypeDef",
    {"Grants": List[ListGrantsPaginateResponseGrantsTypeDef], "Truncated": bool, "NextToken": str},
    total=False,
)


class ListGrantsPaginateResponseTypeDef(_ListGrantsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Grants** *(list) --*

        A list of grants.
        - *(dict) --*

          Contains information about an entry in a list of grants.
          - **KeyId** *(string) --*

            The unique identifier for the customer master key (CMK) to which the grant applies.
    """


_ListKeyPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListKeyPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListKeyPoliciesPaginatePaginationConfigTypeDef(
    _ListKeyPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListKeyPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListKeyPoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "Truncated": bool, "NextToken": str},
    total=False,
)


class ListKeyPoliciesPaginateResponseTypeDef(_ListKeyPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyNames** *(list) --*

        A list of key policy names. The only valid value is ``default`` .
        - *(string) --*
    """


_ListKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListKeysPaginatePaginationConfigTypeDef(_ListKeysPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListKeysPaginateResponseKeysTypeDef = TypedDict(
    "_ListKeysPaginateResponseKeysTypeDef", {"KeyId": str, "KeyArn": str}, total=False
)


class ListKeysPaginateResponseKeysTypeDef(_ListKeysPaginateResponseKeysTypeDef):
    """
    - *(dict) --*

      Contains information about each entry in the key list.
      - **KeyId** *(string) --*

        Unique identifier of the key.
    """


_ListKeysPaginateResponseTypeDef = TypedDict(
    "_ListKeysPaginateResponseTypeDef",
    {"Keys": List[ListKeysPaginateResponseKeysTypeDef], "Truncated": bool, "NextToken": str},
    total=False,
)


class ListKeysPaginateResponseTypeDef(_ListKeysPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Keys** *(list) --*

        A list of customer master keys (CMKs).
        - *(dict) --*

          Contains information about each entry in the key list.
          - **KeyId** *(string) --*

            Unique identifier of the key.
    """
