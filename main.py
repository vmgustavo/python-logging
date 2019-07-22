from time import sleep
import matplotlib.pyplot as plt
from loguru import logger

from package import function
from package import TheClass

from LoggerClass import Logger
Logger()


def main():
    logger.debug('MAIN debug')
    logger.info('MAIN info')
    sleep(2)

    function()
    sleep(3)

    TheClass()
    TheClass().method()

    plt.plot(range(10))
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
