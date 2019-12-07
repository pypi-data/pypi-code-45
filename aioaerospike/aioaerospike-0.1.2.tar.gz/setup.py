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
    'version': '0.1.2',
    'description': 'Async Pure Python implementation of Aerospike client',
    'long_description': "# aioaerospike\n[![codecov](https://codecov.io/gh/aviramha/aioaerospike/branch/master/graph/badge.svg)](https://codecov.io/gh/aviramha/aioaerospike)\n[![Build Status](https://travis-ci.com/aviramha/aioaerospike.svg?branch=master)](https://travis-ci.com/aviramha/aioaerospike)\n\nThis library is planned to be an async API for Aerospike.\nThe library will be Pure-Python, Protocol based on the C Client.\n\n## Installation\nUsing pip\n```\n$ pip install aioaerospike\n```\n\n## Contributing\n\nTo work on the `aioaerospike` codebase, you'll want to fork the project and clone it locally and install the required dependencies via [poetry](https://poetry.eustace.io):\n\n```sh\n$ git clone git@github.com:{USER}/aioaerospike.git\n$ make install\n```\n\nTo run tests and linters use command below (Requires aerospike to run locally on port 3000):\n\n```sh\n$ make lint && make test\n```\n\nIf you want to run only tests or linters you can explicitly specify which test environment you want to run, e.g.:\n\n```sh\n$ make lint-black\n```\n\n## License\n\n`aioaerospike` is licensed under the MIT license. See the license file for details.\n\n# Latest changes\n\n## 0.1.2 (2019-12-08)\n- Fixed key digest, key type can be all supported types (int, float, str, bytes)\n\n## 0.1.1 (2019-12-07)\n- Fixed license and metadata\n\n## 0.1.0 (2019-12-07)\n\n- Initial release.\n\n\n## This package is 3rd party, unrelated to Aerospike company\n",
    'author': 'Aviram Hassan',
    'author_email': 'aviramyhassan@gmail.com',
    'url': 'https://github.com/aviramha/aioaerospike',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
