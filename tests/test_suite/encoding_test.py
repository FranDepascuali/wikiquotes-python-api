# -*- coding: utf-8 -*-
import unittest
import sys
import os
sys.path.append(os.path.abspath('.'))

import wikiquotes
from wikiquotes.managers import language_manager
from wikiquotes.languages import spanish
from wikiquotes.languages import english
from tests.authors import Author

class EncodingTest(unittest.TestCase):

    def test_english_encoding(self):
        self.assertEqual(english, _generate("English"))
        self.assertEqual(english, _generate("english"))
        self.assertEqual(english, _generate("en"))
        self.assertEqual(english, _generate("Inglés"))
        self.assertEqual(english, _generate("Ingles"))
        self.assertEqual(english, _generate("ingles"))

        self.assertEqual(english, _generate(u"English"))
        self.assertEqual(english, _generate(u"english"))
        self.assertEqual(english, _generate(u"en"))
        self.assertEqual(english, _generate(u"Inglés"))
        self.assertEqual(english, _generate(u"Ingles"))
        self.assertEqual(english, _generate(u"ingles"))

    def test_spanish_encoding(self):

        self.assertEqual(spanish, _generate("Spanish"))
        self.assertEqual(spanish, _generate("spanish"))
        self.assertEqual(spanish, _generate("es"))
        self.assertEqual(spanish, _generate("Español"))
        self.assertEqual(spanish, _generate("español"))

        self.assertEqual(spanish, _generate(u"Spanish"))
        self.assertEqual(spanish, _generate(u"spanish"))
        self.assertEqual(spanish, _generate(u"es"))
        self.assertEqual(spanish, _generate(u"Español"))
        self.assertEqual(spanish, _generate(u"español"))

    def test_get_quotes_encoding(self):
        author = Author.random_author()
        quotes = wikiquotes.get_quotes(author.name, author.language)

        for quote in quotes:
            self.assertTrue(language_manager.is_unicode(quote))

    def test_random_quote_encoding(self):
        author = Author.random_author()
        random_quote = wikiquotes.random_quote(author.name, author.language)

        self.assertTrue(language_manager.is_unicode(random_quote))

    def test_quote_of_the_day_encoding(self):
        spanish_quote_of_the_day = wikiquotes.quote_of_the_day("spanish")
        self.assertTrue(language_manager.is_unicode(spanish_quote_of_the_day[0]))
        self.assertTrue(language_manager.is_unicode(spanish_quote_of_the_day[1]))

        english_quote_of_the_day = wikiquotes.quote_of_the_day("english")
        self.assertTrue(language_manager.is_unicode(english_quote_of_the_day[0]))
        self.assertTrue(language_manager.is_unicode(english_quote_of_the_day[1]))

    def test_spanish_quote_of_the_day_encoding_invariance(self):

        quote_of_the_day = wikiquotes.quote_of_the_day("spanish")

        self.assertEqual(quote_of_the_day, _qotd("Spanish"))
        self.assertEqual(quote_of_the_day, _qotd("spanish"))
        self.assertEqual(quote_of_the_day, _qotd("es"))
        self.assertEqual(quote_of_the_day, _qotd("Español"))
        self.assertEqual(quote_of_the_day, _qotd("español"))

        self.assertEqual(quote_of_the_day, _qotd(u"Spanish"))
        self.assertEqual(quote_of_the_day, _qotd(u"spanish"))
        self.assertEqual(quote_of_the_day, _qotd(u"es"))
        self.assertEqual(quote_of_the_day, _qotd(u"Español"))
        self.assertEqual(quote_of_the_day, _qotd(u"español"))

    def test_english_quote_of_the_day_encoding_invariance(self):

        quote_of_the_day = wikiquotes.quote_of_the_day("english")

        self.assertEqual(quote_of_the_day, _qotd("English"))
        self.assertEqual(quote_of_the_day, _qotd("english"))
        self.assertEqual(quote_of_the_day, _qotd("en"))
        self.assertEqual(quote_of_the_day, _qotd("Inglés"))
        self.assertEqual(quote_of_the_day, _qotd("Ingles"))
        self.assertEqual(quote_of_the_day, _qotd("ingles"))

        self.assertEqual(quote_of_the_day, _qotd(u"English"))
        self.assertEqual(quote_of_the_day, _qotd(u"english"))
        self.assertEqual(quote_of_the_day, _qotd(u"en"))
        self.assertEqual(quote_of_the_day, _qotd(u"Inglés"))
        self.assertEqual(quote_of_the_day, _qotd(u"Ingles"))
        self.assertEqual(quote_of_the_day, _qotd(u"ingles"))

def _generate(string):
    return language_manager.from_string(string)

def _qotd(string):
    return wikiquotes.quote_of_the_day(string)

if __name__ == '__main__':
    unittest.main()
