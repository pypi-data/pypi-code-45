import aioredis
import asyncio


class Connection():

    @classmethod
    async def create(cls, redis_server='redis://localhost'):
        self = cls()
        self.redis_server = redis_server
        self.conn = await aioredis.create_redis_pool(self.redis_server)
        return self


class Subscriber(Connection):

    async def subscribe(self, channel_name, callback):
        channel, = await self.conn.subscribe(channel_name)

        async def reader(channel):
            async for message in channel.iter():
                callback(message)
        asyncio.get_running_loop().create_task(reader(channel))

    async def unsubscribe(self):
        self.conn.close()
        await self.conn.wait_closed()


class Publisher(Connection):

    def broadcast(self, channel, message):
        self.conn.publish(channel, message)
