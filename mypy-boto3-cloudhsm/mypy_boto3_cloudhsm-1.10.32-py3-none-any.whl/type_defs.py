"Main interface for cloudhsm service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddTagsToResourceResponseTypeDef",
    "ClientAddTagsToResourceTagListTypeDef",
    "ClientCreateHapgResponseTypeDef",
    "ClientCreateHsmResponseTypeDef",
    "ClientCreateLunaClientResponseTypeDef",
    "ClientDeleteHapgResponseTypeDef",
    "ClientDeleteHsmResponseTypeDef",
    "ClientDeleteLunaClientResponseTypeDef",
    "ClientDescribeHapgResponseTypeDef",
    "ClientDescribeHsmResponseTypeDef",
    "ClientDescribeLunaClientResponseTypeDef",
    "ClientGetConfigResponseTypeDef",
    "ClientListAvailableZonesResponseTypeDef",
    "ClientListHapgsResponseTypeDef",
    "ClientListHsmsResponseTypeDef",
    "ClientListLunaClientsResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyHapgResponseTypeDef",
    "ClientModifyHsmResponseTypeDef",
    "ClientModifyLunaClientResponseTypeDef",
    "ClientRemoveTagsFromResourceResponseTypeDef",
    "ListHapgsPaginatePaginationConfigTypeDef",
    "ListHapgsPaginateResponseTypeDef",
    "ListHsmsPaginatePaginationConfigTypeDef",
    "ListHsmsPaginateResponseTypeDef",
    "ListLunaClientsPaginatePaginationConfigTypeDef",
    "ListLunaClientsPaginateResponseTypeDef",
)


_ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "_ClientAddTagsToResourceResponseTypeDef", {"Status": str}, total=False
)


