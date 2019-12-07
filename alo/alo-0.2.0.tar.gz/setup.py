# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alo']

package_data = \
{'': ['*']}

install_requires = \
['click', 'more-itertools', 'six', 'typing-extensions']

extras_require = \
{':python_version < "3.7"': ['dataclasses', 'typing', 'contextvars']}

entry_points = \
{'console_scripts': ['alo = alo.cli:main']}

setup_kwargs = {
    'name': 'alo',
    'version': '0.2.0',
    'description': 'A tool to combine function with DAG',
    'long_description': '# alo\n\n[![](https://img.shields.io/pypi/v/alo.svg)](https://pypi.python.org/pypi/alo)\n[![](https://img.shields.io/travis/uchuhimo/alo.svg)](https://travis-ci.org/uchuhimo/alo)\n[![](https://github.com/uchuhimo/alo/workflows/Python%20package/badge.svg)](https://github.com/uchuhimo/alo/actions)\n[![Documentation Status](https://readthedocs.org/projects/alo/badge/?version=latest)](https://alo.readthedocs.io/en/latest/?badge=latest)\n[![Updates](https://pyup.io/repos/github/uchuhimo/alo/shield.svg)](https://pyup.io/repos/github/uchuhimo/alo/)\n\nA tool to combine function with DAG.\n\n- Documentation: https://alo.readthedocs.io.\n\n## Development\n\n### Create a virtual environment\n\n```bash\nconda env create -f environment.yml\nsource activate alo\n```\n\n### Install dependencies\n\nThere are two options:\n\n- Use poetry:\n    ```bash\n    poetry install\n    ```\n- Use pip:\n    ```bash\n    pip install -e ".[dev]"\n    ```\n\n### Update dependencies\n\n```bash\npoetry update\n```\n\n### Bump version\n\n```bash\nbumpversion minor  # major, minor, patch\n```\n\n### Show information about installed packages\n\n```bash\npoetry show\n```\n\n### Show dependency tree\n\n```bash\ndephell deps tree\n# or\ndephell deps tree pytest\n```\n\n### Install git pre-commit hooks\n\n```bash\npre-commit install\n```\n\n# License\n\n© uchuhimo, 2019. Licensed under an [Apache 2.0](./LICENSE) license.\n',
    'author': 'uchuhimo',
    'author_email': 'uchuhimo@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/uchuhimo/alo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
