from typing import Optional, Hashable

from django.core.cache import cache


class VersionControlTemporaryStorage:
    """
    The temporary storage class. Storage is required to contain objects that need version control.
    The repository is a wrapper over a regular dictionary that is cached in redis (or another backend) and can be
    restored from him at any given time by the unique key 'request_key'.
    The storage contains all the necessary data for writing versions and can be processed in other processes,
    for example through celery.
    The 'is_verified' flag sets on active transaction commit (transaction.commit ()),
    the 'is_cleaned' flag designed to verify completion of additional storage processing (if specified) before writing
    versions. Both flags must be set to 'True' in order for the storage to give data for recording.
    """

    def __init__(self, storage_key: Hashable, timeout: int = 60):
        self.storage_key = storage_key
        self.__storage = cache.get_or_set(storage_key, default=self.get_empty_storage, timeout=timeout)

    def get_empty_storage(self) -> dict:
        """
        Method for initializing empty storage
        """

        return dict(is_verified=False, is_cleaned=False, changed_objects={})

    def cache_storage(self) -> None:
        """
        Method for storage caching
        """

        cache.set(self.storage_key, self.__storage, timeout=None)

    @property
    def is_verified(self) -> bool:
        """
        Property for check whether it is possible to record versions for storage data
        """

        return self.__storage['is_verified']

    @is_verified.setter
    def is_verified(self, state: bool) -> None:
        """
        Property setter for set the storage verification flag
        """

        self.__storage['is_verified'] = state
        self.cache_storage()

    @property
    def is_cleaned(self) -> bool:
        """
        Property for check if storage is prepared before retrieving modified objects
        """

        return self.__storage['is_cleaned']

    @is_cleaned.setter
    def is_cleaned(self, state: bool) -> None:
        """
        Property setter for set the storage ready flag
        """

        self.__storage['is_cleaned'] = state
        self.cache_storage()

    def add_object(self, serialized_object: dict, changed_object_hash: str, **version_control_kwargs) -> None:
        """
        Method for adding an object to the storage.
        :param serialized_object: serialized state of the object to add to the storage
        :param changed_object_hash: hash of an object to identify it in the storage
        :param version_control_kwargs: parameters for version control service
        :return: None
        """

        changed_object_signature = {
            changed_object_hash: {
                'serialized_object': serialized_object,
                'kwargs': version_control_kwargs
            }
        }
        self.__storage['changed_objects'].update(changed_object_signature)
        self.cache_storage()

    def get_object_by_hash(self, object_hash: str) -> dict:
        """
        Method to retrieve the signature of an object from storage by hash
        """

        return self.__storage['changed_objects'].get(object_hash)

    def remove_object_by_hash(self, object_hash: str) -> Optional[dict]:
        """
        Method for removing the signature of an object from storage by hash
        """

        removed = self.__storage['changed_objects'].pop(object_hash)
        self.cache_storage()
        return removed

    def get_objects(self) -> dict:
        """
        Method for retrieving objects signatures from storage
        """

        storage_data = dict()
        if self.is_verified and self.is_cleaned:
            storage_data = self.__storage['changed_objects'].copy().items()
        return storage_data

    def clean(self) -> None:
        """
        Method for preparing stored objects signatures
        """

        self.is_cleaned = True

    def verify(self) -> None:
        """
        Method for verification of storage
        """

        self.is_verified = True
