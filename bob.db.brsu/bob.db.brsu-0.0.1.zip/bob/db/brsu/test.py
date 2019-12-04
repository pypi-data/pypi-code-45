#!/usr/bin/env python
# encoding: utf-8


"""A few checks on the BRSU database 
"""
import os, sys
import bob.db.base
import bob.db.brsu

def db_available(test):
  """Decorator for detecting if the database file is available"""
  from bob.io.base.test_utils import datafile
  from nose.plugins.skip import SkipTest
  import functools

  @functools.wraps(test)
  def wrapper(*args, **kwargs):
    dbfile = datafile("db.sql3", __name__, None)
    if os.path.exists(dbfile):
      return test(*args, **kwargs)
    else:
      raise SkipTest("The database file '%s' is not available; did you forget to run 'bob_dbmanage.py %s create' ?" % (dbfile, 'brsu'))

  return wrapper


def test_objects():

  # tests if the right number of sample objects is returned
  
  db = bob.db.brsu.Database(protocol='train')
  assert len(db.objects(groups=('train',), purposes=('real',))) == 192
  assert len(db.objects(groups=('train',), purposes=('attack',))) == 84
  db = bob.db.brsu.Database(protocol='test')
  assert len(db.objects(groups=('train',), purposes=('real',))) == 192
  assert len(db.objects(groups=('train',), purposes=('attack',))) == 84
