from loguru import logger


class TheClass:
    def __init__(self):
        logger.info('CLASS INIT info')

    @staticmethod
    def method():
        logger.info('CLASS METHOD info')
