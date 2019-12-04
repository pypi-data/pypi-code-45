# -*- coding: utf-8 -*-

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

import os
from setuptools import find_packages
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    value = open(os.path.join(os.path.dirname(__file__), fname), 'r', encoding='utf-8').read()
    return str(value)


setup(name='iotoutlier1',
      version='0.0.1',
      description='Data representation for IoT traffic',
      long_description=read('readme.md'),
      # long_description='Data representation for IoT traffic',
      long_description_content_type="text/markdown",
      author='Kun',
      author_email='kun.bj@outlook.com',
      url='https://github.com/Learn-Live/IoT_feature_sets_comparison',
      download_url='https://github.com/Learn-Live/IoT_feature_sets_comparison',
      license='xxx',
      python_requires='>=3.6',
      install_requires=['numpy>=1.17.0',
                        'scipy>=1.3.1',
                        'pandas>=0.25.1',
                        'pyod>=0.7.4',
                        'scapy>=2.4.3',
                        'scikit_learn>=0.21.3',
                        'tensorflow',
                        'tensorboard',
                        'keras'],
      extras_require={
          'visualize': ['matplotlib>=3.3.1'],
          'tests': ['pytest',
                    'requests',
                    'markdown'],
          'terminal': ['colorama']
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())  # automatically finds the packages with __init__.py file
                                # starts from the setup.py's directory
