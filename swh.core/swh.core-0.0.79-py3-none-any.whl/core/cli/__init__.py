# Copyright (C) 2019  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

import logging
import logging.config

import click
import pkg_resources
import yaml

LOG_LEVEL_NAMES = ['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

logger = logging.getLogger(__name__)


class AliasedGroup(click.Group):
    '''A simple Group that supports command aliases, as well as notes related to
    options'''

    def __init__(self, name=None, commands=None, **attrs):
        self.option_notes = attrs.pop('option_notes', None)
        super().__init__(name, commands, **attrs)

    @property
    def aliases(self):
        if not hasattr(self, '_aliases'):
            self._aliases = {}
        return self._aliases

    def get_command(self, ctx, cmd_name):
        return super().get_command(ctx, self.aliases.get(cmd_name, cmd_name))

    def add_alias(self, name, alias):
        if not isinstance(name, str):
            name = name.name
        self.aliases[alias] = name

    def format_options(self, ctx, formatter):
        click.Command.format_options(self, ctx, formatter)
        if self.option_notes:
            with formatter.section('Notes'):
                formatter.write_text(self.option_notes)
        self.format_commands(ctx, formatter)


@click.group(
    context_settings=CONTEXT_SETTINGS, cls=AliasedGroup,
    option_notes='''\
If both options are present, --log-level will override the root logger
configuration set in --log-config.

The --log-config YAML must conform to the logging.config.dictConfig schema
documented at https://docs.python.org/3/library/logging.config.html.
'''
)
@click.option('--log-level', '-l', default=None,
              type=click.Choice(LOG_LEVEL_NAMES),
              help="Log level (defaults to INFO).")
@click.option('--log-config', default=None,
              type=click.File('r'),
              help="Python yaml logging configuration file.")
@click.pass_context
def swh(ctx, log_level, log_config):
    """Command line interface for Software Heritage.
    """
    if log_level is None and log_config is None:
        log_level = 'INFO'

    if log_config:
        logging.config.dictConfig(yaml.safe_load(log_config.read()))

    if log_level:
        log_level = logging.getLevelName(log_level)
        logging.root.setLevel(log_level)

    ctx.ensure_object(dict)
    ctx.obj['log_level'] = log_level


def main():
    # Even though swh() sets up logging, we need an earlier basic logging setup
    # for the next few logging statements
    logging.basicConfig()
    # load plugins that define cli sub commands
    for entry_point in pkg_resources.iter_entry_points('swh.cli.subcommands'):
        try:
            cmd = entry_point.load()
            swh.add_command(cmd, name=entry_point.name)
        except Exception as e:
            logger.warning('Could not load subcommand %s: %s',
                           entry_point.name, str(e))

    return swh(auto_envvar_prefix='SWH')


if __name__ == '__main__':
    main()
