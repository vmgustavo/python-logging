import logging
from time import sleep

from package import function
from package import TheClass

from LoggerClass import Logger


def main():
    Logger(path='log.log')
    logger = logging.getLogger(__name__)

    logger.debug('MAIN debug')
    logger.info('MAIN info')
    sleep(2)

    function()
    sleep(3)

    TheClass()
    TheClass().method()


if __name__ == '__main__':
    main()
