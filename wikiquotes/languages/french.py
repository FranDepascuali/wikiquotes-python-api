#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

base_url = "https://fr.wikiquote.org/w/api.php"
quote_of_the_day_url = "https://fr.wikiquote.org/wiki/Mod%C3%A8le:Citation_du_jour"


def _normalize_spaces(text):
    # Normalize non-breaking (U+00A0) and narrow no-break (U+202F) spaces,
    # then collapse every run of whitespace into a single space.
    text = text.replace("\xa0", " ").replace("\u202f", " ")
    return re.sub(r"\s+", " ", text).strip()


def quotes_parser(web_page_manager):
    # French quote pages do NOT use the generic <ul><li>...</li></ul> structure.
    # Each quote lives in a <div class="citation">; the following <ul> blocks are
    # only the optional title ("precisions") and the bibliographic reference.
    soup = web_page_manager.soup
    quotes = []
    for citation in soup.find_all("div", class_="citation"):
        text = _normalize_spaces(citation.get_text())
        if text:
            quotes.append(text)
    return quotes


def _clean(text):
    # Normalize non-breaking (U+00A0) and narrow no-break (U+202F, "DisplaySpace") spaces.
    text = text.replace("\xa0", " ").replace("\u202f", " ").strip()
    # Strip the French guillemets that wrap the quote.
    return text.strip("\u00ab\u00bb \t\r\n")


def quote_of_the_day_parser(html):
    # Structure of Modèle:Citation_du_jour:
    #   <blockquote><p>« ...quote... »</p></blockquote>
    #   <p style="...">— <a ...>Author</a></p>
    blockquote = html.find("blockquote")

    quote = _clean(blockquote.get_text())

    author_paragraph = blockquote.find_next_sibling("p")
    if author_paragraph is None:
        author = ""
    else:
        # Remove the leading em-dash ("—") and any surrounding spaces.
        author = author_paragraph.get_text().lstrip("\u2014 \xa0\u202f").strip()

    return (quote, author)


non_quote_sections = [
    "voir aussi",
    "voir également",
    "liens externes",
    "liens internes",
    "référence",
    "note et référence",
    "citée à tort",
    "citées à tort",
    "à propos",
    "sur wikiquote",
    "bibliographie",
    "articles connexes",
]
