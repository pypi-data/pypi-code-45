# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['db_playmate', 'db_playmate.kobo']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=1.7,<2.0',
 'boxsdk>=2.6,<3.0',
 'docutils>=0.15.2,<0.16.0',
 'flask>=1.1.1,<2.0.0',
 'furl>=2.1,<3.0',
 'keyring>=19.2,<20.0',
 'pytest-cov>=2.8,<3.0',
 'requests>=2.22,<3.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['sync = db_playmate:cli.main']}

setup_kwargs = {
    'name': 'db-playmate',
    'version': '0.1.0',
    'description': 'Client scripts for Databrary PLAY project.',
    'long_description': None,
    'author': 'Shohan Hasan',
    'author_email': 'shohan.hasan.x6@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
