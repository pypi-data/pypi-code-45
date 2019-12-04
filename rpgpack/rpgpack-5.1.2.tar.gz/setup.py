# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpgpack',
 'rpgpack.commands',
 'rpgpack.events',
 'rpgpack.stars',
 'rpgpack.tables',
 'rpgpack.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.5,<4.0',
 'dice>=2.4.2,<3.0.0',
 'royalnet[telegram,discord,alchemy_easy,bard,constellation,sentry,herald,coloredlogs]>=5.1.2,<6.0.0',
 'sortedcontainers>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'rpgpack',
    'version': '5.1.2',
    'description': 'A Royalnet Pack to play role-playing-games',
    'long_description': '# `rpgpack` [![PyPI](https://img.shields.io/pypi/v/rpgpack.svg)](https://pypi.org/project/rpgpack/)\n\nA Royalnet Pack to play role-playing-games\n',
    'author': 'Stefano Pigozzi',
    'author_email': 'ste.pigozzi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Steffo99/royalnet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
