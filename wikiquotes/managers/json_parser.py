from . import custom_exceptions

# Wikiquote api returns an html page inside the content ('extract')
def quotes_from_json(wikiquote_answer):
    pages = wikiquote_answer['query']['pages']

    text = ""

    for (key, value) in pages.items():
        try:
            text += pages[key]['extract']
        except KeyError:
            raise custom_exceptions.PageNotFoundException()

    return text

def correct_title_from_json(wikiquote_answer):
    search_info = wikiquote_answer['query']['searchinfo']

    try:
        suggestion = search_info['suggestion']
        return suggestion
    except KeyError:
        pass

    # If we reach here, no suggestions.
    search =  wikiquote_answer['query']['search']

    if search == []:
        raise custom_exceptions.TitleNotFound

    search_titles = []

    for search_result in search:
        search_titles.append(search_result['title'])

    return search_titles
