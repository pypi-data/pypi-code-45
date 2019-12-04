# Although, yaci supports storage implementaitons in multiple
# versions of Python this one was written using Python 3.7.
# It is important to note this because of changes to how
# cPickle and gdbm are accessed in newer versions of Python.

import contextlib
# We use the GNU implementation of the dbm interface, so that we
# can use the 's' option on open, which enables the synchronized
# mode, which causes chnages to the database to be immediately
# written to file.
import dbm.gnu as dbm
import logging
import os
import weakref


# We use cPickle instead of pickle, because
# it is the C Optimized version
import _pickle as pickle
from yaci import base_storage


# WARNING: This is purley an example implementaiton. There are a number
# issues with using this implementation in production code.
# 1. The pickle module is NOT secure
# 2. This implementaiton uses a single path for for persistent
#    storage by default, which means you could get a result you do not
#    expect.
# 3. While a finalizer is implemented it should probably be given
#    more thought.
# 4. This code is not thread safe.
# 5. Finally, and PROBABLY most importantly, not every object can be
#    pickled! In most cases you will need to implement your own
#    mechanism for serialization.

def _closedb(db):
    db.close()


class DBStorage(base_storage.CacheStorage):
    _path_prefix = 'dbm'

    """
    A dbm (https://docs.python.org/3/library/dbm.html) backed
    implementation of the CacheSorage Class.

    """

    def __init__(self, dirname='/tmp', clear_cache=False, logger=None):
        self.path = os.path.join(dirname, self._path_prefix)
        self._makedirs(self.path)
        self._storage_path = os.path.join(self.path, 'cache_db')
        # TODO: Clean up storage creation. is the open_with_finalizer
        #       function necessary
        self._storage = self._open_with_finalizer('cs')
        self.logger = logger if logger is not None else logging.getLogger(self.__class__.__name__)
        if clear_cache:
            self.clear()

    def _key_id(self, key):
        return str(key)

    def _open_with_finalizer(self, args):
        storage = dbm.open(self._storage_path, args)
        self.finalizer = weakref.finalize(self, _closedb, storage)
        return storage

    def store(self, key, value):
        self.logger.info("Caching %s to %s" % (self._key_id(key), self._storage_path))
        self._storage[self._key_id(key)] = pickle.dumps(value, protocol=4)

    def get(self, key):
        self.logger.debug("Using cache %s from %s" % (self._key_id(key), self._storage_path))
        value = pickle.loads(self._storage[self._key_id(key)])
        return value

    def cached(self, key):
        _cached = self._key_id(key) in self._storage
        return _cached

    @property
    def size(self):
        return len(self._storage)

    def clear(self):
        # Close the db to cleanup resources
        self._storage.close()

        # n option causes new db to be created
        self._storage = self._open_with_finalizer('ns')

    def delete(self, key):
        del self._storage[self._key_id(key)]

    def _makedirs(self, path):
        # NOTE: Python 3.x allows users to set the flag
        # exist_ok = True, but surpressing
        # the FileExistsError works in both 2.x and
        # 3.x
        with contextlib.suppress(FileExistsError):
            os.makedirs(path)

    def _remove_file(self, filename):
        # It's OK if the file can't be found...
        with contextlib.suppress(FileNotFoundError):
            os.remove(filename)

    def __iter__(self):
        for key_id in self._storage.keys():
            yield key_id

    def close(self):
        self._storage.close()
