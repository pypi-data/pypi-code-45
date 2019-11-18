# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['et_micc_build']

package_data = \
{'': ['*'],
 'et_micc_build': ['cmake_tools/F2pyAddModule.cmake',
                   'cmake_tools/F2pyAddModule.cmake',
                   'cmake_tools/F2pyAddModule.cmake',
                   'cmake_tools/F2pyAddModule.cmake',
                   'cmake_tools/F2pyAddModule.cmake',
                   'cmake_tools/F2pyAddModule.cmake',
                   'cmake_tools/F2pyAddModule.cmake',
                   'cmake_tools/FindF2PY.cmake',
                   'cmake_tools/FindF2PY.cmake',
                   'cmake_tools/FindF2PY.cmake',
                   'cmake_tools/FindF2PY.cmake',
                   'cmake_tools/FindF2PY.cmake',
                   'cmake_tools/FindF2PY.cmake',
                   'cmake_tools/FindF2PY.cmake',
                   'cmake_tools/FindPythonLibsNew.cmake',
                   'cmake_tools/FindPythonLibsNew.cmake',
                   'cmake_tools/FindPythonLibsNew.cmake',
                   'cmake_tools/FindPythonLibsNew.cmake',
                   'cmake_tools/FindPythonLibsNew.cmake',
                   'cmake_tools/FindPythonLibsNew.cmake',
                   'cmake_tools/FindPythonLibsNew.cmake',
                   'cmake_tools/pybind11Config.cmake',
                   'cmake_tools/pybind11Config.cmake',
                   'cmake_tools/pybind11Config.cmake',
                   'cmake_tools/pybind11Config.cmake',
                   'cmake_tools/pybind11Config.cmake',
                   'cmake_tools/pybind11Config.cmake',
                   'cmake_tools/pybind11Config.cmake',
                   'cmake_tools/pybind11ConfigVersion.cmake',
                   'cmake_tools/pybind11ConfigVersion.cmake',
                   'cmake_tools/pybind11ConfigVersion.cmake',
                   'cmake_tools/pybind11ConfigVersion.cmake',
                   'cmake_tools/pybind11ConfigVersion.cmake',
                   'cmake_tools/pybind11ConfigVersion.cmake',
                   'cmake_tools/pybind11ConfigVersion.cmake',
                   'cmake_tools/pybind11Targets.cmake',
                   'cmake_tools/pybind11Targets.cmake',
                   'cmake_tools/pybind11Targets.cmake',
                   'cmake_tools/pybind11Targets.cmake',
                   'cmake_tools/pybind11Targets.cmake',
                   'cmake_tools/pybind11Targets.cmake',
                   'cmake_tools/pybind11Targets.cmake',
                   'cmake_tools/pybind11Tools.cmake',
                   'cmake_tools/pybind11Tools.cmake',
                   'cmake_tools/pybind11Tools.cmake',
                   'cmake_tools/pybind11Tools.cmake',
                   'cmake_tools/pybind11Tools.cmake',
                   'cmake_tools/pybind11Tools.cmake',
                   'cmake_tools/pybind11Tools.cmake']}

install_requires = \
['click>=7.0,<8.0',
 'cmake>=3.15.3,<4.0.0',
 'et-micc-tools>=0.1.1,<0.2.0',
 'numpy>=1.17.0,<2.0.0',
 'pybind11>=2.2.4,<3.0.0']

entry_points = \
{'console_scripts': ['micc-build = et_micc_build:cli_build.main']}

setup_kwargs = {
    'name': 'et-micc-build',
    'version': '0.0.3',
    'description': 'CLI micc-build and module for building binary extensions created with micc.',
    'long_description': '=============\net-micc-build\n=============\n\n\n\n<Enter a one-sentence description of this project here.>\n\n\n* Free software: MIT license\n* Documentation: https://et-micc-build.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n',
    'author': 'Engelbert Tijskens',
    'author_email': 'engelbert.tijskens@uantwerpen.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/etijskens/et-micc-build',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
