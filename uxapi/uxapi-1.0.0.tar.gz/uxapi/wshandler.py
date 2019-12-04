import json
import logging
import asyncio

from aiohttp import WSMsgType

from uxapi import UXTopic
from uxapi import HandlerContext
from uxapi import Session
from uxapi import Message


class WSHandler:
    logger = logging.getLogger(__name__)

    def __init__(self, exchange, wsurl, feed):
        self.exchange = exchange
        self.wsurl = wsurl
        self.feed = feed
        self.session = None
        self.own_session = False
        self.ws = None
        self.pending_topics = None
        self.awaitings = {}
        self.pre_handlers = HandlerContext([])
        self.handlers = HandlerContext(list(self.feed.handlers))
        self.post_handlers = HandlerContext([])

    def get_credentials(self):
        credentials = self.exchange.requiredCredentials
        requires = [key for key in credentials if credentials[key]]
        result = {}
        for key in requires:
            value = getattr(self.exchange, key)
            if value:
                result[key] = value
            else:
                raise RuntimeError(f'requires `{key}`')
        return result


    async def run(self):
        try:
            await self._run()
        finally:
            await self._cleanup()

    async def _run(self):
        self.ws = await self.connect()
        self.on_connected()

        self.create_keepalive_task()
        if self.login_required:
            self.create_login_task()
        else:
            self.create_subscribe_task()

        while True:
            if 'recv' not in self.awaitings.values():
                self.create_task(self.recv(), 'recv')
            done, _ = await asyncio.wait(
                self.awaitings.keys(),
                return_when=asyncio.FIRST_COMPLETED)

            data = None
            for task in done:
                key = self.awaitings[task]
                del self.awaitings[task]
                if key == 'recv':
                    data = task.result()
                else:
                    task.result()

            if data is not None:
                message = Message(self.feed.id, self.decode(data))
                self.handle_message(message)

    def handle_message(self, message):
        message = self.pre_handlers.handle_message(message)
        if message:
            message = self.handlers.handle_message(message)
        if message:
            self.post_handlers.handle_message(message)

    async def connect(self):
        if not self.session:
            self.session = Session()
            self.own_session = True
        ws = await self.session.ws_connect(self.wsurl)
        return ws

    def on_connected(self):
        pass

    def create_keepalive_task(self):
        self.pre_handlers.prepend(self.handle_keepalive_message)
        return self.create_task(self.keepalive(), 'keepalive')
        
    async def keepalive(self):
        raise NotImplementedError
        
    def handle_keepalive_message(self, ctx, message):
        raise NotImplementedError

    @property
    def login_required(self):
        return False

    def create_login_task(self):
        self.pre_handlers.append(self.handle_login_message)
        credentials = self.get_credentials()
        return self.create_task(self.login(credentials), 'login')
        
    async def login(self, credentials):
        command = self.login_command(credentials)
        await self.send(command)

    def login_command(self, credentials):
        raise NotImplementedError

    def handle_login_message(self, ctx, message):
        raise NotImplementedError

    def on_login(self):
        self.pre_handlers.remove()
        self.create_subscribe_task()

    def create_subscribe_task(self):
        self.pre_handlers.append(self.handle_subscribe_message)
        topics = [self.convert_topic(topic) for topic in self.feed.topics]
        self.pending_topics = topics
        return self.create_task(self.subscribe(topics), 'subscribe')
        
    def convert_topic(self, topic: UXTopic):
        return self.exchange.convert_topic(topic)

    async def subscribe(self, topics):
        commands = self.subscribe_commands(topics)
        for command in commands:
            await self.send(command)

    def subscribe_commands(self, topics):
        raise NotImplementedError

    def handle_subscribe_message(self, ctx, message):
        raise NotImplementedError

    def on_subscribe(self, topic):
        self.pending_topics.remove(topic)
        if not self.pending_topics:
            self.pre_handlers.remove()
            self.pending_topics = None

    async def send(self, command):
        if isinstance(command, dict):
            await self.ws.send_json(command) 
        else:
            await self.ws.send_str(command)

    async def recv(self):
        wsmsg = await self.ws.receive()
        if wsmsg.type in (WSMsgType.BINARY, WSMsgType.TEXT):
            return wsmsg.data
        else:
            raise RuntimeError(f'unexpected message: {wsmsg}')
            
    def decode(self, data):
        return data

    async def _cleanup(self):
        if self.awaitings:
            for task in self.awaitings:
                task.cancel()
            try:
                await asyncio.wait(
                    self.awaitings.keys(),
                    return_when=asyncio.ALL_COMPLETED)
            except Exception:
                pass

        if self.ws:
            try:
                await self.ws.close()
            except Exception:
                pass

        if self.session and self.own_session:
            try:
                await self.session.close()
            except Exception:
                pass

    def create_task(self, coro, key=None):
        task = asyncio.create_task(coro)
        self.awaitings[task] = key
        return task