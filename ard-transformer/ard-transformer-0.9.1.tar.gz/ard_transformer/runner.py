# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2019 raka2407
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
from pyfiglet import Figlet
from .transformer import transform_ard_to_octane
from .version import __version__


def parse_options():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    general = parser.add_argument_group("General")
    parser.add_argument(
        '-v',
        action='store_true',
        dest='version',
        help='Display transformer version'
    )

    general.add_argument(
        '-p',
        dest='path',
        help="Path of input and output files"
    )

    general.add_argument(
        '-i',
        dest='input',
        help="Name of ARD file"
    )

    general.add_argument(
        '-o',
        dest='output',
        help="Name of Octane file"
    )

    args = parser.parse_args()
    return args


def main():
    f = Figlet(font='slant')
    print('\n','******************************************************************''\n', f.renderText('ARD Transformer'), '******************************************************************''\n')
    args = parse_options()

    if args.version:
        print(__version__)
        exit(0)

    transform_ard_to_octane(args)