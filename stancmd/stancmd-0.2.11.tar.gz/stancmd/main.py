#!/usr/bin/env python3

import sys

if __package__ is None or __package__ == '':
    import stan
    import utils
else:
    from . import stan, utils


def main():
    stan.Stan(4 * 60 * 60, sys.argv[1:] if len(sys.argv) > 1 else ['']).run(utils.signal_handler, utils.bruno)


if __name__ == '__main__':
    main()
