from time import sleep
import logging

logger = logging.getLogger(__name__)


def expensive_func():
    sleep(2)
    return 'expensive function'


def function():
    if logger.isEnabledFor(logging.INFO):
        logger.debug('%s', expensive_func())

    logger.info('FUNCTION info')
