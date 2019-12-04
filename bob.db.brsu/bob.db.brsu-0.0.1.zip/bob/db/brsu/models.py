#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import os

from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base

import bob.db.base
from bob.db.base.sqlalchemy_migration import Enum, relationship

import bob.core
import bob.io.base
import bob.io.image

logger = bob.core.log.setup('bob.db.brsu')

Base = declarative_base()

protocolPurpose_sample_association = Table('protocolPurpose_file_association', Base.metadata,
  Column('protocolPurpose_id', Integer, ForeignKey('protocolPurpose.id')),
  Column('sample_id',  Integer, ForeignKey('sample.id')))

sample_file_association = Table('sample_files_association', Base.metadata,
  Column('sample_id', String, ForeignKey('sample.id')),
  Column('file_id', Integer, ForeignKey('imagefile.id')))

class Sample(Base):
  """ A sample describe an example for this database.
      
      A sample consists in 5 images
      - a color image
      - 4 SWIR images: 935nm, 1060nm, 1300nm and 1550nm

  Attributes
  ----------
  id: str
    The id for the sample
  
  """
  
  __tablename__ = 'sample'
  id = Column(String(100), primary_key=True)
  attack_type = Column(Integer)
  
  files = relationship("ImageFile", secondary=sample_file_association, backref=backref("Sample", order_by=id))

  def __init__(self, id, attack_type=0):
    """ Init function
    
    Parameters
    ----------
    sample_id: str
      The id for the sample
    attack_type: int
      The type of attack. Note that 0 corresponds to a real attempt.
    """
    self.id = id
    self.attack_type = attack_type

  def load(self, directory=None):
    """
    loads a sample.

    This function loads a sample from the BRSU database.
    It should load a single modality or a combination of them.
  
    Parameters
    ----------
    directory: str
      The default directory of the database

    Returns
    -------
    dict:
      Dictionary containing the modality as the key and the corresponding image as value.
    """
    retval = {}
    mods = ['color', '935nm', '1060nm', '1300nm', '1550nm']

    for f in self.files:
      retval[f.modality] = bob.io.base.load(f.make_path(directory=directory))
    return retval


  def is_attack(self):
    return self.attack_type != 0


  def __lt__(self, other):
    if self.id < other.id:
      return True
    else:
      return False


class ImageFile(Base, bob.db.base.File):
  """Generic file container
  
  Class that defines an image file of the BRSU database.

  Attributes
  ----------
  sample_id: str
    The id of the sample associated to this file
  modality: str
    The modality from which this file was recorded
  path: str
    The path on the disk where this file is stored.
  """
  
  __tablename__ = 'imagefile'

  # key id for files
  id = Column(Integer, primary_key=True)

  # client id of this file
  sample_id = Column(String(100), ForeignKey('sample.id'))  
  sample = relationship(Sample, backref=backref('image_file', order_by=id))
  
  # path of this file in the database
  path = Column(String(100), unique=True)
  extension_choices = ('.JPG', '.jpg', '.png')
  extension = Column(Enum(*extension_choices))
  
  # modality
  modality_choices = ('color', '935nm', '1060nm', '1300nm', '1550nm')
  modality = Column(Enum(*modality_choices))

  def __init__(self, sample_id, path, extension, modality):
    """ Init function

    Parameters
    ----------
    sample_id: str
      The id of the sample associated to this file
    path: str
      The path on the disk where this file is stored.
    extension: str
      The extension of this file 
    modality: str
      The modality from which this file was recorded
    
    """
    bob.db.base.File.__init__(self, path=path)
    self.sample_id = sample_id
    self.path = path
    self.extension = extension
    self.modality = modality


  def __repr__(self):
    return "File('%s')" % self.path


  def make_path(self, directory=None, extension=None):
    """Wraps the current path so that a complete path is formed

    Parameters
    ----------
    directory
      An optional directory name that will be prefixed to the returned result.
    extension
      An optional extension that will be suffixed to the returned filename. 
      extension normally includes the leading ``.`` character 

    Returns
    -------
    str:
      the newly generated file path.
    
    """

    if not directory:
      directory = ''
    if not extension:
      extension = self.extension
    
    return os.path.join(directory, self.path + extension)


class Protocol(Base):
  """BRSU protocols
 
  The class representing the protocols.

  Attributes
  ----------
  name:
    The name of the protocol
  """

  __tablename__ = 'protocol'

  id = Column(Integer, primary_key=True)
  name = Column(String(20), unique=True)

  def __init__(self, name):
    """ Init function

    Parameters
    ----------
    name:
      The name of the protocol
    
    """
    self.name = name

  def __repr__(self):
    return "Protocol('%s')" % (self.name,)


class ProtocolPurpose(Base):
  """BRSU protocol purposes
  
  This class represent the protocol purposes, and 
  more importantly, contains the set of files
  associated with each group and each purpose
  for each protocol.

  Attributes
  ----------
  protocol_id: str
    The associated protocol
  group: str
    The group in the associated protocol ('train', 'validation' or 'test')
  purpose: str
    The purpose of the group in this protocol ('real', or 'attack')
  
  """

  __tablename__ = 'protocolPurpose'

  id = Column(Integer, primary_key=True)
  
  protocol_id = Column(Integer, ForeignKey('protocol.id'))
  group_choices = ('train', 'test')
  group = Column(Enum(*group_choices))
  purpose_choices = ('real', 'attack')
  purpose = Column(Enum(*purpose_choices))

  # protocol: a protocol have 1 to many purpose
  protocol = relationship("Protocol", backref=backref("purposes", order_by=id))
  
  # samples: many to many relationship
  samples = relationship("Sample", secondary=protocolPurpose_sample_association, backref=backref("protocolPurposes", order_by=id))

  def __init__(self, protocol_id, group, purpose):
    """ Init function

    Parameters
    ----------
    protocol_id: str
      The associated protocol
    group: str
      The group in the associated protocol ('world', 'dev' or 'eval')
    purpose: str
      The purpose of the group in this protocol ('train', 'enroll' or 'probe')
   
    """
    self.protocol_id = protocol_id
    self.group = group
    self.purpose = purpose

  def __repr__(self):
    return "ProtocolPurpose('%s', '%s', '%s')" % (self.protocol.name, self.group, self.purpose)
