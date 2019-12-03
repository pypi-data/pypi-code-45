from typing import Callable, Any, Dict
from collections import defaultdict
import warnings

from arps.core.abstract_resource import AbstractResource


class ResourcesTableError(Exception):
    '''Error raised when there is something wrong while manipulating the
    resources in the table

    '''


class ResourcesPerEnvironment:
    '''
    This class organizes the resources by their categories.
    '''

    def __init__(self):
        self._resources: Dict[str, AbstractResource] = defaultdict(dict)

    def _add_resource_instance(self, resource_instance: AbstractResource):
        if resource_instance.identifier in self._resources:
            raise ResourcesTableError('Resource already registered')
        self._resources[resource_instance.identifier] = resource_instance

    def resource(self, identifier: str) -> AbstractResource:
        '''
        Return resource by its global unique identifier

        If resource not found, raise ResourcesTableError
        '''
        if identifier not in self._resources:
            raise ResourcesTableError('Resource not found in ResourcesTable')

        return self._resources[identifier]

    def __contains__(self, identifier: str) -> bool:
        return identifier in self._resources


class ResourcesTable:
    '''
    Resources table organizes resources hierarchically:
    - Agent Manager Identifier (which environment the resource is part)
    -- Resources organized by their categories (which category the
       resource is classified)
    '''

    def __init__(self):
        self.environments = defaultdict(ResourcesPerEnvironment)

    def add_resource(self, resource_instance: AbstractResource):
        '''
        Add resource into the resources table. Resources are grouped
        by environment and category

        Args:
        - resource_instance: instance of class AbstractResource
        '''
        assert isinstance(resource_instance, AbstractResource)
        self.environments[resource_instance.environment_identifier]._add_resource_instance(resource_instance)

    def resources_from_environment(self, *, environment: int) -> ResourcesPerEnvironment:
        '''
        Return all categories from a specific environment

        Args:
        - environment: environment identifier
        '''
        return self.environments[environment]

    def add_resources_listener(self, logger: Callable[[Any], bool]):
        '''
        Invoke logger when a resource is modified

        Args:
        - logger: a function expecting a Resouce.Event as parameter to be logged
        '''
        try:
            for resource in self.resources():
                resource.add_listener(logger)
        except AttributeError:
            warnings.warn('This isn\'t supposed to be invoked in real resources')

    def remove_resources_listener(self, logger: Callable[[Any], bool]):
        '''
        Remove logger attached to each resource

        Args:
        - logger: a function expecting a Resouce.Event as parameter to be logged
        '''
        try:
            for resource in self.resources():
                resource.remove_listener(logger)
        except AttributeError:
            warnings.warn('This isn\'t supposed to be invoked in real resources')

    def reset(self):
        '''
        Reset resource state when resource is a fake resource, otherwise do nothing
        '''
        try:
            for resource in self.resources():
                resource.reset()
        except AttributeError:
            warnings.warn('This isn\'t supposed to be invoked in real resources')
            return

    def resources(self):
        '''
        Generator of all resources
        '''
        for environment in self.environments.values():
            for resource in environment._resources.values():
                yield resource
