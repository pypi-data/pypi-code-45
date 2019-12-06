import json
import os


class Credentials:
    def __init__(self, username=None, password=None, token=None, url=None):
        self.username = username
        self.password = password
        self.token = token
        self.url = url

    def __repr__(self):
        return "{}".format(self.username, self.password, self.token, self.url)

    def json(self):
        return {
            'username': self.username,
            'password': self.password,
            'token': self.token,
            'url': self.url
        }

    @classmethod
    def from_json(cls, json_data, filepath=None):
        if filepath:
            header_data = os.path.join(filepath, json_data)
            with open(header_data, 'r') as f:
                headers = json.load(f)
                for header in headers:
                    url = headers['url']
                    username = headers['username']
                    password = headers['password']
                    token = headers['token']
                return Credentials(**headers)
        else:
            with open(json_data, 'r') as f:
                headers = json.load(f)
                for header in headers:
                    url = headers['url']
                    username = headers['username']
                    password = headers['password']
                    token = headers['token']
                return Credentials(**headers)
