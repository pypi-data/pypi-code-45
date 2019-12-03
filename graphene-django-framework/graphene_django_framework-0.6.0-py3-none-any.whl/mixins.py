from functools import partial

import graphene
from graphene_django.utils import maybe_queryset
from graphene_django.filter.utils import get_filtering_args_from_filterset
from django_filters.filterset import filterset_factory
from django.core.paginator import Paginator

from .paginator import PageType
from .utils import select_resolver


class PaginationMixin(object):
    """ Adds pagination functionality to a Field.

        Relies on the created Paginator type for the passed ModelObjectType located in the Meta.
    """

    def __init__(self, _type,
                 type_meta=None,
                 per_page=graphene.Int(default_value=100),
                 orphans=graphene.Int(default_value=0),
                 page=graphene.Int(default_value=1),
                 *args, **kwargs):
        kwargs.update(per_page=per_page,
                      orphans=orphans,
                      page=page)
        _meta = type_meta or _type._meta

        assert getattr(_meta, 'paginator', False), '{} needs to have a paginator.'.format(_type)
        self.paginator_type = _meta.paginator

        super(PaginationMixin, self).__init__(self.paginator_type, *args, **kwargs)

    @classmethod
    def page_resolver(cls, resolver, _type, root, info,
                      per_page: int = None,
                      page: int = None,
                      orphans: int = None,
                      **args):
        selected_resolver = select_resolver(resolver, _type.object_list.of_type, root)
        pager_ret = selected_resolver(root, info, **args)
        paginator = Paginator(maybe_queryset(pager_ret), per_page=per_page, orphans=orphans)
        page = paginator.page(page)
        return _type(
            page_info=PageType(paginator=paginator, page=page,),
            object_list=page.object_list,
        )

    def get_resolver(self, parent_resolver):
        return partial(self.page_resolver, self.resolver or parent_resolver, self.get_type())

    def get_type(self):
        """ Return the type that we are using in the class resolver. """
        return self.paginator_type


class FilterMixin(object):
    """ Adds filtering functionality to a Field.

        Uses defined filter_fields on the ModelObjectType's Meta or a passed custom FilterSet.
    """

    def __init__(self, _type, filter_set_class=None, type_meta=None, *args, **kwargs):
        _meta = type_meta or _type._meta

        # Passing in a custom FilterSet class
        if filter_set_class is not None:
            self._filter_set_class = filter_set_class

        else:
            # filter_fields specified in type's meta
            if getattr(_meta, 'filter_fields', False):
                self._filter_set_class = filterset_factory(_meta.model, fields=_meta.filter_fields)

            else:
                raise NotImplementedError('No filters found. '
                                          'Specify filter_fields through the type\'s Meta, '
                                          'or pass a FilterSet to the Field.')

        # get_filtering_args_from_filterset() doesn't actually use the passed type, but it's a required param so we
        # have to pass it anyways
        filter_args = get_filtering_args_from_filterset(self._filter_set_class, _type)
        kwargs.update(filter_args)

        self.model_type = _meta.paginator.object_list.of_type

        super(FilterMixin, self).__init__(_type, *args, **kwargs)

    @classmethod
    def filter_resolver(cls, resolver, _type, filter_set_class, root, info, **args):
        selected_resolver = select_resolver(resolver, _type, root)
        parent_ret = selected_resolver(root, info, **args)

        if parent_ret is None:
            parent_ret = _type._meta.model._default_manager.none()

        # TODO: Get only filtering arguments from args
        filter_set = filter_set_class(data=args, queryset=maybe_queryset(parent_ret), request=info.context)

        return filter_set.qs

    def get_resolver(self, parent_resolver):
        return partial(self.filter_resolver, self.resolver or parent_resolver, self.get_type(), self._filter_set_class)

    def get_type(self):
        """ Return the type that we are using in the class resolver. """
        return self.model_type
