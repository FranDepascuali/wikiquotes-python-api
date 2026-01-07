![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)

# wikiquotes-python-api

This library is intended to be a python API for wikiquotes (inspired by [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/)).

## Funding

<a href="https://github.com/sponsors/FranDepascuali">
  <img align="right" width="150" alt="This library helped you? Consider sponsoring!" src=".github/funding-octocat.svg">
</a>

This module is provided **as is**, I work on it in my free time.

If your company uses it in a production app, consider sponsoring this project 💰. You also can contact me for enterprise support, help with issues, prioritize bugfixes, feature requests, etc.

## Table of Contents
  * [Usage](#usage)
  * [Installation](#installation)
  * [Motivation](#motivation)
  * [Search](#search)
  * [Output](#output)
  * [Testing](#testing)

## Usage
```python
>>> import wikiquotes

>>> wikiquotes.search("gandi", "english")
['Mahatma Gandhi', 'Indira Gandhi', 'Rahul Gandhi', 'Rajiv Gandhi', 'Arun Manilal Gandhi', 'Gandhi (film)', 'Anand Gandhi', 'Virchand Gandhi', 'Maneka Gandhi', 'Blindness']

>>> wikiquotes.get_quotes('Hau Pei-tsun', "english")
# ["The slogans of 'countering back the mainland' created by Chiang Kai-shek and 'liberating Taiwan' by Mao Zedong several decades ago should be forgotten because none of them could be put into practice.",
#  'When people on both sides of the Strait reach a consensus on their political system, unification will come to fruition naturally.',
#  'Taiwanese independence is a dead end.']

>>> wikiquotes.quote_of_the_day("english")
# ('Even after killing ninety nine tigers the Maharaja should beware of the hundredth.', 'Kalki Krishnamurthy')

>>> wikiquotes.quote_of_the_day("spanish")
# ('Por San Fermín, el calor no tiene fin', 'Refrán español')

>>> wikiquotes.random_quote("Aristotle", "english")
# 'For the things we have to learn before we can do, we learn by doing.'

>>> wikiquotes.supported_languages()
# ['english', 'spanish']
```

## Installation
```sh
pip install wikiquotes
```
## Motivation
There seems to be two options for retrieving quotes from WikiQuotes using python: To implement it yourself or to use [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/).
At a first glance, I chose the second option and used that library. However, usage and code inspection over [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/) lead me to choose the first approach and develop a library.

The main reasons for this decision were that:
1. Quotes retrieved weren't all the quotes in wikiquotes API (tried with different authors).
2. The code was too complex for what it was achieving. The choice in that project was to use urllib to retrieve the quotes, and lxml to parse the html.

This project:
1. Adds tests for retrieving all the quotes from several authors (Though this point is difficult to satisfy, because quotes don't respect a format for all authors).
2. Uses requests and BeautifulSoup, which abstract great part of the complexity which is present in [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/).

Anyway, the correct approach would be to try both and stick with the one that gives you the best results.

This project also gets to avoid fetching quotes included in about section. For example, if using [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/) and not this project:
```python
import wikiquote
print(wikiquote.quotes('Ada Lovelace'))
```
will fetch *"A large, coarse-skinned young woman but with something of my friend's features, particularly the mouth."*
which wasn't said by Ada Lovelace (but said about her).

While if you use this library, that quote and quotes about someone will not appear.
```python
import wikiquotes
print(wikiquotes.get_quotes('Ada Lovelace', 'english'))"
```
*"A large, coarse-skinned young woman but with something of my friend's features, particularly the mouth."* doesn't appear because it wasn't said by Ada Lovelace.

## Search
Quotes are retrieved by searching first for the correct author. This strives for robustness, because it allows to return a quote whether the input is the correct name of the author or not. At the same time, note that subsequent calls to WikiQuotes api have to be made to grab suggestions (see [here](https://github.com/FranDepascuali/wikiquotes-python-api/blob/master/wikiquotes/managers/api_manager.py#L20)).

Example:
"shakspare" -> "shakespeare" -> ['William Shakespeare', 'Last words in Shakespeare', 'Shakespeare in Love', ...]
-> get_quotes = 4 calls.

## Output

All string output is in unicode (Python 3 strings natively support unicode). Non-ASCII characters are handled automatically:
```python
>>> wikiquotes.random_quote("borges", "español")
# '«Todos caminamos hacia el anonimato, solo que los mediocres llegan un poco antes».'
```

## Testing
The approach for testing changed: at a first glance, testing was done by manually adding the code to test each author.
After that, I realized that the structure was the same for every author: We need the name, the language and the quotes. Using some *black* magic for parametrizing tests, I could extract all the logic to code and have a text file for each author. (See [author_test](https://github.com/FranDepascuali/wikiquotes-python-api/blob/master/tests/test_suite/author_test.py) for more info.)

The way of testing right now is to add a txt file of the author to test's [authors](https://github.com/FranDepascuali/wikiquotes-python-api/tree/master/tests/authors). For example, [here](https://github.com/FranDepascuali/wikiquotes-python-api/blob/master/tests/authors/dijkstra.txt) is the test for Dijkstra quotes in english.
Adding a new author is a txt file for the author (the name is irrelevant, but should be the author name) and respecting the following format.
1. First line: Author's name (or the suffix of the wikiquotes page, because sometimes wikipedia has ambiguate redirections if author name is used ).
2. Second line: language.
3. Third line: empty.
4. Following lines should contain one quote per line.
