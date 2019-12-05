# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['genclf']

package_data = \
{'': ['*'], 'genclf': ['models/*']}

install_requires = \
['joblib>=0.14.0,<0.15.0', 'scikit-learn>=0.22.0,<0.23.0']

setup_kwargs = {
    'name': 'genclf',
    'version': '0.0.1',
    'description': 'Gender Classifier ML Package for classifying gender using firstname',
    'long_description': '## GenderClassifier Tool\n+ Aim: using ML models as packages\n+ Purpose: for classifying gender of individuals using their first names\n\n### Installation\n```bash\npip install genclf\n```\n\n### Usage\n#### Basic usage\n```python\n>>> from genclf import GenderClassifier\n>>> g = GenderClassifier()\n>>> g.name = \'Jess\'\n>>> g.predict()\n```\n\n#### Loading Different Models\n```python\n>>> from genclf import GenderClassifier\n>>> g = GenderClassifier()\n>>> g.name = \'Jessica\'\n>>> g.load(\'nv\')\n>>> g.predict()\n```\n\n#### Using the Classify Method\n```python\n>>> from genclf import GenderClassifier\n>>> g = GenderClassifier()\n>>> g.load(\'nb\')\n>>> g.classify("David")\n```\n\n#### Check Gender\n```python\n>>> from genclf import GenderClassifier\n>>> g = GenderClassifier()\n>>> g.is_male("Mark")\n```\n\n```python\n>>> from genclf import GenderClassifier\n>>> g = GenderClassifier()\n>>> g.is_female("Mary")\n```\n\n#### Requirements\n+ Joblib\n+ Scikit-learn\n\n#### Maintainer\n+ Jesse E.Agbe(JCharis)\n+ Jesus Saves@JCharisTech',
    'author': 'JCharis',
    'author_email': 'jcharistech@gmail.com',
    'url': 'https://github.com/Jcharis/genclf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
