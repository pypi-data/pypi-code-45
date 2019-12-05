"Main interface for cloudhsm service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_cloudhsm.client as client_scope

# pylint: disable=import-self
import mypy_boto3_cloudhsm.paginator as paginator_scope
from mypy_boto3_cloudhsm.type_defs import (
    ClientAddTagsToResourceResponseTypeDef,
    ClientAddTagsToResourceTagListTypeDef,
    ClientCreateHapgResponseTypeDef,
    ClientCreateHsmResponseTypeDef,
    ClientCreateLunaClientResponseTypeDef,
    ClientDeleteHapgResponseTypeDef,
    ClientDeleteHsmResponseTypeDef,
    ClientDeleteLunaClientResponseTypeDef,
    ClientDescribeHapgResponseTypeDef,
    ClientDescribeHsmResponseTypeDef,
    ClientDescribeLunaClientResponseTypeDef,
    ClientGetConfigResponseTypeDef,
    ClientListAvailableZonesResponseTypeDef,
    ClientListHapgsResponseTypeDef,
    ClientListHsmsResponseTypeDef,
    ClientListLunaClientsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientModifyHapgResponseTypeDef,
    ClientModifyHsmResponseTypeDef,
    ClientModifyLunaClientResponseTypeDef,
    ClientRemoveTagsFromResourceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [CloudHSM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(
        self, ResourceArn: str, TagList: List[ClientAddTagsToResourceTagListTypeDef]
    ) -> ClientAddTagsToResourceResponseTypeDef:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.add_tags_to_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_hapg(self, Label: str) -> ClientCreateHapgResponseTypeDef:
        """
        [Client.create_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.create_hapg)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_hsm(
        self,
        SubnetId: str,
        SshKey: str,
        IamRoleArn: str,
        SubscriptionType: str,
        EniIp: str = None,
        ExternalId: str = None,
        ClientToken: str = None,
        SyslogIp: str = None,
    ) -> ClientCreateHsmResponseTypeDef:
        """
        [Client.create_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.create_hsm)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_luna_client(
        self, Certificate: str, Label: str = None
    ) -> ClientCreateLunaClientResponseTypeDef:
        """
        [Client.create_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.create_luna_client)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_hapg(self, HapgArn: str) -> ClientDeleteHapgResponseTypeDef:
        """
        [Client.delete_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.delete_hapg)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_hsm(self, HsmArn: str) -> ClientDeleteHsmResponseTypeDef:
        """
        [Client.delete_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.delete_hsm)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_luna_client(self, ClientArn: str) -> ClientDeleteLunaClientResponseTypeDef:
        """
        [Client.delete_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.delete_luna_client)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_hapg(self, HapgArn: str) -> ClientDescribeHapgResponseTypeDef:
        """
        [Client.describe_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.describe_hapg)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_hsm(
        self, HsmArn: str = None, HsmSerialNumber: str = None
    ) -> ClientDescribeHsmResponseTypeDef:
        """
        [Client.describe_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.describe_hsm)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_luna_client(
        self, ClientArn: str = None, CertificateFingerprint: str = None
    ) -> ClientDescribeLunaClientResponseTypeDef:
        """
        [Client.describe_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.describe_luna_client)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_config(
        self, ClientArn: str, ClientVersion: Literal["5.1", "5.3"], HapgList: List[str]
    ) -> ClientGetConfigResponseTypeDef:
        """
        [Client.get_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.get_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_available_zones(
        self, *args: Any, **kwargs: Any
    ) -> ClientListAvailableZonesResponseTypeDef:
        """
        [Client.list_available_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.list_available_zones)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_hapgs(self, NextToken: str = None) -> ClientListHapgsResponseTypeDef:
        """
        [Client.list_hapgs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.list_hapgs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_hsms(self, NextToken: str = None) -> ClientListHsmsResponseTypeDef:
        """
        [Client.list_hsms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.list_hsms)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_luna_clients(self, NextToken: str = None) -> ClientListLunaClientsResponseTypeDef:
        """
        [Client.list_luna_clients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.list_luna_clients)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_hapg(
        self, HapgArn: str, Label: str = None, PartitionSerialList: List[str] = None
    ) -> ClientModifyHapgResponseTypeDef:
        """
        [Client.modify_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.modify_hapg)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_hsm(
        self,
        HsmArn: str,
        SubnetId: str = None,
        EniIp: str = None,
        IamRoleArn: str = None,
        ExternalId: str = None,
        SyslogIp: str = None,
    ) -> ClientModifyHsmResponseTypeDef:
        """
        [Client.modify_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.modify_hsm)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_luna_client(
        self, ClientArn: str, Certificate: str
    ) -> ClientModifyLunaClientResponseTypeDef:
        """
        [Client.modify_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.modify_luna_client)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(
        self, ResourceArn: str, TagKeyList: List[str]
    ) -> ClientRemoveTagsFromResourceResponseTypeDef:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Client.remove_tags_from_resource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_hapgs"]
    ) -> paginator_scope.ListHapgsPaginator:
        """
        [Paginator.ListHapgs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_hsms"]
    ) -> paginator_scope.ListHsmsPaginator:
        """
        [Paginator.ListHsms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_luna_clients"]
    ) -> paginator_scope.ListLunaClientsPaginator:
        """
        [Paginator.ListLunaClients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CloudHsmInternalException: Boto3ClientError
    CloudHsmServiceException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
