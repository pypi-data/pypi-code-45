"Main interface for mediaconnect service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddFlowOutputsOutputsEncryptionTypeDef",
    "ClientAddFlowOutputsOutputsTypeDef",
    "ClientAddFlowOutputsResponseOutputsEncryptionTypeDef",
    "ClientAddFlowOutputsResponseOutputsTransportTypeDef",
    "ClientAddFlowOutputsResponseOutputsTypeDef",
    "ClientAddFlowOutputsResponseTypeDef",
    "ClientCreateFlowEntitlementsEncryptionTypeDef",
    "ClientCreateFlowEntitlementsTypeDef",
    "ClientCreateFlowOutputsEncryptionTypeDef",
    "ClientCreateFlowOutputsTypeDef",
    "ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef",
    "ClientCreateFlowResponseFlowEntitlementsTypeDef",
    "ClientCreateFlowResponseFlowOutputsEncryptionTypeDef",
    "ClientCreateFlowResponseFlowOutputsTransportTypeDef",
    "ClientCreateFlowResponseFlowOutputsTypeDef",
    "ClientCreateFlowResponseFlowSourceDecryptionTypeDef",
    "ClientCreateFlowResponseFlowSourceTransportTypeDef",
    "ClientCreateFlowResponseFlowSourceTypeDef",
    "ClientCreateFlowResponseFlowTypeDef",
    "ClientCreateFlowResponseTypeDef",
    "ClientCreateFlowSourceDecryptionTypeDef",
    "ClientCreateFlowSourceTypeDef",
    "ClientDeleteFlowResponseTypeDef",
    "ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef",
    "ClientDescribeFlowResponseFlowEntitlementsTypeDef",
    "ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef",
    "ClientDescribeFlowResponseFlowOutputsTransportTypeDef",
    "ClientDescribeFlowResponseFlowOutputsTypeDef",
    "ClientDescribeFlowResponseFlowSourceDecryptionTypeDef",
    "ClientDescribeFlowResponseFlowSourceTransportTypeDef",
    "ClientDescribeFlowResponseFlowSourceTypeDef",
    "ClientDescribeFlowResponseFlowTypeDef",
    "ClientDescribeFlowResponseMessagesTypeDef",
    "ClientDescribeFlowResponseTypeDef",
    "ClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef",
    "ClientGrantFlowEntitlementsEntitlementsTypeDef",
    "ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef",
    "ClientGrantFlowEntitlementsResponseEntitlementsTypeDef",
    "ClientGrantFlowEntitlementsResponseTypeDef",
    "ClientListEntitlementsResponseEntitlementsTypeDef",
    "ClientListEntitlementsResponseTypeDef",
    "ClientListFlowsResponseFlowsTypeDef",
    "ClientListFlowsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRemoveFlowOutputResponseTypeDef",
    "ClientRevokeFlowEntitlementResponseTypeDef",
    "ClientStartFlowResponseTypeDef",
    "ClientStopFlowResponseTypeDef",
    "ClientUpdateFlowEntitlementEncryptionTypeDef",
    "ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef",
    "ClientUpdateFlowEntitlementResponseEntitlementTypeDef",
    "ClientUpdateFlowEntitlementResponseTypeDef",
    "ClientUpdateFlowOutputEncryptionTypeDef",
    "ClientUpdateFlowOutputResponseOutputEncryptionTypeDef",
    "ClientUpdateFlowOutputResponseOutputTransportTypeDef",
    "ClientUpdateFlowOutputResponseOutputTypeDef",
    "ClientUpdateFlowOutputResponseTypeDef",
    "ClientUpdateFlowSourceDecryptionTypeDef",
    "ClientUpdateFlowSourceResponseSourceDecryptionTypeDef",
    "ClientUpdateFlowSourceResponseSourceTransportTypeDef",
    "ClientUpdateFlowSourceResponseSourceTypeDef",
    "ClientUpdateFlowSourceResponseTypeDef",
    "ListEntitlementsPaginatePaginationConfigTypeDef",
    "ListEntitlementsPaginateResponseEntitlementsTypeDef",
    "ListEntitlementsPaginateResponseTypeDef",
    "ListFlowsPaginatePaginationConfigTypeDef",
    "ListFlowsPaginateResponseFlowsTypeDef",
    "ListFlowsPaginateResponseTypeDef",
)


