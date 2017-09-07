import requests

def request_quote_of_the_day_page(language):
    return _request_via_api_via_scrapping(language.quote_of_the_day_url, language)

def request_quotes_page(title, language):
    return _request_via_api(title, language.base_url)

def _request_via_api(title, base_url, action = 'query', prop = 'extracts', format = 'json', redirects = True):
    parameters = {}
    parameters['action'] = action
    parameters['prop'] = prop
    parameters['format'] = format
    parameters['redirects'] = redirects
    parameters['titles'] = title

    request = requests.get(base_url, params = parameters, allow_redirects = redirects)

    # TODO: This should be for debug
    print ("Requesting via API: {}".format(request.url))

    if format == "json":
        answer = request.json()
    else:
        # TODO: Correct error handling
        print("Error: Unsupported format")

    return _page_from_json(answer)

# Use this if it can't be achieved by _request_via_api (because _request_via_api solves redirects automatically)
def _request_via_api_via_scrapping(page, language):
    request = requests.get(page)
    print("Requesting via scrapping: {}".format(page))
    return request.content

# Wikiquote api returns an html page inside the content ('extract')
def _page_from_json(wikiquote_answer):
    pages = wikiquote_answer['query']['pages']

    text = ""

    for (key, value) in pages.items():
        text += pages[key]['extract']

    return text
