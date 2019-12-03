import logging
import requests
from base64 import b64decode

_LOGGER = logging.getLogger(__name__)

class PowerView:
    """Class for interacting with the Powerview API."""

    REQUEST_TIMEOUT = 3.0

    def __init__(self, host):
        """Initialize the PowerView Hub."""
        if host is not None:
            self.host = 'http://' + host

    def make_request(self, method, request, data=None):

        url = self.host + request
        _LOGGER.debug("URL: %s", url)

        try:
            if method is "get":
                r = requests.get(url)

                return r.json()

            elif method is "put":
                r = requests.put(url, json = data)

                return True

            else:
                return False

        except:
            return False

    def get_shades(self):
        """List all shade Ids."""
        request = self.make_request("get","/api/shades")

        if request != False:

            shades = []

            for x in request['shadeIds']:

                shades.append(x)

            return shades

        else:
            return False

    def get_shade(self, shade):
        """List all shades."""
        request = self.make_request("get","/api/shade/" + str(shade))

        if request != False:

            shade = Shade(request['id'], b64decode(request['name']).decode('UTF-8'), round((request['positions']['position1'] / 65535) * 100), round(request['batteryStrength'] / 2))

            return shade

        else:
            return False


    def get_status(self, shade):
        """Update status of shade."""
        request = round((self.make_request("get","/api/shade/" + str(shade))['positions']['position1'] / 65535) * 100)

        return request

    def close_shade(self, shade):
        """Close a shade."""
        self.make_request("put","/api/shade/" + str(shade), {"shade": {"motion": "down"}})

        return 0

    def open_shade(self, shade):
        """Open a shade."""
        self.make_request("put","/api/shade/" + str(shade), {"shade": {"motion": "up"}})

        return 100

    def stop_shade(self, shade):
        """Stop a shade."""
        request = self.make_request("put","/api/shade/" + str(shade), {"shade": {"motion": "stop"}})

        return self.get_status(shade)

    def set_shade_position(self, shade, position: int):
        """Set a shade to a specific position."""
        if 0 <= position <= 100: 
            position = round(position * 65535 / 100)
            self.make_request("put","/api/shade/" + str(shade), { "shade": { "positions": { "posKind1": 1, "position1": position } } })

            return position
            
        else:

            return False

class Shade:
    """Class to represent a PowerView shade"""
    def __init__(self,
                 id: int,
                 name: str,
                 position: int,
                 battery: int):
        self.id = id
        self.name = name
        self.position = position
        self.battery_level = battery