_ClientAddFlowOutputsOutputsEncryptionTypeDef = TypedDict(
    "_ClientAddFlowOutputsOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientAddFlowOutputsOutputsEncryptionTypeDef(_ClientAddFlowOutputsOutputsEncryptionTypeDef):
    pass


_ClientAddFlowOutputsOutputsTypeDef = TypedDict(
    "_ClientAddFlowOutputsOutputsTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": ClientAddFlowOutputsOutputsEncryptionTypeDef,
        "MaxLatency": int,
        "Name": str,
        "Port": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientAddFlowOutputsOutputsTypeDef(_ClientAddFlowOutputsOutputsTypeDef):
    """
    - *(dict) --*The output that you want to add to this flow.

      - **CidrAllowList** *(list) --*The range of IP addresses that should be allowed to initiate
      output requests to this flow. These IP addresses should be in the form of a Classless
      Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        - *(string) --*
    """


_ClientAddFlowOutputsResponseOutputsEncryptionTypeDef = TypedDict(
    "_ClientAddFlowOutputsResponseOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientAddFlowOutputsResponseOutputsEncryptionTypeDef(
    _ClientAddFlowOutputsResponseOutputsEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*The type of key used for the encryption. If no keyType is provided,
    the service will use the default setting (static-key).

      - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
      aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
      AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientAddFlowOutputsResponseOutputsTransportTypeDef = TypedDict(
    "_ClientAddFlowOutputsResponseOutputsTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientAddFlowOutputsResponseOutputsTransportTypeDef(
    _ClientAddFlowOutputsResponseOutputsTransportTypeDef
):
    pass


_ClientAddFlowOutputsResponseOutputsTypeDef = TypedDict(
    "_ClientAddFlowOutputsResponseOutputsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": ClientAddFlowOutputsResponseOutputsEncryptionTypeDef,
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": ClientAddFlowOutputsResponseOutputsTransportTypeDef,
    },
    total=False,
)


class ClientAddFlowOutputsResponseOutputsTypeDef(_ClientAddFlowOutputsResponseOutputsTypeDef):
    """
    - *(dict) --*The settings for an output.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **Description** *(string) --*A description of the output.
      - **Destination** *(string) --*The address where you want to send the output.
      - **Encryption** *(dict) --*The type of key used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).

        - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
        aes128, aes192, or aes256).
        - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by
        a 32-character string, to be used with the key for encrypting content. This parameter is not
        valid for static key encryption.
        - **DeviceId** *(string) --*The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.
        - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).
        - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
        This parameter is required for SPEKE encryption and is not valid for static key encryption.
        - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
        the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
        - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).
        - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is not
        valid for SPEKE encryption.
        - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
    """


_ClientAddFlowOutputsResponseTypeDef = TypedDict(
    "_ClientAddFlowOutputsResponseTypeDef",
    {"FlowArn": str, "Outputs": List[ClientAddFlowOutputsResponseOutputsTypeDef]},
    total=False,
)


class ClientAddFlowOutputsResponseTypeDef(_ClientAddFlowOutputsResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect added the outputs successfully.

      - **FlowArn** *(string) --*The ARN of the flow that these outputs were added to.
      - **Outputs** *(list) --*The details of the newly added outputs.

        - *(dict) --*The settings for an output.

          - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.
          - **Description** *(string) --*A description of the output.
          - **Destination** *(string) --*The address where you want to send the output.
          - **Encryption** *(dict) --*The type of key used for the encryption. If no keyType is
          provided, the service will use the default setting (static-key).

            - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such
            as aes128, aes192, or aes256).
            - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented
            by a 32-character string, to be used with the key for encrypting content. This parameter
            is not valid for static key encryption.
            - **DeviceId** *(string) --*The value of one of the devices that you configured with
            your digital rights management (DRM) platform key provider. This parameter is required
            for SPEKE encryption and is not valid for static key encryption.
            - **KeyType** *(string) --*The type of key that is used for the encryption. If no
            keyType is provided, the service will use the default setting (static-key).
            - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created
            in. This parameter is required for SPEKE encryption and is not valid for static key
            encryption.
            - **ResourceId** *(string) --*An identifier for the content. The service sends this
            value to the key server to identify the current endpoint. The resource ID is also known
            as the content ID. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.
            - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you
            set up AWS Elemental MediaConnect as a trusted entity).
            - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets
            Manager to store the encryption key. This parameter is required for static key
            encryption and is not valid for SPEKE encryption.
            - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to
            your key server. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.
    """


_RequiredClientCreateFlowEntitlementsEncryptionTypeDef = TypedDict(
    "_RequiredClientCreateFlowEntitlementsEncryptionTypeDef",
    {"Algorithm": Literal["aes128", "aes192", "aes256"], "RoleArn": str},
)
_OptionalClientCreateFlowEntitlementsEncryptionTypeDef = TypedDict(
    "_OptionalClientCreateFlowEntitlementsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientCreateFlowEntitlementsEncryptionTypeDef(
    _RequiredClientCreateFlowEntitlementsEncryptionTypeDef,
    _OptionalClientCreateFlowEntitlementsEncryptionTypeDef,
):
    """
    - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --***[REQUIRED]** The type of algorithm that is used for the
      encryption (such as aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --***[REQUIRED]** The ARN of the role that you created during setup
      (when you set up AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientCreateFlowEntitlementsTypeDef = TypedDict(
    "_ClientCreateFlowEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientCreateFlowEntitlementsEncryptionTypeDef,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)


class ClientCreateFlowEntitlementsTypeDef(_ClientCreateFlowEntitlementsTypeDef):
    """
    - *(dict) --*The entitlements that you want to grant on a flow.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **Description** *(string) --*A description of the entitlement. This description appears only
      on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.
      - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
      associated with this entitlement.

        - **Algorithm** *(string) --***[REQUIRED]** The type of algorithm that is used for the
        encryption (such as aes128, aes192, or aes256).
        - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by
        a 32-character string, to be used with the key for encrypting content. This parameter is not
        valid for static key encryption.
        - **DeviceId** *(string) --*The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.
        - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).
        - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
        This parameter is required for SPEKE encryption and is not valid for static key encryption.
        - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
        the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
        - **RoleArn** *(string) --***[REQUIRED]** The ARN of the role that you created during setup
        (when you set up AWS Elemental MediaConnect as a trusted entity).
        - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is not
        valid for SPEKE encryption.
        - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
    """


_ClientCreateFlowOutputsEncryptionTypeDef = TypedDict(
    "_ClientCreateFlowOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientCreateFlowOutputsEncryptionTypeDef(_ClientCreateFlowOutputsEncryptionTypeDef):
    pass


_ClientCreateFlowOutputsTypeDef = TypedDict(
    "_ClientCreateFlowOutputsTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": ClientCreateFlowOutputsEncryptionTypeDef,
        "MaxLatency": int,
        "Name": str,
        "Port": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientCreateFlowOutputsTypeDef(_ClientCreateFlowOutputsTypeDef):
    """
    - *(dict) --*The output that you want to add to this flow.

      - **CidrAllowList** *(list) --*The range of IP addresses that should be allowed to initiate
      output requests to this flow. These IP addresses should be in the form of a Classless
      Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        - *(string) --*
    """


_ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef(
    _ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
      aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
      AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientCreateFlowResponseFlowEntitlementsTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientCreateFlowResponseFlowEntitlementsEncryptionTypeDef,
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)


class ClientCreateFlowResponseFlowEntitlementsTypeDef(
    _ClientCreateFlowResponseFlowEntitlementsTypeDef
):
    """
    - *(dict) --*The settings for a flow entitlement.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **Description** *(string) --*A description of the entitlement.
      - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
      associated with this entitlement.

        - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
        aes128, aes192, or aes256).
        - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by
        a 32-character string, to be used with the key for encrypting content. This parameter is not
        valid for static key encryption.
        - **DeviceId** *(string) --*The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.
        - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).
        - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
        This parameter is required for SPEKE encryption and is not valid for static key encryption.
        - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
        the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
        - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).
        - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is not
        valid for SPEKE encryption.
        - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
    """


_ClientCreateFlowResponseFlowOutputsEncryptionTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientCreateFlowResponseFlowOutputsEncryptionTypeDef(
    _ClientCreateFlowResponseFlowOutputsEncryptionTypeDef
):
    pass


_ClientCreateFlowResponseFlowOutputsTransportTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowOutputsTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientCreateFlowResponseFlowOutputsTransportTypeDef(
    _ClientCreateFlowResponseFlowOutputsTransportTypeDef
):
    pass


_ClientCreateFlowResponseFlowOutputsTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowOutputsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": ClientCreateFlowResponseFlowOutputsEncryptionTypeDef,
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": ClientCreateFlowResponseFlowOutputsTransportTypeDef,
    },
    total=False,
)


class ClientCreateFlowResponseFlowOutputsTypeDef(_ClientCreateFlowResponseFlowOutputsTypeDef):
    pass


_ClientCreateFlowResponseFlowSourceDecryptionTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowSourceDecryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientCreateFlowResponseFlowSourceDecryptionTypeDef(
    _ClientCreateFlowResponseFlowSourceDecryptionTypeDef
):
    pass


_ClientCreateFlowResponseFlowSourceTransportTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowSourceTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientCreateFlowResponseFlowSourceTransportTypeDef(
    _ClientCreateFlowResponseFlowSourceTransportTypeDef
):
    pass


_ClientCreateFlowResponseFlowSourceTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": ClientCreateFlowResponseFlowSourceDecryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Name": str,
        "SourceArn": str,
        "Transport": ClientCreateFlowResponseFlowSourceTransportTypeDef,
        "WhitelistCidr": str,
    },
    total=False,
)


class ClientCreateFlowResponseFlowSourceTypeDef(_ClientCreateFlowResponseFlowSourceTypeDef):
    pass


_ClientCreateFlowResponseFlowTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "EgressIp": str,
        "Entitlements": List[ClientCreateFlowResponseFlowEntitlementsTypeDef],
        "FlowArn": str,
        "Name": str,
        "Outputs": List[ClientCreateFlowResponseFlowOutputsTypeDef],
        "Source": ClientCreateFlowResponseFlowSourceTypeDef,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)


class ClientCreateFlowResponseFlowTypeDef(_ClientCreateFlowResponseFlowTypeDef):
    """
    - **Flow** *(dict) --*The settings for a flow, including its source, outputs, and entitlements.

      - **AvailabilityZone** *(string) --*The Availability Zone that you want to create the flow in.
      These options are limited to the Availability Zones within the current AWS.
      - **Description** *(string) --*A description of the flow. This value is not used or seen
      outside of the current AWS Elemental MediaConnect account.
      - **EgressIp** *(string) --*The IP address from which video will be sent to output
      destinations.
      - **Entitlements** *(list) --*The entitlements in this flow.

        - *(dict) --*The settings for a flow entitlement.

          - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.
          - **Description** *(string) --*A description of the entitlement.
          - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
          associated with this entitlement.

            - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such
            as aes128, aes192, or aes256).
            - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented
            by a 32-character string, to be used with the key for encrypting content. This parameter
            is not valid for static key encryption.
            - **DeviceId** *(string) --*The value of one of the devices that you configured with
            your digital rights management (DRM) platform key provider. This parameter is required
            for SPEKE encryption and is not valid for static key encryption.
            - **KeyType** *(string) --*The type of key that is used for the encryption. If no
            keyType is provided, the service will use the default setting (static-key).
            - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created
            in. This parameter is required for SPEKE encryption and is not valid for static key
            encryption.
            - **ResourceId** *(string) --*An identifier for the content. The service sends this
            value to the key server to identify the current endpoint. The resource ID is also known
            as the content ID. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.
            - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you
            set up AWS Elemental MediaConnect as a trusted entity).
            - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets
            Manager to store the encryption key. This parameter is required for static key
            encryption and is not valid for SPEKE encryption.
            - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to
            your key server. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.
    """


_ClientCreateFlowResponseTypeDef = TypedDict(
    "_ClientCreateFlowResponseTypeDef", {"Flow": ClientCreateFlowResponseFlowTypeDef}, total=False
)


class ClientCreateFlowResponseTypeDef(_ClientCreateFlowResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect created the new flow successfully.

      - **Flow** *(dict) --*The settings for a flow, including its source, outputs, and
      entitlements.

        - **AvailabilityZone** *(string) --*The Availability Zone that you want to create the flow
        in. These options are limited to the Availability Zones within the current AWS.
        - **Description** *(string) --*A description of the flow. This value is not used or seen
        outside of the current AWS Elemental MediaConnect account.
        - **EgressIp** *(string) --*The IP address from which video will be sent to output
        destinations.
        - **Entitlements** *(list) --*The entitlements in this flow.

          - *(dict) --*The settings for a flow entitlement.

            - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
            transfer cost to be billed to the subscriber.
            - **Description** *(string) --*A description of the entitlement.
            - **Encryption** *(dict) --*The type of encryption that will be used on the output that
            is associated with this entitlement.

              - **Algorithm** *(string) --*The type of algorithm that is used for the encryption
              (such as aes128, aes192, or aes256).
              - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value
              represented by a 32-character string, to be used with the key for encrypting content.
              This parameter is not valid for static key encryption.
              - **DeviceId** *(string) --*The value of one of the devices that you configured with
              your digital rights management (DRM) platform key provider. This parameter is required
              for SPEKE encryption and is not valid for static key encryption.
              - **KeyType** *(string) --*The type of key that is used for the encryption. If no
              keyType is provided, the service will use the default setting (static-key).
              - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was
              created in. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.
              - **ResourceId** *(string) --*An identifier for the content. The service sends this
              value to the key server to identify the current endpoint. The resource ID is also
              known as the content ID. This parameter is required for SPEKE encryption and is not
              valid for static key encryption.
              - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you
              set up AWS Elemental MediaConnect as a trusted entity).
              - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets
              Manager to store the encryption key. This parameter is required for static key
              encryption and is not valid for SPEKE encryption.
              - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to
              your key server. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.
    """


_RequiredClientCreateFlowSourceDecryptionTypeDef = TypedDict(
    "_RequiredClientCreateFlowSourceDecryptionTypeDef",
    {"Algorithm": Literal["aes128", "aes192", "aes256"], "RoleArn": str},
)
_OptionalClientCreateFlowSourceDecryptionTypeDef = TypedDict(
    "_OptionalClientCreateFlowSourceDecryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientCreateFlowSourceDecryptionTypeDef(
    _RequiredClientCreateFlowSourceDecryptionTypeDef,
    _OptionalClientCreateFlowSourceDecryptionTypeDef,
):
    """
    - **Decryption** *(dict) --*The type of encryption that is used on the content ingested from
    this source.

      - **Algorithm** *(string) --***[REQUIRED]** The type of algorithm that is used for the
      encryption (such as aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --***[REQUIRED]** The ARN of the role that you created during setup
      (when you set up AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientCreateFlowSourceTypeDef = TypedDict(
    "_ClientCreateFlowSourceTypeDef",
    {
        "Decryption": ClientCreateFlowSourceDecryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "Name": str,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "StreamId": str,
        "WhitelistCidr": str,
    },
    total=False,
)


class ClientCreateFlowSourceTypeDef(_ClientCreateFlowSourceTypeDef):
    """
    - **Decryption** *(dict) --*The type of encryption that is used on the content ingested from
    this source.

      - **Algorithm** *(string) --***[REQUIRED]** The type of algorithm that is used for the
      encryption (such as aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --***[REQUIRED]** The ARN of the role that you created during setup
      (when you set up AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientDeleteFlowResponseTypeDef = TypedDict(
    "_ClientDeleteFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)


class ClientDeleteFlowResponseTypeDef(_ClientDeleteFlowResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect is deleting the flow.

      - **FlowArn** *(string) --*The ARN of the flow that was deleted.
      - **Status** *(string) --*The status of the flow when the DeleteFlow process begins.
    """


_ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef(
    _ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
      aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
      AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientDescribeFlowResponseFlowEntitlementsTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientDescribeFlowResponseFlowEntitlementsEncryptionTypeDef,
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)


class ClientDescribeFlowResponseFlowEntitlementsTypeDef(
    _ClientDescribeFlowResponseFlowEntitlementsTypeDef
):
    """
    - *(dict) --*The settings for a flow entitlement.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **Description** *(string) --*A description of the entitlement.
      - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
      associated with this entitlement.

        - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
        aes128, aes192, or aes256).
        - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by
        a 32-character string, to be used with the key for encrypting content. This parameter is not
        valid for static key encryption.
        - **DeviceId** *(string) --*The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.
        - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).
        - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
        This parameter is required for SPEKE encryption and is not valid for static key encryption.
        - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
        the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
        - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).
        - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is not
        valid for SPEKE encryption.
        - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
    """


_ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef(
    _ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef
):
    pass


_ClientDescribeFlowResponseFlowOutputsTransportTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowOutputsTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientDescribeFlowResponseFlowOutputsTransportTypeDef(
    _ClientDescribeFlowResponseFlowOutputsTransportTypeDef
):
    pass


_ClientDescribeFlowResponseFlowOutputsTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowOutputsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": ClientDescribeFlowResponseFlowOutputsEncryptionTypeDef,
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": ClientDescribeFlowResponseFlowOutputsTransportTypeDef,
    },
    total=False,
)


class ClientDescribeFlowResponseFlowOutputsTypeDef(_ClientDescribeFlowResponseFlowOutputsTypeDef):
    pass


_ClientDescribeFlowResponseFlowSourceDecryptionTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowSourceDecryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientDescribeFlowResponseFlowSourceDecryptionTypeDef(
    _ClientDescribeFlowResponseFlowSourceDecryptionTypeDef
):
    pass


_ClientDescribeFlowResponseFlowSourceTransportTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowSourceTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientDescribeFlowResponseFlowSourceTransportTypeDef(
    _ClientDescribeFlowResponseFlowSourceTransportTypeDef
):
    pass


_ClientDescribeFlowResponseFlowSourceTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": ClientDescribeFlowResponseFlowSourceDecryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Name": str,
        "SourceArn": str,
        "Transport": ClientDescribeFlowResponseFlowSourceTransportTypeDef,
        "WhitelistCidr": str,
    },
    total=False,
)


