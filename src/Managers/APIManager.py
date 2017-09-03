import requests

def get_quotes_page(authors):
    return __page_from_json__(__request__(authors))

def __request__(authors, url = 'https://en.wikiquote.org/w/api.php?', action = 'query', prop = 'extracts', format = 'json'):
    parameters = {}
    parameters['action'] = action
    parameters['prop'] = prop
    parameters['format'] = format
    parameters['redirects'] = 'redirects'
    parameters['titles'] = authors

    request = requests.get(url, params = parameters, allow_redirects=True)
    answer = request.json()

    return answer

# Wikiquote api returns an html page inside the content ('extract')
def __page_from_json__(wikiquote_answer):
    pages = wikiquote_answer['query']['pages']

    text = ""

    for (key, value) in pages.items():
        text += pages[key]['extract']

    return text
