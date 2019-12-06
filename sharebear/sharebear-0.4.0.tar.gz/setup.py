#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyyaml',
    'traceback',
    'random',
    'argparse',
    'getpas',
    'shutil'
    ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Anthony Edward Galassi",
    author_email='anthony.galassi@protonmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This project provides a simple api for setting and getting variables and objects from a text file.",
    entry_points={
        'console_scripts': [
            'sharebear=sharebear.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sharebear',
    name='sharebear',
    packages=find_packages(include=['sharebear', 'sharebear.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bendhouseart/sharebear',
    version='0.4.0',
    zip_safe=False,
)
