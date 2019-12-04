
"""
This module contains functions that can be used as decorators or
context managers.
"""

from yaci import cache_manager
from yaci import dict_storage


def cache(storage=None):
    """
    Decorator for wrapping functions that require caching
    """
    # TODO: Consider adding expiration for invalidating cache
    storage = dict_storage.DictStorage() if storage is None else storage

    def wrap(func):
        cm = cache_manager.CacheManager(storage=storage)

        def wrapped_f(*args, **kwargs):
            # Can introspection be used to get complete namespace of func?
            result = cm.default_get((func.__name__, args), func, *args)
            return result
        return wrapped_f
    return wrap


# I am not sure that this is actually useful, but I'll leave it
# here for now
class CacheContext(object):
    """
    Implementation of the Context Manager Protocol that can be used iwth
    a CacheManager.
    """

    def __init__(self, storage=None):
        storage = storage if storage is not None else dict_storage.DictStorage()
        self.cache_manager = cache_manager.CacheManager(storage=storage)

    def __enter__(self):
        return self.cache_manager

    def __exit__(self, exec_type, exec_val, exc_tb):
        try:
            # TODO: This exposes too much of the implementation
            #       Figure out if htere is somehting else we can do.
            self.cache_manger.close()
        except AttributeError:
            pass
