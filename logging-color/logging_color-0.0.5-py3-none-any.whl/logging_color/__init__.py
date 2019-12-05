import sys
import os
import logging


class ColorStreamHandler(logging.StreamHandler):
    colors = {
        'DEBUG': '\033[37m',
        'INFO': '\033[32;22m',
        'WARNING': '\033[33;1m',
        'ERROR': '\033[31;1m',
        'CRITICAL': '\033[41;1m',
    }
    colors_support = sys.platform != 'win32' or 'PYCHARM_HOSTED' in os.environ

    def emit(self, record):
        try:
            msg = self.format(record)
            if self.colors_support:
                msg = f'{self.colors[record.__dict__["levelname"]]}{msg}\033[0m'
            stream = self.stream
            # issue 35046: merged two stream.writes into one.
            stream.write(msg + self.terminator)
            self.flush()
        except RecursionError:  # See issue 36272
            raise
        except Exception:
            self.handleError(record)


def monkey_patch():
    logging.StreamHandler = ColorStreamHandler
