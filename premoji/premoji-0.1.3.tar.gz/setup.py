"""Minimal setup file for learn project."""

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name = 'premoji',
    version = '0.1.3',
    description = 'predict emoji on given text',
    long_description = README,
    long_description_content_type = "text/markdown",
    license = "MIT",
    author = 'Qiang Huang',
    author_email = 'nickyfoto@gmail.com',
    url = 'https://macworks.io',
    download_url = 'https://github.com/nickyfoto/premoji/archive/v0.1.3-alpha.tar.gz',
    packages = find_packages(where='src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    install_requires = [
          'numpy',
          'scikit-learn',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.7',
    ]
)
