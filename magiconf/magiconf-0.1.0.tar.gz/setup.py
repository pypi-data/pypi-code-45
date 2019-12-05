# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['magiconf']

package_data = \
{'': ['*'], 'magiconf': ['.git/*', '.git/hooks/*', '.git/info/*']}

setup_kwargs = {
    'name': 'magiconf',
    'version': '0.1.0',
    'description': 'A small library to automagically load and parse configuration from either environment, configuration file or command line arguments.',
    'long_description': None,
    'author': 'Vladimir Kotikov',
    'author_email': 'kotikov.vladimir@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
