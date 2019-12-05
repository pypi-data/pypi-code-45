# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['igppack', 'igppack.commands', 'igppack.tables']

package_data = \
{'': ['*']}

install_requires = \
['royalnet[telegram,discord,alchemy_easy,bard,constellation,sentry,herald,coloredlogs]>=5.1.2,<6.0.0']

setup_kwargs = {
    'name': 'igppack',
    'version': '0.10.1',
    'description': '',
    'long_description': None,
    'author': 'Alby1',
    'author_email': '30355916+Alby1@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
