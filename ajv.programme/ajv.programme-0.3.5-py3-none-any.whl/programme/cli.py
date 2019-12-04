#!/usr/bin/python3

import argparse
import logging
import sys
from os.path import dirname, join, basename
from csv import DictReader

from jinja2 import Template


def pkgpath(path):
    """ Get full path to a built-in file """
    path = join(dirname(__file__), path)
    assert path
    return path


def print_pkgfile(path, outfile=sys.stdout):
    """ Print a built-in file """
    with open(pkgpath(path)) as f:
        print(f.read().rstrip('\n'), file=outfile)

class HelpFormatter(argparse.HelpFormatter):
    optwidth = 32  # Evil, can't figure out how to hook this.

    def __init__(self, *args, **kwargs):
        # FIXME: HelpFormatter's signature is not public and this may break in a
        # newer python
        kwargs['max_help_position'] = self.optwidth
        super().__init__(*args, **kwargs)


def init_parser():
    parser = argparse.ArgumentParser(
            description="Generate a musical-performance programme",
            usage="programme [options] [infile] [outfile]",
            formatter_class=HelpFormatter,
            add_help=False,
            )


    group = parser.add_argument_group('arguments')
    group.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                       default=sys.stdin,
                       help='input file name (default stdin)')
    group.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                       default=sys.stdout,
                       help='output file (default stdout)')

    group = parser.add_argument_group('common options')
    group.add_argument('-h', '--help', action='help',
                       help='show this help message and exit')
    group.add_argument('-i', '--init', action='store_true',
                       help='generate blank student tsv file')
    group.add_argument('-d', '--details', metavar="KEYS",
                       default='song,author',
                       help='comma-separated list of columns to include')
    group.add_argument('-s', '--sort', metavar="KEYS",
                       help='comma-separated list of columns to sort by')

    group = parser.add_argument_group('advanced options')
    group.add_argument('-t', '--template', type=argparse.FileType('r'),
                       metavar="FILE", default=pkgpath('template.jinja'),
                       help='specify alternate template file')
    group.add_argument('-c', '--css', type=argparse.FileType('r'),
                       metavar="FILE", default=pkgpath('style.css'),
                       help='specify alternate stylesheet')

    group = parser.add_argument_group('debugging options')
    group.add_argument('-v', '--verbose', action='store_true',
                       help='verbose output')
    group.add_argument('-D', '--debug', action='store_true',
                       help='even more verbose output')
    group.add_argument('-V', '--version', action='store_true',
                       help='print version and exit')
    return parser


def main():
    # Get command line arguments
    parser = init_parser()
    args = parser.parse_args()

    # Set up logging
    if args.debug:
        loglevel = logging.DEBUG
    elif args.verbose:
        loglevel = logging.INFO
    else:
        loglevel = logging.WARN
    logging.basicConfig(level=loglevel, format="%(levelname)s\t%(message)s")
    logging.debug("Debug output enabled")

    # Handle the special cases first
    if args.version:
        print_pkgfile('version.txt', args.outfile)
        sys.exit(0)
    elif args.init:
        print_pkgfile('base.tsv', args.outfile)
        sys.exit(0)

    # Now the actual work.
    logging.info("Loading template from %s", basename(args.template.name))
    template = Template(args.template.read(), keep_trailing_newline=True)
    logging.info("Loading students from %s", args.infile.name)
    students = list(DictReader(args.infile, delimiter='\t'))
    logging.info("Found %s students", len(students))
    if args.sort:
        logging.info("Sorting by: %s", args.sort)
        for key in reversed(args.sort.split(',')):
            logging.debug("Sorting students by %s", key)
            students.sort(key=lambda student: student[key])

    context = {
            'students':  students,
            'css':       args.css.read(),
            'details':   args.details.split(','),
            }
    logging.info("Rendering page")
    logging.debug("Context sent to template: %s", context)
    output = template.render(**context)
    logging.info("Writing to %s", args.outfile.name)
    args.outfile.write(output)
    logging.info("Done")


if __name__ == '__main__':
    main()
