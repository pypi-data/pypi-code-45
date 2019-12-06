import sys

this = sys.modules[__name__]

this.current_coid = 1000000


def init():
    pass

def gen_coid():

    this.current_coid += 1

    return this.current_coid