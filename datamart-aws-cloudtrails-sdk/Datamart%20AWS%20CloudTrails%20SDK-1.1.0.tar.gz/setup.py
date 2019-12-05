# -*- coding: utf-8 -*-

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'boto3==1.10.13'
]

# test_requires = [
#     'faker',
#     'pytest'
# ]

setuptools.setup(
    name="Datamart AWS CloudTrails SDK",
    # version='0.0.0',  # will be set by setuptools_scm at build time
    use_scm_version={
        'write_to': 'dm/cloudtrailsdk/__version__.py',
        'write_to_template': '__version__ = "{version}"',
        'tag_regex': r'^v(?:[\w-]+-)?(?P<version>[vV]?\d+(?:\.\d+){0,2}[^\+]+)(?:\+.*)?$'
    },
    install_requires=requires,
    # tests_require=test_requires,
    author="Yaisel Hurtado, Raydel Miranda, Yordano Gonzalez",
    author_email="hurta2yaisel@gmail.com, raydel.miranda.gomez@gmail.com, yorda891216@gmail.com",
    description="AWS Python CloudTrails SDK for Logs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/elasbit/dm-cloudtrails-sdk-py",
    packages=setuptools.find_packages(where='.', exclude=('tests',)),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <3.8",
    classifiers=(
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent"
    ),
)
