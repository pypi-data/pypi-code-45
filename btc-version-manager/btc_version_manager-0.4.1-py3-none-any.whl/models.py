import json
from collections import Collection
from typing import Any, Optional

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField
from django.core import serializers
from django.core.cache import cache
from django.db import models
from django.forms import model_to_dict
from django.utils.timezone import now as tz_now

from version_control.collections import ModelObjectChangeType
from version_control.debugger import Debugger
from version_control.managers import ModelObjectVersionGroupQuerySet, ModelObjectVersionQuerySet
from version_control.utils import format_date
from version_control.utils import get_str_hash, build_vcs_relation_tree


class TemplateProcessor:
    """
    A template processor for displaying version difference
    """

    DISPLAY_VALUE_FOR_DELETED = 'УДАЛЕНО'
    MISSED_FIELD_MESSAGE = 'Не удалось найти поле в этой версии'

    def __init__(self, versions):
        self.versions = versions
        self.version_proxies = [version.get_version_proxy() for version in versions if version]
        self.field_names = self.get_common_field_names()
        self.rows = self._fill_rows()

    def _fill_rows(self) -> list:
        rows = list()

        for field_name in self.field_names:
            field_data_dict = dict()
            field_verbose_name = self.get_verbose_name(field_name)

            if field_verbose_name:
                field_data_dict[field_verbose_name] = row_data = dict()
                for index, proxy in enumerate(self.version_proxies):
                    if proxy.version.change_type != ModelObjectChangeType.OBJECT_DELETED:
                        proxy_field = proxy.fields.get(field_name)
                        value = getattr(proxy_field, 'value', self.MISSED_FIELD_MESSAGE)
                    else:
                        value = self.DISPLAY_VALUE_FOR_DELETED

                    row_data[index] = value

                unique_values = set([str(value) for value in field_data_dict.get(field_verbose_name, {}).values()])
                if len(self.version_proxies) == 1 or len(unique_values) > 1:
                    rows.append(field_data_dict)

        return rows

    def get_common_field_names(self) -> set:
        field_names = []

        if self.version_proxies:
            content_type = self.version_proxies[0].version.group.content_type
            model_class = content_type.model_class()
            if model_class:
                field_names = [field.name for field in model_class._meta.get_fields()]
            else:
                field_names = []
                for proxy in self.version_proxies:
                    state = proxy.version.get_state()
                    state_field_names = state['fields'].keys() if state else []
                    field_names.extend(state_field_names)

        return set(field_names)

    def get_verbose_name(self, field_name: str) -> str:
        verbose_name = None
        reserve_name = None

        for proxy in self.version_proxies:
            proxy_field = proxy.fields.get(field_name)

            verbose_name = getattr(proxy_field, 'verbose_name', None)
            if verbose_name:
                break
            if reserve_name is None:
                reserve_name = getattr(proxy_field, 'name', None)

        return verbose_name or reserve_name


class VersionProxy:
    """
    A helper class for displaying version data in templates
    """

    def __init__(self, version: 'ModelObjectVersion', fields: dict):
        self.version = version
        self.fields = fields


class VersionProxyField:
    """
    A helper class for displaying fields data of changed objects in templates
    """

    def __init__(self, name: str, value: Any, field_extra_data: dict):
        self.name = name
        self.verbose_name = field_extra_data.get('verbose_name', name)
        self.internal_type = field_extra_data.get('internal_type')
        self.field_extra_data = field_extra_data
        self.value = self.cast_value(self.internal_type, value)

    def cast_value(self, internal_type: str, value: Any, default: Any = '-') -> Any:
        prepared_value = None
        bad_values = (None, '', ' ')

        if value is not None:
            # if internal_type == 'DateTimeField':
            #     prepared_value = format_date(value, "d.m.Y H:i")
            # elif internal_type == 'DateField':
            #     prepared_value = format_date(value)
            if internal_type == 'BooleanField':
                prepared_value = 'Да' if value else 'Нет'
            elif internal_type in ['CharField', 'ArrayField']:
                prepared_value = self.field_extra_data.get('display_value', value)
            elif internal_type in ['ForeignKey', 'ManyToManyField']:
                prepared_value = self.field_extra_data.get('representation', value)
            else:
                prepared_value = value

        return prepared_value if prepared_value not in bad_values else default