class ClientAddTagsToResourceResponseTypeDef(_ClientAddTagsToResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The status of the operation.
    """


_RequiredClientAddTagsToResourceTagListTypeDef = TypedDict(
    "_RequiredClientAddTagsToResourceTagListTypeDef", {"Key": str}
)
_OptionalClientAddTagsToResourceTagListTypeDef = TypedDict(
    "_OptionalClientAddTagsToResourceTagListTypeDef", {"Value": str}, total=False
)


class ClientAddTagsToResourceTagListTypeDef(
    _RequiredClientAddTagsToResourceTagListTypeDef, _OptionalClientAddTagsToResourceTagListTypeDef
):
    """
    - *(dict) --*

      A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientCreateHapgResponseTypeDef = TypedDict(
    "_ClientCreateHapgResponseTypeDef", {"HapgArn": str}, total=False
)


class ClientCreateHapgResponseTypeDef(_ClientCreateHapgResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the  CreateHAPartitionGroup action.
      - **HapgArn** *(string) --*

        The ARN of the high-availability partition group.
    """


_ClientCreateHsmResponseTypeDef = TypedDict(
    "_ClientCreateHsmResponseTypeDef", {"HsmArn": str}, total=False
)


class ClientCreateHsmResponseTypeDef(_ClientCreateHsmResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the ``CreateHsm`` operation.
      - **HsmArn** *(string) --*

        The ARN of the HSM.
    """


_ClientCreateLunaClientResponseTypeDef = TypedDict(
    "_ClientCreateLunaClientResponseTypeDef", {"ClientArn": str}, total=False
)


class ClientCreateLunaClientResponseTypeDef(_ClientCreateLunaClientResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the  CreateLunaClient action.
      - **ClientArn** *(string) --*

        The ARN of the client.
    """


_ClientDeleteHapgResponseTypeDef = TypedDict(
    "_ClientDeleteHapgResponseTypeDef", {"Status": str}, total=False
)


class ClientDeleteHapgResponseTypeDef(_ClientDeleteHapgResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the  DeleteHapg action.
      - **Status** *(string) --*

        The status of the action.
    """


_ClientDeleteHsmResponseTypeDef = TypedDict(
    "_ClientDeleteHsmResponseTypeDef", {"Status": str}, total=False
)


class ClientDeleteHsmResponseTypeDef(_ClientDeleteHsmResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the  DeleteHsm operation.
      - **Status** *(string) --*

        The status of the operation.
    """


_ClientDeleteLunaClientResponseTypeDef = TypedDict(
    "_ClientDeleteLunaClientResponseTypeDef", {"Status": str}, total=False
)


class ClientDeleteLunaClientResponseTypeDef(_ClientDeleteLunaClientResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The status of the action.
    """


_ClientDescribeHapgResponseTypeDef = TypedDict(
    "_ClientDescribeHapgResponseTypeDef",
    {
        "HapgArn": str,
        "HapgSerial": str,
        "HsmsLastActionFailed": List[str],
        "HsmsPendingDeletion": List[str],
        "HsmsPendingRegistration": List[str],
        "Label": str,
        "LastModifiedTimestamp": str,
        "PartitionSerialList": List[str],
        "State": Literal["READY", "UPDATING", "DEGRADED"],
    },
    total=False,
)


class ClientDescribeHapgResponseTypeDef(_ClientDescribeHapgResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the  DescribeHapg action.
      - **HapgArn** *(string) --*

        The ARN of the high-availability partition group.
    """


_ClientDescribeHsmResponseTypeDef = TypedDict(
    "_ClientDescribeHsmResponseTypeDef",
    {
        "HsmArn": str,
        "Status": Literal[
            "PENDING", "RUNNING", "UPDATING", "SUSPENDED", "TERMINATING", "TERMINATED", "DEGRADED"
        ],
        "StatusDetails": str,
        "AvailabilityZone": str,
        "EniId": str,
        "EniIp": str,
        "SubscriptionType": str,
        "SubscriptionStartDate": str,
        "SubscriptionEndDate": str,
        "VpcId": str,
        "SubnetId": str,
        "IamRoleArn": str,
        "SerialNumber": str,
        "VendorName": str,
        "HsmType": str,
        "SoftwareVersion": str,
        "SshPublicKey": str,
        "SshKeyLastUpdated": str,
        "ServerCertUri": str,
        "ServerCertLastUpdated": str,
        "Partitions": List[str],
    },
    total=False,
)


class ClientDescribeHsmResponseTypeDef(_ClientDescribeHsmResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the  DescribeHsm operation.
      - **HsmArn** *(string) --*

        The ARN of the HSM.
    """


_ClientDescribeLunaClientResponseTypeDef = TypedDict(
    "_ClientDescribeLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
        "CertificateFingerprint": str,
        "LastModifiedTimestamp": str,
        "Label": str,
    },
    total=False,
)


class ClientDescribeLunaClientResponseTypeDef(_ClientDescribeLunaClientResponseTypeDef):
    """
    - *(dict) --*

      - **ClientArn** *(string) --*

        The ARN of the client.
    """


_ClientGetConfigResponseTypeDef = TypedDict(
    "_ClientGetConfigResponseTypeDef",
    {"ConfigType": str, "ConfigFile": str, "ConfigCred": str},
    total=False,
)


class ClientGetConfigResponseTypeDef(_ClientGetConfigResponseTypeDef):
    """
    - *(dict) --*

      - **ConfigType** *(string) --*

        The type of credentials.
    """


_ClientListAvailableZonesResponseTypeDef = TypedDict(
    "_ClientListAvailableZonesResponseTypeDef", {"AZList": List[str]}, total=False
)


class ClientListAvailableZonesResponseTypeDef(_ClientListAvailableZonesResponseTypeDef):
    """
    - *(dict) --*

      - **AZList** *(list) --*

        The list of Availability Zones that have available AWS CloudHSM capacity.
        - *(string) --*
    """


_ClientListHapgsResponseTypeDef = TypedDict(
    "_ClientListHapgsResponseTypeDef", {"HapgList": List[str], "NextToken": str}, total=False
)


class ClientListHapgsResponseTypeDef(_ClientListHapgsResponseTypeDef):
    """
    - *(dict) --*

      - **HapgList** *(list) --*

        The list of high-availability partition groups.
        - *(string) --*
    """


_ClientListHsmsResponseTypeDef = TypedDict(
    "_ClientListHsmsResponseTypeDef", {"HsmList": List[str], "NextToken": str}, total=False
)


class ClientListHsmsResponseTypeDef(_ClientListHsmsResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the ``ListHsms`` operation.
      - **HsmList** *(list) --*

        The list of ARNs that identify the HSMs.
        - *(string) --*

          An ARN that identifies an HSM.
    """


_ClientListLunaClientsResponseTypeDef = TypedDict(
    "_ClientListLunaClientsResponseTypeDef",
    {"ClientList": List[str], "NextToken": str},
    total=False,
)


class ClientListLunaClientsResponseTypeDef(_ClientListLunaClientsResponseTypeDef):
    """
    - *(dict) --*

      - **ClientList** *(list) --*

        The list of clients.
        - *(string) --*
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    - *(dict) --*

      A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **TagList** *(list) --*

        One or more tags.
        - *(dict) --*

          A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
          - **Key** *(string) --*

            The key of the tag.
    """


_ClientModifyHapgResponseTypeDef = TypedDict(
    "_ClientModifyHapgResponseTypeDef", {"HapgArn": str}, total=False
)


class ClientModifyHapgResponseTypeDef(_ClientModifyHapgResponseTypeDef):
    """
    - *(dict) --*

      - **HapgArn** *(string) --*

        The ARN of the high-availability partition group.
    """


_ClientModifyHsmResponseTypeDef = TypedDict(
    "_ClientModifyHsmResponseTypeDef", {"HsmArn": str}, total=False
)


class ClientModifyHsmResponseTypeDef(_ClientModifyHsmResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the  ModifyHsm operation.
      - **HsmArn** *(string) --*

        The ARN of the HSM.
    """


_ClientModifyLunaClientResponseTypeDef = TypedDict(
    "_ClientModifyLunaClientResponseTypeDef", {"ClientArn": str}, total=False
)


class ClientModifyLunaClientResponseTypeDef(_ClientModifyLunaClientResponseTypeDef):
    """
    - *(dict) --*

      - **ClientArn** *(string) --*

        The ARN of the client.
    """


_ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "_ClientRemoveTagsFromResourceResponseTypeDef", {"Status": str}, total=False
)


class ClientRemoveTagsFromResourceResponseTypeDef(_ClientRemoveTagsFromResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The status of the operation.
    """


_ListHapgsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHapgsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListHapgsPaginatePaginationConfigTypeDef(_ListHapgsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHapgsPaginateResponseTypeDef = TypedDict(
    "_ListHapgsPaginateResponseTypeDef", {"HapgList": List[str]}, total=False
)


class ListHapgsPaginateResponseTypeDef(_ListHapgsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **HapgList** *(list) --*

        The list of high-availability partition groups.
        - *(string) --*
    """


_ListHsmsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHsmsPaginatePaginationConfigTypeDef", {"MaxItems": int, "StartingToken": str}, total=False
)


class ListHsmsPaginatePaginationConfigTypeDef(_ListHsmsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHsmsPaginateResponseTypeDef = TypedDict(
    "_ListHsmsPaginateResponseTypeDef", {"HsmList": List[str]}, total=False
)


class ListHsmsPaginateResponseTypeDef(_ListHsmsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the output of the ``ListHsms`` operation.
      - **HsmList** *(list) --*

        The list of ARNs that identify the HSMs.
        - *(string) --*

          An ARN that identifies an HSM.
    """


_ListLunaClientsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLunaClientsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListLunaClientsPaginatePaginationConfigTypeDef(
    _ListLunaClientsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLunaClientsPaginateResponseTypeDef = TypedDict(
    "_ListLunaClientsPaginateResponseTypeDef", {"ClientList": List[str]}, total=False
)


class ListLunaClientsPaginateResponseTypeDef(_ListLunaClientsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ClientList** *(list) --*

        The list of clients.
        - *(string) --*
    """
