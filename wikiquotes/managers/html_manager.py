from bs4 import BeautifulSoup, Tag

_titles = ['h2', 'h3', 'h4']

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

    def delete_sections(self, non_quotes_section_keywords):

        def is_non_quote_section(html_title):
            for non_section_keyword in non_quotes_section_keywords:
                if non_section_keyword in html_title.text.lower():
                    return True
            return False

        all_sections = find_all_titles(self.soup)
        non_quotes_sections = list(filter(is_non_quote_section, all_sections))

        # Don't know exactly why, but can't decompose directly in loop. Have to do it later.
        elements_to_decompose = []

        for non_quotes_section in non_quotes_sections:
            for element in non_quotes_section.next_siblings:
                if is_title(element):
                    break
                else:
                    if isinstance(element, Tag) and element.name == "ul":
                        elements_to_decompose.append(element)

        # Deletes non quotes
        for element in elements_to_decompose:
            element.decompose()

        # This has to be done after deleting the quotes (sections aren't necesarily in order)
        for non_quotes_section in non_quotes_sections:
            non_quotes_section.decompose()

def is_title(html_element):
    return isinstance(html_element, Tag) and html_element in _titles

def find_all_titles(html):
    return html.findAll(_titles)

def extract_text_from_list(html_list):
    return map(lambda li_quote: li_quote.text.strip(), html_list.find_all("li"))
