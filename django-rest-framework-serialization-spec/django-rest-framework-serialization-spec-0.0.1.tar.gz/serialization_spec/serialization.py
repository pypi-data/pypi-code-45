from django.db.models import Prefetch
from rest_framework.utils import model_meta
from rest_framework.fields import Field
from rest_framework.serializers import ModelSerializer
from zen_queries.rest_framework import QueriesDisabledViewMixin

from typing import List, Dict, Union
from collections import OrderedDict

"""
Parse a serialization spec such as:

class ProductVersionDetail(SerializationSpecMixin, generics.RetrieveAPIView):

    queryset = ProductVersion.objects.all()
    serialization_spec = [
        'id',
        {'product': [
            'id',
            'name'
        ]},
        {'report_templates': [
            'id',
            'name'
        ]}
    ]

1. fetch the data required to populate this
2. output it

mixin should implement get_queryset() and get_serializer()

"""


class SerializerLambdaField(Field):
    def __init__(self, impl, **kwargs):
        self.impl = impl
        kwargs['source'] = '*'
        kwargs['read_only'] = True
        super().__init__(**kwargs)

    def to_representation(self, value):
        return self.impl(value)


class SerializationSpecPlugin:
    """ These methods can access self.key to get the key """

    def modify_queryset(self, queryset):
        return queryset

    # abstract method
    def get_value(self, instance):
        raise NotImplementedError


class Filtered:
    def __init__(self, filters, serialization_spec):
        self.filters = filters
        self.serialization_spec = serialization_spec


def get_fields(serialization_spec):
    return sum(
        [list(x.keys()) if isinstance(x, dict) else [x] for x in serialization_spec],
        []
    )


def get_only_fields(model, serialization_spec):
    field_info = model_meta.get_field_info(model)
    fields = set(field_info.fields_and_pk.keys()) | set(field_info.forward_relations.keys())
    return [
        field for field in get_fields(serialization_spec)
        if field in fields
    ]


def get_childspecs(serialization_spec):
    return [each for each in serialization_spec if isinstance(each, dict)]


def make_serializer_class(model, serialization_spec):
    relations = model_meta.get_field_info(model).relations

    return type(
        'MySerializer',
        (ModelSerializer,),
        {
            'Meta': type(
                'Meta',
                (object,),
                {'model': model, 'fields': get_fields(serialization_spec)}
            ),
            **{
                key: SerializerLambdaField(impl=lambda value: [str(each.id) for each in getattr(value, key).all()])
                for key in get_only_fields(model, serialization_spec)
                if key in relations and relations[key].to_many
            },
            **{
                key: (
                    SerializerLambdaField(impl=values.get_value) if isinstance(values, SerializationSpecPlugin)
                    else make_serializer_class(
                        relations[key].related_model,
                        values.serialization_spec if isinstance(values, Filtered) else values
                    )(many=relations[key].to_many)
                )
                for key, values
                in [item for each in get_childspecs(serialization_spec) for item in each.items()]
            },
        }
    )


def has_plugin(spec):
    return any(
        isinstance(childspec, SerializationSpecPlugin) or has_plugin(childspec)
        for each in spec if isinstance(each, dict)
        for key, childspec in each.items()
    )


