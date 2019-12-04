# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['learnupon']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'learnupon',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Swimlane Learnupon\n\n## Description\nA python package for interacting with the LearnUpon LMS.\n\n## Installation\n```\npip install learnupon\n```\n\n## Usage\n```\nfrom learnupon import LearnUpon\n\nlearnupon = LearnUpon(portal_url="https://myportal.learnupon.com", \n                      username="abc123", password="def456")\n                      \nnew_user = learnupon.invite_user(email_address="new_user@mycompany.com")\n```',
    'author': 'Michael Butler',
    'author_email': 'michael.butler@swimlane.com',
    'url': 'https://github.com/swimlane/swimlane-learnupon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
