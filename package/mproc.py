import logging
import multiprocessing

logger = logging.getLogger(__name__)


def func(x):
    logger.debug(x)  # does not work
    return x + x


def mproc():
    logger.info('start mproc')
    logger.propagate = False
    logger.info('this will not be logged')
    param = [[elem] for elem in range(10)]
    with multiprocessing.Pool(processes=2) as pool:
        res = pool.starmap(func=func, iterable=param)
    logger.propagate = True
    logger.info('end mproc')
    return res
