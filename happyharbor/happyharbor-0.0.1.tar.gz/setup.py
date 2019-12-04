# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py
from os import path

import setuptools

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='happyharbor',
    version="0.0.1",
    author="Giorgos Trichopoulos",
    author_email="giorgos.trichopoulos@gmail.com",
    description="A small example package",
    long_description_content_type="text/markdown",
    long_description=readme,
    url="https://happyharbor.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

