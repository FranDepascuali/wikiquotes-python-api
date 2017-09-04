import requests

def get_quotes_page(author, language):
    return __page_from_json__(__request__(author, language.base_url))

def __request__(author, base_url, action = 'query', prop = 'extracts', format = 'json', redirects = True):
    parameters = {}
    parameters['action'] = action
    parameters['prop'] = prop
    parameters['format'] = format
    parameters['redirects'] = redirects
    parameters['titles'] = author

    request = requests.get(base_url, params = parameters, allow_redirects = redirects)

    if format == "json":
        answer = request.json()
    else:
        # TODO: Correct error handling
        print("Error: Unsupported format")

    return answer

# Wikiquote api returns an html page inside the content ('extract')
def __page_from_json__(wikiquote_answer):
    pages = wikiquote_answer['query']['pages']

    text = ""

    for (key, value) in pages.items():
        text += pages[key]['extract']

    return text
