import requests
import json
import random
from bs4 import BeautifulSoup, Tag
import time

def get_all_quotes(author):
    answer = __get_text_from_json__(__request_to_wikiquote__(author))
    soup = BeautifulSoup(answer, "lxml")

    quotes_start = __find_quotes_start__(soup)
    quotes_ending = __find_quotes_ending__(soup)

    if quotes_start is None:
        print "UPS"
        return []

    probable_quotes = []

    for element in quotes_start.next_elements:
        if element == quotes_ending:
            break

        if __is_ul__(element):
            ul_quote_list = element
            __decompose_inner_lists__(ul_quote_list)
            quotes = __get_quotes_from_ul__(ul_quote_list)
            probable_quotes.extend(quotes)

        if __is_subheading__(element):
            for child in element.findChildren():
                child.decompose()

    return probable_quotes

def __request_to_wikiquote__(titles, action = 'query', prop = 'extracts', format = 'json'):
    base_url = 'https://en.wikiquote.org/w/api.php?'

    parameters = {}
    parameters['action'] = action
    parameters['prop'] = prop
    parameters['format'] = format
    parameters['redirects'] = 'redirects'
    parameters['titles'] = titles

    request = requests.get(base_url, params = parameters, allow_redirects=True)
    answer = request.json()

    return answer

def __get_text_from_json__(wikiquote_answer):
    pages = wikiquote_answer['query']['pages']

    text = ""

    for (key, value) in pages.items():
        text += pages[key]['extract']

    return text

def __get_quotes_from_ul__(ul_quote_list):
    return map(lambda li_quote: li_quote.text.encode('utf-8').strip(), ul_quote_list.find_all("li"))

def __is_ul__(item):
    return isinstance(item, Tag) and item.name == "ul"

def __is_heading__(item):
    return isinstance(item, Tag) and item.name == "h2"

def __is_subheading__(item):
    return isinstance(item, Tag) and item.name == "h3"

def __decompose_inner_lists__(element):
    lis = element.find_all('li')

    for li in lis:
        if not li is -1 and not li is None:
            if not li.ul is None:
                li.ul.decompose()

def __find_quotes_start__(soup):
    ids = ["Quotes", "Quotations", "Sourced"]
    return __find_first__(ids, soup)

def __find_quotes_ending__(soup):
    ids = ["Misattributed", "Disputed", "External_links", "References", "Sources", "See_also"]
    # TODO: This is not working with disputed or Misattributed. BeautifulSoup doesn't catch them, they are in a strange box in wikiquote page.
    # Need to investigate more.

    return __find_first__(ids, soup)

def __find_first__(ids, soup):
    found_tags = []

    for id in ids:
        found = soup.find(id = id)
        if not found is None:
            found_tags.append(found.parent)

    if found_tags == []:
        print "Error: Not found"
    elif len(found_tags) == 1:
        return found_tags[0]
    else:
        return __determine_first_appearence__(soup, found_tags)

def __determine_first_appearence__(soup, tags):
    all_tags = soup.find_all(True)
    # Dummy value
    first_tag = None

    for tag in tags:
        if first_tag == None:
            first_tag = tag
        else:
            if all_tags.index(tag) < first_tag:
                first_tag = tag

    return first_tag
