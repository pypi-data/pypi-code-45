import six
from bson.son import SON
from bson.py3compat import iteritems

from .field import Field
from .const_field import ConstField


class ObjectFieldsMeta(type):
    """
    """
    def __init__(cls, name, bases, local_dict):
        super(ObjectFieldsMeta, cls).__init__(name, bases, local_dict)
        cls._fieldbases = [cls]
        for base in bases:
            if isinstance(base, ObjectFieldsMeta):
                cls._fieldbases.append(base)


@six.add_metaclass(ObjectFieldsMeta)
class ObjectFields(object):
    """

    """

    def __init__(self):
        """
        """
        object.__setattr__(self, '_fields', SON())
        for base in reversed(self._fieldbases):
            for attr_name in dir(base):
                if not hasattr(ObjectFields, attr_name):
                    attr = getattr(base, attr_name)
                    setattr(self, attr_name, attr)

    def __repr__(self):
        items = ', '.join(map(repr, self.iteritems()))
        return "%s([%s])" % (type(self).__name__, items)

    def __getattr__(self, name):
        """
        """
        if name in self._fields:
            return self._fields[name]
        raise AttributeError("%s has no attribute '%s'" % (self, name))

    def __setattr__(self, name, value):
        """
        """
        self[name] = value

    def __delattr__(self, name):
        if name in self._fields:
            del self[name]
        else:
            super(ObjectFields, self).__delattr__(name)

    def __getitem__(self, key):
        return self._fields[key]

    def __setitem__(self, key, value):
        """
        """
        order_index = None
        if value is NotImplemented:
            if key in self._fields:
                attr = self._fields.get(key)
                if isinstance(attr, Field):
                    del self._fields[key]
        else:
            if not isinstance(value, Field):
                value = ConstField(value)
            self._fields[key] = value
            if order_index is not None:
                self._order[key] = order_index

    def __delitem__(self, key):
        del self._fields[key]

    def __iter__(self):
        for key, _ in self.iteritems():
            yield key

    def __bool__(self):
        return bool(self._fields)

    def update(self, fields=None, **kwargs):
        """
        """
        if fields is None:
            pass
        elif isinstance(fields, SON):
            for key, field in fields.iteritems():
                setattr(self, key, field)
        elif isinstance(fields, dict):
            for key, field in iteritems(fields):
                setattr(self, key, field)
        else:
            for key, field in fields:
                setattr(self, key, field)
        if kwargs:
            self.update(kwargs)

    def get(self, key, default=None):
        """
        """
        return self._fields.get(key, default)

    def getitem(self, value, default=None):
        """
        """
        if value is not None:
            for key, field in self.iteritems():
                if key == value or field == value:
                    return (key, field)
        return default

    def iteritems(self):
        """
        """
        fields = self._fields
        # if self._order:
        #     # Copy the fields in to a SON so we could pop items from it.
        #     fields = SON(fields)
        #     for key, _ in sorted(iteritems(self._order), key=lambda o: o[1]):
        #         field = fields.pop(key, None)
        #         if field is not None:
        #             yield key, field
        for item in fields.iteritems():
            yield item

    def itervalues(self):
        """
        """
        for _, field in self.iteritems():
            yield field
