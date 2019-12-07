#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup file
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="v_ft", # Replace with your own username
    version="0.0.1",
    author="Travis_li",
    author_email="wli10@email.wm.edu",
    description="featuretools related extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeremite/ft_extension",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)