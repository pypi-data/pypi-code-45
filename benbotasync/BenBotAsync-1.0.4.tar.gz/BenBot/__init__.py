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

logging.getLogger('asyncio').setLevel(logging.CRITICAL)

from .httpclient import HTTPClient
from .fortnitecosmetic import fortniteCosmetic

http = HTTPClient()

async def get_cosmetic(query, parameter='displayName', sorter=None, filter=None):
    request = await http.request(method='GET', url=f'http://benbotfn.tk:8080/api/cosmetics/search/multiple?{parameter}={query}')

    if sorter is None:
        try:
            cosmetic = fortniteCosmetic(request[0])
            return cosmetic
        except IndexError:
            return None

    else:
        for result in request:
            if result[sorter] == filter:
                cosmetic = fortniteCosmetic(result)
                return cosmetic
            else:
                pass