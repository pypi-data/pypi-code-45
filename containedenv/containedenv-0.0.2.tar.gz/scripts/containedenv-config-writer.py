#!/usr/bin/env python3

import sys
import argparse
from containedenv.functions import parse_env


def parse_args():
    """
    Handle argument parsing here
    """
    parser = argparse.ArgumentParser(
        description='Convert environment variables in to a configuration file')
    parser.add_argument('-p',
                        '--prefix',
                        help='Prefix of env vars to parse',
                        required=True)
    parser.add_argument('-f',
                        '--format',
                        help='Output file format',
                        default='ini',
                        choices=['ini', 'json'])
    parser.add_argument('-o',
                        '--output-file',
                        help='Outfile file path',
                        default='/dev/stdout')
    parser.add_argument(
        '-r',
        '--reference-file',
        type=argparse.FileType('r'),
        help='Load this reference file for existing/hard coded values')

    return parser.parse_args()


def main():
    args = parse_args()
    parse_env(prefix=args.prefix,
              cfg_type=args.format,
              reference_file=args.reference_file,
              output_file=args.output_file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
