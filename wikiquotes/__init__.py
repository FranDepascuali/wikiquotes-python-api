from .wikiquotes_api import search, get_quotes, quote_of_the_day, random_quote, supported_languages

try:
    from importlib.metadata import version
    __version__ = version("wikiquotes")
except Exception:
    __version__ = "unknown"
