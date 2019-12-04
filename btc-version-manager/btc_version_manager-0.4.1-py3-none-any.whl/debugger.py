import time
from collections import OrderedDict
from functools import partial, wraps
from typing import Optional, Callable, Union

from django.conf import settings
from django.db import connection, reset_queries


class Debugger:
    """
    A class for collecting the debug information
    """

    INFO: OrderedDict = OrderedDict()
    HASH: str = 'unknown'

    @classmethod
    def store_data(cls, data: str) -> None:
        """
        Saves debug info to INFO dict
        """

        if cls.HASH not in cls.INFO:
            cls.INFO[cls.HASH] = []

        cls.INFO[cls.HASH] += [data]

    @classmethod
    def get_report(cls) -> str:
        """
        Returns result report string
        """

        data_dict = cls.INFO or {}
        report_string = ''
        for key, value in data_dict.items():
            report_string += f'{key}\n'
            for item in value:
                report_string += f'\r{item}\n'

        cls.flush()
        return report_string

    @classmethod
    def flush(cls) -> None:
        cls.INFO = OrderedDict()


def version_manager_debug_formatter() -> str:
    return str(Debugger.HASH) + ': {func_name!r} за {run_time:.4f} сек, запросов: {queries_count}'


def debug_method(func: Optional[Callable] = None, *,
                 use_setting: str = 'VERSION_MANAGER_DEBUG',
                 formatter: Union[str, Callable] = version_manager_debug_formatter,
                 prefix: str = '',
                 postfix: str = ''):
    """
    Print the runtime of the decorated function
    """

    if func is None:
        return partial(debug_method, use_setting=use_setting, formatter=formatter, prefix=prefix, postfix=postfix)

    @wraps(func)
    def wrapper(*args, **kwargs):
        if use_setting and getattr(settings, use_setting, False) or not use_setting:
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            prepared_format = formatter() if hasattr(formatter, '__call__') else formatter
            message = prefix + prepared_format.format(
                func_name=func.__name__, run_time=run_time, queries_count=len(connection.queries)) + postfix
            Debugger.store_data(message)
            # reset queries count by django built-in func
            reset_queries()
            print(message)
        else:
            value = func(*args, **kwargs)
        return value
    return wrapper
