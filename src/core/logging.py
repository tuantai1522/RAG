import logging
from enum import StrEnum

LOG_DEBUG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

class LogLevels(StrEnum):
    info = "INFO"
    warn = "WARN"
    error = "ERROR"
    debug = "DEBUG"

def configure_logging(log_level: str = LogLevels.error):
    log_level = str(log_level).upper()
    log_levels = [level.value for level in LogLevels]

    if log_level not in log_levels:
        logging.basicConfig(level=LogLevels.error)
        return
    
    if log_level == LogLevels.debug:
        logging.basicConfig(level=LogLevels.debug, format=LOG_DEBUG_FORMAT)

    
    logging.basicConfig(level=log_level)

    