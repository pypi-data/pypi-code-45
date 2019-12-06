# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['konlpy_grpc',
 'konlpy_grpc._generated',
 'konlpy_grpc.clients',
 'konlpy_grpc.monkeypatch']

package_data = \
{'': ['*'], 'konlpy_grpc': ['servers/*']}

install_requires = \
['grpcio', 'grpcio-reflection', 'grpcio-tools']

extras_require = \
{'server': ['konlpy>=0.5.2,<0.6.0']}

setup_kwargs = {
    'name': 'konlpy-grpc',
    'version': '0.1.0',
    'description': 'Redesigned KoNLPy (Wrapper) for Usability and Portability with gRPC.',
    'long_description': '# KoNLPy-gRPC\nRedesigned KoNLPy (Wrapper) for Usability and Portability with gRPC.\n\n## Requirements:\n```bash\npip install poetry\npip install -r $(python manage.py requirements.txt) -r $(python manage.py requirements-dev.txt)\n```\n\n## gRPC Compile needed!\n```bash\npython -m grpc_tools.protoc -I protos/ --python_out=konlpy_grpc/_generated/ --grpc_python_out=konlpy_grpc/_generated/ protos/*.proto\n```\n\n## Server\n```bash\npython -m pip install konlpy\n```\n\n```bash\npython -m konlpy_grpc server\npython -m konlpy_grpc hannanum_server\npython -m konlpy_grpc kkma_server\npython -m konlpy_grpc komoran_server\npython -m konlpy_grpc mecab_server\npython -m konlpy_grpc okt_server\n```\n\n## Tests\n```bash\npython -m pytest\npython -m pytest --grpc-fake-server\npython -m pytest --grpc-real-server=[::]:50051\npython -m pytest --konlpy-repo=../konlpy\n```\n\n## Release\n```bash\nrm -rf dist/\npoetry publish --build -r test\npoetry run twine upload --repository-url https://test.pypi.org/legacy/ dist/*\n```\n\n## TODO\n- [x] [P0] client.py will be a konlpy-alike module.\n  - [x] [P0] KoNLPy monkey-patcher\n- [x] [P1] Packaging with Poetry `pyproject.toml`.\n  - [x] PyPI Register\n  - [ ] Find lowerbound-version of requirements. <!-- poetry debug:resolve -->\n- [P1] gRPC Proto Compile\n- [P1] In-house tool: `manage.py`\n<!--\n  - doit\n  - bazel\n  - bump2version\n  - poetry-dynamic-versioning\n  - pytest.ini to pyproject.toml\n-->\n- [P1] KoNLPy Version Matching (set minimum) and Follow-up\n- [P1] gRPC retry/timeout/error_handling logic <!-- google.api_core.* or grpc-retry-py -->\n- [x] [P1] gRPC reflection\n- [P1] gRPC heartbeat\n- [x] [P1] gRPC Gateway (gRPC to JSON)\n- [x] [P2] Dockerize / Register\n  - k8s and istio?\n- [P2] CI\n- [P3] Button for deploying this to AWS/GCS/Azure now! (and connect by README.)\n- [P3] CustomDic?\n- [P3] Stream I/O\n- [P3] Redesign tests/ with grpc-testing\n- [P4] Java Edition for KoNLPy-gRPC-Server\n  - gRPC protos deploy/versioning\n\n## Additional Links\n- [KoNLPy/KoNLPy](https://github.com/konlpy/konlpy)\n- [Pruned KoNLPy v0.5.2-rc.1](https://github.com/minhoryang/konlpy)\n  - Currently, servers rely on KoNLPy v0.5.2 version.\n\n## License\nGNU GPLv3\n',
    'author': 'Minho Ryang',
    'author_email': 'minhoryang@gmail.com',
    'url': 'https://github.com/minhoryang/KoNLPy-gRPC',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
