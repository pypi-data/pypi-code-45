"""A constant value within a Mongo document."""

from .field import Field


class ConstField(Field):
    """
    """

    nullable = False

    def __init__(self, value, name=None, nullable=None, required=None,
                 get_default=None, **kwargs):
        """Defines a constant value of a field in MongoDB.

        :Parameters:
          - `value`: The value of field.
          - `**kwargs` (optional): See the documentation about
            :class:`~mongomodals.field.Field` for the full details.
        """
        super(ConstField, self).__init__(name=name, nullable=nullable,
                                         required=required,
                                         get_default=get_default, **kwargs)
        self.value = value

    def __repr__(self):
        return "%s<%r>" % (super(ConstField, self).__repr__(), self.value)

    def validate(self, value):
        """Raises :class:`TypeError` if `value` is not equals to this field's
        constant value.
        """
        if super(ConstField, self).validate(value):
            return True
        if value != self.value:
            raise TypeError("value %s must be equals to %s" %
                            (value, self.value))
