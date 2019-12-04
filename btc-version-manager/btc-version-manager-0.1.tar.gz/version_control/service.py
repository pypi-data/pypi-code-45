import json
import uuid
from typing import List, Optional, Union, Type

from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.serializers.base import Serializer
from django.db import transaction
from django.urls import resolve
from django.utils import timezone

from version_control.cache import VersionControlTemporaryStorage
from version_control.collections import ModelObjectChangeType
from version_control.database import TransactionManager
from version_control.middleware import get_request
from version_control.models import ModelObjectVersionGroup, ModelObjectVersion, AbstractVersionControl
from version_control.serializers import VersionControlJSONSerializer, VersionControlPythonSerializer, \
    VersionControlJSONEncoder

TYPE_VS_OBJECT = AbstractVersionControl
USER_MODEL_CLASS = get_user_model()


class VersionControlManager:
    """
    Model object version manager
    """

    def __init__(self, using=None, request_key: str = None, redis_timeout: int = 60):
        self.using = using
        self.redis_timeout = redis_timeout
        self.request = get_request()
        self.request_key = request_key or getattr(self.request, 'key', None)
        self.current_user = getattr(self.request, 'user', None)

        database = 'default' if self.using is None else self.using
        self.atomic_requests_enabled = settings.DATABASES[database]['ATOMIC_REQUESTS']

        self._unsaved_versions = []  # type: List[ModelObjectVersion]
        self.saved_versions = []     # type: List[ModelObjectVersion]

        self.provide_storage_verification()

    def provide_storage_verification(self) -> None:
        """
        Method that sets verification flag for signatures recorded in the 'VersionControlTemporaryStorage'
        storage.
        If the project uses transactions, storage data marks as valid on exit the active transaction block,
        if the project doesn't use transactions - verification flag sets in changed object save method.
        Storage without verification flag will be considered as invalid and versions of objects
        listed in it will be never recorded
        """

        if self.atomic_requests_enabled:
            connection = transaction.get_connection()
            if connection.in_atomic_block:
                run_on_commit = connection.run_on_commit
                for sid, func in run_on_commit:
                    if func.__name__ == self.verify_storage.__name__:
                        return
                transaction.on_commit(self.verify_storage)
        else:
            self.verify_storage()

    def get_storage(self) -> VersionControlTemporaryStorage:
        return VersionControlTemporaryStorage(storage_key=self.request_key, timeout=self.redis_timeout)

    def verify_storage(self) -> None:
        storage = self.get_storage()
        storage.verify()

    @staticmethod
    def get_version_control_model_classes(to_str: bool = False) -> list:
        """
        Method for obtaining all classes of tracked models.
        :param to_str: string conversion flag
        :return: list
        """

        return [model_class.__name__.lower() if to_str else model_class for model_class in apps.get_models()
                if issubclass(model_class, AbstractVersionControl)]

    def initialize_version_control(self,
                                   vcs_datetime: Optional[timezone.datetime],
                                   print_progress: bool = True) -> None:
        """
        Method for initializing version control for connected models - recording their initial versions
        :param vcs_datetime: version initialization date and time
        :param print_progress: bool, flag for result print
        :return: None
        """

        model_classes = self.get_version_control_model_classes()
        model_classes_len = len(model_classes)
        for index, model_class in enumerate(model_classes):
            model_class_objects = model_class.objects.all()
            created = timezone.localtime(timezone.make_aware(vcs_datetime)) if vcs_datetime is not None else None
            self.create_version_from_objects(
                *model_class_objects,
                version_created=created,
                version_change_type=ModelObjectChangeType.OBJECT_STATE_INIT,
                pre_populate_mode=True
            )
            if print_progress:
                print(f'{index+1}/{model_classes_len}: {model_class.__name__} всего: {model_class_objects.count()}')

    def get_current_app(self) -> str:
        return resolve(self.request.path).app_name if self.request else None

    def get_current_url(self) -> str:
        return self.request.get_full_path() if self.request else None

    def add_object_to_storage(self, changed_object: TYPE_VS_OBJECT, **version_control_kwargs) -> None:
        """
        Method for updating the temporary storage
        :param changed_object: object to add to the repository
        :param version_control_kwargs: parameters for version control service
        :return: None
        """

        storage = self.get_storage()
        serialized_object = self.serialize_objects(changed_object)
        changed_object_hash = changed_object.get_hash()
        version_control_kwargs.update(version_author=self.current_user, request_key=self.request_key)
        storage.add_object(serialized_object, changed_object_hash, **version_control_kwargs)

    def create_version_from_storage(self) -> List[ModelObjectVersion]:
        """
        Method that records version for objects in temporary storage
        """

        storage = self.get_storage()
        transaction_manager = TransactionManager(Exception, raise_exc=True)
        transaction_manager.transaction_rollback_log_message = 'Version Control transaction rollback: %s, %s'
        with transaction_manager:
            storage.clean()
            for object_hash, signature in storage.get_objects():
                extracted_object = json.loads(signature['serialized_object'])[0]
                self.create_version_from_serialized(extracted_object, **signature['kwargs'])
                storage.remove_object_by_hash(object_hash)
            self.save_versions(bulk=True)
        return self.saved_versions

    def create_version_from_serialized(self,
                                       serialized_object: dict,
                                       commit: bool = False,
                                       **kwargs) -> Optional[List[ModelObjectVersion]]:
        """
        Method for creating versions from serialized objects
        :param serialized_object: dict, serialized state of the modified object
        :param commit: bool, save version flag
        :param kwargs: dict, parameters for version control service
        :return: Optional[List[ModelObjectVersion]]
        """

        skip_version_control = kwargs.pop('skip_version_control', False)
        if not skip_version_control:
            service_parameters = self.get_service_parameters(**kwargs)
            service = self.Service(serialized_object, **service_parameters)
            if service:
                new_version = service.init_version()
                if new_version is not None:
                    self._unsaved_versions.append(new_version)
        if commit:
            self.save_versions(bulk=True)
            return self.saved_versions

    def create_version_from_objects(self, *changed_objects, **kwargs) -> List[ModelObjectVersion]:
        """
        Method that creates versions for modified objects
        :param changed_objects: collection of objects for writing versions
        :param kwargs: dict, parameters for version control service
        :return: List[ModelObjectVersion]
        """

        serialized_objects = self.serialize_objects(*changed_objects, serializer=VersionControlPythonSerializer)
        for serialized_object in serialized_objects:
            self.create_version_from_serialized(serialized_object, **kwargs)
        self.save_versions(bulk=True)
        return self.saved_versions

    def save_versions(self, bulk: bool = False) -> None:
        # save created versions of model objects
        if self._unsaved_versions:
            if bulk:
                self.saved_versions += ModelObjectVersion.objects.bulk_create(self._unsaved_versions)
            else:
                for version in self._unsaved_versions:
                    version.save()
                    self.saved_versions.append(version)
            self._unsaved_versions.clear()

    def get_service_parameters(self, **kwargs):
        service_parameters = dict()
        service_parameters['version_author'] = kwargs.pop('version_author', self.current_user)
        service_parameters['version_request_key'] = kwargs.pop('request_key', self.request_key)
        service_parameters['version_change_type'] = kwargs.pop('version_change_type', None)
        service_parameters['version_change_url'] = self.get_current_url()
        service_parameters['version_change_app'] = self.get_current_app()
        service_parameters['version_created'] = kwargs.pop('version_created', None)
        service_parameters['pre_populate_mode'] = kwargs.pop('pre_populate_mode', False)
        return service_parameters

    def revert_model_object_version(self, target_version_hash: str) -> None:
        """
        Method for rolling back the model object version
        :param target_version_hash: version hash for rollback
        :return: None
        """

        target_version = ModelObjectVersion.objects.filter(hash=target_version_hash).first()
        if target_version and not target_version.is_last_version():
            if target_version.state is None:
                pass
            else:
                deserialized_object, proxy_object = target_version.get_state_deserialized()
                if deserialized_object and proxy_object:
                    deserialized_object.save()
                    self.create_version_from_objects(proxy_object.object,
                                                     version_change_type=ModelObjectChangeType.OBJECT_RESTORED)

    @classmethod
    def serialize_objects(cls, *changed_objects, serializer: Type[Serializer] = VersionControlJSONSerializer) -> dict:
        return serializer().serialize(changed_objects)

    class Service:
        """
        Service for recording state of model objects
        """

        def __init__(self,
                     serialized_object: dict,
                     version_author: Union[USER_MODEL_CLASS, int] = None,
                     version_request_key: uuid = None,
                     version_change_type: str = None,
                     version_change_url: str = None,
                     version_change_app: str = None,
                     version_created: timezone.datetime = None,
                     pre_populate_mode: bool = False):

            self.serialized_object = serialized_object
            self.version_author = version_author
            self.version_request_key = version_request_key or uuid.uuid4().hex
            self.version_change_type = version_change_type
            self.version_change_url = version_change_url
            self.version_change_app = version_change_app
            self.version_created = version_created or timezone.now()
            self.version_hash = uuid.uuid4().hex
            self.pre_populate_mode = pre_populate_mode
            self.group, self.is_first_version_init = self.init_version_group()

        def init_version_group(self) -> tuple:
            extracted_model = self.serialized_object['model'].split('.')[-1]
            return ModelObjectVersionGroup.objects.get_or_create(
                content_type=ContentType.objects.filter(model=extracted_model).first(),
                object_id=self.serialized_object['pk'],
                defaults=dict(
                    representation=self.serialized_object['obj_extra_data']['representation'],
                    verbose_name=self.serialized_object['obj_extra_data']['verbose_name']
                )
            )

        def init_version(self) -> ModelObjectVersion:
            version = None
            need_pre_population = self.pre_populate_mode and (self.is_first_version_init or
                                                              not self.group.model_object_versions.exists())
            if not self.pre_populate_mode or need_pre_population:
                version = ModelObjectVersion(
                    group=self.group,
                    request_key=self.version_request_key,
                    created=self.version_created,
                    change_url=self.version_change_url,
                    change_app=self.version_change_app,
                    hash=self.version_hash,
                    change_type=self.get_version_change_type(),
                    state=self.get_dumped_state()
                )

                # User set. When set to 'None', it is considered that the change was made by the system
                if isinstance(self.version_author, int):
                    version.author_id = self.version_author
                elif isinstance(self.version_author, USER_MODEL_CLASS):
                    version.author = self.version_author
            return version

        def get_version_change_type(self) -> str:
            version_change_type = self.version_change_type
            if version_change_type is None:
                if self.is_first_version_init:
                    version_change_type = ModelObjectChangeType.OBJECT_CREATED
                else:
                    version_change_type = ModelObjectChangeType.OBJECT_CHANGED
            return version_change_type

        def get_dumped_state(self) -> str:
            """
            Method that dumps changed object state to json string to save in 'JSONField'
            """

            return json.dumps(self.serialized_object, cls=VersionControlJSONEncoder)
