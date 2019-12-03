# -*- coding: utf-8 -*-

"""
Package et_auto_build
=======================================

Top-level package for et_auto_build.
"""

__version__ = "0.0.0"

try:
    import et_auto_build.bar
except ModuleNotFoundError as e:
    # Try to build this binary extention:    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'bar')
    if not msg:
        import et_auto_build.bar
    else:
        click.secho(msg, fg='bright_red')

try:
    import et_auto_build.foo
except ModuleNotFoundError as e:
    # Try to build this binary extention:    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'foo')
    if not msg:
        import et_auto_build.foo
    else:
        click.secho(msg, fg='bright_red')


# Your code here...