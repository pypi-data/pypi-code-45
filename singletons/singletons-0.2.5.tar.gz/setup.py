# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['singletons']

package_data = \
{'': ['*']}

extras_require = \
{'eventlet': ['eventlet>=0.25.1,<0.26.0'], 'gevent': ['gevent>=1.4,<2.0']}

setup_kwargs = {
    'name': 'singletons',
    'version': '0.2.5',
    'description': 'Singleton metaclasses and singleton factories',
    'long_description': None,
    'author': 'James Roeder',
    'author_email': 'jmaroeder@gmail.com',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
