# -*- coding: utf-8 -*-

"""
Package footest
=======================================

Top-level package for footest.
"""

__version__ = "0.0.0"

try:
    import footest.bar
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'bar')
    if not msg:
        import footest.bar
    else:
        click.secho(msg, fg='bright_red')

try:
    import footest.foo
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'foo')
    if not msg:
        import footest.foo
    else:
        click.secho(msg, fg='bright_red')


def hello(who='world'):
    """'Hello world' method.

    :param str who: whom to say hello to
    :returns: a string
    """
    result = "Hello " + who
    return result

# Your code here...