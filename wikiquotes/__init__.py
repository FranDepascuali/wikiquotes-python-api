from .wikiquotes_api import search, get_quotes, quote_of_the_day, random_quote, supported_languages
from .managers import python_version_manager

if python_version_manager.is_python_2():
    # In python 3.x, the default encoding is already utf8.
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
