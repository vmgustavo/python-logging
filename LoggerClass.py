import sys
from loguru import logger


class Logger:
    def __init__(self, path='log.out'):
        # BASIC CONFIG
        format_stdout = '<green>{time:YYYY-MM-DDTHH:mm:ss}</green> | ' \
                        '<level>{level: <8}</level> | ' \
                        '<cyan>{name}</cyan> : <cyan>{function} [{line}]</cyan> - <level>{message}</level>'
        format_file = '{time:YYYY-MM-DDTHH:mm:ss} | {level: <8} | {name} : {function} [{line}] - {message}'
        logger.configure(**{
            "handlers": [
                {"sink": sys.stdout, "level": 'INFO', "format": format_stdout},
                {"sink": path, "level": 'DEBUG', "format": format_file, "rotation": "1 MB"}
            ]
        })
