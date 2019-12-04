import threading
import uuid
from typing import Optional

from django.http import HttpRequest, HttpResponse

# global variable for storing a request
request_local = threading.local()


def get_request() -> Optional[HttpRequest]:
    """
    Function that returning a request
    """

    return getattr(request_local, 'request', None)


class VersionControlMiddleware:
    """
    Middleware to receive request from current thread and install storage for modified objects
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        request_local.request = self._process_request(request)
        return self.get_response(request)

    def process_exception(self, request, exception: Exception) -> None:
        request_local.request = None

    def process_template_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        request_local.request = None
        return response

    def _process_request(self, request: HttpRequest) -> HttpRequest:
        """
        Method for assigning a unique identifier for request
        """

        if not hasattr(request, 'key'):
            setattr(request, 'key', uuid.uuid4().hex)
        return request
