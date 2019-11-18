"""Module in charge of generating mocks."""

import os
import re
from copy import deepcopy

from jinja2 import Environment
from jinja2 import PackageLoader
from pycparser import c_ast as node
from pycparser.c_generator import CGenerator

from . import __version__


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def is_ellipsis(param):
    return isinstance(param, node.EllipsisParam)


def is_char_pointer(param):
    if is_ellipsis(param):
        return False
    elif isinstance(param.type, node.PtrDecl):
        if isinstance(param.type.type, (node.FuncDecl, node.PtrDecl)):
            return False
        elif isinstance(param.type.type.type, node.Struct):
            return False
        elif param.type.type.type.names[0] == 'char':
            return True
        else:
            return False
    else:
        return False


def is_char_pointer_or_non_pointer(param):
    if is_ellipsis(param):
        return False
    elif is_char_pointer(param):
        return True
    elif is_pointer(param):
        return False
    else:
        return True


def is_struct(param):
    try:
        return isinstance(param.type.type, node.Struct)
    except AttributeError:
        False


def is_union(param):
    try:
        return isinstance(param.type.type, node.Union)
    except AttributeError:
        False


def is_void(param):
    if is_ellipsis(param):
        return False
    elif is_pointer(param):
        return False
    elif is_enum(param):
        return False
    elif is_struct(param):
        return False
    elif is_union(param):
        return False
    else:
        return param.type.type.names[0] == 'void'


def is_pointer(param):
    return isinstance(param.type, (node.PtrDecl, node.ArrayDecl))


def is_enum(param):
    return isinstance(param.type.type, node.Enum)


def decl(name, type):
    return node.Decl(name, [], [], [], type, None, None)


def function_ptr_decl(name, return_type, parameters):
    return decl(
        name, node.PtrDecl([], node.FuncDecl(node.ParamList(parameters), return_type))
    )


def bool_param(name):
    return decl(name, node.TypeDecl(name, [], node.IdentifierType(["bool"])))


def set_member(name):
    return decl(name,
                node.TypeDecl(name,
                              [],
                              node.IdentifierType(["struct nala_set_param"])))


def in_assert_member(param):
    name = f'{param.name}_in_assert'

    return function_ptr_decl(
        name,
        void_type(name),
        [
            param,
            decl('nala_buf_p',
                 node.PtrDecl([],
                              node.TypeDecl('nala_buf_p',
                                            ['const'],
                                            node.IdentifierType(["void"])))),
            decl('nala_size',
                 node.TypeDecl('nala_size', [], node.IdentifierType(["size_t"])))
        ])


def out_callback_member(param):
    name = f'{param.name}_out_callback'

    return function_ptr_decl(
        name,
        void_type(name),
        [
            param,
            decl('nala_buf_p',
                 node.PtrDecl([],
                              node.TypeDecl('nala_buf_p',
                                            ['const'],
                                            node.IdentifierType(["void"])))),
            decl('nala_size',
                 node.TypeDecl('nala_size', [], node.IdentifierType(["size_t"])))
        ])


def va_list_param(name):
    return decl(None,
                node.TypeDecl(name, [], node.IdentifierType(["va_list"])))


def is_variadic_func(params):
    if len(params) == 0:
        return False
    else:
        return is_ellipsis(params[-1])


def void_type(name):
    return node.TypeDecl(name, [], node.IdentifierType(['void']))


def rename_return_type(return_type, name):
    return_type = deepcopy(return_type)
    type_decl = return_type

    while not isinstance(type_decl, node.TypeDecl):
        type_decl = type_decl.type

    type_decl.declname = name

    return return_type


def create_implementation_params(params):
    return [
        va_list_param("__nala_va_list")
        if is_ellipsis(param)
        else param
        for param in params
    ]


def get_guard_name(filename):
    slug = re.sub(r"[^a-zA-Z0-9]", "_", os.path.normpath(os.path.relpath(filename)))

    return re.sub(r"_+", "_", slug).upper().strip("_")


def generate_includes(system_includes, local_includes, directory):
    includes = "\n".join(
        includes
        for includes in (
            "".join(f"#include <{path}>\n" for path in sorted(system_includes)),
            "".join(
                f'#include "{os.path.relpath(path, directory)}"\n'
                for path in sorted(local_includes)
            ),
        )
        if includes
    )

    return includes and f"\n{includes}"