class VersionWrapper:
    """
    A helper wrapper class over modified object
    """

    def __init__(self, model_object: models.Model):
        self.state = model_to_dict(model_object)

    def __eq__(self, other: 'VersionWrapper'):
        return not bool(self.__sub__(other))

    def __ne__(self, other: 'VersionWrapper'):
        return bool(self.__sub__(other))

    def __sub__(self, other: 'VersionWrapper'):
        return self.get_diff(self.state, other.state)

    @staticmethod
    def get_diff(start_state: dict, next_state: dict, check_fields: Collection = None):
        # Get changed fields of an object
        changed_fields = dict()
        common_dict_keys = set(start_state) & set(next_state)
        fields_for_check = check_fields or common_dict_keys
        for key in common_dict_keys:
            if key in fields_for_check and start_state[key] != next_state[key]:
                changed_fields[key] = dict(start_state=start_state[key], next_state=next_state[key])
        return changed_fields


class ModelObjectVersionGroup(models.Model):
    """
    The model for binding versions of model objects (version group)
    """

    representation = models.TextField(verbose_name='Описание объекта')
    verbose_name = models.TextField(verbose_name='Наименование объекта')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    relation_tree = JSONField(verbose_name='Дерево отношений', null=True)
    tree_last_update = models.DateTimeField(verbose_name='Последнее обновление дерева отношений', null=True)

    objects = ModelObjectVersionGroupQuerySet.as_manager()

    class Meta:
        verbose_name = 'Группа версий объекта'
        verbose_name_plural = 'Группы версий объектов'
        unique_together = (('content_type', 'object_id'),)

    def __str__(self):
        return f'Группа версий объекта: {self.representation}'

    @classmethod
    def get_content_type_choices_for_vcs_objects(cls, cache_timeout: int = 120) -> tuple:

        from version_control.service import get_version_manager_class

        def get_choices() -> tuple:
            manager_class = get_version_manager_class()
            model_classes = manager_class().get_version_control_model_classes(to_str=True)
            return tuple(
                (content_type.pk, content_type) for content_type in ContentType.objects.filter(model__in=model_classes)
            )

        return cache.get_or_set('vcs_content_type_choices', default=get_choices, timeout=cache_timeout)

    def update_vcs_relation_tree(self) -> None:
        if self.content_object:
            vcs_tree, vcs_missed_objects_tree = build_vcs_relation_tree(self.content_object)
            self.relation_tree = dict(vcs_relation_tree=vcs_tree,
                                      vcs_missed_objects_relation_tree=vcs_missed_objects_tree)
            self.tree_last_update = tz_now()
            self.save()

    def get_vcs_relation_tree(self) -> Optional[list]:
        data = None
        if self.relation_tree:
            data = self.relation_tree.get('vcs_relation_tree')
        return data

    def get_vcs_missed_objects_relation_tree(self) -> Optional[list]:
        data = None
        if self.relation_tree:
            data = self.relation_tree.get('vcs_missed_objects_relation_tree')
        return data


