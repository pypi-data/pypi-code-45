#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import os
from .models import *
import glob

from bob.db.base.driver import Interface as BaseInterface

import bob.core
logger = bob.core.log.setup('bob.db.brsu')

import bob.io.base
import bob.io.image


def visualize_sample(rgb, swirs):
  """ Visualize the sample being added to the DB

  Parameters
  ----------
  rgb: ImageFile object
    The color image
  swirs: list of ImageFile objects
    The different SWIR images

  """
  from matplotlib import pyplot
  rgb_image = bob.io.base.load(rgb.path)
  f, axarr = pyplot.subplots(1, 4)
  f.suptitle(rgb.sample_id)
  axarr[0].imshow(bob.io.image.to_matplotlib(rgb_image))
  for i in range(1, 4):
    swir = bob.io.base.load(swirs[i-1].path)
    axarr[i].imshow(swir, cmap='gray')
  for i in range(len(axarr)):
    axarr[i].set_xticks([])
    axarr[i].set_yticks([])
  pyplot.show()


def add_files_and_samples(session, imagesdir, extension='.jpg'):
  """ Add face images files and samples.

  This function adds the face image files and the samples to the database.

  Parameters
  ----------
  session:
    The session to the SQLite database 
  imagesdir : :py:obj:str
    The directory where to find the images 
  extension: :py:obj:str
    The extension of the image file.

  """
  n_real_samples = 0
  n_attack_samples = 0
 
  # list of subjects for which the shot index in SWIR does not match the one in RGB (and is +1)
  swir_index_plusone = ['F025', 'F032', 'F034', 'F035', 'F041', 'F046', 'F048', 'F053']

  # attack type to attack description
  attack_map = {0: 'Bonafide', 1: 'Replay', 2: 'Mask', 3: 'Disguise', 4: 'Makeup'}

  for root, dirs, files in os.walk(imagesdir, topdown=False):
    for name in files:
      
      image_filename = os.path.join(root, name)
     
      # only consider images
      if os.path.splitext(image_filename)[1] == '.JPG' or os.path.splitext(image_filename)[1] == '.png' or os.path.splitext(image_filename)[1] == '.jpg':
        info = image_filename.split('/')
        
        swir_suffix = ['_935nm', '_1060nm', '_1300nm', '_1550nm']
       
        # =====================
        # === BONAFIDE data ===
        # =====================
        if 'BRSU_FaceDB' in info and len(info) == 9: # test the length to eliminate the spectrometer image
          image, extension = os.path.splitext(info[8])
          image_info = image.split('_')

          # look for the RGB image and then get corresponding SWIR images
          if 'RGB' in image_info:
            rgb_stem = image_filename.replace(imagesdir, '')
            rgb_stem = rgb_stem.replace(extension, '')

            subject_id = info[6][1:]
            sample_id = subject_id + '-' + image_info[2]

            # skip non-frontal images
            if image_info[0] == 'F048' and image_info[2] == '03': # this is a special case (3 shots, and mismatch)
              continue
            if int(image_info[2]) < 4:
              modality = 'color'
              rgb_ImageFile = ImageFile(path=rgb_stem, sample_id=sample_id, extension=extension, modality=modality)
            
              # now get the corresponding SWIR images
              swir_ImageFile = []
              swir_image = image_filename.replace('RGB', 'SWIR')
              swir_image, _ = os.path.splitext(swir_image)

              for s in swir_suffix:
                modality = s[1:]
                swir_filename = swir_image + s + '.png'

                # in some cases, there is a problem with the numbering of SWIR images
                if image_info[0] in swir_index_plusone:
                  rgb_index = int(image_info[2])
                  swir_index = str(rgb_index + 1).zfill(2)
                  swir_filename = swir_filename.replace('_' + image_info[2], '_' + swir_index)
                
                # check that the file exists
                if os.path.isfile(swir_filename):
                  swir_stem = swir_filename.replace(imagesdir, '')
                  swir_stem, ext = os.path.splitext(swir_stem)
                  assert ext == '.png', "SWIR file {} doesn't have a .png ext".format(swir_filename)
                  swir_ImageFile.append(ImageFile(path=swir_stem, sample_id=sample_id, extension=ext, modality=modality))
                else:
                  logger.warning("Cannot find image {} for sample {} !".format(swir_filename, sample_id))
                  continue

              # check that everything is alright for that sample (i.e. there are 4 corresponding SWIR images for the RGB image)  
              if len(swir_ImageFile) == 4:
                if False:
                  visualize_sample(rgb_ImageFile, swir_ImageFile)
                
                # everything is fine, so we can add the files and the sample to the database
                logger.debug("--------------------------------------------------------------")
                
                # add rgb file
                logger.debug("Adding file {}".format(rgb_ImageFile.path))
                session.add(rgb_ImageFile)
                # add SWIR files
                for o in swir_ImageFile:
                  logger.debug("Adding file {}".format(o.path))
                  session.add(o)
                
                # add corresponding sample
                o = Sample(sample_id, 0)
                session.add(o)
                session.flush()
                session.refresh(o)
                # add the files for that sample
                q_im = session.query(ImageFile).join(Sample).filter(Sample.id == sample_id).order_by(ImageFile.id)
                logger.debug("Adding sample {}".format(sample_id))
                for k in q_im:
                  o.files.append(k)
                  logger.debug("with file {}".format(k))
                
                n_real_samples += 1

              else:
                logger.warning("Cannot add sample {} !".format(sample_id))
            
            else:
              logger.debug("Skipping {} -> Non-frontal face".format(image_filename))
            logger.debug("--------------------------------------------------------------")
        
        # ===============
        # === ATTACKS ===
        # ===============
        if 'BRSU_SpoofDB' in info:
          image, extension = os.path.splitext(info[7])
          image_info = image.split('_')

          # look for RGB images and then get corresponding SWIR images
          if image_info[0] == 'RGB':

            rgb_stem = image_filename.replace(imagesdir, '')
            rgb_stem = rgb_stem.replace(extension, '')
            
            # find whatever is after subject id, which is the attack full description 
            import re
            regex = '(?:'+ image_info[1] + '_)(.*)'
            try:
              attack_full_description = re.search(regex, image).group(1)
              sample_id = image_info[1] + '-' + attack_full_description
            except AttributeError:
              logger.error("Cannot determine the attack type ! - QUITTING")
              import sys
              sys.exit()

            # now get the corresponding SWIR images
            swir_base = image_filename.replace('RGB', 'SWIR') 
            swir_base, _ = os.path.splitext(swir_base)
            swir_ImageFile = []
            for s in swir_suffix:
              swir_image = swir_base + s + '.png'

              # if the SWIR image filename is consistent with RGB, the file exists and can be added 
              if os.path.isfile(swir_image):
                modality = s[1:]
                swir_stem = swir_image.replace(imagesdir, '')
                swir_stem, ext = os.path.splitext(swir_stem)
                assert ext == '.png', "SWIR file {} doesn't have a .png ext".format(swir_filename)
                swir_ImageFile.append(ImageFile(path=swir_stem, sample_id=sample_id, extension=ext, modality=modality))
              
              # if not, handle special cases
              else:
                swir_attack = ''
              
                if image_info[1] == 'P01':

                  if attack_full_description == '2D-Full-Attack-Display':
                    swir_attack = '2D-Full-Attack-Display-1'
                  if attack_full_description == 'Full-Mask-1-Latex_M01':
                    swir_attack = 'Full-Mask-1_M01'
                  if attack_full_description == 'Full-Mask-2-Latex_M02':
                    swir_attack = 'Full-Mask-2_M02'
                  if 'Makeup' in attack_full_description:
                    swir_attack = attack_full_description.replace('_', '-')
                    if 'EyeLiner' in attack_full_description:
                      swir_attack = swir_attack.replace('EyeLiner', 'Eyeliner')
                  if attack_full_description == 'Makeup_Eyeshadow-w':
                    swir_attack = 'Makeup-White_Shadow' 
                  if attack_full_description == 'Makeup_Painted-Mouth':
                    swir_attack = 'Makeup-Painted-Mouth-1' 
                            
                if image_info[1] == 'P02':

                  if attack_full_description == 'Full-Mask-1-Latex_M01':
                    swir_attack = 'Full-Mask-1_M01'
                  if attack_full_description == 'Full-Mask-2-Latex_M02':
                    swir_attack = 'Full-Mask-2_M02'
                  if attack_full_description == 'Full-Mask-3-Silicon_M24':
                    swir_attack = 'Full-Mask-3-Silicon_M23_2'
                  if attack_full_description == 'Full-Mask-4-Silicon_24-K':
                    swir_attack = 'Full-Mask-4-Silicon_M24_K_1'
                  if attack_full_description == 'Full-Mask-4-Silicon_M24-2':
                    swir_attack = 'Full-Mask-4-Silicon_M24_2'
                  if attack_full_description == 'Full-Mask-5-Silicon_M25-5':
                    swir_attack = 'Full-Mask-5-Silicon_M25_2'
                  if attack_full_description == 'Full-Mask-6-Plastic_M21':
                    swir_attack = 'Full-Mask-6_M21'
                  if attack_full_description == 'Full-Mask-7-Resin_M22':
                    swir_attack = 'Full-Mask-7_M22_2'
                  if attack_full_description == 'Makeup-colored_M17_33':
                    swir_attack = 'Makeup-colored_M17_2'
                  if attack_full_description == 'Part-Disg_Fake-Scar_M15-MU-Blut_31':
                    swir_attack = 'Part-Disg_Fake-Scar_M15_MU_KB'
                  if attack_full_description == 'Part-Disg_Fake-Scar_M15-MU':
                    swir_attack = 'Part-Disg_Fake-Scar_M15_MU'
                  if attack_full_description == 'Part-Disg_Soft-Nose-Putty-1_M09-MU':
                    swir_attack = 'Part-Disg_Soft-Nose-Putty_M09_MU'
                  if attack_full_description == 'Part-Disg_Soft-Nose-Putty-1_M09':
                    swir_attack = 'Part-Disg_Soft-Nose-Putty_M09'
                  if attack_full_description == 'Part-Disg_Soft-Nose-Putty-1_M09_17':
                    swir_attack = 'Part-Disg_Soft-Nose-Putty_M09_3'
                  if attack_full_description == 'Part-Disg_Soft-Nose-Putty-2_M10-MU':
                    swir_attack = 'Part-Disg_Soft-Nose-Putty-2_M10_MU'
                  if attack_full_description == 'Part-Disg_Soft-Nose-Putty-2_M10':
                    swir_attack = 'Part-Disg_Soft-Nose-Putty-2_M10_1'
                  if attack_full_description == 'Part-Disg_Soft-Nose-Putty-2_M10_23':
                    swir_attack = ''
                  if attack_full_description == 'Part-Disg_Tattoo_M08':
                    swir_attack = 'Tattoo_M08'
                  
                if image_info[1] == 'P04':

                  if attack_full_description == 'Full-Mask-6-Plastic_M21':
                    swir_attack = ''
                  if attack_full_description == 'Full-Mask-7-Resin_M22':
                    swir_attack = ''
                
                if image_info[1] == 'P05':
                  
                  if attack_full_description == '2D-Part-Attack-Display_03':
                    swir_attack = ''
                  if attack_full_description == '2D-Part-Attack-Display_04':
                    swir_attack = ''
                  if attack_full_description == '2D-Part-Attack-Display_05':
                    swir_attack = ''
                  if attack_full_description == '2D-Part-Attack-Display_06':
                    swir_attack = ''

                swir_image = swir_image.replace(attack_full_description, swir_attack)
                if os.path.isfile(swir_image):
                  swir_stem = swir_image.replace(imagesdir, '')
                  swir_stem, ext = os.path.splitext(swir_stem)
                  assert ext == '.png', "SWIR file {} doesn't have a .png ext".format(swir_filename)
                  modality = s[1:]
                  swir_ImageFile.append(ImageFile(path=swir_stem, sample_id=sample_id, extension=ext, modality=modality))
                else:
                  logger.warning("Cannot find image {} for sample {} !".format(swir_filename, sample_id))
                  continue

            # now check that all the SWIR images are present
            if len(swir_ImageFile) == 4:
                
                rgb_ImageFile = ImageFile(path=rgb_stem, sample_id=sample_id, extension=extension, modality='color')
                if False:
                  visualize_sample(rgb_ImageFile, swir_ImageFile)
                
                # everything is fine, so we can add the files and the sample to the database
                logger.debug("--------------------------------------------------------------")
                
                # get the attack type 
                attack_type = None
                if '01' in attack_full_description or '02' in attack_full_description or '03' in attack_full_description:
                  attack_type = 0
                if 'Paper' in attack_full_description or 'Display' in attack_full_description or 'Printed' in attack_full_description:
                  attack_type = 1
                if 'Mask' in attack_full_description:
                  attack_type = 2
                if 'Disg' in attack_full_description:
                  attack_type = 3
                if 'Cream' in attack_full_description or 'Makeup' in attack_full_description:
                  attack_type = 4

                if attack_type is None:
                  logger.warning("This sample has no attack type ?")
                  import sys
                  sys.exit()

                # add rgb file
                logger.debug("Adding file {}".format(rgb_ImageFile.path))
                session.add(rgb_ImageFile)
                # add SWIR files
                for o in swir_ImageFile:
                  logger.debug("Adding file {}".format(o.path))
                  session.add(o)
                
                # add corresponding sample
                o = Sample(sample_id, attack_type)
                session.add(o)
                session.flush()
                session.refresh(o)
                # add the files for that sample
                q_im = session.query(ImageFile).join(Sample).filter(Sample.id == sample_id).order_by(ImageFile.id)
                logger.debug("Adding sample {} (attack type is {}: {})".format(sample_id, attack_type, attack_map[attack_type]))
                for k in q_im:
                  o.files.append(k)
                  logger.debug("with file {}".format(k))
                
                if attack_type > 0:
                  n_attack_samples += 1
                else:
                  n_real_samples += 1
            
            else: 
              logger.warning("Cannot add sample {} !".format(sample_id))
            logger.debug("-----------------------------------------------------")

  logger.info("Added {} BF samples".format(n_real_samples))
  logger.info("Added {} attack samples".format(n_attack_samples))


