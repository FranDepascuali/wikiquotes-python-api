#!/usr/bin/env python
# -*- coding: utf-8 -*-

base_url = "https://es.wikiquote.org/w/api.php"
quote_of_the_day_url = "https://es.wikiquote.org/wiki/Portada"

def quote_of_the_day_parser(html):
    table = html("table")[1]("table")[0]
    quote = table("td")[3].text.strip()
    author = table("td")[5].div.a.text.strip()

    # Author and quote could have an accent
    return (quote, author)

non_quote_sections = ["sobre", "referencias"]
