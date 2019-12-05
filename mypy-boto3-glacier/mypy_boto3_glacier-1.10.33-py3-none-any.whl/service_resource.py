"Main interface for glacier service ServiceResource"
from __future__ import annotations

from typing import Any, Dict, IO, List, Union
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_glacier.service_resource as service_resource_scope
from mypy_boto3_glacier.type_defs import (
    JobGetOutputResponseTypeDef,
    MultipartUploadCompleteResponseTypeDef,
    MultipartUploadPartsResponseTypeDef,
    MultipartUploadUploadPartResponseTypeDef,
    NotificationSetVaultNotificationConfigTypeDef,
    VaultCreateResponseTypeDef,
)


__all__ = (
    "ServiceResource",
    "Account",
    "Archive",
    "Job",
    "MultipartUpload",
    "Notification",
    "Vault",
    "ServiceResourceVaultsCollection",
    "AccountVaultsCollection",
    "VaultCompletedJobsCollection",
    "VaultFailedJobsCollection",
    "VaultJobsCollection",
    "VaultJobsInProgressCollection",
    "VaultMultipartUplaodsCollection",
    "VaultMultipartUploadsCollection",
    "VaultSucceededJobsCollection",
)


class ServiceResource(Boto3ServiceResource):
    """
    [Glacier.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource)
    """

    vaults: service_resource_scope.ServiceResourceVaultsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Account(self, id: str) -> service_resource_scope.Account:
        """
        [ServiceResource.Account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Archive(self, account_id: str, vault_name: str, id: str) -> service_resource_scope.Archive:
        """
        [ServiceResource.Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Archive)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Job(self, account_id: str, vault_name: str, id: str) -> service_resource_scope.Job:
        """
        [ServiceResource.Job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def MultipartUpload(
        self, account_id: str, vault_name: str, id: str
    ) -> service_resource_scope.MultipartUpload:
        """
        [ServiceResource.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Notification(self, account_id: str, vault_name: str) -> service_resource_scope.Notification:
        """
        [ServiceResource.Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Notification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Vault(self, account_id: str, name: str) -> service_resource_scope.Vault:
        """
        [ServiceResource.Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vault(self, vaultName: str) -> service_resource_scope.Vault:
        """
        [ServiceResource.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.create_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.get_available_subresources)
        """


class Account(Boto3ServiceResource):
    """
    [Account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Account)
    """

    id: str
    vaults: service_resource_scope.AccountVaultsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vault(self, vaultName: str) -> service_resource_scope.Vault:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class Archive(Boto3ServiceResource):
    """
    [Archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Archive)
    """

    account_id: str
    vault_name: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_archive_retrieval(self, *args: Any, **kwargs: Any) -> service_resource_scope.Job:
        pass


class Job(Boto3ServiceResource):
    """
    [Job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Job)
    """

    job_id: str
    job_description: str
    action: str
    archive_id: str
    vault_arn: str
    creation_date: str
    completed: bool
    status_code: str
    status_message: str
    archive_size_in_bytes: int
    inventory_size_in_bytes: int
    sns_topic: str
    completion_date: str
    sha256_tree_hash: str
    archive_sha256_tree_hash: str
    retrieval_byte_range: str
    tier: str
    inventory_retrieval_parameters: Dict[str, Any]
    job_output_path: str
    select_parameters: Dict[str, Any]
    output_location: Dict[str, Any]
    account_id: str
    vault_name: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_output(self, range: str = None) -> JobGetOutputResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class MultipartUpload(Boto3ServiceResource):
    """
    [MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.MultipartUpload)
    """

    multipart_upload_id: str
    vault_arn: str
    archive_description: str
    part_size_in_bytes: int
    creation_date: str
    account_id: str
    vault_name: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def abort(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def complete(
        self, archiveSize: str = None, checksum: str = None
    ) -> MultipartUploadCompleteResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def parts(self, marker: str = None, limit: str = None) -> MultipartUploadPartsResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_part(
        self, checksum: str = None, range: str = None, body: Union[bytes, IO] = None
    ) -> MultipartUploadUploadPartResponseTypeDef:
        pass


class Notification(Boto3ServiceResource):
    """
    [Notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Notification)
    """

    sns_topic: str
    events: List[Any]
    account_id: str
    vault_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set(
        self, vaultNotificationConfig: NotificationSetVaultNotificationConfigTypeDef = None
    ) -> None:
        pass


class Vault(Boto3ServiceResource):
    """
    [Vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.Vault)
    """

    vault_arn: str
    vault_name: str
    creation_date: str
    last_inventory_date: str
    number_of_archives: int
    size_in_bytes: int
    account_id: str
    name: str
    completed_jobs: service_resource_scope.VaultCompletedJobsCollection
    failed_jobs: service_resource_scope.VaultFailedJobsCollection
    jobs: service_resource_scope.VaultJobsCollection
    jobs_in_progress: service_resource_scope.VaultJobsInProgressCollection
    multipart_uplaods: service_resource_scope.VaultMultipartUplaodsCollection
    multipart_uploads: service_resource_scope.VaultMultipartUploadsCollection
    succeeded_jobs: service_resource_scope.VaultSucceededJobsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(self, *args: Any, **kwargs: Any) -> VaultCreateResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_inventory_retrieval(self, *args: Any, **kwargs: Any) -> service_resource_scope.Job:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_multipart_upload(
        self, archiveDescription: str = None, partSize: str = None
    ) -> service_resource_scope.MultipartUpload:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_archive(
        self, archiveDescription: str = None, checksum: str = None, body: Union[bytes, IO] = None
    ) -> service_resource_scope.Archive:
        pass


class ServiceResourceVaultsCollection(ResourceCollection):
    """
    [ServiceResource.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.ServiceResource.vaults)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Vault]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, marker: str = None, limit: str = None) -> List[service_resource_scope.Vault]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Vault]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Vault]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class AccountVaultsCollection(ResourceCollection):
    """
    [Account.vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Account.vaults)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Vault]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, marker: str = None, limit: str = None) -> List[service_resource_scope.Vault]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Vault]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Vault]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VaultCompletedJobsCollection(ResourceCollection):
    """
    [Vault.completed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Vault.completed_jobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, limit: str = None, marker: str = None, statuscode: str = None
    ) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VaultFailedJobsCollection(ResourceCollection):
    """
    [Vault.failed_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Vault.failed_jobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, limit: str = None, marker: str = None, completed: str = None
    ) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VaultJobsCollection(ResourceCollection):
    """
    [Vault.jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Vault.jobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, limit: str = None, marker: str = None, statuscode: str = None, completed: str = None
    ) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VaultJobsInProgressCollection(ResourceCollection):
    """
    [Vault.jobs_in_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Vault.jobs_in_progress)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, limit: str = None, marker: str = None, completed: str = None
    ) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VaultMultipartUplaodsCollection(ResourceCollection):
    """
    [Vault.multipart_uplaods documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Vault.multipart_uplaods)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.MultipartUpload]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, marker: str = None, limit: str = None
    ) -> List[service_resource_scope.MultipartUpload]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.MultipartUpload]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.MultipartUpload]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VaultMultipartUploadsCollection(ResourceCollection):
    """
    [Vault.multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Vault.multipart_uploads)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.MultipartUpload]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, marker: str = None, limit: str = None
    ) -> List[service_resource_scope.MultipartUpload]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.MultipartUpload]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.MultipartUpload]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class VaultSucceededJobsCollection(ResourceCollection):
    """
    [Vault.succeeded_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/glacier.html#Glacier.Vault.succeeded_jobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, limit: str = None, marker: str = None, completed: str = None
    ) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Job]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass
