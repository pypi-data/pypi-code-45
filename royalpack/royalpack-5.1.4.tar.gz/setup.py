# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['royalpack',
 'royalpack.commands',
 'royalpack.events',
 'royalpack.stars',
 'royalpack.tables',
 'royalpack.utils']

package_data = \
{'': ['*']}

install_requires = \
['riotwatcher>=2.7.1,<3.0.0',
 'royalnet[telegram,discord,alchemy_easy,bard,constellation,sentry,herald,coloredlogs]>=5.1.4,<6.0.0',
 'royalspells>=3.2,<4.0']

setup_kwargs = {
    'name': 'royalpack',
    'version': '5.1.4',
    'description': 'A Royalnet command pack for the Royal Games community',
    'long_description': '# `royalpack` [![PyPI](https://img.shields.io/pypi/v/royalpack.svg)](https://pypi.org/project/royalpack/)\n\nThe Royalnet Pack used in the Royal Games community!\n',
    'author': 'Stefano Pigozzi',
    'author_email': 'ste.pigozzi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Steffo99/royalpack',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
