import directory

import APIManager
import HTMLManager
import english

def get_all_quotes(author):
    quotes_page = APIManager.get_quotes_page(author)
    webpageManager = HTMLManager.HTMLManager(quotes_page, english)

    quotes_start = webpageManager.start_of_quotes()
    quotes_ending = webpageManager.end_of_quotes()

    if quotes_start is None:
        print ("UPS")
        return []

    quotes = []

    for element in quotes_start.next_elements:
        if element == quotes_ending:
            break

        if HTMLManager.is_list(element):
            webpageManager.remove_sublists(element)
            quotes.extend(HTMLManager.extract_all_items_from_list(element))

        if HTMLManager.is_subheading(element):
            webpageManager.remove(element)

    return quotes

def supported_languages():
    return "English"
