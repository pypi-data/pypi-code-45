from io import BytesIO
from typing import Any
import pkg_resources
import json
import os
import urllib.parse
from memex_client.client import BRAINIAC_CLIENT_PASSWORD, BRAINIAC_CLIENT_USERNAME
import cloudpickle
import requests


def login(url, username: str, password: str):
    login_url = urllib.parse.urljoin(url, "/api/login")
    params = {'username': username, 'password': password}
    res = requests.post(url=login_url, json=params)
    return res


def get_installed_packages():
    installed_packages = pkg_resources.working_set
    return [i.key for i in installed_packages]


def package(some_class: Any, modelName: str,
            url: str = "http://localhost:4000") -> requests.Response:

    res = login(url, os.environ.get(BRAINIAC_CLIENT_USERNAME),
                os.environ.get(BRAINIAC_CLIENT_PASSWORD))
    cookies = res.headers.get("Set-Cookie")

    file = BytesIO(cloudpickle.dumps(some_class))

    files = {"pkledFile": file}
    installed_packages_list = get_installed_packages()
    data = {"modelName": modelName, "dependencies": json.dumps(installed_packages_list)}
    url = urllib.parse.urljoin(url, "/api/model/upload")
    response = requests.put(url, files=files, data=data, headers={"Cookie": cookies})
    return response


__all__ = ["package"]
