import logging
import os
import sys
import threading
import time
import traceback
from collections import namedtuple
from uuid import uuid4

import sentry_sdk
import zmq

from om.message import Message

CallbackEntry = namedtuple("CallbackEntry", ["timestamp", "result"])


class RPCClient(object):
    def __init__(self, config, context=None):
        context = context or zmq.Context()
        self.name = config.NAME
        # self.sub = context.socket(zmq.SUB)
        # self.sub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_PUB_PORT))
        # self.sub.subscribe(b"rpc-rep")
        self.pub = context.socket(zmq.PUB)
        self.pub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_SUB_PORT))

        # self.callbacks_last_cleanup = time.time()
        # self.callbacks_lock = threading.RLock()
        # self.callbacks = dict()

    def _call(self, channel, type, request):
        rpc_id = str(uuid4())
        message = Message(
            name=self.name,
            type=type,
            rpc_id=rpc_id,
            request=request,
        )
        message.to_socket(self.pub, "rpc-req-{}".format(channel).encode("ascii"))
        # with self.callbacks_lock:
        #    result = CallbackEntry(time.time(), None)
        #    self.callbacks[rpc_id] = result
        return None

    def call_async(self, channel, type, request):
        return self._call(channel, type, request)


class RPCServer(object):
    @staticmethod
    def gateway_filter(gate=None, direction=None):
        def _filter(request, message, handler):
            gateway = request.get("gateway")
            if not gateway:
                return False
            return (not gate or gate == gateway.get("gate")) and \
                   (not direction or direction == gateway.get("direction"))

        return _filter

    def __init__(self, config, context=None):
        context = context or zmq.Context()
        self.name = config.NAME
        self.sub = context.socket(zmq.SUB)
        self.sub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_PUB_PORT))
        self.pub = context.socket(zmq.PUB)
        self.pub.connect("tcp://{}:{}".format(config.BROKER_HOST, config.BROKER_SUB_PORT))
        self.handlers = {}
        self.filters = []
        self.log = logging.getLogger("rpc")

    def add_filter(self, handler):
        self.filters.append(handler)

    def _thread_wrapper(self):
        try:
            self.run()
        except Exception as e:
            sentry_sdk.capture_exception()
            traceback.print_exc(file=sys.stderr)
            sys.stderr.flush()
            time.sleep(1)
            os._exit(1)

    def register_handler(self, channel, type, handler):
        """
        :param type: the request type, specify * to catch all types, in this case no other
                     handler will be run for the channel except for the wildcard handler
        :param handler: request handler of the form (request:dict, meta:dict) -> any
                        if the handler returns a dict which contains the key "status",
                        then the value of "status" will be used as the rpc response status.
                        There are no other reserved keys except "status".
        """
        channel = self._ascii(channel)
        type = self._ascii(type)
        self.log.debug("register handler {}:{} -> {}".format(channel, type, handler))
        self.sub.subscribe(b"rpc-req-" + channel)
        self.handlers[(channel, type)] = handler

    def _channel_from_topic(self, topic):
        return topic.split(b"-", 2)[-1]

    def _ascii(self, x):
        if hasattr(x, "encode"):
            return x.encode("ascii")
        else:
            return x

    def _handlers_handler(self):
        pass

    def should_process_message(self, request, message, handler):
        if self.filters:
            for filter in self.filters:
                if filter(request=request, message=message, handler=handler):
                    return True
            return False
        return True

    def find_handler(self, channel, type):
        channel = self._ascii(channel)
        type = self._ascii(type)
        if type == "_handlers":
            return self._handlers_handler
        else:
            return self.handlers.get((channel, b"*")) or self.handlers.get((channel, type))

    def run_as_thread(self):
        thread = threading.Thread(target=self._thread_wrapper)
        thread.setDaemon(True)
        thread.start()
        return thread

    def run(self):
        while True:
            topic, message = Message.from_socket(self.sub)
            channel = self._channel_from_topic(topic)
            request = message["request"]
            type = message["type"]
            del message["request"]
            message["channel"] = channel

            self.log.debug("processing request for {}:{} -> {}".format(topic, channel, request))
            handler = self.find_handler(channel, type)
            if handler:
                try:
                    if not self.should_process_message(request, message, handler):
                        continue
                except Exception as e:
                    sentry_sdk.capture_exception()
                    self.log.info("exception in filter {}:{}".format(channel, type))
                    continue

                try:
                    response = handler(request, message)
                except Exception as e:
                    sentry_sdk.capture_exception()
                    self.log.info("exception in handler {}:{}".format(channel, type))
                    response = {"status": "handler_error", "exception": str(e)}
            else:
                self.log.warning("no handler found for {}:{}".format(channel, type))
                response = {"status": "unhandled"}

            self.log.debug("response: {}".format(response))
            result = Message(type=type, name=self.name)
            result["rpc_id"] = message["rpc_id"]
            result["response"] = response
            result.to_socket(self.pub, "rpc-rep-{}".format(channel).encode("ascii"))
