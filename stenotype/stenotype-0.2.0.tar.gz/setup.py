# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['stenotype', 'stenotype.backend']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['stenotype = stenotype.cli:cli']}

setup_kwargs = {
    'name': 'stenotype',
    'version': '0.2.0',
    'description': 'Support for shorthand type annotations.',
    'long_description': 'stenotype\n=========\n\n.. image:: https://img.icons8.com/color/144/000000/typewriter-with-tablet.png\n   :alt: Tablet in a typewriter\n   :align: center\n\n.. image:: https://github.com/a-recknagel/stenotype/workflows/CI-CD/badge.svg\n   :alt: Main workflow status\n   :target: https://github.com/a-recknagel/stenotype/actions\n\n.. image:: https://img.shields.io/pypi/v/stenotype\n   :alt: Current pyPI version\n   :target: https://pypi.org/project/stenotype/\n\n.. image:: https://img.shields.io/badge/docs-github--pages-blue\n   :alt: Documentation home\n   :target: https://a-recknagel.github.io/stenotype/\n\n.. image:: https://img.shields.io/pypi/l/stenotype\n   :alt: Package licenseCurrent pyPI version\n   :target: https://pypi.org/project/stenotype/\n\n.. image:: https://img.shields.io/pypi/pyversions/stenotype\n   :alt: Supported on python versions\n   :target: https://pypi.org/project/stenotype/\n\n.. image:: https://img.shields.io/badge/codestyle-black-black\n   :alt: Any color you want\n   :target: https://black.readthedocs.io/en/stable/\n\n.. image:: https://badges.gitter.im/stenotype/community.svg\n   :alt: Join the chat at https://gitter.im/stenotype/community\n   :target: https://gitter.im/stenotype/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge\n\n.. header-end\n\nProject Description\n-------------------\n\n.. put your project description here\n',
    'author': 'Arne Recknagel',
    'author_email': 'arne.recknagel@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/a-recknagel/stenotype',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
