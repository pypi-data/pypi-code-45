import threading


class Proxy:
    def __init__(self, method, *args, **kwargs):
        assert callable(method), 'method must be a function'
        self.original_method = method
        self.init = kwargs.get("init")
        self.callback = kwargs.get("callback")

    def __call__(self, *args, **kwargs):
        return self.__new_method(*args, **kwargs)

    def __new_method(self, *args, **kwargs):
        if self.init:
            self.init()

        self.original_method(*args, **kwargs)

        if self.callback:
            self.callback()

    def delay(self, *args, **kwargs):
        t = threading.Thread(target=self.__new_method, args=args, kwargs=kwargs)
        t.start()

    def execute(self, *args, **kwargs):
        self.__new_method(*args, **kwargs)


def task(*args, **kwargs):
    if len(args) == 1 and callable(args[0]):
        return Proxy(args[0])

    def wrapper(method):
        return Proxy(method, *args, **kwargs)

    return wrapper
