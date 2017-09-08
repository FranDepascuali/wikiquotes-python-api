import random
import directory
import os
import logging_manager

import file_manager
import api_manager
import html_manager
import spanish
import english

@logging_manager.log_method_call
def get_quotes(author, language):
    quotes_page = api_manager.request_quotes_page(author, language)
    web_page_manager = html_manager.HTMLManager(quotes_page, language)

    quotes_start = web_page_manager.start_of_quotes()
    quotes_ending = web_page_manager.end_of_quotes()

    if quotes_start is None:
        logging_manager.logger.error("Quotes start not found for {}:{}".format(author, str(language)), exc_info=True)
        raise QuoteStartNotFoundException()

    quotes = []

    for element in quotes_start.next_elements:
        if element == quotes_ending:
            break

        if html_manager.is_list(element):
            web_page_manager.remove_sublists(element)
            quotes.extend(html_manager.extract_all_items_from_list(element))

        if html_manager.is_subheading(element):
            web_page_manager.remove(element)

    return quotes

@logging_manager.log_method_call
def quote_of_the_day(language):
    quotes_page = api_manager.request_quote_of_the_day_page(language)
    web_page_manager = html_manager.HTMLManager(quotes_page, language)

    return language.quote_of_the_day_parser(web_page_manager.soup)

@logging_manager.log_method_call
def random_quote(author, language):
    return random.choice(get_quotes(author, language))

@logging_manager.log_method_call
def supported_languages():
    languages = file_manager.list_relative_files_with_extension(directory.languages_directory, ".py")
    return map(lambda language: language.replace(".py", ""), languages)
