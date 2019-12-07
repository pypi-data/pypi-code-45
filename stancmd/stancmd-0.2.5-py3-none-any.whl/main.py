#!/usr/bin/env python3

import sys

from stan import stan


def main():
    stan.Stan(4 * 60 * 60, sys.argv[1:] if len(sys.argv) > 1 else ['']).run()


if __name__ == '__main__':
    main()
