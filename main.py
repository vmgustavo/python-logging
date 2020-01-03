import logging
import logging.config as lconfig
import json

from package import function, TheClass, mproc

with open('logger.json', 'rt') as f:
    config = json.load(f)
lconfig.dictConfig(config)

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
