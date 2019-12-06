# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['aioaerospike', 'aioaerospike.protocol']

package_data = \
{'': ['*']}

install_requires = \
['bcrypt>=3.1,<4.0', 'construct>=2.9,<3.0']

setup_kwargs = {
    'name': 'aioaerospike',
    'version': '0.1.1',
    'description': 'Async Pure Python implementation of Aerospike client',
    'long_description': '[![codecov](https://codecov.io/gh/aviramha/aioaerospike/branch/master/graph/badge.svg)](https://codecov.io/gh/aviramha/aioaerospike)\n[![Build Status](https://travis-ci.com/aviramha/aioaerospike.svg?branch=master)](https://travis-ci.com/aviramha/aioaerospike)\n\nThis library is planned to be an async API for Aerospike.\nThe library will be Pure-Python, Protocol based on the C Client.\n\n\n** This package is 3rd party, unrelated to Aerospike company **\n\nLicensed under MIT. See LICENSE\n',
    'author': 'Aviram Hassan',
    'author_email': 'aviramyhassan@gmail.com',
    'url': 'https://github.com/aviramha/aioaerospike',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
