"""
Trace module
"""
import json
import logging
from typing import Callable
from requests import Session

from superwise.config import Config
from superwise.exceptions.superwise_exceptions import SuperwiseDataError
from superwise.superwise import Connection
from superwise.validations.superwise_validator import *


class Trace:

    uri = f"https://{Config.SW_HOST}" + "/v1/trace/task/{task_id}/"

    def __init__(self, session: Session, sw_username: str, sw_password: str):
        self._logger = logging.getLogger('superwise')
        self._session = session
        self._sw_username = sw_username
        self._sw_password = sw_password

    def emit_prediction(self, data, task_id: int, version_id: int):
        """
        send trace prediction single record(single mode)
        :param version_id:
        :param _retry: private parameter, which retries
        :param data: data of user
        :param task_id:
        :return: status_code, exception
        """
        url = str(Trace.uri.format(task_id=task_id) + 'prediction/emit')
        body = dict(record=data, version_id=version_id)
        validator = valid_trace_emit_prediction
        return self._prediction_helper_func(url=url, body=body, validator=validator)

    def batch_predictions(self, data, task_id: int, version_id: int):
        """
        send trace prediction records(batch mode)
        :param version_id:
        :param _retry:
        :param data: data of user
        :param task_id:
        :return: status_code, exception
        """
        url = str(Trace.uri.format(task_id=task_id) + 'prediction/batch')
        body = dict(records=data, version_id=version_id)
        validator = valid_trace_batch_predictions
        return self._prediction_helper_func(url=url, body=body, validator=validator)

    def file_predictions(self, file_url: str, version_id: int, task_id: int):
        """
        send trace batch request with path to file in s3.
        :param version_id:
        :param file_url:
        :param task_id:
        :param _retry:
        :return: status code from the request
        """
        url = str(Trace.uri.format(task_id=task_id) + 'prediction/file')
        body = dict(file_url=file_url, version_id=version_id)
        validator = valid_trace_file_predictions
        return self._prediction_helper_func(url=url, body=body, validator=validator)

    def emit_label(self, data, task_id: int):
        """
        send trace label prediction single record(single mode)
        :param version_id:
        :param _retry: private parameter, which retries
        :param data: data of user
        :param task_id:
        :return: status_code, exception
        """
        url = str(Trace.uri.format(task_id=task_id) + 'label/emit')
        validator = valid_trace_emit_label
        return self._prediction_helper_func(url=url, body=data, validator=validator)

    def batch_labels(self, data, task_id: int):
        """
        send trace label prediction records(batch mode)
        :param version_id:
        :param _retry:
        :param data: data of user
        :param task_id:
        :return: status_code, exception
        """
        url = str(Trace.uri.format(task_id=task_id) + 'label/batch')
        body = dict(records=data)
        validator = valid_trace_batch_labels
        return self._prediction_helper_func(url=url, body=body, validator=validator)

    def file_labels(self, file_url: str, task_id: int):
        """
        send trace batch request with path to file in s3.
        :param version_id:
        :param file_url:
        :param task_id:
        :param _retry:
        :return: status code from the request
        """
        url = str(Trace.uri.format(task_id=task_id) + 'label/file')
        body = dict(file_url=file_url)
        validator = valid_trace_file_labels
        return self._prediction_helper_func(url=url, body=body, validator=validator)

    def _prediction_helper_func(self, url: str, body: dict, validator: Callable, _retry: int = 0):
        """
        Centralize function to send post request to the server
        :param url: end point URI
        :param body: request body
        :param validator: validate the body structure
        :param _retry: amount of times try to send post
        :return: Error or Response Code of the request
        """
        header = {'Content-Type': 'application/json'}
        self._logger.info(f"user {self._sw_username} send {url} request")
        if validator(data=body):
            res = self._session.post(url=url, data=json.dumps(body), headers=header)
            if res.status_code == 403 and _retry < 2:
                self._logger.warning(
                    f"user {self._sw_username} {url} request failed try to recreate session,try: {_retry}")
                self._session = Connection(username=self._sw_username, password=self._sw_password).login()
                res = self._prediction_helper_func(url, body, validator, _retry=++_retry)
                return res.status_code
            self._logger.info(
                f"user {self._sw_username} {url} request return with status code {res.status_code}")
            return res.status_code
        self._logger.info(f"user {self._sw_username} {url} request was with wrong data format...")
        raise SuperwiseDataError("Data don't in the right format..")
