name = "woyera"

import requests
import json

class WoyeraAPI:

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api-woyera.com/clean/"

    def clean(self, clean_type, data):
        full_url = self.url + clean_type + "/"
        request_body = {"apiKey": self.api_key, "data": data}

        r = requests.post(full_url, json=json.loads(json.dumps(request_body)))

        status_code = r.status_code

        try:
            json_response = r.json()
        except:
            json_response = {}

        if status_code == 200:
            return {"status_code": status_code, 'cleanData': json_response['cleanData']}
        else:
            if 'error' in json_response:
                return {"status_code": status_code, 'error': json_response['error']}
            else:
                return {"status_code": status_code, 'error': ''}

