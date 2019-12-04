# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['perseus']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['plantuml2freemind = perseus.cli:main']}

setup_kwargs = {
    'name': 'perseus',
    'version': '0.1.1',
    'description': 'Snapshot management tool',
    'long_description': '# perseus\n\nTool for snapshot management. In early progress stage\n\n## Prerequisites\n\n- python >= 3.7\n\n## Installation\n\n`pip install perseus`\n\n## Usage\n\n`perseus --help` or `python -m perseus --help`\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\n### Local development\nThe project uses poetry as a dependency management tool. For local development convenient way to installing and\nrunning project is using `poetry install`. Please, use [>=1.0.0 version](https://pypi.org/project/poetry/#history) of\npoetry even if it is a beta-version.\n\nPoetry automatically creates venv (or uses already activated venv) and install all requirements to it and the project\nitself as `editable` .\nTIP: Use `poetry shell` or `poetry run` before running commands: they activate venv. If you want to connect venv to\nyour IDE, use `poetry env list --full-path`\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Boger',
    'author_email': 'kotvberloge@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/b0g3r/perseus',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
