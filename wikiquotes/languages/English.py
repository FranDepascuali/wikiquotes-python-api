base_url = "https://en.wikiquote.org/w/api.php"

startings = ["Quotes", "Quotations", "Sourced"]

# TODO: This is not working with disputed or Misattributed. BeautifulSoup doesn't catch them, they are in a strange box in wikiquote page.
# Need to investigate more.
endings = ["Misattributed", "Disputed", "External_links", "References", "Sources", "See_also"]
