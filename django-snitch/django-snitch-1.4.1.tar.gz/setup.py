#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['snitch',
 'snitch.migrations',
 'snitch.schedules',
 'snitch.schedules.migrations']

package_data = \
{'': ['*'],
 'snitch': ['locale/*', 'locale/es_ES/*', 'locale/es_ES/LC_MESSAGES/*']}

install_requires = \
['django',
 'django-model-utils',
 'django-push-notifications',
 'bleach',
 'celery']

extras_require = \
{'doc': ['sphinx'],
 'test': ['pytest', 'pytest-django', 'pytest-cov', 'factory_boy']}

setup(name='django-snitch',
      version='1.4.1',
      description='Django app made to integrate generic events that create notifications that',
      author='Marcos Gabarda',
      author_email='hey@marcosgabarda.com',
      url='https://github.com/marcosgabarda/django-snitch',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      python_requires='>=3.6',
     )