class ClientDescribeFlowResponseFlowSourceTypeDef(_ClientDescribeFlowResponseFlowSourceTypeDef):
    pass


_ClientDescribeFlowResponseFlowTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "EgressIp": str,
        "Entitlements": List[ClientDescribeFlowResponseFlowEntitlementsTypeDef],
        "FlowArn": str,
        "Name": str,
        "Outputs": List[ClientDescribeFlowResponseFlowOutputsTypeDef],
        "Source": ClientDescribeFlowResponseFlowSourceTypeDef,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)


class ClientDescribeFlowResponseFlowTypeDef(_ClientDescribeFlowResponseFlowTypeDef):
    """
    - **Flow** *(dict) --*The settings for a flow, including its source, outputs, and entitlements.

      - **AvailabilityZone** *(string) --*The Availability Zone that you want to create the flow in.
      These options are limited to the Availability Zones within the current AWS.
      - **Description** *(string) --*A description of the flow. This value is not used or seen
      outside of the current AWS Elemental MediaConnect account.
      - **EgressIp** *(string) --*The IP address from which video will be sent to output
      destinations.
      - **Entitlements** *(list) --*The entitlements in this flow.

        - *(dict) --*The settings for a flow entitlement.

          - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.
          - **Description** *(string) --*A description of the entitlement.
          - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
          associated with this entitlement.

            - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such
            as aes128, aes192, or aes256).
            - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented
            by a 32-character string, to be used with the key for encrypting content. This parameter
            is not valid for static key encryption.
            - **DeviceId** *(string) --*The value of one of the devices that you configured with
            your digital rights management (DRM) platform key provider. This parameter is required
            for SPEKE encryption and is not valid for static key encryption.
            - **KeyType** *(string) --*The type of key that is used for the encryption. If no
            keyType is provided, the service will use the default setting (static-key).
            - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created
            in. This parameter is required for SPEKE encryption and is not valid for static key
            encryption.
            - **ResourceId** *(string) --*An identifier for the content. The service sends this
            value to the key server to identify the current endpoint. The resource ID is also known
            as the content ID. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.
            - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you
            set up AWS Elemental MediaConnect as a trusted entity).
            - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets
            Manager to store the encryption key. This parameter is required for static key
            encryption and is not valid for SPEKE encryption.
            - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to
            your key server. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.
    """


