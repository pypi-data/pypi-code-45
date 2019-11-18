# Copyright (C) 2019  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information


try:
    from swh.loader.core._version import __version__   # type: ignore
except ImportError:
    __version__ = 'devel'


DEFAULT_PARAMS = {
    'headers': {
        'User-Agent': 'Software Heritage Loader (%s)' % (
            __version__
        )
    }
}
