import logging


def setup_logger(level):
    logging.basicConfig(format='%(asctime)s %(name)-12s: %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.DEBUG)
    root_logger = logging.getLogger('')
    root_logger.setLevel(level)
