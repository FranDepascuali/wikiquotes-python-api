base_url = "https://en.wikiquote.org/w/api.php"
quote_of_the_day_url = "https://en.wikiquote.org/wiki/Wikiquote:Quote_of_the_day"

def quote_of_the_day_parser(html):
    quote_and_author = (html.table)("td")[2]("td")

    quote = quote_and_author[0].text.strip()
    author = quote_and_author[1].text.replace("~", "").strip()

    return (quote, author)

non_quote_sections = ['cast', 'see also', 'external links', 'misquoted', 'misattributed', "about"]
