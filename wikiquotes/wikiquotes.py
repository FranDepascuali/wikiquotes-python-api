# -*- coding: utf-8 -*-
import random
import directory
import os

import file_manager
import api_manager
import html_manager
import spanish

def get_all_quotes(author, language):
    quotes_page = api_manager.get_quotes_page(author, language)
    webpageManager = html_manager.HTMLManager(quotes_page, language)

    quotes_start = webpageManager.start_of_quotes()
    quotes_ending = webpageManager.end_of_quotes()

    if quotes_start is None:
        print ("UPS")
        return []

    quotes = []

    for element in quotes_start.next_elements:
        if element == quotes_ending:
            break

        if html_manager.is_list(element):
            webpageManager.remove_sublists(element)
            quotes.extend(html_manager.extract_all_items_from_list(element))

        if html_manager.is_subheading(element):
            webpageManager.remove(element)

    return quotes

def random_quote(author, language):
    return random.choice(get_all_quotes(author, language))

def supported_languages():
    languages = file_manager.list_files_with_extension(directory.languages_directory, ".py")
    return map(lambda language: language.replace(".py", ""), languages)
