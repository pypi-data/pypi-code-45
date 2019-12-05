# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['observable_models']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.0,<4.0', 'rx>=3.0,<4.0']

setup_kwargs = {
    'name': 'django-observable-models',
    'version': '0.1.0',
    'description': '',
    'long_description': "# Django Observable Models\n\nDjango Observable Models allows you to subscribe to model operations using rxpy Observables. This is particularly useful for implementing things like GraphQL subscriptions.\n\n## Installation\n\n```bash\n$ pip install django-observable-models\n```\n\n## Usage\n\n```python\n# yourapp/models.py\nfrom observable_models.models import ObservableModel\n\nclass YourModel(ObservableModel):\n    pass\n\n# Subscribe to model creation\nYourModel.model_events.pipe(filter(lamda event: event['operation'] == YourModel.CREATED))\n\n# Subscribe to model updates \nYourModel.model_events.pipe(filter(lamda event: event['operation'] == YourModel.UPDATED))\n\n# Subscribe to model deletion \nYourModel.model_events.pipe(filter(lamda event: event['operation'] == YourModel.DELETED))\n```",
    'author': 'Jayden Windle',
    'author_email': 'jaydenwindle@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
