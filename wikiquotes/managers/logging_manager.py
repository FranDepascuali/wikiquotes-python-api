import logging
import time
import sys
import inspect
from functools import wraps
from slacker import Slacker

from ..secrets import slack_token

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')

class SlackHandler(logging.Handler):

    @staticmethod
    def create(action, level, formatter):
        handler = SlackHandler(level=level)
        handler.action = action
        handler.setFormatter(formatter)
        return handler

    def emit(self, record):
        self.action(self.format(record))

def error(message):
    logger.error(message)

def info(message):
    logger.info(message)

def debug(message):
    logger.debug(message)

slack = Slacker(slack_token)

logger = logging.getLogger("wikiquotes")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

_error = lambda message: slack.chat.post_message('#error', message)
_info = lambda message: slack.chat.post_message('#info', message)
_debug = lambda message: slack.chat.post_message('#logs', message)

info_handler = SlackHandler.create(_info, logging.INFO, formatter)
debug_handler = SlackHandler.create(_debug, logging.DEBUG, formatter)
error_handler = SlackHandler.create(_error, logging.ERROR, formatter)

logger.addHandler(info_handler)
logger.addHandler(debug_handler)
logger.addHandler(error_handler)

logger.setLevel(logging.DEBUG)
logger.propagate = False

def log_method_call(task):
    @wraps(task)
    def callable(*args, **kwargs):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        function_called = "{}".format(task.__name__)
        logging.info("{} started: ".format(function_called))
        start_detection = time.time()
        task(*args, **kwargs)
        logging.info("{} finished: took {} seconds".format(function_called, time.time() - start_detection))
        return task(*args, **kwargs)
    return callable
