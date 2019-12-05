from typing import IO, Union
from urllib.parse import quote

import requests

from forecastflow import config

_api_base_url = "https://firebasestorage.googleapis.com/v0/b/"


def download(path: str, file: IO, id_token: str):
    url = get_url(path)
    res = requests.get(url, stream=True,
                       headers={'authorization': f"Firebase {id_token}"})
    file.write(res.content)


def get_url(path):
    if path.startswith('/'):
        path = path[1:]
    api_url = _api_base_url + config.firebase['storageBucket']
    return "{0}/o/{1}?alt=media".format(api_url, quote(path, safe=''))


def upload(file: Union[IO, str], path: str, id_token):
    if path.startswith('/'):
        path = path[1:]
    if isinstance(file, str):
        file_object = open(file, 'rb')
    else:
        file_object = file
    request_ref = _api_base_url + config.firebase['storageBucket'] + "/o?name={0}".format(path)
    headers = {"Authorization": "Firebase " + id_token}
    request_object = requests.post(request_ref, headers=headers, data=file_object)
    return request_object.json()
