import aiohttp
import asyncio
import logging
import sys

name = 'BenBotAsync'
version = '1.0.9'
author = 'xMistt'

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

class fortniteCosmetic:
    def __init__(self, data):
        for key,value in data.items():
            self.__setattr__(key, value)

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
            if result[f'{sorter}'] == filter:
                cosmetic = fortniteCosmetic(result)
                return cosmetic
            else:
                pass

# DEPRECATED FUNCTIONS BELOW.

async def getCosmetic(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getCosmeticId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getCosmeticFromId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Outfit.

async def getSkin(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getSkinId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Harvesting Tool.

async def getPickaxe(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getPickaxeId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Back Bling.

async def getBackpack(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getBackpackId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Glider.

async def getGlider(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getGliderId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Emote.

async def getEmote(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getEmoteId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

# Gets cosmetic with type Pet.

async def getPet(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')

async def getPetId(search):
    print('This function is now deprecated. Join https://discord.gg/VF4txZr or view the source code to see the new functions.')
    print('This message will be removed within a week.')