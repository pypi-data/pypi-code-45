# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['airflow_indexima',
 'airflow_indexima.hooks',
 'airflow_indexima.operators',
 'airflow_indexima.uri']

package_data = \
{'': ['*']}

install_requires = \
['PyHive==0.6.1',
 'apache-airflow==1.10.2',
 'gitpython>=2.1.0,<2.2.0',
 'thrift-sasl==0.3.0',
 'thrift>0.10.0']

setup_kwargs = {
    'name': 'airflow-indexima',
    'version': '2.0.6',
    'description': 'Indexima Airflow integration',
    'long_description': "# airflow-indexima\n\n\n[![Unix Build Status](https://img.shields.io/travis/geronimo-iia/airflow-indexima/master.svg?label=unix)](https://travis-ci.org/geronimo-iia/airflow-indexima)\n[![PyPI Version](https://img.shields.io/pypi/v/airflow-indexima.svg)](https://pypi.org/project/airflow-indexima)\n[![PyPI License](https://img.shields.io/pypi/l/airflow-indexima.svg)](https://pypi.org/project/airflow-indexima)\n\nVersions following [Semantic Versioning](https://semver.org/)\n\n## Overview\n\n[Indexima](https://indexima.com/) [Airflow](https://airflow.apache.org/) integration based on pyhive.\n\nThis project is used in our prod environment with success.\nAs it a young project, take care of change, any help is welcome :)\n\n\n## Setup\n\n### Requirements\n\n* Python 3.6+\n\n### Installation\n\nInstall this library directly into an activated virtual environment:\n\n```text\n$ pip install airflow-indexima\n```\n\nor add it to your [Poetry](https://poetry.eustace.io/) project:\n\n```text\n$ poetry add airflow-indexima\n```\n\n## Usage\n\nAfter installation, the package can imported:\n\n```text\n$ python\n>>> import airflow_indexima\n>>> airflow_indexima.__version__\n```\n\nSee [Api documentation](https://geronimo-iia.github.io/airflow-indexima/api/)\n\n\n### a simple query\n\n```python\nfrom airflow_indexima.operators import IndeximaQueryRunnerOperator\n\n...\n\nwith dag:\n    ...\n    op = IndeximaQueryRunnerOperator(\n        task_id = 'my-task-id',\n        sql_query= 'DELETE FROM Client WHERE GRPD = 1',\n        indexima_conn_id='my-indexima-connection'\n    )\n    ...\n```\n\n\n### a load into indexima\n\n```python\nfrom airflow_indexima.operators.indexima import IndeximaLoadDataOperator\n\n...\n\nwith dag:\n    ...\n    op = IndeximaLoadDataOperator(\n        task_id = 'my-task-id',\n        indexima_conn_id='my-indexima-connection',\n        target_table='Client',\n        source_select_query='select * from dsi.client',\n        truncate=True,\n        load_path_uri='jdbc:redshift://my-private-instance.com:5439/db_client?ssl=true&user=airflow-user&password=XXXXXXXX'\n    )\n    ...\n\n```\n\n### customize credential access\n\nIf you use another backend to store your password (like AWS SSM), you could define a decorator\nand use it as a function in your dag.\n\n```python\nfrom airflow.models import Connection\nfrom airflow import DAG\n\nfrom airdlow_indexima.uri import define_load_path_factory, get_redshift_load_path_uri\n\n\ndef my_decorator(conn:Connection) -> Connection:\n    conn.password = get_ssm_parameter(param_name=f'{conn.conn_id}.{con.login}')\n    return conn\n\n\ndag = DAG(\n    dag_id='my_dag',\n    user_defined_macros={\n        # we define a macro get_load_path_uri\n        'get_load_path_uri': define_load_path_factory(\n            conn_id='my-redshift-connection',\n            decorator=my_decorator,\n            factory=get_redshift_load_path_uri)\n        },\n    ...\n)\n\nwith dag:\n    ...\n    op = IndeximaLoadDataOperator(\n        task_id = 'my-task-id',\n        indexima_conn_id='my-indexima-connection',\n        target_table='Client',\n        source_select_query='select * from dsi.client',\n        truncate=True,\n        load_path_uri='{{ get_load_path_uri() }}'\n    )\n    ...\n\n\n```\n\na Connection decorator must follow this type: ```ConnectionDecorator = Callable[[Connection], Connection]```\n\n```define_load_path_factory``` is a function which take:\n\n- a connnection identifier\n- a decorator ```ConnectionDecorator```\n- an uri factory ```UriGeneratorFactory = Callable[[str, Optional[ConnectionDecorator]], str]```\n\nand return a function with no argument which can be called as a macro in dag's operator.\n\n\n## License\n\n[The MIT License (MIT)](https://geronimo-iia.github.io/airflow-indexima/license)\n\n\n## Contributing\n\nSee [Contributing](https://geronimo-iia.github.io/airflow-indexima/contributing)\n\n",
    'author': 'Jerome Guibert',
    'author_email': 'jguibert@gmail.com',
    'url': 'https://pypi.org/project/airflow_indexima',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
