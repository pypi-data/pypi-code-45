# Copyright (c) 2013, 2019 gocept gmbh & co. kg
# See also LICENSE.txt

# This should be only one line. If it must be multi-line, indent the second
# line onwards to keep the PKG-INFO file format intact.
"""
ZConfig statement to register a logging handler using WatchedFileHandler
"""

from setuptools import setup, find_packages


def read(name):
    """Read a file."""
    with open(name) as f:
        return f.read()


setup(
    name='zconfig_watchedfile',
    version='1.2',

    install_requires=[
        'ZConfig',
        'setuptools',
    ],

    extras_require={
        'test': [
        ],
    },

    author='gocept <mail@gocept.com>',
    author_email='mail@gocept.com',
    license='ZPL 2.1',
    url='https://github.com/gocept/zconfig_watchedfile',
    keywords='ZConfig WatchedFileHandler logging handler',
    classifiers=[
        'License :: OSI Approved :: Zope Public License',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description=__doc__.strip(),
    long_description='\n\n'.join(read(name) for name in (
        'README.rst',
        'CHANGES.rst',
    )),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
)
