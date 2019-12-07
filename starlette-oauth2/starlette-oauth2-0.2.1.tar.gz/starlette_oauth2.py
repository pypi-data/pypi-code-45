import typing
import logging

from starlette.requests import Request
from starlette.responses import RedirectResponse, JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send
from authlib.integrations._client import UserInfoMixin, RemoteApp as _RemoteApp, errors
from authlib.integrations.requests_client import OAuth2Session


logger = logging.getLogger(__name__)


class RemoteApp(_RemoteApp, UserInfoMixin):
    """A RemoteApp for Starlette framework."""
    def __init__(self, **kwargs) -> None:
        super().__init__(oauth2_client_cls=OAuth2Session, **kwargs)

    def _generate_access_token_params(self, request):
        if self.request_token_url:
            return request.scope
        return {
            'code': request.query_params.get('code'),
            'state': request.query_params.get('state'),
        }

    def authorize_redirect(self, request, redirect_uri=None, **kwargs):
        rv = self.create_authorization_url(redirect_uri, **kwargs)
        self.save_authorize_data(request, redirect_uri=redirect_uri, **rv)
        return RedirectResponse(rv['url'])

    def authorize_access_token(self, request, **kwargs):
        params = self.retrieve_access_token_params(request)
        params.update(kwargs)
        return self.fetch_access_token(**params)

    def parse_id_token(self, request, token, claims_options=None):
        """Return an instance of UserInfo from token's ``id_token``."""
        if 'id_token' not in token:
            return None

        return self._parse_id_token(request, token, claims_options)


class AuthenticateMiddleware:
    REDIRECT_PATH = '/authorized'
    PROVIDERS = {
        'microsoft': {
            'name': 'microsoft',
            'server_metadata_url': 'https://login.microsoftonline.com/{}/v2.0/.well-known/openid-configuration',
        },
        'google': {
            'name': 'google',
            'server_metadata_url': 'https://accounts.google.com/.well-known/openid-configuration',
        },
    }
    PROVIDER = PROVIDERS['microsoft']

    # set of public paths (paths that do not need authentication)
    PUBLIC_PATHS = set()

    def __init__(self, app: ASGIApp, tenant_id: str, client_id: str, client_secret: str, db=None, force_https_redirect=True) -> None:
        self.app = app
        self.db = db
        self._force_https_redirect = force_https_redirect

        self._client = RemoteApp(
            name=self.PROVIDER['name'],
            client_id=str(client_id),
            client_secret=str(client_secret),
            server_metadata_url=self.PROVIDER['server_metadata_url'].format(tenant_id),
            client_kwargs={'scope': 'openid email profile'},
        )

    def _redirect_uri(self, request: Request):
        """
        The URI of the redirect path. This should be registered on whatever provider is declared.
        """
        port = request.url.port
        if port is None:
            port = ''
        else:
            port = ':' + str(port)
        scheme = request.url.scheme
        if scheme == 'http' and self._force_https_redirect:
            scheme = 'https'
        return f"{scheme}://{request.url.hostname}{port}{self.REDIRECT_PATH}"

    async def _authenticate(self, scope: Scope, receive: Receive, send: Send):
        request = Request(scope)

        logger.info(f'Authenticating a user arriving at "{request.url.path}"')

        # /authorized is our redirect_uri and thus the only one that is public
        if request.url.path != self.REDIRECT_PATH:
            # any un-authenticated request is redirected to the tenant
            redirect_uri = self._redirect_uri(request)
            response = self._client.authorize_redirect(request, redirect_uri)
            await response(scope, receive, send)
        else:
            logger.info(f'Fetching id token...')
            # try to construct a user from the access token
            try:
                token = self._client.authorize_access_token(request)
                user = self._client.parse_id_token(request, token)
                assert user is not None
            except Exception as e:
                # impossible to build a user => invalidate the whole thing and redirect to home (which triggers a new auth)
                logger.error('User authentication failed', exc_info=True)
                response = RedirectResponse(url='/')
                await response(scope, receive, send)
                return

            # put the user and token in the session.
            request.session['user'] = dict(user)

            logger.info(f'Storing id token of user "{user["email"]}"...')
            if self.db is None:
                request.session['token'] = dict(token)
            else:
                self.db.put(user['email'], dict(token))

            # finally, redirect to home
            response = RedirectResponse(url='/')
            await response(scope, receive, send)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope)

        if request.url.path in self.PUBLIC_PATHS:
            return await self.app(scope, receive, send)

        user = request.session.get('user')

        # no user => start authentication
        if user is None:
            return await self._authenticate(scope, receive, send)

        # fetch the token from the database associated with the user
        if self.db is None:
            token = request.session.get('token')
        else:
            token = self.db.get(user['email'])

        try:
            # check that the token is still valid (e.g. it has not expired)
            self._client.parse_id_token(request, token)
        except (errors.InvalidTokenError, errors.TokenExpiredError):
            # invalidate session and redirect.
            del request.session['user']
            if self.db is None:
                del request.session['token']
            else:
                self.db.delete(user['email'])

            redirect_uri = self._redirect_uri(request)
            response = self._client.authorize_redirect(request, redirect_uri)
            return await response(scope, receive, send)

        logger.info(f'User "{user["email"]}" is authenticated.')

        await self.app(scope, receive, send)
