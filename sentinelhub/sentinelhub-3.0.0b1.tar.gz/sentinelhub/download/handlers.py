"""
Module implementing error handlers which can occur during download procedure
"""
import logging
import time

import requests

from ..decoding import decode_sentinelhub_err_msg
from ..exceptions import DownloadFailedException


LOGGER = logging.getLogger(__name__)


def fail_user_errors(download_func):
    """ Decorator function for handling user errors
    """

    def new_download_func(self, request):
        try:
            return download_func(self, request)
        except requests.HTTPError as exception:
            if exception.response.status_code < requests.status_codes.codes.INTERNAL_SERVER_ERROR and \
                exception.response.status_code != requests.status_codes.codes.TOO_MANY_REQUESTS:

                raise DownloadFailedException(_create_download_failed_message(exception, request.url)) from exception
            raise exception from exception

    return new_download_func


def retry_temporal_errors(download_func):
    """ Decorator function for handling server and connection errors
    """
    backoff_coefficient = 3

    def new_download_func(self, request):
        download_attempts = self.config.max_download_attempts
        sleep_time = self.config.download_sleep_time

        for attempt_num in range(download_attempts):
            try:
                return download_func(self, request)
            except requests.RequestException as exception:

                if not (_is_temporal_problem(exception) or
                        (isinstance(exception, requests.HTTPError) and
                         exception.response.status_code >= requests.status_codes.codes.INTERNAL_SERVER_ERROR)):
                    raise exception from exception

                if attempt_num == download_attempts - 1:
                    raise DownloadFailedException(_create_download_failed_message(exception, request.url)) \
                        from exception

                LOGGER.debug('Download attempt failed: %s\n%d attempts left, will retry in %ds', exception,
                             download_attempts - attempt_num - 1, sleep_time)
                time.sleep(sleep_time)
                sleep_time *= backoff_coefficient

    return new_download_func


def fail_missing_file(download_func):
    """ A decorator for raising an error if a file is missing
    """
    def new_download_func(self, request):
        try:
            return download_func(self, request)
        except requests.HTTPError as exception:
            if exception.response.status_code == requests.status_codes.codes.NOT_FOUND:
                raise DownloadFailedException('File in location %s is missing' % request.url) from exception

            raise exception from exception

    return new_download_func


def _is_temporal_problem(exception):
    """ Checks if the obtained exception is temporal and if download attempt should be repeated

    :param exception: Exception raised during download
    :type exception: Exception
    :return: `True` if exception is temporal and `False` otherwise
    :rtype: bool
    """
    try:
        return isinstance(exception, (requests.ConnectionError, requests.Timeout))
    except AttributeError:  # Earlier requests versions might not have requests.Timeout
        return isinstance(exception, requests.ConnectionError)


def _create_download_failed_message(exception, url):
    """ Creates message describing why download has failed

    :param exception: Exception raised during download
    :type exception: Exception
    :param url: An URL from where download was attempted
    :type url: str
    :return: Error message
    :rtype: str
    """
    message = 'Failed to download from:\n{}\nwith {}:\n{}'.format(url, exception.__class__.__name__, exception)

    if _is_temporal_problem(exception):
        if isinstance(exception, requests.ConnectionError):
            message += '\nPlease check your internet connection and try again.'
        else:
            message += '\nThere might be a problem in connection or the server failed to process ' \
                       'your request. Please try again.'
    elif isinstance(exception, requests.HTTPError):
        server_message = decode_sentinelhub_err_msg(exception.response)
        message += '\nServer response: "{}"'.format(server_message)

    return message
