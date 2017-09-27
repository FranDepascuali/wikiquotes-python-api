import random
import os

from .managers import logging_manager
from .managers import api_manager
from .managers import html_manager
from .managers import language_manager
from .managers import custom_exceptions

def search(author, raw_language):
    # logging_manager.info("API intent: {} author: {} raw_language: {}".format("search", author, raw_language))

    language = language_manager.from_string(raw_language)
    try:
        search_results = api_manager.request_titles(author, language)
    except custom_exceptions.TitleNotFound:
        # logging_manager.error("Author not found: {}: {}".format(author, raw_language))
        raise

    answer = list(map(language_manager.transform_to_unicode, search_results))

    # logging_manager.info("API intent: {} author: {} raw_language: {} result: {}".format("search", author, raw_language, answer))
    return answer

def get_quotes(author, raw_language):
    # logging_manager.info("API intent: {} author: {} raw_language: {}".format("get_quotes", author, raw_language))
    language = language_manager.from_string(raw_language)

    suggested_author = search(author, raw_language)[0]
    quotes_page = api_manager.request_quotes_page(suggested_author, language)
    web_page_manager = html_manager.HTMLManager(quotes_page, language)

    web_page_manager.delete_sections(language.non_quote_sections)

    html_lists = web_page_manager.find_all_lists()
    quotes = []

    # Almost every quote structure is:
    # <ul>
    #   <li> Quote text </li>
    #   <ul>
    #       <li> author or some reference</li>
    #   </ul>
    # </ul>
    for html_list in html_lists:
        web_page_manager.remove_sublists(html_list)
        quotes.extend(html_manager.extract_text_from_list(html_list))

    answer = list(map(language_manager.transform_to_unicode, quotes))

    # logging_manager.info("API intent: {} author: {} resolved_author: {} raw_language: {} result: {}".format("get_quotes", author, suggested_author, raw_language, answer))

    return answer

def quote_of_the_day(raw_language):
    # logging_manager.info("API intent: {} raw_language: {}".format("quote_of_the_day", raw_language))
    language = language_manager.from_string(raw_language)
    quotes_page = api_manager.request_quote_of_the_day_page(language)
    web_page_manager = html_manager.HTMLManager(quotes_page, language)

    quote_of_the_day = language.quote_of_the_day_parser(web_page_manager.soup)
    quote_of_the_day = (language_manager.transform_to_unicode(quote_of_the_day[0]), language_manager.transform_to_unicode(quote_of_the_day[1]))

    # logging_manager.info("API intent: {} raw_language: {} result: {}".format("quote_of_the_day", raw_language, quote_of_the_day))

    return quote_of_the_day

def random_quote(author, raw_language):
    # logging_manager.info("API intent: {} author: {} raw_language: {}".format("random_quote", author, raw_language))

    random_quote = random.choice(get_quotes(author, raw_language))

    # logging_manager.info("API intent: {} author: {} raw_language: {} result: {}".format("random_quote", author, raw_language, random_quote))

    return random_quote

def supported_languages():
    # logging_manager.info("API intent: {}".format("supported_languages"))
    languages = ["english", "spanish"]
    return languages
