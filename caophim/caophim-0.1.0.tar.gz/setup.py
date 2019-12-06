# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['caophim', 'main', 'main.migrations']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.0,<4.0',
 'goodconf>=1.0,<2.0',
 'gunicorn>=20.0,<21.0',
 'psycopg2>=2.8,<3.0']

entry_points = \
{'console_scripts': ['generate-config = caophim:generate_config',
                     'manage = caophim:manage']}

setup_kwargs = {
    'name': 'caophim',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Bùi Thành Nhân',
    'author_email': 'hi@imnhan.com',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
