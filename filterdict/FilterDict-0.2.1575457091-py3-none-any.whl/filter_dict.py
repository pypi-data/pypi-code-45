import inspect


def filter_dict(dict_to_filter, keywords, default=None):
    new_dict = {key: dict_to_filter.get(key, default) for key in keywords}
    return new_dict


def get_method_keywords(method, return_contains_args_kwargs=True):
    sig = inspect.signature(method)
    filter_keys = {
        param.name:param.default if param.default is not inspect._empty else None
        for param in sig.parameters.values()
        if param.kind == param.POSITIONAL_OR_KEYWORD or param.kind == param.KEYWORD_ONLY
    }
    if not return_contains_args_kwargs:
        return filter_keys
    return (
        filter_keys,
        len(
            [
                param.name
                for param in sig.parameters.values()
                if param.kind == param.VAR_POSITIONAL
            ]
        )
        > 0,
        len(
            [
                param.name
                for param in sig.parameters.values()
                if param.kind == param.VAR_KEYWORD
            ]
        )
        > 0,
    )


def call_method(target, args=None, kwargs=None):
    if kwargs is None:
        kwargs = {}
    if args is None:
        args = []
    target_dict = get_method_keywords(target,return_contains_args_kwargs=False)
    keys_needed=list(target_dict.keys())
    target_dict.update(kwargs)
    target_dict = filter_dict(dict_to_filter=target_dict, keywords=keys_needed)
    return target(**target_dict)


if __name__ == "__main__":

    def f(a, b=None, **kwargs):
        print(a, b, kwargs)

    kwargs = {"a": 0, "b": 1, "c": 2}

    target_keywords, with_args, with_kwargs = get_method_keywords(f)

    print(target_keywords, with_args, with_kwargs)
    print(filter_dict(dict_to_filter=kwargs, keywords=target_keywords))
    call_method(f, kwargs=kwargs)
