import requests
from flask import request, abort

from .user_cas_attributes import save_user_cas_attributes


cas_service_validation_url = \
        'https://cas.apiit.edu.my/cas/p3/serviceValidate' \
        '?format=json' \
        '&service=%(service)s' \
        '&ticket=%(ticket)s'


def require_service_ticket(func):
    """
    Makes decorated endpoint to require CAS service ticket as query string parameter
    """
    def service_ticket_decorator(*args, **kwargs):
        ticket = request.args.get('ticket', None)

        if ticket is None:
            abort(403, "Missing service ticket parameter")

        response = requests.get(
            cas_service_validation_url % {"service": request.base_url, "ticket": ticket}
        ).json()['serviceResponse']

        if 'authenticationSuccess' in response:
            save_user_cas_attributes(response['authenticationSuccess']['attributes'])

            return func(*args, **kwargs)

        abort(401, "Invalid service ticket")

    service_ticket_decorator.__name__ = func.__name__

    return service_ticket_decorator
