import directory

import wikiquotes
import unittest

class QuoteLengthTest(unittest.TestCase):

    def test_Reuben_Abel(self):
        self.__execute__('Reuben_Abel', 1)

    def test_Hau_Pei_tsun_(self):
        self.__execute__('Hau_Pei-tsun', 3)

    def test_Jack_Abbott(self):
        self.__execute__('Jack_Abbott', 8)

    def test_Dijkstra(self):
        self.__execute__('Dijkstra', 75)

    def test_Aristotles(self):
        self.__execute__('Aristotle', 153)

    def __execute__(self, author, quotes_length):
        quotes = wikiquotes.get_all_quotes(author)
        # It is probable that new quotes are added.
        # The assumption is that quotes aren't removed.
        # So quotes fetched must be at least the numbers seen.
        # We don't want tests to break if there is a new quote.
        self.assertTrue(len(quotes) >= quotes_length)

        # No repeted elements
        self.assertEqual(len(quotes), len(set(quotes)))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