def read_nala_c():
    path = os.path.join(SCRIPT_DIR, 'templates', 'nala.c')

    with open(path, 'r') as fin:
        return fin.read()


class GeneratedMock:
    DECL_MARKER = "// NALA_DECLARATION"
    IMPL_MARKER = "// NALA_IMPLEMENTATION"

    def __init__(self, function):
        self.function = function

        self.func_name = function.name

        self.wrapped_func = f"__wrap_{self.func_name}"
        self.real_func = f"__real_{self.func_name}"

        self.state_name = f"nala_state_for_{self.func_name}"
        self.state_type = f"nala_state_type_for_{self.func_name}"
        self.params_type = f"struct nala_params_type_for_{self.func_name}"

        self.func_decl = self.function.declaration.type
        self.func_params = self.func_decl.args.params if self.func_decl.args else []
        self.is_variadic_func = is_variadic_func(self.func_params)

        self.params_struct = [
            decl(param.name, node.PtrDecl([], param.type.type))
            if isinstance(param.type, node.ArrayDecl)
            else param
            for param in self.func_params
            if not is_ellipsis(param) and param.name
        ]
        self.forward_args = ", ".join(param.name for param in self.params_struct)

        if self.is_variadic_func:
            self.params_struct.append(decl(
                None,
                node.PtrDecl([],
                             node.TypeDecl("vafmt_p",
                                           ['const'],
                                           node.IdentifierType(["char"])))))
            self.forward_args += ', __nala_vl'

        return_type = self.func_decl.type
        self.return_value = (
            None
            if isinstance(return_type, node.TypeDecl)
            and isinstance(return_type.type, node.IdentifierType)
            and return_type.type.names[0] == "void"
            else "return_value")

        if self.is_variadic_func:
            self.va_list_start_arg_name = self.func_params[-2].name
        else:
            self.va_list_start_arg_name = None

        self.return_value_decl = decl(
            self.return_value,
            rename_return_type(return_type, self.return_value))
        mock_params = self.create_mock_params()
        self.implementation_decl = function_ptr_decl(
            "implementation",
            rename_return_type(return_type, "implementation"),
            create_implementation_params(self.func_params))
        self.mock_func = self.void_function_decl(f'{self.func_name}_mock',
                                                 mock_params)
        self.mock_once_func = self.void_function_decl(
            f'{self.func_name}_mock_once',
            mock_params)
        self.set_errno_func = self.void_function_decl(
            f'{self.func_name}_mock_set_errno',
            [decl(
                "errno_value",
                node.TypeDecl("errno_value", [], node.IdentifierType(["int"])),
            )])
        self.callback_decl = function_ptr_decl(
            "callback",
            void_type("callback"),
            create_implementation_params(self.func_params))
        self.variadic_func_real_wrapper_decl = node.FuncDecl(
            node.ParamList(create_implementation_params(self.func_params)),
            node.TypeDecl(
                f'{self.func_name}_mock_va_arg_real',
                [],
                return_type))
        self.default_variadic_func_real_wrapper_decl = node.FuncDecl(
            node.ParamList(create_implementation_params(self.func_params)),
            node.TypeDecl(
                f'nala_v{self.func_name}',
                [],
                return_type))
        self.real_decl = self.rename_function(self.real_func)
        self.wrapped_decl = self.rename_function(self.wrapped_func)
        self.instance_members = []
        self.set_params = []
        self.char_pointer_params = []
        self.pointer_params = []
        self.non_pointer_params  = []
        self.ignore_params = []

        for param in self.func_params:
            if is_ellipsis(param):
                continue
            elif self.is_struct(param):
                continue
            elif self.is_union(param):
                continue

            if not param.name:
                continue

            self.instance_members.append(bool_param(f'ignore_{param.name}_in'))

            if is_char_pointer(param):
                self.char_pointer_params.append(param)
            elif is_pointer(param):
                self.pointer_params.append(param)
            else:
                self.non_pointer_params.append(param)

            if is_char_pointer_or_non_pointer(param):
                self.ignore_params.append(param.name)

            if not is_pointer(param):
                continue

            self.instance_members.append(set_member(f'{param.name}_in'))
            self.instance_members.append(in_assert_member(param))
            self.instance_members.append(set_member(f'{param.name}_out'))
            self.instance_members.append(out_callback_member(param))
            self.set_params.append(param)

    def void_function_decl(self, name, parameters):
        return node.FuncDecl(node.ParamList(parameters),
                             void_type(name))

    def rename_function(self, name):
        return decl(
            name,
            node.FuncDecl(
                self.func_decl.args, rename_return_type(self.func_decl.type, name)
            ),
        )

    def is_struct(self, param):
        try:
            if isinstance(param.type.type, node.Struct):
                return True
        except AttributeError:
            pass

        try:
            name = param.type.type.names[0]
            typedef = self.lookup_typedef(name)

            if isinstance(typedef.type.type, node.Struct):
                return True
        except AttributeError:
            pass

        return False

    def is_union(self, param):
        try:
            if isinstance(param.type.type, node.Union):
                return True
        except AttributeError:
            pass

        try:
            name = param.type.type.names[0]
            typedef = self.lookup_typedef(name)

            if isinstance(typedef.type.type, node.Union):
                return True
        except AttributeError:
            pass

        return False

    def lookup_typedef(self, name):
        for item in self.function.file_ast:
            if isinstance(item, node.Typedef):
                if item.name == name:
                    return item

    def create_mock_params(self):
        once_params = []
        variable_arguments_params = []

        for param in self.func_params:
            if is_void(param):
                continue
            elif self.is_struct(param):
                continue
            elif self.is_union(param):
                continue
            elif is_char_pointer_or_non_pointer(param):
                once_params.append(param)
            elif is_ellipsis(param):
                variable_arguments_params.append(decl(
                    None,
                    node.PtrDecl([],
                                 node.TypeDecl("vafmt_p",
                                               ['const'],
                                               node.IdentifierType(["char"])))))
                variable_arguments_params.append(param)

        if not is_void(self.return_value_decl):
            once_params.append(self.return_value_decl)

        once_params += variable_arguments_params

        return once_params


