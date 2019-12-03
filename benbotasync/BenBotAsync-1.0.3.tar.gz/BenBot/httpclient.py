"""
“Commons Clause” License Condition v1.0
Copyright Oli 2019

The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.

Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.

For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.

Software: fortnitepy-bot

License: Apache 2.0
"""

import logging
import sys
import aiohttp
import asyncio

from .fortnitecosmetic import fortniteCosmetic

logging.getLogger('asyncio').setLevel(logging.CRITICAL)

class HTTPClient:
    def __init__(self, connector=None):
        self.connector = connector
        self.headers = {}

        self.create_connection()

    @property
    def session(self):
            return self.__session

    def create_connection(self):
        self.__session = aiohttp.ClientSession(
            connector=self.connector,
            loop=self.get_event_loop(),
        )

    async def close(self):
        if self.__session and not self.__session.closed:
            await self.__session.close()

    async def request(self, url, method, *args):
        async with self.__session.request(method=method, url=url) as r:
            response = await r.json()
            return response

    def get_event_loop(self):
        if sys.platform == 'win32':
            policy = asyncio.get_event_loop_policy()
            loop = policy._local._loop

            if loop is None:
                selector = selectors.SelectSelector()
                loop = asyncio.SelectorEventLoop(selector)
                asyncio.set_event_loop(loop)
            
            elif isinstance(loop, asyncio.ProactorEventLoop):
                raise RuntimeError('asyncio.ProactorEventLoop is not supported')
        
        else:
            loop = asyncio.get_event_loop()

        return loop