def prefetch_related(queryset, model, prefixes, serialization_spec, use_select_related):
    relations = model_meta.get_field_info(model).relations

    for each in serialization_spec:
        if isinstance(each, dict):
            for key, childspec in each.items():
                key_path = '__'.join(prefixes + [key])

                if isinstance(childspec, SerializationSpecPlugin):
                    childspec.key = key
                    queryset = childspec.modify_queryset(queryset)

                else:
                    if isinstance(childspec, Filtered):
                        filters = childspec.filters
                        childspec = childspec.serialization_spec
                    else:
                        filters = None

                    relation = relations[key]
                    related_model = relation.related_model

                    if (relation.model_field and relation.model_field.one_to_one) or (use_select_related and not relation.to_many) and not has_plugin(childspec):
                        # no way to .only() on a select_related field
                        queryset = queryset.select_related(key_path)
                        queryset = prefetch_related(queryset, related_model, prefixes + [key], childspec, use_select_related)
                    else:
                        only_fields = get_only_fields(related_model, childspec)
                        if relation.reverse and not relation.has_through_model:
                            # need to include the reverse FK to allow prefetch to stitch results together
                            # Unfortunately that info is in the model._meta but is not in the RelationInfo tuple
                            reverse_fk = next(
                                rel.field.name
                                for rel in model._meta.related_objects
                                if rel.get_accessor_name() == key
                            )
                            only_fields += ['%s_id' % reverse_fk]
                        inner_queryset = prefetch_related(related_model.objects.only(*only_fields), related_model, [], childspec, use_select_related)
                        if filters:
                            inner_queryset = inner_queryset.filter(filters)
                        queryset = queryset.prefetch_related(Prefetch(key_path, queryset=inner_queryset))
        else:
            if each in relations:
                relation = relations[each]
                if relation.to_many:
                    related_model = relation.related_model
                    key_path = '__'.join(prefixes + [each])
                    inner_queryset = related_model.objects.only('id')
                    queryset = queryset.prefetch_related(Prefetch(key_path, queryset=inner_queryset))

    return queryset


def expand_nested_specs(serialization_spec):
    return serialization_spec + sum([
        getattr(childspec, 'serialization_spec', [])
        for each in serialization_spec if isinstance(each, dict)
        for key, childspec in each.items() if isinstance(childspec, SerializationSpecPlugin)
    ], [])


class NormalisedSpec:
    def __init__(self):
        self.spec = None
        self.fields = OrderedDict()
        self.relations = OrderedDict()


def normalise_spec(serialization_spec):
    def normalise(spec, normalised_spec):
        if isinstance(spec, SerializationSpecPlugin) or isinstance(spec, Filtered):
            normalised_spec.spec = spec
            return

        for each in spec:
            if isinstance(each, dict):
                for key, childspec in each.items():
                    if key not in normalised_spec.relations:
                        normalised_spec.relations[key] = NormalisedSpec()
                    normalise(childspec, normalised_spec.relations[key])
            else:
                normalised_spec.fields[each] = True

    def combine(normalised_spec):
        return normalised_spec.spec or (
            list(normalised_spec.fields.keys()) + ([{
                key: combine(value)
                for key, value in normalised_spec.relations.items()
            }] if normalised_spec.relations else [])
        )

    normalised_spec = NormalisedSpec()
    normalise(serialization_spec, normalised_spec)
    return combine(normalised_spec)


class SerializationSpecMixin(QueriesDisabledViewMixin):

    serialization_spec = None  # type: SerializationSpec

    def get_object(self):
        self.use_select_related = True
        return super().get_object()

    def get_queryset(self):
        queryset = self.queryset
        serialization_spec = expand_nested_specs(self.serialization_spec)
        serialization_spec = normalise_spec(serialization_spec)
        queryset = queryset.only(*get_only_fields(queryset.model, serialization_spec))
        queryset = prefetch_related(queryset, queryset.model, [], serialization_spec, getattr(self, 'use_select_related', False))
        return queryset

    def get_serializer_class(self):
        return make_serializer_class(self.queryset.model, self.serialization_spec)


"""
serialization_spec type should be

    SerializationSpec = List[Union[str, Dict[str, Union[SerializationSpecPlugin, 'SerializationSpec']]]]

But recursive types are not yet implemented :(
So we specify to an (arbitrary) depth of 5
"""
SerializationSpec = List[Union[str, Dict[str, Union[Filtered, SerializationSpecPlugin,
    List[Union[str, Dict[str, Union[Filtered, SerializationSpecPlugin,
        List[Union[str, Dict[str, Union[Filtered, SerializationSpecPlugin,
            List[Union[str, Dict[str, Union[Filtered, SerializationSpecPlugin,
                List[Union[str, Dict[str, Union[Filtered, SerializationSpecPlugin,
                    List]]]]
            ]]]]
        ]]]]
    ]]]]
]]]]
