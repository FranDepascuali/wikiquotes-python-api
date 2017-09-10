from bs4 import BeautifulSoup, Tag

import logging_manager

class HTMLManager:

    def __init__(self, html, language):
        self.language = language
        self.soup = BeautifulSoup(html, "lxml")

    # Although this doesn't need self, it mutates state so it's better to have it here and not as a free function.
    def remove_sublists(self, html_list):
            list_items = html_list.find_all('li')

            for li in list_items:
                if not li is -1 and li:
                    if li.ul:
                        li.ul.decompose()

    # Although this doesn't need self, it mutates state so it's better to have it here and not as a free function.
    def remove(self, element):
        for child in element.findChildren():
            child.decompose()

    def pretty_print(self):
        print(self.soup.prettify())

    def find_all_lists(self):
        return self.soup.find_all("ul")

def extract_text_from_list(html_list):
    return map(lambda li_quote: li_quote.text.strip(), html_list.find_all("li"))
