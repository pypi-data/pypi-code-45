# -*- coding: utf-8 -*-

import ast
from typing import Set

from wemake_python_styleguide.compat.aliases import AssignNodes, FunctionNodes
from wemake_python_styleguide.logic.source import node_to_string

#: That's what we expect from `@overload` decorator:
_overload_exceptions = frozenset(('overload', 'typing.overload'))

#: That's what we expect from `@property` decorator:
_property_exceptions = frozenset(('property', '.setter'))


def is_function_overload(node: ast.AST) -> bool:
    """Check that function decorated with `typing.overload`."""
    if isinstance(node, FunctionNodes):
        for decorator in node.decorator_list:
            if node_to_string(decorator) in _overload_exceptions:
                return True
    return False


def is_property_setter(node: ast.AST, _=None):
    """Check that function decorated with `property.setter`."""
    if isinstance(node, FunctionNodes):
        for decorator in node.decorator_list:
            if node_to_string(decorator) in _property_exceptions:
                return True
    return False


def is_same_value_reuse(node: ast.AST, names: Set[str]) -> bool:
    """Checks if the given names are reused by the given node."""
    if isinstance(node, AssignNodes) and node.value:
        used_names = {
            name_node.id
            for name_node in ast.walk(node.value)
            if isinstance(name_node, ast.Name)
        }
        if not names.difference(used_names):
            return True
    return False


def is_no_value_annotation(node: ast.AST, _=None) -> bool:
    """Check that variable has annotation without value."""
    return isinstance(node, ast.AnnAssign) and not node.value
