# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['httprunner',
 'httprunner.loader',
 'httprunner.plugins',
 'httprunner.plugins.locusts']

package_data = \
{'': ['*'], 'httprunner': ['static/*']}

install_requires = \
['colorama>=0.4.1,<0.5.0',
 'colorlog>=4.0.2,<5.0.0',
 'filetype>=1.0.5,<2.0.0',
 'har2case>=0.3.1,<0.4.0',
 'jinja2>=2.10.3,<3.0.0',
 'jsonpath>=0.82,<0.83',
 'pyyaml>=5.1.2,<6.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.22.0,<3.0.0']

extras_require = \
{':python_version >= "2.7" and python_version < "2.8"': ['future>=0.18.1,<0.19.0']}

entry_points = \
{'console_scripts': ['ate = httprunner.cli:main',
                     'hrun = httprunner.cli:main',
                     'httprunner = httprunner.cli:main',
                     'locusts = httprunner.plugins.locusts.cli:main']}

setup_kwargs = {
    'name': 'httprunner',
    'version': '2.4.0b0',
    'description': 'One-stop solution for HTTP(S) testing.',
    'long_description': '\n# HttpRunner\n\n[![downloads](https://pepy.tech/badge/httprunner)](https://pepy.tech/project/httprunner)\n[![travis-ci](https://travis-ci.org/httprunner/httprunner.svg?branch=master)](https://travis-ci.org/httprunner/httprunner)\n[![coveralls](https://coveralls.io/repos/github/HttpRunner/HttpRunner/badge.svg?branch=master)](https://coveralls.io/github/HttpRunner/HttpRunner?branch=master)\n[![pypi version](https://img.shields.io/pypi/v/httprunner.svg)](https://pypi.python.org/pypi/httprunner)\n[![pyversions](https://img.shields.io/pypi/pyversions/httprunner.svg)](https://pypi.python.org/pypi/httprunner)\n[![TesterHome](https://img.shields.io/badge/TTF-TesterHome-2955C5.svg)](https://testerhome.com/github_statistics)\n\n*HttpRunner* is a simple & elegant, yet powerful HTTP(S) testing framework. Enjoy! \xe2\x9c\xa8 \xf0\x9f\x9a\x80 \xe2\x9c\xa8\n\n## Design Philosophy\n\n- Embrace open source, stand on giants\' shoulders, like [`Requests`][Requests], [`unittest`][unittest] and [`Locust`][Locust].\n- Convention over configuration.\n- Pursuit of high rewards, write once and achieve a variety of testing needs\n\n## Key Features\n\n- Inherit all powerful features of [`Requests`][Requests], just have fun to handle HTTP(S) in human way.\n- Define testcases in YAML or JSON format in concise and elegant manner.\n- Record and generate testcases with [`HAR`][HAR] support. see [`har2case`][har2case].\n- Supports `variables`/`extract`/`validate` mechanisms to create full test scenarios.\n- Supports perfect hook mechanism.\n- With `debugtalk.py` plugin, very easy to implement complex logic in testcase.\n- Testcases can be run in diverse ways, with single testcase, multiple testcases, or entire project folder.\n- Test report is concise and clear, with detailed log records.\n- With reuse of [`Locust`][Locust], you can run performance test without extra work.\n- CLI command supported, perfect combination with `CI/CD`.\n\n## Documentation\n\nHttpRunner is rich documented.\n\n- [`\xe4\xb8\xad\xe6\x96\x87\xe7\x94\xa8\xe6\x88\xb7\xe4\xbd\xbf\xe7\x94\xa8\xe6\x89\x8b\xe5\x86\x8c`][user-docs-zh]\n- [`\xe5\xbc\x80\xe5\x8f\x91\xe5\x8e\x86\xe7\xa8\x8b\xe8\xae\xb0\xe5\xbd\x95\xe5\x8d\x9a\xe5\xae\xa2`][development-blogs]\n- [CHANGELOG](docs/CHANGELOG.md)\n\n## Sponsors\n\nThank you to all our sponsors! \xe2\x9c\xa8\xf0\x9f\x8d\xb0\xe2\x9c\xa8 ([become a sponsor](docs/sponsors.md))\n\n### \xe9\x87\x91\xe7\x89\x8c\xe8\xb5\x9e\xe5\x8a\xa9\xe5\x95\x86\xef\xbc\x88Gold Sponsor\xef\xbc\x89\n\n[<img src="docs/assets/hogwarts.png" alt="\xe9\x9c\x8d\xe6\xa0\xbc\xe6\xb2\x83\xe5\x85\xb9\xe6\xb5\x8b\xe8\xaf\x95\xe5\xad\xa6\xe9\x99\xa2" width="400">](https://testing-studio.com)\n\n> [\xe9\x9c\x8d\xe6\xa0\xbc\xe6\xb2\x83\xe5\x85\xb9\xe6\xb5\x8b\xe8\xaf\x95\xe5\xad\xa6\xe9\x99\xa2](https://testing-studio.com) \xe6\x98\xaf\xe7\x94\xb1\xe6\xb5\x8b\xe5\x90\xa7\xef\xbc\x88\xe5\x8c\x97\xe4\xba\xac\xef\xbc\x89\xe7\xa7\x91\xe6\x8a\x80\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8\xe4\xb8\x8e\xe7\x9f\xa5\xe5\x90\x8d\xe8\xbd\xaf\xe4\xbb\xb6\xe6\xb5\x8b\xe8\xaf\x95\xe7\xa4\xbe\xe5\x8c\xba [TesterHome](https://testerhome.com/) \xe5\x90\x88\xe4\xbd\x9c\xe7\x9a\x84\xe9\xab\x98\xe7\xab\xaf\xe6\x95\x99\xe8\x82\xb2\xe5\x93\x81\xe7\x89\x8c\xe3\x80\x82\xe7\x94\xb1 BAT \xe4\xb8\x80\xe7\xba\xbf**\xe6\xb5\x8b\xe8\xaf\x95\xe5\xa4\xa7\xe5\x92\x96\xe6\x89\xa7\xe6\x95\x99**\xef\xbc\x8c\xe6\x8f\x90\xe4\xbe\x9b**\xe5\xae\x9e\xe6\x88\x98\xe9\xa9\xb1\xe5\x8a\xa8**\xe7\x9a\x84\xe6\x8e\xa5\xe5\x8f\xa3\xe8\x87\xaa\xe5\x8a\xa8\xe5\x8c\x96\xe6\xb5\x8b\xe8\xaf\x95\xe3\x80\x81\xe7\xa7\xbb\xe5\x8a\xa8\xe8\x87\xaa\xe5\x8a\xa8\xe5\x8c\x96\xe6\xb5\x8b\xe8\xaf\x95\xe3\x80\x81\xe6\x80\xa7\xe8\x83\xbd\xe6\xb5\x8b\xe8\xaf\x95\xe3\x80\x81\xe6\x8c\x81\xe7\xbb\xad\xe9\x9b\x86\xe6\x88\x90\xe4\xb8\x8e DevOps \xe7\xad\x89\xe6\x8a\x80\xe6\x9c\xaf\xe5\x9f\xb9\xe8\xae\xad\xef\xbc\x8c\xe4\xbb\xa5\xe5\x8f\x8a\xe6\xb5\x8b\xe8\xaf\x95\xe5\xbc\x80\xe5\x8f\x91\xe4\xbc\x98\xe7\xa7\x80\xe4\xba\xba\xe6\x89\x8d\xe5\x86\x85\xe6\x8e\xa8\xe6\x9c\x8d\xe5\x8a\xa1\xe3\x80\x82[\xe7\x82\xb9\xe5\x87\xbb\xe5\xad\xa6\xe4\xb9\xa0!](https://ke.qq.com/course/254956?flowToken=1014690)\n\n\xe9\x9c\x8d\xe6\xa0\xbc\xe6\xb2\x83\xe5\x85\xb9\xe6\xb5\x8b\xe8\xaf\x95\xe5\xad\xa6\xe9\x99\xa2\xe6\x98\xaf HttpRunner \xe7\x9a\x84\xe9\xa6\x96\xe5\xae\xb6\xe9\x87\x91\xe7\x89\x8c\xe8\xb5\x9e\xe5\x8a\xa9\xe5\x95\x86\xe3\x80\x82 \n\n## How to Contribute\n\n1. Check for [open issues](https://github.com/httprunner/httprunner/issues) or [open a fresh issue](https://github.com/httprunner/httprunner/issues/new/choose) to start a discussion around a feature idea or a bug.\n2. Fork [the repository](https://github.com/httprunner/httprunner) on GitHub to start making your changes to the **master** branch (or branch off of it). You also need to comply with the [development rules](https://github.com/httprunner/docs/blob/master/en/docs/dev-rules.md).\n3. Write a test which shows that the bug was fixed or that the feature works as expected.\n4. Send a pull request, you will then become a [contributor](https://github.com/httprunner/httprunner/graphs/contributors) after it gets merged and published.\n\n## Subscribe\n\n\xe5\x85\xb3\xe6\xb3\xa8 HttpRunner \xe7\x9a\x84\xe5\xbe\xae\xe4\xbf\xa1\xe5\x85\xac\xe4\xbc\x97\xe5\x8f\xb7\xef\xbc\x8c\xe7\xac\xac\xe4\xb8\x80\xe6\x97\xb6\xe9\x97\xb4\xe8\x8e\xb7\xe5\xbe\x97\xe6\x9c\x80\xe6\x96\xb0\xe8\xb5\x84\xe8\xae\xaf\xe3\x80\x82\n\n![](docs/assets/qrcode.jpg)\n\n[Requests]: http://docs.python-requests.org/en/master/\n[unittest]: https://docs.python.org/3/library/unittest.html\n[Locust]: http://locust.io/\n[har2case]: https://github.com/httprunner/har2case\n[user-docs-zh]: http://docs.httprunner.org/\n[development-blogs]: http://debugtalk.com/tags/httprunner/\n[HAR]: http://httparchive.org/\n[Swagger]: https://swagger.io/\n\n',
    'author': 'debugtalk',
    'author_email': 'debugtalk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/HttpRunner/HttpRunner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
