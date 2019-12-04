from pkg_resources import get_distribution

try:
    __version__ = get_distribution("travisty").version
except:
    __version__ = "local"


__all__ = ["wibble"]

from travisty import *