_ClientDescribeFlowResponseMessagesTypeDef = TypedDict(
    "_ClientDescribeFlowResponseMessagesTypeDef", {"Errors": List[str]}, total=False
)


class ClientDescribeFlowResponseMessagesTypeDef(_ClientDescribeFlowResponseMessagesTypeDef):
    pass


_ClientDescribeFlowResponseTypeDef = TypedDict(
    "_ClientDescribeFlowResponseTypeDef",
    {
        "Flow": ClientDescribeFlowResponseFlowTypeDef,
        "Messages": ClientDescribeFlowResponseMessagesTypeDef,
    },
    total=False,
)


class ClientDescribeFlowResponseTypeDef(_ClientDescribeFlowResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect returned the flow details successfully.

      - **Flow** *(dict) --*The settings for a flow, including its source, outputs, and
      entitlements.

        - **AvailabilityZone** *(string) --*The Availability Zone that you want to create the flow
        in. These options are limited to the Availability Zones within the current AWS.
        - **Description** *(string) --*A description of the flow. This value is not used or seen
        outside of the current AWS Elemental MediaConnect account.
        - **EgressIp** *(string) --*The IP address from which video will be sent to output
        destinations.
        - **Entitlements** *(list) --*The entitlements in this flow.

          - *(dict) --*The settings for a flow entitlement.

            - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
            transfer cost to be billed to the subscriber.
            - **Description** *(string) --*A description of the entitlement.
            - **Encryption** *(dict) --*The type of encryption that will be used on the output that
            is associated with this entitlement.

              - **Algorithm** *(string) --*The type of algorithm that is used for the encryption
              (such as aes128, aes192, or aes256).
              - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value
              represented by a 32-character string, to be used with the key for encrypting content.
              This parameter is not valid for static key encryption.
              - **DeviceId** *(string) --*The value of one of the devices that you configured with
              your digital rights management (DRM) platform key provider. This parameter is required
              for SPEKE encryption and is not valid for static key encryption.
              - **KeyType** *(string) --*The type of key that is used for the encryption. If no
              keyType is provided, the service will use the default setting (static-key).
              - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was
              created in. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.
              - **ResourceId** *(string) --*An identifier for the content. The service sends this
              value to the key server to identify the current endpoint. The resource ID is also
              known as the content ID. This parameter is required for SPEKE encryption and is not
              valid for static key encryption.
              - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you
              set up AWS Elemental MediaConnect as a trusted entity).
              - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets
              Manager to store the encryption key. This parameter is required for static key
              encryption and is not valid for SPEKE encryption.
              - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to
              your key server. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.
    """


_RequiredClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef = TypedDict(
    "_RequiredClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef",
    {"Algorithm": Literal["aes128", "aes192", "aes256"], "RoleArn": str},
)
_OptionalClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef = TypedDict(
    "_OptionalClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef(
    _RequiredClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef,
    _OptionalClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef,
):
    """
    - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --***[REQUIRED]** The type of algorithm that is used for the
      encryption (such as aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --***[REQUIRED]** The ARN of the role that you created during setup
      (when you set up AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientGrantFlowEntitlementsEntitlementsTypeDef = TypedDict(
    "_ClientGrantFlowEntitlementsEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientGrantFlowEntitlementsEntitlementsEncryptionTypeDef,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)


class ClientGrantFlowEntitlementsEntitlementsTypeDef(
    _ClientGrantFlowEntitlementsEntitlementsTypeDef
):
    """
    - *(dict) --*The entitlements that you want to grant on a flow.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **Description** *(string) --*A description of the entitlement. This description appears only
      on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.
      - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
      associated with this entitlement.

        - **Algorithm** *(string) --***[REQUIRED]** The type of algorithm that is used for the
        encryption (such as aes128, aes192, or aes256).
        - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by
        a 32-character string, to be used with the key for encrypting content. This parameter is not
        valid for static key encryption.
        - **DeviceId** *(string) --*The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.
        - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).
        - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
        This parameter is required for SPEKE encryption and is not valid for static key encryption.
        - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
        the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
        - **RoleArn** *(string) --***[REQUIRED]** The ARN of the role that you created during setup
        (when you set up AWS Elemental MediaConnect as a trusted entity).
        - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is not
        valid for SPEKE encryption.
        - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
    """


_ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef = TypedDict(
    "_ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef(
    _ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
      aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
      AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientGrantFlowEntitlementsResponseEntitlementsTypeDef = TypedDict(
    "_ClientGrantFlowEntitlementsResponseEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientGrantFlowEntitlementsResponseEntitlementsEncryptionTypeDef,
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)


class ClientGrantFlowEntitlementsResponseEntitlementsTypeDef(
    _ClientGrantFlowEntitlementsResponseEntitlementsTypeDef
):
    """
    - *(dict) --*The settings for a flow entitlement.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **Description** *(string) --*A description of the entitlement.
      - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
      associated with this entitlement.

        - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
        aes128, aes192, or aes256).
        - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by
        a 32-character string, to be used with the key for encrypting content. This parameter is not
        valid for static key encryption.
        - **DeviceId** *(string) --*The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.
        - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).
        - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
        This parameter is required for SPEKE encryption and is not valid for static key encryption.
        - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
        the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
        - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).
        - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is not
        valid for SPEKE encryption.
        - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
    """


_ClientGrantFlowEntitlementsResponseTypeDef = TypedDict(
    "_ClientGrantFlowEntitlementsResponseTypeDef",
    {"Entitlements": List[ClientGrantFlowEntitlementsResponseEntitlementsTypeDef], "FlowArn": str},
    total=False,
)


class ClientGrantFlowEntitlementsResponseTypeDef(_ClientGrantFlowEntitlementsResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect granted the entitlements successfully.

      - **Entitlements** *(list) --*The entitlements that were just granted.

        - *(dict) --*The settings for a flow entitlement.

          - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.
          - **Description** *(string) --*A description of the entitlement.
          - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
          associated with this entitlement.

            - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such
            as aes128, aes192, or aes256).
            - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented
            by a 32-character string, to be used with the key for encrypting content. This parameter
            is not valid for static key encryption.
            - **DeviceId** *(string) --*The value of one of the devices that you configured with
            your digital rights management (DRM) platform key provider. This parameter is required
            for SPEKE encryption and is not valid for static key encryption.
            - **KeyType** *(string) --*The type of key that is used for the encryption. If no
            keyType is provided, the service will use the default setting (static-key).
            - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created
            in. This parameter is required for SPEKE encryption and is not valid for static key
            encryption.
            - **ResourceId** *(string) --*An identifier for the content. The service sends this
            value to the key server to identify the current endpoint. The resource ID is also known
            as the content ID. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.
            - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you
            set up AWS Elemental MediaConnect as a trusted entity).
            - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets
            Manager to store the encryption key. This parameter is required for static key
            encryption and is not valid for SPEKE encryption.
            - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to
            your key server. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.
    """


_ClientListEntitlementsResponseEntitlementsTypeDef = TypedDict(
    "_ClientListEntitlementsResponseEntitlementsTypeDef",
    {"DataTransferSubscriberFeePercent": int, "EntitlementArn": str, "EntitlementName": str},
    total=False,
)


class ClientListEntitlementsResponseEntitlementsTypeDef(
    _ClientListEntitlementsResponseEntitlementsTypeDef
):
    """
    - *(dict) --*An entitlement that has been granted to you from other AWS accounts.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **EntitlementArn** *(string) --*The ARN of the entitlement.
      - **EntitlementName** *(string) --*The name of the entitlement.
    """


_ClientListEntitlementsResponseTypeDef = TypedDict(
    "_ClientListEntitlementsResponseTypeDef",
    {"Entitlements": List[ClientListEntitlementsResponseEntitlementsTypeDef], "NextToken": str},
    total=False,
)


class ClientListEntitlementsResponseTypeDef(_ClientListEntitlementsResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect returned the list of entitlements successfully.

      - **Entitlements** *(list) --*A list of entitlements that have been granted to you from other
      AWS accounts.

        - *(dict) --*An entitlement that has been granted to you from other AWS accounts.

          - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.
          - **EntitlementArn** *(string) --*The ARN of the entitlement.
          - **EntitlementName** *(string) --*The name of the entitlement.
    """


_ClientListFlowsResponseFlowsTypeDef = TypedDict(
    "_ClientListFlowsResponseFlowsTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": Literal["OWNED", "ENTITLED"],
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)


class ClientListFlowsResponseFlowsTypeDef(_ClientListFlowsResponseFlowsTypeDef):
    """
    - *(dict) --*Provides a summary of a flow, including its ARN, Availability Zone, and source
    type.

      - **AvailabilityZone** *(string) --*The Availability Zone that the flow was created in.
      - **Description** *(string) --*A description of the flow.
      - **FlowArn** *(string) --*The ARN of the flow.
      - **Name** *(string) --*The name of the flow.
      - **SourceType** *(string) --*The type of source. This value is either owned (originated
      somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or
      entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).
      - **Status** *(string) --*The current status of the flow.
    """


_ClientListFlowsResponseTypeDef = TypedDict(
    "_ClientListFlowsResponseTypeDef",
    {"Flows": List[ClientListFlowsResponseFlowsTypeDef], "NextToken": str},
    total=False,
)


class ClientListFlowsResponseTypeDef(_ClientListFlowsResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect returned the list of flows successfully.

      - **Flows** *(list) --*A list of flow summaries.

        - *(dict) --*Provides a summary of a flow, including its ARN, Availability Zone, and source
        type.

          - **AvailabilityZone** *(string) --*The Availability Zone that the flow was created in.
          - **Description** *(string) --*A description of the flow.
          - **FlowArn** *(string) --*The ARN of the flow.
          - **Name** *(string) --*The name of the flow.
          - **SourceType** *(string) --*The type of source. This value is either owned (originated
          somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or
          entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).
          - **Status** *(string) --*The current status of the flow.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*The tags for the resource

      - **Tags** *(dict) --*A map from tag keys to values. Tag keys can have a maximum character
      length of 128 characters, and tag values can have a maximum length of 256 characters.

        - *(string) --*

          - *(string) --*
    """


_ClientRemoveFlowOutputResponseTypeDef = TypedDict(
    "_ClientRemoveFlowOutputResponseTypeDef", {"FlowArn": str, "OutputArn": str}, total=False
)


class ClientRemoveFlowOutputResponseTypeDef(_ClientRemoveFlowOutputResponseTypeDef):
    """
    - *(dict) --*output successfully removed from flow configuration.

      - **FlowArn** *(string) --*The ARN of the flow that is associated with the output you removed.
      - **OutputArn** *(string) --*The ARN of the output that was removed.
    """


_ClientRevokeFlowEntitlementResponseTypeDef = TypedDict(
    "_ClientRevokeFlowEntitlementResponseTypeDef",
    {"EntitlementArn": str, "FlowArn": str},
    total=False,
)


class ClientRevokeFlowEntitlementResponseTypeDef(_ClientRevokeFlowEntitlementResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect revoked the entitlement successfully.

      - **EntitlementArn** *(string) --*The ARN of the entitlement that was revoked.
      - **FlowArn** *(string) --*The ARN of the flow that the entitlement was revoked from.
    """


_ClientStartFlowResponseTypeDef = TypedDict(
    "_ClientStartFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)


class ClientStartFlowResponseTypeDef(_ClientStartFlowResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect is starting the flow.

      - **FlowArn** *(string) --*The ARN of the flow that you started.
      - **Status** *(string) --*The status of the flow when the StartFlow process begins.
    """


_ClientStopFlowResponseTypeDef = TypedDict(
    "_ClientStopFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)


class ClientStopFlowResponseTypeDef(_ClientStopFlowResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect is stopping the flow.

      - **FlowArn** *(string) --*The ARN of the flow that you stopped.
      - **Status** *(string) --*The status of the flow when the StopFlow process begins.
    """


_ClientUpdateFlowEntitlementEncryptionTypeDef = TypedDict(
    "_ClientUpdateFlowEntitlementEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientUpdateFlowEntitlementEncryptionTypeDef(_ClientUpdateFlowEntitlementEncryptionTypeDef):
    """
    - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
    aes128, aes192, or aes256).
    - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
    32-character string, to be used with the key for encrypting content. This parameter is not valid
    for static key encryption.
    - **DeviceId** *(string) --*The value of one of the devices that you configured with your
    digital rights management (DRM) platform key provider. This parameter is required for SPEKE
    encryption and is not valid for static key encryption.
    - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).
    - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
    This parameter is required for SPEKE encryption and is not valid for static key encryption.
    - **ResourceId** *(string) --*An identifier for the content. The service sends this value to the
    key server to identify the current endpoint. The resource ID is also known as the content ID.
    This parameter is required for SPEKE encryption and is not valid for static key encryption.
    - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
    AWS Elemental MediaConnect as a trusted entity).
    - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
    store the encryption key. This parameter is required for static key encryption and is not valid
    for SPEKE encryption.
    - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
    server. This parameter is required for SPEKE encryption and is not valid for static key
    encryption.
    """


_ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef = TypedDict(
    "_ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef(
    _ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
      aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
      AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientUpdateFlowEntitlementResponseEntitlementTypeDef = TypedDict(
    "_ClientUpdateFlowEntitlementResponseEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": ClientUpdateFlowEntitlementResponseEntitlementEncryptionTypeDef,
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
    total=False,
)


class ClientUpdateFlowEntitlementResponseEntitlementTypeDef(
    _ClientUpdateFlowEntitlementResponseEntitlementTypeDef
):
    """
    - **Entitlement** *(dict) --*The settings for a flow entitlement.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **Description** *(string) --*A description of the entitlement.
      - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
      associated with this entitlement.

        - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
        aes128, aes192, or aes256).
        - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by
        a 32-character string, to be used with the key for encrypting content. This parameter is not
        valid for static key encryption.
        - **DeviceId** *(string) --*The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.
        - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).
        - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
        This parameter is required for SPEKE encryption and is not valid for static key encryption.
        - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
        the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
        - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).
        - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is not
        valid for SPEKE encryption.
        - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
    """


_ClientUpdateFlowEntitlementResponseTypeDef = TypedDict(
    "_ClientUpdateFlowEntitlementResponseTypeDef",
    {"Entitlement": ClientUpdateFlowEntitlementResponseEntitlementTypeDef, "FlowArn": str},
    total=False,
)


class ClientUpdateFlowEntitlementResponseTypeDef(_ClientUpdateFlowEntitlementResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect updated the entitlement successfully.

      - **Entitlement** *(dict) --*The settings for a flow entitlement.

        - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.
        - **Description** *(string) --*A description of the entitlement.
        - **Encryption** *(dict) --*The type of encryption that will be used on the output that is
        associated with this entitlement.

          - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).
          - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.
          - **DeviceId** *(string) --*The value of one of the devices that you configured with your
          digital rights management (DRM) platform key provider. This parameter is required for
          SPEKE encryption and is not valid for static key encryption.
          - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType
          is provided, the service will use the default setting (static-key).
          - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.
          - **ResourceId** *(string) --*An identifier for the content. The service sends this value
          to the key server to identify the current endpoint. The resource ID is also known as the
          content ID. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.
          - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
          up AWS Elemental MediaConnect as a trusted entity).
          - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
          to store the encryption key. This parameter is required for static key encryption and is
          not valid for SPEKE encryption.
          - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
          key server. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.
    """


_ClientUpdateFlowOutputEncryptionTypeDef = TypedDict(
    "_ClientUpdateFlowOutputEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientUpdateFlowOutputEncryptionTypeDef(_ClientUpdateFlowOutputEncryptionTypeDef):
    """
    - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
    aes128, aes192, or aes256).
    - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
    32-character string, to be used with the key for encrypting content. This parameter is not valid
    for static key encryption.
    - **DeviceId** *(string) --*The value of one of the devices that you configured with your
    digital rights management (DRM) platform key provider. This parameter is required for SPEKE
    encryption and is not valid for static key encryption.
    - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).
    - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
    This parameter is required for SPEKE encryption and is not valid for static key encryption.
    - **ResourceId** *(string) --*An identifier for the content. The service sends this value to the
    key server to identify the current endpoint. The resource ID is also known as the content ID.
    This parameter is required for SPEKE encryption and is not valid for static key encryption.
    - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
    AWS Elemental MediaConnect as a trusted entity).
    - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
    store the encryption key. This parameter is required for static key encryption and is not valid
    for SPEKE encryption.
    - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
    server. This parameter is required for SPEKE encryption and is not valid for static key
    encryption.
    """


_ClientUpdateFlowOutputResponseOutputEncryptionTypeDef = TypedDict(
    "_ClientUpdateFlowOutputResponseOutputEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientUpdateFlowOutputResponseOutputEncryptionTypeDef(
    _ClientUpdateFlowOutputResponseOutputEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*The type of key used for the encryption. If no keyType is provided,
    the service will use the default setting (static-key).

      - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
      aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
      AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientUpdateFlowOutputResponseOutputTransportTypeDef = TypedDict(
    "_ClientUpdateFlowOutputResponseOutputTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientUpdateFlowOutputResponseOutputTransportTypeDef(
    _ClientUpdateFlowOutputResponseOutputTransportTypeDef
):
    pass


_ClientUpdateFlowOutputResponseOutputTypeDef = TypedDict(
    "_ClientUpdateFlowOutputResponseOutputTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": ClientUpdateFlowOutputResponseOutputEncryptionTypeDef,
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": ClientUpdateFlowOutputResponseOutputTransportTypeDef,
    },
    total=False,
)


class ClientUpdateFlowOutputResponseOutputTypeDef(_ClientUpdateFlowOutputResponseOutputTypeDef):
    """
    - **Output** *(dict) --*The settings for an output.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **Description** *(string) --*A description of the output.
      - **Destination** *(string) --*The address where you want to send the output.
      - **Encryption** *(dict) --*The type of key used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).

        - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
        aes128, aes192, or aes256).
        - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by
        a 32-character string, to be used with the key for encrypting content. This parameter is not
        valid for static key encryption.
        - **DeviceId** *(string) --*The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.
        - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).
        - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
        This parameter is required for SPEKE encryption and is not valid for static key encryption.
        - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
        the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
        - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).
        - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is not
        valid for SPEKE encryption.
        - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
    """


_ClientUpdateFlowOutputResponseTypeDef = TypedDict(
    "_ClientUpdateFlowOutputResponseTypeDef",
    {"FlowArn": str, "Output": ClientUpdateFlowOutputResponseOutputTypeDef},
    total=False,
)


class ClientUpdateFlowOutputResponseTypeDef(_ClientUpdateFlowOutputResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect updated the output successfully.

      - **FlowArn** *(string) --*The ARN of the flow that is associated with the updated output.
      - **Output** *(dict) --*The settings for an output.

        - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.
        - **Description** *(string) --*A description of the output.
        - **Destination** *(string) --*The address where you want to send the output.
        - **Encryption** *(dict) --*The type of key used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).

          - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).
          - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.
          - **DeviceId** *(string) --*The value of one of the devices that you configured with your
          digital rights management (DRM) platform key provider. This parameter is required for
          SPEKE encryption and is not valid for static key encryption.
          - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType
          is provided, the service will use the default setting (static-key).
          - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.
          - **ResourceId** *(string) --*An identifier for the content. The service sends this value
          to the key server to identify the current endpoint. The resource ID is also known as the
          content ID. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.
          - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
          up AWS Elemental MediaConnect as a trusted entity).
          - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
          to store the encryption key. This parameter is required for static key encryption and is
          not valid for SPEKE encryption.
          - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
          key server. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.
    """


