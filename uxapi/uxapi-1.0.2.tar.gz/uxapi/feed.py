from uxapi import HandlerContext
from uxapi.helpers import all_equal


class Feed:
    def __init__(self, id):
        self.id = id
        self.topics = []
        self.handlers = []

    def __repr__(self):
        return (f'<Feed id={self.id} topics={self.topics}>')

    def add_topic(self, topic, *handlers):
        assert (not self.topics
                    or self.topics[0].exchange_id == topic.exchange_id)
        self.topics.append(topic)
        for handler in handlers:
            self.handlers.append(handler)

    def add_handler(self, handler):
        self.handlers.append(handler)