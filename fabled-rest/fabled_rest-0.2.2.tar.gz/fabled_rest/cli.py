# -*- coding: utf-8 -*-

"""Console script for fabled_rest."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for fabled_rest."""
    click.echo("Replace this message by putting your code into "
               "fabled_rest.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
