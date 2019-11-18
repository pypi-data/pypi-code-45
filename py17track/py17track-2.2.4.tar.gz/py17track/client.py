"""Define a 17track.net client."""
from typing import Optional

from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientError

from .errors import RequestError
from .profile import Profile

# from .track import Track


class Client:  # pylint: disable=too-few-public-methods
    """Define the client."""

    def __init__(self, websession: ClientSession) -> None:
        """Initialize."""
        self._websession: ClientSession = websession

        self.profile: Profile = Profile(self._request)

        # This is disabled until a workaround can be found:
        # self.track = Track(self._request)

    async def _request(
        self,
        method: str,
        url: str,
        *,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
    ) -> dict:
        """Make a request against the RainMachine device."""
        if not headers:
            headers = {}

        try:
            async with self._websession.request(
                method, url, headers=headers, params=params, json=json
            ) as resp:
                resp.raise_for_status()
                data: dict = await resp.json(content_type=None)
                return data
        except ClientError as err:
            raise RequestError(f"Error requesting data from {url}: {err}")
