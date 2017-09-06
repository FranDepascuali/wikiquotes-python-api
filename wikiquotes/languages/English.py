base_url = "https://en.wikiquote.org/w/api.php"

startings = ["Quotes", "Quotations", "Sourced"]

# TODO: This is not working with disputed or Misattributed. BeautifulSoup doesn't catch them, they are in a strange box in wikiquote page.
# Need to investigate more.
endings = ["Misattributed", "Disputed", "External_links", "References", "Sources", "See_also"]

quote_of_the_day_url = "https://en.wikiquote.org/wiki/Wikiquote:Quote_of_the_day"

def quote_of_the_day_parser(html):
    quote_and_author = (html.table)("td")[2]("td")

    quote = quote_and_author[0].text.strip()
    author = quote_and_author[1].text.replace("~", "").strip()

    return (quote, author)
