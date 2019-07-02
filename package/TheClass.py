import logging


class TheClass:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('CLASS INIT info')

    def method(self):
        self.logger.info('CLASS METHOD info')
