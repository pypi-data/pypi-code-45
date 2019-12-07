#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys

def sum(*values):
    s = 0
    for v in values:
        i = int(v)
        s = s + i
    print s

def output():
    print('http://hhrtest.me')

def main():
    print('this is main()')
    print(sys.argv[1:])

if __name__ == "__main__":
    main()
