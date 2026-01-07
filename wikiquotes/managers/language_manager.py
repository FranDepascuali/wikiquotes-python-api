# -*- coding: utf-8 -*-
import unidecode

from ..languages import spanish
from ..languages import english
from . import custom_exceptions

def from_string(raw_language):
    lowered = strip_special_characters(raw_language.lower())
    if lowered == "en" or lowered == "english" or lowered == "ingles":
        return english
    elif lowered == "es" or lowered == "spanish" or lowered == "espanol":
        return spanish

    raise custom_exceptions.UnsupportedLanguageException()

def transform_to_unicode(string):
    return string

def strip_special_characters(accented_string):
    return unidecode.unidecode(accented_string)
