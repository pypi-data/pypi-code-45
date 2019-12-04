# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['footest']

package_data = \
{'': ['*'],
 'footest': ['cpp_bar/CMakeLists.txt',
             'cpp_bar/CMakeLists.txt',
             'cpp_bar/CMakeLists.txt',
             'cpp_bar/bar.cpp',
             'cpp_bar/bar.cpp',
             'cpp_bar/bar.cpp',
             'cpp_bar/bar.rst',
             'cpp_bar/bar.rst',
             'cpp_bar/bar.rst',
             'f2py_foo/foo.f90',
             'f2py_foo/foo.f90',
             'f2py_foo/foo.rst',
             'f2py_foo/foo.rst']}

install_requires = \
['et-micc-build>=0.10.3,<0.11.0']

setup_kwargs = {
    'name': 'footest',
    'version': '0.0.0',
    'description': '<Enter a one-sentence description of this project here.>',
    'long_description': '=======\nfootest\n=======\n\n\n\n<Enter a one-sentence description of this project here.>\n\n\n* Free software: MIT license\n* Documentation: https://footest.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n',
    'author': 'Engelbert Tijskens',
    'author_email': 'engelbert.tijskens@uantwerpen.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/etijskens/footest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
