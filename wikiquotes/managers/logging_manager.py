import logging
import time
import sys
import inspect

from functools import wraps

import directory

logging.basicConfig(filename=directory.log_path, level = logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
logger = logging

def log_method_call(task):
    @wraps(task)
    def callable(*args, **kwargs):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        function_called = "{}.{}".format(module.__name__, task.__name__)
        logging.info("{} started: ".format(function_called))
        start_detection = time.time()
        task(*args, **kwargs)
        logging.info("{} finished: took {} seconds".format(function_called, time.time() - start_detection))
        return task(*args, **kwargs)
    return callable