class FileGenerator:

    HEADER_FILE = "nala_mocks.h"
    SOURCE_FILE = "nala_mocks.c"
    LINKER_FILE = "nala_mocks.ld"

    def __init__(self):
        self.code_generator = CGenerator()

        self.jinja_env = Environment(
            loader=PackageLoader("nala", "templates"),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.jinja_env.filters["render"] = self.code_generator.visit

        self.header_template = self.jinja_env.get_template(f"{self.HEADER_FILE}.jinja2")
        self.source_template = self.jinja_env.get_template(f"{self.SOURCE_FILE}.jinja2")

        self.mocks = []
        self.system_includes = set()
        self.local_includes = set()

    def add_mock(self, mocked_function):
        self.mocks.append(GeneratedMock(mocked_function))

        if mocked_function.include:
            if mocked_function.include.system:
                self.system_includes.add(mocked_function.include.path)
            else:
                self.local_includes.add(mocked_function.include.path)

    def write_to_directory(self, directory):
        os.makedirs(directory, exist_ok=True)

        header_filename = os.path.join(directory, self.HEADER_FILE)
        source_filename = os.path.join(directory, self.SOURCE_FILE)
        linker_filename = os.path.join(directory, self.LINKER_FILE)

        mocks = list(sorted(self.mocks, key=lambda m: m.func_name))

        header_code = self.header_template.render(
            nala_version=__version__,
            guard_name=get_guard_name(header_filename),
            includes=generate_includes(
                self.system_includes, self.local_includes, directory),
            mocks=mocks)

        source_code = self.source_template.render(
            nala_version=__version__,
            includes=generate_includes(
                {"stddef.h", "errno.h"}, {header_filename}, directory),
            nala_c=read_nala_c(),
            mocks=mocks)

        with open(header_filename, "w") as fout:
            fout.write(header_code.strip())
            fout.write('\n')

        with open(source_filename, "w") as fout:
            fout.write(source_code.strip())
            fout.write('\n')

        with open(linker_filename, "w") as fout:
            fout.write(' '.join([
                f'-Wl,--wrap={mock.function.name}'
                for mock in mocks
            ]))
