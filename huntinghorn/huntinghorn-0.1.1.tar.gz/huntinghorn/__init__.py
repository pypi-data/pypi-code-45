#! /bin/env python

"""Command-line tool for viewing hunting horn melodies.

Usage:
    horn list [--notes=<notes>]
    horn -h | --help
    horn --version

Options:
    --help -h        Show this screen.
    --version        Show version.
    --notes=<notes>  Notes to filter by [default: ABGMRWY]
"""

__version__ = '0.1.1'

from typing import Set

from docopt import docopt

from huntinghorn.constants import Note, melodies


def main():
    """Entry point for the command line interface."""
    arguments = docopt(__doc__, version=f'horn {__version__}')

    notes: Set[Note] = set()
    note_names = dict(
        A=Note.AQUA,
        B=Note.BLUE,
        G=Note.GREEN,
        M=Note.MAGENTA,
        R=Note.RED,
        W=Note.WHITE,
        Y=Note.YELLOW
    )

    for name in arguments['--notes']:
        if (note := note_names.get(name)):
            notes.add(note)

    available_melodies = [
        melody for melody in melodies
        if notes >= set(melody.notes)
    ]

    padding = max(
        len(str(melody))
        for melody in available_melodies
    )

    for melody in available_melodies:
        print(melody.as_str(padding + 1))
