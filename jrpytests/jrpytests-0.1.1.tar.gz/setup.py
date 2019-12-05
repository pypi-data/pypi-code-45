# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['jrpytests']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.7.9', 'pytest>=3.0,<4.0']

setup_kwargs = {
    'name': 'jrpytests',
    'version': '0.1.1',
    'description': '',
    'long_description': "# jrpytests\n\n## Overview\n\nThis package contains functions for CI testing of JR python packages and was created using the poetry python package, for more details see\n\n[https://github.com/sdispater/poetry](https://github.com/sdispater/poetry).\n\njrpytests allows: \n\n* to run pytest,\n* to check coding style (via flake8) in python files, \n* to extract python chunks from Rmd files and check their coding style,\n* to check if a directory 'vignettes' exists in appropriate folder and,\n* to count pdf files in 'vignettes' and compare to number of Rmd files.\n\nThe flake8 configuration file is stored in this package, see\n\njrpytests/flake8\\_config.ini.\n\n## Basic usage\n\nImport the package using\n\n`import jrpytests`.\n\nRun pytest\n\n`jrpytests.runpytests()`.\n\nRun flake8 in python files\n\n`jrpytests.runflake8pythonfiles()`.\n\nRun flake8 in Rmd python chunks\n\n`jrpytests.runflake8rmdpychunks()`.\n\nCheck 'vignettes' and number of pdf files in it\n\n`jrpytests.checkvignettespdffiles()`.\n",
    'author': 'Matteo Leo',
    'author_email': 'matteoleo89@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
