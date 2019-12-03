#!/usr/bin/python3
import random
import string


def GetRandomString(size):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
