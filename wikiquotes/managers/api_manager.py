import requests

from . import logging_manager
from . import custom_exceptions
from . import json_parser

def request_quote_of_the_day_page(language):
    return _request_via_scrapping(language.quote_of_the_day_url, language)

def request_quotes_page(title, language):
    answer = _request_quotes_via_api(title, language.base_url)
    if answer is None:
        raise custom_exceptions.PageNotFoundException()

    return json_parser.quotes_from_json(answer)

def request_titles(title, language):
    answer = None
    search_result = title

    while not isinstance(search_result, list):
        answer = _search_for_correct_title_via_api(search_result, language.base_url)
        search_result = json_parser.correct_title_from_json(answer)

    return search_result

def _search_for_correct_title_via_api(title, base_url):
    # https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=shakespeare
    return _request_via_api(base_url, action = 'query', list = 'search', srsearch = title, format = 'json')

def _request_quotes_via_api(title, base_url):
    return _request_via_api(base_url, titles = title, action = 'query', prop = 'extracts', format = 'json', redirects = True)

def _request_via_api(base_url, titles = None, action = None, prop = None, format = None, list = None, srsearch = None, redirects = None):
    def set_value(dictionary, key, value):
        if value:
            dictionary[key] = value

    parameters = {}
    set_value(parameters, 'action', action)
    set_value(parameters, 'prop', prop)
    set_value(parameters, 'format', format)
    set_value(parameters, 'redirects', redirects)
    set_value(parameters, 'titles', titles)
    set_value(parameters, 'list', list)
    set_value(parameters, 'srsearch', srsearch)

    request = requests.get(base_url, params = parameters, allow_redirects = redirects)

    if format == "json":
        answer = request.json()
    else:
        # logging_manager.error("Incorrect format (json expected)", exc_info=True)
        raise custom_exceptions.IncorrectAPIFormatException()

    return answer

# Use this if it can't be achieved by _request_via_api (because _request_via_api solves redirects automatically)
def _request_via_scrapping(page, language):
    request = requests.get(page)
    # logging_manager.info("Requesting via scrapping: {}".format(page))
    return request.content
