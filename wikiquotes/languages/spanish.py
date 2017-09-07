#!/usr/bin/env python
# -*- coding: utf-8 -*-

base_url = "https://es.wikiquote.org/w/api.php"

startings = ["Citas"]

# TODO: This is not working with mw-normal-catlinks. BeautifulSoup doesn't catch them, they are in a strange box in wikiquote page.
# Need to investigate more.
endings = ["mw-normal-catlinks"]


quote_of_the_day_url = "https://es.wikiquote.org/wiki/Wikiquote:Frase_del_día"

def quote_of_the_day_parser(html):
    table = html("table")[1].table
    td = table("td")
    quote = td[2].text.strip()
    author = td[-1].div.a.text.strip()

    # Author and quote could have an accent
    return (quote.encode('utf-8'), author.encode('utf-8'))
