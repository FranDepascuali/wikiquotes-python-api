import logging
import time
import inspect
from functools import wraps

logger = logging.getLogger("wikiquotes")
logger.addHandler(logging.NullHandler())

def error(message):
    logger.error(message)

def info(message):
    logger.info(message)

def debug(message):
    logger.debug(message)

def log_method_call(task):
    @wraps(task)
    def callable(*args, **kwargs):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        function_called = "{}".format(task.__name__)
        logger.info("{} started".format(function_called))  # Use logger, not logging
        start_detection = time.time()
        result = task(*args, **kwargs)  # Call once and store result
        logger.info("{} finished: took {} seconds".format(function_called, time.time() - start_detection))  # Use logger, not logging
        return result  # Return the stored result
    return callable
