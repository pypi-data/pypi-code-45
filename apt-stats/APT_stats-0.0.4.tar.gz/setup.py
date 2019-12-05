#Setup file for Pandora program
import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='APT_stats',
      version='0.0.4',
      description='Python Tool for APT Mass Statistics',
      url='https://victorgarric.github.io/APT_stats/',
      license='GNU GPLv3',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Victor Garric',
      packages=setuptools.find_packages(),
      author_email='victor.garric@gmail.com',
      keywords='TEM image analysis precipitate cluster clustering',
      install_requires=['mendeleev','tableprint','matplotlib','numpy'],
      zip_safe=False)