_ClientUpdateFlowSourceDecryptionTypeDef = TypedDict(
    "_ClientUpdateFlowSourceDecryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientUpdateFlowSourceDecryptionTypeDef(_ClientUpdateFlowSourceDecryptionTypeDef):
    """
    - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
    aes128, aes192, or aes256).
    - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
    32-character string, to be used with the key for encrypting content. This parameter is not valid
    for static key encryption.
    - **DeviceId** *(string) --*The value of one of the devices that you configured with your
    digital rights management (DRM) platform key provider. This parameter is required for SPEKE
    encryption and is not valid for static key encryption.
    - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).
    - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
    This parameter is required for SPEKE encryption and is not valid for static key encryption.
    - **ResourceId** *(string) --*An identifier for the content. The service sends this value to the
    key server to identify the current endpoint. The resource ID is also known as the content ID.
    This parameter is required for SPEKE encryption and is not valid for static key encryption.
    - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
    AWS Elemental MediaConnect as a trusted entity).
    - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
    store the encryption key. This parameter is required for static key encryption and is not valid
    for SPEKE encryption.
    - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
    server. This parameter is required for SPEKE encryption and is not valid for static key
    encryption.
    """


_ClientUpdateFlowSourceResponseSourceDecryptionTypeDef = TypedDict(
    "_ClientUpdateFlowSourceResponseSourceDecryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientUpdateFlowSourceResponseSourceDecryptionTypeDef(
    _ClientUpdateFlowSourceResponseSourceDecryptionTypeDef
):
    """
    - **Decryption** *(dict) --*The type of encryption that is used on the content ingested from
    this source.

      - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
      aes128, aes192, or aes256).
      - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.
      - **DeviceId** *(string) --*The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.
      - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).
      - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.
      - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
      - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set up
      AWS Elemental MediaConnect as a trusted entity).
      - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.
      - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.
    """


_ClientUpdateFlowSourceResponseSourceTransportTypeDef = TypedDict(
    "_ClientUpdateFlowSourceResponseSourceTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientUpdateFlowSourceResponseSourceTransportTypeDef(
    _ClientUpdateFlowSourceResponseSourceTransportTypeDef
):
    pass


_ClientUpdateFlowSourceResponseSourceTypeDef = TypedDict(
    "_ClientUpdateFlowSourceResponseSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": ClientUpdateFlowSourceResponseSourceDecryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Name": str,
        "SourceArn": str,
        "Transport": ClientUpdateFlowSourceResponseSourceTransportTypeDef,
        "WhitelistCidr": str,
    },
    total=False,
)


