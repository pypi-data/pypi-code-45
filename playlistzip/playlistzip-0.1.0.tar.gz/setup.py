# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['playlistzip']

package_data = \
{'': ['*']}

install_requires = \
['jsonpath-rw>=1.4,<2.0', 'pycurl>=7.43,<8.0']

entry_points = \
{'console_scripts': ['plz = playlistzip.cli:main']}

setup_kwargs = {
    'name': 'playlistzip',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ross Vorotynskij',
    'author_email': 'ross@rvcg.net',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
