import sys


class LoggerRepository(object):
    def initilize(self):
        pass

    def write(self, log_name, msg, severity='INFO'):
        pass


class PrintLoggerRepository(LoggerRepository):
    logging_client = None

    def __init__(self):
        super().__init__()

    def initilize(self):
        pass

    def write(self, log_name, msg, severity='INFO'):
        print("{}: {}".format(severity, msg))


class SysLoggerRepository(LoggerRepository):
    logging_client = None

    def __init__(self):
        super().__init__()

    def initilize(self):
        pass

    def write(self, log_name, msg: str, severity='INFO'):
        sys.stderr.write("{}: {}".format(severity, msg))
