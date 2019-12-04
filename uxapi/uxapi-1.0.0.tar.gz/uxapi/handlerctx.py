from uxapi import seqiter


class HandlerContext(seqiter):
    def handle_message(self, message):
        self.rewind()
        for handler in self:
            message = handler(self, message)
            if message is None:
                return None
        return message

    def fire_message(self, message):
        self.mark()
        for handler in self:
            message = handler(self, message)
            if message is None:
                break
        self.reset()
        return message