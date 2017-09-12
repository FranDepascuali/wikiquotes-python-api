# -*- coding: utf-8 -*-
import unidecode

from ..languages import spanish
from ..languages import english
from . import custom_exceptions
from . import python_version_manager

def from_string(raw_language):
    if not is_unicode(raw_language):
        raw_language = unicode(raw_language)
    lowered = strip_special_characters(raw_language.lower())
    if lowered == u"en" or lowered == u"english" or lowered == u"ingles":
        return english
    # Using espanol because special character replaces accents and ñ
    elif lowered == u"es" or lowered == u"spanish" or lowered == u"espanol":
        return spanish

    raise custom_exceptions.UnsupportedLanguageException()

def transform_to_unicode(string):
    return string if is_unicode(string) else unicode(string)

def strip_special_characters(accented_string):
    if is_unicode(accented_string):
        return unidecode.unidecode(accented_string)
    else:
        return accented_string

def is_unicode(string):
    if python_version_manager.is_python_2():
        return isinstance(string, unicode)

    return python_version_manager.is_python_3()
