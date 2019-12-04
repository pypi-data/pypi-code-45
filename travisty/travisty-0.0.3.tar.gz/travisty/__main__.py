#!/usr/bin/env python3

import argparse

import travisty


def main(args=None):
    parser = argparse.ArgumentParser(
        prog="travisty",
        usage="travisty <command> <options>",
        description="travisty: doesn't do a lot",
    )

    parser.add_argument("--version", action="version", version=travisty.__version__)
    subparsers = parser.add_subparsers(title="Available commands", help="", metavar="")

    subparser_random_int = subparsers.add_parser(
        "random_int",
        help="Prints a random integer between 41 and 43",
        usage="travisty random_int",
        description="Prints a random integer between 41 and 43",
    )
    subparser_random_int.set_defaults(func=travisty.wibble.floopy)
    args = parser.parse_args()

    if hasattr(args, "func"):
            args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

