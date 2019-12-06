"Main interface for kms service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_kms.client as client_scope

# pylint: disable=import-self
import mypy_boto3_kms.paginator as paginator_scope
from mypy_boto3_kms.type_defs import (
    ClientCancelKeyDeletionResponseTypeDef,
    ClientCreateCustomKeyStoreResponseTypeDef,
    ClientCreateGrantConstraintsTypeDef,
    ClientCreateGrantResponseTypeDef,
    ClientCreateKeyResponseTypeDef,
    ClientCreateKeyTagsTypeDef,
    ClientDecryptResponseTypeDef,
    ClientDescribeCustomKeyStoresResponseTypeDef,
    ClientDescribeKeyResponseTypeDef,
    ClientEncryptResponseTypeDef,
    ClientGenerateDataKeyPairResponseTypeDef,
    ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef,
    ClientGenerateDataKeyResponseTypeDef,
    ClientGenerateDataKeyWithoutPlaintextResponseTypeDef,
    ClientGenerateRandomResponseTypeDef,
    ClientGetKeyPolicyResponseTypeDef,
    ClientGetKeyRotationStatusResponseTypeDef,
    ClientGetParametersForImportResponseTypeDef,
    ClientGetPublicKeyResponseTypeDef,
    ClientListAliasesResponseTypeDef,
    ClientListGrantsResponseTypeDef,
    ClientListKeyPoliciesResponseTypeDef,
    ClientListKeysResponseTypeDef,
    ClientListResourceTagsResponseTypeDef,
    ClientListRetirableGrantsResponseTypeDef,
    ClientReEncryptResponseTypeDef,
    ClientScheduleKeyDeletionResponseTypeDef,
    ClientSignResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientVerifyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [KMS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_key_deletion(self, KeyId: str) -> ClientCancelKeyDeletionResponseTypeDef:
        """
        [Client.cancel_key_deletion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.cancel_key_deletion)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def connect_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        [Client.connect_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.connect_custom_key_store)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_alias(self, AliasName: str, TargetKeyId: str) -> None:
        """
        [Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.create_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_custom_key_store(
        self,
        CustomKeyStoreName: str,
        CloudHsmClusterId: str,
        TrustAnchorCertificate: str,
        KeyStorePassword: str,
    ) -> ClientCreateCustomKeyStoreResponseTypeDef:
        """
        [Client.create_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.create_custom_key_store)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_grant(
        self,
        KeyId: str,
        GranteePrincipal: str,
        Operations: List[
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
        RetiringPrincipal: str = None,
        Constraints: ClientCreateGrantConstraintsTypeDef = None,
        GrantTokens: List[str] = None,
        Name: str = None,
    ) -> ClientCreateGrantResponseTypeDef:
        """
        [Client.create_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.create_grant)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_key(
        self,
        Policy: str = None,
        Description: str = None,
        KeyUsage: Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"] = None,
        CustomerMasterKeySpec: Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ] = None,
        Origin: Literal["AWS_KMS", "EXTERNAL", "AWS_CLOUDHSM"] = None,
        CustomKeyStoreId: str = None,
        BypassPolicyLockoutSafetyCheck: bool = None,
        Tags: List[ClientCreateKeyTagsTypeDef] = None,
    ) -> ClientCreateKeyResponseTypeDef:
        """
        [Client.create_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.create_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decrypt(
        self,
        CiphertextBlob: bytes,
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
        KeyId: str = None,
        EncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
    ) -> ClientDecryptResponseTypeDef:
        """
        [Client.decrypt documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.decrypt)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_alias(self, AliasName: str) -> None:
        """
        [Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.delete_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        [Client.delete_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.delete_custom_key_store)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_imported_key_material(self, KeyId: str) -> None:
        """
        [Client.delete_imported_key_material documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.delete_imported_key_material)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_custom_key_stores(
        self,
        CustomKeyStoreId: str = None,
        CustomKeyStoreName: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> ClientDescribeCustomKeyStoresResponseTypeDef:
        """
        [Client.describe_custom_key_stores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.describe_custom_key_stores)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_key(
        self, KeyId: str, GrantTokens: List[str] = None
    ) -> ClientDescribeKeyResponseTypeDef:
        """
        [Client.describe_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.describe_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_key(self, KeyId: str) -> None:
        """
        [Client.disable_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.disable_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_key_rotation(self, KeyId: str) -> None:
        """
        [Client.disable_key_rotation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.disable_key_rotation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disconnect_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        [Client.disconnect_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.disconnect_custom_key_store)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_key(self, KeyId: str) -> None:
        """
        [Client.enable_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.enable_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_key_rotation(self, KeyId: str) -> None:
        """
        [Client.enable_key_rotation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.enable_key_rotation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def encrypt(
        self,
        KeyId: str,
        Plaintext: bytes,
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
        EncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
    ) -> ClientEncryptResponseTypeDef:
        """
        [Client.encrypt documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.encrypt)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_data_key(
        self,
        KeyId: str,
        EncryptionContext: Dict[str, str] = None,
        NumberOfBytes: int = None,
        KeySpec: Literal["AES_256", "AES_128"] = None,
        GrantTokens: List[str] = None,
    ) -> ClientGenerateDataKeyResponseTypeDef:
        """
        [Client.generate_data_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.generate_data_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_data_key_pair(
        self,
        KeyId: str,
        KeyPairSpec: Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
    ) -> ClientGenerateDataKeyPairResponseTypeDef:
        """
        [Client.generate_data_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.generate_data_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_data_key_pair_without_plaintext(
        self,
        KeyId: str,
        KeyPairSpec: Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
    ) -> ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef:
        """
        [Client.generate_data_key_pair_without_plaintext documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.generate_data_key_pair_without_plaintext)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_data_key_without_plaintext(
        self,
        KeyId: str,
        EncryptionContext: Dict[str, str] = None,
        KeySpec: Literal["AES_256", "AES_128"] = None,
        NumberOfBytes: int = None,
        GrantTokens: List[str] = None,
    ) -> ClientGenerateDataKeyWithoutPlaintextResponseTypeDef:
        """
        [Client.generate_data_key_without_plaintext documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.generate_data_key_without_plaintext)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_random(
        self, NumberOfBytes: int = None, CustomKeyStoreId: str = None
    ) -> ClientGenerateRandomResponseTypeDef:
        """
        [Client.generate_random documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.generate_random)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_key_policy(self, KeyId: str, PolicyName: str) -> ClientGetKeyPolicyResponseTypeDef:
        """
        [Client.get_key_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.get_key_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_key_rotation_status(self, KeyId: str) -> ClientGetKeyRotationStatusResponseTypeDef:
        """
        [Client.get_key_rotation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.get_key_rotation_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_parameters_for_import(
        self,
        KeyId: str,
        WrappingAlgorithm: Literal["RSAES_PKCS1_V1_5", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"],
        WrappingKeySpec: str,
    ) -> ClientGetParametersForImportResponseTypeDef:
        """
        [Client.get_parameters_for_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.get_parameters_for_import)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_public_key(
        self, KeyId: str, GrantTokens: List[str] = None
    ) -> ClientGetPublicKeyResponseTypeDef:
        """
        [Client.get_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.get_public_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_key_material(
        self,
        KeyId: str,
        ImportToken: bytes,
        EncryptedKeyMaterial: bytes,
        ValidTo: datetime = None,
        ExpirationModel: Literal["KEY_MATERIAL_EXPIRES", "KEY_MATERIAL_DOES_NOT_EXPIRE"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.import_key_material documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.import_key_material)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aliases(
        self, KeyId: str = None, Limit: int = None, Marker: str = None
    ) -> ClientListAliasesResponseTypeDef:
        """
        [Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.list_aliases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_grants(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ClientListGrantsResponseTypeDef:
        """
        [Client.list_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.list_grants)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_key_policies(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ClientListKeyPoliciesResponseTypeDef:
        """
        [Client.list_key_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.list_key_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_keys(self, Limit: int = None, Marker: str = None) -> ClientListKeysResponseTypeDef:
        """
        [Client.list_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.list_keys)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_tags(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ClientListResourceTagsResponseTypeDef:
        """
        [Client.list_resource_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.list_resource_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_retirable_grants(
        self, RetiringPrincipal: str, Limit: int = None, Marker: str = None
    ) -> ClientListRetirableGrantsResponseTypeDef:
        """
        [Client.list_retirable_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.list_retirable_grants)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_key_policy(
        self, KeyId: str, PolicyName: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None
    ) -> None:
        """
        [Client.put_key_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.put_key_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def re_encrypt(
        self,
        CiphertextBlob: bytes,
        DestinationKeyId: str,
        SourceEncryptionContext: Dict[str, str] = None,
        SourceKeyId: str = None,
        DestinationEncryptionContext: Dict[str, str] = None,
        SourceEncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
        DestinationEncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
        GrantTokens: List[str] = None,
    ) -> ClientReEncryptResponseTypeDef:
        """
        [Client.re_encrypt documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.re_encrypt)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def retire_grant(self, GrantToken: str = None, KeyId: str = None, GrantId: str = None) -> None:
        """
        [Client.retire_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.retire_grant)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_grant(self, KeyId: str, GrantId: str) -> None:
        """
        [Client.revoke_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.revoke_grant)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def schedule_key_deletion(
        self, KeyId: str, PendingWindowInDays: int = None
    ) -> ClientScheduleKeyDeletionResponseTypeDef:
        """
        [Client.schedule_key_deletion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.schedule_key_deletion)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def sign(
        self,
        KeyId: str,
        Message: bytes,
        SigningAlgorithm: Literal[
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
        MessageType: Literal["RAW", "DIGEST"] = None,
        GrantTokens: List[str] = None,
    ) -> ClientSignResponseTypeDef:
        """
        [Client.sign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.sign)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, KeyId: str, Tags: List[ClientTagResourceTagsTypeDef]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, KeyId: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_alias(self, AliasName: str, TargetKeyId: str) -> None:
        """
        [Client.update_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.update_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_custom_key_store(
        self,
        CustomKeyStoreId: str,
        NewCustomKeyStoreName: str = None,
        KeyStorePassword: str = None,
        CloudHsmClusterId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.update_custom_key_store)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_key_description(self, KeyId: str, Description: str) -> None:
        """
        [Client.update_key_description documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.update_key_description)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def verify(
        self,
        KeyId: str,
        Message: bytes,
        Signature: bytes,
        SigningAlgorithm: Literal[
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
        MessageType: Literal["RAW", "DIGEST"] = None,
        GrantTokens: List[str] = None,
    ) -> ClientVerifyResponseTypeDef:
        """
        [Client.verify documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Client.verify)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aliases"]
    ) -> paginator_scope.ListAliasesPaginator:
        """
        [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Paginator.ListAliases)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_grants"]
    ) -> paginator_scope.ListGrantsPaginator:
        """
        [Paginator.ListGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Paginator.ListGrants)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_key_policies"]
    ) -> paginator_scope.ListKeyPoliciesPaginator:
        """
        [Paginator.ListKeyPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Paginator.ListKeyPolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_keys"]
    ) -> paginator_scope.ListKeysPaginator:
        """
        [Paginator.ListKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/kms.html#KMS.Paginator.ListKeys)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    CloudHsmClusterInUseException: Boto3ClientError
    CloudHsmClusterInvalidConfigurationException: Boto3ClientError
    CloudHsmClusterNotActiveException: Boto3ClientError
    CloudHsmClusterNotFoundException: Boto3ClientError
    CloudHsmClusterNotRelatedException: Boto3ClientError
    CustomKeyStoreHasCMKsException: Boto3ClientError
    CustomKeyStoreInvalidStateException: Boto3ClientError
    CustomKeyStoreNameInUseException: Boto3ClientError
    CustomKeyStoreNotFoundException: Boto3ClientError
    DependencyTimeoutException: Boto3ClientError
    DisabledException: Boto3ClientError
    ExpiredImportTokenException: Boto3ClientError
    IncorrectKeyException: Boto3ClientError
    IncorrectKeyMaterialException: Boto3ClientError
    IncorrectTrustAnchorException: Boto3ClientError
    InvalidAliasNameException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidCiphertextException: Boto3ClientError
    InvalidGrantIdException: Boto3ClientError
    InvalidGrantTokenException: Boto3ClientError
    InvalidImportTokenException: Boto3ClientError
    InvalidKeyUsageException: Boto3ClientError
    InvalidMarkerException: Boto3ClientError
    KMSInternalException: Boto3ClientError
    KMSInvalidStateException: Boto3ClientError
    KeyUnavailableException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MalformedPolicyDocumentException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TagException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError
