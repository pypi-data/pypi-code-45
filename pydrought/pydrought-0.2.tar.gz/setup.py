#!/usr/bin/env python
from setuptools import setup, find_packages
setup(name='pydrought',
      version='0.2',
      description='Standardized Precipitation Index',
      author='Ch B Komaki',
      author_email='gmail@gmail.com',
      url='http://gau.ac.ir/',
      packages=['pydrought'],
      package_data={'pydrought': ["data/*.csv"]},
##      find_packages=find_packages()
     )
