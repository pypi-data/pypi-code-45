#!/usr/bin/env python
# encoding: utf-8

import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="mrsn-might",
    version="1.0.3",
    author="Brendan Corey",
    author_email="brendan.w.corey.ctr@mail.mil",
    description="MIGHT: MRSN Integrated Genome Handling Tool for bacterial clinical isolates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/mrsn-bio/might/",
    license="GPLv3",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['might = might.might:premain',
                                      'allmight = might.allmight:main']
                  },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires='>=3.6'
)