def add_protocols(session):
  """

  Protocols for the BRSU database.

  Protocols will be used to get either
  - a training set will all images
  - a test set will all images

  Parameters
  ----------
  session:
    The session to the SQLite database 
  """

  from sqlalchemy import and_
  protocols = ['train', 'test']
  
  group_purpose = {'train': [('train', 'real'), ('train', 'attack')],
                   'test': [('test', 'real'), ('test', 'attack')]
                  }

  for protocol_name in protocols:
    
    p = Protocol(protocol_name)
    logger.info("Adding protocol {}...".format(protocol_name))
    session.add(p)
    session.flush()
    session.refresh(p)

    for proto, gp_list in group_purpose.items():

      if proto == protocol_name:
      
        for gp in gp_list:
          group = gp[0]
          purpose = gp[1]
          pu = ProtocolPurpose(p.id, group, purpose)
       
          logger.info("  Adding protocol purpose ({}, {})...".format(group, purpose))
          session.add(pu)
          session.flush()
          session.refresh(pu)

          if purpose == 'real':
            q = session.query(Sample).filter(Sample.attack_type == 0).order_by(Sample.id)
          if purpose == 'attack':
            q = session.query(Sample).filter(Sample.attack_type > 0).order_by(Sample.id)

          # now add the samples
          for k in q:
            pu.samples.append(k)
          logger.info("added {} samples".format(len(list(q))))


def create_tables(args):
    """Creates all necessary tables (only to be used at the first time)"""

    from bob.db.base.utils import create_engine_try_nolock
    engine = create_engine_try_nolock(args.type, args.files[0], echo=(args.verbose > 2))
    Base.metadata.create_all(engine)


# Driver API
# ==========

def create(args):
  """Creates or re-creates this database"""

  from bob.db.base.utils import session_try_nolock

  print(args)
  dbfile = args.files[0]

  if args.recreate:
    if args.verbose and os.path.exists(dbfile):
      print(('unlinking %s...' % dbfile))
    if os.path.exists(dbfile):
      os.unlink(dbfile)

  if not os.path.exists(os.path.dirname(dbfile)):
    os.makedirs(os.path.dirname(dbfile))

  bob.core.log.set_verbosity_level(logger, args.verbose)

  # the real work...
  create_tables(args)
  s = session_try_nolock(args.type, args.files[0], echo=False)
  
  add_files_and_samples(s, args.imagesdir)
  add_protocols(s)
  s.commit()
  s.close()

  return 0


def add_command(subparsers):
  """Add specific subcommands that the action "create" can use"""

  parser = subparsers.add_parser('create', help=create.__doc__)

  parser.add_argument('-R', '--recreate', action='store_true', default=False,
                      help="If set, I'll first erase the current database")
  parser.add_argument('-v', '--verbose', action='count', default=0,
                      help="Do SQL operations in a verbose way")
  parser.add_argument('imagesdir', action='store', metavar='DIR',
                      help="The path to the extracted images of the database")

  parser.set_defaults(func=create)  # action
