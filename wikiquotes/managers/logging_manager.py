import logging
import time
import sys
import inspect

from functools import wraps

logging.basicConfig(level = logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

logger = logging
