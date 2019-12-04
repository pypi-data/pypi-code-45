# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['ninja']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'django-ninja',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Vitaliy Kucheriavyi',
    'author_email': 'ppr.vitaly@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
