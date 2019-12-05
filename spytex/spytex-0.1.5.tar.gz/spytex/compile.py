"""Functions to extract Definitions from JSON-like objects representation."""


import collections.abc
from typing import Any, Mapping

from .defs import (Definition, ConcreteValue, NameReference, Call, SeqDef,
                   DictDef, ContextValue, ContextBinder, SequentialRun)
from .magics import get_magic


def _compile_dict_vals(mapping: Mapping[Any, Any]) -> Mapping[Any, Definition]:
    return {key: compile(val) for key, val in mapping.items()}


def compile(obj: Any) -> Definition:
    """Extract a definition from a JSON-like object representation."""
    if isinstance(obj, collections.abc.Mapping):
        if len(obj) == 1:
            key, val = next(iter(obj.items()))
            if key.startswith("!"):
                key = key[1:]
                if key == "sequential":
                    steps = []
                    for step in val:
                        name = None,
                        if (isinstance(step, collections.abc.Mapping)
                                and ":=" in step):
                            step = step.copy()
                            name = step.pop(":=")
                        step = compile(step)
                        steps.append((step, name))
                    return SequentialRun(steps)
                if key:
                    arg = compile(val)
                magic = get_magic(key)
                if magic:
                    pass_context = getattr(magic, "_pass_context", False)
                    return Call(ConcreteValue(magic), [arg],
                                pass_context=1 if pass_context else None)
                elif key:
                    return Call(NameReference(key), [arg])
            elif key == "=":
                return ContextValue(val)
            elif key == ".":
                return NameReference(val)
        if "=" in obj:
            obj = obj.copy()
            values = _compile_dict_vals(obj.pop("="))
            wrapped = compile(obj)
            return ContextBinder(values, wrapped)
        elif "!" in obj:
            obj = obj.copy()
            callee = obj.pop("!")
            posargs = list(map(compile, obj.pop("*", [])))
            kwargs = _compile_dict_vals(obj)
            return Call(NameReference(callee), posargs, kwargs)
        else:
            return DictDef(_compile_dict_vals(obj))
    elif (isinstance(obj, collections.abc.Sequence)
            and not isinstance(obj, (str, bytes, bytearray))):
        return SeqDef(list, map(compile, obj))
    else:
        return ConcreteValue(obj)
