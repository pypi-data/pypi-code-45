# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['diot']
install_requires = \
['inflection<1.0.0']

setup_kwargs = {
    'name': 'diot',
    'version': '0.0.4',
    'description': 'Python dictionary with dot notation.',
    'long_description': '![Logo](https://raw.githubusercontent.com/pwwang/diot/master/logo.png)\n\nPython dictionary with dot notation\n\n- Partially compartible with `python-box`\n- Issue #87 of `python-box` fixed\n- Nest conversion of inside `dict/list` turned off\n- Customization of key conversion\n\n```python\nfrom diot import Diot, NestDiot\n\nmovie_data = {\n  "movies": {\n    "Spaceballs": {\n      "imdb stars": 7.1,\n      "rating": "PG",\n      "length": 96,\n      "director": "Mel Brooks",\n      "stars": [{"name": "Mel Brooks", "imdb": "nm0000316", "role": "President Skroob"},\n                {"name": "John Candy","imdb": "nm0001006", "role": "Barf"},\n                {"name": "Rick Moranis", "imdb": "nm0001548", "role": "Dark Helmet"}\n      ]\n    },\n    "Robin Hood: Men in Tights": {\n      "imdb stars": 6.7,\n      "rating": "PG-13",\n      "length": 104,\n      "director": "Mel Brooks",\n      "stars": [\n                {"name": "Cary Elwes", "imdb": "nm0000144", "role": "Robin Hood"},\n                {"name": "Richard Lewis", "imdb": "nm0507659", "role": "Prince John"},\n                {"name": "Roger Rees", "imdb": "nm0715953", "role": "Sheriff of Rottingham"},\n                {"name": "Amy Yasbeck", "imdb": "nm0001865", "role": "Marian"}\n      ]\n    }\n  }\n}\n\n# Box is a conversion_box by default, pass in `conversion_box=False` to disable that behavior\n# Explicitly tell Diot to convert dict/list inside\nmovie_diot = Diot(movie_data, diot_nest = True)\n# or movie_diot = NestDiot(movie_data)\n\nmovie_diot.movies.Robin_Hood_Men_in_Tights.imdb_stars\n# 6.7\n\nmovie_diot.movies.Spaceballs.stars[0].name\n# \'Mel Brooks\'\n\n# Different as box, you have to use Diot for new data in a list\nmovie_diot.movies.Spaceballs.stars.append(\n\tDiot({"name": "Bill Pullman", "imdb": "nm0000597", "role": "Lone Starr"}))\nmovie_diot.movies.Spaceballs.stars[-1].role\n# \'Lone Starr\'\n```\n\n## Install\n```shell\npip install diot\n```\n\n## Diot\n\nInstantiated the same ways as `dict`\n```python\nDiot({\'data\': 2, \'count\': 5})\nDiot(data=2, count=5)\nDiot({\'data\': 2, \'count\': 1}, count=5)\nDiot([(\'data\', 2), (\'count\', 5)])\n\n# All will create\n# Diot([(\'data\', 2), (\'count\', 5)], diot_nest = False, diot_transform = \'safe\')\n```\n\nSame as `python-box`, `Diot` is a subclass of dict which overrides some base functionality to make sure everything stored in the dict can be accessed as an attribute or key value.\n\n```python\ndiot = Diot({\'data\': 2, \'count\': 5})\ndiot.data == diot[\'data\'] == getattr(diot, \'data\')\n```\n\nBy default, diot uses a safe transformation to transform keys into safe names that can be accessed by `diot.xxx`\n```python\ndt = Diot({"321 Is a terrible Key!": "yes, really"})\ndt._321_Is_a_terrible_Key_\n# \'yes, really\'\n```\n\nDifferent as `python-box`, duplicate attributes are not allowed.\n```python\ndt = Diot({"!bad!key!": "yes, really", ".bad.key.": "no doubt"})\n# KeyError\n```\n\nUse different transform functions:\n\n```python\ndt = Diot(oneTwo = 12, diot_transform = \'snake_case\')\n# or use alias:\n# dt = SnakeDiot(oneTwo = 12)\ndt.one_two == dt[\'one_two\'] == dt[\'oneTwo\'] == 12\n\ndt = Diot(one_two = 12, diot_transform = \'camel_case\')\n# or use alias:\n# dt = CamelDiot(one_two = 12)\ndt.oneTwo == dt[\'one_two\'] == dt[\'oneTwo\'] == 12\n\ndt = Diot(one_two = 12, diot_transform = \'upper\')\ndt.ONE_TWO == dt[\'one_two\'] == dt[\'ONETWO\'] == 12\n\ndt = Diot(ONE_TWO = 12, diot_transform = \'lower\')\ndt.one_two == dt[\'ONE_TWO\'] == dt[\'one_two\'] == 12\n```\n\nUse your own transform function:\n\n```python\nimport inflection\n\ndt = Diot(post = 10, diot_transform = inflection.pluralize)\ndt.posts == dt[\'posts\'] == dt[\'post\'] == 10\n```\n\n## OrderedDiot\n```python\ndiot_of_order = OrderedDiot()\ndiot_of_order.c = 1\ndiot_of_order.a = 2\ndiot_of_order.d = 3\n\nlist(diot_of_order.keys()) == [\'c\', \'a\', \'d\']\n```\n',
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'url': 'https://github.com/pwwang/diot',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
