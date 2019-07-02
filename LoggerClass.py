import logging


class Logger:
    def __init__(self, path=None):
        format_string = '%(asctime)s : T%(relativeCreated)05ds : %(levelname)-8s - %(name)s : %(message)s'
        format_date = '%Y-%m-%dT%H:%M:%S'

        # BASIC CONFIG
        if path is not None:
            logging.basicConfig(filename=path, filemode='a', format=format_string, datefmt=format_date)

        # START LOGGER
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        # DEFINE FORMAT
        formatter = logging.Formatter(fmt=format_string, datefmt=format_date)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # LEVEL SET
        logger.setLevel(logging.DEBUG)

        self.logger = logging.getLogger(__name__)
