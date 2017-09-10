import random
import os

import directory
import logging_manager
import file_manager
import api_manager
import html_manager
import language_manager

@logging_manager.log_method_call
def get_quotes(author, raw_language):
    language = language_manager.LanguageManager(raw_language).language
    quotes_page = api_manager.request_quotes_page(author, language)
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

    return quotes

@logging_manager.log_method_call
def quote_of_the_day(raw_language):
    language = language_manager.LanguageManager(raw_language).language
    quotes_page = api_manager.request_quote_of_the_day_page(language)
    web_page_manager = html_manager.HTMLManager(quotes_page, language)

    return language.quote_of_the_day_parser(web_page_manager.soup)

@logging_manager.log_method_call
def random_quote(author, raw_language):
    return random.choice(get_quotes(author, raw_language))

@logging_manager.log_method_call
def supported_languages():
    languages = file_manager.list_relative_files_with_extension(directory.languages_directory, ".py")
    return map(lambda language: language.replace(".py", ""), languages)
