# -*- coding: utf-8 -*-
import unittest
import sys
import os

import pytest
sys.path.append(os.path.abspath('.'))

import wikiquotes
from wikiquotes.managers import language_manager
from wikiquotes.languages import spanish
from wikiquotes.languages import english
from tests.authors import Author

# class EncodingTest(unittest.TestCase):


#     def test_english_encoding(self):
#         self.assertEqual(english, _generate("English"))
#         self.assertEqual(english, _generate("english"))
#         self.assertEqual(english, _generate("en"))
#         self.assertEqual(english, _generate("Inglés"))
#         self.assertEqual(english, _generate("Ingles"))
#         self.assertEqual(english, _generate("ingles"))

#     def test_spanish_encoding(self):

#         self.assertEqual(spanish, _generate("Spanish"))
#         self.assertEqual(spanish, _generate("spanish"))
#         self.assertEqual(spanish, _generate("es"))
#         self.assertEqual(spanish, _generate("Español"))
#         self.assertEqual(spanish, _generate("español"))

#     @unittest.skipIf(SKIP_QOTD_TESTS, "Skipped in CI - quote changes during execution")
#     def test_spanish_quote_of_the_day_encoding_invariance(self):
#         # Test that different language string formats return the same result
#         # Note: We can't test exact quote content as it changes daily

#         # Get quote of the day with different language string formats
#         results = [
#             _qotd("Spanish"),
#             _qotd("spanish"),
#             _qotd("es"),
#             _qotd("Español"),
#             _qotd("español")
#         ]

#         # All results should be identical (same quote, same author)
#         first_result = results[0]
#         for result in results:
#             self.assertEqual(result, first_result)

#         # Verify result structure (tuple with 2 non-empty strings)
#         self.assertIsInstance(first_result, tuple)
#         self.assertEqual(len(first_result), 2)
#         self.assertIsInstance(first_result[0], str)  # quote
#         self.assertIsInstance(first_result[1], str)  # author
#         self.assertGreater(len(first_result[0]), 0)
#         self.assertGreater(len(first_result[1]), 0)

#     # @unittest.skipIf(SKIP_QOTD_TESTS, "Skipped in CI - quote changes during execution")
#     # def test_english_quote_of_the_day_encoding_invariance(self):
#         # Test that different language string formats return the same result
#         # Note: We can't test exact quote content as it changes daily

#         # Get quote of the day with different language string formats
#         results = [
#             _qotd("English"),
#             _qotd("english"),
#             _qotd("en"),
#             _qotd("Inglés"),
#             _qotd("Ingles"),
#             _qotd("ingles")
#         ]

#         # All results should be identical (same quote, same author)
#         first_result = results[0]
#         for result in results:
#             self.assertEqual(result, first_result)

#         # Verify result structure (tuple with 2 non-empty strings)
#         self.assertIsInstance(first_result, tuple)
#         self.assertEqual(len(first_result), 2)
#         self.assertIsInstance(first_result[0], str)  # quote
#         self.assertIsInstance(first_result[1], str)  # author
#         self.assertGreater(len(first_result[0]), 0)
#         self.assertGreater(len(first_result[1]), 0)

def _generate(string):
    return language_manager.from_string(string)

def _qotd(string):
    return wikiquotes.quote_of_the_day(string)

if __name__ == '__main__':
    unittest.main()
