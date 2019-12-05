import sys
import os
import logging
import importlib

logger = logging.getLogger('logging_color')
if sys.platform == 'win32' and 'PYCHARM_HOSTED' not in os.environ:
    try:
        colorama = importlib.import_module('colorama')
        colorama.init()
        COLOR_TRIGGER = True
    except ImportError:
        logger.warning('you need install `colorama` on win32 platform')
        COLOR_TRIGGER = False
else:
    COLOR_TRIGGER = True


class ColorStreamHandler(logging.StreamHandler):
    colors = {
        'DEBUG': '\033[37m',
        'INFO': '\033[32;22m',
        'WARNING': '\033[33;1m',
        'ERROR': '\033[31;1m',
        'CRITICAL': '\033[41;1m',
    }

    def emit(self, record):
        try:
            msg = self.format(record)
            if COLOR_TRIGGER:
                msg = '{}{}\033[0m'.format(self.colors.get(record.__dict__["levelname"], "\033[0m"), msg)
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
