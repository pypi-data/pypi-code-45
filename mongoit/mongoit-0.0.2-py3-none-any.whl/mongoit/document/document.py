from .field_access import FieldAccess
from ..fields import ObjectField


class Document(object):
    """
    """

    def __init__(self, object_field):
        self.__field = object_field

    def __getattr__(self, name):
        return self[name]

    def __getitem__(self, key):
        sub_field = self.__field.get_field(key)
        name = self.__field.get_field_name(key)
        return FieldAccess(key, name, sub_field)
