import os
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = open(os.path.join(BASEDIR, 'VERSION')).read().strip()

BASE_DEPENDENCIES = [
    'wf-cv-utils>=0.1.0',
    'wf-cv-datetime-utils>=0.1.0',
    'wf-smc-kalman>=0.1.0',
    'numpy>=1.14',
    'scipy>=1.1',
    'pandas>=0.23',
    'matplotlib>=2.2',
    'networkx>=2.1',
    'boto3>=1.7'
]

# allow setup.py to be run from any path
os.chdir(os.path.normpath(BASEDIR))

setup(
    name='wf-pose-tracking-3d',
    packages=find_packages(),
    version=VERSION,
    include_package_data=True,
    description='Classes and methods for performing 3D pose tracking from 2D poses',
    long_description=open('README.md').read(),
    url='https://github.com/WildflowerSchools/wf-pose-tracking-3d',
    author='Theodore Quinn',
    author_email='ted.quinn@wildflowerschools.org',
    install_requires=BASE_DEPENDENCIES,
    keywords=['cv'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
