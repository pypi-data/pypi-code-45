import os
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = open(os.path.join(BASEDIR, 'VERSION')).read().strip()

BASE_DEPENDENCIES = [
    'pandas>=0.25',
    'python-dateutil>=2.8'
]

# allow setup.py to be run from any path
os.chdir(os.path.normpath(BASEDIR))

setup(
    name='wf-cv-datetime-utils',
    packages=find_packages(),
    version=VERSION,
    include_package_data=True,
    description='Miscellaneous utilities for working with datetimes when processing images',
    long_description=open('README.md').read(),
    url='https://github.com/WildflowerSchools/wf-cv-datetime-utils',
    author='Theodore Quinn',
    author_email='ted.quinn@wildflowerschools.org',
    install_requires=BASE_DEPENDENCIES,
    keywords=['cv', 'datetime'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
