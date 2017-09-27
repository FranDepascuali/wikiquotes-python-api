#!/usr/bin/env python
# -*- coding: utf-8 -*-

base_url = "https://es.wikiquote.org/w/api.php"
quote_of_the_day_url = "https://es.wikiquote.org/wiki/Wikiquote:Frase_del_día"

def quote_of_the_day_parser(html):
    table = html("table")[1].table
    td = table("td")
    quote = td[2].text.strip()
    author = td[-1].div.a.text.strip()

    # Author and quote could have an accent
    return (quote, author)

non_quote_sections = ["sobre", "referencias"]
