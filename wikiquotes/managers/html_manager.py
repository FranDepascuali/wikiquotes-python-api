from bs4 import BeautifulSoup, Tag

class HTMLManager:

    def __init__(self, html, language):
        self.language = language
        self.soup = BeautifulSoup(html, "lxml")

    def start_of_quotes(self):
        return _find_first(self.language.startings, self.soup)

    def end_of_quotes(self):
        return _find_first(self.language.endings, self.soup)

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
        print self.soup
        print(self.soup.prettify())

def is_list(item):
    return isinstance(item, Tag) and item.name == "ul"

def extract_all_items_from_list(html_list):
    return map(lambda li_quote: li_quote.text.encode('utf-8').strip(), html_list.find_all("li"))

def is_subheading(item):
    return isinstance(item, Tag) and item.name == "h3"

def _find_first(ids, soup):
    maybe_tags_found = map(lambda id: soup.find(id = id), ids)
    tags_found = filter(None, maybe_tags_found)

    if tags_found == []:
        # TODO: Correct error handling
        print("THIS IS NOT NECESSARILY AN ERROR!. Not found: {}".format(ids))
        print("Because there are some author that don't have any finish tag. Example: https://en.wikiquote.org/wiki/Reuben_Abel")
    else:
        return _determine_first_appearence(soup, tags_found)

def _determine_first_appearence(soup, tags):
    all_tags = soup.find_all(True)
    return min(tags, key = lambda tag: all_tags.index(tag))
