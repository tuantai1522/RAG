import logging
from enum import StrEnum

LOG_DEBUG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

class LogLevels(StrEnum):
    INFO = "info"
    WARD = "warn"
    ERROR = "error"
    DEBUG = "debug"

def configure_logging(log_level: str = LogLevels.ERROR):
    if log_level == LogLevels.DEBUG:
        logging.basicConfig(level=log_level, format=LOG_DEBUG_FORMAT)
        return
    
    logging.basicConfig(level=log_level)

    