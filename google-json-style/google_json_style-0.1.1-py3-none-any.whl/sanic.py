from sanic.response import json

from ._google import get_google_body


def json_resp(data = '', status: int = 200, headers=None, *args, **kwargs):
    return json(
        body=get_google_body(data, status=status, *args, **kwargs),
        status=status,
        headers=headers)
