import sys

from .abstract_resource import AbstractResource
from .simulator.resource import Resource


__this = sys.modules[__name__]
__this.actual_environment = False
__this.created_resources = []


def initialize_real_environment():
    if hasattr(sys, '_called_from_test'):
        sys.exit('Code related by the actual environment isnt supposed to be executed by pytest directly.')
    __this.actual_environment = True


def create_resource_class(cls_name: str,
                          resource_cls: AbstractResource) -> AbstractResource:
    return type(cls_name, (resource_cls,), {})


def select_resource_class(cls_name: str,
                          fake_resource_cls: Resource,
                          real_resource_cls: AbstractResource) -> AbstractResource:
    '''Select between a Fake or Real resource class based on the
    environment that the resource will be implemented

    '''
    assert issubclass(fake_resource_cls, Resource), 'Expecting a fake resource'
    assert not issubclass(real_resource_cls, Resource), 'Expecting a real resource'
    cls = create_resource_class(cls_name, fake_resource_cls)
    if __this.actual_environment:
        cls = create_resource_class(cls_name, real_resource_cls)

    if cls.__name__ in __this.created_resources:
        raise RuntimeError(f'Resource {cls} already created. See if select_resource_class is being called with the correct args')

    __this.created_resources.append(cls.__name__)
    return cls
