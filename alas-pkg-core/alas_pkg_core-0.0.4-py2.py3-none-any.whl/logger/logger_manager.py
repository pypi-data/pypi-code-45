import sys
from logger_repository import SysLoggerRepository
import os


class LoggerManager(object):
    log_name = 'my-log'

    def __init__(self, loggerRepository: LoggerRepository, debug=False):
        super().__init__()
        self.loggerRepository = loggerRepository
        self.sysloggerRepository = SysLoggerRepository()
        serv_name = os.getenv('SERVICE-NAME', None)
        self.debug = debug
        if serv_name:
            self.log_name = serv_name

    def log_info(self, msg):
        if not self.debug:
            self.loggerRepository.write(self.log_name, msg, severity="INFO")
        else:
            print(msg)

    def log_error(self, msg):
        if not self.debug:
            self.loggerRepository.write(self.log_name, msg, severity='ERROR')
        else:
            self.sysloggerRepository.write(
                self.log_name, msg, severity='ERROR')
