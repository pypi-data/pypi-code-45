# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['perseus']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'perseus',
    'version': '0.1.0',
    'description': 'Snapshot management tool',
    'long_description': None,
    'author': 'Boger',
    'author_email': 'kotvberloge@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/b0g3r/perseus',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