class ModelObjectVersion(models.Model):
    """
    The model for storing versions of model objects
    """

    group = models.ForeignKey(ModelObjectVersionGroup, related_name='model_object_versions',
                              verbose_name='Группа версий', on_delete=models.CASCADE)
    change_type = models.CharField(verbose_name='Тип изменения объекта', max_length=50,
                                   choices=ModelObjectChangeType.CHOICES, default=ModelObjectChangeType.OBJECT_CHANGED)
    change_url = models.TextField(verbose_name='URL создания версии', null=True)
    change_app = models.TextField(verbose_name='APP создания версии', null=True)
    created = models.DateTimeField(verbose_name='Дата и время версии')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', related_name='model_objects_versions',
                               on_delete=models.SET_NULL, null=True)
    request_key = models.UUIDField(verbose_name='Уникальный ключ request', null=True)
    hash = models.UUIDField(verbose_name='Хэш версии')
    state = JSONField(null=True)

    objects = ModelObjectVersionQuerySet.as_manager()

    class Meta:
        verbose_name = 'Версия объекта'
        verbose_name_plural = 'Версии объектов'
        ordering = ('-created',)

    def __str__(self):
        return f'Версия объекта ({self.hash}) "{self.group.representation}": {format_date(self.created, "d.m.Y H:i")}'

    def get_state(self) -> dict:
        # state may be a string or a dictionary
        loaded_state = json.loads(self.state) if isinstance(self.state, str) else self.state
        return loaded_state[0] if isinstance(loaded_state, list) else loaded_state or {}

    def get_fields(self) -> list:
        # get all fields of the changed object
        fields = []
        model_class = self.group.content_type.model_class()
        if model_class:
            fields = [field.name for field in model_class._meta.local_fields]
        return fields

    def get_version_proxy(self) -> VersionProxy:
        # get and prepare all fields changes
        state = self.get_state()
        fields_extra_data = state.get('fields_extra_data', {})
        version_proxy = VersionProxy(version=self, fields={})
        if state:
            for name, value in state['fields'].items():
                version_proxy.fields[name] = VersionProxyField(name, value, fields_extra_data.get(name, {}))
        return version_proxy

    def is_deleted(self) -> bool:
        return self.change_type == ModelObjectChangeType.OBJECT_DELETED

    @property
    def proxy_object(self) -> models.Model:
        # get the deserialized version state object
        proxy_object = None
        deserialized_state = self.get_state_deserialized()
        if deserialized_state:
            _, proxy_object = deserialized_state
        return proxy_object

    def get_previous_version(self) -> 'ModelObjectVersion':
        return ModelObjectVersion.objects.filter(group=self.group, id__lt=self.id).order_by('-created').first()

    def get_next_version(self) -> 'ModelObjectVersion':
        return ModelObjectVersion.objects.filter(group=self.group, id__gt=self.id).order_by('created').first()

    def is_last_version(self) -> bool:
        return not ModelObjectVersion.objects.filter(group=self.group, id__gt=self.id).exists()

    def get_state_deserialized(self) -> tuple:
        # deserialize the state of a model object stored in version
        deserialized_object, proxy_object = None, None
        if self.state:
            wrapper_generator = serializers.deserialize('json', self.state, ignorenonexistent=True)
            for item in wrapper_generator:
                deserialized_object, proxy_object = item, item.object
                break
        return deserialized_object, proxy_object


class AbstractVersionControl(models.Model):
    """
    The abstract model that provide methods for track model object changes
    """

    VERSION_MANAGER_ENABLED = True  # a flag for turn on / off tracking by version manager

    class Meta:
        abstract = True

    @classmethod
    def from_db(cls, db, field_names, values):
        # record initial state of fields
        instance = super().from_db(db, field_names, values)
        setattr(instance, 'initial_field_names', field_names)
        setattr(instance, 'initial_values', values)
        return instance

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # check for changes (or for adding an object)
        object_changed = self.VERSION_MANAGER_ENABLED and (self.check_changes() or self._state.adding)
        super().save(force_insert, force_update, using, update_fields)
        if object_changed:
            self.handle_version()

    def handle_version(self, **kwargs) -> None:

        from version_control.service import get_version_manager_class

        # set object hash for debug info collector
        Debugger.HASH = self.get_hash()

        manager_class = get_version_manager_class()
        manager = manager_class()
        # verify storage if it is not verified yet
        manager.provide_storage_verification()
        # adding an object to the temporary storage for further processing
        # If there is a 'request' - recording is done through temporary storage
        if manager.can_fill_storage():
            manager.add_object_to_storage(self, **kwargs)
        # If not, synchronously with saving the object (necessary when executing commands through manage.py)
        else:
            manager.create_version_from_objects(self, **kwargs)

    def get_hash(self) -> str:
        # get the hash value of the current object
        hash_data_string = f'{self.__class__.__name__}-{self.id}'
        return str(get_str_hash(hash_data_string, digest_size=5))

    def check_changes(self) -> bool:
        # check changes of the model object after the first initialization
        object_changed = False
        initial_field_names = getattr(self, 'initial_field_names', None)
        initial_values = getattr(self, 'initial_values', None)
        if initial_field_names and initial_values:
            current_values = tuple(self.__dict__.get(field_name) for field_name in initial_field_names)
            object_changed = current_values != initial_values
        return object_changed
