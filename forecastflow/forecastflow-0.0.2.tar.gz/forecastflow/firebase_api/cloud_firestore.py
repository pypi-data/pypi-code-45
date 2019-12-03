import json
from typing import Union

import requests

from forecastflow import config


def get(path: str, id_token: str):
    api_base_url = f"https://firestore.googleapis.com/v1/projects/" \
                   f"{config.gcp['project_name']}/databases/(default)/documents"
    if path.startswith('/'):
        path = path[1:]
    request_url = f"{api_base_url}/{path}"
    res = requests.get(request_url,
                       headers={'Authorization': f"Firebase {id_token}"})
    j = json.loads(res.text)
    # j is like
    # {'name': <path to document>,
    #  'fields': {
    #    <some filed name>: {<type>: <value>},
    #  }
    return {k: parse(j['fields'][k]) for k in j['fields']}


def parse(type_and_value: dict) -> Union[bool, int, float, str, dict, list, None]:
    """
    Parse json from cloud firestore.

    Types are here https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Value

    Args:
        type_and_value:
            {type: value}

    Returns:
        parsed value
    """
    type_ = list(type_and_value.keys())[0]
    value = type_and_value[type_]

    if type_ == 'stringValue':
        return value

    elif type_ == 'nullValue':
        return None

    elif type_ == 'booleanValue':
        return value == 'true'

    elif type_ == 'integerValue':
        return int(value)

    elif type_ == 'doubleValue':
        return float(value)

    elif type_ == 'timestampValue':
        # TODO: Implement TimestampValue parser
        return None

    elif type_ == 'mapValue':
        fields = value['fields']
        res = {k: parse(fields[k]) for k in fields}
        return res

    elif type_ == 'arrayValue':
        if len(value) > 0:
            values = value['values']
            res = [parse(value) for value in values]
            return res
        else:
            return []
    else:
        raise ValueError(f"Unsupported type '{type_}'.")
