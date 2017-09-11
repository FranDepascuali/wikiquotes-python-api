import random
import os

import directory
import logging_manager
import file_manager
import api_manager
import html_manager
import language_manager
import custom_exceptions

def search(author, raw_language):
    language = language_manager.LanguageManager(raw_language).language
    try:
        search_results = api_manager.request_titles(author, language)
    except custom_exceptions.TitleNotFound:
        logging_manager.logger.error("Author not found: {}: {}".format(author, raw_language))
        raise

    return list(map(language_manager.transform_to_unicode, search_results))

def get_quotes(author, raw_language):
    language = language_manager.LanguageManager(raw_language).language

    suggested_author = search(author, raw_language)[0]
    quotes_page = api_manager.request_quotes_page(suggested_author, language)
    web_page_manager = html_manager.HTMLManager(quotes_page, language)

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

    return list(map(language_manager.transform_to_unicode, quotes))

def quote_of_the_day(raw_language):
    language = language_manager.LanguageManager(raw_language).language
    quotes_page = api_manager.request_quote_of_the_day_page(language)
    web_page_manager = html_manager.HTMLManager(quotes_page, language)

    quote_of_the_day = language.quote_of_the_day_parser(web_page_manager.soup)
    quote_of_the_day = (language_manager.transform_to_unicode(quote_of_the_day[0]), language_manager.transform_to_unicode(quote_of_the_day[1]))
    return quote_of_the_day

def random_quote(author, raw_language):
    return random.choice(get_quotes(author, raw_language))

def supported_languages():
    languages = file_manager.list_relative_files_with_extension(directory.languages_directory, ".py")
    return map(lambda language: language.replace(".py", ""), languages)
