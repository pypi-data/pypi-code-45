import logging

from superwise.controller.connection import Connection
from superwise.controller.trace import Trace
from superwise.exceptions.superwise_exceptions import SuperwiseDataError
from superwise.validations.superwise_validator import valid_trace_batch_predictions, valid_trace_emit_prediction


class Superwise:

    def __init__(self, sw_username: str, sw_password: str):
        """
        Create connection to working with superwise sdk.
        :param sw_username:
        :param sw_password:
        """
        self._logger = logging.getLogger('superwise')
        self._sw_username = sw_username
        self._sw_password = sw_password
        self._session = Connection(username=sw_username, password=sw_password).login()
        self.trace = Trace(self._session, sw_username=sw_username, sw_password=sw_password)

    def login(self):
        """
        Relogin  to superwise, Update session data member to superwise.
        :return:str Superwise class
        """
        self._session = Connection(username=self._sw_username, password=self._sw_password).login()
        self._logger.info(f"user {self._sw_username} login")
        return self

    @staticmethod
    def validate_emit_prediction_req(data):
        """
        validate data getting from user is in the right format.
        :param data: single record of data from user
        :return: Boolean, Error
        """
        if valid_trace_emit_prediction(data):
            return True
        raise SuperwiseDataError("Data don't in the right format..")

    @staticmethod
    def validate_batch_predictions_req(data):
        """
           validate data getting from user is in the right format.
           :param data: multiple record of data from user
           :return: Boolean, Error
       """
        if valid_trace_batch_predictions(data):
            return True
        raise SuperwiseDataError("Data don't in the right format..")
