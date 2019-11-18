#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages
import os
import io

import pymerkle


URL = "https://github.com/FoteinosMerg/pymerkle"

current_dir = os.path.abspath(os.path.dirname(__file__))

try:
  with io.open(os.path.join(current_dir, "requirements.txt"),
    encoding="utf-8") as __file:
    install_requires = [_.strip() for _ in __file.readlines()]
except FileNotFoundError:
    install_requires = ["tqdm>=4.28.1",]

with open("README.md", 'r') as __file:
    long_description = __file.read()

def main():
    setup(
       name=pymerkle.__name__,
       version=pymerkle.__version__,
       description=pymerkle.__doc__.strip(),
       long_description=long_description,
       long_description_content_type='text/markdown',
       packages=find_packages(),
       # package_dir={'': 'pymerkle'},
       url=URL,
       project_urls={
            "github": URL,
            "source": "%s/%s" % (URL, "tree/master/%s" % pymerkle.__name__),
            "docs": "https://%s.readthedocs.io/en/latest/" % pymerkle.__name__,
       },
       author="FoteinosMerg",
       author_email="foteinosmerg@protonmail.com",
       python_requires=">=3.6",
       install_requires=install_requires,
       zip_safe=False,
       keywords=[
           "merkle", "proof", "audit", "consistency",
       ],
       classifiers=[
           "Development Status :: 4 - Beta",
           "Intended Audience :: Developers",
           "Intended Audience :: Science/Research",
           "Programming Language :: Python :: 3.6",
           "Operating System :: POSIX",
           "Topic :: Security :: Cryptography",
           "Topic :: Software Development :: Libraries :: Python Modules",
           "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
       ],
    )


if __name__ == '__main__':
    main()
