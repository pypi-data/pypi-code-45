# Licensed under a 3-clause BSD style license - see LICENSE.rst

from types import FunctionType
from contextlib import contextmanager
from functools import wraps

from astropy.table import QTable

__all__ = ['BaseTimeSeries', 'autocheck_required_columns']

COLUMN_RELATED_METHODS = ['add_column',
                          'add_columns',
                          'keep_columns',
                          'remove_column',
                          'remove_columns',
                          'rename_column']


def autocheck_required_columns(cls):
    """
    This is a decorator that ensures that the table contains specific
    methods indicated by the _required_columns attribute. The aim is to
    decorate all methods that might affect the columns in the table and check
    for consistency after the methods have been run.
    """

    def decorator_method(method):

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            self._check_required_columns()
            return result

        return wrapper

    for name in COLUMN_RELATED_METHODS:
        if (not hasattr(cls, name) or
                not isinstance(getattr(cls, name), FunctionType)):
            raise ValueError("{0} is not a valid method".format(name))
        setattr(cls, name, decorator_method(getattr(cls, name)))

    return cls


class BaseTimeSeries(QTable):

    _required_columns = None
    _required_columns_enabled = True

    # If _required_column_relax is True, we don't require the columns to be
    # present but we do require them to be the correct ones IF present. Note
    # that this is a temporary state - as soon as the required columns
    # are all present, we toggle this to False
    _required_columns_relax = False

    def _check_required_columns(self):

        if not self._required_columns_enabled:
            return

        if self._required_columns is not None:

            if self._required_columns_relax:
                required_columns = self._required_columns[:len(self.colnames)]
            else:
                required_columns = self._required_columns

            plural = 's' if len(required_columns) > 1 else ''

            if not self._required_columns_relax and len(self.colnames) == 0:

                raise ValueError("{0} object is invalid - expected '{1}' "
                                 "as the first column{2} but time series has no columns"
                                 .format(self.__class__.__name__, required_columns[0], plural))

            elif self.colnames[:len(required_columns)] != required_columns:

                raise ValueError("{0} object is invalid - expected '{1}' "
                                 "as the first column{2} but found '{3}'"
                                 .format(self.__class__.__name__, required_columns[0], plural, self.colnames[0]))

            if (self._required_columns_relax
                    and self._required_columns == self.colnames[:len(self._required_columns)]):
                self._required_columns_relax = False

    @contextmanager
    def _delay_required_column_checks(self):
        self._required_columns_enabled = False
        yield
        self._required_columns_enabled = True
        self._check_required_columns()
