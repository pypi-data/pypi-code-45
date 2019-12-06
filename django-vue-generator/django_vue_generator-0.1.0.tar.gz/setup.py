# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['django_vue_generator',
 'django_vue_generator.management',
 'django_vue_generator.migrations']

package_data = \
{'': ['*'], 'django_vue_generator.management': ['commands/*']}

install_requires = \
['django-filter>=2.2,<3.0',
 'django>=2.2,<3.0',
 'djangorestframework>=3.10,<4.0']

setup_kwargs = {
    'name': 'django-vue-generator',
    'version': '0.1.0',
    'description': 'Generates vue frontend for django rest framework projects.',
    'long_description': None,
    'author': 'ph',
    'author_email': 'robotnaoborot@gmail.com',
    'url': 'https://github.com/pawnhearts/django_vue_generator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
