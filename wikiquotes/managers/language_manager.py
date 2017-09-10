# -*- coding: utf-8 -*-
import unidecode

import english
import spanish
import custom_exceptions


class LanguageManager:

    def __init__(self, language_string):
        self.language = __get_language__(language_string)

def __get_language__(language_string):
    lowered = strip_accents(language_string.lower())
    if lowered == "en" or lowered == "english" or lowered == "ingles":
        return english
    elif lowered == "es" or lowered == "spanish" or lowered == "español":
        return spanish

    raise custom_exceptions.UnsupportedLanguageException()

def strip_accents(accented_string):
    return unidecode.unidecode(accented_string)
