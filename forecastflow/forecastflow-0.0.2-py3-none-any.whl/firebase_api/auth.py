import json
import logging

import requests

from forecastflow import config

logger = logging.Logger(__name__)


def sign_in_with_password(email: str, password: str) -> dict:
    """
    Sign in with e-mail and password by using firebase REST API.
    Document is here https://firebase.google.com/docs/reference/rest/auth/#section-sign-in-email-password .

    Args:
        email:
            User's e-mail to sign in.

        password:
            Password for sign in.

    Returns:
        Dictionary object. keys = ['kind',
            'localId', 'email', 'displayName', 'idToken', 'registered', 'refreshToken', 'expiresIn']
    """
    api_key = config.firebase['apiKey']
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
    data = {
        'email': email,
        'password': password,
        'returnSecureToken': True
    }
    res = json.loads(
        requests.post(url, json.dumps(data)).text
    )
    return res
