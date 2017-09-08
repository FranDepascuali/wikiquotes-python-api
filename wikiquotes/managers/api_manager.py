import requests
import logging_manager
import custom_exceptions

def request_quote_of_the_day_page(language):
    return _request_via_api_via_scrapping(language.quote_of_the_day_url, language)

def request_quotes_page(title, language):
    try:
        return _request_via_api(title, language.base_url)
    except custom_exceptions.PageNotFoundException:
        logging_manager.logger.error("Quotes not found: {}: {}".format(title, str(language)))

def _request_via_api(title, base_url, action = 'query', prop = 'extracts', format = 'json', redirects = True):
    parameters = {}
    parameters['action'] = action
    parameters['prop'] = prop
    parameters['format'] = format
    parameters['redirects'] = redirects
    parameters['titles'] = title

    request = requests.get(base_url, params = parameters, allow_redirects = redirects)

    if format == "json":
        answer = request.json()
    else:
        logging_manager.logger.error("Incorrect format (json expected)", exc_info=True)
        raise custom_exceptions.IncorrectAPIFormatException()

    try:
        quotes_page = _page_from_json(answer)
    except KeyError:
        logging_manager.logger.error("Quotes not found {}".format(request.url), exc_info=True)
        raise custom_exceptions.PageNotFoundException()

    return _page_from_json(answer)

# Use this if it can't be achieved by _request_via_api (because _request_via_api solves redirects automatically)
def _request_via_api_via_scrapping(page, language):
    request = requests.get(page)
    logging_manager.logger.info("Requesting via scrapping: {}".format(page))
    return request.content

# Wikiquote api returns an html page inside the content ('extract')
def _page_from_json(wikiquote_answer):
    pages = wikiquote_answer['query']['pages']

    text = ""

    for (key, value) in pages.items():
        try:
            text += pages[key]['extract']
        except KeyError:
            raise custom_exceptions.PageNotFoundException()

    return text
