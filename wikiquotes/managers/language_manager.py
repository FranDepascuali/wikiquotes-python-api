# -*- coding: utf-8 -*-
import directory
import unidecode

import english
import spanish
import custom_exceptions


class LanguageManager:

    def __init__(self, language_string):
        if not is_unicode(language_string):
            language_string = unicode(language_string)
        self.language = __get_language__(language_string)

def __get_language__(language_string):
    lowered = strip_special_characters(language_string.lower())
    if lowered == u"en" or lowered == u"english" or lowered == u"ingles":
        return english
    # Using espanol because special character replaces accents and ñ
    elif lowered == u"es" or lowered == u"spanish" or lowered == u"espanol":
        return spanish

    raise custom_exceptions.UnsupportedLanguageException()

def transform_to_unicode(string):
    return string if is_unicode(string) else unicode(string)

def strip_special_characters(accented_string):
    if is_unicode(accented_string) or directory.python_version[0] == 3:
        return unidecode.unidecode(accented_string)
    else:
        return accented_string

def is_unicode(string):
    if directory.python_version[0] == 2:
        return isinstance(string, unicode)

    return True
