# -*- coding: utf-8 -*-

import time

from fastlogging import LogInit


def test_logorder():
    logger = LogInit(console=True, colors=False)
    for _ in range(10):
        logger.debug('this is a debug message')
        logger.info('this is a info msg')
        logger.warning('this is a warning msg')
        logger.error('this is a error msg')
        logger.fatal('this is a fatal msg')
        logger.critical('this is a critical msg')
        #time.sleep(1)
        print()
    assert 0


if __name__ == "__main__":
    test_logorder()
