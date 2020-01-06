import logging

from package import function, TheClass, mproc

logger = logging.getLogger(__name__)


def main():
    logger.info('### START EXECUTION ###')
    logger.info('info')
    logger.warning('warning')
    logger.debug('debug')
    logger.error('error')
    logger.critical('critical')

    function()

    cls = TheClass()
    cls.method()

    res = mproc()
    print(res)


if __name__ == '__main__':
    main()
