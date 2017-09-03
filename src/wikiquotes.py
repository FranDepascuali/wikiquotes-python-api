# TODO: Make imports cleaner
import os
import sys
Directory = os.path.dirname(os.path.realpath(__file__))
Managers = os.path.join(Directory, "Managers")
Languages = os.path.join(Managers, "Languages")

sys.path.append(Directory)
sys.path.append(Managers)
sys.path.append(Languages)

import HTMLManager
import APIManager
import English

def get_all_quotes(authors):
    quotes_page = APIManager.get_quotes_page(authors)
    webpageManager = HTMLManager.HTMLManager(quotes_page, English)

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
