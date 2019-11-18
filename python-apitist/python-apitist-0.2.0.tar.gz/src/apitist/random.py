import typing

import attr

from apitist.utils import has_args, is_attrs_class, is_sequence, is_tuple

from .logging import Logging

T = typing.TypeVar("T")


class Randomer:
    _types_dict = None

    def __init__(self):
        self._types_dict = dict()

    @property
    def available_hooks(self):
        return self._types_dict

    def get_hook(self, t: typing.Type):
        """Get function for given type"""
        func = self._types_dict.get(t)
        if func is None:
            raise TypeError("Unable to find hook for {} type".format(t))
        return func

    def run_hook(self, t: typing.Type):
        """Generate random data for given type"""
        res = self.get_hook(t)()
        Logging.logger.debug("Generated data for type %s: %s", t, res)
        return res

    def add_type(self, t: typing.Type[T], func: typing.Callable[[], T]):
        """
        Add new type for random generation.
        Function should return given type.
        """
        if t in self._types_dict:
            Logging.logger.warning(
                "Type %s already exists in dict, overriding", t
            )
        Logging.logger.debug("Registering type %s with function %s", t, func)
        self._types_dict[t] = func

    def add_types(
        self, types_dict: typing.Dict[typing.Type[T], typing.Callable[[], T]]
    ):
        """
        Add new types for random generation.
        Functions should return given type.
        """
        Logging.logger.debug("Registering list of types: %s", types_dict)
        self._types_dict.update(types_dict)

    def random_object(
        self,
        t: typing.Type[T],
        required_only=False,
        ignore: typing.List[str] = None,
        inverse=False,
        **set_params,
    ) -> T:
        """
        Create object of given type with random data

        Be careful, random object does not use converter to create a type
        It may lead to types missmatch

        :param t: Type which would me generated randomly
        :param required_only: Use only fields which do not have default values
        :param ignore: List of fields which should be ignored
        :param inverse: Inverse ignore list
        :param set_params: Custom params which would be manually set to type
        :return: Object of given type
        """
        Logging.logger.debug("Generating random data for type %s", t)
        if ignore is None:
            ignore = list()
        if t in self.available_hooks:
            return self.run_hook(t)
        elif is_attrs_class(t):
            data = {}
            for field in attr.fields(t):
                f_name = field.name
                has_default = field.default is not attr.NOTHING
                if f_name in set_params:
                    data[f_name] = set_params[f_name]
                    continue
                if (
                    (f_name in ignore and inverse is False)
                    or (ignore and f_name not in ignore and inverse is True)
                    or (required_only and has_default)
                ):
                    data[f_name] = field.default if has_default else None
                    continue
                data[f_name] = self.random_object(
                    field.type,
                    required_only=required_only,
                    ignore=ignore,
                    inverse=inverse,
                    **set_params,
                )
            data = t(**data)
            Logging.logger.debug(
                "Generating random data for attrs type %s", data
            )
            return data
        elif is_tuple(t) and has_args(t):
            return (
                self.random_object(
                    t.__args__[0],
                    required_only=required_only,
                    ignore=ignore,
                    inverse=inverse,
                    **set_params,
                ),
            )
        elif is_sequence(t) and has_args(t):
            return [
                self.random_object(
                    t.__args__[0],
                    required_only=required_only,
                    ignore=ignore,
                    inverse=inverse,
                    **set_params,
                )
            ]
        return None

    object = random_object

    def random_partial(
        self, t: typing.Type[T], use: list = (), **set_params
    ) -> T:
        """
        Create object of given type with random data with only given fields.
        """
        if t in self.available_hooks:
            return self.run_hook(t)
        elif "__attrs_attrs__" in dir(t):
            data = {}
            for field in attr.fields(t):
                key = field.name

                if set_params and key in set_params:
                    data[key] = set_params[key]
                    continue

                if (
                    use
                    and key not in use
                    and "__attrs_attrs__" not in dir(field.type)
                ):
                    data[key] = attr.NOTHING
                    continue

                data[key] = self.random_partial(field.type, use, **set_params)

            return t(**data)

        elif is_tuple(t) and has_args(t):
            return (self.random_partial(t.__args__[0], use=use, **set_params),)
        elif is_sequence(t) and has_args(t):
            return [self.random_partial(t.__args__[0], use=use, **set_params)]
        return None

    partial = random_partial
