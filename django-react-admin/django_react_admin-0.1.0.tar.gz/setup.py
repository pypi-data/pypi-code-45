# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['django_react_admin',
 'django_react_admin.management',
 'django_react_admin.migrations']

package_data = \
{'': ['*'],
 'django_react_admin': ['src/*',
                        'src/public/*',
                        'src/src/*',
                        'static/*',
                        'static/django_react_admin/*',
                        'static/django_react_admin/static/css/*',
                        'static/django_react_admin/static/js/*'],
 'django_react_admin.management': ['commands/*']}

install_requires = \
['django>=2.2,<3.0',
 'django_filters>=0.2.1,<0.3.0',
 'djangorestframework>=3.10,<4.0']

setup_kwargs = {
    'name': 'django-react-admin',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ph',
    'author_email': 'robotnaoborot@gmail.com',
    'url': 'https://github.com/pawnhearts/django_react_admin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