class ClientUpdateFlowSourceResponseSourceTypeDef(_ClientUpdateFlowSourceResponseSourceTypeDef):
    """
    - **Source** *(dict) --*The settings for the source of the flow.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **Decryption** *(dict) --*The type of encryption that is used on the content ingested from
      this source.

        - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such as
        aes128, aes192, or aes256).
        - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented by
        a 32-character string, to be used with the key for encrypting content. This parameter is not
        valid for static key encryption.
        - **DeviceId** *(string) --*The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.
        - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).
        - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created in.
        This parameter is required for SPEKE encryption and is not valid for static key encryption.
        - **ResourceId** *(string) --*An identifier for the content. The service sends this value to
        the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
        - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).
        - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is not
        valid for SPEKE encryption.
        - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.
    """


_ClientUpdateFlowSourceResponseTypeDef = TypedDict(
    "_ClientUpdateFlowSourceResponseTypeDef",
    {"FlowArn": str, "Source": ClientUpdateFlowSourceResponseSourceTypeDef},
    total=False,
)


class ClientUpdateFlowSourceResponseTypeDef(_ClientUpdateFlowSourceResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect updated the flow successfully.

      - **FlowArn** *(string) --*The ARN of the flow that you want to update.
      - **Source** *(dict) --*The settings for the source of the flow.

        - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.
        - **Decryption** *(dict) --*The type of encryption that is used on the content ingested from
        this source.

          - **Algorithm** *(string) --*The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).
          - **ConstantInitializationVector** *(string) --*A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.
          - **DeviceId** *(string) --*The value of one of the devices that you configured with your
          digital rights management (DRM) platform key provider. This parameter is required for
          SPEKE encryption and is not valid for static key encryption.
          - **KeyType** *(string) --*The type of key that is used for the encryption. If no keyType
          is provided, the service will use the default setting (static-key).
          - **Region** *(string) --*The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.
          - **ResourceId** *(string) --*An identifier for the content. The service sends this value
          to the key server to identify the current endpoint. The resource ID is also known as the
          content ID. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.
          - **RoleArn** *(string) --*The ARN of the role that you created during setup (when you set
          up AWS Elemental MediaConnect as a trusted entity).
          - **SecretArn** *(string) --*The ARN of the secret that you created in AWS Secrets Manager
          to store the encryption key. This parameter is required for static key encryption and is
          not valid for SPEKE encryption.
          - **Url** *(string) --*The URL from the API Gateway proxy that you set up to talk to your
          key server. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.
    """


_ListEntitlementsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEntitlementsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEntitlementsPaginatePaginationConfigTypeDef(
    _ListEntitlementsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEntitlementsPaginateResponseEntitlementsTypeDef = TypedDict(
    "_ListEntitlementsPaginateResponseEntitlementsTypeDef",
    {"DataTransferSubscriberFeePercent": int, "EntitlementArn": str, "EntitlementName": str},
    total=False,
)


class ListEntitlementsPaginateResponseEntitlementsTypeDef(
    _ListEntitlementsPaginateResponseEntitlementsTypeDef
):
    """
    - *(dict) --*An entitlement that has been granted to you from other AWS accounts.

      - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.
      - **EntitlementArn** *(string) --*The ARN of the entitlement.
      - **EntitlementName** *(string) --*The name of the entitlement.
    """


_ListEntitlementsPaginateResponseTypeDef = TypedDict(
    "_ListEntitlementsPaginateResponseTypeDef",
    {"Entitlements": List[ListEntitlementsPaginateResponseEntitlementsTypeDef]},
    total=False,
)


class ListEntitlementsPaginateResponseTypeDef(_ListEntitlementsPaginateResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect returned the list of entitlements successfully.

      - **Entitlements** *(list) --*A list of entitlements that have been granted to you from other
      AWS accounts.

        - *(dict) --*An entitlement that has been granted to you from other AWS accounts.

          - **DataTransferSubscriberFeePercent** *(integer) --*Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.
          - **EntitlementArn** *(string) --*The ARN of the entitlement.
          - **EntitlementName** *(string) --*The name of the entitlement.
    """


_ListFlowsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFlowsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFlowsPaginatePaginationConfigTypeDef(_ListFlowsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFlowsPaginateResponseFlowsTypeDef = TypedDict(
    "_ListFlowsPaginateResponseFlowsTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": Literal["OWNED", "ENTITLED"],
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)


class ListFlowsPaginateResponseFlowsTypeDef(_ListFlowsPaginateResponseFlowsTypeDef):
    """
    - *(dict) --*Provides a summary of a flow, including its ARN, Availability Zone, and source
    type.

      - **AvailabilityZone** *(string) --*The Availability Zone that the flow was created in.
      - **Description** *(string) --*A description of the flow.
      - **FlowArn** *(string) --*The ARN of the flow.
      - **Name** *(string) --*The name of the flow.
      - **SourceType** *(string) --*The type of source. This value is either owned (originated
      somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or
      entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).
      - **Status** *(string) --*The current status of the flow.
    """


_ListFlowsPaginateResponseTypeDef = TypedDict(
    "_ListFlowsPaginateResponseTypeDef",
    {"Flows": List[ListFlowsPaginateResponseFlowsTypeDef]},
    total=False,
)


class ListFlowsPaginateResponseTypeDef(_ListFlowsPaginateResponseTypeDef):
    """
    - *(dict) --*AWS Elemental MediaConnect returned the list of flows successfully.

      - **Flows** *(list) --*A list of flow summaries.

        - *(dict) --*Provides a summary of a flow, including its ARN, Availability Zone, and source
        type.

          - **AvailabilityZone** *(string) --*The Availability Zone that the flow was created in.
          - **Description** *(string) --*A description of the flow.
          - **FlowArn** *(string) --*The ARN of the flow.
          - **Name** *(string) --*The name of the flow.
          - **SourceType** *(string) --*The type of source. This value is either owned (originated
          somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or
          entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).
          - **Status** *(string) --*The current status of the flow.
    """
