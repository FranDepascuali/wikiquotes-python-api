# wikiquote-python-api

This library is intended to be a python API for wikiquotes (inspired by [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/)).

## Table of Contents

  * [Motivation](#motivation)
  * [Usage](#usage)
  * [Languages](#bootstrap)
  * [Testing](#testing)
  * [About](#about)

## Motivation
There seems to be two options for retrieving quotes from WikiQuotes using python: To implement it yourself or to use [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/).
At a first glance, I chose the second option and used that library. However, usage and code inspection over [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/) lead me to choose the first approach and develop a library.

The main reasons for this decision were that:
1. Quotes retrieved weren't all the quotes in wikiquotes API (tried with different authors).
2. It doesn't work for python 2.x 
2. The code was too complex for what it was achieving. The choice in that project was to use urllib to retrieve the quotes, and lxml to parse the html.

This project:
1. Adds tests for retrieving all the quotes from several authors (Though this point is difficult to satisfy, because quotes don't respect a format for all authors). 
2. Works for python 2.x and 3.x
3. Uses requests and BeautifulSoup, which abstract great part of the complexity which is present in [python-wikiquotes](https://github.com/federicotdn/python-wikiquotes/).

Anyway, the correct approach would be to try both and stick with the one that gives you the best results.

## Usage
```python
TODO
```

## Languages
Wikiquotes currently support English and Spanish.

## Testing
The approach for testing changed: at a first glance, testing was done by manually adding the code to test each author. 
After that, I realized that the structure was the same for every author: We need the name, the language and the quotes. Using some *black* magic for parametrizing tests, I could extract all the logic to code and have a text file for each author. (See [author_test](https://github.com/FranDepascuali/wikiquotes-python-api/blob/master/tests/test_suite/author_test.py) for more info.)

The way of testing right now is to add a txt file of the author to test's [authors](https://github.com/FranDepascuali/wikiquotes-python-api/tree/master/tests/authors). For example, [here](https://github.com/FranDepascuali/wikiquotes-python-api/blob/master/tests/authors/dijkstra.txt) is the test for Dijkstra quotes in english. 
Adding a new author is a txt file for the author (the name is irrelevant, but should be the author name) and respecting the format: 
1. First line: Author's name (or the suffix of the wikiquotes page, because sometimes wikipedia has ambiguate redirections if author name is used ). 
2. Second line: language  
3. Third line: empty
4. Following lines should contain one quote per line. 
