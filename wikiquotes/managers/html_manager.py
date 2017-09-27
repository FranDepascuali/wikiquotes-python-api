from bs4 import BeautifulSoup, Tag

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

    def delete_sections(self, sections):
        def find_section(section_text):
            return self.soup.find('h2', text = lambda found_section: found_section and section_text in found_section.lower())

        non_quote_sections = list(filter(None, map(find_section, sections)))
        # Don't know exactly why, but can't decompose directly in loop. Have to do it later.
        elements_to_decompose = []

        for section in non_quote_sections:
            for element in section.next_siblings:
                if isinstance(element, Tag) and element.name == "h2":
                    break
                else:
                    if isinstance(element, Tag) and element.name == "ul":
                        elements_to_decompose.append(element)

        # Deletes non quotes
        for element in elements_to_decompose:
            element.decompose()

        # This has to be done after deleting the quotes (sections aren't necesarily in order)
        for non_quote_section in non_quote_sections:
            non_quote_section.decompose()

def extract_text_from_list(html_list):
    return map(lambda li_quote: li_quote.text.strip(), html_list.find_all("li"))
