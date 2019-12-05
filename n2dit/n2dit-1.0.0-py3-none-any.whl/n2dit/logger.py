import logging
import os
from logging import handlers


class Logger:
    logger = None

    @classmethod
    def init(cls, package_name, level='INFO', log_file=None):
        Logger._tf_log_off() if level != 'DEBUG' else None
        cls.logger = logging.getLogger(package_name)
        if level == 'DEBUG':
            cls.logger.setLevel(logging.DEBUG)
        elif level == 'INFO':
            cls.logger.setLevel(logging.INFO)
        elif level == 'WARNING':
            cls.logger.setLevel(logging.WARNING)
        elif level == 'ERROR':
            cls.logger.setLevel(logging.ERROR)
        elif level == 'CRITICAL':
            cls.logger.setLevel(logging.CRITICAL)
        else:
            cls.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt='%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        cls.logger.addHandler(sh)
        if log_file:
            log_dir = os.path.dirname(log_file)
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            fh = handlers.TimedRotatingFileHandler(
                filename=log_file, when='D', interval=1, encoding='utf-8')
            fh.suffix = "%Y%m%d"
            fh.setFormatter(formatter)
            cls.logger.addHandler(fh)

    @classmethod
    def debug(cls, tag, msg):
        cls.logger.debug(tag + ': ' + msg)

    @classmethod
    def info(cls, tag, msg):
        cls.logger.info(tag + ': ' + msg)

    @classmethod
    def warning(cls, tag, msg):
        cls.logger.warning(tag + ': ' + msg)

    @classmethod
    def error(cls, tag, msg):
        cls.logger.error(tag + ': ' + msg)

    @classmethod
    def critical(cls, tag, msg):
        cls.logger.critical(tag + ': ' + msg)

    @classmethod
    def _tf_log_off(cls):
        import os
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        import tensorflow as tf
        if type(tf.contrib) != type(tf): tf.contrib._warning = None
        tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
