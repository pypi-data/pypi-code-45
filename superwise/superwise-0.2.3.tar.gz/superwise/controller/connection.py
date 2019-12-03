"""
Connection module
"""
import logging

import requests

from superwise.config import Config
from superwise.exceptions.superwise_exceptions import SuperwiseConnectionError


class Connection:
    """
    Connection class aims to manage connection with superwise
    """
    def __init__(self, username: str, password: str):
        """
        create connection for user
        :param username:
        :param password:
        """
        self._logger = logging.getLogger('superwise')
        self._username: str = username
        self._password: str = password

    def login(self):
        """
        Login using username and password to work with superwise.
        :return: return requests session object with contains jwt from superwise.
        """
        self._logger.info(f"user {self._username} try to login")

        session = requests.session()
        try:
            uri = f"https://{Config.SW_HOST}" + "/v1/admin/login"
            response = session.get(uri, auth=(self._username, self._password))
            if response.status_code == 401:
                self._logger.debug(f"user {self._username} failed login")
                raise SuperwiseConnectionError("Problem login to superwise with msg: {msg}".format(msg=response.text))
            else:
                if response.status_code == 200:
                    self._logger.info(f"user {self._username} success login")
                    session.headers.update({'Authorization': 'Bearer ' + response.json()['token']})
                    return session
                self._logger.critical(f"user {self._username} failed login")
                raise SuperwiseConnectionError("Internal error in superwise".format(msg=response.text))
        except Exception:
            self._logger.critical(f"user {self._username} failed login")
            raise SuperwiseConnectionError("Problem login to superwise...")
